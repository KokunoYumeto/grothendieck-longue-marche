from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path('/workspace/scratch/0cab6a548abb')
BOXES = {
    'p01': (872, 55, 1549, 179),
    'p02': (332, 133, 1518, 343),
    'p03': (328, 300, 1641, 452),
    'p04': (331, 439, 1625, 616),
    'p05': (325, 576, 1673, 723),
    'p06': (16, 48, 292, 435),
    'p07': (327, 730, 1574, 866),
    'p08': (313, 855, 1590, 985),
    'p09': (355, 981, 1148, 1122),
    'p10': (320, 1027, 497, 1134),
    'p11': (300, 1080, 1503, 1256),
    'p12': (319, 1278, 874, 1388),
    'p13': (292, 1391, 966, 1496),
    'p14': (297, 1505, 1590, 1630),
    'p15': (314, 1633, 1551, 1768),
    'p16': (305, 1762, 1474, 1887),
    'p17': (285, 1884, 1644, 2168),
    'p18': (263, 2151, 1622, 2348),
    'p19': (18, 2300, 94, 2354),
}

if __name__ == '__main__':
    source = Image.open(ROOT / 'packets/149_scan116/full.jpg').convert('RGB')
    for place, box in BOXES.items():
        path = ROOT / f'edition/crops/149_scan116_{place}.png'
        if path.exists():
            raise FileExistsError(f'Refusing to regenerate {path}')
        part = source.crop(box)
        if place == 'p06':
            part = part.rotate(-45, resample=Image.Resampling.BICUBIC,
                               expand=True, fillcolor='white')
        part = ImageOps.autocontrast(part, cutoff=0.5)
        ratio = 2800 / part.width
        part = part.resize((2800, round(part.height * ratio)),
                           Image.Resampling.LANCZOS)
        part = part.filter(ImageFilter.UnsharpMask(radius=1, percent=110, threshold=4))
        part.save(path)
        print(place, list(box), str(path))
