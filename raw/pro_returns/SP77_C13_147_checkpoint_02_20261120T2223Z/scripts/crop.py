from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import sys,json
ROOT=Path('/workspace/scratch/88012a0a2bcc')
scan=int(sys.argv[1]);name=sys.argv[2];box=tuple(map(int,sys.argv[3:7]))
im=Image.open(ROOT/f'inputs/SP77_C13_147_scans/147_scan{scan:03d}.jpg')
cr=im.crop(box)
if len(sys.argv)>7: cr=cr.rotate(float(sys.argv[7]),expand=True,fillcolor='white')
cr=ImageOps.autocontrast(cr).resize((2400,round(cr.height*2400/cr.width)),Image.Resampling.LANCZOS)
cr=cr.filter(ImageFilter.UnsharpMask(radius=1,percent=125,threshold=3))
p=ROOT/f'SP77_C13_147_work/crops/147_scan{scan:03d}_{name}.jpg'
cr.save(p,quality=94)
print(json.dumps({'file':str(p),'box':box,'size':cr.size}))
