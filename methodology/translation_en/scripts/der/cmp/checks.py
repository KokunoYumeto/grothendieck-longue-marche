"""Script checks of every translation (no API call). For each output runs/<config>/<sample>.tex against
source/<sample>.tex:

1. formulas and macros back unchanged: every formula (inline $...$, \\[...\\], $$...$$, math environments) compared in
   order with the French, the wording inside \\text{...} masked (it is translated); identical / identical up to spacing
   / changed / missing / added. Page anchors (\\scanpage, \\mspage, \\printedpage, \\msp with their arguments) in order;
   comment lines; the count of every macro outside formulas; the bars of \\unsure{A|B}.
2. no French sentence left: French function words and elisions in the running text of the English (comments and
   formulas removed), sentences with several of them, and accented words; and French left in the wording inside
   \\text{...} of the formulas (which is to be translated).
3. each paragraph's length against the French: paragraphs split at blank lines, paired in order, the length of the
   running text (formulas and macro names removed) English / French.
4. the glossary terms used where their French occurs: for each glossary entry found on a French page (the regex of the
   decision file, as in the glossary build), whether its English form occurs on the same page of the translation;
   and the count of British spellings (the glossary decided American spelling).

Writes checks/CHECKS.json and checks/<config>_<sample>.md. usage: python -I -B checks.py [CONFIG ...]
"""
import difflib
import json
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_tc as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
RUNS = os.path.join(T.ROOT, "runs")
OUT = os.path.join(T.ROOT, "checks")

# ---------------------------------------------------------------- the English form of each glossary entry found
EN = {
    "LM": {
        "groupe à lacets": r"groups? with loops", "structure à lacets": r"loop[- ]structures?", "lacet": r"\bloops?\b",
        "sous-groupe à lacets": r"loop[- ]subgroups?", "action extérieure": r"outer (actions?|operations?)",
        "groupe extérieur": r"outer (\w+ )?(§-)?groups?", "anabélien": r"anabelian\w*",
        "prédiscrétification": r"prediscretification",
        "arithmétisation": r"arithmetiz\w+", "bouchage de trous": r"\bplug\w*", "trou": r"\bholes?\b",
        "germe": r"\bgerms?\b", "relèvement admissible": r"admissible (liftings?|actions?)|admissibility",
        "relèvement": r"\bliftings?\b", "scindage": r"\bsplit\w*", "structure d'extension": r"extension structures?",
        "sous-groupe": r"subgroups?", "sous-groupe ouvert, d'indice fini":
        r"open (\w+ )?subgroups?|subgroups? of finite index",
        "groupe profini": r"profinite", "extension": r"extensions?", "noyau": r"\bkernels?\b", "commutant": r"commutant",
        "centralisateur, normalisateur, stabilisateur": r"centralizers?|normalizers?|stabilizers?",
        "centre": r"\bcenters?\b", "conjugaison": r"conjugat\w+|conjugacy", "classe de conjugaison": r"conjugacy class\w*",
        "opérer, opération": r"\boperat\w+", "action": r"\bactions?\b", "fidèle, fidèlement": r"faithful\w*",
        "revêtement": r"\bcover\w*", "point base": r"base[- ]?points?", "surface, genre, bord": r"\bgenus\b|\bgenera\b",
        "orientation": r"\borient\w+", "courbe elliptique, courbe algébrique": r"algebraic (\w+ )?curves?",
        "pleinement fidèle": r"fully faithful|full faithfulness", "passage au quotient": r"passage to the quotient",
        "N.B., Rmq": r"\bN\.\s?B\.?", "hom, isom, autom": r"(homo|iso|auto|endo)morphisms?", "tt, tte, ts, tjrs":
        r"\bevery\b|\ball\b|\balways\b", "pt, élt, mb": r"\bpoints?\b|\belements?\b",
        "néc., gén., loc., can., alg., géom., top.": r"algebraic|canonical\w*|geometric\w*|\bouter\b|extension",
        "i.e., cf., resp.": r"\bi\.e\.|\bcf\.|\bresp\.",
    },
    "DER": {
        "flèche": r"\barrows?\b", "sous-catégorie pleine": r"full (\w+ ){0,2}subcategor(y|ies)", "pleinement fidèle":
        r"fully faithful|full faithfulness", "image essentielle": r"essential image", "petite catégorie":
        r"small (\w+ ){0,3}(sub)?categor(y|ies)", "paratopos": r"paratop(os|oi)\b", "pseudo-topos": r"pseudo-?(§-)?top(os|oi)\b",
        "topos": r"(?<!para)(?<!pseudo-)(?<!-)\btop(os|oi)\b", "préfaisceau, faisceau": r"\b(pre)?shea(f|ves)\b",
        "U-catégorie, U-petit": r"§-(categor(y|ies)|small)", "strictement génératrice": r"strictly generating",
        "épimorphisme strict, "
        "famille épimorphique stricte": r"strict epimorphi\w+", "stable par": r"stable under", "limite inductive":
        r"direct limits?", "limite projective": r"inverse limits?", "contrafoncteur": r"contrafunctors?",
        "adjoint à gauche, à droite": r"(left|right) adjoints?", "flèche d'adjonction":
        r"adjunction (arrows?|morphisms?)", "exact à gauche, à droite": r"(left|right)[- ]exact\w*",
        "factorisation": r"factorization", "monomorphisme, épimorphisme": r"(mono|epi)morphisms?",
        "N.B.": r"\bN\.\s?B\.", "i.e., cf., resp., p. ex.": r"\bi\.e\.|\bcf\.|\bresp\.|\be\.g\.",
    },
}
BRITISH = re.compile(r"\b(centres?|fibres?|fibred|neighbourhoods?|colou?rs?|behaviour|realis\w*|generalis\w*|"
                     r"recognis\w*|characteris\w*|localis\w*|normalis\w*|analys(e|es|ed|ing)|\w+isations?|"
                     r"\w+ising|organis\w*|arithmetis\w*|discretis\w*|rigidis\w*)\b", re.I)
