"""Create retained visual-reading crops for statement L609 on scan 36/16."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan016.jpg"
CROPS = [
    ("36_scan016_L609_hodge_exponent.png", (195, 1490, 1640, 1705)),
    ("36_scan016_L609_E_definition.png", (195, 925, 650, 1005)),
    ("36_scan016_L609_inclusion_context.png", (1180, 350, 1635, 435)),
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
