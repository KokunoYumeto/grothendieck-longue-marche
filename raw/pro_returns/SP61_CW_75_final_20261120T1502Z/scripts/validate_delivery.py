#!/usr/bin/env python3
"""Mechanical delivery checks; no OCR, rendering, or reading decisions.

Usage: python3 scripts/validate_delivery.py OUTPUT_DIRECTORY [--strict-macros]

Unknown TeX commands are warnings unless --strict-macros is supplied: the
standard/package command catalogue below is deliberately finite. This checker
cannot establish fidelity to a scan, completeness of collation, or TeX semantics.
It never changes any file and never invokes a compiler.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from pathlib import Path


PREFIX = "SP61_CW_75"
SCANS = tuple(range(16, 26))
PAGE_NAMES = {
    scan: f"{'J75-02' if scan < 18 else 'J75-03'}_75_scan{scan:03d}.tex"
    for scan in SCANS
}
CUSTOM = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible handwritten".split())
# A practical catalogue, not a replacement for LaTeX/package documentation.
STANDARD = set("""
begin end par medskip smallskip bigskip noindent indent newline linebreak pagebreak
newpage clearpage hfill vfill quad qquad qquad text textup textnormal textrm textsf
texttt textit textsl textbf emph underline overline overbrace underbrace left right
middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr frac dfrac tfrac
cfrac binom dbinom tbinom sqrt root overset underset stackrel substack mathchoice
mathrm mathit mathbf mathsf mathtt mathcal mathscr mathfrak mathbb mathnormal
operatorname operatornamewithlimits DeclareMathOperator limits nolimits displaystyle
textstyle scriptstyle scriptscriptstyle phantom hphantom vphantom smash raisebox
mbox fbox boxed makebox framebox parbox rule vspace hspace vspace* hspace* kern mkern
setlength tag label ref eqref notag nonumber allowdisplaybreaks displaybreak
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon
phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
aleph beth gimel daleth ell hbar hslash imath jmath wp Re Im partial nabla infty
emptyset varnothing forall exists nexists neg lnot top bot vdots ddots cdots ldots
dots dotsb dotsc dotsm dotso dotsi prime backprime star ast circ bullet cdot times
div pm mp otimes oplus ominus odot oslash bigotimes bigoplus bigodot uplus sqcup
sqcap cup cap bigcup bigcap biguplus bigsqcup wedge vee bigwedge bigvee amalg wr
setminus smallsetminus triangleleft triangleright bigtriangleup bigtriangledown
diamond Box square Diamond angle measuredangle sphericalangle complement degree
le leq leqq leqslant ge geq geqq geqslant ne neq equiv sim simeq approx approxeq
cong asymp doteq doteqdot eqcirc circeq triangleq propto ll gg lesssim gtrsim
lessapprox gtrapprox lessgtr gtrless lesseqgtr gtreqless prec succ preceq succeq
precsim succsim precapprox succapprox in notin ni owns subset supset subseteq
supseteq subsetneq supsetneq subsetneqq supsetneqq varsubsetneq varsupsetneq
sqsubset sqsupset sqsubseteq sqsupseteq nsubseteq nsupseteq nsubseteqq nsupseteqq
parallel nparallel mid nmid vdash dashv models Vdash vDash Vvdash nvdash nvDash
perp smile frown not therefore because colon ratio proportion
to gets mapsto longmapsto rightarrow leftarrow leftrightarrow longrightarrow
longleftarrow longleftrightarrow Rightarrow Leftarrow Leftrightarrow Longrightarrow
Longleftarrow Longleftrightarrow iff implies impliesby uparrow downarrow updownarrow
Uparrow Downarrow Updownarrow nearrow searrow swarrow nwarrow hookrightarrow
hookleftarrow twoheadrightarrow twoheadleftarrow rightarrowtail leftarrowtail
leftharpoonup leftharpoondown rightharpoonup rightharpoondown rightleftharpoons
leftrightharpoons rightsquigarrow leftrightsquigarrow leadsto dashrightarrow
dashleftarrow curvearrowright curvearrowleft circlearrowright circlearrowleft
xrightarrow xleftarrow overrightarrow overleftarrow overleftrightarrow
underleftarrow underrightarrow underleftrightarrow vec hat widehat tilde widetilde
bar dot ddot dddot ddddot check breve acute grave mathring
sum prod coprod int iint iiint iiiint idotsint oint bigcap bigcup lim limsup liminf
sup inf max min arg det dim deg gcd hom ker coker Pr exp log ln lg sin cos tan cot
sec csc arcsin arccos arctan sinh cosh tanh coth bmod pmod mod pod
langle rangle lbrace rbrace lbrack rbrack lvert rvert lVert rVert vert Vert backslash
lceil rceil lfloor rfloor ulcorner urcorner llcorner lrcorner land lor
item itemindent leftmargin rightmargin itemsep parsep topsep partopsep
footnote footnotemark footnotetext footnotesize scriptsize tiny small normalsize
large Large LARGE huge Huge centering raggedright raggedleft textsuperscript
textsubscript textcircled textbackslash textasciitilde textasciicircum textbar
textendash textemdash textdegree textquotedblleft textquotedblright textquotesingle
textquotedbl guillemotleft guillemotright guilsinglleft guilsinglright
aa AA ae AE oe OE o O l L ss i j P S dag ddag copyright pounds euro
color textcolor colorbox fcolorbox sout xout uwave dashuline dotuline
draw path node coordinate fill filldraw clip foreach pgfmathsetmacro tikzset
tikz linewidth rm leftrightarrows
usetikzlibrary arrow arrows matrix graph scope pgftransformrotate
pgftransformshift pgftransformscale pgfpoint pgfusepath pgfpathmoveto
pgfpathlineto pgfpathcurveto pgfpathclose pgfsetlinewidth pgfsetdash
multicolumn multirow hline cline vline arraystretch tabcolsep arraycolsep
shortstack vphantom texorpdfstring ensuremath mathop mathrel mathbin mathord mathpunct
mathopen mathclose mathinner boldsymbol pmb underbracket overbracket
qquad space thinspace negthinspace enspace enskip hss vss nulldelimiterspace
""".split())
FORBIDDEN = set("documentclass usepackage newcommand renewcommand providecommand def gdef edef xdef let newenvironment renewenvironment input include".split())
H_ONLY = set("page pages dating foldertitle note ill drawing".split())
COLLATION_HEADER = [
    "folder", "their_page", "our_scan", "line", "their_reading", "codex_reading",
    "final_reading", "scan_shows", "kind", "marked_in_H", "confidence",
]
INVENTORY_HEADER = [
    "scan", "sheet_kind", "hand", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
KINDS = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state (struck given live or live given struck)", "insertion or placement",
    "abbreviation expanded or spelling modernised", r"readable ink left as \ill{}",
    "drawing or diagram", "other",
}
SHEET_KINDS = {"text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
FORBIDDEN_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".tif", ".bmp", ".svg", ".pdf", ".zip", ".tar", ".gz", ".bz2", ".7z", ".rar", ".pyc"}


def without_comments(text: str) -> str:
    """Remove TeX comments, retaining line numbers and escaped percent signs."""
    lines = []
    for line in text.splitlines(keepends=True):
        cut = None
        for i, char in enumerate(line):
            if char == "%":
                j = i - 1
                while j >= 0 and line[j] == "\\":
                    j -= 1
                if (i - 1 - j) % 2 == 0:
                    cut = i
                    break
        lines.append(line if cut is None else line[:cut] + ("\n" if line.endswith("\n") else ""))
    return "".join(lines)


def check_tex(text: str, label: str, strict_macros: bool = False):
    """Return errors/warnings for structural TeX syntax only."""
    errors, warnings = [], []
    clean = without_comments(text)
    braces, envs = [], []
    # Check delimiter balance independently. Text boxes and minipages legally
    # suspend their surrounding math mode, so a flat token scan must not reject
    # dollars or displays merely because an outer delimiter remains open.
    math = {"$": [], r"\[": [], r"\(": []}
    unknown = set()
    token = re.compile(r"\\(?:begin|end)\s*\{[^{}]*\}|\\[A-Za-z@]+\*?|\\[^A-Za-z@]|[{}$]")
    for match in token.finditer(clean):
        value = match.group()
        line = clean.count("\n", 0, match.start()) + 1
        if value == "{":
            braces.append(line)
        elif value == "}":
            if braces:
                braces.pop()
            else:
                errors.append(f"{label}:{line}: unmatched closing brace")
        elif re.match(r"\\(?:begin|end)\s*\{", value):
            opening = value.startswith(r"\begin")
            env = value[value.index("{") + 1:-1].strip()
            if opening:
                envs.append((env, line))
            elif not envs or envs[-1][0] != env:
                errors.append(f"{label}:{line}: mismatched end of environment {env}")
            else:
                envs.pop()
        elif value in ("$", r"\[", r"\]", r"\(", r"\)"):
            if value == "$":
                if math["$"]:
                    math["$"].pop()
                else:
                    math["$"].append(line)
            elif value in (r"\[", r"\("):
                math[value].append(line)
            else:
                expected = {r"\]": r"\[", r"\)": r"\("}[value]
                if math[expected]:
                    math[expected].pop()
                else:
                    errors.append(f"{label}:{line}: unmatched math delimiter {value}")
        elif value.startswith("\\") and len(value) > 1 and value[1].isalpha():
            command = value[1:].rstrip("*")
            if command in {"begin", "end"}:
                errors.append(f"{label}:{line}: environment command lacks a simple braced name")
            elif command in FORBIDDEN or command in H_ONLY:
                errors.append(f"{label}:{line}: disallowed fragment command \\{command}")
            elif command not in STANDARD and command not in CUSTOM:
                unknown.add(command)
    errors.extend(f"{label}:{line}: unclosed brace" for line in braces)
    errors.extend(f"{label}:{line}: unclosed environment {env}" for env, line in envs)
    errors.extend(f"{label}:{line}: unclosed math delimiter {delim}" for delim, lines in math.items() for line in lines)
    if "$$" in clean:
        errors.append(f"{label}: double-dollar display used; expected \\[ ... \\]")
    if unknown:
        message = f"{label}: commands outside finite catalogue: " + ", ".join("\\" + s for s in sorted(unknown))
        (errors if strict_macros else warnings).append(message)
    return errors, warnings


def read_table(path: Path, delimiter: str, expected_header: list[str], errors: list[str]):
    if not path.is_file():
        errors.append(f"missing {path.name}")
        return []
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream, delimiter=delimiter)
            if reader.fieldnames != expected_header:
                errors.append(f"{path.name}: header differs from required ordered columns")
            rows = list(reader)
        for number, row in enumerate(rows, 2):
            if None in row or any(v is None for v in row.values()):
                errors.append(f"{path.name}:{number}: malformed column count")
        return rows
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{path.name}: {exc}")
        return []


def validate(root: Path, strict_macros: bool = False):
    errors, warnings = [], []
    pages = []
    for scan in SCANS:
        path = root / "pages" / PAGE_NAMES[scan]
        if not path.is_file():
            errors.append(f"missing pages/{path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        pages.append(text)
        e, w = check_tex(text, str(path.relative_to(root)), strict_macros)
        errors.extend(e)
        warnings.extend(w)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", without_comments(text))
        if markers != [str(scan)]:
            errors.append(f"{path.name}: expected exactly one scanpage{{{scan}}}")
    if (root / "pages").is_dir():
        extra = set(p.name for p in (root / "pages").glob("*.tex")) - set(PAGE_NAMES.values())
        if extra:
            errors.append("unexpected page files: " + ", ".join(sorted(extra)))

    combined = root / f"{PREFIX}_transcription.tex"
    if not combined.is_file():
        errors.append(f"missing {combined.name}")
    else:
        text = combined.read_text(encoding="utf-8")
        clean = without_comments(text)
        markers = re.findall(r"\\cotefile\s*\{([^{}]*)\}", clean)
        if markers != ["75"] or not re.match(r"\s*\\cotefile\s*\{75\}", clean):
            errors.append(f"{combined.name}: expected exactly one leading cotefile{{75}}")
        if len(pages) == len(SCANS):
            # Only boundary whitespace may differ; page-internal bytes are preserved.
            page_chunks = [p.strip() for p in pages]
            full = text.strip()
            if not re.match(r"\s*\\cotefile\s*\{75\}", without_comments(pages[0])):
                full = re.sub(r"^\\cotefile\s*\{75\}\s*", "", full, count=1)
            position = 0
            for scan, chunk in zip(SCANS, page_chunks):
                while position < len(full) and full[position].isspace():
                    position += 1
                if not full.startswith(chunk, position):
                    errors.append(f"{combined.name}: differs from concatenated page content at scan {scan}")
                    break
                position += len(chunk)
            else:
                if full[position:].strip():
                    errors.append(f"{combined.name}: surplus content after last page")
        e, w = check_tex(text, combined.name, strict_macros)
        errors.extend(e)
        warnings.extend(w)

    inventory = read_table(root / f"{PREFIX}_inventory.csv", ",", INVENTORY_HEADER, errors)
    seen_scans = set()
    for number, row in enumerate(inventory, 2):
        label = f"inventory:{number}"
        try:
            seen_scans.add(int(row.get("scan", "")))
        except (TypeError, ValueError):
            errors.append(f"{label}: invalid scan")
        if row.get("transcribed") != "yes":
            errors.append(f"{label}: transcribed must be yes")
        if row.get("kind") not in ELEMENT_KINDS:
            errors.append(f"{label}: unsupported element kind")
        if row.get("sheet_kind") not in SHEET_KINDS:
            errors.append(f"{label}: unsupported sheet kind")
    if seen_scans != set(SCANS):
        errors.append("inventory does not cover exactly scans 16–25")
    collation = read_table(root / f"{PREFIX}_collation.tsv", "\t", COLLATION_HEADER, errors)
    for number, row in enumerate(collation, 2):
        label = f"collation:{number}"
        try:
            scan, their_page = int(row.get("our_scan", "")), int(row.get("their_page", ""))
            if scan not in SCANS or their_page != scan - 1:
                errors.append(f"{label}: scan/page mapping invalid")
            if row.get("folder") != ("J75-02" if scan < 18 else "J75-03"):
                errors.append(f"{label}: folder mapping invalid")
        except (TypeError, ValueError):
            errors.append(f"{label}: nonnumeric scan/page")
        if row.get("confidence") not in {"high", "medium", "low"}:
            errors.append(f"{label}: invalid confidence")
        if row.get("kind") not in KINDS:
            errors.append(f"{label}: unsupported kind")
    check_path = root / "CHECK_EVENTS.tsv"
    if not check_path.is_file():
        errors.append("missing CHECK_EVENTS.tsv")
    else:
        with check_path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream, delimiter="\t")
            normalized = {re.sub(r"[ -]+", "_", s.lower()) for s in (reader.fieldnames or [])}
            if not {"statement_id", "date", "who", "type", "outcome"} <= normalized:
                errors.append("CHECK_EVENTS.tsv: missing one of statement_id, date, who, type, outcome")
            for number, row in enumerate(reader, 2):
                if None in row or any(v is None for v in row.values()):
                    errors.append(f"CHECK_EVENTS.tsv:{number}: malformed column count")
    for suffix in ("changes.md", "doubts.md", "notes.md", "sheet_feedback.md", "hand_log.md"):
        if not (root / f"{PREFIX}_{suffix}").is_file():
            errors.append(f"missing {PREFIX}_{suffix}")
    if not (root / "progress.log").is_file():
        errors.append("missing progress.log")
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"image/archive/compiled artifact inside output: {path.relative_to(root)}")

    hash_file = root / "transcription_hashes.sha256"
    if hash_file.is_file():
        hashed = set()
        for number, line in enumerate(hash_file.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line)
            if not match:
                errors.append(f"{hash_file.name}:{number}: malformed hash entry")
                continue
            digest, name = match.groups()
            path = root / name
            if not path.resolve().is_relative_to(root.resolve()):
                errors.append(f"{hash_file.name}:{number}: path escapes output directory")
                continue
            hashed.add(name)
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest.lower():
                errors.append(f"frozen hash mismatch or missing file: {name}")
        required_hashes = {f"pages/{name}" for name in PAGE_NAMES.values()} | {combined.name}
        if not required_hashes <= hashed:
            errors.append("freeze hash manifest omits a page or combined transcription")
    else:
        warnings.append("transcription_hashes.sha256 absent; frozen hashes not checked")
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--strict-macros", action="store_true")
    args = parser.parse_args()
    try:
        errors, warnings = validate(args.output_directory, args.strict_macros)
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    for message in warnings:
        print("WARNING: " + message)
    for message in errors:
        print("ERROR: " + message)
    print(f"Mechanical validation: {len(errors)} error(s), {len(warnings)} warning(s).")
    print("This result does not verify readings, mathematical claims, or completeness against the scans.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
