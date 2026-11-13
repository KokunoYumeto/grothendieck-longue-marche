"""Script checks of every English unit against its French (no API call).

The checks are those of the comparison (translation_comparison_20261111/scripts/checks.py, loaded from the
byte-identical copy scripts/cmp/checks.py): formulas back unchanged (\\text{...} wording masked), page anchors in
order, comment lines, macro counts outside formulas, no French left (function words, flagged sentences, elisions,
accented words, French in \\text{...} of formulas), paragraph lengths, glossary terms used where their French occurs,
British spellings. What scale changed:
  - each unit is read with its own macros, and its pages are keyed so that two unnumbered pages stay apart;
  - the glossary check covers all 171 entries (scripts/terms_DER.txt); a term missing on its page but present within
    the neighbouring page break is counted as present (an anchor can fall inside a sentence);
  - labels: the arguments of \\tag, the optional arguments of \\footnote, \\footnotemark, \\footnotetext in order, and
    the labels of axioms (Der n, Loc (n), PS n, W(n), L n; "Dér" read as "Der") as a multiset; \\item labels (review);
  - control sequences: none that the French does not have; one that could act outside the page (\\input, \\directlua,
    \\write, \\def, ...) blocks the build.
Refined after batch b02 (11 Nov), where these checks misfired on correct translations:
  - a formula whose only difference is the wording inside a text-mode box (\\texttt, \\parbox, \\tl, \\tls, tabular
    cells, ...; the inline math inside the box and everything outside it unchanged) is listed for review, not failed;
    so is a formula that only moved (missing at one place and added at another);
  - the French glossary patterns match from the start of a word (so "lisse" no longer fires inside "établissent");
  - the English running text is read with the English forms of the macros that print French words
    (common_dt.english_preamble: \\pl prints [rather, \\defeq prints def, \\cardred and \\red print red);
  - "Ét", "Coét", "ét." inside formulas are notation, not French left;
  - a paragraph whose French running text is under 80 characters is not failed on its length ratio (listed for
    review);
  - waivers (checks/WAIVERS.jsonl) can name one glossary entry on one page, or one failed check by its exact text.
After batch b03: the label macros of chapter VII and others (\\lab, \\edbr, ...) count as text-mode boxes, and a line
break \\\\[1ex] in a tabular of the running text no longer reads as the opening of a display (protect()); the 14 page
anchors whose argument is French are read in their English form (common_dt.ANCHOR_EN) in both texts.
During batch b04: the cells of the paragraph columns (p, m, b) of an array in a formula are text mode, like the cells
of a tabular (the other columns stay math); the check for French left in formulas reads all their text-mode wording
(text_runs: \\parbox, \\shortstack, tabular and array cells ..., not only the \\text-like boxes the comparison reads),
with a few more French words ("si", "pour", "non" standing alone, ...); the punctuation of text-mode wording is not
compared (a comma that word order moves next to a formula); British spellings: "surprising" is American.
During batch b05: minipage environments, tabulars with a position argument (\\begin{tabular}[b]) and the text of TikZ
nodes (\\node ... {text}, node[...] {text}) are text mode too; quotation marks of the wording are not compared, and a
formula whose words only moved around an inline formula inside a text box counts as changed only in its wording;
"devant" counts as French in formulas; "petite catégorie" is not matched after "plus " (FR_NOT_AFTER).
Each unit gets a verdict: PASS, or FAIL with the failed checks (to be re-run or fixed: scripts/fixes.py), and the
points to REVIEW (macro counts, new harmless macros, single French words, accented words, fewer terms, item labels,
formulas identical up to spacing).

usage: python -I -B check_units.py [--raw] [UNIT ...]
  default: the English units translation/<folder>/<unit>.tex (raw output plus the fixes of checks/FIXES.jsonl)
  --raw:   the model's output runs/out/<unit>.tex as it came back (results in checks/raw/)
Writes checks/CHECKS.json, checks/units/<unit>.md (or checks/raw/...), checks/SUMMARY.md.
"""
import collections
import importlib.util
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_dt as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
_spec = importlib.util.spec_from_file_location("cmp_checks", os.path.join(T.HERE, "cmp", "checks.py"))
C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(C)

