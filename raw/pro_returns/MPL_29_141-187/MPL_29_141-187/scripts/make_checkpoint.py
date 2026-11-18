#!/usr/bin/env python3
"""Create one complete, numbered checkpoint ZIP when its hourly interval is due.

The archive contains current deliverables, logs, notes, and scripts beneath one
MPL_29_141-187/ root. It excludes source scans/attachments/context, earlier
checkpoints, the final package ZIP, caches, and symlinks. It never overwrites an
existing checkpoint and never changes the files being archived.

This script only prepares a local ZIP. The primary agent must then save that
ZIP durably and record the successful save in progress.log. It does not upload
anything or certify the completeness or accuracy of the transcription.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
import zipfile


PACKAGE = "MPL_29_141-187"
STAMP = "%Y-%m-%d %H:%M:%S UTC"
CHECKPOINT_PATTERN = re.compile(rf"{re.escape(PACKAGE)}_checkpoint_(\d+)\.zip")
COMMENT_PATTERN = re.compile(
    rf"{re.escape(PACKAGE)} checkpoint (\d+) created "
    r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC)"
)
EXCLUDED_DIRS = {
    "__pycache__", ".git", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    "scans", "upload", "uploads", "source", "sources", "context",
    "inspection", "latex_qa", "checkpoints",
}


def excluded(relative: Path) -> bool:
    if any(part.lower() in EXCLUDED_DIRS for part in relative.parts[:-1]):
        return True
    name = relative.name
    lower = name.lower()
    if lower.endswith((".pyc", ".pyo")):
        return True
    if CHECKPOINT_PATTERN.fullmatch(name) or name == f"{PACKAGE}.zip":
        return True
    if lower.startswith((PACKAGE.lower() + "_scans", PACKAGE.lower() + "_context", PACKAGE.lower() + "_prompt")):
        return True
    if re.fullmatch(r"PROMPT(?:\([^)]*\))?\.md", name, flags=re.IGNORECASE):
        return True
    if name in {"29.pdf", "MANIFEST.tsv"}:
        return True
    if re.fullmatch(
        rf"{re.escape(PACKAGE)}_29_scan\d+(?:_[ab])?\.(?:jpg|jpeg|png|tif|tiff|webp)",
        name, flags=re.IGNORECASE,
    ):
        return True
    return False


def gather(root: Path) -> tuple[list[Path], list[str]]:
    included: list[Path] = []
    skipped: list[str] = []
    for current, folders, names in os.walk(root, followlinks=False):
        current_path = Path(current)
        kept = []
        for name in sorted(folders):
            candidate = current_path / name
            relative = candidate.relative_to(root)
            if name.lower() in EXCLUDED_DIRS or candidate.is_symlink():
                skipped.append(relative.as_posix() + "/")
            else:
                kept.append(name)
        folders[:] = kept
        for name in sorted(names):
            candidate = current_path / name
            relative = candidate.relative_to(root)
            if excluded(relative):
                skipped.append(relative.as_posix())
                continue
            mode = candidate.lstat().st_mode
            if not stat.S_ISREG(mode):
                skipped.append(relative.as_posix() + " [not a regular file]")
                continue
            included.append(candidate)
    return sorted(included, key=lambda p: p.relative_to(root).as_posix()), skipped


def previous_checkpoints(folder: Path) -> list[tuple[int, Path]]:
    found: list[tuple[int, Path]] = []
    for path in folder.glob(f"{PACKAGE}_checkpoint_*.zip"):
        match = CHECKPOINT_PATTERN.fullmatch(path.name)
        if match:
            found.append((int(match[1]), path))
    return sorted(found)


def started_at(root: Path) -> datetime:
    with (root / "progress.log").open(encoding="utf-8") as stream:
        first = stream.readline().strip()
    return datetime.strptime(first, STAMP).replace(tzinfo=timezone.utc)


def previous_creation(path: Path) -> datetime:
    with zipfile.ZipFile(path) as archive:
        comment = archive.comment.decode("utf-8", errors="replace").strip()
    match = COMMENT_PATTERN.fullmatch(comment)
    if match:
        return datetime.strptime(match[2], STAMP).replace(tzinfo=timezone.utc)
    # This supports earlier checkpoints prepared by another method. It never
    # moves the hourly gate earlier than the previous local file timestamp.
    print(f"Previous ZIP has no creation comment; using its modification time: {path.name}", file=sys.stderr)
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)


def main() -> int:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=default_root)
    parser.add_argument("--output-dir", type=Path, help="Defaults to the package's parent; must be outside the package.")
    parser.add_argument("--number", type=int, help="Optional assertion of the next sequential number; cannot skip or overwrite.")
    parser.add_argument("--list", action="store_true", help="Show inclusion/exclusion names only; create nothing and do not read file contents.")
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output_dir or root.parent).resolve()
    if not root.is_dir():
        parser.error(f"Package directory does not exist: {root}")
    if output == root or root in output.parents:
        parser.error("Checkpoint output must be outside the package directory.")
    try:
        files, skipped = gather(root)
    except OSError as exc:
        print(f"Cannot enumerate package: {exc}", file=sys.stderr)
        return 2
    if args.list:
        for path in files:
            print("INCLUDE " + PACKAGE + "/" + path.relative_to(root).as_posix())
        for relative in skipped:
            print("EXCLUDE " + relative)
        print(f"{len(files)} included files; {len(skipped)} excluded entries. No ZIP created.")
        return 0
    if not files:
        print("Refusing to create an empty checkpoint.", file=sys.stderr)
        return 2
    existing = previous_checkpoints(output) if output.is_dir() else []
    numbers = [number for number, _ in existing]
    if numbers and numbers != list(range(1, max(numbers) + 1)):
        print("Local checkpoint numbers are not a contiguous sequence; resolve the missing/duplicate number before creating another.", file=sys.stderr)
        return 2
    next_number = (numbers[-1] + 1) if numbers else 1
    if args.number is not None and args.number != next_number:
        print(f"The next permitted checkpoint number is {next_number:02d}, not {args.number:02d}.", file=sys.stderr)
        return 2
    try:
        interval_start = started_at(root)
        if existing:
            interval_start = max(interval_start, previous_creation(existing[-1][1]))
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"Cannot establish the hourly checkpoint interval: {exc}", file=sys.stderr)
        return 2
    due = interval_start + timedelta(hours=1)
    now = datetime.now(timezone.utc)
    if now < due:
        print(f"Checkpoint {next_number:02d} is not due until {due.strftime(STAMP)}. No ZIP created.")
        return 3
    output.mkdir(parents=True, exist_ok=True)
    target = output / f"{PACKAGE}_checkpoint_{next_number:02d}.zip"
    if target.exists():
        print(f"Refusing to overwrite {target}.", file=sys.stderr)
        return 2
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{target.name}.", suffix=".tmp", dir=output)
    os.close(descriptor)
    temporary = Path(temporary_name)
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            archive.comment = f"{PACKAGE} checkpoint {next_number:02d} created {now.strftime(STAMP)}".encode("utf-8")
            for path in files:
                archive.write(path, PACKAGE + "/" + path.relative_to(root).as_posix())
        # A same-directory hard link publishes atomically without overwriting a
        # file that appeared between the existence check and publication.
        os.link(temporary, target)
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"Checkpoint creation failed: {exc}", file=sys.stderr)
        return 2
    finally:
        temporary.unlink(missing_ok=True)
    print(f"Created {target}")
    print(f"UTC creation time: {now.strftime(STAMP)}")
    print(f"Included files: {len(files)}; excluded entries: {len(skipped)}; ZIP bytes: {target.stat().st_size}")
    print("Local ZIP only: save it durably, then record the successful save in progress.log.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
