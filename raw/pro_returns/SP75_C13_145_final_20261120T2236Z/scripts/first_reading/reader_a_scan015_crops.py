from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import json
base=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
im=Image.open(base/'packets/145_scan015/page.jpg')
specs=[
('opening_and_insertion',[271,15,1654,215],3000),
('expanded_product',[398,410,1065,650],3000),
('margin_relation',[1199,420,1638,559],2500),
('on_a_donc',[269,644,969,774],2800),
('on_peut_tirer',[295,789,1658,890],3000),
('sans_doute',[325,1330,1010,1435],2800),
('first_live_relation',[655,1450,1027,1542],2400),
('divider',[260,1787,403,1834],2200),
('critique_firstlines',[230,1835,1609,2064],3000),
('profinis',[232,2050,1540,2240],3000),
('final_line',[231,2230,1629,2339],3000),
('footer14',[15,2280,105,2356],2000),
]
items=[]
for name,box,width in specs:
    cr=ImageOps.autocontrast(im.crop(box).convert('RGB'))
    cr=cr.resize((width,round(cr.height*width/cr.width)),Image.Resampling.LANCZOS)
    cr=cr.filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
    rel=f'crops/145_scan015_{name}.png'
    cr.save(base/'edition'/rel)
    items.append({'name':name,'box':box,'crop':rel,'rotation':0})
p=base/'edition/reader_reports/145_scan015_crop_manifest.json'
p.write_text(json.dumps(items,indent=2)+'\n')
print(json.dumps({'crops':len(items),'manifest':str(p),'names':[x['name'] for x in items]}))
