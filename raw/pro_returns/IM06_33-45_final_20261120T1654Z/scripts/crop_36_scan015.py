from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan015.jpg"
CONTRAST = 1.25
CROPS = [
    ("36_scan015_L605_claim_calculs.png", (195, 995, 1645, 1265), 2600),
    ("36_scan015_L605_later_conditions.png", (195, 1310, 1655, 1575), 2600),
    ("36_scan015_Qsow062_peu_importe.png", (1175, 520, 1665, 605), 2600),
    ("36_scan015_Qsow062_period_control.png", (555, 1055, 760, 1130), 2200),
    ("36_scan015_Qsow143_Ybars.png", (785, 1430, 1085, 1520), 2600),
    ("36_scan015_Qsow143_soit.png", (925, 1335, 1245, 1430), 2600),
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
