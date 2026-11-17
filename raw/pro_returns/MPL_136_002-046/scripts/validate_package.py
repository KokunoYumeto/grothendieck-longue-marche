#!/usr/bin/env python3
"""Read-only structural checks for MPL_136_002-046.

This does not assess readings, completeness against images, or mathematics.
It never opens scans or the context archive and never changes deliverables.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import sys


PACKAGE = "MPL_136_002-046"
COTE = "136"
SCANS = tuple(n for n in range(2, 47) if n != 19)
HEADER = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
EDITORIAL_MACROS = {
    "cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
    "uline", "uuline", "diagram", "figure", "unsure", "illegible",
}
# An intentionally non-exhaustive recognition list. Unknown commands are
# reported for human review, never automatically rejected or substituted.
KNOWN_COMMANDS = set("""
begin end text textnormal textrm textsf texttt textbf textit textsl textsc emph
mathrm mathit mathsf mathtt mathbf mathcal mathfrak mathbb mathscr mathrm
boxed fbox mathbin natural sharp textcircled textsuperscript varinjlim varprojlim
operatorname DeclareMathOperator frac dfrac tfrac binom dbinom tbinom sqrt
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
overline underline widehat widetilde hat tilde bar vec dot ddot dddot acute
grave breve check ring mathring overset underset stackrel overbrace underbrace
overrightarrow overleftarrow underrightarrow underleftarrow phantom hphantom
vphantom smash strut mathstrut raisebox rule hspace vspace quad qquad
qquad thinspace medspace thickspace negthinspace kern mkern hfill vfill
smallskip medskip bigskip noindent indent par newline linebreak pagebreak
newpage clearpage ensuremath displaystyle textstyle scriptstyle scriptscriptstyle
limits nolimits substack displaylimits bmod pmod mod pod
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau
upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma
Upsilon Phi Psi Omega digamma
aleph beth gimel daleth ell hbar imath jmath wp Re Im partial nabla infty
emptyset varnothing forall exists nexists neg lnot land lor wedge vee
bigwedge bigvee cap cup bigcap bigcup uplus biguplus sqcap sqcup bigsqcup
setminus smallsetminus complement subset supset subseteq supseteq subsetneq
supsetneq subsetneqq supsetneqq nsubseteq nsupseteq Subset Supset sqsubset
sqsupset sqsubseteq sqsupseteq in ni notin owns
le leq leqq ge geq geqq neq ne equiv sim simeq cong approx asymp propto
ll gg lesssim gtrsim lessgtr gtrless doteq triangleq prec succ preceq succeq
precsim succsim nleq ngeq nsim ncong not
times cdot ast star circ bullet odot oplus ominus otimes oslash bigodot
bigoplus bigotimes pm mp div amalg wr diamond triangle triangleleft
triangleright lhd rhd unlhd unrhd top bot perp parallel mid nmid nparallel
vdash dashv models Vdash vDash Vvdash
sum prod coprod int iint iiint iiiint oint smallint
to gets mapsto longmapsto rightarrow leftarrow leftrightarrow Rightarrow
Leftarrow Leftrightarrow longrightarrow longleftarrow longleftrightarrow
Longrightarrow Longleftarrow Longleftrightarrow hookrightarrow hookleftarrow
twoheadrightarrow twoheadleftarrow rightrightarrows leftleftarrows
rightleftarrows leftrightarrows rightleftharpoons leftrightharpoons
rightharpoonup rightharpoondown leftharpoonup leftharpoondown
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow nearrow searrow
swarrow nwarrow leadsto rightsquigarrow multimap xrightarrow xleftarrow
longrightsquigarrow dashrightarrow dashleftarrow
ldots cdots vdots ddots dots dotsc dotsb dotsm dotsi dotso colon
langle rangle lbrace rbrace lvert rvert lVert rVert vert Vert lceil rceil
lfloor rfloor backslash slash prime backprime surd angle measuredangle
sphericalangle triangle square Box Diamond checkmark
ar arrow harpoonarrow looparrowleft looparrowright curvearrowleft
curvearrowright circlearrowleft circlearrowright
draw path node coordinate fill filldraw clip foreach scope tikz
matrix multicolumn multirow hline cline cr crcr omit span vline tabularnewline
intertext shortintertext tag notag nonumber label ref eqref
rm it bf sf tt cal mit bgroup egroup relax null
log ln exp sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh coth
lim limsup liminf sup inf max min det gcd hom ker dim deg Pr arg
oplus otimes
ss ae AE oe OE o O aa AA l L i j c v H u t r b d
textbackslash textasciitilde textasciicircum textquotedblleft textquotedblright
textquoteleft textquoteright guillemotleft guillemotright
""".split())
FORBIDDEN_FRAGMENT_COMMANDS = {"documentclass", "usepackage", "RequirePackage"}


def page_name(scan: int) -> str:
    return f"{PACKAGE}_{COTE}_scan{scan:03d}.tex"


def strip_comments(text: str) -> str:
    """Remove unescaped TeX comments while preserving line numbering."""
    result = []
    for line in text.splitlines(keepends=True):
        cut = None
        for idx, char in enumerate(line):
            if char != "%":
                continue
            preceding = 0
            pos = idx - 1
            while pos >= 0 and line[pos] == "\\":
                preceding += 1
                pos -= 1
            if preceding % 2 == 0:
                cut = idx
                break
        if cut is None:
            result.append(line)
        else:
            result.append(line[:cut] + ("\n" if line.endswith("\n") else ""))
    return "".join(result)


def tex_structure(text: str) -> tuple[Counter, list[str]]:
    """Basic token/group/environment checks; not a full TeX parser."""
    clean = strip_comments(text)
    commands = Counter()
    problems = []
    braces = []
    environments = []
    token_re = re.compile(r"\\(?:[A-Za-z@]+|[^\r\n])|[{}]")
    for match in token_re.finditer(clean):
        token = match.group()
        line = clean.count("\n", 0, match.start()) + 1
        if token.startswith("\\"):
            command = token[1:]
            if command.isalpha() or "@" in command:
                commands[command] += 1
        elif token == "{":
            braces.append(line)
        elif braces:
            braces.pop()
        else:
            problems.append(f"unmatched closing brace on line {line}")
    if braces:
        problems.append("unclosed brace(s) opened on line(s) " + ", ".join(map(str, braces)))
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
        direction, name = match.groups()
        line = clean.count("\n", 0, match.start()) + 1
        if direction == "begin":
            environments.append((name, line))
        elif not environments:
            problems.append(f"unmatched end of environment {name!r} on line {line}")
        elif environments[-1][0] != name:
            expected = environments[-1][0]
            problems.append(f"environment {name!r} closes {expected!r} on line {line}")
        else:
            environments.pop()
    for name, line in environments:
        problems.append(f"unclosed environment {name!r} opened on line {line}")
    return commands, problems


class Validator:
    def __init__(self, root: Path, final: bool, check_log: bool):
        self.root = root
        self.final = final
        self.check_log = check_log or final
        self.issues = []
        self.commands = Counter()
        self.page_bytes = {}
        self.metrics = {}

    def issue(self, severity: str, code: str, message: str):
        self.issues.append({"severity": severity, "code": code, "message": message})

    def missing(self, code: str, message: str):
        self.issue("error" if self.final else "warning", code, message)

    def read_utf8(self, path: Path) -> tuple[bytes, str] | None:
        try:
            content = path.read_bytes()
            return content, content.decode("utf-8")
        except (OSError, UnicodeError) as exc:
            self.issue("error", "read", f"{path.name}: {exc}")
            return None

    def validate_pages(self):
        expected_names = {page_name(scan) for scan in SCANS}
        pages_dir = self.root / "pages"
        actual_names = {p.name for p in pages_dir.glob("*.tex")} if pages_dir.is_dir() else set()
        extras = sorted(actual_names - expected_names)
        if extras:
            self.issue("error", "unexpected_pages", f"Unexpected page files: {', '.join(extras)}")
        absent = []
        for scan in SCANS:
            path = pages_dir / page_name(scan)
            if not path.is_file():
                absent.append(f"{scan:03d}")
                continue
            loaded = self.read_utf8(path)
            if loaded is None:
                continue
            content, text = loaded
            self.page_bytes[scan] = content
            clean = strip_comments(text)
            scans = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
            if len(scans) != 1 or int(scans[0]) != scan:
                self.issue("error", "scanpage", f"{path.name}: expected exactly one scanpage{{{scan}}} marker; found {scans}")
            cote_markers = re.findall(r"\\cotefile\s*\{\s*([^{}]+)\s*\}", clean)
            if scan == 2:
                if cote_markers != [COTE]:
                    self.issue("error", "cotefile", f"{path.name}: expected exactly one cotefile{{136}} marker")
                if not re.match(r"\s*\\cotefile\s*\{136\}\s*\\scanpage\s*\{0*2\}", clean):
                    self.issue("error", "first_marker", f"{path.name}: first content must be cotefile{{136}} followed by scanpage{{2}}")
            elif cote_markers:
                self.issue("error", "cotefile", f"{path.name}: repeated cotefile marker")
            counts, problems = tex_structure(text)
            self.commands.update(counts)
            for problem in problems:
                self.issue("error", "tex_structure", f"{path.name}: {problem}")
            for command in sorted(FORBIDDEN_FRAGMENT_COMMANDS.intersection(counts)):
                self.issue("error", "fragment", f"{path.name}: preamble command \\{command} is not permitted in the fragment")
            if re.search(r"\\(?:begin|end)\s*\{document\}", clean):
                self.issue("error", "fragment", f"{path.name}: document environment is not permitted in the fragment")
        if absent:
            self.missing("missing_pages", "Missing scans: " + ", ".join(absent))
        self.metrics["expected_pages"] = len(SCANS)
        self.metrics["readable_pages"] = len(self.page_bytes)
        existing = sorted(self.page_bytes)
        if existing and existing != list(SCANS[:len(existing)]):
            self.issue("warning", "page_order", "Existing pages are not a continuous prefix of the prescribed scan order")

    def validate_combined(self):
        path = self.root / f"{PACKAGE}_transcription.tex"
        if not path.is_file():
            self.missing("combined_missing", f"Missing {path.name}")
            return
        loaded = self.read_utf8(path)
        if loaded is None:
            return
        content, _ = loaded
        expected = b"".join(self.page_bytes[scan] for scan in SCANS if scan in self.page_bytes)
        if content != expected:
            self.issue("error", "combined_mismatch", f"{path.name} differs from the byte-for-byte concatenation of existing pages in scan order")
        else:
            self.metrics["combined_matches_pages"] = True

    def validate_inventory(self):
        path = self.root / f"{PACKAGE}_inventory.csv"
        if not path.is_file():
            self.missing("inventory_missing", f"Missing {path.name}")
            return
        loaded = self.read_utf8(path)
        if loaded is None:
            return
        _, text = loaded
        try:
            reader = csv.DictReader(io.StringIO(text.lstrip("\ufeff"), newline=""))
            if reader.fieldnames != HEADER:
                self.issue("error", "inventory_header", f"Inventory header must be exactly {','.join(HEADER)}")
                return
            coverage = Counter()
            elements = set()
            rows = 0
            for row_number, row in enumerate(reader, start=2):
                rows += 1
                if None in row or any(value is None for value in row.values()):
                    self.issue("error", "inventory_columns", f"Inventory row {row_number}: wrong number of fields")
                    continue
                if row["cote"] != COTE:
                    self.issue("error", "inventory_cote", f"Inventory row {row_number}: cote must be 136")
                try:
                    scan = int(row["scan"])
                except ValueError:
                    self.issue("error", "inventory_scan", f"Inventory row {row_number}: scan is not an integer")
                    continue
                if scan not in SCANS:
                    self.issue("error", "inventory_scan", f"Inventory row {row_number}: unexpected scan {scan}")
                coverage[scan] += 1
                if row["sheet_kind"] not in SHEET_KINDS:
                    self.issue("error", "inventory_sheet_kind", f"Inventory row {row_number}: invalid sheet_kind")
                if row["kind"] not in ELEMENT_KINDS:
                    self.issue("error", "inventory_kind", f"Inventory row {row_number}: invalid kind")
                if row["transcribed"] != "yes":
                    self.issue("error", "inventory_unfinished", f"Inventory row {row_number}: transcribed must equal yes")
                for field in ("element", "position"):
                    if not row[field].strip():
                        self.issue("error", "inventory_empty", f"Inventory row {row_number}: empty {field}")
                key = (row["cote"], scan, row["element"])
                if key in elements:
                    self.issue("warning", "inventory_duplicate_element", f"Inventory row {row_number}: repeated element identifier on scan {scan:03d}")
                elements.add(key)
            target_scans = SCANS if self.final else tuple(self.page_bytes)
            absent = [f"{scan:03d}" for scan in target_scans if not coverage[scan]]
            if absent:
                self.missing("inventory_coverage", "Inventory has no rows for scans: " + ", ".join(absent))
            self.metrics["inventory_rows"] = rows
            self.metrics["inventoried_pages"] = len(set(coverage).intersection(SCANS))
        except csv.Error as exc:
            self.issue("error", "inventory_csv", f"Cannot parse inventory: {exc}")

    def validate_other_files(self):
        for suffix in ("doubts.md", "notes.md"):
            path = self.root / f"{PACKAGE}_{suffix}"
            if not path.is_file():
                self.missing("deliverable_missing", f"Missing {path.name}")
            elif path.stat().st_size == 0:
                self.missing("deliverable_empty", f"Empty {path.name}")

    def validate_progress(self):
        path = self.root / "progress.log"
        if not path.is_file():
            self.missing("progress_missing", "Missing progress.log")
            return
        if not self.check_log:
            return
        loaded = self.read_utf8(path)
        if loaded is None:
            return
        _, text = loaded
        lines = text.splitlines()
        timestamp = r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?: UTC|Z|[+-]\d{2}:?\d{2})"
        if not lines or not re.fullmatch(timestamp, lines[0].strip()):
            self.issue("error", "progress_start", "First progress.log line must contain the starting UTC timestamp only")
        done = Counter(int(m.group(1)) for m in re.finditer(r"(?m)^136 scan (\d+) done\s+", text))
        audited = Counter(int(m.group(1)) for m in re.finditer(r"(?m)^scan (\d+) audited\s+", text))
        for label, values in (("done", done), ("audited", audited)):
            targets = SCANS if self.final else tuple(self.page_bytes)
            missing = [f"{scan:03d}" for scan in targets if not values[scan]]
            if missing:
                self.missing(f"progress_{label}", f"Missing {label} records for scans: " + ", ".join(missing))
            extras = sorted(set(values) - set(SCANS))
            if extras:
                self.issue("error", f"progress_{label}_unexpected", f"Unexpected scans in {label} records: {extras}")
        freezes = [i for i, line in enumerate(lines) if line.startswith("transcription frozen ")]
        contexts = [i for i, line in enumerate(lines) if line.startswith("context opened ")]
        if not freezes:
            self.missing("freeze_missing", "No transcription frozen record")
        if contexts and (not freezes or min(contexts) <= min(freezes)):
            self.issue("error", "context_order", "context opened record precedes transcription frozen record")
        if self.final and not contexts:
            self.issue("error", "context_missing", "No context opened record")
        for line_number, line in enumerate(lines, start=1):
            if re.match(r"(?:136 scan \d+ done|scan \d+ audited|transcription frozen|context opened) ", line):
                if not re.search(timestamp + r"\s*$", line):
                    self.issue("error", "progress_timestamp", f"Progress record on line {line_number} lacks a recognized UTC timestamp")
        if freezes:
            # The last hash for each file before the first context-open record
            # is the frozen reference. Hash records may precede or immediately
            # follow the freeze label; interim, later verification records do
            # not replace the frozen values once context has been opened.
            cutoff = min(contexts) if contexts else len(lines)
            candidates = {}
            expected = {page_name(scan): self.root / "pages" / page_name(scan) for scan in SCANS}
            expected[f"{PACKAGE}_transcription.tex"] = self.root / f"{PACKAGE}_transcription.tex"
            for line in lines[:cutoff]:
                hashes = re.findall(r"(?<![0-9A-Fa-f])[0-9A-Fa-f]{64}(?![0-9A-Fa-f])", line)
                if len(hashes) != 1:
                    continue
                for name in expected:
                    if re.search(r"(?<![A-Za-z0-9_.-])" + re.escape(name) + r"(?![A-Za-z0-9_.-])", line):
                        candidates[name] = hashes[0].lower()
            checked = 0
            for name, source in expected.items():
                if name not in candidates:
                    self.missing("hash_missing", f"No frozen SHA-256 record for {name}")
                elif not source.is_file():
                    self.missing("hash_file_missing", f"Cannot verify SHA-256: missing {name}")
                else:
                    actual = hashlib.sha256(source.read_bytes()).hexdigest()
                    if actual != candidates[name]:
                        self.issue("error", "frozen_hash_changed", f"Frozen SHA-256 mismatch: {name}")
                    else:
                        checked += 1
            self.metrics["frozen_hashes_verified"] = checked
        self.metrics["done_records"] = len(set(done).intersection(SCANS))
        self.metrics["audit_records"] = len(set(audited).intersection(SCANS))

    def run(self):
        self.validate_pages()
        self.validate_combined()
        self.validate_inventory()
        self.validate_other_files()
        self.validate_progress()
        unknown = {name: count for name, count in self.commands.items()
                   if name not in EDITORIAL_MACROS | KNOWN_COMMANDS | FORBIDDEN_FRAGMENT_COMMANDS}
        if unknown:
            self.issue("warning", "macro_review", "Unclassified commands require human review: " + ", ".join("\\" + name for name in sorted(unknown)))
        return {
            "package": PACKAGE,
            "mode": "final" if self.final else "provisional",
            "root": str(self.root),
            "scope": "Read-only structural checks; no image comparison, OCR, mathematical checking, or assessment of reading accuracy.",
            "metrics": self.metrics,
            "editorial_macros": dict(sorted((name, count) for name, count in self.commands.items() if name in EDITORIAL_MACROS)),
            "recognized_commands": dict(sorted((name, count) for name, count in self.commands.items() if name in KNOWN_COMMANDS)),
            "unclassified_commands": dict(sorted(unknown.items())),
            "issues": self.issues,
            "passed": not any(issue["severity"] == "error" for issue in self.issues),
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1], help="Package directory (default: parent of scripts/)")
    parser.add_argument("--final", action="store_true", help="Require all deliverables, 44 pages, audits, freeze records, and frozen hashes")
    parser.add_argument("--check-log", action="store_true", help="Check progress records and available frozen hashes before final completion")
    parser.add_argument("--json", action="store_true", help="Print the report as JSON to stdout")
    args = parser.parse_args()
    report = Validator(args.root.resolve(), args.final, args.check_log).run()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"{PACKAGE}: {report['mode']} structural validation")
        print(report["scope"])
        for name, value in report["metrics"].items():
            print(f"{name}: {value}")
        print("Editorial macro occurrences: " + ", ".join(f"\\{name}={count}" for name, count in report["editorial_macros"].items()))
        print("Unclassified commands: " + (", ".join(f"\\{name}={count}" for name, count in report["unclassified_commands"].items()) or "none"))
        for issue in report["issues"]:
            print(f"{issue['severity'].upper()} [{issue['code']}]: {issue['message']}")
        errors = sum(issue["severity"] == "error" for issue in report["issues"])
        warnings = sum(issue["severity"] == "warning" for issue in report["issues"])
        print(f"Result: {errors} error(s), {warnings} warning(s)")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
