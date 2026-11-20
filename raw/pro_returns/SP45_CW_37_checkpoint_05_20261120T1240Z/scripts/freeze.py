#!/usr/bin/env python3
"""Freeze or verify the decided transcription; no reading decisions."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
root=Path(__file__).resolve().parents[1]
def utc():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((root/'run_state.json').read_text())
assert state['completed_scans']==state['scan_order'],'Not all pages are decided'
paths=sorted((root/'pages').glob('*.tex'))+[root/'SP45_CW_37_transcription.tex']
assert len(paths)==31
if sys.argv[1]=='freeze':
    assert not (root/'transcription_sha256.json').exists(),'Already frozen'
    for n in state['scan_order']:
        for r in ['r1','r2','r3']:
            d=root/f'readers/scan{n:03d}/{r}'
            assert (d/'reading.tex').is_file() and (d/'report.json').is_file(),d
    hashes={str(p.relative_to(root)):digest(p) for p in paths}
    (root/'transcription_sha256.json').write_text(json.dumps(hashes,indent=2)+'\n')
    with (root/'progress.log').open('a') as f:
        f.write('transcription frozen '+utc()+'\n')
        for p,h in hashes.items():f.write('SHA-256 '+h+'  '+p+'\n')
    print('Frozen 30 page files and combined transcription.')
elif sys.argv[1]=='verify':
    hashes=json.loads((root/'transcription_sha256.json').read_text())
    assert all(digest(root/p)==h for p,h in hashes.items()),'Frozen transcription changed'
    with (root/'progress.log').open('a') as f:f.write('frozen SHA-256 hashes unchanged (all 31 files) '+utc()+'\n')
    s=(root/'SP45_CW_37_transcription.tex').read_text()
    print(json.dumps({'frozen_files_verified':len(hashes),'unsure_marks':len(re.findall(r'\\unsure\{',s)),'illegible_marks':len(re.findall(r'\\illegible\{',s)),'deleted_marks':len(re.findall(r'\\deleted\{',s))}))
else:raise SystemExit('Use freeze or verify')
