from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
import json

ROOT=Path('/workspace/scratch/8759b8008681')
im=Image.open(ROOT/'source/SP89_C13_149+150_scans/150_scan012.jpg')
assert im.size==(1685,2361)
boxes={
 'P00':[30,18,192,184],
 'P01':[517,35,1674,199],
 'P02':[1090,185,1679,315],
 'P03':[107,248,834,358],
 'P04':[1176,273,1592,377],
 'P05':[202,355,502,439],
 'P06':[1266,363,1662,457],
 'P07':[203,438,520,512],
 'P08':[197,517,1443,595],
 'P09':[193,603,1335,690],
 'P10':[382,759,873,890],
 'P11':[978,758,1665,1136],
 'P12':[17,842,435,1240],
 'P13':[378,883,1317,977],
 'P14':[770,927,1233,1198],
 'P15':[16,933,752,1587],
 'P16':[205,1190,1605,1293],
 'P17':[209,1300,1255,1512],
 'P18':[895,1490,1676,1571],
 'P19':[899,1574,1167,1677],
 'P20':[1184,1569,1679,1695],
 'P21':[1203,1825,1648,1921],
 'P22':[213,1994,1666,2091],
 'P23':[210,2078,1668,2167],
 'P24':[208,2167,1670,2260],
 'P25':[220,2245,1649,2347],
 'P26':[24,2303,75,2345],
}
rotations={'P12':-25,'P15':-39}
out=ROOT/'work/reports/150_scan012'
(out/'crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
(out/'crop_rotations.json').write_text(json.dumps(rotations,indent=2)+'\n')
for k,b in boxes.items():
 p=ROOT/f'work/crops/150_scan012_{k}.png'
 assert not p.exists(),p
 t=ImageOps.autocontrast(im.crop(b).convert('L'))
 if k in rotations:
  t=t.rotate(rotations[k],resample=Image.Resampling.BICUBIC,expand=True,fillcolor=255)
 width=3000 if k not in ('P00','P26') else 1800
 t=t.resize((width,round(t.height*width/t.width)),Image.Resampling.LANCZOS)
 ImageEnhance.Sharpness(t).enhance(1.12).save(p)
print(f'{len(boxes)} crops saved')
