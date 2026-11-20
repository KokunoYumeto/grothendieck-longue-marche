from PIL import Image,ImageOps,ImageFilter
from pathlib import Path
import json

base=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
im=Image.open(base/'packets/145_scan011/page.jpg')
specs=[
 ('opening_and_number4',[220,21,1599,168],0,3000),
 ('opening_system',[310,164,1608,408],0,3000),
 ('nb_heading',[241,490,487,580],0,2200),
 ('restant',[404,723,1179,829],0,2700),
 ('caractere_cyclotomique',[221,844,1643,947],0,3000),
 ('fonction_insertions',[221,908,1457,1077],0,3000),
 ('group_definition',[500,1028,1283,1201],0,2800),
 ('donnee_gamma',[833,1065,1623,1302],0,2800),
 ('application_map',[444,1843,1320,2090],0,2900),
 ('margin_nb',[21,1725,445,2344],-50,3000),
 ('closing_prose',[279,2107,1615,2352],0,3000),
 ('footer10',[1554,2274,1656,2354],0,2200),
]
saved=[]
for name,box,angle,width in specs:
    crop=ImageOps.autocontrast(im.crop(box).convert('RGB'))
    if angle:crop=crop.rotate(angle,Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
    crop=crop.filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
    rel=f'crops/145_scan011_{name}.png';crop.save(base/'edition'/rel)
    saved.append({'name':name,'box':box,'crop':rel,'rotation':angle})
(base/'edition/reader_reports/145_scan011_crop_manifest.json').write_text(json.dumps(saved,indent=2)+'\n')
print(json.dumps(saved,indent=2))
