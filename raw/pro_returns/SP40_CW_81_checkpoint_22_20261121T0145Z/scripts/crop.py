"""One tight crop, enlarged for human visual reading; no recognition."""
from PIL import Image, ImageOps, ImageFilter
import argparse, json
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('dest');p.add_argument('bbox',nargs=4,type=int)
p.add_argument('--rotate',type=float,default=0);p.add_argument('--width',type=int,default=2600)
a=p.parse_args()
im=Image.open(a.source).crop(tuple(a.bbox))
if a.rotate:im=im.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
Path(a.dest).parent.mkdir(parents=True,exist_ok=True)
im.save(a.dest)
print(json.dumps({'source':a.source,'crop':a.dest,'bbox':a.bbox,'rotation':a.rotate,'size':im.size}))
