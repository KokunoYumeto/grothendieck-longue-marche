#!/usr/bin/env python3
"""Freeze or verify the finished diplomatic text without typesetting it."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--verify',action='store_true');a=p.parse_args()
manifest=root/'records/frozen_sha256.json'
def digest(f):return hashlib.sha256(f.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if a.verify:
 data=json.loads(manifest.read_text())
 changed=[name for name,sha in data['files'].items() if digest(root/name)!=sha]
 if changed:raise SystemExit('Frozen transcription changed: '+', '.join(changed))
 with (root/'progress.log').open('a') as f:f.write('frozen transcription hashes unchanged '+now+'; all 8 page files and combined fragment verified\n')
 print('All nine frozen SHA-256 values are unchanged.')
else:
 if manifest.exists():raise SystemExit('The transcription is already frozen; use --verify.')
 pages=[root/'pages'/f'H156-01_156-7_scan{n:03d}.tex' for n in range(2,10)]
 for f in pages:
  if not f.exists():raise SystemExit('Cannot freeze: missing '+str(f))
 files=pages+[root/'SP35_CW_156-7_transcription.tex']
 data={'frozen_utc':now,'files':{str(f.relative_to(root)):digest(f) for f in files}}
 manifest.write_text(json.dumps(data,indent=2)+'\n')
 with (root/'progress.log').open('a') as f:
  f.write('transcription frozen '+now+'\n')
  for name,sha in data['files'].items():f.write('sha256 '+sha+'  '+name+'\n')
 print(json.dumps(data,indent=2))
