"""Create retained visual-reading crops for statement L607 on scan 36/24."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan024.jpg"
CROPS = [
    ("36_scan024_L607_inequality_context.png", (240, 1490, 1640, 1690)),
    ("36_scan024_L607_inequality_detail.png", (765, 1600, 1030, 1688)),
    ("36_scan024_L607_comparison_signs.png", (460, 1185, 925, 1325)),
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
