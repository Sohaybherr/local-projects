import csv
import json
import re
import time
from urllib.parse import urljoin, urlencode

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.daad.de"

SEARCH_URL = (
    "https://www.daad.de/en/studying-in-germany/"
    "universities/all-degree-programmes/"
)

# نفس filters ديال الرابط ديالك
SEARCH_PARAMS = {
    "hec-degreeProgrammeType": "w",
    "hec-subjectGroup": "2-547",
    
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/153.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

REQUEST_DELAY = 1.0
TIMEOUT = 30


session = requests.Session()
session.headers.update(HEADERS)


def clean_text(value):
    """Clean whitespace."""
    if not value:
        return None

    value = re.sub(r"\s+", " ", value).strip()
    return value or None


def get_soup(url, params=None):
    """
    Download a webpage and return BeautifulSoup object.
    """
    print(f"[GET] {url}")

    response = session.get(
        url,
        params=params,
        timeout=TIMEOUT,
    )

    response.raise_for_status()

    time.sleep(REQUEST_DELAY)

    return BeautifulSoup(response.text, "lxml")


def absolute_url(url):
    if not url:
        return None

    return urljoin(BASE_URL, url)


# --------------------------------------------------
# SEARCH RESULTS
# --------------------------------------------------

def find_programme_links(soup):
    """
    Extract DAAD programme detail links from a search result page.

    Detail URLs normally contain:
    /all-degree-programmes/detail/
    """

    programmes = {}

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if "/all-degree-programmes/detail/" not in href:
            continue

        full_url = absolute_url(href)

        # Get DAAD ID from URL, e.g. w76982
        match = re.search(r"hec-id=(w\d+)", full_url)

        if not match:
            match = re.search(r"-w(\d+)/", full_url)

            if match:
                programme_id = "w" + match.group(1)
            else:
                programme_id = full_url
        else:
            programme_id = match.group(1)

        programmes[programme_id] = full_url

    return programmes


def discover_all_programmes():
    """
    Go through DAAD result pages and collect unique programme links.
    """

    all_programmes = {}

    offset = 0
    page_size = 20

    while True:

        params = SEARCH_PARAMS.copy()

        if offset:
            params["hec-offset"] = offset

        soup = get_soup(
            SEARCH_URL,
            params=params,
        )

        # Check total number of programmes
        page_text = soup.get_text(" ", strip=True)

        total_match = re.search(
            r"(\d+)\s+study programmes found",
            page_text,
            re.I,
        )

        total = int(total_match.group(1)) if total_match else None

        links = find_programme_links(soup)

        before = len(all_programmes)

        all_programmes.update(links)

        added = len(all_programmes) - before

        print(
            f"Page offset={offset}: "
            f"{added} new programmes "
            f"(total collected={len(all_programmes)})"
        )

        if total:
            print(f"Expected programmes: {total}")

            if len(all_programmes) >= total:
                break

        # Nothing new = stop
        if added == 0:
            break

        offset += page_size

    return all_programmes


# --------------------------------------------------
# GENERIC DETAIL HELPERS
# --------------------------------------------------

def extract_heading_value(soup, heading_text):
    """
    Find:

        ### Heading
        value

    Works for many DAAD detail-page sections.
    """

    heading = soup.find(
        lambda tag:
        tag.name in ["h2", "h3", "h4"]
        and clean_text(tag.get_text()) == heading_text
    )

    if not heading:
        return None

    values = []

    for sibling in heading.next_siblings:

        if getattr(sibling, "name", None) in [
            "h2",
            "h3",
            "h4",
        ]:
            break

        if hasattr(sibling, "get_text"):
            text = clean_text(
                sibling.get_text(" ", strip=True)
            )

            if text:
                values.append(text)

    return clean_text(" ".join(values))


def extract_section_items(soup, heading_text):
    """
    Extract text under a heading until the next heading.
    Useful for areas of study etc.
    """

    heading = soup.find(
        lambda tag:
        tag.name in ["h2", "h3", "h4"]
        and clean_text(tag.get_text()) == heading_text
    )

    if not heading:
        return []

    items = []

    for sibling in heading.next_siblings:

        if getattr(sibling, "name", None) in [
            "h2",
            "h3",
            "h4",
        ]:
            break

        if hasattr(sibling, "find_all"):

            li_elements = sibling.find_all("li")

            for li in li_elements:
                text = clean_text(li.get_text())

                if text:
                    items.append(text)

    # Remove duplicates
    return list(dict.fromkeys(items))


def find_external_links(soup):
    """
    Collect useful external website links.
    """

    links = []

    for a in soup.find_all("a", href=True):

        href = absolute_url(a["href"])

        text = clean_text(
            a.get_text(" ", strip=True)
        )

        if not href:
            continue

        if "daad.de" in href:
            continue

        links.append({
            "label": text,
            "url": href,
        })

    return links


# --------------------------------------------------
# DEADLINES
# --------------------------------------------------

def parse_deadlines(soup):
    """
    Parse application deadlines from the programme detail page.

    Output example:

    {
        "Winter semester (2025/2026)": {
            "Application deadline for Germans and inhabitants":
                "15.05.2026 - 30.09.2026"
        }
    }
    """

    deadlines = {}

    application_heading = soup.find(
        lambda tag:
        tag.name == "h2"
        and "Application deadlines"
        in clean_text(tag.get_text())
    )

    if not application_heading:
        return deadlines

    current_semester = None
    current_label = None

    for element in application_heading.find_all_next():

        # Stop at next H2
        if (
            element.name == "h2"
            and element is not application_heading
        ):
            break

        text = clean_text(
            element.get_text(" ", strip=True)
        )

        if not text:
            continue

        if element.name == "h3":

            current_semester = text

            deadlines.setdefault(
                current_semester,
                {}
            )

            current_label = None

        elif element.name == "h4":

            current_label = text

        elif current_semester and current_label:

            # Only direct-ish textual elements
            if element.name in [
                "p",
                "div",
                "span",
                "li",
            ]:

                if (
                    text != current_label
                    and text != current_semester
                ):

                    # Don't overwrite once found
                    if current_label not in deadlines[
                        current_semester
                    ]:

                        deadlines[
                            current_semester
                        ][current_label] = text

    return deadlines


# --------------------------------------------------
# MAIN PROGRAMME PARSER
# --------------------------------------------------

def parse_programme(url):
    """
    Scrape one DAAD programme detail page.
    """

    soup = get_soup(url)

    data = {
        "daad_url": url,
    }

    # -----------------------
    # Programme name
    # -----------------------

    h1 = soup.find("h1")

    programme_name = (
        clean_text(h1.get_text(" ", strip=True))
        if h1
        else None
    )

    data["programme_name"] = programme_name

    # -----------------------
    # DAAD ID
    # -----------------------

    match = re.search(
        r"hec-id=(w\d+)",
        url,
    )

    if not match:
        match = re.search(
            r"-w(\d+)/",
            url,
        )

        daad_id = (
            "w" + match.group(1)
            if match
            else None
        )

    else:
        daad_id = match.group(1)

    data["daad_id"] = daad_id

    # -----------------------
    # Main overview
    # -----------------------

    data["study_type"] = extract_heading_value(
        soup,
        "Study Type",
    )

    data["admission_semester"] = (
        extract_heading_value(
            soup,
            "Admission semester",
        )
    )

    data["focus"] = extract_heading_value(
        soup,
        "Focus",
    )

    data["admission_mode"] = (
        extract_heading_value(
            soup,
            "Admission modus",
        )
    )

    data["area_of_study"] = (
        extract_section_items(
            soup,
            "Area of study",
        )
    )

    # -----------------------
    # Main language
    # -----------------------

    data["main_language"] = (
        extract_heading_value(
            soup,
            "Main language",
        )
    )

    # -----------------------
    # Tuition
    # -----------------------

    data["tuition_fees"] = (
        extract_heading_value(
            soup,
            "Tuition fees",
        )
    )

    # -----------------------
    # Deadlines
    # -----------------------

    data["deadlines"] = parse_deadlines(
        soup
    )

    # -----------------------
    # External URLs
    # -----------------------

    data["external_links"] = (
        find_external_links(
            soup
        )
    )

    # -----------------------
    # Extract top summary
    # -----------------------

    page_text = soup.get_text(
        "\n",
        strip=True,
    )

    degree_match = re.search(
        r"Degree\s*\n(.+)",
        page_text,
    )

    if degree_match:
        data["degree"] = clean_text(
            degree_match.group(1)
        )

    period_match = re.search(
        r"Standard period of study "
        r"\(amount\)\s*\n(.+)",
        page_text,
        re.I,
    )

    if period_match:
        data["standard_period"] = (
            clean_text(
                period_match.group(1)
            )
        )

    location_match = re.search(
        r"Location\s*\n(.+)",
        page_text,
    )

    if location_match:
        data["location"] = clean_text(
            location_match.group(1)
        )

    # -----------------------
    # University name
    # -----------------------

    title = soup.title.get_text(
        " ",
        strip=True,
    ) if soup.title else ""

    # Example:
    # Study "Computational..." (Master)
    # in Germany - KIT - DAAD

    if " - DAAD" in title:

        title_without_daad = title.replace(
            " - DAAD",
            "",
        )

        parts = title_without_daad.split(
            " - "
        )

        if len(parts) >= 2:
            data["university"] = (
                parts[-1].strip()
            )

    return data


# --------------------------------------------------
# CSV FLATTENING
# --------------------------------------------------

def flatten_for_csv(programme):
    """
    JSON can store nested objects.
    CSV cannot, so convert lists/dicts into JSON strings.
    """

    row = {}

    for key, value in programme.items():

        if isinstance(
            value,
            (dict, list),
        ):

            row[key] = json.dumps(
                value,
                ensure_ascii=False,
            )

        else:
            row[key] = value

    return row


# --------------------------------------------------
# SAVE FUNCTIONS
# --------------------------------------------------

def save_json(programmes, filename):
    with open(
        filename,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            programmes,
            f,
            indent=2,
            ensure_ascii=False,
        )

    print(
        f"[OK] JSON saved: {filename}"
    )


def save_csv(programmes, filename):

    if not programmes:
        return

    rows = [
        flatten_for_csv(p)
        for p in programmes
    ]

    fieldnames = sorted({
        key
        for row in rows
        for key in row.keys()
    })

    with open(
        filename,
        "w",
        encoding="utf-8-sig",
        newline="",
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(rows)

    print(
        f"[OK] CSV saved: {filename}"
    )


# --------------------------------------------------
# EXECUTION
# --------------------------------------------------

def main():

    print("=" * 60)
    print("DAAD PROGRAMME SCRAPER")
    print("=" * 60)

    programme_links = (
        discover_all_programmes()
    )

    print()
    print(
        f"Found {len(programme_links)} "
        f"unique programmes."
    )

    programmes = []

    total = len(programme_links)

    for index, (
        programme_id,
        url,
    ) in enumerate(
        programme_links.items(),
        start=1,
    ):

        print()
        print(
            f"[{index}/{total}] "
            f"Scraping {programme_id}"
        )

        try:

            programme = parse_programme(
                url
            )

            programmes.append(
                programme
            )

            print(
                "    ->",
                programme.get(
                    "programme_name"
                ),
            )

        except Exception as e:

            print(
                f"[ERROR] {url}"
            )

            print(
                f"        {e}"
            )

    # -----------------------
    # Save results
    # -----------------------

    save_json(
        programmes,
        "daad_programmes.json",
    )

    save_csv(
        programmes,
        "daad_programmes.csv",
    )

    print()
    print("=" * 60)

    print(
        f"Finished: "
        f"{len(programmes)}/{total} "
        f"programmes scraped."
    )

    print("=" * 60)


if __name__ == "__main__":
    main()