from PIL import Image,ImageOps
from pathlib import Path
im=Image.open('source/SP65_C13_16_scans/16_scan042.jpg')
boxes={'first_sub':(1230,255,1505,340),'cancel_et':(900,265,990,325),'correspond':(805,595,1095,660),'insert_degree':(1330,610,1689,730),'polarise':(870,685,1500,755),'cancel_xi':(760,745,1115,825),'cancel_sum':(1080,850,1565,955),'cancel_middle':(555,975,1260,1105),'pn':(705,1180,920,1260),'final':(940,1620,1620,1840)}
for name,box in boxes.items():
 out=Path('views')/f'042_{name}.png';assert not out.exists()
 c=ImageOps.autocontrast(im.crop(box));c=c.rotate(3,expand=True) if name=='final' else c
 w=2600 if c.width>500 else 1400;c.resize((w,round(c.height*w/c.width)),Image.Resampling.LANCZOS).save(out)
print(boxes)
