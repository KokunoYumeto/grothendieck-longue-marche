#!/usr/bin/env python3
"""Freeze the audited page stream before opening any contextual source."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
manifest = root / 'records/frozen_hashes.json'
if manifest.exists():
    raise SystemExit('Already frozen; refusing to replace manifest or transcription.')
scans = [n for n in range(77,127) if n != 99]
log = (root / 'progress.log').read_text()
paths = [root / 'pages' / f'MPL_154_077-126_154_scan{n:03d}.tex' for n in scans]
for n,p in zip(scans,paths):
    assert p.is_file(), n
    assert f'154 scan {n:03d} done ' in log, n
    assert f'scan {n:03d} audited ' in log, n
combined = root / 'MPL_154_077-126_transcription.tex'
combined.write_bytes(b''.join(p.read_bytes() for p in paths))
assert combined.read_bytes().startswith(b'\\cotefile{154}\n\\scanpage{77}')
files = {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
         for p in paths + [combined]}
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest.write_text(json.dumps({'frozen_utc': stamp, 'files':files},indent=2)+'\n')
with (root / 'progress.log').open('a') as f:
    for name,digest in files.items():
        f.write(f'SHA-256 {digest} {name}\n')
    f.write(f'transcription frozen {stamp}\n')
print(f'Frozen {len(paths)} pages plus exact combined fragment at {stamp}')
