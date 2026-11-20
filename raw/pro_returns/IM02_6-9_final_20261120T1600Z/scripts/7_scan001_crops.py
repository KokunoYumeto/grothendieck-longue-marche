from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/7_scan001/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("7_scan001_L734_cover_overview.jpg", (0, 0, 824, 485), 2800),
    ("7_scan001_L740_IMAG_label.jpg", (10, 115, 440, 385), 2800),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.2)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
