"""Create retained visual-reading crops for statement L612 on scan 36/40."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan040.jpg"
CROPS = [
    ("36_scan040_L612_margin_question.png", (25, 290, 520, 795)),
    ("36_scan040_L612_vanishing_scope.png", (25, 575, 305, 790)),
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
