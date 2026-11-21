from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan126/full.jpg'
BOXES = {
    'p01': (276, 70, 1655, 270),
    'p02': (315, 232, 1625, 355),
    'p03': (275, 350, 1633, 483),
    'p04': (610, 650, 972, 811),
    'p05': (1010, 762, 1645, 1029),
    'p06': (865, 1022, 1562, 1155),
    'p07': (250, 1287, 1634, 1570),
    'p08': (17, 80, 335, 555),
    'p09': (250, 1578, 1624, 1862),
    'p10': (255, 1810, 1655, 2151),
    'p11': (250, 2136, 1664, 2346),
    'p12': (16, 2305, 97, 2346),
    'p13': (1205, 320, 1635, 435),
    'p14': (1250, 230, 1625, 330),
    'p15': (250, 2095, 1664, 2346),
}
ROTATIONS = {'p08': -30}

def save_crop(key, box):
    target = ROOT / f'edition/crops/149_scan126_{key}.png'
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(target)
    with Image.open(SOURCE) as source:
        im = ImageOps.autocontrast(source.crop(box).convert('L'), cutoff=1)
    if key in ROTATIONS:
        im = im.rotate(ROTATIONS[key], resample=Image.Resampling.BICUBIC,
                       expand=True, fillcolor=255)
    width = max(1800, min(2600, im.width * 3))
    im = im.resize((width, round(im.height * width / im.width)), Image.Resampling.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=125, threshold=2))
    im.save(target)

if __name__ == '__main__':
    for key, box in BOXES.items():
        save_crop(key, box)
        print(key, box, ROTATIONS.get(key, 0))
