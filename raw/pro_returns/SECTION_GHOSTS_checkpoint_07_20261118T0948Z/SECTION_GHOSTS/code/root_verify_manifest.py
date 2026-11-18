"""Verify the supplied archive's manifest without changing any source file."""
from pathlib import Path
import csv
import hashlib

root = Path(__file__).resolve().parents[2] / "background"
rows = list(csv.DictReader((root / "MANIFEST.tsv").open(), delimiter="\t"))
errors = []
total = 0
for row in rows:
    path = root / row["file"]
    if not path.is_file():
        errors.append((row["file"], "missing"))
        continue
    data = path.read_bytes()
    total += len(data)
    if len(data) != int(row["bytes"]):
        errors.append((row["file"], "size mismatch"))
    if hashlib.sha256(data).hexdigest() != row["sha256"]:
        errors.append((row["file"], "hash mismatch"))
print(f"Manifest entries checked: {len(rows)}")
print(f"Total source bytes checked: {total}")
print(f"Errors: {len(errors)}")
for error in errors:
    print(error)
assert not errors
