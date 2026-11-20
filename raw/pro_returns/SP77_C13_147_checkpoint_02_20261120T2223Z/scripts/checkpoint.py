"""Create a new immutable work checkpoint at the requested 45-minute boundary.

The original attachment folders and regenerated halves are outside the work tree.
Uploading is deliberately a separate step so the receipt can be inspected.
"""
from datetime import datetime, timezone, timedelta
from pathlib import Path
import hashlib
import json
import sys
import zipfile

W = Path(__file__).resolve().parents[1]
number = int(sys.argv[1])
started = datetime(2026, 11, 20, 20, 53, 23, tzinfo=timezone.utc)
due = started + timedelta(minutes=45 * number)
now = datetime.now(timezone.utc)
if now < due:
    raise SystemExit(f"Checkpoint {number:02d} is not due until {due.isoformat()}")
target = W.parent / f"SP77_C13_147_checkpoint_{number:02d}.zip"
if target.exists():
    raise SystemExit("Refusing to replace an existing checkpoint")
with (W / 'progress.log').open('a') as f:
    f.write(f"checkpoint {number:02d} started {now.strftime('%Y-%m-%d %H:%M:%S UTC')}; scheduled {due.strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
with zipfile.ZipFile(target, 'x', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
    for path in sorted(W.rglob('*')):
        if path.is_file() and path.suffix != '.zip' and '__pycache__' not in path.parts:
            archive.write(path, path.relative_to(W))
with zipfile.ZipFile(target) as archive:
    bad = archive.testzip()
    if bad:
        raise SystemExit(f"Archive CRC failure: {bad}")
print(json.dumps({
    'path': str(target),
    'created': now.strftime('%Y-%m-%d %H:%M:%S UTC'),
    'bytes': target.stat().st_size,
    'sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
}))
