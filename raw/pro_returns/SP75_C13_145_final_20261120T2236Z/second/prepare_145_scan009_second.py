from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import csv,json
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
packet=root/'audit_packets/145_scan009'
with (packet/'boxes.tsv').open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t',quoting=csv.QUOTE_NONE))
source=Image.open(packet/'page.jpg')
manifest=[]
for row in rows:
    box=row['box']; coords=[int(row[k]) for k in ('x0','y0','x1','y1')]
    angle=-42 if box=='B09' else 0
    crop=ImageOps.autocontrast(source.crop(coords))
    if angle: crop=crop.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    crop=crop.resize((2500,round(crop.height*2500/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1,percent=105,threshold=3))
    rel=f'crops/second_145_scan009_{box}.png'
    crop.save(root/'edition'/rel)
    manifest.append({'box':box,'crop':rel,'original_coordinates':coords,'rotation_degrees':angle,'observations':[]})
(root/'edition/second/145_scan009_second_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print({'source_size':source.size,'crops_saved':len(manifest),'rotated_box':'B09','rotation_degrees':-42})
