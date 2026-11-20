"""Create the facsimile evidence crop for L625 without text recognition."""

from pathlib import Path

from PIL import Image, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/34_scan082.jpg"
OUTPUT = ROOT / "crops/34_scan082_L625_levels_3_and_2.png"
BOX = (245, 625, 1645, 854)


def main():
    image = Image.open(SOURCE)
    crop = ImageEnhance.Contrast(image.crop(BOX)).enhance(1.25)
    crop = crop.resize(
        (2600, round(crop.height * 2600 / crop.width)), Image.Resampling.LANCZOS
    )
    OUTPUT.parent.mkdir(exist_ok=True)
    crop.save(OUTPUT)
    print("Source dimensions:", image.size)
    print(OUTPUT.relative_to(ROOT), BOX, crop.size)


if __name__ == "__main__":
    main()
