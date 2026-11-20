from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

BASE = Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE = BASE / 'assignments/9_scan007/scan.jpg'
OUT = BASE / 'deliverables/crops'
CROPS = {
    '9_scan007_L769_quotient_exponents.jpg': (330, 140, 750, 255),
    '9_scan007_L769_Wn_dualizing_functor.jpg': (85, 1035, 1145, 1375),
    '9_scan007_L769_final_isomorphism.jpg': (230, 1650, 1030, 1808),
}

OUT.mkdir(parents=True, exist_ok=True)
with Image.open(SOURCE) as original:
    print('source dimensions', original.size)
    for name, box in CROPS.items():
        crop = original.crop(box).convert('RGB')
        crop = ImageOps.autocontrast(crop, cutoff=0.5)
        crop = ImageEnhance.Contrast(crop).enhance(1.7)
        crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
        crop.save(OUT / name, quality=96)
        print(name, 'box', box, 'size', crop.size)
