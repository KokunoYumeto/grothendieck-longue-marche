"""Analytical image crop only. No OCR or recognition. Coordinates are manually chosen."""
import argparse, json
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from datetime import datetime, timezone
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('dest')
p.add_argument('box',nargs=4,type=int)
p.add_argument('--rotate',type=float,default=0)
p.add_argument('--width',type=int,default=2600)
a=p.parse_args()
im=Image.open(a.source).crop(tuple(a.box))
if a.rotate: im=im.rotate(a.rotate,expand=True,fillcolor='white',resample=Image.Resampling.BICUBIC)
im=ImageOps.autocontrast(im,cutoff=0.4)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
dest=Path(a.dest);dest.parent.mkdir(parents=True,exist_ok=True);im.save(dest)
entry=dict(source=Path(a.source).name,dest=dest.name,box=a.box,rotate=a.rotate,width=a.width,time=datetime.now(timezone.utc).isoformat())
with (dest.parent/'crop_manifest.jsonl').open('a') as f: f.write(json.dumps(entry)+'\n')
print(json.dumps(entry))
