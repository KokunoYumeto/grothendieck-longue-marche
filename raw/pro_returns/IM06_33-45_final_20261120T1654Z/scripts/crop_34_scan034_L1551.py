"""Document context crops for L1551; image manipulation only, without OCR."""

from pathlib import Path

from PIL import Image, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/34_scan034.jpg"
CROPS = [
    ("34_scan034_L1551_page_heading.png", (235, 35, 1650, 455)),
    ("34_scan034_L1551_inertia_statement.png", (305, 620, 1650, 1155)),
    ("34_scan034_L1551_section_7_2.png", (55, 1180, 1650, 2125)),
]


def main():
    image = Image.open(SOURCE)
    print("Source dimensions:", image.size)
    (ROOT / "crops").mkdir(exist_ok=True)
    for filename, box in CROPS:
        crop = ImageEnhance.Contrast(image.crop(box)).enhance(1.25)
        height = round(crop.height * 2600 / crop.width)
        crop = crop.resize((2600, height), Image.Resampling.LANCZOS)
        destination = ROOT / "crops" / filename
        crop.save(destination)
        print(destination.relative_to(ROOT), box, crop.size)


if __name__ == "__main__":
    main()
