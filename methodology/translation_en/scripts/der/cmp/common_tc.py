"""Shared definitions of the translation comparison of 11 Nov 2026 (read-only on every source file).

The two French samples, the glossary machinery (the decision files of translation_glossary_20261110, read through its
own common.py), and small helpers. Nothing here writes outside C:\\Users\\user\\Documents\\translation_comparison_20261111.
"""
import hashlib
import os
import re
import sys

ROOT = r"C:\Users\user\Documents\translation_comparison_20261111"
GLOSS = r"C:\Users\user\Documents\translation_glossary_20261110"
GS = os.path.join(GLOSS, "scripts")
LM_FILE = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\second_pass\LM_P049_checked.tex"
DER_FILE = r"C:\Users\user\Documents\derivateurs_companion_20261109\corrected_french_20261111\DER_XVIII-a.tex"
LEDGER = r"C:\Users\user\Documents\compute_cost_ledger\LEDGER.jsonl"

sys.path.insert(0, GS)
import common as GC  # noqa: E402  (the glossary's own text/math separation, so counts agree with the CSVs)

# The samples: (work, label, file, first anchor, anchor after the last page, pages)
SAMPLES = {
    "LM": dict(file=LM_FILE, start=r"\scanpage{483}", stop=r"\scanpage{488}", pages=5,
               what="La Longue Marche, package LM_P049 (second pass), scans 483-487 (manuscript pages 245-247)",
               head="La Longue Marche, scans 483-487, manuscript pages 245-247"),
    "DER": dict(file=DER_FILE, start=r"\printedpage{1}", stop=r"\printedpage{6}", pages=5,
                what="Les Dérivateurs, Ch. XVIII (chunk DER_XVIII-a, corrected French of 11 Nov), edition pages 1-5 "
                     "(manuscript pages 50-60)",
                head="Les Dérivateurs, chapter XVIII, edition pages 1-5, manuscript pages 50-60"),
}
# The reference configuration (Fable 5.2 at max) translates one page of each work: the first page of each sample.
REF = {
    "LM": dict(file=LM_FILE, start=r"\scanpage{483}", stop=r"\scanpage{484}", pages=1,
               what="La Longue Marche, package LM_P049 (second pass), scan 483",
               head="La Longue Marche, scan 483, manuscript page 245"),
    "DER": dict(file=DER_FILE, start=r"\printedpage{1}", stop=r"\printedpage{2}", pages=1,
                what="Les Dérivateurs, Ch. XVIII (chunk DER_XVIII-a), edition page 1",
                head="Les Dérivateurs, chapter XVIII, edition page 1, manuscript pages 50-52"),
}


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def sha256(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def cut(spec):
    s = read(spec["file"])
    i = s.index(spec["start"])
    j = s.index(spec["stop"], i)
    return s[i:j].rstrip() + "\n", s[:i].count("\n") + 1, s[:j].rstrip().count("\n") + 1


def decision_lines(name):
    out = []
    for line in open(os.path.join(GS, name), encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        out.append([x.strip() for x in re.split(r"\s;;(?:\s|$)", line)])
    return out


def glossary(work):
    """Entries of entries_<work>.txt: (french, regex, english, source, note)."""
    return [p for p in decision_lines("entries_%s.txt" % work) if len(p) == 5]


def der_macros():
    return GC.preamble_macros(read(DER_FILE))


def running_text(s, work):
    """The glossary's running text: comments out, (DER) macros expanded, formulas replaced by the mark, markup dropped;
    words inside \\text{...} of formulas appended (as build_glossary.py does)."""
    d = der_macros() if work == "DER" else {}
    s = GC.expand(GC.strip_comments(s), d)
    t, maths = GC.split_math(s)
    t = re.sub(GC.MARK + r" -(?=[A-Za-zÀ-ÿ])", GC.MARK + "-", t)
    t = re.sub(GC.MARK + r" \\[a-z]+\{-(?=[A-Za-zÀ-ÿ])", GC.MARK + "-", t)
    t = GC.detex_text(t)
    inner = " ".join(re.findall(r"\\(?:text|textit|textup|mbox|textrm)\{([^{}]*)\}", " ".join(maths)))
    return re.sub(r"\s+", " ", t + " " + inner)


def split_pages(s, work):
    """[(anchor, text)] split at the page anchors of the work."""
    pat = r"(?=\\scanpage\{)" if work == "LM" else r"(?=\\printedpage\{)"
    out = []
    for p in re.split(pat, s):
        m = re.match(r"\\(?:scanpage|printedpage)\{([^}]*)\}", p)
        if m:
            out.append((m.group(1), p))
    return out
