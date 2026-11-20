from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

BASE = Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE = BASE / 'assignments/6_scan032/scan.jpg'
DEST = BASE / 'deliverables/crops'
DEST.mkdir(parents=True, exist_ok=True)
# Coordinates are from manual inspection of the 1809 x 2282 scan.
CROPS = {
    '6_scan032_L705_setup.jpg': (220, 572, 1788, 990),
    '6_scan032_L705_lifting_filtration.jpg': (220, 930, 1788, 1280),
    '6_scan032_H0504_upper.jpg': (0, 105, 1809, 640),
    '6_scan032_H0504_middle.jpg': (0, 600, 1809, 1130),
    '6_scan032_H0504_lower.jpg': (0, 1080, 1809, 1630),
    '6_scan032_H0504_bottom_margin.jpg': (0, 1570, 1809, 2282),
}
with Image.open(SOURCE) as source:
    for name, box in CROPS.items():
        crop = ImageOps.autocontrast(source.crop(box).convert('RGB'), cutoff=0.5)
        crop = ImageEnhance.Contrast(crop).enhance(1.45)
        crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
        crop.save(DEST / name, quality=96)
        print(name, box, crop.size)
