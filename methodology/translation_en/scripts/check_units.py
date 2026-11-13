"""Script checks of every English unit against its French (no API call): formula identity and completeness per unit.

The checks are those of the Dérivateurs translation (derivateurs_translation_20261111/scripts/check_units.py, loaded
from the byte-identical copy scripts/der/check_units.py, which loads the comparison's checks.py from scripts/der/cmp/):
formulas back unchanged (the wording of text-mode boxes masked: \\text, \\mbox, \\hbox, tabular cells, TikZ node
labels ...; a formula changed only in that wording, or only moved, is listed for review), page anchors in order (here
\\scanpage and \\mspage), comment lines, macro counts, no French left (function words, flagged sentences, elisions,
French in the text-mode wording of formulas), paragraphs paired one for one with their lengths, glossary terms used
where their French occurs, British spellings, control sequences the French does not have. What this work changed:
  - formulas: his "même" written m with a bar, set as a formula of its own, is written out in the English (NOTATION_LM,
    decided 10 Nov): those formulas (common_lm.MBAR) are left out of the comparison on both sides; one still in the
    English is listed for review;
  - the apparatus of the transcription is checked scan by scan: the number of \\deleted, \\inserted, \\unsure,
    \\illegible, \\margin, \\uline, \\uuline on each scan (formulas included) must be the same in both texts (FAIL; the
    Dérivateurs check listed marks by page for review), and so must the bars of \\unsure{A|B};
  - completeness by scan: the running text of each scan of at least 300 French characters must be at least 0.7 of
    its French in length (FAIL below; above 1.8 listed for review), besides the comparison's pairing of paragraphs;
  - paragraph lengths: a paragraph whose French running text has at least 80 characters fails below 0.7 or above
    1.8 (his abbreviations written out lengthen the English: 1.5 to 1.8 is listed for review); shorter ones review;
  - the glossary check covers all 116 entries (scripts/terms_LM.txt); entries of level "review" (his abbreviations,
    words with ordinary senses) are listed, not failed; a term missing on its scan but present within the
    neighbouring scan break counts as present;
  - labels: the arguments of \\tag in order; \\item labels (review). No axioms or footnotes in this work.
Each unit gets a verdict: PASS, or FAIL with the failed checks (to be re-run or fixed: checks/FIXES.jsonl), and the
points to REVIEW.

usage: python -I -B check_units.py [--raw] [UNIT ...]
  default: the English units translation/units/<package>/<unit>.tex (raw output plus the fixes of checks/FIXES.jsonl)
  --raw:   the model's output runs/out/<unit>.tex as it came back (results in checks/raw/)
Writes checks/CHECKS.json (or CHECKS_raw.json), checks/units/<unit>.md (or checks/raw/...), checks/SUMMARY.md.
"""
import collections
import importlib.util
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_lm as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
_spec = importlib.util.spec_from_file_location("der_check_units", os.path.join(T.HERE, "der", "check_units.py"))
D = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(D)
C = D.C

CK = os.path.join(T.ROOT, "checks")
D.ACCENT_OK |= {"université", "eugène", "poincaré", "teichmüller", "étale", "étales", "pro-étale", "proétale",
                "dévissage", "dévissages", "galois-teichmüller", "fréchet", "čech", "künneth", "hölder", "möbius", "grothendieck",
                "riemann-roch", "bieberbach", "bely", "belyĭ", "schottky", "néron", "kähler", "zariski", "frobenius",
                "lefschetz", "malcev", "mal'cev", "sémantique"}
ACCENT_OK = D.ACCENT_OK
APPARATUS = ("deleted", "inserted", "unsure", "illegible", "margin", "uline", "uuline")
OTHER_MARKS = ("texttt", "textit", "textbf", "diagram", "figure", "textsuperscript", "textcircled", "fbox")
MB = "\u27e8m\u0304\u27e9"   # what a standalone m-bar formula is replaced by for the formula comparison


def drop_mbar(s):
    """The text with every standalone m-bar formula replaced by a mark (outside comments), and their number."""
    n = 0

    def rep(m):
        nonlocal n
        if T.MBAR.match(m.group(0).strip()):
            n += 1
            return MB
        return m.group(0)
    parts = re.split(r"((?<!\\)%[^\n]*)", s)
    out = [p if k % 2 else C.MATH.sub(rep, p) for k, p in enumerate(parts)]
    return "".join(out), n


