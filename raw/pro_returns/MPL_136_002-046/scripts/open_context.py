"""Open supplied research context once, only after verified freeze."""
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re
import zipfile

root = Path(__file__).resolve().parents[1]
log = root / 'progress.log'
s = log.read_text()
assert 'transcription frozen' in s
assert 'context opened' not in s
records = re.findall(r'^SHA-256 ([0-9a-f]{64}) (.+)$', s, re.M)
assert len(records) == 45
for digest, name in records:
    assert hashlib.sha256((root/name).read_bytes()).hexdigest() == digest
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log.open('a') as f:
    f.write(f'structural pre-context validation passed {now}; 44 pages, exact combined concatenation, 902 inventory rows; TeX compilation unavailable because installed engines lack format files, no pages read by attempted compilation\n')
    f.write(f'context opened {now}\n')
dest = root.parent / 'context'
dest.mkdir(exist_ok=True)
source = root.parent / 'upload/MPL_136_002-046_context.zip'
with zipfile.ZipFile(source) as z:
    for member in z.infolist():
        target = (dest/member.filename).resolve()
        assert target.is_relative_to(dest.resolve()), member.filename
    z.extractall(dest)
print(f'Context opened after 45 matching frozen hashes at {now}.')
for p in sorted(dest.rglob('*')):
    if p.is_file():
        print(p.relative_to(dest).as_posix())
