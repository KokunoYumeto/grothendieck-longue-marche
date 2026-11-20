#!/usr/bin/env python3
"""Read-only structural validation of the SP69 C13 141+142 deliverable.

Usage:
    python scripts/validate_structure.py OUTPUT_DIR SOURCE_TEXTS_DIR
    python scripts/validate_structure.py OUTPUT_DIR SOURCE_TEXTS_DIR --json

This script does not perform OCR, compile TeX, assess readings, or judge
mathematics. It reports filenames, counts, identifiers, and structural errors;
it never quotes transcription or witness text and never changes any record.
The only source table consumed is MARKS.tsv, for its header and ordered IDs.
PREAMBLE.tex is read only to identify declared command names. Source page and
witness files are never opened. The canonical progress records are:

    scan NNN audited YYYY-MM-DD HH:MM:SS UTC [cote CCC]
    transcription frozen YYYY-MM-DD HH:MM:SS UTC
    sha256 <64 hexadecimal digits> <path relative to OUTPUT_DIR>
    hashes verified unchanged YYYY-MM-DD HH:MM:SS UTC (25 files)

The brackets above denote an optional cote suffix, not literal bracket text.
The frozen hash set must cover pages/<filename> for all 24 pages and the combined
transcription. The verification record must follow all hashes and page audits.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


STEM = "SP69_C13_141+142"
PAGE_NAMES = (
    "141_scan015.tex", "141_scan016.tex", "142_scan002.tex",
    "142_scan003.tex", "142_scan004.tex", "142_scan005.tex",
    "142_scan006.tex", "142_scan007.tex", "142_scan008.tex",
    "142_scan009.tex", "142_scan010.tex", "142_scan011.tex",
    "142_scan012.tex", "142_scan013.tex", "142_scan014.tex",
    "142_scan016.tex", "142_scan017.tex", "142_scan018.tex",
    "142_scan019.tex", "142_scan020.tex", "142_scan021.tex",
    "142_scan022.tex", "142_scan024.tex", "142_scan025.tex",
)
REQUIRED_OUTPUTS = tuple(
    f"{STEM}_{suffix}"
    for suffix in (
        "transcription.tex", "changes.md", "collation.tsv", "doubts.md",
        "inventory.csv", "notes.md", "sheet_feedback.md", "hand_log.md",
    )
) + ("decisions.tsv", "CHECK_EVENTS.tsv", "progress.log")
EXPECTED_HASH_PATHS = {f"pages/{name}" for name in PAGE_NAMES} | {f"{STEM}_transcription.tex"}
NO_H_PAGES = {(142, 2), (142, 22)}

DECISIONS_HEADER = (
    "id", "cote", "scan", "decision", "reading", "what the ink shows",
    "crop", "confidence",
)
COLLATION_HEADER = (
    "folder", "their_page", "our_scan", "line", "their_reading",
    "codex_reading", "final_reading", "scan_shows", "kind",
    "marked_in_H", "confidence",
)
INVENTORY_HEADER = (
    "scan", "sheet_kind", "hand", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
EVENTS_HEADER = ("statement_id", "date", "who", "type", "outcome")
EVENTS_OPTIONAL_HEADERS = {"place", "statement"}
MARKS_HEADER = (
    "id", "cote", "scan", "kind", "the mark as written",
    "the LaTeX around it",
)
DECISIONS = {"first", "alternative", "other", "undecided"}
CONFIDENCES = {"high", "medium", "low"}
DISALLOWED_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".jpe", ".jfif", ".tif", ".tiff",
    ".gif", ".bmp", ".webp", ".heic", ".heif", ".avif", ".ico",
    ".svg", ".pdf", ".zip", ".7z", ".rar", ".tar", ".gz",
    ".bz2", ".xz", ".tgz", ".tbz", ".tbz2", ".txz",
}
SCRIPT_SUFFIXES = {".py", ".sh", ".bash", ".js", ".mjs", ".cjs", ".ts", ".ps1"}
FORBIDDEN_DIRECTORIES = {
    "source", "sources", "input", "inputs", "scan", "scans", "witness",
    "witnesses", "hua", "crop", "crops", "cache", "caches", "__pycache__",
    ".cache", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".git",
    ".venv", "venv", "node_modules",
}
FORBIDDEN_CACHE_NAMES = {".ds_store", "thumbs.db", "desktop.ini"}
UTC_TEXT = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"
DONE_RE = re.compile(
    rf"scan (?P<scan>\d{{3}}) done (?P<time>{UTC_TEXT}) cote (?P<cote>\d{{3}})"
)
AUDIT_RE = re.compile(
    rf"scan (?P<scan>\d{{3}}) audited (?P<time>{UTC_TEXT})"
    r"(?: cote (?P<cote>\d{3}))?"
)
HASH_RE = re.compile(r"sha256 (?P<digest>[0-9a-fA-F]{64}) (?P<path>.+)")
HASH_VERIFIED_RE = re.compile(
    rf"hashes verified unchanged (?P<time>{UTC_TEXT}) \((?P<count>\d+) files\)"
)
TEX_COMMAND_RE = re.compile(r"\\([A-Za-z@]+|[^\n])")
# Explicit public command names from standard LaTeX and the packages declared by
# the supplied preamble (AMS math/symbols, mathrsfs, ulem, xcolor, TikZ/TikZ-CD).
# No arbitrary pgf*/tikz* or other command-name prefix is whitelisted.
STANDARD_TEX_COMMANDS = set("""
begin end par noindent indent newline linebreak nolinebreak pagebreak nopagebreak
newpage clearpage cleardoublepage hspace vspace hfill vfill stretch smallskip medskip
bigskip smallskipamount medskipamount bigskipamount addvspace leavevmode ignorespaces
unskip relax protect unprotect aftergroup begingroup endgroup bgroup egroup
text textnormal textrm textsf texttt textmd textbf textup textit textsl textsc
textsuperscript textsubscript emph normalfont rmfamily sffamily ttfamily mdseries
bfseries upshape itshape slshape scshape rm sf tt bf it sl sc em cal mit oldstylenums
tiny scriptsize footnotesize small normalsize large Large LARGE huge Huge
fontsize selectfont fontfamily fontseries fontshape usefont mathversion boldmath
unboldmath mbox makebox parbox fbox framebox raisebox rule hrule vrule hbox vbox vtop
raise lower kern mkern hskip vskip mskip penalty nobreak break allowbreak dotfill
hrulefill null phantom hphantom vphantom smash mathstrut strut strutbox
linewidth textwidth textheight columnwidth columnsep baselineskip lineskip
lineskiplimit parindent parskip hsize vsize unitlength arraycolsep tabcolsep
arraystretch extrarowheight jot fboxsep fboxrule topsep itemsep parsep labelwidth
labelsep leftmargin rightmargin textfloatsep
item label ref pageref eqref cite nocite footnote footnotemark footnotetext
marginpar marginparwidth marginparsep caption captionof centering raggedright
raggedleft centerline rightline leftline shortstack multicolumn hline cline vline
tabularnewline topnewpage intertext shortintertext notag nonumber tag substack
section subsection subsubsection paragraph subparagraph chapter part title author
date maketitle thanks abstract tableofcontents listoffigures listoftables
setcounter addtocounter stepcounter refstepcounter value arabic roman Roman alph
Alph fnsymbol newcounter newlength setlength addtolength settowidth settoheight
settodepth newcommand renewcommand providecommand DeclareRobustCommand
newenvironment renewenvironment NewDocumentCommand RenewDocumentCommand
ProvideDocumentCommand DeclareDocumentCommand NewDocumentEnvironment
RenewDocumentEnvironment ProvideDocumentEnvironment DeclareMathOperator
def gdef edef xdef let futurelet global long outer protected expandafter noexpand
unexpanded csname endcsname if ifx ifnum ifdim ifodd ifcase ifmmode ifhmode ifvmode
ifinner ifcat ifdefined ifcsname else or fi loop repeat advance multiply divide
count dimen skip muskip countdef dimendef skipdef muskipdef newcount newdimen
number romannumeral the numexpr dimexpr glueexpr muglueexpr detokenize string
mathcal mathbb mathfrak mathscr mathnormal mathrm mathbf mathsf mathtt mathit
mathbin mathop mathord mathrel mathopen mathclose mathpunct mathinner boldsymbol pmb
displaystyle textstyle scriptstyle scriptscriptstyle limits nolimits displaylimits
left right middle big Big bigg Bigg bigl bigr bigm Bigl Bigr Bigm biggl biggr biggm
Biggl Biggr Biggm frac dfrac tfrac cfrac genfrac binom dbinom tbinom sqrt root of
over atop choose above overwithdelims atopwithdelims abovewithdelims
operatorname operatornamewithlimits overset underset stackrel sideset boxed
hat widehat tilde widetilde bar vec dot ddot dddot ddddot breve check acute grave
mathring overline underline overbrace underbrace overleftarrow overrightarrow
overleftrightarrow underleftarrow underrightarrow underleftrightarrow
xrightarrow xleftarrow substack mathchoice
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon
phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi
Omega digamma
aleph beth gimel daleth hbar hslash ell imath jmath wp Re Im partial nabla infty
emptyset varnothing forall exists nexists neg lnot top bot angle measuredangle
sphericalangle triangle Box square Diamond diamond blacksquare blacklozenge
lozenge bigstar surd complement eth mho Finv Game Bbbk backprime prime
clubsuit diamondsuit heartsuit spadesuit checkmark circledR circledS maltese
sum prod coproduct int iint iiint iiiint idotsint oint smallint bigcap bigcup
bigsqcup bigvee bigwedge bigodot bigotimes bigoplus biguplus bigtriangleup
bigtriangledown
cdot cdotp times div ast star circ bullet odot oplus ominus otimes oslash amalg
pm mp setminus smallsetminus cap cup sqcap sqcup uplus wedge vee land lor wr
dagger ddagger ltimes rtimes leftthreetimes rightthreetimes dotplus divideontimes
intercal circledast circledcirc circleddash boxplus boxminus boxtimes boxdot
le leq ge geq neq ne lesssim gtrsim lessapprox gtrapprox ll gg lll ggg
leqq geqq leqslant geqslant lneq gneq lneqq gneqq lvertneqq gvertneqq
lesseqgtr gtreqless lesseqqgtr gtreqqless lessgtr gtrless eqslantless eqslantgtr
prec succ preceq succeq preccurlyeq succcurlyeq curlyeqprec curlyeqsucc
precsim succsim precapprox succapprox precneqq succneqq precnsim succnsim
precnapprox succnapprox nprec nsucc npreceq nsucceq
subset supset subseteq supseteq subsetneq supsetneq subsetneqq supsetneqq
subseteqq supseteqq nsubseteq nsupseteq nsubseteqq nsupseteqq varsubsetneq
varsupsetneq varsubsetneqq varsupsetneqq sqsubset sqsupset sqsubseteq sqsupseteq
Subset Supset in ni owns notin mid nmid parallel nparallel shortmid shortparallel
nshortmid nshortparallel perp propto asymp sim simeq approx approxeq cong equiv
doteq doteqdot Doteq fallingdotseq risingdotseq triangleq circeq eqcirc bumpyeq
Bumpeq backsim backsimeq between pitchfork smile frown smallsmile smallfrown
models vdash dashv Vdash vDash Vvdash VDash nvdash nvDash nVdash nVDash
triangleleft triangleright trianglelefteq trianglerighteq vartriangle
blacktriangle blacktriangledown blacktriangleleft blacktriangleright
vartriangleleft vartriangleright ntriangleleft ntriangleright ntrianglelefteq
ntrianglerighteq unlhd unrhd lhd rhd not nless ngtr nleq ngeq nleqq ngeqq
nleqslant ngeqslant nsim ncong
to gets mapsto longmapsto leftarrow rightarrow leftrightarrow Leftarrow
Rightarrow Leftrightarrow longleftarrow longrightarrow longleftrightarrow
Longleftarrow Longrightarrow Longleftrightarrow uparrow downarrow updownarrow
Uparrow Downarrow Updownarrow nearrow searrow swarrow nwarrow hookleftarrow
hookrightarrow leftharpoonup leftharpoondown rightharpoonup rightharpoondown
rightleftharpoons leftrightharpoons upharpoonleft upharpoonright downharpoonleft
downharpoonright twoheadleftarrow twoheadrightarrow leftleftarrows
rightrightarrows leftrightarrows rightleftarrows Lleftarrow Rrightarrow
looparrowleft looparrowright curvearrowleft curvearrowright circlearrowleft
circlearrowright leftrightsquigarrow rightsquigarrow leadsto multimap
Lsh Rsh dashleftarrow dashrightarrow restriction nleftarrow nrightarrow
nleftrightarrow nLeftarrow nRightarrow nLeftrightarrow iff implies impliedby
nearrow searrow nwarrow swarrow
langle rangle lbrace rbrace lbrack rbrack lvert rvert lVert rVert vert Vert
lfloor rfloor lceil rceil backslash lmoustache rmoustache lgroup rgroup arrowvert
Arrowvert bracevert ulcorner urcorner llcorner lrcorner
ldots cdots vdots ddots dots dotsc dotsb dotsm dotsi dotso colon semicolon
bmod pmod mod pod arg deg det dim exp gcd hom inf ker lg lim liminf limsup ln
log max min Pr sec csc cot sin cos tan sinh cosh tanh arcsin arccos arctan
sup injlim projlim varinjlim varprojlim varliminf varlimsup
LaTeX TeX LaTeXe S P copyright pounds dag ddag textdagger textdaggerdbl
textbackslash textasciitilde textasciicircum textbar textbraceleft textbraceright
textless textgreater textunderscore textvisiblespace textbullet textendash
textemdash textellipsis textquoteleft textquoteright textquotedblleft
textquotedblright guillemotleft guillemotright guilsinglleft guilsinglright
oe OE ae AE aa AA o O l L ss i j c v u H d b k r t ensuremath
color textcolor colorbox fcolorbox definecolor colorlet pagecolor nopagecolor
uline uuline sout xout uwave dashuline dotuline markoverwith ULon
verb verbatim endverbatim space thinspace medspace thickspace negthinspace
negmedspace negthickspace enspace quad qquad @
""".split())
TIKZ_COMMANDS = set("""
tikz tikzset tikzstyle usetikzlibrary usepgflibrary path draw fill filldraw clip
shade shadedraw node nodepart coordinate matrix graph foreach scope endscope
useasboundingbox pgfextra tikzcdset arrow ar rar lar uar dar urar ular drar dlar
pgfmathparse pgfmathresult pgfmathsetmacro pgfmathtruncatemacro
pgfmathsetlengthmacro pgfmathsetcount pgfmathsetlength pgfmathaddtolength
pgfmathprintnumber pgfmathprintnumberto pgfmathsetseed pgfmathrandominteger
pgfmathdeclarefunction pgfmathapproxequalto pgfmathfloatparsenumber
pgfpoint pgfpointorigin pgfpointxy pgfpointxyz pgfpointpolar pgfpointpolarxy
pgfpointadd pgfpointdiff pgfpointscale pgfpointanchor pgfextractx pgfextracty
pgfpathmoveto pgfpathlineto pgfpathcurveto pgfpathquadraticcurveto pgfpathclose
pgfpathrectangle pgfpathrectanglecorners pgfpathcircle pgfpathellipse pgfpatharc
pgfpatharcaxes pgfpathgrid pgfusepath pgftransformshift pgftransformxshift
pgftransformyshift pgftransformscale pgftransformxscale pgftransformyscale
pgftransformrotate pgftransformcm pgftransformreset pgfsetlinewidth pgfsetdash
pgfsetcolor pgfsetfillcolor pgfsetstrokecolor pgfsetfillopacity pgfsetstrokeopacity
pgfsetroundcap pgfsetbuttcap pgfsetrectcap pgfsetroundjoin pgfsetbeveljoin
pgfsetmiterjoin pgfsetmiterlimit pgfsetarrows pgfsetarrowsstart pgfsetarrowsend
pgfkeys pgfkeysalso pgfkeysvalueof pgfkeysgetvalue pgfkeyssetvalue pgftext pgfnode
pgfcoordinate pgfdeclarelayer pgfsetlayers pgfresetboundingbox pgfinterruptboundingbox
endpgfinterruptboundingbox
""".split())
FRAGMENT_FORBIDDEN_COMMANDS = {
    "documentclass", "documentstyle", "usepackage", "RequirePackage", "LoadClass",
    "LoadClassWithOptions", "ProvidesClass", "ProvidesPackage", "NeedsTeXFormat",
    "PassOptionsToPackage", "PassOptionsToClass", "document", "enddocument",
    "input", "include", "includeonly", "includegraphics",
}


@dataclass
class Check:
    name: str
    status: str
    message: str
    details: list[str]


class Report:
    def __init__(self, output_dir: Path, source_dir: Path) -> None:
        self.output_dir = output_dir
        self.source_dir = source_dir
        self.checks: list[Check] = []

    def add(
        self, name: str, ok: bool, message: str, details: Iterable[str] = (),
    ) -> None:
        self.checks.append(Check(name, "pass" if ok else "fail", message, list(details)))

    def warn(self, name: str, message: str, details: Iterable[str] = ()) -> None:
        self.checks.append(Check(name, "warning", message, list(details)))

    @property
    def ok(self) -> bool:
        return not any(c.status == "fail" for c in self.checks)

    def payload(self) -> dict:
        return {
            "ok": self.ok,
            "output_dir": str(self.output_dir),
            "source_texts_dir": str(self.source_dir),
            "expected_page_count": len(PAGE_NAMES),
            "counts": dict(Counter(c.status for c in self.checks)),
            "checks": [asdict(c) for c in self.checks],
        }


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_utf8(path: Path) -> str:
    # Normalize only platform line endings, not interior spacing or punctuation.
    return path.read_text(encoding="utf-8-sig")


def classify_package_path(path: Path | str) -> tuple[bool, str]:
    """Classify a relative package path without inspecting its file contents.

    Shared with package_checkpoint.py so validation and packaging use the same
    policy. Actual symlinks must additionally be rejected by the caller.
    """
    path = Path(path)
    rel = path.as_posix()
    if path.is_absolute() or ".." in path.parts or "\\" in rel:
        return False, "unsafe package path"
    if path.suffix.lower() in DISALLOWED_SUFFIXES:
        return False, "image, PDF, or nested archive"
    if path.suffix.lower() in {".pyc", ".pyo"} or path.name.lower() in FORBIDDEN_CACHE_NAMES:
        return False, "cache or operating-system metadata"
    if any(part.lower() in FORBIDDEN_DIRECTORIES
           or part.lower().endswith(("_scans", "_texts"))
           for part in path.parts[:-1]):
        return False, "input, scan, witness, crop, or cache directory"
    if path.name.lower().startswith("hua_") or path.name in {"MARKS.tsv", "PREAMBLE.tex"}:
        return False, "source table, preamble, or witness copy"
    if rel in REQUIRED_OUTPUTS or path.name in PAGE_NAMES:
        return True, "required deliverable"
    if rel == "crop_register.tsv":
        return True, "crop register metadata"
    if path.suffix.lower() in SCRIPT_SUFFIXES:
        return True, "work script"
    if len(path.parts) >= 2 and path.parts[0] == "records" and path.suffix.lower() == ".json":
        return True, "work record"
    if path.suffix.lower() == ".txt":
        # Page-shaped text files are not auxiliary prose documentation.
        if re.search(r"(?:^|_)scan\d{3}(?:\.|_)", path.name, re.IGNORECASE):
            return False, "possible source page or witness copy"
        return True, "auxiliary text documentation"
    return False, "unexpected file or possible input copy"


def read_table(
    path: Path,
    delimiter: str,
    required_header: tuple[str, ...],
    report: Report,
    name: str,
    optional_headers: set[str] | None = None,
) -> list[dict[str, str]] | None:
    try:
        text = read_utf8(path)
        parsed = list(csv.reader(io.StringIO(text, newline=""), delimiter=delimiter, strict=True))
    except (OSError, UnicodeError, csv.Error) as exc:
        report.add(name, False, f"Cannot read {path.name}: {type(exc).__name__}.")
        return None
    if not parsed:
        report.add(name, False, f"{path.name} is empty.")
        return None
    header = tuple(parsed[0])
    if optional_headers is None:
        header_ok = header == required_header
    else:
        header_ok = (
            header[:len(required_header)] == required_header
            and set(header[len(required_header):]).issubset(optional_headers)
            and len(header) == len(set(header))
        )
    if not header_ok:
        report.add(
            name, False, f"{path.name} has an incorrect header.",
            ["Required columns: " + ", ".join(required_header)],
        )
        return None
    rows: list[dict[str, str]] = []
    problems = []
    for row_number, row in enumerate(parsed[1:], 2):
        if len(row) != len(header):
            problems.append(
                f"Record {row_number}: {len(row)} fields; expected {len(header)}."
            )
        else:
            rows.append(dict(zip(header, row)))
    report.add(
        name, not problems,
        f"{path.name}: header and record widths checked ({len(rows)} records).",
        problems,
    )
    return rows if not problems else None


def check_package(root: Path, report: Report) -> dict[str, Path]:
    all_paths = sorted(root.rglob("*"))
    files = [p for p in all_paths if p.is_file() or p.is_symlink()]
    missing = [name for name in REQUIRED_OUTPUTS if not (root / name).is_file()]
    empty = [name for name in REQUIRED_OUTPUTS
             if (root / name).is_file() and (root / name).stat().st_size == 0]
    report.add(
        "required_outputs", not missing and not empty,
        f"Checked {len(REQUIRED_OUTPUTS)} required top-level outputs.",
        [f"Missing: {name}" for name in missing] + [f"Empty: {name}" for name in empty],
    )

    by_name: dict[str, list[Path]] = {}
    for path in files:
        by_name.setdefault(path.name, []).append(path)
    page_problems = []
    pages = {}
    for name in PAGE_NAMES:
        matches = by_name.get(name, [])
        if len(matches) != 1:
            page_problems.append(f"{name}: found {len(matches)} copies; expected 1.")
        elif matches[0].is_symlink():
            page_problems.append(f"{name}: symbolic links are not package records.")
        else:
            pages[name] = matches[0]
    other_tex = [
        relative(p, root) for p in files
        if p.suffix.lower() == ".tex"
        and p.name not in PAGE_NAMES
        and relative(p, root) != f"{STEM}_transcription.tex"
    ]
    page_problems += [f"Unexpected TeX file: {p}" for p in other_tex]
    report.add(
        "page_filenames", not page_problems,
        f"Found {len(pages)} of {len(PAGE_NAMES)} uniquely named page files.",
        page_problems,
    )

    package_problems = []
    for path in files:
        rel = relative(path, root)
        if path.is_symlink():
            package_problems.append(f"Symbolic link: {rel}")
        allowed, reason = classify_package_path(rel)
        if not allowed:
            package_problems.append(f"{rel}: {reason}.")
    report.add(
        "package_contents", not package_problems,
        "Package allows deliverables, work scripts, crop metadata, record JSON, and text documentation; "
        "images, inputs, witnesses, caches, and nested archives are excluded.",
        package_problems,
    )
    return pages


def boundary_equivalent(combined: str, pages: list[str]) -> bool:
    """Allow whitespace changes only before, between, and after whole pages.

    Every page must have a nonempty core. Each core is matched literally and
    consecutively; no interior whitespace is discarded or normalized.
    """
    cursor = 0
    for page in pages:
        core = page.strip()
        if not core:
            return False
        while cursor < len(combined) and combined[cursor].isspace():
            cursor += 1
        if not combined.startswith(core, cursor):
            return False
        cursor += len(core)
    return all(char.isspace() for char in combined[cursor:])


def brace_errors(text: str) -> list[str]:
    """Check literal unescaped braces, ignoring TeX percent comments.

    A brace or percent sign is escaped iff preceded by an odd run of backslashes.
    This is a deliberately basic structural check, without macro expansion.
    """
    stack: list[tuple[int, int]] = []
    errors = []
    line, column = 1, 0
    backslashes = 0
    comment = False
    for char in text:
        column += 1
        if char == "\n":
            line, column = line + 1, 0
            comment, backslashes = False, 0
            continue
        if comment:
            continue
        escaped = backslashes % 2 == 1
        if char == "%" and not escaped:
            comment = True
        elif char == "{" and not escaped:
            stack.append((line, column))
        elif char == "}" and not escaped:
            if stack:
                stack.pop()
            else:
                errors.append(f"Unmatched closing brace at line {line}, column {column}.")
        backslashes = backslashes + 1 if char == "\\" else 0
    errors += [f"Unmatched opening brace at line {line}, column {column}."
               for line, column in stack]
    return errors


def mask_tex_literals(text: str) -> str:
    """Mask comments and literal verb payloads, preserving offsets and newlines."""
    masked = list(text)

    def blank(start: int, end: int) -> None:
        for index in range(start, end):
            if masked[index] != "\n":
                masked[index] = " "

    index = 0
    while index < len(text):
        char = text[index]
        if char == "%":
            end = text.find("\n", index)
            end = len(text) if end < 0 else end
            blank(index, end)
            index = end
        elif char == "\\":
            token = TEX_COMMAND_RE.match(text, index)
            if token is None:
                index += 1
                continue
            end = token.end()
            if token[1] == "verb":
                start = end + (end < len(text) and text[end] == "*")
                if start < len(text) and not text[start].isspace():
                    close = text.find(text[start], start + 1)
                    if close >= 0:
                        blank(start, close + 1)
                        end = close + 1
            elif token[1] == "begin":
                env = re.match(r"\s*\{(verbatim\*?)\}", text[end:])
                if env:
                    start = end + env.end()
                    close = text.find("\\end{" + env[1] + "}", start)
                    if close >= 0:
                        blank(start, close)
                        end = close
            index = end
        else:
            index += 1
    return "".join(masked)


def preamble_command_names(text: str) -> set[str]:
    """Take permission from declarations, never from incidental body references."""
    clean = mask_tex_literals(text)
    command_starts = {match.start() for match in TEX_COMMAND_RE.finditer(clean)}
    names = set()
    declaration = re.compile(
        r"\\(?:newcommand|renewcommand|providecommand|DeclareRobustCommand|DeclareMathOperator|"
        r"NewDocumentCommand|RenewDocumentCommand|ProvideDocumentCommand|DeclareDocumentCommand|"
        r"DeclareMathSymbol|DeclareMathDelimiter|DeclareMathAccent)\*?\s*"
        r"(?:\{\s*\\([A-Za-z@]+)\s*\}|\\([A-Za-z@]+))"
    )
    for match in declaration.finditer(clean):
        if match.start() in command_starts:
            names.add(match[1] or match[2])
    for match in re.finditer(r"\\(?:def|gdef|edef|xdef|let)\s*\\([A-Za-z@]+)", clean):
        if match.start() in command_starts:
            names.add(match[1])
    for match in re.finditer(r"\\newif\s*\\if([A-Za-z@]+)", clean):
        if match.start() in command_starts:
            names.update({"if" + match[1], match[1] + "true", match[1] + "false"})
    return names


def tex_scopes(clean: str) -> tuple[dict[int, int], list[tuple[int, int]], list[tuple[int, int]]]:
    """Locate lexical groups and environments; this is not TeX expansion."""
    braces: dict[int, int] = {}
    brace_stack: list[int] = []
    index = 0
    while index < len(clean):
        if clean[index] == "\\":
            match = TEX_COMMAND_RE.match(clean, index)
            index = match.end() if match else index + 1
            continue
        if clean[index] == "{":
            brace_stack.append(index)
        elif clean[index] == "}" and brace_stack:
            braces[brace_stack.pop()] = index + 1
        index += 1
    scopes = list(braces.items())
    tikz_scopes = []
    env_stack: list[tuple[str, int]] = []
    command_starts = {match.start() for match in TEX_COMMAND_RE.finditer(clean)}
    for match in re.finditer(r"\\(begin|end)\s*\{([A-Za-z*]+)\}", clean):
        if match.start() not in command_starts:
            continue
        if match[1] == "begin":
            env_stack.append((match[2], match.start()))
        elif env_stack and env_stack[-1][0] == match[2]:
            name, start = env_stack.pop()
            span = (start, match.end())
            scopes.append(span)
            if name == "tikzpicture":
                tikz_scopes.append(span)
    for match in re.finditer(r"\\tikz\b\s*(?:\[[^\]]*\]\s*)?(\{)", clean):
        if match.start() not in command_starts:
            continue
        opening = match.start(1)
        if opening in braces:
            tikz_scopes.append((opening, braces[opening]))
    return braces, scopes, tikz_scopes


def local_drawing_bindings(clean: str) -> dict[str, list[tuple[int, int]]]:
    """Recognize local TikZ/PGF variables without granting page-wide macros."""
    braces, scopes, tikz_scopes = tex_scopes(clean)
    command_starts = {match.start() for match in TEX_COMMAND_RE.finditer(clean)}
    bindings: dict[str, list[tuple[int, int]]] = {}

    def scope_end(position: int) -> int:
        return min((end for start, end in scopes if start < position < end), default=len(clean))

    def bind(name: str, start: int, end: int | None = None) -> None:
        end = scope_end(start) if end is None else min(end, scope_end(start))
        bindings.setdefault(name, []).append((start, end))

    # Simple local numeric/coordinate definitions are normal drawing variables.
    # Global and parameterized definitions never grant additional permission.
    for match in re.finditer(r"\\def\s*\\([A-Za-z@]+)\s*(\{)", clean):
        if match.start() not in command_starts or re.search(r"\\global(?:\s*\\(?:long|outer|protected))*\s*$", clean[:match.start()]):
            continue
        opening = match.start(2)
        if opening not in braces or not any(start <= match.start() < end for start, end in tikz_scopes):
            continue
        body = clean[opening + 1:braces[opening] - 1]
        if "#" in body or re.search(r"\\(?:def|gdef|edef|xdef|let|csname|newcommand|renewcommand)\b", body):
            continue
        bind(match[1], match.start())
    targets = (
        r"pgfmathsetmacro|pgfmathtruncatemacro|pgfmathsetlengthmacro|"
        r"pgfmathrandominteger|pgfmathsetcount|pgfmathsetlength"
    )
    for match in re.finditer(r"\\(?:" + targets + r")\s*(?:\{\s*\\([A-Za-z@]+)\s*\}|\\([A-Za-z@]+))", clean):
        if match.start() in command_starts:
            bind(match[1] or match[2], match.start())
    for match in re.finditer(r"\\(?:pgfkeysgetvalue|pgfmathprintnumberto)\s*(?:\[[^\]]*\]\s*)?\{[^{}]*\}\s*\{\s*\\([A-Za-z@]+)\s*\}", clean):
        if match.start() in command_starts:
            bind(match[1], match.start())
    for match in re.finditer(r"\\foreach\b", clean):
        if match.start() not in command_starts:
            continue
        in_match = re.search(r"\bin\b", clean[match.end():scope_end(match.start())])
        if in_match is None:
            continue
        header_end = match.end() + in_match.start()
        header = clean[match.end():header_end]
        variables = re.match(r"\s*(?:\[[^\]]*\]\s*)?(\\[A-Za-z@]+(?:\s*/\s*\\[A-Za-z@]+)*)", header)
        names = set(re.findall(r"\\([A-Za-z@]+)", variables[1])) if variables else set()
        names.update(re.findall(r"(?:\bcount\s*=|\bas\s+)\s*\\([A-Za-z@]+)", header))
        cursor = match.end() + in_match.end()
        while cursor < len(clean) and clean[cursor].isspace():
            cursor += 1
        if cursor in braces:  # the value list, followed by the loop body
            cursor = braces[cursor]
        else:
            token = TEX_COMMAND_RE.match(clean, cursor)
            if token:
                cursor = token.end()
        while cursor < len(clean) and clean[cursor].isspace():
            cursor += 1
        if cursor in braces:
            end = braces[cursor]
        else:
            semicolon = clean.find(";", cursor, scope_end(match.start()))
            end = semicolon + 1 if semicolon >= 0 else scope_end(match.start())
        for name in names:
            bind(name, match.start(), end)
    # TikZ's let syntax creates numeric coordinate component registers.
    for match in re.finditer(r"\blet\s+\\[pxyn][0-9]+", clean):
        if any(start <= match.start() < end for start, end in tikz_scopes):
            semicolon = clean.find(";", match.end(), scope_end(match.start()))
            end = semicolon + 1 if semicolon >= 0 else scope_end(match.start())
            for name in ("p", "x", "y", "n"):
                bind(name, match.start(), end)
    return bindings


def audit_fragment(text: str, preamble_names: set[str]) -> tuple[list[str], list[str]]:
    """Return wrapper errors and unsupported command names, without text excerpts."""
    clean = mask_tex_literals(text)
    allowed = STANDARD_TEX_COMMANDS | TIKZ_COMMANDS | preamble_names
    bindings = local_drawing_bindings(clean)
    command_starts = {match.start() for match in TEX_COMMAND_RE.finditer(clean)}
    wrappers = []
    unsupported: dict[str, int] = {}
    for match in TEX_COMMAND_RE.finditer(clean):
        name = match[1]
        if not re.fullmatch(r"[A-Za-z@]+", name):
            continue
        line = clean.count("\n", 0, match.start()) + 1
        if name in FRAGMENT_FORBIDDEN_COMMANDS:
            wrappers.append(f"Line {line}: fragment contains forbidden preamble/wrapper or file-input command \\{name}.")
        elif name not in allowed and not any(start <= match.start() < end for start, end in bindings.get(name, [])):
            unsupported.setdefault(name, line)
    for match in re.finditer(r"\\(?:begin|end)\s*\{\s*document\s*\}", clean):
        if match.start() not in command_starts:
            continue
        line = clean.count("\n", 0, match.start()) + 1
        wrappers.append(f"Line {line}: document environment is not permitted in a fragment.")
    macro_errors = [f"Line {line}: unsupported command \\{name}; absent from PREAMBLE declarations and the explicit standard/TikZ allowlist."
                    for name, line in sorted(unsupported.items())]
    return wrappers, macro_errors


def check_transcription(root: Path, page_paths: dict[str, Path], report: Report, source: Path) -> None:
    if len(page_paths) != len(PAGE_NAMES):
        report.add("combined_transcription", False, "Cannot compare: page file set is incomplete.")
        report.add("brace_balance", False, "Cannot check all pages: page file set is incomplete.")
        return
    pages: list[str] = []
    problems = []
    fragments: list[tuple[str, str]] = []
    for name in PAGE_NAMES:
        try:
            page = read_utf8(page_paths[name])
            pages.append(page)
            fragments.append((name, page))
            if not page.strip():
                problems.append(f"{name}: empty page content.")
            problems += [f"{name}: {message}" for message in brace_errors(page)]
        except (OSError, UnicodeError) as exc:
            problems.append(f"{name}: cannot read UTF-8 ({type(exc).__name__}).")
    report.add(
        "brace_balance", not problems,
        "Checked unescaped brace balance in all available page files; TeX comments ignored.",
        problems,
    )
    try:
        combined = read_utf8(root / f"{STEM}_transcription.tex")
    except (OSError, UnicodeError) as exc:
        report.add("combined_transcription", False,
                   f"Cannot read combined transcription ({type(exc).__name__}).")
        return
    fragments.append((f"{STEM}_transcription.tex", combined))
    if len(pages) != len(PAGE_NAMES):
        report.add("combined_transcription", False, "Cannot compare: one or more pages are unreadable.")
    elif combined == "".join(pages):
        report.add("combined_transcription", True,
                   "Combined transcription equals the ordered page concatenation exactly.")
    elif boundary_equivalent(combined, pages):
        report.add("combined_transcription", True,
                   "Combined transcription matches all page interiors exactly; only boundary whitespace differs.")
    else:
        report.add("combined_transcription", False,
                   "Combined transcription differs from the ordered pages beyond boundary whitespace.")
    try:
        preamble_names = preamble_command_names(read_utf8(source / "PREAMBLE.tex"))
    except (OSError, UnicodeError) as exc:
        report.add("macro_audit", False,
                   f"Cannot read PREAMBLE.tex command declarations ({type(exc).__name__}).")
        preamble_names = set()
    wrapper_problems, macro_problems = [], []
    for filename, text in fragments:
        wrappers, macros = audit_fragment(text, preamble_names)
        wrapper_problems.extend(f"{filename}: {item}" for item in wrappers)
        macro_problems.extend(f"{filename}: {item}" for item in macros)
    report.add("fragment_wrappers", not wrapper_problems,
               "Checked all page files and the combined fragment for preambles, document wrappers, and external file inputs.",
               wrapper_problems)
    report.add("macro_commands", not macro_problems,
               f"Conservative command audit using {len(preamble_names)} preamble declarations, explicit standard/TikZ names, "
               "and scoped drawing variables; no TeX expansion or compilation.", macro_problems)


def page_identity(cote: str, scan: str) -> tuple[int, int] | None:
    """Compare numeric page metadata without treating zero padding as a change."""
    if not re.fullmatch(r"[0-9]+", cote) or not re.fullmatch(r"[0-9]+", scan):
        return None
    return int(cote), int(scan)


def check_tables(root: Path, source: Path, report: Report) -> None:
    marks = read_table(source / "MARKS.tsv", "\t", MARKS_HEADER, report, "marks_schema")
    decisions = read_table(root / "decisions.tsv", "\t", DECISIONS_HEADER,
                           report, "decisions_schema")
    if marks is not None and decisions is not None:
        mark_ids = [row["id"] for row in marks]
        decision_ids = [row["id"] for row in decisions]
        problems = []
        if not mark_ids:
            problems.append("MARKS.tsv contains no mark IDs.")
        if any(not value for value in mark_ids):
            problems.append("MARKS.tsv contains an empty ID.")
        if len(mark_ids) != len(set(mark_ids)):
            problems.append("MARKS.tsv contains duplicate IDs.")
        mark_locations = {}
        for index, row in enumerate(marks, 2):
            location = page_identity(row["cote"], row["scan"])
            mark_locations[row["id"]] = location
            if location is None:
                problems.append(f"MARKS.tsv record {index}: invalid cote/scan metadata.")
        if mark_ids != decision_ids:
            problems.append("Decision IDs do not equal the MARKS.tsv IDs in source order.")
            missing = Counter(mark_ids) - Counter(decision_ids)
            extra = Counter(decision_ids) - Counter(mark_ids)
            if missing:
                problems.append(f"Missing decision rows: {sum(missing.values())}.")
            if extra:
                problems.append(f"Extra or repeated decision rows: {sum(extra.values())}.")
            if not missing and not extra:
                problems.append("ID membership agrees, but row order differs.")
        for index, row in enumerate(decisions, 2):
            if row["decision"] not in DECISIONS:
                problems.append(f"decisions.tsv record {index}: invalid decision enum.")
            if row["confidence"] not in CONFIDENCES:
                problems.append(f"decisions.tsv record {index}: invalid confidence enum.")
            location = page_identity(row["cote"], row["scan"])
            if location is None:
                problems.append(f"decisions.tsv record {index}: invalid cote/scan metadata.")
            elif row["id"] in mark_locations and location != mark_locations[row["id"]]:
                problems.append(f"decisions.tsv record {index}: cote/scan differs from MARKS.tsv for this ID.")
        report.add("decision_coverage", not problems,
                   f"Checked ordered coverage and page assignments for {len(mark_ids)} mark IDs, "
                   "plus decision/confidence enums.",
                   problems)
    else:
        report.add("decision_coverage", False, "Cannot verify decisions because a required table is invalid.")

    collation = read_table(root / f"{STEM}_collation.tsv", "\t", COLLATION_HEADER,
                           report, "collation_schema")
    if collation is not None:
        invalid = [f"Record {index}: invalid confidence enum."
                   for index, row in enumerate(collation, 2)
                   if row["confidence"] not in CONFIDENCES]
        report.add("collation_confidence", not invalid,
                   "Checked collation confidence values.", invalid)
        no_h_problems = []
        for index, row in enumerate(collation, 2):
            location = page_identity(row["folder"], row["our_scan"])
            if location is None:
                no_h_problems.append(f"Record {index}: invalid folder/our_scan metadata.")
            elif location in NO_H_PAGES:
                no_h_problems.append(f"Record {index}: cote 142 scan {location[1]:03d} has no H witness and must have no collation rows.")
        report.add("collation_no_h_pages", not no_h_problems,
                   "Checked absence of H collation rows for cote 142 scans 002 and 022.", no_h_problems)
    inventory = read_table(root / f"{STEM}_inventory.csv", ",", INVENTORY_HEADER,
                           report, "inventory_schema")
    if inventory is not None:
        invalid = [f"Record {index}: transcribed must be yes."
                   for index, row in enumerate(inventory, 2)
                   if row["transcribed"] != "yes"]
        if not inventory:
            invalid.append("Inventory contains no records.")
        report.add("inventory_transcribed", not invalid,
                   "Checked inventory transcribed values.", invalid)
    read_table(root / "CHECK_EVENTS.tsv", "\t", EVENTS_HEADER,
               report, "events_schema", EVENTS_OPTIONAL_HEADERS)


def parse_utc(value: str) -> datetime | None:
    try:
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
    except ValueError:
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z", value):
            return None
        try:
            return datetime.fromisoformat(value[:-1] + "+00:00")
        except ValueError:
            return None


def check_progress(root: Path, report: Report) -> None:
    try:
        lines = read_utf8(root / "progress.log").splitlines()
    except (OSError, UnicodeError) as exc:
        report.add("progress_log", False, f"Cannot read progress.log ({type(exc).__name__}).")
        return
    problems = []
    if not lines or parse_utc(lines[0]) is None:
        problems.append("First line must be a valid UTC datetime.")
    expected_pairs = [(name[:3], name[8:11]) for name in PAGE_NAMES]
    done_pairs: list[tuple[str, str]] = []
    audit_explicit: list[tuple[str, str]] = []
    audit_implicit: list[str] = []
    frozen_lines: list[int] = []
    hashes: list[tuple[int, str, str]] = []
    verified: list[tuple[int, str, int]] = []
    page_event_lines: list[int] = []
    event_times: list[datetime] = []
    for index, line in enumerate(lines[1:], 2):
        if not line.strip():
            continue
        done = DONE_RE.fullmatch(line)
        audit = AUDIT_RE.fullmatch(line)
        hash_match = HASH_RE.fullmatch(line)
        verification = HASH_VERIFIED_RE.fullmatch(line)
        if done:
            page_event_lines.append(index)
            done_pairs.append((done["cote"], done["scan"]))
            if parse_utc(done["time"]) is None:
                problems.append(f"Line {index}: invalid done datetime.")
            else:
                event_times.append(parse_utc(done["time"]))
        elif audit:
            page_event_lines.append(index)
            if audit["cote"] is None:
                audit_implicit.append(audit["scan"])
            else:
                audit_explicit.append((audit["cote"], audit["scan"]))
            if parse_utc(audit["time"]) is None:
                problems.append(f"Line {index}: invalid audit datetime.")
            else:
                event_times.append(parse_utc(audit["time"]))
        elif line.startswith("transcription frozen "):
            frozen_lines.append(index)
            if parse_utc(line[len("transcription frozen "):]) is None:
                problems.append(f"Line {index}: invalid freeze datetime.")
            else:
                event_times.append(parse_utc(line[len("transcription frozen "):]))
        elif hash_match:
            hashes.append((index, hash_match["digest"].lower(), hash_match["path"]))
        elif verification:
            verified.append((index, verification["time"], int(verification["count"])))
        elif re.search(r"\b(?:done|audited|sha256|frozen)\b", line) or line.startswith("hashes verified"):
            problems.append(f"Line {index}: malformed done, audit, freeze, hash, or verification record.")

    expected = Counter(expected_pairs)
    if len(done_pairs) != 24 or Counter(done_pairs) != expected:
        problems.append(f"Found {len(done_pairs)} done records; require exactly one for each of the 24 pages.")
    explicit = Counter(audit_explicit)
    unmatched_explicit = explicit - expected
    remaining = expected - explicit
    remaining_scans: Counter[str] = Counter()
    for (_, scan), count in remaining.items():
        remaining_scans[scan] += count
    audit_count = len(audit_explicit) + len(audit_implicit)
    if (audit_count != 24 or unmatched_explicit
            or Counter(audit_implicit) != remaining_scans):
        problems.append(f"Found {audit_count} audit records; require exactly one per page (cote may be omitted).")
    report.add("progress_log", not problems,
               f"Checked first-line UTC datetime, {len(done_pairs)} done records, and {audit_count} audit records.",
               problems)

    hash_problems = []
    if len(frozen_lines) != 1:
        hash_problems.append(f"Found {len(frozen_lines)} freeze records; expected 1.")
    if not hashes:
        hash_problems.append("No sha256 records found after transcription freeze.")
    seen_paths: set[str] = set()
    for line_number, digest, raw_path in hashes:
        path = Path(raw_path)
        if path.is_absolute() or ".." in path.parts or "\\" in raw_path:
            hash_problems.append(f"Line {line_number}: hash path must be a safe relative POSIX path.")
            continue
        rel = path.as_posix()
        if rel in seen_paths:
            hash_problems.append(f"Line {line_number}: repeated hash path.")
            continue
        seen_paths.add(rel)
        if frozen_lines and line_number <= frozen_lines[0]:
            hash_problems.append(f"Line {line_number}: sha256 record precedes the freeze record.")
        target = root / path
        try:
            if not target.resolve().is_relative_to(root):
                hash_problems.append(f"Line {line_number}: hash path escapes the output directory.")
                continue
            with target.open("rb") as stream:
                actual = hashlib.file_digest(stream, "sha256").hexdigest()
        except (OSError, ValueError) as exc:
            hash_problems.append(f"Line {line_number}: cannot read hashed file ({type(exc).__name__}).")
            continue
        if actual != digest:
            hash_problems.append(f"Line {line_number}: SHA-256 mismatch for {rel}.")
    missing_hashes = sorted(EXPECTED_HASH_PATHS - seen_paths)
    hash_problems += [f"Missing required frozen hash: {rel}." for rel in missing_hashes]
    if len(verified) != 1:
        hash_problems.append(f"Found {len(verified)} final unchanged-verification records; expected 1.")
    for line_number, timestamp, count in verified:
        if count != len(EXPECTED_HASH_PATHS):
            hash_problems.append(f"Line {line_number}: verification must state ({len(EXPECTED_HASH_PATHS)} files).")
        verification_time = parse_utc(timestamp)
        if verification_time is None:
            hash_problems.append(f"Line {line_number}: invalid verification datetime.")
        elif event_times and verification_time < max(event_times):
            hash_problems.append(f"Line {line_number}: verification time precedes a page event or the freeze time.")
        preceding = frozen_lines + page_event_lines + [line for line, _, _ in hashes]
        if preceding and line_number <= max(preceding):
            hash_problems.append(f"Line {line_number}: verification must follow the freeze, all hashes, and all done/audit records.")
    report.add("frozen_hashes", not hash_problems,
               f"Checked one freeze marker, {len(hashes)} recorded hashes, coverage of all 25 transcription files, "
               "and the final unchanged-verification record.", hash_problems)


def validate(output_dir: Path, source_dir: Path) -> Report:
    root, source = output_dir.resolve(), source_dir.resolve()
    report = Report(root, source)
    if not root.is_dir() or not source.is_dir():
        report.add("directories", False, "Output directory and source texts directory must both exist.")
        return report
    pages = check_package(root, report)
    check_transcription(root, pages, report, source)
    check_tables(root, source, report)
    check_progress(root, report)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("source_texts_dir", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit the complete report as JSON to stdout.")
    parser.add_argument("--verbose", action="store_true", help="Also show successful checks in text mode.")
    args = parser.parse_args(argv)
    report = validate(args.output_dir, args.source_texts_dir)
    if args.json:
        print(json.dumps(report.payload(), ensure_ascii=False, indent=2))
    else:
        counts = Counter(c.status for c in report.checks)
        print(f"{'PASS' if report.ok else 'FAIL'}: {counts['pass']} passed, {counts['fail']} failed, "
              f"{counts['warning']} warnings; expected 24 pages.")
        for check in report.checks:
            if args.verbose or check.status != "pass":
                print(f"[{check.status.upper()}] {check.name}: {check.message}")
                details = check.details if args.verbose else check.details[:10]
                for detail in details:
                    print(f"  - {detail}")
                if len(details) < len(check.details):
                    print(f"  - {len(check.details) - len(details)} further details; use --verbose or --json.")
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
