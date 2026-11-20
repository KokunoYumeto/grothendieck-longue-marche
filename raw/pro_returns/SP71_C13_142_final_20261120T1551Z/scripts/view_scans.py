"""Prepare native halves and one-off crops. No OCR or text recognition."""
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import argparse,datetime,csv
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'source/SP71_C13_142_scans'
V=ROOT/'views';V.mkdir(exist_ok=True)
LOG=ROOT/'SP71_C13_142_work/crop_register.tsv'
def halves(n):
 im=Image.open(SRC/f'142_scan{n:03}.jpg');w,h=im.size
 names=['top','bottom'] if h>=w else ['left','right']
 boxes=[(0,0,w,round(h*.55)),(0,round(h*.45),w,h)] if h>=w else [(0,0,round(w*.55),h),(round(w*.45),0,w,h)]
 for name,box in zip(names,boxes):
  path=V/f'{n:03}_{name}.png'
  if path.exists():raise RuntimeError(f'Half already exists: {path}')
  im.crop(box).save(path)
 print(n,im.size)
def crop(n,label,box,rotation=0,width=2400):
 p=V/f'{n:03}_{label}.png'
 if p.exists():raise RuntimeError('This crop already exists; do not crop a decided place again')
 im=Image.open(SRC/f'142_scan{n:03}.jpg').crop(box)
 im=ImageOps.autocontrast(im)
 if rotation:im=im.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
 im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1,percent=120,threshold=3))
 im.save(p)
 new=not LOG.exists()
 with LOG.open('a') as f:
  w=csv.writer(f,delimiter='\t')
  if new:w.writerow(['scan','label','x0','y0','x1','y1','rotation','width','created_utc'])
  w.writerow([n,label,*box,rotation,width,datetime.datetime.now(datetime.timezone.utc).isoformat()])
 print(p)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('scan',type=int);a=ap.parse_args();halves(a.scan)
