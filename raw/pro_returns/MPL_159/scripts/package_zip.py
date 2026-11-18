#!/usr/bin/env python3
"""List package contents or create a new checkpoint/final ZIP without overwrite.

Default action is read-only listing; it never creates a ZIP. A checkpoint is
created only with --checkpoint NN, and only at/after start + NN hours as read
from progress.log. --final first requires the structural validator to pass.

The archive contains every included file under the package directory, with
relative root-level paths. Inputs, source-image/context directories, source
archives, previous ZIPs, and caches are excluded. No source contents are opened.
No progress, audit, freeze, inventory, or CHECK_EVENTS records are changed.
ZIP entry order, timestamps, permissions, and compression settings are fixed,
making the same file snapshot reproducible in the same Python/zlib environment.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import zipfile


EXCLUDED_DIRS = {
    "scans", "upload", "uploads", "context", "sources", "source", "inputs",
    "MPL_159_context", "MPL_159_scans", "hua_project", "__pycache__",
    ".pytest_cache", ".mypy_cache", ".ruff_cache", ".cache", ".git",
    "node_modules", "checkpoints",
}
EXCLUDED_NAMES = {
    "RESULTS_STATE.md", "159.modern.tex", "159.pdf", ".DS_Store",
}
EXCLUDED_SUFFIXES = {
    ".zip", ".pyc", ".pyo", ".tmp", ".part", ".swp", ".swo",
    ".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff",
}


def collect(root: Path) -> tuple[list[Path], list[str]]:
    included = []
    excluded = []
    for directory, dirs, files in os.walk(root, topdown=True, followlinks=False):
        parent = Path(directory)
        for name in sorted(list(dirs)):
            path = parent / name
            if name in EXCLUDED_DIRS or path.is_symlink():
                excluded.append(path.relative_to(root).as_posix() + "/")
                dirs.remove(name)
        dirs.sort()
        for name in sorted(files):
            path = parent / name
            relative = path.relative_to(root).as_posix()
            if (path.is_symlink() or name in EXCLUDED_NAMES
                    or path.suffix.lower() in EXCLUDED_SUFFIXES
                    or re.fullmatch(r"PROMPT.*\.md", name)):
                excluded.append(relative)
            elif path.is_file():
                included.append(path)
    return sorted(included, key=lambda path: path.relative_to(root).as_posix()), sorted(excluded)


def checkpoint_due(root: Path, number: int) -> datetime:
    first = (root / "progress.log").read_text(encoding="utf-8").splitlines()[0]
    start = datetime.strptime(first, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    return start + timedelta(hours=number)


def create_archive(root: Path, files: list[Path], target: Path) -> dict:
    if target.exists():
        raise FileExistsError(f"Refusing to overwrite {target}")
    snapshot = [(path.relative_to(root).as_posix(), path.read_bytes()) for path in files]
    for relative, data in snapshot:
        if (root / relative).read_bytes() != data:
            raise RuntimeError(f"File changed while collecting snapshot: {relative}")
    if {path.relative_to(root).as_posix() for path in collect(root)[0]} != {relative for relative, _ in snapshot}:
        raise RuntimeError("Package file set changed while collecting snapshot")
    target.parent.mkdir(parents=True, exist_ok=True)
    created = False
    try:
        with target.open("xb") as stream:
            created = True
            with zipfile.ZipFile(stream, mode="w", compression=zipfile.ZIP_DEFLATED,
                                 compresslevel=9, allowZip64=True) as archive:
                for relative, data in snapshot:
                    entry = zipfile.ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
                    entry.create_system = 3
                    entry.external_attr = 0o100644 << 16
                    entry.compress_type = zipfile.ZIP_DEFLATED
                    archive.writestr(entry, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        with zipfile.ZipFile(target) as archive:
            if archive.testzip() is not None:
                raise RuntimeError("ZIP CRC verification failed")
            if archive.namelist() != [relative for relative, _ in snapshot]:
                raise RuntimeError("ZIP member list differs from snapshot")
        return {"path": str(target), "files": len(snapshot), "bytes": target.stat().st_size,
                "sha256": hashlib.sha256(target.read_bytes()).hexdigest()}
    except Exception:
        if created and target.is_file():
            target.unlink()
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-directory", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--checkpoint", type=int)
    mode.add_argument("--final", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output_directory.resolve() if args.output_directory else root.parent
    included, excluded = collect(root)
    report = {"root": str(root), "included_files": len(included),
              "included_bytes": sum(path.stat().st_size for path in included),
              "excluded": excluded}
    if args.checkpoint is not None:
        if not 1 <= args.checkpoint <= 99:
            parser.error("Checkpoint number must be between 1 and 99")
        due = checkpoint_due(root, args.checkpoint)
        now = datetime.now(timezone.utc)
        if now < due:
            parser.error(f"Checkpoint {args.checkpoint:02d} is not due before {due:%Y-%m-%d %H:%M:%S UTC}; no ZIP created")
        report["checkpoint_due"] = due.strftime("%Y-%m-%d %H:%M:%S UTC")
        report["archive"] = create_archive(root, included, output / f"MPL_159_checkpoint_{args.checkpoint:02d}.zip")
    elif args.final:
        from validate_package import validate
        validation = validate(root)
        if not validation["ok"]:
            report["validation"] = validation
            print(json.dumps(report, ensure_ascii=False, indent=2))
            return 1
        report["archive"] = create_archive(root, included, output / "MPL_159.zip")
    else:
        report["mode"] = "read-only listing; no ZIP created"
        report["files"] = [path.relative_to(root).as_posix() for path in included]
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
