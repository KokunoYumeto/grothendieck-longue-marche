#!/usr/bin/env python3
"""Read-only structural checks for MPL_22+23_002-016.

This program performs no OCR and never opens source images or context archives.
It does not assess transcription accuracy, legibility, or semantic completeness.
Run it only when the transcription owner chooses to do so.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


STEM = "MPL_22+23_002-016"
EXPECTED = [(22, n) for n in range(2, 31)] + [(23, n) for n in range(2, 17)]
HEADER = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
CUSTOM = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())
# A deliberately transparent, extendable recognition list. An unrecognized
# command is reported for review, rather than declared to be a forbidden macro.
STANDARD = set("""
begin end par noindent indent hfill vfill hspace vspace quad qquad enspace thinspace
medspace thickspace negthinspace smallskip medskip bigskip linebreak newline pagebreak
nopagebreak newpage clearpage centering raggedright raggedleft leavevmode protect
text textnormal textrm textsf texttt textup textit textsl textsc textbf textmd emph
textsuperscript textsubscript hrule not xrightarrow xleftarrow
mbox makebox parbox shortstack raisebox rule framebox fbox minipage footnote footnotemark
footnotetext thanks url href label ref pageref eqref cite nocite index phantom hphantom
vphantom smash strut mathstrut ensuremath displaystyle textstyle scriptstyle
scriptscriptstyle mathrm mathbf mathit mathsf mathtt mathnormal mathcal mathfrak
mathbb mathscr boldsymbol bm operatorname DeclareMathOperator limits nolimits
displaylimits left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr
Biggl Biggr overset underset stackrel overline underline overbrace underbrace
widehat widetilde hat check breve acute grave tilde bar vec dot ddot dddot ddddot
mathring frac dfrac tfrac cfrac binom dbinom tbinom genfrac sqrt root atop choose
brace brack substack multicolumn multirow hline cline vline multispan span cr tabularnewline
caption item description enumerate itemize verb verbatim textbackslash textasciitilde
textasciicircum textbraceleft textbraceright textless textgreater textbar
textemdash textendash textquotedblleft textquotedblright textquoteleft textquoteright
guillemotleft guillemotright og fg glqq grqq flqq frqq LaTeX TeX S P dag ddag dagger
ddagger copyright pounds euro aa AA ae AE oe OE o O l L ss i j u v H c d b k r t
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa varkappa
lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon phi varphi
chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
aleph beth gimel daleth ell hbar hslash imath jmath wp Re Im partial nabla infty
emptyset varnothing top bot prime backprime forall exists nexists neg lnot
angle measuredangle sphericalangle triangle square Box Diamond diamond lozenge
blacklozenge blacksquare blacktriangle blacktriangledown blacktriangleleft blacktriangleright
triangledown triangleleft triangleright bigtriangleup bigtriangledown
sum prod coprod int iint iiint iiiint idotsint oint oiint oiiint
bigcap bigcup bigsqcup bigvee bigwedge bigodot bigotimes bigoplus biguplus
pm mp times div cdot ast star circ bullet odot oplus ominus otimes oslash
amalg wr setminus smallsetminus cap cup sqcap sqcup uplus vee wedge land lor
dagger ddagger intercal dotplus centerdot lt gt le leq ge geq neq ne equiv
cong sim simeq approx asymp propto doteq dot= triangleq circeq bumpeq Bumpeq
ll gg lll ggg lesssim gtrsim lessapprox gtrapprox leqq geqq lneq gneq lneqq gneqq
prec succ preceq succeq preccurlyeq succcurlyeq precsim succsim subset supset
subseteq supseteq subsetneq supsetneq subsetneqq supsetneqq sqsubset sqsupset
sqsubseteq sqsupseteq nsubseteq nsupseteq nsubset nsupset in ni owns notin notni
vdash dashv models vDash Vdash Vvdash nvdash nvDash perp parallel nparallel
mid nmid smile frown bowtie Join pitchfork therefore because
rightarrow leftarrow leftrightarrow Rightarrow Leftarrow Leftrightarrow
longrightarrow longleftarrow longleftrightarrow Longrightarrow Longleftarrow
Longleftrightarrow mapsto longmapsto hookrightarrow hookleftarrow twoheadrightarrow
twoheadleftarrow rightarrowtail leftarrowtail rightsquigarrow leftrightsquigarrow
dashrightarrow dashleftarrow leadsto to gets implies impliedby iff
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow nearrow searrow
swarrow nwarrow upharpoonleft upharpoonright downharpoonleft downharpoonright
rightharpoonup rightharpoondown leftharpoonup leftharpoondown rightleftharpoons
leftrightharpoons rightleftarrows leftrightarrows looparrowleft looparrowright
curvearrowleft curvearrowright circlearrowleft circlearrowright multimap
Lsh Rsh restriction harpoonright harpoonleft
ldots cdots vdots ddots dots dotsc dotsb dotsm dotsi dotso
langle rangle lbrace rbrace lbrack rbrack lceil rceil lfloor rfloor lvert rvert
lVert rVert vert Vert backslash surd slash
ar arrow draw path node coordinate fill filldraw clip scope endscope foreach
pgfmathsetmacro pgfmathtruncatemacro pgfmathparse pgfmathresult pgfkeys tikz tikzset
usetikzlibrary tikzcdset color colorbox textcolor mathchoice mathbin mathrel mathop
mathord mathopen mathclose mathpunct boxed cancel bcancel xcancel cancelto
acute grave ddot tilde bar breve check hat vec dot
sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh coth
log ln lg exp lim limsup liminf max min sup inf det gcd ker dim hom Pr arg deg
injlim projlim varinjlim varprojlim varlimsup varliminf mod bmod pmod pod
rm bf it cal frak mit sf tt scriptsize tiny small normalsize large Large LARGE
huge Huge baselineskip arraystretch textwidth linewidth columnwidth
""".split())
STAMP_RE = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"
CMD_RE = re.compile(r"\\([A-Za-z@]+)\*?")


def timestamp(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)


def without_comments(source: str) -> str:
    """Replace TeX comments by spaces while preserving offsets and newlines."""
    result = list(source)
    for line in re.finditer(r"[^\n]*", source):
        start, end = line.span()
        for pos in range(start, end):
            if source[pos] != "%":
                continue
            backslashes = 0
            before = pos - 1
            while before >= start and source[before] == "\\":
                backslashes += 1
                before -= 1
            if backslashes % 2 == 0:
                result[pos:end] = " " * (end - pos)
                break
    return "".join(result)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.facts: dict = {}

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def tex_checks(name: str, source: str, allowed: set[str], report: Report) -> str:
    cleaned = without_comments(source)
    braces: list[int] = []
    pos = 0
    while pos < len(cleaned):
        char = cleaned[pos]
        if char == "\\":
            match = re.match(r"\\verb\*?([^A-Za-z\s])", cleaned[pos:])
            if match:
                delimiter = match.group(1)
                end = cleaned.find(delimiter, pos + len(match.group(0)))
                if end < 0:
                    report.error(f"{name}: unterminated \\verb")
                    break
                pos = end + 1
                continue
            command = re.match(r"\\(?:[A-Za-z@]+|.)", cleaned[pos:], re.S)
            pos += len(command.group(0)) if command else 1
            continue
        if char == "{":
            braces.append(pos)
        elif char == "}":
            if braces:
                braces.pop()
            else:
                report.error(f"{name}: unmatched closing brace at line {cleaned.count(chr(10), 0, pos) + 1}")
        pos += 1
    for start in braces:
        report.error(f"{name}: unmatched opening brace at line {cleaned.count(chr(10), 0, start) + 1}")
    commands = set(CMD_RE.findall(cleaned))
    unknown = sorted(commands - STANDARD - CUSTOM - allowed)
    if unknown:
        report.warn(f"{name}: commands needing standard/TikZ or permitted-macro review: " + ", ".join("\\" + x for x in unknown))
    for forbidden in ("documentclass", "newcommand", "renewcommand", "providecommand", "def", "gdef", "edef", "xdef"):
        if forbidden in commands:
            report.error(f"{name}: preamble or macro-definition command \\{forbidden} in a transcription fragment")
    if re.search(r"\\begin\s*\{document\}", cleaned):
        report.error(f"{name}: document environment in a transcription fragment")
    if re.search(r"\\(?:includegraphics|input|include)\b", cleaned):
        report.error(f"{name}: image/file inclusion in the complete transcription fragment")
    return cleaned


def page_stream(cleaned: str) -> list[tuple[int | None, int]]:
    cote = None
    result = []
    for kind, value in re.findall(r"\\(cotefile|scanpage)\s*\{\s*(\d+)\s*\}", cleaned):
        if kind == "cotefile":
            cote = int(value)
        else:
            result.append((cote, int(value)))
    return result


def check_inventory(root: Path, report: Report) -> None:
    file = root / f"{STEM}_inventory.csv"
    if not file.is_file():
        return
    counts = Counter()
    elements = set()
    kinds = Counter()
    sheet_kinds = defaultdict(set)
    with file.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != HEADER:
            report.error(f"Inventory header differs from required header: {reader.fieldnames!r}")
            return
        for row_number, row in enumerate(reader, 2):
            if None in row or any(value is None for value in row.values()):
                report.error(f"Inventory row {row_number}: malformed CSV field count")
                continue
            try:
                key = (int(row["cote"]), int(row["scan"]))
            except ValueError:
                report.error(f"Inventory row {row_number}: invalid cote/scan")
                continue
            if key not in EXPECTED:
                report.error(f"Inventory row {row_number}: unexpected page {key}")
            counts[key] += 1
            kinds[row["kind"]] += 1
            sheet_kinds[key].add(row["sheet_kind"])
            if row["kind"] not in KINDS:
                report.error(f"Inventory row {row_number}: unsupported kind {row['kind']!r}")
            if row["sheet_kind"] not in SHEET_KINDS:
                report.error(f"Inventory row {row_number}: unsupported sheet_kind {row['sheet_kind']!r}")
            if row["transcribed"] != "yes":
                report.error(f"Inventory row {row_number}: transcribed is {row['transcribed']!r}")
            for field in ("element", "position", "first_words_or_objects"):
                if not row[field].strip():
                    report.error(f"Inventory row {row_number}: empty {field}")
            element = (*key, row["element"])
            if element in elements:
                report.error(f"Inventory row {row_number}: duplicate page/element identifier {element}")
            elements.add(element)
    for key in EXPECTED:
        if not counts[key]:
            report.error(f"Inventory has no rows for cote {key[0]}, scan {key[1]:03d}")
        if len(sheet_kinds[key]) > 1:
            report.warn(f"Inventory has multiple sheet_kind values for {key}: {sorted(sheet_kinds[key])}")
    report.facts["inventory_rows"] = sum(counts.values())
    report.facts["inventory_kinds"] = dict(kinds)


def check_progress(root: Path, hashes: dict[str, str], report: Report) -> None:
    file = root / "progress.log"
    if not file.is_file():
        return
    lines = file.read_text(encoding="utf-8").splitlines()
    if not lines or not re.fullmatch(STAMP_RE, lines[0]):
        report.error("progress.log: first line is not a UTC timestamp in the requested format")
    done = []
    audited = []
    freeze_line = None
    context_line = None
    claimed_hashes = {}
    previous = None
    for line_number, line in enumerate(lines, 1):
        for stamp in re.findall(STAMP_RE, line):
            try:
                value = timestamp(stamp)
            except ValueError:
                report.error(f"progress.log:{line_number}: invalid UTC timestamp {stamp}")
                continue
            if previous is not None and value < previous:
                report.warn(f"progress.log:{line_number}: timestamp predates a preceding timestamp")
            previous = value
        match = re.fullmatch(rf"(\d+) scan (\d+) done ({STAMP_RE})", line)
        if match:
            done.append((int(match[1]), int(match[2])))
        match = re.fullmatch(rf"(?:(\d+) )?scan (\d+) audited ({STAMP_RE})", line)
        if match:
            audited.append((int(match[1]) if match[1] else None, int(match[2])))
        if re.fullmatch(rf"transcription frozen ({STAMP_RE})", line):
            freeze_line = line_number
        if re.fullmatch(rf"context opened ({STAMP_RE})", line):
            context_line = line_number
        # Accept conventional sha256sum lines, optionally prefixed SHA256,
        # plus the equally explicit "SHA256 path digest" form.
        match = re.fullmatch(r"(?:SHA-?256\s+)?([a-fA-F0-9]{64})\s+\*?(.+)", line)
        if match:
            digest, path = match.groups()
        else:
            match = re.fullmatch(r"SHA-?256\s+(.+?)\s+([a-fA-F0-9]{64})", line)
            if not match:
                continue
            path, digest = match.groups()
        local = Path(path)
        if local.is_absolute():
            try:
                path = str(local.relative_to(root))
            except ValueError:
                report.warn(f"progress.log:{line_number}: hash path lies outside package: {path}")
                continue
        path = path.removeprefix("./")
        if path in claimed_hashes and claimed_hashes[path] != digest.lower():
            report.error(f"progress.log:{line_number}: inconsistent repeated hashes for {path}")
        claimed_hashes[path] = digest.lower()
    if done != EXPECTED:
        report.error("progress.log: 'done' page sequence differs from the required 44-page sequence")
    # Bare scan audit labels are accepted in required page order; cote-prefixed
    # labels, when present, must identify that same sequence.
    if len(audited) != len(EXPECTED) or any(scan != want_scan or (cote is not None and cote != want_cote)
            for (cote, scan), (want_cote, want_scan) in zip(audited, EXPECTED)):
        report.error("progress.log: audit sequence differs from the required 44-page sequence")
    if freeze_line is None:
        report.error("progress.log: missing 'transcription frozen' timestamp")
    if context_line is None:
        report.warn("progress.log: no 'context opened' timestamp recorded")
    elif freeze_line is None or context_line <= freeze_line:
        report.error("progress.log: context-open marker does not follow the freeze marker")
    for path, digest in hashes.items():
        if path not in claimed_hashes:
            report.error(f"progress.log: missing SHA-256 record for {path}")
        elif claimed_hashes[path] != digest:
            report.error(f"progress.log: SHA-256 mismatch for {path}")
    unknown_paths = set(claimed_hashes) - set(hashes)
    if unknown_paths:
        report.warn("progress.log: additional hash paths were not validated: " + ", ".join(sorted(unknown_paths)))
    if not any(re.search(r"hash(?:es)? .*unchanged|unchanged .*hash", line, re.I) for line in lines):
        report.warn("progress.log: no textual final statement that the frozen hashes remain unchanged was recognized")
    report.facts["done_entries"] = len(done)
    report.facts["audit_entries"] = len(audited)
    report.facts["recorded_transcription_hashes"] = len(set(claimed_hashes) & set(hashes))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--allow-macro", action="append", default=[], metavar="NAME",
                        help="recognize a manually verified standard/TikZ command; repeat as needed")
    parser.add_argument("--strict-macros", action="store_true",
                        help="treat unrecognized-command review warnings as errors")
    parser.add_argument("--json-report", type=Path,
                        help="write the report to this path; otherwise the package is read-only")
    args = parser.parse_args()
    root = args.root.resolve()
    report = Report()
    report.facts["scope"] = "Mechanical structure only; no assessment of transcription accuracy or semantic completeness."
    report.facts["expected_pages"] = len(EXPECTED)
    required = [f"{STEM}_transcription.tex", f"{STEM}_doubts.md",
                f"{STEM}_inventory.csv", f"{STEM}_notes.md", "progress.log"]
    for name in required:
        if not (root / name).is_file():
            report.error(f"Missing required file: {name}")
    expected_names = [f"{STEM}_{cote}_scan{scan:03d}.tex" for cote, scan in EXPECTED]
    actual_names = sorted(p.name for p in (root / "pages").glob("*.tex"))
    for name in sorted(set(actual_names) - set(expected_names)):
        report.error(f"Unexpected page file: pages/{name}")
    sources = []
    hashes = {}
    allowed = {name.lstrip("\\") for name in args.allow_macro}
    for (cote, scan), name in zip(EXPECTED, expected_names):
        path = root / "pages" / name
        if not path.is_file():
            report.error(f"Missing page file: pages/{name}")
            continue
        raw = path.read_bytes()
        source = raw.decode("utf-8")
        sources.append(source)
        hashes[f"pages/{name}"] = hashlib.sha256(raw).hexdigest()
        cleaned = tex_checks(name, source, allowed, report)
        labels = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", cleaned)
        if labels != [str(scan)] and labels != [f"{scan:03d}"]:
            report.error(f"{name}: expected exactly one scanpage marker for {scan}, found {labels}")
        cotes = [int(x) for x in re.findall(r"\\cotefile\s*\{\s*(\d+)\s*\}", cleaned)]
        expected_cotes = [cote] if scan == 2 else []
        if cotes != expected_cotes:
            report.error(f"{name}: expected cotefile markers {expected_cotes}, found {cotes}")
        first = re.match(r"\s*\\(?:cotefile|scanpage)\b", cleaned)
        if not first:
            report.error(f"{name}: page fragment does not start with its page/cote marker")
    combined = root / f"{STEM}_transcription.tex"
    if combined.is_file():
        raw = combined.read_bytes()
        source = raw.decode("utf-8")
        hashes[combined.name] = hashlib.sha256(raw).hexdigest()
        cleaned = tex_checks(combined.name, source, allowed, report)
        if page_stream(cleaned) != EXPECTED:
            report.error("Combined transcription: cote/scan marker sequence differs from required order")
        if len(sources) == len(EXPECTED):
            # All page text must occur verbatim in order. Only whitespace at
            # fragment joins is permitted; no paragraph text is rewritten.
            pos = 0
            for index, page in enumerate(sources):
                while pos < len(source) and source[pos].isspace():
                    pos += 1
                fragment = page.lstrip("\r\n").rstrip("\r\n")
                if not source.startswith(fragment, pos):
                    report.error(f"Combined transcription differs from verbatim page content at {expected_names[index]}")
                    break
                pos += len(fragment)
            else:
                if source[pos:].strip():
                    report.error("Combined transcription has extra content after the last page fragment")
                else:
                    report.facts["combined_matches_pages"] = True
    check_inventory(root, report)
    check_progress(root, hashes, report)
    if args.strict_macros:
        for warning in report.warnings:
            if "commands needing standard/TikZ" in warning:
                report.errors.append(warning)
    result = {"checked_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
              "passed_mechanical_checks": not report.errors,
              "facts": report.facts, "errors": report.errors, "warnings": report.warnings}
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    print(rendered, end="")
    if args.json_report:
        args.json_report.parent.mkdir(parents=True, exist_ok=True)
        args.json_report.write_text(rendered, encoding="utf-8")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
