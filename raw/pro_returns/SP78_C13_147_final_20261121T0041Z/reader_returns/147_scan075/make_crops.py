from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/ea90d891106a')
work=root/'SP78_C13_147_work'
im=Image.open(root/'runtime/packets/147_scan075/scan.jpg')
boxes={
 '01':[290,63,1650,175],
 '02':[295,158,1605,264],
 '03':[290,224,1675,355],
 '04':[1180,447,1650,545],
 '05':[294,635,1660,889],
 '06':[300,878,1670,1110],
 '07':[300,1088,1658,1203],
 '08':[296,1182,1570,1408],
 '09':[470,1308,1477,1506],
 '10':[305,1538,690,1633],
 '11':[700,1557,1268,1680],
 '12':[715,1718,1300,1814],
 '13':[305,1818,1676,1975],
 '14':[23,2295,89,2351]
}
for k,b in boxes.items():
 p=work/'crops'/f'147_scan075_place{k}.png'
 assert not p.exists(),p
 c=ImageOps.autocontrast(im.crop(b),cutoff=.3)
 width=2400 if k in ('04','10','14') else 3000
 c=c.resize((width,round(width*c.height/c.width)),Image.Resampling.LANCZOS)
 c=c.filter(ImageFilter.UnsharpMask(radius=1,percent=40,threshold=3))
 c.save(p)
(work/'reader_returns/147_scan075/crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print('Saved 14 crops: 147_scan075_place01.png through 147_scan075_place14.png')
