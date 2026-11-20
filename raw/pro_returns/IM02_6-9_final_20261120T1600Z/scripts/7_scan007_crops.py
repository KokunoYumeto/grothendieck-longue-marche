from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/7_scan007/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("7_scan007_L726_name.jpg", (850, 1565, 1375, 1705), 2800),
    ("7_scan007_L726_pro_objects_context.jpg", (270, 1420, 1630, 1710), 3000),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.6)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
