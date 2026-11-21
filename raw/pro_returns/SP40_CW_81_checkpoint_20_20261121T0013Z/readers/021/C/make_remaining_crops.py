from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
base=Path('out/readers/021/C')
src=Path('source/SP40_CW_81_scans/J81-03_81_scan021.jpg')
items=[
('crop18_first_intersection',(545,140,1025,285),'Complete first two Sigma heads, roofs and indices; separate runs left open after half inspection'),
('crop19_second_intersection',(1225,145,1545,290),'Complete right-hand intersection Sigma heads and low alpha0'),
('crop20_first_union_sigma',(505,460,1045,625),'Complete first main union, roofed Sigma head and indices'),
('crop21_last_union_sigma',(575,1900,1085,2075),'Complete corollary union, roofed Sigma head and indices'),
('crop22_proof_conclusion',(275,1520,925,1655),'Complete concluding intersections, Sigma heads and cqfd punctuation')
]
im=Image.open(src)
man=json.loads((base/'crop_manifest.json').read_text())
for stem,bbox,purpose in items:
    cut=im.crop(bbox)
    target_width=2600
    target_height=round(cut.height*target_width/cut.width)
    cut=ImageOps.autocontrast(cut.resize((target_width,target_height),Image.Resampling.LANCZOS))
    cut=cut.filter(ImageFilter.UnsharpMask(radius=1.2,percent=100,threshold=3))
    target=base/(stem+'.png'); cut.save(target)
    man['crops'].append({'path':target.name,'source':str(src),'bbox':list(bbox),'coordinate_origin':'full scan top-left; x right, y down','rotation':0,'output_size':[target_width,target_height],'purpose':purpose,'viewed':False})
(base/'crop_manifest.json').write_text(json.dumps(man,ensure_ascii=False,indent=2)+'\n')
print('Prepared five further distinct open head/formula targets; first seventeen crops were viewed once each.')
