#!/usr/bin/env python3
"""Package all current deliverables without source attachments or images.

This script creates a local ZIP only; it never uploads or saves to Library.
Run it only at an authorized checkpoint time, or for the final delivery.
Existing archive names are never overwritten, renamed, or removed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path

PREFIX = "SP66_C13_16+120+136"
EXCLUDED_SUFFIXES = {
    ".zip", ".pyc", ".pyo", ".jpg", ".jpeg", ".png", ".gif", ".webp",
    ".tif", ".tiff", ".bmp", ".svg", ".avif", ".heic", ".ico",
    ".pdf", ".eps", ".ps",
}
EXCLUDED_DIRS = {"__pycache__", ".git", ".pytest_cache", "source", "upload", "scans", "halves", "crops"}
MANIFEST_NAME = "PACKAGE_MANIFEST.tsv"


def excluded(relative: Path) -> bool:
    if relative.suffix.lower() in EXCLUDED_SUFFIXES:
        return True
    if any(part in EXCLUDED_DIRS or part.endswith(("_scans", "_texts")) for part in relative.parts[:-1]):
        return True
    if relative.name in {"MARKS.tsv", "PREAMBLE.tex", MANIFEST_NAME}:
        return True
    if relative.name.startswith("PROMPT(") and relative.suffix.lower() == ".md":
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="Current work/deliverables directory")
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory for immutable ZIP files")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--checkpoint", type=int, metavar="NN", help="Positive checkpoint number")
    group.add_argument("--final", action="store_true", help="Use the required final ZIP filename")
    parser.add_argument("--not-before", help="Optional earliest UTC time, e.g. 2026-11-20T15:02:23Z")
    args = parser.parse_args()
    root = args.root.resolve()
    out_dir = args.output_dir.resolve()
    if not root.is_dir():
        parser.error("--root must be an existing directory")
    if args.checkpoint is not None and args.checkpoint < 1:
        parser.error("--checkpoint must be a positive integer")
    if args.not_before:
        try:
            earliest = datetime.fromisoformat(args.not_before.replace("Z", "+00:00"))
            if earliest.tzinfo is None:
                earliest = earliest.replace(tzinfo=timezone.utc)
        except ValueError:
            parser.error("--not-before must be an ISO datetime")
        if datetime.now(timezone.utc) < earliest:
            parser.error("checkpoint time has not arrived; no ZIP was created")
    name = PREFIX + (".zip" if args.final else f"_checkpoint_{args.checkpoint:02d}.zip")
    destination = out_dir / name
    if destination.exists():
        parser.error(f"refusing to overwrite existing archive: {destination}")
    selected: list[tuple[Path, str]] = []
    skipped = 0
    for directory, dirs, names in os.walk(root, followlinks=False):
        directory = Path(directory)
        dirs[:] = sorted(d for d in dirs
                         if d not in EXCLUDED_DIRS
                         and not d.endswith(("_scans", "_texts"))
                         and not (directory / d).is_symlink())
        for filename in sorted(names):
            path = directory / filename
            relative = path.relative_to(root)
            if path.is_symlink() or excluded(relative):
                skipped += 1
                continue
            if path.is_file():
                selected.append((path, relative.as_posix()))
    selected.sort(key=lambda item: item[1])
    if not selected:
        parser.error("no deliverables were found")
    if not any(relative == "progress.log" for _, relative in selected):
        parser.error("progress.log is missing; refusing to create a checkpoint")
    out_dir.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix=".package-", suffix=".tmp", dir=out_dir)
    os.close(fd)
    temporary = Path(temporary_name)
    manifest = io.StringIO(newline="")
    writer = csv.writer(manifest, delimiter="\t", lineterminator="\n")
    writer.writerow(["path", "size_bytes", "sha256"])
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path, relative in selected:
                before = path.stat()
                content = path.read_bytes()
                after = path.stat()
                if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                    raise RuntimeError(f"file changed during packaging: {relative}")
                archive.writestr(relative, content)
                writer.writerow([relative, len(content), hashlib.sha256(content).hexdigest()])
            archive.writestr(MANIFEST_NAME, manifest.getvalue().encode("utf-8"))
        # Atomic publication without an overwrite-capable rename. The temporary
        # and destination files are necessarily on the same filesystem.
        os.link(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)
    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    print(f"archive: {destination}")
    print(f"files: {len(selected)} + {MANIFEST_NAME}")
    print(f"excluded files: {skipped}")
    print(f"size_bytes: {destination.stat().st_size}")
    print(f"sha256: {digest}")
    print("Local ZIP created; no upload was performed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, zipfile.BadZipFile) as exc:
        print(f"Packaging failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
