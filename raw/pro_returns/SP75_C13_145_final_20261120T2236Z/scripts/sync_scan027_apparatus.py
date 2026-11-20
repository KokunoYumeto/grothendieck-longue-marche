"""Preflight or apply the exact, separately reviewed scan027 metadata plan.

Prepared without execution. Default operation is read-only preflight.
Only --apply-reviewed-plan authorizes this script's single report-file write.
Root must first review the adjacent paired JSON plan. The script patches only
selected JSON string-value spans, preserving every intervening byte. It never
writes a page, sealed reading, audit file, certificate, notation table, historical
review, validation cache or reader C's specified rho-serialization pointers.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import sys
import tempfile

EDITION = Path(__file__).resolve().parents[1]
PLAN = Path(__file__).with_name("sync_scan027_apparatus_plan.json")
EXPECTED_PLAN_SHA256 = '908a5ceb705c6f83b62cd715b1afc674663990c6491f7cc95665c328c5622a32'
TARGET = 'reader_reports/145_scan027_reviewed.json'
ALLOWED_PATHS = frozenset((('inventory', 2, 'first_words_or_objects'), ('inventory', 32, 'first_words_or_objects'), ('inventory', 32, 'position'), ('c_markup_audit', 'items', 3, 'reading'), ('c_markup_audit', 'items', 5, 'reading'), ('c_markup_audit', 'newly_recorded_cancellations', 1, 'reading'), ('notation', 4, 'observation'), ('notes', 2), ('notes', 1), ('changes', 18, 'place'), ('changes', 23, 'place'), ('doubts', 9, 'place'), ('doubts', 12, 'place'), ('doubts', 17, 'alternatives', 1)))
FORBIDDEN_READER_C_PATHS = frozenset((('changes', 6, 'final'), ('unlisted_decisions', 1, 'reading'), ('doubts', 4, 'reading'), ('doubts', 4, 'alternatives', 1), ('inventory', 12, 'first_words_or_objects'), ('inventory', 13, 'first_words_or_objects'), ('audit', 'differences', 4, 'final'), ('c_markup_audit', 'items', 1, 'reading')))
EXPECTED_IDS = frozenset(('A027-01', 'A027-02', 'A027-03', 'A027-04', 'A027-05', 'A027-06', 'A027-07', 'A027-08', 'A027-09', 'A027-10', 'A027-11', 'A027-12', 'A027-13', 'A027-14'))
RUNTIME_GLOBS = ('pages/*.tex', 'second/**/*', 'reader_reports/*_reviewed.json', 'reader_reports/*_check*.json', 'reader_reports/*certificate*.json', 'reader_reports/*counterexample*.json', 'reader_reports/final_consistency_review*.md', 'scripts/check_*.py', 'notation.md')
MISSING = object()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def hash_bytes(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    return hash_bytes(path.read_bytes())


def safe_file(name):
    require(isinstance(name, str) and name, "Empty or non-string file path")
    relative = PurePosixPath(name)
    require(not relative.is_absolute() and ".." not in relative.parts
            and "\\" not in name, f"Unsafe relative path: {name}")
    path = EDITION / name
    require(path.is_file() and path.resolve() == path,
            f"Missing, redirected or symlinked file: {name}")
    return path


def value_at(document, path):
    for key in path:
        document = document[key]
    return document


def parse_json_with_spans(source):
    """Parse without reserializing; retain exact character spans of every value."""
    decoder, spans = json.JSONDecoder(), {}

    def whitespace(position):
        while position < len(source) and source[position] in " \t\r\n":
            position += 1
        return position

    def parse(position, path):
        position = whitespace(position)
        require(position < len(source), "Unexpected end of JSON")
        start = position
        if source[position] == "{":
            value, position = {}, whitespace(position + 1)
            if source[position] == "}":
                position += 1
            else:
                while True:
                    key, end = decoder.raw_decode(source, position)
                    require(isinstance(key, str) and key not in value,
                            f"Invalid or duplicate JSON key at {path}")
                    position = whitespace(end)
                    require(source[position] == ":", "Missing JSON colon")
                    child, position = parse(position + 1, path + (key,))
                    value[key] = child
                    position = whitespace(position)
                    if source[position] == "}":
                        position += 1
                        break
                    require(source[position] == ",", "Missing JSON object comma")
                    position = whitespace(position + 1)
        elif source[position] == "[":
            value, position = [], whitespace(position + 1)
            if source[position] == "]":
                position += 1
            else:
                while True:
                    child, position = parse(position, path + (len(value),))
                    value.append(child)
                    position = whitespace(position)
                    if source[position] == "]":
                        position += 1
                        break
                    require(source[position] == ",", "Missing JSON array comma")
                    position = whitespace(position + 1)
        else:
            value, position = decoder.raw_decode(source, position)
        spans[path] = (start, position)
        return value, position

    document, end = parse(0, ())
    require(whitespace(end) == len(source), "Trailing material after JSON")
    require(document == json.loads(source), "JSON span parser disagrees with standard parser")
    return document, spans


def changed_leaf_paths(before, after, path=()):
    if before == after:
        return set()
    if path in ALLOWED_PATHS:
        require(isinstance(before, str) and isinstance(after, str),
                f"A permitted string field changed type: {path}")
        return {path}
    if isinstance(before, dict) and isinstance(after, dict):
        require(before.keys() == after.keys(), f"Unapproved object-key change at {path}")
        changed = set()
        for key in before:
            changed.update(changed_leaf_paths(before[key], after[key], path + (key,)))
        return changed
    if isinstance(before, list) and isinstance(after, list):
        require(len(before) == len(after), f"Unapproved record-count change at {path}")
        changed = set()
        for index, (old, new) in enumerate(zip(before, after)):
            changed.update(changed_leaf_paths(old, new, path + (index,)))
        return changed
    raise RuntimeError(f"Unapproved field change at {path}")


def protected_snapshot(plan):
    require(tuple(plan["protection"]["runtime_globs"]) == RUNTIME_GLOBS,
            "Runtime protection policy differs from the paired script")
    names = set(plan["protection"]["pinned_sha256"])
    for pattern in RUNTIME_GLOBS:
        for path in EDITION.glob(pattern):
            if path.is_file():
                name = path.relative_to(EDITION).as_posix()
                if name != TARGET:
                    names.add(name)
    require(TARGET not in names, "Writable target also appears in protected set")
    return {name: digest(safe_file(name)) for name in sorted(names)}


def verify_seals_and_evidence(plan):
    for pattern, expected_count in plan["protection"]["immutable_set_counts"].items():
        names = {p.relative_to(EDITION).as_posix()
                 for p in EDITION.glob(pattern) if p.is_file()}
        require(len(names) == expected_count == 24,
                f"Immutable 24-file set changed: {pattern}")
        require(names.issubset(plan["protection"]["pinned_sha256"]),
                f"Unpinned immutable record: {pattern}")
    seal_spec = plan["protection"]["first_seal"]
    require(seal_spec == {"file": "second/FIRST_READINGS_SHA256.tsv",
                          "expected_entries": 24}, "Unexpected first-seal specification")
    with safe_file(seal_spec["file"]).open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        require(reader.fieldnames == ["file", "sha256"], "Unexpected first-seal columns")
        rows = list(reader)
    require(len(rows) == 24 and len({r["file"] for r in rows}) == 24,
            "Expected exactly 24 unique sealed first readings")
    for row in rows:
        name = row["file"]
        require(Path(name).name == name and name.endswith("_first.tsv"),
                f"Unsafe first-seal filename: {name}")
        relative = "second/" + name
        require(relative in plan["protection"]["pinned_sha256"],
                f"First reading is not pinned: {name}")
        require(digest(safe_file(relative)) == row["sha256"], f"First seal failed: {name}")
    for identifier, evidence in plan["evidence"].items():
        source = safe_file(evidence["file"])
        if evidence["kind"] == "file_hash":
            require(digest(source) == evidence["sha256"], f"Evidence changed: {identifier}")
        elif evidence["kind"] == "audit_box":
            require(digest(source) == evidence["source_sha256"],
                    f"Adjudication bytes changed: {identifier}")
            document = json.loads(source.read_bytes())
            rows = [r for r in document["differences"] if r["box"] == evidence["box"]]
            require(len(rows) == 1, f"Missing or duplicated audit box: {identifier}")
            for field in ("final", "adjudication", "ink"):
                require(rows[0][field] == evidence["accepted_" + field],
                        f"Accepted audit {field} changed: {identifier}")
        else:
            raise RuntimeError(f"Unknown evidence kind: {identifier}")


def preflight():
    require(PLAN.is_file() and PLAN.resolve() == PLAN, "Missing or redirected plan")
    require(digest(PLAN) == EXPECTED_PLAN_SHA256, "Plan differs from exact paired bytes")
    plan = json.loads(PLAN.read_bytes())
    require(plan["schema"] == "cote145-scan027-apparatus-sync-plan-v1", "Wrong plan schema")
    require(plan["scope_scans"] == [27] and plan["target_file"] == TARGET,
            "Wrong scope or target")
    require(frozenset(map(tuple, plan["forbidden_reader_c_paths"])) == FORBIDDEN_READER_C_PATHS,
            "Reader C's reserved pointer set changed")
    require(not ALLOWED_PATHS.intersection(FORBIDDEN_READER_C_PATHS),
            "Metadata stage overlaps reader C's serialization stage")
    require(digest(safe_file(plan["basis"]["review"])) == plan["basis"]["review_sha256"],
            "Completed review changed")
    protected = protected_snapshot(plan)
    for name, expected in plan["protection"]["pinned_sha256"].items():
        require(protected.get(name) == expected, f"Pinned immutable file changed: {name}")
    require(set(plan["protection"]["prepared_inventory_sha256"]).issubset(protected),
            "A prepared protected file is missing")
    verify_seals_and_evidence(plan)

    original = safe_file(TARGET).read_bytes()
    source = original.decode("utf-8")
    document, spans = parse_json_with_spans(source)
    seen_paths, seen_ids, patches = set(), set(), []
    for operation in plan["operations"]:
        identifier = operation["id"]
        path = tuple(operation["path"])
        require(identifier not in seen_ids and identifier in EXPECTED_IDS,
                f"Unrecognized or repeated operation: {identifier}")
        require(path in ALLOWED_PATHS and path not in seen_paths,
                f"Unapproved or repeated field: {path}")
        require(operation["file"] == TARGET and operation["kind"] == "json_string_field",
                f"Invalid operation target or kind: {identifier}")
        require(operation.get("reason") and operation.get("evidence")
                and all(ref in plan["evidence"] for ref in operation["evidence"]),
                f"Missing rationale or evidence: {identifier}")
        for anchor in operation["anchors"]:
            require(value_at(document, anchor["path"]) == anchor["value"],
                    f"Record anchor changed: {identifier}")
        old, new = operation["old"], operation["new"]
        require(isinstance(old, str) and isinstance(new, str) and old != new,
                f"Operation must change one string value: {identifier}")
        require(value_at(document, path) == old, f"Exact old value changed: {identifier}")
        start, end = spans[path]
        require(source[start:end] == operation["old_json_lexeme"],
                f"Exact JSON string serialization changed: {identifier}")
        replacement = json.dumps(new, ensure_ascii=False)
        require(replacement == operation["new_json_lexeme"],
                f"New string lexeme is not the exact proposed value: {identifier}")
        patches.append((start, end, replacement, identifier))
        seen_paths.add(path)
        seen_ids.add(identifier)
    require(seen_paths == ALLOWED_PATHS and seen_ids == EXPECTED_IDS,
            "Incomplete operation ID or exact field set")
    require(len(patches) == plan["counts"]["operations"] == 14
            and plan["counts"]["target_files"] == 1, "Plan counts differ")

    pieces, cursor, unchanged_segments = [], 0, []
    for start, end, replacement, identifier in sorted(patches):
        require(cursor <= start < end, f"Overlapping JSON patches: {identifier}")
        segment = source[cursor:start]
        pieces.extend((segment, replacement))
        unchanged_segments.append(segment)
        cursor = end
    pieces.append(source[cursor:])
    unchanged_segments.append(source[cursor:])
    updated_source = "".join(pieces)
    updated_document, _ = parse_json_with_spans(updated_source)
    require(changed_leaf_paths(document, updated_document) == ALLOWED_PATHS,
            "Semantic report diff is not exactly the permitted metadata field set")
    # Every untouched segment is copied directly from the original UTF-8 text.
    require(pieces[0::2] == unchanged_segments, "Unexpected rewrite outside value spans")
    payload = updated_source.encode("utf-8")
    return plan, original, payload, protected


def stage_bytes(target, payload):
    """Only called inside the explicit reviewed-plan apply branch."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=target.parent,
                                         prefix=target.name + ".scan027-", delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.chmod(stat.S_IMODE(target.stat().st_mode))
        return temporary
    except BaseException:
        if temporary is not None and temporary.exists():
            temporary.unlink()
        raise


