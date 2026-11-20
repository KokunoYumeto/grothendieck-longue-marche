"""Make page-specific visual evidence crops; no OCR or text recognition."""

from pathlib import Path

from PIL import Image, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan010.jpg"
CROPS = [
    ("36_scan010_Qsow079_leray_formula.png", (525, 1025, 1130, 1125)),
    ("36_scan010_Qsow079_deleted_subscript.png", (880, 1030, 1045, 1107)),
    ("36_scan010_Qsow204_primitive_formula.png", (1095, 745, 1435, 835)),
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
