#!/usr/bin/env python3
"""Apply the primary reader's explicit apparatus reconciliation once; no TeX edits."""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
import csv
import fcntl
import hashlib
import io
import json
import re
import validate_package as v

ROOT = Path(__file__).resolve().parent.parent
PREFIX = "MPL_138_090-133"
MAPPING = {"deleted": "deletion", "inserted": "insertion", "margin": "margin note", "figure": "drawing", "diagram": "diagram"}
SPLITS = {
    "093.13": ("deleted", [2, 9]), "100.10": ("deleted", [5, 6]),
    "123.15": ("deleted", [3, 4, 5, 6, 7, 8]), "123.14": ("inserted", [1, 2, 3, 4, 5, 6]),
    "124.02": ("deleted", [1, 2]), "125.10": ("deleted", [6, 7]),
    "125.16": ("deleted", [10, 11]), "126.02": ("inserted", [1, 2]),
    "132.14": ("deleted", [5, 6]), "132.20": ("deleted", [8, 9]),
    "132.22": ("deleted", [10, 11]), "132.25": ("deleted", [12, 13]),
}
# anchor, before/after, macro, ordinal, optional kind, optional grouping note
ADDITIONS = [
    ("093.01", "before", "diagram", 1, None, None),
    ("093.14", "after", "diagram", 2, "deletion", "one cancelled diagram element containing deleted occurrences 3–8"),
    ("096.06", "after", "deleted", 1, None, None),
    ("100.15", "after", "deleted", 10, None, None),
    ("104.29", "after", "deleted", 9, None, None),
    ("111.07", "after", "deleted", 3, None, None),
    *[("111.08", "after", "deleted", n, None, None) for n in (4, 5, 6, 7)],
    ("112.03", "after", "deleted", 1, None, None),
    ("112.05", "after", "figure", 2, None, None),
    *[("112.08", "after", "deleted", n, None, None) for n in (3, 4, 5)],
    ("118.26", "after", "deleted", 2, None, None),
    ("119.51", "after", "margin", 1, None, None),
    ("119.61", "after", "margin", 2, None, None),
    ("119.61", "after", "deleted", 2, None, None),
    ("120.15", "after", "margin", 1, None, None),
    ("120.27", "after", "margin", 2, None, None),
    ("122.03", "after", "inserted", 1, None, None),
    ("122.04", "after", "deleted", 3, None, None),
    ("122.04", "after", "inserted", 2, None, None),
    ("122.26", "after", "inserted", 6, None, None),
    ("125.03", "after", "inserted", 1, None, None),
    ("132.27", "after", "margin", 2, None, None),
]


