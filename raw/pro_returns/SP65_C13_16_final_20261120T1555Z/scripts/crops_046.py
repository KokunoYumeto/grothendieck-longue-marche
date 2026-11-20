from PIL import Image,ImageOps
from pathlib import Path
r=Path(__file__).resolve().parents[2];im=Image.open(r/'source/SP65_C13_16_scans/16_scan046.jpg')
boxes={'thhe':(410,435,510,490),'cancel_et':(790,925,875,985),'edge':(1570,975,1684,1055),'cancel_phi':(550,1275,645,1355),'nb':(1100,1410,1684,1515),'dim':(870,1930,960,1990),'bottom1':(900,1990,1580,2080),'bottom2':(240,2070,730,2125)}
for name,box in boxes.items():
 t=r/f'views/046_{name}.png';assert not t.exists();a=ImageOps.autocontrast(im.crop(box));w=2400 if a.width>500 else 1800;a.resize((w,round(a.height*w/a.width)),Image.Resampling.LANCZOS).save(t)
print(boxes)
