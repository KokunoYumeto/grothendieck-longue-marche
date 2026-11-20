"""Retain crops for the degree comparisons in L932 on manuscript scan 43/114."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/43_scan114.jpg"
CROPS = [
    ("43_scan114_L932_top_box.png", (260, 350, 1510, 565)),
    ("43_scan114_L932_final_sequence.png", (180, 1920, 1650, 2110)),
    ("43_scan114_L932_sequence_left.png", (280, 1935, 670, 2110)),
    ("43_scan114_L932_sequence_middle.png", (650, 1925, 990, 2070)),
    ("43_scan114_L932_sequence_right.png", (1020, 1910, 1650, 2100)),
    ("43_scan114_L932_later_duality_box.png", (200, 1350, 1580, 1525)),
    ("43_scan114_L932_shift_box.png", (120, 1135, 1715, 1370)),
    ("43_scan114_L932_spectral_box.png", (280, 1730, 1570, 1950)),
    ("43_scan114_L932_degree_comparison.png", (920, 945, 1450, 1100)),
    ("43_scan114_L932_lower_comparison.png", (205, 1600, 1190, 1730)),
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
