"""Cut the current French texts of the second pass into units, and write every unit's prompt.

Input: second_pass/CURRENT_TEXT_INDEX.tsv (116 packages, the closed second pass of 12 Nov 2026; column current_text).
Writes (only inside translation_en_20261112):
  source/units/<unit>.tex   each unit, the exact characters of its package's current text (their concatenation is
                            the package, checked)
  source/MANIFEST.json      per package: current text, its sha256, size, scans; per unit: package, cote, scans, his
                            page numbers, offsets, sha256, the whitespace that ends the cut (to join the English)
  prompt/system/<unit>.txt  PROMPT_TEMPLATE.txt (the comparison's, byte for byte) filled with PROMPT_PARTS_LM.txt
  prompt/user/<unit>.txt    the request line and the unit's text
A unit is a run of consecutive scans of one package, cut at \\scanpage lines (all at brace depth 0 in the 116 texts)
into parts of about UNIT_TARGET characters; a cut that would leave a formula, a group or an environment open moves to
the next scan. usage: python -I -B prepare.py
"""
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_lm as T  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
P = os.path.join(T.ROOT, "prompt")
TEMPLATE = T.read(os.path.join(P, "PROMPT_TEMPLATE.txt"))


def parts():
    """PROMPT_PARTS_LM.txt: sections '@@ LM <PLACEHOLDER>' and '@@ SLOT <NAME>'; the text up to the next header."""
    out, cur = {}, None
    for line in T.read(os.path.join(P, "PROMPT_PARTS_LM.txt")).split("\n"):
        m = re.match(r"@@ (LM|SLOT) ([A-Z_]+)\s*$", line)
        if m:
            cur = out.setdefault(m.group(1), {}).setdefault(m.group(2), [])
            continue
        if cur is not None:
            cur.append(line)
    return {w: {k: "\n".join(v).strip("\n") for k, v in d.items()} for w, d in out.items()}


PARTS = parts()
MORE_MACROS = ["uuline", "textsuperscript", "textit", "textbf", "emph", "fbox", "shortstack", "textup", "mbox", "hbox",
               "footnote", "textsc", "underline"]


def balanced(t):
    """No group, environment or formula left open in a cut (comments out)."""
    s = T.strip_comments(t)
    depth, k = 0, 0
    while k < len(s):
        c = s[k]
        if c == "\\":
            k += 2
            continue
        depth += {"{": 1, "}": -1}.get(c, 0)
        if depth < 0:
            return False
        k += 1
    if depth:
        return False
    if collections.Counter(re.findall(r"\\begin\{([^}]*)\}", s)) != collections.Counter(
            re.findall(r"\\end\{([^}]*)\}", s)):
        return False
    rest = T.GC.split_math(s)[0]
    return not re.search(r"\\\[|\\\]|\\\(|\\\)", rest) and len(re.findall(r"(?<!\\)\$", rest)) == 0


def cut(text):
    """Offsets [0, c1, ..., len] of the units of one package."""
    pos = [m.start() for m in re.finditer(r"(?m)^\\scanpage\{", text)]
    n = max(1, round(len(text) / T.UNIT_TARGET))
    cuts = [0]
    for k in range(1, n):
        target = k * len(text) / n
        cands = [p for p in pos[1:] if p > cuts[-1]]
        if not cands:
            break
        best = min(cands, key=lambda p: abs(p - target))
        # move forward until the part before is balanced
        i = pos.index(best)
        while i < len(pos) and not balanced(text[cuts[-1]:pos[i]]):
            i += 1
        if i < len(pos) and pos[i] < len(text):
            cuts.append(pos[i])
    cuts.append(len(text))
    return sorted(set(cuts))


def terms_for(text):
    terms = T.terms()
    hits = T.french_hits(T.running_text(text))
    lines = [terms[fr][0] for fr, *_ in T.glossary() if fr in hits and fr in terms and terms[fr][0] != "-"]
    return lines


def outside_math(text):
    return T.GC.split_math(T.strip_comments(text))[0]


