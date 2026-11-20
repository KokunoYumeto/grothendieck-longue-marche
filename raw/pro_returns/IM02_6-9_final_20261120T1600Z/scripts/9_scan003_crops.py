from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/9_scan003/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("9_scan003_L765_corollary_context.jpg", (520, 1535, 1620, 1810), 3000),
    ("9_scan003_L765_Gstar_detail.jpg", (700, 1600, 1020, 1690), 3000),
    ("9_scan003_L766_margin_derivations.jpg", (1110, 1390, min(1815, im.width), 1585), 3200),
    ("9_scan003_L766_derivations_detail.jpg", (1480, 1395, 1810, 1510), 3000),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.4)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
