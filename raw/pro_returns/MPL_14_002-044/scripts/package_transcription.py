#!/usr/bin/env python3
"""Mechanical assembly, validation, freezing, and ZIP packaging.

This utility performs no OCR or image access and makes no judgment about readings.
Run with --help for commands. It reads transcription text only when invoked.
"""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
from pathlib import Path
import re
import sys
import zipfile


PREFIX = "MPL_14_002-044"
COTE = "14"
EXPECTED_SCANS = tuple(n for n in range(2, 45) if n not in (18, 23, 43))
INVENTORY_COLUMNS = (
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"
}
SCAN_RE = re.compile(r"\\scanpage\s*\{\s*(\d+)\s*\}")
COTE_RE = re.compile(r"\\cotefile\s*\{\s*([^{}]+?)\s*\}")
FORBIDDEN_RE = re.compile(
    r"\\(?:documentclass|usepackage|includegraphics|includepdf|input|include)\b"
    r"|\\(?:begin|end)\s*\{\s*document\s*\}"
)
ENV_RE = re.compile(r"\\(begin|end)\s*\{([^{}]+)\}")
FILE_RE = re.compile(rf"{PREFIX}_14_scan(\d{{3}})\.tex")


class ValidationError(Exception):
    pass


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def uncomment(text: str) -> str:
    """Remove unescaped TeX comments, preserving line positions."""
    lines = []
    for line in text.splitlines(keepends=True):
        for index, char in enumerate(line):
            if char != "%":
                continue
            preceding_backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                preceding_backslashes += 1
                cursor -= 1
            if preceding_backslashes % 2 == 0:
                line = line[:index] + ("\n" if line.endswith("\n") else "")
                break
        lines.append(line)
    return "".join(lines)


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def check_tex(text: str, label: str) -> list[str]:
    """Structural lint only; this is deliberately not a TeX parser."""
    errors = []
    clean = uncomment(text)
    for match in FORBIDDEN_RE.finditer(clean):
        errors.append(f"{label}:{line_number(clean, match.start())}: forbidden command {match.group(0)}")

    braces = []
    cursor = 0
    while cursor < len(clean):
        char = clean[cursor]
        if char == "\\":
            # Control symbols such as \{, \}, \%, and \\ consume the next char.
            if cursor + 1 < len(clean) and not clean[cursor + 1].isalpha():
                cursor += 2
                continue
        if char == "{":
            braces.append(cursor)
        elif char == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"{label}:{line_number(clean, cursor)}: unmatched closing brace")
        cursor += 1
    for opening in braces:
        errors.append(f"{label}:{line_number(clean, opening)}: unmatched opening brace")

    environments = []
    for match in ENV_RE.finditer(clean):
        action, name = match.groups()
        if action == "begin":
            environments.append((name, match.start()))
        elif not environments:
            errors.append(f"{label}:{line_number(clean, match.start())}: unmatched end of {name}")
        elif environments[-1][0] != name:
            expected, _ = environments[-1]
            errors.append(f"{label}:{line_number(clean, match.start())}: end of {name}, expected {expected}")
        else:
            environments.pop()
    for name, opening in environments:
        errors.append(f"{label}:{line_number(clean, opening)}: unclosed environment {name}")
    return errors


def page_paths(root: Path, partial: bool = False) -> dict[int, Path]:
    folder = root / "pages"
    paths = {}
    errors = []
    for path in sorted(folder.glob("*.tex")):
        match = FILE_RE.fullmatch(path.name)
        if not match:
            errors.append(f"Unexpected page filename: {path.name}")
            continue
        scan = int(match.group(1))
        if scan not in EXPECTED_SCANS:
            errors.append(f"Unexpected scan page: {scan:03d}")
        elif scan in paths:
            errors.append(f"Duplicate scan page: {scan:03d}")
        else:
            paths[scan] = path
    missing = set(EXPECTED_SCANS) - set(paths)
    if not partial and missing:
        errors.append("Missing pages: " + ", ".join(f"{n:03d}" for n in sorted(missing)))
    if partial and paths:
        last = max(paths)
        gaps = {n for n in EXPECTED_SCANS if n <= last} - set(paths)
        if gaps:
            errors.append("Nonsequential partial pages; gaps: " + ", ".join(f"{n:03d}" for n in sorted(gaps)))
    if not paths:
        errors.append("No completed page files found")
    if errors:
        raise ValidationError("\n".join(errors))
    return dict(sorted(paths.items()))


