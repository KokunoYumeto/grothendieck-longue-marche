"""First-pass crops for scan075 only. Existing crop files are never overwritten."""
from pathlib import Path
from PIL import Image, ImageOps
import json
import os

EDITION = Path(__file__).resolve().parents[1]
ROOT = EDITION.parent
SOURCE = ROOT / "input/SP91_C13_150_scans/150_scan075.jpg"
PLACES = [
    ("p01_standart_first", [1276,57,1536,145], 0, 2400, "First standart/standard, including its written ending."),
    ("p02_first_display", [266,244,1668,646], 0, 3600, "Entire first braced display: crossed number, cancelled low group, all three rows and right-hand de sorte que expression with both union bounds."),
    ("p03_prend_pose", [267,608,773,732], 0, 2400, "On, cancelled pose, inserted prend and alors; attachment and cancellation extent."),
    ("p04_standart_T1", [265,726,887,834], 0, 2400, "Second standart, cancelled de, T1 and its raised reworked mark; H's additional cancelled word."),
    ("p05_standart_third", [1236,943,1668,1041], 0, 2400, "vois. tub. and third standart/standard at the right paper edge."),
    ("p06_M0645", [275,1039,1275,1158], 0, 2400, "Complete X^(1)_(1) and following x^(1)/X^(1) expressions, punctuation and On pose."),
    ("p07_second_display", [222,1179,1507,1428], 0, 3600, "Entire second two-line display including crossed number, all ringed T expressions and reworked raised mark after the final X."),
    ("p08_OPS_margin", [20,1194,548,1656], -40, 2400, "Complete oblique OPS/Ops note, union bounds, wording and X_i/star question."),
    ("p09_live48", [270,1795,1102,1957], 0, 2400, "Whole live (48), including the horizontal subtraction stroke, full union bound, ringed T and terminal point."),
    ("p10_final49", [242,2039,1669,2332], 0, 3600, "Entire final (49), isolated upright M0646, lowered (d), cancelled pre-union glyph, local T marks, both decorated bounds and cancelled right-hand relation."),
]

im = Image.open(SOURCE).convert("RGB")
assert im.size == (1680,2363), im.size
out = []
for stem, box, angle, width, purpose in PLACES:
    dest = EDITION / "crops" / f"150_scan075_{stem}.png"
    assert not dest.exists(), dest
    crop = im.crop(box)
    if angle:
        crop = crop.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True, fillcolor="white")
    crop = ImageOps.autocontrast(crop)
    crop = crop.resize((width, round(crop.height*width/crop.width)), Image.Resampling.LANCZOS)
    temporary = dest.with_name(dest.name+".tmp")
    crop.save(temporary, format="PNG")
    os.replace(temporary, dest)
    out.append({"file": f"crops/{dest.name}", "box": box, "rotation": angle, "width": width, "purpose": purpose})

manifest = EDITION / "scripts/reader_c_075_crop_manifest.json"
temporary = manifest.with_name(manifest.name+".tmp")
with temporary.open("w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
    f.flush()
    os.fsync(f.fileno())
os.replace(temporary, manifest)
print(json.dumps({"crops":len(out), "manifest":str(manifest)}, ensure_ascii=False))
