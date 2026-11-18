#!/usr/bin/env python3
"""Validate and optionally ZIP the MPL_93_047-091 deliverables.

This utility checks file structure and transcription bookkeeping only. It does
not establish completeness or accuracy against the scans, and never reads an
input scan or the supplied context archive. The transcriber must perform those
checks visually. No third-party dependencies are required.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import sys
import zipfile
from pathlib import Path


PREFIX = "MPL_93_047-091"
COTE = "93"
SCANS = tuple(n for n in range(47, 92) if n not in {71, 79, 85})
PAGE_RE = re.compile(rf"{re.escape(PREFIX)}_{COTE}_scan(\d{{3}})\.tex\Z")
INVENTORY_COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
REQUIRED_FILES = (
    f"{PREFIX}_transcription.tex",
    f"{PREFIX}_doubts.md",
    f"{PREFIX}_inventory.csv",
    f"{PREFIX}_notes.md",
    "progress.log",
    "CHECK_EVENTS.tsv",
)
# These are structural exclusions, not a restrictive whitelist of LaTeX.
# Standard LaTeX, TikZ, tikz-cd, and the task's transcription macros are allowed.
FORBIDDEN_COMMANDS = {
    "documentclass", "documentstyle", "usepackage", "RequirePackage",
    "LoadClass", "PassOptionsToPackage", "PassOptionsToClass",
    "newcommand", "renewcommand", "providecommand", "DeclareRobustCommand",
    "newenvironment", "renewenvironment", "newtheorem", "newtheoremstyle",
    "def", "gdef", "edef", "xdef", "let", "futurelet",
    "includegraphics", "includepdf", "epsfig", "psfig", "pdfximage",
    "XeTeXpicfile", "XeTeXpdffile", "graphicspath",
    "input", "include", "subfile",
}
EXCLUDED_DIRS = {
    "upload", "uploads", "input", "inputs", "scan", "scans", "source",
    "sources", "context", "checkpoints", "__pycache__", ".git", ".venv",
    "venv", ".pytest_cache", ".mypy_cache", ".ruff_cache", "node_modules",
}
EXCLUDED_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".webp",
    ".pyc", ".pyo", ".aux", ".toc", ".out", ".synctex.gz",
}


def without_comments(text: str) -> str:
    """Remove TeX comments without treating an escaped percent as a comment."""
    result = []
    for line in text.splitlines(keepends=True):
        for index, char in enumerate(line):
            if char != "%":
                continue
            preceding = index - 1
            while preceding >= 0 and line[preceding] == "\\":
                preceding -= 1
            if (index - 1 - preceding) % 2 == 0:
                line = line[:index] + ("\n" if line.endswith("\n") else "")
                break
        result.append(line)
    return "".join(result)


def marker_values(text: str, name: str) -> list[str]:
    return re.findall(r"\\" + name + r"\s*\{\s*([^{}]*?)\s*\}", text)


def read_utf8(path: Path, errors: list[str]) -> str | None:
    try:
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        errors.append(f"Cannot read UTF-8 file {path.name}: {exc}")
        return None


def check_fragment(path: Path, text: str, errors: list[str]) -> None:
    live = without_comments(text)
    commands = set(re.findall(r"\\([A-Za-z@]+)", live))
    bad = sorted(commands & FORBIDDEN_COMMANDS)
    if bad:
        errors.append(f"{path.name}: forbidden fragment/image commands: " + ", ".join("\\" + x for x in bad))
    if re.search(r"\\(?:begin|end)\s*\{\s*document\s*\}", live):
        errors.append(f"{path.name}: document environment is forbidden in a fragment")


def validate(root: Path, partial: bool) -> tuple[list[str], list[str], list[int]]:
    errors: list[str] = []
    notes: list[str] = []
    pages_dir = root / "pages"
    present: dict[int, Path] = {}
    if not pages_dir.is_dir():
        errors.append("Missing pages/ directory")
    else:
        for path in sorted(pages_dir.iterdir()):
            if not path.is_file():
                errors.append(f"Unexpected non-file in pages/: {path.name}")
                continue
            match = PAGE_RE.fullmatch(path.name)
            if not match:
                errors.append(f"Unexpected page filename: {path.name}")
                continue
            scan = int(match.group(1))
            if scan not in SCANS:
                errors.append(f"Page filename uses an excluded/out-of-range scan: {path.name}")
            elif scan in present:
                errors.append(f"Duplicate page for scan {scan:03d}")
            else:
                present[scan] = path

    ordered = sorted(present)
    if partial:
        if ordered != list(SCANS[:len(ordered)]):
            errors.append("Partial page set must be a consecutive initial segment of the prescribed scan order")
    elif ordered != list(SCANS):
        missing = [f"{n:03d}" for n in SCANS if n not in present]
        errors.append("Missing required page files: " + ", ".join(missing))
    notes.append(f"Page files: {len(ordered)}/{len(SCANS)}")

    for scan in ordered:
        path = present[scan]
        text = read_utf8(path, errors)
        if text is None:
            continue
        live = without_comments(text)
        markers = marker_values(live, "scanpage")
        if markers != [str(scan)] and markers != [f"{scan:03d}"]:
            errors.append(f"{path.name}: expected exactly one scanpage marker for {scan}; found {markers!r}")
        cotes = marker_values(live, "cotefile")
        if scan == SCANS[0]:
            if cotes != [COTE]:
                errors.append(f"{path.name}: first page must contain exactly \\cotefile{{{COTE}}}")
            if not re.match(r"\s*\\cotefile\s*\{\s*93\s*\}\s*\\scanpage\s*\{\s*0?47\s*\}", live):
                errors.append(f"{path.name}: fragment must begin with cotefile then scanpage")
        else:
            if cotes:
                errors.append(f"{path.name}: unexpected extra cotefile marker")
            if not re.match(rf"\s*\\scanpage\s*\{{\s*0?{scan}\s*\}}", live):
                errors.append(f"{path.name}: page fragment must begin with its scanpage marker")
        check_fragment(path, text, errors)

    for name in REQUIRED_FILES:
        path = root / name
        # Notes are deliberately not begun until the transcription is frozen.
        if partial and name == f"{PREFIX}_notes.md" and not path.exists():
            notes.append("Research notes not yet present (allowed in partial mode)")
            continue
        if not path.is_file():
            errors.append(f"Missing required file: {name}")

    combined = root / f"{PREFIX}_transcription.tex"
    if combined.is_file():
        try:
            expected = b"".join(present[n].read_bytes() for n in ordered)
            actual = combined.read_bytes()
            if actual != expected:
                errors.append("Combined transcription is not the exact byte concatenation of ordered page files")
            text = read_utf8(combined, errors)
            if text is not None:
                check_fragment(combined, text, errors)
                found = marker_values(without_comments(text), "scanpage")
                try:
                    actual_order = [int(x) for x in found]
                except ValueError:
                    actual_order = []
                if actual_order != ordered:
                    errors.append(f"Combined transcription scan order differs from page set: {found!r}")
        except OSError as exc:
            errors.append(f"Cannot compare combined transcription: {exc}")

    inventory = root / f"{PREFIX}_inventory.csv"
    if inventory.is_file():
        raw = read_utf8(inventory, errors)
        if raw is not None:
            try:
                reader = csv.DictReader(io.StringIO(raw, newline=""))
                if reader.fieldnames != INVENTORY_COLUMNS:
                    errors.append(f"Inventory columns must be exactly {INVENTORY_COLUMNS!r}; found {reader.fieldnames!r}")
                else:
                    inventory_scans: set[int] = set()
                    element_keys: set[tuple[int, str]] = set()
                    previous_scan = -1
                    count = 0
                    for rownum, row in enumerate(reader, start=2):
                        count += 1
                        label = f"Inventory row {rownum}"
                        if None in row or any(value is None for value in row.values()):
                            errors.append(f"{label}: malformed CSV row")
                            continue
                        if any(not row[name].strip() for name in INVENTORY_COLUMNS):
                            errors.append(f"{label}: one or more required fields are empty")
                        if row["cote"].strip() != COTE:
                            errors.append(f"{label}: cote must be {COTE}")
                        try:
                            scan = int(row["scan"])
                        except ValueError:
                            errors.append(f"{label}: scan is not an integer")
                            continue
                        if scan not in present:
                            errors.append(f"{label}: scan {scan:03d} has no corresponding page file")
                        if scan < previous_scan:
                            errors.append(f"{label}: inventory scans are not in ascending page order")
                        previous_scan = scan
                        inventory_scans.add(scan)
                        key = (scan, row["element"].strip())
                        if key in element_keys:
                            errors.append(f"{label}: duplicate element identifier within scan {scan:03d}")
                        element_keys.add(key)
                        if row["sheet_kind"].strip() not in SHEET_KINDS:
                            errors.append(f"{label}: unknown sheet_kind {row['sheet_kind']!r}")
                        if row["kind"].strip() not in ELEMENT_KINDS:
                            errors.append(f"{label}: unknown element kind {row['kind']!r}")
                        if row["transcribed"].strip() != "yes":
                            errors.append(f"{label}: transcribed must be exactly yes")
                    absent = sorted(set(ordered) - inventory_scans)
                    if absent:
                        errors.append("Pages without inventory elements: " + ", ".join(f"{n:03d}" for n in absent))
                    notes.append(f"Inventory elements: {count}")
            except csv.Error as exc:
                errors.append(f"Cannot parse inventory CSV: {exc}")

    # The check-event schema's wording was not rigidly prescribed; only verify
    # that the file is a nonempty tabular TSV with a header, not invented checks.
    events = root / "CHECK_EVENTS.tsv"
    if events.is_file():
        raw = read_utf8(events, errors)
        if raw is not None:
            first = raw.splitlines()[0] if raw.splitlines() else ""
            if not first or "\t" not in first:
                errors.append("CHECK_EVENTS.tsv must contain a tab-separated header (zero events is allowed)")

    return errors, notes, ordered


def package_files(root: Path, output: Path) -> tuple[list[Path], list[str]]:
    selected: list[Path] = []
    skipped: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        lowered_parts = {part.lower() for part in relative.parts[:-1]}
        lowered_name = path.name.lower()
        excluded = (
            bool(lowered_parts & EXCLUDED_DIRS)
            or any(part.startswith(".") for part in relative.parts)
            or path.suffix.lower() in EXCLUDED_SUFFIXES
            or lowered_name.endswith(".synctex.gz")
            or path.suffix.lower() == ".zip"
            or "_scans_part" in lowered_name
            or lowered_name in {"manifest.tsv", "prompt.md"}
            or path.resolve() == output.resolve()
        )
        if excluded:
            skipped.append(str(relative))
            continue
        if path.is_symlink():
            raise ValueError(f"Refusing to package symlink: {relative}")
        selected.append(path)
    return selected, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="deliverable folder (defaults to the parent of scripts/)")
    parser.add_argument("--partial", action="store_true",
                        help="permit a sequential initial subset of pages and absent research notes")
    parser.add_argument("--output", type=Path,
                        help="create this ZIP after validation succeeds; existing ZIPs are never overwritten")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"ERROR: deliverable folder does not exist: {root}", file=sys.stderr)
        return 2
    errors, notes, scans = validate(root, args.partial)
    for note in notes:
        print(note)
    if errors:
        for error in errors:
            print("ERROR: " + error, file=sys.stderr)
        print(f"Validation failed: {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("Structural validation passed (" + ("partial" if args.partial else "final") + ").")
    print("This does not certify visual transcription accuracy or research claims.")
    if args.output is None:
        return 0
    output = args.output.resolve()
    if output.exists():
        print(f"ERROR: refusing to overwrite existing ZIP: {output}", file=sys.stderr)
        return 2
    if not output.parent.is_dir():
        print(f"ERROR: output parent directory does not exist: {output.parent}", file=sys.stderr)
        return 2
    try:
        files, skipped = package_files(root, output)
        # Exclusive creation prevents an accidental overwrite between the
        # existence check and archive creation.
        with zipfile.ZipFile(output, mode="x", compression=zipfile.ZIP_DEFLATED,
                             compresslevel=9) as archive:
            for path in files:
                archive.write(path, arcname=path.relative_to(root).as_posix())
        with zipfile.ZipFile(output) as archive:
            bad_member = archive.testzip()
            if bad_member:
                raise ValueError(f"ZIP CRC check failed for {bad_member}")
        digest = hashlib.sha256(output.read_bytes()).hexdigest()
        print(f"Created ZIP: {output}")
        print(f"Included {len(files)} files; excluded {len(skipped)} input/archive/cache files.")
        print(f"ZIP SHA-256: {digest}")
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"ERROR: packaging failed: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
