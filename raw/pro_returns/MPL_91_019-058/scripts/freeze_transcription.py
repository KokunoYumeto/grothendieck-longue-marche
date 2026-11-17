from pathlib import Path
import hashlib,re
from record_page import ROOT,now
log=ROOT/'progress.log'; prior=log.read_text()
assert 'transcription frozen' not in prior
assert 'context opened' not in prior
nums=[n for n in range(19,59) if n not in (30,33)]
ps=[ROOT/'pages'/f'MPL_91_019-058_91_scan{n:03}.tex' for n in nums]
assert len(list((ROOT/'pages').glob('*.tex')))==38
for n,p in zip(nums,ps):
 assert p.is_file() and p.stat().st_size
 assert len(re.findall(rf'^scan {n:03} audited .*$',prior,re.M))==1
combined=ROOT/'MPL_91_019-058_transcription.tex'
assert combined.read_bytes()==b''.join(p.read_bytes() for p in ps)
records=[]
for p in ps+[combined]:
 records.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(ROOT)))
with log.open('a') as f:
 f.write('notation comparison completed before context '+now()+'\n')
 f.write('\n'.join(records)+'\n')
 f.write('transcription frozen '+now()+'\n')
print('Frozen 38 pages plus exact concatenation; 39 SHA-256 records saved.')
