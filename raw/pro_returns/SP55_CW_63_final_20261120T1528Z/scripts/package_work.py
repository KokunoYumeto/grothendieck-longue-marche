#!/usr/bin/env python3
"""Package current SP55_CW_63 work; never read scans or compile TeX.

Examples (the caller controls the requested 45-minute checkpoint schedule):
  python work/scripts/package_work.py --checkpoint 1
  python work/scripts/package_work.py --final
  python work/scripts/package_work.py --final --overwrite-final

Only archive creation is performed. This script does not edit work files, alter
progress.log, save to Library, or assert the visual accuracy of transcriptions.
Checkpoint archives are immutable: an existing target always causes failure.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path


PREFIX = "SP55_CW_63"
EXCLUDED_DIRS = {
    "input", "inputs", "upload", "uploads", "witnesses", "scans", "context", "codex", "hua",
    "contexts", "__pycache__", ".git", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    ".cache", "node_modules",
}
IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".jpe", ".jfif", ".png", ".apng", ".gif", ".bmp", ".dib",
    ".tif", ".tiff", ".webp", ".avif", ".heic", ".heif", ".svg", ".svgz",
    ".ico", ".icns", ".ppm", ".pgm", ".pbm", ".pnm", ".pam", ".xbm", ".xpm",
    ".jp2", ".j2k", ".jpf", ".jpx", ".pcx", ".tga", ".psd", ".xcf", ".eps",
}
EXCLUDED_EXTENSIONS = IMAGE_EXTENSIONS | {
    ".zip", ".pyc", ".pyo", ".pdf", ".aux", ".fls", ".fdb_latexmk", ".synctex",
}


def reason_to_exclude(relative: Path) -> str | None:
    for part in relative.parts[:-1]:
        name = part.lower()
        if name in EXCLUDED_DIRS or name.endswith("_scans") or name.endswith("_witnesses"):
            return "input, witness, scan, context or runtime-cache directory"
    suffix = relative.suffix.lower()
    if suffix in IMAGE_EXTENSIONS:
        return "image file"
    if suffix == ".zip":
        return "existing ZIP (including earlier checkpoints)"
    if suffix in {".pyc", ".pyo"}:
        return "compiled Python bytecode"
    if suffix in EXCLUDED_EXTENSIONS:
        return "unrequested source/render/build artifact"
    media_type, _ = mimetypes.guess_type(relative.name)
    if media_type and media_type.startswith("image/"):
        return "image media type"
    if relative.name.lower().endswith(".synctex.gz"):
        return "TeX build artifact"
    return None


def fingerprint(path: Path) -> tuple[int, int, int, int]:
    stat = path.stat()
    return stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--checkpoint", type=int, metavar="NN", help="create a new immutable numbered checkpoint")
    choice.add_argument("--final", action="store_true", help="create the final ZIP")
    parser.add_argument("--overwrite-final", action="store_true", help="explicitly replace a provisional final ZIP; forbidden for checkpoints")
    parser.add_argument("--work-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-dir", type=Path, help="defaults to WORK_DIR's sibling output directory")
    args = parser.parse_args()
    if args.checkpoint is not None and args.checkpoint < 1:
        parser.error("--checkpoint must be a positive integer")
    if args.overwrite_final and not args.final:
        parser.error("--overwrite-final is allowed only with --final")

    work = args.work_dir.resolve()
    output = args.output_dir.resolve() if args.output_dir else work.parent / "output"
    filename = f"{PREFIX}_checkpoint_{args.checkpoint:02d}.zip" if args.checkpoint is not None else f"{PREFIX}.zip"
    target = output / filename
    temp_path = None

    try:
        if not work.is_dir():
            raise RuntimeError(f"Work directory does not exist: {work}")
        if output == work:
            raise RuntimeError("Output directory must be separate from the work directory.")
        if target.exists() and not (args.final and args.overwrite_final):
            raise FileExistsError(f"Refusing to overwrite existing archive: {target}")
        # These are explicitly required in every checkpoint and final archive.
        for required in ("progress.log", "CHECK_EVENTS.tsv"):
            if not (work / required).is_file():
                raise RuntimeError(f"Required checkpoint/final documentation is absent: {required}")

        included = []
        excluded = []
        for directory, subdirs, filenames in os.walk(work, followlinks=False):
            directory_path = Path(directory)
            kept_subdirs = []
            for name in sorted(subdirs):
                path = directory_path / name
                relative = path.relative_to(work)
                # Add a dummy filename so directory rules inspect the final part.
                reason = reason_to_exclude(relative / "_file_")
                if path.is_symlink():
                    reason = "symbolic-link directory (not followed)"
                elif path.resolve() == output:
                    reason = "archive output directory"
                if reason:
                    excluded.append({"path": relative.as_posix() + "/", "reason": reason})
                else:
                    kept_subdirs.append(name)
            subdirs[:] = kept_subdirs
            for name in sorted(filenames):
                path = directory_path / name
                relative = path.relative_to(work)
                reason = reason_to_exclude(relative)
                if path.is_symlink():
                    reason = "symbolic-link file (not followed)"
                if reason:
                    excluded.append({"path": relative.as_posix(), "reason": reason})
                    continue
                if not path.is_file():
                    raise RuntimeError(f"Cannot archive nonregular file: {relative}")
                included.append((relative.as_posix(), path, fingerprint(path)))
        included.sort(key=lambda item: item[0])
        if not included:
            raise RuntimeError("No eligible work files were found.")

        output.mkdir(parents=True, exist_ok=True)
        descriptor, temp_name = tempfile.mkstemp(prefix=".SP55_CW_63_pack_", suffix=".tmp", dir=output)
        os.close(descriptor)
        temp_path = Path(temp_name)
        manifest = []
        with zipfile.ZipFile(temp_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for relative, path, initial in included:
                if fingerprint(path) != initial:
                    raise RuntimeError(f"Source changed while packaging: {relative}")
                data = path.read_bytes()
                if fingerprint(path) != initial:
                    raise RuntimeError(f"Source changed while being read: {relative}")
                info = zipfile.ZipInfo.from_file(path, arcname=relative)
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
                manifest.append({"path": relative, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
        for relative, path, initial in included:
            if fingerprint(path) != initial:
                raise RuntimeError(f"Source changed before archive completion: {relative}")
        with zipfile.ZipFile(temp_path) as archive:
            damaged = archive.testzip()
            if damaged is not None:
                raise RuntimeError(f"ZIP integrity failure: {damaged}")

        # A hard link is an atomic no-replace publication on the same filesystem.
        # It protects checkpoints against races as well as the initial exists check.
        if args.final and args.overwrite_final:
            os.replace(temp_path, target)
            temp_path = None
        else:
            os.link(temp_path, target)
        result = {
            "created": str(target),
            "mode": "checkpoint" if args.checkpoint is not None else "final",
            "checkpoint_number": args.checkpoint,
            "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "archive_bytes": target.stat().st_size,
            "archive_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
            "file_count": len(manifest),
            "files": manifest,
            "excluded": excluded,
            "scope": "Packaging only; no Library save and no assertion of visual reading accuracy.",
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, RuntimeError, zipfile.BadZipFile) as exc:
        print(json.dumps({"created": None, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
