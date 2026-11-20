from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

root = Path('/workspace/scratch/94548b74fbe0')
source = root / 'source/SP40_CW_81_scans/J81-01_81_scan007.jpg'
dest = root / 'out/readers/007/C'
items = [
    ('01_top_cancel.png', [22, 18, 180, 94], 2600, 'Initial cancelled mark and adjoining Soit'),
    ('02_upper_comparison.png', [929, 408, 1212, 515], 2800, 'Upper parenthetical car q comparison 2'),
    ('03_numbered_sum.png', [271, 521, 958, 632], 3200, 'Numbered sum, small dot left of summation and complete indices'),
    ('04_pale_note.png', [1006, 961, 1326, 1053], 3200, 'Complete two-line pale note, initial character and word ending'),
    ('05_crowded_sum.png', [395, 1487, 991, 1590], 3200, 'Crowded penultimate summation, indices and extra local marks'),
    ('06_final_sum.png', [235, 1574, 1184, 1673], 3400, 'Final expression, small indices and detached mark'),
]
records=[]
for name, box, width, purpose in items:
    im = Image.open(source).crop(tuple(box))
    im = ImageOps.autocontrast(im)
    im = im.resize((width, round(im.height*width/im.width)), Image.Resampling.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.1,percent=120,threshold=3))
    im.save(dest/name)
    records.append({'path':name,'bbox':box,'rotation':0,'purpose':purpose})
print(json.dumps(records, indent=2))
