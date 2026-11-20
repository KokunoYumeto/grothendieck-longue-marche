from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/7_scan041/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("7_scan041_L724_formula.jpg", (570, 510, 1665, 805), 3000),
    ("7_scan041_L724_disc_radius.jpg", (235, 1105, 1655, 1460), 3000),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