# Refined after b04 (12 Nov), where the check failed correct translations, as the Dérivateurs checks were refined
# during their run: (1) a formula whose only difference is the word (two letters or more, nothing but letters and
# punctuation) inside a mark of the transcription standing in the formula (\deleted{\unsure{par}} is
# \deleted{\unsure{by}}, \uline{et} is \uline{and}) is listed for review with the formulas changed only in their
# text-box wording; (2) a French formula that is only the raised ending of one of his abbreviations ($^{\mathrm t}$,
# ${}^{t}$: "comp.$^{\mathrm t}$ble") and is missing from the English, because the abbreviation is written out, is
# listed for review, not failed.
MARKWORD = re.compile(r"\\(deleted|inserted|unsure|uline|uuline)\{([A-Za-zÀ-ÖØ-öø-ÿœŒ.'’ -]{2,})\}")
RAISED = re.compile(r"^(?:\$|\\\()\s*(?:\{\})?\^\{?\s*(?:\\mathrm\s*\{?|\\text\{|\\textrm\{)?\s*[A-Za-z]{1,4}\s*\}?\s*\}?\s*"
                    r"(?:\$|\\\))$")


def compare_formulas(fr, en):
    r = D.compare_formulas(fr, en)
    keep = []
    for a, b in r["changed"]:
        if MARKWORD.sub(r"\\\1{⁘}", a) == MARKWORD.sub(r"\\\1{⁘}", b):
            r["text_only"].append([a, b])
        else:
            keep.append([a, b])
    r["changed"] = keep
    raised = [f for f in r["missing"] if RAISED.match(f.strip())]
    r["missing"] = [f for f in r["missing"] if not RAISED.match(f.strip())]
    r["raised_endings"] = raised
    return r


def marks_by_scan(fr, en):
    pe = dict(T.split_pages(en))
    fail, review = [], []
    for page, tf in T.split_pages(fr):
        te = pe.get(page, "")
        for m in APPARATUS + OTHER_MARKS:
            a = len(re.findall(r"\\%s(?![A-Za-z])" % m, C.strip_comments(tf)))
            b = len(re.findall(r"\\%s(?![A-Za-z])" % m, C.strip_comments(te)))
            if a != b:
                (fail if m in APPARATUS else review).append("%s %s %d→%d" % (page, m, a, b))
        ba, bb = C.unsure_bars(tf), C.unsure_bars(te)
        if ba != bb:
            fail.append("%s unsure-bars %d→%d" % (page, ba, bb))
    return fail, review


def scan_lengths(fr, en):
    pe = dict(T.split_pages(en))
    short, long_ = [], []
    for page, tf in T.split_pages(fr):
        lf, le = len(C.prose(tf)), len(C.prose(pe.get(page, "")))
        if lf < 300:
            continue
        r = le / lf
        if r < 0.7:
            short.append("scan %s: %.2f (%d/%d)" % (page, r, le, lf))
        elif r > 1.8:
            long_.append("scan %s: %.2f (%d/%d)" % (page, r, le, lf))
    return short, long_


def glossary_check(fr, en):
    def clean(s):
        return re.sub(r"\\illegible\{[^{}]*\}", " ", s)
    terms = T.terms()
    pf, pe = T.split_pages(clean(fr)), dict(T.split_pages(clean(en)))
    keys = [k for k, _ in pf]
    ert = {k: T.running_text(pe.get(k, "")) for k in keys}
    pairs, present, occ_fr, occ_en, missing, missing_review, fewer, across = 0, 0, 0, 0, [], [], [], []
    for i, (page, ftext) in enumerate(pf):
        ft, et = T.running_text(ftext), ert[page]
        for name, nf in T.french_hits(ft).items():
            if name not in terms or terms[name][1] == "-":
                continue
            rx, level = terms[name][1], terms[name][2]
            ne = len(re.findall(rx, et, re.I))
            pairs += 1
            occ_fr += nf
            if not ne:
                window = (ert[keys[i - 1]][-400:] if i else "") + " " + et + " " + (
                    ert[keys[i + 1]][:400] if i + 1 < len(keys) else "")
                if re.search(rx, window, re.I):
                    across.append("%s (scan %s)" % (name, page))
                    present += 1
                    occ_en += 1
                    continue
                (missing if level == "fail" else missing_review).append("%s (scan %s, %d in the French)" % (
                    name, page, nf))
                continue
            present += 1
            occ_en += min(ne, nf)
            if ne < nf:
                fewer.append("%s (scan %s: %d in the French, %d in the English)" % (name, page, nf, ne))
    brit = [m.group(0) for m in C.BRITISH.finditer(C.prose(en))
            if m.group(0).lower() not in C.BRITISH_OK and not D.BRITISH_NOT.match(m.group(0))]
    return {"entry_pages": pairs, "present": present, "occurrences_french": occ_fr, "occurrences_covered": occ_en,
            "missing": missing, "missing_review": missing_review, "fewer": fewer, "across_page_break": across,
            "british_spellings": brit}


