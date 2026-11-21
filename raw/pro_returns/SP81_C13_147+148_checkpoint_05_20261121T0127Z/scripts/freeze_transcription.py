"""Freeze the completed, audited page fragments and combined transcription."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'work/manifest.json').read_text())
files = [root / 'pages' / (m['page'] + '.tex') for m in manifest]
files.append(root / 'SP81_C13_147+148_transcription.tex')
hashes = {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
freeze = root / 'work/frozen_hashes.json'
mode = sys.argv[1] if len(sys.argv) > 1 else 'freeze'
if mode == 'freeze':
    assert not freeze.exists(), 'A transcription has already been frozen.'
    assert len(manifest) == 24
    for m in manifest:
        r = json.loads((root / 'work' / (m['page'] + '_final.json')).read_text())
        assert r.get('root_approved') and r.get('audit'), m['page']
    assert (root / 'SP81_C13_147+148_transcription.tex').read_text() == '\n'.join(p.read_text().rstrip()+'\n' for p in files[:-1])
    freeze.write_text(json.dumps({'frozen_at': stamp, 'hashes': hashes}, indent=2)+'\n')
    with (root / 'progress.log').open('a') as f:
        f.write('transcription frozen '+stamp+'\n')
        for name, digest in hashes.items(): f.write('SHA-256 '+digest+' '+name+'\n')
elif mode == 'verify':
    saved = json.loads(freeze.read_text())['hashes']
    assert saved == hashes, 'Frozen transcription has changed.'
    with (root / 'progress.log').open('a') as f:
        f.write('frozen hashes verified unchanged '+stamp+': all 24 page files and combined transcription\n')
else:
    raise SystemExit('Use freeze or verify')
print(json.dumps({'mode': mode, 'files': len(hashes), 'time': stamp}))
