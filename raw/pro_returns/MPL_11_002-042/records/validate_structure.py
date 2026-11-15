#!/usr/bin/env python3
"""Validate the transcription deliverable's structure using the standard library.

Usage:
    python records/validate_structure.py .
    python records/validate_structure.py /path/to/deliverable --inventory inventory.csv

This performs structural checks only. It does not run OCR, interpret mathematics,
or establish the accuracy or completeness of the manuscript transcription.
"""

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path


PREFIX = "MPL_11_002-042"
SCANS = tuple(range(3, 33)) + tuple(range(34, 43))
HEADERS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]


def without_comments(text):
    """Remove unescaped TeX comments while retaining line breaks."""
    result = []
    index = 0
    while index < len(text):
        char = text[index]
        if char == "\\" and index + 1 < len(text):
            result.append(text[index:index + 2])
            index += 2
        elif char == "%":
            newline = text.find("\n", index)
            if newline == -1:
                break
            index = newline
        else:
            result.append(char)
            index += 1
    return "".join(result)


def commands(text):
    """Yield (control-word name, end offset), respecting escaped backslashes."""
    index = 0
    while index < len(text):
        if text[index] != "\\":
            index += 1
            continue
        index += 1
        start = index
        while index < len(text) and text[index] in (
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@"
        ):
            index += 1
        if index > start:
            yield text[start:index], index
        else:
            index += 1


def integer_argument(text, offset):
    match = re.match(r"\s*\{\s*([0-9]+)\s*\}", text[offset:])
    return int(match.group(1)) if match else None


def brace_errors(text):
    """Return unmatched brace positions, ignoring TeX escaped characters."""
    opening = []
    closing = []
    index = 0
    line = 1
    column = 1
    while index < len(text):
        char = text[index]
        if char == "\\" and index + 1 < len(text):
            pair = text[index:index + 2]
            if "\n" in pair:
                line += 1
                column = 1
            else:
                column += 2
            index += 2
            continue
        if char == "{":
            opening.append((line, column))
        elif char == "}":
            if opening:
                opening.pop()
            else:
                closing.append((line, column))
        if char == "\n":
            line += 1
            column = 1
        else:
            column += 1
        index += 1
    return opening, closing


def find_inventory(root, supplied, errors):
    if supplied:
        candidate = Path(supplied)
        return candidate if candidate.is_absolute() else root / candidate
    matches = []
    for candidate in sorted(root.rglob("*.csv")):
        try:
            with candidate.open("r", encoding="utf-8-sig", newline="") as handle:
                if next(csv.reader(handle), None) == HEADERS:
                    matches.append(candidate)
        except (OSError, UnicodeError, csv.Error):
            continue
    if len(matches) != 1:
        errors.append(
            "Expected exactly one inventory CSV with the required ordered header; "
            f"found {len(matches)}. Supply --inventory to select a file."
        )
        return None
    return matches[0]


def check_inventory(path, errors):
    seen = set()
    rows = 0
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != HEADERS:
                errors.append(f"{path.name}: expected CSV header {HEADERS!r}.")
                return 0
            for row in reader:
                rows += 1
                location = f"{path.name}, CSV line {reader.line_num}"
                if None in row or any(value is None for value in row.values()):
                    errors.append(f"{location}: row does not have exactly eight fields.")
                    continue
                # Accept numeric scan identifiers or a literal scanNNN identifier.
                match = re.fullmatch(r"(?:scan)?([0-9]+)", row["scan"])
                if not match:
                    errors.append(f"{location}: invalid scan value {row['scan']!r}.")
                else:
                    scan = int(match.group(1))
                    if scan not in SCANS:
                        errors.append(f"{location}: unexpected scan {scan:03d}.")
                    else:
                        seen.add(scan)
                if row["transcribed"] != "yes":
                    errors.append(f"{location}: transcribed must be exactly 'yes'.")
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"Cannot read inventory {path}: {exc}")
        return rows
    missing = sorted(set(SCANS) - seen)
    if missing:
        errors.append("Inventory has no row for scans: " + ", ".join(
            f"{scan:03d}" for scan in missing
        ))
    return rows


def manifest_entries(payload):
    """Accept a path-to-digest object or a files list/object wrapper."""
    if isinstance(payload, dict) and "files" in payload:
        payload = payload["files"]
    if isinstance(payload, dict):
        entries = []
        for path, value in payload.items():
            digest = value.get("sha256") if isinstance(value, dict) else value
            entries.append((path, digest))
        return entries
    if isinstance(payload, list):
        entries = []
        for entry in payload:
            if not isinstance(entry, dict) or "path" not in entry or "sha256" not in entry:
                raise ValueError("Each manifest list entry requires path and sha256.")
            entries.append((entry["path"], entry["sha256"]))
        return entries
    raise ValueError("Manifest must be an object or a list of path/sha256 entries.")