def labels(s):
    s = C.strip_comments(s)
    return {"tags": re.findall(r"\\tag\*?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", s),
            "items": re.findall(r"\\item(?![A-Za-z])(\[[^\]]*\])?", s)}


def check(unit, en_body, meta):
    u = T.unit_map()[unit]
    fr0 = T.unit_text(u)
    fr = D.protect(fr0)
    en = D.protect(en_body)
    first = next((ln for ln in fr.splitlines() if ln.strip()), "")
    clean = en.lstrip().startswith(first.strip()) and "```" not in en and "\\begin{document}" not in en
    frm, nmf = drop_mbar(fr)
    enm, nme = drop_mbar(en)
    mf, me = C.macro_counts(fr), C.macro_counts(en)
    macro_diff = {k: [mf.get(k, 0), me.get(k, 0)] for k in sorted(set(mf) | set(me)) if mf.get(k, 0) != me.get(k, 0)}
    af, ae = C.anchors(fr), C.anchors(en)
    cf, ce = C.comments(fr), C.comments(en)
    lf, le = labels(fr), labels(en)
    (csf, envf), (cse, enve) = D.control_sequences(fr), D.control_sequences(en)
    new_cs = sorted(set(cse) - set(csf))
    new_env = sorted(set(enve) - set(envf))
    mk_fail, mk_review = marks_by_scan(fr, en)
    short, long_ = scan_lengths(fr, en)
    r = {
        "unit": unit, "status": (meta or {}).get("status"), "chars_french": len(fr), "chars_english": len(en),
        "clean_output": clean, "output_start": en.lstrip()[:80],
        "formulas": compare_formulas(frm, enm), "mbar": {"french": nmf, "english_kept": nme},
        "anchors": {"french": len(af), "english": len(ae), "same_sequence": af == ae,
                    "missing": [a for a in af if a not in ae], "added": [a for a in ae if a not in af]},
        "comments": {"french": len(cf), "english": len(ce), "same": sorted(cf) == sorted(ce),
                     "missing": [c for c in cf if c not in ce], "added": [c for c in ce if c not in cf]},
        "macros_differing": macro_diff, "marks_by_scan": {"fail": mk_fail, "review": mk_review},
        "scan_lengths": {"short": short, "long": long_},
        "labels": {k: {"same": lf[k] == le[k], "french": lf[k], "english": le[k]} for k in lf},
        "new_control_sequences": new_cs, "new_environments": new_env,
        "dangerous": sorted(set(new_cs) & D.DANGER) + sorted(set(new_env) & D.DANGER_ENV),
        "empty_marks_english": C.empty_marks(en),
        "french_left": C.french_left(en), "paragraphs": C.para_lengths(fr, en),
        "glossary": glossary_check(fr, en),
    }
    r["french_left"]["accented_words"] = [w for w in r["french_left"]["accented_words"] if w.lower() not in ACCENT_OK]
    r["french_left"]["french_in_formula_text"] = D.french_in_formula_text(en)
    r["french_left"]["formula_texts"] = len(D.text_runs(en))
    pl = r["paragraphs"]
    pl["short_flagged"] = [x for x in pl["flagged"] if len(x["french"]) < 80]
    big = [x for x in pl["flagged"] if len(x["french"]) >= 80]
    pl["flagged"] = [x for x in big if x["ratio"] < 0.7 or x["ratio"] > 1.8]
    pl["long_review"] = [x for x in big if 0.7 <= x["ratio"] <= 1.8]
    waived = []
    for w in waivers().get(unit, []):  # one glossary entry on one scan: a misfire on a correct translation
        if "entry" not in w:
            continue
        g = r["glossary"]
        for key in ("missing", "fewer"):
            for item in list(g[key]):
                if item.startswith("%s (scan %s," % (w["entry"], w["scan"])) or \
                        item.startswith("%s (scan %s:" % (w["entry"], w["scan"])):
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
    if mk_fail:
        fail.append("apparatus marks by scan: %s" % ", ".join(mk_fail))
    if short:
        fail.append("scans short against the French: %s" % "; ".join(short))
    fl = r["french_left"]
    if fl["flagged_sentences"] or fl["french_in_formula_text"] or fl["elisions"]:
        fail.append("French left: %d sentences, %d formula boxes, %d elisions" % (
            len(fl["flagged_sentences"]), len(fl["french_in_formula_text"]), fl["elisions"]))
    p = r["paragraphs"]
    if p["unmatched"] or p["flagged"] or p["paragraphs_french"] != p["paragraphs_english"]:
        fail.append("paragraphs: French %d, English %d, %d length ratios out of 0.7-1.8" % (
            p["paragraphs_french"], p["paragraphs_english"], len(p["flagged"])))
    g = r["glossary"]
    if g["missing"]:
        fail.append("glossary: %d terms missing" % len(g["missing"]))
    if g["british_spellings"]:
        fail.append("British spellings: %s" % ", ".join(g["british_spellings"]))
    if not r["labels"]["tags"]["same"]:
        fail.append("labels: tags")
    if macro_diff:
        review.append("macro counts outside formulas (French, English): %s" % macro_diff)
    harmless = [x for x in new_cs if x not in D.DANGER] + [x for x in new_env if x not in D.DANGER_ENV]
    if harmless:
        review.append("control sequences or environments the French does not have: %s" % harmless)
    if fl["french_words"]:
        review.append("French function words: %s" % fl["french_word_counts"])
    if fl["accented_words"]:
        review.append("accented words: %s" % ", ".join(fl["accented_words"]))
    if g["missing_review"]:
        review.append("glossary terms of level review not found: %s" % "; ".join(g["missing_review"]))
    if g["fewer"]:
        review.append("terms found fewer times than their French: %d" % len(g["fewer"]))
    if not r["labels"]["items"]["same"]:
        review.append("item labels differ")
    if nme:
        review.append("m-bar formulas kept in the English: %d (of %d)" % (nme, nmf))
    if fo["spacing_only"]:
        review.append("formulas identical up to spacing: %d" % fo["spacing_only"])
    if fo["text_only"]:
        review.append("formulas changed only in the wording of text-mode boxes: %d" % len(fo["text_only"]))
    if fo["moved"]:
        review.append("formulas moved: %d" % len(fo["moved"]))
    if fo.get("raised_endings"):
        review.append("raised endings of his abbreviations written out with them: %d" % len(fo["raised_endings"]))
    if p["short_flagged"]:
        review.append("short paragraphs with a length ratio out of 0.7-1.5: %d" % len(p["short_flagged"]))
    if p["long_review"]:
        review.append("paragraphs with a length ratio of 1.5-1.8: %d" % len(p["long_review"]))
    if long_:
        review.append("scans long against the French: %s" % "; ".join(long_))
    if mk_review:
        review.append("other marks by scan: %s" % ", ".join(mk_review))
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
    """checks/WAIVERS.jsonl: {"unit", "fail_prefix" | "fail" | ("entry", "scan"), "reason", "by", "date"}, one per
    check that is a false alarm on a correct translation."""
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
          "## 1. Formulas, anchors, labels, marks",
          "formulas: French %d, English %d; identical %d, identical up to spacing %d, changed %d, missing %d, added %d"
          "; m-bar formulas left out: French %d, kept in the English %d"
          % (f["french"], f["english"], f["identical"], f["spacing_only"], len(f["changed"]), len(f["missing"]),
             len(f["added"]), r["mbar"]["french"], r["mbar"]["english_kept"])]
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
    L += ["apparatus marks by scan that differ: %s" % (", ".join(r["marks_by_scan"]["fail"]) or "none"),
          "other marks by scan that differ: %s" % (", ".join(r["marks_by_scan"]["review"]) or "none"),
          "scans short against the French: %s; long: %s" % ("; ".join(r["scan_lengths"]["short"]) or "none",
                                                            "; ".join(r["scan_lengths"]["long"]) or "none"),
          "macros outside formulas whose count differs (French, English): %s" % (r["macros_differing"] or "none"),
          "control sequences the French does not have: %s; environments: %s" % (
              r["new_control_sequences"] or "none", r["new_environments"] or "none"), "",
          "## 2. French left",
          "French function words: %d %s; elisions: %d" % (fl["french_words"], fl["french_word_counts"], fl["elisions"]),
          "sentences with several French words: %d" % len(fl["flagged_sentences"])]
    L += ["- %s" % x for x in fl["flagged_sentences"]]
    L += ["accented words: %s" % (", ".join(fl["accented_words"]) or "none"),
          "French left in the text-mode wording of formulas: %d of %d runs%s" % (
              len(fl["french_in_formula_text"]), fl["formula_texts"],
              (": " + "; ".join(fl["french_in_formula_text"])) if fl["french_in_formula_text"] else ""), "",
          "## 3. Paragraph lengths",
          "paragraphs: French %d, English %d, unmatched %d; measured %d; English/French length of the running text: "
          "median %s, min %s, max %s, whole text %s" % (p["paragraphs_french"], p["paragraphs_english"], p["unmatched"],
                                                       p["measured"], p["ratio_median"], p["ratio_min"],
                                                       p["ratio_max"], p["ratio_total"])]
    L += ["- ratio %s: FR `%s` / EN `%s`" % (x["ratio"], x["french"], x["english"]) for x in p["flagged"]]
    L += ["- ratio %s (review): FR `%s` / EN `%s`" % (x["ratio"], x["french"], x["english"])
          for x in p.get("long_review", []) + p.get("short_flagged", [])]
    L += ["", "## 4. Glossary",
          "entry-scan pairs with the English form: %d of %d (%d across a scan break); occurrences covered %d of %d" % (
              g["present"], g["entry_pages"], len(g["across_page_break"]), g["occurrences_covered"],
              g["occurrences_french"])]
    L += ["- missing: %s" % x for x in g["missing"]]
    L += ["- missing (level review): %s" % x for x in g["missing_review"]]
    L += ["- fewer: %s" % x for x in g["fewer"]]
    L += ["- across a scan break: %s" % x for x in g["across_page_break"]]
    L += ["British spellings: %s" % (", ".join(g["british_spellings"]) or "none")]
    return "\n".join(L) + "\n"


