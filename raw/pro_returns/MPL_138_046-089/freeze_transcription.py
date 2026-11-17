from pathlib import Path
import hashlib
import re
from workflow import ROOT, PREFIX, now, log

expected=[n for n in range(46,90) if n not in (79,88)]
pages=sorted((ROOT/'pages').glob('*.tex'))
assert [int(re.search(r'scan(\d+)',p.name)[1]) for p in pages]==expected
progress=(ROOT/'progress.log').read_text()
assert 'transcription frozen ' not in progress
for n in expected:
    assert f'scan {n:03} audited ' in progress
combined=ROOT/(PREFIX+'_transcription.tex')
assert combined.read_bytes()==b'\n'.join(p.read_bytes() for p in pages)
manifest=[]
for p in [*pages,combined]:
    manifest.append(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT)}')
(ROOT/'frozen_sha256.txt').write_text('\n'.join(manifest)+'\n')
log('transcription frozen '+now())
for line in manifest:log('SHA-256 '+line)
print('Frozen 42 page files and the combined transcription, 43 SHA-256 hashes recorded.')
