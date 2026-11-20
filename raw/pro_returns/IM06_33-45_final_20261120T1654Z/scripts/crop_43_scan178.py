from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/43_scan178.jpg"
CONTRAST = 1.25
CROPS = [
    ("43_scan178_H0442_target.png", (120, 132, 448, 210), 2800),
    ("43_scan178_H0442_top_label.png", (235, 35, 435, 100), 2400),
    ("43_scan178_H0442_unipotent_label.png", (690, 285, 850, 375), 2400),
    ("43_scan178_H0442_multiplicatif_comparison.png", (270, 550, 520, 635), 2600),
    ("43_scan178_H0442_separable_comparison.png", (235, 430, 435, 515), 2400),
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
