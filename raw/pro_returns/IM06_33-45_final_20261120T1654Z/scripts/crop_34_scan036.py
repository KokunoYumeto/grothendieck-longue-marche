from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/34_scan036.jpg"
CONTRAST = 1.25
CROPS = [
    ("34_scan036_L622_soient_detail.png", (1280, 1415, 1640, 1535), 2600, 0),
    ("34_scan036_L622_final_claim.png", (215, 1230, 1640, 1755), 2600, 0),
    ("34_scan036_L622_char_qualification.png", (200, 460, 1650, 725), 2600, 0),
    ("34_scan036_L622_margin_nb.png", (10, 840, 310, 1475), 2200, 0),
    ("34_scan036_L622_margin_nb_rotated.png", (10, 840, 310, 1475), 2600, -40),
]

image = Image.open(SOURCE)
print("source dimensions:", image.size)
for name, box, output_width, rotation in CROPS:
    crop = ImageEnhance.Contrast(image.crop(box)).enhance(CONTRAST)
    if rotation:
        crop = crop.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor="white")
    crop = crop.resize((output_width, round(crop.height * output_width / crop.width)), Image.Resampling.LANCZOS)
    target = ROOT / "crops" / name
    target.parent.mkdir(exist_ok=True)
    crop.save(target)
    print(name, box, crop.size, "rotation", rotation)
