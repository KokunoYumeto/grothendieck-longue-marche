from pathlib import Path
from PIL import Image,ImageOps
r=Path(__file__).resolve().parents[1]
with Image.open(r.parent/'source/SP88_C13_149_scans/149_scan109.jpg') as im:
 for name,box in [('b06_descender',(320,550,650,715)),('b08_lower_mark',(1390,775,1585,895))]:
  p=r/'crops'/f'149_scan109_audit_{name}.png'
  if p.exists():raise RuntimeError('Already made')
  c=ImageOps.autocontrast(im.crop(box));c.resize((c.width*6,c.height*6),Image.Resampling.LANCZOS).save(p)
  print(name,box)
