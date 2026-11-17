"""Deterministic colour/contrast crops for visual reading only. No OCR."""
from pathlib import Path
import sys
import numpy as np
from PIL import Image, ImageFilter
scan=int(sys.argv[1]); base=Path('/workspace/scratch/25412ac386a9')
im=Image.open(base/f'scans/MPL_137_002-044_137_scan{scan:03}.jpg').convert('RGB')
a=np.array(im.filter(ImageFilter.GaussianBlur(.6)),dtype=float)
r=a[:,:,0]
bg=np.asarray(Image.fromarray(r.astype('uint8')).filter(ImageFilter.GaussianBlur(18)),dtype=float)
diff=bg-r
# Blue ink is suppressed in red; preserve strokes with a fixed monotone contrast.
x=np.clip(240-12*diff,0,255).astype('uint8')
folder=base/'reading';folder.mkdir(exist_ok=True)
for k,y in enumerate(range(0,im.height,550)):
    Image.fromarray(x).crop((0,max(0,y-40),im.width,min(im.height,y+610))).save(folder/f'{scan:03}_{k}.png')
print(f'Created visual contrast crops for scan {scan:03}; no text extraction.')
