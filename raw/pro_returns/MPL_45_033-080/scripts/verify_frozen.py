from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'scripts/frozen_hashes.json').read_text())
changed = []
for name, digest in manifest['hashes'].items():
    p = root / name
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != digest:
        changed.append(name)
assert not changed, changed
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
message = f'transcription hashes verified unchanged {stamp}: all {len(manifest["hashes"])} SHA-256 values match the pre-context freeze.\n'
with (root / 'progress.log').open('a') as f:
    f.write(message)
print(message.strip())
