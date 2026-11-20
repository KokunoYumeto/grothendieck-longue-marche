"""Create retained visual-reading crops for statement L1548 on scan 39/20."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/39_scan020.jpg"
CROPS = [
    ("39_scan020_L1548_final_formula.png", (645, 1765, 1470, 1900)),
    ("39_scan020_L1548_alpha_coefficient.png", (1070, 1780, 1470, 1885)),
    ("39_scan020_L1548_deleted_coefficient.png", (745, 1800, 885, 1890)),
    ("39_scan020_L1548_index_comparison.png", (955, 55, 1410, 170)),
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
