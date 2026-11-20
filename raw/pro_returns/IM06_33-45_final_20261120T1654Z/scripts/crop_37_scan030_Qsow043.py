"""Crop the disputed punctuation and same-page comparators, without OCR."""

from pathlib import Path

from PIL import Image, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/37_scan030.jpg"
CROPS = [
    ("37_scan030_Qsow043_disputed_mark.png", (930, 760, 1345, 835)),
    ("37_scan030_Qsow043_earlier_th.png", (1200, 335, 1600, 390)),
    ("37_scan030_Qsow043_typed_comma.png", (642, 765, 912, 835)),
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
