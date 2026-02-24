# AI-Powered Funding Intelligence

A simple script that takes a Grants.gov URL, gets the funding opportunity data, and saves it as both **JSON** and **CSV**.

---
## What It Does

1. Takes a Grants.gov opportunity URL
2. Calls the Grants.gov API to fetch the data
3. Maps the response to a clean schema
4. Applies rule-based tags (simple keyword matching)
5. Saves two output files: `foa.json` and `foa.csv`

Basic PDF support is added. The script downloads the PDF from the API response and extracts text using pdfminer.Currently, it only checks for simple keywords like “Title”, “Agency”, and “Deadline” as a trial test, and full structured parsing is not yet implemented. I have not attached these files in mail but they will be generated once the code is run.

---
## Files

| `main.py` 
| `requirements.txt` 
| `out/foa.json` 
| `out/foa.csv` 
| `out/pdf.json`
| `out/foa.pdf`

---
## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

> **Note:** The API key is hardcoded in `main.py` (not in a `.env` file) since these files are meant for submission.

---

## How to Run

```bash
python main.py --url "https://simpler.grants.gov/opportunity/e1f118fb-8e9d-4c86-b0c3-e9e5c5e0b59d" --out_dir ./out
```

- `--url` → the Grants.gov opportunity page URL
- `--out_dir` → folder where output files are saved (created automatically if it doesn't exist)

---

## Example URL Used

```
https://simpler.grants.gov/opportunity/e1f118fb-8e9d-4c86-b0c3-e9e5c5e0b59d
```

---

## How It Works (Simple Version)

```
URL -> extract opportunity ID -> call API -> map fields to schema -> apply tags -> save JSON + CSV
```
---
## References
```
API reference: [Grants.gov API Docs](https://api.simpler.grants.gov/docs#/Opportunity%20v1/get_v1_opportunities__opportunity_id_)
```
---


