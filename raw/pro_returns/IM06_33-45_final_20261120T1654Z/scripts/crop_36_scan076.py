from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan076.jpg"
CONTRAST = 1.25
CROPS = [
    ("36_scan076_L615_one_control.png", (1070, 1200, 1320, 1315), 2200),
    ("36_scan076_L615_rank_pairing.png", (630, 520, 1170, 625), 2600),
    ("36_scan076_L615_tori.png", (790, 335, 1415, 420), 2600),
    ("36_scan076_L615_tate_pairing.png", (465, 425, 1180, 515), 2600),
]

image = Image.open(SOURCE)
print("source dimensions:", image.size)
for name, box, output_width in CROPS:
    crop = ImageEnhance.Contrast(image.crop(box)).enhance(CONTRAST)
    crop = crop.resize((output_width, round(crop.height * output_width / crop.width)), Image.Resampling.LANCZOS)
    target = ROOT / "crops" / name
    target.parent.mkdir(exist_ok=True)
    crop.save(target)
    print(name, box, crop.size)
