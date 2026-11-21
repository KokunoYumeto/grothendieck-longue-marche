from pathlib import Path
from PIL import Image,ImageOps
import json
p=Path('/workspace/scratch/4644e52611c0')
im=Image.open(p/'source/SP84_C13_149_scans/149_scan027.jpg').convert('RGB')
boxes={1:[705,66,1155,167],2:[1176,62,1600,169],3:[487,242,1051,354],4:[308,345,1395,468],5:[661,581,956,672],6:[315,756,1593,991],7:[1035,942,1607,1061],8:[318,1070,660,1205],9:[333,1427,596,1511],10:[20,1180,455,1795],11:[405,1480,1463,1605],12:[317,1700,850,1870],13:[1207,1780,1650,1930],14:[24,1800,278,2130],15:[291,1918,951,2072],16:[970,1897,1580,2061],17:[936,2012,1580,2145],18:[317,2105,985,2240],19:[872,2094,1650,2217],20:[313,2181,1650,2306],21:[318,2254,1643,2353],22:[20,2298,83,2356],23:[1272,706,1396,823]}
rot={10:-40,14:-40}
for n,b in boxes.items():
    q=ImageOps.autocontrast(im.crop(b),cutoff=.5)
    if n in rot:q=q.rotate(rot[n],Image.Resampling.BICUBIC,expand=True,fillcolor='white')
    q=q.resize((3000,round(q.height*3000/q.width)),Image.Resampling.LANCZOS)
    q.save(p/f'edition/crops/149_scan027_c{n:02d}.png')
(p/'work/149_scan027_reader_a_crop_boxes.json').write_text(json.dumps({'boxes':boxes,'rotations':rot},indent=2)+'\n')
print('Saved 23 scan027 crops and original-coordinate manifest.')
