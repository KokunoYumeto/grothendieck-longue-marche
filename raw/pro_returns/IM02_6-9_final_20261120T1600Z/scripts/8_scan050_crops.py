from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/8_scan050/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("8_scan050_L760_scaling_formulas.jpg", (525, 825, 1660, 1075), 3000),
    ("8_scan050_L760_Omega_exponent.jpg", (1180, 915, 1535, 1025), 2600),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.4)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
