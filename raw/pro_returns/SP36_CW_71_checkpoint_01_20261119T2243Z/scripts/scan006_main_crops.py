from pathlib import Path
from PIL import Image,ImageOps
import json
ROOT=Path(__file__).resolve().parents[2]; dest=ROOT/'out/adjudication/scan006'
items=[('span_diagram','a',[1074,151,1452,350]),('points_and_complement','a',[423,1001,1045,1114]),('map_end','a',[1378,1060,1650,1178]),('invariance_heading','b',[397,132,1450,264]),('replacement_words','b',[281,303,1020,398]),('pourvu','b',[1005,414,1381,516]),('sufficiency_dash','b',[744,680,1055,793]),('div_hypotheses','b',[1045,795,1400,900]),('vertical_stroke','b',[269,980,355,1154])]
manifest=[]
for name,half,box in items:
 src=ROOT/f'source/SP36_CW_71_scans/J71-01_71_scan006_{half}.jpg';dst=dest/(name+'.jpg')
 if dst.exists():raise RuntimeError('No recropping')
 with Image.open(src) as im:
  c=ImageOps.autocontrast(im.crop(box).convert('L')); size=(2800,round(c.height*2800/c.width));c=c.resize(size,Image.Resampling.LANCZOS);c.save(dst,quality=97)
 manifest.append(dict(file=str(dst),source=str(src),box=box,rotation=0,output_width=2800,processing='grayscale; autocontrast; LANCZOS; JPEG quality97; no sharpening',place=name,viewed_once=False))
(dest/'new_crops.json').write_text(json.dumps(manifest,indent=2))
print('Created',len(manifest),'new tight crops for main adjudication.')
