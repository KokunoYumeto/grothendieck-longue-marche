#!/usr/bin/env python3
"""Combine the audited page stream and freeze its exact UTF-8 bytes once."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, re

r=Path(__file__).resolve().parents[1]
log=r/'progress.log'
history=log.read_text()
assert not re.search(r'^transcription frozen ',history,re.M), 'Already frozen'
assert not re.search(r'^context opened ',history,re.M), 'Context already opened'
scans=[n for n in range(48,95) if n!=79]
paths=[r/'pages'/f'MPL_136_047-094_136_scan{n:03}.tex' for n in scans]
for n,p in zip(scans,paths):
    prefix='\\cotefile{136}\n' if n==48 else ''
    assert p.read_text().startswith(prefix+f'\\scanpage{{{n}}}')
    assert re.search(rf'^scan {n:03} audited ',history,re.M)
    assert re.search(rf'^136 scan {n:03} done ',history,re.M)
combined=r/'MPL_136_047-094_transcription.tex'
combined.write_text(''.join(p.read_text().rstrip()+'\n\n' for p in paths),encoding='utf-8')
paths.append(combined)
manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(r))+'\n' for p in paths)
(r/'validation').mkdir(exist_ok=True)
(r/'validation/transcription_frozen.sha256').write_text(manifest)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log.open('a') as f:
    f.write('SHA-256 frozen transcription manifest (46 pages and combined fragment)\n'+manifest)
    f.write('transcription frozen '+now+'\n')
print('Frozen '+str(len(paths))+' files at '+now)
print('Combined bytes '+str(combined.stat().st_size))
