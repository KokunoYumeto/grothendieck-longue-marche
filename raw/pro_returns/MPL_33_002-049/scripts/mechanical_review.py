#!/usr/bin/env python3
"""Report source-level consistency candidates; never edit manuscript readings."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

from extract_uncertainties import extract_file, mask_comments, write_tsv
from validate_package import validate, PREFIX, KINDS, SHEETS


def inline_code(text: str) -> str:
    runs = re.findall(r"`+", text)
    fence = "`" * (max((len(run) for run in runs), default=0) + 1)
    pad = " " if runs else ""
    return fence + pad + text + pad + fence


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    records = root / "records"
    records.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    paths = sorted((root / "pages").glob(f"{PREFIX}_33_scan[0-9][0-9][0-9].tex"))
    pages = {}
    hashes = {}
    source_commands = {}
    macro_total = Counter()
    for path in paths:
        raw = path.read_bytes()
        scan = int(re.search(r"scan(\d+)", path.name).group(1))
        pages[scan] = (path, raw.decode("utf-8"))
        hashes[path.name] = hashlib.sha256(raw).hexdigest()
        _, _, commands = extract_file(path)
        source_commands[scan] = commands
        macro_total.update(commands)
    with (root / f"{PREFIX}_inventory.csv").open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_scan = defaultdict(list)
    for row in rows:
        by_scan[int(row["scan"])].append(row)
    invalid = []
    gaps = []
    blank = []
    inventory_summary = []
    count_differences = []
    for scan in sorted(pages):
        numbers = []
        scan_rows = by_scan[scan]
        kinds = Counter(row["kind"] for row in scan_rows)
        for row in scan_rows:
            match = re.fullmatch(r"(\d+)-(\d+)", row["element"])
            if match and int(match.group(1)) == scan:
                numbers.append(int(match.group(2)))
            else:
                invalid.append((scan, row["element"], "element numbering format/prefix"))
            if row["kind"] not in KINDS or row["sheet_kind"] not in SHEETS:
                invalid.append((scan, row["element"], "kind or sheet_kind"))
            for field in ("element", "position", "first_words_or_objects", "transcribed"):
                if not row.get(field, "").strip():
                    blank.append((scan, row["element"], field))
        if numbers and sorted(numbers) != list(range(1, max(numbers) + 1)):
            gaps.append((scan, sorted(set(range(1, max(numbers) + 1)) - set(numbers))))
        inventory_summary.append({"scan": f"{scan:03}", "rows": len(scan_rows),
                                  **{kind: kinds[kind] for kind in sorted(KINDS)}})
        for command, kind in [("deleted", "deletion"), ("inserted", "insertion"),
                              ("margin", "margin note"), ("diagram", "diagram"), ("figure", "drawing")]:
            c = source_commands[scan][command]
            if c != kinds[kind]:
                count_differences.append((scan, command, c, kind, kinds[kind]))

    notation_rows = []
    patterns = {
        "Gamma notation": r"\\Gamma(?:_\{[^{}\n]*\}|_[a-zA-Z0-9])?",
        "f notation": r"f(?:_\{[^{}\n]*\}|_[a-zA-Z0-9*!]|\^\{[^{}\n]*\}|\^[a-zA-Z0-9*!])",
        "bang subscript": r"_(?:!|\{!\})",
        "bang superscript": r"\^(?:!|\{!\})",
        "double quote/prime": r"``|''|[«»“”„]",
        "R exponent": r"(?<![A-Za-z])R(?:\^\{[^{}\n]*\}|\^[a-zA-Z0-9*!])",
    }
    notation_counts = defaultdict(Counter)
    for scan, (path, text) in sorted(pages.items()):
        clean = mask_comments(text)
        for line, content in enumerate(clean.splitlines(), start=1):
            for category, pattern in patterns.items():
                for match in re.finditer(pattern, content):
                    token = match.group(0)
                    notation_counts[category][token] += 1
                    notation_rows.append({"filename": path.name, "scan": f"{scan:03}",
                                          "source_line": line, "category": category, "token": token,
                                          "source_context": content[max(0, match.start() - 65):match.end() + 85]})
    write_tsv(records / "notation_occurrences.tsv", notation_rows,
              ["filename", "scan", "source_line", "category", "token", "source_context"])
    write_tsv(records / "inventory_mechanical_summary.tsv", inventory_summary,
              ["scan", "rows", *sorted(KINDS)])
    write_tsv(records / "review_source_hashes.tsv",
              [{"filename": name, "sha256": digest} for name, digest in hashes.items()],
              ["filename", "sha256"])
    write_tsv(records / "control_word_counts.tsv",
              [{"control_word": "\\" + name, "occurrences": count} for name, count in sorted(macro_total.items())],
              ["control_word", "occurrences"])
    result = validate(root, final=False)
    (records / "mechanical_validation.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    changed = [p.name for p in paths if hashlib.sha256(p.read_bytes()).hexdigest() != hashes[p.name]]
    report = ["# Mechanical review of saved transcription", "", f"Generated: {stamp}.", "",
              "Scope: saved LaTeX and inventory only. No scan images or context files were opened. "
              "These checks cannot establish visual completeness, intended notation, or correctness of a reading.", "",
              "## Structural results", "",
              f"- Page files: {len(paths)}. Inventory rows: {len(rows)}. Inventory scans: {len(by_scan)}.",
              f"- Validator result: {'PASS' if result['ok'] else 'FAIL'} in partial mode (no final freeze assertion).",
              f"- Invalid inventory kinds or element identifiers: {len(invalid)}.",
              f"- Element-number gaps: {len(gaps)}. Blank required inventory cells: {len(blank)}.",
              "- Text rows by scan are retained in inventory_mechanical_summary.tsv. Absence of an image element "
              "cannot be detected from saved text alone.",
              f"- Source files changed while this report ran: {', '.join(changed) or 'none'}.", "",
              "## Macro counts versus inventory rows", "",
              "These are count differences for visual/inventory review. Nested deletions may be covered by one "
              "inventory entry; one figure wrapper may contain several drawings. No difference is automatically an omission.", "",
              "| Scan | Source macro | Occurrences | Inventory kind | Rows |", "|---|---|---:|---|---:|"]
    report += [f"| {scan:03} | `\\{command}` | {count} | {kind} | {nrows} |"
               for scan, command, count, kind, nrows in count_differences]
    if not count_differences:
        report.append("| — | — | — | — | — |")
    report += ["", "## Recurring notation tokens", "",
               "Counts are literal source strings. Prime pairs are included in the double-quote/prime category; "
               "its opening/closing totals are therefore not a quotation-balance test. "
               "notation_occurrences.tsv records each source location and context.", ""]
    for category in patterns:
        report.append(f"### {category}")
        report.append("")
        if notation_counts[category]:
            report.extend(f"- {inline_code(token)}: {count}." for token, count in sorted(notation_counts[category].items()))
        else:
            report.append("No matching source token.")
        report.append("")
    report += ["## Delimiter and macro scope", "",
               "extract_uncertainties.py supplies uncertainty_occurrences.tsv and latex_mechanical_findings.tsv. "
               "The checks respect escaped braces and comments, include nested uncertainty macros, and flag unmatched "
               "math delimiters or near-misses of the editorial macro names. They do not prove general TeX compilability.", "",
               "The source uses the TikZ loop control word `\\x`, locally bound by `\\foreach`. "
               "control_word_counts.tsv is tokenized to distinguish a control word from an alphabetic character "
               "after a doubled backslash line break. No source change was made.", ""]
    if invalid or gaps or blank:
        report += ["## Inventory details", "", "```json",
                   json.dumps({"invalid": invalid, "number_gaps": gaps, "blank_cells": blank}, indent=2), "```", ""]
    (records / "mechanical_review.md").write_text("\n".join(report), encoding="utf-8")
    print(json.dumps({"pages": len(paths), "inventory_rows": len(rows), "invalid_inventory_entries": len(invalid),
                      "element_number_gaps": len(gaps), "blank_inventory_cells": len(blank),
                      "macro_inventory_count_differences": count_differences,
                      "notation_occurrences": len(notation_rows), "sources_changed_during_run": changed,
                      "report": str(records / "mechanical_review.md")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
