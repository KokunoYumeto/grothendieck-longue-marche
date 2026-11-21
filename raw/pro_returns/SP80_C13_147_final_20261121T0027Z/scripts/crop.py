from pathlib import Path
import sys, json
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

BASE=Path(__file__).resolve().parents[2]
scan=int(sys.argv[1]); name=sys.argv[2]
box=tuple(map(int,sys.argv[3:7])); angle=float(sys.argv[7]) if len(sys.argv)>7 else 0
stage='second' if name.startswith('second_') else 'first'
target=BASE/'edition/crops'/f'147_scan{scan:03d}_{name}.jpg'
if target.exists():
    raise RuntimeError(f'Crop already exists: {target}; view it, do not replace or recrop.')
im=Image.open(BASE/'source/SP80_C13_147_scans'/f'147_scan{scan:03d}.jpg')
if not (0<=box[0]<box[2]<=im.width and 0<=box[1]<box[3]<=im.height):
    raise ValueError((box,im.size))
im=ImageOps.autocontrast(im.crop(box))
if angle:im=im.rotate(angle,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
# Fresh crops reach a few thousand pixels across, with a height cap for tall marginal boxes.
scale=max(1, min(2400/im.width,4000/im.height))
im=im.resize((round(im.width*scale),round(im.height*scale)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=115,threshold=3))
im.save(target,quality=92)
row={'scan':scan,'crop':str(target.relative_to(BASE/'edition')),'box':box,'angle':angle,'stage':stage}
with (BASE/'edition/reports'/f'147_scan{scan:03d}_crops.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
print(json.dumps(row))