def check_manifest(root, errors):
    manifest = root / "records" / "frozen_sha256.json"
    if not manifest.exists():
        return None
    try:
        payload = json.loads(manifest.read_text(encoding="utf-8"))
        entries = manifest_entries(payload)
    except (OSError, UnicodeError, ValueError) as exc:
        errors.append(f"Cannot read frozen SHA-256 manifest: {exc}")
        return 0
    if not entries:
        errors.append("Frozen SHA-256 manifest contains no file entries.")
    seen = set()
    checked = 0
    for relative, expected in entries:
        if not isinstance(relative, str) or not relative:
            errors.append(f"Manifest has an invalid path: {relative!r}.")
            continue
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", expected):
            errors.append(f"Manifest has an invalid SHA-256 digest for {relative!r}.")
            continue
        path = root / relative
        try:
            if Path(relative).is_absolute():
                raise ValueError("manifest paths must be relative to the deliverable root")
            resolved = path.resolve()
            resolved.relative_to(root)
            if resolved in seen:
                raise ValueError("duplicate manifest path")
            seen.add(resolved)
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
        except (OSError, ValueError) as exc:
            errors.append(f"Manifest file {relative!r}: {exc}")
            continue
        checked += 1
        if actual != expected.lower():
            errors.append(
                f"SHA-256 mismatch: {relative}\n"
                f"  expected {expected.lower()}\n"
                f"  actual   {actual}"
            )
    return checked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Deliverable root directory")
    parser.add_argument("--inventory", help="Inventory CSV path, relative to root or absolute")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error(f"Deliverable root is not a directory: {root}")

    errors = []
    expected_names = {f"{PREFIX}_11_scan{scan:03d}.tex": scan for scan in SCANS}
    candidates = {}
    for path in sorted(root.rglob(f"{PREFIX}_11_scan*.tex")):
        candidates.setdefault(path.name, []).append(path)
        if path.name not in expected_names:
            errors.append(f"Unexpected page fragment: {path.relative_to(root)}")

    contents = []
    counts = []
    for name, scan in expected_names.items():
        matches = candidates.get(name, [])
        if len(matches) != 1:
            errors.append(f"Expected exactly one {name}; found {len(matches)}.")
            counts.append((scan, None, None))
            continue
        path = matches[0]
        try:
            raw = path.read_bytes()
            text = raw.decode("utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {name}: {exc}")
            counts.append((scan, None, None))
            continue
        contents.append(raw)
        clean = without_comments(text)
        tokens = list(commands(clean))
        scanpages = [integer_argument(clean, end) for command, end in tokens if command == "scanpage"]
        if scanpages != [scan]:
            errors.append(f"{name}: expected one \\scanpage{{{scan}}}; found arguments {scanpages!r}.")
        if scan == SCANS[0]:
            cotefiles = [integer_argument(clean, end) for command, end in tokens if command == "cotefile"]
            if 11 not in cotefiles:
                errors.append(f"{name}: missing \\cotefile{{11}}.")
        forbidden = sorted({command for command, _ in tokens if command in {"includegraphics", "documentclass"}})
        if forbidden:
            errors.append(f"{name}: forbidden fragment command(s): " + ", ".join(forbidden))
        opening, closing = brace_errors(clean)
        for kind, positions in (("opening", opening), ("closing", closing)):
            if positions:
                locations = ", ".join(f"{line}:{column}" for line, column in positions)
                errors.append(f"{name}: unmatched {kind} brace(s) at line:column {locations}.")
        counts.append((
            scan,
            sum(command == "unsure" for command, _ in tokens),
            sum(command == "illegible" for command, _ in tokens),
        ))

    combined = root / f"{PREFIX}_transcription.tex"
    try:
        combined_bytes = combined.read_bytes()
        if len(contents) == len(SCANS) and combined_bytes != b"".join(contents):
            errors.append(f"{combined.name}: does not equal the exact ordered concatenation of the 39 page files.")
    except OSError as exc:
        errors.append(f"Cannot read combined transcription: {exc}")

    inventory = find_inventory(root, args.inventory, errors)
    inventory_rows = check_inventory(inventory, errors) if inventory is not None else 0
    manifest_checked = check_manifest(root, errors)

    print(f"Deliverable: {root}")
    print("Expected scans: 003–032, 034–042 (39 pages)")
    print(f"Readable unique expected pages: {len(contents)}/39")
    print(f"Inventory: {inventory if inventory is not None else 'unresolved'} ({inventory_rows} rows)")
    print("Frozen SHA-256 manifest: " + (
        "absent (optional check skipped)" if manifest_checked is None
        else f"{manifest_checked} files hashed"
    ))
    print("\nUncertainty command counts (comments excluded):")
    print("scan\tunsure\tillegible")
    for scan, unsure, illegible in counts:
        print(f"{scan:03d}\t{unsure if unsure is not None else 'unavailable'}\t{illegible if illegible is not None else 'unavailable'}")
    print("TOTAL\t{}\t{}".format(
        sum(unsure for _, unsure, _ in counts if unsure is not None),
        sum(illegible for _, _, illegible in counts if illegible is not None),
    ))
    if errors:
        print(f"\nFAIL: {len(errors)} structural issue(s).")
        for error in errors:
            print(f"- {error}")
        return 1
    print("\nPASS: all requested structural checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
