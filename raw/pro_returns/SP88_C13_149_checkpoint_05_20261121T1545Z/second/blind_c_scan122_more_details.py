from pathlib import Path
from PIL import Image
import json
b=Path('/workspace/scratch/0cab6a548abb/edition')
p=b/'crops/149_scan122_second_b03.png'
im=Image.open(p)
rs=[]
for name,bb in [('proof_formula',[3050,3680,4950,4300]),('proof_correction',[2100,4630,4950,5100]),('regular_insertion',[1400,4060,2550,4530])]:
    fn=b/'crops'/f'149_scan122_second_b03_{name}.png'
    im.crop(bb).save(fn)
    rs.append({'box':'b03','file':str(fn),'derived_from':str(p),'derivative_pixel_bbox':bb,'rotation_degrees':0})
(b/'second/blind_c_scan122_more_detail_records.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Created 3 proof detail panels.')
