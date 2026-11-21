from PIL import Image, ImageOps
from pathlib import Path
import csv,json
base=Path('/workspace/scratch/0cab6a548abb')
source=base/'source/SP88_C13_149_scans/149_scan103.jpg'
rows=list(csv.DictReader((base/'edition/second/149_scan103_boxes.tsv').open(),delimiter='\t'))
im=Image.open(source)
metadata=[]
for row in rows:
    box=row['box']
    bbox=tuple(int(row[key]) for key in ('x0','y0','x1','y1'))
    crop=im.crop(bbox)
    scale=3 if crop.height<200 else 2
    crop=ImageOps.autocontrast(crop).resize((crop.width*scale,crop.height*scale),Image.Resampling.LANCZOS)
    target=base/f'edition/crops/149_scan103_second_{box}.png'
    crop.save(target)
    metadata.append({'box':box,'bbox':list(bbox),'rotation_degrees':0,'scale':scale,'crop_file':str(target)})
(base/'edition/second/blind_a_scan103_crop_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
print(f'Created {len(metadata)} crops; source dimensions {im.size}.')
