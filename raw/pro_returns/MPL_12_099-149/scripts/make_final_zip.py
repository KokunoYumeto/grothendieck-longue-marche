#!/usr/bin/env python3
"""Package the final deliverable only after structural and frozen-hash checks.

No scans or context sources are opened. This script does not freeze, edit,
upload, or claim semantic accuracy of the transcription.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path

# Some managed runtimes omit the entrypoint directory from sys.path.
SCRIPT_DIRECTORY = Path(__file__).resolve().parent
if str(SCRIPT_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIRECTORY))
from make_checkpoint import included  # noqa: E402
from validate_structure import Check, PREFIX, SCANS, STAMP  # noqa: E402

SOURCE_BASENAMES = {
    "MPL_16+47+54+44_doubts.md",
    "MPL_16+47+54+44_notes.md",
    "MPL_16+47+54+44_transcription.tex",
    "Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf",
    "RESULTS_STATE.md",
}
REQUIRED = {
    "progress.log",
    f"{PREFIX}_transcription.tex",
    f"{PREFIX}_inventory.csv",
    f"{PREFIX}_doubts.md",
    f"{PREFIX}_notes.md",
    *(f"pages/{PREFIX}_12_scan{scan:03d}.tex" for scan in SCANS),
}
VALIDATION_RECORD = "records/final_structure_check.json"


def admissible(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    if not included(path, root):
        return False
    if path.name in SOURCE_BASENAMES:
        return False
    if "hua_project" in relative.parts:
        return False
    # Any new context extraction directory whose name includes the package
    # name is also a source container, even when not literally named context.
    if any("context" in part.lower() or "scans" in part.lower() for part in relative.parts[:-1]):
        return False
    return True


def frozen_hashes(log: bytes) -> dict[str, str]:
    values = {}
    for line in log.decode("utf-8").splitlines():
        if re.fullmatch(r"transcription frozen " + STAMP, line):
            break
        match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line)
        if match:
            values[match.group(2)] = match.group(1).lower()
    return values


def create(root: Path, output: Path) -> dict:
    root, output = root.resolve(), output.resolve()
    if not root.is_dir():
        raise RuntimeError("Bundle directory does not exist")
    if output.name != f"{PREFIX}.zip":
        raise RuntimeError(f"Final archive must be named {PREFIX}.zip")
    if root == output.parent or root in output.parents:
        raise RuntimeError("Final archive must be outside the work bundle")
    if output.exists():
        raise RuntimeError("Final archive already exists; refusing to overwrite it")

    report = Check(root, final=True).run()
    if not report["passed"]:
        return {"created": False, "validation": report}

    paths = []
    for path in sorted(root.rglob("*")):
        if not admissible(path, root):
            continue
        if path.is_symlink():
            raise RuntimeError(f"Symlink refused: {path.relative_to(root).as_posix()}")
        if path.is_file():
            stat = path.stat()
            paths.append((path, stat.st_size, stat.st_mtime_ns))
    names = {path.relative_to(root).as_posix() for path, _, _ in paths}
    missing = REQUIRED - names
    if missing:
        raise RuntimeError("Required archive members are missing: " + ", ".join(sorted(missing)))
    if VALIDATION_RECORD in names:
        raise RuntimeError(f"Reserved generated record already exists: {VALIDATION_RECORD}")

    # The log's frozen values independently certify the actual page bytes
    # copied into the archive, not merely the source files at an earlier instant.
    log_bytes = (root / "progress.log").read_bytes()
    frozen = frozen_hashes(log_bytes)
    frozen_names = {f"{PREFIX}_transcription.tex"} | {
        f"pages/{PREFIX}_12_scan{scan:03d}.tex" for scan in SCANS
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=".final_bundle_", suffix=".zip", dir=output.parent)
    os.close(descriptor)
    temporary = Path(temporary_name)
    created = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            archive.comment = f"{PREFIX}; final bundle; packaged_utc={created}".encode("ascii")
            for path, _, _ in paths:
                relative = path.relative_to(root).as_posix()
                data = path.read_bytes()
                if relative in frozen_names:
                    if hashlib.sha256(data).hexdigest() != frozen.get(relative):
                        raise RuntimeError(f"Archive bytes do not match frozen SHA-256: {relative}")
                if relative == "progress.log" and data != log_bytes:
                    raise RuntimeError("Progress log changed during packaging")
                # Preserve file timestamps and permissions while writing the
                # same bytes whose frozen digest was just checked.
                info = zipfile.ZipInfo.from_file(path, arcname=relative)
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
            record = dict(report)
            record.update({"packaged_utc": created, "frozen_hashes_verified_for_archive_bytes": len(frozen_names)})
            archive.writestr(VALIDATION_RECORD, json.dumps(record, ensure_ascii=False, indent=2) + "\n")
        for path, size, modified in paths:
            current = path.stat()
            if (current.st_size, current.st_mtime_ns) != (size, modified):
                raise RuntimeError("A work file changed during packaging; partial archive discarded")
        with zipfile.ZipFile(temporary) as archive:
            if archive.testzip() is not None:
                raise RuntimeError("Final ZIP failed its CRC check")
            if set(archive.namelist()) != names | {VALIDATION_RECORD}:
                raise RuntimeError("Final ZIP member list differs from the selected work files")
        os.link(temporary, output)
        digest = hashlib.sha256(output.read_bytes()).hexdigest()
    finally:
        temporary.unlink(missing_ok=True)
    return {
        "created": True,
        "path": str(output),
        "created_utc": created,
        "included_files": len(paths) + 1,
        "page_files": len(SCANS),
        "frozen_hashes_verified": len(frozen_names),
        "size_bytes": output.stat().st_size,
        "sha256": digest,
        "warnings": report["warnings"],
        "uploaded": False,
        "scope": "Structural consistency and frozen-byte preservation only; manuscript fidelity is not certified",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=SCRIPT_DIRECTORY.parent)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = args.output or args.root.resolve().parent / f"{PREFIX}.zip"
    try:
        result = create(args.root, output)
    except (OSError, RuntimeError, ValueError, UnicodeError, zipfile.BadZipFile) as error:
        print(json.dumps({"created": False, "error": str(error)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["created"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
