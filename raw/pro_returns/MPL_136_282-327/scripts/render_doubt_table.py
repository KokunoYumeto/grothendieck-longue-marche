#!/usr/bin/env python3
"""Join explicit doubt occurrences and reading records into a reviewable table.

The script never infers readings, alternatives, confidence, or approximate-line
equivalence. A reading record joins an inline occurrence only when cote, scan,
and complete raw argument exactly equal its recorded reading, and that key is
unique in both inputs. Every other record is retained as a separate row.
Unrecorded fields stay explicitly unrecorded. Nested macros are preserved.

Output is restricted to records/, never the root doubts.md file. The exact
occurrences remain in inline_doubts.csv; the Markdown display HTML-escapes code
and literal pipes so neither nested TeX nor a pipe can split a table cell.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
from collections import Counter
from pathlib import Path


PACKAGE = "MPL_136_282-327"


def code_cell(value: object) -> str:
    if value is None or value == "":
        return "—"
    text = str(value)
    # Use an entity rather than a backslash escape inside a code span: a TeX
    # literal \| must preserve its own backslash while keeping the pipe inert.
    escaped = html.escape(text, quote=False).replace("|", "&#124;")
    escaped = escaped.replace("\r\n", "\n").replace("\r", "\n")
    return "<code>" + escaped.replace("\n", "</code><br><code>") + "</code>"


def key(row: dict, inline: bool) -> tuple[str, str, str]:
    return (str(row["cote"]), str(row["scan"]),
            row["raw_argument"] if inline else row["reading"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path,
                        help="default: records/doubts_table_draft.md; must stay inside records/")
    args = parser.parse_args()
    root = args.root.resolve()
    records = root / "records"
    output = (args.output or records / "doubts_table_draft.md").resolve()
    if not output.is_relative_to(records.resolve()) or output.suffix.lower() != ".md":
        raise SystemExit("Output must be a Markdown file inside records/; doubts.md will not be touched")
    with (records / "inline_doubts.csv").open(encoding="utf-8", newline="") as stream:
        inline = list(csv.DictReader(stream))
    reading = []
    for line_number, line in enumerate((root / "reading_doubts.jsonl").read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        required = {"cote", "scan", "line", "reading", "alternatives", "confidence"}
        if not isinstance(row, dict) or not required <= row.keys():
            raise SystemExit(f"Unexpected reading_doubts.jsonl schema at physical line {line_number}")
        row = dict(row)
        row["record_id"] = f"reading_doubts.jsonl:{line_number}"
        reading.append(row)
    inline_keys = Counter(key(row, True) for row in inline)
    reading_keys = Counter(key(row, False) for row in reading)
    unique_readings = {key(row, False): row for row in reading
                       if reading_keys[key(row, False)] == 1
                       and inline_keys[key(row, False)] == 1}
    matched_ids = set()
    display = []
    for row in inline:
        note = unique_readings.get(key(row, True))
        if note:
            matched_ids.add(note["record_id"])
        location = "physical .tex line " + row["line_start"]
        if row["line_end"] != row["line_start"]:
            location += "–" + row["line_end"]
        if note:
            location += "; recorded position: " + note["line"]
        provenance = row["occurrence_id"]
        if row["enclosing_doubt_id"]:
            provenance += "; nested in " + row["enclosing_doubt_id"]
        if note:
            provenance += "; " + note["record_id"]
        display.append({
            "sort": (int(row["scan"]), 0, int(row["line_start"]), int(row["start_offset"])),
            "values": [row["cote"], row["scan"], location, row["raw_occurrence"],
                       note["reading"] if note else "not separately recorded",
                       note["alternatives"] if note else "not separately recorded",
                       note["confidence"] if note else "not individually recorded",
                       provenance],
        })
    unjoined = [row for row in reading if row["record_id"] not in matched_ids]
    for index, row in enumerate(unjoined):
        display.append({
            "sort": (int(row["scan"]), 1, index, 0),
            "values": [row["cote"], row["scan"], row["line"], "",
                       row["reading"], row["alternatives"], row["confidence"], row["record_id"]],
        })
    lines = [
        "# Mechanically consolidated doubt records — review draft",
        "",
        "This derived table preserves every explicit inline doubt and every reading record. "
        "Only unique exact matches on cote, scan, and the complete raw argument were joined. "
        "No confidence, alternative, reading, or location was inferred. Entries without an "
        "individual confidence remain marked as such for the principal reader to assess.",
        "",
        f"Inline occurrences: {len(inline)}. Reading records: {len(reading)}. "
        f"Exact joins: {len(matched_ids)}. Separate reading-record rows: {len(unjoined)}. "
        f"Total displayed rows: {len(display)}.",
        "",
        "Physical line numbers identify the saved .tex files; verbal positions are retained "
        "from reading_doubts.jsonl. Source hashes and exact original text remain in inline_doubts.csv. "
        "Pipes are HTML-escaped in this display, including those inside TeX macro arguments.",
        "",
        "| File | Scan | Line / recorded position | Exact inline occurrence | Recorded reading | Recorded alternatives | Recorded confidence | Record IDs |",
        "|---|---:|---|---|---|---|---|---|",
    ]
    for row in sorted(display, key=lambda row: row["sort"]):
        lines.append("| " + " | ".join(code_cell(value) for value in row["values"]) + " |")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(display)} rows: {output}")
    print(f"Inline: {len(inline)}; reading records: {len(reading)}; exact joins: {len(matched_ids)}; unjoined notes: {len(unjoined)}")
    print("Root doubts.md was not modified. Unrecorded confidence values were not assigned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
