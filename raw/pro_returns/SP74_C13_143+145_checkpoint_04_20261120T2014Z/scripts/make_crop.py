#!/usr/bin/env python3
"""Create one evidence crop; refuses to overwrite an existing crop."""
from pathlib import Path
import sys,json
from PIL import Image,ImageOps,ImageEnhance
ROOT=Path(__file__).resolve().parents[1]
key,name=sys.argv[1:3];box=tuple(map(int,sys.argv[3:7]));rotation=float(sys.argv[7]) if len(sys.argv)>7 else 0
source=ROOT.parent/'source'/'SP74_C13_143+145_scans'/f'{key}.jpg'
dest=ROOT/'crops'/f'{key}_main_{name}.png'
if dest.exists():raise FileExistsError(dest)
im=Image.open(source).crop(box)
im=ImageOps.autocontrast(im)
if rotation:im=im.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
im=im.resize((2800,max(1,round(im.height*2800/im.width))),Image.Resampling.LANCZOS)
im.save(dest)
record={'page':key,'crop':str(dest.relative_to(ROOT)),'box':box,'rotation_degrees':rotation,'reader':'main'}
with (ROOT/'main_crop_manifest.jsonl').open('a') as f:f.write(json.dumps(record)+'\n')
print(json.dumps(record))
