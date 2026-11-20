"""Crop the inserted qualification and its placement without OCR."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/44_scan002.jpg"
CROPS = [
    ("44_scan002_L935_insertion_detail.png", (1195, 315, 1670, 415)),
    ("44_scan002_L935_insertion_placement.png", (945, 295, 1670, 490)),
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
