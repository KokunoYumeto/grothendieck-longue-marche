from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import argparse
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('dest');p.add_argument('x0',type=int);p.add_argument('y0',type=int);p.add_argument('x1',type=int);p.add_argument('y1',type=int);p.add_argument('--width',type=int,default=2600);p.add_argument('--rotate',type=float,default=0);a=p.parse_args()
im=Image.open(a.source).crop((a.x0,a.y0,a.x1,a.y1))
im=ImageOps.autocontrast(im)
if a.rotate: im=im.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.0,percent=110,threshold=3))
im.save(a.dest)
