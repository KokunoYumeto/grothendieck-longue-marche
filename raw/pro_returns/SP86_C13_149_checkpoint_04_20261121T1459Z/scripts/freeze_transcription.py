"""Freeze the completed transcription, or verify its unchanged bytes at delivery."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys
import validate

BASE = Path(__file__).resolve().parents[1]
MANIFEST = BASE / 'transcription_sha256.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(verify=False):
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    if verify:
        record = json.loads(MANIFEST.read_text())
        failed = [name for name, digest in record['files'].items() if sha(BASE / name) != digest]
        assert not failed, f'Frozen transcription changed: {failed}'
        with (BASE / 'progress.log').open('a') as log:
            log.write(f'transcription hashes verified unchanged {stamp}: all 23 page files and combined transcription match the frozen SHA-256 values\n')
        print(json.dumps({'verified_utc': stamp, 'files': len(record['files']), 'unchanged': True}))
        return
    assert not MANIFEST.exists(), 'Transcription already frozen'
    assert not validate.validate(final=True)['errors']
    paths = sorted((BASE / 'pages').glob('149_scan*.tex'))
    assert len(paths) == 23
    paths.append(BASE / 'SP86_C13_149_transcription.tex')
    record = {'frozen_utc': stamp, 'files': {str(path.relative_to(BASE)): sha(path) for path in paths}}
    MANIFEST.write_text(json.dumps(record, indent=2) + '\n')
    with (BASE / 'progress.log').open('a') as log:
        log.write(f'transcription frozen {stamp}\n')
        for name, digest in record['files'].items():
            log.write(f'SHA-256 {digest} {name}\n')
    print(json.dumps({'frozen_utc': stamp, 'files': len(paths)}))

if __name__ == '__main__':
    run('--verify' in sys.argv)
