#!/usr/bin/env python3
"""Package the current work without inputs, images, caches, or older archives.

Usage:
    python scripts/package_checkpoint.py OUTPUT_DIR ARCHIVE_PATH --dry-run
    python scripts/package_checkpoint.py OUTPUT_DIR ARCHIVE_PATH

The archive has a flat package root, preserving paths below OUTPUT_DIR. The
destination must be a new .zip file outside OUTPUT_DIR. This script neither
updates progress.log nor freezes records, validates manuscript content, or
uploads/saves anything to a remote service. Checkpoint completeness is left to
the caller; incomplete but permitted current records can be packaged.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import zipfile

# Importing the policy must not add a new cache file to the working package.
sys.dont_write_bytecode = True
from validate_structure import classify_package_path  # noqa: E402


def select_package_files(root: Path) -> tuple[list[tuple[Path, str]], list[dict[str, str]]]:
    """Select by path and file type only; do not read manuscript content."""
    selected: list[tuple[Path, str]] = []
    excluded: list[dict[str, str]] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() and not path.is_symlink():
            continue
        rel = path.relative_to(root).as_posix()
        if path.is_symlink():
            excluded.append({"path": rel, "reason": "symbolic link"})
            continue
        allowed, reason = classify_package_path(rel)
        if allowed:
            selected.append((path, rel))
        else:
            excluded.append({"path": rel, "reason": reason})
    return selected, excluded


def signature(path: Path) -> tuple[int, int]:
    stat = path.stat()
    return stat.st_size, stat.st_mtime_ns


def create_archive(root: Path, destination: Path, selected: list[tuple[Path, str]]) -> str:
    """Create a new archive atomically; never overwrite an existing archive."""
    if destination.exists() or destination.is_symlink():
        raise ValueError("Destination already exists; choose a new checkpoint filename.")
    if not destination.parent.is_dir():
        raise ValueError("Destination parent directory must already exist.")
    if not selected:
        raise ValueError("No permitted files were selected.")
    before = {rel: signature(path) for path, rel in selected}
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=".checkpoint-", suffix=".tmp", dir=destination.parent,
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with zipfile.ZipFile(temporary, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            for path, rel in selected:
                archive.write(path, arcname=rel)
        now, _ = select_package_files(root)
        if [rel for _, rel in now] != [rel for _, rel in selected]:
            raise RuntimeError("Permitted file selection changed during packaging; retry when writes are paused.")
        if any(signature(path) != before[rel] for path, rel in selected):
            raise RuntimeError("A selected file changed during packaging; retry when writes are paused.")
        with temporary.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        # Same-directory hard linking publishes the completed ZIP without any
        # overwrite race. The temporary name is removed in the finally block.
        os.link(temporary, destination)
        return digest
    finally:
        temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("archive_path", type=Path)
    parser.add_argument("--dry-run", action="store_true", help="Report selection only; create no files.")
    parser.add_argument("--json", action="store_true", help="Emit a structured report to stdout.")
    args = parser.parse_args(argv)
    root = args.output_dir.resolve()
    destination = args.archive_path.absolute()
    try:
        if not root.is_dir():
            raise ValueError("Output directory must exist.")
        if destination.suffix.lower() != ".zip":
            raise ValueError("Archive destination must have a .zip suffix.")
        if destination.resolve().is_relative_to(root):
            raise ValueError("Archive destination must be outside the output directory.")
        selected, excluded = select_package_files(root)
        report = {
            "dry_run": args.dry_run,
            "archive_path": str(destination),
            "included_count": len(selected),
            "excluded_count": len(excluded),
            "included": [rel for _, rel in selected],
            "excluded": excluded,
        }
        if not args.dry_run:
            report["sha256"] = create_archive(root, destination, selected)
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            verb = "Would include" if args.dry_run else "Packaged"
            print(f"{verb} {len(selected)} files; excluded {len(excluded)} files.")
            print(f"Archive: {destination}")
            for item in excluded:
                print(f"Excluded: {item['path']} ({item['reason']})")
            if "sha256" in report:
                print(f"SHA-256: {report['sha256']}")
        return 0
    except (OSError, ValueError, RuntimeError, zipfile.BadZipFile) as exc:
        if args.json:
            print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        else:
            print(f"Packaging failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
