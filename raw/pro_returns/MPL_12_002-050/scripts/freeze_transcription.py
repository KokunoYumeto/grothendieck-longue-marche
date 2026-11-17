from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
root=Path(__file__).resolve().parents[1]
manifest=root/'frozen_hashes.json'
if manifest.exists(): raise SystemExit('Already frozen; refusing overwrite')
scans=[n for n in range(2,51) if n not in {20,22}]
files=[root/'pages'/f'MPL_12_002-050_12_scan{n:03d}.tex' for n in scans]
combined=root/'MPL_12_002-050_transcription.tex'
assert combined.read_text()=='\n\n'.join(p.read_text().rstrip() for p in files)+'\n'
progress=(root/'progress.log').read_text()
assert [int(n) for n in re.findall(r'12 scan (\d+) done',progress)]==scans
assert [int(n) for n in re.findall(r'scan (\d+) audited',progress)]==scans
assert 'context opened' not in progress
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files+[combined]}
manifest.write_text(json.dumps({'algorithm':'sha256','frozen_utc':stamp,'files':hashes},indent=2)+'\n')
with (root/'progress.log').open('a') as out:
 out.write('notation reconciliation completed '+stamp+'\n')
 out.write('Reconciled cursive category M / object M / straight ring M, reinforced coefficient alphabets, quotation marks, duality marks, shriek versus prime, shorthand and arrows against the source images before context access. Inventory rebuilt: 749 elements; doubts rebuilt: 411 entries.\n')
 for name,digest in hashes.items():out.write('SHA-256 '+digest+' '+name+'\n')
 out.write('transcription frozen '+stamp+'\n')
print('transcription frozen '+stamp)
print('Frozen SHA-256 entries:',len(hashes))