def read_pages(root: Path, partial: bool = False) -> dict[int, str]:
    pages = {}
    errors = []
    for scan, path in page_paths(root, partial).items():
        text = path.read_bytes().decode("utf-8")
        clean = uncomment(text)
        markers = [int(n) for n in SCAN_RE.findall(clean)]
        if markers != [scan]:
            errors.append(f"{path.name}: expected one scanpage{{{scan}}}, found {markers}")
        cotes = COTE_RE.findall(clean)
        if scan == EXPECTED_SCANS[0]:
            if cotes not in ([], [COTE]):
                errors.append(f"{path.name}: invalid cote markers {cotes}")
            if cotes and not clean.lstrip().startswith("\\cotefile{14}"):
                errors.append(f"{path.name}: cotefile marker must precede all page content")
        elif cotes:
            errors.append(f"{path.name}: cotefile marker occurs after the first page")
        errors.extend(check_tex(text, path.name))
        pages[scan] = text
    if errors:
        raise ValidationError("\n".join(errors))
    return pages


def expected_combined(pages: dict[int, str]) -> str:
    first = next(iter(pages.values()))
    prefix = "" if COTE_RE.search(uncomment(first)) else "\\cotefile{14}\n"
    # Page text is retained verbatim; separators are added between fragments.
    return prefix + "\n\n".join(pages.values()) + ("" if list(pages.values())[-1].endswith("\n") else "\n")


def frozen_manifest(root: Path) -> Path:
    return root / "records" / "frozen_hashes.txt"


def require_unfrozen(root: Path) -> None:
    if frozen_manifest(root).exists():
        raise ValidationError("The transcription is frozen; assembly and a second freeze are disabled")


def assemble(root: Path, partial: bool) -> None:
    require_unfrozen(root)
    pages = read_pages(root, partial)
    target = root / f"{PREFIX}_transcription.tex"
    target.write_text(expected_combined(pages), encoding="utf-8", newline="")
    print(f"Assembled {len(pages)} pages: {target}")


def check_inventory(root: Path, scans: set[int]) -> tuple[list[str], int]:
    path = root / f"{PREFIX}_inventory.csv"
    if not path.exists():
        return [f"Missing inventory: {path.name}"], 0
    errors = []
    content = path.read_text(encoding="utf-8-sig")
    reader = csv.DictReader(io.StringIO(content, newline=""))
    if tuple(reader.fieldnames or []) != INVENTORY_COLUMNS:
        errors.append(f"{path.name}: columns must be exactly {','.join(INVENTORY_COLUMNS)}")
        return errors, 0
    rows = 0
    seen = set()
    for line, row in enumerate(reader, start=2):
        rows += 1
        where = f"{path.name}:{line}"
        if None in row:
            errors.append(f"{where}: extra CSV fields")
        if any(row.get(column) is None for column in INVENTORY_COLUMNS):
            errors.append(f"{where}: missing CSV fields")
            continue
        if row["cote"].strip() != COTE:
            errors.append(f"{where}: cote must be 14")
        try:
            scan = int(row["scan"])
        except ValueError:
            errors.append(f"{where}: scan must be an integer")
            continue
        seen.add(scan)
        if scan not in scans:
            errors.append(f"{where}: scan {scan} has no completed page file")
        if row["sheet_kind"] not in SHEET_KINDS:
            errors.append(f"{where}: unknown sheet_kind {row['sheet_kind']!r}")
        if row["kind"] not in ELEMENT_KINDS:
            errors.append(f"{where}: unknown kind {row['kind']!r}")
        if row["transcribed"] != "yes":
            errors.append(f"{where}: transcribed must equal yes")
        for column in ("element", "position", "first_words_or_objects"):
            if not row[column].strip():
                errors.append(f"{where}: empty {column}")
    missing = scans - seen
    if missing:
        errors.append("Inventory has no elements for scans: " + ", ".join(f"{n:03d}" for n in sorted(missing)))
    return errors, rows


