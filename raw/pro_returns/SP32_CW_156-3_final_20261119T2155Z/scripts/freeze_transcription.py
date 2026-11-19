#!/usr/bin/env python3
"""One-time freeze after the root reader's sixteen visual audits."""
from pathlib import Path
import hashlib,json
from record_page import ROOT,utc

manifest=ROOT/'records/frozen.sha256'
assert not manifest.exists(), 'Freeze already exists; do not rewrite it'
pages=sorted((ROOT/'pages').glob('*.tex'))
assert len(pages)==16
for n in range(26,42):
    p=ROOT/'records'/f'audit{n:03}.json'
    d=json.loads(p.read_text())
    assert d['scan']==n and d['reader'].startswith('/root')
combined=ROOT/'SP32_CW_156-3_transcription.tex'
assert combined.read_text()=='\n'.join(p.read_text().rstrip() for p in pages)+'\n'
files=pages+[combined]
rows=[(hashlib.sha256(p.read_bytes()).hexdigest(),p.relative_to(ROOT).as_posix()) for p in files]
manifest.write_text(''.join(f'{digest}  {name}\n' for digest,name in rows))
when=utc()
with (ROOT/'progress.log').open('a') as f:
    for digest,name in rows:f.write(f'sha256 {digest} {name}\n')
    f.write(f'transcription frozen {when}\n')
(ROOT/'records/freeze.json').write_text(json.dumps({'time_utc':when,'files':len(rows),'reader':'/root','context_opened_before_freeze':False,'manifest':'records/frozen.sha256'},indent=2)+'\n')
print(f'Transcription frozen {when}: {len(rows)} SHA-256 hashes')
