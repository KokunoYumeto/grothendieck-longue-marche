#!/usr/bin/env python3
"""Create a new cumulative checkpoint ZIP only when at least one hour is due.

Does not upload. The parent must preserve the resulting ZIP using Library.
An incomplete current page can be kept in the work directory and is included.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import re
import shutil
from zipfile import ZIP_DEFLATED, ZipFile

PREFIX = "MPL_93_002-046"
STAMP = "%Y-%m-%d %H:%M:%S UTC"
EXCLUDED_DIRS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
                 ".git", "node_modules", "scans", "upload", "uploads",
                 "attachments", "context", "context_sources"}
EXCLUDED_SUFFIXES = {".zip", ".pyc", ".pyo", ".jpg", ".jpeg", ".png",
                     ".tif", ".tiff", ".gif", ".webp", ".bmp", ".heic",
                     ".svg", ".avif", ".ico"}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = p.parse_args()
    root = args.root.resolve()
    progress = root / "progress.log"
    lines = progress.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise SystemExit("Refusing checkpoint: progress.log has no initial UTC timestamp")
    try:
        last_time = datetime.strptime(lines[0], STAMP).replace(tzinfo=timezone.utc)
        for line in lines[1:]:
            match = re.fullmatch(r"checkpoint \d+ created (.+)", line)
            if match:
                last_time = max(last_time, datetime.strptime(match[1], STAMP).replace(tzinfo=timezone.utc))
    except ValueError as exc:
        raise SystemExit(f"Refusing checkpoint: malformed timestamp: {exc}")
    now = datetime.now(timezone.utc)
    elapsed = (now - last_time).total_seconds()
    if elapsed < 3600:
        raise SystemExit(f"Checkpoint not due: {max(0, 3600 - elapsed):.0f} seconds until one hour")
    # Page-writing helpers may live beside the work directory. Preserve all
    # workspace-root Python/shell scripts without importing or executing them.
    # This also leaves their copies in the work tree for the final package.
    script_copies = root / "tools" / "session_scripts"
    for pattern in ("*.py", "*.sh"):
        for source in sorted(root.parent.glob(pattern)):
            if source.is_file() and not source.is_symlink():
                script_copies.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, script_copies / source.name)
    numbers = []
    for f in root.parent.glob(f"{PREFIX}_checkpoint_*.zip"):
        match = re.fullmatch(re.escape(PREFIX) + r"_checkpoint_(\d+)\.zip", f.name)
        if match:
            numbers.append(int(match[1]))
    number = max(numbers, default=0) + 1
    target = root.parent / f"{PREFIX}_checkpoint_{number:02d}.zip"
    stamp_line = f"checkpoint {number:02d} created {now.strftime(STAMP)}\n"
    # Append only after the archive closes successfully; place the same new log
    # bytes in the ZIP, so that it carries its own creation record.
    log_bytes = progress.read_bytes()
    if log_bytes and not log_bytes.endswith(b"\n"):
        log_bytes += b"\n"
    log_bytes += stamp_line.encode("utf-8")
    # Exclusive creation happens outside the cleanup handler: an already
    # existing checkpoint can never be overwritten or deleted by this script.
    with target.open("xb") as output:
        try:
            with ZipFile(output, "w", ZIP_DEFLATED, compresslevel=9) as archive:
                for f in sorted(root.rglob("*")):
                    relative = f.relative_to(root)
                    if not f.is_file() or f.is_symlink():
                        continue
                    if any(part in EXCLUDED_DIRS for part in relative.parts):
                        continue
                    if f.suffix.lower() in EXCLUDED_SUFFIXES:
                        continue
                    if f == progress:
                        archive.writestr(relative.as_posix(), log_bytes)
                    else:
                        archive.write(f, relative.as_posix())
        except Exception:
            target.unlink(missing_ok=True)
            raise
    with progress.open("ab") as stream:
        if progress.stat().st_size and not progress.read_bytes().endswith(b"\n"):
            stream.write(b"\n")
        stream.write(stamp_line.encode("utf-8"))
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
