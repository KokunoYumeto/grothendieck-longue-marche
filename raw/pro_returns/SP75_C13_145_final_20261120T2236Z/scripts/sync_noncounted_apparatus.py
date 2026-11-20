"""Preflight, then optionally apply the separately reviewed noncounted-row plan.

Prepared but not executed by reader B. Default operation is read-only preflight.
--apply-reviewed-plan stages only the four targets named in the JSON plan. It
does not run build_edition.py, verify_edition.py, or a TeX compiler. Root controls
the subsequent rebuild, verification, receipt and progress-log entry.
"""

from __future__ import annotations

import argparse
import ast
import collections
import copy
import csv
import hashlib
import json
import os
from pathlib import Path
import tempfile


EDITION = Path(__file__).resolve().parents[1]
PLAN = Path(__file__).with_name("sync_noncounted_apparatus_plan.json")
TARGETS = {
    "reader_reports/145_scan022_reviewed.json",
    "reader_reports/145_scan023_reviewed.json",
    "scripts/build_edition.py",
    "scripts/verify_edition.py",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def get(document, path):
    for key in path:
        document = document[key]
    return document


def noncounted(reports):
    return [
        {"scan": report["scan"], "id": row["id"]}
        for report in reports for row in report["changes"]
        if not row["c_changed"] and not row["h_changed"]
    ]


def counts(reports, substantive_only):
    records = [row for report in reports for row in report["changes"]]
    selected = [row for row in records if row["c_changed"] or row["h_changed"]] if substantive_only else records
    categories = collections.Counter()
    for row in selected:
        values = row.get("error_category", [])
        values = [values] if isinstance(values, int) else values
        categories.update(int(value) for value in set(values))
    return {
        "published_records": len(records),
        "substantive_loci": len(selected),
        "against_C": sum(row["c_changed"] for row in selected),
        "against_H": sum(row["h_changed"] for row in selected),
        "confidence": dict(collections.Counter(row["confidence"] for row in selected)),
        "feedback_categories": dict(categories),
        "audit_changed_boxes": sum(
            sum(row["changed"] for row in report.get("audit", {}).get("differences", []))
            for report in reports
        ),
    }


def preflight():
    plan = json.loads(PLAN.read_text())
    require(plan["schema"] == "cote145-noncounted-sync-v1", "Unknown plan schema")
    require(set(plan["targets"]) == TARGETS, "Target scope differs from reviewed plan")
    for name, expected in plan["protected_review_sha256"].items():
        require(sha(EDITION / name) == expected, f"Existing review changed: {name}")
    for name, expected in plan["protected_page_sha256"].items():
        require(sha(EDITION / name) == expected, f"Accepted page changed: {name}")
    original = {}
    staged_values = {}
    for name in TARGETS:
        path = EDITION / name
        require(path.resolve() == path, f"Target must not be a symlink: {name}")
        require(sha(path) == plan["target_sha256"][name], f"Target changed after plan preparation: {name}")
        original[name] = path.read_bytes()
        staged_values[name] = json.loads(original[name]) if name.endswith(".json") else original[name].decode()

    reports = [json.loads(path.read_text()) for path in sorted((EDITION / "reader_reports").glob("*_reviewed.json"))]
    for report in reports:
        for row in report["changes"]:
            require(type(row["c_changed"]) is bool and type(row["h_changed"]) is bool, f"Non-Boolean flags: {row['id']}")
    require(noncounted(reports) == plan["existing_row_census"]["both_false"], "New both-false rows require explicit scope review")

    ids = set()
    for operation in plan["operations"]:
        require(operation["id"] not in ids, "Duplicate operation ID")
        ids.add(operation["id"])
        name = operation["file"]
        require(name in TARGETS, f"Unexpected target: {name}")
        if operation["type"] == "json_field":
            document = staged_values[name]
            anchor = operation.get("anchor")
            if anchor:
                require(get(document, anchor["path"]) == anchor["value"], f"Record anchor moved: {operation['id']}")
            require(get(document, operation["path"]) == operation["old"], f"Old field value changed: {operation['id']}")
            parent = get(document, operation["path"][:-1])
            parent[operation["path"][-1]] = copy.deepcopy(operation["new"])
        elif operation["type"] == "text_replace":
            source = staged_values[name]
            require(source.count(operation["old"]) == operation["expected_occurrences"] == 1, f"Exact code anchor changed: {operation['id']}")
            staged_values[name] = source.replace(operation["old"], operation["new"])
        else:
            raise RuntimeError(f"Unknown operation type: {operation['type']}")

    for name in TARGETS:
        if name.endswith(".py"):
            ast.parse(staged_values[name], filename=name)
        else:
            old = json.loads(original[name])
            new = staged_values[name]
            for key in ("audit", "second_boxes", "decisions", "doubts", "check_events"):
                require(old.get(key) == new.get(key), f"Protected report field changed: {name}/{key}")
            if name.endswith("022_reviewed.json"):
                old_row = next(row for row in old["changes"] if row["id"] == "s022-26")
                new_row = next(row for row in new["changes"] if row["id"] == "s022-26")
                omit = {"c_changed", "h_changed"}
                require({k: v for k, v in old_row.items() if k not in omit} == {k: v for k, v in new_row.items() if k not in omit}, "Noncounted observation lost or changed evidence")

    after_reports = [staged_values.get(f"reader_reports/145_scan{report['scan']:03d}_reviewed.json", report) for report in reports]
    require(noncounted(after_reports) == plan["expected_new_noncounted"], "Unexpected affected rows")
    before, after = counts(reports, False), counts(after_reports, True)
    for key in ("substantive_loci", "against_C", "against_H"):
        require(before[key] - after[key] == 1, f"Unexpected count effect: {key}")
    for key in ("published_records", "audit_changed_boxes"):
        require(before[key] == after[key], f"Preserved count changed: {key}")
    for key in ("high", "medium", "low"):
        require(before["confidence"].get(key, 0) - after["confidence"].get(key, 0) == (key == "low"), f"Unexpected confidence effect: {key}")
    for key in range(1, 11):
        require(before["feedback_categories"].get(key, 0) - after["feedback_categories"].get(key, 0) == (key in {1, 10}), f"Unexpected feedback effect: {key}")

    seal = EDITION / "second/FIRST_READINGS_SHA256.tsv"
    with seal.open(newline="") as stream:
        sealed = list(csv.DictReader(stream, delimiter="\t"))
    require(len(sealed) == 24, "Incomplete first-reading seal")
    for row in sealed:
        require(sha(seal.parent / row["file"]) == row["sha256"], f"First-reading seal mismatch: {row['file']}")
    protected = {seal, *EDITION.glob("pages/*.tex"), *EDITION.glob("reader_reports/final_consistency_review_b*.md")}
    for pattern in ("*_first.tsv", "*_second.tsv", "*_boxes.tsv", "*_reading_receipt.json", "*_comparison.tsv", "*_adjudication.json"):
        protected.update((EDITION / "second").glob(pattern))
    protected_hashes = {path: sha(path) for path in protected}
    return plan, original, staged_values, protected_hashes, before, after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply-reviewed-plan", action="store_true")
    args = parser.parse_args()
    plan, original, values, protected, before, after = preflight()
    result = {"status": "PREFLIGHT_ONLY", "plan_sha256": sha(PLAN), "operations": len(plan["operations"]), "targets": sorted(TARGETS), "counts_before": before, "counts_after": after, "other_affected_rows": [], "builder_or_verifier_executed": False}
    if not args.apply_reviewed_plan:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    staged = {}
    try:
        for name in sorted(TARGETS):
            target = EDITION / name
            require(target.read_bytes() == original[name], f"Concurrent target edit: {name}")
            value = values[name]
            payload = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode() if isinstance(value, dict) else value.encode()
            with tempfile.NamedTemporaryFile(dir=target.parent, prefix=target.name + ".sync-", delete=False) as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
                staged[name] = Path(stream.name)
            staged[name].chmod(target.stat().st_mode & 0o777)
        for name in TARGETS:
            require((EDITION / name).read_bytes() == original[name], f"Concurrent target edit: {name}")
        for path, expected in protected.items():
            require(sha(path) == expected, f"Protected evidence changed during preflight: {path.name}")
        for name in sorted(TARGETS):
            os.replace(staged[name], EDITION / name)
        for path, expected in protected.items():
            require(sha(path) == expected, f"Protected evidence changed: {path.name}")
    finally:
        for path in staged.values():
            if path.exists():
                path.unlink()
    result["status"] = "APPLIED_REVIEWED_PLAN"
    result["next_step"] = "Root may inspect the four diffs, rebuild and verify, then record the receipt and progress entry."
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
