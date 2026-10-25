#!/usr/bin/env python3

import csv
import sys
from pathlib import Path


def clean_csv(input_file: Path, output_file: Path) -> tuple[int, int]:
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    if input_file.resolve() == output_file.resolve():
        raise ValueError("Input and output files must be different.")

    with input_file.open("r", newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        if not reader.fieldnames:
            raise ValueError("The input CSV must have a header row.")

        fieldnames = [name.strip() if name else "" for name in reader.fieldnames]
        if any(not name for name in fieldnames):
            raise ValueError("Every column must have a non-empty header.")
        if len(set(fieldnames)) != len(fieldnames):
            raise ValueError("Column names must be unique after trimming whitespace.")

        cleaned_rows = []
        seen = set()
        input_count = 0

        for original_row in reader:
            input_count += 1
            row = {}
            for original_key, value in original_row.items():
                if original_key is None:
                    continue
                key = original_key.strip()
                row[key] = value.strip() if isinstance(value, str) else value

            # Preserve the declared column order and remove exact duplicate rows.
            normalized = {name: row.get(name, "") for name in fieldnames}
            fingerprint = tuple(normalized[name] for name in fieldnames)
            if fingerprint not in seen:
                seen.add(fingerprint)
                cleaned_rows.append(normalized)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", newline="", encoding="utf-8") as destination:
        writer = csv.DictWriter(destination, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    return input_count, len(cleaned_rows)


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python3 clean_csv.py INPUT.csv OUTPUT.csv", file=sys.stderr)
        return 2

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])
    try:
        before, after = clean_csv(input_file, output_file)
    except (OSError, csv.Error, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Done. Rows read: {before}; rows written after duplicate removal: {after}.")
    print(f"Output: {output_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
