"""Shared definitions of the English translation of Les Dérivateurs (11 Nov 2026).

Adapted from translation_comparison_20261111/scripts/common_tc.py. What scale changed: the units are the five-page
files of the transcription (the source of record: derivateurs_publish_20261111/repo/transcription, release
v2026-11-11b), each a complete LaTeX document with its own preamble and macros, so the macros used to read a unit
are that unit's own; the page keys tell apart the unnumbered pages (\\printedpage{--} and the like), which can occur
twice in one unit. Reads the glossary through its own common.py (translation_glossary_20261110/scripts), so the
running text is the one the glossary was counted on. Nothing here writes outside derivateurs_translation_20261111.
"""
import hashlib
import os
import re
import sys

ROOT = r"C:\Users\user\Documents\derivateurs_translation_20261111"
REPO = r"C:\Users\user\Documents\derivateurs_publish_20261111\repo"
SRC = os.path.join(REPO, "transcription")
RELEASE = "v2026-11-11b"
COMMIT = "f42cfdd0831efc294d8269f9cc62ea3150e35f0c"
GLOSS = r"C:\Users\user\Documents\translation_glossary_20261110"
GS = os.path.join(GLOSS, "scripts")
CMP = r"C:\Users\user\Documents\translation_comparison_20261111"
LEDGER = r"C:\Users\user\Documents\compute_cost_ledger\LEDGER.jsonl"
HERE = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, GS)
import common as GC  # noqa: E402  (the glossary's own text/math separation, so the term hits agree with the CSVs)

BD, ED = "\\begin{document}", "\\end{document}"
BABEL_FR, BABEL_EN = "\\usepackage[french]{babel}", "\\usepackage[french,english]{babel}"
# Macros of the preambles whose definitions print French words, and the English they print in the English units
# (assemble.py; the checks read the English with them). Decided by Claude, 11 Nov 2026, after batch b02:
#   \pl (chapter II) prints "[plutôt": the glossary's "[plutôt ...] → [rather ...]";
#   \defeq, \deq, \deff, \dfeq print "déf" over "=": NOTATION_DER "equal by definition" (English: "def");
#   \cardred, \red, \redop (chapters VII and XVIII) print "réd" ("cardinal réduit", reduced cardinal): "red".
MACRO_EN = [("\\texttt{[plutôt}", "\\texttt{[rather}"), ("{déf}", "{def}"), ("\\upshape déf}", "\\upshape def}")]
MACRO_EN_RX = [(r"(?<![A-Za-zÀ-ÿ])réd(?![A-Za-zÀ-ÿ])", "red"), (r"r\\acute\{e\}d(?![A-Za-z])", "red")]
# Page anchors whose argument carries French words (printed in the margin). The model keeps every anchor as it is
# (they align the English with the French); the English units carry these English forms (assemble.py), and the checks
# read both texts with them. Decided by Claude, 11 Nov 2026. "quater", "quinquies" and primes stay as they are.
ANCHOR_EN = {
    "\\msp{48 vide}": "\\msp{48 blank}",
    "\\msp{page 114 vide}": "\\msp{page 114 blank}",
    "\\msp{page 170 manque}": "\\msp{page 170 missing}",
    "\\msp{page 2 n'existe pas}": "\\msp{page 2 does not exist}",
    "\\msp{page 22 vide}": "\\msp{page 22 blank}",
    "\\msp{page 32 vide}": "\\msp{page 32 blank}",
    "\\msp{page 320 biffé}": "\\msp{page 320 struck out}",
    "\\msp{page 48 (vide)}": "\\msp{page 48 (blank)}",
    "\\msp{page 49$'$ (il y a un décalage dans la numérotation)}": "\\msp{page 49$'$ (the numbering is shifted)}",
    "\\msp{page 68 vide}": "\\msp{page 68 blank}",
    "\\msp{page 78 barrée}": "\\msp{page 78 crossed out}",
    "\\printedpage{(non numérotée)}": "\\printedpage{(unnumbered)}",
    "\\printedpage{[non numérotée]}": "\\printedpage{[unnumbered]}",
    "\\printedpage{[sans numéro]}": "\\printedpage{[no number]}",
}


