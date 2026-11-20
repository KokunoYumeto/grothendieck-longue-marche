#!/usr/bin/env python3
"""Make a single documented tight inspection crop; never recognize text."""
import argparse,json
from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('output');p.add_argument('box',nargs=4,type=int)
p.add_argument('--width',type=int,default=2600);p.add_argument('--rotate',type=float,default=0)
p.add_argument('--locus',required=True);a=p.parse_args()
src=Path(a.source);out=Path(a.output);assert not out.exists(),out
im=Image.open(src).crop(tuple(a.box))
if a.rotate:im=im.rotate(a.rotate,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.0,percent=120,threshold=3))
out.parent.mkdir(parents=True,exist_ok=True)
im.save(out,quality=96,subsampling=0)
meta={'source':str(src),'output':str(out),'bbox':a.box,'locus':a.locus,'width':a.width,'rotate':a.rotate,'transforms':'PIL autocontrast; LANCZOS; UnsharpMask radius=1 percent=120 threshold=3; JPEG quality=96 when .jpg'}
out.with_suffix(out.suffix+'.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta))
