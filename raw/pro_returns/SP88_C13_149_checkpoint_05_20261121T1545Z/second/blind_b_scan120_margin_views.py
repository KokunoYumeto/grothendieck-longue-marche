"""Rotate saved scan120 crops for reading diagonal marginal text."""
from pathlib import Path
from PIL import Image, ImageDraw
import json
base=Path('/workspace/scratch/0cab6a548abb')
dest=base/'edition/second/diagnostics'
records=[]
for box,angle in [('b08',-47),('b09',-34)]:
    source=base/f'edition/crops/149_scan120_second_{box}.png'
    im=Image.open(source).rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    path=dest/f'149_scan120_{box}_rotated.png'
    im.save(path)
    overview=dest/f'149_scan120_{box}_rotated_overview.png'
    im.resize((1800,round(im.height*1800/im.width)),Image.Resampling.LANCZOS).save(overview)
    panels=[]
    for row,y in enumerate(sorted(set([0,max(0,im.height-1500)])),1):
        for col,x in enumerate(sorted(set([0,max(0,im.width-1800)])),1):
            rect=(x,y,min(x+1800,im.width),min(y+1500,im.height))
            part=im.crop(rect)
            canvas=Image.new('RGB',(part.width,part.height+28),'white')
            canvas.paste(part,(0,28))
            ImageDraw.Draw(canvas).text((8,5),f'{box}, rotation {angle}; panel r{row} c{col}; derivative bbox {rect}',fill='black')
            panel=dest/f'149_scan120_{box}_rot_r{row}_c{col}.png'
            canvas.save(panel)
            panels.append({'file':str(panel),'bbox_in_rotated_derivative':rect})
    records.append({'box':box,'source_saved_crop':str(source),'rotation_degrees_pillow':angle,'rotated_file':str(path),'overview':str(overview),'panels':panels,'source_recropped':False})
(dest/'149_scan120_margin_views_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Rotated saved crops b08 and b09; no new original-coordinate crops.')
