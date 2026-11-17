from pathlib import Path
from datetime import datetime, timezone, timedelta
from zipfile import ZipFile, ZIP_DEFLATED
import sys

root=Path(__file__).resolve().parents[1]
n=int(sys.argv[1])
start=datetime.strptime((root/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
now=datetime.now(timezone.utc)
assert now >= start+timedelta(hours=n), 'Hourly checkpoint is not due yet.'
out=root.parent/f'MPL_15_170-194r_checkpoint_{n:02d}.zip'
assert not out.exists(), 'Never overwrite a checkpoint.'
with (root/'progress.log').open('a') as f:f.write(f'checkpoint {n:02d} assembled '+now.strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
files=[p for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc']
with ZipFile(out,'x',ZIP_DEFLATED) as z:
 for p in files:z.write(p,p.relative_to(root))
with ZipFile(out) as z:assert z.testzip() is None
print(str(out.resolve()))
print(f'{len(files)} files; {out.stat().st_size} bytes')
