"""Create L614 facsimile evidence crops; no OCR."""

from pathlib import Path

from PIL import Image, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan061.jpg"
CROPS = [
    ("36_scan061_L614_d_definition.png", (600, 805, 980, 885)),
    ("36_scan061_L614_dt_definition.png", (230, 1490, 1310, 1570)),
    ("36_scan061_L614_clause_and_inserted_formula.png", (230, 1635, 1648, 1876)),
    ("36_scan061_L614_perfect_field_margin.png", (16, 1810, 225, 1958)),
]


def main():
    image = Image.open(SOURCE)
    (ROOT / "crops").mkdir(exist_ok=True)
    print("Source dimensions:", image.size)
    for filename, box in CROPS:
        crop = ImageEnhance.Contrast(image.crop(box)).enhance(1.25)
        crop = crop.resize(
            (2600, round(crop.height * 2600 / crop.width)),
            Image.Resampling.LANCZOS,
        )
        path = ROOT / "crops" / filename
        crop.save(path)
        print(path.relative_to(ROOT), box, crop.size)


if __name__ == "__main__":
    main()
