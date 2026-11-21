from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from pathlib import Path
import sys

src,name,*args=sys.argv[1:]
box=tuple(map(int,args[:4]))
im=Image.open(src).convert('RGB').crop(box)
if len(args)>4:
    im=im.rotate(float(args[4]),resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
im=ImageOps.autocontrast(im,cutoff=0.4)
im=im.resize((2400,round(im.height*2400/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.3,percent=110,threshold=3))
dest=Path(__file__).resolve().parents[1]/'crops'/name
dest.parent.mkdir(exist_ok=True)
if dest.exists():
    raise SystemExit('Refusing to overwrite existing crop: '+str(dest))
pending=dest.with_name(dest.name+'.pending')
im.save(pending,format='PNG')
pending.replace(dest)
print(dest,box)
