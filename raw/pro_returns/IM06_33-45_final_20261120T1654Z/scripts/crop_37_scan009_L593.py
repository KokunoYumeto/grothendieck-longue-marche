"""Document the transcribed letter on scan 009 using image crops only."""

from pathlib import Path

from PIL import Image, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/37_scan009.jpg"
CROPS = [
    ("37_scan009_L593_letter_opening.png", (335, 60, 1580, 435)),
    ("37_scan009_L593_correction_list.png", (335, 445, 1220, 965)),
    ("37_scan009_L593_closing_and_margin.png", (100, 975, 1665, 1610)),
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
