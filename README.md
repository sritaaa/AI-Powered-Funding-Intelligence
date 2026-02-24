# AI-Powered Funding Intelligence

A simple script that takes a Grants.gov URL, extracts the funding opportunity data, and saves it in a structured format both **JSON** and **CSV**.

## What It Does

1. Takes a Grants.gov opportunity URL
2. Calls the Grants.gov API to get the data
3. Maps the response to a schema
4. Applies rule-based tags (simple keyword matching)
5. Saves two output files: `foa.json` and `foa.csv`


## Files

| `main.py` 
| `requirements.txt` 
| `out/foa.json` 
| `out/foa.csv` 
|  `README.md`


## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```


## How to Run

```bash
python main.py --url "https://simpler.grants.gov/opportunity/e1f118fb-8e9d-4c86-b0c3-e9e5c5e0b59d" --out_dir ./out
```

- `--url` → the Grants.gov opportunity page URL
- `--out_dir` → folder where output files are saved (created automatically if it doesn't exist)


## Example URL Used

```
https://simpler.grants.gov/opportunity/e1f118fb-8e9d-4c86-b0c3-e9e5c5e0b59d
```

## How It Works 

```
URL -> extract opportunity ID -> call API -> map fields to schema -> apply tags -> save JSON + CSV
```

## Note
API key for Grants.gov is hardcoded rather than stored in an env file.

## References
```
API reference: [Grants.gov API Docs](https://api.simpler.grants.gov/docs#/Opportunity%20v1/get_v1_opportunities__opportunity_id_)
```



