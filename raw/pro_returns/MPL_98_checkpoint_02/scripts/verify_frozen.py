"""Verify, without rewriting, all 44 frozen transcription files."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys
base = Path(__file__).resolve().parents[1]
manifest = json.loads((base / 'research/frozen_sha256.json').read_text())
bad = []
for name, digest in manifest['files'].items():
    p = base / name
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != digest:
        bad.append(name)
if bad:
    raise SystemExit('Frozen hash mismatch: ' + ', '.join(bad))
msg = f"Frozen SHA-256 verification: all {len(manifest['files'])} files unchanged since {manifest['frozen_utc']}."
if '--log' in sys.argv:
    with (base / 'progress.log').open('a') as f:
        f.write(msg + ' Checked ' + datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC') + '\n')
print(msg)
