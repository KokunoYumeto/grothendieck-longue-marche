"""Crop theorem text and authorial margins for L608; no OCR."""

from pathlib import Path

from PIL import Image, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/36_scan018.jpg"
CROPS = [
    ("36_scan018_L608_top_caution.png", (635, 18, 1085, 120), 0),
    ("36_scan018_L608_theorem_margin.png", (15, 350, 195, 635), 0),
    ("36_scan018_L608_theorem_margin_rotated.png", (15, 350, 195, 635), -42),
    ("36_scan018_L608_trace_and_deleted_consequence.png", (195, 1305, 1645, 1725), 0),
    ("36_scan018_L608_corollary_margin.png", (14, 1785, 195, 2110), 0),
    ("36_scan018_L608_corollary_margin_rotated.png", (14, 1785, 195, 2110), -42),
    ("36_scan018_L608_corollary_start.png", (203, 1820, 1640, 2080), 0),
]


def main():
    image = Image.open(SOURCE)
    (ROOT / "crops").mkdir(exist_ok=True)
    print("Source dimensions:", image.size)
    for filename, box, angle in CROPS:
        crop = ImageEnhance.Contrast(image.crop(box)).enhance(1.25)
        if angle:
            crop = crop.rotate(angle, expand=True, fillcolor="white")
        crop = crop.resize(
            (2600, round(crop.height * 2600 / crop.width)),
            Image.Resampling.LANCZOS,
        )
        path = ROOT / "crops" / filename
        crop.save(path)
        print(path.relative_to(ROOT), box, angle, crop.size)


if __name__ == "__main__":
    main()
