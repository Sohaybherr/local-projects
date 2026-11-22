
import json
from playwright.sync_api import sync_playwright

URL = (
    "https://betting.sjmtech.ma/api/vrol-api/vrol/"
    "archivio/getArchivioGareEventiSingoli/"
    "1/1/5/09-11-2026"
)

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    print("Opening Cote & Sport...")

    page.goto(
        "https://www.coteetsport.ma/cote-sport-3d/archives-du-concours",
        wait_until="domcontentloaded",
        timeout=60000
    )

    print("Website opened.")
    print("Requesting archive through browser...")

    result = page.evaluate(
        """async (url) => {
            const response = await fetch(url);

            return {
                status: response.status,
                body: await response.json()
            };
        }""",
        URL
    )

    print("HTTP status:", result["status"])

    if result["status"] == 200:
        with open(
            "archive_test.json",
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                result["body"],
                f,
                ensure_ascii=False,
                indent=2
            )

        print("SUCCESS: archive_test.json saved.")

    browser.close()
