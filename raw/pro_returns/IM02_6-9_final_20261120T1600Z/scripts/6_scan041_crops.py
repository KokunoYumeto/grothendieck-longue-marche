from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps
BASE = Path('/workspace/scratch/a54e5f656239/IM02_work')
SOURCE = BASE / 'assignments/6_scan041/scan.jpg'
DEST = BASE / 'deliverables/crops'
DEST.mkdir(parents=True, exist_ok=True)
CROPS = {
 '6_scan041_L718_question_a.jpg': (195, 85, 1648, 530),
 '6_scan041_L718_question_b.jpg': (225, 520, 1648, 900),
 '6_scan041_L718_question_c.jpg': (225, 890, 1590, 1218),
 '6_scan041_L718_question_d.jpg': (230, 1205, 1628, 1480),
}
with Image.open(SOURCE) as source:
    print('Source dimensions:', source.size)
    for name, box in CROPS.items():
        crop = ImageOps.autocontrast(source.crop(box).convert('RGB'), cutoff=0.5)
        crop = ImageEnhance.Contrast(crop).enhance(1.45)
        crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
        crop.save(DEST / name, quality=96)
        print(name, box, crop.size)
