"""Freeze, or verify, the completed diplomatic text without changing it."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json

OUT = Path(__file__).resolve().parents[1]
NAME = 'SP57_CW_97+123+162-1+162-6'
parser = argparse.ArgumentParser()
parser.add_argument('--verify', action='store_true')
args = parser.parse_args()
order = json.loads((OUT / 'page_order.json').read_text())
paths = [OUT / 'pages' / (m['stem'] + '.tex') for m in order]
paths.append(OUT / (NAME + '_transcription.tex'))
assert all(p.exists() for p in paths), 'Every page must be decided before freezing'
hashes = {str(p.relative_to(OUT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
frozen = OUT / 'frozen_transcription_sha256.json'
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if args.verify:
    assert frozen.exists(), 'No frozen manifest'
    assert hashes == json.loads(frozen.read_text())['sha256'], 'Frozen text changed'
    message = 'frozen transcription hashes unchanged ' + now
else:
    assert not frozen.exists(), 'A frozen manifest already exists'
    frozen.write_text(json.dumps({'frozen_utc': now, 'sha256': hashes}, indent=2) + '\n')
    message = 'transcription frozen ' + now
with (OUT / 'progress.log').open('a') as log:
    log.write(message + '\n')
    if not args.verify:
        for name, digest in hashes.items():
            log.write('SHA-256 ' + digest + ' ' + name + '\n')
print(json.dumps({'message': message, 'files': len(hashes)}))
