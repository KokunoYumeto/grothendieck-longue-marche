from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

BASE = Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE = BASE / 'assignments/8_scan046/scan.jpg'
OUT = BASE / 'deliverables/crops'
CROPS = {
    '8_scan046_L761_deformation_hypothesis.jpg': (260, 120, 1655, 675),
    '8_scan046_L761_divided_powers.jpg': (270, 265, 1260, 360),
}

OUT.mkdir(parents=True, exist_ok=True)
with Image.open(SOURCE) as original:
    print('source dimensions', original.size)
    for name, box in CROPS.items():
        crop = original.crop(box).convert('RGB')
        crop = ImageOps.autocontrast(crop, cutoff=0.5)
        crop = ImageEnhance.Contrast(crop).enhance(1.6)
        crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
        crop.save(OUT / name, quality=96)
        print(name, crop.size)