CK = os.path.join(T.ROOT, "checks")
DANGER = {"input", "include", "InputIfFileExists", "directlua", "luaexec", "luadirect", "latelua", "luacode",
          "write", "immediate", "openout", "openin", "read", "readline", "closeout", "catcode", "def", "edef",
          "gdef", "xdef", "let", "futurelet", "newcommand", "renewcommand", "providecommand", "DeclareRobustCommand",
          "usepackage", "RequirePackage", "documentclass", "special", "csname", "expandafter", "ShellEscape",
          "write18", "pdfobj", "pdfextension", "scantokens", "everyjob", "everypar", "output", "lowercase",
          "uppercase", "makeatletter", "endinput", "end", "begin"}
DANGER_ENV = {"luacode", "luacode*", "filecontents", "filecontents*", "verbatimwrite"}
ACCENT_OK = set(C.ACCENT_OK) | {"coétale", "coétales", "poincaré", "künneth", "čech", "malgoire", "maltsiniotis",
                                 "dérivateurs", "grothendieck", "hölder", "möbius", "théorème"}
AXIOM = re.compile(r"\b(?:Der|Dér|Loc|PS|L) ?\(?\d+|\bW\(\d+")
# American words that the comparison's British pattern also catches ("characteris\w*", "\w+ising", "analyses").
BRITISH_NOT = re.compile(r"^(characteristic\w*|realis[mt]\w*|organism\w*|analyses|(pro|surp|surpr|r|ar|upr|comp|exerc|adv|"
                         r"dev|rev|superv|ra|pra|appra|comprom|improv|enterpr|advert|chast|desp|disgu|franch|merchand|"
                         r"telev|no|po|cru|bru|prec)ising)$", re.I)


# French words before which a glossary entry's French pattern is not the term ("la plus petite sous-catégorie" is
# "the smallest subcategory", not a small category; added in batch b05).
FR_NOT_AFTER = {"petite catégorie": "plus "}


def french_hits(ft):
    """Matches of each glossary entry in a French running text, without those inside a longer match of another entry
    (as the comparison's french_hits, over all entries); a match must start a word."""
    spans = {fr: [m.span() for m in re.finditer(r"(?<![^\W\d_])%s(?:%s)" % (
                  "(?<!%s)" % re.escape(FR_NOT_AFTER[fr]) if fr in FR_NOT_AFTER else "", rx), ft, re.I)]
             for fr, rx, en, src, note in T.glossary() if rx != "-"}
    allspans = [(o, a, b) for o, ss in spans.items() for a, b in ss]
    out = {}
    for name, ss in spans.items():
        keep = [s for s in ss if not any(o != name and a <= s[0] and s[1] <= b and (b - a) > (s[1] - s[0])
                                         for o, a, b in allspans)]
        if keep:
            out[name] = len(keep)
    return out


def glossary_check(fr, en, macros, en_macros):
    def clean(s):
        return re.sub(r"\\illegible\{[^{}]*\}", " ", s)
    terms = T.terms()
    pf, pe = T.split_pages(clean(fr)), dict(T.split_pages(clean(en)))
    keys = [k for k, _ in pf]
    ert = {k: T.running_text(pe.get(k, ""), en_macros) for k in keys}
    pairs, present, occ_fr, occ_en, missing, fewer, across = 0, 0, 0, 0, [], [], []
    for i, (page, ftext) in enumerate(pf):
        ft, et = T.running_text(ftext, macros), ert[page]
        for name, nf in french_hits(ft).items():
            rx = terms[name][1]
            ne = len(re.findall(rx, et, re.I))
            pairs += 1
            occ_fr += nf
            if not ne:
                window = (ert[keys[i - 1]][-400:] if i else "") + " " + et + " " + (
                    ert[keys[i + 1]][:400] if i + 1 < len(keys) else "")
                if re.search(rx, window, re.I):
                    across.append("%s (page %s)" % (name, page))
                    present += 1
                    occ_en += 1
                    continue
                missing.append("%s (page %s, %d in the French)" % (name, page, nf))
                continue
            present += 1
            occ_en += min(ne, nf)
            if ne < nf:
                fewer.append("%s (page %s: %d in the French, %d in the English)" % (name, page, nf, ne))
    brit = [m.group(0) for m in C.BRITISH.finditer(C.prose(en))
            if m.group(0).lower() not in C.BRITISH_OK and not BRITISH_NOT.match(m.group(0))]
    return {"entry_pages": pairs, "present": present, "occurrences_french": occ_fr, "occurrences_covered": occ_en,
            "missing": missing, "fewer": fewer, "across_page_break": across, "british_spellings": brit}


