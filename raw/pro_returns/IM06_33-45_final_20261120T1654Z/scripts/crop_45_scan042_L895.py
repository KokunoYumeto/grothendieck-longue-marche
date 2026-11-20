"""Crop the overwritten group name, its table, and same-page comparators; no OCR."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/45_scan042.jpg"
CROPS = [
    ("45_scan042_L895_group_name.png", (680, 1635, 985, 1740)),
    ("45_scan042_L895_bracket_table.png", (440, 1730, 825, 1965)),
    ("45_scan042_L895_sl_comparator.png", (640, 1045, 910, 1130)),
    ("45_scan042_L895_heading_comparator.png", (160, 535, 325, 640)),
]

def main():
    source = Image.open(SOURCE)
    print("Source dimensions:", source.size)
    (ROOT / "crops").mkdir(exist_ok=True)
    for name, box in CROPS:
        crop = ImageEnhance.Contrast(source.crop(box)).enhance(1.25)
        crop = crop.resize((2600, round(crop.height * 2600 / crop.width)), Image.Resampling.LANCZOS)
        destination = ROOT / "crops" / name
        crop.save(destination)
        print(destination.relative_to(ROOT), box, crop.size)

if __name__ == "__main__":
    main()
