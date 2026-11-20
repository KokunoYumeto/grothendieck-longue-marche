from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
ROOT = Path('/workspace/scratch/a54e5f656239/IM02_work')
im = Image.open(ROOT / 'assignments/6_scan054/scan.jpg').convert('RGB')
output = ROOT / 'deliverables/crops'
output.mkdir(parents=True, exist_ok=True)
regions = {
    '6_scan054_L715_seulement': ((850, 744, 1080, 809), 2600),
    '6_scan054_L715_firstwords': ((440, 744, 1075, 822), 3000),
    '6_scan054_L715_provient': ((480, 793, 700, 845), 2600),
    '6_scan054_L715_bracket': ((390, 735, 1640, 890), 3200),
    '6_scan054_L715_firstline': ((410, 749, 1590, 810), 3200),
    '6_scan054_L715_secondline': ((430, 788, 1630, 850), 3200),
    '6_scan054_L715_torseur_top': ((1100, 650, 1335, 726), 2400),
    '6_scan054_L715_torseur_lower': ((1410, 1555, 1645, 1630), 2400),
}
for name, (box, width) in regions.items():
    crop = im.crop(box)
    crop = ImageOps.autocontrast(crop, cutoff=0.3)
    crop = ImageEnhance.Contrast(crop).enhance(1.5)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(output / (name + '.jpg'), quality=97)
