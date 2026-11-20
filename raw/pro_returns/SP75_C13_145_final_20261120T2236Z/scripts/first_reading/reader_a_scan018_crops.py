from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import json
base=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
im=Image.open(base/'packets/145_scan018/page.jpg')
specs=[
('top_system',[300,50,1278,281],0,3000),
('margin_trials',[1309,48,1678,329],0,2400),
('margin_identity',[1330,294,1678,419],0,2500),
('margin_actions',[1380,390,1678,707],0,2400),
('rho_path',[246,292,1377,472],0,3000),
('conjugation_system',[407,500,1230,791],0,3000),
('contre',[223,892,1602,1088],0,3000),
('crossed_relation_and_cube',[224,1075,1585,1390],0,3000),
('rho_deletion_and_faudra',[249,1397,1590,1565],0,3000),
('pas_and_struck_ending',[252,1570,1566,1778],0,3000),
('dotted_presentation',[420,1776,1620,2013],0,3000),
('small_margin',[460,1899,818,2049],-25,2500),
('que_systeme',[270,2012,1620,2118],0,3000),
('final_paragraph',[240,2188,1627,2348],0,3000),
('faux_margin',[38,2010,550,2344],-40,3000),
('footer17',[1530,2280,1643,2351],0,2000),
]
items=[]
for name,box,angle,width in specs:
    cr=ImageOps.autocontrast(im.crop(box).convert('RGB'))
    if angle:cr=cr.rotate(angle,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    cr=cr.resize((width,round(cr.height*width/cr.width)),Image.Resampling.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
    rel=f'crops/145_scan018_{name}.png';cr.save(base/'edition'/rel)
    items.append({'name':name,'box':box,'crop':rel,'rotation':angle})
p=base/'edition/reader_reports/145_scan018_crop_manifest.json'
p.write_text(json.dumps(items,indent=2)+'\n')
print(json.dumps({'crops':len(items),'manifest':str(p),'names':[x['name'] for x in items]}))
