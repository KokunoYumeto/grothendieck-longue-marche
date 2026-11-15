#!/usr/bin/env python3
"""Structural checks for the completed MPL_14_087-132 transcription package.

This tool does not perform OCR, interpret a reading, inspect source images, or
read the supplied context archive. Run it only when the transcription is ready.

Canonical assembly (the default --separator raw):
  * Read the expected page files in numerical scan order as UTF-8 bytes.
  * Preserve their bytes exactly and concatenate them, without an added separator.
  * If the first page has no \\cotefile marker, prepend b'\\cotefile{14}\\n'.
  * Otherwise the sole \\cotefile{14} must already occur at the first page's start.
Use --separator newline if one extra LF was placed between each pair of files.
There is no trimming or newline normalization in the byte comparison.

Optional freeze manifest: records/frozen_hashes.json, a JSON object mapping
package-relative filenames to 64-character SHA-256 hex digests. A wrapper of
the form {"sha256": {path: digest, ...}} or {"files": {path: digest, ...}}
is also accepted. All page files and the combined transcription must be covered.

Exit status: 0 = no structural errors; 1 = structural errors; 2 = usage error.
Warnings flag possible TeX syntax issues and require human review. Passing this
validator does not establish transcription accuracy or inventory completeness.
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import sys


PREFIX = "MPL_14_087-132"
EXPECTED_SCANS = tuple(n for n in range(87, 133) if n not in {105, 110, 119, 125, 130})
COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position", "first_words_or_objects", "transcribed"]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
PAGE_NAME = re.compile(r"MPL_14_087-132_14_scan(\d{3})\.tex\Z")
COTE = re.compile(r"\\cotefile\s*\{([^{}]*)\}")
SCAN = re.compile(r"\\scanpage\s*\{([^{}]*)\}")
FORBIDDEN = re.compile(r"\\(?:documentclass|usepackage|includegraphics|include|input|includepdf)\b|\\begin\s*\{document\}")


def uncomment(source: str) -> str:
    """Remove unescaped TeX comments while retaining line numbers."""
    output = []
    for line in source.splitlines(keepends=True):
        cut = None
        for i, char in enumerate(line):
            if char != "%":
                continue
            previous_slashes = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                previous_slashes += 1
                j -= 1
            if previous_slashes % 2 == 0:
                cut = i
                break
        output.append(line if cut is None else line[:cut] + ("\n" if line.endswith("\n") else ""))
    return "".join(output)


def brace_issues(source: str) -> list[dict]:
    """Conservative brace check; ignore escaped characters and \\verb bodies."""
    source = uncomment(source)
    stack: list[int] = []
    issues: list[dict] = []
    line = 1
    i = 0
    while i < len(source):
        char = source[i]
        if char == "\n":
            line += 1
        if char == "\\":
            verb = re.match(r"\\verb\*?([^A-Za-z\s])", source[i:])
            if verb:
                delimiter = verb.group(1)
                body_start = i + len(verb.group(0))
                end = source.find(delimiter, body_start)
                if end < 0:
                    issues.append({"line": line, "issue": "Unterminated verbatim command"})
                    i = body_start
                    continue
                line += source[i:end + 1].count("\n")
                i = end + 1
                continue
            if i + 1 < len(source) and not source[i + 1].isalpha():
                i += 2
                continue
        elif char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                issues.append({"line": line, "issue": "Unmatched closing brace"})
        i += 1
    issues.extend({"line": n, "issue": "Unmatched opening brace"} for n in stack)
    return issues


def environment_issues(source: str) -> list[dict]:
    source = uncomment(source)
    stack: list[tuple[str, int]] = []
    issues: list[dict] = []
    for m in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", source):
        action, name = m.groups()
        line = source.count("\n", 0, m.start()) + 1
        if action == "begin":
            stack.append((name, line))
        elif not stack:
            issues.append({"line": line, "issue": f"Unmatched end of environment {name}"})
        elif stack[-1][0] != name:
            issues.append({"line": line, "issue": f"Environment {name} ended while {stack[-1][0]} is open"})
        else:
            stack.pop()
    issues.extend({"line": line, "issue": f"Unclosed environment {name}"} for name, line in stack)
    return issues


def doubt_occurrences(source: str) -> list[dict]:
    """Return each explicit doubt and its source-file line, without judging it."""
    clean = uncomment(source)
    result: list[dict] = []
    for m in re.finditer(r"\\(unsure|illegible)\s*\{", clean):
        depth = 1
        i = m.end()
        start = i
        while i < len(clean) and depth:
            if clean[i] == "\\" and i + 1 < len(clean):
                i += 2
                continue
            if clean[i] == "{":
                depth += 1
            elif clean[i] == "}":
                depth -= 1
            i += 1
        result.append({"line": clean.count("\n", 0, m.start()) + 1,
                       "macro": m.group(1),
                       "argument": clean[start:i - 1] if not depth else clean[start:],
                       "closed": depth == 0})
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1],
                        help="Package root (default: parent of this script's scripts directory)")
    parser.add_argument("--separator", choices=("raw", "newline"), default="raw",
                        help="Bytes inserted between page fragments for exact combined-file comparison")
    parser.add_argument("--json-output", type=Path, help="Write detailed results and doubt locations as JSON")
    parser.add_argument("--require-frozen", action="store_true", help="Fail if the freeze manifest does not exist")
    args = parser.parse_args()
    root = args.root.resolve()
    report: dict = {"root": str(root), "expected_scans": list(EXPECTED_SCANS), "errors": [], "warnings": [],
                    "page_statistics": [], "doubts": [], "freeze": {"present": False}}

    def error(code: str, detail: str, file: str | None = None) -> None:
        report["errors"].append({"code": code, "detail": detail, **({"file": file} if file else {})})

    def warning(code: str, detail: str, file: str | None = None, line: int | None = None) -> None:
        report["warnings"].append({"code": code, "detail": detail,
                                   **({"file": file} if file else {}), **({"line": line} if line else {})})

    page_paths = {n: root / "pages" / f"{PREFIX}_14_scan{n:03}.tex" for n in EXPECTED_SCANS}
    found_paths = sorted((root / "pages").glob("*.tex"))
    expected_names = {p.name for p in page_paths.values()}
    for path in found_paths:
        if path.name not in expected_names:
            error("unexpected_page", "Unexpected page fragment in pages directory", str(path.relative_to(root)))
    page_data: dict[int, bytes] = {}
    page_text: dict[int, str] = {}
    for scan, path in page_paths.items():
        relative = str(path.relative_to(root))
        if not path.is_file():
            error("missing_page", f"Missing scan {scan}", relative)
            continue
        page_data[scan] = path.read_bytes()
        try:
            text = page_data[scan].decode("utf-8")
        except UnicodeDecodeError as exc:
            error("encoding", f"Invalid UTF-8: {exc}", relative)
            continue
        page_text[scan] = text
        clean = uncomment(text)
        markers = SCAN.findall(clean)
        if markers != [str(scan)]:
            error("scan_marker", f"Expected one \\scanpage{{{scan}}}; found {markers!r}", relative)
        cotes = COTE.findall(clean)
        if scan == EXPECTED_SCANS[0]:
            if cotes not in ([], ["14"]):
                error("cote_marker", f"First page permits zero or one cote 14 marker; found {cotes!r}", relative)
            if cotes and not clean.lstrip().startswith("\\cotefile{14}"):
                error("cote_position", "The cote marker must start the first page if present", relative)
        elif cotes:
            error("cote_marker", "A later page repeats the cote marker", relative)
        if not clean.lstrip().startswith(("\\scanpage{" + str(scan) + "}", "\\cotefile{14}")):
            error("page_start", "Page does not start with its expected page or initial cote marker", relative)
        for issue in brace_issues(text) + environment_issues(text):
            warning("potential_tex_structure", issue["issue"], relative, issue["line"])
        doubts = doubt_occurrences(text)
        report["doubts"].extend({"file": relative, "scan": scan, **item} for item in doubts)
        counts = collections.Counter(item["macro"] for item in doubts)
        report["page_statistics"].append({"scan": scan, "bytes": len(page_data[scan]),
                                           "lines": len(text.splitlines()), "doubt_counts": dict(counts)})

    combined_path = root / f"{PREFIX}_transcription.tex"
    combined_relative = combined_path.name
    if not combined_path.is_file():
        error("missing_combined", "Missing combined transcription", combined_relative)
    else:
        combined_data = combined_path.read_bytes()
        try:
            combined = combined_data.decode("utf-8")
        except UnicodeDecodeError as exc:
            error("encoding", f"Invalid UTF-8: {exc}", combined_relative)
        else:
            clean = uncomment(combined)
            if not clean.lstrip().startswith("\\cotefile{14}"):
                error("combined_start", "Combined transcription must start with \\cotefile{14}", combined_relative)
            if COTE.findall(clean) != ["14"]:
                error("combined_cote", "Combined transcription must contain exactly one cote 14 marker", combined_relative)
            if SCAN.findall(clean) != [str(n) for n in EXPECTED_SCANS]:
                error("combined_scans", "Combined scan markers differ from the required scan order", combined_relative)
            for m in FORBIDDEN.finditer(clean):
                error("forbidden_fragment_command", f"Found forbidden command {m.group(0)!r} at line "
                      f"{clean.count(chr(10), 0, m.start()) + 1}", combined_relative)
            if len(page_data) == len(EXPECTED_SCANS) and len(page_text) == len(EXPECTED_SCANS):
                separator = b"" if args.separator == "raw" else b"\n"
                expected = separator.join(page_data[n] for n in EXPECTED_SCANS)
                if not COTE.search(uncomment(page_text[EXPECTED_SCANS[0]])):
                    expected = b"\\cotefile{14}\n" + expected
                if combined_data != expected:
                    at = next((i for i, (a, b) in enumerate(zip(combined_data, expected)) if a != b),
                              min(len(combined_data), len(expected)))
                    error("assembly_mismatch", f"Combined file differs from exact page assembly at byte {at}; "
                          f"actual length {len(combined_data)}, expected {len(expected)} (separator={args.separator})",
                          combined_relative)

    inventory_path = root / f"{PREFIX}_inventory.csv"
    inventory_scans: set[int] = set()
    inventory_count = 0
    keys: set[tuple[int, str]] = set()
    if not inventory_path.is_file():
        error("missing_inventory", "Missing inventory", inventory_path.name)
    else:
        try:
            with inventory_path.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                if reader.fieldnames != COLUMNS:
                    error("inventory_columns", f"Expected columns {COLUMNS!r}; found {reader.fieldnames!r}", inventory_path.name)
                for row_number, row in enumerate(reader, 2):
                    inventory_count += 1
                    if None in row:
                        error("inventory_row", f"Row {row_number} has excess cells", inventory_path.name)
                    if str(row.get("cote", "")).strip() != "14":
                        error("inventory_cote", f"Row {row_number} has an incorrect cote", inventory_path.name)
                    try:
                        scan = int(str(row.get("scan", "")).strip())
                    except (ValueError, TypeError):
                        error("inventory_scan", f"Row {row_number} has an invalid scan", inventory_path.name)
                        scan = -1
                    if scan not in EXPECTED_SCANS:
                        error("inventory_scan", f"Row {row_number} has unexpected scan {scan}", inventory_path.name)
                    else:
                        inventory_scans.add(scan)
                    if row.get("sheet_kind") not in SHEET_KINDS:
                        error("inventory_sheet_kind", f"Row {row_number} has invalid sheet_kind {row.get('sheet_kind')!r}", inventory_path.name)
                    if row.get("kind") not in KINDS:
                        error("inventory_kind", f"Row {row_number} has invalid kind {row.get('kind')!r}", inventory_path.name)
                    if row.get("transcribed") != "yes":
                        error("inventory_unfinished", f"Row {row_number} is not exactly transcribed=yes", inventory_path.name)
                    for column in ("element", "position", "first_words_or_objects"):
                        if not str(row.get(column) or "").strip():
                            error("inventory_empty", f"Row {row_number} has empty {column}", inventory_path.name)
                    key = (scan, str(row.get("element", "")))
                    if key in keys:
                        warning("inventory_duplicate_element", f"Row {row_number} repeats element {key!r}", inventory_path.name)
                    keys.add(key)
        except (OSError, UnicodeError, csv.Error) as exc:
            error("inventory_read", str(exc), inventory_path.name)
        for scan in EXPECTED_SCANS:
            if scan not in inventory_scans:
                error("inventory_missing_scan", f"No inventory rows for scan {scan}", inventory_path.name)
    report["inventory_rows"] = inventory_count

    manifest_path = root / "records" / "frozen_hashes.json"
    if manifest_path.is_file():
        report["freeze"]["present"] = True
        try:
            hashes = json.loads(manifest_path.read_text(encoding="utf-8"))
            if isinstance(hashes, dict) and isinstance(hashes.get("sha256"), dict):
                hashes = hashes["sha256"]
            elif isinstance(hashes, dict) and isinstance(hashes.get("files"), dict):
                hashes = hashes["files"]
            if not isinstance(hashes, dict):
                raise ValueError("Expected an object mapping relative paths to SHA-256 strings")
            required = {str(path.relative_to(root)) for path in page_paths.values()} | {combined_relative}
            for relative in sorted(required - set(hashes)):
                error("freeze_missing_hash", "Required transcription file has no frozen hash", relative)
            verified = 0
            for relative, digest in hashes.items():
                if not isinstance(relative, str) or not isinstance(digest, str) or not re.fullmatch(r"[0-9A-Fa-f]{64}", digest):
                    error("freeze_format", f"Invalid manifest entry for {relative!r}", str(manifest_path.relative_to(root)))
                    continue
                target = (root / relative).resolve()
                if not target.is_relative_to(root):
                    error("freeze_path", "Manifest path leaves the package root", relative)
                elif not target.is_file():
                    error("freeze_missing_file", "Frozen file is missing", relative)
                elif hashlib.sha256(target.read_bytes()).hexdigest() != digest.lower():
                    error("freeze_changed", "File no longer matches its frozen SHA-256", relative)
                else:
                    verified += 1
            report["freeze"]["hashes_verified"] = verified
        except (OSError, UnicodeError, ValueError, TypeError) as exc:
            error("freeze_manifest", str(exc), str(manifest_path.relative_to(root)))
    elif args.require_frozen:
        error("freeze_missing", "Frozen hash manifest is required but missing", str(manifest_path.relative_to(root)))

    report["summary"] = {"pages_found": len(page_data), "pages_required": len(EXPECTED_SCANS),
                         "inventory_rows": inventory_count, "explicit_doubts": len(report["doubts"]),
                         "errors": len(report["errors"]), "warnings": len(report["warnings"])}
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False))
    for level in ("errors", "warnings"):
        for item in report[level]:
            location = item.get("file", "")
            if "line" in item:
                location += f":{item['line']}"
            print(f"{level[:-1].upper()} [{item['code']}] {location}: {item['detail']}")
    if args.json_output:
        print(f"Detailed report: {args.json_output}")
    else:
        print("Use --json-output PATH to retain every explicit doubt and its source-file line.")
    print("Structural validation does not assess the manuscript readings or the completeness of visual inventories.")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
