from pathlib import Path
from PIL import Image, ImageOps
root=Path(__file__).resolve().parents[1]
source=root.parent/'source/SP88_C13_149_scans/149_scan105.jpg'
# Both places remained open after the assigned audit crops. No settled word is recropped.
with Image.open(source) as im:
 for name,box in [('b04_ending',(1120,190,1440,320)),('b14_abbreviation',(1430,2020,1680,2215))]:
  p=root/'crops'/f'149_scan105_audit_{name}.png'
  if p.exists():raise RuntimeError('Do not recrop')
  c=ImageOps.autocontrast(im.crop(box).convert('RGB'));c.resize((c.width*6,c.height*6),Image.Resampling.LANCZOS).save(p)
  print(name,box)
