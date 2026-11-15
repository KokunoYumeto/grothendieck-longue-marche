#!/usr/bin/env python3
"""Package all written work, excluding supplied sources and reproducible caches.

This program never edits the transcription, inventory, doubts, notes, or log.
It does not upload anything. --status and --dry-run never create an archive.
Checkpoint files are never overwritten and cannot be created before their
scheduled hourly time, measured from the first UTC line of progress.log.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import tempfile
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path


PACKAGE = "MPL_33_002-049"
DEFAULT_ROOT = Path(__file__).resolve().parent.parent
SUPPLIED_DIRECTORIES = {"upload", "uploads", "scans", "context", "sources", "same_cote_33",
                        f"{PACKAGE}_scans", f"{PACKAGE}_context"}
CACHE_DIRECTORIES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
                     ".cache", ".git", "node_modules"}
TEMPORARY_SUFFIXES = {".fmt", ".xdv", ".dvi", ".aux", ".toc", ".lof", ".lot",
                      ".nav", ".snm", ".vrb", ".out", ".fdb_latexmk", ".fls",
                      ".synctex", ".pyc", ".pyo", ".tmp", ".temp", ".part",
                      ".swp", ".swo"}
MANIFEST = "records/archive_manifest.txt"


def utc_text(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def start_time(root: Path) -> datetime:
    with (root / "progress.log").open(encoding="utf-8") as handle:
        first = handle.readline().strip()
    try:
        return datetime.strptime(first, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    except ValueError as exc:
        raise ValueError(f"progress.log first line is not the expected UTC timestamp: {first!r}") from exc


def exclusion(relative: Path) -> str | None:
    parts = relative.parts
    if any(part in SUPPLIED_DIRECTORIES for part in parts[:-1]):
        return "supplied source directory"
    if any(part in CACHE_DIRECTORIES for part in parts[:-1]):
        return "reproducible cache directory"
    name = relative.name
    if name == "RESULTS_STATE.md" or re.fullmatch(r"PROMPT\(\d{8}-\d{6}\)\.md", name):
        return "supplied contextual or instruction source"
    if re.fullmatch(re.escape(PACKAGE) + r"_33_scan\d{3}(?:_[ab])?\.jpe?g", name, re.I):
        return "supplied scan image"
    if name == f"{PACKAGE}_notes.md" and "same_cote_33" in parts:
        return "supplied contextual notes"
    if name.lower().endswith(".zip"):
        return "archive (never nest archives)"
    if relative.suffix.lower() in TEMPORARY_SUFFIXES or name.endswith(".synctex.gz"):
        return "reproducible compilation or cache product"
    if name.endswith("~"):
        return "editor backup"
    if relative.as_posix() == "records/latex_smoke/smoke.pdf":
        return "temporary compiler rendering"
    if relative.as_posix() == MANIFEST:
        return "manifest is regenerated inside the archive"
    return None


def inventory(root: Path):
    included, excluded = [], []
    for base, directories, files in os.walk(root, followlinks=False):
        base = Path(base)
        for directory in sorted(directories[:]):
            path = base / directory
            relative = path.relative_to(root)
            if directory in SUPPLIED_DIRECTORIES or directory in CACHE_DIRECTORIES:
                directories.remove(directory)
                excluded.append((relative.as_posix() + "/", "supplied source or cache directory"))
            elif path.is_symlink():
                directories.remove(directory)
                excluded.append((relative.as_posix() + "/", "symbolic link (not traversed)"))
        for filename in sorted(files):
            path = base / filename
            relative = path.relative_to(root)
            reason = exclusion(relative)
            if reason:
                excluded.append((relative.as_posix(), reason))
            elif path.is_symlink():
                excluded.append((relative.as_posix(), "symbolic link (not followed)"))
            else:
                included.append(path)
    included.sort(key=lambda p: p.relative_to(root).as_posix())
    excluded.sort()
    return included, excluded


def package(root: Path, target: Path, label: str, began: datetime,
            now: datetime, included: list[Path], excluded):
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=target.name + ".", suffix=".part", dir=target.parent)
    os.close(fd)
    temp = Path(temp_name)
    records = []
    try:
        with zipfile.ZipFile(temp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in included:
                relative = path.relative_to(root).as_posix()
                data = path.read_bytes()
                digest = hashlib.sha256(data).hexdigest()
                records.append((relative, len(data), digest))
                info = zipfile.ZipInfo.from_file(path, arcname=relative, strict_timestamps=False)
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
            # Fail rather than silently creating a mixed snapshot if another
            # process writes a deliverable while this archive is being made.
            current, _ = inventory(root)
            if current != included:
                raise RuntimeError("Written-work inventory changed during packaging; retry at a quiet boundary")
            for relative, size, digest in records:
                if hashlib.sha256((root / relative).read_bytes()).hexdigest() != digest:
                    raise RuntimeError(f"File changed during packaging: {relative}; retry")
            text = [f"{PACKAGE}: {label}", f"Packaged: {utc_text(now)}",
                    f"Work began: {utc_text(began)}", f"Written-work files: {len(records)}", "",
                    "The supplied scans, uploads, and context sources are excluded.",
                    "Compiler diagnostics, testing scripts, notes, logs, and records are retained.",
                    "This record documents packaging, not upload or durable saving.", "",
                    "SHA-256 | bytes | archive path"]
            text.extend(f"{digest} | {size} | {relative}" for relative, size, digest in records)
            text += ["", "Excluded paths and reasons:"]
            text.extend(f"{relative}: {reason}" for relative, reason in excluded)
            archive.writestr(MANIFEST, "\n".join(text) + "\n")
        # Atomic publication without overwriting an existing checkpoint/final.
        os.link(temp, target)
    finally:
        temp.unlink(missing_ok=True)
    with zipfile.ZipFile(target) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"ZIP CRC verification failed for {bad}")
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--output-dir", type=Path, help="Default: parent directory of the work folder")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--checkpoint", type=int, metavar="NN", help="Hourly checkpoint number, starting at 1")
    mode.add_argument("--final", action="store_true", help="Final delivery ZIP")
    mode.add_argument("--status", action="store_true", help="Show schedule and inventory; write nothing")
    parser.add_argument("--dry-run", action="store_true", help="Show plan and exclusions; write nothing")
    args = parser.parse_args()
    root = args.root.resolve()
    now = datetime.now(timezone.utc)
    began = start_time(root)
    included, excluded = inventory(root)
    print(f"Work began: {utc_text(began)}")
    print(f"First hourly checkpoint due: {utc_text(began + timedelta(hours=1))}")
    print(f"Current UTC time: {utc_text(now)}")
    if args.status:
        print(f"Written-work files eligible for packaging: {len(included)}")
        print(f"Excluded files/directories: {len(excluded)}")
        return 0
    if args.checkpoint is not None:
        if not 1 <= args.checkpoint <= 99:
            parser.error("--checkpoint must be between 1 and 99")
        due = began + timedelta(hours=args.checkpoint)
        name = f"{PACKAGE}_checkpoint_{args.checkpoint:02d}.zip"
        label = f"hourly checkpoint {args.checkpoint:02d}"
        print(f"This checkpoint due: {utc_text(due)}")
        if now < due and not args.dry_run:
            parser.error(f"Checkpoint is not due before {utc_text(due)}; no archive created")
    else:
        name, label = f"{PACKAGE}.zip", "final delivery"
    output_dir = args.output_dir.resolve() if args.output_dir else root.parent
    target = output_dir / name
    print(f"Archive path: {target}")
    print(f"Include {len(included)} written-work files; exclude {len(excluded)} paths")
    if args.dry_run:
        for relative, reason in excluded:
            print(f"EXCLUDE {relative}: {reason}")
        print("Dry run: no archive created and no work files changed.")
        return 0
    records = package(root, target, label, began, now, included, excluded)
    print(f"Created and CRC-verified {target} ({target.stat().st_size} bytes)")
    print(f"Included {len(records)} work files plus {MANIFEST}; nothing uploaded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
