from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan115/full.jpg'
BOXES = {
    'p01': (802, 35, 886, 96),
    'p02': (817, 174, 1655, 302),
    'p03': (301, 423, 771, 571),
    'p04': (300, 519, 1558, 723),
    'p05': (309, 847, 1640, 1004),
    'p06': (294, 1004, 1568, 1144),
    'p07': (300, 1111, 1301, 1238),
    'p08': (414, 1267, 1090, 1434),
    'p09': (250, 1555, 1628, 1740),
    'p10': (250, 2005, 1648, 2304),
    'p11': (18, 2306, 102, 2354),
}

def save_crop(key, box):
    target = ROOT / f'edition/crops/149_scan115_{key}.png'
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(target)
    with Image.open(SOURCE) as source:
        crop = ImageOps.autocontrast(source.crop(box).convert('L'), cutoff=1)
    width = max(1800, min(2600, crop.width * 3))
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=125, threshold=2))
    crop.save(target)

if __name__ == '__main__':
    for key, box in BOXES.items():
        save_crop(key, box)
        print(key, box)
