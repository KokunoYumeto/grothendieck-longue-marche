from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/43_scan133.jpg"
CONTRAST = 1.25
CROPS = [
    ("43_scan133_L931_first_twist.png", (930, 1345, 1035, 1422), 2200),
    ("43_scan133_L931_second_twist.png", (895, 1575, 1005, 1645), 2200),
    ("43_scan133_L931_first_context.png", (325, 1330, 1665, 1505), 2800),
    ("43_scan133_L931_local_minus.png", (1190, 1330, 1455, 1430), 2600),
    ("43_scan133_L931_ones.png", (360, 40, 525, 120), 2200),
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
