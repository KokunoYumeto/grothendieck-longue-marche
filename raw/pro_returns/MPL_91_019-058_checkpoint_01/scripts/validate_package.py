#!/usr/bin/env python3
"""Mechanical validation only; this cannot certify transcription completeness.

Run from anywhere:
    python scripts/validate_package.py [PACKAGE_DIRECTORY]

The default directory is this script's parent package directory. The combined
fragment must be the exact byte-for-byte concatenation of the individual page
files in scan order, without extra separators. Unknown TeX commands are warnings
requiring human classification; --strict-commands makes those warnings errors.

Recommended progress.log hash format (sha256sum format):
    <64 lowercase hex digits>  pages/MPL_91_019-058_91_scan019.tex
    <64 lowercase hex digits>  MPL_91_019-058_transcription.tex
    transcription frozen YYYY-MM-DD HH:MM:SS UTC

Hashes are checked whenever recognized records exist. A freeze record additionally
requires hashes for all 38 pages and the combined fragment and an audit record for
each scan. This script reads deliverables only, never source images or archives.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from pathlib import Path

PREFIX = "MPL_91_019-058"
SCANS = tuple(n for n in range(19, 59) if n not in (30, 33))
CUSTOM = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())
INVENTORY_FIELDS = ["cote", "scan", "sheet_kind", "element", "kind", "position", "first_words_or_objects", "transcribed"]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}

# A practical recognition list, not a complete TeX-language parser. Commands not
# listed here are reported for review, never silently treated as allowed custom
# commands. No source contents are inferred from these lists.
STANDARD = set("""
begin end label ref eqref pageref tag notag nonumber par noindent indent newline
linebreak pagebreak newpage clearpage hspace vspace hfill vfill quad qquad enspace
enskip thinspace medspace thickspace negthinspace negmedspace negthickspace
smallskip medskip bigskip allowbreak nobreak mbox fbox framebox makebox rule strut
phantom hphantom vphantom smash raisebox stackrel overset underset substack
text textrm textsf texttt textit textbf textsl textsc textup textnormal emph
mathrm mathit mathbf mathsf mathtt mathnormal mathcal mathbb mathfrak mathscr
operatorname operatornamewithlimits DeclareMathOperator mathop mathord mathbin
mathrel mathopen mathclose mathpunct mathinner limits nolimits displaylimits
frac dfrac tfrac cfrac binom dbinom tbinom sqrt root over atop choose
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
overline underline widehat widetilde hat tilde bar vec dot ddot dddot ddddot
acute grave breve check mathring overbrace underbrace overrightarrow
overleftarrow overrightharpoon underleftarrow underrightarrow
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon
phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
aleph beth gimel daleth hbar hslash imath jmath ell wp Re Im partial nabla
infty prime emptyset varnothing top bot angle measuredangle sphericalangle
forall exists nexists neg lnot land lor wedge vee bigwedge bigvee
in ni notin owns subset supset subseteq supseteq subsetneq supsetneq
subseteqq supseteqq subsetneqq supsetneqq nsubseteq nsupseteq
cap cup bigcap bigcup uplus biguplus sqcap sqcup bigsqcup
sqsubset sqsupset sqsubseteq sqsupseteq setminus smallsetminus complement
le leq ge geq neq ne equiv sim simeq cong approx approxeq asymp doteq
ll gg lll ggg lesssim gtrsim lessgtr gtrless lesseqgtr gtreqless
leqq geqq leqslant geqslant lneq gneq lneqq gneqq nleq ngeq
prec succ preceq succeq preccurlyeq succcurlyeq precsim succsim
parallel nparallel mid nmid divides perp propto models vdash dashv
Vdash vDash Vvdash nvdash nvDash nVdash nVDash bowtie Join smile frown
rightarrow leftarrow leftrightarrow Rightarrow Leftarrow Leftrightarrow
longrightarrow longleftarrow longleftrightarrow Longrightarrow Longleftarrow
Longleftrightarrow to gets mapsto longmapsto hookrightarrow hookleftarrow
twoheadrightarrow twoheadleftarrow rightarrowtail leftarrowtail
leftharpoonup leftharpoondown rightharpoonup rightharpoondown rightleftharpoons
leftrightharpoons rightleftarrows leftrightarrows leftrightarrow
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow
nearrow searrow swarrow nwarrow dashrightarrow dashleftarrow
rightsquigarrow leftrightsquigarrow leadsto curvearrowleft curvearrowright
circlearrowleft circlearrowright restriction multimap implies impliedby iff
times div cdot centerdot ast star circ bullet diamond pm mp dotplus
oplus ominus otimes oslash odot bigoplus bigotimes bigodot circledast
wr amalg triangleleft triangleright bigtriangleup bigtriangledown triangle
triangleq lhd rhd unlhd unrhd sum prod coprod int iint iiint oint
lim limsup liminf injlim projlim varinjlim varprojlim sup inf min max
sin cos tan cot sec csc sinh cosh tanh coth arcsin arccos arctan
log ln exp det dim deg ker hom gcd Pr arg bmod pmod mod
ldots cdots vdots ddots dots dotsc dotsb dotsm dotsi dotso
langle rangle lceil rceil lfloor rfloor lbrace rbrace lvert rvert lVert rVert
vert Vert backslash slash surd checkmark dag ddag S P copyright pounds
AA aa AE ae OE oe O o L l ss i j LaTeX TeX
qquad displaystyle textstyle scriptstyle scriptscriptstyle
small tiny scriptsize footnotesize normalsize large Large LARGE huge Huge
rm bf it sl sc tt sf cal mit choose centering raggedright raggedleft
item hline cline multicolumn vline tabularnewline arraystretch
ar arrow arrows path draw fill filldraw node coordinate foreach clip
matrix pgfmathsetmacro pgfmathparse pgfmathresult tikzset pgfsetlayers
pgfdeclarelayer pgfextra pgftransformshift pgfpoint cm pgfpointorigin
""".split())
STANDARD.update("xrightarrow xleftarrow linewidth boxed".split())
FORBIDDEN = set("documentclass usepackage RequirePackage newcommand renewcommand providecommand def gdef edef xdef newenvironment renewenvironment input include includegraphics".split())


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def strip_comments(text: str) -> str:
    """Remove unescaped TeX comments while retaining newline/line positions."""
    output = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for i, char in enumerate(line):
            if char == "%":
                backslashes = 0
                j = i - 1
                while j >= 0 and line[j] == "\\":
                    backslashes += 1
                    j -= 1
                if backslashes % 2 == 0:
                    cut = i
                    break
        output.append(line[:cut] + ("\n" if cut < len(line) and line.endswith("\n") else ""))
    return "".join(output)


def check_tex(path: Path, report: Report, strict: bool) -> str | None:
    try:
        original = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.error(f"{path.name}: cannot read UTF-8 text: {exc}")
        return None
    text = strip_comments(original)
    stack: list[int] = []
    line = 1
    index = 0
    while index < len(text):
        char = text[index]
        if char == "\\":
            # Escaped literal braces and other control symbols are not groups.
            match = re.match(r"\\[A-Za-z@]+|\\[^\n]", text[index:])
            if match:
                index += len(match.group())
                continue
        if char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                report.error(f"{path.name}:{line}: unmatched closing brace")
        elif char == "\n":
            line += 1
        index += 1
    for opening_line in stack:
        report.error(f"{path.name}:{opening_line}: unmatched opening brace")

    # Consume control symbols as well as control words so a row break followed
    # immediately by Z, for example, is not misclassified as a command named Z.
    commands = {match.group(1) for match in re.finditer(r"\\([A-Za-z@]+)|\\[^\n]", text) if match.group(1)}
    for command in sorted(commands & FORBIDDEN):
        report.error(f"{path.name}: fragment contains forbidden command \\{command}")
    unknown = sorted(commands - CUSTOM - STANDARD - FORBIDDEN)
    if unknown:
        message = f"{path.name}: manually classify unrecognized commands: " + ", ".join("\\" + cmd for cmd in unknown)
        (report.error if strict else report.warn)(message)
    if re.search(r"\\begin\s*\{document\}", text):
        report.error(f"{path.name}: document environment is forbidden in the fragment")
    return text


def check_inventory(root: Path, report: Report) -> int:
    path = root / f"{PREFIX}_inventory.csv"
    seen: set[int] = set()
    count = 0
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != INVENTORY_FIELDS:
                report.error(f"{path.name}: expected columns in order {INVENTORY_FIELDS!r}; got {reader.fieldnames!r}")
                return 0
            for count, row in enumerate(reader, start=1):
                location = f"{path.name}:CSV record {count + 1}"
                if None in row or any(value is None for value in row.values()):
                    report.error(f"{location}: wrong number of fields")
                    continue
                if row["cote"].strip() != "91":
                    report.error(f"{location}: cote is not 91")
                try:
                    scan = int(row["scan"])
                except ValueError:
                    report.error(f"{location}: scan is not an integer")
                    continue
                seen.add(scan)
                if scan not in SCANS:
                    report.error(f"{location}: unexpected scan {scan}")
                if row["sheet_kind"] not in SHEET_KINDS:
                    report.error(f"{location}: invalid sheet_kind {row['sheet_kind']!r}")
                if row["kind"] not in ELEMENT_KINDS:
                    report.error(f"{location}: invalid element kind {row['kind']!r}")
                if row["transcribed"] != "yes":
                    report.error(f"{location}: transcribed is not exactly 'yes'")
                for field in ("element", "position", "first_words_or_objects"):
                    if not row[field].strip():
                        report.warn(f"{location}: empty {field}")
    except (OSError, UnicodeError, csv.Error) as exc:
        report.error(f"{path.name}: cannot read inventory: {exc}")
    missing = sorted(set(SCANS) - seen)
    if missing:
        report.error(f"{path.name}: missing scans {missing}")
    return count


def parse_hash_record(line: str) -> tuple[str, str] | None:
    patterns = (
        r"^(?:sha256\s+)?([0-9a-fA-F]{64})\s+\*?(.+?)\s*$",
        r"^SHA256\s*\((.+?)\)\s*=\s*([0-9a-fA-F]{64})\s*$",
        r"^sha256\s+(.+?)\s+([0-9a-fA-F]{64})\s*$",
        r"^(.+?)\s+sha256\s+([0-9a-fA-F]{64})\s*$",
    )
    for index, pattern in enumerate(patterns):
        match = re.match(pattern, line, flags=re.IGNORECASE)
        if match:
            first, second = match.groups()
            return (second, first.lower()) if index == 0 else (first, second.lower())
    return None


def check_log(root: Path, expected: list[Path], report: Report) -> tuple[bool, int]:
    path = root / "progress.log"
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        report.error(f"progress.log: cannot read: {exc}")
        return False, 0
    frozen = bool(re.search(r"^transcription frozen\s+", text, re.MULTILINE))
    lines = text.splitlines()
    if not lines or not re.search(r"\d{4}-\d{2}-\d{2}.*(?:UTC|Z|\+00:00)", lines[0]):
        report.warn("progress.log: first line is not a recognized explicit UTC timestamp")
    audited = {int(n) for n in re.findall(r"^scan\s+(\d+)\s+audited\s+", text, re.MULTILINE)}
    done = {int(n) for n in re.findall(r"^91\s+scan\s+(\d+)\s+done\s+", text, re.MULTILINE)}
    if set(SCANS) - done:
        report.error(f"progress.log: missing done records for scans {sorted(set(SCANS) - done)}")
    if frozen and set(SCANS) - audited:
        report.error(f"progress.log: frozen but missing audited records for scans {sorted(set(SCANS) - audited)}")

    expected_resolved = {p.resolve() for p in expected}
    hashes: dict[Path, str] = {}
    freeze_index = next((i for i, line in enumerate(lines) if line.startswith("transcription frozen ")), None)
    for record_index, line in enumerate(lines):
        record = parse_hash_record(line)
        if record is None:
            continue
        name, digest = record
        candidate = Path(name)
        if not candidate.is_absolute():
            if re.fullmatch(rf"{re.escape(PREFIX)}_91_scan\d{{3}}\.tex", name):
                candidate = root / "pages" / name
            else:
                candidate = root / candidate
        candidate = candidate.resolve()
        if candidate not in expected_resolved:
            report.warn(f"progress.log:{record_index + 1}: hash record is not for an expected transcription file: {name}")
            continue
        if candidate in hashes and hashes[candidate] != digest:
            report.error(f"progress.log:{record_index + 1}: conflicting recorded hashes for {name}")
        hashes[candidate] = digest
    if frozen:
        for candidate in sorted(expected_resolved - set(hashes)):
            report.error(f"progress.log: frozen but no recognized SHA-256 for {candidate.relative_to(root.resolve())}")
        if not re.search(r"(?:hash(?:es)?|SHA-256).*(?:unchanged|match)|(?:unchanged|match).*(?:hash(?:es)?|SHA-256)", "\n".join(lines[(freeze_index or 0) + 1:]), re.IGNORECASE):
            report.warn("progress.log: no explicit post-freeze statement that hashes are unchanged/match")
    else:
        report.warn("progress.log: no transcription frozen record; freeze validation is not yet applicable")
    for candidate, recorded in hashes.items():
        try:
            actual = hashlib.sha256(candidate.read_bytes()).hexdigest()
        except OSError as exc:
            report.error(f"cannot read hashed file {candidate.name}: {exc}")
            continue
        if actual != recorded:
            report.error(f"SHA-256 mismatch: {candidate.relative_to(root.resolve())}")
    return frozen, len(hashes)


def validate(root: Path, strict: bool = False) -> tuple[Report, dict[str, object]]:
    report = Report()
    pages = [root / "pages" / f"{PREFIX}_91_scan{n:03d}.tex" for n in SCANS]
    expected_names = {p.name for p in pages}
    actual_names = {p.name for p in (root / "pages").glob("*.tex")}
    for name in sorted(expected_names - actual_names):
        report.error(f"missing page file: pages/{name}")
    for name in sorted(actual_names - expected_names):
        report.error(f"unexpected page file: pages/{name}")
    for scan, path in zip(SCANS, pages):
        if not path.is_file():
            continue
        text = check_tex(path, report, strict)
        if text is not None:
            markers = re.findall(r"\\scanpage\s*\{([^{}]*)\}", text)
            if markers != [str(scan)]:
                report.error(f"{path.name}: expected exactly \\scanpage{{{scan}}}; got {markers!r}")
            cote_markers = re.findall(r"\\cotefile\s*\{([^{}]*)\}", text)
            if cote_markers != (["91"] if scan == 19 else []):
                report.error(f"{path.name}: unexpected cote markers {cote_markers!r}")

    combined = root / f"{PREFIX}_transcription.tex"
    combined_text = check_tex(combined, report, strict)
    if combined_text is not None:
        if not re.match(r"\s*\\cotefile\s*\{91\}\s*\\scanpage\s*\{19\}", combined_text):
            report.error("combined fragment does not start with cote 91 / scan 19 markers")
        if all(p.is_file() for p in pages):
            if combined.read_bytes() != b"".join(p.read_bytes() for p in pages):
                report.error("combined fragment is not the exact byte concatenation of the 38 pages in order")
    for suffix in ("doubts.md", "notes.md"):
        path = root / f"{PREFIX}_{suffix}"
        if not path.is_file() or path.stat().st_size == 0:
            report.error(f"missing or empty required deliverable: {path.name}")
    inventory_rows = check_inventory(root, report)
    frozen, hash_count = check_log(root, pages + [combined], report)
    return report, {"expected_pages": len(SCANS), "page_files_found": len(actual_names & expected_names), "inventory_rows": inventory_rows, "frozen_record_present": frozen, "recognized_hash_records": hash_count}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("package_directory", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict-commands", action="store_true", help="fail on unrecognized TeX commands instead of warning")
    args = parser.parse_args()
    report, stats = validate(args.package_directory.resolve(), args.strict_commands)
    for key, value in stats.items():
        print(f"{key}: {value}")
    for message in report.errors:
        print(f"ERROR: {message}")
    for message in report.warnings:
        print(f"WARNING: {message}")
    print(f"Mechanical result: {len(report.errors)} errors, {len(report.warnings)} warnings.")
    print("Scope: file structure, TeX syntax heuristics, inventory metadata, and recorded hashes only. This does not certify completeness, correct readings, faithful notation, actual image inspection, or the chronology of human work.")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
