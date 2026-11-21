from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
import json
root=Path('/workspace/scratch/8759b8008681')
im=Image.open(root/'source/SP89_C13_149+150_scans/150_scan007.jpg')
boxes={
 'P01':[1283,41,1349,116],
 'P02':[242,128,753,430],
 'P03':[93,315,177,475],
 'P04':[1148,139,1402,342],
 'P05':[540,496,752,580],
 'P06':[755,493,1334,683],
 'P07':[255,678,1038,795],
 'P08':[255,769,1530,1095],
 'P09':[1025,1102,1254,1223],
 'P10':[43,763,328,1168],
 'P11':[260,1207,578,1312],
 'P12':[250,1280,1490,1618],
 'P13':[629,1606,1303,2153],
 'P14':[159,1900,515,2224],
 'P15':[104,2229,152,2289],
}
rotations={'P03':-90,'P10':-90,'P14':-55}
for k,b in boxes.items():
 p=root/f'work/crops/150_scan007_{k}.png'
 assert not p.exists(),p
 t=ImageOps.autocontrast(im.crop(b).convert('L'))
 if k in rotations:
  t=t.rotate(rotations[k],resample=Image.Resampling.BICUBIC,expand=True,fillcolor=255)
 width=2800 if k not in ('P01','P15') else 1800
 t=t.resize((width,round(t.height*width/t.width)),Image.Resampling.LANCZOS)
 t=ImageEnhance.Sharpness(t).enhance(1.15)
 t.save(p)
(root/'work/reports/150_scan007/crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
(root/'work/reports/150_scan007/crop_rotations.json').write_text(json.dumps(rotations,indent=2)+'\n')
print(f'{len(boxes)} crops created')
