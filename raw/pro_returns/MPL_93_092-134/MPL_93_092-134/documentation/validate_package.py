#!/usr/bin/env python3
"""Mechanical checks only for MPL_93_092-134.

This program does not inspect images or judge readings, mathematics, page-element
completeness, or whether a suspected placeholder actually occurs in the source.
It never modifies the package. Run after page production, for example:

    python documentation/validate_package.py
    python documentation/validate_package.py --frozen-sha256 documentation/frozen.sha256

The combined fragment must be the byte-for-byte concatenation of sorted page
files, with no extra separators. Put desired separating newlines in each page
file before combining. SHA-256 manifests use sha256sum format, with paths
relative to the package root; a JSON path-to-digest object is also accepted.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

STEM = "MPL_93_092-134"
SCANS = tuple(n for n in range(92, 135) if n != 125)
HEADER = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note",
                 "insertion", "deletion"}


def uncomment(text: str) -> str:
    """Remove TeX comments, retaining line numbers; respect escaped percent."""
    lines = []
    for line in text.splitlines(keepends=True):
        for i, char in enumerate(line):
            if char != "%":
                continue
            preceding = 0
            j = i - 1
            while j >= 0 and line[j] == "\\":
                preceding += 1
                j -= 1
            if preceding % 2 == 0:
                line = line[:i] + ("\n" if line.endswith("\n") else "")
                break
        lines.append(line)
    return "".join(lines)


def brace_errors(text: str) -> list[str]:
    """Check unescaped braces, excluding comments; not a complete TeX parser."""
    stack: list[int] = []
    errors: list[str] = []
    line = 1
    i = 0
    while i < len(text):
        char = text[i]
        if char == "\n":
            line += 1
        if char == "\\":
            # Escaped braces, percent and backslash are not group delimiters.
            if i + 1 < len(text) and text[i + 1] in "{}%\\":
                i += 2
                continue
        elif char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                errors.append(f"unmatched closing brace at line {line}")
        i += 1
    errors.extend(f"unclosed opening brace at line {n}" for n in stack)
    return errors


def parse_manifest(path: Path) -> dict[str, str]:
    raw = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        value = json.loads(raw)
        if not isinstance(value, dict) or not all(isinstance(k, str) and
                isinstance(v, str) for k, v in value.items()):
            raise ValueError("JSON manifest must map relative paths to digest strings")
        return value
    result: dict[str, str] = {}
    for n, line in enumerate(raw.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([0-9a-fA-F]{64})\s+[ *]?(.+)", line)
        if not match:
            raise ValueError(f"manifest line {n} is not sha256sum format")
        digest, name = match.groups()
        if name in result:
            raise ValueError(f"duplicate manifest path: {name}")
        result[name] = digest
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--frozen-sha256", type=Path,
                        help="optional sha256sum or JSON manifest of frozen files")
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    info: list[str] = []
    pages = [root / "pages" / f"{STEM}_93_scan{n:03d}.tex" for n in SCANS]
    expected = {p.name for p in pages}
    present = {p.name for p in (root / "pages").glob("*.tex")}
    for name in sorted(expected - present):
        errors.append(f"missing page file: {name}")
    for name in sorted(present - expected):
        errors.append(f"unexpected page file: {name}")

    forbidden = re.compile(r"\\(?:includegraphics|includepdf|input|include|includeonly|"
                           r"pdfximage|epsfig|epsfbox|documentclass|usepackage)\b")
    placeholders = re.compile(r"\[\s*(?:\.{3}|…)\s*\]|\b(?:TODO|PLACEHOLDER)\b")
    page_bytes: list[bytes] = []
    for n, path in zip(SCANS, pages):
        if not path.is_file():
            continue
        raw = path.read_bytes()
        page_bytes.append(raw)
        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path.name}: invalid UTF-8: {exc}")
            continue
        clean = uncomment(content)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if markers != [str(n)]:
            errors.append(f"{path.name}: scan markers {markers!r}, expected [{str(n)!r}]")
        if n == SCANS[0] and not re.match(
                r"\s*\\cotefile\s*\{93\}\s*\\scanpage\s*\{92\}", clean):
            errors.append(f"{path.name}: must start with cotefile 93 and scanpage 92")
        for match in forbidden.finditer(clean):
            line = clean.count("\n", 0, match.start()) + 1
            errors.append(f"{path.name}:{line}: disallowed fragment/image command {match.group()}")
        for match in placeholders.finditer(clean):
            line = clean.count("\n", 0, match.start()) + 1
            errors.append(f"{path.name}:{line}: possible placeholder {match.group()!r}; inspect manually")
        errors.extend(f"{path.name}: {message}" for message in brace_errors(clean))

    combined = root / f"{STEM}_transcription.tex"
    if not combined.is_file():
        errors.append(f"missing combined transcription: {combined.name}")
    elif len(page_bytes) == len(SCANS):
        actual = combined.read_bytes()
        joined = b"".join(page_bytes)
        if actual != joined:
            first = next((i for i, (a, b) in enumerate(zip(actual, joined)) if a != b),
                         min(len(actual), len(joined)))
            errors.append(f"combined transcription differs from exact ordered concatenation "
                          f"at byte {first}; sizes {len(actual)} versus {len(joined)}")
        else:
            info.append("Combined transcription equals exact ordered page-file concatenation.")

    inventory = root / f"{STEM}_inventory.csv"
    covered: set[int] = set()
    rows = 0
    if not inventory.is_file():
        errors.append(f"missing inventory: {inventory.name}")
    else:
        try:
            with inventory.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                if reader.fieldnames != HEADER:
                    errors.append(f"inventory header is {reader.fieldnames!r}, expected {HEADER!r}")
                for line, row in enumerate(reader, 2):
                    rows += 1
                    prefix = f"{inventory.name}:{line}"
                    if None in row or any(row.get(key) is None for key in HEADER):
                        errors.append(f"{prefix}: malformed row/column count")
                        continue
                    try:
                        scan = int(row["scan"])
                    except ValueError:
                        errors.append(f"{prefix}: non-integer scan {row['scan']!r}")
                        continue
                    if scan not in SCANS:
                        errors.append(f"{prefix}: unexpected scan {scan}")
                    else:
                        covered.add(scan)
                    if row["cote"] != "93":
                        errors.append(f"{prefix}: cote must be 93")
                    if row["sheet_kind"] not in SHEET_KINDS:
                        errors.append(f"{prefix}: invalid sheet_kind {row['sheet_kind']!r}")
                    if row["kind"] not in ELEMENT_KINDS:
                        errors.append(f"{prefix}: invalid element kind {row['kind']!r}")
                    if row["transcribed"] != "yes":
                        errors.append(f"{prefix}: transcribed must be exactly yes")
                    for key in ("element", "position", "first_words_or_objects"):
                        if not row[key].strip():
                            errors.append(f"{prefix}: blank {key}")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"inventory could not be parsed: {exc}")
    for n in sorted(set(SCANS) - covered):
        errors.append(f"inventory has no element rows for scan {n:03d}")
    info.append(f"Inventory has {rows} rows and covers {len(covered)}/{len(SCANS)} expected scans.")

    if args.frozen_sha256:
        manifest = args.frozen_sha256
        if not manifest.is_absolute():
            manifest = root / manifest
        try:
            entries = parse_manifest(manifest)
            needed = {str(path.relative_to(root)) for path in pages + [combined]}
            missing = needed - set(entries)
            for name in sorted(missing):
                errors.append(f"frozen manifest lacks {name}")
            for name, digest in entries.items():
                if not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
                    errors.append(f"invalid SHA-256 digest for {name}")
                    continue
                path = (root / name).resolve()
                if not path.is_relative_to(root):
                    errors.append(f"manifest path escapes package: {name}")
                    continue
                if not path.is_file():
                    errors.append(f"manifest file missing: {name}")
                    continue
                actual = hashlib.sha256(path.read_bytes()).hexdigest()
                if actual.lower() != digest.lower():
                    errors.append(f"frozen hash changed: {name}")
            info.append(f"Checked {len(entries)} frozen-manifest entries.")
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"cannot validate frozen manifest: {exc}")

    for message in info:
        print(f"INFO: {message}")
    for message in errors:
        print(f"ERROR: {message}")
    print("LIMITATION: mechanical checks cannot verify visual fidelity, complete page "
          "inventories, correct use of doubt macros, or mathematical correctness. "
          "Placeholder flags require source-image judgment; literal mathematical "
          "ellipsis commands are not treated as placeholders.")
    print(f"{'FAIL' if errors else 'PASS'}: {len(errors)} mechanical issue(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
