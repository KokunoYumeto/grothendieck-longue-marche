from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

base = Path('/workspace/scratch/94548b74fbe0')
out = base / 'out/readers/008/B'
source = base / 'source/SP40_CW_81_scans/J81-01_81_scan008.jpg'
items = [
 ('01_top_cancel.png', (1124,196,1393,278), 2400, 'Cancelled comparison after q-i-1'),
 ('02_isolated_cancel.png', (90,379,483,453), 2600, 'First isolated struck line'),
 ('03_parenthesis_cancel.png', (877,579,1358,709), 2800, 'Two-line parenthesis and its cancellation paths'),
 ('04_zeta.png', (548,880,1160,978), 3200, 'Second existential letter and repeated exponent'),
 ('05_a_overmark.png', (456,959,849,1043), 2600, 'Detached mark above a in et si a=...'),
 ('06_a_subscript.png', (403,1052,652,1135), 2400, 'Cancelled subscript below a prime'),
 ('07_hypothesis_accent.png', (226,1320,637,1406), 2700, 'Accent in first hypothese occurrence'),
 ('08_lower_alors.png', (313,1387,775,1455), 3000, 'Cancelled word before on a'),
 ('09_pale_formula.png', (760,1382,1014,1457), 2400, 'Pale addition p=q, a-prime/alpha-prime=gamma'),
 ('10_lower_p.png', (92,1454,550,1535), 3000, 'Cancelled predecessor before q squared'),
 ('11_lower_cancellations.png', (452,1458,835,1595), 3000, 'Two ou p=1 cancellations and pale absurde addition'),
 ('12_final_gamma.png', (199,1579,735,1699), 3200, 'Cancelled q and raised q alpha minus 1'),
 ('13_final_accent.png', (1017,1581,1342,1687), 2600, 'Accent and endpoint in final parenthesis'),
 ('14_right_note.png', (840,1446,1374,1646), 3000, 'Right note spelling and return arrow'),
 ('15_upper_right_trace.png', (1322,18,1385,91), 2400, 'Mottled upper-right trace inspected for a possible character'),
]
im = Image.open(source)
manifest = []
for name, box, width, purpose in items:
    crop = ImageOps.autocontrast(im.crop(box))
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.1, percent=120, threshold=3))
    crop.save(out / name)
    manifest.append({'path':name,'bbox':list(box),'rotation':0,'purpose':purpose})
(out / 'crop_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(manifest, ensure_ascii=False))
