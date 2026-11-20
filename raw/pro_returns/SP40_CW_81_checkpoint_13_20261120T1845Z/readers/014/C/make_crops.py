from pathlib import Path
from PIL import Image, ImageOps
root = Path('/workspace/scratch/94548b74fbe0')
source = root / 'source/SP40_CW_81_scans/J81-02_81_scan014.jpg'
out = root / 'out/readers/014/C'
im = Image.open(source)
specs = [
    ('01_first_word.png', (860, 90, 1295, 195), 6),
    ('02_insertion_and_naires.png', (1135, 28, 1565, 180), 6),
    ('03_second_line.png', (930, 182, 1565, 305), 5),
]
for name, box, factor in specs:
    crop = ImageOps.autocontrast(im.crop(box).convert('RGB'))
    crop = crop.resize((crop.width * factor, crop.height * factor), Image.Resampling.LANCZOS)
    crop.save(out / name)
    print(name, 'full_scan_bbox=', box, 'size=', crop.size, 'rotation=0')
