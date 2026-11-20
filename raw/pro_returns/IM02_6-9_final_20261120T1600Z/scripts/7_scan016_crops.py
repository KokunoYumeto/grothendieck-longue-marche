from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
ROOT = Path('/workspace/scratch/a54e5f656239/IM02_work')
im = Image.open(ROOT / 'assignments/7_scan016/scan.jpg').convert('RGB')
output = ROOT / 'deliverables/crops'
output.mkdir(parents=True, exist_ok=True)
regions = {
    '7_scan016_L730_margin': ((12, 1205, 300, 1815), 2800, -48),
    '7_scan016_L730_bubble': ((20, 1220, 245, 1515), 2800, -48),
    '7_scan016_L730_calculs': ((20, 1380, 270, 1815), 3000, -48),
    '7_scan016_L739_remarque': ((240, 1310, 1625, 2130), 3000, 0),
}
for name, (box, width, angle) in regions.items():
    crop = im.crop(box)
    crop = ImageOps.autocontrast(crop, cutoff=0.3)
    crop = ImageEnhance.Contrast(crop).enhance(1.5)
    if angle:
        crop = crop.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor='white')
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(output / (name + '.jpg'), quality=97)
