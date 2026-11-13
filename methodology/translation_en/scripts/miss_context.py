"""For each glossary entry missing in a unit's check (checks/raw/<unit>.md or checks/units/<unit>.md), print the French
match on its scan and the English lines of that scan that hold a related word, for a hand decision. Writes nothing.
usage: python -I -B miss_context.py [--units] UNIT ..."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_lm as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
HINT = {"automorphisme à lacets": r"morphisms?\b[^.;]{0,40}?loops?|loop[- ]\w*morph", "morphisme de topos": r"morphisms?\b.{0,25}top",
        "N.B., Rmq": r"\bN\.?\s?B\b|remark", "topos modulaire": r"modular|topo", "suite exacte": r"exact|sequence",
        "conjugaison": r"conjug", "transport de structure": r"transport", "point base": r"base",
        "homomorphisme extérieur": r"outer|exterior|external|morphism", "classe de conjugaison": r"conjug|class"}
units = [a for a in sys.argv[1:] if not a.startswith("--")]
sub = "units" if "--units" in sys.argv else "raw"
gl = {e[0]: e for e in T.glossary()}
for u in units:
    md = T.read(os.path.join(T.ROOT, "checks", sub, u + ".md"))
    um = T.unit_map()[u]
    en_p = os.path.join(T.ROOT, "runs", "out", u + ".tex") if sub == "raw" else \
        os.path.join(T.ROOT, "translation", "units", um["package"], u + ".tex")
    fr, en = dict(T.split_pages(T.unit_text(um))), dict(T.split_pages(T.read(en_p)))
    for m in re.finditer(r"^- missing: (.+?) \(scan (\S+?), \d+ in the French\)", md, re.M):
        name, scan = m.group(1), m.group(2)
        ft = T.running_text(fr.get(scan, ""))
        fm = [ft[max(0, x.start() - 50):x.end() + 30] for x in re.finditer(r"(?<![^\W\d_])(?:%s)" % gl[name][1], ft, re.I)]
        et = T.running_text(en.get(scan, ""))
        em = [et[max(0, x.start() - 50):x.end() + 40] for x in re.finditer(HINT.get(name, re.escape(name.split()[0])), et, re.I)]
        print("%s | %s | scan %s\n   FR: %s\n   EN: %s" % (u, name, scan, " || ".join(fm)[:260], " || ".join(em)[:330]))
