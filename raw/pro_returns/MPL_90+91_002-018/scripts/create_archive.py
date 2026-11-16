#!/usr/bin/env python3
"""Create a new verified ZIP of this package's work directory.

The source is fixed to the script's parent work directory. Attachments, scans,
and unopened context outside that directory are never traversed. This script
does not parse or interpret any document or image.
"""

from __future__ import annotations

import argparse
import os
import sys
import tempfile
import zipfile
from pathlib import Path


CACHE_DIRS = {
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".cache",
    ".git", ".ipynb_checkpoints",
}
TEMP_DIRS = {"tmp", "temp", "_tmp", ".tmp", ".temp"}
EXCLUDED_ROOT_DIRS = {"upload", "scans", "context", "deliverables"}
TEMP_SUFFIXES = (".pyc", ".pyo", ".tmp", ".temp", ".part", ".swp", ".swo", "~")


def collect_files(work: Path) -> tuple[list[Path], int]:
    files: list[Path] = []
    excluded = 0
    for directory, dirnames, filenames in os.walk(work, followlinks=False):
        here = Path(directory)
        kept = []
        for name in sorted(dirnames):
            path = here / name
            if path.is_symlink():
                raise ValueError(f"Refusing a directory symlink in the source tree: {path.relative_to(work)}")
            if (name in CACHE_DIRS or name in TEMP_DIRS or
                    (here == work and name in EXCLUDED_ROOT_DIRS)):
                excluded += 1
            else:
                kept.append(name)
        dirnames[:] = kept
        for name in sorted(filenames):
            path = here / name
            if path.is_symlink():
                raise ValueError(f"Refusing a file symlink in the source tree: {path.relative_to(work)}")
            if name == ".DS_Store" or name.endswith(TEMP_SUFFIXES):
                excluded += 1
                continue
            if not path.is_file():
                raise ValueError(f"Refusing a nonregular source file: {path.relative_to(work)}")
            files.append(path)
    files.sort(key=lambda path: path.relative_to(work).as_posix())
    return files, excluded


def create_archive(name: str) -> tuple[Path, int, int, int]:
    if (not name or name in (".", "..") or Path(name).name != name or
            "/" in name or "\\" in name or not name.endswith(".zip")):
        raise ValueError("Output must be a single filename ending in .zip, without directory components.")
    work = Path(__file__).resolve().parents[1]
    destination_dir = work.parent / "deliverables"
    destination_dir.mkdir(exist_ok=True)
    if destination_dir.is_symlink():
        raise ValueError("Refusing a symlink as the deliverables directory.")
    destination = destination_dir / name
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"Refusing to overwrite {destination}")

    files, excluded = collect_files(work)
    if not files:
        raise ValueError("The work directory contains no eligible files.")
    manifest = {
        path.relative_to(work).as_posix(): (path.stat().st_size, path.stat().st_mtime_ns)
        for path in files
    }
    total_bytes = sum(metadata[0] for metadata in manifest.values())
    fd, temporary_name = tempfile.mkstemp(prefix=".archive-", suffix=".part", dir=destination_dir)
    temporary = Path(temporary_name)
    published = False
    try:
        with os.fdopen(fd, "w+b") as handle:
            with zipfile.ZipFile(handle, mode="w", compression=zipfile.ZIP_DEFLATED,
                                 compresslevel=9, allowZip64=True) as archive:
                for path in files:
                    relative = path.relative_to(work).as_posix()
                    before = path.stat()
                    if (before.st_size, before.st_mtime_ns) != manifest[relative]:
                        raise RuntimeError(f"Source changed during archiving: {relative}; rerun after writes finish.")
                    archive.write(path, arcname=relative)
                    after = path.stat()
                    if (after.st_size, after.st_mtime_ns) != manifest[relative]:
                        raise RuntimeError(f"Source changed while being archived: {relative}; rerun after writes finish.")
            handle.flush()
            os.fsync(handle.fileno())

        with zipfile.ZipFile(temporary, "r") as archive:
            members = archive.infolist()
            names = [member.filename for member in members]
            if len(members) != len(files) or names != list(manifest):
                raise RuntimeError("ZIP member count or relative paths differ from the collected source files.")
            if len(set(names)) != len(names):
                raise RuntimeError("ZIP contains duplicate member names.")
            for member in members:
                if member.file_size != manifest[member.filename][0]:
                    raise RuntimeError(f"ZIP member size mismatch: {member.filename}")
            bad_member = archive.testzip()
            if bad_member is not None:
                raise RuntimeError(f"ZIP CRC verification failed: {bad_member}")

        # A hard link publishes the completed ZIP atomically and fails if the
        # requested filename appeared meanwhile. It never replaces an old ZIP.
        os.link(temporary, destination)
        published = True
        return destination, len(files), excluded, total_bytes
    finally:
        temporary.unlink(missing_ok=True)
        if published:
            try:
                directory_fd = os.open(destination_dir, os.O_DIRECTORY)
                try:
                    os.fsync(directory_fd)
                finally:
                    os.close(directory_fd)
            except (AttributeError, OSError):
                pass


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_name", help="New ZIP filename, created under the workspace deliverables directory")
    args = parser.parse_args()
    try:
        destination, count, excluded, total_bytes = create_archive(args.output_name)
    except (OSError, ValueError, RuntimeError, zipfile.BadZipFile) as exc:
        print(f"Archive failed: {exc}", file=sys.stderr)
        return 1
    print(f"Created: {destination}")
    print(f"Members: {count}; uncompressed bytes: {total_bytes}; excluded cache/temporary entries: {excluded}")
    print("Verified: exact member count, ordered relative names, member sizes, all member CRCs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
