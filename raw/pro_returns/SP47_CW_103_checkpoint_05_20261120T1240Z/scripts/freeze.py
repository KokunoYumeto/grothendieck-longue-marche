from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1]
expected=[2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18]
decisions=[json.loads(p.read_text()) for p in sorted((R/'decisions').glob('scan*.json'))]
if [d['scan'] for d in decisions]!=expected:raise SystemExit('Cannot freeze incomplete transcription')
paths=[R/'pages'/d['filename'] for d in decisions]+[R/'SP47_CW_103_transcription.tex']
hashes={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
dest=R/'records/frozen_hashes.json'
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if dest.exists():
    original=json.loads(dest.read_text())
    if original['sha256']!=hashes:raise SystemExit('Frozen transcription hashes CHANGED: stop and investigate')
    with (R/'progress.log').open('a') as f:f.write('frozen hashes unchanged '+now+' (16 page files and combined transcription)\n')
    print('All 17 frozen hashes unchanged.')
else:
    dest.write_text(json.dumps({'frozen_utc':now,'sha256':hashes},indent=2))
    with (R/'progress.log').open('a') as f:
        f.write('transcription frozen '+now+'\n')
        for path,h in hashes.items():f.write(h+'  '+path+'\n')
    print('Transcription frozen with 17 SHA-256 hashes.')
