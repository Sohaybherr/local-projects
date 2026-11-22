
import csv
import json
import time
import random
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright, Error as PlaywrightError

# ==========================================
# CONFIGURATION
# ==========================================

BASE_URL = (
    "https://betting.sjmtech.ma/api/vrol-api/vrol/"
    "archivio/getArchivioGareEventiSingoli"
)

# These three parameters come from your browser request.
# Their exact meanings have not yet been confirmed.
API_PARAMETERS = "1/1/5"

OUTPUT_DIR = Path("cote_sport_data")
OUTPUT_DIR.mkdir(exist_ok=True)

ARCHIVE_PAGE = "https://www.coteetsport.ma/cote-sport-3d/archives-du-concours"
REQUEST_TIMEOUT_MS = 90000

CSV_FIELDS = [
    "date",
    "time",
    "calendar_code",
    "event_code",
    "match",
    "sport",
    "final_score",
    "market",
    "selection",
    "odds",
    "market_result",
    "is_winner",
    "factory_id",
]


# ==========================================
# SESSION
# ==========================================

class BrowserSession:
    def __init__(self, headless=False):
        self.playwright = sync_playwright().start()
        self.browser = None
        try:
            self.browser = self.playwright.chromium.launch(headless=headless)
            self.page = self.browser.new_page()
            self.page.goto(ARCHIVE_PAGE, wait_until="domcontentloaded", timeout=60000)
        except BaseException:
            self.close()
            raise

    def close(self):
        try:
            if self.browser is not None:
                self.browser.close()
        finally:
            self.playwright.stop()


def create_session(headless=False):
    return BrowserSession(headless=headless)


# ==========================================
# DATE GENERATOR
# ==========================================

def generate_dates(start_date, end_date):
    start = datetime.strptime(start_date, "%d-%m-%Y")
    end = datetime.strptime(end_date, "%d-%m-%Y")

    if start > end:
        raise ValueError("Start date must be before end date.")

    current = start

    while current <= end:
        yield current.strftime("%d-%m-%Y")
        current += timedelta(days=1)


# ==========================================
# FETCH ARCHIVE
# ==========================================

def fetch_archive(session, date):
    url = f"{BASE_URL}/{API_PARAMETERS}/{date}"
    print(f"\nFetching {date}")
    for attempt in range(3):
        try:
            result = session.page.evaluate(
                """async ({url, timeout}) => {
                    const controller = new AbortController();
                    const timer = setTimeout(() => controller.abort(), timeout);
                    try {
                        const response = await fetch(url, {signal: controller.signal});
                        return {status: response.status, body: await response.text()};
                    } finally {
                        clearTimeout(timer);
                    }
                }""",
                {"url": url, "timeout": REQUEST_TIMEOUT_MS},
            )
            status = result["status"]
            print("HTTP status:", status)
            if 200 <= status < 300:
                try:
                    data = json.loads(result["body"])
                    extract_matches(data)
                    return data
                except (ValueError, TypeError) as error:
                    print(f"Invalid archive response for {date}: {error}")
                    return None
            if status not in (429, 500, 502, 503, 504):
                print(f"HTTP error {status}: {date}")
                return None
        except PlaywrightError as error:
            print(f"Browser request failed for {date}: {error}")
            if session.page.is_closed():
                return None
        if attempt < 2:
            delay = 2 ** (attempt + 1)
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)
    return None


# ==========================================
# EXTRACT MATCH LIST
# ==========================================

def extract_matches(data):
    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        # Handle common API response wrappers.
        for key in [
            "data",
            "results",
            "result",
            "items",
            "content",
            "archivio",
        ]:
            value = data.get(key)

            if isinstance(value, list):
                return value

    raise ValueError(
        "Unknown JSON structure. "
        "Inspect the saved raw JSON response."
    )


# ==========================================
# ODDS CONVERSION
# ==========================================

def convert_odds(value):
    if value is None:
        return None

    try:
        values = [int(part.strip()) / 100 for part in str(value).split(",")]
        return values[0] if len(values) == 1 else ",".join(str(item) for item in values)
    except (ValueError, TypeError):
        return None


# ==========================================
# EXTRACT DATA
# ==========================================

