"""Freeze or verify final transcription bytes, with a UTC audit-log entry."""
from pathlib import Path
import hashlib,json,sys
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[1]
SCANS=list(range(108,118))+list(range(119,132))
paths=[ROOT/'pages'/f'147_scan{s}.tex' for s in SCANS]+[ROOT/'SP80_C13_147_transcription.tex']
record_path=ROOT/'review/frozen_hashes.json'
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
if sys.argv[1]=='freeze':
    assert not record_path.exists(), 'A final transcription is already frozen.'
    record_path.write_text(json.dumps({'frozen_at':now,'sha256':hashes},indent=2)+'\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write('transcription frozen '+now+'\n')
        for name,h in hashes.items():f.write(f'SHA-256 {name} {h}\n')
    print('Frozen 23 page files and combined transcription.')
elif sys.argv[1]=='check':
    expected=json.loads(record_path.read_text())['sha256']
    assert expected==hashes,'Frozen transcription changed.'
    with (ROOT/'progress.log').open('a') as f:
        f.write('frozen SHA-256 hashes rechecked '+now+': all 23 page files and combined transcription unchanged\n')
    print('All frozen hashes unchanged.')
else:raise ValueError('Use freeze or check.')
