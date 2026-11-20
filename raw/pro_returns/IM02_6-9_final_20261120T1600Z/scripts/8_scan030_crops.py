from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

BASE = Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE = BASE / 'assignments/8_scan030/scan.jpg'
OUT = BASE / 'deliverables/crops'
CROPS = {
    '8_scan030_L742_chart_definition.jpg': (750, 480, 1650, 930),
    '8_scan030_L742_family_classes.jpg': (25, 890, 1440, 1350),
}

OUT.mkdir(parents=True, exist_ok=True)
with Image.open(SOURCE) as original:
    for name, box in CROPS.items():
        crop = original.crop(box).convert('RGB')
        crop = ImageOps.autocontrast(crop, cutoff=0.5)
        crop = ImageEnhance.Contrast(crop).enhance(1.5)
        crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
        crop.save(OUT / name, quality=96)
        print(name, crop.size)
