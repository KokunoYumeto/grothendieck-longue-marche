from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

BASE = Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE = BASE / 'assignments/8_scan061/scan.jpg'
OUT = BASE / 'deliverables/crops'
# Fractional boxes use only the dimensions of this assigned scan.
CROPS = {
    '8_scan061_L742_tannakian_heading.jpg': (0.16, 0.01, 0.99, 0.22),
    '8_scan061_L744_fibre_and_representations.jpg': (0.19, 0.64, 0.97, 0.996),
}

OUT.mkdir(parents=True, exist_ok=True)
with Image.open(SOURCE) as original:
    print('source dimensions', original.size)
    for name, fractional_box in CROPS.items():
        box = tuple(round(v * (original.width if i % 2 == 0 else original.height))
                    for i, v in enumerate(fractional_box))
        crop = original.crop(box).convert('RGB')
        crop = ImageOps.autocontrast(crop, cutoff=0.5)
        crop = ImageEnhance.Contrast(crop).enhance(1.5)
        crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
        crop.save(OUT / name, quality=96)
        print(name, 'box', box, 'size', crop.size)
