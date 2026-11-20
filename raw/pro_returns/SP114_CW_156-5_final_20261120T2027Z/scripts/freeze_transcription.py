"""Freeze or verify the eight fragments and their combined transcription."""
from pathlib import Path
import argparse,hashlib,json
root=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--utc',required=True)
ap.add_argument('--verify',action='store_true')
a=ap.parse_args()
paths=[root/'pages'/f'J156-5-04_156-5_scan{n:03}.tex' for n in range(26,34)]+[root/'SP114_CW_156-5_transcription.tex']
current={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
manifest=root/'review/transcription_frozen_sha256.json'
if a.verify:
 saved=json.loads(manifest.read_text())
 assert current==saved['sha256'],'Frozen transcription has changed'
 line=f'transcription hashes verified unchanged {a.utc}: all eight page files and the combined fragment match the frozen SHA-256 values.\n'
else:
 assert not manifest.exists(),'A freeze already exists; verify it instead'
 for n in range(26,34):
  rec=json.loads((root/'review'/f'scan{n:03}_adjudicated.json').read_text())
  assert rec.get('second_audit_complete'),f'Scan {n} not audited'
 v=json.loads((root/'review/validation.json').read_text());assert v['passed'],'Structural verification failed'
 manifest.write_text(json.dumps({'frozen_utc':a.utc,'sha256':current},indent=2)+'\n')
 line=f'transcription frozen {a.utc}\n'+''.join(f'SHA-256 {h}  {p}\n' for p,h in current.items())
with (root/'progress.log').open('a') as f:f.write(line)
print(line.rstrip())
