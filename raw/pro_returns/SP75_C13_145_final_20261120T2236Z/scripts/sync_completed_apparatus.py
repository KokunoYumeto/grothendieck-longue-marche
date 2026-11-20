"""Apply a separately reviewed, exact apparatus-only plan for completed pages.

Prepared by reader B; not executed by its preparer. The accompanying JSON lists
every old/new value and its already-adjudicated evidence. No image reading or
source-text revision occurs here. Running without --apply-reviewed-plan performs
preflight only. The explicit apply flag is for root after reviewing the plan.

This script does not rebuild the edition, change the plan, or write a log into
the sealed evidence. Root may rebuild derived apparatus and log the application
after checking the resulting reviewed reports.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import os
from pathlib import Path
import tempfile


EDITION = Path(__file__).resolve().parents[1]
PLAN = Path(__file__).with_name("sync_completed_apparatus_plan.json")
SCANS = (3, *range(5, 19))
REPORT_NAMES = {
    f"reader_reports/145_scan{scan:03d}_reviewed.json" for scan in SCANS
}
ALLOWED_FILES = REPORT_NAMES | {"H_doubt_metadata_review.json"}
REPORT_FIELDS = {
    "unlisted_decisions", "changes", "notation", "abbreviations",
    "inventory", "notes", "diff_coverage", "layout",
}
METADATA_FIELDS = {
    "scope_or_editorial_correction_no", "inspected_H_notes_scans",
    "scope_evidence",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def value_at(document, path):
    for key in path:
        document = document[key]
    return document


def has_value(document, path) -> bool:
    parent = value_at(document, path[:-1])
    key = path[-1]
    if isinstance(parent, list):
        return isinstance(key, int) and not isinstance(key, bool) and 0 <= key < len(parent)
    return isinstance(parent, dict) and key in parent


def preserved_report_fields(before: dict, after: dict, name: str) -> None:
    """Forbid silent changes to readings, states, attribution or proof records."""
    for field in (
        "scan", "reader", "decisions", "doubts", "second_boxes", "audit",
        "check_events", "hand",
    ):
        require(before.get(field) == after.get(field), f"Protected field changed: {name}/{field}")
    protected_rows = {
        "changes": (
            "id", "C", "H", "c_changed", "h_changed", "confidence", "kind",
            "error_category", "math_consequence", "crop", "box",
        ),
        "unlisted_decisions": (
            "id", "decision", "confidence", "source_mark", "C_mark",
        ),
        "inventory": (
            "element", "kind", "position", "box", "sheet_kind", "hand", "transcribed",
        ),
        "diff_coverage": ("row", "status", "change_id"),
    }
    for field, keys in protected_rows.items():
        old_rows, new_rows = before.get(field, []), after.get(field, [])
        require(len(old_rows) == len(new_rows), f"Record count changed: {name}/{field}")
        for old, new in zip(old_rows, new_rows):
            for key in keys:
                require(old.get(key) == new.get(key), f"Protected record field changed: {name}/{field}/{key}")


def preflight():
    plan = json.loads(PLAN.read_text())
    require(plan["schema"] == "cote145-apparatus-sync-plan-v1", "Unrecognized plan schema")
    require(tuple(plan["scope_scans"]) == SCANS, "Plan scope differs from completed-page scope")
    review = EDITION / plan["basis"]["review"]
    require(digest(review) == plan["basis"]["review_sha256"], "Sealed consistency review changed")
    for name, expected in plan["evidence_page_sha256"].items():
        require(digest(EDITION / name) == expected, f"Accepted page changed after plan preparation: {name}")

    # Verify the seal, and retain protected-file hashes for the application check.
    seal = EDITION / "second/FIRST_READINGS_SHA256.tsv"
    with seal.open(newline="") as stream:
        sealed = list(csv.DictReader(stream, delimiter="\t"))
    require(len(sealed) == 24, "Expected the complete 24-file first-reading seal")
    for row in sealed:
        require(digest(seal.parent / row["file"]) == row["sha256"], f"First-reading seal mismatch: {row['file']}")
    protected = {review, seal, *EDITION.glob("pages/*.tex")}
    protected.update(EDITION.glob("second/*_first.tsv"))
    protected.update(EDITION.glob("second/*_second.tsv"))
    protected.update(EDITION.glob("second/*_boxes.tsv"))
    protected.update(EDITION.glob("second/*_reading_receipt.json"))
    protected.update(EDITION.glob("second/*_comparison.tsv"))
    protected.update(EDITION.glob("second/*_adjudication.json"))
    protected_hashes = {path: digest(path) for path in protected}

    original_bytes, documents = {}, {}
    seen, ids = set(), set()
    for operation in plan["operations"]:
        name, path = operation["file"], operation["path"]
        require(name in ALLOWED_FILES, f"Unapproved target file: {name}")
        require(path and isinstance(path, list), "An operation has no explicit field path")
        allowed_fields = REPORT_FIELDS if name in REPORT_NAMES else METADATA_FIELDS
        require(path[0] in allowed_fields, f"Unapproved target field: {name}/{path[0]}")
        key = (name, tuple(path))
        require(key not in seen, f"Repeated operation target: {key}")
        require(operation["id"] not in ids, f"Duplicate operation ID: {operation['id']}")
        seen.add(key)
        ids.add(operation["id"])
        target = EDITION / name
        require(target.resolve() == target, f"Target must not be a symlink: {name}")
        if name not in documents:
            original_bytes[name] = target.read_bytes()
            documents[name] = json.loads(original_bytes[name])
        document = documents[name]
        anchor = operation.get("anchor")
        if anchor:
            require(value_at(document, anchor["path"]) == anchor["value"], f"Record anchor moved: {operation['id']}")
        exists = has_value(document, path)
        require(exists == operation["old_exists"], f"Expected-field presence changed: {operation['id']}")
        if exists:
            require(value_at(document, path) == operation["old"], f"Exact old value changed: {operation['id']}")
        require(operation.get("reason") and operation.get("evidence"), f"Missing rationale/evidence: {operation['id']}")
        evidence = operation["evidence"]
        evidence_items = evidence if isinstance(evidence, list) else [evidence]
        for item in evidence_items:
            if "source_sha256" in item:
                require(digest(EDITION / item["source"]) == item["source_sha256"], "H evidence file changed")
            if "audit_box" in item:
                source = json.loads((EDITION / item["report"]).read_text())
                matches = [row for row in source["audit"]["differences"] if row["box"] == item["audit_box"]]
                require(len(matches) == 1, f"Audit evidence box missing: {item['audit_box']}")
                require(matches[0]["final"] == item["accepted_final"], f"Accepted audit evidence changed: {item['audit_box']}")

    updated = copy.deepcopy(documents)
    for operation in plan["operations"]:
        parent = value_at(updated[operation["file"]], operation["path"][:-1])
        parent[operation["path"][-1]] = copy.deepcopy(operation["new"])
    for name, document in updated.items():
        if name in REPORT_NAMES:
            preserved_report_fields(documents[name], document, name)
    require(len(plan["operations"]) == plan["counts"]["operations"], "Plan operation count mismatch")
    require(len(updated) == plan["counts"]["target_files"], "Plan file count mismatch")
    return plan, original_bytes, updated, protected_hashes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply-reviewed-plan", action="store_true", help="Apply only after root has reviewed the explicit JSON plan")
    args = parser.parse_args()
    plan, original, updated, protected = preflight()
    summary = {
        "status": "PREFLIGHT_ONLY",
        "plan_sha256": digest(PLAN),
        "operations": len(plan["operations"]),
        "target_files": sorted(updated),
        "protected_files_checked": len(protected),
        "rebuild_executed": False,
    }
    if not args.apply_reviewed_plan:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return

    # Stage all outputs only after the entire exact-value preflight succeeds.
    staged = {}
    try:
        for name, document in updated.items():
            target = EDITION / name
            require(target.read_bytes() == original[name], f"Concurrent target edit: {name}")
            payload = (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode()
            with tempfile.NamedTemporaryFile(dir=target.parent, prefix=target.name + ".sync-", delete=False) as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
                staged[name] = Path(stream.name)
            staged[name].chmod(target.stat().st_mode & 0o777)
        for name in updated:
            require((EDITION / name).read_bytes() == original[name], f"Concurrent target edit: {name}")
        for path, expected in protected.items():
            require(digest(path) == expected, f"Protected evidence changed during preflight: {path.name}")
        for name in updated:
            os.replace(staged[name], EDITION / name)
        for path, expected in protected.items():
            require(digest(path) == expected, f"Protected evidence changed: {path.name}")
    finally:
        for path in staged.values():
            if path.exists():
                path.unlink()
    summary["status"] = "APPLIED_REVIEWED_PLAN"
    summary["next_step"] = "Root may inspect the report diffs, rebuild derived apparatus, and record the synchronization."
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
