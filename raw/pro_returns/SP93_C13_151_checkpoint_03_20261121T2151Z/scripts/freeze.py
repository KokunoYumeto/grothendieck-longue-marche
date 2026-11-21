"""Freeze and verify the exact transcription bytes after all image decisions."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json
OUT=Path('/workspace/scratch/d12e26a9cd50/SP93_C13_151_work')
p=argparse.ArgumentParser();p.add_argument('--verify',action='store_true');a=p.parse_args()
files=sorted((OUT/'pages').glob('151_scan*.tex'))+[OUT/'SP93_C13_151_transcription.tex']
actual={str(p.relative_to(OUT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest=OUT/'transcription_hashes.sha256'
if a.verify:
    expected={line.split('  ',1)[1]:line.split('  ',1)[0] for line in manifest.read_text().splitlines()}
    if expected!=actual:raise RuntimeError('Frozen transcription hashes changed')
    with (OUT/'progress.log').open('a') as f:f.write(f'transcription hashes verified unchanged {stamp}: {len(actual)} files\n')
    print(json.dumps({'verified_unchanged':len(actual)}))
else:
    if manifest.exists():raise FileExistsError('Transcription has already been frozen')
    lines=[f'{v}  {k}' for k,v in actual.items()]
    manifest.write_text('\n'.join(lines)+'\n')
    with (OUT/'progress.log').open('a') as f:
        f.write(f'transcription frozen {stamp}\n')
        for line in lines:f.write('SHA256 '+line+'\n')
    print(json.dumps({'frozen_files':len(actual)}))
