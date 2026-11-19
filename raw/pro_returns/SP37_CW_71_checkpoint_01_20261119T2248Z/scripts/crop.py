#!/usr/bin/env python3
"""Create one documented visual crop; no OCR or text recognition."""
from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
from datetime import datetime, timezone
import argparse, json
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('destination')
p.add_argument('box',nargs=4,type=int)
p.add_argument('--rotate',type=float,default=0)
p.add_argument('--width',type=int,default=2800)
a=p.parse_args()
im=Image.open(a.source).crop(tuple(a.box))
if a.rotate: im=im.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.0,percent=120,threshold=3))
d=Path(a.destination);d.parent.mkdir(parents=True,exist_ok=True);im.save(d)
meta={'source':a.source,'destination':str(d),'box':a.box,'rotation':a.rotate,'width':a.width,'created_utc':datetime.now(timezone.utc).isoformat()}
d.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta))
