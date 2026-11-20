from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/8_scan017/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("8_scan017_L744_cancelled_page.jpg", (0, 0, 1685, 2160), 2600),
    ("8_scan017_L764_restricted_equivalence.jpg", (210, 1460, 1655, 1915), 3000),
    ("8_scan017_L764_rigidity_formula.jpg", (220, 1190, 1655, 1480), 3000),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.35)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
