from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/6_scan049/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("6_scan049_L713_isomorphic_product.jpg", (220, 100, 1650, 345), 3000),
    ("6_scan049_L714_locally_closed_family.jpg", (230, 350, 1640, 880), 3000),
    ("6_scan049_L714_open_U.jpg", (240, 870, 1660, 1040), 3000),
    ("6_scan049_L714_transcendence_conclusion.jpg", (270, 1690, 1670, 2130), 3000),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.6)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
