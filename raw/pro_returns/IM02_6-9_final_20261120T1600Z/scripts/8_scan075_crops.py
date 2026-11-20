from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

BASE = Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE = BASE / 'assignments/8_scan075/scan.jpg'
OUT = BASE / 'deliverables/crops'
CROPS = {
    '8_scan075_L755_first_tate_group.jpg': (210, 365, 1150, 480),
    '8_scan075_L755_second_tate_group.jpg': (215, 445, 1390, 570),
    '8_scan075_L755_tate_and_p_comparison.jpg': (200, 125, 1590, 430),
}

OUT.mkdir(parents=True, exist_ok=True)
with Image.open(SOURCE) as original:
    print('source dimensions', original.size)
    for name, box in CROPS.items():
        crop = original.crop(box).convert('RGB')
        crop = ImageOps.autocontrast(crop, cutoff=0.5)
        crop = ImageEnhance.Contrast(crop).enhance(1.5)
        crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
        crop.save(OUT / name, quality=96)
        print(name, 'box', box, 'size', crop.size)
