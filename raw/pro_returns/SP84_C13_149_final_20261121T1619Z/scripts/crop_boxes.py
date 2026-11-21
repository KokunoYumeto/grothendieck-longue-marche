"""Make the prescribed independent-reading crops; never recognizes text.

This script reads only the target image and its neutral coordinate table.
The independent reader must inspect every output image and write a reading.
"""
from pathlib import Path
import csv,sys
from PIL import Image,ImageOps,ImageFilter

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent

def make(n):
    page=f'149_scan{n:03d}'
    source=BASE/f'source/SP84_C13_149_scans/{page}.jpg'
    with (ROOT/f'second/{page}_boxes.tsv').open() as f:
        boxes=list(csv.DictReader(f,delimiter='\t'))
    im=Image.open(source).convert('RGB')
    manifest=[]
    for b in boxes:
        coords=tuple(int(b[k]) for k in ('x0','y0','x1','y1'))
        assert 0<=coords[0]<coords[2]<=im.width and 0<=coords[1]<coords[3]<=im.height,(b,im.size)
        out=ROOT/f"crops/{page}_second_{b['box']}.png"
        assert not out.exists(),f'Refusing to remake {out}'
        crop=ImageOps.autocontrast(im.crop(coords))
        w=2800;h=round(crop.height*w/crop.width)
        crop=crop.resize((w,h),Image.Resampling.LANCZOS)
        crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=135,threshold=2))
        crop.save(out)
        manifest.append(dict(box=b['box'],crop=str(out.relative_to(ROOT)),x0=coords[0],y0=coords[1],x1=coords[2],y1=coords[3],rotation=0))
    with (ROOT/f'second/{page}_crop_manifest.tsv').open('w') as f:
        writer=csv.DictWriter(f,fieldnames=['box','crop','x0','y0','x1','y1','rotation'],delimiter='\t')
        writer.writeheader();writer.writerows(manifest)
    print(f'{page}: {len(manifest)} image-only crops prepared')

if __name__=='__main__':
    for arg in sys.argv[1:]:make(int(arg))
