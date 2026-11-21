from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import argparse
p=argparse.ArgumentParser()
p.add_argument('page');p.add_argument('place');p.add_argument('box',nargs=4,type=int)
p.add_argument('--rotate',type=float,default=0)
p.add_argument('--width',type=int,default=2400)
p.add_argument('--second',action='store_true')
a=p.parse_args()
root=Path(__file__).resolve().parents[2]
im=Image.open(root/'source/SP92_C13_150+151_scans'/f'{a.page}.jpg')
im=im.crop(tuple(a.box))
if a.rotate:im=im.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((a.width,round(im.height*a.width/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
name=f'{a.page}_{"second_" if a.second else ""}{a.place}.png'
out=root/'SP92_C13_150+151_work/crops'/name
if out.exists():raise SystemExit(f'Crop already exists: {out}; inspect that crop rather than recropping.')
im.save(out)
print(str(out))
