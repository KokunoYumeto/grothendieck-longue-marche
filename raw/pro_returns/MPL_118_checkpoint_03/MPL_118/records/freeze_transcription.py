#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

root=Path(__file__).resolve().parents[1]
manifest=root/'records/frozen_sha256.json'
assert not manifest.exists(), 'The transcription has already been frozen.'
expected=list(range(2,13))+list(range(14,38))+list(range(39,42))
pages=[root/'pages'/f'MPL_118_118_scan{n:03d}.tex' for n in expected]
log=(root/'progress.log').read_text()
assert len(re.findall(r'^118 scan \d+ done ',log,re.M))==38
assert len(re.findall(r'^scan \d+ audited ',log,re.M))==38
assert 'context opened ' not in log
combined=root/'MPL_118_transcription.tex'
combined.write_text('\\cotefile{118}\n'+ '\n'.join(p.read_text().rstrip()+'\n' for p in pages))
files=pages+[combined]
hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest.write_text(json.dumps({'frozen_utc':stamp,'sha256':hashes},indent=2)+'\n')
with (root/'progress.log').open('a') as out:
    for name,digest in hashes.items(): out.write(f'SHA-256 {digest} {name}\n')
    out.write(f'transcription frozen {stamp}\n')
for p in files:p.chmod(0o444)
print(json.dumps({'frozen_utc':stamp,'files_hashed':len(hashes),'combined_sha256':hashes[combined.name], 'combined_bytes':combined.stat().st_size},indent=2))
