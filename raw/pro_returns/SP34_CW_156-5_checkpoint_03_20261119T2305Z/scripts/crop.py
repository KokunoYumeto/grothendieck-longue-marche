#!/usr/bin/env python3
"""Create a documented image crop; no OCR or recognition is used."""
from PIL import Image
from pathlib import Path
import argparse,json
p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('output');p.add_argument('bbox',nargs=4,type=int);p.add_argument('--rotate',type=float,default=0);p.add_argument('--scale',type=float,default=2);p.add_argument('--manifest');p.add_argument('--scan',type=int);p.add_argument('--reader',default='root');a=p.parse_args()
im=Image.open(a.source).crop(a.bbox)
if a.rotate:im=im.rotate(a.rotate,expand=True,fillcolor='white')
im=im.resize((round(im.width*a.scale),round(im.height*a.scale)),Image.Resampling.LANCZOS)
Path(a.output).parent.mkdir(parents=True,exist_ok=True);im.save(a.output)
if a.manifest:
    with open(a.manifest,'a') as f:f.write(json.dumps({'scan':a.scan,'reader':a.reader,'source':a.source,'file':a.output,'bbox':a.bbox,'rotation':a.rotate,'scale':a.scale})+'\n')
print(a.output)
