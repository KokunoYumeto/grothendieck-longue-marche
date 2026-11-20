"""Freeze or verify the final transcription, only after all sixteen decisions."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
root=Path(__file__).resolve().parents[1]
manifest=root/'records/frozen_transcription_sha256.json'
files=sorted((root/'pages').glob('*.tex'))+[root/'SP51_CW_134-2_transcription.tex']
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
actual={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
log=root/'progress.log'
if sys.argv[1:] == ['verify']:
 if not manifest.exists():raise RuntimeError('No frozen transcription manifest')
 expected=json.loads(manifest.read_text())['sha256']
 if actual!=expected:raise RuntimeError('Frozen transcription hashes changed')
 with log.open('a') as f:f.write(f'transcription hashes unchanged {now}; all 16 page files and combined transcription verified against freeze\n')
 print('All 17 frozen transcription hashes unchanged.')
elif not sys.argv[1:]:
 if manifest.exists():raise FileExistsError('Transcription already frozen; use verify')
 scans=[json.loads(p.read_text())['scan'] for p in sorted((root/'records').glob('scan*/decision.json'))]
 if scans!=list(range(170,186)) or len(files)!=17:raise RuntimeError('All sixteen pages must be decided before freeze')
 if not all(f'scan {n} done ' in log.read_text() for n in scans):raise RuntimeError('Missing page completion log')
 v=json.loads((root/'records/validation.json').read_text())
 if v['issues'] or v['pages']!=16:raise RuntimeError('Final structural validation required')
 manifest.write_text(json.dumps({'frozen_at':now,'sha256':actual},indent=2)+'\n')
 with log.open('a') as f:
  f.write(f'transcription frozen {now}\n')
  for path,digest in actual.items():f.write(f'SHA-256 {digest} {path}\n')
 print('Transcription frozen: all 16 pages and combined fragment.')
else:raise SystemExit('Usage: freeze.py [verify]')
