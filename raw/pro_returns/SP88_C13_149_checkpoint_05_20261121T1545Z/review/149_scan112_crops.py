from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan112/full.jpg'
BOXES = {
    'p01': (326, 15, 1643, 194),
    'p02': (304, 175, 1640, 336),
    'p03': (265, 352, 1368, 475),
    'p04': (300, 426, 1523, 663),
    'p05': (75, 740, 666, 1140),
    'p06': (410, 895, 1419, 1020),
    'p07': (848, 1006, 1630, 1141),
    'p08': (304, 1120, 1589, 1314),
    'p09': (315, 1300, 1490, 1424),
    'p10': (318, 1418, 1597, 1541),
    'p11': (318, 1544, 1643, 1689),
    'p12': (299, 1667, 1570, 1842),
    'p13': (272, 1870, 1513, 2095),
    'p14': (281, 2100, 1646, 2329),
    'p15': (18, 2290, 96, 2350),
}

def save_crop(key, box):
    target = ROOT / f'edition/crops/149_scan112_{key}.png'
    if target.exists():
        raise FileExistsError(f'Refusing to overwrite previously saved crop: {target}')
    with Image.open(SOURCE) as source:
        crop = ImageOps.autocontrast(source.crop(box).convert('L'), cutoff=1)
    width = max(1800, min(2600, crop.width * 3))
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=125, threshold=2))
    crop.save(target)

if __name__ == '__main__':
    for key, box in BOXES.items():
        save_crop(key, box)
    print(f'Saved {len(BOXES)} distinct contextual crops.')
