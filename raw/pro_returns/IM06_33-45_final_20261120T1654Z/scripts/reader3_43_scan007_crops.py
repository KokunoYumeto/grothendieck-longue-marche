"""Create retained visual-reading crops for L939 on manuscript scan 43/7."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/43_scan007.jpg"
CROPS = [
    ("43_scan007_L939_chain.png", (260, 1240, 1750, 1365)),
    ("43_scan007_L939_quotient.png", (840, 1230, 1390, 1360)),
    ("43_scan007_L939_exact_sequence.png", (300, 880, 1450, 1025)),
    ("43_scan007_L939_units_definition.png", (280, 1370, 1740, 1535)),
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
