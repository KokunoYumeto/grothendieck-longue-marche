"""Package the current edition and its evidence, excluding attached originals."""
from pathlib import Path
from datetime import datetime, timezone
from zipfile import ZipFile, ZIP_DEFLATED
import argparse
import hashlib
import json

ROOT=Path('/workspace/scratch/d12e26a9cd50')
OUT=ROOT/'SP93_C13_151_work'

def main(checkpoint=None):
    delivery=ROOT/'deliverables'; delivery.mkdir(exist_ok=True)
    name=f'SP93_C13_151_checkpoint_{checkpoint:02d}.zip' if checkpoint is not None else 'SP93_C13_151.zip'
    target=delivery/name
    if checkpoint is not None and target.exists(): raise FileExistsError(target)
    if checkpoint is not None:
        with (OUT/'progress.log').open('a') as f:
            f.write(datetime.now(timezone.utc).strftime(f'checkpoint {checkpoint:02d} packaged %Y-%m-%d %H:%M:%S UTC')+'\n')
    paths=sorted(p for p in OUT.rglob('*') if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts)
    with ZipFile(target,'w',ZIP_DEFLATED,compresslevel=6) as z:
        for p in paths: z.write(p,p.relative_to(OUT).as_posix())
    print(json.dumps({'path':str(target),'files':len(paths),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}))

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--checkpoint',type=int)
    main(p.parse_args().checkpoint)
