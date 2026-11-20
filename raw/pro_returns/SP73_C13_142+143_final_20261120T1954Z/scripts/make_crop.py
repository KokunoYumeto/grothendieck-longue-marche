from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import argparse, json
p=argparse.ArgumentParser()
p.add_argument('page');p.add_argument('place');p.add_argument('box',nargs=4,type=int)
p.add_argument('--rotate',type=float,default=0)
a=p.parse_args()
root=Path('/workspace/scratch/615b60ecbb6e')
out=root/'SP73_C13_142+143_work'
target=out/'crops'/f'{a.page}_{a.place}.png'
if target.exists(): raise SystemExit('Crop exists: reuse it; no recropping decided places.')
im=Image.open(root/'source/SP73_C13_142+143_scans'/f'{a.page}.jpg').crop(tuple(a.box))
im=ImageOps.autocontrast(im)
if a.rotate: im=im.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
factor=3000/im.width
im=im.resize((3000,round(im.height*factor)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=115,threshold=3))
im.save(target)
with (out/'state/crop_register.jsonl').open('a') as f:
    f.write(json.dumps({'page':a.page,'file':str(target.relative_to(out)),'box':a.box,'rotation':a.rotate})+'\n')
print(target)
