"""Make enlarged facsimile crops for L590; no OCR or recognition."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/40_scan027.jpg"
CROPS = [
    ("40_scan027_L590_assertion.png", (440, 620, 1740, 960)),
    ("40_scan027_L590_uniformizer_formula.png", (460, 950, 1690, 1140)),
    ("40_scan027_L590_bounds.png", (480, 1120, 1690, 1335)),
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
