"""One documented crop per unresolved place; no text recognition."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import argparse
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('destination');p.add_argument('box',nargs=4,type=int);p.add_argument('--angle',type=float,default=0);a=p.parse_args()
im=Image.open(a.source).crop(tuple(a.box))
if a.angle:im=im.rotate(a.angle,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((2400,round(im.height*2400/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
Path(a.destination).parent.mkdir(parents=True,exist_ok=True);im.save(a.destination)
print(a.source,tuple(a.box),'rotation',a.angle,'=>',a.destination)