def parse_matches(matches, date):
    rows = []

    for match in matches:
        if not isinstance(match, dict):
            continue

        base = {
            "date": date,
            "time": match.get("dataOra"),
            "calendar_code": match.get("codicePalinsesto"),
            "event_code": match.get("codiceAvvenimento"),
            "match": match.get("descrizioneAvventimento") or match.get("descrizioneAvvenimento"),
            "sport": match.get("descrizioneDisciplina"),
            "final_score": match.get("risultato"),
        }

        markets = match.get(
            "risultatoScommessaUfficialeList", []
        ) or []

        if not markets:
            rows.append({
                **base,
                "market": None,
                "selection": None,
                "odds": None,
                "market_result": None,
                "is_winner": None,
                "factory_id": None,
            })
            continue

        for market in markets:
            if not isinstance(market, dict):
                continue

            rows.append({
                **base,
                "market": market.get(
                    "descrizioneScommessa"
                ),
                "selection": market.get(
                    "descrizioneEsito"
                ),
                "odds": convert_odds(
                    market.get("quoteComb")
                ),
                "market_result": market.get(
                    "risultato"
                ),
                "is_winner": None,
                "factory_id": market.get(
                    "factoryId"
                ),
            })

    return rows


# ==========================================
# SAVE FILES
# ==========================================

def save_json(data, date):
    path = OUTPUT_DIR / f"archive_{date}.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


def append_csv(rows):
    if not rows:
        return

    path = OUTPUT_DIR / "all_matches.csv"

    # Replace rows for these dates so retrying after an interrupted run is safe.
    dates = {row["date"] for row in rows}
    previous = []
    if path.exists() and path.stat().st_size:
        with path.open(newline="", encoding="utf-8-sig") as f:
            previous = [row for row in csv.DictReader(f) if row["date"] not in dates]
    temporary = path.with_suffix(".csv.tmp")
    with temporary.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(previous)
        writer.writerows(rows)
    temporary.replace(path)


# ==========================================
# DUPLICATE PREVENTION
# ==========================================

def load_processed_dates():
    path = OUTPUT_DIR / "processed_dates.json"

    if not path.exists():
        return set()

    try:
        with open(path, encoding="utf-8") as f:
            return set(json.load(f))
    except (ValueError, OSError):
        return set()


def save_processed_dates(dates):
    path = OUTPUT_DIR / "processed_dates.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            sorted(dates),
            f,
            indent=2
        )


# ==========================================
# MAIN SCRAPER
# ==========================================

def scrape(start_date, end_date, headless=False):
    dates = list(generate_dates(start_date, end_date))
    session = create_session(headless=headless)

    processed = load_processed_dates()

    total_matches = 0
    total_rows = 0

    print("=" * 50)
    print("COTE & SPORT 3D ARCHIVE SCRAPER")
    print("=" * 50)
    print("Start date:", start_date)
    print("End date:", end_date)
    print("Total dates:", len(dates))

    try:
        for index, date in enumerate(dates, start=1):
            print(f"\n[{index}/{len(dates)}] {date}")

            if date in processed:
                print("Already processed. Skipping.")
                continue

            data = fetch_archive(session, date)

            if data is None:
                print("Failed. Will retry on next run.")
                continue

            save_json(data, date)

            try:
                matches = extract_matches(data)
            except ValueError as error:
                print(error)
                continue

            rows = parse_matches(matches, date)

            append_csv(rows)

            processed.add(date)
            save_processed_dates(processed)

            total_matches += len(matches)
            total_rows += len(rows)

            print("Matches:", len(matches))
            print("Records:", len(rows))

            # Avoid excessive requests.
            if index < len(dates):
                time.sleep(random.uniform(2, 4))

    except KeyboardInterrupt:
        print("\nScraping interrupted.")

    finally:
        session.close()

    print("\n" + "=" * 50)
    print("SCRAPING SUMMARY")
    print("=" * 50)
    print("New matches:", total_matches)
    print("New records:", total_rows)
    print("Output directory:", OUTPUT_DIR.resolve())


# ==========================================
# ENTRY POINT
# ==========================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--start",
        default="09-11-2026",
        help="Start date DD-MM-YYYY"
    )

    parser.add_argument(
        "--end",
        default="09-11-2026",
        help="End date DD-MM-YYYY"
    )

    parser.add_argument("--headless", action="store_true", help="Run Chromium without a visible window")

    args = parser.parse_args()

    try:
        scrape(args.start, args.end, headless=args.headless)
    except (ValueError, OSError, PlaywrightError) as error:
        parser.exit(1, f"Error: {error}\n")
