"""Show, for each glossary miss of the last batches, the glossary entry, the French around the term and the English of
the same scan (read-only). usage: python -I -B show_glossary_misses_20261113.py"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
D = Path(r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\translation_en_20261112")
CASES = [("LM_C4-134-152_s140-146", 141, "automorphisme"), ("LM_C4-153-171_s162-171", 169, "cyclotomique"),
         ("LM_C4-172-190_s172-180", 180, "à lacets"), ("LM_C4-172-190_s181-190", 187, "extérieur"),
         ("LM_C4-191-209_s191-202", 196, "multiplicit"), ("LM_C4-210-228_s217-222", 219, "approximation"),
         ("LM_C4-210-228_s217-222", 221, "approximation")]
terms = (D / "scripts" / "terms_LM.txt").read_text(encoding="utf-8").splitlines()


def scan(s, k):
    m = BS + "scanpage{%d}" % k
    i = s.find(m)
    if i < 0:
        return ""
    j = s.find(BS + "scanpage{", i + len(m))
    return s[i:j if j > 0 else len(s)]


EN_HINT = {"automorphisme": "automorphism", "cyclotomique": "cyclotomic", "à lacets": "loop", "extérieur": "outer|exterior",
           "multiplicit": "multiplicit", "approximation": "approximation"}
for unit, k, key in CASES:
    print("=" * 100)
    print(unit, "scan", k, "| glossary:", [t for t in terms if key.split()[0] in t and ";;" in t][:2])
    fr = scan((D / "source" / "units" / (unit + ".tex")).read_text(encoding="utf-8"), k)
    en = scan((D / "runs" / "out" / (unit + ".tex")).read_text(encoding="utf-8"), k)
    for m in re.finditer(re.escape(key), fr):
        print("  FR:", " ".join(fr[max(0, m.start() - 160):m.end() + 120].split()))
    for m in re.finditer(EN_HINT[key], en, re.I):
        print("  EN:", " ".join(en[max(0, m.start() - 160):m.end() + 120].split()))
