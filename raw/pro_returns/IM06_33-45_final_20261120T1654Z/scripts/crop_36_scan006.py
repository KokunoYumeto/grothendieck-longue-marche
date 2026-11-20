from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan006.jpg"
CONTRAST = 1.25
CROPS = [
    ("36_scan006_L616_guillemets.png", (55, 165, 325, 345), 2200),
    ("36_scan006_L616_je_le_dis.png", (65, 765, 325, 910), 2200),
    ("36_scan006_L616_cest_dit.png", (20, 1295, 290, 1505), 2200),
    ("36_scan006_L616_question_reply.png", (20, 1060, 480, 1285), 2600),
    ("36_scan006_L1549_numeral.png", (455, 1880, 825, 1990), 2600),
    ("36_scan006_L1549_page_keys.png", (185, 1485, 1625, 1750), 2600),
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
