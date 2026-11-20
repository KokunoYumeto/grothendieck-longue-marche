from pathlib import Path
import csv,json
from PIL import Image,ImageOps,ImageFilter
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
packet=root/'audit_packets/145_scan018'; edition=root/'edition'
with (packet/'boxes.tsv').open(encoding='utf-8',newline='') as f:
    boxes=list(csv.DictReader(f,delimiter='\t'))
manifest=[]
rotations={'B10':-35,'B14':-45}
with Image.open(packet/'page.jpg') as source:
    for box in boxes:
        coords=[int(box[k]) for k in ('x0','y0','x1','y1')]
        target=edition/f"crops/second_145_scan018_{box['box']}.png"
        assert not target.exists(),f'Existing crop must not be replaced: {target}'
        im=ImageOps.autocontrast(source.crop(coords))
        rotation=rotations.get(box['box'],0)
        if rotation:
            im=im.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
        width=2200 if box['box']=='B02' else 2500
        im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
        im=im.filter(ImageFilter.UnsharpMask(radius=1,percent=105,threshold=3))
        im.save(target)
        manifest.append({'box':box['box'],'crop':f'crops/{target.name}','original_coordinates':coords,'rotation_degrees':rotation,'observations':[]})
mp=edition/'second/145_scan018_second_manifest.json'
assert not mp.exists()
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Saved {len(manifest)} crops and initial manifest.')
