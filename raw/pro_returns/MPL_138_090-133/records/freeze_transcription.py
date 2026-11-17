"""One-shot freeze, run only by the primary reader after all visual work."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
ROOT=Path(__file__).resolve().parent.parent
PREFIX='MPL_138_090-133'
SCANS=[90,91]+list(range(93,134))
log=ROOT/'progress.log'; old=log.read_text()
assert not re.search(r'^transcription frozen ',old,re.M), 'Already frozen'
assert not re.search(r'^context opened ',old,re.M), 'Context was already opened'
assert sorted(int(n) for n in re.findall(r'^scan (\d+) audited ',old,re.M))==SCANS
assert sorted(int(n) for n in re.findall(r'^138 scan (\d+) done ',old,re.M))==SCANS
pages=[ROOT/'pages'/f'{PREFIX}_138_scan{n:03d}.tex' for n in SCANS]
combined=ROOT/f'{PREFIX}_transcription.tex'
combined.write_text('\n'.join(p.read_text().rstrip()+'\n' for p in pages))
assert combined.read_text().startswith('\\cotefile{138}\n\\scanpage{90}')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in pages+[combined]}
with log.open('a') as f:
 for p,h in hashes.items(): f.write(f'SHA-256 {p} {h}\n')
 f.write(f'transcription frozen {stamp}\n')
(ROOT/'records/frozen_hashes.json').write_text(json.dumps({'time':stamp,'sha256':hashes},indent=2)+'\n')
print(f'Frozen {len(pages)} page files and combined fragment at {stamp}')
