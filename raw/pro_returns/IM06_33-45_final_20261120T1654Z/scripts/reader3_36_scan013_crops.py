"""Create retained visual-reading crops for the three o/0 loci on scan 36/13.

Q100034 and Qsow034 are two review rows for the same double-prime occurrence.
"""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan013.jpg"
CROPS = [
    ("36_scan013_Q100034_Qsow034_double_prime.png", (575, 1735, 980, 1820)),
    ("36_scan013_Qsow188_plain.png", (1015, 1240, 1410, 1330)),
    ("36_scan013_Qsow195_prime.png", (180, 1735, 565, 1820)),
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