def marks_by_page(fr, en):
    pe = dict(T.split_pages(en))
    out = []
    for page, tf in T.split_pages(fr):
        te = pe.get(page, "")
        for m in C.MARKS:
            a = len(re.findall(r"\\%s(?![A-Za-z])" % m, C.strip_comments(tf)))
            b = len(re.findall(r"\\%s(?![A-Za-z])" % m, C.strip_comments(te)))
            if a != b:
                out.append("%s %s %d→%d" % (page, m, a, b))
    return out


def labels(s):
    s = C.strip_comments(s)
    return {"tags": re.findall(r"\\tag\*?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", s),
            "footnote_marks": ["%s%s" % (a, b) for a, b in
                               re.findall(r"\\(footnote|footnotemark|footnotetext)(?![A-Za-z])(\[[^\]]*\])?", s)],
            "items": re.findall(r"\\item(?![A-Za-z])(\[[^\]]*\])?", s),
            "axioms": sorted(re.sub(r"\s", "", x).replace("Dér", "Der") for x in AXIOM.findall(C.prose(s)))}


def control_sequences(s):
    s = C.strip_comments(s)
    return (collections.Counter(re.findall(r"\\([A-Za-z@]+)", s)),
            collections.Counter(re.findall(r"\\begin\{([^{}]*)\}", s)))


# Text-mode boxes inside formulas whose wording is translated (the comparison masks only \text-like boxes).
TEXTARG = re.compile(r"\\(text|textrm|textup|textit|textbf|textsf|texttt|textsc|textnormal|emph|mbox|hbox|tl|tls|"
                     r"shortstack|makecell|lab|edbr|mspin|rbox|cercle|circled|circnum|circlabel|encadre|encircled|"
                     r"encoval|ovalbox|ovale|dashedbox)(?![A-Za-z])\*?\s*(?:\[[^\]]*\]\s*)*\{")


def protect(s):
    """A line break with its spacing, \\\\[1ex], written outside a formula (in a tabular of the running text) reads to
    the comparison's formula pattern as the opening of a display \\[ ... \\]: written \\\\{}[1ex] for the checks."""
    return re.sub(r"(?<!\\)(\\\\\s*)\[", lambda m: m.group(1) + "{}[", s)
PARBOX = re.compile(r"\\parbox\s*(?:\[[^\]]*\]\s*)*\{[^{}]*\}\s*\{")
TABULAR = re.compile(r"\\begin\{(tabular|minipage)\}\s*(?:\[[^\]]*\]\s*)*\{(?:[^{}]|\{[^{}]*\})*\}")
NODE = re.compile(r"(?:\\node|(?<![A-Za-z\\])node)\s*(?:\[[^\]]*\]\s*)?(?:\([^()]*\)\s*)?(?:at\s*\([^()]*\)\s*)?\{")
ARRAY = re.compile(r"\\begin\{array\}\s*(?:\[[a-z]\]\s*)?\{")
ENV = re.compile(r"\\(begin|end)\{[^{}]*\}")
WORD = r"[A-Za-zÀ-ÖØ-öø-ÿœŒ’']+"


CSEQ = re.compile(r"\\(?:[A-Za-z]+\*?|.)", re.S)


def array_cols(spec):
    """The columns of an array's column spec, in order: True for a paragraph column (p, m, b: text mode), False for
    l, c, r (math mode). @{...}, !{...}, >{...}, <{...} and | are skipped; *{n}{...} is expanded."""
    cols, i = [], 0
    while i < len(spec):
        ch = spec[i]
        if ch in "@!<>":
            i += 1
            while i < len(spec) and spec[i] == " ":
                i += 1
            if i < len(spec) and spec[i] == "{":
                i = C.arg_end(spec, i)
            continue
        if ch == "*":
            m = re.match(r"\*\s*\{\s*(\d+)\s*\}\s*\{", spec[i:])
            if m:
                b = i + m.end() - 1
                e = C.arg_end(spec, b)
                cols += array_cols(spec[b + 1:e - 1]) * int(m.group(1))
                i = e
                continue
        if ch in "pmb":
            cols.append(True)
            i += 1
            while i < len(spec) and spec[i] == " ":
                i += 1
            if i < len(spec) and spec[i] == "{":
                i = C.arg_end(spec, i)
            continue
        if ch in "lcr":
            cols.append(False)
        i += 1
    return cols


