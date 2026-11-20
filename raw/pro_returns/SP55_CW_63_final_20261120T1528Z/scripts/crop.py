"""Non-generative image inspection utility; no recognition of any kind."""
from editorial import *
from PIL import Image, ImageOps, ImageFilter
import argparse
p=argparse.ArgumentParser(); p.add_argument('scan',type=int); p.add_argument('name'); p.add_argument('box',type=int,nargs=4); p.add_argument('--angle',type=float,default=0); p.add_argument('--width',type=int,default=2600); a=p.parse_args()
name=Path(MAP[a.scan]['codex_file']).stem+'.jpg'
im=Image.open(ROOT.parent/'input'/'SP55_CW_63_scans'/name).crop(tuple(a.box))
if a.angle: im=im.rotate(a.angle,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=140,threshold=3))
path=ROOT.parent/'crops'/f'{a.scan:03}_{a.name}.png'; im.save(path)
print(str(path)); print(f'Original-pixel box: {tuple(a.box)}; rotation: {a.angle}')
