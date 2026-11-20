"""Freeze and verify page/combined SHA-256 values without compiling the edition."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys

E=Path(__file__).resolve().parents[1]
expected=[3]+list(range(5,28))
paths=[E/'pages'/f'145_scan{n:03d}.tex' for n in expected]+[E/'SP75_C13_145_transcription.tex']
hashes={str(p.relative_to(E)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
p=E/'transcription_sha256.json'
if sys.argv[1]=='freeze':
    assert not p.exists(),'Refusing to replace an earlier freeze'
    for n in expected:
        r=json.loads((E/'reader_reports'/f'145_scan{n:03d}_reviewed.json').read_text())
        assert r.get('audit')
    p.write_text(json.dumps({'frozen':now,'sha256':hashes},indent=2))
    with (E/'progress.log').open('a') as f:
        f.write('transcription frozen '+now+'\n')
        for name,h in hashes.items():f.write(h+'  '+name+'\n')
    print('Transcription frozen: 24 page hashes and combined hash recorded.')
elif sys.argv[1]=='verify':
    old=json.loads(p.read_text())['sha256']
    assert hashes==old,'Frozen transcription changed'
    with (E/'progress.log').open('a') as f:f.write('frozen transcription verified unchanged '+now+': all 24 page SHA-256 hashes and the combined transcription SHA-256 match the freeze.\n')
    print('All 25 frozen hashes are unchanged.')
else:raise SystemExit('Expected freeze or verify')
