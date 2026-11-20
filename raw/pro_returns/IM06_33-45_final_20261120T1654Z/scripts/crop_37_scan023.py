from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/37_scan023.jpg"
CONTRAST = 1.25
CROPS = [
    ("37_scan023_Qsow068_end_line.png", (1340, 1210, 1660, 1290), 2600),
    ("37_scan023_Qsow068_continuation.png", (235, 1285, 800, 1355), 2600),
    ("37_scan023_Qsow068_two_lines.png", (235, 1210, 1660, 1355), 2600),
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
