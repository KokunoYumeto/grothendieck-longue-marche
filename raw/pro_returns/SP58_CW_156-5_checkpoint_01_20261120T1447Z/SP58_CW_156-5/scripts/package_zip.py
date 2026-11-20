"""Package all current deliverables, excluding source material and inspection pixels."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,zipfile

OUT=Path(__file__).resolve().parents[1]
PREFIX='SP58_CW_156-5'
parser=argparse.ArgumentParser()
parser.add_argument('--checkpoint',type=int)
args=parser.parse_args()
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
name=f'{PREFIX}_checkpoint_{args.checkpoint:02d}.zip' if args.checkpoint else f'{PREFIX}.zip'
dest=OUT.parent/name
if dest.exists(): raise SystemExit(f'Refusing to overwrite {dest}')
if args.checkpoint:
    with (OUT/'progress.log').open('a') as f:
        f.write(f'checkpoint {args.checkpoint:02d} packaging {stamp}; pages committed through scan 044; first reading continuing; no audits claimed yet\n')
files=sorted(p for p in OUT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix.lower() not in {'.zip','.jpg','.jpeg','.png','.gif','.webp','.tiff','.pdf','.pyc'})
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,Path(PREFIX)/p.relative_to(OUT))
print(str(dest))
print(f'{len(files)} files, {dest.stat().st_size} bytes')
