# CSV Cleanup Script — Portfolio Demo

## What it demonstrates

- Reads a CSV file using Python's standard library (no third-party packages).
- Trims whitespace from column names and cell values.
- Removes exact duplicate rows.
- Writes a cleaned CSV and reports row counts.
- Checks for common input errors instead of silently failing.

## Run it on macOS

1. Open Terminal and change into this folder (or open this folder in VS Code and use its terminal).
2. Check Python: `python3 --version`
3. Run: `python3 clean_csv.py sample_input.csv cleaned_output.csv`
4. Open `cleaned_output.csv` to inspect the result.

Expected message: `Done. Rows read: 4; rows written after duplicate removal: 3.`

## Important scope note

This is a sample portfolio project using synthetic data, not a claim of paid client work. For a real project, first agree on the exact cleaning rules, encoding, delimiters, row count, expected output, and whether the client needs a reusable script or just a cleaned file. Never include client-confidential data in a public portfolio.
