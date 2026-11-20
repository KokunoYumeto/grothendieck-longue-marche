from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/40_scan023.jpg"
CONTRAST = 1.25
CROPS = [
    ("40_scan023_L591_open_step.png", (245, 1220, 1640, 1510), 2800),
]

image = Image.open(SOURCE)
for name, box, output_width in CROPS:
    crop = ImageEnhance.Contrast(image.crop(box)).enhance(CONTRAST)
    crop = crop.resize(
        (output_width, round(crop.height * output_width / crop.width)),
        Image.Resampling.LANCZOS,
    )
    target = ROOT / "crops" / name
    target.parent.mkdir(exist_ok=True)
    crop.save(target)
    print(name, box, crop.size)
