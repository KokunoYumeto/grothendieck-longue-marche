"""Create one complete work ZIP at the requested hourly boundary."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import sys, time, zipfile

root=Path(__file__).resolve().parents[1]
n=int(sys.argv[1])
start=datetime(2026,11,15,10,0,31,tzinfo=timezone.utc)
due=start+timedelta(hours=n)
remaining=(due-datetime.now(timezone.utc)).total_seconds()
if remaining>60: raise SystemExit('Hourly checkpoint is not due yet.')
if remaining>0: time.sleep(remaining)
name=f'MPL_91_099-143_checkpoint_{n:02d}.zip'
dest=root.parent/name
if dest.exists(): raise SystemExit('Never overwrite an earlier checkpoint.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:f.write(f'checkpoint {n:02d} assembled {now}\n')
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts:
            z.write(p,p.relative_to(root))
print(str(dest))
