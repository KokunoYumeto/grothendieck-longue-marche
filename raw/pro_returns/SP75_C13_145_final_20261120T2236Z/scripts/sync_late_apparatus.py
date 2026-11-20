"""Preflight or apply the separately reviewed late apparatus synchronization plan.

Prepared by reader A and not executed by its preparer. Without the explicit
--apply-reviewed-plan gate, this script performs read-only preflight and prints
a summary. Root must review the adjacent exact-value JSON plan before applying.

The only writable targets are three reviewed reports and the documentation
header of check_006_words.py. Accepted pages, immutable readings, audit records,
comparison/adjudication records, first seals, mathematical certificate outputs,
and the completed consistency review are protected. No edition rebuild, proof
execution, image reading, audit-log write, or new check event occurs here.
"""

from __future__ import annotations

import argparse
import ast
import copy
import csv
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import sys
import tempfile


EDITION = Path(__file__).resolve().parents[1]
PLAN = Path(__file__).with_name("sync_late_apparatus_plan.json")
EXPECTED_PLAN_SHA256 = '982068ce99921cf445fef7db5df04d7dd6ec5b48a073ed33037d20092e310906'
ALLOWED_JSON_PATHS = {
    name: frozenset(paths) for name, paths in {'reader_reports/145_scan019_reviewed.json': [('layout',), ('hand', 0), ('hand', 3), ('diff_coverage', 17, 'explanation'), ('unlisted_decisions', 1, 'ink'), ('unlisted_decisions', 2, 'ink'), ('unlisted_decisions', 3, 'ink'), ('unlisted_decisions', 4, 'ink'), ('doubts', 3, 'place'), ('inventory', 17, 'position'), ('inventory', 25, 'position'), ('notes', 12), ('notes', 13), ('check_events', 0, 'outcome'), ('check_events', 1, 'outcome')], 'reader_reports/145_scan020_reviewed.json': [('notation', 1), ('hand', 3), ('hand', 1), ('notes', 2), ('diff_coverage', 52, 'status'), ('diff_coverage', 52, 'change_id'), ('diff_coverage', 52, 'related_change_ids'), ('diff_coverage', 52, 'explanation'), ('changes', 34, 'place'), ('changes', 35, 'place')], 'reader_reports/145_scan006_reviewed.json': [('notes', 6), ('notes', 7), ('check_events', 0, 'outcome')]}.items()
}
ALLOWED_TARGETS = frozenset(('reader_reports/145_scan006_reviewed.json', 'reader_reports/145_scan019_reviewed.json', 'reader_reports/145_scan020_reviewed.json', 'scripts/check_006_words.py'))
EXPECTED_OPERATION_IDS = frozenset(('A019-01', 'A019-02', 'A019-03', 'A019-04', 'A019-05', 'A019-06', 'A019-07', 'A019-08', 'A019-09', 'A019-10', 'A019-11', 'A019-12', 'A019-13', 'A019-14', 'A019-15', 'A020-01', 'A020-02', 'A020-03', 'A020-04', 'A020-05', 'A020-06', 'A020-07', 'A020-08', 'A020-09', 'A020-10', 'A006-01', 'A006-02', 'A006-03', 'A006-04'))
RUNTIME_GLOBS = ('pages/*.tex', 'second/**/*', 'crops/second_*', 'reader_reports/*word_check*.json', 'reader_reports/*certificate*.json', 'reader_reports/*counterexample*.json', 'reader_reports/*proof_check*.json', 'reader_reports/*math_check*.json', 'scripts/check_*.py', 'reader_reports/final_consistency_review_a.md')
HEADER_TARGET = "scripts/check_006_words.py"
MISSING = object()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def hash_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def digest(path: Path) -> str:
    return hash_bytes(path.read_bytes())


def safe_file(name: str) -> Path:
    require(isinstance(name, str) and bool(name), "Empty or non-string path")
    relative = PurePosixPath(name)
    require(not relative.is_absolute() and ".." not in relative.parts
            and "\\" not in name, f"Unsafe relative path: {name}")
    path = EDITION / name
    require(path.is_file(), f"Required file missing: {name}")
    require(path.resolve() == path, f"Symlink or redirected file is not allowed: {name}")
    return path


def value_at(document, path):
    for key in path:
        document = document[key]
    return document


def has_value(document, path) -> bool:
    parent = value_at(document, path[:-1])
    key = path[-1]
    if isinstance(parent, list):
        return isinstance(key, int) and not isinstance(key, bool) and 0 <= key < len(parent)
    return isinstance(parent, dict) and isinstance(key, str) and key in parent


