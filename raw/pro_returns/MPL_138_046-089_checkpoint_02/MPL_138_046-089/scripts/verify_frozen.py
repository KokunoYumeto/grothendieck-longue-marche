from pathlib import Path
from datetime import datetime, timezone
import hashlib
ROOT=Path(__file__).resolve().parents[1]
rows=(ROOT/'SHA256SUMS').read_text().splitlines()
assert len(rows)==43
for row in rows:
    expected,name=row.split('  ',1)
    actual=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    assert actual==expected, name
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:f.write('frozen hashes unchanged: 42 pages and combined transcription '+stamp+'\n')
print('All 43 frozen hashes unchanged;',stamp)
