from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path('/workspace/scratch/94548b74fbe0')
out=root/'out/readers/012/C'
(out/'crops').mkdir(exist_ok=True)
im=Image.open(root/'source/SP40_CW_81_scans/J81-02_81_scan012.jpg')
items=[
('01_upper_right_label',(1435,20,1553,121),'C doubt row 1: final letter case in upper-right OK label'),
('02_between_miniatures',(149,811,268,900),'C doubt row 2: compressed ou between miniature ovals'),
('03_overdrawn_left_oval',(142,547,407,838),'C doubt row 3: oval, crossing chords, superposed zigzags and their cancellation role; complete upper/lower overdrawn endpoints'),
('04_connected_right_group',(797,339,1664,1202),'H cancellation assertion and right group rule/curve geometry; full connected extents'),
('05_faint_lower_curve',(349,1254,456,1356),'Untranscribed faint curved trace beneath drawing field'),
('06_lower_dark_dot',(742,1385,829,1470),'Detached dark mark in otherwise blank lower field'),
('07_lower_paired_dots',(1478,1670,1563,1748),'Detached paired dark marks in lower-right field'),
('08_triangle_upper_tick',(177,418,251,493),'Detached tick above triangle apex and local pale traces'),
('09_gap_mark',(412,451,486,530),'Detached dark dot and faint spot between point and upright loop'),
('10_upper_pair',(527,16,644,107),'Small separated upper marks to right of miniature oval'),
('11_right_edge_dash',(1620,756,1680,829),'Right-edge horizontal mark at fold level, omitted by C'),
('12_faint_low_vertical',(1401,2058,1491,2145),'Pale lower-field upright trace; determine supported shape without supplying a character')
]
manifest=[]
for name,bbox,purpose in items:
 crop=ImageOps.autocontrast(im.crop(bbox),cutoff=0)
 width=2400 if bbox[2]-bbox[0]<400 else 2800
 ratio=width/crop.width
 crop=crop.resize((width,round(crop.height*ratio)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1.0,percent=70,threshold=3))
 rel='crops/'+name+'.png'
 crop.save(out/rel)
 manifest.append(dict(path=rel,bbox=list(bbox),rotation=0,purpose=purpose,source_image='source/SP40_CW_81_scans/J81-02_81_scan012.jpg',processing='PIL autocontrast cutoff=0, LANCZOS resize, UnsharpMask radius=1 percent=70 threshold=3'))
(out/'crops/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(manifest),'planned crops; full-scan coordinates; half a origin (0,0), half b origin (0,1100).')
