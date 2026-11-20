#!/usr/bin/env python3
"""Crop and enlarge a scan for direct visual inspection; never OCR."""
import argparse, csv, datetime, fcntl
from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

p=argparse.ArgumentParser()
p.add_argument('page')
p.add_argument('name')
p.add_argument('box',type=int,nargs=4,metavar=('LEFT','TOP','RIGHT','BOTTOM'))
p.add_argument('--width',type=int,default=2600)
p.add_argument('--contrast',type=float,default=1.25)
a=p.parse_args()
w=Path(__file__).resolve().parents[1]
source=w/'source/IM03_9-12_scans'/f'{a.page}.jpg'
im=Image.open(source)
left,top,right,bottom=a.box
assert 0<=left<right<=im.width and 0<=top<bottom<=im.height,(a.box,im.size)
crop=im.crop(a.box)
crop=ImageEnhance.Contrast(crop).enhance(a.contrast)
crop=crop.resize((a.width,round(crop.height*a.width/crop.width)),Image.Resampling.LANCZOS)
out=w/'crops'/f'{a.page}_{a.name}.jpg'
assert not out.exists(),f'Refusing to overwrite existing crop {out}'
crop.save(out,quality=95)
manifest=w/'crops/manifest.tsv'
with manifest.open('a+',newline='') as f:
    fcntl.flock(f,fcntl.LOCK_EX)
    f.seek(0,2)
    wr=csv.writer(f,delimiter='\t')
    if f.tell()==0: wr.writerow(['crop','source','left','top','right','bottom','output_width','output_height','contrast','utc'])
    wr.writerow([str(out.relative_to(w)),str(source.relative_to(w)),*a.box,*crop.size,a.contrast,datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')])
    f.flush()
print(out)
