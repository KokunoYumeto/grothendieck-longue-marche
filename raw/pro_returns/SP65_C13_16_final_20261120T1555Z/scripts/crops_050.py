from PIL import Image,ImageOps
from pathlib import Path
r=Path(__file__).resolve().parents[2];im=Image.open(r/'source/SP65_C13_16_scans/16_scan050.jpg')
boxes={'paragraph':(830,205,1020,260),'intro_a':(195,505,240,555),'intro_sub':(630,505,705,570),'old_of':(865,695,940,765),'old_end':(350,765,795,845),'us':(335,860,395,910),'critical':(510,930,690,985),'plus':(332,1200,405,1260),'prop_C':(448,1350,510,1415),'conjunction':(1000,1350,1235,1410),'analogous':(195,1525,365,1585),'old_product':(695,1630,785,1700),'old_X':(1000,1770,1080,1835),'odd_degree':(320,1820,480,1905)}
for name,box in boxes.items():
 t=r/f'views/050_{name}.png';assert not t.exists();a=ImageOps.autocontrast(im.crop(box));w=2200 if a.width>400 else 1600;a.resize((w,round(a.height*w/a.width)),Image.Resampling.LANCZOS).save(t)
print(boxes)
