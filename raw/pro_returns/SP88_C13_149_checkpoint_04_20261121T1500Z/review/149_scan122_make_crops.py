from pathlib import Path
import json
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan122/full.jpg'
TARGET = ROOT / 'edition/crops'
TARGET.mkdir(parents=True, exist_ok=True)

# Coordinates refer to the original 1681 x 2365 image.  No OCR is used.
PLAN = [
    ('p01', [310, 60, 1625, 177], 2.2, 0, 'opening line and complete mapping formula'),
    ('p02', [315, 175, 1645, 305], 2.2, 0, 'aux jauges line, including the disputed short form'),
    ('p03', [305, 560, 1665, 1080], 2.1, 0, 'second paragraph with cancelled tout and full inserted clause'),
    ('p04', [15, 1080, 1665, 1755], 1.9, 0, 'complete Proposition block, marginal rule and oblique note'),
    ('p05', [18, 1080, 365, 1735], 3.0, -40, 'still-open oblique marginal note, rotated for reading'),
    ('p06', [280, 1735, 1650, 2090], 2.2, 0, 'proof opening with both inserted letter/word baselines and complete formulas'),
    ('p07', [280, 2050, 1650, 2355], 2.2, 0, 'proof ending: cancellations, replacement insertion and final line'),
    ('p08', [18, 2310, 115, 2355], 9.0, 0, 'thin foliation 121'),
    ('p09', [940, 690, 1665, 895], 3.7, 0, 'still-open inserted est/soit and altered upper closing mark'),
    ('p10', [630, 1060, 1655, 1215], 2.8, 0, 'incomplete-view repair: full upper curls of Proposition formula clipped in p04'),
    ('p11', [280, 1705, 1650, 2355], 2.2, 0, 'incomplete-view repair: full proof opening ascenders clipped in p06, with all proof context'),
]

im = Image.open(SOURCE).convert('RGB')
assert im.size == (1681, 2365)
manifest = []
for place, box, scale, angle, purpose in PLAN:
    path = TARGET / f'149_scan122_{place}.png'
    if path.exists():
        with Image.open(path) as saved:
            manifest.append({'id': place, 'bbox': box, 'scale': scale, 'rotation_degrees': angle,
                             'purpose': purpose, 'file': f'crops/{path.name}', 'size': list(saved.size)})
        continue
    out = ImageOps.autocontrast(im.crop(tuple(box)), cutoff=0.4)
    out = out.resize((round(out.width * scale), round(out.height * scale)), Image.Resampling.LANCZOS)
    if angle:
        out = out.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    out = ImageEnhance.Contrast(out).enhance(1.12)
    out = out.filter(ImageFilter.UnsharpMask(radius=1.2, percent=90, threshold=3))
    out.save(path)
    manifest.append({'id': place, 'bbox': box, 'scale': scale, 'rotation_degrees': angle,
                     'purpose': purpose, 'file': f'crops/{path.name}', 'size': list(out.size)})
(ROOT / 'edition/review/149_scan122_crop_geometry.json').write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'saved': len(manifest), 'source_size': list(im.size), 'crops': manifest}, ensure_ascii=False))