def validate(root: Path, partial: bool, require_notes: bool = False) -> dict[int, Path]:
    pages = read_pages(root, partial)
    errors = []
    combined = root / f"{PREFIX}_transcription.tex"
    if not combined.exists():
        errors.append(f"Missing combined transcription: {combined.name}")
    else:
        text = combined.read_bytes().decode("utf-8")
        if text != expected_combined(pages):
            errors.append(f"{combined.name}: combined content differs from ordered page files")
        clean = uncomment(text)
        if COTE_RE.findall(clean) != [COTE]:
            errors.append(f"{combined.name}: expected exactly one cotefile{{14}} marker")
        if [int(n) for n in SCAN_RE.findall(clean)] != list(pages):
            errors.append(f"{combined.name}: scan markers are not in the expected order")
        errors.extend(check_tex(text, combined.name))
    inventory_errors, rows = check_inventory(root, set(pages))
    errors.extend(inventory_errors)
    for filename in (f"{PREFIX}_doubts.md", "progress.log"):
        if not (root / filename).is_file():
            errors.append(f"Missing deliverable: {filename}")
    if require_notes and not (root / f"{PREFIX}_notes.md").is_file():
        errors.append(f"Missing research notes: {PREFIX}_notes.md")
    if errors:
        raise ValidationError("\n".join(errors))
    print(f"Mechanical validation passed: {len(pages)} pages; {rows} inventory rows")
    return page_paths(root, partial)


def hash_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def freeze(root: Path) -> None:
    require_unfrozen(root)
    paths = validate(root, partial=False)
    log = root / "progress.log"
    log_text = log.read_text(encoding="utf-8")
    audited = {int(n) for n in re.findall(r"(?m)^scan\s+(\d+)\s+audited\s+", log_text)}
    missing_audits = set(EXPECTED_SCANS) - audited
    if missing_audits:
        raise ValidationError("Cannot freeze before all audits are logged: " + ", ".join(f"{n:03d}" for n in sorted(missing_audits)))
    if re.search(r"(?m)^context opened\s+", log_text):
        raise ValidationError("Context opening is already logged; refusal to create a new freeze record")
    targets = list(paths.values()) + [root / f"{PREFIX}_transcription.tex"]
    records = [(hash_file(path), path.relative_to(root).as_posix()) for path in targets]
    manifest = frozen_manifest(root)
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text("".join(f"{digest}  {relative}\n" for digest, relative in records), encoding="utf-8")
    stamp = now()
    with log.open("a", encoding="utf-8") as out:
        if log_text and not log_text.endswith("\n"):
            out.write("\n")
        for digest, relative in records:
            out.write(f"SHA256 {relative} {digest}\n")
        out.write(f"transcription frozen {stamp}\n")
    print(f"Frozen {len(records)} files at {stamp}")


