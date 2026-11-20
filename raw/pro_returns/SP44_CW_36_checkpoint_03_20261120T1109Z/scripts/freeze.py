from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,subprocess
O=Path(__file__).resolve().parents[1]
mode=sys.argv[1] if len(sys.argv)>1 else 'freeze'
manifest=O/'validation/frozen_sha256.json'
if mode=='freeze':
    if manifest.exists():raise SystemExit('Transcription already frozen')
    subprocess.run([sys.executable,str(O/'scripts/validate.py'),'--complete'],check=True)
    paths=sorted((O/'pages').glob('*.tex'))+[O/'SP44_CW_36_transcription.tex']
    hashes={str(p.relative_to(O)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    manifest.write_text(json.dumps(hashes,indent=2)+'\n')
    with (O/'progress.log').open('a') as f:
        f.write('transcription frozen '+datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')+'\n')
        for name,h in hashes.items():f.write('SHA-256 '+h+'  '+name+'\n')
    print('Frozen',len(hashes),'files')
elif mode=='verify':
    hashes=json.loads(manifest.read_text())
    expected={f'pages/{"A36-01" if n<=18 else "A36-02"}_36_scan{n:03d}.tex' for n in range(10,28)}|{'SP44_CW_36_transcription.tex'}
    actual={str(p.relative_to(O)) for p in (O/'pages').glob('*.tex')}|{'SP44_CW_36_transcription.tex'}
    if set(hashes)!=expected or actual!=expected:raise SystemExit('Frozen/current transcription file set differs from the required 18 pages and combined file')
    changed=[name for name,h in hashes.items() if hashlib.sha256((O/name).read_bytes()).hexdigest()!=h]
    if changed:raise SystemExit('Frozen transcription changed: '+str(changed))
    with (O/'progress.log').open('a') as f:f.write('frozen hashes unchanged '+datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')+'; '+str(len(hashes))+' files verified\n')
    print('All frozen hashes unchanged:',len(hashes))
else:raise SystemExit('Unknown mode')
