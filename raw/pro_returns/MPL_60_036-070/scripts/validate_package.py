#!/usr/bin/env python3
"""Structural checks for MPL_60_036-070; never assesses manuscript fidelity.

The combined fragment must be the byte-for-byte concatenation of page files.
Unknown control words are reported for manual review, not silently approved or
automatically rejected: a static list cannot enumerate all standard LaTeX/TikZ.
No OCR, image reading, contextual interpretation, or transcription correction.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import zipfile
from pathlib import Path


PREFIX = "MPL_60_036-070"
EXPECTED = list(range(36, 71))
COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
           "first_words_or_objects", "transcribed"]
CUSTOM = set("cotefile scanpage mspage deleted inserted margin uline uuline "
             "diagram figure unsure illegible".split())
STANDARD = set("""
begin end label ref eqref tag notag nonumber text textrm textit textbf textsf
texttt textnormal emph mb mbox hbox parbox fbox boxed textcircled llcorner
par smallskip medskip bigskip noindent
quad qquad enspace thinspace space hfill vfill newline linebreak pagebreak
newpage clearpage left right middle big Big bigg Bigg bigl bigr Bigl Bigr
biggl biggr Biggl Biggr mathrm mathit mathbf mathsf mathtt mathcal mathfrak
mathbb mathscr mathnormal boldsymbol bm operatorname displaystyle textstyle
scriptstyle scriptscriptstyle limits nolimits substack overset underset
stackrel binom tbinom dbinom frac dfrac tfrac sqrt bar overline underline
hat widehat tilde widetilde dot ddot dddot vec overbrace underbrace
overrightarrow overleftarrow overleftrightarrow accent acute grave breve
check ring H phantom hphantom vphantom smash raisebox makebox vcenter
multicolumn multirow arraystretch le leq ge geq neq ne lt gt nleq ngeq
equiv sim simeq approx cong asymp propto doteq triangleq coloneqq colon
in notin ni owns subset subseteq supset supseteq nsubseteq nsupseteq
subsetneq supsetneq prec preceq succ succeq ll gg triangleleft triangleright
unlhd unrhd lhd rhd mid nmid parallel nparallel perp models vdash dashv
vdashV Vdash Vvdash to gets mapsto longmapsto hookrightarrow hookleftarrow
rightarrow leftarrow leftrightarrow Rightarrow Leftarrow Leftrightarrow
longrightarrow longleftarrow longleftrightarrow Longrightarrow
Longleftarrow Longleftrightarrow twoheadrightarrow twoheadleftarrow
rightarrowtail leftarrowtail rightsquigarrow leftrightsquigarrow
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow nearrow searrow
swarrow nwarrow rightleftarrows leftrightarrows rightrightarrows
leftleftarrows rightleftharpoons leftrightharpoons leftharpoonup
leftharpoondown rightharpoonup rightharpoondown xrightarrow xleftarrow
rightsquigarrow dashrightarrow dashleftarrow multimap leadsto
sum prod coprod int iint iiint oint bigcup bigcap bigvee bigwedge
bigoplus bigotimes bigodot biguplus bigsqcup cup cap sqcup sqcap vee wedge
oplus otimes odot ominus oslash circ bullet cdot times div pm mp ast star
diamond dagger ddagger setminus smallsetminus wr amalg uplus boxplus boxtimes
ldots cdots vdots ddots dots dotsc dotsb dotsm dotsi dotso infinity infty
emptyset varnothing partial nabla forall exists nexists neg lnot land lor
top bot ell hbar imath jmath Re Im wp aleph beth gimel daleth angle measuredangle
triangle square Box Diamond surd prime backprime flat natural sharp
langle rangle lbrace rbrace lbrack rbrack lceil rceil lfloor rfloor
vert Vert lvert rvert lVert rVert backslash not mathrel mathbin mathord
mathop mathopen mathclose mathpunct mathinner prescript sideset
sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh coth exp log ln
lg lim liminf limsup inf sup min max det dim hom ker gcd Pr deg arg
injlim projlim varinjlim varprojlim mod bmod pmod pod
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota
kappa varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma
tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma
Upsilon Phi Psi Omega
arrow ar draw node path coordinate fill filldraw clip foreach matrix
usetikzlibrary tikzset pgfmathsetmacro pgfmathtruncatemacro pgfplotsset
tikzcdset tikz scope endscope color textcolor colorbox fcolorbox
cdashline hline cline cr crcr omit span centering raggedright raggedleft
textbackslash textasciitilde textasciicircum textquoteleft textquoteright
textquotedblleft textquotedblright textendash textemdash textdegree
textsuperscript textsubscript ensuremath LaTeX TeX S P copyright pounds
oe OE ae AE aa AA o O l L ss i j IJ ij u v c r b d t k
""".split())
ALLOWED_ENVS = set("""
math displaymath equation equation* align align* aligned alignedat alignat
alignat* gather gather* gathered multline multline* split cases array
matrix pmatrix bmatrix Bmatrix vmatrix Vmatrix smallmatrix tikzcd tikzpicture
scope tabular tabular* center flushleft flushright minipage quotation quote
itemize enumerate description
""".split())


def strip_comments(text: str) -> str:
    """Remove unescaped percent comments; preserve newlines/positions."""
    output = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for i, char in enumerate(line):
            if char == "%":
                j = i - 1
                while j >= 0 and line[j] == "\\":
                    j -= 1
                if (i - j - 1) % 2 == 0:
                    cut = i
                    break
        output.append(line[:cut] + ("\n" if cut < len(line) and line.endswith("\n") else ""))
    return "".join(output)


def braces(text: str) -> list[str]:
    """Check grouping braces, ignoring comments and escaped literal braces."""
    clean = strip_comments(text)
    stack = []
    problems = []
    i = 0
    while i < len(clean):
        char = clean[i]
        if char == "\\":
            if i + 1 < len(clean) and not clean[i + 1].isalpha():
                i += 2
                continue
            # \verb is unusual in these fragments, but its content is literal.
            verb = re.match(r"\\verb\*?([^A-Za-z\s])", clean[i:])
            if verb:
                start = i + verb.end()
                stop = clean.find(verb.group(1), start)
                if stop < 0:
                    problems.append("unterminated \\verb")
                    break
                i = stop + 1
                continue
        elif char == "{":
            stack.append(clean.count("\n", 0, i) + 1)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                problems.append(f"unmatched closing brace at line {clean.count(chr(10), 0, i) + 1}")
        i += 1
    problems.extend(f"unmatched opening brace at line {line}" for line in stack)
    return problems


def validate(root: Path, partial: bool, extra_commands: set[str]) -> dict:
    errors = []
    warnings = []
    pages = {}
    pattern = re.compile(rf"{re.escape(PREFIX)}_60_scan(\d{{3}})\.tex")
    page_dir = root / "pages"
    if not page_dir.is_dir():
        errors.append("pages/ directory is missing")
    for path in sorted(page_dir.glob("*.tex")):
        match = pattern.fullmatch(path.name)
        if not match or int(match.group(1)) not in EXPECTED:
            errors.append(f"unexpected page filename: {path.name}")
            continue
        scan = int(match.group(1))
        pages[scan] = path
    present = sorted(pages)
    target = EXPECTED[:len(present)] if partial else EXPECTED
    if present != target:
        errors.append(f"page sequence is {present}; expected {target}")

    unknown_commands = {}
    unknown_envs = {}
    combined_bytes = b""
    for scan, path in sorted(pages.items()):
        data = path.read_bytes()
        combined_bytes += data
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path.name}: invalid UTF-8: {exc}")
            continue
        clean = strip_comments(text)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if markers != [str(scan)] and markers != [f"{scan:03d}"]:
            errors.append(f"{path.name}: expected one matching scanpage marker; found {markers}")
        if scan == EXPECTED[0]:
            if not re.match(r"\s*\\cotefile\{60\}\s*\\scanpage\{0*36\}", clean):
                errors.append(f"{path.name}: must start with \\cotefile{{60}} then \\scanpage{{36}}")
        elif not re.match(rf"\s*\\scanpage\{{0*{scan}\}}", clean):
            errors.append(f"{path.name}: must start with its scanpage marker")
        if re.search(r"\\(?:documentclass|usepackage|newcommand|renewcommand|def|input|includegraphics)\b", clean):
            errors.append(f"{path.name}: preamble, definition, input, or image command found")
        errors.extend(f"{path.name}: {problem}" for problem in braces(text))
        commands = set(re.findall(r"\\([A-Za-z]+)", clean))
        unknown = commands - CUSTOM - STANDARD - extra_commands
        if unknown:
            unknown_commands[path.name] = sorted(unknown)
        envs = set(re.findall(r"\\(?:begin|end)\{([^{}]+)\}", clean))
        if envs - ALLOWED_ENVS:
            unknown_envs[path.name] = sorted(envs - ALLOWED_ENVS)
        stack = []
        for kind, name in re.findall(r"\\(begin|end)\{([^{}]+)\}", clean):
            if kind == "begin":
                stack.append(name)
            elif not stack or stack.pop() != name:
                errors.append(f"{path.name}: mismatched environment ending {name}")
        if stack:
            errors.append(f"{path.name}: unclosed environments {stack}")

    combined = root / f"{PREFIX}_transcription.tex"
    if not combined.is_file():
        errors.append("combined transcription is missing")
    elif combined.read_bytes() != combined_bytes:
        errors.append("combined transcription is not the exact ordered byte concatenation of page files")

    inventory = root / f"{PREFIX}_inventory.csv"
    row_count = 0
    inventory_scans = set()
    seen_elements = set()
    if not inventory.is_file():
        errors.append("inventory CSV is missing")
    else:
        with inventory.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != COLUMNS:
                errors.append(f"inventory columns must be exactly {COLUMNS}; found {reader.fieldnames}")
            else:
                for row_count, row in enumerate(reader, 1):
                    location = f"inventory row {row_count + 1}"
                    if None in row or any(value is None for value in row.values()):
                        errors.append(f"{location}: malformed number of CSV fields")
                        continue
                    try:
                        scan = int(row["scan"])
                    except ValueError:
                        errors.append(f"{location}: noninteger scan")
                        continue
                    inventory_scans.add(scan)
                    if row["cote"] != "60" or scan not in EXPECTED:
                        errors.append(f"{location}: unexpected cote or scan")
                    if row["sheet_kind"] not in {"text", "reused_typed", "cancelled_draft", "cover"}:
                        errors.append(f"{location}: invalid sheet_kind")
                    if row["kind"] not in {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}:
                        errors.append(f"{location}: invalid kind")
                    if row["transcribed"] != "yes":
                        errors.append(f"{location}: transcribed is not yes")
                    if any(not row[key].strip() for key in COLUMNS):
                        errors.append(f"{location}: empty required field")
                    key = (scan, row["element"])
                    if key in seen_elements:
                        errors.append(f"{location}: duplicate scan/element identifier {key}")
                    seen_elements.add(key)
        if inventory_scans != set(present):
            errors.append(f"inventory scan coverage {sorted(inventory_scans)} differs from page files {present}")

    for filename in [f"{PREFIX}_doubts.md", "progress.log"] + ([] if partial else [f"{PREFIX}_notes.md"]):
        if not (root / filename).is_file():
            errors.append(f"required file is missing: {filename}")
    if unknown_commands:
        warnings.append("unrecognized control words need manual review; this checker does not decide whether they are standard")
    if unknown_envs:
        warnings.append("unrecognized environments need manual review")
    warnings.append("Structural checks cannot establish reading accuracy, completeness of image coverage, or correctness of inventory descriptions.")
    if partial:
        warnings.append("PARTIAL MODE: this result never certifies a complete package, even if all pages happen to exist.")
    return {"mode": "partial" if partial else "full", "structural_pass": not errors,
            "page_count": len(present), "scans": present, "inventory_rows": row_count,
            "errors": errors, "warnings": warnings, "unknown_commands": unknown_commands,
            "unknown_environments": unknown_envs}


def make_zip(root: Path, destination: Path) -> None:
    if destination.exists():
        raise FileExistsError(f"will not overwrite existing archive: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.is_symlink() or path.resolve() == destination.resolve():
                continue
            relative = path.relative_to(root)
            if "__pycache__" in relative.parts or path.suffix == ".pyc":
                continue
            archive.write(path, relative.as_posix())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package_directory", type=Path)
    parser.add_argument("--partial", action="store_true", help="validate only the current sequential prefix; never report a complete package")
    parser.add_argument("--allow-command", action="append", default=[], help="manually reviewed standard command to accept, without backslash; repeatable")
    parser.add_argument("--zip", type=Path, metavar="DESTINATION", help="create a new ZIP after structural checks pass; partial mode cannot package")
    args = parser.parse_args()
    if args.partial and args.zip:
        parser.error("--zip is disabled in --partial mode; checkpoint creation is handled separately")
    root = args.package_directory.resolve()
    result = validate(root, args.partial, set(args.allow_command))
    if args.zip and result["structural_pass"]:
        if result["unknown_commands"] or result["unknown_environments"]:
            result["errors"].append("packaging requires manual resolution of unknown commands/environments")
            result["structural_pass"] = False
        else:
            try:
                make_zip(root, args.zip.resolve())
                result["archive"] = str(args.zip.resolve())
            except (OSError, zipfile.BadZipFile) as exc:
                result["errors"].append(f"packaging failed: {exc}")
                result["structural_pass"] = False
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["structural_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
