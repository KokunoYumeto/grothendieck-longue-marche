#!/usr/bin/env python3
"""Validate and assemble the final ZIP without changing frozen transcription files."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile


PREFIX = "MPL_11_043-058+56"
ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_SUFFIXES = {".pyc", ".aux", ".xdv", ".fmt"}
SOURCE_SUFFIXES = {".zip", ".pdf", ".png", ".jpg", ".jpeg"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def check_command(script: str, *arguments: str) -> dict:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script), *arguments],
        check=True, capture_output=True, text=True,
    )
    return json.loads(completed.stdout)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()
    output = args.output_directory.resolve()
    if output == ROOT or ROOT in output.parents:
        raise RuntimeError("The archive output directory must be outside the package.")
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"{PREFIX}.zip"
    if archive.exists():
        raise FileExistsError(f"Refusing to overwrite {archive}")

    required = [
        f"{PREFIX}_transcription.tex", f"{PREFIX}_doubts.md",
        f"{PREFIX}_inventory.csv", f"{PREFIX}_notes.md", "progress.log", "README.md",
        "records/final_research_preflight.md", "records/context_searches.json",
        "records/transcription_freeze.json", "records/transcription_sha256.txt",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            raise FileNotFoundError(relative)

    preflight = (ROOT / "records/final_research_preflight.md").read_text()
    for label, relative in [
        ("Main notes SHA-256", f"{PREFIX}_notes.md"),
        ("Context-search JSON SHA-256", "records/context_searches.json"),
    ]:
        match = re.search(re.escape(label) + r": `([0-9a-f]{64})`", preflight)
        if match is None or digest((ROOT / relative).read_bytes()) != match.group(1):
            raise RuntimeError(f"The final research preflight snapshot differs: {relative}")

    structure = check_command("validate_package.py")
    if structure["status"] != "passed" or structure["warnings"]:
        raise RuntimeError(f"Structural validation did not pass cleanly: {structure}")
    (ROOT / "records/final_structure_validation.json").write_text(
        json.dumps(structure, ensure_ascii=False, indent=2) + "\n"
    )

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    with (ROOT / "progress.log").open("a") as log:
        log.write(f"research notes completed {stamp} notes=104 final_preflight=passed\n")
        log.write(f"final package assembly {stamp} filename={PREFIX}.zip\n")

    frozen_check = check_command("verify_frozen_transcription.py", "--log")
    if not frozen_check["unchanged"] or frozen_check["files_checked"] != 51:
        raise RuntimeError(f"Frozen transcription check failed: {frozen_check}")
    (ROOT / "records/final_frozen_check.json").write_text(
        json.dumps(frozen_check, ensure_ascii=False, indent=2) + "\n"
    )

    manifest = ROOT / "records/package_manifest.sha256"
    files = sorted(
        p for p in ROOT.rglob("*")
        if p.is_file() and p != manifest
        and "__pycache__" not in p.parts and p.suffix.lower() not in EXCLUDED_SUFFIXES
    )
    forbidden = [str(p.relative_to(ROOT)) for p in files if p.suffix.lower() in SOURCE_SUFFIXES]
    if forbidden:
        raise RuntimeError(f"Source or binary files must not enter the final package: {forbidden}")
    hashes = {p.relative_to(ROOT).as_posix(): digest(p.read_bytes()) for p in files}
    manifest.write_text("".join(f"{sha}  {name}\n" for name, sha in hashes.items()))
    files.append(manifest)
    files.sort()

    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for path in files:
            z.write(path, path.relative_to(ROOT).as_posix())

    freeze = json.loads((ROOT / "records/transcription_freeze.json").read_text())
    with zipfile.ZipFile(archive) as z:
        bad_crc = z.testzip()
        if bad_crc is not None:
            raise RuntimeError(f"Archive CRC check failed: {bad_crc}")
        names = z.namelist()
        if len(names) != len(set(names)) or len(names) != len(files):
            raise RuntimeError("Archive member coverage or uniqueness failed.")
        if sum(name.startswith("pages/") and name.endswith(".tex") for name in names) != 50:
            raise RuntimeError("Archive page count differs from 50.")
        for name, expected in hashes.items():
            if digest(z.read(name)) != expected:
                raise RuntimeError(f"Archive member hash mismatch: {name}")
        if z.read("records/package_manifest.sha256") != manifest.read_bytes():
            raise RuntimeError("Archive manifest differs from the checked manifest.")
        for name, expected in freeze["hashes"].items():
            if digest(z.read(name)) != expected:
                raise RuntimeError(f"Frozen archive member differs: {name}")

    print(json.dumps({
        "archive": str(archive),
        "bytes": archive.stat().st_size,
        "files": len(files),
        "page_files": 50,
        "frozen_hashes_verified": len(freeze["hashes"]),
        "member_hashes_verified": len(hashes),
        "crc_check": "passed",
        "sha256": digest(archive.read_bytes()),
    }, indent=2))


if __name__ == "__main__":
    main()
