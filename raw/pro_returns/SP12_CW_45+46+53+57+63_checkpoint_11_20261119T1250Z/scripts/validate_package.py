#!/usr/bin/env python3
"""Validate output structure and optionally package an archival transcription.

This utility checks structure, filename coverage, literal page inclusion, and
optional frozen hashes. It does not verify transcription, collation, readings,
historical claims, or any other editorial content. It never opens source images.

Expected-map TSV: rows are ordered; use a ``page_file`` column containing each
output .tex filename. An optional ``scan`` column checks inventory coverage.
``filename`` or ``scan`` can instead identify scans whose stems equal the output
page stems. Only filename columns are used; source files are never opened.

Freeze manifests accept sha256sum format, or TSV with ``path`` and ``sha256``
columns. Manifest paths are relative to OUTPUT_ROOT and may not escape it.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import zipfile


COLLATION_HEADERS = [
    "folder", "their_page", "our_scan", "line", "their_reading",
    "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H",
    "confidence",
]
INVENTORY_HEADERS = [
    "scan", "sheet_kind", "hand", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
PAGE_COLUMNS = (
    "page_file", "page_filename", "page_tex", "tex_file", "tex_filename",
    "output_file", "output_filename",
)
SCAN_COLUMNS = ("scan", "scan_file", "scan_filename", "our_scan")
NAME_COLUMNS = PAGE_COLUMNS + ("filename", "file") + SCAN_COLUMNS
CACHE_DIRS = {
    "__pycache__", ".cache", "cache", "caches", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", ".ipynb_checkpoints", ".git",
    ".svn", ".hg", "node_modules",
}
SOURCE_DIRS = {
    "source", "sources", "source_attachments", "source-attachments",
    "attachments", "attachment", "input", "inputs", "originals",
    "witness", "witnesses", "scan", "scans", "images",
}
# Restrict the archive to text deliverable and metadata formats. Attachment
# formats (including images, PDFs, office files, and nested archives) are never
# included. Keep all originals, including plain-text sources, outside the output
# tree or in one of SOURCE_DIRS.
OUTPUT_SUFFIXES = {
    ".tex", ".md", ".tsv", ".csv", ".log", ".txt", ".json",
    ".sha256", ".sha256sum", ".sha256sums", ".sum", ".manifest",
}
OUTPUT_BASENAMES = {"sha256sums", "sha256sum", "checksums", "manifest"}
HEX_SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")
CHECKPOINT_NAME = re.compile(r"checkpoint", re.IGNORECASE)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.facts: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    def print(self) -> None:
        for message in self.facts:
            print(f"OK: {message}")
        for message in self.warnings:
            print(f"WARNING: {message}")
        for message in self.errors:
            print(f"ERROR: {message}", file=sys.stderr)
        print(
            "Scope: structural and integrity checks only; editorial content "
            "has not been verified."
        )


def safe_regular_file(path: Path, root: Path | None = None) -> bool:
    """Reject symlinks, including symlinked parents within the output root."""
    try:
        if not stat.S_ISREG(path.lstat().st_mode):
            return False
        if root is not None:
            relative = path.relative_to(root)
            current = root
            for part in relative.parts[:-1]:
                current = current / part
                if current.is_symlink():
                    return False
        return True
    except (OSError, ValueError):
        return False


def read_text(path: Path, report: Report, root: Path | None = None) -> str | None:
    if not safe_regular_file(path, root):
        report.error(f"Missing, non-regular, or symlinked file: {path}")
        return None
    try:
        text = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        report.error(f"Cannot read UTF-8 file {path}: {exc}")
        return None
    if not text.strip():
        report.error(f"Empty file: {path}")
    return text


def table_rows(
    path: Path,
    delimiter: str,
    report: Report,
    expected_headers: list[str] | None = None,
    root: Path | None = None,
) -> tuple[list[str], list[tuple[int, list[str]]]]:
    text = read_text(path, report, root)
    if text is None or not text.strip():
        return [], []
    try:
        rows = list(csv.reader(text.splitlines(keepends=True), delimiter=delimiter, strict=True))
    except csv.Error as exc:
        report.error(f"Malformed delimited file {path.name}: {exc}")
        return [], []
    if not rows:
        return [], []
    headers = rows[0]
    if not headers or any(not header.strip() for header in headers):
        report.error(f"Blank header in {path.name}")
    if len(set(headers)) != len(headers):
        report.error(f"Duplicate header in {path.name}")
    if expected_headers is not None and headers != expected_headers:
        report.error(
            f"Unexpected headers/order in {path.name}; expected "
            + delimiter.join(expected_headers)
        )
    valid_rows: list[tuple[int, list[str]]] = []
    for number, row in enumerate(rows[1:], start=2):
        if not row or not any(cell.strip() for cell in row):
            continue
        if len(row) != len(headers):
            report.error(f"Wrong field count in {path.name}, record {number}")
            continue
        valid_rows.append((number, row))
    return headers, valid_rows


def normalized_header(value: str) -> str:
    return value.strip().lower().replace(" ", "_").replace("-", "_")


def filename_only(value: str) -> str:
    return PurePosixPath(value.strip().replace("\\", "/")).name


def expected_map(
    path: Path, report: Report
) -> tuple[list[str], set[str] | None]:
    headers, rows = table_rows(path, "\t", report)
    normalized = [normalized_header(header) for header in headers]
    if len(set(normalized)) != len(normalized):
        report.error(f"Ambiguous normalized headers in expected map: {path}")
        return [], None
    column = next((name for name in NAME_COLUMNS if name in normalized), None)
    if column is None:
        report.error(
            "Expected map needs a page_file column (preferred), filename, "
            "or scan filename column."
        )
        return [], None
    scan_column = next((name for name in SCAN_COLUMNS if name in normalized), None)
    pages: list[str] = []
    scans: set[str] | None = set() if scan_column is not None else None
    seen: set[str] = set()
    for number, row in rows:
        value = row[normalized.index(column)].strip()
        name = filename_only(value)
        if not name or name in {".", ".."} or any(ord(c) < 32 for c in name):
            report.error(f"Invalid filename in expected map, record {number}")
            continue
        if column in PAGE_COLUMNS and Path(name).suffix.lower() != ".tex":
            report.error(f"Expected output filename is not .tex, map record {number}")
            continue
        page_name = name if Path(name).suffix.lower() == ".tex" else Path(name).stem + ".tex"
        if page_name in seen:
            report.error(f"Duplicate expected page filename: {page_name}")
        else:
            seen.add(page_name)
            pages.append(page_name)
        if scans is not None and scan_column is not None:
            scan_name = filename_only(row[normalized.index(scan_column)])
            if not scan_name:
                report.error(f"Blank scan filename in expected map, record {number}")
            else:
                scans.add(scan_name)
    if not pages:
        report.error("Expected map contains no usable page filenames.")
    return pages, scans


def validate_tables(root: Path, prefix: str, report: Report) -> set[str]:
    collation = root / f"{prefix}_collation.tsv"
    headers, rows = table_rows(collation, "\t", report, COLLATION_HEADERS, root)
    if headers == COLLATION_HEADERS:
        seen: dict[tuple[str, ...], int] = {}
        for number, row in rows:
            key = tuple(row)
            if key in seen:
                report.error(
                    f"Duplicate collation row at records {seen[key]} and {number}"
                )
            else:
                seen[key] = number
        report.facts.append(f"Read {len(rows)} collation records.")

    inventory = root / f"{prefix}_inventory.csv"
    headers, rows = table_rows(inventory, ",", report, INVENTORY_HEADERS, root)
    scan_names: set[str] = set()
    if headers == INVENTORY_HEADERS:
        if not rows:
            report.error("Inventory has no data records.")
        for number, row in rows:
            if row[-1].strip().lower() != "yes":
                report.error(f"Inventory record {number}: transcribed must be yes.")
            scan_name = filename_only(row[0])
            if not scan_name:
                report.error(f"Inventory record {number}: scan filename is blank.")
            else:
                scan_names.add(scan_name)
        report.facts.append(f"Read {len(rows)} inventory records.")

    headers, rows = table_rows(root / "CHECK_EVENTS.tsv", "\t", report, root=root)
    if headers and not rows:
        report.error("CHECK_EVENTS.tsv has no event records.")
    return scan_names


def validate_pages(
    root: Path, prefix: str, map_path: Path | None, inventory_scans: set[str],
    report: Report,
) -> None:
    page_dir = root / "pages"
    if page_dir.is_symlink() or not page_dir.is_dir():
        report.error("Missing or symlinked pages directory.")
        return
    pages = {
        path.name: path for path in page_dir.glob("*.tex")
        if safe_regular_file(path, root)
    }
    for path in page_dir.glob("*.tex"):
        if not safe_regular_file(path, root):
            report.error(f"Non-regular or symlinked page file: {path.name}")
    if not pages:
        report.error("No page files found in pages/*.tex.")
    order = sorted(pages)
    if map_path is not None:
        order, expected_scans = expected_map(map_path, report)
        missing = set(order) - set(pages)
        extra = set(pages) - set(order)
        for name in sorted(missing):
            report.error(f"Expected page file is missing: pages/{name}")
        for name in sorted(extra):
            report.error(f"Page file is absent from expected map: pages/{name}")
        if expected_scans is not None:
            for name in sorted(expected_scans - inventory_scans):
                report.error(f"Expected scan is missing from inventory: {name}")
            for name in sorted(inventory_scans - expected_scans):
                report.error(f"Inventory scan is absent from expected map: {name}")
    else:
        report.warning(
            "No expected map supplied; coverage against source filenames was "
            "not checked. Combined-file order is checked lexicographically."
        )
    combined = read_text(root / f"{prefix}_transcription.tex", report, root)
    cursor = 0
    included = 0
    for name in order:
        if name not in pages:
            continue
        content = read_text(pages[name], report, root)
        if content is None or not content.strip() or combined is None:
            continue
        # read_text normalizes newlines; ignore only boundary line endings.
        content = content.strip("\n")
        position = combined.find(content, cursor)
        if position < 0:
            if combined.find(content) >= 0:
                report.error(f"Page content appears out of order in combined file: {name}")
            else:
                report.error(f"Literal page content missing from combined file: {name}")
        else:
            cursor = position + len(content)
            included += 1
    report.facts.append(f"Located {included}/{len(order)} page texts in combined-file order.")


def parse_manifest(path: Path, report: Report) -> list[tuple[str, str]]:
    text = read_text(path, report)
    if text is None or not text.strip():
        return []
    lines = text.splitlines()
    first = next((line for line in lines if line.strip()), "")
    first_fields = [normalized_header(field) for field in first.split("\t")]
    entries: list[tuple[str, str]] = []
    if "path" in first_fields and "sha256" in first_fields:
        headers, rows = table_rows(path, "\t", report)
        normalized = [normalized_header(header) for header in headers]
        for number, row in rows:
            digest = row[normalized.index("sha256")].strip()
            name = row[normalized.index("path")].strip()
            if not HEX_SHA256.fullmatch(digest) or not name:
                report.error(f"Invalid freeze manifest record {number}: {path.name}")
                continue
            entries.append((name, digest.lower()))
    else:
        for number, line in enumerate(lines, start=1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            match = re.fullmatch(r"([0-9a-fA-F]{64})[ \t]+\*?(.+)", line)
            if not match:
                report.error(f"Invalid SHA-256 manifest line {number}: {path.name}")
                continue
            entries.append((match.group(2), match.group(1).lower()))
    if not entries:
        report.error(f"Freeze manifest has no usable entries: {path.name}")
    return entries


def validate_manifest(root: Path, manifest: Path, report: Report) -> None:
    checked = 0
    seen: set[str] = set()
    for name, expected in parse_manifest(manifest, report):
        relative = PurePosixPath(name.replace("\\", "/"))
        if relative.is_absolute() or ".." in relative.parts or not relative.parts:
            report.error(f"Unsafe path in freeze manifest: {name}")
            continue
        if re.match(r"^[A-Za-z]:", name):
            report.error(f"Absolute drive path in freeze manifest: {name}")
            continue
        normalized = relative.as_posix()
        if normalized in seen:
            report.error(f"Duplicate path in freeze manifest: {normalized}")
            continue
        seen.add(normalized)
        target = root.joinpath(*relative.parts)
        if not safe_regular_file(target, root):
            report.error(f"Missing, non-regular, or symlinked frozen file: {normalized}")
            continue
        if excluded_file(target.relative_to(root)) is not None:
            report.error(f"Freeze manifest references excluded/source-like file: {normalized}")
            continue
        try:
            digest = hashlib.sha256()
            with target.open("rb") as handle:
                for block in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(block)
            if digest.hexdigest() != expected:
                report.error(f"Frozen SHA-256 mismatch: {normalized}")
            else:
                checked += 1
        except OSError as exc:
            report.error(f"Cannot hash frozen file {normalized}: {exc}")
    report.facts.append(f"Verified {checked} frozen hashes from {manifest.name}.")


def excluded_directory(name: str) -> str | None:
    lower = name.lower()
    if CHECKPOINT_NAME.search(name):
        return "checkpoint"
    if lower in CACHE_DIRS or lower.startswith(".cache"):
        return "cache/version-control directory"
    if lower in SOURCE_DIRS:
        return "source directory"
    return None


def excluded_file(relative: Path) -> str | None:
    for part in relative.parts[:-1]:
        reason = excluded_directory(part)
        if reason:
            return reason
    name = relative.name
    lower = name.lower()
    if CHECKPOINT_NAME.search(name):
        return "checkpoint"
    if relative.suffix.lower() == ".zip":
        return "ZIP archive"
    if lower.startswith(".") or lower.endswith(("~", ".bak", ".tmp", ".pyc")):
        return "cache/temporary file"
    if relative.suffix.lower() not in OUTPUT_SUFFIXES and lower not in OUTPUT_BASENAMES:
        return "attachment or unsupported output format"
    return None


def package(root: Path, destination: Path, report: Report) -> None:
    if destination.exists() or destination.is_symlink():
        report.error(f"Refusing to overwrite existing ZIP destination: {destination}")
        return
    selected: list[Path] = []
    skipped: list[tuple[str, str]] = []
    for directory, dirs, files in os.walk(root, followlinks=False):
        base = Path(directory)
        keep_dirs: list[str] = []
        for name in sorted(dirs):
            path = base / name
            reason = "symlink" if path.is_symlink() else excluded_directory(name)
            if reason:
                skipped.append((path.relative_to(root).as_posix() + "/", reason))
            else:
                keep_dirs.append(name)
        dirs[:] = keep_dirs
        for name in sorted(files):
            path = base / name
            relative = path.relative_to(root)
            reason = excluded_file(relative)
            if not safe_regular_file(path, root):
                reason = "symlink or non-regular file"
            if reason:
                skipped.append((relative.as_posix(), reason))
            else:
                selected.append(path)
    if not selected:
        report.error("No eligible output files to package.")
        return
    created = False
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(destination, mode="x", compression=zipfile.ZIP_DEFLATED) as archive:
            created = True
            for path in sorted(selected, key=lambda item: item.relative_to(root).as_posix()):
                if not safe_regular_file(path, root):
                    raise OSError(f"Output changed to a symlink/non-regular file: {path.name}")
                archive.write(path, arcname=path.relative_to(root).as_posix())
        report.facts.append(f"Created ZIP with {len(selected)} files: {destination}")
        for name, reason in skipped:
            report.warning(f"Excluded from ZIP ({reason}): {name}")
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        report.error(f"ZIP creation failed: {exc}")
        if created:
            try:
                destination.unlink()
            except OSError as cleanup_exc:
                report.warning(f"Could not remove incomplete ZIP: {cleanup_exc}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", required=True, type=Path, help="Output-only directory to validate.")
    parser.add_argument("--prefix", default="SP12_CW_45+46+53+57+63", help="Deliverable filename prefix.")
    parser.add_argument("--expected-map", type=Path, help="Ordered metadata TSV; never opens named source files.")
    parser.add_argument(
        "--freeze-manifest", "--sha-manifest", action="append", default=[], type=Path,
        help="SHA-256 manifest; may be supplied more than once.",
    )
    parser.add_argument("--zip", dest="zip_path", type=Path, help="Create a new ZIP after successful validation.")
    args = parser.parse_args()
    report = Report()
    root_input = args.root.expanduser()
    if root_input.is_symlink() or not root_input.is_dir():
        report.error(f"Output root must be an existing, non-symlinked directory: {root_input}")
        report.print()
        return 1
    root = root_input.resolve()
    if not args.prefix or args.prefix in {".", ".."} or any(c in args.prefix for c in "/\\\x00"):
        report.error("Prefix must be a nonempty filename component.")
        report.print()
        return 1
    for suffix in ("changes.md", "doubts.md", "notes.md"):
        read_text(root / f"{args.prefix}_{suffix}", report, root)
    read_text(root / "progress.log", report, root)
    inventory_scans = validate_tables(root, args.prefix, report)
    validate_pages(root, args.prefix, args.expected_map, inventory_scans, report)
    for manifest in args.freeze_manifest:
        validate_manifest(root, manifest, report)
    if not args.freeze_manifest:
        report.warning("No freeze manifest supplied; frozen-state integrity was not checked.")
    if args.zip_path and not report.errors:
        package(root, args.zip_path.expanduser().absolute(), report)
    elif args.zip_path:
        report.warning("ZIP was not created because validation failed.")
    report.print()
    if report.errors:
        print(f"FAILED: {len(report.errors)} structural/integrity error(s).", file=sys.stderr)
        return 1
    print("PASS: requested structural/integrity checks completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
