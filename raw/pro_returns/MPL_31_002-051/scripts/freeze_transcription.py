from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
base=Path(__file__).resolve().parent.parent
utc=lambda:datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
prefix='MPL_31_002-051'
expected=set(range(2,52))-{34,40,41,46}
pages=sorted((base/'pages').glob(prefix+'_31_scan*.tex'))
assert {int(re.search(r'scan(\d+)',p.name).group(1)) for p in pages}==expected
log=base/'progress.log';s=log.read_text()
assert 'transcription frozen' not in s and 'context opened' not in s
assert {int(n) for n in re.findall(r'^31 scan (\d+) done ',s,re.M)}==expected
assert {int(n) for n in re.findall(r'^scan (\d+) audited ',s,re.M)}==expected
combined=base/(prefix+'_transcription.tex')
assert combined.read_bytes()==b''.join(p.read_bytes() for p in pages)
manifest={str(p.relative_to(base)):hashlib.sha256(p.read_bytes()).hexdigest() for p in pages+[combined]}
stamp=utc()
(base/'records/frozen_sha256.json').write_text(json.dumps({'frozen_utc':stamp,'files':manifest},indent=2)+'\n')
with log.open('a') as f:
 for name,h in manifest.items():f.write(f'SHA-256 {h}  {name}\n')
 f.write('transcription frozen '+stamp+'\n')
print('Frozen',len(manifest),'files at',stamp)