def text_mask(f):
    """For each character of a formula: True when it is wording in text mode (inside a text-mode box or a tabular, and
    not inside inline math there); control sequences are never wording. Nesting (math, box, math, ...) is followed."""
    mask = [False] * len(f)

    def tab_end(i, name):
        depth, k = 1, i
        op, cl = "\\begin{%s}" % name, "\\end{%s}" % name
        while True:
            a, e = f.find(op, k), f.find(cl, k)
            if e < 0:
                return len(f), len(f)
            if 0 <= a < e:
                depth, k = depth + 1, a + len(op)
                continue
            depth -= 1
            if depth == 0:
                return e, e + len(cl)
            k = e + len(cl)

    def box_at(i):
        for rx in (TEXTARG, PARBOX, NODE):
            m = rx.match(f, i)
            if m:
                b = m.end() - 1
                e = C.arg_end(f, b)
                return b + 1, e - 1, e
        m = TABULAR.match(f, i)
        if m:
            ce, after = tab_end(m.end(), m.group(1))
            return m.end(), ce, after
        return None

    def math_end(i, b):
        k = i
        while k < b:
            if f[k] == "\\":
                bx = box_at(k)
                if bx:
                    k = bx[2]
                    continue
                m = CSEQ.match(f, k)
                k += len(m.group(0)) if m else 1
                continue
            if f[k] == "$":
                return k
            k += 1
        return b

    def mark_array(i, limit, kinds):
        """The cells of an array whose spec has paragraph columns, from i (after the spec) to its \\end{array}: a
        paragraph column's cells are text mode, the others math. Returns the index after \\end{array}."""
        col, cell, depth, env, k = 0, i, 0, 0, i

        def kind():
            return kinds[min(col, len(kinds) - 1)]
        while k < limit:
            if f.startswith("\\end{array}", k) and env == 0 and depth == 0:
                mark(cell, k, kind())
                return k + len("\\end{array}")
            m = ENV.match(f, k)
            if m:
                env, k = env + (1 if m.group(1) == "begin" else -1), m.end()
                continue
            ch = f[k]
            if ch == "\\":
                if f.startswith("\\\\", k) and depth == 0 and env == 0:
                    mark(cell, k, kind())
                    k += 2
                    cell, col = k, 0
                    continue
                m = CSEQ.match(f, k)
                k += len(m.group(0)) if m else 1
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            elif ch == "&" and depth == 0 and env == 0:
                mark(cell, k, kind())
                col += 1
                cell = k + 1
            k += 1
        mark(cell, limit, kind())
        return limit

    def mark(a, b, text):
        i = a
        while i < b:
            if f[i] == "\\":
                ar = ARRAY.match(f, i)
                if ar:
                    e = C.arg_end(f, ar.end() - 1)
                    kinds = array_cols(f[ar.end():e - 1])
                    if any(kinds):
                        i = mark_array(e, b, kinds)
                        continue
                bx = box_at(i)
                if bx:
                    mark(bx[0], bx[1], True)
                    i = bx[2]
                    continue
                m = CSEQ.match(f, i)
                i += len(m.group(0)) if m else 1
                continue
            if text and f[i] == "$":
                j = math_end(i + 1, b)
                mark(i + 1, j, False)
                i = j + 1
                continue
            if not text and f[i] == "n":  # a node on a TikZ path: node[...] {text}
                m = NODE.match(f, i)
                if m:
                    e = C.arg_end(f, m.end() - 1)
                    mark(m.end(), e - 1, True)
                    i = e
                    continue
            mask[i] = text
            i += 1

    mark(0, len(f), False)
    return mask


def skeleton(f, loose=False):
    """The formula with the wording of its text-mode boxes reduced to one mark per run of words (control sequences,
    inline math and everything outside the boxes kept), spaces removed. loose: the marks next to inline math are
    dropped too (word order moves the words around a formula: "par $\\varinjlim$ ordinales" is "ordinal
    $\\varinjlim$")."""
    mask = text_mask(f)
    out, i = [], 0
    while i < len(f):
        j = i
        while j < len(f) and mask[j] == mask[i]:
            j += 1
        chunk = f[i:j]
        if mask[i]:
            # punctuation and quotation marks of the wording go with the words (word order moves a comma next to a
            # formula; “...” is ``...'' in the English)
            parts = re.split(r"(\\[A-Za-z]+\*?|\\.)", chunk)
            chunk = "".join(p if k % 2 else re.sub(WORD, "⁘", re.sub(r"[,;.:!?“”«»„‚‹›`\"'’‘]", "", p))
                            for k, p in enumerate(parts))
            chunk = re.sub("⁘(?:[\\s,;.:!?/'’-]*⁘)*", "⁘", chunk)
        out.append(chunk)
        i = j
    s = re.sub(r"\s+", "", "".join(out))
    return re.sub("⁘?(\\$)⁘?", r"\1", s) if loose else s


