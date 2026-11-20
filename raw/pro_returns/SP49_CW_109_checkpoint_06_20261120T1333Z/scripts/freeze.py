"""Freeze or recheck the completed transcription after the cross-page notation audit."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,argparse
W=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('mode',choices=['freeze','check']);a=p.parse_args()
state=json.loads((W/'state.json').read_text());order=[int(r['our_scan']) for r in json.loads((W/'page_map.json').read_text())]
assert state['done']==order,'All pages must be committed in order before freezing.'
audit=W/'records/notation_audit.md';assert audit.exists(),'Cross-page notation audit must be documented first.'
records=[json.loads(p.read_text()) for p in sorted((W/'records').glob('scan*.json'))]
paths=[W/'pages'/r['filename'] for r in records]+[W/'SP49_CW_109_transcription.tex']
hashes={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');hp=W/'records/frozen_sha256.json'
if a.mode=='freeze':
 assert not hp.exists(),'Already frozen; do not silently replace frozen hashes.'
 hp.write_text(json.dumps({'frozen_utc':stamp,'files':hashes},indent=2))
 with (W/'progress.log').open('a') as f:
  f.write('transcription frozen '+stamp+'\n')
  for file,digest in hashes.items():f.write('SHA-256 '+digest+'  '+file+'\n')
else:
 expected=json.loads(hp.read_text())['files'];assert hashes==expected,'Frozen transcription changed.'
 with (W/'progress.log').open('a') as f:f.write('frozen hashes checked unchanged '+stamp+'; '+str(len(hashes))+' files\n')
print(a.mode+': '+str(len(hashes))+' transcription files; '+stamp)
