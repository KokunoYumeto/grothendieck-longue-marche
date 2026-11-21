#!/usr/bin/env python3
"""Freeze or verify the final transcription bytes without compiling TeX."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys

root = Path(__file__).resolve().parents[1]
mode = sys.argv[1]
state = json.loads((root/'run_state.json').read_text())
expected = [f'pages/147_scan{n:03}.tex' for n in state['scope']]
expected += ['SP78_C13_147_transcription.tex']
manifest = root/'TRANSCRIPTION_SHA256SUMS'
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def digest(name):
    return hashlib.sha256((root/name).read_bytes()).hexdigest()
if mode == 'freeze':
    assert not manifest.exists(), 'Refusing to overwrite a frozen manifest'
    for n in state['scope']:
        r = json.loads((root/'reviewed'/f'147_scan{n:03}.json').read_text())
        assert r.get('root_review_complete') and r.get('audit_complete'), n
    # Match the builder's exact assembly before freezing any hashes.
    pages = sorted((root/'pages').glob('147_scan*.tex'))
    if [f'pages/{p.name}' for p in pages] != expected[:-1]:
        raise SystemExit('Page file coverage/order does not match the freeze scope')
    combined = root/'SP78_C13_147_transcription.tex'
    if not combined.is_file():
        raise SystemExit('Missing combined transcription; rebuild before freezing')
    assembled = '\\cotefile{147}\n\n' + '\n\n'.join(p.read_text().rstrip() for p in pages) + '\n'
    if combined.read_text() != assembled:
        raise SystemExit('Combined transcription does not match page files; rebuild before freezing')
    rows = [(digest(name), name) for name in expected]
    manifest.write_text(''.join(f'{sha}  {name}\n' for sha,name in rows))
    with (root/'progress.log').open('a') as f:
        f.write(f'transcription frozen {now}\n')
        for sha,name in rows:
            f.write(f'SHA-256 {sha} {name}\n')
elif mode == 'verify':
    rows = [line.split('  ',1) for line in manifest.read_text().splitlines()]
    assert [name for sha,name in rows] == expected, 'Manifest coverage/order mismatch'
    for sha,name in rows:
        assert digest(name) == sha, f'Frozen transcription changed: {name}'
    with (root/'progress.log').open('a') as f:
        f.write(f'frozen transcription hashes verified unchanged {now}: {len(rows)} files\n')
else:
    raise SystemExit('Use freeze or verify')
print(json.dumps({'mode':mode,'files':len(rows),'time':now}))
