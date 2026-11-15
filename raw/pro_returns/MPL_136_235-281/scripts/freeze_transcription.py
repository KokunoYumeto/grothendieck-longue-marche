"""Freeze once, or verify the recorded hashes without changing the transcription."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
LOG=ROOT/'progress.log'
STEM='MPL_136_235-281'
expected=[n for n in range(235,282) if n!=243]
now=lambda:datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
log=LOG.read_text()

if '--freeze' in sys.argv:
    assert 'transcription frozen' not in log
    pages=[ROOT/'pages'/f'{STEM}_136_scan{n}.tex' for n in expected]
    assert set(map(int,re.findall(r'^136 scan (\d+) done ',log,re.M)))==set(expected)
    assert set(map(int,re.findall(r'^scan (\d+) audited ',log,re.M)))==set(expected)
    combined=ROOT/f'{STEM}_transcription.tex'
    combined.write_bytes(b''.join(p.read_bytes() for p in pages))
    with LOG.open('a') as f:
        for p in pages+[combined]:
            f.write(f'sha256 {p.relative_to(ROOT)} {hashlib.sha256(p.read_bytes()).hexdigest()}\n')
        f.write(f'transcription frozen {now()}\n')
    print('Frozen: 46 individual pages and exact ordered combined transcription.')
else:
    assert 'transcription frozen' in log
    records=re.findall(r'^sha256 (\S+) ([0-9a-f]{64})$',log,re.M)
    assert len(records)==47
    for name,digest in records:
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
    assert (ROOT/f'{STEM}_transcription.tex').read_bytes()==b''.join((ROOT/'pages'/f'{STEM}_136_scan{n}.tex').read_bytes() for n in expected)
    with LOG.open('a') as f:
        f.write(f'transcription hashes unchanged {now()}: all 46 page files and combined transcription match the pre-context SHA-256 freeze.\n')
    print('All 47 frozen SHA-256 values unchanged; ordered concatenation unchanged.')
