"""Inspect the diagonal annotation from the saved rotated derivative."""
from pathlib import Path
from PIL import Image, ImageDraw
import json

base=Path('/workspace/scratch/0cab6a548abb/edition/second/diagnostics')
im=Image.open(base/'149_scan117_b03_rot29.png')
records=[]
for row,y in enumerate([1500,2450],1):
    for col,x in enumerate([0,1500,3000],1):
        bbox=(x,y,x+1800,y+1350)
        part=im.crop(bbox)
        canvas=Image.new('RGB',(part.width,part.height+28),'white')
        canvas.paste(part,(0,28))
        ImageDraw.Draw(canvas).text((8,5),f'b03 rotated -29 degrees; panel r{row} c{col}; rotated bbox {bbox}',fill='black')
        filename=f'149_scan117_b03_rot29_r{row}_c{col}.png'
        canvas.save(base/filename)
        records.append({'file':str(base/filename),'rotated_derivative_bbox':bbox,'rotation_degrees_pillow':-29})
(base/'149_scan117_rotated_panels_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(len(records),'rotated inspection panels created')
