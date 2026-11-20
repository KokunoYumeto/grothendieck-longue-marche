"""Retain the group-name and statement crops for L926 on scan 45/20."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/45_scan020.jpg"
CROPS = [
    ("45_scan020_L926_group_name.png", (820, 505, 1090, 610)),
    ("45_scan020_L926_statement.png", (485, 505, 1680, 700)),
    ("45_scan020_L926_earlier_example.png", (790, 260, 1060, 350)),
    ("45_scan020_L926_injective_radicial.png", (65, 420, 1290, 715)),
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
