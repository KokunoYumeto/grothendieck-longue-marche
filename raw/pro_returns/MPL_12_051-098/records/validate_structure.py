#!/usr/bin/env python3
"""Read-only structural checks for this transcription package; no image/OCR access.

Use --partial during work.  By default require the complete 39-page package.
Use --emit-hashes to print a JSON path -> SHA-256 manifest for freezing.
Use --hash-manifest PATH to verify that manifest after research work.
This script cannot establish whether a reading or an inventory element is accurate.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

PREFIX = "MPL_12_051-098"
OMITTED = {66, 68, 69, 70, 81, 83, 85, 97, 98}
EXPECTED = [n for n in range(51, 99) if n not in OMITTED]
STATE_MACROS = {
    "cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
    "uline", "uuline", "diagram", "figure", "unsure", "illegible",
}
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position", "first_words_or_objects", "transcribed"]
FORBIDDEN = {"documentclass", "usepackage", "newcommand", "renewcommand", "providecommand", "def", "input", "include", "includegraphics"}


def without_comments(text: str) -> str:
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in text.splitlines())


def brace_errors(text: str) -> list[str]:
    depth = 0
    errors = []
    for i, char in enumerate(text):
        slash_count = 0
        j = i - 1
        while j >= 0 and text[j] == "\\":
            slash_count += 1
            j -= 1
        if slash_count % 2:
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                errors.append(f"unmatched closing brace near character {i}")
                depth = 0
    if depth:
        errors.append(f"{depth} unclosed brace(s)")
    return errors


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true")
    parser.add_argument("--inventory", type=Path, help="Check a separate inventory candidate without changing the current inventory")
    parser.add_argument("--hash-manifest", type=Path)
    parser.add_argument("--emit-hashes", action="store_true")
    args = parser.parse_args()
    base = args.base.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    files = sorted((base / "pages").glob(f"{PREFIX}_12_scan*.tex"))
    combined = base / f"{PREFIX}_transcription.tex"
    relevant = files + ([combined] if combined.exists() else [])
    hashes = {str(p.relative_to(base)): digest(p) for p in relevant}
    if args.emit_hashes:
        print(json.dumps(hashes, indent=2, sort_keys=True))
        return 0

    pages: dict[int, str] = {}
    commands: set[str] = set()
    state_counts = {name: 0 for name in sorted(STATE_MACROS)}
    for path in files:
        match = re.fullmatch(rf"{PREFIX}_12_scan(\d{{3}})\.tex", path.name)
        if not match:
            errors.append(f"unexpected page filename: {path.name}")
            continue
        number = int(match.group(1))
        text = path.read_text(encoding="utf-8")
        if number in pages:
            errors.append(f"duplicate scan: {number}")
        pages[number] = text
        clean = without_comments(text)
        markers = re.findall(r"\\scanpage\s*\{(\d+)\}", clean)
        if markers != [str(number)]:
            errors.append(f"{path.name}: scanpage markers are {markers!r}")
        cotes = re.findall(r"\\cotefile\s*\{([^}]*)\}", clean)
        if any(cote != "12" for cote in cotes):
            errors.append(f"{path.name}: unexpected cote markers {cotes!r}")
        found = set(re.findall(r"\\([A-Za-z]+)", clean))
        commands.update(found)
        if found & FORBIDDEN:
            errors.append(f"{path.name}: forbidden preamble/input commands {sorted(found & FORBIDDEN)}")
        for state in STATE_MACROS:
            state_counts[state] += len(re.findall(r"\\" + state + r"\b", clean))
        for problem in brace_errors(clean):
            errors.append(f"{path.name}: {problem}")
    missing = sorted(set(EXPECTED) - pages.keys())
    extra = sorted(pages.keys() - set(EXPECTED))
    if missing:
        (warnings if args.partial else errors).append(f"missing scans: {missing}")
    if extra:
        errors.append(f"unexpected scans: {extra}")
    if pages and sorted(pages) != [n for n in EXPECTED if n in pages]:
        errors.append("page order differs from supplied scan order")

    concatenation = None
    if combined.exists():
        text = combined.read_text(encoding="utf-8")
        clean = without_comments(text).lstrip()
        if not re.match(r"\\cotefile\{12\}\s*\\scanpage\{51\}", clean):
            errors.append("combined fragment does not start with cotefile{12}, scanpage{51}")
        actual_order = [int(n) for n in re.findall(r"\\scanpage\s*\{(\d+)\}", clean)]
        if actual_order != sorted(pages):
            errors.append(f"combined scan order {actual_order} differs from page files")
        ordered = [pages[n] for n in sorted(pages)]
        for separator in ("", "\n", "\n\n"):
            if text == separator.join(ordered):
                concatenation = repr(separator)
                break
        if concatenation is None:
            errors.append("combined transcription is not an exact concatenation of page files (0, 1, or 2 newline separators)")
    elif not args.partial:
        errors.append("combined transcription is missing")

    inventory_path = args.inventory or base / f"{PREFIX}_inventory.csv"
    row_counts: dict[int, int] = {}
    sheet_kinds: dict[int, set[str]] = {}
    keys: set[tuple[int, str]] = set()
    inventory_rows = 0
    if inventory_path.exists():
        with inventory_path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != COLUMNS:
                errors.append(f"inventory columns differ: {reader.fieldnames!r}")
            for i, row in enumerate(reader, start=2):
                inventory_rows += 1
                try:
                    scan = int(row.get("scan", ""))
                except (TypeError, ValueError):
                    errors.append(f"inventory row {i}: invalid scan")
                    continue
                row_counts[scan] = row_counts.get(scan, 0) + 1
                sheet = row.get("sheet_kind", "")
                sheet_kinds.setdefault(scan, set()).add(sheet)
                if row.get("cote") != "12":
                    errors.append(f"inventory row {i}: cote must be 12")
                if scan not in pages:
                    errors.append(f"inventory row {i}: no saved page for scan {scan}")
                if sheet not in SHEET_KINDS:
                    errors.append(f"inventory row {i}: invalid sheet_kind {sheet!r}")
                if row.get("kind") not in ELEMENT_KINDS:
                    errors.append(f"inventory row {i}: invalid kind {row.get('kind')!r}")
                if row.get("transcribed") != "yes":
                    errors.append(f"inventory row {i}: transcribed is not yes")
                key = (scan, row.get("element", ""))
                if not key[1] or key in keys:
                    errors.append(f"inventory row {i}: missing/duplicate element id {key!r}")
                keys.add(key)
        for scan in pages:
            if not row_counts.get(scan):
                errors.append(f"scan {scan}: no inventory elements")
        for scan, kinds in sheet_kinds.items():
            if len(kinds) > 1:
                errors.append(f"scan {scan}: inconsistent sheet_kind {sorted(kinds)}")
    elif pages or not args.partial:
        errors.append("inventory file is missing")

    frozen_checks = 0
    if args.hash_manifest:
        frozen = json.loads(args.hash_manifest.read_text(encoding="utf-8"))
        if not isinstance(frozen, dict):
            errors.append("hash manifest must be a JSON object mapping relative paths to SHA-256 values")
        else:
            if set(frozen) != set(hashes):
                errors.append("hash manifest file set differs from pages plus combined transcription")
            for name, expected in frozen.items():
                if hashes.get(name) != expected:
                    errors.append(f"frozen hash mismatch: {name}")
                else:
                    frozen_checks += 1

    if not args.partial:
        for name in (f"{PREFIX}_doubts.md", f"{PREFIX}_notes.md", "progress.log"):
            if not (base / name).is_file():
                errors.append(f"required deliverable missing: {name}")
    report = {
        "ok": not errors,
        "mode": "partial" if args.partial else "complete",
        "expected_page_count": len(EXPECTED),
        "actual_page_count": len(pages),
        "scan_order": sorted(pages),
        "inventory_rows": inventory_rows,
        "inventory_rows_by_scan": row_counts,
        "combined_exact_separator": concatenation,
        "state_macro_counts": state_counts,
        "other_tex_commands_for_manual_review": sorted(commands - STATE_MACROS),
        "frozen_hashes_verified": frozen_checks,
        "errors": errors,
        "warnings": warnings,
        "limitation": "Structural checks only; no claim of transcription accuracy or inventory completeness.",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
