from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/43_scan110.jpg"
CONTRAST = 1.25
CROPS = [
    ("43_scan110_L934_L1562_inegalite.png", (270, 1145, 1555, 1255), 2800),
    ("43_scan110_L1562_display.png", (700, 1090, 1235, 1165), 2600),
    ("43_scan110_L934_L1562_proof_equality.png", (275, 1640, 1590, 1820), 2800),
    ("43_scan110_L1562_same_page_comparison.png", (755, 647, 980, 710), 2400),
]

image = Image.open(SOURCE)
for name, box, output_width in CROPS:
    crop = ImageEnhance.Contrast(image.crop(box)).enhance(CONTRAST)
    crop = crop.resize(
        (output_width, round(crop.height * output_width / crop.width)),
        Image.Resampling.LANCZOS,
    )
    target = ROOT / "crops" / name
    target.parent.mkdir(exist_ok=True)
    crop.save(target)
    print(name, box, crop.size)
