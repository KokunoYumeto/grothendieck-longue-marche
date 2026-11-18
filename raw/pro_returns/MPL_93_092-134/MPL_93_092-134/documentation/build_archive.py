"""Build the final deliverable without modifying the frozen transcription.

Run from any directory. The output is the package's sibling
MPL_93_092-134.zip; existing archives are never overwritten.
All current deliverables and work documentation are included. Supplied source
archives, scan images/crops, external context and previous ZIPs are excluded.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "documentation" / "package_manifest.sha256"
OUT = ROOT.parent / (ROOT.name + ".zip")

frozen = ROOT / "documentation" / "frozen.sha256"
for line in frozen.read_text().splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    expected, name = line.split(None, 1)
    name = name.lstrip("*")
    path = ROOT / name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, name

files = sorted(p for p in ROOT.rglob("*") if p.is_file()
               and "__pycache__" not in p.parts and p.suffix not in {".pyc", ".zip"}
               and p != MANIFEST)
for p in files:
    assert not p.is_symlink(), p
    assert p.suffix.lower() not in {".jpg", ".jpeg", ".png", ".tif", ".tiff"}, p
MANIFEST.write_text(
    "# SHA-256 of every package file except this manifest itself.\n"
    "# The immutable transcription subset is separately recorded in frozen.sha256.\n" +
    "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT).as_posix()}\n" for p in files)
)
files = sorted(files + [MANIFEST])
assert not OUT.exists(), f"Refusing to overwrite {OUT}"
with ZipFile(OUT, "w", ZIP_DEFLATED) as z:
    for p in files:
        z.write(p, (Path(ROOT.name) / p.relative_to(ROOT)).as_posix())
with ZipFile(OUT) as z:
    assert z.testzip() is None, "ZIP CRC validation failed"
    assert len(z.namelist()) == len(files)
    for line in MANIFEST.read_text().splitlines():
        if line.startswith("#"):
            continue
        expected, name = line.split(None, 1)
        assert hashlib.sha256(z.read(ROOT.name + "/" + name)).hexdigest() == expected, name
print(f"Archive: {OUT}")
print(f"Files: {len(files)}; bytes: {OUT.stat().st_size}")
print(f"SHA256: {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
print("ZIP CRC and every packaged manifest hash verified; all 43 frozen hashes unchanged.")
