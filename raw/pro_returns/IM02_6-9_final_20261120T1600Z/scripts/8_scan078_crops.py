from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/8_scan078/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("8_scan078_L752_heading.jpg", (190, 60, 1280, 185), 3000),
    ("8_scan078_L752_coLie_detail.jpg", (520, 65, 690, 145), 2600),
    ("8_scan078_L753_Mazur_Roberts.jpg", (1050, 985, 1535, 1110), 3000),
    ("8_scan078_L737_formulas_page77.jpg", (0, 1360, im.width, im.height), 3000),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.4)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
