from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import csv,json
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
edition=root/'edition'
packet=root/'audit_packets'/'145_scan008'
with (packet/'boxes.tsv').open(encoding='utf-8',newline='') as f:
    boxes=list(csv.DictReader(f,delimiter='\t'))
im=Image.open(packet/'page.jpg')
manifest=[]
for box in boxes:
    name=box['box']
    coords=[int(box[k]) for k in ('x0','y0','x1','y1')]
    out=edition/'crops'/f'second_145_scan008_{name}.png'
    if out.exists():
        raise SystemExit(f'Refusing to remake {out}')
    crop=im.crop(coords)
    rotation=-25 if name=='B07' else 0
    if rotation:
        crop=crop.rotate(rotation,expand=True,resample=Image.Resampling.BICUBIC,fillcolor='white')
    crop=ImageOps.autocontrast(crop,cutoff=0.5)
    crop=crop.resize((2800,round(crop.height*2800/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
    crop.save(out)
    manifest.append({'box':name,'crop':str(out.relative_to(edition)),'coords':coords,'rotation_degrees':rotation,'observations':''})
mp=edition/'second'/'145_scan008_crop_manifest.json'
if mp.exists(): raise SystemExit('Refusing existing manifest')
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'crops':len(manifest),'page_size':im.size,'manifest':str(mp)},indent=2))

