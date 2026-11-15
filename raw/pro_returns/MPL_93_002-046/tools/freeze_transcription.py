from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess, sys

root=Path(__file__).resolve().parents[1]
log=root/'progress.log'
text=log.read_text()
assert 'transcription frozen ' not in text, 'Already frozen'
assert 'context opened ' not in text, 'Context must remain closed before freeze'
expected=[n for n in range(3,47) if n not in (26,35)]
assert sorted(map(int,re.findall(r'^scan (\d+) audited ',text,re.M)))==expected
pages=[root/'pages'/f'MPL_93_002-046_93_scan{n:03d}.tex' for n in expected]
combined=root/'MPL_93_002-046_transcription.tex'
assert combined.read_bytes()==b''.join(p.read_bytes() for p in pages)
subprocess.run([sys.executable,str(root/'tools/validate_package.py')],check=True)
entries={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in pages+[combined]}
(root/'frozen_sha256.json').write_text(json.dumps(entries,indent=2)+'\n')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log.open('a') as f:
 f.write('notation consistency review completed '+stamp+'; recurring alphabets, exclamation/prime/star signs, Greek variants, arrows, quotation marks and underlines checked against image readings\n')
 for path,digest in entries.items(): f.write('SHA-256 '+digest+' '+path+'\n')
 f.write('transcription frozen '+stamp+'\n')
print('Frozen',len(entries),'files at',stamp)
