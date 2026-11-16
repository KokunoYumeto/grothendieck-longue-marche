#!/usr/bin/env python3
"""Read-only lexical macro and inventory checks, without reading inference.

Usage: python scripts/check_inventory_macros.py PACKAGE_DIRECTORY OUTPUT_DIRECTORY

Macro/row counts need not be equal when an inventory row intentionally groups
elements. Differences are inspection prompts, not automatic omission findings.
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from validate_package import KINDS, SHEET_KINDS, sanitize_tex
from extract_doubts import closing_brace

EDITORIAL = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())
MAPPING = {"deleted": "deletion", "inserted": "insertion", "margin": "margin note", "diagram": "diagram", "figure": "drawing"}
SPECIAL_NESTING = {("deleted", "deleted"), ("uuline", "uline"), ("unsure", "diagram")}
FLAGS = set("caption captionof includegraphics input include documentclass usepackage newcommand renewcommand def newenvironment".split())


def scan_commands(raw: str):
    clean = sanitize_tex(raw)
    counts = collections.Counter()
    spans = []
    i = 0
    while i < len(clean):
        if clean[i] != "\\":
            i += 1
            continue
        start = i
        i += 1
        if i < len(clean) and clean[i].isascii() and clean[i].isalpha():
            j = i
            while j < len(clean) and clean[j].isascii() and clean[j].isalpha():
                j += 1
            name = clean[i:j]
            counts[name] += 1
            i = j
            if name in EDITORIAL:
                opening = j
                while opening < len(clean) and clean[opening].isspace():
                    opening += 1
                if opening < len(clean) and clean[opening] == "{":
                    closing = closing_brace(clean, opening, len(clean))
                    if closing is not None:
                        spans.append((start, closing, name, raw.count("\n", 0, start) + 1))
        else:
            # Consume a control symbol (including both characters of \\).
            i += 1
    return counts, spans


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("directory", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    inventory_path = args.directory / "MPL_136_047-094_inventory.csv"
    with inventory_path.open(encoding="utf-8", newline="") as handle:
        inventory_rows = list(csv.DictReader(handle))
    inventory = collections.Counter((int(row["scan"]), row["kind"]) for row in inventory_rows)
    kinds = collections.Counter(row["kind"] for row in inventory_rows)
    sheet_kinds = collections.Counter(row["sheet_kind"] for row in inventory_rows)
    invalid = [(number, row["kind"], row["sheet_kind"], row["transcribed"])
               for number, row in enumerate(inventory_rows, 2)
               if row["kind"] not in KINDS or row["sheet_kind"] not in SHEET_KINDS or row["transcribed"] != "yes"]
    commands = collections.Counter()
    nested = collections.Counter()
    nesting_locations = []
    differences = []
    hashes = []
    for path in sorted((args.directory / "pages").glob("MPL_136_047-094_136_scan*.tex")):
        data = path.read_bytes()
        raw = data.decode("utf-8")
        scan = int(re.search(r"scan(\d+)\.tex$", path.name).group(1))
        counts, spans = scan_commands(raw)
        commands.update(counts)
        hashes.append(f"{hashlib.sha256(data).hexdigest()}  pages/{path.name}\n")
        for macro, kind in MAPPING.items():
            if counts[macro] != inventory[scan, kind]:
                differences.append([scan, macro, counts[macro], kind, inventory[scan, kind], counts[macro] - inventory[scan, kind]])
        for start, end, name, line in spans:
            parents = [span for span in spans if span[0] < start and span[1] >= end]
            if parents:
                parent = max(parents, key=lambda span: span[0])
                pair = (parent[2], name)
                nested[pair] += 1
                if pair in SPECIAL_NESTING:
                    nesting_locations.append([scan, parent[2], parent[3], name, line])
    with (args.output / "inventory_macro_counts.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["scan", "macro", "macro_count", "inventory_kind", "inventory_count", "difference"])
        writer.writerows(differences)
    with (args.output / "nested_macro_locations.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["scan", "outer_macro", "outer_line", "inner_macro", "inner_line"])
        writer.writerows(nesting_locations)
    hashes.append(f"{hashlib.sha256(inventory_path.read_bytes()).hexdigest()}  {inventory_path.name}\n")
    (args.output / "sources.sha256").write_text("".join(hashes), encoding="utf-8")
    lines = [f"Inventory rows: {len(inventory_rows)}", f"Invalid inventory label/status rows: {invalid}",
             "Inventory kinds: " + repr(dict(kinds)), "Inventory sheet kinds: " + repr(dict(sheet_kinds)),
             "Editorial macro counts: " + repr({name: commands[name] for name in sorted(EDITORIAL)}),
             "Other control words: " + " ".join(sorted(set(commands) - EDITORIAL)),
             "Flagged commands: " + repr({name: commands[name] for name in sorted(FLAGS) if commands[name]}),
             "Direct nested editorial pairs: " + repr(dict(sorted(nested.items()))),
             "Special nesting locations: " + repr(nesting_locations),
             "Macro/inventory count differences (not automatic omissions):"]
    lines.extend(" | ".join(map(str, row)) for row in differences)
    report = "\n".join(lines) + "\n"
    (args.output / "macro_inventory_check.txt").write_text(report, encoding="utf-8")
    print(report)
    return 1 if invalid else 0


if __name__ == "__main__":
    raise SystemExit(main())
