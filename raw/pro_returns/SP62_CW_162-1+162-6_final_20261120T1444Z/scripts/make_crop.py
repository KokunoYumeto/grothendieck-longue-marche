"""One recorded, explicit crop per unresolved visual place. No OCR."""
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import csv, sys
from datetime import datetime, timezone

if __name__=='__main__':
    source=Path(sys.argv[1]); label=sys.argv[2]
    box=tuple(map(int,sys.argv[3:7])); angle=float(sys.argv[7]) if len(sys.argv)>7 else 0
    root=Path(__file__).resolve().parents[1]
    log=root/'crop_register.tsv'
    if log.exists():
        with log.open() as f:
            if any(r['place']==label and r['source']==source.name for r in csv.DictReader(f,delimiter='\t')):
                raise SystemExit('This place already has a crop; do not crop it twice.')
    im=Image.open(source).crop(box)
    if angle: im=im.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    im=ImageOps.autocontrast(im)
    width=2400
    im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.5,percent=110,threshold=3))
    dest=root.parent/'temp_crops';dest.mkdir(exist_ok=True)
    target=dest/f'{source.stem}_{label}.jpg'; im.save(target,quality=94)
    exists=log.exists()
    with log.open('a',newline='') as f:
        w=csv.writer(f,delimiter='\t')
        if not exists:w.writerow(['source','place','x0','y0','x1','y1','rotation_ccw_degrees','time_UTC'])
        w.writerow([source.name,label,*box,angle,datetime.now(timezone.utc).isoformat()])
    print(target)
