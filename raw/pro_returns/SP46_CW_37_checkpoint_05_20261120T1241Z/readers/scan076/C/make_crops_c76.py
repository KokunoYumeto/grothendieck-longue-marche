from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json

ROOT = Path('/workspace/scratch/006c0e32b2af/out/readers/scan076/C')
SOURCE = Path('/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan076.jpg')
OPEN = [
 ('c76_01_transition.jpg', [480,367,658,443], 0, 'First transition glyph and lowered ij; eta/n/gamma doubt.'),
 ('c76_02_source_index.jpg', [932,364,1101,445], 0, 'Retraced subscript under the source primed U.'),
 ('c76_03_target_index.jpg', [1202,364,1393,446], 0, 'Retraced subscript under the target primed U.'),
 ('c76_04_tels_correction.jpg', [935,452,1055,516], 0, 'Possible cancelled d beneath the initial t of tels.'),
 ('c76_05_donne.jpg', [1374,454,1480,512], 0, 'Final letters and accent in donne/donnee.'),
 ('c76_06_rmq_heading.jpg', [304,959,417,1023], 0, 'Detached terminal character after underlined Rmq.'),
 ('c76_07_cancelled_heading.jpg', [300,1035,420,1103], 0, 'Read all surviving letters of the cancelled second remark heading.'),
 ('c76_08_signature_initial.jpg', [811,1204,970,1288], -18, 'Small slanted signature initial and exact signature letters.'),
 ('c76_09_detached_pair.jpg', [1388,1366,1430,1402], 0, 'Shape and placement of detached marginal points; punctuation or incidental origin unresolved.'),
]
image = Image.open(SOURCE).convert('RGB')
rows = []
for name, bbox, rotation, reason in OPEN:
    crop = image.crop(bbox)
    if rotation:
        crop = crop.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    crop = ImageOps.autocontrast(crop, cutoff=0.3)
    width = 2400
    crop = crop.resize((width, round(crop.height*width/crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.1, percent=90, threshold=3))
    crop.save(ROOT/name, quality=96, subsampling=0)
    rows.append({'file': str(ROOT/name), 'source': str(SOURCE), 'bbox': bbox, 'rotation': rotation, 'reason': reason, 'processing': 'RGB; autocontrast cutoff 0.3%; LANCZOS width 2400; UnsharpMask radius 1.1, percent 90, threshold 3', 'requested_deliveries': 0, 'actual_visual_views': 0})
(ROOT/'crop_manifest_c76.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'created': len(rows), 'manifest': str(ROOT/'crop_manifest_c76.json')}, ensure_ascii=False))
