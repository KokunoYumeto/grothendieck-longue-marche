#!/usr/bin/env python3
"""Write a complete deliverable ZIP, excluding source images and temporary caches."""
from pathlib import Path
import sys,zipfile
ROOT=Path(__file__).resolve().parents[1]
if len(sys.argv)!=2:raise SystemExit('Usage: package.py /absolute/output.zip')
target=Path(sys.argv[1])
if not target.is_absolute() or target.suffix.lower()!='.zip':raise SystemExit('Absolute ZIP destination required.')
if target.exists():raise SystemExit('Refusing to overwrite an existing ZIP.')
forbidden={'.jpg','.jpeg','.png','.gif','.webp','.tif','.tiff','.bmp','.pdf','.zip','.pyc'}
files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and '__pycache__' not in p.parts]
for p in files:
    if p.suffix.lower() in forbidden:raise SystemExit('Forbidden file in deliverable tree: '+str(p))
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,str(p.relative_to(ROOT)))
print(str(target));print(str(len(files))+' files, '+str(target.stat().st_size)+' bytes')
