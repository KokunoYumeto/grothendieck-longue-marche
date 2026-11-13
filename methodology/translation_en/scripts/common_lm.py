"""Shared definitions of the English translation of La Longue Marche à travers la théorie de Galois (12 Nov 2026).

Adapted from derivateurs_translation_20261111/scripts/common_dt.py (itself from the comparison's common_tc.py). What
changed for this work: the input is the closed second pass of the transcription, one current text per package
(second_pass/CURRENT_TEXT_INDEX.tsv, column current_text); a package is a LaTeX body without preamble, its pages are
the scans (\\scanpage{n}, with \\mspage{n} for his own page numbers); a unit is a few consecutive scans of one package
(prepare.py cuts them at \\scanpage lines, about 12,000 characters each); the transcription's macros are the
apparatus macros of its check wrapper (answers/fixed/build/wrap.tex), none expanded for the glossary's running text.
Reads the glossary through its own common.py (translation_glossary_20261110/scripts). Nothing here writes outside
translation_en_20261112.
"""
import csv
import hashlib
import json
import os
import re
import sys

ROOT = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104\translation_en_20261112"
LM = r"C:\Users\user\Documents\longue_marche_pro_pilot_20261104"
INDEX = os.path.join(LM, "second_pass", "CURRENT_TEXT_INDEX.tsv")
WRAP = os.path.join(LM, "answers", "fixed", "build", "wrap.tex")
GLOSS = r"C:\Users\user\Documents\translation_glossary_20261110"
GS = os.path.join(GLOSS, "scripts")
LEDGER = r"C:\Users\user\Documents\compute_cost_ledger\LEDGER.jsonl"
HERE = os.path.dirname(os.path.abspath(__file__))
UNIT_TARGET = 12000   # characters of French per unit (prepare.py); the Dérivateurs units had about 15,000

sys.path.insert(0, GS)
import common as GC  # noqa: E402  (the glossary's own text/math separation, so the term hits agree with the CSVs)

# His "même", an m with a bar, set by the transcription as a formula of its own. NOTATION_LM (decided 10 Nov): written
# out in the English ("same", "even", "itself"). Only a formula that is nothing but the shorthand is written out; inside
# a larger formula it is copied. The formula check leaves these formulas out on both sides (check_units.py).
# Since b02 (12 Nov, change 1 of the faithfulness review of the pilot): also the plural (^{s}, ^{\mathrm s}, \mathrm{s})
# and the formulas that are nothing but a doubt between the m with a bar and a sign (= or \simeq), in either order:
# $\unsure{\overline{\mathrm m}|=}$ (the pilot's LM_C4-001-019_s1-8 had three, which the first pattern missed).
_M = r"\\(?:overline|bar)\{\\mathrm\{?\s*m\}?\}(?:\^\{\\mathrm\{?\s*s\}?\}|\^\{s\}|\^s|\\mathrm\{s\})?"
_SIGN = r"(?:=|\\simeq)"
MBAR = re.compile(r"^(?:\$|\\\()\s*(?:%s|\\unsure\{\s*%s\s*\}|\\unsure\{\s*%s\s*\|\s*%s\s*\}|\\unsure\{\s*%s\s*\|\s*%s\s*\})"
                  r"\s*(?:\$|\\\))$" % (_M, _M, _M, _SIGN, _SIGN, _M))
