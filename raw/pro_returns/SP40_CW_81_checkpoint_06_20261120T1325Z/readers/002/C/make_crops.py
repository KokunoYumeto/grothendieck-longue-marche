from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

base = Path('/workspace/scratch/94548b74fbe0/out/readers/002/C')
source = Path('/workspace/scratch/94548b74fbe0/source/SP40_CW_81_scans/J81-01_81_scan002.jpg')
im = Image.open(source)
print({'source_dimensions': im.size})
specs = [
    ('crop_01_initial_oval.png', (505, 45, 805, 140), 2400),
    ('crop_02_first_word.png', (625, 40, 835, 145), 2400),
    ('crop_03_title_accents.png', (810, 45, 1105, 245), 2600),
]
for name, bbox, target_width in specs:
    cut = ImageOps.autocontrast(im.crop(bbox).convert('RGB'))
    cut = cut.resize((target_width, round(cut.height * target_width / cut.width)), Image.Resampling.LANCZOS)
    cut = cut.filter(ImageFilter.UnsharpMask(radius=1.2, percent=100, threshold=3))
    cut.save(base / name)
    print({'path': name, 'bbox': bbox, 'rotation': 0, 'dimensions': cut.size})
