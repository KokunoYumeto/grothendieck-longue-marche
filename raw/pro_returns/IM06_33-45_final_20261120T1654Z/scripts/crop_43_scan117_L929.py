"""Enlarge the coefficient group, exponent, and prime comparators; no OCR."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/43_scan117.jpg"
CROPS = [
    ("43_scan117_L929_coefficient_detail.png", (940, 1590, 1260, 1705)),
    ("43_scan117_L929_sequence.png", (780, 1490, 2140, 1710)),
    ("43_scan117_L929_rank_definition.png", (80, 1490, 780, 1710)),
    ("43_scan117_L929_prime_comparators.png", (240, 60, 470, 170)),
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
