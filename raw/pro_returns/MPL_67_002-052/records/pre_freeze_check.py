#!/usr/bin/env python3
"""Read-only completion checks. No audit, source, inventory, doubt or hash writes.

This checks file structure and recorded events. It does not assess manuscript
readings, notation identity, image coverage, research claims or PDF layout.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
import validate_package as package


def split_table_row(line: str) -> list[str]:
    result, current = [], []
    escaped = False
    for char in line.strip():
        if char == "|" and not escaped:
            result.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        escaped = (not escaped) if char == "\\" else False
    result.append("".join(current).strip())
    if result and not result[0]:
        result.pop(0)
    if result and not result[-1]:
        result.pop()
    return result


def tables(lines: list[str]) -> list[dict]:
    found = []
    i = 0
    while i + 1 < len(lines):
        if lines[i].lstrip().startswith("|") and lines[i + 1].lstrip().startswith("|"):
            header = split_table_row(lines[i])
            separator = split_table_row(lines[i + 1])
            if separator and all(re.fullmatch(r":?-{3,}:?", cell) for cell in separator):
                start = i
                i += 2
                rows = []
                while i < len(lines) and lines[i].lstrip().startswith("|"):
                    rows.append((i + 1, split_table_row(lines[i])))
                    i += 1
                found.append({"line": start + 1, "header": header, "rows": rows})
                continue
        i += 1
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=package.DEFAULT_ROOT)
    parser.add_argument("--before-assembly", action="store_true", help="Inspect readiness without requiring the combined fragment")
    parser.add_argument("--allow-stale-qa", action="store_true", help="Report stale syntax checks as warnings while an audit is in progress")
    parser.add_argument("--after-freeze", action="store_true", help="Verify the frozen state without writing any hash or log record")
    args = parser.parse_args()
    root = args.root.resolve()
    errors = package.validate(root, require_combined=not args.before_assembly)
    warnings = []
    expected = set(package.SCANS)
    progress = (root / "progress.log").read_text(encoding="utf-8")
    done = {int(n) for n in re.findall(r"^67 scan (\d{3}) done ", progress, re.MULTILINE)}
    audited = {int(n) for n in re.findall(r"^scan (\d{3}) audited ", progress, re.MULTILINE)}
    for kind, seen in (("done", done), ("audited", audited)):
        if expected - seen:
            errors.append(f"Missing {kind} log markers: " + ",".join(f"{n:03d}" for n in sorted(expected - seen)))
        if seen - expected:
            errors.append(f"Unexpected {kind} scan numbers: " + ",".join(map(str, sorted(seen - expected))))
    if not args.after_freeze and re.search(r"^context opened ", progress, re.MULTILINE):
        errors.append("A context-opened event is already recorded; this is a pre-freeze check")
    if not args.after_freeze and re.search(r"^transcription frozen ", progress, re.MULTILINE):
        warnings.append("The transcription is already frozen; use verify-freeze for integrity checks")
    frozen_count = 0
    frozen_hashes_unchanged = None
    if args.after_freeze:
        frozen_hashes_unchanged = True
        manifest_path = root / "records/transcription.sha256"
        if not manifest_path.is_file():
            errors.append("Freeze manifest is missing")
            frozen_hashes_unchanged = False
        else:
            expected_paths = {package.page_path(root, n).relative_to(root).as_posix() for n in package.SCANS}
            expected_paths.add(package.combined_path(root).relative_to(root).as_posix())
            seen_paths = set()
            for line in manifest_path.read_text(encoding="utf-8").splitlines():
                frozen_count += 1
                digest, relative = line.split("  ", 1)
                if relative in seen_paths or relative not in expected_paths:
                    errors.append("Duplicate or unexpected freeze-manifest path: " + relative)
                    frozen_hashes_unchanged = False
                    continue
                seen_paths.add(relative)
                target = root / relative
                if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != digest:
                    errors.append("Frozen hash differs: " + relative)
                    frozen_hashes_unchanged = False
            if frozen_count != 47 or seen_paths != expected_paths:
                errors.append("Freeze manifest does not contain exactly the 47 required paths")
                frozen_hashes_unchanged = False

    inventory = list(csv.DictReader((root / f"{package.PACKAGE}_inventory.csv").open(newline="", encoding="utf-8")))
    inventory_kinds = {}
    mixed_sheet_kinds = []
    for scan in package.SCANS:
        rows = [row for row in inventory if row.get("scan", "").isdigit() and int(row["scan"]) == scan]
        kinds = {row["sheet_kind"] for row in rows}
        if len(kinds) > 1:
            mixed_sheet_kinds.append(scan)
        inventory_kinds[scan] = {kind: sum(row["kind"] == kind for row in rows)
                                 for kind in package.ELEMENT_KINDS}
    if mixed_sheet_kinds:
        errors.append("Different sheet_kind values occur within scans: " + ",".join(map(str, mixed_sheet_kinds)))

    uncertainty_counts = {}
    annotation_count_differences = []
    annotation_totals = {}
    for scan in package.SCANS:
        source = package.page_path(root, scan).read_text(encoding="utf-8")
        uncertainty_counts[scan] = len(re.findall(r"\\(?:unsure|illegible)\s*\{", source))
        if re.search(r"\\(?:includegraphics|includesvg|includepdf|pdfximage)\b", source):
            errors.append(f"Image-inclusion command found in scan {scan:03d}")
        for macro, kind in (("deleted", "deletion"), ("inserted", "insertion"),
                            ("margin", "margin note"), ("diagram", "diagram"),
                            ("figure", "drawing")):
            count = len(re.findall(r"\\" + macro + r"\s*\{", source))
            rows = inventory_kinds[scan][kind]
            totals = annotation_totals.setdefault(macro, {"inventory_kind": kind, "macro_occurrences": 0, "inventory_rows": 0})
            totals["macro_occurrences"] += count
            totals["inventory_rows"] += rows
            if count != rows:
                annotation_count_differences.append({"scan": scan, "macro": macro, "kind": kind, "macro_count": count, "inventory_rows": rows,
                    "count_relation": "more_macro_occurrences" if count > rows else "more_inventory_rows"})
    if annotation_count_differences:
        warnings.append("Annotation macro and inventory-row counts differ in listed cases; grouping and scope are for the primary reader to resolve")

    doubt_lines = (root / f"{package.PACKAGE}_doubts.md").read_text(encoding="utf-8").splitlines()
    headings = [(i + 1, line.lower()) for i, line in enumerate(doubt_lines) if re.match(r"^#{1,6}\s", line)]
    sections = {name: any(re.search(pattern, heading) for _, heading in headings)
                for name, pattern in {"notation": "notation", "doubts": "doubt", "abbreviations": "abbreviat", "legibility": "legib|reliab|trust"}.items()}
    for name, present in sections.items():
        if not present:
            warnings.append(f"A {name} section was not identified by its heading; confirm the requested content is present")
    parsed_tables = tables(doubt_lines)
    doubt_table = next((table for table in parsed_tables
                        if any("confidence" in header.lower() for header in table["header"])
                        and any("scan" in header.lower() for header in table["header"])), None)
    doubt_counts = {scan: 0 for scan in package.SCANS}
    if not parsed_tables:
        errors.append("No Markdown tables were recognized in the doubts file")
    if not doubt_table:
        errors.append("No doubts table with scan and confidence columns was recognized")
    else:
        headers = [header.lower() for header in doubt_table["header"]]
        scan_col = next(i for i, header in enumerate(headers) if "scan" in header)
        confidence_col = next(i for i, header in enumerate(headers) if "confidence" in header)
        for line, cells in doubt_table["rows"]:
            if len(cells) != len(headers):
                errors.append(f"Doubts table line {line} has {len(cells)} cells; expected {len(headers)} (check unescaped pipes)")
                continue
            if cells[confidence_col].strip().lower() not in {"high", "medium", "low"}:
                errors.append(f"Doubts table line {line} has a confidence value outside high/medium/low")
            if cells[scan_col].isdigit() and int(cells[scan_col]) in expected:
                doubt_counts[int(cells[scan_col])] += 1
            else:
                warnings.append(f"Doubts table line {line} has a scan reference that needs manual interpretation")
        if parsed_tables[0] is doubt_table:
            errors.append("The doubts table precedes the notation table")
        missing_doubt_scans = [scan for scan in package.SCANS if uncertainty_counts[scan] and not doubt_counts[scan]]
        if missing_doubt_scans:
            errors.append("Uncertainty macros occur without a recognized doubts-table row for scans: " + ",".join(map(str, missing_doubt_scans)))

    qa_path = root / "records/latex_qa_report.json"
    stale_qa, failed_qa, missing_glyphs = [], [], []
    if not qa_path.is_file():
        errors.append("No per-page syntax QA report exists")
    else:
        qa = json.loads(qa_path.read_text(encoding="utf-8"))
        reports = {entry["scan"]: entry for entry in qa.get("reports", [])}
        for scan in package.SCANS:
            entry = reports.get(scan, {})
            source = package.page_path(root, scan)
            current = hashlib.sha256(source.read_bytes()).hexdigest()
            if entry.get("source_hashes", {}).get(str(source)) != current:
                stale_qa.append(scan)
            if entry.get("compiler_returncode") != 0:
                failed_qa.append(scan)
            if entry.get("missing_character_diagnostics"):
                missing_glyphs.append(scan)
        if stale_qa:
            (warnings if args.allow_stale_qa else errors).append("Syntax QA is stale for scans: " + ",".join(map(str, stale_qa)))
        if failed_qa:
            errors.append("Unsuccessful recorded syntax checks for scans: " + ",".join(map(str, failed_qa)))
        if missing_glyphs:
            errors.append("Recorded missing-glyph diagnostics for scans: " + ",".join(map(str, missing_glyphs)))

    manifest = root / "records/scripts/script_manifest.json"
    provenance_count = 0
    if manifest.is_file():
        for entry in json.loads(manifest.read_text(encoding="utf-8"))["scripts"]:
            provenance_count += 1
            copy = root / "records/scripts" / entry["filename"]
            if not copy.is_file() or hashlib.sha256(copy.read_bytes()).hexdigest() != entry["sha256"]:
                errors.append("Provenance copy differs from its manifest: " + entry["filename"])
    else:
        warnings.append("No script provenance manifest was found")
    report = {
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "scope": "Read-only structure and recorded-event checks; no reading, research or layout assessment",
        "combined_required": not args.before_assembly,
        "phase": "after-freeze" if args.after_freeze else "before-freeze",
        "frozen_hashes_checked": frozen_count,
        "frozen_hashes_unchanged": frozen_hashes_unchanged,
        "done_scans": len(done & expected), "audited_scans": len(audited & expected),
        "inventory_rows": len(inventory), "doubts_sections_detected_by_heading": sections,
        "uncertainty_macro_count": sum(uncertainty_counts.values()),
        "recognized_doubt_rows": sum(doubt_counts.values()),
        "annotation_totals": annotation_totals,
        "annotation_count_differences": annotation_count_differences,
        "provenance_copies_checked": provenance_count,
        "stale_syntax_qa_scans": stale_qa,
        "errors": errors, "warnings": warnings,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
