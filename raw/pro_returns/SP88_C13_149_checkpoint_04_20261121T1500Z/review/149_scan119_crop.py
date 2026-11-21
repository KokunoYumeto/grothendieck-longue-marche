"""Reproduce the one first-reading crop per hard place on scan119; no OCR."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan119/full.jpg'
DEST = ROOT / 'edition/crops'
# Original-image coordinates; rotation is clockwise where negative in Pillow.
CROPS = {
    'p01': ([1165, 38, 1540, 145], 0),
    'p02': ([335, 142, 1490, 285], 0),
    'p03': ([343, 274, 1630, 395], 0),
    'p04': ([337, 398, 1300, 499], 0),
    'p05': ([1305, 363, 1670, 508], 0),
    'p06': ([340, 500, 1535, 609], 0),
    'p07': ([333, 560, 1630, 730], 0),
    'p08': ([325, 738, 1540, 861], 0),
    'p09': ([314, 862, 1505, 986], 0),
    'p10': ([308, 951, 1520, 1081], 0),
    'p11': ([307, 1081, 1265, 1177], 0),
    'p12': ([278, 1177, 1665, 1506], 0),
    'p13': ([939, 1395, 1657, 1746], 0),
    'p14': ([20, 1243, 671, 1879], -25),
    'p15': ([260, 1735, 1660, 1849], 0),
    'p16': ([653, 1829, 885, 1898], 0),
    'p17': ([233, 1871, 352, 1940], 0),
    'p18': ([250, 1869, 1662, 2106], 0),
    'p19': ([278, 2040, 1648, 2322], 0),
    'p20': ([18, 1932, 260, 2345], 0),
    'p21': ([785, 25, 855, 85], 0),
}

if __name__ == '__main__':
    image = Image.open(SOURCE).convert('RGB')
    DEST.mkdir(parents=True, exist_ok=True)
    for place, (bbox, angle) in CROPS.items():
        target = DEST / f'149_scan119_{place}.png'
        if target.exists():
            raise FileExistsError(f'Refusing to overwrite inspected crop: {target}')
        crop = ImageOps.autocontrast(image.crop(bbox), cutoff=0.5)
        if angle:
            crop = crop.rotate(angle, Image.Resampling.BICUBIC, expand=True, fillcolor='white')
        width = 2800
        crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
        crop = crop.filter(ImageFilter.UnsharpMask(radius=1, percent=110, threshold=4))
        crop.save(target)
        print(place, bbox, angle, target.name)
