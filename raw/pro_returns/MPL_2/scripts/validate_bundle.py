#!/usr/bin/env python3
"""Mechanical checks only; never opens images or the context archive.

Exit 0: no mechanical errors. Exit 1: one or more errors.
Missing unfinished deliverables are allowed with --partial.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
import re
import sys


EXPECTED_SCANS = tuple(n for n in range(2, 46) if n not in (6, 27, 31))
HEADERS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
           "first_words_or_objects", "transcribed"]
KINDS = {"text", "display", "diagram", "drawing", "margin note",
         "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
TIME_FORMAT = "%Y-%m-%d %H:%M:%S UTC"
TIME_RE = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"
HASH_RE = r"[0-9a-fA-F]{64}"


def visible_tex(source: str) -> tuple[str, list[str]]:
    """Remove unescaped comments and check braces, preserving line positions.

    TeX control symbols such as \\{, \\%, and \\\\ consume their next
    character; their braces/comment markers are consequently not structural.
    This is lexical validation, not a TeX interpreter.
    """
    out: list[str] = []
    stack: list[tuple[int, int]] = []
    errors: list[str] = []
    i, line, column = 0, 1, 1
    while i < len(source):
        ch = source[i]
        if ch == "\\" and i + 1 < len(source):
            nxt = source[i + 1]
            if not nxt.isalpha():
                out.extend((ch, nxt))
                i += 2
                if nxt == "\n":
                    line, column = line + 1, 1
                else:
                    column += 2
                continue
        if ch == "%":
            end = source.find("\n", i)
            if end == -1:
                out.extend(" " * (len(source) - i))
                break
            out.extend(" " * (end - i))
            column += end - i
            i = end
            continue
        if ch == "{":
            stack.append((line, column))
        elif ch == "}":
            if stack:
                stack.pop()
            else:
                errors.append(f"unmatched closing brace at line {line}, column {column}")
        out.append(ch)
        if ch == "\n":
            line, column = line + 1, 1
        else:
            column += 1
        i += 1
    errors.extend(f"unclosed opening brace at line {ln}, column {col}"
                  for ln, col in stack)
    return "".join(out), errors


def command_matches(source: str, name: str) -> list[re.Match[str]]:
    # The preceding-backslash guard suffices for ordinary fragment macros.
    return list(re.finditer(r"(?<!\\)\\" + re.escape(name)
                            + r"\s*\{([^{}]*)\}", source))


def check_bundle(root: Path, partial: bool) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    pages: dict[int, tuple[Path, str]] = {}
    expected_paths = {f"MPL_2_2_scan{scan:03d}.tex": scan
                      for scan in EXPECTED_SCANS}

    for path in sorted((root / "pages").glob("*.tex")):
        if path.name not in expected_paths:
            errors.append(f"Unexpected page filename: pages/{path.name}")
            continue
        scan = expected_paths[path.name]
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read pages/{path.name}: {exc}")
            continue
        pages[scan] = (path, source)
        clean, brace_errors = visible_tex(source)
        errors.extend(f"pages/{path.name}: {msg}" for msg in brace_errors)
        marks = command_matches(clean, "scanpage")
        if len(marks) != 1 or marks[0].group(1).strip() != str(scan):
            errors.append(f"pages/{path.name}: expected exactly one \\scanpage{{{scan}}}")
        cotes = command_matches(clean, "cotefile")
        if scan == EXPECTED_SCANS[0]:
            if len(cotes) != 1 or cotes[0].group(1).strip() != "2":
                errors.append(f"pages/{path.name}: expected exactly one \\cotefile{{2}}")
            elif not re.match(r"\s*\\cotefile\s*\{2\}\s*\\scanpage\s*\{2\}", clean):
                errors.append(f"pages/{path.name}: first content must be \\cotefile{{2}} then \\scanpage{{2}}")
        elif cotes:
            errors.append(f"pages/{path.name}: unexpected repeated \\cotefile")
        forbidden = re.findall(
            r"(?<!\\)\\(?:documentclass|usepackage|includegraphics\*?|graphicspath|"
            r"includepdf|include|input)\b|(?<!\\)\\(?:begin|end)\s*\{document\}", clean)
        if forbidden:
            errors.append(f"pages/{path.name}: forbidden preamble/document/image/external-input command(s): "
                          + ", ".join(sorted(set(forbidden))))

    missing = sorted(set(EXPECTED_SCANS) - set(pages))
    if missing and not partial:
        errors.append("Missing page files: " + ", ".join(f"{n:03d}" for n in missing))
    if pages and list(sorted(pages)) != list(EXPECTED_SCANS[:len(pages)]):
        errors.append("Present page files do not form a sequential prefix of the required scan order")

    combined_path = root / "MPL_2_transcription.tex"
    if combined_path.exists():
        combined = combined_path.read_text(encoding="utf-8")
        cursor = 0
        for scan, (_, source) in sorted(pages.items()):
            while cursor < len(combined) and combined[cursor].isspace():
                cursor += 1
            block = source.strip()
            if not combined.startswith(block, cursor):
                errors.append(f"Combined fragment differs from page file, or is out of order, at scan {scan:03d}")
                break
            cursor += len(block)
        else:
            if combined[cursor:].strip():
                errors.append("Combined fragment has unmatched content beyond the page files")
        clean, brace_errors = visible_tex(combined)
        errors.extend(f"MPL_2_transcription.tex: {msg}" for msg in brace_errors)
        combined_scans = [m.group(1).strip() for m in command_matches(clean, "scanpage")]
        if combined_scans != [str(scan) for scan in sorted(pages)]:
            errors.append("Combined fragment scan markers differ from the ordered page-file set")
        if pages and not re.match(r"\s*\\cotefile\s*\{2\}\s*\\scanpage\s*\{2\}", clean):
            errors.append("Combined fragment must start with \\cotefile{2} and \\scanpage{2}")
    elif not partial:
        errors.append("Missing MPL_2_transcription.tex")

    inventory_path = root / "MPL_2_inventory.csv"
    inventory_counts: Counter[int] = Counter()
    element_keys: set[tuple[int, str]] = set()
    if inventory_path.exists():
        with inventory_path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != HEADERS:
                errors.append("Inventory columns/order do not match the required schema")
            else:
                for row_number, row in enumerate(reader, start=2):
                    prefix = f"Inventory row {row_number}"
                    if None in row or any(row.get(key) is None for key in HEADERS):
                        errors.append(f"{prefix}: malformed CSV column count")
                        continue
                    for key in HEADERS:
                        if not row[key].strip():
                            errors.append(f"{prefix}: empty {key}")
                    try:
                        scan = int(row["scan"])
                    except ValueError:
                        errors.append(f"{prefix}: scan is not an integer")
                        continue
                    inventory_counts[scan] += 1
                    if row["cote"] != "2" or scan not in EXPECTED_SCANS:
                        errors.append(f"{prefix}: invalid cote/scan")
                    if scan not in pages:
                        errors.append(f"{prefix}: no matching page file for scan {scan:03d}")
                    if row["sheet_kind"] not in SHEET_KINDS:
                        errors.append(f"{prefix}: invalid sheet_kind")
                    if row["kind"] not in KINDS:
                        errors.append(f"{prefix}: invalid element kind")
                    if row["transcribed"] != "yes":
                        errors.append(f"{prefix}: transcribed must be exactly yes")
                    key = (scan, row["element"])
                    if key in element_keys:
                        errors.append(f"{prefix}: repeated element identifier within scan")
                    element_keys.add(key)
        for scan in pages:
            if not inventory_counts[scan]:
                errors.append(f"No inventory rows for scan {scan:03d}")
    elif not partial:
        errors.append("Missing MPL_2_inventory.csv")

    log_path = root / "progress.log"
    if log_path.exists():
        log = log_path.read_text(encoding="utf-8")
        lines = log.splitlines()
        try:
            datetime.strptime(lines[0], TIME_FORMAT)
        except (IndexError, ValueError):
            errors.append("progress.log first line must be the starting UTC timestamp")
        done = re.findall(r"^2 scan (\d{3}) done (" + TIME_RE + r")$", log, re.M)
        done_scans = [int(scan) for scan, _ in done]
        if done_scans != sorted(pages):
            errors.append("Page-done log entries do not equal the ordered page-file set")
        audits = re.findall(r"^scan (\d{3}) audited (" + TIME_RE + r")$", log, re.M)
        freezes = re.findall(r"^transcription frozen (" + TIME_RE + r")$", log, re.M)
        contexts = re.findall(r"^context opened (" + TIME_RE + r")$", log, re.M)
        if contexts and not freezes:
            errors.append("Context-opened log entry exists without a transcription freeze")
        if len(freezes) > 1:
            errors.append("Multiple transcription-frozen entries")
        if freezes:
            freeze = freezes[0]
            audit_scans = [int(scan) for scan, _ in audits]
            if audit_scans != list(EXPECTED_SCANS):
                errors.append("Frozen transcription requires one audit per scan in order")
            if any(timestamp > freeze for _, timestamp in audits):
                errors.append("An audit timestamp is later than the freeze timestamp")
            if any(timestamp < freeze for timestamp in contexts):
                errors.append("A context-opened timestamp precedes the freeze timestamp")
            hashes: dict[str, str] = {}
            for line in lines:
                # Canonical: sha256 HEX relative/path ; also accepts sha256sum form.
                match = re.fullmatch(r"(?:sha256\s+)?(" + HASH_RE + r")\s+[*]?(.+)", line, re.I)
                if match:
                    digest, filename = match.groups()
                else:
                    match = re.fullmatch(r"(?:sha256|SHA-256)\s+(.+?)\s+(" + HASH_RE + r")", line, re.I)
                    if not match:
                        continue
                    filename, digest = match.groups()
                hashes[filename.removeprefix("./")] = digest.lower()
            targets = [f"pages/MPL_2_2_scan{scan:03d}.tex" for scan in EXPECTED_SCANS]
            targets.append("MPL_2_transcription.tex")
            for relative in targets:
                digest = hashes.get(relative)
                if digest is None:
                    errors.append(f"No recognized frozen SHA-256 record for {relative}")
                elif not (root / relative).is_file():
                    errors.append(f"Frozen file is missing: {relative}")
                elif hashlib.sha256((root / relative).read_bytes()).hexdigest() != digest:
                    errors.append(f"Frozen SHA-256 mismatch: {relative}")
            if not re.search(r"hashes unchanged", log, re.I):
                warnings.append("No final 'hashes unchanged' statement found in progress.log")
        elif not partial:
            warnings.append("No freeze yet; audit and hash checks have not run")
    elif not partial:
        errors.append("Missing progress.log")

    if not partial:
        for filename in ("MPL_2_doubts.md", "MPL_2_notes.md"):
            if not (root / filename).is_file():
                errors.append(f"Missing {filename}")

    return {"ok": not errors, "mode": "partial" if partial else "complete",
            "pages_present": len(pages), "pages_expected": len(EXPECTED_SCANS),
            "inventory_rows": sum(inventory_counts.values()),
            "errors": errors, "warnings": warnings,
            "scope": "Mechanical structure only; no image reading or content/accuracy validation."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true", help="Allow unfinished/missing deliverables")
    parser.add_argument("--json", action="store_true", help="Print a machine-readable report")
    args = parser.parse_args()
    result = check_bundle(args.root, args.partial)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Mechanical validation: {'PASS' if result['ok'] else 'FAIL'} ({result['mode']})")
        print(f"Pages: {result['pages_present']}/{result['pages_expected']}; inventory rows: {result['inventory_rows']}")
        for error in result["errors"]:
            print(f"ERROR: {error}")
        for warning in result["warnings"]:
            print(f"WARNING: {warning}")
        print(result["scope"])
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
