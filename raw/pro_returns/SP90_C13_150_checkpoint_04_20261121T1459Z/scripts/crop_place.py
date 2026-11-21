from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import argparse, json
p=argparse.ArgumentParser()
p.add_argument('scan',type=int);p.add_argument('place');p.add_argument('box',nargs=4,type=int)
p.add_argument('--rotate',type=float,default=0);p.add_argument('--second',action='store_true')
a=p.parse_args()
root=Path(__file__).resolve().parents[2]
src=root/'source/SP90_C13_150_scans'/f'150_scan{a.scan:03}.jpg'
im=Image.open(src).convert('RGB'); crop=im.crop(tuple(a.box))
if a.rotate: crop=crop.rotate(a.rotate,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
crop=ImageOps.autocontrast(crop,cutoff=0.2)
factor=max(1,2600/crop.width)
crop=crop.resize((round(crop.width*factor),round(crop.height*factor)),Image.Resampling.LANCZOS)
crop=crop.filter(ImageFilter.UnsharpMask(radius=1,percent=110,threshold=3))
name=f'150_scan{a.scan:03}_{a.place}.jpg'; dest=root/'SP90_C13_150_work/crops'/name
if dest.exists(): raise FileExistsError('Do not recrop a decided place: '+str(dest))
crop.save(dest,quality=94,subsampling=0)
meta={'file':name,'scan':a.scan,'box':a.box,'rotation_degrees':a.rotate,'output_size':list(crop.size),'phase':'second' if a.second else 'first'}
dest.with_suffix('.json').write_text(json.dumps(meta,indent=2))
print(json.dumps(meta))
