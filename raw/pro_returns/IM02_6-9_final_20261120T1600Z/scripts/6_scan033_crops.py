from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
source = ROOT / "assignments/6_scan033/scan.jpg"
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
im = Image.open(source).convert("RGB")
for name, box, width in [
    ("6_scan033_L709_heading.jpg", (1270, 35, 1740, 480), 2800),
    ("6_scan033_L709_page.jpg", (16, 16, 1772, 2205), 2600),
]:
    crop = im.crop(box)
    crop = ImageEnhance.Contrast(crop).enhance(1.4)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
