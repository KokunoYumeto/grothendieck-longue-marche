from pathlib import Path
from PIL import Image, ImageOps
import json
import os

EDITION = Path(__file__).resolve().parents[1]
SOURCE = EDITION.parent / "input/SP91_C13_150_scans/150_scan068.jpg"
PLACES = [
    ("p01_initial", [247,24,652,146], "Cancelled Ceci/Cela posé and its relation to the live opening", 0),
    ("p02_reflexive", [1119,18,1460,151], "Cancelled symétrique and inserted réflexive", 0),
    ("p03_top_formula", [464,234,1649,332], "Entire opening pi-zero expression, all parenthesized Sigma arguments and underlined labels", 0),
    ("p04_b_fibrant", [1044,394,1446,480], "Underlined b and est fibrant, punctuation and crossing neighbouring descenders", 0),
    ("p05_lemma_diagram", [963,449,1222,627], "Whole four-object square, all arrows, labels, primes and endpoint forms", 0),
    ("p06_top_fibrant", [469,593,1605,685], "cartésien d'espaces top abbreviation, punctuation and f fibrant", 0),
    ("p07_lemma_result", [476,677,1672,773], "Whole concluding pi-zero map, product index and surjectif ending", 0),
    ("p08_associee", [1227,770,1674,879], "Top abbreviation and right-edge discrète associée", 0),
    ("p09_ens_pre", [291,884,792,990], "ens punctuation, inserted pré and ordonné", 0),
    ("p10_I_equality", [852,841,1128,982], "I/I-zero and the full inserted pi-zero equality with its leader", 0),
    ("p11_M0615", [1415,924,1673,995], "Bracketed interlinear word M0615 and both delimiter forms", 0),
    ("p12_designera", [296,995,747,1100], "on désignera/désigne par and ending strokes", 0),
    ("p13_canonique_added", [241,1071,557,1191], "Inserted canonique and curved attachment leader", 0),
    ("p14_canonique_deleted", [1058,1076,1377,1165], "Cancelled canonique/canoniques and exact final letters", 0),
    ("p15_functor", [563,1199,955,1305], "Whole underlined-Sigma functor map, phi/f label and target underline", 0),
    ("p16_apps0", [528,1394,1008,1512], "First application row, Sigma argument zero, phi-zero and I-zero=I", 0),
    ("p17_apps1", [527,1481,1673,1668], "Whole second application expression with appended image formula and crossed intermediate ending", 0),
    ("p18_sum0", [545,1754,941,1851], "Whole first lower coproduct equality, argument zero and punctuation", 0),
    ("p19_sum1", [545,1848,990,2009], "Whole second lower coproduct equality, overwritten operator and both index lines", 0),
    ("p20_NB", [33,1710,524,1975], "Slanted marginal NB, every word, underline and Sigma index", -14),
    ("p21_compatibles", [1186,1820,1649,1983], "Right-hand compatibles note, s/b punctuation and both whole short maps", 0),
    ("p22_delta", [580,1976,1490,2099], "Whole delta map and parenthetical identity, including densely cancelled predecessor", 0),
    ("p23_cequi", [1028,2084,1600,2184], "Crossed et ainsi or other reading, opening delimiter and ce qui", 0),
    ("p24_implique", [279,2170,554,2276], "implique/indique and visible ascenders/descenders", 0),
    ("p25_varphi", [1253,2174,1519,2258], "Whole phi=(phi-zero,phi-one) expression and underline state", 0),
    ("p26_composition", [285,2244,1187,2350], "la composition, terminal delimiter, De plus and punctuation", 0),
    ("p27_est_un", [1196,2261,1560,2341], "Last phi and est un/a une wording", 0),
    ("p28_folio", [19,2301,88,2357], "Other-hand pale lower-left foliation67", 0),
]

source = Image.open(SOURCE).convert("RGB")
assert source.size == (1684,2361)
records = []
for name, box, purpose, rotation in PLACES:
    target = EDITION / "crops" / f"150_scan068_{name}.png"
    assert not target.exists(), ("Do not recrop an existing first-pass place", str(target))
    crop = ImageOps.autocontrast(source.crop(box))
    if rotation:
        crop = crop.rotate(rotation, resample=Image.Resampling.BICUBIC,
                           expand=True, fillcolor="white")
    width = 3000 if box[2]-box[0] > 1000 else 2400
    crop = crop.resize((width, round(crop.height*width/crop.width)), Image.Resampling.LANCZOS)
    temporary = target.with_name(target.name + ".tmp")
    crop.save(temporary, format="PNG")
    os.replace(temporary, target)
    records.append({
        "file": str(target.relative_to(EDITION)), "box": box,
        "purpose": purpose, "rotation_degrees": rotation,
    })
manifest = EDITION / "scripts/reader_c_068_crop_manifest.json"
temporary = manifest.with_name(manifest.name + ".tmp")
with temporary.open("w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)
    f.write("\n")
    f.flush()
    os.fsync(f.fileno())
os.replace(temporary, manifest)
print(f"{len(records)} crops saved; manifest {manifest}")
