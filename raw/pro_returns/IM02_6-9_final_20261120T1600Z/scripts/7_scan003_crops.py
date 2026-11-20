from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
ROOT = Path('/workspace/scratch/a54e5f656239/IM02_work')
im = Image.open(ROOT / 'assignments/7_scan003/scan.jpg').convert('RGB')
output = ROOT / 'deliverables/crops'
output.mkdir(parents=True, exist_ok=True)
regions = {
    '7_scan003_L721_context': ((260, 130, 1655, 375), 3000),
    '7_scan003_L721_stratifiants': ((715, 302, 1030, 375), 2800),
    '7_scan003_L721_stratifies': ((335, 208, 615, 283), 2600),
    '7_scan003_L731_page': ((14, 15, 1667, 2131), 2400),
}
for name, (box, width) in regions.items():
    crop = im.crop(box)
    crop = ImageOps.autocontrast(crop, cutoff=0.3)
    crop = ImageEnhance.Contrast(crop).enhance(1.5)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(output / (name + '.jpg'), quality=97)
