from pathlib import Path
import csv, json
from PIL import Image, ImageOps, ImageFilter
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
packet=root/'audit_packets/145_scan014'
edition=root/'edition'
with (packet/'boxes.tsv').open(encoding='utf-8',newline='') as f:
    boxes=list(csv.DictReader(f,delimiter='\t'))
manifest=[]
with Image.open(packet/'page.jpg') as source:
    for box in boxes:
        coords=[int(box[k]) for k in ('x0','y0','x1','y1')]
        target=edition/f"crops/second_145_scan014_{box['box']}.png"
        assert not target.exists(), f'Existing crop must not be replaced: {target}'
        im=ImageOps.autocontrast(source.crop(coords))
        im=im.resize((2500,round(im.height*2500/im.width)),Image.Resampling.LANCZOS)
        im=im.filter(ImageFilter.UnsharpMask(radius=1,percent=105,threshold=3))
        im.save(target)
        manifest.append({'box':box['box'],'crop':f'crops/{target.name}','original_coordinates':coords,'rotation_degrees':0,'observations':[]})
mp=edition/'second/145_scan014_second_manifest.json'
assert not mp.exists()
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Saved {len(manifest)} crops and initial manifest.')
