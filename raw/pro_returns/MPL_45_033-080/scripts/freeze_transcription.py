from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
log = root / 'progress.log'
old = log.read_text()
assert 'transcription frozen ' not in old
assert 'context opened ' not in old
expected = [33,34,35,36,37,38,39,40,41,42,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,66,67,68,69,70,71,76,77,78,79]
pages = [root / f'pages/MPL_45_033-080_45_scan{n:03}.tex' for n in expected]
for n in expected:
    assert len(re.findall(rf'^45 scan {n:03} done ', old, re.M)) == 1
    assert len(re.findall(rf'^scan {n:03} audited ', old, re.M)) == 1
combined = root / 'MPL_45_033-080_transcription.tex'
assert combined.read_text() == '\n'.join(p.read_text().rstrip() for p in pages) + '\n'
hashes = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in pages + [combined]}
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest = {'frozen_at': stamp, 'hashes': hashes}
(root / 'scripts/frozen_hashes.json').write_text(json.dumps(manifest, indent=2) + '\n')
with log.open('a') as f:
    for name, digest in hashes.items():
        f.write(f'SHA-256 {digest}  {name}\n')
    f.write('transcription frozen ' + stamp + '\n')
print('transcription frozen', stamp, len(hashes), 'hashes')
