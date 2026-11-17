#!/usr/bin/env python3
"""Mechanical checks and packaging only; this tool never evaluates readings.

No OCR, scan access, context access, or automatic transcription correction.
Validation does not establish that an inventory is exhaustive or a reading correct.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

STEM = "MPL_57_089-132"
EXPECTED = tuple(n for n in range(89, 133) if n != 98)
PAGE_RE = re.compile(r"MPL_57_089-132_57_scan(\d{3})\.tex\Z")
SCAN_RE = re.compile(r"\\scanpage\s*\{\s*(\d+)\s*\}")
COTE_RE = re.compile(r"\\cotefile\s*\{\s*([^{}]+)\s*\}")
DOUBT_RE = re.compile(r"\\(unsure|illegible)\s*\{")
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
HEADERS = ["cote", "scan", "sheet_kind", "element", "kind", "position", "first_words_or_objects", "transcribed"]
EXCLUDE_DIRS = {"scans", "upload", "uploads", "context", "__pycache__", ".git", ".pytest_cache", ".mypy_cache"}
EXCLUDE_SUFFIXES = {".zip", ".pyc", ".pyo"}


def escaped(text: str, index: int) -> bool:
    n = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        n += 1
        index -= 1
    return bool(n % 2)


def uncomment(text: str) -> str:
    # Preserve offsets and newlines for diagnostics, replacing comments with spaces.
    chars = list(text)
    i = 0
    while i < len(chars):
        if chars[i] == "%" and not escaped(text, i):
            while i < len(chars) and chars[i] != "\n":
                chars[i] = " "
                i += 1
        else:
            i += 1
    return "".join(chars)


def brace_errors(text: str) -> list[str]:
    clean = uncomment(text)
    openings = []
    errors = []
    for i, c in enumerate(clean):
        if escaped(clean, i):
            continue
        if c == "{":
            openings.append(i)
        elif c == "}":
            if openings:
                openings.pop()
            else:
                errors.append(f"unmatched closing brace at line {clean.count(chr(10), 0, i) + 1}")
    for i in openings:
        errors.append(f"unclosed opening brace at line {clean.count(chr(10), 0, i) + 1}")
    return errors


def doubts(text: str):
    clean = uncomment(text)
    for m in DOUBT_RE.finditer(clean):
        depth = 1
        i = m.end()
        start = i
        while i < len(clean) and depth:
            if not escaped(clean, i):
                if clean[i] == "{":
                    depth += 1
                elif clean[i] == "}":
                    depth -= 1
            i += 1
        yield m.group(1), clean.count("\n", 0, m.start()) + 1, text[start:i - 1] if depth == 0 else text[start:]


def page_files(root: Path):
    result = []
    for path in sorted((root / "pages").glob("*.tex")):
        match = PAGE_RE.fullmatch(path.name)
        result.append((int(match.group(1)) if match else None, path))
    return result


def combined_bytes(root: Path) -> bytes:
    chunks = []
    for _, path in page_files(root):
        data = path.read_bytes()
        chunks.append(data if data.endswith(b"\n") else data + b"\n")
    return b"\n".join(chunks)


def validate(root: Path, complete: bool = False):
    errors = []
    warnings = []
    entries = page_files(root)
    scans = []
    doubt_rows = []
    for number, path in entries:
        if number is None:
            errors.append(f"Unrecognized page filename: {path.name}")
            continue
        scans.append(number)
        if number not in EXPECTED:
            errors.append(f"Unexpected scan {number:03d}: {path.name}")
        text = path.read_text(encoding="utf-8")
        clean = uncomment(text)
        markers = [int(s) for s in SCAN_RE.findall(clean)]
        if markers != [number]:
            errors.append(f"{path.name}: scan markers {markers!r}; expected exactly [{number}]")
        for cote in COTE_RE.findall(clean):
            if cote.strip() != "57":
                errors.append(f"{path.name}: unexpected cote marker {cote!r}")
        errors.extend(f"{path.name}: {e}" for e in brace_errors(text))
        doubt_rows.extend((number, line, macro, value) for macro, line, value in doubts(text))
    missing = sorted(set(EXPECTED) - set(scans))
    if complete and missing:
        errors.append("Missing scans: " + ", ".join(f"{n:03d}" for n in missing))
    if len(scans) != len(set(scans)):
        errors.append("Duplicate scan numbers in page filenames")
    if scans and scans != list(EXPECTED[:len(scans)]):
        warnings.append("Existing page files are not an uninterrupted prefix of the required sequence")

    inv_path = root / f"{STEM}_inventory.csv"
    inventory_scans = set()
    inventory_rows = 0
    if not inv_path.exists():
        errors.append("Missing inventory CSV")
    else:
        with inv_path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != HEADERS:
                errors.append(f"Inventory headers differ from required columns: {reader.fieldnames!r}")
            for i, row in enumerate(reader, 2):
                inventory_rows += 1
                prefix = f"Inventory line {i}"
                try:
                    number = int(row.get("scan", ""))
                    inventory_scans.add(number)
                except (TypeError, ValueError):
                    errors.append(f"{prefix}: invalid scan")
                    continue
                if row.get("cote") != "57":
                    errors.append(f"{prefix}: cote must be 57")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    errors.append(f"{prefix}: invalid sheet_kind {row.get('sheet_kind')!r}")
                if row.get("kind") not in ELEMENT_KINDS:
                    errors.append(f"{prefix}: invalid kind {row.get('kind')!r}")
                if row.get("transcribed") != "yes":
                    errors.append(f"{prefix}: transcribed is not yes")
                if not row.get("element"):
                    errors.append(f"{prefix}: missing element identifier")
        for number in sorted(set(scans) - inventory_scans):
            errors.append(f"Scan {number:03d} has no inventory rows")
        for number in sorted(inventory_scans - set(scans)):
            errors.append(f"Inventory scan {number:03d} has no page file")

    combined = root / f"{STEM}_transcription.tex"
    if complete and not combined.exists():
        errors.append("Missing combined transcription")
    if combined.exists():
        combined_text = combined.read_text(encoding="utf-8")
        if not re.match(r"\s*\\cotefile\{57\}\s*\\scanpage\{89\}", uncomment(combined_text)):
            errors.append("Combined transcription does not start with cote 57 and scan 89")
        if combined.read_bytes() != combined_bytes(root):
            errors.append("Combined transcription differs from the ordered page-file concatenation")
        if re.search(r"\\(?:documentclass|begin\{document\})", uncomment(combined_text)):
            errors.append("Combined transcription contains a document preamble/environment")
    return errors, warnings, scans, missing, inventory_rows, doubt_rows


def report(root: Path, complete: bool = False):
    errors, warnings, scans, missing, inventory_rows, doubt_rows = validate(root, complete)
    lines = ["# Mechanical validation", "", f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}", "", "These checks do not certify readings, visual coverage, inventory exhaustiveness, or research conclusions.", "", f"Page files: {len(scans)} / {len(EXPECTED)}. Inventory rows: {inventory_rows}. Doubt macro instances: {len(doubt_rows)}.", "", "## Errors", ""]
    lines.extend([f"- {e}" for e in errors] or ["None."])
    lines.extend(["", "## Warnings", ""])
    lines.extend([f"- {w}" for w in warnings] or ["None."])
    if missing:
        lines.extend(["", "Missing expected scans: " + ", ".join(f"{n:03d}" for n in missing) + "."])
    lines.extend(["", "## All doubt macro instances", "", "| Scan | Source line | Macro | Argument |", "|---|---:|---|---|"])
    for number, line, macro, value in doubt_rows:
        escaped_value = value.replace("\n", " ").replace("|", "\\|")
        lines.append(f"| {number:03d} | {line} | `{macro}` | `{escaped_value}` |")
    return "\n".join(lines) + "\n", errors


def zip_members(root: Path):
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(p in EXCLUDE_DIRS for p in relative.parts):
            continue
        if path.suffix.lower() in EXCLUDE_SUFFIXES or path.is_symlink() or not path.is_file():
            continue
        if path.name.startswith(".nfs"):
            continue
        yield path, relative


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("validate")
    check.add_argument("--complete", action="store_true")
    check.add_argument("--report", type=Path)
    combine = sub.add_parser("combine")
    combine.add_argument("--partial", action="store_true")
    checkpoint = sub.add_parser("checkpoint")
    checkpoint.add_argument("number", type=int)
    checkpoint.add_argument("--output-dir", type=Path)
    final = sub.add_parser("final")
    final.add_argument("--output-dir", type=Path)
    sub.add_parser("hashes")
    args = parser.parse_args()
    root = args.root.resolve()

    if args.command == "validate":
        contents, errors = report(root, args.complete)
        if args.report:
            args.report.write_text(contents, encoding="utf-8")
            print(args.report.resolve())
            print(f"Mechanical errors: {len(errors)}")
        else:
            print(contents, end="")
        return int(bool(errors))

    if args.command == "combine":
        progress = root / "progress.log"
        if progress.exists() and re.search(r"^transcription frozen ", progress.read_text(), re.M):
            raise SystemExit("Refusing to rewrite combined transcription after its freeze marker")
        scans = [n for n, _ in page_files(root)]
        if not args.partial and scans != list(EXPECTED):
            raise SystemExit("All 43 ordered page files are required; --partial is for an unfinished working copy")
        target = root / f"{STEM}_transcription.tex"
        target.write_bytes(combined_bytes(root))
        print(target)
        return 0

    if args.command == "hashes":
        paths = [p for _, p in page_files(root)]
        combined = root / f"{STEM}_transcription.tex"
        if combined.exists():
            paths.append(combined)
        for path in paths:
            print(hashlib.sha256(path.read_bytes()).hexdigest(), " ", path.relative_to(root), sep="")
        return 0

    output_dir = (args.output_dir or root.parent).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    if args.command == "checkpoint":
        if args.number < 1:
            raise SystemExit("Checkpoint number must be positive")
        target = output_dir / f"{STEM}_checkpoint_{args.number:02d}.zip"
        first_line = (root / "progress.log").read_text().splitlines()[0]
        started = datetime.strptime(first_line, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
        previous = list(output_dir.glob(f"{STEM}_checkpoint_*.zip"))
        latest = max([started] + [datetime.fromtimestamp(p.stat().st_mtime, timezone.utc) for p in previous])
        permitted = latest + timedelta(hours=1)
        if datetime.now(timezone.utc) < permitted:
            raise SystemExit(f"Hourly checkpoint not due before {permitted.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        existing_numbers = [int(p.stem.rsplit("_", 1)[1]) for p in previous]
        expected_number = max(existing_numbers, default=0) + 1
        if args.number != expected_number:
            raise SystemExit(f"Next checkpoint number must be {expected_number:02d}")
    else:
        target = output_dir / f"{STEM}.zip"
        _, errors = report(root, complete=True)
        if errors:
            raise SystemExit("Final packaging blocked by mechanical validation:\n" + "\n".join(errors))
        for name in [f"{STEM}_doubts.md", f"{STEM}_notes.md", "progress.log"]:
            if not (root / name).is_file():
                raise SystemExit(f"Final packaging requires {name}")
    if target.exists():
        raise SystemExit(f"Refusing to overwrite {target}")
    members = list(zip_members(root))
    with ZipFile(target, "x", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path, relative in members:
            archive.write(path, arcname=relative.as_posix())
    print(f"{target}\n{len(members)} files; {target.stat().st_size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
