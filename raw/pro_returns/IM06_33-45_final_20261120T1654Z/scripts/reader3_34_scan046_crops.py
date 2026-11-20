"""Create retained visual-reading crops for statement L623 on scan 34/46."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/34_scan046.jpg"
CROPS = [
    ("34_scan046_L623_sequence.png", (450, 1945, 1665, 2050)),
    ("34_scan046_L623_first_term.png", (580, 1955, 875, 2050)),
    ("34_scan046_L623_open_closed_context.png", (285, 1770, 1610, 1945)),
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
