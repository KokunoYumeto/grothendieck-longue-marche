import json
from pathlib import Path
from PIL import Image,ImageOps,ImageEnhance,ImageFilter
p=Path('/workspace/scratch/4644e52611c0')
im=Image.open(p/'source/SP84_C13_149_scans/149_scan014.jpg')
boxes={
'c01':[302,176,1251,296],
'c02':[318,68,694,172],
'c03':[303,408,513,482],
'c04':[980,442,1638,571],
'c05':[33,598,256,757],
'c06':[314,674,1553,786],
'c07':[523,798,901,907],
'c08':[1404,779,1625,879],
'c09':[1322,555,1642,637],
'c10':[316,1008,980,1149],
'c11':[588,1347,1369,1500],
'c12':[1090,1478,1644,1604],
'c13':[895,1624,1201,1750],
'c14':[1230,1608,1634,1724],
'c15':[979,1752,1458,1890],
'c16':[858,1875,1436,2004],
'c17':[328,2039,607,2161],
'c18':[928,2022,1315,2139],
'c19':[429,2154,723,2254],
'c20':[24,2298,74,2348]
}
for k,b in boxes.items():
 crop=ImageOps.autocontrast(im.crop(b))
 if k=='c05': crop=crop.rotate(-30,expand=True,fillcolor='white')
 crop=crop.resize((2900,round(crop.height*2900/crop.width)),Image.Resampling.LANCZOS)
 crop=ImageEnhance.Contrast(crop).enhance(1.1).filter(ImageFilter.UnsharpMask(radius=1.1,percent=105,threshold=3))
 crop.save(p/f'edition/crops/149_scan014_{k}.png')
Path('/tmp/reader_b_014_boxes.json').write_text(json.dumps(boxes))
print('Created 20 crops; c05 rotated 30 degrees clockwise for reading. All stored boxes are original-image coordinates.')
