#!/usr/bin/env python3
"""Static syntax diagnostics and an optional LaTeX compilation wrapper.

This reads only saved page fragments. It never opens source scans or context,
never changes page fragments, and never writes completion/audit/freeze records.
Static checks are deliberately not a claim of visual or mathematical accuracy.

    python scripts/check_tex_structure.py
    python scripts/check_tex_structure.py --write-wrapper
    python scripts/check_tex_structure.py --compile

The diagnostic rendering displays editorial annotations using colors. It is
not a publication edition: in particular deletion content is colored gray,
rather than struck through, to keep paragraph and mathematics handling robust.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess


CUSTOM = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())
STANDARD = set("""
Huge huge LARGE Large large small footnotesize scriptsize tiny normalsize
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda
mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
begin end par bfseries sffamily rmfamily ttfamily itshape slshape scshape mdseries
textbf textit textsf texttt textrm textnormal emph
mathbb mathcal mathfrak mathbf mathrm mathsf mathtt mathit mathnormal boldsymbol
text operatorname mathop mathrel mathbin mathord mathopen mathclose mathpunct
operatorname nolimits limits displaystyle textstyle scriptstyle scriptscriptstyle
frac dfrac tfrac binom dbinom tbinom sqrt root of
sum prod coprod int iint iiint oint lim limsup liminf varlimsup varliminf
varprojlim varinjlim inf sup min max det dim deg hom Hom ker coker gcd Pr exp log ln
sin cos tan cot sec csc sinh cosh tanh coth arcsin arccos arctan
in notin ni owns subset supset subseteq supseteq subsetneq supsetneq
le leq ge geq neq ne equiv sim simeq cong approx asymp propto
to gets leftarrow rightarrow longleftarrow longrightarrow leftrightarrow
longleftrightarrow Leftarrow Rightarrow Longleftarrow Longrightarrow
Leftrightarrow Longleftrightarrow mapsto longmapsto hookrightarrow hookleftarrow
xrightarrow xleftarrow twoheadrightarrow twoheadleftarrow rightleftarrows
leftrightarrows rightarrowtail leftarrowtail uparrow downarrow Uparrow Downarrow
leadsto rightsquigarrow lhook rhook joinrel upharpoonright
times div cdot cdots ldots dots vdots ddots bullet ast star circ bigcirc
otimes oplus odot ominus oslash bigotimes bigoplus bigodot
wedge vee bigwedge bigvee cap cup bigcap bigcup sqcap sqcup amalg uplus biguplus
forall exists nexists neg emptyset varnothing infty partial nabla hbar ell wp
Re Im aleph beth gimel daleth top bot perp parallel shortmid shortparallel
mid Vert vert lvert rvert lVert rVert langle rangle lceil rceil lfloor rfloor
backslash setminus smallsetminus angle triangle prime
bar overline underline underbrace overbrace widehat hat check tilde widetilde
dot ddot dddot ddddot breve acute grave vec overset underset stackrel
left right big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
quad qquad enspace hspace vspace thinspace medspace thickspace negthinspace
phantom vphantom hphantom smash strut mathstrut raisebox makebox mbox hbox
boxed fbox framebox substack hline cline multicolumn
draw fill node path coordinate scope foreach clip filldraw
arrow ar edge matrix label tag tagstar notag nonumber
ensuremath color textcolor
""".split())
SPECIAL_STANDARD = set(" !,;:#%&_$^{}\\/[]()'\"`~=.-".strip("\n"))
ENVIRONMENTS = set("""
array aligned alignedat gathered split cases matrix pmatrix bmatrix Bmatrix
vmatrix Vmatrix smallmatrix tikzcd tikzpicture scope center flushleft flushright
minipage tabular equation equation* align align* gather gather* multline multline*
""".split())

# These commands require mathematical mode.  Text-capable spacing, phantom,
# underline, and editorial commands are intentionally omitted.
MATH_ONLY = set("""
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda
mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
mathbb mathcal mathfrak mathbf mathrm mathsf mathtt mathit mathnormal boldsymbol
operatorname mathop mathrel mathbin mathord mathopen mathclose mathpunct
nolimits limits displaystyle textstyle scriptstyle scriptscriptstyle
frac dfrac tfrac binom dbinom tbinom sqrt root
sum prod coprod int iint iiint oint lim limsup liminf varlimsup varliminf
varprojlim varinjlim inf sup min max det dim deg hom ker coker gcd Pr exp log ln
sin cos tan cot sec csc sinh cosh tanh coth arcsin arccos arccos arctan
in notin ni owns subset supset subseteq supseteq subsetneq supsetneq
le leq ge geq neq ne equiv sim simeq cong approx asymp propto
to gets leftarrow rightarrow longleftarrow longrightarrow leftrightarrow
longleftrightarrow Leftarrow Rightarrow Longleftarrow Longrightarrow
Leftrightarrow Longleftrightarrow mapsto longmapsto hookrightarrow hookleftarrow
xrightarrow xleftarrow twoheadrightarrow twoheadleftarrow rightleftarrows
leftrightarrows rightarrowtail leftarrowtail uparrow downarrow Uparrow Downarrow
leadsto rightsquigarrow lhook rhook joinrel upharpoonright
times div cdot cdots ldots dots vdots ddots bullet ast star circ bigcirc
otimes oplus odot ominus oslash bigotimes bigoplus bigodot
wedge vee bigwedge bigvee cap cup bigcap bigcup sqcap sqcup amalg uplus biguplus
forall exists nexists neg emptyset varnothing infty partial nabla hbar ell wp
Re Im aleph beth gimel daleth top bot perp parallel shortmid shortparallel
mid Vert vert lvert rvert lVert rVert langle rangle lceil rceil lfloor rfloor
backslash setminus smallsetminus angle triangle prime
bar overline underbrace overbrace widehat hat check tilde widetilde
dot ddot dddot ddddot breve acute grave vec overset underset stackrel
left right big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
boxed substack
""".split())
# LaTeX/amsmath's dots commands select text ellipses when used outside math.
MATH_ONLY.difference_update({"ldots", "dots"})
TEXT_ARGUMENTS = set("text mbox hbox textnormal textrm textsf texttt textbf textit textsl textsc emph".split())
MATH_ARGUMENTS = {"ensuremath"}
MATH_ENVIRONMENTS = set("equation equation* align align* gather gather* multline multline*".split())
MATH_REQUIRED_ENVIRONMENTS = set("array aligned alignedat gathered split cases matrix pmatrix bmatrix Bmatrix vmatrix Vmatrix smallmatrix".split())


def math_mode_issues(text: str, filename: str) -> list[dict]:
    """Conservative mode checks, including math cells and nested text boxes.

