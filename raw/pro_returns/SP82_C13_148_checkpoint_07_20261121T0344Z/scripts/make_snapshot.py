"""Copy the complete deliverable tree before a scheduled archival encoding.

Source scans, witness packets, native halves and display proxies live outside
the deliverable tree. JPEG display proxies under readers are also excluded.
All evidence crops and work documentation are retained.
"""
from pathlib import Path
import shutil
import sys

OUT = Path(__file__).resolve().parents[1]
dest = Path(sys.argv[1]).resolve()
assert not dest.exists(), 'Snapshots are immutable and uniquely named.'
dest.mkdir(parents=True)
count = 0
size = 0
for p in sorted(OUT.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts or p.suffix == '.zip':
        continue
    if p.suffix.lower() in {'.jpg','.jpeg'} and any(k in p.parts for k in ('readers','previews','halves')):
        continue
    target = dest / p.relative_to(OUT)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, target)
    count += 1
    size += p.stat().st_size
print(f'Immutable snapshot: {count} files, {size} bytes, {dest}')
