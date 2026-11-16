#!/usr/bin/env python3
"""Freeze only a complete, personally audited transcription, before context opens."""
import hashlib,json,re
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
log=root/'progress.log';old=log.read_text()
assert 'transcription frozen ' not in old and 'context opened ' not in old
for n in range(2,36):
 assert re.search(rf'^scan {n:03d} audited ',old,re.M),n
pages=sorted((root/'pages').glob('*.tex'));assert len(pages)==34
combined=root/'MPL_60_002-035_transcription.tex'
assert combined.read_bytes()==b''.join(p.read_bytes() for p in pages)
for p in pages:
 n=int(p.stem[-3:]);d=json.loads((root/f'records/page{n:03d}.json').read_text());assert p.read_bytes()==d['text'].encode()
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
files={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in pages+[combined]}
(root/'records/frozen_hashes.json').write_text(json.dumps({'frozen_utc':now,'files':files},indent=2)+'\n')
with log.open('a') as f:
 f.write(f'notation reconciled {now}\n')
 for path,h in files.items():f.write(f'SHA-256 {h} {path}\n')
 f.write(f'transcription frozen {now}\n')
print(f'Frozen {len(pages)} page files and combined fragment at {now}')
