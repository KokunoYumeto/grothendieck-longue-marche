"""Crop the disputed subscript and same-page case comparators, without OCR."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/43_scan136.jpg"
CROPS = [
    ("43_scan136_L930_target_equality.png", (1340, 1695, 1665, 1805)),
    ("43_scan136_L930_lower_chain.png", (1380, 1960, 1670, 2130)),
    ("43_scan136_L930_triangle_comparators.png", (330, 930, 790, 1090)),
]

def main():
    source = Image.open(SOURCE)
    print("Source dimensions:", source.size)
    (ROOT / "crops").mkdir(exist_ok=True)
    for name, box in CROPS:
        crop = ImageEnhance.Contrast(source.crop(box)).enhance(1.25)
        crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
        destination = ROOT / "crops" / name
        crop.save(destination)
        print(destination.relative_to(ROOT), box, crop.size)

if __name__ == "__main__":
    main()
