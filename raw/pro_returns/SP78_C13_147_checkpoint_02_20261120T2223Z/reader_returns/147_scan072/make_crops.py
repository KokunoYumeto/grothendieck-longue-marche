from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/ea90d891106a')
work=root/'SP78_C13_147_work'
im=Image.open(root/'runtime/packets/147_scan072/scan.jpg')
boxes={
 '01':[430,265,940,352],
 '02':[225,342,1085,510],
 '03':[1080,340,1676,859],
 '04':[310,794,1676,1035],
 '05':[440,986,1680,1117],
 '06':[300,1100,950,1190],
 '07':[1420,983,1682,1197],
 '08':[300,1190,1655,1303],
 '09':[278,1313,1644,1455],
 '10':[270,1443,1520,1562],
 '11':[260,1810,1679,2044],
 '12':[337,2050,1150,2321],
 '13':[26,2296,92,2344]
}
for k,box in boxes.items():
 p=work/'crops'/f'147_scan072_place{k}.png'
 assert not p.exists(),p
 c=ImageOps.autocontrast(im.crop(box), cutoff=.3)
 width=3000 if k not in ('01','06','07','13') else 2400
 c=c.resize((width,round(width*c.height/c.width)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1,percent=40,threshold=3))
 c.save(p)
(root/'SP78_C13_147_work/reader_returns/147_scan072/crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print(json.dumps({'crops':len(boxes),'paths':[str(work/'crops'/f'147_scan072_place{k}.png') for k in boxes]},indent=2))
