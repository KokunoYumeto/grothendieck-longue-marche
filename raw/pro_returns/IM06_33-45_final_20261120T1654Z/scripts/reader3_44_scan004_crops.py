"""Retain separate insertion and word-reading crops for scan 44/4."""
from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/IM06_33-45_scans/44_scan004.jpg"
CROPS = [
    ("44_scan004_L936_sur_Y.png", (1400, 395, 1650, 495)),
    ("44_scan004_L936_hypotheses.png", (800, 490, 1650, 625)),
    ("44_scan004_L936_cancelled_word.png", (1365, 495, 1645, 615)),
    ("44_scan004_L937_sentence.png", (650, 1535, 1640, 1670)),
    ("44_scan004_L937_word.png", (1180, 1560, 1415, 1655)),
    ("44_scan004_L937_article.png", (1000, 1550, 1210, 1660)),
    ("44_scan004_L937_article_comparison.png", (1185, 1430, 1660, 1525)),
]

image = Image.open(SOURCE)
(ROOT / "crops").mkdir(exist_ok=True)
for filename, box in CROPS:
    crop = ImageEnhance.Contrast(image.crop(box)).enhance(1.25)
    crop = crop.resize(
        (2600, round(crop.height * 2600 / crop.width)), Image.Resampling.LANCZOS
    )
    crop.save(ROOT / "crops" / filename)
    print(f"crops/{filename}")
