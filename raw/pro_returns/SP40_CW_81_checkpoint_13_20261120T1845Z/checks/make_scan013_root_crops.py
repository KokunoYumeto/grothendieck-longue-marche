from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/crops/013';OUT.mkdir(parents=True,exist_ok=True)
source=BASE/'source/SP40_CW_81_scans/J81-02_81_scan013.jpg'
rows=[
('01_rules_top.png',(18,105,2358,312),0,'Table ruling: first two horizontal rules and pale intermediate row near y285; no glyph adjudication'),
('02_rules_middle.png',(18,541,2358,858),0,'Table ruling: four horizontal paths near y555/640/753/842, all six columns; wording context only'),
('03_rules_subdivisions.png',(18,918,2358,1106),0,'Table ruling: faint intermediate path near y932 and lower subdivision rule near y1090; crossed words context only'),
('04_rules_lower.png',(18,1192,2358,1317),0,'Table ruling: lower title and translation rules near y1205/1298; attached local dark wedge contextual'),
('05_rule_foot.png',(18,1545,2358,1588),0,'Table ruling: final long horizontal path near y1564'),
('06_vertical_first.png',(381,181,432,1678),90,'First column division pale long trace near x400; narrow rotated strip, date hook context only'),
('07_vertical_second.png',(770,181,817,1678),90,'Second proposed column division near x792, disputed A versus B/C'),
('08_vertical_third.png',(1165,181,1212,1678),90,'Third proposed column division near x1186, disputed A versus B/C'),
('09_vertical_fourth.png',(1543,11,1593,1678),90,'Fourth proposed division near x1570 including A upper extension'),
('10_vertical_fifth.png',(1943,181,1995,1678),90,'Fifth proposed column division near x1967, disputed A versus B/C')]
im=Image.open(source)
manifest=[]
for name,bbox,rot,purpose in rows:
 p=OUT/name;assert not p.exists(),p
 crop=ImageOps.autocontrast(im.crop(bbox))
 if rot:crop=crop.rotate(rot,expand=True)
 width=4000
 crop=crop.resize((width,round(crop.height*width/crop.width)),Image.Resampling.LANCZOS)
 crop=crop.filter(ImageFilter.UnsharpMask(radius=1,percent=80,threshold=2));crop.save(p)
 manifest.append({'path':str(p.relative_to(BASE/'out')),'bbox':list(bbox),'rotation':rot,'purpose':purpose,'source_image':str(source.relative_to(BASE)),'processing':'PIL autocontrast, LANCZOS4000px across after rotation, mild UnsharpMask','viewed':False})
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Created10 targeted ruling crops; none viewed by root yet.')