def apply_payload(plan, original, payload, protected):
    temporary, committed = None, False
    try:
        target = safe_file(TARGET)
        require(target.read_bytes() == original, "Concurrent report edit before staging")
        temporary = stage_bytes(target, payload)
        require(digest(PLAN) == EXPECTED_PLAN_SHA256, "Plan changed after preflight")
        require(target.read_bytes() == original, "Concurrent report edit before commit")
        require(protected_snapshot(plan) == protected,
                "Protected state changed during preflight; no target committed")
        os.replace(temporary, target)
        committed = True
        require(safe_file(TARGET).read_bytes() == payload, "Report changed after replacement")
        require(protected_snapshot(plan) == protected, "Protected state changed during application")
    except BaseException as failure:
        rollback_error = None
        if committed:
            rollback = None
            try:
                target = safe_file(TARGET)
                require(target.read_bytes() == payload, "Concurrent report edit prevents safe rollback")
                rollback = stage_bytes(target, original)
                os.replace(rollback, target)
            except BaseException as error:
                rollback_error = str(error)
            finally:
                if rollback is not None and rollback.exists():
                    rollback.unlink()
        print(json.dumps({"status": "FAILED_ROLLBACK_INCOMPLETE" if rollback_error
                          else "FAILED_TARGET_RESTORED_OR_NOT_COMMITTED",
                          "error": str(failure), "rollback_error": rollback_error,
                          "protected_files_were_never_write_targets": True},
                         ensure_ascii=False, indent=2), file=sys.stderr)
        raise
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply-reviewed-plan", action="store_true",
                        help="Root may apply only after reviewing the exact paired JSON plan")
    args = parser.parse_args()
    plan, original, payload, protected = preflight()
    prepared = plan["protection"]["prepared_inventory_sha256"]
    summary = {
        "status": "PREFLIGHT_ONLY",
        "plan_sha256": EXPECTED_PLAN_SHA256,
        "target": TARGET,
        "operations": 14,
        "target_changed_since_preparation": hash_bytes(original) != plan["target_prepared_sha256"],
        "planned_target_sha256": hash_bytes(payload),
        "pinned_immutable_files_checked": len(plan["protection"]["pinned_sha256"]),
        "protected_files_checked": len(protected),
        "protected_files_changed_since_preparation": [name for name, old in prepared.items()
                                                      if protected[name] != old],
        "protected_files_added_since_preparation": sorted(set(protected) - set(prepared)),
        "all_unselected_json_bytes_preserved": True,
        "actual_reading_fields_and_flags_preserved": True,
        "reader_c_pointers_written": False,
        "validation_written": False,
        "audit_records_written": False,
        "certificate_executed": False,
        "rebuild_executed": False,
        "deferred_current_counts": plan["deferred_validation_caches"]["derived_current_counts"],
    }
    if not args.apply_reviewed_plan:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return
    apply_payload(plan, original, payload, protected)
    summary["status"] = "APPLIED_REVIEWED_PLAN"
    summary["next_step"] = ("Root may inspect the exact report-field diff, coordinate reader C's "
                            "separate rho stage, and separately preserve historical validation "
                            "before generating fresh current counts after final serialization.")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
