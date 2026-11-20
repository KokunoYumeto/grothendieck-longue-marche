from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
ROOT = Path('/workspace/scratch/a54e5f656239/IM02_work')
im = Image.open(ROOT / 'assignments/7_scan059/scan.jpg').convert('RGB')
output = ROOT / 'deliverables/crops'
output.mkdir(parents=True, exist_ok=True)
regions = {
    '7_scan059_L722_opening': ((215, 60, 1585, 190), 3000, 0),
    '7_scan059_L722_ending': ((240, 1640, 1615, 2007), 3000, 0),
    '7_scan059_L722_folio': ((20, 2020, 150, 2140), 2400, 0),
    '7_scan059_L726_margin': ((40, 35, 270, 1140), 3200, -90),
    '7_scan059_L726_name': ((110, 200, 200, 540), 2800, -90),
}
for name, (box, width, angle) in regions.items():
    crop = im.crop(box)
    crop = ImageOps.autocontrast(crop, cutoff=0.3)
    crop = ImageEnhance.Contrast(crop).enhance(1.5)
    if angle:
        crop = crop.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(output / (name + '.jpg'), quality=97)
