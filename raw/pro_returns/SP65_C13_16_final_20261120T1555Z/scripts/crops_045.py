from PIL import Image,ImageOps
from pathlib import Path
r=Path(__file__).resolve().parents[2];im=Image.open(r/'source/SP65_C13_16_scans/16_scan045.jpg')
boxes={'xi1':(1200,150,1330,235),'xi2':(1410,220,1530,310),'xi3':(940,330,1060,420),'cancel_ii':(725,825,1140,900),'cancel_iv':(430,1330,690,1400),'star':(305,1470,425,1545),'degree':(1570,1590,1685,1660),'ces':(475,1895,560,1955),'ells':(680,1965,1030,2040),'nonsing':(1030,2020,1250,2100)}
for name,box in boxes.items():
 t=r/f'views/045_{name}.png';assert not t.exists();a=ImageOps.autocontrast(im.crop(box));w=1800;a.resize((w,round(a.height*w/a.width)),Image.Resampling.LANCZOS).save(t)
print(boxes)
box=(1300,1970,1490,2030);t=r/'views/045_chain.png';assert not t.exists();a=ImageOps.autocontrast(im.crop(box));a.resize((1800,round(a.height*1800/a.width)),Image.Resampling.LANCZOS).save(t)
