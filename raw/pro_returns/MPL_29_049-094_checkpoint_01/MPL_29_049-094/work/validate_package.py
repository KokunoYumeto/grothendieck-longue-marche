#!/usr/bin/env python3
"""Read-only structural validation of the MPL_29_049-094 delivery.

This is not a reading, transcription audit, or mathematical check. It never
opens the supplied scans or context. Final validation requires every expected
page and all requested deliverables; --partial checks only work already present.

Recommended frozen-hash log syntax (standard sha256sum syntax also accepted):
    sha256 HEX_DIGEST pages/MPL_29_049-094_29_scan049.tex
    sha256 HEX_DIGEST MPL_29_049-094_transcription.tex
    transcription frozen YYYY-MM-DD HH:MM:SS UTC
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

STEM = "MPL_29_049-094"
EXPECTED = tuple(n for n in range(49, 95) if n not in (79, 80, 81, 83))
INV_COLUMNS = (
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
)
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
STATE_MACROS = {
    "cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
    "uline", "uuline", "diagram", "figure", "unsure", "illegible",
}
# Unknown commands are warnings, not failures: LaTeX and TikZ have extensive APIs.
# The compile harness is the authoritative undefined-command check.
KNOWN_COMMANDS = set("""
begin end text textrm textsf texttt textbf textit textsl textsc textnormal
emph emphnormal rm sf tt bf it sl sc normalfont rmfamily sffamily ttfamily
bfseries mdseries itshape upshape slshape scshape tiny scriptsize footnotesize
small normalsize large Large LARGE huge Huge par noindent indent newline
linebreak pagebreak newpage clearpage hfill vfill hspace vspace hskip vskip
quad qquad enspace thinspace medspace thickspace negthinspace phantom hphantom
vphantom smash rule strut mathstrut makebox mbox raisebox ensuremath
label ref eqref tag notag nonumber numberwithin
frac dfrac tfrac cfrac binom dbinom tbinom sqrt root over atop choose
sum prod coprod int iint iiint oint bigcup bigcap bigvee bigwedge bigoplus
bigotimes bigodot bigsqcup smallint limits nolimits displaylimits
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi
varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
mathbb mathcal mathscr mathfrak mathrm mathsf mathtt mathbf mathit mathnormal
boldsymbol bm operatorname operatornamewithlimits textup textmd
le leq leqslant ge geq geqslant neq ne eqsim equiv sim simeq cong approx
asymp propto doteq coloneqq eqqcolon colon subset supset subseteq supseteq
subsetneq supsetneq subsetneqq supsetneqq nsubseteq nsupseteq in ni notin
owns parallel nparallel perp mid nmid vdash dashv models prec succ preceq
succeq preccurlyeq succcurlyeq ll gg lesssim gtrsim bowtie triangleleft
triangleright unlhd unrhd sqsubset sqsupset sqsubseteq sqsupseteq
to gets mapsto longmapsto rightarrow leftarrow leftrightarrow longrightarrow
longleftarrow longleftrightarrow Rightarrow Leftarrow Leftrightarrow
Longrightarrow Longleftarrow Longleftrightarrow hookrightarrow hookleftarrow
twoheadrightarrow twoheadleftarrow rightleftarrows leftrightarrows
rightrightarrows leftleftarrows rightleftharpoons leftrightharpoons
rightarrowtail leftarrowtail looparrowright looparrowleft curvearrowright
curvearrowleft circlearrowright circlearrowleft nearrow searrow nwarrow swarrow
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow xrightarrow
xleftarrow xhookrightarrow xhookleftarrow xmapsto xleftrightarrow
dashrightarrow dashleftarrow leadsto rightsquigarrow implies impliedby iff
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
langle rangle langle rangle lbrace rbrace lbrack rbrack lceil rceil lfloor
rfloor vert Vert lvert rvert lVert rVert backslash
bar overline underline hat widehat tilde widetilde vec dot ddot dddot acute
grave breve check mathring overbrace underbrace overset underset stackrel
overrightarrow overleftarrow underrightarrow underleftarrow
pm mp times div cdot ast star circ bullet odot oplus ominus otimes oslash
cup cap sqcup sqcap vee wedge setminus smallsetminus amalg wr uplus
forall exists nexists neg lnot land lor top bot emptyset varnothing partial
nabla infinity infty ell hbar imath jmath wp Re Im aleph beth gimel daleth
angle triangle square Box Diamond diamond prime flat natural sharp dag ddag
dagger ddagger S P copyright circledcirc circledast circleddash surd
ldots cdots vdots ddots dots dotsc dotsb dotsm dotsi dotso
min max inf sup lim liminf limsup varliminf varlimsup injlim projlim
varinjlim varprojlim colim det dim ker hom Hom Pr log ln exp sin cos tan
arcsin arccos arctan sinh cosh tanh cot sec csc gcd arg deg
displaystyle textstyle scriptstyle scriptscriptstyle substack mathchoice
multicolumn multirow shortstack intertext shortintertext displaybreak
cr hline cline vline item enumerate itemize description centering center
raggedright raggedleft flushleft flushright quote quotation verb verbatim
ar arrow arrows path draw node coordinate foreach fill filldraw clip
matrix edge graph tikz tikzset pgfplotsset pgfmathsetmacro pgfmathparse
pathreplacing decoration pgfkeys foreachpgfmath
""".split()) | STATE_MACROS | {"mathbin", "boxed", "fbox", "parbox", "hrule", "medskip"}
FORBIDDEN = {
    "documentclass", "usepackage", "RequirePackage", "input", "include",
    "includegraphics", "pgfimage", "newcommand", "renewcommand", "providecommand",
    "DeclareRobustCommand", "def", "gdef", "edef", "xdef", "let", "write",
    "openout", "read", "catcode", "csname", "directlua",
}


def uncomment(text: str) -> str:
    """Strip TeX comments, preserving escaped percent signs and line numbers."""
    out = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for i, char in enumerate(line):
            if char != "%":
                continue
            j = i - 1
            while j >= 0 and line[j] == "\\":
                j -= 1
            if (i - j - 1) % 2 == 0:
                cut = i
                break
        out.append(line[:cut] + ("\n" if cut < len(line) else ""))
    return "".join(out)


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []

    def error(self, message):
        self.errors.append(message)

    def warn(self, message):
        self.warnings.append(message)


def check_tex(text: str, name: str, report: Report) -> None:
    clean = uncomment(text)
    braces = []
    for token in re.finditer(r"\\(?:[A-Za-z@]+|.)|[{}]", clean):
        value = token.group()
        line = clean.count("\n", 0, token.start()) + 1
        if value == "{":
            braces.append(line)
        elif value == "}":
            if not braces:
                report.error(f"{name}:{line}: unmatched closing brace")
            else:
                braces.pop()
    if braces:
        report.error(f"{name}: unmatched opening braces at lines {braces}")
    stack = []
    for token in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
        action, env = token.groups()
        line = clean.count("\n", 0, token.start()) + 1
        if env == "document":
            report.error(f"{name}:{line}: document environment in a fragment")
        if action == "begin":
            stack.append((env, line))
        elif not stack or stack[-1][0] != env:
            report.error(f"{name}:{line}: mismatched end of environment {env}")
        else:
            stack.pop()
    if stack:
        report.error(f"{name}: unclosed environments {stack}")
    # Lex control symbols first: in `\\\\Y`, the first two backslashes form
    # one row-break command, and Y is an ordinary letter, not a command.
    control_tokens = re.findall(r"\\(?:[A-Za-z@]+|.)", clean)
    commands = {token[1:] for token in control_tokens
                if re.fullmatch(r"\\[A-Za-z@]+", token)}
    forbidden = commands & FORBIDDEN
    if forbidden:
        report.error(f"{name}: forbidden fragment commands {sorted(forbidden)}")
    unknown = commands - KNOWN_COMMANDS - FORBIDDEN
    if unknown:
        report.warn(f"{name}: commands needing LaTeX/standard-macro confirmation: {sorted(unknown)}")
    for left, right in ((r"\[", r"\]"), (r"\(", r"\)")):
        if control_tokens.count(left) != control_tokens.count(right):
            report.error(f"{name}: unequal counts of {left} and {right}")
    dollars = re.findall(r"(?<!\\)(?:\\\\)*\$", clean)
    if len(dollars) % 2:
        report.error(f"{name}: odd number of unescaped dollar signs")
    if re.search(r"\\illegible\s*\{\s*[^0-9\s}]", clean):
        report.error(f"{name}: illegible argument is not an estimated word count")


def load_utf8(path: Path, report: Report) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeError, OSError) as exc:
        report.error(f"{path.name}: cannot read UTF-8: {exc}")
        return ""


def validate(root: Path, partial: bool) -> Report:
    r = Report()
    required = [f"{STEM}_transcription.tex", f"{STEM}_doubts.md",
                f"{STEM}_inventory.csv", f"{STEM}_notes.md", "progress.log", "CHECK_EVENTS.tsv"]
    for filename in required:
        p = root / filename
        if not p.is_file() and not partial:
            r.error(f"Missing required deliverable: {filename}")
        elif p.is_file() and p.stat().st_size == 0:
            r.warn(f"Empty deliverable: {filename}")
    pages = {}
    for p in sorted((root / "pages").glob("*.tex")):
        match = re.fullmatch(STEM + r"_29_scan(\d{3})\.tex", p.name)
        if not match:
            r.error(f"Unexpected page filename: {p.name}")
            continue
        scan = int(match.group(1))
        if scan not in EXPECTED:
            r.error(f"Unexpected scan in pages/: {scan}")
        text = load_utf8(p, r)
        pages[scan] = (p, text)
        check_tex(text, f"pages/{p.name}", r)
        scan_tags = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", uncomment(text))
        if scan_tags != [str(scan)]:
            r.error(f"{p.name}: scanpage tags {scan_tags}, expected [{scan}]")
        cote_tags = re.findall(r"\\cotefile\s*\{([^}]+)\}", uncomment(text))
        if cote_tags and (scan != 49 or cote_tags != ["29"]):
            r.error(f"{p.name}: unexpected cotefile tags {cote_tags}")
    missing = set(EXPECTED) - pages.keys()
    if missing and not partial:
        r.error(f"Missing page scans: {sorted(missing)}")
    r.info.append(f"Page files: {len(pages)}/{len(EXPECTED)}; pending: {sorted(missing)}")
    combined_path = root / f"{STEM}_transcription.tex"
    if combined_path.is_file():
        combined = load_utf8(combined_path, r)
        check_tex(combined, combined_path.name, r)
        clean = uncomment(combined).lstrip()
        if not re.match(r"\\cotefile\{29\}\s*\\scanpage\{49\}", clean):
            r.error("Combined transcription must start with cotefile{29}, then scanpage{49}")
        scans = [int(x) for x in re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)]
        target = sorted(pages) if partial else list(EXPECTED)
        if scans != target:
            r.error(f"Combined scan order differs: {scans}; expected {target}")
        merged = "\n".join(pages[n][1] for n in sorted(pages))
        def normalize(value):
            value = re.sub(r"\\cotefile\s*\{29\}", "", uncomment(value))
            return re.sub(r"\s+", " ", value).strip()
        if normalize(merged) != normalize(combined):
            r.error("Combined transcription differs from concatenated page files (ignoring comments, whitespace and cotefile tag)")
    inv_path = root / f"{STEM}_inventory.csv"
    if inv_path.is_file():
        with inv_path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if tuple(reader.fieldnames or ()) != INV_COLUMNS:
                r.error(f"Inventory columns differ: {reader.fieldnames}")
            rows = list(reader)
        counts, keys, order = Counter(), set(), []
        for line, row in enumerate(rows, 2):
            prefix = f"inventory:{line}"
            try:
                scan = int(row.get("scan", ""))
            except (TypeError, ValueError):
                r.error(f"{prefix}: invalid scan")
                continue
            order.append(scan)
            counts[scan] += 1
            if scan not in pages:
                r.error(f"{prefix}: inventory scan {scan} has no page file")
            if row.get("cote") != "29":
                r.error(f"{prefix}: cote must be 29")
            if row.get("sheet_kind") not in SHEET_KINDS:
                r.error(f"{prefix}: invalid sheet_kind {row.get('sheet_kind')!r}")
            if row.get("kind") not in KINDS:
                r.error(f"{prefix}: invalid element kind {row.get('kind')!r}")
            if row.get("transcribed") != "yes":
                r.error(f"{prefix}: transcribed is not yes")
            for col in ("element", "position", "first_words_or_objects"):
                if not str(row.get(col) or "").strip():
                    r.error(f"{prefix}: empty {col}")
            key = (scan, row.get("element"))
            if key in keys:
                r.error(f"{prefix}: repeated element identifier {key}")
            keys.add(key)
        if order != sorted(order):
            r.error("Inventory scans are not in ascending order")
        for scan in sorted(pages):
            if not counts[scan]:
                r.error(f"Scan {scan} has no inventory rows")
        r.info.append(f"Inventory: {len(rows)} rows over {len(counts)} scans")
    log_path = root / "progress.log"
    if log_path.is_file():
        log = load_utf8(log_path, r)
        lines = log.splitlines()
        if not lines or not re.fullmatch(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?: UTC|Z|\+00:00)", lines[0]):
            r.warn("First progress.log line is not a recognized UTC timestamp")
        done = Counter(int(n) for n in re.findall(r"(?m)^29 scan (\d{3}) done\b", log))
        audited = Counter(int(n) for n in re.findall(r"(?m)^scan (\d{3}) audited\b", log))
        for scan in sorted(pages):
            if not done[scan]:
                r.error(f"Scan {scan} lacks a done entry")
            if not partial and not audited[scan]:
                r.error(f"Scan {scan} lacks an audited entry")
        freeze = log.find("transcription frozen")
        context = log.find("context opened")
        if not partial and freeze < 0:
            r.error("No transcription frozen log event")
        if context >= 0 and (freeze < 0 or context < freeze):
            r.error("Context-opened event precedes transcription freeze")
        hashes = {}
        for line in lines:
            match = re.match(r"(?:sha256\s+)?([0-9a-fA-F]{64})\s+\*?(.+?)\s*$", line, re.I)
            if not match:
                match2 = re.match(r"sha256\s+(.+?)\s+([0-9a-fA-F]{64})\s*$", line, re.I)
                if match2:
                    match = (match2.group(2), match2.group(1))
            if match:
                digest, filename = match.groups() if hasattr(match, "groups") else match
                p = Path(filename)
                p = p if p.is_absolute() else root / p
                try:
                    rel = str(p.resolve().relative_to(root.resolve()))
                except ValueError:
                    r.error(f"Frozen hash points outside package: {filename}")
                    continue
                if rel in hashes and hashes[rel] != digest.lower():
                    r.error(f"Conflicting logged frozen hashes: {rel}")
                hashes[rel] = digest.lower()
                if not p.is_file():
                    r.error(f"Logged frozen file is absent: {rel}")
                elif hashlib.sha256(p.read_bytes()).hexdigest() != digest.lower():
                    r.error(f"Frozen SHA-256 mismatch: {rel}")
        required_hashes = [str(p.relative_to(root)) for p, _ in pages.values()]
        if combined_path.is_file():
            required_hashes.append(combined_path.name)
        if freeze >= 0 or not partial:
            for filename in required_hashes:
                if filename not in hashes:
                    r.error(f"Missing frozen SHA-256 record: {filename}")
        if freeze >= 0:
            before = log[:freeze]
            prior_audits = set(int(n) for n in re.findall(r"(?m)^scan (\d{3}) audited\b", before))
            for scan in sorted(pages):
                if scan not in prior_audits:
                    r.error(f"Scan {scan} was not logged audited before freeze")
        r.info.append(f"Log: {len(done)} done scans, {len(audited)} audited scans, {len(hashes)} frozen hashes")
    events_path = root / "CHECK_EVENTS.tsv"
    if events_path.is_file():
        with events_path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            fields = reader.fieldnames or []
            events = list(reader)
        normalized = [re.sub(r"[^a-z]", "", s.lower()) for s in fields]
        groups = ({"statementid", "statement"}, {"date", "dateutc"},
                  {"who", "whomodeleffortrun"}, {"type", "checktype", "eventtype"}, {"outcome"})
        if not all(set(normalized) & group for group in groups):
            r.warn(f"Check-events columns need human confirmation: {fields}")
        for line, row in enumerate(events, 2):
            if None in row or any(value is None for value in row.values()):
                r.error(f"CHECK_EVENTS.tsv:{line}: wrong number of fields")
        r.info.append(f"Check events: {len(events)} rows (event substance is not assessed)")
    return r


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--partial", action="store_true", help="allow deliverables/pages still pending")
    args = parser.parse_args()
    report = validate(args.root.resolve(), args.partial)
    for line in report.info:
        print("INFO:", line)
    for line in report.warnings:
        print("WARNING:", line)
    for line in report.errors:
        print("ERROR:", line)
    print(f"RESULT: {len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    print("LIMIT: Structural checks cannot establish visual completeness, reading accuracy, or mathematical validity.")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
