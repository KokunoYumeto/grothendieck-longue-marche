from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/8_scan025/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("8_scan025_L745_heading_category.jpg", (170, 70, 1640, 905), 3000),
    ("8_scan025_L745_functor_question.jpg", (260, 1720, 1645, 2045), 3000),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.4)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
