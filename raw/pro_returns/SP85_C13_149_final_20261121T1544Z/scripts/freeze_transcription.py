"""Freeze or verify the final fragment without compiling or interpreting TeX."""
from pathlib import Path
import hashlib, json, datetime, sys

root = Path(__file__).resolve().parents[1]
record = root/'records/transcription_freeze.json'
mode = sys.argv[1] if len(sys.argv)>1 else 'verify'
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
files = sorted((root/'pages').glob('*.tex')) + [root/'SP85_C13_149_transcription.tex']
actual = {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
if mode=='freeze':
    assert not record.exists(), 'Transcription already frozen'
    records = [json.loads(p.read_text()) for p in (root/'records').glob('149_scan*.json')]
    assert len(records)==23 and len(files)==24
    assert all(p.get('main_reviewed') and p.get('audited') for p in records)
    record.write_text(json.dumps({'frozen_utc':now,'sha256':actual},indent=2)+'\n')
    with (root/'progress.log').open('a') as f:
        f.write('transcription frozen '+now+'\n')
        for name,digest in actual.items():f.write('SHA-256 '+digest+'  '+name+'\n')
    print('Frozen 23 pages and combined fragment')
elif mode=='verify':
    expected = json.loads(record.read_text())['sha256']
    assert actual==expected, 'Frozen transcription hashes changed'
    with (root/'progress.log').open('a') as f:
        f.write('transcription hashes verified unchanged '+now+': all 23 pages and combined fragment\n')
    print('All 24 transcription hashes unchanged')
else:
    raise SystemExit('Use freeze or verify')
