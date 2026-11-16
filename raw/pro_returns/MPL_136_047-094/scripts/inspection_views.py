"""Create enlarged contrast views for human inspection only. No OCR.

Usage: python inspection_views.py SCAN [GAIN]
Derived images stay outside the deliverable directory and are not packaged.
"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter
base=Path(__file__).resolve().parents[2]
n=int(sys.argv[1]); gain=float(sys.argv[2]) if len(sys.argv)>2 else 7
im=Image.open(base/'scans'/f'MPL_136_047-094_136_scan{n:03d}.jpg')
out=base/'inspection';out.mkdir(exist_ok=True)
red=im.getchannel('R')
a=np.asarray(red,dtype=float)
b=np.asarray(red.filter(ImageFilter.GaussianBlur(16)),dtype=float)
flat=Image.fromarray(np.clip(246+gain*(a-b),0,255).astype('uint8'))
step=im.height//4
for i in range(4):
    c=flat.crop((0,max(0,i*step-25),im.width,min(im.height,(i+1)*step+35)))
    c.resize((c.width*2,c.height*2)).save(out/f'{n:03d}_strip{i+1}.png')
print('Created four red-channel local-contrast strips for scan',n)
