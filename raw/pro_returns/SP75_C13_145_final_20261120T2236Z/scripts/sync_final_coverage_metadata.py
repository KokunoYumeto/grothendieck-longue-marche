"""Preflight seven reviewed metadata updates; apply only with the explicit flag.

This script is prepared, not executed, by reader B. It never rebuilds the edition
or changes a page, historical reading, audit, seal, review, or mathematical note.
"""

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile

E = Path(__file__).resolve().parents[1]
P = Path(__file__).with_name("sync_final_coverage_metadata_plan.json")
TARGETS = {f"reader_reports/145_scan{n:03d}_reviewed.json" for n in (25, 26)}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def value(document, path):
    for key in path:
        document = document[key]
    return document


def totals(report):
    rows = [row for row in report["changes"] if row["c_changed"] or row["h_changed"]]
    return {"records": len(report["changes"]), "substantive_loci": len(rows),
            "C": sum(row["c_changed"] for row in rows), "H": sum(row["h_changed"] for row in rows),
            "audit_changed_boxes": sum(row["changed"] for row in report["audit"]["differences"])}


def preflight():
    plan = json.loads(P.read_text())
    require(plan["schema"] == "cote145-final-coverage-metadata-v1", "Unknown plan schema")
    require(set(plan["targets"]) == TARGETS and len(plan["operations"]) == 7, "Unexpected plan scope")
    for name, expected in plan["source_reviews_sha256"].items():
        require(sha(E / name) == expected, f"Source review changed: {name}")
    original = {name: (E / name).read_bytes() for name in TARGETS}
    before = {name: json.loads(data) for name, data in original.items()}
    seen = set()
    for op in plan["operations"]:
        name, path = op["file"], op["path"]
        require(name in TARGETS, f"Unexpected target: {name}")
        require((E / name).resolve() == E / name, f"Target must not be a symlink: {name}")
        permitted = ((path[0] == "diff_coverage" and path[-1] == "explanation") or
                     (name.endswith("026_reviewed.json") and path[0] == "changes" and path[-1] == "place") or
                     (name.endswith("026_reviewed.json") and path[:2] == ["abbreviations", 2] and
                      path[-1] in {"form", "expansion", "place"}))
        require(permitted, f"Non-metadata field requested: {op['id']}")
        require((name, tuple(path)) not in seen, "Duplicate field operation")
        seen.add((name, tuple(path)))
        require(value(before[name], op["anchor"]["path"]) == op["anchor"]["value"], f"Record anchor moved: {op['id']}")
        require(value(before[name], path) == op["old"], f"Exact old value changed: {op['id']}")
    after = copy.deepcopy(before)
    for op in plan["operations"]:
        parent = value(after[op["file"]], op["path"][:-1])
        parent[op["path"][-1]] = copy.deepcopy(op["new"])
    for name in TARGETS:
        old, new = before[name], after[name]
        for field in ("audit", "second_boxes", "decisions", "unlisted_decisions", "doubts", "inventory",
                      "notation", "hand", "notes", "check_events"):
            require(old.get(field) == new.get(field), f"Protected report field changed: {name}/{field}")
        require(totals(old) == totals(new), f"Counts changed: {name}")
        require(len(old["changes"]) == len(new["changes"]), "Changed record count")
        for left, right in zip(old["changes"], new["changes"]):
            require({k: v for k, v in left.items() if k != "place"} ==
                    {k: v for k, v in right.items() if k != "place"}, "Reading, confidence, category or witness flag changed")
        for left, right in zip(old["diff_coverage"], new["diff_coverage"]):
            require({k: v for k, v in left.items() if k != "explanation"} ==
                    {k: v for k, v in right.items() if k != "explanation"}, "Coverage status or reference changed")
    protected = set(E.glob("pages/*.tex")) | set(E.glob("reader_reports/final_consistency_review*.md"))
    protected.add(E / "second/FIRST_READINGS_SHA256.tsv")
    for pattern in ("*_first.tsv", "*_second.tsv", "*_boxes.tsv", "*_reading_receipt.json", "*_comparison.tsv", "*_adjudication.json"):
        protected.update((E / "second").glob(pattern))
    hashes = {path: sha(path) for path in protected}
    return original, after, hashes, {name: totals(report) for name, report in before.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply-reviewed-plan", action="store_true")
    args = parser.parse_args()
    original, after, protected, counts = preflight()
    result = {"status": "PREFLIGHT_ONLY", "plan_sha256": sha(P), "operations": 7,
              "targets": sorted(TARGETS), "counts_unchanged": counts, "builder_executed": False}
    if not args.apply_reviewed_plan:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    staged = {}
    try:
        for name in sorted(TARGETS):
            target = E / name
            require(target.read_bytes() == original[name], f"Concurrent target edit: {name}")
            with tempfile.NamedTemporaryFile(dir=target.parent, prefix=target.name + ".sync-", delete=False) as stream:
                stream.write((json.dumps(after[name], ensure_ascii=False, indent=2) + "\n").encode())
                stream.flush()
                os.fsync(stream.fileno())
                staged[name] = Path(stream.name)
            staged[name].chmod(target.stat().st_mode & 0o777)
        for name in TARGETS:
            require((E / name).read_bytes() == original[name], f"Concurrent target edit: {name}")
        for path, expected in protected.items():
            require(sha(path) == expected, f"Protected file changed during preflight: {path.name}")
        for name in sorted(TARGETS):
            os.replace(staged[name], E / name)
        for path, expected in protected.items():
            require(sha(path) == expected, f"Protected file changed: {path.name}")
    finally:
        for path in staged.values():
            if path.exists():
                path.unlink()
    result["status"] = "APPLIED_REVIEWED_PLAN"
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
