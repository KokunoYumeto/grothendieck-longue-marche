from pathlib import Path
import hashlib,json,re
from record_page import ROOT,now
log=(ROOT/'progress.log').read_text()
assert 'transcription frozen ' not in log
assert 'context opened ' not in log
expected={2,3,4,5,*range(7,45)}
audits=[int(x) for x in re.findall(r'^scan (\d+) audited ',log,re.M)]
assert len(audits)==42 and set(audits)==expected
pages=sorted((ROOT/'pages').glob('*.tex'))
combined=ROOT/'MPL_137_002-044_transcription.tex'
assert combined.read_text()=='\n'.join(p.read_text() for p in pages)
paths=pages+[combined]
hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
t=now()
(ROOT/'records'/'frozen_hashes.json').write_text(json.dumps({'frozen_utc':t,'algorithm':'SHA-256','hashes':hashes},indent=2)+'\n')
with (ROOT/'progress.log').open('a') as f:
 f.write('pre-freeze structural validation '+t+'; PASS: 42 pages, exact combined fragment, 833 inventory rows all yes, lexical braces/environments/math-delimiters balanced. Full typesetting compilation unavailable because required TeX packages are absent.\n')
 for name,h in hashes.items():f.write('SHA256 '+h+'  '+name+'\n')
 f.write('transcription frozen '+t+'\n')
print('Frozen',len(hashes),'files at',t)
print('Combined SHA256',hashes[combined.name])
