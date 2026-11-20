from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/6_scan037/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("6_scan037_L703_reduction.jpg", (245, 465, 1670, 780), 3000),
    ("6_scan037_L704_twisted.jpg", (235, 945, 1685, 1275), 3000),
    ("6_scan037_L704_separably_closed.jpg", (235, 1175, 1655, 1780), 3000),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.6)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