def assert_only_allowed_leaves(before, after, allowed, path=()) -> None:
    """A changed parent, reading, ID, state or record count cannot hide in a leaf edit."""
    if path in allowed:
        return
    if before == after:
        return
    if isinstance(before, dict) and isinstance(after, dict):
        for key in before.keys() | after.keys():
            assert_only_allowed_leaves(before.get(key, MISSING), after.get(key, MISSING),
                                       allowed, path + (key,))
        return
    if isinstance(before, list) and isinstance(after, list):
        require(len(before) == len(after), f"Unapproved record-count change: {path}")
        for index, (old, new) in enumerate(zip(before, after)):
            assert_only_allowed_leaves(old, new, allowed, path + (index,))
        return
    raise RuntimeError(f"Unapproved report-field change: {path}")


def executable_ast_without_header(payload: bytes):
    tree = ast.parse(payload.decode("utf-8"))
    require(bool(tree.body) and isinstance(tree.body[0], ast.Expr)
            and isinstance(tree.body[0].value, ast.Constant)
            and isinstance(tree.body[0].value.value, str),
            "The proof script must begin with its documentation string")
    tree.body = tree.body[1:]
    return ast.dump(tree, include_attributes=False)


def protected_snapshot(plan) -> dict[str, str]:
    names = set()
    require(tuple(plan["protection"]["runtime_globs"]) == RUNTIME_GLOBS,
            "Protected-file policy differs from the prepared script")
    for pattern in RUNTIME_GLOBS:
        for path in EDITION.glob(pattern):
            if path.is_file():
                name = path.relative_to(EDITION).as_posix()
                if name not in ALLOWED_TARGETS:
                    names.add(name)
    names.update(plan["protection"]["pinned_sha256"])
    require(not names.intersection(ALLOWED_TARGETS), "A protected file is also a writable target")
    return {name: digest(safe_file(name)) for name in sorted(names)}


def verify_first_seal(plan) -> None:
    specification = plan["protection"]["first_seal"]
    require(specification["file"] == "second/FIRST_READINGS_SHA256.tsv",
            "Unexpected first-reading seal")
    seal = safe_file(specification["file"])
    with seal.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        require(reader.fieldnames == ["file", "sha256"], "Unexpected first-seal columns")
        rows = list(reader)
    require(len(rows) == specification["expected_entries"] == 24,
            "The complete 24-file first-reading seal is required")
    seen = set()
    for row in rows:
        name = row["file"]
        require(Path(name).name == name and name.endswith("_first.tsv"),
                f"Invalid sealed filename: {name}")
        require(name not in seen, f"Duplicate first-seal entry: {name}")
        seen.add(name)
        relative = "second/" + name
        require(relative in plan["protection"]["pinned_sha256"],
                f"Sealed first reading is not pinned: {name}")
        require(digest(safe_file(relative)) == row["sha256"],
                f"First-reading seal mismatch: {name}")


def verify_evidence(plan) -> None:
    for identifier, item in plan["evidence"].items():
        kind = item["kind"]
        source = safe_file(item["file"])
        if kind == "file_hash":
            require(digest(source) == item["sha256"], f"Evidence changed: {identifier}")
        elif kind == "audit_box":
            require(digest(source) == item["source_sha256"],
                    f"Accepted adjudication changed: {identifier}")
            document = json.loads(source.read_text(encoding="utf-8"))
            rows = [row for row in document["differences"] if row["box"] == item["box"]]
            require(len(rows) == 1, f"Audit box missing or duplicated: {identifier}")
            for key, expected in (
                ("final", item["accepted_final"]),
                ("adjudication", item["accepted_adjudication"]),
                ("ink", item["accepted_ink"]),
            ):
                require(rows[0][key] == expected, f"Audit {key} changed: {identifier}")
        elif kind == "json_value":
            document = json.loads(source.read_text(encoding="utf-8"))
            require(value_at(document, item["path"]) == item["value"],
                    f"Conditional-scope evidence changed: {identifier}")
        elif kind == "python_body":
            payload = source.read_bytes()
            header = item["old_header"].encode("utf-8")
            require(payload.startswith(header), f"Proof header anchor changed: {identifier}")
            require(hash_bytes(payload[len(header):]) == item["body_sha256"],
                    f"Executable proof body changed: {identifier}")
        else:
            raise RuntimeError(f"Unrecognized evidence type: {kind}")