BRITISH_OK = {"colors", "color", "analysis"}
FRENCH = set("""le la les des du au aux une est sont que qui dans avec sur cette ces cet mais donc ainsi pas très nous
je il elle ils elles leur leurs aussi comme entre où sans sous vers chez déjà encore toujours après avant depuis peut
faut fait été cela ceci ça quand lorsque puis alors tout toute tous toutes soit et ou un dont lequel laquelle lesquels
celle celui ceux ici sera serait était avait ont avons être avoir même plutôt notamment ne se sa son ses mon ma mes
on""".split())
FRENCH_IN_ENGLISH = {"on"}  # "on" is an English word too: counted, never decisive
ACCENT = re.compile(r"[àâçéèêëîïôûùüÿœ]", re.I)
ACCENT_OK = {"étale", "dévissage", "teichmüller", "künzer"}
MATH = re.compile(r"\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\\)\$.*?(?<!\\)\$|\\begin\{(" + T.GC.MATH_ENVS +
                  r")\}.*?\\end\{\1\}", re.S)
ANCHOR = re.compile(r"\\(scanpage|mspage|printedpage|msp)(?![A-Za-z])")
TEXTBOX = re.compile(r"\\(text|textrm|textup|textit|textbf|mbox|hbox)(?![A-Za-z])\s*\{")


def arg_end(s, i):
    """Index after the brace group that opens at s[i] == '{'."""
    depth = 0
    for k in range(i, len(s)):
        c = s[k]
        if c == "\\":
            continue
        if c == "{" and (k == 0 or s[k - 1] != "\\"):
            depth += 1
        elif c == "}" and s[k - 1] != "\\":
            depth -= 1
            if depth == 0:
                return k + 1
    return len(s)


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def comments(s):
    return [m.group(0).rstrip() for m in re.finditer(r"(?<!\\)%.*", s)]


def mask_text(f):
    """Replace the argument of every \\text{...}-like box inside a formula by a dot."""
    out, i = [], 0
    for m in TEXTBOX.finditer(f):
        if m.start() < i:
            continue
        b = m.end() - 1
        e = arg_end(f, b)
        out.append(f[i:b] + "{·}")
        i = e
    out.append(f[i:])
    return "".join(out)


def formulas(s):
    s = strip_comments(s)
    return [re.sub(r"\s+", " ", mask_text(m.group(0))).strip() for m in MATH.finditer(s)]