def verify(root: Path, log_result: bool = False) -> None:
    manifest = frozen_manifest(root)
    if not manifest.is_file():
        raise ValidationError("Missing frozen hash manifest")
    expected_names = {f"pages/{PREFIX}_14_scan{n:03d}.tex" for n in EXPECTED_SCANS}
    expected_names.add(f"{PREFIX}_transcription.tex")
    entries = {}
    errors = []
    for number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), start=1):
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            errors.append(f"{manifest.name}:{number}: malformed manifest row")
            continue
        digest, relative = match.groups()
        if relative in entries:
            errors.append(f"Duplicate manifest entry: {relative}")
        entries[relative] = digest
    if set(entries) != expected_names:
        errors.append("Manifest file set does not equal the 40 pages plus combined transcription")
    for relative, digest in entries.items():
        path = root / relative
        if relative not in expected_names:
            continue
        if not path.is_file():
            errors.append(f"Missing frozen file: {relative}")
        elif hash_file(path) != digest:
            errors.append(f"Frozen hash changed: {relative}")
    if errors:
        raise ValidationError("\n".join(errors))
    stamp = now()
    if log_result:
        with (root / "progress.log").open("a", encoding="utf-8") as out:
            out.write(f"frozen hashes verified unchanged {stamp}\n")
    print(f"All {len(entries)} frozen SHA-256 hashes are unchanged ({stamp})")


def zip_paths(root: Path) -> list[Path]:
    # Deliberately include authored text, scripts, records, and logs only.
    # Exclude supplied archives, image sources, prior ZIPs, and transient caches.
    excluded_extensions = {".zip", ".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".pdf", ".pyc", ".pyo"}
    excluded_dirs = {"upload", "scans", "context", "sources", "inputs", "__pycache__", ".git", "node_modules"}
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root)
        if any(part in excluded_dirs or part.startswith(".") for part in relative.parts):
            continue
        if path.suffix.lower() in excluded_extensions:
            continue
        files.append(path)
    return files


def package(root: Path, output: Path, checkpoint: bool) -> None:
    if output.exists():
        raise ValidationError(f"Refusing to overwrite an existing ZIP: {output}")
    expected_name = re.compile(rf"{PREFIX}_checkpoint_\d{{2,}}\.zip") if checkpoint else re.compile(rf"{PREFIX}\.zip")
    if not expected_name.fullmatch(output.name):
        raise ValidationError("Output filename must follow the requested final/checkpoint naming convention")
    if not checkpoint:
        validate(root, partial=False, require_notes=True)
        verify(root)
    files = zip_paths(root)
    if not files:
        raise ValidationError("No files selected for ZIP")
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in files:
                archive.write(path, path.relative_to(root).as_posix())
        with zipfile.ZipFile(output) as archive:
            bad = archive.testzip()
            if bad is not None:
                raise ValidationError(f"ZIP integrity check failed at {bad}")
    except Exception:
        # Leave any partial file for diagnosis; never silently overwrite a ZIP.
        raise
    print(f"Created {'checkpoint' if checkpoint else 'final'} ZIP with {len(files)} files: {output}")
    print(f"ZIP SHA256: {hash_file(output)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Deliverables directory")
    commands = parser.add_subparsers(dest="command", required=True)
    p_assemble = commands.add_parser("assemble", help="Combine page files without modifying them")
    p_assemble.add_argument("--partial", action="store_true", help="Accept a sequential completed prefix")
    p_validate = commands.add_parser("validate", help="Check files, markers, syntax, and inventory")
    p_validate.add_argument("--partial", action="store_true")
    p_validate.add_argument("--require-notes", action="store_true")
    commands.add_parser("freeze", help="Record hashes after all 40 audits, before context opening")
    p_verify = commands.add_parser("verify", help="Compare all frozen hashes")
    p_verify.add_argument("--log", action="store_true", help="Append successful verification to progress.log")
    p_zip = commands.add_parser("zip", help="Package authored deliverables, records, and scripts")
    p_zip.add_argument("output", type=Path)
    p_zip.add_argument("--checkpoint", action="store_true", help="Package current work without completeness/freeze requirements")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "assemble":
            assemble(root, args.partial)
        elif args.command == "validate":
            validate(root, args.partial, args.require_notes)
        elif args.command == "freeze":
            freeze(root)
        elif args.command == "verify":
            verify(root, args.log)
        elif args.command == "zip":
            package(root, args.output.resolve(), args.checkpoint)
    except (ValidationError, OSError, UnicodeError, csv.Error) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
