"""Crop L585 and a same-page handwriting comparator without OCR."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/42_scan007.jpg"
CROPS = [
    ("42_scan007_L585_finie_clause.png", (330, 1660, 1660, 1850)),
    ("42_scan007_L585_finie_detail.png", (725, 1740, 1045, 1850)),
    ("42_scan007_L585_construction.png", (350, 1820, 1660, 2140)),
    ("42_scan007_L585_fini_comparator.png", (565, 910, 1000, 1010)),
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
