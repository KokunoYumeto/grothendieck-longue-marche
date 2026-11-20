"""Pillow-only geometric views; no OCR or text-recognition calls."""
from pathlib import Path
from PIL import Image,ImageOps,ImageFilter
import argparse,json
p=argparse.ArgumentParser();p.add_argument('scan',type=int);p.add_argument('--crops');p.add_argument('--rotate',type=int,default=0);a=p.parse_args()
root=Path(__file__).resolve().parents[2];im=Image.open(root/f'source/SP63_C13_15_scans/15_scan{a.scan}.jpg');out=root/'views';out.mkdir(exist_ok=True)
if a.crops:
 for label,box in json.loads(a.crops).items():
  f=out/f'{a.scan}_{label}.png'
  if f.exists():raise ValueError('Refusing second crop of '+str(f))
  cr=ImageOps.autocontrast(im.crop(box)).rotate(a.rotate,expand=True)
  cr=cr.resize((2400,round(cr.height*2400/cr.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=100,threshold=3));cr.save(f);print(label,box)
else:
 im=im.rotate(a.rotate,expand=True);w,h=im.size
 halves={'top':(0,0,w,round(h*.55)),'bottom':(0,round(h*.45),w,h)} if h>=w else {'left':(0,0,round(w*.55),h),'right':(round(w*.45),0,w,h)}
 for label,box in halves.items():
  f=out/f'{a.scan}_{label}.png'
  if f.exists():raise ValueError('Halves already exist')
  im.crop(box).save(f)
 print('Dimensions',im.size)
