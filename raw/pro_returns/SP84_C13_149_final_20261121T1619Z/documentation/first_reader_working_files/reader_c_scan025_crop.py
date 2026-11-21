from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/4644e52611c0')
src=Image.open(root/'source/SP84_C13_149_scans/149_scan025.jpg')
boxes={
'c01':[1120,225,1585,335],
'c02':[280,340,1630,550],
'c03':[280,545,855,655],
'c04':[295,735,1020,870],
'c05':[280,855,710,945],
'c06':[300,925,1100,1045],
'c07':[295,1005,1630,1200],
'c08':[310,1295,790,1385],
'c09':[300,1380,1030,1495],
'c10':[570,1495,830,1610],
'c11':[1090,1430,1310,1590],
'c12':[545,1570,1210,1710],
'c13':[865,1670,1100,1785],
'c14':[575,1845,800,2015],
'c15':[535,2025,1250,2180],
'c16':[17,2285,100,2351]
}
for name, box in boxes.items():
    im=src.crop(box)
    im=ImageOps.autocontrast(im, cutoff=.5)
    w=2700
    im=im.resize((w, round(im.height*w/im.width)),Image.Resampling.LANCZOS)
    im=im.filter(ImageFilter.UnsharpMask(radius=1,percent=120,threshold=3))
    im.save(root/f'edition/crops/149_scan025_{name}.png')
(root/'work/reader_c_scan025_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
print(f'Saved {len(boxes)} crops; original dimensions {src.size}.')
