# Cote Sport Archive Scraper

A Playwright-based Python utility for collecting archived sports events, odds, and results into local CSV output.

## Usage

Requirements: Python 3, Playwright Chromium, and internet access.

```sh
python -m pip install -r requirements.txt
python -m playwright install chromium
python script.py --help
python script.py --start 01-11-2026 --end 02-11-2026 --headless
```

Dates use `DD-MM-YYYY`. Output and resume state are written under `cote_sport_data/` and excluded from Git. `test.py` is an additional local experiment, not an automated test suite. Live scraping was not performed during preparation; external endpoints and response formats may change.
