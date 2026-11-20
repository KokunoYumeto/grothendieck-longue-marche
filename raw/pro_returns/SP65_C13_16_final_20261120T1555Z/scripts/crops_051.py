from PIL import Image,ImageOps
from pathlib import Path
base=Path('/workspace/scratch/825ce1dd1d03');im=Image.open(base/'source/SP65_C13_16_scans/16_scan051.jpg')
rows=[('degree_words',(170,305,515,400),0,2200),('member',(1340,260,1420,345),0,1800),('chain_symbol',(220,500,325,615),0,1800),('factor',(1140,675,1280,770),0,2000),('degree_insert',(1110,350,1575,485),0,2600),('old_et',(1005,315,1265,375),0,2200),('old_pi',(940,590,1105,675),0,2000),('bounds',(205,800,1115,895),0,2800),('range',(680,1095,895,1170),0,2200),('old_iii',(305,1320,400,1400),0,1800),('old_symbol',(1265,1275,1340,1380),0,1800),('procedure',(1320,1915,1570,2015),0,2200),('margin',(25,575,270,745),-30,2400)]
for name,box,rot,w in rows:
 p=base/'views'/f'051_{name}.png';assert not p.exists()
 c=ImageOps.autocontrast(im.crop(box));c=c.rotate(rot,expand=True,fillcolor='white') if rot else c
 c=c.resize((w,round(c.height*w/c.width)),Image.Resampling.LANCZOS);c.save(p)
 print(name,box)
