#!/usr/bin/env python3
"""Create an image-free package of the current work deliverables.

Usage:
    python scripts/package_deliverables.py WORK_DIR OUTPUT.zip
    python scripts/package_deliverables.py WORK_DIR OUTPUT.zip --hashes

The helper accepts incomplete page sets for scheduled checkpoints. Scheduling
belongs to its caller: invoking this script creates the requested archive now.
It reads selected files as bytes and performs no interpretation of their text.

Allowed members are specified page files in pages/, known
primary/support files, top-level Markdown documentation, and scripts/*.py.
Other directories, images, archives, and caches are omitted. Unrecognized files
with potential deliverable extensions in an examined directory cause failure.
Symlinks are never included. Paths are retained inside the ZIP.

--hashes regenerates work_dir/hashes.tsv atomically and includes it in the ZIP.
Without that option, an existing hashes.tsv must exactly cover the selected
members and contain matching digests. The manifest excludes itself.
--overwrite authorizes replacing an existing output ZIP; each publication uses
an atomic filesystem operation. The output must be outside work_dir.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import stat
import sys
import tempfile
import zipfile
from pathlib import Path


PREFIX = "SP64_C13_15+16"
PAGE_NAMES = {
    *(f"15_scan{number}.tex" for number in (180, 183, 184, 185, 187, 189, 190, 191, 192, 193, 194)),
    *(f"16_scan{number:03d}.tex" for number in range(3, 17)),
}
PRIMARY_FILES = {
    f"{PREFIX}_transcription.tex",
    f"{PREFIX}_collation.tsv",
    f"{PREFIX}_inventory.csv",
    "decisions.tsv",
    "CHECK_EVENTS.tsv",
    "progress.log",
    "hashes.tsv",
}
SUPPORT_FILES = {
    "changes_records.tsv", "notation.tsv", "remaining_doubts.tsv",
    "abbreviations.tsv", "audit_notes.tsv", "certainty_only.tsv",
}
POTENTIAL_DELIVERABLE_SUFFIXES = {".tex", ".md", ".tsv", ".csv", ".log", ".py"}
EXCLUDED_DIRECTORIES = {
    "source", "sources", "witness", "witnesses", "hua", "scan", "scans",
    "image", "images", "crop", "crops", "views", "checkpoint", "checkpoints",
    "deliveries", "archive", "archives", "backup", "backups", "__pycache__",
    ".git", ".venv", "tmp", "temp", "cache", "caches",
}


class PackageError(Exception):
    """An actionable structural or publication error."""


def within(path: Path, directory: Path) -> bool:
    try:
        path.relative_to(directory)
        return True
    except ValueError:
        return False


def select_members(work: Path) -> dict[str, Path]:
    selected: dict[str, Path] = {}
    unexpected: list[str] = []
    page_locations: dict[str, str] = {}

    def add(path: Path) -> None:
        relative = path.relative_to(work).as_posix()
        if path.is_symlink():
            raise PackageError(f"A selected file is a symlink: {relative}")
        if not path.is_file():
            raise PackageError(f"A selected path is not a regular file: {relative}")
        if not within(path.resolve(), work):
            raise PackageError(f"A selected file resolves outside work_dir: {relative}")
        if path.name in PAGE_NAMES:
            previous = page_locations.get(path.name)
            if previous is not None:
                raise PackageError(f"A page has two package locations: {previous}, {relative}")
            page_locations[path.name] = relative
        selected[relative] = path

    for path in sorted(work.iterdir(), key=lambda item: item.name):
        if path.name in EXCLUDED_DIRECTORIES:
            continue
        if path.name in {"pages", "scripts"}:
            if path.is_symlink():
                raise PackageError(f"An allowed directory is a symlink: {path.name}")
            if not path.is_dir():
                raise PackageError(f"Expected a directory: {path.name}")
            for child in sorted(path.iterdir(), key=lambda item: item.name):
                if child.name in EXCLUDED_DIRECTORIES:
                    continue
                allowed = (
                    path.name == "pages" and child.name in PAGE_NAMES
                ) or (
                    path.name == "scripts" and child.suffix == ".py"
                )
                if allowed:
                    add(child)
                elif child.suffix.lower() in POTENTIAL_DELIVERABLE_SUFFIXES:
                    unexpected.append(child.relative_to(work).as_posix())
            continue
        if path.is_dir():
            continue
        if path.name in PRIMARY_FILES | SUPPORT_FILES or path.suffix == ".md":
            add(path)
        elif path.suffix.lower() in POTENTIAL_DELIVERABLE_SUFFIXES:
            unexpected.append(path.name)
    if unexpected:
        raise PackageError(
            "Unrecognized potential deliverables require an explicit allowlist decision: "
            + ", ".join(unexpected)
        )
    if not selected:
        raise PackageError("No allowed deliverables were found.")
    return selected


def read_snapshot(path: Path, work: Path) -> bytes:
    relative = path.relative_to(work).as_posix()
    if path.is_symlink() or not within(path.resolve(), work):
        raise PackageError(f"Selected path changed or became a symlink: {relative}")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(path, flags)
    with os.fdopen(descriptor, "rb") as handle:
        before = os.fstat(handle.fileno())
        if not stat.S_ISREG(before.st_mode):
            raise PackageError(f"Selected path is not a regular file: {relative}")
        payload = handle.read()
        after = os.fstat(handle.fileno())
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise PackageError(f"A selected file changed while being packaged: {relative}")
    return payload


def make_manifest(payloads: dict[str, bytes]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(("file", "sha256"))
    for name, payload in sorted(payloads.items()):
        if name != "hashes.tsv":
            writer.writerow((name, hashlib.sha256(payload).hexdigest()))
    return stream.getvalue().encode("utf-8")


def verify_existing_manifest(payloads: dict[str, bytes]) -> None:
    try:
        reader = csv.reader(
            io.StringIO(payloads["hashes.tsv"].decode("utf-8-sig"), newline=""),
            delimiter="\t", strict=True,
        )
        if next(reader, None) != ["file", "sha256"]:
            raise PackageError("Existing hashes.tsv has an unexpected header; use --hashes to regenerate it.")
        manifest: dict[str, str] = {}
        for row_number, row in enumerate(reader, start=2):
            if len(row) != 2 or not row[0] or row[0] in manifest:
                raise PackageError(f"Existing hashes.tsv has an invalid row {row_number}; use --hashes.")
            manifest[row[0]] = row[1]
    except (UnicodeError, csv.Error) as exc:
        raise PackageError("Existing hashes.tsv cannot be parsed; use --hashes to regenerate it.") from exc
    expected = set(payloads) - {"hashes.tsv"}
    if set(manifest) != expected:
        raise PackageError("Existing hashes.tsv does not exactly cover the selected members; use --hashes.")
    for name in sorted(expected):
        if manifest[name].lower() != hashlib.sha256(payloads[name]).hexdigest():
            raise PackageError(f"Existing hashes.tsv has a stale digest for {name}; use --hashes.")


def temporary_file(parent: Path, prefix: str) -> Path:
    descriptor, name = tempfile.mkstemp(dir=parent, prefix=prefix, suffix=".tmp")
    os.close(descriptor)
    return Path(name)


def atomic_publish(temporary: Path, target: Path, overwrite: bool) -> None:
    if overwrite:
        os.replace(temporary, target)
    else:
        try:
            os.link(temporary, target)
        except FileExistsError as exc:
            raise PackageError(f"Output already exists; use --overwrite to replace it: {target}") from exc
        temporary.unlink()


def create_package(work: Path, output: Path, regenerate_hashes: bool, overwrite: bool) -> tuple[int, int, str]:
    if not work.is_dir():
        raise PackageError("work_dir is unavailable or is not a directory.")
    if within(output, work):
        raise PackageError("The output ZIP must be outside work_dir.")
    if output.suffix.lower() != ".zip":
        raise PackageError("The output filename must end in .zip.")
    if output.is_symlink():
        raise PackageError("The output ZIP path must not be a symlink.")
    if output.exists() and (not overwrite or not output.is_file()):
        raise PackageError("The output already exists; a regular file can be replaced with --overwrite.")
    selected = select_members(work)
    payloads = {
        name: read_snapshot(path, work)
        for name, path in sorted(selected.items())
        if name != "hashes.tsv" or not regenerate_hashes
    }
    if regenerate_hashes:
        payloads["hashes.tsv"] = make_manifest(payloads)
    elif "hashes.tsv" in payloads:
        verify_existing_manifest(payloads)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_zip = temporary_file(output.parent, f".{output.name}.")
    temporary_manifest: Path | None = None
    try:
        with zipfile.ZipFile(
            temporary_zip, "w", compression=zipfile.ZIP_DEFLATED,
            compresslevel=9, allowZip64=True,
        ) as archive:
            for name, payload in sorted(payloads.items()):
                entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                entry.create_system = 3
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, payload, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        with temporary_zip.open("rb+") as handle:
            zip_digest = hashlib.sha256(handle.read()).hexdigest()
            os.fsync(handle.fileno())
        size = temporary_zip.stat().st_size
        if regenerate_hashes:
            manifest_target = work / "hashes.tsv"
            if manifest_target.is_symlink():
                raise PackageError("hashes.tsv became a symlink; refusing to replace it.")
            temporary_manifest = temporary_file(work, ".hashes.tsv.")
            with temporary_manifest.open("wb") as handle:
                handle.write(payloads["hashes.tsv"])
                handle.flush()
                os.fsync(handle.fileno())
            atomic_publish(temporary_manifest, manifest_target, overwrite=True)
        atomic_publish(temporary_zip, output, overwrite=overwrite)
        return len(payloads), size, zip_digest
    finally:
        for path in (temporary_zip, temporary_manifest):
            if path is not None:
                try:
                    path.unlink(missing_ok=True)
                except OSError:
                    pass


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("work_dir", type=Path)
    parser.add_argument("output_zip", type=Path)
    parser.add_argument("--hashes", action="store_true", help="Regenerate and include hashes.tsv for the current members")
    parser.add_argument("--overwrite", action="store_true", help="Atomically replace an existing output ZIP")
    args = parser.parse_args(argv)
    try:
        work = args.work_dir.expanduser().resolve()
        raw_output = args.output_zip.expanduser()
        if raw_output.is_symlink():
            raise PackageError("The output ZIP path must not be a symlink.")
        output = raw_output.resolve()
        count, size, digest = create_package(work, output, args.hashes, args.overwrite)
    except (PackageError, OSError, ValueError, RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Created: {output}")
    print(f"Members: {count}")
    print(f"Bytes: {size}")
    print(f"SHA256: {digest}")
    if args.hashes:
        print("Hash manifest: hashes.tsv regenerated and included; manifest excludes itself.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
