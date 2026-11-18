#!/usr/bin/env python3
"""Package this completed directory; verify frozen text and ZIP integrity."""
from pathlib import Path
import hashlib
import json
import re
import zipfile

root = Path(__file__).resolve().parents[1]
destination = root.parent / "MPL_64_116-157.zip"
required = {
    "MPL_64_116-157_transcription.tex",
    "MPL_64_116-157_doubts.md",
    "MPL_64_116-157_inventory.csv",
    "MPL_64_116-157_notes.md",
    "CHECK_EVENTS.tsv",
    "progress.log",
    "SHA256SUMS.txt",
    "STRUCTURAL_VALIDATION.txt",
}
for name in required:
    assert (root / name).is_file() and (root / name).stat().st_size, name

hashes = []
for line in (root / "SHA256SUMS.txt").read_text().splitlines():
    if not line.strip() or line.lstrip().startswith("#"):
        continue
    match = re.fullmatch(r"([0-9a-f]{64})\s+\*?(.+)", line)
    assert match, line
    expected, name = match.groups()
    actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
    assert actual == expected, name
    hashes.append(name)
assert len(hashes) == 40
assert len(list((root / "pages").glob("*.tex"))) == 39

files = sorted(p for p in root.rglob("*") if p.is_file()
               and "__pycache__" not in p.parts
               and not any(part.startswith(".") for part in p.relative_to(root).parts))
for path in files:
    assert path.suffix.lower() not in {".zip", ".jpg", ".jpeg", ".png", ".pdf"}, path
names = {p.relative_to(root).as_posix() for p in files}
assert required <= names

with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in files:
        archive.write(path, path.relative_to(root).as_posix())
with zipfile.ZipFile(destination) as archive:
    assert archive.testzip() is None
    assert set(archive.namelist()) == names
    for name in hashes:
        assert archive.read(name) == (root / name).read_bytes(), name
print(json.dumps({
    "file": str(destination), "entries": len(files),
    "bytes": destination.stat().st_size,
    "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
    "frozen_transcription_hashes_unchanged": len(hashes),
    "zip_crc": "PASS", "required_deliverables": "PASS",
}, indent=2))
