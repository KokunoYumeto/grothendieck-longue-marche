from PIL import Image,ImageOps,ImageEnhance
import csv,json
from pathlib import Path
root=Path('/workspace/scratch/0cab6a548abb')
source=root/'source/SP88_C13_149_scans/149_scan106.jpg'
img=Image.open(source)
records=[]
with (root/'edition/second/149_scan106_boxes.tsv').open(newline='',encoding='utf8') as f:
    for row in csv.DictReader(f,delimiter='\t'):
        bbox=tuple(int(row[k]) for k in ('x0','y0','x1','y1'))
        crop=img.crop(bbox)
        crop=ImageOps.autocontrast(crop).resize((crop.width*3,crop.height*3),Image.Resampling.LANCZOS)
        path=root/f"edition/crops/149_scan106_second_{row['box']}.png"
        crop.save(path)
        records.append({'box':row['box'],'crop_file':str(path),'bbox':list(bbox),'rotation_degrees':0,'scale':3,'processing':'Pillow crop once, autocontrast, LANCZOS 3x'})
(root/'edition/second/blind_c_scan106_crop_records.json').write_text(json.dumps(records,indent=2),encoding='utf8')
print('Created',len(records),'crops. Source dimensions:',img.size)
