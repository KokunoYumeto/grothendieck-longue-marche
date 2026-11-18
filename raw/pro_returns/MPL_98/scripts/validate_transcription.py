#!/usr/bin/env python3
"""Mechanical checks for MPL_98; never an image, reading, or mathematics audit.

Run from any directory. This program does not edit the transcription. Optional
reports and compile files go only to --output (default: a system temporary dir).
Use --partial during transcription and omit it for the complete 43-page set.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import tempfile
from collections import Counter
from pathlib import Path


HEADER = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
STATE_MACROS = {"cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
                "uline", "uuline", "diagram", "figure", "unsure", "illegible"}
# A conservative aid, not a replacement for the package symbol tables. Unknown
# names are review candidates, not automatically nonstandard editorial macros.
KNOWN_COMMANDS = set("""
Alpha Beta Gamma Delta Epsilon Zeta Eta Theta Iota Kappa Lambda Mu Nu Xi Omicron
Pi Rho Sigma Tau Upsilon Phi Chi Psi Omega alpha beta gamma delta epsilon
varepsilon zeta eta theta vartheta iota kappa varkappa lambda mu nu xi omicron
pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
aleph beth gimel daleth ell hbar imath jmath wp Re Im partial nabla infty
emptyset varnothing forall exists nexists neg lnot top bot angle triangle
square Box Diamond diamondsuit heartsuit clubsuit spadesuit prime backprime
sum prod coprod int iint iiint oint bigcap bigcup bigvee bigwedge bigoplus
bigotimes bigodot biguplus bigsqcup lim limsup liminf min max inf sup det dim
deg gcd hom ker Pr exp log ln sin cos tan cot sec csc arcsin arccos arctan
sinh cosh tanh coth mod bmod pmod pod operatorname mathop limits nolimits
cdot times div ast star circ bullet odot oplus ominus otimes oslash boxplus
boxtimes amalg cap cup uplus sqcap sqcup vee wedge land lor setminus smallsetminus
wr diamond triangleleft triangleright bigtriangleup bigtriangledown
le leq leqslant ge geq geqslant ne neq equiv sim simeq approx cong asymp doteq
propto ll gg prec succ preceq succeq subset supset subseteq supseteq subsetneq
supsetneq sqsubset sqsupset sqsubseteq sqsupseteq in ni owns notin mid nmid
parallel nparallel perp vdash dashv models smile frown not
to gets leftarrow rightarrow leftrightarrow Leftarrow Rightarrow Leftrightarrow
longleftarrow longrightarrow longleftrightarrow Longleftarrow Longrightarrow
Longleftrightarrow mapsto longmapsto hookleftarrow hookrightarrow
leftharpoonup leftharpoondown rightharpoonup rightharpoondown rightleftharpoons
leftrightharpoons leftrightarrows rightleftarrows twoheadleftarrow
twoheadrightarrow tailleftarrow tailrightarrow uparrow downarrow updownarrow
Uparrow Downarrow Updownarrow nearrow searrow swarrow nwarrow leadsto
xrightarrow xleftarrow overset underset stackrel overline underline overbrace
underbrace hat widehat check breve acute grave tilde widetilde bar vec dot ddot
dddot ddddot boxed fbox framebox phantom hphantom vphantom smash
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
langle rangle lbrace rbrace lbrack rbrack lceil rceil lfloor rfloor vert Vert
backslash slash lmoustache rmoustache lgroup rgroup
mathbf mathit mathrm mathsf mathtt mathnormal mathcal mathbb mathfrak boldsymbol
text textnormal textrm textsf texttt textbf textit textsl textsc emph mbox
mathrm mathalpha mathbin mathrel mathord mathopen mathclose mathpunct
quad qquad enspace thinspace medspace thickspace negthinspace hspace vspace
hfill vfill kern mkern hskip vskip smallskip medskip bigskip noindent indent
par newline linebreak newpage clearpage pagebreak raggedright centering
begin end substack multicolumn cline hline arraystretch cr displaystyle
textstyle scriptstyle scriptscriptstyle label ref eqref tag notag nonumber
section subsection subsubsection paragraph subparagraph item chapter part
footnote footnotemark footnotetext marginpar title author date maketitle
S P dag ddag copyright pounds aa AA ae AE oe OE o O ss l L i j t H c d b v u r
LaTeX TeX dots ldots cdots vdots ddots dotsc dotsb dotsm dotsi dotso
rule raisebox makebox parbox shortstack textsuperscript textsubscript
normalfont rmfamily sffamily ttfamily upshape itshape slshape scshape bfseries
mdseries tiny scriptsize footnotesize small normalsize large Large LARGE huge Huge
ensuremath protect relax leavevmode mathstrut strut natural textcircled checkmark
arrow ar arrows draw path node coordinate fill filldraw clip shade shadedraw
matrix foreach pgfextra pgfmathsetmacro tikz tikzset tikzstyle tikzcdmatrixname
endpgfextra color textcolor
""".split())
REQUIRED_PACKAGES = ["article.cls", "amsmath.sty", "amssymb.sty", "tikz.sty",
                     "tikz-cd.sty", "xcolor.sty", "geometry.sty",
                     "inputenc.sty", "fontenc.sty", "lmodern.sty"]


def remove_comments(text: str) -> str:
    """Keep line count, removing an unescaped percent and the rest of its line."""
    result = []
    for line in text.splitlines(keepends=True):
        for i, char in enumerate(line):
            if char == "%":
                n = 0
                j = i - 1
                while j >= 0 and line[j] == "\\":
                    n += 1
                    j -= 1
                if n % 2 == 0:
                    line = line[:i] + ("\n" if line.endswith("\n") else "")
                    break
        result.append(line)
    return "".join(result)


def structural_errors(text: str) -> list[dict]:
    """Checks literal braces/environments, not TeX expansion or catcodes."""
    text = remove_comments(text)
    errors, stack = [], []
    line = 1
    i = 0
    while i < len(text):
        char = text[i]
        if char == "\n":
            line += 1
        if char == "\\":
            # An escaped single character cannot open or close a brace group.
            if i + 1 < len(text) and not text[i + 1].isalpha():
                i += 2
                continue
        if char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                errors.append({"check": "braces", "line": line,
                               "message": "unmatched closing brace"})
        i += 1
    for opening in stack:
        errors.append({"check": "braces", "line": opening,
                       "message": "unclosed opening brace"})
    envs = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", text):
        op, name = match.groups()
        at = text.count("\n", 0, match.start()) + 1
        if op == "begin":
            envs.append((name, at))
        elif not envs:
            errors.append({"check": "environments", "line": at,
                           "message": f"end of unopened environment {name}"})
        elif envs[-1][0] != name:
            errors.append({"check": "environments", "line": at,
                           "message": f"environment end {name}; expected {envs[-1][0]}"})
        else:
            envs.pop()
    for name, at in envs:
        errors.append({"check": "environments", "line": at,
                       "message": f"unclosed environment {name}"})
    return errors


def command_words(text: str) -> list[str]:
    """Read control words without mistaking the second slash of \\\\ for one."""
    return [match.group(1) for match in re.finditer(r"\\([A-Za-z@]+|.)", text, re.DOTALL)
            if match.group(1)[0].isalpha() or match.group(1)[0] == "@"]


def tex_availability(environment: dict | None = None) -> dict:
    engines = {name: shutil.which(name) for name in
               ("lualatex", "xelatex", "pdflatex", "latexmk", "kpsewhich")}
    packages = {}
    for package in REQUIRED_PACKAGES:
        path = None
        if engines["kpsewhich"]:
            run = subprocess.run([engines["kpsewhich"], package],
                                 capture_output=True, text=True, timeout=10,
                                 env=environment)
            path = run.stdout.strip() or None
        packages[package] = path
    optional = {}
    if engines["kpsewhich"]:
        run = subprocess.run([engines["kpsewhich"], "ulem.sty"],
                             capture_output=True, text=True, timeout=10,
                             env=environment)
        optional["ulem.sty"] = run.stdout.strip() or None
    return {"executables": engines, "packages": packages,
            "optional_packages": optional}


def make_harness(files: list[Path], destination: Path) -> Path:
    # Large paper avoids forcing the manuscript diagrams into book-size pages.
    # Colored state wrappers are deliberately simple: this is a syntax harness,
    # not a critical edition layout or a replacement for the manuscript images.
    preamble = r"""\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[paperwidth=420mm,paperheight=594mm,margin=20mm]{geometry}
