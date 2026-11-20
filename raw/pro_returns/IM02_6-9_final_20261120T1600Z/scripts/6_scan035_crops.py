from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
ROOT = Path('/workspace/scratch/a54e5f656239/IM02_work')
im = Image.open(ROOT / 'assignments/6_scan035/scan.jpg').convert('RGB')
output = ROOT / 'deliverables/crops'
output.mkdir(parents=True, exist_ok=True)
regions = {
    '6_scan035_L701_statement': ((180, 95, 1590, 430), 3000),
    '6_scan035_L701_formula': ((590, 270, 1530, 430), 3000),
    '6_scan035_L702_conjecture': ((200, 800, 1655, 1415), 3000),
    '6_scan035_L706_fraction': ((520, 1040, 960, 1175), 2800),
}
for name, (box, width) in regions.items():
    crop = im.crop(box)
    crop = ImageOps.autocontrast(crop, cutoff=0.3)
    crop = ImageEnhance.Contrast(crop).enhance(1.5)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(output / (name + '.jpg'), quality=97)
