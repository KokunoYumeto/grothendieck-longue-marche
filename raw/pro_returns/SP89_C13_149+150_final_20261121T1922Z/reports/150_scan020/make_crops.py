from PIL import Image,ImageOps,ImageEnhance
from pathlib import Path
import json
r=Path('/workspace/scratch/8759b8008681')
im=Image.open(r/'source/SP89_C13_149+150_scans/150_scan020.jpg')
boxes={
'P00':[35,25,120,100],
'P01':[635,180,1420,305],
'P02':[655,390,910,510],
'P03':[1010,390,1145,490],
'P04':[1150,355,1595,495],
'P05':[320,490,1600,600],
'P06':[875,590,1665,745],
'P07':[330,725,1645,855],
'P08':[330,860,1595,965],
'P09':[1230,935,1660,1100],
'P10':[330,1060,1620,1195],
'P11':[335,1185,1645,1305],
'P12':[340,1295,1545,1415],
'P13':[340,1415,1550,1545],
'P14':[330,1535,1495,1735],
'P15':[340,1720,1630,1955],
'P16':[20,2280,90,2345]
}
for k,b in boxes.items():
 c=ImageOps.autocontrast(im.crop(b).convert('L'))
 w=1800 if k in ['P00','P16'] else 3000
 c=c.resize((w,round(c.height*w/c.width)),Image.Resampling.LANCZOS)
 c=ImageEnhance.Sharpness(c).enhance(1.12)
 c.save(r/f'work/crops/150_scan020_{k}.png')
(r/'work/reports/150_scan020/crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print('Saved',len(boxes),'crops and crop_boxes.json')
