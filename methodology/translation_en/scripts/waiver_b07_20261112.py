"""Add the waiver for the one unit of batch b07 that fails the raw checks (12 Nov 2026).
usage: python -I -B waiver_b07_20261112.py"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
fr = "sous-groupes " + BS + "inserted{" + BS + "deleted{" + BS + "unsure{invariants} abéliens}}"
en = "subgroups " + BS + "inserted{" + BS + "deleted{" + BS + "unsure{invariant} abelian}}"
rec = {
    "unit": "LM_C4-020-038_s20-27",
    "fail": "glossary: 1 terms missing",
    "reason": ("scan 24: '" + fr + "' is rendered '" + en + "': his struck insertion stays where he put it, so "
               "'invariant' follows 'subgroups' and the glossary pattern (invariant ... subgroup) does not match; the "
               "term is rendered as the glossary says (as the waiver for LM_C3-587-605_s601-605, glossary across an "
               + BS + "inserted mark)"),
    "by": "Claude (Opus 5.5)",
    "date": "2026-11-12",
}
path = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\translation_en_20261112\checks\WAIVERS.jsonl"
with open(path, "a", encoding="utf-8") as f:
    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
print(sum(1 for line in open(path, encoding="utf-8") if line.strip()), "waivers")
