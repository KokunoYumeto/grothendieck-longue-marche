#!/usr/bin/env python3
"""Mechanical checks and packaging; never records a reading or audit itself.

Run only when the human/model transcriber requests the relevant operation.
The checks establish file/marker consistency, not transcription accuracy.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path
import re
import sys
import zipfile

PREFIX = "MPL_64_040-077"
SCANS = list(range(40, 78))
INVENTORY_COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
EXCLUDED_DIRS = {"upload", "scans", "context", "__pycache__", ".git"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def page_path(root: Path, scan: int) -> Path:
    return root / "pages" / f"{PREFIX}_64_scan{scan:03d}.tex"


def checked_paths(root: Path) -> list[Path]:
    return [page_path(root, scan) for scan in SCANS] + [
        root / f"{PREFIX}_transcription.tex"
    ]


def scan_markers(text: str) -> list[int]:
    # Ignore TeX comments, including archive-foliation records.
    live = "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0]
                     for line in text.splitlines())
    return [int(n) for n in re.findall(r"\\scanpage\{(\d+)\}", live)]


def structural_errors(text: str) -> list[str]:
    """Small token-aware checks, not a replacement for a LaTeX compiler."""
    errors: list[str] = []
    braces: list[int] = []
    environments: list[tuple[str, int]] = []
    delimiters: list[tuple[str, int]] = []
    dollars = 0
    tokens = re.finditer(
        r"\\(?:begin|end)\{[^}]+\}|\\(?:[A-Za-z]+|.)|%[^\n]*|[{}$#]", text)
    for match in tokens:
        token = match.group()
        line = text.count("\n", 0, match.start()) + 1
        if token.startswith("%"):
            continue
        environment = re.fullmatch(r"\\(begin|end)\{([^}]+)\}", token)
        if environment:
            action, name = environment.groups()
            if action == "begin":
                environments.append((name, line))
            elif not environments or environments[-1][0] != name:
                errors.append(f"line {line}: unmatched end of {name}")
            else:
                environments.pop()
        elif token == "{":
            braces.append(line)
        elif token == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"line {line}: unmatched closing brace")
        elif token in (r"\[", r"\("):
            delimiters.append((token, line))
        elif token in (r"\]", r"\)"):
            expected = r"\[" if token == r"\]" else r"\("
            if not delimiters or delimiters[-1][0] != expected:
                errors.append(f"line {line}: unmatched math delimiter {token}")
            else:
                delimiters.pop()
        elif token == "$":
            dollars += 1
        elif token == "#":
            errors.append(f"line {line}: unescaped parameter character #")
    errors.extend(f"line {line}: unclosed grouping brace" for line in braces)
    errors.extend(f"line {line}: unclosed environment {name}" for name, line in environments)
    errors.extend(f"line {line}: unclosed math delimiter {token}" for token, line in delimiters)
    if dollars % 2:
        errors.append("odd number of unescaped dollar math delimiters")
    return errors


def check(root: Path, *, final: bool = True) -> None:
    errors: list[str] = []
    required = checked_paths(root) + [
        root / f"{PREFIX}_doubts.md",
        root / f"{PREFIX}_inventory.csv",
        root / "progress.log", root / "CHECK_EVENTS.tsv",
    ]
    if final:
        required.append(root / f"{PREFIX}_notes.md")
    for path in required:
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Missing or empty: {path.relative_to(root)}")
    expected_pages = {page_path(root, scan) for scan in SCANS}
    actual_pages = set((root / "pages").glob("*.tex"))
    for extra in sorted(actual_pages - expected_pages):
        errors.append(f"Unexpected page file: {extra.name}")
    for scan in SCANS:
        path = page_path(root, scan)
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            if scan_markers(text) != [scan]:
                errors.append(f"Expected exactly one scan marker {scan}: {path.name}")
            errors.extend(f"{path.name}: {error}" for error in structural_errors(text))
    combined = root / f"{PREFIX}_transcription.tex"
    if combined.is_file():
        text = combined.read_text(encoding="utf-8")
        if scan_markers(text) != SCANS:
            errors.append("Combined transcription scan markers are not 40 through 77 in order")
        if not re.match(r"\s*\\cotefile\{64\}\s*\\scanpage\{0*40\}", text):
            errors.append("Combined transcription does not begin with cote 64 and scan 40")
        if re.search(r"\\(?:documentclass|begin\{document\})", text):
            errors.append("Combined transcription must be a fragment, without document preamble")
        if all(page_path(root, scan).is_file() for scan in SCANS):
            joined = b"".join(page_path(root, scan).read_bytes() for scan in SCANS)
            if combined.read_bytes() != joined:
                errors.append("Combined transcription is not the exact byte concatenation of page files")
    inventory = root / f"{PREFIX}_inventory.csv"
    if inventory.is_file():
        with inventory.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != INVENTORY_COLUMNS:
                errors.append("Inventory columns do not match the requested schema")
            rows = list(reader)
        seen: set[int] = set()
        identifiers: set[tuple[str | None, str | None, str | None]] = set()
        for number, row in enumerate(rows, 2):
            try:
                scan = int(row.get("scan", ""))
                seen.add(scan)
                if scan not in SCANS:
                    errors.append(f"Inventory row {number}: unexpected scan {scan}")
            except (TypeError, ValueError):
                errors.append(f"Inventory row {number}: invalid scan")
            if row.get("cote") != "64":
                errors.append(f"Inventory row {number}: cote is not 64")
            if row.get("transcribed") != "yes":
                errors.append(f"Inventory row {number}: transcribed is not yes")
            if row.get("kind") not in ELEMENT_KINDS:
                errors.append(f"Inventory row {number}: invalid element kind")
            if row.get("sheet_kind") not in SHEET_KINDS:
                errors.append(f"Inventory row {number}: invalid sheet kind")
            identifier = (row.get("cote"), row.get("scan"), row.get("element"))
            if not row.get("element") or identifier in identifiers:
                errors.append(f"Inventory row {number}: empty or duplicate element identifier")
            identifiers.add(identifier)
            if None in row or any(row.get(column) is None for column in INVENTORY_COLUMNS):
                errors.append(f"Inventory row {number}: malformed CSV field count")
        if seen != set(SCANS):
            errors.append("Inventory does not cover exactly scans 40 through 77")
    if errors:
        raise ValueError("\n".join(errors))
    print("Mechanical file, page-marker, and inventory checks passed.")


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def freeze(root: Path) -> None:
    check(root, final=False)
    log_path = root / "progress.log"
    log = log_path.read_text(encoding="utf-8")
    if re.search(r"^transcription frozen ", log, re.M):
        raise ValueError("A freeze is already recorded; refusing to replace it")
    missing_audits = [n for n in SCANS if not re.search(
        rf"^scan 0*{n} audited \d{{4}}-\d{{2}}-\d{{2}} ", log, re.M)]
    if missing_audits:
        raise ValueError("No recorded audit for scans: " + ", ".join(map(str, missing_audits)))
    lines = [f"sha256 {digest(path)} {path.relative_to(root).as_posix()}"
             for path in checked_paths(root)]
    lines.append(f"transcription frozen {utc_now()}")
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")
    print("Recorded SHA-256 values for 38 page files and the combined transcription.")


def verify_frozen(root: Path, *, record: bool = True) -> None:
    log_path = root / "progress.log"
    log = log_path.read_text(encoding="utf-8")
    if not re.search(r"^transcription frozen ", log, re.M):
        raise ValueError("No recorded freeze")
    frozen_part = re.split(r"^transcription frozen ", log, maxsplit=1, flags=re.M)[0]
    records = dict((name, value) for value, name in re.findall(
        r"^sha256 ([0-9a-f]{64}) (.+)$", frozen_part, re.M))
    expected = {path.relative_to(root).as_posix() for path in checked_paths(root)}
    if set(records) != expected:
        raise ValueError("Frozen SHA-256 records do not cover exactly the 39 transcription files")
    changed = [name for name, value in records.items()
               if not (root / name).is_file() or digest(root / name) != value]
    if changed:
        raise ValueError("Frozen transcription changed: " + ", ".join(changed))
    if record:
        with log_path.open("a", encoding="utf-8") as handle:
            handle.write(f"frozen hashes unchanged {utc_now()} (39 files)\n")
    print("All 39 frozen transcription SHA-256 values are unchanged.")


def eligible(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    return (path.is_file() and not path.is_symlink()
            and not any(part in EXCLUDED_DIRS or part.startswith(".")
                        for part in relative.parts)
            and path.suffix.lower() not in {".zip", ".pyc"}
            and not path.name.startswith("PROMPT("))


def package(root: Path, checkpoint: int | None) -> Path:
    if checkpoint is None:
        check(root, final=True)
        verify_frozen(root)
        name = f"{PREFIX}.zip"
    else:
        if checkpoint < 1:
            raise ValueError("Checkpoint number must be positive")
        # Scheduling is deliberately left to the transcriber; this utility does
        # not decide that a page/section boundary warrants a checkpoint.
        name = f"{PREFIX}_checkpoint_{checkpoint:02d}.zip"
    destination = root.parent / name
    files = sorted(path for path in root.rglob("*") if eligible(path, root))
    if not files:
        raise ValueError("No deliverable or documentation files to package")
    # Exclusive creation protects previous checkpoints and an existing final.
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(root).as_posix())
    print(f"Created {destination} ({len(files)} files)")
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true")
    action.add_argument("--check-transcription", action="store_true",
                        help="read-only checks before research notes are written")
    action.add_argument("--freeze", action="store_true")
    action.add_argument("--verify-frozen", action="store_true")
    action.add_argument("--checkpoint", type=int, metavar="NN")
    action.add_argument("--final", action="store_true")
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        if args.check:
            check(root)
        elif args.check_transcription:
            check(root, final=False)
        elif args.freeze:
            freeze(root)
        elif args.verify_frozen:
            verify_frozen(root)
        else:
            package(root, args.checkpoint)
        return 0
    except (OSError, ValueError, csv.Error, zipfile.BadZipFile) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
