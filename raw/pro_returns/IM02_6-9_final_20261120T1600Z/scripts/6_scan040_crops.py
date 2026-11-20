from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
BASE = Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE = BASE / 'assignments/6_scan040/scan.jpg'
DEST = BASE / 'deliverables/crops'
DEST.mkdir(parents=True, exist_ok=True)
with Image.open(SOURCE) as source:
    print('Source dimensions:', source.size)
    # The two-line handwritten title, located manually on the full scan.
    box = (1140, 35, 1730, 225)
    crop = ImageOps.autocontrast(source.crop(box).convert('RGB'), cutoff=0.5)
    crop = ImageEnhance.Contrast(crop).enhance(1.45)
    crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
    target = DEST / '6_scan040_L1325_handwritten_title.jpg'
    crop.save(target, quality=96)
    print(target.name, box, crop.size)
