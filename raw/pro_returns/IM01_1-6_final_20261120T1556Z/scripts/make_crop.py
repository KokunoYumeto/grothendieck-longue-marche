#!/usr/bin/env python3
"""Reproduce a crop from the recorded original coordinates; no OCR."""
import argparse
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('destination')
p.add_argument('box',nargs=4,type=int)
p.add_argument('--width',type=int,default=2800)
p.add_argument('--contrast',type=float,default=1.5)
p.add_argument('--rotate',type=float,default=0)
p.add_argument('--contrast-after-resize',action='store_true')
a=p.parse_args()
im=Image.open(a.source).crop(tuple(a.box))
if a.rotate: im=im.rotate(a.rotate,expand=True)
if not a.contrast_after_resize: im=ImageEnhance.Contrast(im).enhance(a.contrast)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
if a.contrast_after_resize: im=ImageEnhance.Contrast(im).enhance(a.contrast)
Path(a.destination).parent.mkdir(parents=True,exist_ok=True)
im.save(a.destination,quality=95)
