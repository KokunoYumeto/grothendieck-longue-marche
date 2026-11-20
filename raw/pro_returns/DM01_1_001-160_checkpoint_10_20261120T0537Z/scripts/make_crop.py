#!/usr/bin/env python3
"""Crop only (no OCR): source-pixel bounds, optional zoom/contrast/rotation.

Example: python deliverable/scripts/make_crop.py 3 770 135 1310 245 --scale 3
The output is a temporary inspection image and is excluded from packages.
"""
import argparse,json
from pathlib import Path
from PIL import Image,ImageEnhance,ImageOps
ROOT=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser(description=__doc__);p.add_argument('scan',type=int);p.add_argument('box',type=int,nargs=4);p.add_argument('--scale',type=float,default=3);p.add_argument('--contrast',type=float,default=1);p.add_argument('--rotate',type=float,default=0);p.add_argument('--grayscale',action='store_true');p.add_argument('--autocontrast',action='store_true');p.add_argument('--output',type=Path);a=p.parse_args()
source=ROOT/f'source/DM01_1_001-160_scans/1_scan{a.scan:03}.jpg'
with Image.open(source) as image:
 x0,y0,x1,y1=a.box
 if not(0<=x0<x1<=image.width and 0<=y0<y1<=image.height):raise ValueError('Box outside actual source dimensions')
 c=image.crop(a.box)
 if a.grayscale:c=ImageOps.grayscale(c)
 if a.autocontrast:c=ImageOps.autocontrast(c)
 if a.contrast!=1:c=ImageEnhance.Contrast(c).enhance(a.contrast)
 if a.scale!=1:c=c.resize((round(c.width*a.scale),round(c.height*a.scale)),Image.Resampling.LANCZOS)
 if a.rotate:c=c.rotate(a.rotate,expand=True,fillcolor='white')
 output=a.output or ROOT/('work/crops/scan'+f'{a.scan:03}_'+'_'.join(map(str,a.box))+'.png')
 output.parent.mkdir(parents=True,exist_ok=True);c.save(output)
 print(json.dumps({'path':str(output),'box':a.box,'scale':a.scale,'contrast':a.contrast,'rotate':a.rotate,'grayscale':a.grayscale,'autocontrast':a.autocontrast,'note':'Generated; a visual check still requires opening this image.'}))
