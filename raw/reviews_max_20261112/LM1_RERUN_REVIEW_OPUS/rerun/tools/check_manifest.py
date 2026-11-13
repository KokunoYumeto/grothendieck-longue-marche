"""Verify MANIFEST.sha256 of the unpacked return (read-only)."""
import hashlib
import sys
from pathlib import Path

root = Path(sys.argv[1])
ok = bad = missing = 0
listed = set()
for line in (root / "MANIFEST.sha256").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    digest, name = line.split(maxsplit=1)
    name = name.lstrip("*").strip()
    listed.add(name)
    p = root / name
    if not p.exists():
        missing += 1
        print("MISSING", name)
        continue
    if hashlib.sha256(p.read_bytes()).hexdigest() == digest:
        ok += 1
    else:
        bad += 1
        print("MISMATCH", name)
present = {str(p.relative_to(root)).replace("\\", "/") for p in root.rglob("*") if p.is_file()}
extra = sorted(present - listed - {"MANIFEST.sha256"})
print(f"ok={ok} mismatch={bad} missing={missing} unlisted_files={len(extra)}")
for e in extra:
    print("UNLISTED", e)