def system_prompt(u, text):
    d = dict(PARTS["LM"])
    rest = outside_math(text)
    more_style = ""
    if T.mbar_formulas(text):
        more_style += "\n" + PARTS["SLOT"]["MBAR"]
    if T.FOOTER in text:
        more_style += "\n" + PARTS["SLOT"]["FOOTER"]
    macros = [m for m in MORE_MACROS if re.search(r"\\%s(?![A-Za-z])" % m, rest)]
    more_app = ""
    if re.search(r"\\(diagram|figure)\{", text):
        more_app += "\n" + PARTS["SLOT"]["DIAGRAMS"]
    if re.search("[\u201c\u201d\u00ab\u00bb]|(?<!\\\\)\"", rest):
        more_app += "\n" + PARTS["SLOT"]["QUOTES"]
    d["WORK"] = d["WORK"].replace("<<COTE>>", "cote " + u["cote"])
    d["STYLE"] = d["STYLE"].replace("<<MORE_STYLE>>", more_style)
    d["TEXT_MACROS"] = d["TEXT_MACROS"].replace("<<MORE_TEXT_MACROS>>", "".join(", \\" + m for m in macros))
    d["APPARATUS"] = d["APPARATUS"].replace("<<MORE_APPARATUS>>", more_app)
    tl = terms_for(text)
    d["TERMS"] = "\n".join("- " + x for x in tl) if tl else "- (none of the glossary's terms occurs on these pages)"
    s = TEMPLATE
    for k, v in d.items():
        s = s.replace("{" + k + "}", v.rstrip("\n"))
    assert not re.search(r"\{[A-Z_]{4,}\}|<<[A-Z_]+>>", s), "unfilled placeholder in " + u["id"]
    return s, len(tl)


def user_prompt(u, text):
    sc = u["scans"]
    ms = u["mspages"]
    head = "Translate this LaTeX into English (La Longue Marche, cote %s, scan%s %s%s; %d page%s)." % (
        u["cote"], "s" if len(sc) > 1 else "", sc[0] if len(sc) == 1 else "%s-%s" % (sc[0], sc[-1]),
        (", manuscript page%s %s" % ("s" if len(set(ms)) > 1 else "",
                                     ms[0] if len(set(ms)) == 1 else "%s-%s" % (ms[0], ms[-1]))) if ms else "",
        len(sc), "s" if len(sc) > 1 else "")
    return head + "\n\n" + text


def main():
    pk, units = [], []
    for r in T.packages():
        text = T.read(r["path"])
        cuts = cut(text)
        pieces = [text[a:b] for a, b in zip(cuts, cuts[1:])]
        assert "".join(pieces) == text
        ids = []
        for (a, b), piece in zip(zip(cuts, cuts[1:]), pieces):
            sc = T.scans_of(piece)
            uid = "%s_s%s-%s" % (r["package"], sc[0], sc[-1]) if len(sc) > 1 else "%s_s%s" % (r["package"], sc[0])
            body = piece.strip("\n") + "\n"
            trail = piece[len(piece.rstrip("\n")):]
            lead = piece[:len(piece) - len(piece.lstrip("\n"))]
            u = {"id": uid, "package": r["package"], "cote": r["cote"], "scans": sc, "n_scans": len(sc),
                 "mspages": T.mspages_of(piece), "start": a, "end": b, "chars": len(body),
                 "sha256": T.sha256_text(piece), "lead": lead, "trail": trail, "balanced": balanced(piece)}
            T.write(os.path.join(T.ROOT, "source", "units", uid + ".tex"), piece)
            units.append(u)
            ids.append(uid)
        pk.append({"package": r["package"], "cote": r["cote"], "scans": r["scans"], "current_text": r["current_text"],
                   "sha256": T.sha256(r["path"]), "chars": len(text), "n_scans": len(T.scans_of(text)),
                   "compile_second_pass": r["compile"], "units": ids})
    man = {"input": os.path.relpath(T.INDEX, T.LM), "input_sha256": T.sha256(T.INDEX), "unit_target": T.UNIT_TARGET,
           "packages": pk, "units": units}
    T.write(os.path.join(T.ROOT, "source", "MANIFEST.json"), json.dumps(man, ensure_ascii=False, indent=1) + "\n")
    nterms, kept = [], []
    for u in units:
        text = T.unit_text(u)
        s, nt = system_prompt(u, text)
        nterms.append(nt)
        if os.path.exists(os.path.join(T.ROOT, "runs", "out", u["id"] + "_result.json")):
            kept.append(u["id"])  # a prompt that was sent stays as it was sent (its sha256 is in the result)
            continue
        T.write(os.path.join(P, "system", u["id"] + ".txt"), s)
        T.write(os.path.join(P, "user", u["id"] + ".txt"), user_prompt(u, text))
    if kept:
        print("prompts already sent, kept as they were: %d" % len(kept))
    sizes = sorted(u["chars"] for u in units)
    print("packages %d, units %d, scans %d; unit chars median %d, min %d, max %d; unbalanced %d; terms per unit "
          "median %d, max %d" % (len(pk), len(units), sum(u["n_scans"] for u in units), sizes[len(sizes) // 2],
                                 sizes[0], sizes[-1], sum(not u["balanced"] for u in units),
                                 sorted(nterms)[len(nterms) // 2], max(nterms)))


if __name__ == "__main__":
    main()