Editorial commands preserve the current mode. tikzcd cells are mathematical,
while TikZ picture/node content starts as text. Text-taking commands recurse
in text mode so an explicit $...$ inside \\text is handled independently.
This models the supplied diagnostic wrapper; it is not a full TeX expansion
engine and intentionally does not claim to evaluate arbitrary macro programs.
"""
    text = strip_comments(text)
    issues = []

    def add(offset: int, message: str) -> None:
        issues.append({"file": filename, "line": text.count("\n", 0, offset) + 1,
                       "kind": "math mode", "severity": "error", "message": message})

    def group_span(start: int) -> tuple[int, int, int] | None:
        while start < len(text) and text[start].isspace():
            start += 1
        body, end = argument(text, start)
        return (start + 1, end - 1, end) if body is not None else None

    def walk(start: int, end: int, initial_math: bool) -> None:
        math = initial_math
        environments = []
        displays = []
        i = start
        while i < end:
            char = text[i]
            if char == "\\":
                match = re.match(r"\\([A-Za-z@]+|.)", text[i:])
                if not match:
                    i += 1
                    continue
                name = match.group(1)
                after = i + len(match.group(0))
                if name in {"begin", "end"}:
                    env, env_end = argument(text, after)
                    if env is not None:
                        if name == "begin":
                            environments.append((env, math))
                            if env in MATH_REQUIRED_ENVIRONMENTS and not math:
                                add(i, "Math-only environment outside math mode: " + env)
                            if env == "tikzcd" or env in MATH_ENVIRONMENTS | MATH_REQUIRED_ENVIRONMENTS:
                                math = True
                            elif env in {"tikzpicture", "tabular", "minipage"}:
                                math = False
                        elif environments and environments[-1][0] == env:
                            _, math = environments.pop()
                        i = env_end
                        continue
                if name in TEXT_ARGUMENTS | MATH_ARGUMENTS:
                    span = group_span(after)
                    if span:
                        walk(span[0], span[1], name in MATH_ARGUMENTS)
                        i = span[2]
                        continue
                if name in {"[", "("}:
                    displays.append((name, math))
                    math = True
                elif name in {"]", ")"}:
                    wanted = "[" if name == "]" else "("
                    if displays and displays[-1][0] == wanted:
                        _, math = displays.pop()
                    else:
                        math = False
                elif name in MATH_ONLY and not math:
                    add(i, "Math-only command outside math mode: \\" + name)
                i = after
                continue
            if char == "{":
                span = group_span(i)
                if span:
                    walk(span[0], span[1], math)
                    i = span[2]
                    continue
            if char == "$":
                math = not math
                i += 2 if text[i:i + 2] == "$$" else 1
                continue
            if char in "_^" and not math:
                add(i, "Math-only script character outside math mode: " + char)
            i += 1

    walk(0, len(text), False)
    return issues


def strip_comments(text: str) -> str:
    """Preserve offsets/newlines so diagnostics retain source line numbers."""
    out = list(text)
    i = 0
    while i < len(text):
        if text[i] == "\\":
            match = re.match(r"\\(?:[A-Za-z@]+|.)", text[i:])
            i += len(match.group(0)) if match else 1
        elif text[i] == "%":
            end = text.find("\n", i)
            if end < 0:
                end = len(text)
            out[i:end] = " " * (end - i)
            i = end
        else:
            i += 1
    return "".join(out)


def argument(text: str, start: int) -> tuple[str | None, int]:
    """Read one braced argument; control-symbol braces are not grouping."""
    while start < len(text) and text[start].isspace():
        start += 1
    if start >= len(text) or text[start] != "{":
        return None, start
    depth = 1
    i = start + 1
    while i < len(text):
        if text[i] == "\\":
            match = re.match(r"\\(?:[A-Za-z@]+|.)", text[i:])
            i += len(match.group(0)) if match else 1
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if not depth:
                return text[start + 1:i], i + 1
        i += 1
    return None, len(text)


def visible_remainder(text: str) -> str:
    """Strip spacing and phantom constructions, retaining visible symbols."""
    output = []
    i = 0
    while i < len(text):
        match = re.match(r"\\(?:vphantom|hphantom|phantom)\b", text[i:])
        if match:
            body, end = argument(text, i + len(match.group(0)))
            if body is not None:
                i = end
                continue
        output.append(text[i])
        i += 1
    result = "".join(output)
    result = re.sub(r"\\(?:quad|qquad|enspace|thinspace|medspace|thickspace)\b", "", result)
    result = re.sub(r"\\[ ,;!\[\]\(\)]", "", result)
    return re.sub(r"[\s{}$]", "", result)


def inspect(path: Path) -> list[dict]:
    text = strip_comments(path.read_text(encoding="utf-8"))
    issues: list[dict] = []

    def add(kind: str, offset: int, message: str, severity: str = "error") -> None:
        issues.append({"file": path.name, "line": text.count("\n", 0, offset) + 1,
                       "kind": kind, "severity": severity, "message": message})

    braces: list[int] = []
    envs: list[tuple[str, int]] = []
    maths: list[tuple[str, int]] = []
    lefts: list[int] = []
    unknowns: set[str] = set()
    i = 0
    while i < len(text):
        char = text[i]
        if char == "\\":
            match = re.match(r"\\([A-Za-z@]+|.)", text[i:])
            if not match:
                add("command", i, "Trailing backslash")
                i += 1
                continue
            name = match.group(1)
            end = i + len(match.group(0))
            if name not in CUSTOM | STANDARD | SPECIAL_STANDARD and name not in unknowns:
                add("macro", i, "Unrecognized macro: \\" + name, "warning")
                unknowns.add(name)
            if name in {"begin", "end"}:
                env, _ = argument(text, end)
                if env is None:
                    add("environment", i, "Missing braced environment name")
                elif name == "begin":
                    envs.append((env, i))
                    if env not in ENVIRONMENTS:
                        add("environment", i, "Unrecognized environment: " + env, "warning")
                elif not envs:
                    add("environment", i, "Unmatched end of " + env)
                elif envs[-1][0] != env:
                    add("environment", i, "Expected end of " + envs[-1][0] + "; found " + env)
                else:
                    envs.pop()
            if name in {"[", "("}:
                maths.append((name, i))
            elif name in {"]", ")"}:
                wanted = "[" if name == "]" else "("
                if not maths or maths[-1][0] != wanted:
                    add("math delimiter", i, "Unmatched or mismatched \\" + name)
                else:
                    maths.pop()
            elif name == "left":
                lefts.append(i)
            elif name == "right":
                if not lefts:
                    add("delimiter", i, "Unmatched \\right")
                else:
                    lefts.pop()
            if name == "unsure":
                body, _ = argument(text, end)
                if body is None:
                    add("doubt", i, "Missing or unclosed unsure argument")
                elif not visible_remainder(body):
                    kind = "phantom-only unsure" if re.search(r"\\(?:[vh]?phantom)\b", body) else "empty unsure"
                    add("doubt", i, kind + ": \\unsure{" + body + "}")
            i = end
            continue
        if char == "{":
            braces.append(i)
        elif char == "}":
            if braces:
                braces.pop()
            else:
                add("brace", i, "Unmatched closing brace")
        elif char == "$":
            token = "$$" if text[i:i + 2] == "$$" else "$"
            if maths and maths[-1][0] == token:
                maths.pop()
            else:
                maths.append((token, i))
            i += len(token)
            continue
        i += 1
    for offset in braces:
        add("brace", offset, "Unclosed opening brace")
    for env, offset in envs:
        add("environment", offset, "Unclosed environment " + env)
    for token, offset in maths:
        add("math delimiter", offset, "Unclosed math delimiter " + token)
    for offset in lefts:
        add("delimiter", offset, "Unmatched \\left")
    issues.extend(math_mode_issues(text, path.name))
    return issues


PREAMBLE = r"""\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,tikz-cd,xcolor}
\usepackage[normalem]{ulem}
\setlength{\textwidth}{17cm}
\setlength{\oddsidemargin}{-.5cm}
\setlength{\emergencystretch}{2em}
\newcommand{\cotefile}[1]{\par\section*{Cote #1}}
\newcommand{\scanpage}[1]{\clearpage\section*{Scan #1}}
\newcommand{\mspage}[1]{\par\noindent Manuscript page: #1\par}
\newcommand{\deleted}[1]{{\color{gray}#1}}
\newcommand{\inserted}[1]{{\color{green!40!black}#1}}
\newcommand{\margin}[1]{{\color{violet}#1}}
\newcommand{\unsure}[1]{{\color{red!70!black}#1}}
\newcommand{\illegible}[1]{\ifmmode\text{[illegible #1]}\else[illegible #1]\fi}
\newcommand{\diagram}[1]{#1}
\renewcommand{\figure}[1]{#1}
\let\TextUline\uline
\let\TextUUline\uuline
\renewcommand{\uline}[1]{\ifmmode\underline{#1}\else\TextUline{#1}\fi}
\renewcommand{\uuline}[1]{\ifmmode\underline{\underline{#1}}\else\TextUUline{#1}\fi}
\begin{document}
"""
REQUIRED_TEX = ("latex.ltx", "article.cls", "inputenc.sty", "fontenc.sty",
                "amsmath.sty", "amssymb.sty", "tikz-cd.sty", "xcolor.sty", "ulem.sty")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write-wrapper", action="store_true")
    parser.add_argument("--compile", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    pages = sorted((root / "pages").glob("MPL_159_159_scan*.tex"))
    issues = [issue for page in pages for issue in inspect(page)]
    report = {"files_checked": len(pages), "issues": issues,
              "scope": "Static delimiters, known macros, math-mode contexts, and empty/phantom-only doubts; no source or semantic review."}
    if args.write_wrapper or args.compile:
        output = root / "diagnostics"
        output.mkdir(exist_ok=True)
        wrapper = output / "MPL_159_diagnostic.tex"
        body = "\n".join(r"\input{\detokenize{" + str(p) + "}}" for p in pages)
        wrapper.write_text(PREAMBLE + body + "\n\\end{document}\n", encoding="utf-8")
        report["wrapper"] = str(wrapper)
        if args.compile:
            kpse = shutil.which("kpsewhich")
            missing = []
            for name in REQUIRED_TEX:
                result = subprocess.run([kpse, name], capture_output=True, text=True) if kpse else None
                if result is None or result.returncode or not result.stdout.strip():
                    missing.append(name)
            engine = shutil.which("pdflatex")
            report["missing_tex_dependencies"] = missing
            if missing or engine is None:
                report["compilation"] = "not run: required TeX installation files are unavailable"
            else:
                result = subprocess.run([engine, "-interaction=nonstopmode", "-file-line-error",
                                         "-output-directory", str(output), str(wrapper)],
                                        capture_output=True, text=True, timeout=120)
                (output / "compiler_stdout.txt").write_text(result.stdout + result.stderr, encoding="utf-8")
                report["compilation_exit_code"] = result.returncode
                report["compilation_log"] = str(output / "MPL_159_diagnostic.log")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if any(x["severity"] == "error" for x in issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
