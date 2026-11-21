from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
import sys

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan114'
BOXES = {
    'p01': ([347, 53, 1577, 195], 0),
    'p02': ([346, 191, 1655, 353], 0),
    'p03': ([426, 380, 1598, 590], 0),
    'p04': ([311, 599, 1648, 742], 0),
    'p05': ([314, 733, 1552, 884], 0),
    'p06': ([307, 880, 1511, 1025], 0),
    'p07': ([298, 980, 1520, 1146], 0),
    'p08': ([299, 1140, 1656, 1311], 0),
    'p09': ([301, 1279, 1531, 1423], 0),
    'p10': ([17, 1230, 405, 1968], -40),
    'p11': ([269, 1510, 1546, 1702], 0),
    'p12': ([270, 1830, 1541, 1976], 0),
    'p13': ([274, 2207, 1641, 2341], 0),
    'p14': ([17, 2300, 96, 2350], 0),
    'p15': ([274, 2120, 1641, 2341], 0),
    'p16': ([1240, 2070, 1648, 2341], 0),
}
image = Image.open(ROOT / 'packets' / PAGE / 'full.jpg')
selected = set(sys.argv[1:]) if len(sys.argv) > 1 else set(BOXES)
if selected - set(BOXES):
    raise ValueError(f'Unknown crop names: {selected - set(BOXES)}')
for place, (box, rotation) in BOXES.items():
    if place not in selected:
        continue
    out = ROOT / 'edition' / 'crops' / f'{PAGE}_{place}.png'
    if out.exists():
        raise RuntimeError(f'Refusing to overwrite an existing crop: {out}')
    cropped = ImageOps.autocontrast(image.crop(box).convert('RGB'))
    if rotation:
        cropped = cropped.rotate(rotation, Image.Resampling.BICUBIC,
                                 expand=True, fillcolor='white')
    cropped = cropped.resize((2400, round(cropped.height * 2400 / cropped.width)),
                             Image.Resampling.LANCZOS)
    cropped = cropped.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    cropped.save(out)
(ROOT / 'edition' / 'review' / f'{PAGE}_crop_boxes.json').write_text(
    json.dumps(BOXES, indent=2) + '\n')
print(f'Saved {len(selected)} crops for {PAGE}.')
