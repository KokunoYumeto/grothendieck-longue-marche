"""Create a numbered hourly snapshot, excluding the supplied sources and images."""
from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys, zipfile

root = Path(__file__).resolve().parents[1]
number = int(sys.argv[1])
start = datetime(2026, 11, 17, 14, 35, 35, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)
assert now >= start + timedelta(hours=number), 'Hourly checkpoint is not due yet'
dest = root.parent / f'MPL_136_328-376_checkpoint_{number:02}.zip'
assert not dest.exists(), 'Never overwrite an earlier checkpoint'
with (root / 'progress.log').open('a', encoding='utf-8') as f:
    f.write(f'checkpoint {number:02} snapshot ' + now.strftime('%Y-%m-%d %H:%M:%S UTC') + '\n')
with zipfile.ZipFile(dest, 'x', compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts:
            z.write(p, p.relative_to(root))
print(dest)
