"""Freeze or verify finalized transcription bytes without compiling TeX."""
from pathlib import Path
import datetime
import hashlib
import json
import sys

W = Path(__file__).resolve().parents[1]
PREFIX = 'SP89_C13_149+150'
ORDER = (W / 'scripts' / 'page_order.txt').read_text().split()
RECORD = W / 'reports' / 'frozen_transcription.json'


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def hashes():
    files = [W / 'pages' / (p + '.tex') for p in ORDER]
    files.append(W / (PREFIX + '_transcription.tex'))
    return {str(p.relative_to(W)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}


if '--verify' in sys.argv:
    frozen = json.loads(RECORD.read_text())
    current = hashes()
    if current != frozen['sha256']:
        changed = [p for p in current if current[p] != frozen['sha256'].get(p)]
        raise RuntimeError('Frozen transcription changed: ' + ', '.join(changed))
    stamp = now()
    with (W / 'progress.log').open('a') as f:
        f.write(f'transcription hashes verified unchanged {stamp}: {len(current)} files\n')
    print(f'All {len(current)} transcription hashes are unchanged.')
else:
    if RECORD.exists():
        raise RuntimeError('A freeze record already exists; do not silently refreeze.')
    if len(ORDER) != 25:
        raise RuntimeError('The required 25-page order is incomplete.')
    for page in ORDER:
        r = json.loads((W / 'reports' / page / 'report.json').read_text())
        if not r.get('main_reviewed') or not r.get('audited_utc'):
            raise RuntimeError('Page is not fully adjudicated: ' + page)
    stamp = now()
    values = hashes()
    RECORD.write_text(json.dumps({'frozen_utc': stamp, 'sha256': values}, indent=2) + '\n')
    with (W / 'progress.log').open('a') as f:
        f.write(f'transcription frozen {stamp}\n')
        for name, digest in values.items():
            f.write(f'SHA-256 {digest}  {name}\n')
    print(f'Froze {len(values)} transcription files at {stamp}.')
