"""Audit-only supplements for independently reported clipped box edges.

No recognition. The frozen box lists and readings remain untouched.
"""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json, hashlib

R = Path(__file__).resolve().parents[1]
source = R.parent / 'source/SP84_C13_149_scans/149_scan027.jpg'
specs = [
    ('b12_b14', (310, 925, 1635, 1220), 'Complete named functions and both map lines; original b12 and b14 clipped glyphs at their vertical boundaries.'),
    ('b15', (310, 1225, 1635, 1440), 'Complete terminal equality and its preceding line; original b15 clipped the upper portions of the formula.'),
]
source_image = Image.open(source).convert('RGB')
rows = []
for name, box, reason in specs:
    destination = R / f'crops/149_scan027_second_{name}_supplement.png'
    assert not destination.exists(), destination
    im = ImageOps.autocontrast(source_image.crop(box), cutoff=0.5)
    im = im.resize((3000, round(im.height * 3000 / im.width)), Image.Resampling.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3))
    im.save(destination)
    rows.append(dict(crop=str(destination.relative_to(R)), box=list(box), reason=reason,
                     source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                     crop_sha256=hashlib.sha256(destination.read_bytes()).hexdigest(),
                     method='RGB crop; autocontrast cutoff0.5; LANCZOS3000wide; unsharp1.5/120/3; no OCR'))
(R / 'documentation/scan027_supplement_crops.json').write_text(json.dumps(rows, indent=2)+'\n')
print(json.dumps(rows, indent=2))
