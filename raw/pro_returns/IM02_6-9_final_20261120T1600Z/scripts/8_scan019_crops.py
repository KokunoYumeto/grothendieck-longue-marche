from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
ROOT = Path('/workspace/scratch/a54e5f656239/IM02_work')
im = Image.open(ROOT / 'assignments/8_scan019/scan.jpg').convert('RGB')
output = ROOT / 'deliverables/crops'
output.mkdir(parents=True, exist_ok=True)
regions = {
    '8_scan019_L742_header': ((520, 205, 1460, 450), 3000),
    '8_scan019_L747_integration': ((215, 470, 1605, 800), 3000),
    '8_scan019_L750_measures': ((215, 1385, 1625, 1710), 3000),
}
for name, (box, width) in regions.items():
    crop = im.crop(box)
    crop = ImageOps.autocontrast(crop, cutoff=0.3)
    crop = ImageEnhance.Contrast(crop).enhance(1.5)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(output / (name + '.jpg'), quality=97)
