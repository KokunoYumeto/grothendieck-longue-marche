#!/usr/bin/env python3
"""Mechanical checks only; this program performs no OCR or visual assessment.

Default mode checks the material currently present. --final requires the full
package and workflow records. Unknown TeX commands are warnings, because this is
a conservative command inventory rather than a TeX parser; --strict-macros makes
them errors. The script never reads any images, ZIPs, or contextual material.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path


PACKAGE = "MPL_136_282-327"
COTE = "136"
SCANS = tuple(n for n in range(282, 328) if n != 319)
COLUMNS = (
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
PAGE_MACROS = {
    "cotefile", "scanpage", "mspage", "deleted", "inserted", "margin", "uline",
    "uuline", "diagram", "figure", "unsure", "illegible",
}
# Familiar LaTeX/AMS/TikZ commands. This list is deliberately conservative and
# extensible. A warning does not establish that an unfamiliar command is invalid.
STANDARD = set("""
begin end label ref eqref pageref tag notag nonumber intertext shortintertext
text textrm textit textbf textsf texttt textsc textnormal emph underline overline
mbox hbox vbox par newline linebreak nolinebreak smallskip medskip bigskip
quad qquad hspace hspace* vspace vspace* kern mkern hfill vfill strut mathstrut
phantom hphantom vphantom smash raisebox rule ensuremath relax protect noindent
indent centering raggedright raggedleft footnote footnotemark footnotetext
tiny scriptsize footnotesize small normalsize large Large LARGE huge Huge
displaystyle textstyle scriptstyle scriptscriptstyle mathrm mathit mathbf mathsf
mathtt mathcal mathscr mathbb mathfrak mathnormal boldsymbol bm operatorname
mathop mathbin mathrel boxed boxtimes flat varinjlim varprojlim
DeclareMathOperator limits nolimits substack underset overset stackrel atop
frac dfrac tfrac cfrac binom dbinom tbinom genfrac sqrt left right middle
big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
hat widehat bar vec tilde widetilde dot ddot dddot ddddot acute grave breve
check mathring overbrace underbrace overrightarrow overleftarrow
overleftrightarrow underrightarrow underleftarrow cancel bcancel xcancel
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon
phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
aleph beth gimel daleth ell hbar imath jmath wp Re Im partial nabla infty
forall exists nexists neg lnot emptyset varnothing bot top angle measuredangle
triangle square Box Diamond diamond lozenge blacksquare blacktriangle
prime backprime dots ldots cdots vdots ddots dotsb dotsc dotsi dotsm dotso
cdot times div ast star circ bullet oplus ominus otimes oslash odot bigcirc
dagger ddagger amalg wreath wr cap cup uplus sqcap sqcup wedge vee land lor
bigcap bigcup bigsqcup bigvee bigwedge bigoplus bigotimes bigodot sum prod coprod
int iint iiint iiiint idotsint oint smallint
pm mp setminus smallsetminus backslash triangleleft triangleright
le leq ge geq neq ne equiv sim simeq approx approxeq cong asymp doteq
ll gg lesssim gtrsim lessapprox gtrapprox lneq gneq lneqq gneqq nleq ngeq
prec succ preceq succeq preccurlyeq succcurlyeq nprec nsucc
in ni notin owns subset supset subseteq supseteq subsetneq supsetneq
nsubseteq nsupseteq sqsubset sqsupset sqsubseteq sqsupseteq
mid nmid parallel nparallel perp propto models vdash dashv Vdash Vvdash
triangleq coloneqq eqqcolon colon not
rightarrow leftarrow leftrightarrow Rightarrow Leftarrow Leftrightarrow
longrightarrow longleftarrow longleftrightarrow Longrightarrow Longleftarrow
Longleftrightarrow mapsto longmapsto hookrightarrow hookleftarrow
twoheadrightarrow twoheadleftarrow rightarrowtail leftarrowtail
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow
nearrow searrow swarrow nwarrow rightsquigarrow leftrightsquigarrow
leadsto dashrightarrow dashleftarrow looparrowright looparrowleft
curvearrowright curvearrowleft circlearrowright circlearrowleft
rightleftarrows leftrightarrows rightrightarrows leftleftarrows
rightrightharpoons leftrightharpoons rightleftharpoons
rightharpoonup rightharpoondown leftharpoonup leftharpoondown
xrightarrow xleftarrow xRightarrow xLeftarrow xleftrightarrow
to gets iff implies impliedby
langle rangle lbrace rbrace lvert rvert lVert rVert vert Vert
lfloor rfloor lceil rceil lgroup rgroup lmoustache rmoustache
sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh coth
exp log ln lg lim liminf limsup inf sup max min det dim gcd hom ker Pr arg deg
bmod pmod mod pod
hline cline vline multicolumn multirow cr noalign omit span tabularnewline
item enumerate itemize description enditem endenumerate enditemize
tikz draw path node fill filldraw coordinate clip scope endscope
arrow ar foreach pgfmathsetmacro pgfmathtruncatemacro
matrix useasboundingbox pgftransformshift pgfpoint pgfsetarrowsend
pgfsetarrowsstart pgfsetlinewidth pgfpathmoveto pgfpathlineto pgfusepath
color textcolor fcolorbox colorbox
rotatebox textcircled u c
ae AE oe OE aa AA o O l L ss i j S P dag ddag pounds copyright LaTeX TeX
ldq rdq glqq grqq guillemotleft guillemotright textquotedblleft
textquotedblright textquoteleft textquoteright textendash textemdash
textasciicircum textasciitilde textbackslash textsuperscript textsubscript
""".split())
FORBIDDEN = {
    "documentclass", "usepackage", "includegraphics", "includepdf", "input",
    "include", "newcommand", "renewcommand", "providecommand", "def", "gdef",
    "edef", "xdef", "write", "openout", "read", "directlua",
}


class Checks:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def need(self, condition: bool, message: str) -> None:
        if not condition:
            self.error(message)


def without_comments(source: str) -> str:
    """Remove TeX comments, respecting whether a percent is backslash escaped."""
    lines = []
    for line in source.splitlines(keepends=True):
        for pos, char in enumerate(line):
            if char != "%":
                continue
            preceding = 0
            k = pos - 1
            while k >= 0 and line[k] == "\\":
                preceding += 1
                k -= 1
            if preceding % 2 == 0:
                line = line[:pos] + ("\n" if line.endswith("\n") else "")
                break
        lines.append(line)
    return "".join(lines)


def check_tex(path: Path, checks: Checks, strict: bool) -> str:
    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        checks.error(f"{path.name}: cannot read UTF-8: {exc}")
        return ""
    text = without_comments(raw)
    stack: list[int] = []
    line = 1
    pos = 0
    while pos < len(text):
        char = text[pos]
        if char == "\n":
            line += 1
        if char == "\\":
            # Escaped braces and escaped backslashes are literal control symbols.
            match = re.match(r"\\(?:[A-Za-z@]+|[^\n])", text[pos:])
            if match:
                pos += len(match.group())
                continue
        if char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                checks.error(f"{path.name}:{line}: unmatched closing brace")
        pos += 1
    for opening in stack:
        checks.error(f"{path.name}:{opening}: unmatched opening brace")

    environments: list[tuple[str, int]] = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", text):
        line_no = text.count("\n", 0, match.start()) + 1
        action, name = match.groups()
        if name == "document":
            checks.error(f"{path.name}:{line_no}: document environment in fragment")
        if action == "begin":
            environments.append((name, line_no))
        elif not environments:
            checks.error(f"{path.name}:{line_no}: end of unopened environment {name}")
        else:
            previous, opened = environments.pop()
            checks.need(previous == name,
                        f"{path.name}:{line_no}: closes {name}, but {previous} opened at {opened}")
    for name, opened in environments:
        checks.error(f"{path.name}:{opened}: unclosed environment {name}")

    # TikZ's foreach command binds local control-sequence variables; these are
    # not user-defined editorial macros. Recognize the explicit declaration
    # rather than globally allowing arbitrary commands such as \\x or \\y.
    loop_variables: set[str] = set()
    for declaration in re.finditer(
        r"\\foreach\s+((?:\\[A-Za-z]+)(?:\s*/\s*\\[A-Za-z]+)*)\s+in\b",
        text,
    ):
        loop_variables.update(re.findall(r"\\([A-Za-z]+)", declaration.group(1)))
    commands = Counter(re.findall(r"\\([A-Za-z@]+)", text))
    for command in sorted(commands):
        if command in FORBIDDEN:
            checks.error(f"{path.name}: forbidden fragment command \\{command}")
        elif command not in PAGE_MACROS | STANDARD | loop_variables:
            message = (f"{path.name}: unrecognized command \\{command} "
                       f"({commands[command]} occurrence(s)); review manually")
            (checks.error if strict else checks.warn)(message)
    return text


def check_inventory(root: Path, present: set[int], final: bool, checks: Checks) -> None:
    path = root / f"{PACKAGE}_inventory.csv"
    if not path.exists():
        (checks.error if final or present else checks.warn)("Inventory is missing")
        return
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            checks.need(tuple(reader.fieldnames or ()) == COLUMNS,
                        "Inventory columns do not exactly match the requested schema/order")
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        checks.error(f"Inventory could not be read: {exc}")
        return
    counts: Counter[int] = Counter()
    identifiers: set[tuple[int, str]] = set()
    for number, row in enumerate(rows, 2):
        prefix = f"Inventory row {number}"
        if None in row or any(row.get(column) is None for column in COLUMNS):
            checks.error(f"{prefix}: ragged CSV row")
            continue
        checks.need(row["cote"].strip() == COTE, f"{prefix}: cote is not {COTE}")
        try:
            scan = int(row["scan"].strip())
        except ValueError:
            checks.error(f"{prefix}: scan is not an integer")
            continue
        checks.need(scan in SCANS, f"{prefix}: unexpected scan {scan}")
        checks.need(scan in present, f"{prefix}: no corresponding page file for {scan}")
        counts[scan] += 1
        checks.need(row["sheet_kind"].strip() in SHEET_KINDS,
                    f"{prefix}: invalid sheet_kind {row['sheet_kind']!r}")
        checks.need(row["kind"].strip() in KINDS,
                    f"{prefix}: invalid element kind {row['kind']!r}")
        checks.need(row["transcribed"].strip() == "yes",
                    f"{prefix}: transcribed must equal yes")
        for column in ("element", "position", "first_words_or_objects"):
            checks.need(bool(row[column].strip()), f"{prefix}: empty {column}")
        identifier = (scan, row["element"].strip())
        checks.need(identifier not in identifiers,
                    f"{prefix}: duplicate element identifier for scan {scan}")
        identifiers.add(identifier)
    for scan in sorted(set(SCANS) if final else present):
        checks.need(counts[scan] > 0, f"Inventory has no rows for scan {scan}")


def check_log(root: Path, final: bool, checks: Checks) -> None:
    path = root / "progress.log"
    if not path.exists():
        (checks.error if final else checks.warn)("progress.log is missing")
        return
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    timestamp = r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?: UTC|Z|\+00:00)"
    checks.need(bool(lines and re.fullmatch(timestamp, lines[0].strip())),
                "progress.log must begin with a UTC timestamp on its first line")
    if not final:
        return
    done_positions = {}
    audit_positions = {}
    for scan in SCANS:
        done = re.search(rf"(?m)^136 scan 0*{scan} done ({timestamp})\s*$", content)
        audit = re.search(rf"(?m)^scan 0*{scan} audited ({timestamp})\s*$", content)
        checks.need(done is not None, f"Missing done record for scan {scan}")
        checks.need(audit is not None, f"Missing audit record for scan {scan}")
        if done:
            done_positions[scan] = done.start()
        if audit:
            audit_positions[scan] = audit.start()
    checks.need(list(done_positions.values()) == sorted(done_positions.values()),
                "Done records are not in ascending scan order")
    if len(done_positions) == len(SCANS) and audit_positions:
        checks.need(min(audit_positions.values()) > max(done_positions.values()),
                    "At least one final audit record precedes completion of all pages")
    freeze = re.search(rf"(?m)^transcription frozen ({timestamp})\s*$", content)
    checks.need(freeze is not None, "Missing transcription frozen UTC record")
    context = re.search(rf"(?m)^context opened ({timestamp})\s*$", content)
    checks.need(context is not None, "Missing context opened UTC record")
    if freeze:
        checks.need(all(pos < freeze.start() for pos in audit_positions.values()),
                    "An audit record occurs after transcription freeze")
        if context:
            checks.need(context.start() > freeze.start(), "Context opened before freeze record")
        # Names and hash values must both be recorded in the log; their formatting
        # need not follow one exact sha256sum command convention.
        for name in [*(f"{PACKAGE}_136_scan{scan}.tex" for scan in SCANS),
                     f"{PACKAGE}_transcription.tex"]:
            hash_line = next((line for line in lines
                              if name in line and re.search(r"\b[a-fA-F0-9]{64}\b", line)), None)
            checks.need(hash_line is not None, f"No SHA-256 log record for {name}")
    checks.need(bool(re.search(r"(?im)^.*(?:hash(?:es)?|sha-?256).*(?:unchanged|verified|match).*$", content)),
                "No final hash-verification statement found in progress.log")


def check_manifest(root: Path, final: bool, checks: Checks) -> None:
    path = root / "frozen_hashes.sha256"
    if not path.exists():
        # The prompt requires hashes in the log; a separate manifest is optional.
        checks.warn("No frozen_hashes.sha256 manifest; byte verification was not run")
        return
    expected = {f"pages/{PACKAGE}_136_scan{scan}.tex" for scan in SCANS}
    expected.add(f"{PACKAGE}_transcription.tex")
    seen: set[str] = set()
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([a-fA-F0-9]{64})[ \t]+\*?(.+)", line)
        if not match:
            checks.error(f"Manifest line {number}: expected SHA-256 and relative file path")
            continue
        digest, name = match.groups()
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts:
            checks.error(f"Manifest line {number}: path must stay inside package")
            continue
        canonical = relative.as_posix()
        checks.need(canonical not in seen, f"Duplicate manifest entry: {canonical}")
        seen.add(canonical)
        target = root / relative
        if not target.is_file():
            checks.error(f"Manifest target missing: {canonical}")
            continue
        # Restrict verification to declared text deliverables. Never read attached
        # images or contextual archives, even if a malformed manifest names them.
        if canonical not in expected:
            checks.error(f"Manifest entry outside allowed transcription files: {canonical}")
            continue
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        checks.need(actual == digest.lower(), f"SHA-256 changed: {canonical}")
    if final:
        for name in sorted(expected - seen):
            checks.error(f"Manifest is missing {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path,
                        default=Path(__file__).resolve().parent.parent,
                        help="package directory (default: parent of scripts/)")
    parser.add_argument("--final", action="store_true",
                        help="require all 45 pages and complete final workflow records")
    parser.add_argument("--strict-macros", action="store_true",
                        help="treat commands outside conservative allowlist as errors")
    args = parser.parse_args()
    root = args.root.resolve()
    checks = Checks()
    present: set[int] = set()
    for path in sorted((root / "pages").glob("*.tex")):
        match = re.fullmatch(rf"{PACKAGE}_136_scan(\d+)\.tex", path.name)
        if not match:
            checks.error(f"Unexpected page filename: {path.name}")
            continue
        scan = int(match.group(1))
        checks.need(scan in SCANS, f"Unexpected page scan {scan}")
        checks.need(scan not in present, f"Duplicate page scan {scan}")
        present.add(scan)
        source = check_tex(path, checks, args.strict_macros)
        markers = re.findall(r"\\scanpage\s*\{(\d+)\}", source)
        checks.need(markers == [str(scan)], f"{path.name}: scan marker missing, wrong, or repeated")
        cotefiles = re.findall(r"\\cotefile\s*\{([^{}]+)\}", source)
        checks.need(all(cote == COTE for cote in cotefiles), f"{path.name}: wrong cotefile")
        checks.need(len(cotefiles) <= 1, f"{path.name}: repeated cotefile marker")
        checks.need(bool(re.match(r"\s*(?:\\cotefile\s*\{136\}\s*)?\\scanpage\s*\{" + str(scan) + r"\}", source)),
                    f"{path.name}: page does not begin with scan marker")
    missing = sorted(set(SCANS) - present)
    if missing:
        message = "Missing page scans: " + ", ".join(map(str, missing))
        (checks.error if args.final else checks.warn)(message)
    combined = root / f"{PACKAGE}_transcription.tex"
    if combined.exists():
        source = check_tex(combined, checks, args.strict_macros)
        markers = [int(n) for n in re.findall(r"\\scanpage\s*\{(\d+)\}", source)]
        desired = list(SCANS) if args.final else sorted(present)
        checks.need(markers == desired, "Combined transcription scan markers differ from ordered page files")
        checks.need(bool(re.match(r"\s*\\cotefile\s*\{136\}\s*\\scanpage\s*\{282\}", source)),
                    "Combined fragment must begin with cotefile 136 and scanpage 282")
        checks.need(re.findall(r"\\cotefile\s*\{([^{}]+)\}", source) == [COTE],
                    "Combined fragment must contain exactly one cotefile marker")
    elif args.final:
        checks.error("Combined transcription fragment is missing")
    check_inventory(root, present, args.final, checks)
    check_log(root, args.final, checks)
    check_manifest(root, args.final, checks)
    if args.final:
        for suffix in ("doubts.md", "notes.md"):
            path = root / f"{PACKAGE}_{suffix}"
            checks.need(path.is_file() and path.stat().st_size > 0, f"Missing or empty {path.name}")
    print(f"Checked {len(present)}/{len(SCANS)} page files ({'final' if args.final else 'in-progress'} mode).")
    for message in checks.errors:
        print(f"ERROR: {message}")
    for message in checks.warnings:
        print(f"WARNING: {message}")
    print(f"Result: {len(checks.errors)} error(s), {len(checks.warnings)} warning(s).")
    print("Mechanical validation cannot establish visual completeness, reading accuracy, or fidelity of diagrams.")
    return 1 if checks.errors else 0


if __name__ == "__main__":
    sys.exit(main())