def anchors(s):
    s = strip_comments(s)
    out = []
    for m in ANCHOR.finditer(s):
        j = m.end()
        if j < len(s) and s[j] == "{":
            out.append("\\%s%s" % (m.group(1), s[j:arg_end(s, j)]))
        else:
            out.append("\\" + m.group(1))
    return out


def macro_counts(s):
    t = MATH.sub(" ", strip_comments(s))
    c = {}
    for m in re.finditer(r"\\([A-Za-z]+\*?)", t):
        c[m.group(1)] = c.get(m.group(1), 0) + 1
    return c


def unsure_bars(s):
    """Number of top-level bars inside \\unsure{...} arguments (outside and inside formulas)."""
    s = strip_comments(s)
    n = 0
    for m in re.finditer(r"\\unsure\{", s):
        b = m.end() - 1
        e = arg_end(s, b)
        inner, depth = s[b + 1:e - 1], 0
        for k, c in enumerate(inner):
            if c == "{" and (k == 0 or inner[k - 1] != "\\"):
                depth += 1
            elif c == "}" and inner[k - 1] != "\\":
                depth -= 1
            elif c == "|" and depth == 0 and (k == 0 or inner[k - 1] != "\\"):
                n += 1
    return n


def empty_marks(s):
    return len(re.findall(r"\\(deleted|inserted|unsure|margin|uline)\{\s*\}", s))


MARKS = ("deleted", "inserted", "unsure", "illegible", "margin", "uline", "uuline", "footnote", "texttt", "textit",
         "textbf", "section", "subsection")


def marks_by_page(fr, en, work):
    """Pages where the number of a mark (anywhere, formulas included) differs: ["483 deleted 4→3", ...]."""
    pe = dict(T.split_pages(en, work))
    out = []
    for page, tf in T.split_pages(fr, work):
        te = pe.get(page, "")
        for m in MARKS:
            a = len(re.findall(r"\\%s(?![A-Za-z])" % m, strip_comments(tf)))
            b = len(re.findall(r"\\%s(?![A-Za-z])" % m, strip_comments(te)))
            if a != b:
                out.append("%s %s %d→%d" % (page, m, a, b))
    return out


def prose(s):
    """Running text: comments and formulas out, anchors out, macro names out (their arguments kept)."""
    t = MATH.sub(" § ", strip_comments(s))
    t = re.sub(r"\\(scanpage|mspage|printedpage|msp|illegible|tag\*?|label|ref|vspace\*?|hspace\*?|setcounter)"
               r"\{[^{}]*(\{[^{}]*\}[^{}]*)*\}", " ", t)
    t = re.sub(r"\\footnote\[[^\]]*\]", " ", t)
    t = re.sub(r"\\(begin|end)\{[^{}]*\}(\[[^\]]*\])?", " ", t)
    t = re.sub(r"\\[A-Za-z]+\*?", " ", t)
    t = re.sub(r"\\.", " ", t)
    t = t.replace("{", " ").replace("}", " ").replace("~", " ")
    return re.sub(r"\s+", " ", t).strip()


def paragraphs(s):
    return [p for p in re.split(r"\n[ \t]*\n", s) if p.strip()]


def compare_formulas(fr, en):
    F, E = formulas(fr), formulas(en)
    sm = difflib.SequenceMatcher(None, F, E, autojunk=False)
    res = {"french": len(F), "english": len(E), "identical": 0, "spacing_only": 0, "changed": [], "missing": [],
           "added": []}
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == "equal":
            res["identical"] += a2 - a1
            continue
        fa, eb = F[a1:a2], E[b1:b2]
        nows = [re.sub(r"\s", "", x) for x in eb]
        left = []
        for f in fa:
            k = re.sub(r"\s", "", f)
            if k in nows:
                j = nows.index(k)
                nows[j] = None
                eb[j] = None
                res["spacing_only"] += 1
            else:
                left.append(f)
        rest = [x for x in eb if x is not None]
        for f, e in zip(left, rest):
            res["changed"].append([f, e])
        res["missing"] += left[len(rest):]
        res["added"] += rest[len(left):]
    return res


def formula_texts(s):
    """The wording inside \\text{...}-like boxes of the formulas."""
    out = []
    for m in MATH.finditer(strip_comments(s)):
        f = m.group(0)
        for b in TEXTBOX.finditer(f):
            j = b.end() - 1
            inner = f[j + 1:arg_end(f, j) - 1]
            inner = re.sub(r"\\[A-Za-z]+\*?", " ", inner)
            inner = re.sub(r"\$[^$]*\$", " ", inner)
            if re.search(r"[A-Za-zÀ-ÿ]", inner):
                out.append(inner.strip())
    return out


