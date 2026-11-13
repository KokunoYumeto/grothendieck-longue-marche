"""Search the units of a batch for the four patterns of the faithfulness review of the pilot (12 Nov 2026), in the
output as it came back (runs/out), beside the French: (1) his m with a bar in the forms the first prompt did not cover
(a formula kept in the English, or the word dropped); (2) "homomorphism" for maps between schemes, preschemes, pairs,
spaces, topoi or sheaves; (3) "soit" that restates rendered "or"; (4) Latin (loc. cit., op. cit., a priori) put into
English. Prints one line per place, for a hand decision; writes nothing.
usage: python -I -B b02_patterns.py BATCH
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_lm as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
batch = sys.argv[1]
rec = [json.loads(x) for x in T.read(os.path.join(T.ROOT, "runs", "RUNS.jsonl")).splitlines() if x.strip()]
units = [q["unit"] for r in rec if r["event"] == "done" and r["batch"] == batch for q in r["requests"]]
M = r"\\(?:overline|bar)\{\\mathrm\{?\s*m\}?\}"
HOM_EN = re.compile(r"homomorphisms?(\s+)(of|between)(\s+)(\\deleted\{[^{}]*\}\s*)?(the\s+)?(?!group)(\w+[\s-]+)?"
                    r"(pre)?(schemes|topoi|topos|sheaves|spaces|pairs|coverings)\b", re.I)
HOM_FR = re.compile(r"\b(hom|homom|homomorphismes?)\b\.?\s+(de|entre)\s+(\S+\s+)?(pr[ée])?(schémas|topos|faisceaux|espaces|"
                    r"couples|paires|revêtements)\b(?!\s+en\s+groupes)", re.I)
LATIN = ["loc. cit", "op. cit", "a priori", "a posteriori"]


def snip(t, i, j, a=70, b=60):
    return t[max(0, i - a):j + b].replace("\n", " ")


tot = {"mbar": 0, "hom": 0, "soit": 0, "latin": 0}
for u in units:
    p = os.path.join(T.ROOT, "runs", "out", u + ".tex")
    if not os.path.exists(p):
        continue
    en = T.read(p)
    fr = T.unit_text(T.unit_map()[u])
    out = []
    # (1) m-bar: every formula holding the m with a bar, in the English
    for m in re.finditer(r"(?<!\\)\$[^$]*?" + M + r"[^$]*?(?<!\\)\$|\\\(.*?" + M + r".*?\\\)", en):
        out.append(("mbar", snip(en, m.start(), m.end())))
    # (2) homomorphism for morphisms
    nfr = len(HOM_FR.findall(T.strip_comments(fr)))
    for m in HOM_EN.finditer(en):
        out.append(("hom", snip(en, m.start(), m.end())))
    # (3) soit: \text{soit} in the French formulas against \text{or} in the English; prose "soit" before "(" or after ";"
    nsoit = len(re.findall(r"\\text\{\s*soit\s*\}|;\s*soit\b|\bsoit\s*\(|(?:^|\n)\s*soit\b|\\\]\s*soit\b",
                           T.strip_comments(fr), re.I))
    if nsoit:
        for m in re.finditer(r"\\text\{\s*or\s*\}|;\s*or\b|\bor\s*\(|(?:^|\n)\s*or\b|\\\]\s*or\b|\\deleted\{\s*or\s*\}", en):
            out.append(("soit", snip(en, m.start(), m.end())))
    # (4) Latin
    for w in LATIN:
        a, b = T.strip_comments(fr).count(w), T.strip_comments(en).count(w)
        if a > b:
            out.append(("latin", "%s: French %d, English %d" % (w, a, b)))
    for k, s in out:
        tot[k] += 1
        print("%-26s %-5s %s" % (u, k, s))
    if nfr:
        print("%-26s %-5s French 'hom de schémas/topos/faisceaux/...' places: %d" % (u, "homFR", nfr))
print("candidates:", tot)
