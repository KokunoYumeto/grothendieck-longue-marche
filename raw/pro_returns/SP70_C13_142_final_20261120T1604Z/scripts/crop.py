from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import sys
root=Path(__file__).resolve().parents[2]
n=int(sys.argv[1]);label=sys.argv[2];box=tuple(map(int,sys.argv[3:7]));angle=float(sys.argv[7]) if len(sys.argv)>7 else 0
out=root/f'views/{n:03}_{label}.png'
if out.exists():raise SystemExit('Crop already exists; do not recrop a decided place')
im=Image.open(root/f'source/SP70_C13_142_scans/142_scan{n:03}.jpg').crop(box)
if angle:im=im.rotate(angle,expand=True,fillcolor='white',resample=Image.Resampling.BICUBIC)
im=ImageOps.autocontrast(im)
factor=min(2800/im.width,4000/im.height)
im=im.resize((round(im.width*factor),round(im.height*factor)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.4,percent=110,threshold=3));im.save(out)
print(f'{n:03} {box} rotation {angle}: {out}')