def compare_formulas(fr, en):
    """The comparison's formula check, then: a changed formula that differs only in text-mode wording goes to
    'text_only' (also when the words moved around an inline formula: skeleton(loose=True)); a missing formula that is
    added elsewhere goes to 'moved'."""
    r = C.compare_formulas(fr, en)
    keep, text_only = [], []
    for a, b in r["changed"]:
        same = skeleton(a) == skeleton(b) or skeleton(a, True) == skeleton(b, True)
        (text_only if same else keep).append([a, b])
    miss, add, moved = list(r["missing"]), list(r["added"]), []
    for f in list(miss):
        for e in add:
            if re.sub(r"\s", "", e) == re.sub(r"\s", "", f) or skeleton(e) == skeleton(f):
                add.remove(e)
                miss.remove(f)
                moved.append(f)
                break
    r.update(changed=keep, text_only=text_only, missing=miss, added=add, moved=moved)
    return r


NOTATION_OK = {"ét", "coét", "étale", "coétale", "étales", "coétales"}


FRENCH_MORE = {"si", "pour", "ssi", "sinon", "commutatif", "commutatifs", "morphisme", "morphismes", "foncteur",
               "foncteurs", "devant"}


def text_runs(s):
    """The wording in text mode of every formula, as text_mask reads it: \\text-like boxes, \\parbox, \\shortstack and
    the other text-mode boxes, tabular cells, the paragraph columns of arrays (inline math and control sequences
    left out)."""
    out = []
    for m in C.MATH.finditer(C.strip_comments(s)):
        f = m.group(0)
        mask = text_mask(f)
        i = 0
        while i < len(f):
            if not mask[i]:
                i += 1
                continue
            j = i
            while j < len(f) and mask[j]:
                j += 1
            if re.search(r"[A-Za-zÀ-ÿ]", f[i:j]):
                out.append(f[i:j].strip())
            i = j
    return out


def french_in_formula_text(en):
    """The comparison's French-in-formula-text check, read on all the text-mode wording of the formulas (text_runs:
    the comparison reads only \\text-like boxes; from batch b04 on), with this edition's notation words allowed (Ét,
    Coét, ét.) and a few more French words (FRENCH_MORE; "non" standing alone)."""
    bad = []
    for x in text_runs(en):
        ws = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ]+", x)
        if any(w.lower() in C.FRENCH and w.lower() not in C.FRENCH_IN_ENGLISH for w in ws) or \
                any(C.ACCENT.search(w) and w.lower() not in ACCENT_OK and w.lower() not in NOTATION_OK for w in ws) or \
                any(w.lower() in ("pl", "fid") or w.lower() in FRENCH_MORE for w in ws) or \
                re.search(r"(?<![A-Za-z-])non(?![A-Za-z-])", x):
            bad.append(x)
    return bad


