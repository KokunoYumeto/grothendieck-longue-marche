from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
# The supplied page is upside down; rotate only to make the original ink readable.
im = Image.open(ROOT / "assignments/8_scan003/scan.jpg").convert("RGB").transpose(Image.Transpose.ROTATE_180)
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("8_scan003_L741_upright_page.jpg", (0, 0, 1685, 2160), 2600),
    ("8_scan003_L741_heading_page132.jpg", (150, 115, 1495, 430), 3000),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.3)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
