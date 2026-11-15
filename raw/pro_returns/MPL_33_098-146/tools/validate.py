#!/usr/bin/env python3
"""Read-only structural checks for the MPL_33_098-146 delivery.

This does not read images, use OCR, interpret the manuscript, or certify
paleographic accuracy/completeness. Run only when the transcriber requests it.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path


PREFIX = "MPL_33_098-146"
EXPECTED_SCANS = set(range(98, 147))
HEADERS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
DIPLOMATIC = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())

# A deliberately broad vocabulary of standard LaTeX/AMS/math-alphabet/TikZ
# commands. Unknown commands are reported for human review, not automatically
# rejected: a finite vocabulary cannot establish which commands all packages
# and local rendering setups supply.
STANDARD = set("""
begin end label ref eqref tag notag nonumber par noindent indent newline
linebreak pagebreak newpage clearpage hfill vfill quad qquad enspace thinspace
medspace thickspace negthinspace negmedspace negthickspace hspace vspace kern
mkern mspace phantom hphantom vphantom smash llap rlap mathllap mathrlap
text textrm textsf texttt textbf textit textsl textsc textnormal textcircled emph mb mbox boxed
rm sf tt bf it sl sc cal frak mathrm mathsf mathtt mathbf mathit mathcal
mathscr mathfrak mathbb mathnormal boldsymbol pmb bm operatorname mathop
mathbin mathrel mathord mathpunct mathopen mathclose limits nolimits
displaylimits displaystyle textstyle scriptstyle scriptscriptstyle
displaystyle dfrac tfrac frac cfrac binom dbinom tbinom sqrt root of
over atop choose brack brace genfrac left right middle big Big bigg Bigg
bigl bigr Bigl Bigr biggl biggr Biggl Biggr bigm Bigm biggm Biggm
overline underline widehat widetilde hat tilde bar vec dot ddot dddot
ddddot acute grave breve check mathring overbrace underbrace overset
underset stackrel overrightarrow overleftarrow underrightarrow
underleftarrow overleftrightarrow underleftrightarrow
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota
kappa varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma
tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi
Sigma Upsilon Phi Psi Omega digamma varGamma varDelta varTheta varLambda
varXi varPi varSigma varUpsilon varPhi varPsi varOmega
aleph beth gimel daleth hbar ell imath jmath wp Re Im partial nabla
infty emptyset varnothing forall exists nexists neg lnot top bot
land lor wedge vee bigwedge bigvee cap cup bigcap bigcup sqcap sqcup
bigsqcup setminus smallsetminus complement in ni notin owns notni
subset supset subseteq supseteq subsetneq supsetneq subsetneqq supsetneqq
sqsubset sqsupset sqsubseteq sqsupseteq nsubseteq nsupseteq
le ge leq geq leqq geqq leqslant geqslant neq ne neqq ll gg lll ggg
lesssim gtrsim lessapprox gtrapprox lessgtr gtrless nleq ngeq nless ngtr
prec succ preceq succeq preccurlyeq succcurlyeq sim simeq cong approx
approxeq asymp equiv doteq doteqdot triangleq propto not
to gets mapsto longmapsto hookrightarrow hookleftarrow
rightarrow leftarrow leftrightarrow longrightarrow longleftarrow
longleftrightarrow Rightarrow Leftarrow Leftrightarrow Longrightarrow
Longleftarrow Longleftrightarrow uparrow downarrow updownarrow Uparrow
Downarrow Updownarrow nearrow searrow swarrow nwarrow
twoheadrightarrow twoheadleftarrow rightarrowtail leftarrowtail
rightsquigarrow leftrightsquigarrow dashrightarrow dashleftarrow
leftharpoonup leftharpoondown rightharpoonup rightharpoondown
rightleftarrows leftrightarrows rightleftharpoons leftrightharpoons
rightrightarrows leftleftarrows upuparrows downdownarrows
circlearrowleft circlearrowright curvearrowleft curvearrowright
looparrowleft looparrowright xrightarrow xleftarrow xleftrightarrow
xRightarrow xLeftarrow xLeftrightarrow xmapsto xhookrightarrow xhookleftarrow
restriction multimap leadsto implies impliedby iff
cdot cdots dots ldots vdots ddots dotsc dotsb dotsm dotsi dotso
times div pm mp ast star circ bullet oplus ominus otimes oslash odot
bigoplus bigotimes bigodot amalg uplus biguplus wr diamond triangle
triangleleft triangleright lhd rhd unlhd unrhd bigtriangleup bigtriangledown
prod coproduct coprod sum int iint iiint iiiint oint smallint
lim limsup liminf varlimsup varliminf injlim projlim varinjlim varprojlim
sup inf max min arg deg dim det gcd hom Hom ker coker im id sin cos tan
cot sec csc sinh cosh tanh coth log ln lg exp Pr mod bmod pmod pod
mid nmid parallel nparallel perp vdash dashv models Vdash Vvdash
vdash nvdash nVdash nvDash nVDash vDash
langle rangle lbrace rbrace lbrack rbrack lceil rceil lfloor rfloor
lvert rvert lVert rVert vert Vert backslash slash
angle measuredangle sphericalangle square Box boxdot boxtimes boxplus
boxminus blacksquare blacktriangle blacktriangledown lozenge blacklozenge
checkmark dagger ddagger dag ddag prime backprime flat natural sharp
S P copyright pounds euro mathsterling textendash textemdash endash emdash
textquotedblleft textquotedblright textquoteleft textquoteright
textbackslash textasciicircum textasciitilde textunderscore
textless textgreater textbar textbraceleft textbraceright
ae AE oe OE aa AA o O l L ss i j c v H r u b d k t
LaTeX TeX protect relax ensuremath
multicolumn multirow hline cline hdashline vline cr
shortstack substack subarray arraystretch
footnote footnotemark footnotetext
ar arrow arrows tikz tikzset tikzstyle path draw fill filldraw
node coordinate matrix scope foreach clip shade shadedraw
pgfmathsetmacro pgfmathtruncatemacro pgfmathparse pgfmathresult
pgfsetlayers pgfdeclarelayer pgfpoint pgfpointxy pgfpointpolar
pgfpathmoveto pgfpathlineto pgfpathcurveto pgfpathclose pgfusepath
pgfsetlinewidth pgfsetstrokecolor pgfsetfillcolor pgftransformshift
pgftransformrotate pgftransformscale pgftext
scriptsize tiny small normalsize large Large LARGE huge Huge
color textcolor colorbox fcolorbox rotatebox scalebox resizebox
makebox framebox rule raisebox unitlength put multiput linethickness
qbezier oval circle vector line
""".split())

FORBIDDEN_COMMANDS = {
    "documentclass", "usepackage", "RequirePackage", "includegraphics",
    "input", "include", "newcommand", "renewcommand", "providecommand",
    "DeclareRobustCommand", "DeclareMathOperator", "def", "gdef", "edef",
    "xdef", "newenvironment", "renewenvironment", "newtheorem",
}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.facts: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def fact(self, message: str) -> None:
        self.facts.append(message)

    def print(self) -> None:
        for message in self.facts:
            print("INFO: " + message)
        for message in self.warnings:
            print("WARNING: " + message)
        for message in self.errors:
            print("ERROR: " + message)
        print(f"Structural result: {len(self.errors)} error(s), {len(self.warnings)} warning(s).")
        print("These checks do not certify paleographic accuracy or completeness.")


def without_comments(text: str) -> str:
    """Remove unescaped %-comments while retaining newlines and character offsets."""
    out = list(text)
    i = 0
    while i < len(text):
        if text[i] == "\\":
            # A control symbol consumes both characters. A control word also
            # moves past its first letter; later letters are harmless here.
            i += 2
        elif text[i] == "%":
            while i < len(text) and text[i] != "\n":
                out[i] = " "
                i += 1
        else:
            i += 1
    return "".join(out)


def line_at(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def check_tex(path: Path, text: str, report: Report) -> str:
    clean = without_comments(text)
    stack: list[int] = []
    i = 0
    while i < len(clean):
        ch = clean[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "{":
            stack.append(i)
        elif ch == "}":
            if stack:
                stack.pop()
            else:
                report.error(f"{path.name}:{line_at(clean, i)}: unmatched closing brace")
        i += 1
    for offset in stack:
        report.error(f"{path.name}:{line_at(clean, offset)}: unclosed opening brace")

    # Match TeX control sequences; skip control symbols such as \\, \%, and \{.
    commands = [(m.group(1), m.start()) for m in re.finditer(r"\\([A-Za-z@]+|[^\n])", clean)
                if re.fullmatch(r"[A-Za-z@]+", m.group(1))]
    unknown: dict[str, int] = {}
    for command, offset in commands:
        if command in FORBIDDEN_COMMANDS:
            report.error(f"{path.name}:{line_at(clean, offset)}: forbidden fragment command \\{command}")
        elif command not in DIPLOMATIC and command not in STANDARD:
            unknown.setdefault(command, line_at(clean, offset))
    for command, line in sorted(unknown.items()):
        report.warn(f"{path.name}:{line}: review unrecognized command \\{command} against standard LaTeX/TikZ")

    env_stack: list[tuple[str, int]] = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
        action, env = match.groups()
        if env == "document":
            report.error(f"{path.name}:{line_at(clean, match.start())}: document environment in fragment")
        if action == "begin":
            env_stack.append((env, match.start()))
        elif not env_stack:
            report.error(f"{path.name}:{line_at(clean, match.start())}: unmatched end of {env}")
        elif env_stack[-1][0] != env:
            report.error(f"{path.name}:{line_at(clean, match.start())}: ends {env}, but {env_stack[-1][0]} is open")
            env_stack.pop()
        else:
            env_stack.pop()
    for env, offset in env_stack:
        report.error(f"{path.name}:{line_at(clean, offset)}: unclosed {env} environment")
    return clean


def scan_markers(clean: str) -> list[int]:
    return [int(value) for value in re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)]


def read_utf8(path: Path, report: Report) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.error(f"Cannot read {path.name}: {exc}")
        return None


def check_pages(base: Path, partial: bool, report: Report) -> dict[int, str]:
    pages_dir = base / "pages"
    texts: dict[int, str] = {}
    if not pages_dir.is_dir():
        report.error("Missing pages/ directory")
        return texts
    for path in sorted(pages_dir.glob("*.tex")):
        match = re.fullmatch(r"MPL_33_098-146_33_scan(\d{3})\.tex", path.name)
        if not match:
            report.error(f"Unexpected page filename: {path.name}")
            continue
        scan = int(match.group(1))
        if scan not in EXPECTED_SCANS:
            report.error(f"Unexpected scan in page filename: {path.name}")
            continue
        text = read_utf8(path, report)
        if text is None:
            continue
        if not text.strip():
            report.error(f"Empty page file: {path.name}")
        texts[scan] = text
        clean = check_tex(path, text, report)
        if scan_markers(clean) != [scan]:
            report.error(f"{path.name}: expected exactly one \\scanpage{{{scan}}} marker")
        for cote in re.findall(r"\\cotefile\s*\{([^{}]+)\}", clean):
            if cote.strip() != "33":
                report.error(f"{path.name}: unexpected cote {cote!r}")

    present = set(texts)
    missing = sorted(EXPECTED_SCANS - present)
    report.fact(f"Page files present: {len(present)}/49")
    if missing and not partial:
        report.error("Missing page files for scans: " + ", ".join(f"{s:03}" for s in missing))
    if present and present != set(range(98, max(present) + 1)):
        report.error("Page files do not form a contiguous sequence starting at scan 098")
    if not present and not partial:
        report.error("No page files found")
    return texts


def check_combined(base: Path, texts: dict[int, str], partial: bool, report: Report) -> None:
    path = base / f"{PREFIX}_transcription.tex"
    if not path.exists():
        if not partial:
            report.error("Missing combined transcription")
        return
    text = read_utf8(path, report)
    if text is None:
        return
    clean = check_tex(path, text, report)
    expected = sorted(texts) if partial else sorted(EXPECTED_SCANS)
    if scan_markers(clean) != expected:
        report.error("Combined transcription scan markers do not match the required ordered page sequence")
    if not re.match(r"\s*\\cotefile\s*\{33\}\s*\\scanpage\s*\{98\}", clean):
        report.error("Combined transcription must begin with \\cotefile{33} and \\scanpage{98}")

    # Check exact page text, allowing only whitespace between whole page files.
    # No mathematical or linguistic normalization is performed.
    cursor = 0
    for scan in sorted(texts):
        page = texts[scan].strip()
        start = cursor
        while start < len(text) and text[start].isspace():
            start += 1
        if not text.startswith(page, start):
            report.error(f"Combined transcription differs from page file at scan {scan:03}")
            return
        cursor = start + len(page)
    if text[cursor:].strip():
        report.error("Combined transcription contains non-whitespace after the concatenated page files")


def check_inventory(base: Path, present: set[int], partial: bool, report: Report) -> None:
    path = base / f"{PREFIX}_inventory.csv"
    if not path.exists():
        if not partial or present:
            report.error("Missing inventory CSV")
        return
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != HEADERS:
                report.error(f"Inventory headers must be exactly: {','.join(HEADERS)}")
                return
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        report.error(f"Cannot parse inventory CSV: {exc}")
        return
    scans: set[int] = set()
    element_ids: set[tuple[int, str]] = set()
    sheet_kinds: dict[int, set[str]] = {}
    for number, row in enumerate(rows, 2):
        loc = f"Inventory row {number}"
        if None in row or any(v is None for v in row.values()):
            report.error(f"{loc}: column count does not match header")
            continue
        if row["cote"].strip() != "33":
            report.error(f"{loc}: cote must be 33")
        try:
            scan = int(row["scan"])
        except ValueError:
            report.error(f"{loc}: invalid scan number")
            continue
        scans.add(scan)
        if scan not in EXPECTED_SCANS:
            report.error(f"{loc}: scan outside 098–146")
        if row["sheet_kind"] not in SHEET_KINDS:
            report.error(f"{loc}: invalid sheet_kind {row['sheet_kind']!r}")
        sheet_kinds.setdefault(scan, set()).add(row["sheet_kind"])
        if row["kind"] not in KINDS:
            report.error(f"{loc}: invalid element kind {row['kind']!r}")
        if row["transcribed"] != "yes":
            report.error(f"{loc}: transcribed must be exactly yes")
        for field in ("element", "position", "first_words_or_objects"):
            if not row[field].strip():
                report.error(f"{loc}: empty {field}")
        key = (scan, row["element"])
        if key in element_ids:
            report.error(f"{loc}: duplicate element identifier within scan {scan:03}")
        element_ids.add(key)
    target = present if partial else EXPECTED_SCANS
    if scans != target:
        report.error("Inventory/page coverage differs: "
                     f"missing={sorted(target - scans)}, extra={sorted(scans - target)}")
    for scan, kinds in sheet_kinds.items():
        if len(kinds) > 1:
            report.warn(f"Scan {scan:03} has multiple sheet_kind values: {sorted(kinds)}; review classification")
    report.fact(f"Inventory: {len(rows)} element rows across {len(scans)} scans")


TIMESTAMP = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"


def check_progress(base: Path, present: set[int], partial: bool, report: Report) -> None:
    path = base / "progress.log"
    if not path.exists():
        report.error("Missing progress.log")
        return
    text = read_utf8(path, report)
    if text is None:
        return
    lines = text.splitlines()
    if not lines or not re.fullmatch(TIMESTAMP, lines[0].strip()):
        report.error("progress.log first line is not a UTC timestamp (YYYY-MM-DD HH:MM:SS UTC)")
    done = [int(x) for x in re.findall(r"^33 scan (\d{3}) done " + TIMESTAMP + r"\s*$", text, re.M)]
    audited = [int(x) for x in re.findall(r"^scan (\d{3}) audited " + TIMESTAMP + r"\s*$", text, re.M)]
    target = present if partial else EXPECTED_SCANS
    if set(done) != target:
        report.error(f"Completion records differ from page coverage: missing={sorted(target - set(done))}, extra={sorted(set(done) - target)}")
    if done != sorted(done):
        report.error("Completion records are not in scan order")
    for label, sequence in (("completion", done), ("audit", audited)):
        duplicates = [scan for scan, count in Counter(sequence).items() if count > 1]
        if duplicates:
            report.warn(f"Repeated {label} records for scans {sorted(duplicates)}")
    frozen = re.search(r"^transcription frozen " + TIMESTAMP + r"\s*$", text, re.M)
    opened = re.search(r"^context opened " + TIMESTAMP + r"\s*$", text, re.M)
    if not partial:
        if set(audited) != EXPECTED_SCANS:
            report.error(f"Audit records missing={sorted(EXPECTED_SCANS - set(audited))}, extra={sorted(set(audited) - EXPECTED_SCANS)}")
        if frozen is None:
            report.error("Missing 'transcription frozen <UTC timestamp>' record")
        if opened is None:
            report.error("Missing 'context opened <UTC timestamp>' record")
        if not re.search(r"(?i)(hash(?:es)?.{0,100}unchanged|unchanged.{0,100}hash(?:es)?)", text):
            report.error("Missing explicit end-of-work hash-unchanged statement in progress.log")
    if frozen is not None:
        audit_matches = list(re.finditer(r"^scan (\d{3}) audited " + TIMESTAMP + r"\s*$", text, re.M))
        before_freeze = {int(m.group(1)) for m in audit_matches if m.start() < frozen.start()}
        if before_freeze != EXPECTED_SCANS:
            report.error("Freeze record is not preceded by all 49 page audit records")
    if opened is not None and (frozen is None or opened.start() < frozen.start()):
        report.error("Context-opened record precedes the transcription freeze")
    report.fact(f"Progress: {len(set(done))} scans done; {len(set(audited))} scans audited; freeze recorded={frozen is not None}")


def check_hashes(base: Path, partial: bool, report: Report) -> None:
    path = base / "records" / "frozen_sha256.json"
    if not path.exists():
        if not partial:
            report.warn("No records/frozen_sha256.json: hash integrity cannot be checked by this tool")
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        report.error(f"Cannot read frozen hash manifest: {exc}")
        return
    mapping = data.get("files", data) if isinstance(data, dict) else None
    if not isinstance(mapping, dict):
        report.error("Frozen hash manifest must be a path-to-SHA256 object, or contain such an object in 'files'")
        return
    expected = {f"pages/{PREFIX}_33_scan{s:03}.tex" for s in EXPECTED_SCANS}
    expected.add(f"{PREFIX}_transcription.tex")
    if set(mapping) != expected:
        report.error(f"Frozen hash manifest coverage: missing={sorted(expected - set(mapping))}, extra={sorted(set(mapping) - expected)}")
    log_path = base / "progress.log"
    log = read_utf8(log_path, report) if log_path.exists() else None
    checked = 0
    for relative, digest in mapping.items():
        if not isinstance(relative, str) or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
            report.error("Frozen hash manifest has an invalid path or SHA256 value")
            continue
        file = (base / relative).resolve()
        if not file.is_relative_to(base.resolve()):
            report.error(f"Frozen hash path escapes working directory: {relative}")
            continue
        try:
            actual = hashlib.sha256(file.read_bytes()).hexdigest()
        except OSError as exc:
            report.error(f"Cannot hash {relative}: {exc}")
            continue
        if actual != digest.lower():
            report.error(f"SHA256 mismatch after freeze: {relative}")
        else:
            checked += 1
        if log is not None and not any(digest.lower() in line.lower() and relative in line for line in log.splitlines()):
            report.error(f"Hash and relative filename are not recorded together in progress.log: {relative}")
    report.fact(f"Frozen hashes verified unchanged: {checked}/{len(mapping)}")


def check_companions(base: Path, partial: bool, report: Report) -> None:
    if partial:
        return
    for suffix in ("doubts.md", "notes.md"):
        path = base / f"{PREFIX}_{suffix}"
        if not path.exists():
            report.error(f"Missing required companion: {path.name}")
        elif path.stat().st_size == 0:
            report.error(f"Empty required companion: {path.name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="delivery working directory (default: parent of this tools directory)")
    parser.add_argument("--partial", action="store_true",
                        help="check only the currently present contiguous page prefix; do not require final audit/freeze")
    args = parser.parse_args()
    report = Report()
    base = args.directory.resolve()
    if not base.is_dir():
        report.error(f"Working directory does not exist: {base}")
    else:
        texts = check_pages(base, args.partial, report)
        check_combined(base, texts, args.partial, report)
        check_inventory(base, set(texts), args.partial, report)
        check_progress(base, set(texts), args.partial, report)
        check_hashes(base, args.partial, report)
        check_companions(base, args.partial, report)
    report.print()
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
