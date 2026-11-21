"""First-pass crops for scan071 only. Do not rerun after the crops exist."""
from pathlib import Path
from PIL import Image, ImageOps
import json
import os

EDITION = Path(__file__).resolve().parents[1]
ROOT = EDITION.parent
SOURCE = ROOT / "input/SP91_C13_150_scans/150_scan071.jpg"
PLACES = [
    ("p01_d_added", [1062, 38, 1558, 149], 0, "First-line a), c), raised d), page reference and punctuation."),
    ("p02_A_t_on", [281, 176, 542, 275], 0, "A-t-on versus H's Montrons."),
    ("p03_question_formula", [543, 273, 1662, 378], 0, "Whole intersection equality and its question wording, including wrapped comparables."),
    ("p04_intersection", [727, 353, 1181, 489], 0, "Whole x-membership/intersection expression and raised subset addition."),
    ("p05_alors", [1122, 387, 1585, 488], 0, "alors versus donc, followed by on aurait."),
    ("p06_M0623_pair", [694, 494, 1194, 587], 0, "Complete pair of element labels, first retraced, with et and de Sigma."),
    ("p07_au_dessus", [1205, 492, 1626, 579], 0, "First au dessus phrase and H's supplied hyphen."),
    ("p08_au_dessus_second", [1183, 572, 1650, 651], 0, "Relation before x, opening parenthesis, and second au dessus phrase."),
    ("p09_tot", [808, 648, 1659, 744], 0, "Whole Sigma_<x expression and abbreviated ordinality clause."),
    ("p10_on_aurait", [282, 770, 879, 877], 0, "Cancelled on aurait followed by the live x et y."),
    ("p11_les_quotes", [276, 995, 1640, 1155], 0, "Conséquence, les/Les, structures and opening quotation marks."),
    ("p12_indexes", [1247, 1095, 1641, 1201], 0, "indexés versus indexées, detached accent and par."),
    ("p13_dans", [278, 1210, 1639, 1368], 0, "Closing quotation, décrites, dans strike state, page 28 and équivalent."),
    ("p14_M0624_margin", [16, 1280, 280, 1683], -43, "Complete oblique marginal note, initial et/si and its final punctuation."),
    ("p15_cancelled_Sigma", [350, 1447, 957, 1575], 0, "Circled a, Un, cancelled Sigma and espace."),
    ("p16_aux", [584, 1572, 1034, 1668], 0, "aux live/struck state before conditions."),
    ("p17_condition", [1058, 1630, 1513, 1734], 0, "End of la condition and H's reported extra cancelled group."),
    ("p18_pour_tout", [266, 1761, 948, 1899], 0, "que, cancelled pour tout, posant and intervening ink."),
    ("p19_Itilde", [1000, 1722, 1420, 1850], 0, "Complete I-tilde equals pi-zero(Sigma) expression."),
    ("p20_index_relation", [614, 1858, 1087, 1990], 0, "Complete i,j membership in I-tilde and i<j."),
    ("p21_immersion_bordant", [267, 1948, 1145, 2096], 0, "d'immersion propre and raised dark bordant, compared with H's placement."),
    ("p22_bij_map", [1191, 1908, 1636, 2044], 0, "Whole Sigma_ij-to-Sigma_j expression, b_ij label and shaft endpoint."),
    ("p23_strictement", [903, 2108, 1510, 2210], 0, "strictement croissante and the crowded ending."),
    ("p24_M0625", [260, 2199, 929, 2334], 0, "Complete parenthetical pas néc. surjection, abbreviation and ending."),
    ("p25_final_map", [769, 2246, 1153, 2341], 0, "Complete final I-tilde-to-I map, head and target bars."),
]

im = Image.open(SOURCE).convert("RGB")
assert im.size == (1678, 2364), im.size
out = []
for stem, box, rotation, purpose in PLACES:
    dest = EDITION / "crops" / f"150_scan071_{stem}.png"
    assert not dest.exists(), dest
    crop = im.crop(box)
    if rotation:
        crop = crop.rotate(rotation, resample=Image.Resampling.BICUBIC, expand=True, fillcolor="white")
    crop = ImageOps.autocontrast(crop)
    crop = crop.resize((2400, round(crop.height*2400/crop.width)), Image.Resampling.LANCZOS)
    temporary = dest.with_name(dest.name + ".tmp")
    crop.save(temporary, format="PNG")
    os.replace(temporary, dest)
    out.append({"file": f"crops/{dest.name}", "box": box, "rotation": rotation, "purpose": purpose})

manifest = EDITION / "scripts/reader_c_071_crop_manifest.json"
temporary = manifest.with_name(manifest.name + ".tmp")
with temporary.open("w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
    f.flush()
    os.fsync(f.fileno())
os.replace(temporary, manifest)
print(json.dumps({"crops": len(out), "manifest": str(manifest)}, ensure_ascii=False))
