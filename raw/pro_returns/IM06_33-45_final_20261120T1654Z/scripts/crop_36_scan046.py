from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan046.jpg"
CONTRAST = 1.25
CROPS = [
    ("36_scan046_L613_torsion.png", (305, 1175, 1705, 1335), 2600),
    ("36_scan046_L613_kummer.png", (275, 975, 1705, 1150), 2600),
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
