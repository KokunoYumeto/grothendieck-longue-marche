#!/usr/bin/env python3
"""Structural validation only; this script cannot certify a visual transcription.

Usage: python scripts/validate_package.py [ROOT] [--draft] [--json] [--zip ARCHIVE]
The default ROOT is the directory containing this script's scripts/ folder.
No file is modified. No scan image or context archive is opened. Reports contain
locations and counts, never quotations from the transcription.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
from package_integrity import frozen_checks, zip_checks


PREFIX = "MPL_138_001-045"
SCANS = tuple(n for n in range(1, 46) if n != 24)
COLUMNS = (
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}


def uncomment(source: str) -> str:
    """Remove TeX comments, retaining newline positions and escaped percent signs."""
    output = []
    for line in source.splitlines(keepends=True):
        cut = len(line)
        for index, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut = index
                break
        output.append(line[:cut] + ("\n" if cut < len(line) and line.endswith("\n") else ""))
    return "".join(output)


def structural_tex_issues(source: str) -> list[tuple[str, int]]:
    """Conservative lexical checks; not a substitute for a TeX engine."""
    clean = uncomment(source)
    # Verbatim material is unusual here, but its punctuation is not TeX syntax.
    clean = re.sub(r"\\verb\*?([^A-Za-z\s])(.*?)\1", "", clean)
    issues = []
    stack = []
    line = 1
    index = 0
    while index < len(clean):
        char = clean[index]
        if char == "\n":
            line += 1
        elif char == "\\":
            if index + 1 < len(clean) and clean[index + 1] in "{}%\\":
                index += 1
        elif char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                issues.append(("Unmatched closing brace", line))
        index += 1
    issues.extend(("Unclosed opening brace", n) for n in stack)

    env_stack = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
        action, environment = match.groups()
        line = clean.count("\n", 0, match.start()) + 1
        if action == "begin":
            env_stack.append((environment, line))
        elif not env_stack:
            issues.append(("Environment closes without opening", line))
        elif env_stack[-1][0] != environment:
            issues.append(("Environment nesting mismatch", line))
        else:
            env_stack.pop()
    issues.extend(("Unclosed environment", n) for _, n in env_stack)
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--draft", action="store_true", help="Report unfinished audit/freeze gates as warnings.")
    parser.add_argument("--json", action="store_true", help="Print a JSON report instead of plain text.")
    parser.add_argument("--zip", type=Path, help="Also verify final ZIP membership and every member's bytes.")
    args = parser.parse_args()
    root = args.root.resolve()
    errors = []
    warnings = []
    stats = {"expected_pages": len(SCANS), "present_pages": 0, "inventory_rows": 0}

    def error(message: str) -> None:
        errors.append(message)

    def pending(message: str) -> None:
        (warnings if args.draft else errors).append(message)

    def read(path: Path) -> str | None:
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            error(f"{path.name}: cannot read UTF-8 ({type(exc).__name__}).")
            return None

    page_paths = [root / "pages" / f"{PREFIX}_138_scan{scan:03}.tex" for scan in SCANS]
    expected_names = {path.name for path in page_paths}
    actual_names = {path.name for path in (root / "pages").glob("*.tex")}
    for name in sorted(actual_names - expected_names):
        error(f"Unexpected page file: {name}.")
    pages = []
    macros = Counter()
    source_files = []
    for scan, path in zip(SCANS, page_paths):
        text = read(path)
        if text is None:
            continue
        stats["present_pages"] += 1
        pages.append(text)
        source_files.append(path)
        clean = uncomment(text)
        scan_tags = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if len(scan_tags) != 1 or int(scan_tags[0]) != scan:
            error(f"{path.name}: expected exactly one matching scanpage tag.")
        for issue, line in structural_tex_issues(text):
            error(f"{path.name}:{line}: {issue}.")
        macros.update(re.findall(r"\\(unsure|illegible|deleted|inserted|margin|diagram|figure)\b", clean))
        if re.search(r"\\(?:includegraphics|includepdf|pdfximage|epsfig|psfig|pgfimage)\b", clean):
            error(f"{path.name}: raster/image inclusion command detected.")
        if re.search(r"\\documentclass\b|\\begin\s*\{document\}", clean):
            error(f"{path.name}: document wrapper found in fragment.")
        if re.search(r"\\(?:input|include)\b", clean):
            warnings.append(f"{path.name}: external input command requires review.")
        if re.search(r"\bTODO\b|\bPLACEHOLDER\b|\b(?:diagram|drawing|figure|text)\s+(?:omitted|not transcribed)\b", clean, re.I):
            warnings.append(f"{path.name}: possible editorial placeholder requires manual review.")
    stats["macro_counts"] = dict(sorted(macros.items()))

    combined_path = root / f"{PREFIX}_transcription.tex"
    combined = read(combined_path)
    if combined is not None:
        source_files.append(combined_path)
        clean = uncomment(combined)
        cote_tags = re.findall(r"\\cotefile\s*\{\s*([^{}]+)\s*\}", clean)
        if cote_tags != ["138"]:
            error("Combined fragment: expected exactly one cotefile{138} tag.")
        if not re.match(r"\s*\\cotefile\s*\{138\}\s*\\scanpage\s*\{0*1\}", clean):
            error("Combined fragment: first commands must be cotefile{138} and scanpage{1}.")
        tags = [int(value) for value in re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)]
        if tags != list(SCANS):
            error("Combined fragment: scanpage sequence differs from expected 44 scans.")
        if len(pages) == len(SCANS):
            candidates = {separator.join(pages) for separator in ("", "\n", "\n\n")}
            if not re.search(r"\\cotefile\b", uncomment(pages[0])):
                candidates = {
                    "\\cotefile{138}" + separator + value
                    for value in candidates for separator in ("\n", "\n\n")
                }
            # Permit a final newline only; never normalize page contents.
            candidates |= {value + "\n" for value in tuple(candidates)}
            if combined not in candidates:
                error("Combined fragment is not an exact concatenation of page files (with optional blank seams).")
        for issue, line in structural_tex_issues(combined):
            error(f"{combined_path.name}:{line}: {issue}.")

    inventory = read(root / f"{PREFIX}_inventory.csv")
    if inventory is not None:
        try:
            reader = csv.DictReader(io.StringIO(inventory))
            if tuple(reader.fieldnames or ()) != COLUMNS:
                error("Inventory columns differ from the specified order and names.")
            covered = Counter()
            element_ids = set()
            kinds = Counter()
            for row_number, row in enumerate(reader, start=2):
                stats["inventory_rows"] += 1
                if None in row or any(value is None for value in row.values()):
                    error(f"Inventory row {row_number}: wrong number of CSV fields.")
                    continue
                try:
                    scan = int(row.get("scan", ""))
                except (TypeError, ValueError):
                    error(f"Inventory row {row_number}: invalid scan number.")
                    continue
                covered[scan] += 1
                if scan not in SCANS or row.get("cote") != "138":
                    error(f"Inventory row {row_number}: unexpected cote or scan.")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    error(f"Inventory row {row_number}: invalid sheet_kind.")
                if row.get("kind") not in ELEMENT_KINDS:
                    error(f"Inventory row {row_number}: invalid element kind.")
                kinds[row.get("kind") or ""] += 1
                if row.get("transcribed") != "yes":
                    error(f"Inventory row {row_number}: transcribed is not yes.")
                for field in ("element", "position", "first_words_or_objects"):
                    if not (row.get(field) or "").strip():
                        error(f"Inventory row {row_number}: empty {field}.")
                key = (scan, row.get("element"))
                if key in element_ids:
                    warnings.append(f"Inventory row {row_number}: repeated element identifier within scan.")
                element_ids.add(key)
            for scan in SCANS:
                if not covered[scan]:
                    error(f"Inventory: no element for scan {scan:03}.")
            stats["inventory_kind_counts"] = dict(sorted(kinds.items()))
        except csv.Error:
            error("Inventory cannot be parsed as CSV.")

    for suffix in ("doubts.md", "notes.md"):
        path = root / f"{PREFIX}_{suffix}"
        if not path.is_file() or not path.stat().st_size:
            pending(f"Missing or empty deliverable: {path.name}.")

    progress = read(root / "progress.log")
    if progress is not None:
        lines = progress.splitlines()
        if not lines or not re.search(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}.*(?:UTC|Z|\+00:00)", lines[0]):
            error("progress.log: first line must contain the initial UTC timestamp.")
        done_matches = list(re.finditer(r"(?m)^138\s+scan\s+(\d+)\s+done\b", progress))
        audit_matches = list(re.finditer(r"(?m)^(?:138\s+)?scan\s+(\d+)\s+audited\b", progress))
        done_sequence = [int(match.group(1)) for match in done_matches]
        audit_sequence = [int(match.group(1)) for match in audit_matches]
        done = set(done_sequence)
        audited = set(audit_sequence)
        if done_sequence != list(SCANS):
            error("progress.log: done records must list the 44 expected scans once and in order.")
        if audit_sequence != list(SCANS):
            pending("progress.log: audited records must list the 44 expected scans once and in order.")
        if done_matches and audit_matches and done_matches[-1].start() > audit_matches[0].start():
            error("progress.log: second-reading audit began before the final page's done record.")
        stats["done_records"] = len(done & set(SCANS))
        stats["audit_records"] = len(audited & set(SCANS))
        for scan in SCANS:
            if scan not in done:
                error(f"progress.log: missing done record for scan {scan:03}.")
            if scan not in audited:
                pending(f"progress.log: missing audited record for scan {scan:03}.")
        freeze = progress.find("transcription frozen")
        context = progress.find("context opened")
        if freeze < 0:
            pending("progress.log: missing transcription frozen record.")
        if context >= 0 and (freeze < 0 or context < freeze):
            error("progress.log: context opened precedes transcription frozen.")
        if context < 0:
            pending("progress.log: missing context opened record.")
        if freeze >= 0 and any(match.start() > freeze for match in audit_matches):
            error("progress.log: an audit record occurs after the transcription freeze.")
        if (root / "records" / "frozen.sha256").is_file():
            integrity = frozen_checks(root, progress)
            errors.extend(integrity["errors"])
            stats["matching_hash_files"] = integrity["frozen_hashes_verified"]
            stats["frozen_manifest_entries"] = integrity["manifest_entries"]
            stats["progress_frozen_hash_entries"] = integrity["progress_hash_entries"]
        else:
            pending("Missing records/frozen.sha256 manifest for the 45 frozen files.")
        final_verifications = list(re.finditer(
            r"(?im)^.*(?:hashes[^\n]*(?:unchanged|verified)|(?:unchanged|verified)[^\n]*hashes).*$", progress
        ))
        if not any(match.start() > max(freeze, context) for match in final_verifications):
            pending("progress.log: no final unchanged-hashes verification statement after freeze/context opening.")

    if args.zip:
        archive_report = zip_checks(root, args.zip.resolve())
        errors.extend(archive_report["errors"])
        stats["zip_members_verified"] = archive_report["zip_members_verified"]
        stats["zip_frozen_hashes_verified"] = archive_report["zip_frozen_hashes_verified"]
        stats["excluded_work_files"] = archive_report["excluded_work_files"]

    warnings.append(
        "Structural checks do not establish visual completeness, reading accuracy, correct attachment of insertions, "
        "or the absence of every possible descriptive substitution; those require the requested page-by-page audit."
    )
    report = {"ok": not errors, "mode": "draft" if args.draft else "final", "stats": stats,
              "errors": errors, "warnings": warnings}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("Structural validation:", "PASS" if not errors else "FAIL")
        print(json.dumps(stats, ensure_ascii=False, sort_keys=True))
        for item in errors:
            print("ERROR:", item)
        for item in warnings:
            print("WARNING:", item)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
