# DAAD Degree Programme Scraper

## Overview

A Python scraper that collects degree-programme information from DAAD and exports JSON and CSV files.

## Academic Objectives

Implement a structured collection pipeline for degree-programme information from a web source.

## Methodology and Implementation

The script issues filtered HTTP requests, parses HTML using BeautifulSoup, follows programme links, normalizes extracted text, and exports records to CSV and JSON. Request delays regulate collection frequency.

## Source Organization

- `daadscraping.py`: request configuration, parsing, and export functions.
- `requirements.txt`: direct Python dependencies.

## Environment and Execution

Requirements: Python 3 and internet access.

```sh
python -m pip install -r requirements.txt
python daadscraping.py
```

Edit `SEARCH_PARAMS` in the script to change the search filters. Results are written to `daad_programmes.json` and `daad_programmes.csv`; generated exports are excluded. The script includes request delays, but has not been run against the live service as part of the documented validation. Changes to the source website may require parser updates.

## Evaluation and Limitations

This directory presents an educational implementation. Compilation or syntax checks establish only the properties recorded in the repository [validation report](../VALIDATION.md); they do not establish functional correctness, completeness, performance, or deployment readiness. Dependencies, external services, datasets, and hardware requirements should be considered when interpreting results. No quantitative evaluation is claimed unless explicitly supplied in the source.
