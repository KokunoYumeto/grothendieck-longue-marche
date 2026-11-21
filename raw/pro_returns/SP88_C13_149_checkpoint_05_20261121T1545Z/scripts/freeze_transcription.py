"""Freeze or verify the adjudicated transcription and the blind first readings."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys

ROOT = Path(__file__).resolve().parents[1]
mode = sys.argv[1]
record = ROOT/'TRANSCRIPTION_SHA256.json'
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if mode == 'freeze':
    if record.exists():
        raise SystemExit('Already frozen; refusing to replace the freeze record.')
    pages = sorted((ROOT/'pages').glob('149_scan*.tex'))
    if len(pages) != 25:
        raise SystemExit('All 25 page fragments are required.')
    for p in (ROOT/'review/accepted').glob('*.json'):
        if not json.loads(p.read_text()).get('audited'):
            raise SystemExit(f'Independent audit not recorded for {p.name}')
    files = pages + [ROOT/'SP88_C13_149_transcription.tex']
    hashes = {str(p.relative_to(ROOT)):sha(p) for p in files}
    record.write_text(json.dumps(hashes,indent=2)+'\n')
    with (ROOT/'progress.log').open('a') as f:
        f.write('transcription frozen '+now()+'\n')
        for path, digest in hashes.items():
            f.write(f'SHA-256 {digest} {path}\n')
    print(json.dumps({'frozen':len(hashes)}))
elif mode == 'verify':
    hashes=json.loads(record.read_text())
    wrong=[p for p,h in hashes.items() if not (ROOT/p).exists() or sha(ROOT/p)!=h]
    if wrong:
        raise SystemExit('Transcription changed after freeze: '+', '.join(wrong))
    with (ROOT/'progress.log').open('a') as f:
        f.write('transcription hashes verified unchanged '+now()+f': {len(hashes)} files\n')
    print(json.dumps({'verified_unchanged':len(hashes)}))
else:
    raise SystemExit('Use freeze or verify.')
