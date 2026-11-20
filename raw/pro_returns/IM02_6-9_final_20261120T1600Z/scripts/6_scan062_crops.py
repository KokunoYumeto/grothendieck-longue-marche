from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/6_scan062/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("6_scan062_L716_equivalence_chain.jpg", (565, 635, 1658, 850), 3000),
    ("6_scan062_L716_RHom_ending.jpg", (1300, 640, 1658, 745), 2600),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.5)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
