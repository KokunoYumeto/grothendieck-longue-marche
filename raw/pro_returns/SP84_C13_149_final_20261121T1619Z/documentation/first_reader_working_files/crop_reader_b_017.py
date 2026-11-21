import json
from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
p=Path('/workspace/scratch/4644e52611c0')
im=Image.open(p/'source/SP84_C13_149_scans/149_scan017.jpg')
boxes={
'c01':[643,70,1361,159],
'c02':[280,410,1546,608],
'c03':[398,873,1071,1014],
'c04':[1102,843,1584,1003],
'c05':[641,1104,914,1198],
'c06':[261,1318,990,1447],
'c07':[525,1467,835,1569],
'c08':[306,1587,786,1687],
'c09':[508,1686,793,1819],
'c10':[1070,1892,1633,2056],
'c11':[901,2079,1481,2197],
'c12':[27,2308,76,2345]
}
for name,box in boxes.items():
 c=ImageOps.autocontrast(im.crop(box))
 c=c.resize((2900,round(c.height*2900/c.width)),Image.Resampling.LANCZOS)
 c=ImageEnhance.Contrast(c).enhance(1.1).filter(ImageFilter.UnsharpMask(radius=1.1,percent=105,threshold=3))
 c.save(p/f'edition/crops/149_scan017_{name}.png')
Path('/tmp/reader_b_017_boxes.json').write_text(json.dumps(boxes))
print('Created 12 crops; paths and boxes will remain stable.')