def english_body(unit, raw):
    if raw:
        p = os.path.join(T.ROOT, "runs", "out", unit + ".tex")
        return T.read(p) if os.path.exists(p) else None
    u = T.unit_map()[unit]
    p = os.path.join(T.ROOT, "translation", "units", u["package"], unit + ".tex")
    return T.read(p) if os.path.exists(p) else None


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
        print("%-28s %s %s%s" % (u, r["verdict"], "; ".join(r["fail"])[:600],
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
        tot["formulas_identical"] += r["formulas"]["identical"]
        tot["formulas_spacing"] += r["formulas"]["spacing_only"]
        tot["formulas_text_only"] += len(r["formulas"].get("text_only", []))
        tot["formulas_moved"] += len(r["formulas"].get("moved", []))
        tot["formulas_changed"] += len(r["formulas"]["changed"]) + len(r["formulas"]["missing"])
        tot["mbar"] += r["mbar"]["french"]
        tot["mbar_kept"] += r["mbar"]["english_kept"]
        tot["anchors"] += r["anchors"]["french"]
        tot["entry_pages"] += r["glossary"]["entry_pages"]
        tot["present"] += r["glossary"]["present"]
        tot["paragraphs"] += r["paragraphs"]["paragraphs_french"]
        tot["review_units"] += bool(r["review"])
    L += ["## Totals over the checked units", "",
          "formulas (m-bar formulas left out) %d: identical %d, identical up to spacing %d, changed only in the wording "
          "of text-mode boxes %d, moved %d, changed or missing %d; m-bar formulas written out %d of %d; page anchors %d; "
          "paragraphs %d; glossary entry-scans with the English form %d of %d; units with points to review %d" % (
              tot["formulas"], tot["formulas_identical"], tot["formulas_spacing"], tot["formulas_text_only"],
              tot["formulas_moved"], tot["formulas_changed"], tot["mbar"] - tot["mbar_kept"], tot["mbar"],
              tot["anchors"], tot["paragraphs"], tot["present"], tot["entry_pages"], tot["review_units"]), ""]
    T.write(os.path.join(CK, "SUMMARY.md"), "\n".join(L))


if __name__ == "__main__":
    main()
