"""Make one documented tight image crop; no OCR or text recognition."""
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import argparse, json
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('dest');p.add_argument('box',nargs=4,type=int)
p.add_argument('--width',type=int,default=2600);p.add_argument('--rotate',type=float,default=0)
p.add_argument('--sharpen',action='store_true')
a=p.parse_args()
im=Image.open(a.source).crop(tuple(a.box))
if a.rotate:im=im.rotate(a.rotate,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
if a.sharpen:im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=130,threshold=3))
Path(a.dest).parent.mkdir(parents=True,exist_ok=True)
im.save(a.dest,quality=94)
print(json.dumps({'source':a.source,'path':a.dest,'box':a.box,'rotate':a.rotate,'width':a.width,'sharpen':a.sharpen,'size':im.size}))
