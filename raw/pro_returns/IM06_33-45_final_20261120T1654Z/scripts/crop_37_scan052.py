from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/37_scan052.jpg"
CONTRAST = 1.25
CROPS = [
    ("37_scan052_Q100011_Qsow011_arrow.png", (735, 1405, 965, 1500), 2600),
    ("37_scan052_Q100011_Qsow011_context.png", (530, 1400, 1585, 1535), 2600),
]

image = Image.open(SOURCE)
print("source dimensions:", image.size)
for name, box, output_width in CROPS:
    crop = ImageEnhance.Contrast(image.crop(box)).enhance(CONTRAST)
    crop = crop.resize((output_width, round(crop.height * output_width / crop.width)), Image.Resampling.LANCZOS)
    target = ROOT / "crops" / name
    target.parent.mkdir(exist_ok=True)
    crop.save(target)
    print(name, box, crop.size)
