#!/usr/bin/env python3
"""Structural checks and packaging for MPL_46_002-048.

This script does not read scan images, perform OCR, inspect context sources, or
judge transcription readings. It never modifies pages or progress.log. A final
human visual audit remains indispensable.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import re
import sys
import tempfile
import zipfile
from pathlib import Path

PREFIX = "MPL_46_002-048"
COTE = "46"
SCANS = tuple(n for n in range(2, 49) if n not in {24, 25, 26, 35, 37})
COLUMNS = ("cote", "scan", "sheet_kind", "element", "kind", "position",
           "first_words_or_objects", "transcribed")
KINDS = {"text", "display", "diagram", "drawing", "margin note",
         "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
EXCLUDED_DIRS = {"upload", "uploads", "scans", "context", "inputs", "input",
                 "sources", "__pycache__", ".cache", ".git", "node_modules",
                 "library_helpers"}
EXCLUDED_NAMES = {"MPL_46_002-048_scans.zip", "MPL_46_002-048_context.zip",
                  "PROMPT(20261117-101412).md"}

def page_path(root: Path, scan: int) -> Path:
    return root / "pages" / f"{PREFIX}_{COTE}_scan{scan:03d}.tex"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def pages_present(root: Path) -> list[int]:
    known = {page_path(root, n).name: n for n in SCANS}
    unknown = [p.name for p in (root / "pages").glob("*.tex") if p.name not in known]
    if unknown:
        raise ValueError(f"Unexpected .tex page files: {unknown}")
    return [n for n in SCANS if page_path(root, n).is_file()]

def combined_bytes(root: Path, scans: list[int]) -> bytes:
    # Exact documented combine rule: strip only terminal CR/LF, then two LF
    # between pages and one LF at EOF. Page contents are otherwise unchanged.
    return b"\n\n".join(page_path(root, n).read_bytes().rstrip(b"\r\n")
                       for n in scans) + b"\n"

def uncommented_tex(text: str) -> str:
    lines = []
    for line in text.splitlines():
        cut = len(line)
        for i, char in enumerate(line):
            if char == "%":
                count, j = 0, i - 1
                while j >= 0 and line[j] == "\\":
                    count += 1
                    j -= 1
                if count % 2 == 0:
                    cut = i
                    break
        lines.append(line[:cut])
    return "\n".join(lines)

def tex_structure(path: Path, errors: list[str]) -> None:
    text = uncommented_tex(path.read_text(encoding="utf-8"))
    braces = []
    for i, char in enumerate(text):
        if char not in "{}":
            continue
        count, j = 0, i - 1
        while j >= 0 and text[j] == "\\":
            count += 1
            j -= 1
        if count % 2:
            continue
        if char == "{":
            braces.append(i)
        elif not braces:
            errors.append(f"{path.name}: unmatched closing brace at character {i}")
        else:
            braces.pop()
    if braces:
        errors.append(f"{path.name}: {len(braces)} unmatched opening braces")
    stack = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", text):
        command, env = match.groups()
        if command == "begin":
            stack.append(env)
        elif not stack or stack[-1] != env:
            errors.append(f"{path.name}: unmatched/misnested end of {env}")
        else:
            stack.pop()
    if stack:
        errors.append(f"{path.name}: unclosed environments {stack}")
    for opening, closing in [(r"\[", r"\]"), (r"\(", r"\)")]:
        if text.count(opening) != text.count(closing):
            errors.append(f"{path.name}: unequal {opening}/{closing} counts")
    if re.search(r"\\(?:documentclass|usepackage)\b", text):
        errors.append(f"{path.name}: preamble command in fragment")

def read_manifest(path: Path) -> dict[str, str]:
    """Accept standard sha256sum lines, or 'SHA256 digest path' log lines."""
    result = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"(?:SHA-?256\s+)?([0-9a-fA-F]{64})\s+\*?(.+)$", line)
        if not match:
            # A progress log may also contain ordinary status lines.
            if path.name == "progress.log":
                continue
            raise ValueError(f"{path.name}:{number}: invalid hash-manifest line")
        digest, filename = match.groups()
        if filename in result and result[filename].lower() != digest.lower():
            raise ValueError(f"Conflicting hashes for {filename}")
        result[filename] = digest.lower()
    if not result:
        raise ValueError(f"No SHA-256 entries in {path}")
    return result

def verify_hashes(root: Path, manifest: Path) -> list[str]:
    errors = []
    hashes = read_manifest(manifest)
    for name, digest in hashes.items():
        path = Path(name)
        if path.is_absolute():
            try:
                path.relative_to(root)
            except ValueError:
                errors.append(f"Hash target outside work root: {name}")
                continue
        else:
            path = root / path
        try:
            path.resolve().relative_to(root.resolve())
        except ValueError:
            errors.append(f"Hash target escapes work root: {name}")
            continue
        if not path.is_file():
            errors.append(f"Hash target missing: {name}")
        elif sha256(path) != digest:
            errors.append(f"SHA-256 mismatch: {name}")
    return errors

def validate(root: Path, partial: bool, manifest: Path | None) -> list[str]:
    errors = []
    scans = pages_present(root)
    if not partial and scans != list(SCANS):
        errors.append("Missing pages: " + ", ".join(f"{n:03d}" for n in SCANS
                                                 if n not in scans))
    if partial and scans and scans != list(SCANS[:len(scans)]):
        errors.append("Partial pages are not a contiguous prefix of scan order")
    for scan in scans:
        path = page_path(root, scan)
        text = uncommented_tex(path.read_text(encoding="utf-8"))
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", text)
        if markers != [str(scan)]:
            errors.append(f"{path.name}: scan markers {markers}, expected [{scan}]")
        cotes = re.findall(r"\\cotefile\s*\{\s*([^{}]+)\s*\}", text)
        if cotes and cotes != [COTE]:
            errors.append(f"{path.name}: invalid cote marker(s) {cotes}")
        if scan != SCANS[0] and cotes:
            errors.append(f"{path.name}: cote marker repeated after first page")
        tex_structure(path, errors)
    combined = root / f"{PREFIX}_transcription.tex"
    if scans and combined.is_file():
        text = uncommented_tex(combined.read_text(encoding="utf-8")).lstrip()
        if not re.match(r"\\cotefile\s*\{46\}\s*\\scanpage\s*\{2\}", text):
            errors.append("Combined fragment does not start with cote 46 / scan 2")
        order = [int(x) for x in re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", text)]
        if order != scans:
            errors.append(f"Combined scan order differs: {order}")
        if combined.read_bytes() != combined_bytes(root, scans):
            errors.append("Combined bytes differ from documented page concatenation")
    elif not partial:
        errors.append("Combined transcription is missing")
    inventory = root / f"{PREFIX}_inventory.csv"
    if inventory.is_file():
        with inventory.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if tuple(reader.fieldnames or ()) != COLUMNS:
                errors.append(f"Inventory columns differ: {reader.fieldnames}")
            coverage = set()
            elements = set()
            for rownum, row in enumerate(reader, 2):
                try:
                    scan = int(row.get("scan", ""))
                except (ValueError, TypeError):
                    errors.append(f"Inventory row {rownum}: invalid scan")
                    continue
                coverage.add(scan)
                if scan not in scans:
                    errors.append(f"Inventory row {rownum}: no page file for scan {scan}")
                if row.get("cote") != COTE:
                    errors.append(f"Inventory row {rownum}: invalid cote")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    errors.append(f"Inventory row {rownum}: invalid sheet_kind")
                if row.get("kind") not in KINDS:
                    errors.append(f"Inventory row {rownum}: invalid element kind")
                if row.get("transcribed") != "yes":
                    errors.append(f"Inventory row {rownum}: transcribed is not yes")
                for column in ("element", "position", "first_words_or_objects"):
                    if not row.get(column, "").strip():
                        errors.append(f"Inventory row {rownum}: blank {column}")
                key = (scan, row.get("element"))
                if key in elements:
                    errors.append(f"Inventory row {rownum}: duplicate element {key}")
                elements.add(key)
        if set(scans) != coverage:
            errors.append(f"Inventory/page coverage differs: {sorted(set(scans)^coverage)}")
    elif scans or not partial:
        errors.append("Inventory is missing")
    if not partial:
        for name in (f"{PREFIX}_doubts.md", f"{PREFIX}_notes.md", "progress.log"):
            if not (root / name).is_file():
                errors.append(f"Required file missing: {name}")
    if manifest:
        errors.extend(verify_hashes(root, manifest))
    return errors

def package(root: Path, output: Path) -> tuple[int, int]:
    root = root.resolve()
    output = output.resolve()
    if output.exists():
        raise ValueError(f"Refusing to overwrite existing ZIP: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    paths = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_DIRS or part.startswith("library_helpers")
               for part in relative.parts):
            continue
        if path.name in EXCLUDED_NAMES or path.suffix.lower() in {".zip", ".pyc", ".pyo"}:
            continue
        if path.is_symlink():
            raise ValueError(f"Refusing to package symlink: {relative}")
        if path.is_file() and path.resolve() != output:
            # Source scan copies are never deliverables.
            if re.match(r"MPL_46_002-048_46_scan\d{3}(?:_[ab])?\.jpg$", path.name):
                continue
            paths.append(path)
    descriptor, temporary = tempfile.mkstemp(prefix=output.name + ".", suffix=".tmp",
                                            dir=output.parent)
    import os
    os.close(descriptor)
    temporary = Path(temporary)
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED,
                             compresslevel=9) as archive:
            for path in paths:
                archive.write(path, path.relative_to(root).as_posix())
        with zipfile.ZipFile(temporary) as archive:
            bad = archive.testzip()
            if bad is not None:
                raise ValueError(f"ZIP CRC error: {bad}")
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    return len(paths), output.stat().st_size

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parent.parent)
    sub = parser.add_subparsers(dest="command", required=True)
    combine = sub.add_parser("combine")
    combine.add_argument("--partial", action="store_true")
    check = sub.add_parser("validate")
    check.add_argument("--partial", action="store_true")
    check.add_argument("--hashes", type=Path)
    hashes = sub.add_parser("hashes")
    hashes.add_argument("--write", type=Path)
    verify = sub.add_parser("verify-hashes")
    verify.add_argument("manifest", type=Path)
    pack = sub.add_parser("package")
    pack.add_argument("output", type=Path)
    pack.add_argument("--partial", action="store_true")
    pack.add_argument("--hashes", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "combine":
            scans = pages_present(root)
            if not scans:
                raise ValueError("No page files to combine")
            if not args.partial and scans != list(SCANS):
                raise ValueError("Cannot combine final transcription: pages missing")
            path = root / f"{PREFIX}_transcription.tex"
            path.write_bytes(combined_bytes(root, scans))
            print(f"Combined {len(scans)} page files: {path}")
        elif args.command in {"validate", "package"}:
            errors = validate(root, args.partial, args.hashes)
            if errors:
                print("\n".join("ERROR: " + e for e in errors), file=sys.stderr)
                return 1
            print("Structural checks passed; this does not establish visual accuracy.")
            if args.command == "package":
                count, size = package(root, args.output)
                print(f"Created {args.output.resolve()} ({count} files, {size} bytes)")
        elif args.command == "hashes":
            paths = [page_path(root, n) for n in SCANS]
            paths.append(root / f"{PREFIX}_transcription.tex")
            missing = [str(p) for p in paths if not p.is_file()]
            if missing:
                raise ValueError(f"Cannot hash final transcription: missing {missing}")
            text = "".join(f"{sha256(p)}  {p.relative_to(root).as_posix()}\n" for p in paths)
            if args.write:
                if args.write.exists():
                    raise ValueError(f"Refusing to overwrite hash baseline: {args.write}")
                args.write.parent.mkdir(parents=True, exist_ok=True)
                args.write.write_text(text, encoding="utf-8")
                print(f"Wrote {len(paths)} SHA-256 values to {args.write}")
            else:
                print(text, end="")
        elif args.command == "verify-hashes":
            errors = verify_hashes(root, args.manifest)
            if errors:
                print("\n".join("ERROR: " + e for e in errors), file=sys.stderr)
                return 1
            print("All frozen SHA-256 values are unchanged.")
    except (OSError, ValueError, csv.Error) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

