from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan062'
im=Image.open(root/'source/SP83_C13_148+149_scans/148_scan062.jpg').convert('RGB')
items=[
('topfolio',[730,20,825,95],0),
('dira',[1110,225,1440,340],0),
('uniques',[1350,338,1610,418],0),
('global_formula',[586,455,860,596],0),
('insertion',[824,392,1645,508],0),
('operations',[745,580,1358,690],0),
('reconstitue',[1046,677,1604,782],0),
('exception',[28,669,321,924],-28),
('cancelled_diagrams',[480,1047,1120,1602],0),
('live_frame',[738,1158,1673,1435],0),
('shorthand',[790,1337,1075,1515],0),
('margin',[20,1275,610,1980],-29),
('definition_index',[296,1715,458,1830],0),
('pour_tout',[306,1915,580,2023],0),
('tuple',[308,2012,804,2136],0),
('graph',[765,2098,905,2244],0),
('libres_weight',[920,2098,1418,2235],0),
('final_clause',[846,2279,1544,2348],0),
('bottomfolio',[36,2268,120,2334],0),
]
out=[]
for name,box,angle in items:
    p=root/'result/crops'/f'{page}_{name}.png'
    region=ImageOps.autocontrast(im.crop(box))
    if angle: region=region.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    scale=max(3,min(8,3000/region.width))
    region=region.resize((round(region.width*scale),round(region.height*scale)),Image.Resampling.LANCZOS)
    region=region.filter(ImageFilter.UnsharpMask(radius=1.2,percent=105,threshold=3))
    region.save(p)
    out.append({'name':name,'path':str(p),'crop':f'crops/{p.name}','box':box,'rotation':angle,'viewed':False})
(root/'proposed'/f'{page}_crop_boxes.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'Created {len(out)} crops; dimensions in original-pixel boxes retained.')