def english_anchors(text):
    for a, b in ANCHOR_EN.items():
        text = text.replace(a, b)
    return text
DEFLINE = re.compile(r"\s*\\((re)?newcommand|providecommand|DeclareRobustCommand|def\\)")


def english_preamble(pre):
    """A unit's preamble for its English: babel's main language English (French stays loaded for the \\frenchsetup
    lines of some preambles), and the macro definitions of MACRO_EN in English. Nothing else changes."""
    if pre.count(BABEL_FR) != 1:
        raise ValueError("babel line not found once")
    out = []
    for line in pre.replace(BABEL_FR, BABEL_EN).split("\n"):
        if DEFLINE.match(line):
            for a, b in MACRO_EN:
                line = line.replace(a, b)
            for a, b in MACRO_EN_RX:
                line = re.sub(a, b, line)
        out.append(line)
    return "\n".join(out)

# The edition's files in order (as kit/build_transcription_master.py of the repository): folder, the phrase that
# names it in the prompt, the English heading and title for the contents of the English book (titles: Claude).
FILES = [
    ("dertbmt", "the table of contents", "Table of contents", ""),
    ("Der-ChI-234", "chapter I", "Chapter I", "Generalities on (pre)derivators"),
    ("Der-ChII-234", "chapter II", "Chapter II",
     "Cofinality (on the right and on the left) (preliminary to cohomological cofinality)"),
    ("Der-ChIII-567", "chapter III", "Chapter III", "External Hom in derivators"),
    ("Der-ChIV-567", "chapter IV", "Chapter IV", "Substantial diagrams"),
    ("Der-ChV-234", "chapter V", "Chapter V", "Categories of paths and localization"),
    ("Der-ChVI-345", "chapter VI", "Chapter VI", "HOT"),
    ("Der-ChVII-456", "chapter VII", "Chapter VII", "Categories of paths (2)"),
    ("Der-ChVIII-567", "chapter VIII", "Chapter VIII", "Relative homotopy 1-types: their integration\\,\\dots"),
    ("Der-ChIX-678", "chapter IX", "Chapter IX",
     "Return to the categories of fractions $\\mathcal{M}W^{-1}$, comparison with Quillen"),
    ("Der-ChX-789", "chapter X", "Chapter X", "Comparison of Cat with $\\boldsymbol{\\Delta}^{\\wedge}$"),
    ("Der-ChXI-890", "chapter XI", "Chapter XI", "Hot-fibrations, proper functors and smooth functors etc. (in Cat)"),
    ("Der-ChXIIa-012", "chapter XII, sections 1-4", "Chapter XII, sections 1--4",
     "Characterization of $W_\\infty$. $W$-proper, $W$-smooth functors etc. Amalgamated sums and "
     "$W$-cocartesian squares in Cat"),
    ("Der-ChXIIb-012", "chapter XII, section 5", "Chapter XII, section 5", ""),
    ("Der-ChXIIc-30-03-03", "chapter XII, section 6", "Chapter XII, section 6", ""),
    ("Der-ChXIIapp-19-06-03", "the appendix to chapter XII", "Appendix to Chapter XII", ""),
    ("Der-ChXIII-25-01-04", "chapter XIII", "Chapter XIII", "Categories of models (1)"),
    ("Der-ChXIV-07-10-10", "chapter XIV", "Chapter XIV", "h-cartesian and h-cocartesian squares"),
    ("Der-ChXV-05-11-10", "chapter XV", "Chapter XV", "Factorization theorems (Models (2))"),
    ("der-ch16", "chapter XVI", "Chapter XVI", "The basic localizers"),
    ("der-ch17", "chapter XVII", "Chapter XVII", "Categories with fibrations and with cofibrations (Models (3))"),
    ("der-ch18", "chapter XVIII", "Chapter XVIII", "Accessible categories and sets"),
    ("der-ch19", "chapter XIX", "Chapter XIX", "Models (4)"),
]
VERSIONS = {  # the version printed at the foot of each edition file (kit/build_transcription_master.py)
    "Der-ChI-234": "8 July 2001", "Der-ChII-234": "8 July 2001", "Der-ChIII-567": "2 February 2002",
    "Der-ChIV-567": "2 February 2002", "Der-ChV-234": "9 September 2001", "Der-ChVI-345": "9 November 2001",
    "Der-ChVII-456": "22 December 2001", "Der-ChVIII-567": "2 February 2002", "Der-ChIX-678": "12 March 2002",
    "Der-ChX-789": "9 April 2002", "Der-ChXI-890": "28 May 2002", "Der-ChXIIa-012": "7 December 2002",
    "Der-ChXIIb-012": "7 December 2002", "Der-ChXIIc-30-03-03": "30 March 2003",
    "Der-ChXIIapp-19-06-03": "20 June 2003", "Der-ChXIII-25-01-04": "25 January 2004",
    "Der-ChXIV-07-10-10": "7 October 2010", "Der-ChXV-05-11-10": "5 November 2010", "der-ch16": "18 March 2019",
    "der-ch17": "9 February 2019", "der-ch18": "17 December 2025", "der-ch19": "11 February 2019",
}


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


