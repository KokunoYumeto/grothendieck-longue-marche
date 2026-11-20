from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

BASE = Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE = BASE / 'assignments/8_scan035/scan.jpg'
OUT = BASE / 'deliverables/crops'
# Coordinates below refer to the scan after a 180-degree rotation, since the
# typescript is upside down in the supplied image.
CROPS = {
    '8_scan035_L742_number_and_page.jpg': (150, 115, 1580, 425),
    '8_scan035_L742_jets_section.jpg': (150, 430, 1640, 1110),
}

OUT.mkdir(parents=True, exist_ok=True)
with Image.open(SOURCE) as source:
    original = source.convert('RGB').rotate(180, expand=True)
    print('source dimensions', source.size)
    for name, box in CROPS.items():
        crop = original.crop(box)
        crop = ImageOps.autocontrast(crop, cutoff=0.5)
        crop = ImageEnhance.Contrast(crop).enhance(1.5)
        crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
        crop.save(OUT / name, quality=96)
        print(name, crop.size)