def french_in_formula_text(s):
    bad = []
    for x in formula_texts(s):
        ws = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ]+", x)
        if any(w.lower() in FRENCH and w.lower() not in FRENCH_IN_ENGLISH for w in ws) or \
                any(ACCENT.search(w) and w.lower() not in ACCENT_OK for w in ws) or \
                any(w.lower() in ("pl", "fid") for w in ws):
            bad.append(x)
    return bad


def french_left(en):
    t = prose(en)
    elisions = re.findall(r"\b(?:l|d|qu|j|n|c|s)['’](?=[A-Za-zÀ-ÿ])", t, re.I)
    words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ]+", t)
    fw = [w for w in words if w.lower() in FRENCH]
    counts = {}
    for w in fw:
        counts[w.lower()] = counts.get(w.lower(), 0) + 1
    flagged = []
    for chunk in re.split(r"[.;:!?]\s|\n|§|\(|\)", t):
        ws = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ]+", chunk)
        fr = [w for w in ws if w.lower() in FRENCH and w.lower() not in FRENCH_IN_ENGLISH]
        el = re.findall(r"\b(?:l|d|qu|j|n|c|s)['’](?=[A-Za-zÀ-ÿ])", chunk, re.I)
        n = len(fr) + len(el)
        if (n >= 2 and n / max(len(ws), 1) >= 0.25) or n >= 4:
            flagged.append(chunk.strip()[:160])
    acc = sorted({w for w in words if ACCENT.search(w) and w.lower() not in ACCENT_OK})
    return {"french_words": sum(v for k, v in counts.items() if k not in FRENCH_IN_ENGLISH),
            "french_word_counts": {k: v for k, v in sorted(counts.items()) if k not in FRENCH_IN_ENGLISH},
            "elisions": len(elisions), "flagged_sentences": flagged, "accented_words": acc,
            "french_in_formula_text": french_in_formula_text(en), "formula_texts": len(formula_texts(en))}


def para_lengths(fr, en):
    PF, PE = paragraphs(fr), paragraphs(en)

    def sig(p):
        return tuple(re.sub(r"\s", "", x) for x in formulas(p)) + tuple(anchors(p))
    pairs = []
    if len(PF) == len(PE):
        pairs = list(zip(PF, PE))
        unmatched = 0
    else:
        sm = difflib.SequenceMatcher(None, [sig(p) for p in PF], [sig(p) for p in PE], autojunk=False)
        unmatched = 0
        for op, a1, a2, b1, b2 in sm.get_opcodes():
            if op == "equal" or (a2 - a1) == (b2 - b1):
                pairs += list(zip(PF[a1:a2], PE[b1:b2]))
            else:
                unmatched += max(a2 - a1, b2 - b1)
    ratios, flagged = [], []
    for p, q in pairs:
        lf, le = len(prose(p)), len(prose(q))
        if lf < 30:
            continue
        r = le / lf
        ratios.append(r)
        if r < 0.7 or r > 1.5:
            flagged.append({"ratio": round(r, 2), "french": prose(p)[:120], "english": prose(q)[:120]})
    return {"paragraphs_french": len(PF), "paragraphs_english": len(PE), "unmatched": unmatched,
            "ratio_median": round(statistics.median(ratios), 3) if ratios else None,
            "ratio_min": round(min(ratios), 3) if ratios else None, "ratio_max": round(max(ratios), 3) if ratios else None,
            "ratio_total": round(len(prose(en)) / max(len(prose(fr)), 1), 3), "flagged": flagged,
            "measured": len(ratios)}


def french_hits(ft, work):
    """Matches of each glossary entry in a French running text, without the matches that lie inside a longer match of
    another entry (so "groupes à lacets" inside "sous-groupes à lacets" counts for the loop subgroup only)."""
    gl = {e[0]: e for e in T.glossary(work)}
    spans = {name: [m.span() for m in re.finditer(gl[name][1], ft, re.I)] for name in EN[work]}
    out = {}
    for name, ss in spans.items():
        keep = [s for s in ss if not any(o != name and a <= s[0] and s[1] <= b and (b - a) > (s[1] - s[0])
                                         for o, os_ in spans.items() for a, b in os_)]
        if keep:
            out[name] = len(keep)
    return out


