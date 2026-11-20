"""Snapshot all written deliverables/documentation; never include supplied inputs or earlier ZIPs."""
from pathlib import Path
import datetime, hashlib, json, sys, zipfile

out = Path(__file__).resolve().parents[1]
n = int(sys.argv[1])
start = datetime.datetime(2026, 11, 20, 18, 19, 5, tzinfo=datetime.timezone.utc)
now = datetime.datetime.now(datetime.timezone.utc)
due = start + datetime.timedelta(minutes=45*n)
if now < due:
    raise SystemExit(f"Checkpoint {n:02d} not due until {due.isoformat()}")
dest = out.parent / f"SP117_CW_97+123+162-1_checkpoint_{n:02d}.zip"
if dest.exists():
    raise SystemExit(f"Refusing to overwrite {dest}")
stamp = now.strftime('%Y-%m-%d %H:%M:%S UTC')
with (out/'progress.log').open('a') as f:
    f.write(f"checkpoint {n:02d} snapshot {stamp}; scheduled at {due.strftime('%Y-%m-%d %H:%M:%S UTC')}; complete current deliverables and documentation, no supplied inputs or prior checkpoint ZIPs.\n")
files = sorted(p for p in out.rglob('*') if p.is_file() and not p.is_symlink() and p.suffix != '.zip' and '__pycache__' not in p.parts)
with zipfile.ZipFile(dest, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for p in files:
        z.write(p, p.relative_to(out))
with zipfile.ZipFile(dest) as z:
    bad = z.testzip()
    if bad: raise RuntimeError(f'ZIP CRC error: {bad}')
print(json.dumps({'path':str(dest), 'bytes':dest.stat().st_size, 'files':len(files), 'sha256':hashlib.file_digest(dest.open('rb'),'sha256').hexdigest(), 'snapshot_utc':stamp},indent=2))
