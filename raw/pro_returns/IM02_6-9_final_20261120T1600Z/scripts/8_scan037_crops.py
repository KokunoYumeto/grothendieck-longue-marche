from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
# The source typescript is upside down; rotate it only for viewing.
im = Image.open(ROOT / "assignments/8_scan037/scan.jpg").convert("RGB").transpose(Image.Transpose.ROTATE_180)
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
crop = ImageEnhance.Contrast(im.crop((240, 80, im.width - 20, 1050))).enhance(1.35)
crop = crop.resize((3000, round(crop.height * 3000 / crop.width)), Image.Resampling.LANCZOS)
crop.save(out / "8_scan037_L748_number382_page83.jpg", quality=95)
