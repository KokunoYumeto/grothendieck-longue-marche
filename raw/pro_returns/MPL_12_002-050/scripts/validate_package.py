#!/usr/bin/env python3
"""Structural validation and packaging for MPL_12_002-050.

This utility cannot establish transcription completeness or reading accuracy.
It never sets page-completion or audit status and never changes progress.log.
It reads only files beneath the deliverable root, never the source scans/context.

Typical commands (from any directory):
    python3 work/scripts/validate_package.py --combine
    python3 work/scripts/validate_package.py
    python3 work/scripts/validate_package.py --zip MPL_12_002-050.zip
    python3 work/scripts/validate_package.py --checkpoint --zip CHECKPOINT.zip

--combine is the only operation that writes the combined transcription. It is
refused once frozen_hashes.json exists. ZIP creation includes the deliverable
tree and its support records/scripts, excluding source inputs, images, caches,
and ZIP archives. --checkpoint permits incomplete work to be archived without
claiming that the final structural checks pass; it does not schedule checkpoints.

Optional frozen_hashes.json format, with paths relative to the deliverable root:
    {"pages/MPL_12_002-050_12_scan002.tex": "<64-character SHA-256>", ...}
or:
    {"algorithm": "sha256", "files": {"relative/path": "<SHA-256>", ...}}
The frozen manifest must cover all 47 pages and the combined transcription.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath


PREFIX = "MPL_12_002-050"
SCANS = tuple(n for n in range(2, 51) if n not in {20, 22})
PAGE_NAMES = tuple(f"{PREFIX}_12_scan{n:03d}.tex" for n in SCANS)
COMBINED = f"{PREFIX}_transcription.tex"
INVENTORY = f"{PREFIX}_inventory.csv"
REQUIRED = (COMBINED, f"{PREFIX}_doubts.md", INVENTORY,
            f"{PREFIX}_notes.md", "progress.log")
FIELDS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
SHEET_KINDS = {"text", "reused_typed", "typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note",
                 "insertion", "deletion"}
OMIT_DIRS = {"upload", "uploads", "scans", "context", "sources", "source",
             "__pycache__", ".git", ".venv", "node_modules", "tmp", "temp"}
OMIT_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tif",
                 ".tiff", ".pdf", ".zip", ".pyc", ".pyo"}


def escaped(text: str, pos: int) -> bool:
    """Whether a character is preceded by an odd run of backslashes."""
    n = 0
    pos -= 1
    while pos >= 0 and text[pos] == "\\":
        n += 1
        pos -= 1
    return n % 2 == 1


def uncomment(text: str) -> str:
    """Remove TeX comments without treating escaped percent signs as comments."""
    out = []
    for line in text.splitlines(keepends=True):
        cut = next((i for i, ch in enumerate(line)
                    if ch == "%" and not escaped(line, i)), None)
        out.append(line if cut is None else line[:cut] + "\n")
    return "".join(out)


def brace_errors(text: str) -> list[str]:
    clean = uncomment(text)
    stack: list[int] = []
    errors = []
    line = 1
    for i, ch in enumerate(clean):
        if ch == "\n":
            line += 1
        elif ch in "{}" and not escaped(clean, i):
            if ch == "{":
                stack.append(line)
            elif stack:
                stack.pop()
            else:
                errors.append(f"unmatched closing brace at line {line}")
    if stack:
        errors.append("unmatched opening braces at line(s) "
                      + ", ".join(map(str, stack)))
    return errors


def combined_text(pages: dict[int, str]) -> str:
    return "\n\n".join(pages[n].rstrip() for n in SCANS) + "\n"


def inspect_pages(root: Path, errors: list[str]) -> dict[int, str]:
    directory = root / "pages"
    found = {p.name for p in directory.glob("*.tex")} if directory.exists() else set()
    expected = set(PAGE_NAMES)
    for name in sorted(expected - found):
        errors.append(f"missing page: pages/{name}")
    for name in sorted(found - expected):
        errors.append(f"unexpected page: pages/{name}")
    pages = {}
    for scan, name in zip(SCANS, PAGE_NAMES):
        path = directory / name
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"pages/{name}: cannot read UTF-8: {exc}")
            continue
        pages[scan] = text
        clean = uncomment(text).strip()
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if markers != [str(scan)] and markers != [f"{scan:03d}"]:
            errors.append(f"pages/{name}: expected exactly one scanpage for {scan}; "
                          f"found {markers}")
        start = (rf"\\cotefile\s*\{{\s*12\s*\}}\s*" if scan == SCANS[0] else "")
        start += rf"\\scanpage\s*\{{\s*0*{scan}\s*\}}"
        if not re.match(start, clean):
            errors.append(f"pages/{name}: wrong opening marker(s)")
        for detail in brace_errors(text):
            errors.append(f"pages/{name}: {detail}")
        if re.search(r"\\(?:documentclass|includegraphics)\b", clean):
            errors.append(f"pages/{name}: contains documentclass or includegraphics")
    return pages


def inspect_inventory(root: Path, errors: list[str]) -> int:
    path = root / INVENTORY
    if not path.is_file():
        return 0  # The required-file check reports it.
    seen_scans = set()
    seen_elements = set()
    sheet_kind_by_scan = {}
    count = 0
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != FIELDS:
                errors.append(f"{INVENTORY}: columns must be exactly {FIELDS}")
                return 0
            for lineno, row in enumerate(reader, 2):
                count += 1
                label = f"{INVENTORY}:{lineno}"
                if None in row or any(v is None for v in row.values()):
                    errors.append(f"{label}: malformed CSV row")
                    continue
                if row["cote"].strip() != "12":
                    errors.append(f"{label}: cote is not 12")
                try:
                    scan = int(row["scan"].strip())
                except ValueError:
                    errors.append(f"{label}: invalid scan number")
                    continue
                if scan not in SCANS:
                    errors.append(f"{label}: unexpected scan {scan}")
                seen_scans.add(scan)
                if row["transcribed"].strip() != "yes":
                    errors.append(f"{label}: transcribed is not yes")
                kind = row["sheet_kind"].strip()
                if kind not in SHEET_KINDS:
                    errors.append(f"{label}: unsupported sheet_kind {kind!r}")
                if scan in sheet_kind_by_scan and sheet_kind_by_scan[scan] != kind:
                    errors.append(f"{label}: inconsistent sheet_kind for scan {scan}")
                sheet_kind_by_scan[scan] = kind
                if row["kind"].strip() not in ELEMENT_KINDS:
                    errors.append(f"{label}: unsupported element kind {row['kind']!r}")
                element = row["element"].strip()
                if not element:
                    errors.append(f"{label}: empty element identifier")
                key = (scan, element)
                if key in seen_elements:
                    errors.append(f"{label}: duplicate element {element!r} for scan {scan}")
                seen_elements.add(key)
                for field in ("position", "first_words_or_objects"):
                    if not row[field].strip():
                        errors.append(f"{label}: empty {field}")
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{INVENTORY}: cannot read inventory: {exc}")
    missing = sorted(set(SCANS) - seen_scans)
    if missing:
        errors.append("inventory has no rows for scan(s): " + ", ".join(map(str, missing)))
    return count


def inspect_hashes(root: Path, manifest: Path, errors: list[str]) -> int | None:
    if not manifest.is_file():
        return None
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("manifest must be a JSON object")
        if "files" in data:
            if data.get("algorithm", "sha256").lower() not in {"sha256", "sha-256"}:
                raise ValueError("manifest algorithm is not SHA-256")
            data = data["files"]
        if not isinstance(data, dict):
            raise ValueError("files must be an object mapping relative paths to hashes")
        expected = {f"pages/{name}" for name in PAGE_NAMES} | {COMBINED}
        missing = sorted(expected - set(data))
        if missing:
            errors.append("frozen manifest omits: " + ", ".join(missing))
        checked = 0
        for name, digest in data.items():
            relative = PurePosixPath(name)
            if relative.is_absolute() or ".." in relative.parts or "\\" in name:
                errors.append(f"frozen manifest has unsafe path: {name!r}")
                continue
            path = root.joinpath(*relative.parts)
            if not isinstance(digest, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", digest):
                errors.append(f"frozen manifest has invalid SHA-256 for {name!r}")
                continue
            if not path.is_file() or path.is_symlink():
                errors.append(f"frozen file missing or symlink: {name}")
                continue
            if hashlib.sha256(path.read_bytes()).hexdigest() != digest.lower():
                errors.append(f"FROZEN HASH MISMATCH: {name}")
            checked += 1
        return checked
    except (OSError, UnicodeError, ValueError, TypeError, AttributeError) as exc:
        errors.append(f"cannot read frozen manifest {manifest.name}: {exc}")
        return 0


def zip_files(root: Path, destination: Path) -> int:
    selected = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root)
        if any(part.lower() in OMIT_DIRS for part in relative.parts[:-1]):
            continue
        if path.suffix.lower() in OMIT_SUFFIXES or path.resolve() == destination.resolve():
            continue
        if path.name.startswith("."):
            continue
        selected.append((path, relative.as_posix()))
    if destination.exists():
        raise FileExistsError(f"refusing to overwrite existing ZIP: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=9) as archive:
        for path, relative in selected:
            archive.write(path, relative)
    return len(selected)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="deliverable directory (default: the script's work/ parent)")
    parser.add_argument("--combine", action="store_true",
                        help="explicitly assemble the combined transcription before validation")
    parser.add_argument("--frozen-hashes", type=Path,
                        help="optional manifest; default ROOT/frozen_hashes.json")
    parser.add_argument("--zip", type=Path, dest="zip_path",
                        help="write a new ZIP if checks pass; never overwrite")
    parser.add_argument("--checkpoint", action="store_true",
                        help="allow incomplete work in a ZIP; does not mark it final or audited")
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = args.frozen_hashes or root / "frozen_hashes.json"
    errors: list[str] = []
    pages = inspect_pages(root, errors)
    if args.combine:
        if manifest.exists():
            errors.append("--combine refused: a frozen manifest exists")
        elif errors or len(pages) != len(SCANS):
            errors.append("--combine refused: page structural checks have errors")
        else:
            (root / COMBINED).write_text(combined_text(pages), encoding="utf-8")
            print(f"Assembled {COMBINED} from {len(pages)} page files.")
    for name in REQUIRED:
        path = root / name
        if not path.is_file():
            errors.append(f"missing required file: {name}")
        elif path.stat().st_size == 0:
            errors.append(f"empty required file: {name}")
    if (root / COMBINED).is_file():
        try:
            text = (root / COMBINED).read_text(encoding="utf-8")
            if len(pages) == len(SCANS) and text != combined_text(pages):
                errors.append("combined transcription does not match the ordered page files "
                              "(including the documented blank-line separators)")
            for detail in brace_errors(text):
                errors.append(f"{COMBINED}: {detail}")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read combined transcription: {exc}")
    rows = inspect_inventory(root, errors)
    hashes = inspect_hashes(root, manifest, errors)
    print(f"Structural scope: {len(pages)}/47 pages; {rows} inventory elements.")
    print("Visual accuracy, line completeness, and claimed audit status require human/model "
          "inspection against the images; this utility does not verify them.")
    print("Frozen manifest: " + ("absent (hash check not performed)." if hashes is None
                                 else f"{hashes} file hashes checked."))
    if errors:
        print(f"Structural validation found {len(errors)} issue(s):")
        for error in errors:
            print(f"  - {error}")
    else:
        print("Structural validation passed.")
    if args.zip_path:
        if errors and not args.checkpoint:
            print("ZIP not written: resolve structural issues or use --checkpoint for "
                  "an explicitly incomplete archive.")
        else:
            try:
                count = zip_files(root, args.zip_path)
                kind = "Checkpoint" if args.checkpoint else "Deliverable"
                print(f"{kind} ZIP written: {args.zip_path} ({count} files).")
            except (OSError, ValueError) as exc:
                print(f"ZIP creation failed: {exc}", file=sys.stderr)
                return 2
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
