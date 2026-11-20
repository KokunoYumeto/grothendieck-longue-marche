"""Create retained visual-reading crops for statement L611 on scan 36/39."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan039.jpg"
CROPS = [
    ("36_scan039_L611_bottom_sequence.png", (355, 1980, 1665, 2100)),
    ("36_scan039_L611_bottom_Q.png", (840, 1985, 1095, 2085)),
    ("36_scan039_L611_first_limit_comparison.png", (455, 1310, 1050, 1430)),
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
