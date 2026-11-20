from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
# Rotate the original upside-down scan only for reading.
im = Image.open(ROOT / "assignments/8_scan032/scan.jpg").convert("RGB").transpose(Image.Transpose.ROTATE_180)
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("8_scan032_L743_page55ter_proof.jpg", (170, 0, im.width, 1010), 3000),
    ("8_scan032_L744_remark5131.jpg", (170, 1770, im.width, im.height), 3000),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.35)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)
