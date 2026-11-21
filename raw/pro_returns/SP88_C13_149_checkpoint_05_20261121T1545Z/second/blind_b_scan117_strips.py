"""Save contextual reading strips from the already inspected crop derivatives."""
from pathlib import Path
from PIL import Image
import json

base=Path('/workspace/scratch/0cab6a548abb')
dest=base/'edition/second/diagnostics'
specs=[
    ('main_question',base/'edition/crops/149_scan117_second_b03.png',(750,770,4700,1725)),
    ('main_middle',base/'edition/crops/149_scan117_second_b03.png',(700,1720,4850,2720)),
    ('margin_upper',dest/'149_scan117_b03_rot29.png',(500,1600,4900,2650)),
    ('margin_lower',dest/'149_scan117_b03_rot29.png',(0,2500,2300,3650)),
]
records=[]
for name,source,bbox in specs:
    part=Image.open(source).crop(bbox)
    part=part.resize((1800,round(part.height*1800/part.width)),Image.Resampling.LANCZOS)
    path=dest/f'149_scan117_{name}_strip.png'
    part.save(path)
    records.append({'file':str(path),'input':str(source),'derivative_bbox':bbox,'resized_width':1800})
(dest/'149_scan117_strip_manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(len(records),'contextual strips created')
