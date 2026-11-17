#!/usr/bin/env python3
"""Package completed work, retaining records and excluding inputs/caches."""
from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import sys
import zipfile


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    package = "MPL_136_282-327"
    destination = root.parent / f"{package}.zip"
    validation = subprocess.run(
        [sys.executable, str(root / "scripts/validate_package.py"),
         "--final", "--strict-macros"],
        cwd=root, capture_output=True, text=True,
    )
    report = validation.stdout + validation.stderr
    (root / "records/final_validation.txt").write_text(report, encoding="utf-8")
    print(report, end="")
    if validation.returncode:
        raise SystemExit(validation.returncode)
    subprocess.run(
        [sys.executable, str(root / "scripts/assemble_and_freeze.py"), "--verify"],
        cwd=root, check=True,
    )
    files = sorted(
        p for p in root.rglob("*")
        if p.is_file() and "__pycache__" not in p.relative_to(root).parts
    )
    allowed = {".tex", ".md", ".csv", ".jsonl", ".log", ".sha256", ".py", ".txt"}
    unexpected = [str(p.relative_to(root)) for p in files if p.suffix not in allowed]
    if unexpected:
        raise SystemExit(f"Unexpected files; inspect before packaging: {unexpected}")
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            archive.write(path, path.relative_to(root).as_posix())
    with zipfile.ZipFile(destination) as archive:
        bad = archive.testzip()
        if bad:
            raise SystemExit(f"CRC failure: {bad}")
        names = archive.namelist()
        expected = {
            f"pages/{package}_136_scan{n:03d}.tex"
            for n in range(282, 328) if n != 319
        }
        actual = {name for name in names if name.startswith("pages/")}
        if actual != expected:
            raise SystemExit("Archived page set differs from the required 45 pages")
        entries = archive.read("frozen_hashes.sha256").decode("utf-8").splitlines()
        if len(entries) != 46:
            raise SystemExit("Frozen manifest must contain 46 entries")
        for entry in entries:
            expected_hash, name = entry.split("  ", 1)
            if hashlib.sha256(archive.read(name)).hexdigest() != expected_hash:
                raise SystemExit(f"Frozen hash mismatch inside archive: {name}")
        for path in files:
            if archive.read(path.relative_to(root).as_posix()) != path.read_bytes():
                raise SystemExit(f"Archived file changed while packaging: {path.name}")
    print(f"Archive: {destination}")
    print(f"Files: {len(files)}; page files: 45; frozen hashes verified: 46; CRC: passed")
    print(f"Bytes: {destination.stat().st_size}")
    print(f"SHA-256: {hashlib.sha256(destination.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
