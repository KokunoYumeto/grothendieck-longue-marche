#!/usr/bin/env python3
"""Freeze the visually audited fragments; later calls verify, never rewrite them."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, sys

root = Path(__file__).resolve().parents[1]
manifest = root/'records/frozen_hashes.json'
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
if '--verify' in sys.argv:
    hashes = json.loads(manifest.read_text())['sha256']
    bad = [name for name, value in hashes.items() if digest(root/name) != value]
    if bad:
        raise SystemExit('Frozen-file mismatch: ' + ', '.join(bad))
    with (root/'progress.log').open('a') as log:
        log.write(f'frozen hashes verified unchanged: {len(hashes)} files {stamp}\n')
    print(f'All {len(hashes)} frozen SHA-256 values are unchanged.')
    raise SystemExit(0)
if manifest.exists():
    raise SystemExit('Already frozen; use --verify.')
log = (root/'progress.log').read_text()
assert 'context opened ' not in log
pages = sorted((root/'pages').glob('*.tex'))
assert len(pages) == 38
assert {int(re.search(r'scan(\d+)',p.name)[1]) for p in pages} == set(range(2,40))
assert {int(n) for n in re.findall(r'^scan (\d+) audited ',log,re.M)} == set(range(2,40))
combined = root/'MPL_64_002-039_transcription.tex'
assert combined.read_text() == ''.join(p.read_text()+'\n' for p in pages)
assert combined.read_text().startswith('\\cotefile{64}\n\\scanpage{2}\n')
assert (root/'MPL_64_002-039_doubts.md').stat().st_size > 5000
hashes = {p.relative_to(root).as_posix():digest(p) for p in pages+[combined]}
manifest.write_text(json.dumps({'frozen_utc':stamp,'sha256':hashes},indent=2)+'\n')
with (root/'progress.log').open('a') as out:
    for name,value in hashes.items():
        out.write(f'sha256 {value} {name}\n')
    out.write(f'transcription frozen {stamp}\n')
print(f'Frozen {len(hashes)} files at {stamp}')
