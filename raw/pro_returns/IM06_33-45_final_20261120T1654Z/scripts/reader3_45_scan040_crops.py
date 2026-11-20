"""Retain the hypothesis and vanishing-question crops for L893 on scan 45/40."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/45_scan040.jpg"
CROPS = [
    ("45_scan040_L893_hypotheses.png", (470, 1920, 1680, 2025)),
    ("45_scan040_L893_vanishing_question.png", (340, 2020, 1100, 2150)),
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
