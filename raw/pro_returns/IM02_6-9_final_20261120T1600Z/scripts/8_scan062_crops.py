from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
# The typescript is upside down in the supplied scan.
im = Image.open(ROOT / "assignments/8_scan062/scan.jpg").convert("RGB").transpose(Image.Transpose.ROTATE_180)
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
crop = ImageEnhance.Contrast(im.crop((340, 35, im.width - 80, 1085))).enhance(1.35)
crop = crop.resize((3000, round(crop.height * 3000 / crop.width)), Image.Resampling.LANCZOS)
crop.save(out / "8_scan062_L743_page35_local_construction.jpg", quality=95)
