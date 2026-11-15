#!/usr/bin/env python3
"""Package existing work without changing records, invoking Library, or reading input archives."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
from validate import PREFIX, validate_tree  # noqa: E402

EXCLUDED_DIRS = {
    ".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".cache",
    "tmp", "temp", "preview", "previews", "qa", "rendered", "renders",
    "scan", "scans", "upload", "uploads", "attachments", "inputs", "sources", "context",
}
EXCLUDED_SUFFIXES = {
    ".zip", ".7z", ".rar", ".tar", ".gz", ".bz2", ".xz", ".pyc", ".pyo",
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".tif", ".tiff", ".bmp",
    ".aux", ".toc", ".out", ".synctex", ".fls", ".fdb_latexmk",
}


def selected_files(root: Path):
    included, excluded = [], []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if not path.is_file():
            continue
        reason = None
        if path.is_symlink():
            reason = "symlink (not followed)"
        elif any(part.lower() in EXCLUDED_DIRS for part in relative.parts[:-1]):
            reason = "input, temporary, or cache directory"
        elif path.suffix.lower() in EXCLUDED_SUFFIXES:
            reason = "archive, image, bytecode, or LaTeX temporary file"
        elif path.name in {".DS_Store", "Thumbs.db"}:
            reason = "operating-system metadata"
        if reason:
            excluded.append({"path": relative.as_posix(), "reason": reason})
        else:
            included.append(path)
    return included, excluded


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--checkpoint", type=int, metavar="NN", help="Package one numbered checkpoint; never upload automatically")
    choice.add_argument("--final", action="store_true", help="Require final mechanical validation, then package")
    parser.add_argument("--output-dir", type=Path, help="Defaults to the work directory's parent")
    parser.add_argument("--list-only", action="store_true", help="Report included/excluded paths without creating a ZIP")
    args = parser.parse_args()
    root = args.root.resolve()
    output_dir = (args.output_dir or root.parent).resolve()
    if args.checkpoint is not None and not 1 <= args.checkpoint <= 99:
        parser.error("checkpoint number must be from 1 to 99")
    filename = f"{PREFIX}.zip" if args.final else f"{PREFIX}_checkpoint_{args.checkpoint:02d}.zip"
    output = output_dir / filename
    included, excluded = selected_files(root)
    if args.list_only:
        print(json.dumps({"output": str(output), "included": [p.relative_to(root).as_posix() for p in included], "excluded": excluded}, indent=2))
        return 0
    if output.exists():
        parser.error(f"Refusing to overwrite existing ZIP: {output}")
    mode = "final" if args.final else "checkpoint"
    validation = validate_tree(root, mode)
    # Preserve partial work in checkpoints even when mechanical checks flag a problem.
    # Final delivery requires addressing mechanical errors first.
    if args.final and validation["errors"]:
        print(json.dumps({"status": "refused", "validation": validation}, indent=2), file=sys.stderr)
        return 1
    if not included:
        parser.error("No work files found")
    if args.checkpoint is not None:
        elapsed = validation["facts"].get("seconds_since_start")
        if elapsed is not None and elapsed < 3600:
            parser.error(f"First hourly checkpoint is not due: only {elapsed} seconds since progress.log began")
    output_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in included:
            archive.write(path, path.relative_to(root).as_posix())
    with zipfile.ZipFile(output) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"ZIP CRC verification failed for {bad}")
        member_count = len(archive.infolist())
    print(json.dumps({
        "status": "packaged",
        "path": str(output),
        "kind": mode,
        "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "files": member_count,
        "bytes": output.stat().st_size,
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "excluded": excluded,
        "mechanical_errors": validation["errors"],
        "mechanical_warnings": validation["warnings"],
        "note": "Packaging does not establish transcription completeness or accuracy. No upload or log mutation was performed.",
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
