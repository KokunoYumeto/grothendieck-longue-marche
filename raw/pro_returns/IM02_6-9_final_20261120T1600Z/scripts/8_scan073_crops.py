from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/8_scan073/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
# The lower list and folio number are upright in the supplied mixed-orientation page.
crop = ImageEnhance.Contrast(im.crop((0, 1530, im.width, im.height))).enhance(1.35)
crop = crop.resize((3000, round(crop.height * 3000 / crop.width)), Image.Resampling.LANCZOS)
crop.save(out / "8_scan073_L751_handwritten_list_page72.jpg", quality=95)
