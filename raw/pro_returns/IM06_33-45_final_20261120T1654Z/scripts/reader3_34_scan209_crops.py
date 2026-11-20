"""Create retained visual-reading crops for statement L630 on scan 34/209."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/34_scan209.jpg"
CROPS = [
    ("34_scan209_L630_absolute_values_statement.png", (285, 1020, 1675, 1380)),
    ("34_scan209_L630_power_detail.png", (945, 1150, 1680, 1280)),
]

image = Image.open(SOURCE)
(ROOT / "crops").mkdir(exist_ok=True)
for filename, box in CROPS:
    crop = ImageEnhance.Contrast(image.crop(box)).enhance(1.25)
    crop = crop.resize(
        (2600, round(crop.height * 2600 / crop.width)), Image.Resampling.LANCZOS
    )
    crop.save(ROOT / "crops" / filename)
    print(f"crops/{filename}")
