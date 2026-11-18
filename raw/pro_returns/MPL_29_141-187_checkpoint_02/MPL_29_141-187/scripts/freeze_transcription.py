#!/usr/bin/env python3
"""Freeze the already audited transcription; never reads sources or context."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import re

root = Path(__file__).resolve().parents[1]
prefix = 'MPL_29_141-187'
log = root / 'progress.log'
history = log.read_text()
assert 'transcription frozen' not in history, 'Already frozen'
assert 'context opened' not in history, 'Context was already opened'
expected = list(range(141, 188))
done = [int(n) for n in re.findall(r'^29 scan (\d+) done ', history, re.M)]
audited = [int(n) for n in re.findall(r'^scan (\d+) audited ', history, re.M)]
assert done == expected, 'Missing, duplicate, or out-of-order first-pass record'
assert audited == expected, 'Missing, duplicate, or out-of-order visual audit'
pages = [root / 'pages' / f'{prefix}_29_scan{n:03d}.tex' for n in expected]
combined = root / f'{prefix}_transcription.tex'
assert combined.read_text() == '\n'.join(p.read_text().rstrip() for p in pages) + '\n'
assert len(re.findall(r'\\cotefile\{29\}', combined.read_text())) == 1
entries = []
for path in pages + [combined]:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    entries.append(f'sha256 {digest} {path.relative_to(root).as_posix()}')
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log.open('a') as stream:
    stream.write('\n'.join(entries) + '\n')
    stream.write('transcription frozen ' + stamp + '\n')
print(f'Frozen {len(entries)} files at {stamp}')
