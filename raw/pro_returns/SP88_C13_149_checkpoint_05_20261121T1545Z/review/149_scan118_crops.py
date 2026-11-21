from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan118/full.jpg'
BOXES = {
    'p01': (307, 407, 1310, 549),
    'p02': (22, 533, 288, 902),
    'p03': (278, 554, 1230, 682),
    'p04': (271, 716, 1637, 953),
    'p05': (285, 948, 1610, 1088),
    'p06': (22, 978, 336, 1406),
    'p07': (271, 1080, 1545, 1239),
    'p08': (265, 1235, 1544, 1486),
    'p09': (263, 1494, 1253, 1642),
    'p10': (269, 1647, 1338, 1783),
    'p11': (263, 1755, 1655, 2140),
    'p12': (251, 2084, 1572, 2336),
    'p13': (16, 2306, 100, 2352),
    'p14': (22, 527, 318, 902),
    'p15': (1026, 1841, 1654, 2124),
    'p16': (246, 2228, 584, 2338),
}
ROTATIONS = {'p02': -35, 'p06': -38, 'p14': -35}

def save_crop(key, box):
    target = ROOT / f'edition/crops/149_scan118_{key}.png'
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(target)
    with Image.open(SOURCE) as source:
        crop = ImageOps.autocontrast(source.crop(box).convert('L'), cutoff=1)
    if key in ROTATIONS:
        crop = crop.rotate(ROTATIONS[key], resample=Image.Resampling.BICUBIC, expand=True, fillcolor=255)
    width = max(1800, min(2600, crop.width * 3))
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop = crop.filter(ImageFilter.UnsharpMask(radius=1.2, percent=125, threshold=2))
    crop.save(target)

if __name__ == '__main__':
    for key, box in BOXES.items():
        save_crop(key, box)
        print(key, box, ROTATIONS.get(key, 0))