\usepackage{amsmath,amssymb,xcolor,tikz,tikz-cd}
\IfFileExists{ulem.sty}{\usepackage[normalem]{ulem}}{%
  \typeout{MPL98: ulem absent; simple underline wrappers used for syntax only.}}
\providecommand{\uline}[1]{\underline{#1}}
\providecommand{\uuline}[1]{\underline{\underline{#1}}}
\usetikzlibrary{arrows.meta,calc,decorations.pathmorphing,positioning}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\newcommand{\cotefile}[1]{\par\section*{Cote #1}}
\newcommand{\scanpage}[1]{\clearpage\subsection*{Scan #1}}
\newcommand{\mspage}[1]{\par\textbf{Manuscript page #1}\par}
% Streaming wrappers consume only the literal opening brace, never the body.
% This preserves tikz-cd ampersand tokenization even in inserted/marginal groups.
\def\deleted{\bgroup\color{red!70!black}\let\mplwrapperopen=}
\def\inserted{\bgroup\color{blue!70!black}\let\mplwrapperopen=}
\def\margin{\par\bgroup\color{violet}\aftergroup\par\let\mplwrapperopen=}
\def\unsure{\bgroup\color{orange!60!black}\let\mplwrapperopen=}
\newcommand{\illegible}[1]{\textnormal{[illegible: #1]}}
% Do not pre-read diagram arguments: tikz-cd must tokenize its own ampersands.
% The literal group already supplied by \diagram{...} supplies grouping.
\def\diagram{\par\bgroup\centering\aftergroup\par\let\mplwrapperopen=}
\def\figure{\par\bgroup\centering\aftergroup\par\let\mplwrapperopen=}
\begin{document}
\textit{Syntax-validation harness. Red: deleted; blue: inserted; orange:
uncertain; violet: marginal. Color does not certify a reading or placement.}
"""
    inputs = []
    for path in files:
        # Current filenames contain no TeX-significant characters. Refuse one
        # rather than silently interpolate arbitrary paths into executable TeX.
        if any(char in str(path) for char in "{}%#\\"):
            raise ValueError("A page path has characters unsafe for TeX input")
        inputs.append("\\input{" + path.as_posix() + "}\n")
    harness = destination / "syntax_harness.tex"
    harness.write_text(preamble + "".join(inputs) + "\\end{document}\n", encoding="utf-8")
    return harness


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true")
    parser.add_argument("--compile", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--tex-environment", type=Path,
                        help="JSON environment overrides generated by setup_tex_validation.py")
    args = parser.parse_args()
    base = args.base.resolve()
    output = (args.output or Path(tempfile.mkdtemp(prefix="mpl98-validation-"))).resolve()
    output.mkdir(parents=True, exist_ok=True)
    tex_environment = dict(os.environ)
    if args.tex_environment:
        overrides = json.loads(args.tex_environment.read_text(encoding="utf-8"))
        allowed = {"TEXMF", "TEXMFVAR", "TEXMFCONFIG", "TEXFORMATS", "TEXFONTMAPS"}
        if not isinstance(overrides, dict) or set(overrides) - allowed or not all(isinstance(value, str) for value in overrides.values()):
            parser.error("--tex-environment must contain only the documented TeX path variables with string values")
        tex_environment.update(overrides)
    report = {"scope": "mechanical only; no image, paleographic, or mathematical checking",
              "base": str(base), "partial": args.partial, "errors": [], "warnings": [],
              "pages": [], "state_macros_allowed": sorted(STATE_MACROS)}
    errors = report["errors"]
    warnings = report["warnings"]
    files = sorted((base / "pages").glob("MPL_98_98_scan*.tex"))
    numbers, contents = [], []
    commands = Counter()
    for path in files:
        match = re.fullmatch(r"MPL_98_98_scan(\d{3})\.tex", path.name)
        if not match:
            errors.append({"file": path.name, "check": "filename", "message": "unexpected filename"})
            continue
        number = int(match.group(1))
        numbers.append(number)
        text = path.read_text(encoding="utf-8")
        contents.append(text)
        clean = remove_comments(text)
        page_report = {"scan": number, "file": path.name,
                       "bytes": path.stat().st_size, "lines": text.count("\n") + 1}
        report["pages"].append(page_report)
        markers = re.findall(r"\\scanpage\s*\{([^{}]*)\}", clean)
        if markers != [str(number)]:
            errors.append({"file": path.name, "check": "scanpage", "message": f"markers {markers!r}; expected [{str(number)!r}]"})
        prefixes = r"\s*(?:\\cotefile\s*\{98\}\s*)?\\scanpage\s*\{" + str(number) + r"\}"
        if not re.match(prefixes, clean):
            errors.append({"file": path.name, "check": "top marker", "message": "scan marker is not first, apart from optional cote marker"})
        cote = re.findall(r"\\cotefile\s*\{([^{}]*)\}", clean)
        if cote != (["98"] if number == 2 else []):
            errors.append({"file": path.name, "check": "cotefile", "message": "cote marker must occur exactly once on scan 002"})
        forbidden = re.findall(r"\\(?:documentclass|usepackage|RequirePackage|newcommand|renewcommand|providecommand|def|gdef|edef|xdef|input|include)\b|\\(?:begin|end)\s*\{document\}", clean)
        if forbidden:
            errors.append({"file": path.name, "check": "fragment", "message": "preamble, definition, or file-input command present", "commands": forbidden})
        for issue in structural_errors(text):
            errors.append({"file": path.name, **issue})
        commands.update(command_words(clean))
    expected = list(range(2, (max(numbers) if numbers else 1) + 1)) if args.partial else list(range(2, 45))
    if not files or numbers != expected or any(n < 2 or n > 44 for n in numbers):
        errors.append({"check": "page sequence", "message": "page set differs from required contiguous sequence", "present": numbers, "expected": expected})
    report["commands_seen"] = dict(sorted(commands.items()))
    report["state_macro_counts"] = {name: commands[name] for name in sorted(STATE_MACROS)}
    report["commands_for_review"] = sorted(set(commands) - STATE_MACROS - KNOWN_COMMANDS)
    if report["commands_for_review"]:
        warnings.append("Commands outside the conservative standard/TikZ/editorial list require review: " + ", ".join(report["commands_for_review"]))
    warnings.append("Command inventory is reported, but classifying all macros as standard requires TeX compilation or manual review; brace balance alone is not TeX validation.")

    inventory = base / "MPL_98_inventory.csv"
    coverage, keys = Counter(), set()
    if not inventory.exists():
        errors.append({"check": "inventory", "message": "inventory absent"})
    else:
        with inventory.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != HEADER:
                errors.append({"check": "inventory header", "message": "header differs", "found": reader.fieldnames})
            for line, row in enumerate(reader, 2):
                row_errors = []
                if None in row or any(row.get(field) is None for field in HEADER):
                    row_errors.append("wrong field count")
                try:
                    scan = int(row.get("scan", ""))
                except (ValueError, TypeError):
                    scan = -1
                    row_errors.append("scan is not an integer")
                if scan not in numbers:
                    row_errors.append("scan has no page file")
                if row.get("cote") != "98":
                    row_errors.append("cote is not 98")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    row_errors.append("invalid sheet_kind")
                if row.get("kind") not in KINDS:
                    row_errors.append("invalid element kind")
                if row.get("transcribed") != "yes":
                    row_errors.append("transcribed is not yes")
                for field in ["element", "position", "first_words_or_objects"]:
                    if not row.get(field, "").strip():
                        row_errors.append(f"empty {field}")
                key = (scan, row.get("element"))
                if key in keys:
                    row_errors.append("duplicate element identifier within page")
                keys.add(key)
                coverage[scan] += 1
                if row_errors:
                    errors.append({"check": "inventory row", "line": line, "message": "; ".join(row_errors)})
        for number in numbers:
            if not coverage[number]:
                errors.append({"check": "inventory coverage", "scan": number, "message": "no rows"})
    report["inventory_rows_by_scan"] = dict(sorted(coverage.items()))

    combined = base / "MPL_98_transcription.tex"
    if combined.exists():
        text = combined.read_text(encoding="utf-8")
        cursor = 0
        for number, part in zip(numbers, contents):
            part = part.strip()
            while cursor < len(text) and text[cursor].isspace():
                cursor += 1
            if not text.startswith(part, cursor):
                errors.append({"check": "combined", "scan": number, "message": "combined differs from page sequence (ignoring only inter-page whitespace)"})
                break
            cursor += len(part)
        else:
            if text[cursor:].strip():
                errors.append({"check": "combined", "message": "extra content after last page"})
        report["combined_present"] = True
    else:
        report["combined_present"] = False
        (warnings if args.partial else errors).append("Combined fragment is absent." if args.partial else {"check": "combined", "message": "combined fragment absent"})

    report["tex_availability"] = tex_availability(tex_environment)
    report["tex_environment_file"] = str(args.tex_environment) if args.tex_environment else None
    if not report["tex_availability"]["optional_packages"].get("ulem.sty"):
        warnings.append("ulem.sty is unavailable; the syntax harness supplies simple underline/double-underline definitions without line wrapping.")
    harness = make_harness(files, output)
    report["harness"] = str(harness)
    if args.compile:
        unavailable = [name for name, path in report["tex_availability"]["packages"].items() if not path]
        engine = report["tex_availability"]["executables"]["pdflatex"]
        if not engine or unavailable:
            report["compilation"] = {"status": "not run: dependencies unavailable", "missing_packages": unavailable, "engine": engine}
            warnings.append("Compilation was requested but could not be attempted because the TeX dependency preflight failed.")
        else:
            try:
                run = subprocess.run([engine, "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", harness.name], cwd=output, env=tex_environment, capture_output=True, text=True, timeout=120)
                (output / "compile_stdout.txt").write_text(run.stdout + run.stderr, encoding="utf-8")
                report["compilation"] = {"status": "passed" if run.returncode == 0 else "failed", "exit_code": run.returncode, "output": str(output / "compile_stdout.txt")}
                if run.returncode:
                    errors.append({"check": "compilation", "message": "TeX exited unsuccessfully; inspect the compile log"})
            except subprocess.TimeoutExpired:
                report["compilation"] = {"status": "timed out after 120 seconds"}
                errors.append({"check": "compilation", "message": "timed out"})
    else:
        report["compilation"] = {"status": "not requested"}
    report["mechanical_status"] = "passed" if not errors else "failed"
    report["limitations"] = [
        "No images were read or compared by this program.",
        "Inventory rows marked yes are checked as data; completeness or correctness against images is not established.",
        "Authorial versus archive foliation, uncertainty readings, deletion placement, and diagram geometry are not verified.",
        "No mathematical statement, proof, or research claim is checked.",
        "Brace/environment checks are lexical and assume ordinary LaTeX catcodes; verbatim constructs or macro-generated environments need separate review.",
        "The syntax harness uses simple colored state wrappers and is not a diplomatic layout specification."]
    destination = output / "validation_report.json"
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"mechanical_status": report["mechanical_status"], "page_count": len(files), "inventory_rows": sum(coverage.values()), "errors": errors, "warnings": warnings, "compilation": report["compilation"], "report": str(destination), "harness": str(harness)}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
