from pathlib import Path
from PIL import Image, ImageOps
import json
base=Path('/workspace/scratch/0cab6a548abb/edition')
src=base/'crops/149_scan122_second_b03.png'
im=Image.open(src)
records=[]
def detail(name, box, rotation=0, scale=1):
    img=im.crop(box)
    if rotation:
        img=img.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    if scale != 1:
        img=img.resize((round(img.width*scale),round(img.height*scale)),Image.Resampling.LANCZOS)
    fn=base/'crops'/f'149_scan122_second_b03_{name}.png'
    img.save(fn)
    records.append({'box':'b03','file':str(fn),'derived_from':str(src),'derivative_pixel_bbox':box,'rotation_degrees':rotation,'additional_scale':scale})
detail('margin_rotated',[0,1500,1050,3520],-45,.85)
detail('proof_overview',[780,3500,4950,5350],0,.58)
detail('upper_correction',[2350,300,4950,1250],0,1)
detail('proof_middle',[800,4050,4900,4860],0,.7)
detail('proof_bottom',[800,4770,4900,5350],0,.7)
(base/'second/blind_c_scan122_detail_records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Created {len(records)} derived inspection panels from the saved canonical crop.')