def glossary_check(fr, en, work):
    def clean(s):
        return re.sub(r"\\illegible\{[^{}]*\}", " ", s)
    pf, pe = dict(T.split_pages(clean(fr), work)), dict(T.split_pages(clean(en), work))
    pairs, present, occ_fr, occ_en, missing, fewer = 0, 0, 0, 0, [], []
    for page, ftext in pf.items():
        etext = pe.get(page, clean(en) if not pe else "")
        ft, et = T.running_text(ftext, work), T.running_text(etext, work)
        hits = french_hits(ft, work)
        for name, rx in EN[work].items():
            nf = hits.get(name, 0)
            if not nf:
                continue
            ne = len(re.findall(rx, et, re.I))
            pairs += 1
            present += ne > 0
            occ_fr += nf
            occ_en += min(ne, nf)
            if not ne:
                missing.append("%s (page %s, %d in the French)" % (name, page, nf))
            elif ne < nf:
                fewer.append("%s (page %s: %d in the French, %d in the English)" % (name, page, nf, ne))
    brit = [m.group(0) for m in BRITISH.finditer(prose(en)) if m.group(0).lower() not in BRITISH_OK]
    return {"entry_pages": pairs, "present": present, "occurrences_french": occ_fr, "occurrences_covered": occ_en,
            "missing": missing, "fewer": fewer, "british_spellings": brit, "pages_found": sorted(pe)}


def check(cfg, sample):
    work = sample.split("_")[0]
    fr = T.read(os.path.join(T.ROOT, "source", sample + ".tex"))
    path = os.path.join(RUNS, cfg, sample + ".tex")
    en = T.read(path)
    meta = json.load(open(os.path.join(RUNS, cfg, sample + "_result.json"), encoding="utf-8"))
    first = next((ln for ln in fr.splitlines() if ln.strip()), "")
    clean = en.lstrip().startswith(first.strip()) and "```" not in en
    mf, me = macro_counts(fr), macro_counts(en)
    macro_diff = {k: [mf.get(k, 0), me.get(k, 0)] for k in sorted(set(mf) | set(me)) if mf.get(k, 0) != me.get(k, 0)}
    af, ae = anchors(fr), anchors(en)
    cf, ce = comments(fr), comments(en)
    return {
        "config": cfg, "sample": sample, "stop_reason": meta.get("stop_reason"), "chars_french": len(fr),
        "chars_english": len(en), "clean_output": clean, "output_start": en.lstrip()[:80],
        "formulas": compare_formulas(fr, en),
        "anchors": {"french": len(af), "english": len(ae), "same_sequence": af == ae,
                    "missing": [a for a in af if a not in ae], "added": [a for a in ae if a not in af]},
        "comments": {"french": len(cf), "english": len(ce), "same": sorted(cf) == sorted(ce),
                     "missing": [c for c in cf if c not in ce], "added": [c for c in ce if c not in cf]},
        "macros_differing": macro_diff, "marks_by_page": marks_by_page(fr, en, work),
        "unsure_bars": [unsure_bars(fr), unsure_bars(en)],
        "empty_marks_english": empty_marks(en),
        "french_left": french_left(en), "paragraphs": para_lengths(fr, en), "glossary": glossary_check(fr, en, work),
    }


