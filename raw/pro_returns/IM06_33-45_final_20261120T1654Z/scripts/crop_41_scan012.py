from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/41_scan012.jpg"
CONTRAST = 1.25
CROPS = [
    ("41_scan012_L584_first_implication.png", (1280, 674, 1560, 743), 2600),
    ("41_scan012_L584_reverse_implication.png", (1035, 847, 1340, 920), 2600),
    ("41_scan012_L584_context.png", (595, 672, 1650, 1080), 2800),
]

image = Image.open(SOURCE)
for name, box, output_width in CROPS:
    crop = ImageEnhance.Contrast(image.crop(box)).enhance(CONTRAST)
    crop = crop.resize(
        (output_width, round(crop.height * output_width / crop.width)),
        Image.Resampling.LANCZOS,
    )
    target = ROOT / "crops" / name
    target.parent.mkdir(exist_ok=True)
    crop.save(target)
    print(name, box, crop.size)
