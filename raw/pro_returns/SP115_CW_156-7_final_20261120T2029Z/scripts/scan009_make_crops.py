from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
ROOT=Path('/workspace/scratch/ddf8babdc42e')
SOURCE=ROOT/'source/SP115_CW_156-7_scans/H156-01_156-7_scan009.jpg'
SPECS=[
 ('page_number',[0,0,1300,220],0),
 ('intro_end',[258,329,1612,438],0),
 ('atdc1',[264,452,1673,535],0),
 ('atdc1_follow',[276,516,1683,663],0),
 ('cor1',[421,645,1683,825],0),
 ('cor2',[407,764,1668,899],0),
 ('margin_nb',[22,622,456,1467],-45),
 ('atdc2_header',[266,861,1662,964],0),
 ('atdc2_formula',[278,940,1668,1067],0),
 ('atdc2_assumptions',[286,1047,1669,1160],0),
 ('atdc2_end',[290,1134,1138,1248],0),
 ('onvoudra',[294,1234,741,1308],0),
 ('propriete',[302,1296,1545,1537],0),
 ('reference',[449,1508,1647,1624],0),
 ('cancelled_montrons',[341,1542,1655,1659],0),
 ('ceci_equivalent',[386,1590,1653,1764],0),
 ('margin_criterion',[21,1571,476,2125],-45),
 ('drawing',[46,2125,199,2268],0),
 ('margin_after_figure',[134,1903,631,2348],-45),
 ('atdd1_first',[324,1660,1626,1871],0),
 ('atdd1_rest',[283,1830,1641,2021],0),
 ('cor_main1',[342,1998,1391,2124],0),
 ('cor_main2',[342,2096,1632,2218],0),
 ('plus_gen',[349,2173,1596,2344],0),
 ('upper_cancellation_scope',[261,452,1671,1246],0),
]
im=Image.open(SOURCE)
out=ROOT/'out/crops'
out.mkdir(parents=True,exist_ok=True)
crops=[]
for name,box,rot in SPECS:
    q=im.crop(box)
    if rot:
        q=q.rotate(rot,resample=Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    q=ImageOps.autocontrast(q)
    q=q.filter(ImageFilter.UnsharpMask(radius=1.1,percent=135,threshold=3))
    q=q.resize((2800,round(q.height*2800/q.width)),Image.Resampling.LANCZOS)
    f=out/f'scan009_{name}.png'
    q.save(f)
    crops.append(dict(name=name,file=str(f.relative_to(ROOT)),box=box,rotation_degrees=rot,
      rotation_parameters='Pillow BICUBIC, expand=True, fillcolor=white' if rot else None,
      output_size=list(q.size)))
manifest=dict(source=str(SOURCE.relative_to(ROOT)),source_size=list(im.size),
 coordinate_system='Original whole-image pixels; [x0,y0,x1,y1], right and bottom exclusive.',
 transform_order=['crop','optional rotation','autocontrast','UnsharpMask','resize'],
 default_transform=dict(output_width_px=2800,resize='Pillow LANCZOS, aspect ratio preserved',
 contrast='ImageOps.autocontrast, defaults',sharpen='UnsharpMask(radius=1.1,percent=135,threshold=3)',rotation_degrees=0),
 generation_script='out/scripts/scan009_make_crops.py',crops=crops)
(ROOT/'out/review/scan009_crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print({'crops':len(crops),'source_size':im.size})

