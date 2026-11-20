"""Create retained visual-reading crops for statement Q100064 on scan 37/3."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/37_scan003.jpg"
CROPS = [
    ("37_scan003_Q100064_overstruck_word.png", (865, 1620, 1190, 1680)),
    ("37_scan003_Q100064_clean_comparison.png", (495, 1730, 800, 1785)),
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