def check(unit, en_body, meta):
    fr_doc = T.read(os.path.join(T.ROOT, "source", unit + ".tex"))
    pre = T.split_doc(fr_doc)[0]
    fr = protect(T.english_anchors(T.body_text(fr_doc)))  # both texts with the English anchors (common_dt.ANCHOR_EN)
    en = protect(T.english_anchors(en_body))
    macros = T.macros_of(pre)
    en_macros = T.macros_of(T.english_preamble(pre))
    first = next((ln for ln in fr.splitlines() if ln.strip()), "")
    clean = en.lstrip().startswith(first.strip()) and "```" not in en and "\\begin{document}" not in en
    mf, me = C.macro_counts(fr), C.macro_counts(en)
    macro_diff = {k: [mf.get(k, 0), me.get(k, 0)] for k in sorted(set(mf) | set(me)) if mf.get(k, 0) != me.get(k, 0)}
    af, ae = C.anchors(fr), C.anchors(en)
    cf, ce = C.comments(fr), C.comments(en)
    lf, le = labels(fr), labels(en)
    (csf, envf), (cse, enve) = control_sequences(fr), control_sequences(en)
    new_cs = sorted(set(cse) - set(csf))
    new_env = sorted(set(enve) - set(envf))
    r = {
        "unit": unit, "status": (meta or {}).get("status"), "chars_french": len(fr), "chars_english": len(en),
        "clean_output": clean, "output_start": en.lstrip()[:80],
        "formulas": compare_formulas(fr, en),
        "anchors": {"french": len(af), "english": len(ae), "same_sequence": af == ae,
                    "missing": [a for a in af if a not in ae], "added": [a for a in ae if a not in af]},
        "comments": {"french": len(cf), "english": len(ce), "same": sorted(cf) == sorted(ce),
                     "missing": [c for c in cf if c not in ce], "added": [c for c in ce if c not in cf]},
        "macros_differing": macro_diff, "marks_by_page": marks_by_page(fr, en),
        "labels": {k: {"same": lf[k] == le[k], "french": lf[k], "english": le[k]} for k in lf},
        "new_control_sequences": new_cs, "new_environments": new_env,
        "dangerous": sorted(set(new_cs) & DANGER) + sorted(set(new_env) & DANGER_ENV),
        "empty_marks_english": C.empty_marks(en),
        "french_left": C.french_left(en), "paragraphs": C.para_lengths(fr, en),
        "glossary": glossary_check(fr, en, macros, en_macros),
    }
    r["french_left"]["accented_words"] = [w for w in r["french_left"]["accented_words"] if w.lower() not in ACCENT_OK]
    r["french_left"]["french_in_formula_text"] = french_in_formula_text(en)
    r["french_left"]["formula_texts"] = len(text_runs(en))
    pl = r["paragraphs"]
    pl["short_flagged"] = [x for x in pl["flagged"] if len(x["french"]) < 80]
    pl["flagged"] = [x for x in pl["flagged"] if len(x["french"]) >= 80]
    waived = []
    for w in waivers().get(unit, []):  # one glossary entry on one page: a misfire on a correct translation
        if "entry" not in w:
            continue
        g = r["glossary"]
        for key in ("missing", "fewer"):
            for item in list(g[key]):
                if item.startswith("%s (page %s," % (w["entry"], w["page"])) or \
                        item.startswith("%s (page %s:" % (w["entry"], w["page"])):
                    g[key].remove(item)
                    waived.append("glossary, %s: %s (waived: %s)" % (key, item, w["reason"]))
    fail, review = [], []
    if r["status"] != "completed":
        fail.append("status %s" % r["status"])
    if not en.strip():
        fail.append("no output")
    if not clean:
        fail.append("output not only the LaTeX")
    fo = r["formulas"]
    if fo["changed"] or fo["missing"] or fo["added"]:
        fail.append("formulas: %d changed, %d missing, %d added" % (len(fo["changed"]), len(fo["missing"]),
                                                                    len(fo["added"])))
    if not r["anchors"]["same_sequence"]:
        fail.append("page anchors")
    if not r["comments"]["same"]:
        fail.append("comment lines")
    if r["dangerous"]:
        fail.append("control sequences that act outside the page: %s" % r["dangerous"])
    fl = r["french_left"]
    if fl["flagged_sentences"] or fl["french_in_formula_text"] or fl["elisions"]:
        fail.append("French left: %d sentences, %d formula boxes, %d elisions" % (
            len(fl["flagged_sentences"]), len(fl["french_in_formula_text"]), fl["elisions"]))
    p = r["paragraphs"]
    if p["unmatched"] or p["flagged"] or p["paragraphs_french"] != p["paragraphs_english"]:
        fail.append("paragraphs: French %d, English %d, %d length ratios out of 0.7-1.5" % (
            p["paragraphs_french"], p["paragraphs_english"], len(p["flagged"])))
    g = r["glossary"]
    if g["missing"]:
        fail.append("glossary: %d terms missing" % len(g["missing"]))
    if g["british_spellings"]:
        fail.append("British spellings: %s" % ", ".join(g["british_spellings"]))
    lab = r["labels"]
    bad = [k for k in ("tags", "footnote_marks", "axioms") if not lab[k]["same"]]
    if bad:
        fail.append("labels: %s" % ", ".join(bad))
    if macro_diff:
        review.append("macro counts outside formulas (French, English): %s" % macro_diff)
    harmless = [x for x in new_cs if x not in DANGER] + [x for x in new_env if x not in DANGER_ENV]
    if harmless:
        review.append("control sequences or environments the French does not have: %s" % harmless)
    if fl["french_words"]:
        review.append("French function words: %s" % fl["french_word_counts"])
    if fl["accented_words"]:
        review.append("accented words: %s" % ", ".join(fl["accented_words"]))
    if g["fewer"]:
        review.append("terms found fewer times than their French: %d" % len(g["fewer"]))
    if not lab["items"]["same"]:
        review.append("item labels differ")
    if fo["spacing_only"]:
        review.append("formulas identical up to spacing: %d" % fo["spacing_only"])
    if fo["text_only"]:
        review.append("formulas changed only in the wording of text-mode boxes: %d" % len(fo["text_only"]))
    if fo["moved"]:
        review.append("formulas moved: %d" % len(fo["moved"]))
    if p["short_flagged"]:
        review.append("short paragraphs with a length ratio out of 0.7-1.5: %d" % len(p["short_flagged"]))
    if r["marks_by_page"]:
        review.append("marks by page: %s" % ", ".join(r["marks_by_page"]))
    for w in waivers().get(unit, []):  # a check that misfires on a correct translation: the reason is recorded
        if "entry" in w:
            continue
        for f in list(fail):
            if ("fail" in w and f == w["fail"]) or ("fail_prefix" in w and f.startswith(w["fail_prefix"])):
                fail.remove(f)
                waived.append("%s (waived: %s)" % (f, w["reason"]))
    r["verdict"] = "FAIL" if fail else "PASS"
    r["fail"], r["review"], r["waived"] = fail, review, waived
    return r


