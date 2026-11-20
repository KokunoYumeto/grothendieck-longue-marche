"""Retain shift-reading crops for L933 on manuscript scan 43/140."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/43_scan140.jpg"
CROPS = [
    ("43_scan140_L933_box.png", (1110, 1700, 1660, 1880)),
    ("43_scan140_L933_left_degree.png", (1160, 1735, 1445, 1845)),
    ("43_scan140_L933_repeated_degree.png", (875, 1835, 1270, 1970)),
    ("43_scan140_L933_comparison.png", (380, 1600, 1095, 1845)),
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