FOOTER = "\\texttt{https://grothendieck.umontpellier.fr}"


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, text):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def sha256(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def sha256_text(t):
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def packages():
    """The rows of CURRENT_TEXT_INDEX.tsv in manuscript order, with the absolute path of the current text."""
    rows = list(csv.DictReader(open(INDEX, encoding="utf-8"), delimiter="\t"))
    for r in rows:
        r["path"] = os.path.join(LM, r["current_text"].replace("/", os.sep))
    return rows


def manifest():
    return json.loads(read(os.path.join(ROOT, "source", "MANIFEST.json")))


def units():
    """The units in the order of the manuscript (cote 140-1, 140-2, 140-3, 140-4): dicts of MANIFEST.json."""
    return manifest()["units"]


def unit_map():
    return {u["id"]: u for u in units()}


def unit_text(u):
    """The French of a unit as it is sent: the cut without the blank lines at its ends, ending in one newline."""
    return read(os.path.join(ROOT, "source", "units", u["id"] + ".tex")).strip("\n") + "\n"


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def running_text(s):
    """The glossary's running text: comments out, formulas replaced by the mark, markup dropped; words inside
    \\text{...} of formulas appended (as build_glossary.py does). No macro is expanded (the transcription has none)."""
    s = GC.strip_comments(s)
    t, maths = GC.split_math(s)
    t = re.sub(GC.MARK + r" -(?=[A-Za-zÀ-ÿ])", GC.MARK + "-", t)
    t = re.sub(GC.MARK + r" \\[a-z]+\{-(?=[A-Za-zÀ-ÿ])", GC.MARK + "-", t)
    t = GC.detex_text(t)
    inner = " ".join(re.findall(r"\\(?:text|textit|textup|mbox|textrm)\{([^{}]*)\}", " ".join(maths)))
    return re.sub(r"\s+", " ", t + " " + inner)


def split_pages(s):
    """[(key, text)] split at the \\scanpage anchors; the key is the anchor's argument, with '#k' added to the k-th
    repetition of the same argument. Text before the first anchor, if any, is the page '^'."""
    out, seen = [], {}
    for p in re.split(r"(?=\\scanpage\{)", s):
        m = re.match(r"\\scanpage\{([^}]*)\}", p)
        if not m:
            if p.strip():
                out.append(("^", p))
            continue
        k = m.group(1)
        seen[k] = seen.get(k, 0) + 1
        out.append((k if seen[k] == 1 else "%s#%d" % (k, seen[k]), p))
    return out


def decision_lines(path):
    out = []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        out.append([x.strip() for x in re.split(r"\s;;(?:\s|$)", line)])
    return out


def glossary():
    """Entries of the glossary's decision file entries_LM.txt: (french, regex, english, source, note)."""
    return [p for p in decision_lines(os.path.join(GS, "entries_LM.txt")) if len(p) == 5]


def terms():
    """scripts/terms_LM.txt: for each glossary entry, the line the prompt carries, the regex that finds its English
    form in the translation, and the check level ('fail' or 'review'): {french: (line, regex, level)}."""
    out = {}
    for p in decision_lines(os.path.join(HERE, "terms_LM.txt")):
        assert len(p) == 4 and p[3] in ("fail", "review"), p
        out[p[0]] = (p[1], p[2], p[3])
    return out


def french_hits(ft):
    """Matches of each glossary entry in a French running text, without those inside a longer match of another entry
    (as the comparison's french_hits, over all entries); a match must start a word (check_units.py of Les
    Dérivateurs, from its batch b05)."""
    spans = {fr: [m.span() for m in re.finditer(r"(?<![^\W\d_])(?:%s)" % rx, ft, re.I)]
             for fr, rx, en, src, note in glossary() if rx != "-"}
    allspans = [(o, a, b) for o, ss in spans.items() for a, b in ss]
    out = {}
    for name, ss in spans.items():
        keep = [s for s in ss if not any(o != name and a <= s[0] and s[1] <= b and (b - a) > (s[1] - s[0])
                                         for o, a, b in allspans)]
        if keep:
            out[name] = len(keep)
    return out


def mbar_formulas(s):
    """The formulas of a text that are nothing but his m with a bar ("même")."""
    return [f for f in GC.split_math(strip_comments(s))[1] if MBAR.match(f.strip())]


def scans_of(text):
    return re.findall(r"\\scanpage\{([^}]*)\}", strip_comments(text))


def mspages_of(text):
    return re.findall(r"\\mspage\{([^}]*)\}", strip_comments(text))