def main():
    backup = ROOT / "records/inventory_before_apparatus_reconciliation.csv"
    audit = ROOT / "records/apparatus_inventory_reconciliation.json"
    if backup.exists() or audit.exists():
        raise SystemExit("This one-time reconciliation already has a backup or audit record; refusing to duplicate it.")
    macros = defaultdict(lambda: defaultdict(list))
    source_hashes = {}
    for path in sorted((ROOT / "pages").glob(f"{PREFIX}_138_scan[0-9][0-9][0-9].tex")):
        scan = int(re.search(r"scan(\d+)", path.name).group(1))
        raw = path.read_text()
        clean = v.uncomment(raw)
        source_hashes[scan] = hashlib.sha256(path.read_bytes()).hexdigest()
        for match in re.finditer(r"\\(deleted|inserted|margin|figure|diagram)(?![A-Za-z])\s*", clean):
            if v.escaped(clean, match.start()):
                continue
            start = match.end()
            while start < len(clean) and clean[start].isspace():
                start += 1
            body, end = v.argument_at(clean, start)
            if body is None:
                raise ValueError((scan, match.group(1)))
            exact = raw[start + 1:end - 1] if clean[start] == "{" else raw[start:end]
            macros[scan][match.group(1)].append({"body": exact, "line": v.line_at(raw, match.start())})
    path = ROOT / f"{PREFIX}_inventory.csv"
    events = []
    with path.open("r+", newline="") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        original = f.read()
        reader = csv.DictReader(io.StringIO(original))
        fields, rows = reader.fieldnames, list(reader)
        by_id = {r["element"]: r for r in rows}
        assert len(by_id) == len(rows)
        expected_ids = set(SPLITS) | {x[0] for x in ADDITIONS}
        if not expected_ids <= set(by_id):
            raise ValueError(f"Missing anchors: {expected_ids - set(by_id)}")
        maximum = defaultdict(int)
        for row in rows:
            maximum[int(row["scan"])] = max(maximum[int(row["scan"])], int(row["element"].split(".")[1]))

        def make(base, macro, ordinal, retain_id=False, kind=None, grouping=None):
            scan = int(base["scan"])
            occurrence = macros[scan][macro][ordinal - 1]
            new = dict(base)
            if not retain_id:
                maximum[scan] += 1
                new["element"] = f"{scan:03d}.{maximum[scan]:02d}"
            new["kind"] = kind or MAPPING[macro]
            new["position"] = base["position"] + f"; TeX line {occurrence['line']}; \\{macro} occurrence {ordinal}; apparatus locator reconciliation"
            if grouping:
                new["position"] += "; " + grouping
            new["first_words_or_objects"] = occurrence["body"]
            new["transcribed"] = "yes"
            return new

        additions = defaultdict(lambda: defaultdict(list))
        for anchor, relation, macro, ordinal, kind, grouping in ADDITIONS:
            additions[anchor][relation].append((macro, ordinal, kind, grouping))
        output_rows = []
        for row in rows:
            element = row["element"]
            for macro, ordinal, kind, grouping in additions[element]["before"]:
                new = make(row, macro, ordinal, kind=kind, grouping=grouping)
                output_rows.append(new)
                events.append({"action": "add", "anchor": element, "relation": "before", "macro": macro, "ordinal": ordinal, "row": new})
            if element in SPLITS:
                macro, ordinals = SPLITS[element]
                split_rows = [make(row, macro, ordinal, retain_id=(i == 0)) for i, ordinal in enumerate(ordinals)]
                output_rows.extend(split_rows)
                events.append({"action": "split", "original": row, "macro": macro, "ordinals": ordinals, "rows": split_rows})
            else:
                output_rows.append(row)
            for macro, ordinal, kind, grouping in additions[element]["after"]:
                new = make(row, macro, ordinal, kind=kind, grouping=grouping)
                output_rows.append(new)
                events.append({"action": "add", "anchor": element, "relation": "after", "macro": macro, "ordinal": ordinal, "row": new})
        result_ids = {r["element"] for r in output_rows}
        assert len(result_ids) == len(output_rows)
        assert set(by_id) <= result_ids
        result_by_id = {r["element"]: r for r in output_rows}
        for element, row in by_id.items():
            if element not in SPLITS:
                assert result_by_id[element] == row, element
            else:
                for field in fields:
                    if field not in {"position", "first_words_or_objects"}:
                        assert result_by_id[element][field] == row[field], (element, field)
        for source, digest in source_hashes.items():
            source_path = ROOT / "pages" / f"{PREFIX}_138_scan{source:03d}.tex"
            if hashlib.sha256(source_path.read_bytes()).hexdigest() != digest:
                raise RuntimeError(f"Source scan {source} changed during reconciliation; inventory was not written.")
        buffer = io.StringIO(newline="")
        writer = csv.DictWriter(buffer, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output_rows)
        output = buffer.getvalue()
        backup.write_bytes(original.encode("utf-8"))
        f.seek(0)
        f.write(output)
        f.truncate()
        f.flush()
        fcntl.flock(f, fcntl.LOCK_UN)
    record = {"time": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"), "authority": "Explicit primary-reader reconciliation instructions after the visual audit; every added/split source element was already transcribed and audited by that reader. No new visual or mathematical check was performed by the mechanical support agent.", "before_rows": len(rows), "after_rows": len(output_rows), "added_rows": len(output_rows) - len(rows), "prechange_copy": backup.name, "before_sha256": hashlib.sha256(original.encode()).hexdigest(), "after_sha256": hashlib.sha256(output.encode()).hexdigest(), "source_hashes": source_hashes, "events": events, "intentional_grouping": {"scan": 93, "source": "diagram occurrence 2", "deleted_macro_ordinals": [3, 4, 5, 6, 7, 8], "physical_element_count": 1, "reason": "Primary reader identified a single crossed diagram, whose individual objects/labels retain separate deleted macros."}}
    audit.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: record[k] for k in ["time", "before_rows", "after_rows", "added_rows", "prechange_copy"]}, indent=2))


if __name__ == "__main__":
    main()
