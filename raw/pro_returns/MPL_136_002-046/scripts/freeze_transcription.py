"""Concatenate the independently saved pages byte-for-byte, then freeze once.

Use --combine-only before checks; run with no option only after visual audits
and notation reconciliation. No context input is read here.
"""
import argparse
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re

p = argparse.ArgumentParser()
p.add_argument('--combine-only', action='store_true')
args = p.parse_args()
root = Path(__file__).resolve().parents[1]
scans = [n for n in range(2, 47) if n != 19]
pages = [root / f'pages/MPL_136_002-046_136_scan{n:03}.tex' for n in scans]
log = root / 'progress.log'
record = log.read_text()
assert 'context opened' not in record
assert 'transcription frozen' not in record
assert len(pages) == 44 and all(p.is_file() for p in pages)
assert set(map(int, re.findall(r'^136 scan (\d+) done ', record, re.M))) == set(scans)
assert set(map(int, re.findall(r'^scan (\d+) audited ', record, re.M))) == set(scans)
assert 'notation reconciliation completed' in record
combined = root / 'MPL_136_002-046_transcription.tex'
combined.write_bytes(b''.join(p.read_bytes() for p in pages))
assert combined.read_bytes() == b''.join(p.read_bytes() for p in pages)
if args.combine_only:
    print(f'Combined {len(pages)} pages; {combined.stat().st_size} bytes; no separators added.')
else:
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    with log.open('a') as f:
        f.write(f'transcription frozen {now}\n')
        for path in pages + [combined]:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            f.write(f'SHA-256 {digest} {path.relative_to(root).as_posix()}\n')
    print(f'Frozen 44 pages plus combined transcription at {now}.')
