from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
SOURCE = ROOT / 'packets/149_scan113/full.jpg'
DEST = ROOT / 'edition/crops'
BOXES = {
    'p01': (770, 29, 847, 87),
    'p02': (295, 93, 950, 185),
    'p03': (980, 55, 1569, 195),
    'p04': (290, 196, 1652, 329),
    'p05': (281, 331, 1543, 446),
    'p06': (289, 473, 737, 539),
    'p07': (267, 535, 1140, 901),
    'p08': (244, 947, 609, 1041),
    'p09': (735, 921, 1575, 1060),
    'p10': (252, 1041, 1642, 1193),
    'p11': (260, 1183, 1609, 1325),
    'p12': (247, 1483, 1615, 1755),
    'p13': (255, 1744, 1615, 1909),
    'p14': (250, 2012, 1397, 2152),
    'p15': (257, 2146, 1598, 2290),
    'p16': (21, 2304, 105, 2352),
}

if __name__ == '__main__':
    source = Image.open(SOURCE).convert('RGB')
    DEST.mkdir(exist_ok=True)
    for place, bbox in BOXES.items():
        target = DEST / f'149_scan113_{place}.png'
        if target.exists():
            raise FileExistsError(f'Refusing to regenerate existing crop: {target}')
        crop = ImageOps.autocontrast(source.crop(bbox), cutoff=0.5)
        scale = 2800 / crop.width
        crop = crop.resize((2800, round(crop.height * scale)), Image.Resampling.LANCZOS)
        crop = crop.filter(ImageFilter.UnsharpMask(radius=1, percent=110, threshold=4))
        crop.save(target)
        print(place, list(bbox), str(target))
