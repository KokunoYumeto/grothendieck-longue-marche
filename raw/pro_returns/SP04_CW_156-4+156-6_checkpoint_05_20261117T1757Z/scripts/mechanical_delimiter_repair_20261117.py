#!/usr/bin/env python3
"""One explicitly authorized seven-token lexical repair; no reading decisions.

Each selected command token receives one separating space. The corresponding
authoring scripts were checked mechanically and contained no safe exact token
literal to replace; this script does not rerun or alter them.
"""
from pathlib import Path
import hashlib
import json
import re

from manage import Project, atomic_text, utcnow, PREFIX

OUT = Path(__file__).resolve().parents[1]
REPAIRS = [
    ("J156-4-01_156-4_scan003.tex", r"\equivF", r"\equiv F"),
    ("J156-4-01_156-4_scan007.tex", r"\capX", r"\cap X"),
    ("J156-4-02_156-4_scan016.tex", r"\leqF", r"\leq F"),
    ("J156-4-03_156-4_scan022.tex", r"\longmapstoL", r"\longmapsto L"),
    ("J156-4-04_156-4_scan031.tex", r"\inL", r"\in L"),
    ("J156-4-06_156-4_scan042.tex", r"\llF", r"\ll F"),
    ("J156-4-06_156-4_scan044.tex", r"\llX", r"\ll X"),
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    if (OUT / "freeze.sha256").exists():
        raise SystemExit("Refusing changes to a frozen transcription")
    planned, statuses = [], {}
    for name, old, new in REPAIRS:
        path = OUT / "pages" / name
        source = path.read_text(encoding="utf-8")
        pattern = re.compile(re.escape(old) + r"(?![A-Za-z@])")
        if len(pattern.findall(source)) != 1:
            raise SystemExit(f"Expected exactly one authorized old token in {name}; no changes applied")
        changed = pattern.sub(lambda _: new, source)
        if len(changed.encode("utf-8")) != len(source.encode("utf-8")) + 1:
            raise SystemExit("Unexpected lexical-repair size difference")
        scan = int(re.search(r"scan(\d+)\.tex$", name).group(1))
        record = OUT / "records" / f"156-4_scan{scan:03d}.json"
        statuses[str(record)] = json.loads(record.read_text(encoding="utf-8")).get("status", {})
        planned.append((path, changed, {"path": str(path), "old_token": old, "new_token": new,
                                       "replacement_count": 1, "before_sha256": sha(path)}))
    aggregate_paths = [OUT / f"{PREFIX}_{suffix}" for suffix in
                       ["transcription.tex", "changes.md", "collation.tsv", "inventory.csv", "doubts.md"]]
    before_aggregates = {str(path): sha(path) for path in aggregate_paths if path.is_file()}
    report_rows = []
    for path, changed, row in planned:
        atomic_text(path, changed)
        row["after_sha256"] = sha(path)
        report_rows.append(row)
    unchanged = all(json.loads(Path(path).read_text(encoding="utf-8")).get("status", {}) == status
                    for path, status in statuses.items())
    if not unchanged:
        raise SystemExit("Record status changed during the operation; inspect concurrent work")
    now = utcnow()
    details = "; ".join(f"{Path(row['path']).name}: {row['old_token']} -> {row['new_token']}" for row in report_rows)
    project = Project()
    project._append_log(f"mechanical TeX delimiter repairs {now} 7 pages / 7 single-space token repairs; {details}; authoring-script exact literal matches 0; record statuses unchanged")
    rendered = project.render()
    changed_aggregates = [str(path) for path in aggregate_paths if path.is_file() and before_aggregates.get(str(path)) != sha(path)]
    result = {"performed_utc": now, "page_files_changed": 7, "token_repairs": 7,
              "authoring_script_literals_changed": 0, "record_statuses_unchanged": unchanged,
              "repairs": report_rows, "aggregate_files_changed": changed_aggregates, "render": rendered}
    atomic_text(OUT / "scripts" / "mechanical_delimiter_repairs_report.json", json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
