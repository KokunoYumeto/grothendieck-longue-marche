"""Requested visual crops only; no OCR or image recognition."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import argparse, json
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('destination');p.add_argument('box',nargs=4,type=int)
p.add_argument('--rotate',type=float,default=0);p.add_argument('--width',type=int,default=2800)
a=p.parse_args()
im=Image.open(a.source).crop(tuple(a.box))
if a.rotate: im=im.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=130,threshold=3))
dest=Path(a.destination);dest.parent.mkdir(parents=True,exist_ok=True);im.save(dest)
dest.with_suffix('.json').write_text(json.dumps({'source':a.source,'box':a.box,'rotation':a.rotate,'width':a.width,'no_ocr':True},indent=2)+'\n')
print(dest)
