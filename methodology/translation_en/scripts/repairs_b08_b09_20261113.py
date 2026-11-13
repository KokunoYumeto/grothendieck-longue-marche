"""Fixes and waivers for the units of b08-b09 that fail the raw checks (glossary only), 13 Nov 2026, after reading each
place in French and English (show_glossary_misses_20261113.py). Each fix's old text is checked to occur exactly once.
usage: python -I -B repairs_b08_b09_20261113.py"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
D = Path(r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\translation_en_20261112")
BY, DATE = "Claude (Opus 5.5)", "2026-11-13"
I = BS + "inserted"
DEL = BS + "deleted"
UL = BS + "uline"

fixes = [
    ("LM_C4-134-152_s140-146",
     "automorphisms of the " + I + "{profinite} loop groups",
     "automorphisms of the " + I + "{profinite} groups with loops",
     "scan 141: 'automorphismes des groupes à lacets " + I + "{profinis}': the glossary renders groupe à lacets as group with loops, never 'loop group' (which means something else in English)"),
    ("LM_C4-153-171_s162-171",
     "-adic} character induced",
     "-adic} character induces",
     "scan 169: in 'le caractère cyclotomique " + I + "{ℓ-adique} induit [display (362)]' induit is the verb: the character induces the map displayed"),
    ("LM_C4-210-228_s217-222",
     DEL + "{" + UL + "{homomorphism}}",
     DEL + "{" + UL + "{hom}}",
     "scan 221: his struck word is the abbreviation 'hom', so the mark holds 'hom' (a mark holds exactly what it holds)"),
]
waivers = [
    ("LM_C4-134-152_s140-146", "glossary: 1 terms missing",
     "scan 141: the term found is 'automorphismes des groupes à lacets " + I + "{profinis}', rendered 'automorphisms of the " + I + "{profinite} groups with loops'; his insertion stands between the words, so the pattern does not match"),
    ("LM_C4-153-171_s162-171", "glossary: 1 terms missing",
     "scan 169: 'caractère cyclotomique " + I + "{ℓ-adique}' is rendered 'cyclotomic " + I + "{ℓ-adic} character': his insertion stands between the words"),
    ("LM_C4-172-190_s172-180", "glossary: 1 terms missing",
     "scan 180: 'structures de groupe à lacets' is rendered 'group-with-loops structures', the glossary's term written as a compound; the pattern expects spaces"),
    ("LM_C4-172-190_s181-190", "glossary: 1 terms missing",
     "scan 187: 'L-autos extérieurs' and 'L-automorphismes extérieurs' are rendered 'outer L-automorphisms'; the prefix L- breaks the pattern"),
    ("LM_C4-191-209_s191-202", "glossary: 1 terms missing",
     "scan 196: 'multiplicité modulaire' twice, with his deletion and insertion between the words ('" + DEL + "{schéma} " + I + "{multiplicité} modulaire'), rendered 'modular " + DEL + "{scheme} " + I + "{multiplicity}'"),
    ("LM_C4-210-228_s217-222", "glossary: 2 terms missing",
     "scans 219 and 221: 'approximation de Lie' with his deletion and insertion inside the underlined term, rendered '" + UL + "{Lie " + DEL + "{...}" + I + "{approximation}}' and '" + UL + "{Lie} " + DEL + "{...}" + I + "{approximation}'"),
]
for unit, old, new, why in fixes:
    out = (D / "runs" / "out" / (unit + ".tex")).read_text(encoding="utf-8")
    assert out.count(old) == 1, (unit, out.count(old))
with open(D / "checks" / "FIXES.jsonl", "a", encoding="utf-8") as f:
    for unit, old, new, why in fixes:
        f.write(json.dumps({"unit": unit, "kind": "replace", "old": old, "new": new, "count": 1, "reason": why, "by": BY, "date": DATE}, ensure_ascii=False) + "\n")
with open(D / "checks" / "WAIVERS.jsonl", "a", encoding="utf-8") as f:
    for unit, fail, why in waivers:
        f.write(json.dumps({"unit": unit, "fail": fail, "reason": why, "by": BY, "date": DATE}, ensure_ascii=False) + "\n")
print(len(fixes), "fixes,", len(waivers), "waivers recorded")
