#!/usr/bin/env python3
"""Freeze the personally audited transcription once, or verify existing hashes.

This script does not inspect images and does not certify transcription accuracy.
It refuses to create a freeze before all page done/audited events exist or after
context has been opened. Run with --verify after the research phase.
"""
from pathlib import Path
import argparse, hashlib, re
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
SCANS=[n for n in range(1,35) if n not in (14,24)]
parser=argparse.ArgumentParser()
parser.add_argument('--verify',action='store_true')
a=parser.parse_args()
log=ROOT/'progress.log'
s=log.read_text()
paths=[ROOT/'pages'/f'MPL_159_159_scan{n:03}.tex' for n in SCANS]+[ROOT/'MPL_159_transcription.tex']
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if a.verify:
    recorded=dict(re.findall(r'^sha256 (\S+) ([a-f0-9]{64})$',s,re.M))
    assert 'transcription frozen ' in s, 'Not frozen'
    assert len(recorded)==33, f'Expected 33 hashes; got {len(recorded)}'
    for p in paths:
        rel=p.relative_to(ROOT).as_posix()
        assert hashlib.sha256(p.read_bytes()).hexdigest()==recorded[rel], f'Hash changed: {rel}'
    with log.open('a') as f: f.write(f'hashes unchanged {now}: all 32 page files and combined transcription match the pre-context freeze\n')
    print('VERIFIED: all 33 frozen SHA-256 hashes unchanged')
else:
    assert 'transcription frozen ' not in s, 'Already frozen'
    assert 'context opened ' not in s, 'Context already opened'
    for n in SCANS:
        assert re.search(fr'^159 scan {n:03} done ',s,re.M),f'Missing completion {n}'
        assert re.search(fr'^scan {n:03} audited ',s,re.M),f'Missing personal audit {n}'
    assert paths[-1].read_bytes()==b''.join(p.read_bytes() for p in paths[:-1]),'Combined transcription mismatch'
    hashes=[(p.relative_to(ROOT).as_posix(),hashlib.sha256(p.read_bytes()).hexdigest()) for p in paths]
    (ROOT/'TRANSCRIPTION_SHA256SUMS').write_text(''.join(f'{h}  {p}\n' for p,h in hashes))
    with log.open('a') as f:
        for p,h in hashes: f.write(f'sha256 {p} {h}\n')
        f.write(f'transcription frozen {now}\n')
    print(f'Frozen {len(hashes)} files at {now}')
