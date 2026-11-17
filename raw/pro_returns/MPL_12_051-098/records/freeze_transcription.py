from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

base=Path(__file__).resolve().parents[1]
prefix='MPL_12_051-098'
expected=list(range(51,66))+[67]+list(range(71,81))+[82,84]+list(range(86,97))
log=base/'progress.log'
history=log.read_text()
if 'context opened ' in history:
    raise SystemExit('Context is already open; freezing or rewriting is prohibited.')
if 'transcription frozen ' in history:
    raise SystemExit('Already frozen; use verify_frozen.py instead.')
audited=[int(x) for x in re.findall(r'^scan (\d+) audited ',history,re.M)]
done=[int(x) for x in re.findall(r'^12 scan (\d+) done ',history,re.M)]
assert done==expected,(done,expected)
assert audited==expected,(audited,expected)
paths=[base/'pages'/f'{prefix}_12_scan{s:03d}.tex' for s in expected]
combined=base/f'{prefix}_transcription.tex'
assert combined.read_bytes()==b'\n'.join(p.read_bytes() for p in paths)
paths.append(combined)
hashes={p.relative_to(base).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(base/'records'/'frozen_transcription_hashes.json').write_text(json.dumps({'frozen_utc':now,'sha256':hashes},indent=2)+'\n')
with log.open('a') as f:
    f.write('notation consistency review completed '+now+'; see doubts table and visual audit records\n')
    for path,digest in hashes.items():f.write('SHA-256 '+digest+' '+path+'\n')
    f.write('transcription frozen '+now+'\n')
for p in paths:p.chmod(0o444)
print(json.dumps({'frozen_utc':now,'page_files':len(expected),'hashed_files':len(hashes)},indent=2))
