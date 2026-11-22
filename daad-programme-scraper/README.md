# DAAD Degree Programme Scraper

A Python scraper that collects degree-programme information from DAAD and exports JSON and CSV files.

## Usage

Requirements: Python 3 and internet access.

```sh
python -m pip install -r requirements.txt
python daadscraping.py
```

Edit `SEARCH_PARAMS` in the script to change the search filters. Results are written to `daad_programmes.json` and `daad_programmes.csv`; generated exports are excluded. The script includes request delays, but has not been run against the live service during repository preparation. Changes to the source website may require parser updates.
