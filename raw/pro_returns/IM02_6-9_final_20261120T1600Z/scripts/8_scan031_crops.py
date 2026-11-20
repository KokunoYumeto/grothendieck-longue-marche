from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
ROOT = Path('/workspace/scratch/a54e5f656239/IM02_work')
im = Image.open(ROOT / 'assignments/8_scan031/scan.jpg').convert('RGB')
output = ROOT / 'deliverables/crops'
output.mkdir(parents=True, exist_ok=True)
regions = {
    '8_scan031_L758_gauge': ((455, 1360, 910, 1550), 2800),
    '8_scan031_L758_complex': ((530, 1605, 1650, 1890), 3200),
    '8_scan031_L758_firstmap': ((615, 1705, 985, 1810), 2800),
    '8_scan031_L758_pair': ((1020, 1680, 1615, 1790), 3000),
    '8_scan031_L758_sign': ((755, 1720, 845, 1795), 2400),
}
for name, (box, width) in regions.items():
    crop = im.crop(box)
    crop = ImageOps.autocontrast(crop, cutoff=0.3)
    crop = ImageEnhance.Contrast(crop).enhance(1.5)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(output / (name + '.jpg'), quality=97)
