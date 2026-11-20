"""Create visual evidence crops for scan 014, without OCR."""

from pathlib import Path

from PIL import Image, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan014.jpg"
CROPS = [
    ("36_scan014_L609_inserted_morphism.png", (180, 65, 1380, 158)),
    ("36_scan014_Qsow146_first_base.png", (1330, 1920, 1555, 1990)),
    ("36_scan014_Qsow146_last_morphism.png", (1385, 1988, 1665, 2085)),
    ("36_scan014_Qsow146_typed_S_comparator.png", (210, 810, 480, 875)),
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
