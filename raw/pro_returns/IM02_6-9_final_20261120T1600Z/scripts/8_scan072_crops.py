from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps

BASE = Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE = BASE / 'assignments/8_scan072/scan.jpg'
OUT = BASE / 'deliverables/crops'
# Fractional crop boxes refer to the image after a 180-degree rotation.
CROPS = {
    '8_scan072_L743_number_and_convolution.jpg': (0.16, 0.10, 0.98, 0.49),
    '8_scan072_L743_bourbaki_note.jpg': (0.16, 0.77, 0.98, 0.97),
}

OUT.mkdir(parents=True, exist_ok=True)
with Image.open(SOURCE) as source:
    original = source.convert('RGB').rotate(180, expand=True)
    print('source dimensions', original.size)
    for name, fractional_box in CROPS.items():
        box = tuple(round(v * (original.width if i % 2 == 0 else original.height))
                    for i, v in enumerate(fractional_box))
        crop = original.crop(box)
        crop = ImageOps.autocontrast(crop, cutoff=0.5)
        crop = ImageEnhance.Contrast(crop).enhance(1.5)
        crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
        crop.save(OUT / name, quality=96)
        print(name, 'box', box, 'size', crop.size)
