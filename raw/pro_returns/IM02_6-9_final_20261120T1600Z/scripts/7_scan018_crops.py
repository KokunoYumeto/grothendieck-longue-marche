from pathlib import Path
from PIL import Image, ImageEnhance

ROOT = Path("/workspace/scratch/a54e5f656239/IM02_work")
im = Image.open(ROOT / "assignments/7_scan018/scan.jpg").convert("RGB")
out = ROOT / "deliverables/crops"
out.mkdir(parents=True, exist_ok=True)
for name, box, width in [
    ("7_scan018_L727_opening.jpg", (340, 515, 1645, 625), 3000),
    ("7_scan018_L728_algebra_phrase.jpg", (240, 1085, 1640, 1325), 3000),
    ("7_scan018_L729_morphism.jpg", (245, 1190, 1660, 1535), 3000),
    ("7_scan018_H0561_affine_space.jpg", (965, 965, 1650, 1110), 3000),
    ("7_scan018_H0561_triple.jpg", (660, 865, 1225, 1010), 2800),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(1.6)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)

# Tighter crops retained for uncertain letters and overwritten symbols.
for name, box, width, contrast in [
    ("7_scan018_L727_noun_detail.jpg", (1035, 520, 1355, 620), 2800, 1.2),
    ("7_scan018_L727_verb_detail.jpg", (715, 515, 1040, 615), 2800, 1.3),
    ("7_scan018_L728_deleted_words.jpg", (805, 1090, 1015, 1205), 2600, 1.3),
    ("7_scan018_H0561_symbol_comparison.jpg", (925, 1380, 1305, 1510), 2800, 1.3),
]:
    crop = ImageEnhance.Contrast(im.crop(box)).enhance(contrast)
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(out / name, quality=95)

name = "7_scan018_L728_Alg_detail.jpg"
crop = ImageEnhance.Contrast(im.crop((250, 1230, 485, 1345))).enhance(1.3)
crop = crop.resize((2800, round(crop.height * 2800 / crop.width)), Image.Resampling.LANCZOS)
crop.save(out / name, quality=95)
