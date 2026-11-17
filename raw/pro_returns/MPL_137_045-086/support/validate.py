#!/usr/bin/env python3
"""Structural checks only; never an assessment of transcription accuracy.

Run after page files have been written. This script does not use OCR or inspect
images. It reads only the resulting text, inventory, and optional hash manifest.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


PACKAGE = "MPL_137_045-086"
SCANS = tuple(range(45, 87))
COLUMNS = (
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
PAGE_PATTERN = re.compile(r"MPL_137_045-086_137_scan(\d{3})\.tex")
IMAGE_COMMANDS = re.compile(
    r"\\(?:includegraphics|includepdf|pgfimage|pdfximage|pdfrefximage|epsfig|epsfbox)\b"
)
PLACEHOLDERS = re.compile(
    r"\[\s*(?:\.{3}|…)\s*\]|\b(?:TODO|TBD|PLACEHOLDER)\b"
)


def without_comments(text: str) -> str:
    """Remove unescaped TeX comments, preserving line numbers."""
    output = []
    for line in text.splitlines(keepends=True):
        cut = None
        for index, char in enumerate(line):
            if char != "%":
                continue
            preceding_slashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                preceding_slashes += 1
                cursor -= 1
            if preceding_slashes % 2 == 0:
                cut = index
                break
        if cut is None:
            output.append(line)
        else:
            output.append(line[:cut] + ("\n" if line.endswith("\n") else ""))
    return "".join(output)


def brace_errors(text: str) -> list[str]:
    """Check unescaped braces, ignoring comments; report their line numbers."""
    stack = []
    problems = []
    line = 1
    slashes = 0
    for char in without_comments(text):
        if char == "\n":
            line += 1
        if char in "{}" and slashes % 2 == 0:
            if char == "{":
                stack.append(line)
            elif stack:
                stack.pop()
            else:
                problems.append(f"unmatched closing brace at line {line}")
        slashes = slashes + 1 if char == "\\" else 0
    problems.extend(f"unmatched opening brace at line {number}" for number in stack)
    return problems


def resolve_inside(root: Path, value: str) -> Path:
    candidate = (root / value).resolve() if not Path(value).is_absolute() else Path(value).resolve()
    if not candidate.is_relative_to(root.resolve()):
        raise ValueError(f"hash path lies outside deliverable: {value}")
    return candidate


def parse_hashes(path: Path, root: Path) -> dict[Path, str]:
    """Accept JSON {relative_path: sha256} or sha256sum-format lines.

    sha256sum lines may be included in a larger progress.log; unrelated log
    lines are ignored. A manifest must include every page and the combined file.
    """
    source = path.read_text(encoding="utf-8")
    hashes = {}
    if path.suffix.lower() == ".json":
        values = json.loads(source)
        if not isinstance(values, dict):
            raise ValueError("JSON hash manifest must map paths to SHA-256 strings")
        items = values.items()
    else:
        items = []
        for line in source.splitlines():
            # Both `HASH  PATH` and `SHA256 HASH  PATH` are accepted.
            match = re.fullmatch(r"(?:SHA256\s+)?([0-9a-fA-F]{64})\s+\*?(.+?)\s*", line)
            if match:
                items.append((match.group(2), match.group(1)))
    for filename, digest in items:
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
            raise ValueError(f"invalid SHA-256 digest for {filename!r}")
        target = resolve_inside(root, str(filename))
        if target in hashes and hashes[target] != digest.lower():
            raise ValueError(f"conflicting hashes for {filename}")
        hashes[target] = digest.lower()
    if not hashes:
        raise ValueError("no supported SHA-256 entries found")
    return hashes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true", help="allow a contiguous initial subset of scans 045–086")
    parser.add_argument("--hashes", type=Path, help="verify an existing JSON or sha256sum-format freeze manifest/log")
    args = parser.parse_args()
    root = args.root.resolve()
    errors = []
    warnings = []
    pages = {}

    page_directory = root / "pages"
    if not page_directory.is_dir():
        errors.append("pages/ directory is missing")
    else:
        for path in sorted(page_directory.glob("*.tex")):
            match = PAGE_PATTERN.fullmatch(path.name)
            if not match:
                errors.append(f"unexpected page filename: {path.name}")
                continue
            scan = int(match.group(1))
            if scan not in SCANS:
                errors.append(f"scan outside expected range: {path.name}")
            else:
                pages[scan] = path

    expected = set(SCANS)
    if args.partial:
        if pages:
            expected = set(range(45, max(pages) + 1))
        else:
            expected = set()
            warnings.append("no page files yet; partial validation cannot establish coverage")
    missing = sorted(expected - pages.keys())
    if missing:
        errors.append("missing pages: " + ", ".join(f"{scan:03d}" for scan in missing))

    page_bytes = []
    for scan, path in sorted(pages.items()):
        data = path.read_bytes()
        page_bytes.append(data)
        try:
            source = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path.name}: invalid UTF-8: {exc}")
            continue
        live = without_comments(source)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", live)
        if len(markers) != 1 or int(markers[0]) != scan:
            errors.append(f"{path.name}: expected exactly one \\scanpage{{{scan}}}, found {markers}")
        for problem in brace_errors(source):
            errors.append(f"{path.name}: {problem}")
        for match in IMAGE_COMMANDS.finditer(live):
            errors.append(f"{path.name}: forbidden image command {match.group(0)}")
        for match in PLACEHOLDERS.finditer(live):
            line = live.count("\n", 0, match.start()) + 1
            errors.append(f"{path.name}:{line}: possible forbidden placeholder {match.group(0)!r}; verify against ink")
        if re.search(r"\\(?:documentclass|usepackage)\b|\\begin\{document\}", live):
            errors.append(f"{path.name}: preamble/document wrapper in required fragment")

    combined = root / f"{PACKAGE}_transcription.tex"
    if not combined.is_file():
        if args.partial:
            warnings.append("combined transcription not yet present")
        else:
            errors.append("combined transcription is missing")
    else:
        data = combined.read_bytes()
        if data != b"".join(page_bytes):
            errors.append("combined transcription is not byte-for-byte concatenation of ordered page files")
        try:
            live = without_comments(data.decode("utf-8")).lstrip()
            if not re.match(r"\\cotefile\s*\{137\}\s*\\scanpage\s*\{0?45\}", live):
                errors.append("combined transcription does not start with \\cotefile{137} and \\scanpage{45}")
        except UnicodeDecodeError as exc:
            errors.append(f"combined transcription: invalid UTF-8: {exc}")

    inventory = root / f"{PACKAGE}_inventory.csv"
    inventory_scans = set()
    row_count = 0
    if not inventory.is_file():
        errors.append("inventory CSV is missing")
    else:
        with inventory.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if tuple(reader.fieldnames or ()) != COLUMNS:
                errors.append(f"inventory columns differ from required order: {reader.fieldnames}")
            for number, row in enumerate(reader, 2):
                row_count += 1
                label = f"inventory row {number}"
                if row.get("cote", "").strip() != "137":
                    errors.append(f"{label}: cote must be 137")
                try:
                    scan = int(row.get("scan", ""))
                except (ValueError, TypeError):
                    errors.append(f"{label}: invalid scan value")
                    continue
                inventory_scans.add(scan)
                if scan not in pages:
                    errors.append(f"{label}: scan {scan:03d} has no page file")
                if row.get("transcribed", "").strip() != "yes":
                    errors.append(f"{label}: transcribed must be yes")
                if row.get("sheet_kind", "").strip() not in SHEET_KINDS:
                    errors.append(f"{label}: unknown sheet_kind")
                if row.get("kind", "").strip() not in KINDS:
                    errors.append(f"{label}: unknown element kind")
                for key in ("element", "position", "first_words_or_objects"):
                    if not row.get(key, "").strip():
                        errors.append(f"{label}: empty {key}")
        for scan in sorted(pages.keys() - inventory_scans):
            errors.append(f"scan {scan:03d} has no inventory rows")

    hash_count = 0
    if args.hashes:
        try:
            hashes = parse_hashes(args.hashes, root)
            required_hashes = {path.resolve() for path in pages.values()} | {combined.resolve()}
            for path in sorted(required_hashes - hashes.keys()):
                errors.append(f"freeze manifest lacks {path.relative_to(root)}")
            for path, digest in hashes.items():
                if not path.is_file():
                    errors.append(f"freeze manifest file missing: {path.relative_to(root)}")
                elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                    errors.append(f"freeze hash changed: {path.relative_to(root)}")
                else:
                    hash_count += 1
        except (OSError, ValueError, TypeError) as exc:
            errors.append(f"cannot verify freeze hashes: {exc}")

    for warning in warnings:
        print("WARNING:", warning)
    for error in errors:
        print("ERROR:", error)
    print(f"Checked {len(pages)} page files, {row_count} inventory rows, {hash_count} matching freeze hashes.")
    print("PASS: structural checks only." if not errors else f"FAIL: {len(errors)} structural issue(s).")
    print("This does not verify completeness, readings, notation consistency, diagrams, or fidelity to the images.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
