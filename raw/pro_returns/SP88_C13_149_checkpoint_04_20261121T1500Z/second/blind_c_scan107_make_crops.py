from PIL import Image,ImageOps
from pathlib import Path
import csv,json
root=Path('/workspace/scratch/0cab6a548abb')
img=Image.open(root/'source/SP88_C13_149_scans/149_scan107.jpg')
records=[]
with (root/'edition/second/149_scan107_boxes.tsv').open(newline='',encoding='utf8') as f:
    for row in csv.DictReader(f,delimiter='\t'):
        bbox=tuple(int(row[k]) for k in ('x0','y0','x1','y1'))
        im=img.crop(bbox)
        im=ImageOps.autocontrast(im).resize((im.width*3,im.height*3),Image.Resampling.LANCZOS)
        path=root/f"edition/crops/149_scan107_second_{row['box']}.png"
        im.save(path)
        records.append({'box':row['box'],'crop_file':str(path),'bbox':list(bbox),'rotation_degrees':0,'scale':3,'processing':'Pillow crop once, autocontrast, LANCZOS 3x'})
(root/'edition/second/blind_c_scan107_crop_records.json').write_text(json.dumps(records,indent=2),encoding='utf8')
print('Created',len(records),'source crops.')
