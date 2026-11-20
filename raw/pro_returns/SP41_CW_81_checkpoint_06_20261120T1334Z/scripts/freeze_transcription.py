"""Perform the user-requested freeze and later byte-for-byte hash verification."""
from pathlib import Path
import json,hashlib,datetime,sys
w=Path(__file__).resolve().parents[1]
scope=[27,28,29,30,*range(32,56)]
records=[json.loads(p.read_text()) for p in sorted((w/'decisions').glob('scan*.json'))]
assert [d['scan'] for d in records]==scope
assert all(d['status']=='decided' for d in records)
log=w/'progress.log';s=log.read_text()
assert all(f'scan {n:03d} done ' in s for n in scope)
paths=[w/'pages'/d['filename'] for d in records]+[w/'SP41_CW_81_transcription.tex']
hashes={str(p.relative_to(w)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
target=w/'validation/frozen_transcription_hashes.json'
mode=sys.argv[1]
if mode=='freeze':
 assert 'transcription frozen ' not in s,'Do not create a second freeze record.'
 assert (w/'validation/notation_audit_final.json').exists(),'Complete the cross-page ink comparison first.'
 assert (w/'validation/legibility_note.md').exists(),'Complete the final legibility assessment first.'
 target.write_text(json.dumps({'frozen_utc':now,'sha256':hashes},indent=2))
 with log.open('a') as f:
  f.write('transcription frozen '+now+'\n')
  for name,digest in hashes.items():f.write('SHA-256 '+name+' '+digest+'\n')
 print('Frozen',len(hashes),'transcription files at',now)
elif mode=='verify':
 frozen=json.loads(target.read_text());assert frozen['sha256']==hashes,'A frozen transcription file changed.'
 with log.open('a') as f:f.write('frozen transcription hashes unchanged '+now+'; all '+str(len(hashes))+' page/combined file hashes match.\n')
 print('All',len(hashes),'frozen transcription hashes are unchanged.')
else:raise ValueError('Use freeze or verify.')
