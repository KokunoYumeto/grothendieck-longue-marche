from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_073/R3')
source=Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan073.jpg')
(root/'crops').mkdir(exist_ok=True)
items=[
('01_margin',(20,20,310,455),-53,2500,'Entire slanted marginal note, including low detached de-like group; lettering and line order.'),
('02_top_deleted',(670,25,1115,265),0,2500,'Cancelled primed letter after de, with folio and surrounding lines.'),
('03_top_overwrite',(1165,75,1620,295),0,2500,'Worked G in second continuation line and its older layer.'),
('04_c7_final',(1210,420,1665,650),0,2500,'Final verb and open primed capital of C7 statement; preceding line retained.'),
('05_roles_orders',(760,630,1535,855),0,2700,'Role ending, descender touching extra mark before straight order, and bowed order.'),
('06_faux_mark',(410,745,810,1045),0,2400,'Curled crossed mark after faux and following colon, with context above and below.'),
('07_donnes',(290,840,790,1138),0,2500,'Donnés ending/number of e strokes and following comma with surrounding two lines.'),
('08_tte_sousfigure',(900,845,1650,1145),0,2700,'tte ending, possible lexical hyphen, noun ending, and associated primes.'),
('09_soit',(290,945,835,1152),0,2500,'Verb between F prime and induite, with adjacent adjective ending.'),
('10_parenthesis_F',(1360,960,1665,1160),0,2400,'Worked last F and final parenthesis punctuation.'),
('11_strengthen',(440,1130,1660,1350),0,2800,'Renforcera versus renforcer, par la suite, and nearby C7 zero reference.'),
('12_before_C7',(275,1160,755,1435),0,2400,'Small older mark before C7 and surrounding choice paragraph.'),
('13_draft_heading',(275,1450,1050,1710),0,2800,'Cancelled title, inserted Considérons les, connector enclosure, Conditions and cancelled adjective.'),
('14_draft_G',(1060,1450,1658,1695),0,2600,'Worked G after F comma and remaining Soient line.'),
('15_draft_conclusion',(960,2000,1662,2170),0,2800,'Word after Mais pas, possible comma, and final three exclamation marks/parenthesis/point.'),
('16_diagram',(1250,2070,1565,2320),0,2500,'Complete small square including relation overstroke, left cup, dotted links and all endpoints.'),
('17_final_arrow',(330,2145,1110,2338),0,2800,'Cancelled first implication and final heavy implication with full final C7 zero.'),
]
base=Image.open(source)
manifest=[]
for name,bbox,rotation,width,reason in items:
    im=base.crop(bbox)
    if rotation: im=im.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    scale=width/im.width
    im=im.resize((width,round(im.height*scale)),Image.Resampling.LANCZOS)
    im=ImageOps.autocontrast(im).filter(ImageFilter.UnsharpMask(radius=1.2,percent=110,threshold=3))
    path=root/'crops'/f'{name}.jpg'
    im.save(path,quality=94)
    manifest.append({'path':str(path),'source':str(source),'bbox':list(bbox),'scale':scale,'rotation':rotation,'reason':reason,'width':im.width,'height':im.height})
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(manifest),'own crops.')
