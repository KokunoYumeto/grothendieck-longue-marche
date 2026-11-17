#!/usr/bin/env python3
"""Freeze the completed one-reader transcription; never opens comparison sources."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import re
from validate_structure import Check, SCANS, PREFIX

root = Path(__file__).resolve().parent.parent
log_path = root / 'progress.log'
log = log_path.read_text()
assert 'transcription frozen ' not in log
assert not re.search(r'^context opened ', log, re.M)
assert 'notation comparison completed ' in log
for n in SCANS:
    assert re.search(rf'^scan {n:03d} audited ', log, re.M), n
pages = [root / 'pages' / f'{PREFIX}_12_scan{n:03d}.tex' for n in SCANS]
combined = root / f'{PREFIX}_transcription.tex'
assert not combined.exists()
combined.write_bytes(b''.join(p.read_bytes() for p in pages))
report = Check(root, False).run()
assert report['passed'], report
assert report['page_files'] == len(SCANS)
lines = []
for p in pages + [combined]:
    lines.append(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.relative_to(root).as_posix())
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log_path.open('a') as f:
    f.write('\n'.join(lines) + '\n')
    f.write('transcription frozen ' + now + '\n')
print('transcription frozen ' + now)
print(f'{len(pages)} page hashes and one combined hash recorded; {report["inventory_rows"]} inventory elements.')
print('Combined SHA-256: ' + hashlib.sha256(combined.read_bytes()).hexdigest())
