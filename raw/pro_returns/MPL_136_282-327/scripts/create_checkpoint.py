#!/usr/bin/env python3
"""Create one complete, sequential checkpoint only when explicitly invoked.

This is a local packager, not a scheduler or an uploader. It does nothing until
called. It refuses an invocation before the first due time or within one hour
of the most recent checkpoint. Existing checkpoint ZIPs are never overwritten.
Source attachments, scans, context material, caches, and previous ZIPs are
excluded. All remaining files beneath the package directory are included.

After a successful invocation, the caller must save the reported ZIP to the
user's persistent destination. This script does not claim that such a save has
occurred. Checkpoint file entries are relative to the package directory.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path


PACKAGE = "MPL_136_282-327"
FIRST_DUE = datetime(2026, 11, 17, 11, 14, 52, tzinfo=timezone.utc)
INTERVAL = timedelta(hours=1)
EXCLUDED_DIRECTORIES = {
    "__pycache__", ".git", ".pytest_cache", "upload", "uploads", "scans",
    "source_scans", "context", "source_context", "sources", "attachments",
    "same_cote_136", "ps_chapters_vi_vii", "hua_project",
}
EXCLUDED_BASENAMES = {
    "prompt(20261117-101417).md", "pursuing_stacks_contents.md", "results_state.md",
    "mpl_136_282-327_scans.zip", "mpl_136_282-327_context.zip",
}
SOURCE_SCAN = re.compile(
    r"MPL_136_282-327_136_scan\d+(?:_[ab])?\.(?:jpg|jpeg|png|tif|tiff|webp)$",
    re.IGNORECASE,
)
ARCHIVE_COMMENT_PREFIX = "checkpoint-created-utc: "


def utc_string(value: datetime) -> str:
    return value.strftime("%Y-%m-%d %H:%M:%S UTC")


def checkpoint_time(path: Path) -> datetime:
    """Read only a previous generated checkpoint's timestamp metadata."""
    # No archive entries are opened. This is never called on a source ZIP.
    try:
        with zipfile.ZipFile(path) as archive:
            comment = archive.comment.decode("ascii")
        if comment.startswith(ARCHIVE_COMMENT_PREFIX):
            timestamp = comment[len(ARCHIVE_COMMENT_PREFIX):].strip()
            return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S UTC").replace(
                tzinfo=timezone.utc)
    except (OSError, zipfile.BadZipFile, UnicodeError, ValueError):
        pass
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)


def excluded(relative: Path) -> bool:
    if any(part.lower() in EXCLUDED_DIRECTORIES for part in relative.parts[:-1]):
        return True
    name = relative.name.lower()
    return (
        name in EXCLUDED_BASENAMES
        or relative.suffix.lower() in {".zip", ".pyc", ".pyo", ".tmp"}
        or SOURCE_SCAN.fullmatch(relative.name) is not None
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path,
                        default=Path(__file__).resolve().parent.parent,
                        help="package directory (default: parent of scripts/)")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f"ERROR: package directory does not exist: {root}", file=sys.stderr)
        return 1
    now = datetime.now(timezone.utc)
    existing: list[tuple[int, Path]] = []
    for path in root.parent.glob(f"{PACKAGE}_checkpoint_*.zip"):
        match = re.fullmatch(rf"{PACKAGE}_checkpoint_(\d+)\.zip", path.name)
        if match:
            existing.append((int(match.group(1)), path))
    most_recent = max((checkpoint_time(path) for _, path in existing), default=None)
    due = max(FIRST_DUE, most_recent + INTERVAL) if most_recent else FIRST_DUE
    if now < due:
        print(f"NOT DUE: next checkpoint may be created at {utc_string(due)}")
        return 2

    # Refuse symlinks rather than following content outside the package root.
    # A sorted snapshot keeps ZIP ordering stable and includes every deliverable
    # currently written, irrespective of which page or phase is in progress.
    files: list[tuple[Path, Path]] = []
    omitted = 0
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if excluded(relative):
            if path.is_file():
                omitted += 1
            continue
        if path.is_symlink():
            print(f"ERROR: review symlink before checkpointing: {relative}", file=sys.stderr)
            return 1
        if path.is_file():
            files.append((path, relative))
    if not files:
        print("ERROR: no eligible files found", file=sys.stderr)
        return 1
    next_number = max((number for number, _ in existing), default=0) + 1
    target = root.parent / f"{PACKAGE}_checkpoint_{next_number:02d}.zip"
    created = False
    try:
        # Exclusive creation is intentional: never truncate or replace a ZIP.
        with zipfile.ZipFile(target, mode="x", compression=zipfile.ZIP_DEFLATED,
                             compresslevel=9, strict_timestamps=False) as archive:
            created = True
            archive.comment = (ARCHIVE_COMMENT_PREFIX + utc_string(now)).encode("ascii")
            for path, relative in files:
                archive.write(path, arcname=relative.as_posix())
        # CRC verification reads only this newly generated checkpoint.
        with zipfile.ZipFile(target) as archive:
            bad_entry = archive.testzip()
            if bad_entry:
                raise RuntimeError(f"CRC verification failed: {bad_entry}")
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        if created:
            target.unlink(missing_ok=True)
        print(f"ERROR: checkpoint not created: {exc}", file=sys.stderr)
        return 1
    print(f"Created: {target}")
    print(f"UTC: {utc_string(now)}")
    print(f"Included files: {len(files)}; excluded files: {omitted}")
    print(f"SHA-256: {digest}")
    print(f"Next due: {utc_string(now + INTERVAL)}")
    print("This ZIP still needs to be saved to the persistent destination.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