def preflight():
    require(PLAN.resolve() == PLAN and PLAN.is_file(), "Plan is missing or redirected")
    require(digest(PLAN) == EXPECTED_PLAN_SHA256,
            "Plan bytes differ from the exact plan paired with this script")
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    require(plan["schema"] == "cote145-late-apparatus-sync-plan-v1", "Wrong plan schema")
    require(plan["scope_scans"] == [6, 19, 20], "Wrong plan scope")
    require(frozenset(plan["allowed_target_files"]) == ALLOWED_TARGETS,
            "Plan target files differ from the hardcoded allowlist")
    review = safe_file(plan["basis"]["review"])
    require(digest(review) == plan["basis"]["review_sha256"], "Completed review changed")
    protected = protected_snapshot(plan)
    for name, expected in plan["protection"]["pinned_sha256"].items():
        require(protected.get(name) == expected, f"Pinned evidence changed: {name}")
    prepared_protected = plan["protection"]["prepared_inventory_sha256"]
    require(set(prepared_protected).issubset(protected), "A prepared protected file is missing")
    verify_first_seal(plan)
    verify_evidence(plan)

    originals, documents, payloads = {}, {}, {}
    seen_paths, seen_ids, header_operations = set(), set(), []
    actual_json_paths = {name: set() for name in ALLOWED_JSON_PATHS}
    for operation in plan["operations"]:
        identifier, kind, name = operation["id"], operation["kind"], operation["file"]
        require(identifier not in seen_ids, f"Duplicate operation ID: {identifier}")
        seen_ids.add(identifier)
        require(name in ALLOWED_TARGETS, f"Unapproved target: {name}")
        require(operation.get("reason") and operation.get("evidence"),
                f"Missing rationale or evidence: {identifier}")
        require(all(key in plan["evidence"] for key in operation["evidence"]),
                f"Unknown evidence reference: {identifier}")
        target = safe_file(name)
        originals.setdefault(name, target.read_bytes())
        if kind == "json_field":
            path = operation["path"]
            require(isinstance(path, list) and path
                    and all(isinstance(key, str) or
                            (isinstance(key, int) and not isinstance(key, bool)) for key in path),
                    f"Invalid exact field path: {identifier}")
            key = (name, tuple(path))
            require(name in ALLOWED_JSON_PATHS and tuple(path) in ALLOWED_JSON_PATHS[name],
                    f"Unapproved field: {identifier}")
            require(key not in seen_paths, f"Repeated field: {identifier}")
            seen_paths.add(key)
            actual_json_paths[name].add(tuple(path))
            if name not in documents:
                documents[name] = json.loads(originals[name])
            document = documents[name]
            for item in operation["anchors"]:
                require(value_at(document, item["path"]) == item["value"],
                        f"Record anchor changed: {identifier}")
            exists = has_value(document, path)
            require(exists == operation["old_exists"], f"Field presence changed: {identifier}")
            if exists:
                require(value_at(document, path) == operation["old"],
                        f"Exact old field value changed: {identifier}")
            require(operation["old"] != operation["new"], f"No-op operation: {identifier}")
        elif kind == "python_header":
            require(name == HEADER_TARGET and operation["header_offset_bytes"] == 0,
                    "Only the scan006 documentation header may be changed")
            header_operations.append(operation)
        else:
            raise RuntimeError(f"Unknown operation kind: {kind}")
    require(seen_ids == EXPECTED_OPERATION_IDS, "Operation ID set differs from the prepared plan")
    require({name: frozenset(paths) for name, paths in actual_json_paths.items()} == ALLOWED_JSON_PATHS,
            "The exact report-field set differs from the prepared script")
    require(len(header_operations) == 1, "Exactly one proof documentation-header change is required")
    require(set(originals) == ALLOWED_TARGETS, "Writable target set is incomplete")

    updated = copy.deepcopy(documents)
    for operation in plan["operations"]:
        if operation["kind"] == "json_field":
            parent = value_at(updated[operation["file"]], operation["path"][:-1])
            parent[operation["path"][-1]] = copy.deepcopy(operation["new"])
    for name, document in updated.items():
        assert_only_allowed_leaves(documents[name], document, ALLOWED_JSON_PATHS[name])
        payloads[name] = (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")

    operation = header_operations[0]
    name = operation["file"]
    old_header, new_header = operation["old"].encode("utf-8"), operation["new"].encode("utf-8")
    original = originals[name]
    require(original.startswith(old_header) and original.count(old_header) == 1,
            "The exact scan006 header anchor changed")
    body = original[len(old_header):]
    require(hash_bytes(body) == operation["body_sha256"], "The scan006 proof body changed")
    payloads[name] = new_header + body
    require(payloads[name][len(new_header):] == body, "The proof body would not remain byte-identical")
    require(executable_ast_without_header(original) == executable_ast_without_header(payloads[name]),
            "Executable proof AST would change")

    require(len(plan["operations"]) == plan["counts"]["operations"] == 29,
            "Plan operation count mismatch")
    require(sum(x["kind"] == "json_field" for x in plan["operations"])
            == plan["counts"]["json_field_operations"] == 28, "JSON operation count mismatch")
    require(plan["counts"]["python_header_operations"] == 1, "Header count mismatch")
    require(len(payloads) == plan["counts"]["target_files"] == 4, "Target count mismatch")
    return plan, originals, payloads, protected


def stage_bytes(target: Path, payload: bytes) -> Path:
    """Called only after the explicit reviewed-plan apply gate."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=target.parent, prefix=target.name + ".late-",
                                         delete=False) as stream:
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


def apply_payloads(plan, originals, payloads, protected):
    staged, committed = {}, []
    try:
        for name, payload in payloads.items():
            target = safe_file(name)
            require(target.read_bytes() == originals[name], f"Concurrent target edit: {name}")
            staged[name] = stage_bytes(target, payload)
        require(digest(PLAN) == EXPECTED_PLAN_SHA256, "Plan changed during preflight")
        for name, original in originals.items():
            require(safe_file(name).read_bytes() == original, f"Concurrent target edit: {name}")
        require(protected_snapshot(plan) == protected,
                "Protected evidence changed during preflight; no targets committed")
        for name in payloads:
            require(safe_file(name).read_bytes() == originals[name], f"Concurrent target edit: {name}")
            os.replace(staged[name], EDITION / name)
            committed.append(name)
        for name, payload in payloads.items():
            require(safe_file(name).read_bytes() == payload, f"Target changed after replacement: {name}")
        require(protected_snapshot(plan) == protected, "Protected evidence changed during application")
    except BaseException as failure:
        rollback_problems = []
        for name in reversed(committed):
            temporary = None
            try:
                target = safe_file(name)
                require(target.read_bytes() == payloads[name],
                        f"Concurrent edit prevents safe rollback: {name}")
                temporary = stage_bytes(target, originals[name])
                os.replace(temporary, target)
            except BaseException as rollback_failure:
                rollback_problems.append(str(rollback_failure))
            finally:
                if temporary is not None and temporary.exists():
                    temporary.unlink()
        print(json.dumps({
            "status": "FAILED_ROLLBACK_INCOMPLETE" if rollback_problems else "FAILED_TARGETS_RESTORED",
            "error": str(failure),
            "rollback_problems": rollback_problems,
            "protected_files_were_never_write_targets": True,
        }, ensure_ascii=False, indent=2), file=sys.stderr)
        raise
    finally:
        for temporary in staged.values():
            if temporary.exists():
                temporary.unlink()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply-reviewed-plan", action="store_true",
                        help="Root may apply only after reviewing the exact paired JSON plan")
    args = parser.parse_args()
    plan, originals, payloads, protected = preflight()
    prepared_protected = plan["protection"]["prepared_inventory_sha256"]
    summary = {
        "status": "PREFLIGHT_ONLY",
        "plan_sha256": EXPECTED_PLAN_SHA256,
        "operations": len(plan["operations"]),
        "target_files": sorted(payloads),
        "planned_target_sha256": {name: hash_bytes(payload) for name, payload in payloads.items()},
        "pinned_files_checked": len(plan["protection"]["pinned_sha256"]),
        "protected_files_checked": len(protected),
        "protected_files_changed_since_preparation": [
            name for name, old in prepared_protected.items() if protected[name] != old
        ],
        "protected_files_added_since_preparation": sorted(set(protected) - set(prepared_protected)),
        "target_metadata_changed_since_preparation": [
            name for name, payload in originals.items()
            if hash_bytes(payload) != plan["targets_prepared_sha256"][name]
        ],
        "only_explicit_field_anchors_authorize_report_updates": True,
        "proof_body_and_executable_ast_unchanged": True,
        "rebuild_executed": False,
        "certificate_executed": False,
        "audit_records_written": False,
    }
    if not args.apply_reviewed_plan:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return
    apply_payloads(plan, originals, payloads, protected)
    summary["status"] = "APPLIED_REVIEWED_PLAN"
    summary["next_step"] = (
        "Root may inspect the four target diffs and separately rebuild derived apparatus. "
        "Historical audit/report_replace snapshots, certificates and sealed readings remain unchanged."
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
