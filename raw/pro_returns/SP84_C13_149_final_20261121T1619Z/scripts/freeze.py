"""Freeze and recheck the finished transcription, without compiling TeX."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'documentation/frozen_sha256.json'


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def hashes():
    pages = sorted((ROOT / 'pages').glob('149_scan*.tex'))
    assert [p.stem for p in pages] == [f'149_scan{n:03d}' for n in range(5,28)]
    files = pages + [ROOT / 'SP84_C13_149_transcription.tex']
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in files}


def freeze():
    assert not MANIFEST.exists(), 'A freeze already exists; investigate before replacing it.'
    for n in range(5,28):
        r = json.loads((ROOT / f'reviews/149_scan{n:03d}.json').read_text())
        assert r.get('root_approved') and r.get('audited'), n
    h = hashes()
    now = utc()
    MANIFEST.write_text(json.dumps({'frozen_utc': now, 'sha256': h}, indent=2)+'\n')
    with (ROOT / 'progress.log').open('a') as stream:
        stream.write(f'transcription frozen {now}\n')
        for name, digest in h.items():
            stream.write(f'SHA-256 {digest}  {name}\n')
    print(json.dumps({'frozen_utc': now, 'files': len(h)}))


def verify():
    expected = json.loads(MANIFEST.read_text())['sha256']
    actual = hashes()
    assert actual == expected, 'Frozen transcription changed; do not package as verified.'
    now = utc()
    with (ROOT / 'progress.log').open('a') as stream:
        stream.write(f'frozen transcription verified unchanged {now}: '
                     f'all {len(actual)} SHA-256 hashes match the freeze.\n')
    print(json.dumps({'verified_utc': now, 'files': len(actual), 'unchanged': True}))


if __name__ == '__main__':
    {'freeze': freeze, 'verify': verify}[sys.argv[1]]()