def md(r):
    f, g, p, fl = r["formulas"], r["glossary"], r["paragraphs"], r["french_left"]
    L = ["# %s, %s" % (r["config"], r["sample"]), "",
         "stop reason %s; clean output (only the LaTeX): %s; %d characters (French %d)" % (
             r["stop_reason"], r["clean_output"], r["chars_english"], r["chars_french"]), "",
         "## 1. Formulas and macros",
         "formulas: French %d, English %d; identical %d, identical up to spacing %d, changed %d, missing %d, added %d" % (
             f["french"], f["english"], f["identical"], f["spacing_only"], len(f["changed"]), len(f["missing"]),
             len(f["added"]))]
    for a, b in f["changed"]:
        L += ["- changed:", "  - French:  `%s`" % a, "  - English: `%s`" % b]
    L += ["- missing: `%s`" % x for x in f["missing"]] + ["- added: `%s`" % x for x in f["added"]]
    L += ["", "page anchors: French %d, English %d, same sequence %s; missing %s; added %s" % (
        r["anchors"]["french"], r["anchors"]["english"], r["anchors"]["same_sequence"], r["anchors"]["missing"],
        r["anchors"]["added"]),
          "comment lines: French %d, English %d, same %s; missing %s; added %s" % (
              r["comments"]["french"], r["comments"]["english"], r["comments"]["same"], r["comments"]["missing"],
              r["comments"]["added"]),
          "macros outside formulas whose count differs (French, English): %s" % (r["macros_differing"] or "none"),
          "marks whose count differs, by page (formulas included): %s" % (", ".join(r["marks_by_page"]) or "none"),
          "bars in \\unsure{A|B} (French, English): %s; empty marks in the English: %d" % (
              r["unsure_bars"], r["empty_marks_english"]), "",
          "## 2. French left",
          "French function words: %d %s; elisions: %d" % (fl["french_words"], fl["french_word_counts"], fl["elisions"]),
          "sentences with several French words: %d" % len(fl["flagged_sentences"])]
    L += ["- %s" % x for x in fl["flagged_sentences"]]
    L += ["accented words: %s" % (", ".join(fl["accented_words"]) or "none"),
          "French left inside \\text{...} of formulas: %d of %d text boxes%s" % (
              len(fl["french_in_formula_text"]), fl["formula_texts"],
              (": " + "; ".join(fl["french_in_formula_text"])) if fl["french_in_formula_text"] else ""), "",
          "## 3. Paragraph lengths",
          "paragraphs: French %d, English %d, unmatched %d; measured %d; English/French length of the running text: "
          "median %s, min %s, max %s, whole text %s" % (p["paragraphs_french"], p["paragraphs_english"], p["unmatched"],
                                                       p["measured"], p["ratio_median"], p["ratio_min"],
                                                       p["ratio_max"], p["ratio_total"])]
    L += ["- ratio %s: FR `%s` / EN `%s`" % (x["ratio"], x["french"], x["english"]) for x in p["flagged"]]
    L += ["", "## 4. Glossary",
          "entry-page pairs with the English form: %d of %d; occurrences covered %d of %d" % (
              g["present"], g["entry_pages"], g["occurrences_covered"], g["occurrences_french"])]
    L += ["- missing: %s" % x for x in g["missing"]]
    L += ["- fewer: %s" % x for x in g["fewer"]]
    L += ["British spellings: %s" % (", ".join(g["british_spellings"]) or "none")]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    cfgs = sys.argv[1:] or sorted(d for d in os.listdir(RUNS) if os.path.isdir(os.path.join(RUNS, d)))
    os.makedirs(OUT, exist_ok=True)
    allr = {}
    if os.path.exists(os.path.join(OUT, "CHECKS.json")):
        allr = json.load(open(os.path.join(OUT, "CHECKS.json"), encoding="utf-8"))
    for c in cfgs:
        for f in sorted(os.listdir(os.path.join(RUNS, c))):
            if not f.endswith(".tex"):
                continue
            s = f[:-4]
            r = check(c, s)
            allr["%s/%s" % (c, s)] = r
            with open(os.path.join(OUT, "%s_%s.md" % (c, s)), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(md(r))
            fo = r["formulas"]
            print("%-15s %-8s fml %d/%d id %d sp %d ch %d miss %d add %d | anchors %s | FR words %d flagged %d | "
                  "para %d/%d med %s | gloss %d/%d" % (
                      c, s, fo["english"], fo["french"], fo["identical"], fo["spacing_only"], len(fo["changed"]),
                      len(fo["missing"]), len(fo["added"]), r["anchors"]["same_sequence"],
                      r["french_left"]["french_words"], len(r["french_left"]["flagged_sentences"]),
                      r["paragraphs"]["paragraphs_english"], r["paragraphs"]["paragraphs_french"],
                      r["paragraphs"]["ratio_median"], r["glossary"]["present"], r["glossary"]["entry_pages"]))
    with open(os.path.join(OUT, "CHECKS.json"), "w", encoding="utf-8") as fh:
        json.dump(allr, fh, ensure_ascii=False, indent=1)
