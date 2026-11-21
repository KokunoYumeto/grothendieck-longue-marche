#!/usr/bin/env python3
"""First and only first-pass crops for reader C's scan 078 places."""
from pathlib import Path
import json
import os
from PIL import Image, ImageOps

EDITION = Path(__file__).resolve().parents[1]
ROOT = EDITION.parent
im = Image.open(ROOT / "input/SP91_C13_150_scans/150_scan078.jpg")
assert im.size == (1681, 2359)
specs = [
    ("p01_initial_c", [283,73,430,133], 2400, "Opening c'est/C'est case and exposed apostrophe."),
    ("p02_first_deletion", [1156,67,1611,173], 2400, "de, crossed espaces-candidate and live proespaces; first-line lexical difference."),
    ("p03_ens", [430,160,920,241], 2400, "l'ens and its following gap, with ordonné; abbreviated spelling and stop question."),
    ("p04_pour_le", [780,256,1641,333], 2400, "(pour/avec l'inclusion), dont le/la, including punctuation and article."),
    ("p05_lim_M0660", [263,351,1123,467], 2400, "Whole underlined lim est ... approx X expression; M0660, abbreviation, underline and terminal point."),
    ("p06_Soit_Z_deleted_X", [373,482,905,593], 2400, "Soit Z, cancelled following letter, and une; readable-cancellation question."),
    ("p07_loc_insertion", [910,431,1569,614], 2400, "partie (fermée) with raised loc-t insertion and its leader, followed by de X comma."),
    ("p08_cancelled_quantifier", [951,599,1409,703], 2400, "Cancelled quantifier-like group before un i tel; complete old glyph and surrounding words."),
    ("p09_condition", [264,719,569,838], 2400, "Entire overwritten X_i-star subset Z condition, with separate glyph and cancellation-state assessment."),
    ("p10_display55", [264,811,1669,972], 3600, "Whole display (55), both V forms, raised Z, number and two-line caption."),
    ("p11_display56_and_prefix", [264,975,1639,1167], 3600, "Whole display (56), both hooked connectors, both V forms and exponent; cancelled de/et and On/on a at left."),
    ("p12_parenthesis", [265,1192,1583,1304], 2400, "Full Plus généralement paragraph line and complete parenthesized X_i_n subset Z condition."),
    ("p13_middle_chain", [570,1298,1587,1430], 3600, "Whole middle equality chain: all V forms, raised marks, four subscripts and continuation strokes."),
    ("p14_inline_V_relatif", [264,1444,1334,1577], 3000, "C'est aussi le, complete indexed V, relatif punctuation and following article."),
    ("p15_fil_edge", [1322,1431,1681,1573], 2400, "Cancelled fil-like group and entire following stratification-shaped word at the paper edge."),
    ("p16_definition", [1072,1561,1673,1694], 2400, "Whole Z_i definition, def accent question, comma and right-edge pour."),
    ("p17_indices_On_a", [962,1705,1447,1812], 2400, "Complete i_0 continuation i_n sequence, point and On a."),
    ("p18_display57", [234,1816,1681,1985], 3600, "Whole display (57), both V forms, exponent, two continuation clusters, hook/head contour and right-edge caption."),
    ("p19_display58", [240,2108,1596,2258], 3600, "Whole final display (58): original digits, both unions, stars, capital J indices and comma.")
]
out = []
for suffix, box, width, purpose in specs:
    name = f"150_scan078_{suffix}.png"
    path = EDITION / "crops" / name
    assert not path.exists(), f"Do not make a second first-pass crop: {path}"
    crop = ImageOps.autocontrast(im.crop(box).convert("RGB"))
    crop = crop.resize((width, round(crop.height * width / crop.width)), Image.Resampling.LANCZOS)
    crop.save(path, "PNG")
    out.append({"file": "crops/" + name, "box": box, "rotation": 0,
                "width": width, "purpose": purpose})
target = EDITION / "scripts/reader_c_078_crop_manifest.json"
tmp = target.with_name(target.name + ".tmp")
with tmp.open("w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
    f.flush()
    os.fsync(f.fileno())
os.replace(tmp, target)
print(json.dumps({"scan": "078", "crops": len(out), "manifest": str(target)}))
