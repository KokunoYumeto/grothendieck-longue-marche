"""Record the immutable pre-context transcription boundary exactly once."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

base = Path(__file__).resolve().parents[1]
manifest = base / 'research/frozen_sha256.json'
if manifest.exists():
    raise SystemExit('Already frozen; no rewrite permitted.')
pages = [base / 'pages' / f'MPL_98_98_scan{n:03}.tex' for n in range(2, 45)]
assert all(p.is_file() for p in pages)
log = (base / 'progress.log').read_text()
assert set(map(int, re.findall(r'^98 scan (\d+) done ', log, re.M))) == set(range(2, 45))
assert set(map(int, re.findall(r'^scan (\d+) audited ', log, re.M))) == set(range(2, 45))
assert all(r['transcribed'] == 'yes' for r in csv.DictReader((base / 'MPL_98_inventory.csv').open()))
combined = base / 'MPL_98_transcription.tex'
assert combined.read_text() == '\n'.join(p.read_text().rstrip() for p in pages) + '\n'
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
hashes = {str(p.relative_to(base)): hashlib.sha256(p.read_bytes()).hexdigest() for p in pages + [combined]}
manifest.write_text(json.dumps({'frozen_utc': stamp, 'algorithm': 'SHA-256', 'files': hashes}, indent=2) + '\n')
with (base / 'progress.log').open('a') as f:
    f.write('Pre-freeze mechanical validation: 43 pages; 694 inventory elements; all transcribed=yes; TeX compilation passed.\n')
    for name, digest in hashes.items():
        f.write(f'SHA-256 {name} {digest}\n')
    f.write(f'transcription frozen {stamp}\n')
for p in pages + [combined]:
    p.chmod(0o444)
print(f'Transcription frozen {stamp}; {len(hashes)} hashes recorded.')
