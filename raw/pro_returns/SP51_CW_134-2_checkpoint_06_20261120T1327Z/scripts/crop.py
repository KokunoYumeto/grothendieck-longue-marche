"""Create one adjudication crop; no OCR or text-recognition operations."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import argparse, json

def make_crop(source, target, bbox, width=2800, rotate=0, reason=''):
    target=Path(target)
    if target.exists(): raise FileExistsError(f'Crop already exists: {target}; reuse it rather than recrop.')
    target.parent.mkdir(parents=True,exist_ok=True)
    with Image.open(source) as im:
        cropped=im.crop(tuple(bbox))
        if rotate: cropped=cropped.rotate(rotate,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
        cropped=ImageOps.autocontrast(cropped)
        size=(width,round(cropped.height*width/cropped.width))
        cropped=cropped.resize(size,Image.Resampling.LANCZOS)
        cropped=cropped.filter(ImageFilter.UnsharpMask(radius=1.2,percent=115,threshold=3))
        cropped.save(target,quality=94)
    meta={'source':str(source),'crop':str(target),'bbox':list(bbox),'output_size':list(size),'rotation':rotate,'reason':reason}
    target.with_suffix('.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
    return meta

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('target');p.add_argument('bbox',nargs=4,type=int);p.add_argument('--width',type=int,default=2800);p.add_argument('--rotate',type=float,default=0);p.add_argument('--reason',default='')
    a=p.parse_args();print(json.dumps(make_crop(a.source,a.target,a.bbox,a.width,a.rotate,a.reason),ensure_ascii=False))
