#!/usr/bin/env python3
"""Read-only inventory reconciliation; writes reports, never the inventory/TeX.

Counts alone do not establish physical completeness: one drawing macro can hold
several drawings, and an existing inventory row can describe a grouped block.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import json
import re
import validate_package as validator

ROOT = Path(__file__).resolve().parent.parent
PREFIX = "MPL_138_090-133"
MAPPING = {"deleted": "deletion", "inserted": "insertion", "margin": "margin note", "figure": "drawing", "diagram": "diagram"}


def main():
    rows = list(csv.DictReader((ROOT / f"{PREFIX}_inventory.csv").open(newline="")))
    inv = defaultdict(Counter)
    for row in rows:
        inv[int(row["scan"])][row["kind"]] += 1
    occurrences = defaultdict(lambda: defaultdict(list))
    hashes = {}
    for path in sorted((ROOT / "pages").glob(f"{PREFIX}_138_scan[0-9][0-9][0-9].tex")):
        scan = int(re.search(r"scan(\d+)", path.name).group(1))
        raw = path.read_text()
        clean = validator.uncomment(raw)
        hashes[scan] = hashlib.sha256(path.read_bytes()).hexdigest()
        for match in re.finditer(r"\\(deleted|inserted|margin|figure|diagram)(?![A-Za-z])\s*", clean):
            if validator.escaped(clean, match.start()):
                continue
            macro = match.group(1)
            start = match.end()
            while start < len(clean) and clean[start].isspace():
                start += 1
            body, end = validator.argument_at(clean, start)
            if body is None:
                raise ValueError(f"Unclosed {macro} argument in scan {scan}.")
            exact = raw[start + 1:end - 1] if clean[start] == "{" else raw[start:end]
            occurrences[scan][macro].append({"line": validator.line_at(raw, match.start()), "body": exact})
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    columns = ["scan"]
    for macro, kind in MAPPING.items():
        columns += [f"{macro}_macros", f"{kind.replace(' ', '_')}_rows"]
    columns += ["source_tex_sha256"]
    table, deficits = [], []
    for scan in sorted(hashes):
        row = {"scan": scan, "source_tex_sha256": hashes[scan]}
        for macro, kind in MAPPING.items():
            count = len(occurrences[scan][macro])
            row[f"{macro}_macros"] = count
            row[f"{kind.replace(' ', '_')}_rows"] = inv[scan][kind]
            if count > inv[scan][kind]:
                deficits.append({"scan": scan, "macro": macro, "kind": kind, "macros": count, "rows": inv[scan][kind], "difference": count - inv[scan][kind]})
        table.append(row)
    reconciliation = ROOT / "records/apparatus_inventory_reconciliation.json"
    if reconciliation.exists():
        grouping = json.loads(reconciliation.read_text()).get("intentional_grouping", {})
        expected_difference = len(grouping.get("deleted_macro_ordinals", [])) - grouping.get("physical_element_count", 0)
        for item in deficits:
            if item["scan"] == grouping.get("scan") and item["macro"] == "deleted" and item["difference"] == expected_difference:
                item["explained_by_documented_group"] = True
                item["explanation"] = grouping.get("reason", "")
    with (ROOT / "records/apparatus_inventory_counts.tsv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter="\t")
        writer.writeheader()
        writer.writerows(table)
    locator_findings = []
    locator_count = 0
    for row in rows:
        match = re.search(r"TeX line (\d+); apparatus locator expansion: \\(deleted|inserted|margin|figure|diagram) occurrence (\d+)", row["position"])
        if not match:
            match = re.search(r"TeX line (\d+); \\(deleted|inserted|margin|figure|diagram) occurrence (\d+); apparatus locator reconciliation", row["position"])
        if not match:
            continue
        locator_count += 1
        line, macro, ordinal = int(match.group(1)), match.group(2), int(match.group(3))
        scan = int(row["scan"])
        candidates = occurrences[scan][macro]
        current = candidates[ordinal - 1] if ordinal <= len(candidates) else None
        if current is None or current["body"] != row["first_words_or_objects"]:
            locator_findings.append({"element": row["element"], "scan": scan, "macro": macro, "occurrence": ordinal, "status": "body_or_occurrence_changed", "recorded_line": line, "current_line": current["line"] if current else None, "current_equal_body_occurrences": [i + 1 for i, item in enumerate(candidates) if item["body"] == row["first_words_or_objects"]]})
        elif line != current["line"]:
            locator_findings.append({"element": row["element"], "scan": scan, "macro": macro, "occurrence": ordinal, "status": "line_number_changed_body_matches", "recorded_line": line, "current_line": current["line"]})
    stale_cancel = [row["element"] for row in rows if re.search(r"\\cancel(?=\{)", row["first_words_or_objects"])]
    text = f"# Apparatus and inventory count review\n\nSnapshot: {now}\n\n"
    text += ("This report reads generated TeX and the inventory only. It does not read scans or context, "
             "modify the inventory, or establish visual completeness. A count difference is a review signal, "
             "not a proven omission: a figure macro can contain several drawings, and inventory rows may group elements.\n\n")
    text += "## Counts by page\n\nEach pair is **macro occurrences / inventory rows of the corresponding kind**.\n\n"
    text += "| Scan | deleted / deletion | inserted / insertion | margin / margin note | figure / drawing | diagram / diagram |\n|---|---:|---:|---:|---:|---:|\n"
    for scan in sorted(hashes):
        text += f"| {scan} | " + " | ".join(f"{len(occurrences[scan][macro])} / {inv[scan][kind]}" for macro, kind in MAPPING.items()) + " |\n"
    text += "\n## Remaining positive count differences\n\nThese require primary-reader review; no matching or inventory rows were guessed.\n\n"
    text += "| Scan | Macro | Inventory kind | Macros | Rows | Difference |\n|---|---|---|---:|---:|---:|\n"
    for item in deficits:
        text += f"| {item['scan']} | `{item['macro']}` | {item['kind']} | {item['macros']} | {item['rows']} | {item['difference']} |\n"
    for item in deficits:
        if item.get("explained_by_documented_group"):
            text += f"\nScan {item['scan']}'s difference is explained by the primary reader's documented grouping: {item['explanation']} It is not an unresolved inventory gap.\n"
    text += f"\n## Exact apparatus locator rows\n\nChecked {locator_count} recorded apparatus locator rows against the current macro ordinal, exact body, and TeX line. Found {len(locator_findings)} changes needing reconciliation.\n\n"
    text += "```json\n" + json.dumps(locator_findings, ensure_ascii=False, indent=2) + "\n```\n"
    text += f"\nInventory captions still containing `\\cancel{{`: {stale_cancel}.\n"
    text += ("\n## Authorized expansion already performed\n\n"
             "The primary agent authorized additions only for page/kind combinations that had zero existing rows. "
             "That pass added 34 locator rows, preserving the original rows and continuing their element IDs. "
             "Each new row contains the exact macro body and a position explicitly identified as an apparatus locator expansion. "
             "The separately authorized caption correction in element 127.10 changed cancel to deleted. "
             "See `apparatus_locator_expansion.json` for the event and source hashes. "
             "Rerun this script after the visual audit to detect locator drift; it never repairs or changes those rows automatically.\n")
    if reconciliation.exists():
        rec = json.loads(reconciliation.read_text())
        text += f"\nThe subsequent explicitly authorized inventory reconciliation added {rec['added_rows']} rows through additions and splits, taking the inventory from {rec['before_rows']} to {rec['after_rows']} rows. Its pre-change copy, per-ID actions, and source hashes are recorded in `apparatus_inventory_reconciliation.json`. The locator check above includes those reconciled rows as well as the initial expansion.\n"
    (ROOT / "records/apparatus_inventory_review.md").write_text(text)
    summary = {"time": now, "pages": len(hashes), "inventory_rows": len(rows), "positive_count_differences": deficits, "locator_rows_checked": locator_count, "locator_findings": locator_findings, "stale_cancel_captions": stale_cancel}
    (ROOT / "records/apparatus_inventory_review.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
