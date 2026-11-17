#!/usr/bin/env python3
"""Validate and package the completed transcription; never creates checkpoints.

Nothing is edited in the transcription directory. This script refuses to make
the final ZIP until all 42 pages, required deliverables, audit log entries, and
unchanged frozen hashes pass the available mechanical checks.
"""

from pathlib import Path
import argparse
import hashlib
import re
import subprocess
import sys
import zipfile


PACKAGE = "MPL_137_045-086"
EXCLUDE_DIRS = {"__pycache__", "scans", "context", "upload"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--hashes", type=Path, help="freeze manifest; default: root/progress.log")
    parser.add_argument("--output", type=Path, help="default: root's parent/MPL_137_045-086.zip")
    parser.add_argument("--replace", action="store_true", help="replace an existing final archive")
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output or root.parent / f"{PACKAGE}.zip").resolve()
    if output.name != f"{PACKAGE}.zip":
        parser.error(f"final archive must be named {PACKAGE}.zip")
    if output.exists() and not args.replace:
        parser.error("final archive already exists; pass --replace to replace it")
    required = [
        root / f"{PACKAGE}_transcription.tex",
        root / f"{PACKAGE}_doubts.md",
        root / f"{PACKAGE}_inventory.csv",
        root / f"{PACKAGE}_notes.md",
        root / "progress.log",
    ]
    for path in required:
        if not path.is_file() or not path.stat().st_size:
            parser.error(f"required deliverable is missing or empty: {path.name}")
    log = (root / "progress.log").read_text(encoding="utf-8")
    frozen = re.search(r"(?m)^transcription frozen\s+", log)
    opened = re.search(r"(?m)^context opened\s+", log)
    if not frozen or not opened or frozen.start() >= opened.start():
        parser.error("log must record transcription frozen before context opened")
    for scan in range(45, 87):
        audited = re.search(rf"(?m)^scan\s+0*{scan}\s+audited\s+", log)
        if not audited or audited.start() >= frozen.start():
            parser.error(f"scan {scan:03d} lacks an audit log entry before the freeze")
    hashes = args.hashes or root / "progress.log"
    command = [sys.executable, "-B", str(root / "support" / "validate.py"), str(root), "--hashes", str(hashes)]
    result = subprocess.run(command, check=False)
    if result.returncode:
        return result.returncode
    result = subprocess.run([sys.executable, "-B", str(root / "support" / "static_tex_checks.py"), str(root)], check=False)
    if result.returncode:
        return result.returncode
    members = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if any(part in EXCLUDE_DIRS for part in relative.parts):
            continue
        if path.suffix.lower() in {".pyc", ".zip"}:
            continue
        if path.is_symlink():
            parser.error(f"refusing symlink in package: {relative}")
        if path.is_file():
            members.append((path, relative))
    temporary = output.with_suffix(".zip.part")
    if temporary.exists():
        parser.error(f"temporary output already exists: {temporary}")
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path, relative in members:
                archive.write(path, arcname=relative.as_posix())
        with zipfile.ZipFile(temporary, "r") as archive:
            failed = archive.testzip()
            if failed:
                raise RuntimeError(f"ZIP integrity check failed: {failed}")
        temporary.replace(output)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise
    print(f"Created {output} with {len(members)} files.")
    print("SHA256", hashlib.sha256(output.read_bytes()).hexdigest())
    print("Input archives, scans, extracted context, bytecode caches, and earlier ZIPs are excluded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
