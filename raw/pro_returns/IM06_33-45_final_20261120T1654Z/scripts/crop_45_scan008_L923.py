"""Document the present Lemma 4 context and page-ending proof fragment; no OCR."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/45_scan008.jpg"
CROPS = [
    ("45_scan008_L923_lemma_hypothesis.png", (310, 1180, 1680, 1480)),
    ("45_scan008_L923_lemma_conclusion.png", (300, 1490, 1655, 1940)),
    ("45_scan008_L923_page_end.png", (360, 1950, 1655, 2175)),
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
