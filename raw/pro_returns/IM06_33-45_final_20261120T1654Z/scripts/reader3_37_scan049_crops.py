"""Create retained visual-reading crops for statements L588/L589 on scan 37/49."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/37_scan049.jpg"
CROPS = [
    ("37_scan049_L588_monomorphisms.png", (245, 1140, 1610, 1245)),
    ("37_scan049_L589_generisation.png", (390, 715, 1575, 820)),
    ("37_scan049_L589_parenthesis.png", (525, 765, 995, 820)),
    ("37_scan049_L589_downward_opens.png", (385, 360, 1345, 440)),
]

image = Image.open(SOURCE)
(ROOT / "crops").mkdir(exist_ok=True)
for filename, box in CROPS:
    crop = ImageEnhance.Contrast(image.crop(box)).enhance(1.25)
    crop = crop.resize(
        (2600, round(crop.height * 2600 / crop.width)), Image.Resampling.LANCZOS
    )
    crop.save(ROOT / "crops" / filename)
    print(f"crops/{filename}")
