from PIL import Image,ImageOps
from pathlib import Path
r=Path(__file__).resolve().parents[2];im=Image.open(r/'source/SP65_C13_16_scans/16_scan047.jpg')
boxes={'soc':(785,330,875,385),'will':(1420,845,1530,900),'birat':(1040,1050,1305,1110)}
for name,box in boxes.items():
 t=r/f'views/047_{name}.png';assert not t.exists();a=ImageOps.autocontrast(im.crop(box));a.resize((1800,round(a.height*1800/a.width)),Image.Resampling.LANCZOS).save(t)
print(boxes)
