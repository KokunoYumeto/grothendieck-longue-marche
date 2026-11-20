"""Create retained visual-reading crops for statement L618 on scan 34/10."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/34_scan010.jpg"
CROPS = [
    ("34_scan010_L618_galois_formula.png", (440, 910, 1662, 1040)),
    ("34_scan010_L618_extension_definition.png", (430, 215, 1065, 325)),
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
