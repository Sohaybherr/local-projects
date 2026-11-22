# Cote Sport Archive Scraper

## Overview

A Playwright-based Python utility for collecting archived sports events, odds, and results into local CSV output.

## Academic Objectives

Investigate browser-assisted retrieval and structured representation of archived sports-event data.

## Methodology and Implementation

Playwright establishes a browser session for archive requests. Retrieved event structures are transformed into tabular records, appended to CSV output, and accompanied by progress state for subsequent execution.

## Source Organization

- `script.py`: archive retrieval and command-line interface.
- `test.py`: supplementary exploratory script.
- `requirements.txt`: browser automation dependency.

## Environment and Execution

Requirements: Python 3, Playwright Chromium, and internet access.

```sh
python -m pip install -r requirements.txt
python -m playwright install chromium
python script.py --help
python script.py --start 01-11-2026 --end 02-11-2026 --headless
```

Dates use `DD-MM-YYYY`. Output and resume state are written under `cote_sport_data/` and excluded from Git. `test.py` is an additional local experiment, not an automated test suite. Live scraping was not performed as part of the documented validation; external endpoints and response formats may change.

## Evaluation and Limitations

This directory presents an educational implementation. Compilation or syntax checks establish only the properties recorded in the repository [validation report](../VALIDATION.md); they do not establish functional correctness, completeness, performance, or deployment readiness. Dependencies, external services, datasets, and hardware requirements should be considered when interpreting results. No quantitative evaluation is claimed unless explicitly supplied in the source.