def units():
    """Every five-page file of the transcription, in the order of the book: dict(id, folder, phrase, src)."""
    out = []
    for folder, phrase, _, _ in FILES:
        d = os.path.join(SRC, folder)
        names = [f for f in os.listdir(d) if re.match(re.escape(folder) + r"_p\d+-\d+\.tex$", f)]
        names.sort(key=lambda f: int(re.search(r"_p(\d+)-", f).group(1)))
        for f in names:
            out.append({"id": f[:-4], "folder": folder, "phrase": phrase, "src": os.path.join(d, f)})
    return out


def unit_map():
    return {u["id"]: u for u in units()}


def split_doc(s):
    """(preamble, body) of a complete LaTeX document."""
    i = s.index(BD)
    j = s.rindex(ED)
    return s[:i], s[i + len(BD):j]


def body_text(s):
    """The text of a unit that is translated: the body without the blank lines at its ends, ending in one newline."""
    return split_doc(s)[1].strip("\n") + "\n"


def macros_of(pre):
    return GC.preamble_macros(pre + BD)


def running_text(s, macros):
    """The glossary's running text: comments out, the unit's macros expanded, formulas replaced by the mark, markup
    dropped; words inside \\text{...} of formulas appended (as build_glossary.py does)."""
    s = GC.expand(GC.strip_comments(s), macros)
    t, maths = GC.split_math(s)
    t = re.sub(GC.MARK + r" -(?=[A-Za-zÀ-ÿ])", GC.MARK + "-", t)
    t = re.sub(GC.MARK + r" \\[a-z]+\{-(?=[A-Za-zÀ-ÿ])", GC.MARK + "-", t)
    t = GC.detex_text(t)
    inner = " ".join(re.findall(r"\\(?:text|textit|textup|mbox|textrm)\{([^{}]*)\}", " ".join(maths)))
    return re.sub(r"\s+", " ", t + " " + inner)


def split_pages(s):
    """[(key, text)] split at the \\printedpage anchors; the key is the anchor's argument, with '#k' added to the
    k-th repetition of the same argument (two unnumbered pages in one unit). Text before the first anchor, if any,
    is the page '^'."""
    out, seen = [], {}
    parts = re.split(r"(?=\\printedpage\{)", s)
    for p in parts:
        m = re.match(r"\\printedpage\{([^}]*)\}", p)
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
    """Entries of the glossary's decision file entries_DER.txt: (french, regex, english, source, note)."""
    return [p for p in decision_lines(os.path.join(GS, "entries_DER.txt")) if len(p) == 5]


def terms():
    """scripts/terms_DER.txt: for each glossary entry, the line the prompt carries and the regex that finds its
    English form in the translation: {french: (line, regex)}."""
    out = {}
    for p in decision_lines(os.path.join(HERE, "terms_DER.txt")):
        assert len(p) == 3, p
        out[p[0]] = (p[1], p[2])
    return out


def pages_of(text):
    """Edition pages of a unit: its \\printedpage anchors (the unnumbered ones count)."""
    return len(re.findall(r"\\printedpage\{", GC.strip_comments(text)))
