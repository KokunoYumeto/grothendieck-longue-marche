"""Make user-requested visual crops; never OCR; images stay outside deliverables."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import argparse
p=argparse.ArgumentParser();p.add_argument('scan',type=int);p.add_argument('label');p.add_argument('box',nargs=4,type=int);p.add_argument('--rotate',type=float,default=0);p.add_argument('--mirror',action='store_true');a=p.parse_args()
root=Path(__file__).resolve().parents[2]
f=next((root/'source/SP59_CW_71_scans').glob(f'*_scan{a.scan:03d}.jpg'))
im=Image.open(f).crop(a.box)
if a.mirror:im=ImageOps.mirror(im)
if a.rotate:im=im.rotate(a.rotate,expand=True,fillcolor='white')
im=ImageOps.autocontrast(im)
im=im.resize((2400,round(im.height*2400/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.5,percent=130,threshold=3))
out=root/'crops'/f'{a.scan:03d}_{a.label}.jpg';out.parent.mkdir(exist_ok=True);im.save(out,quality=95)
log=root/'output'/'crop_register.tsv'
if not log.exists():log.write_text('scan\tlabel\tx0\ty0\tx1\ty1\trotation\n')
with log.open('a') as stream:stream.write('\t'.join(map(str,[a.scan,a.label,*a.box,a.rotate]))+'\n')
print(str(out))