_W = None


def waivers():
    """checks/WAIVERS.jsonl: {"unit", "fail_prefix", "reason", "by", "date"}, one per failed check that is a false
    alarm on a correct translation (e.g. a French title cited in French)."""
    global _W
    if _W is None:
        _W = {}
        p = os.path.join(CK, "WAIVERS.jsonl")
        if os.path.exists(p):
            for x in T.read(p).splitlines():
                if x.strip():
                    w = json.loads(x)
                    _W.setdefault(w["unit"], []).append(w)
    return _W


def md(r):
    f, g, p, fl = r["formulas"], r["glossary"], r["paragraphs"], r["french_left"]
    L = ["# %s: %s" % (r["unit"], r["verdict"]), ""]
    L += ["- FAIL: %s" % x for x in r["fail"]] + ["- %s" % x for x in r.get("waived", [])]
    L += ["- review: %s" % x for x in r["review"]]
    L += ["", "status %s; clean output (only the LaTeX): %s; %d characters (French %d)" % (
        r["status"], r["clean_output"], r["chars_english"], r["chars_french"]), "",
          "## 1. Formulas, anchors, labels, macros",
          "formulas: French %d, English %d; identical %d, identical up to spacing %d, changed %d, missing %d, added %d"
          % (f["french"], f["english"], f["identical"], f["spacing_only"], len(f["changed"]), len(f["missing"]),
             len(f["added"]))]
    for a, b in f["changed"]:
        L += ["- changed:", "  - French:  `%s`" % a, "  - English: `%s`" % b]
    L += ["- missing: `%s`" % x for x in f["missing"]] + ["- added: `%s`" % x for x in f["added"]]
    for a, b in f.get("text_only", []):
        L += ["- changed only in the wording of text-mode boxes (review):", "  - French:  `%s`" % a,
              "  - English: `%s`" % b]
    L += ["- moved (review): `%s`" % x for x in f.get("moved", [])]
    L += ["", "page anchors: French %d, English %d, same sequence %s; missing %s; added %s" % (
        r["anchors"]["french"], r["anchors"]["english"], r["anchors"]["same_sequence"], r["anchors"]["missing"],
        r["anchors"]["added"]),
          "comment lines: French %d, English %d, same %s; missing %s; added %s" % (
              r["comments"]["french"], r["comments"]["english"], r["comments"]["same"], r["comments"]["missing"],
              r["comments"]["added"])]
    for k, v in r["labels"].items():
        L.append("labels, %s: same %s%s" % (k, v["same"], "" if v["same"] else "; French %s; English %s" % (
            v["french"], v["english"])))
    L += ["macros outside formulas whose count differs (French, English): %s" % (r["macros_differing"] or "none"),
          "marks whose count differs, by page: %s" % (", ".join(r["marks_by_page"]) or "none"),
          "control sequences the French does not have: %s; environments: %s" % (
              r["new_control_sequences"] or "none", r["new_environments"] or "none"), "",
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
    L += ["- short paragraph, ratio %s (review): FR `%s` / EN `%s`" % (x["ratio"], x["french"], x["english"])
          for x in p.get("short_flagged", [])]
    L += ["", "## 4. Glossary",
          "entry-page pairs with the English form: %d of %d (%d across a page break); occurrences covered %d of %d" % (
              g["present"], g["entry_pages"], len(g["across_page_break"]), g["occurrences_covered"],
              g["occurrences_french"])]
    L += ["- missing: %s" % x for x in g["missing"]]
    L += ["- fewer: %s" % x for x in g["fewer"]]
    L += ["- across a page break: %s" % x for x in g["across_page_break"]]
    L += ["British spellings: %s" % (", ".join(g["british_spellings"]) or "none")]
    return "\n".join(L) + "\n"


def english_body(unit, raw):
    if raw:
        p = os.path.join(T.ROOT, "runs", "out", unit + ".tex")
        return T.read(p) if os.path.exists(p) else None
    folder = T.unit_map()[unit]["folder"]
    p = os.path.join(T.ROOT, "translation", folder, unit + ".tex")
    if not os.path.exists(p):
        return None
    return T.body_text(T.read(p))


def main():
    args = sys.argv[1:]
    raw = "--raw" in args
    want = [a for a in args if not a.startswith("--")]
    sub = "raw" if raw else "units"
    os.makedirs(os.path.join(CK, sub), exist_ok=True)
    store = os.path.join(CK, "CHECKS_raw.json" if raw else "CHECKS.json")
    allr = json.loads(T.read(store)) if os.path.exists(store) else {}
    for u in [x["id"] for x in T.units()]:
        if want and u not in want:
            continue
        en = english_body(u, raw)
        if en is None:
            continue
        mp = os.path.join(T.ROOT, "runs", "out", u + "_result.json")
        meta = json.loads(T.read(mp)) if os.path.exists(mp) else {}
        r = check(u, en, meta)
        allr[u] = r
        T.write(os.path.join(CK, sub, u + ".md"), md(r))
        print("%-28s %s %s%s" % (u, r["verdict"], "; ".join(r["fail"]),
                                 ("  [review: %d]" % len(r["review"])) if r["review"] else ""))
    T.write(store, json.dumps(allr, ensure_ascii=False, indent=1))
    if not raw:
        summary(allr)


def summary(allr):
    us = [x["id"] for x in T.units()]
    done = [u for u in us if u in allr]
    fails = [u for u in done if allr[u]["verdict"] == "FAIL"]
    L = ["# Check results of the English units", "",
         "%d of %d units checked; %d pass, %d fail. Per unit: `checks/units/<unit>.md`; all figures: `CHECKS.json`."
         % (len(done), len(us), len(done) - len(fails), len(fails)), ""]
    if fails:
        L += ["## Failing", ""] + ["- %s: %s" % (u, "; ".join(allr[u]["fail"])) for u in fails] + [""]
    wv = [u for u in done if allr[u].get("waived")]
    if wv:
        L += ["## Checks waived (false alarms on a correct translation; checks/WAIVERS.jsonl)", ""]
        L += ["- %s: %s" % (u, "; ".join(allr[u]["waived"])) for u in wv] + [""]
    tot = collections.Counter()
    for u in done:
        r = allr[u]
        tot["formulas"] += r["formulas"]["french"]
        tot["formulas_identical"] += r["formulas"]["identical"] + r["formulas"]["spacing_only"]
        tot["formulas_text_only"] += len(r["formulas"].get("text_only", []))
        tot["formulas_moved"] += len(r["formulas"].get("moved", []))
        tot["anchors"] += r["anchors"]["french"]
        tot["entry_pages"] += r["glossary"]["entry_pages"]
        tot["present"] += r["glossary"]["present"]
        tot["review_units"] += bool(r["review"])
    L += ["## Totals over the checked units", "",
          "formulas identical (or up to spacing) %d of %d, changed only in the wording of text-mode boxes %d, "
          "moved %d; page anchors %d; glossary entry-pages with the English form %d of %d; units with points to "
          "review %d" % (tot["formulas_identical"], tot["formulas"], tot["formulas_text_only"], tot["formulas_moved"],
                         tot["anchors"], tot["present"], tot["entry_pages"], tot["review_units"]), ""]
    T.write(os.path.join(CK, "SUMMARY.md"), "\n".join(L))


if __name__ == "__main__":
    main()
