"""Freeze/verify exact transcription bytes after every independent audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys

W = Path(__file__).resolve().parents[1]
order = (W/'page_order.txt').read_text().splitlines()
paths = ['pages/'+p+'.tex' for p in order]+['SP76_C13_145+147_transcription.tex']
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
actual = {p:hashlib.sha256((W/p).read_bytes()).hexdigest() for p in paths}
manifest = W/'reports/frozen_hashes.json'
if sys.argv[1]=='freeze':
    if manifest.exists(): raise SystemExit('Already frozen; do not overwrite.')
    if any(not json.loads((W/'reports'/f'{p}.json').read_text()).get('audited') for p in order):
        raise SystemExit('Every page must be audited first.')
    manifest.write_text(json.dumps(actual,indent=2)+'\n')
    with (W/'progress.log').open('a') as f:
        f.write('transcription frozen '+now+'\n')
        for p,h in actual.items(): f.write('SHA-256 '+h+' '+p+'\n')
elif sys.argv[1]=='verify':
    expected=json.loads(manifest.read_text())
    if actual!=expected: raise SystemExit('Frozen transcription hashes changed.')
    with (W/'progress.log').open('a') as f:
        f.write('transcription hashes verified unchanged '+now+': 24 page files and combined transcription\n')
else: raise SystemExit('Use freeze or verify.')
print(sys.argv[1],len(actual),'SHA-256 values')
