from pathlib import Path
import csv,json
from PIL import Image,ImageOps,ImageFilter
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
packet=root/'audit_packets/145_scan021'
ed=root/'edition'
with (packet/'boxes.tsv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
rotations={'B02':-45,'B06':-40,'B08':-45}
manifest=[]
with Image.open(packet/'page.jpg') as source:
    for row in rows:
        box=row['box'];coords=[int(row[k]) for k in ('x0','y0','x1','y1')]
        path=ed/f'crops/second_145_scan021_{box}.png'
        assert not path.exists(),f'Existing crop must not be replaced: {path}'
        crop=ImageOps.autocontrast(source.crop(coords).convert('RGB'))
        rotation=rotations.get(box,0)
        if rotation:crop=crop.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
        width=3000 if box=='B08' else 2500
        crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
        crop=crop.filter(ImageFilter.UnsharpMask(radius=1,percent=105,threshold=3))
        crop.save(path)
        manifest.append({'box':box,'crop':f'crops/second_145_scan021_{box}.png','original_coordinates':coords,'rotation_degrees':rotation,'inspected':False,'observations':[]})
mp=ed/'second/145_scan021_second_manifest.json'
assert not mp.exists()
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Saved {len(manifest)} original crops and provisional manifest.')
