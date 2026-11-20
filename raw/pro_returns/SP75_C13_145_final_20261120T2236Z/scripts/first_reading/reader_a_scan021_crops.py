from pathlib import Path
import json
from PIL import Image, ImageOps, ImageFilter

root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
page=Image.open(root/'packets/145_scan021/page.jpg').convert('RGB')
targets=[
 ('heading_system13',[300,68,1338,365],0,3000),
 ('nb_margin',[24,263,303,723],-40,2500),
 ('image_reciproque',[274,338,1636,525],0,3000),
 ('operations_above',[276,540,1620,841],0,3000),
 ('plane_and_lacets',[244,853,1522,1187],0,3000),
 ('transport_margin',[24,740,387,1194],-40,2800),
 ('formula14',[214,1228,1451,1477],0,3000),
 ('critique_margin',[16,1128,440,2288],-45,3000),
 ('relations_font',[224,1480,1616,1692],0,3000),
 ('elimination',[225,1695,1663,1910],0,3000),
 ('remonter',[257,1920,1538,2116],0,3000),
 ('footer20',[1537,2270,1640,2340],0,2000),
 ('upper_e_s_marks',[828,302,1178,429],0,2600),
]
manifest=[]
for name,box,rotation,width in targets:
    im=page.crop(box)
    if rotation:
        im=im.rotate(rotation,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    im=ImageOps.autocontrast(im)
    im=im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
    im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=130,threshold=3))
    relative=f'crops/145_scan021_{name}.png'
    im.save(root/'edition'/relative)
    manifest.append(dict(name=name,box=box,crop=relative,rotation=rotation))
(root/'edition/reader_reports/145_scan021_crop_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
