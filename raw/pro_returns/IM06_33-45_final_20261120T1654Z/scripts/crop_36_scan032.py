from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan032.jpg"
CONTRAST = 1.25
# Boxes are in the original, upside-down source image; crop first, then rotate 180 degrees.
CROPS = [
    ("36_scan032_L610_last_pair.png", (20, 30, 1010, 155), 2600),
    ("36_scan032_L610_previous_pair.png", (20, 245, 1010, 335), 2600),
]

image = Image.open(SOURCE)
print("source dimensions:", image.size)
image.rotate(180).save(ROOT / "crops/36_scan032_full_upright.png")
for name, box, output_width in CROPS:
    crop = ImageEnhance.Contrast(image.crop(box)).enhance(CONTRAST).rotate(180)
    crop = crop.resize((output_width, round(crop.height * output_width / crop.width)), Image.Resampling.LANCZOS)
    target = ROOT / "crops" / name
    target.parent.mkdir(exist_ok=True)
    crop.save(target)
    print(name, box, crop.size)
