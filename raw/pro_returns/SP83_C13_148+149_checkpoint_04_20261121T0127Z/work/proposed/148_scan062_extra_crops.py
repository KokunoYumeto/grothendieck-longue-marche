from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/f28c4f52d3ec')
page='148_scan062'
im=Image.open(root/'source/SP83_C13_148+149_scans/148_scan062.jpg').convert('RGB')
items=[
 ('margin_replacement',[270,1485,550,1715],-29),
 ('margin_lower',[24,1680,300,1976],-29),
 ('graph_complete',[765,2070,910,2245],0),
]
records=json.loads((root/'proposed'/f'{page}_crop_boxes.json').read_text())
for rec in records: rec['viewed']=True
for name,box,angle in items:
    p=root/'result/crops'/f'{page}_{name}.png'
    region=ImageOps.autocontrast(im.crop(box))
    if angle: region=region.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    scale=max(3,min(8,3000/region.width))
    region=region.resize((round(region.width*scale),round(region.height*scale)),Image.Resampling.LANCZOS)
    region=region.filter(ImageFilter.UnsharpMask(radius=1.2,percent=105,threshold=3))
    region.save(p)
    records.append({'name':name,'path':str(p),'crop':f'crops/{p.name}','box':box,'rotation':angle,'viewed':False})
(root/'proposed'/f'{page}_crop_boxes.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Created two unresolved margin crops and one graph crop restoring the previously clipped brace top. Retained all earlier files.')
