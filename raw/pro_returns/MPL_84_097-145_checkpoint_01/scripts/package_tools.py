#!/usr/bin/env python3
"""Mechanical checks and archives for MPL_84_097-145.

This program does not perform OCR, assess readings, or mark pages done/audited.
The root transcription agent alone supplies and audits the manuscript text.
It never opens the source scans or the context archive.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

PACKAGE = "MPL_84_097-145"
EXPECTED = tuple(n for n in range(97, 146) if n != 123)
PAGE_RE = re.compile(r"MPL_84_097-145_84_scan(\d{3})\.tex$")
INVENTORY_FIELDS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
STAMP_FORMAT = "%Y-%m-%d %H:%M:%S UTC"


class PackageError(RuntimeError):
    pass


def now() -> str:
    return datetime.now(timezone.utc).strftime(STAMP_FORMAT)


def read_log(root: Path) -> str:
    path = root / "progress.log"
    if not path.is_file():
        raise PackageError("progress.log does not exist")
    return path.read_text(encoding="utf-8")


def append_log(root: Path, text: str) -> None:
    with (root / "progress.log").open("a", encoding="utf-8") as stream:
        stream.write(text.rstrip("\n") + "\n")


def pages(root: Path) -> dict[int, Path]:
    result: dict[int, Path] = {}
    for path in sorted((root / "pages").glob("*.tex")):
        match = PAGE_RE.fullmatch(path.name)
        if not match:
            raise PackageError(f"Unrecognized page filename: {path.name}")
        scan = int(match.group(1))
        if scan not in EXPECTED:
            raise PackageError(f"Unexpected scan file: {path.name}")
        if scan in result:
            raise PackageError(f"Duplicate scan {scan}")
        result[scan] = path
    return dict(sorted(result.items()))


def uncomment(text: str) -> str:
    """Remove TeX comments, honoring escaped percent signs."""
    output: list[str] = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for pos, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            before = pos - 1
            while before >= 0 and line[before] == "\\":
                backslashes += 1
                before -= 1
            if backslashes % 2 == 0:
                cut = pos
                break
        output.append(line[:cut] + ("\n" if cut < len(line) else ""))
    return "".join(output)


def brace_errors(text: str) -> list[str]:
    text = uncomment(text)
    stack: list[int] = []
    errors: list[str] = []
    line = 1
    index = 0
    while index < len(text):
        char = text[index]
        if char == "\\":
            # Escaped braces and escaped backslashes are not delimiters.
            if index + 1 < len(text) and text[index + 1] in "{}\\%":
                index += 2
                continue
        if char == "\n":
            line += 1
        elif char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                errors.append(f"unmatched closing brace at line {line}")
        index += 1
    errors.extend(f"unmatched opening brace at line {line}" for line in stack)
    return errors


def combined_text(page_paths: dict[int, Path]) -> str:
    if not page_paths:
        raise PackageError("No page files exist")
    chunks = [p.read_text(encoding="utf-8").strip() for p in page_paths.values()]
    text = "\n\n".join(chunks) + "\n"
    if not re.match(r"\\cotefile\s*\{84\}", text):
        text = "\\cotefile{84}\n" + text
    return text


def combine(root: Path) -> None:
    if "transcription frozen " in read_log(root):
        raise PackageError("Transcription is frozen; combine will not overwrite it")
    target = root / f"{PACKAGE}_transcription.tex"
    target.write_text(combined_text(pages(root)), encoding="utf-8")
    print(f"Combined transcription: {target}")


def validate(root: Path, complete: bool, require_combined: bool = True) -> list[str]:
    errors: list[str] = []
    try:
        page_paths = pages(root)
    except PackageError as exc:
        return [str(exc)]
    if complete:
        missing = sorted(set(EXPECTED) - page_paths.keys())
        if missing:
            errors.append("Missing pages: " + ", ".join(f"{n:03}" for n in missing))
    for scan, path in page_paths.items():
        text = path.read_text(encoding="utf-8")
        clean = uncomment(text)
        markers = re.findall(r"\\scanpage\s*\{(\d+)\}", clean)
        if markers != [str(scan)]:
            errors.append(f"scan {scan:03}: scanpage markers are {markers!r}")
        errors.extend(f"scan {scan:03}: {e}" for e in brace_errors(text))
        if re.search(r"\\(?:documentclass|includegraphics|input|include)\b", clean):
            errors.append(f"scan {scan:03}: forbidden preamble/image/external-file macro")
        if "\\begin{document}" in clean or "\\end{document}" in clean:
            errors.append(f"scan {scan:03}: document environment in fragment")
        cote = re.findall(r"\\cotefile\s*\{([^}]*)\}", clean)
        if cote and (scan != 97 or cote != ["84"]):
            errors.append(f"scan {scan:03}: unexpected cotefile markers {cote!r}")
    inv_path = root / f"{PACKAGE}_inventory.csv"
    covered: set[int] = set()
    keys: set[tuple[int, str]] = set()
    if not inv_path.is_file():
        errors.append("Inventory file does not exist")
    else:
        with inv_path.open(newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != INVENTORY_FIELDS:
                errors.append(f"Wrong inventory header: {reader.fieldnames!r}")
            for row_number, row in enumerate(reader, 2):
                label = f"inventory row {row_number}"
                if None in row or any(value is None for value in row.values()):
                    errors.append(f"{label}: inconsistent column count")
                    continue
                try:
                    scan = int(row.get("scan", ""))
                except ValueError:
                    errors.append(f"{label}: invalid scan")
                    continue
                if row.get("cote") != "84":
                    errors.append(f"{label}: cote is not 84")
                if scan not in page_paths:
                    errors.append(f"{label}: scan {scan:03} has no page file")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    errors.append(f"{label}: unrecognized sheet_kind")
                if row.get("kind") not in ELEMENT_KINDS:
                    errors.append(f"{label}: unrecognized kind")
                if row.get("transcribed") != "yes":
                    errors.append(f"{label}: transcribed is not yes")
                key = (scan, row.get("element", ""))
                if not key[1] or key in keys:
                    errors.append(f"{label}: empty or duplicate element identifier")
                keys.add(key)
                covered.add(scan)
        for scan in sorted(page_paths.keys() - covered):
            errors.append(f"scan {scan:03}: no inventory rows")
    if require_combined:
        combined = root / f"{PACKAGE}_transcription.tex"
        if not combined.is_file():
            errors.append("Combined transcription does not exist")
        elif page_paths:
            if combined.read_text(encoding="utf-8") != combined_text(page_paths):
                errors.append("Combined transcription differs from ordered page fragments")
            if not re.match(r"\\cotefile\{84\}\s*\\scanpage\{97\}", combined.read_text(encoding="utf-8")):
                errors.append("Combined transcription does not start with cote 84, scan 97")
    return errors


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def transcription_paths(root: Path) -> list[Path]:
    return [*pages(root).values(), root / f"{PACKAGE}_transcription.tex"]


def freeze(root: Path) -> None:
    log = read_log(root)
    if "context opened " in log:
        raise PackageError("Context has already been opened; refusing a new freeze")
    if "transcription frozen " in log or (root / "freeze.sha256").exists():
        raise PackageError("A freeze is already recorded; use verify-frozen")
    errors = validate(root, complete=True)
    for scan in EXPECTED:
        if not re.search(rf"^84 scan {scan:03} done \d{{4}}-", log, re.M):
            errors.append(f"scan {scan:03}: completion log line missing")
        if not re.search(rf"^scan {scan:03} audited \d{{4}}-", log, re.M):
            errors.append(f"scan {scan:03}: audit log line missing")
    if errors:
        raise PackageError("\n".join(errors))
    lines = [f"{digest(path)}  {path.relative_to(root).as_posix()}" for path in transcription_paths(root)]
    (root / "freeze.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")
    append_log(root, "\n".join("sha256 " + line for line in lines))
    append_log(root, f"transcription frozen {now()}")
    print(f"Recorded SHA-256 hashes for {len(lines)} files; transcription files unchanged")


def verify_frozen(root: Path, record: bool = False) -> None:
    manifest = root / "freeze.sha256"
    if not manifest.is_file():
        raise PackageError("freeze.sha256 does not exist")
    expected_names = {p.relative_to(root).as_posix() for p in transcription_paths(root)}
    actual_names: set[str] = set()
    errors: list[str] = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            errors.append("Malformed freeze manifest line")
            continue
        recorded_hash, name = match.groups()
        if name in actual_names:
            errors.append(f"Duplicate freeze manifest entry: {name}")
        actual_names.add(name)
        path = root / name
        if name not in expected_names or not path.is_file():
            errors.append(f"Unexpected or missing frozen file: {name}")
        elif digest(path) != recorded_hash:
            errors.append(f"HASH CHANGED: {name}")
    if actual_names != expected_names:
        errors.append("Freeze manifest file set differs from transcription file set")
    if len(expected_names) != 49:
        errors.append("Expected 48 pages and one combined transcription")
    if errors:
        raise PackageError("\n".join(errors))
    if record:
        append_log(root, f"frozen transcription hashes unchanged {now()}")
    print(f"All {len(actual_names)} frozen transcription hashes unchanged")


def archive_members(root: Path) -> list[Path]:
    excluded_dirs = {"upload", "uploads", "scans", "context", "sources", "__pycache__", ".git"}
    excluded_suffixes = {".zip", ".jpg", ".jpeg", ".png", ".tiff", ".tif", ".pyc"}
    members: list[Path] = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part.lower() in excluded_dirs for part in relative.parts):
            continue
        if path.is_symlink():
            raise PackageError(f"Refusing archive symlink: {relative}")
        if path.is_file() and path.suffix.lower() not in excluded_suffixes:
            members.append(path)
    return members


def write_archive(root: Path, destination: Path) -> None:
    if destination.exists():
        raise PackageError(f"Archive already exists; never overwriting: {destination}")
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in archive_members(root):
            archive.write(path, path.relative_to(root).as_posix())
    print(f"Archive created: {destination}")
    print(f"Archive SHA-256: {digest(destination)}")
    print("This command does not upload the archive; persist it using the approved Library create tool.")


def checkpoint(root: Path) -> None:
    log = read_log(root)
    entries = re.findall(r"^checkpoint (\d+) assembled (.+)$", log, re.M)
    baseline = entries[-1][1] if entries else log.splitlines()[0]
    try:
        baseline_dt = datetime.strptime(baseline, STAMP_FORMAT).replace(tzinfo=timezone.utc)
    except ValueError as exc:
        raise PackageError("Cannot parse checkpoint baseline UTC timestamp") from exc
    elapsed = (datetime.now(timezone.utc) - baseline_dt).total_seconds()
    if elapsed < 3600:
        raise PackageError(f"Hourly checkpoint is not due: {int(3600 - elapsed)} seconds remaining")
    prior_numbers = [int(n) for n, _ in entries]
    for path in root.parent.glob(f"{PACKAGE}_checkpoint_*.zip"):
        match = re.fullmatch(re.escape(PACKAGE) + r"_checkpoint_(\d+)\.zip", path.name)
        if match:
            prior_numbers.append(int(match.group(1)))
    number = max(prior_numbers, default=0) + 1
    target = root.parent / f"{PACKAGE}_checkpoint_{number:02}.zip"
    append_log(root, f"checkpoint {number:02} assembled {now()}")
    try:
        write_archive(root, target)
    except Exception:
        append_log(root, f"checkpoint {number:02} assembly failed {now()}")
        raise


def final_archive(root: Path) -> None:
    errors = validate(root, complete=True)
    for suffix in ("doubts.md", "notes.md"):
        path = root / f"{PACKAGE}_{suffix}"
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"Required nonempty deliverable missing: {path.name}")
    if errors:
        raise PackageError("\n".join(errors))
    verify_frozen(root, record=True)
    append_log(root, f"final package assembled {now()}")
    write_archive(root, root.parent / f"{PACKAGE}.zip")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("combine", help="Combine existing page files; forbidden after freeze")
    check_parser = sub.add_parser("check", help="Mechanical structure check only")
    check_parser.add_argument("--partial", action="store_true", help="Allow not-yet-written scans")
    check_parser.add_argument("--without-combined", action="store_true")
    sub.add_parser("freeze", help="Record hashes after all required done/audited log lines")
    verify_parser = sub.add_parser("verify-frozen", help="Check frozen SHA-256 hashes")
    verify_parser.add_argument("--record", action="store_true", help="Append successful check to log")
    sub.add_parser("checkpoint", help="Create next checkpoint only when at least one hour is due")
    sub.add_parser("final", help="Validate structure and hashes, then create final ZIP")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "combine":
            combine(root)
        elif args.command == "check":
            errors = validate(root, complete=not args.partial, require_combined=not args.without_combined)
            if errors:
                raise PackageError("\n".join(errors))
            print("Mechanical checks passed; this does not certify the visual transcription")
        elif args.command == "freeze":
            freeze(root)
        elif args.command == "verify-frozen":
            verify_frozen(root, record=args.record)
        elif args.command == "checkpoint":
            checkpoint(root)
        elif args.command == "final":
            final_archive(root)
    except (PackageError, OSError, csv.Error, UnicodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
