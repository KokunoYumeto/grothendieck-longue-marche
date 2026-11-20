"""One-off manually selected visual crop. No OCR. Coordinates refer to the source image."""
from pathlib import Path
import sys,csv
from PIL import Image,ImageOps,ImageFilter,ImageEnhance
root=Path(__file__).resolve().parents[2]
key,tag=sys.argv[1:3];box=tuple(map(int,sys.argv[3:7]));angle=float(sys.argv[7]) if len(sys.argv)>7 else 0
out=root/'views'/(key+'_crop_'+tag+'.png')
if out.exists():raise RuntimeError('Crop exists; do not recrop decided places')
im=Image.open(root/'source/SP66_C13_16+120+136_scans'/(key+'.jpg')).crop(box)
im=ImageOps.autocontrast(im)
if angle:im=im.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
w=3200;im=im.resize((w,round(im.height*w/im.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.4,percent=110,threshold=3));im.save(out)
p=root/'work/CROP_LEDGER.tsv';exists=p.exists()
with p.open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 if not exists:w.writerow(['page','tag','x0','y0','x1','y1','rotation_degrees'])
 w.writerow([key,tag,*box,angle])
print(str(out))
