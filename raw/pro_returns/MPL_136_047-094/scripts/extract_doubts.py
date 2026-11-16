#!/usr/bin/env python3
"""Mechanically extract uncertainty macros without interpreting manuscript text.

Usage: python scripts/extract_doubts.py PACKAGE_DIRECTORY OUTPUT.tsv

Each page is read once; source_sha256 identifies that exact revision. Nested
macros are separate records linked to their parent and descendants. Contents
remain verbatim. top_level_bar_parts is a JSON-encoded list split solely on
unescaped bars outside brace groups; it does not assert that a bar semantically
denotes an alternative. No confidence, expansion, or reading is inferred.
The only output written is the requested TSV and an adjacent SHA-256 manifest.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from validate_package import escaped, sanitize_tex

MACRO = re.compile(r"\\(unsure|illegible)(?![A-Za-z])")
SCAN = re.compile(r"_scan(\d{3})\.tex$")
FIELDS = ["file", "scan", "tex_line", "macro", "record_id", "parent_id",
          "content", "top_level_bar_parts", "nested_doubts", "context", "source_sha256"]


def closing_brace(clean: str, opening: int, limit: int) -> int | None:
    depth = 0
    for index in range(opening, limit):
        char = clean[index]
        if char not in "{}" or escaped(clean, index):
            continue
        depth += 1 if char == "{" else -1
        if depth == 0:
            return index
    return None


def split_bars(raw: str, clean: str) -> list[str]:
    depth = 0
    starts = [0]
    ends = []
    for index, char in enumerate(clean):
        if escaped(clean, index):
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
        elif char == "|" and depth == 0:
            ends.append(index)
            starts.append(index + 1)
    ends.append(len(raw))
    return [raw[start:end] for start, end in zip(starts, ends)]


def short_context(raw: str, start: int, end: int) -> str:
    left = " ".join(raw[max(0, start - 90):start].split())
    middle = " ".join(raw[start:end].split())
    right = " ".join(raw[end:min(len(raw), end + 90)].split())
    if len(middle) > 140:
        middle = middle[:68] + " … " + middle[-68:]
    return f"{left} ⟦{middle}⟧ {right}".strip()


def extract(raw: str, filename: str, scan: str, digest: str) -> tuple[list[dict], list[str]]:
    clean = sanitize_tex(raw)
    records: list[dict] = []
    errors: list[str] = []

    def region(start: int, limit: int, parent: str = "") -> list[str]:
        descendants: list[str] = []
        cursor = start
        while cursor < limit:
            match = MACRO.search(clean, cursor, limit)
            if match is None:
                break
            cursor = match.end()
            if escaped(clean, match.start()):
                continue
            opening = match.end()
            while opening < limit and clean[opening].isspace():
                opening += 1
            line = raw.count("\n", 0, match.start()) + 1
            if opening >= limit or clean[opening] != "{":
                errors.append(f"{filename}:{line}: {match.group(0)} has no braced argument")
                continue
            closing = closing_brace(clean, opening, limit)
            if closing is None:
                errors.append(f"{filename}:{line}: {match.group(0)} has an unclosed argument")
                # Continue after the opening so nested occurrences still appear.
                cursor = opening + 1
                continue
            record_id = f"{scan}:{len(records) + 1}"
            content = raw[opening + 1:closing]
            record = {
                "file": filename, "scan": scan, "tex_line": line,
                "macro": match.group(1), "record_id": record_id, "parent_id": parent,
                "content": content,
                "top_level_bar_parts": json.dumps(split_bars(content, clean[opening + 1:closing]), ensure_ascii=False),
                "nested_doubts": "", "context": short_context(raw, match.start(), closing + 1),
                "source_sha256": digest,
            }
            records.append(record)
            nested = region(opening + 1, closing, record_id)
            record["nested_doubts"] = json.dumps(nested, ensure_ascii=False)
            descendants.extend([record_id, *nested])
            cursor = closing + 1
        return descendants

    region(0, len(raw))
    return records, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("directory", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    files = sorted((args.directory / "pages").glob("MPL_136_047-094_136_scan*.tex"))
    all_records: list[dict] = []
    all_errors: list[str] = []
    manifest: list[str] = []
    for path in files:
        data = path.read_bytes()
        raw = data.decode("utf-8")
        digest = hashlib.sha256(data).hexdigest()
        filename = "pages/" + path.name
        scan_match = SCAN.search(path.name)
        assert scan_match is not None
        records, errors = extract(raw, filename, scan_match.group(1), digest)
        all_records.extend(records)
        all_errors.extend(errors)
        manifest.append(f"{digest}  {filename}\n")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(all_records)
    args.output.with_suffix(".sources.sha256").write_text("".join(manifest), encoding="utf-8")
    counts = {name: sum(record["macro"] == name for record in all_records) for name in ("unsure", "illegible")}
    nested_count = sum(bool(record["parent_id"]) for record in all_records)
    print(f"Read {len(files)} page files; extracted {counts}; {nested_count} nested occurrences.")
    print(f"Wrote {args.output}")
    for error in all_errors:
        print(error, file=sys.stderr)
    print(f"Extraction syntax errors: {len(all_errors)}")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
