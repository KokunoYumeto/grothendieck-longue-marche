from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
ROOT = Path('/workspace/scratch/a54e5f656239/IM02_work')
im = Image.open(ROOT / 'assignments/8_scan081/scan.jpg').convert('RGB')
output = ROOT / 'deliverables/crops'
output.mkdir(parents=True, exist_ok=True)
regions = {
    '8_scan081_L749_illusie': ((875, 885, 1645, 1000), 3000),
    '8_scan081_L754_denominator': ((1340, 1085, 1585, 1200), 2800),
    '8_scan081_L754_context': ((275, 1005, 1630, 1255), 3200),
    '8_scan081_L754_insertion': ((280, 1165, 745, 1275), 2800),
    '8_scan081_L763_expectation': ((275, 1220, 1640, 1505), 3200),
}
for name, (box, width) in regions.items():
    crop = im.crop(box)
    crop = ImageOps.autocontrast(crop, cutoff=0.3)
    crop = ImageEnhance.Contrast(crop).enhance(1.5)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(output / (name + '.jpg'), quality=97)
