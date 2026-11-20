from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
ROOT = Path('/workspace/scratch/a54e5f656239/IM02_work')
im = Image.open(ROOT / 'assignments/8_scan074/scan.jpg').convert('RGB').rotate(180, expand=True)
output = ROOT / 'deliverables/crops'
output.mkdir(parents=True, exist_ok=True)
# Boxes are measured in the upright image after the 180-degree rotation.
regions = {
    '8_scan074_L1366_page': ((0, 0, 1734, 2231), 2400),
    '8_scan074_L1366_opening': ((380, 70, 1570, 650), 3000),
    '8_scan074_L1366_theorem': ((350, 1570, 1720, 2065), 3000),
}
for name, (box, width) in regions.items():
    crop = im.crop(box)
    crop = ImageOps.autocontrast(crop, cutoff=0.3)
    crop = ImageEnhance.Contrast(crop).enhance(1.4)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(output / (name + '.jpg'), quality=97)
