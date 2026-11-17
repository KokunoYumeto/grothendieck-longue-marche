#!/usr/bin/env python3
"""Create one complete hourly checkpoint ZIP, without uploading or editing pages.

Default paths are derived from this script. A checkpoint cannot be created before
one hour after the UTC first line of progress.log, or less than one hour after a
previous checkpoint. --dry-run lists the planned contents and timing without
creating any archive or changing any file. Final delivery packaging is separate.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import hashlib
from pathlib import Path
import re
import sys
from zipfile import ZIP_DEFLATED, ZipFile

PREFIX = "MPL_91_019-058"
BLOCKED_DIRS = {".git", "__pycache__", "upload", "scans", "source", "sources", "context", "checkpoints"}
BLOCKED_SUFFIXES = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".gif", ".bmp", ".heic", ".avif", ".zip", ".gz", ".tgz", ".bz2", ".7z", ".rar", ".pyc", ".pyo"}
RECORD_NAME = "_checkpoint_record.txt"


def parse_utc(value: str) -> datetime:
    value = value.strip()
    if value.endswith(" UTC"):
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp must explicitly identify UTC")
    return parsed.astimezone(timezone.utc)


def utc_string(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def eligible(path: Path, relative: Path) -> bool:
    if path.is_symlink() or not path.is_file():
        return False
    if any(part.lower() in BLOCKED_DIRS for part in relative.parts):
        return False
    if path.suffix.lower() in BLOCKED_SUFFIXES:
        return False
    if relative.name == RECORD_NAME:
        return False
    return True


def collect(package: Path, helpers: Path) -> list[tuple[Path, str]]:
    files = []
    for path in sorted(package.rglob("*")):
        relative = path.relative_to(package)
        if eligible(path, relative):
            files.append((path, relative.as_posix()))
    # These are the current bundled transfer helpers, not user source material.
    if helpers.is_dir():
        for path in sorted(helpers.rglob("*")):
            relative = path.relative_to(helpers)
            if eligible(path, relative) and path.suffix.lower() in {".py", ".md", ".txt"}:
                files.append((path, (Path("scripts/library_helpers") / relative).as_posix()))
    archive_names = [name for _, name in files]
    if len(archive_names) != len(set(archive_names)):
        raise ValueError("duplicate archive paths; move conflicting support files before packaging")
    return files


def previous_checkpoints(directory: Path) -> list[tuple[int, Path]]:
    found = []
    for path in directory.glob(f"{PREFIX}_checkpoint_*.zip"):
        match = re.fullmatch(rf"{re.escape(PREFIX)}_checkpoint_(\d+)\.zip", path.name)
        if match:
            found.append((int(match.group(1)), path))
    return sorted(found)


def previous_time(path: Path) -> datetime:
    with ZipFile(path) as archive:
        if RECORD_NAME in archive.namelist():
            first = archive.read(RECORD_NAME).decode("utf-8").splitlines()[0]
            return parse_utc(first.removeprefix("checkpoint created "))
    # Compatibility with an earlier manually created checkpoint. Copying such an
    # archive can only delay this gate; it cannot authorize an earlier checkpoint.
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("package_directory", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-directory", type=Path)
    parser.add_argument("--helpers-directory", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    package = args.package_directory.resolve()
    output = (args.output_directory or package.parent / "checkpoints").resolve()
    helpers = (args.helpers_directory or package.parent / "library_helpers").resolve()
    with (package / "progress.log").open(encoding="utf-8") as stream:
        start = parse_utc(stream.readline())
    now = datetime.now(timezone.utc)
    previous = previous_checkpoints(output)
    due = start + timedelta(hours=1)
    if previous:
        due = max(due, previous_time(previous[-1][1]) + timedelta(hours=1))
    number = previous[-1][0] + 1 if previous else 1
    destination = output / f"{PREFIX}_checkpoint_{number:02d}.zip"
    files = collect(package, helpers)
    if not files:
        raise ValueError("no eligible files to checkpoint")
    print(f"Current UTC: {utc_string(now)}")
    print(f"Earliest allowed checkpoint: {utc_string(due)}")
    print(f"Next archive: {destination}")
    print(f"Files selected: {len(files)}")
    if args.dry_run:
        print("DRY RUN: no archive created; no files modified.")
        for _, name in files:
            print(name)
        return 0
    if now < due:
        print("REFUSED: the next hourly checkpoint is not yet due.", file=sys.stderr)
        return 2
    output.mkdir(parents=True, exist_ok=True)
    # Exclusive creation guarantees that an earlier checkpoint is never replaced.
    owns_archive = False
    try:
        with ZipFile(destination, mode="x", compression=ZIP_DEFLATED, compresslevel=9) as archive:
            owns_archive = True
            record = [f"checkpoint created {utc_string(now)}", f"checkpoint number {number:02d}",
                      "Complete snapshot of all eligible work files present at packaging time.",
                      "Supplied inputs, scan images, image inspection derivatives, previous archives, and bytecode excluded.",
                      "Hashes below identify checkpoint members; they do not certify transcription accuracy.", ""]
            for path, name in files:
                before = path.stat()
                data = path.read_bytes()
                after = path.stat()
                if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                    raise RuntimeError(f"file changed while packaging: {name}")
                archive.writestr(name, data)
                record.append(f"{hashlib.sha256(data).hexdigest()}  {name}")
            archive.writestr(RECORD_NAME, "\n".join(record) + "\n")
    except Exception:
        # Remove only the incomplete archive created by this invocation. Never
        # unlink an existing archive when exclusive creation itself failed.
        if owns_archive and destination.exists():
            try:
                with ZipFile(destination) as archive:
                    complete = RECORD_NAME in archive.namelist()
            except Exception:
                complete = False
            if not complete:
                destination.unlink()
        raise
    with ZipFile(destination) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"checkpoint integrity failure: {bad}")
    print(f"Created: {destination}")
    print(f"SHA-256: {hashlib.sha256(destination.read_bytes()).hexdigest()}")
    print("Upload this ZIP through the Library create tool, then apply returned metadata with the current transfer helper.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"Checkpoint error: {exc}", file=sys.stderr)
        sys.exit(1)
