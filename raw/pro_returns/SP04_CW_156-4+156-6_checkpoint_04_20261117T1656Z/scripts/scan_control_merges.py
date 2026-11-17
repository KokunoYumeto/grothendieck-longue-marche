#!/usr/bin/env python3
"""Read-only scan for known TeX commands merged with capital-letter suffixes.

Reports filename, source line, and control-word token only. The suffix rule
is lexical; it makes no manuscript reading or proposed correction.
"""
from pathlib import Path
import argparse
import json

from audit_unsure import mask_comments

OUT = Path(__file__).resolve().parents[1]
PREFIXES = {
    "in", "notin", "ni", "not", "to", "mapsto", "longmapsto", "rightarrow", "leftarrow", "leftrightarrow",
    "longrightarrow", "longleftarrow", "longleftrightarrow", "hookrightarrow", "hookleftarrow", "twoheadrightarrow",
    "twoheadleftarrow", "Rightarrow", "Leftarrow", "Leftrightarrow", "Longrightarrow", "Longleftarrow",
    "Longleftrightarrow", "subset", "subseteq", "subsetneq", "supset", "supseteq", "supsetneq", "nsubseteq",
    "nsupseteq", "equiv", "cong", "simeq", "sim", "approx", "asymp", "neq", "ne", "le", "leq", "ge", "geq",
    "ll", "gg", "prec", "preceq", "succ", "succeq", "perp", "parallel", "mid", "vert", "lvert", "rvert",
    "cup", "cap", "bigcup", "bigcap", "sqcup", "sqcap", "coprod", "prod", "sum", "oplus", "otimes", "ominus",
    "times", "circ", "cdot", "bullet", "star", "ast", "wedge", "vee", "setminus", "backslash", "emptyset",
    "forall", "exists", "nexists", "ldots", "cdots", "vdots", "ddots", "dots", "colon", "triangleleft",
    "alpha", "beta", "gamma", "delta", "epsilon", "varepsilon", "zeta", "eta", "theta", "vartheta", "iota",
    "kappa", "lambda", "mu", "nu", "xi", "pi", "varpi", "rho", "varrho", "sigma", "varsigma", "tau",
    "upsilon", "phi", "varphi", "chi", "psi", "omega", "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi",
    "Sigma", "Upsilon", "Phi", "Psi", "Omega", "mathcal", "mathscr", "mathbb", "mathbf", "mathrm", "mathfrak",
    "mathsf", "mathtt", "overline", "underline", "widehat", "hat", "widetilde", "tilde", "bar", "vec",
    "overbrace", "underbrace", "overset", "underset", "left", "right", "big", "Big", "bigg", "Bigg",
}
KNOWN_WORDS = PREFIXES | {"LaTeX", "TeX", "BibTeX", "ifLuaTeX", "XeTeX", "LuaTeX", "Pr", "Re", "Im"}


def scan(out=OUT):
    findings = []
    for path in sorted((Path(out) / "pages").glob("*.tex")):
        text = mask_comments(path.read_text(encoding="utf-8"))
        i = 0
        while i < len(text):
            if text[i] != "\\":
                i += 1
                continue
            start = i
            i += 1
            if i >= len(text) or not (text[i].isalpha() or text[i] == "@"):
                i += 1
                continue
            end = i
            while end < len(text) and (text[end].isalpha() or text[end] == "@"):
                end += 1
            word = text[i:end]
            i = end
            if word in KNOWN_WORDS:
                continue
            matches = [prefix for prefix in PREFIXES if word.startswith(prefix) and word[len(prefix):]
                       and all("A" <= char <= "Z" for char in word[len(prefix):])]
            if matches:
                findings.append({"filename": path.name, "line": text.count("\n", 0, start)+1, "command_token": "\\"+word})
    return findings


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args()
    print(json.dumps(scan(args.out), ensure_ascii=False, indent=2))
