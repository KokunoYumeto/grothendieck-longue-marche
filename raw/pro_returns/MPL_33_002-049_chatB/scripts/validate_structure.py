#!/usr/bin/env python3
"""Structural checks only; never reads scans and never performs OCR.

This script cannot establish fidelity or completeness against handwriting.
It does not modify any deliverable. Use --partial while work is in progress.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from pathlib import Path


PACKAGE = "MPL_33_002-049"
COTE = "33"
SCANS = set(range(2, 50))
FIELDS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
EDITORIAL = {"cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
             "uline", "uuline", "diagram", "figure", "unsure", "illegible"}
# Unknown commands are reported for human review, rather than rejected: LaTeX
# and TikZ permit many valid commands, and a finite list cannot certify them.
STANDARD = set("""
begin end text textnormal textrm textsf texttt textbf textit emph mbox hbox vbox
mathrm mathsf mathtt mathbf mathit mathcal mathscr mathfrak mathbb operatorname
operatornamewithlimits boldsymbol bm limits nolimits displaystyle textstyle
scriptstyle scriptscriptstyle left right middle big Big bigg Bigg bigl bigr
Bigl Bigr biggl biggr Biggl Biggr frac dfrac tfrac binom dbinom tbinom sqrt
over under atop choose overline underline overbrace underbrace hat widehat
check widecheck tilde widetilde bar vec dot ddot dddot ddddot acute grave breve
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi
varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
aleph beth gimel daleth ell hbar imath jmath wp Re Im partial nabla infty
emptyset varnothing top bot angle triangle square Box Diamond diamond
forall exists nexists neg lnot land lor wedge vee bigwedge bigvee cap cup
bigcap bigcup sqcap sqcup bigsqcup setminus smallsetminus backslash complement
in ni notin subset supset subseteq supseteq nsubseteq nsupseteq subsetneq
supsetneq subsetneqq supsetneqq preceq succeq prec succ ll gg le leq ge geq
leqq geqq leqslant geqslant neq ne equiv sim simeq approx cong asymp propto
parallel nparallel perp mid nmid models vdash dashv Vdash Vvdash not
to gets rightarrow leftarrow leftrightarrow Rightarrow Leftarrow Leftrightarrow
longrightarrow longleftarrow longleftrightarrow Longrightarrow Longleftarrow
Longleftrightarrow mapsto longmapsto hookrightarrow hookleftarrow
twoheadrightarrow twoheadleftarrow rightleftarrows leftrightarrows
rightrightarrows leftleftarrows rightleftharpoons leftrightharpoons
rightarrowtail leftarrowtail rightsquigarrow leftrightsquigarrow leadsto
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow nearrow searrow
swarrow nwarrow xrightarrow xleftarrow overset underset stackrel
times otimes bigotimes oplus bigoplus ominus odot bigodot oslash circ bullet
cdot ast star pm mp div amalg wr sum prod coprod int iint iiint oint
ldots cdots vdots ddots dots dotsb dotsc dotsm dotso primes prime backprime
colon coloneqq eqqcolon lbrace rbrace langle rangle lvert rvert lVert rVert
vert Vert lfloor rfloor lceil rceil brackets lgroup rgroup
hom Hom ker Ker coker Coker im Im lim limsup liminf injlim projlim varinjlim
varprojlim sup inf max min det dim deg rank gcd log ln exp sin cos tan cot
sinh cosh tanh sec csc arg Pr mod bmod pmod pod id Ob Spec End Ext Tor
qquad quad enspace thinspace medspace thickspace hspace vspace kern mkern
phantom hphantom vphantom smash strut mathstrut rule raisebox makebox parbox
par noindent indent newline linebreak pagebreak newpage clearpage smallskip
medskip bigskip hfill vfill centering raggedright raggedleft footnotesize small
normalsize large Large LARGE huge Huge tiny scriptsize normalfont rmfamily
sffamily ttfamily bfseries itshape upshape slshape scshape selectfont
label ref eqref tag nonumber notag textbackslash textasciicircum textasciitilde
textquotedblleft textquotedblright textquoteleft textquoteright textendash
textemdash guillemotleft guillemotright oe OE ae AE aa AA o O ss i j
draw path node coordinate fill filldraw clip foreach pgfmathsetmacro
pgfmathtruncatemacro tikz tikzset arrow ar matrix draw plot
multicolumn multirow hline cline vline toprule midrule bottomrule cmidrule
intertext shortintertext substack genfrac S boxed fbox mathbin mathop rotatebox textcircled
""".split())
FORBIDDEN = {"documentclass", "usepackage", "RequirePackage", "input", "include",
             "includegraphics", "newcommand", "renewcommand", "providecommand",
             "def", "gdef", "edef", "xdef", "newenvironment", "renewenvironment",
             "newtheorem", "DeclareMathOperator", "todo", "TODO"}


class Report:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str):
        self.errors.append(message)

    def warn(self, message: str):
        self.warnings.append(message)


def strip_comments(source: str) -> str:
    """Preserve line numbers; % is escaped only after an odd backslash count."""
    result = []
    for line in source.splitlines(keepends=True):
        cut = len(line)
        for i, char in enumerate(line):
            if char == "%":
                j = i - 1
                while j >= 0 and line[j] == "\\":
                    j -= 1
                if (i - 1 - j) % 2 == 0:
                    cut = i
                    break
        result.append(line[:cut] + ("\n" if cut < len(line) and line.endswith("\n") else ""))
    return "".join(result)


def brace_errors(source: str) -> list[str]:
    source = strip_comments(source)
    stack, errors = [], []
    line, i = 1, 0
    while i < len(source):
        char = source[i]
        if char == "\\":
            # A control symbol consumes the next non-letter, so \{ and \}
            # do not delimit a group, whereas \\ followed by { does.
            i += 1
            if i < len(source) and not source[i].isalpha():
                if source[i] == "\n":
                    line += 1
                i += 1
            continue
        if char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                errors.append(f"unmatched closing brace at line {line}")
        elif char == "\n":
            line += 1
        i += 1
    errors.extend(f"unclosed opening brace at line {line}" for line in stack)
    return errors


def control_words(source: str):
    """Yield control words while consuming control symbols such as \\\\."""
    i = 0
    while i < len(source):
        if source[i] != "\\":
            i += 1
            continue
        start = i
        i += 1
        if i == len(source):
            break
        if not ("A" <= source[i] <= "Z" or "a" <= source[i] <= "z"):
            i += 1
            continue
        begin = i
        while i < len(source) and ("A" <= source[i] <= "Z" or "a" <= source[i] <= "z"):
            i += 1
        yield source[begin:i], start, i


def marker_arguments(source: str, name: str) -> list[str]:
    result = []
    for command, start, end in control_words(source):
        if command == name:
            match = re.match(r"\s*\{([^{}]*)\}", source[end:])
            if match:
                result.append(match[1])
    return result


def check_tex(path: Path, report: Report, unknown: dict[str, set[str]]) -> str:
    source = path.read_text(encoding="utf-8")
    clean = strip_comments(source)
    for error in brace_errors(source):
        report.error(f"{path.name}: {error}")
    tokens = list(control_words(clean))
    commands = {token[0] for token in tokens}
    for command in sorted(commands & FORBIDDEN):
        report.error(f"{path.name}: prohibited fragment command \\{command}")
    for command in commands - EDITORIAL - STANDARD - FORBIDDEN:
        unknown.setdefault(command, set()).add(path.name)
    for command, start, end in tokens:
        if command in EDITORIAL and not re.match(r"\s*\{", clean[end:]):
            report.error(f"{path.name}: \\{command} must have a braced argument")
    if "document" in marker_arguments(clean, "begin") + marker_arguments(clean, "end"):
        report.error(f"{path.name}: document environment is forbidden in a fragment")
    for argument in marker_arguments(clean, "illegible"):
        if not re.fullmatch(r"[1-9]\d*", argument.strip()):
            report.error(f"{path.name}: illegible argument is not a positive word count: {argument!r}")
    return clean


def normalize_lines(source: str) -> str:
    return "\n".join(line.rstrip() for line in source.replace("\r\n", "\n").splitlines()).strip()


def check_inventory(path: Path, present: set[int], partial: bool, report: Report):
    if not path.exists():
        (report.warn if partial else report.error)(f"Missing {path.name}")
        return
    covered, records = set(), set()
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDS:
            report.error(f"{path.name}: expected exact fields {FIELDS!r}, got {reader.fieldnames!r}")
            return
        for rownum, row in enumerate(reader, 2):
            prefix = f"{path.name}, CSV row {rownum}"
            if None in row or any(v is None for v in row.values()):
                report.error(f"{prefix}: malformed CSV record")
                continue
            try:
                scan = int(row["scan"])
            except ValueError:
                report.error(f"{prefix}: scan is not an integer")
                continue
            covered.add(scan)
            if row["cote"] != COTE or scan not in SCANS:
                report.error(f"{prefix}: wrong cote or out-of-range scan")
            if row["sheet_kind"] not in SHEET_KINDS:
                report.error(f"{prefix}: invalid sheet_kind {row['sheet_kind']!r}")
            if row["kind"] not in KINDS:
                report.error(f"{prefix}: invalid kind {row['kind']!r}")
            if row["transcribed"] != "yes":
                report.error(f"{prefix}: transcribed is not exactly 'yes'")
            for field in ("element", "position", "first_words_or_objects"):
                if not row[field].strip():
                    report.error(f"{prefix}: empty {field}")
            key = tuple(row[field] for field in FIELDS)
            if key in records:
                report.warn(f"{prefix}: exact duplicate inventory record; review")
            records.add(key)
    missing = (present if partial else SCANS) - covered
    if missing:
        report.error(f"{path.name}: missing inventory for scans {sorted(missing)}")
    if covered - present:
        report.error(f"{path.name}: inventory refers to absent page files {sorted(covered - present)}")


def check_hashes(root: Path, manifest: Path, report: Report):
    count = 0
    for number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+?)\s*", line)
        if not match:
            report.error(f"{manifest.name}:{number}: expected 'SHA256  relative/path'")
            continue
        digest, filename = match.groups()
        path = Path(filename)
        if not path.is_absolute():
            path = root / path
        if not path.is_file():
            report.error(f"{manifest.name}:{number}: hash target does not exist: {filename}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != digest.lower():
            report.error(f"Frozen hash changed: {filename}")
        count += 1
    if not count:
        report.error(f"{manifest.name}: no hash entries")
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--partial", action="store_true", help="Permit unfinished scans and missing final files")
    parser.add_argument("--manifest", type=Path, help="SHA-256 manifest; paths inside are relative to root")
    args = parser.parse_args()
    root, report, unknown = args.root.resolve(), Report(), {}
    pages = root / "pages"
    found = {}
    if pages.is_dir():
        for path in sorted(pages.glob("*.tex")):
            match = re.fullmatch(re.escape(PACKAGE) + r"_33_scan(\d{3})\.tex", path.name)
            if not match or int(match[1]) not in SCANS:
                report.error(f"Unexpected page filename: {path.name}")
                continue
            scan = int(match[1])
            found[scan] = path
            source = check_tex(path, report, unknown)
            markers = marker_arguments(source, "scanpage")
            if markers != [str(scan)]:
                report.error(f"{path.name}: expected only scanpage{{{scan}}}; found {markers!r}")
            cotes = marker_arguments(source, "cotefile")
            if cotes not in ([], [COTE]):
                report.error(f"{path.name}: invalid cote markers {cotes!r}")
    else:
        (report.warn if args.partial else report.error)("Missing pages directory")
    missing = SCANS - set(found)
    if missing:
        (report.warn if args.partial else report.error)(f"Missing page files: {sorted(missing)}")
    combined = root / f"{PACKAGE}_transcription.tex"
    if combined.exists():
        source = check_tex(combined, report, unknown)
        if not re.match(r"\s*\\cotefile\s*\{33\}\s*\\scanpage\s*\{2\}", source):
            report.error(f"{combined.name}: must begin with cotefile{{33}} then scanpage{{2}}")
        markers = marker_arguments(source, "scanpage")
        expected = [str(n) for n in sorted(found if args.partial else SCANS)]
        if markers != expected:
            report.error(f"{combined.name}: scan markers are not the expected ordered sequence")
        if marker_arguments(source, "cotefile") != [COTE]:
            report.error(f"{combined.name}: expected exactly one cotefile{{33}} marker")
        if found:
            joined = "\n".join(found[n].read_text(encoding="utf-8") for n in sorted(found))
            if not re.match(r"\s*\\cotefile\s*\{33\}", strip_comments(joined)):
                joined = "\\cotefile{33}\n" + joined
            if normalize_lines(combined.read_text(encoding="utf-8")) != normalize_lines(joined):
                report.warn("Combined text differs from exact concatenation of pages (including comments/blank lines); review this difference")
    elif not args.partial:
        report.error(f"Missing {combined.name}")
    check_inventory(root / f"{PACKAGE}_inventory.csv", set(found), args.partial, report)
    if not args.partial:
        for name in (f"{PACKAGE}_doubts.md", f"{PACKAGE}_notes.md", "progress.log"):
            path = root / name
            if not path.is_file() or not path.stat().st_size:
                report.error(f"Missing or empty {name}")
    manifests = [args.manifest] if args.manifest else [
        root / "records/frozen_hashes.sha256", root / "frozen_hashes.sha256",
        root / "SHA256SUMS"]
    hashes = 0
    for manifest in manifests:
        if not manifest.is_absolute():
            manifest = root / manifest
        if manifest.exists():
            hashes += check_hashes(root, manifest, report)
        elif args.manifest:
            report.error(f"Missing requested hash manifest: {manifest}")
    for command, locations in sorted(unknown.items()):
        sample = ", ".join(sorted(locations)[:3])
        report.warn(f"Unclassified LaTeX command \\{command}: {sample}; verify it is standard LaTeX/TikZ")
    for warning in report.warnings:
        print(f"WARNING: {warning}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print(f"Checked {len(found)}/48 page files; {hashes} frozen hashes; "
          f"{len(report.errors)} errors; {len(report.warnings)} warnings.")
    print("Structural validation does not certify visual transcription accuracy or completeness.")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
