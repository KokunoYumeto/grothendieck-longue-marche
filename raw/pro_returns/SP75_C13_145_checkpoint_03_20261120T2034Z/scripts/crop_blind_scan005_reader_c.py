from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import csv, json

root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
packet=root/'audit_packets/145_scan005'
img=Image.open(packet/'page.jpg')
with (packet/'boxes.tsv').open(newline='') as f:
    boxes=list(csv.DictReader(f,delimiter='\t'))
manifest=[]
for item in boxes:
    box=[int(item[k]) for k in ['x0','y0','x1','y1']]
    rotation=-45 if item['box']=='B03' else 0
    dest=root/'edition/crops'/f"second_145_scan005_{item['box']}.png"
    if dest.exists(): raise RuntimeError(f'Refusing to remake {dest}')
    crop=ImageOps.autocontrast(img.crop(box),cutoff=0.5)
    if rotation:
        crop=crop.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    crop=crop.resize((2800,round(crop.height*2800/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
    crop.save(dest)
    manifest.append({'box':item['box'],'crop':f'crops/{dest.name}','coords':box,
                     'rotation_degrees':rotation,'observations':''})
target=root/'edition/second/145_scan005_crop_manifest.json'
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'crops':len(manifest),'source_size':img.size,'manifest':str(target)}))
