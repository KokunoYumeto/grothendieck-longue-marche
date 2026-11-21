"""Crop only the supplied blind box list; never opens witnesses or first readings."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import argparse, csv, json
ROOT=Path('/workspace/scratch/d12e26a9cd50')
OUT=ROOT/'SP93_C13_151_work'
p=argparse.ArgumentParser();p.add_argument('scan',type=int)
p.add_argument('--rotate',action='append',default=[],metavar='BOX:DEGREES',
               help='Rotate this box counterclockwise, as determined from the image alone.')
a=p.parse_args()
rotations={}
for item in a.rotate:
    box,degrees=item.split(':',1)
    rotations[box]=float(degrees)
name=f'151_scan{a.scan:03}'
im=Image.open(ROOT/'source/SP93_C13_151_scans'/f'{name}.jpg')
with (OUT/'second'/f'{name}_boxes.tsv').open(newline='') as f:
    boxes=list(csv.DictReader(f,delimiter='\t'))
for b in boxes:
    coords=[int(b[k]) for k in ['x0','y0','x1','y1']]
    target=OUT/'crops'/f'{name}_second_{b["box"]}.png'
    if target.exists():
        raise FileExistsError(f'Blind crop already exists: {target}')
    crop=ImageOps.autocontrast(im.crop(coords).convert('RGB'))
    if b['box'] in rotations:
        crop=crop.rotate(rotations[b['box']],expand=True,resample=Image.Resampling.BICUBIC)
    # Wide boxes receive the requested enlarged view; tiny upright boxes are
    # bounded on both axes to avoid pointless multi-megapixel empty expansions.
    scale=min(3000/crop.width,3600/crop.height)
    crop=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1,percent=110,threshold=3))
    crop.save(target)
    print(json.dumps({'box':b['box'],'kind':b['kind'],'original_box':coords,'rotation':rotations.get(b['box'],0),'crop':str(target)},ensure_ascii=False))
