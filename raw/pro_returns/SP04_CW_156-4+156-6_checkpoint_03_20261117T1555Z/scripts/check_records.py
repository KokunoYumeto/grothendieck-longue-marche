#!/usr/bin/env python3
"""Read-only record-schema and path-existence checks, without reading decisions.

Does not import author.py/manage.py, open source witnesses or scans, open page
transcriptions, or interpret/print any prose or LaTeX record field. Only JSON
keys, types, identity/status/category metadata, and explicit crop paths are
examined. A crop mentioned only inside free-text comments is not inspected.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import json
from pathlib import Path
import re

DEFAULT_OUT = Path(__file__).resolve().parents[1]
EXPECTED = [("156-4", scan) for scan in range(2, 90)] + [("156-6", scan) for scan in range(2, 34)]
CONFIDENCES = {"high", "medium", "low"}
CHANGE_KINDS = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state (struck given live or live given struck)", "insertion or placement",
    "abbreviation expanded or spelling modernised", "readable ink left as \\ill{}",
    "drawing or diagram", "other",
}
INVENTORY_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover"}
MARKS = {"yes", "no", "unclear"}
RECORD_RE = re.compile(r"^(156-[46])_scan(\d{3})\.json$")


def compressed_pages(pages):
    """Present missing/pending identities as ranges, never record text."""
    groups = {}
    for cote, scan in pages:
        groups.setdefault(cote, []).append(scan)
    output = []
    for cote, scans in sorted(groups.items()):
        ordered = sorted(set(scans))
        if not ordered:
            continue
        first = last = ordered[0]
        for scan in ordered[1:] + [None]:
            if scan == last + 1:
                last = scan
                continue
            output.append(f"{cote}:{first:03d}" + (f"–{last:03d}" if last != first else ""))
            first = last = scan
    return output


def check_records(out=DEFAULT_OUT, require_all=False):
    out = Path(out).resolve()
    record_dir = out / "records"
    issues, warnings = [], []
    done, audited, missing, present = [], [], [], []
    crop_count = 0
    crop_paths = set()
    totals = Counter()

    def problem(record_name, location, code, message, severity="error"):
        item = {"record": record_name, "field": location, "code": code, "message": message}
        (issues if severity == "error" else warnings).append(item)

    def require_keys(obj, keys, name, location):
        for key in keys:
            if key not in obj:
                problem(name, f"{location}.{key}" if location else key, "missing_key", "Required field is missing")

    def text_field(obj, key, name, location, required=True, nonempty=False):
        """Inspect only string type/length. Never inspect or expose its content."""
        if key not in obj:
            if required:
                problem(name, f"{location}.{key}" if location else key, "missing_key", "Required field is missing")
            return
        value = obj[key]
        if not isinstance(value, str):
            problem(name, f"{location}.{key}" if location else key, "wrong_type", "Expected a string")
        elif nonempty and len(value) == 0:
            problem(name, f"{location}.{key}" if location else key, "empty_string", "Required string is empty")

    def explicit_crop(value, name, location):
        nonlocal crop_count
        crop_count += 1
        if not isinstance(value, str):
            problem(name, location, "wrong_type", "Crop reference must be a path string")
            return
        if not value:
            problem(name, location, "missing_crop_reference", "Crop reference is empty")
            return
        path = Path(value)
        resolved = path.resolve() if path.is_absolute() else (out / path).resolve()
        crop_paths.add(str(resolved))
        try:
            resolved.relative_to(out / "crops")
        except ValueError:
            problem(name, location, "crop_outside_crops", "Explicit crop reference is outside out/crops", "warning")
        if not resolved.is_file():
            # The path is administrative metadata, not reading text.
            problem(name, location, "missing_crop_file", f"Referenced crop file does not exist: {value}")

    files = sorted(record_dir.glob("*.json")) if record_dir.exists() else []
    expected_paths = {f"{cote}_scan{scan:03d}.json": (cote, scan) for cote, scan in EXPECTED}
    for path in files:
        name = path.name
        match = RECORD_RE.fullmatch(name)
        if not match or name not in expected_paths:
            problem(name, "filename", "unexpected_record", "Filename is outside the task's expected cote/scan ranges")
            continue
        cote, scan = expected_paths[name]
        present.append((cote, scan))
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            problem(name, "", "invalid_json", f"Invalid JSON at line {error.lineno}, column {error.colno}")
            continue
        except (OSError, UnicodeError) as error:
            problem(name, "", "unreadable_record", f"Cannot read record ({type(error).__name__})")
            continue
        if not isinstance(record, dict):
            problem(name, "", "wrong_type", "Record must be an object")
            continue
        require_keys(record, ("cote", "scan", "changes", "inventory", "doubts"), name, "")
        if record.get("cote") != cote or type(record.get("scan")) is not int or record.get("scan") != scan:
            problem(name, "identity", "identity_mismatch", "Cote/scan identity must agree with the filename")

        status = record.get("status", {})
        if not isinstance(status, dict):
            problem(name, "status", "wrong_type", "Status must be an object")
            status = {}
        for status_key, destination in (("done", done), ("audited", audited)):
            if status_key not in status:
                continue
            value = status[status_key]
            if not isinstance(value, str) or not value:
                problem(name, f"status.{status_key}", "invalid_timestamp", "Status requires a nonempty timestamp string")
                continue
            try:
                datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC")
            except ValueError:
                problem(name, f"status.{status_key}", "invalid_timestamp", "Timestamp must use YYYY-MM-DD HH:MM:SS UTC")
                continue
            destination.append((cote, scan))
        if "audited" in status and "done" not in status:
            problem(name, "status", "audit_without_done", "An audit mark exists without a done mark")

        for list_key in ("changes", "inventory", "doubts", "notation", "abbreviations"):
            if list_key not in record:
                continue
            if not isinstance(record[list_key], list):
                problem(name, list_key, "wrong_type", "Expected an array")
                continue
            totals[list_key] += len(record[list_key])

        changes = record.get("changes", [])
        for index, change in enumerate(changes if isinstance(changes, list) else [], 1):
            where = f"changes[{index}]"
            if not isinstance(change, dict):
                problem(name, where, "wrong_type", "Change must be an object")
                continue
            for key in ("place", "C", "H", "final", "scan_shows"):
                text_field(change, key, name, where)
            for key in ("differs_C", "differs_H"):
                if key not in change:
                    problem(name, f"{where}.{key}", "missing_key", "Required difference flag is missing")
                elif type(change[key]) is not bool:
                    problem(name, f"{where}.{key}", "wrong_type", "Difference flag must be a boolean")
            if not isinstance(change.get("confidence"), str) or change["confidence"] not in CONFIDENCES:
                problem(name, f"{where}.confidence", "invalid_confidence", "Expected high, medium, or low")
            mark = change.get("marked_in_H")
            if isinstance(mark, bool):
                problem(name, f"{where}.marked_in_H", "boolean_marked_in_H", "Boolean found; expected the string yes, no, or unclear")
            elif not isinstance(mark, str) or mark not in MARKS:
                problem(name, f"{where}.marked_in_H", "invalid_marked_in_H", "Expected the string yes, no, or unclear")
            kind = change.get("kind")
            if not isinstance(kind, str) or kind not in CHANGE_KINDS:
                problem(name, f"{where}.kind", "invalid_change_kind", "Expected one of the prompt's exact collation kind values")
            if "crop" not in change:
                problem(name, f"{where}.crop", "missing_crop_reference", "Required explicit crop reference is missing")
            else:
                explicit_crop(change["crop"], name, f"{where}.crop")

        inventory = record.get("inventory", [])
        if isinstance(inventory, list) and not inventory:
            problem(name, "inventory", "empty_inventory", "A page record must contain inventory elements")
        element_ids = set()
        for index, item in enumerate(inventory if isinstance(inventory, list) else [], 1):
            where = f"inventory[{index}]"
            if not isinstance(item, dict):
                problem(name, where, "wrong_type", "Inventory element must be an object")
                continue
            for key in ("position", "first_words_or_objects", "hand"):
                text_field(item, key, name, where, nonempty=True)
            element_id = item.get("element")
            if not isinstance(element_id, (str, int)) or isinstance(element_id, bool) or element_id == "":
                problem(name, f"{where}.element", "invalid_element_id", "Element identifier must be a nonempty string or integer")
            elif element_id in element_ids:
                problem(name, f"{where}.element", "duplicate_element_id", "Element identifier is duplicated within this record")
            else:
                element_ids.add(element_id)
            if not isinstance(item.get("kind"), str) or item["kind"] not in INVENTORY_KINDS:
                problem(name, f"{where}.kind", "invalid_inventory_kind", "Expected a permitted inventory kind")
            if not isinstance(item.get("sheet_kind"), str) or item["sheet_kind"] not in SHEET_KINDS:
                problem(name, f"{where}.sheet_kind", "invalid_sheet_kind", "Expected a permitted sheet kind")
            if item.get("transcribed") != "yes":
                problem(name, f"{where}.transcribed", "inventory_not_confirmed", "Expected the string yes")

        doubts = record.get("doubts", [])
        for index, doubt in enumerate(doubts if isinstance(doubts, list) else [], 1):
            where = f"doubts[{index}]"
            if not isinstance(doubt, dict):
                problem(name, where, "wrong_type", "Doubt must be an object")
                continue
            for key in ("line", "reading"):
                text_field(doubt, key, name, where)
            text_field(doubt, "comment", name, where, required=False)
            alternatives = doubt.get("alternatives")
            if not isinstance(alternatives, (str, list)) or (isinstance(alternatives, list) and any(not isinstance(x, str) for x in alternatives)):
                problem(name, f"{where}.alternatives", "invalid_alternatives_type", "Expected a string or array of strings")
            if not isinstance(doubt.get("confidence"), str) or doubt["confidence"] not in CONFIDENCES:
                problem(name, f"{where}.confidence", "invalid_confidence", "Expected high, medium, or low")
            if "crop" in doubt:
                explicit_crop(doubt["crop"], name, f"{where}.crop")
            else:
                totals["doubts_without_structured_crop"] += 1

        notation = record.get("notation", [])
        for index, entry in enumerate(notation if isinstance(notation, list) else [], 1):
            where = f"notation[{index}]"
            if not isinstance(entry, dict):
                problem(name, where, "wrong_type", "Notation entry must be an object")
                continue
            for key in ("sign", "latex", "appearance", "locations", "alternatives"):
                text_field(entry, key, name, where)
        abbreviations = record.get("abbreviations", [])
        for index, entry in enumerate(abbreviations if isinstance(abbreviations, list) else [], 1):
            where = f"abbreviations[{index}]"
            if not isinstance(entry, dict):
                problem(name, where, "wrong_type", "Abbreviation entry must be an object")
                continue
            for key in ("abbreviation", "expansion", "evidence"):
                text_field(entry, key, name, where, required=(key != "evidence"))

    present_set = set(present)
    missing = [key for key in EXPECTED if key not in present_set]
    if require_all and missing:
        problem("", "records", "missing_records", f"{len(missing)} expected page records are absent")
    done_set, audited_set = set(done), set(audited)
    # Enforce only status ordering; no conclusion about whether reading occurred.
    for key in done:
        index = EXPECTED.index(key)
        if any(previous not in done_set for previous in EXPECTED[:index]):
            problem(f"{key[0]}_scan{key[1]:03d}.json", "status.done", "completion_order_gap", "An earlier expected page lacks a valid done timestamp")
            break
    if audited and len(done_set) != len(EXPECTED):
        problem("", "status.audited", "audits_before_all_done", "Audit timestamps are present before all 120 pages have valid done timestamps")
    for key in audited:
        index = EXPECTED.index(key)
        if any(previous not in audited_set for previous in EXPECTED[:index]):
            problem(f"{key[0]}_scan{key[1]:03d}.json", "status.audited", "audit_order_gap", "An earlier expected page lacks a valid audited timestamp")
            break
    return {
        "expected_pages": len(EXPECTED), "record_files_found": len(files),
        "expected_records_present": len(present), "done": len(done_set), "audited": len(audited_set),
        "missing_records": compressed_pages(missing),
        "present_without_done": compressed_pages([key for key in present if key not in done_set]),
        "entry_counts": dict(totals), "explicit_crop_references_checked": crop_count,
        "unique_crop_paths_checked": len(crop_paths),
        "error_count": len(issues), "warning_count": len(warnings),
        "errors": issues, "warnings": warnings,
        "limits": [
            "Only schema, categorical metadata, identity/status timestamps, and explicit crop-path existence were checked.",
            "Prose and LaTeX values were not interpreted or printed; page/scans/witness/context files were not opened.",
            "Doubt crop references stored only inside free-text comments are not inspected; add a separate crop field to enable path checking.",
            "Done/audited counts report record timestamps only; they do not establish that visual readings occurred."
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--require-all", action="store_true", help="Treat missing expected page records as an error")
    args = parser.parse_args()
    result = check_records(args.out, args.require_all)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["error_count"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
