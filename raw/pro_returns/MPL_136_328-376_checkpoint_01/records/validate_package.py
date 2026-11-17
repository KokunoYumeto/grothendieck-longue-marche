#!/usr/bin/env python3
"""Read-only structural checks for the MPL_136_328-376 deliverable.

This program does not inspect images, use OCR, interpret mathematics, or judge
transcription completeness against a source.  It reads only the package's text
deliverables and, if supplied, a SHA-256 manifest.

Run from any directory:
    python records/validate_package.py              # partial package
    python records/validate_package.py --final      # all required deliverables
    python records/validate_package.py --manifest SHA256SUMS --final

The combined transcription must be the exact byte concatenation, in scan order,
of the individual page files.  Each page file should therefore end in a newline.
Hashes may be recorded in progress.log as, for example:
    sha256 pages/MPL_136_328-376_136_scan328.tex <64 hex digits>
or as ordinary sha256sum lines.  An explicit manifest can be a sha256sum-style
text file or a JSON object mapping relative filenames to hexadecimal hashes.
Only files under the package root are accepted as manifest targets.

Exit status: 0 = no structural errors; 1 = errors; 2 = usage/input exception.
Unknown LaTeX commands are informational, never grounds for a failed check.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path


PREFIX = "MPL_136_328-376"
COTE = "136"
EXPECTED = tuple(n for n in range(328, 377) if n not in {344, 347, 354, 356})
EXPECTED_SET = set(EXPECTED)
PAGE_RE = re.compile(r"MPL_136_328-376_136_scan(\d{3})\.tex\Z")
COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
STATE_COMMANDS = {
    "cotefile", "scanpage", "mspage", "deleted", "inserted", "margin", "uline",
    "uuline", "diagram", "figure", "unsure", "illegible",
}
# A convenience list, not an assertion that every other command is nonstandard.
COMMON_COMMANDS = set("""
begin end text textrm textsf texttt textbf textit textsl textsc emph mbox hbox vbox
mathrm mathit mathsf mathtt mathbf mathcal mathfrak mathbb mathscr boldsymbol bm
operatorname mathop mathrel mathbin mathord mathopen mathclose mathpunct mathinner
limits nolimits displaystyle textstyle scriptstyle scriptscriptstyle
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon phi
varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
digamma varkappa partial nabla ell hbar imath jmath wp Re Im aleph beth gimel daleth
emptyset varnothing infty top bot angle triangle square Box Diamond diamond
forall exists nexists neg lnot land lor wedge vee bigwedge bigvee cap cup
bigcap bigcup setminus smallsetminus complement in ni notin owns subset supset
subseteq supseteq nsubseteq nsupseteq subsetneq supsetneq sqsubset sqsupset
sqsubseteq sqsupseteq prec succ preceq succeq sim simeq approx approxeq asymp
cong equiv ne neq le leq ge geq ll gg lesssim gtrsim propto parallel perp mid
nmid nparallel models vdash dashv Vdash vDash Vvdash nvdash nvDash
pm mp times div cdot bullet ast star circ oplus ominus otimes oslash odot
bigoplus bigotimes bigodot amalg uplus biguplus wr triangleleft triangleright
unlhd unrhd lhd rhd diamond bigtriangleup bigtriangledown bowtie dotplus
sum prod coprod int iint iiint oint lim limsup liminf inf sup max min det dim
ker hom Hom coker Coker End Aut Ext Tor Spec Proj ord deg gcd Pr arg log ln
exp sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh coth mod bmod pmod
frac dfrac tfrac binom dbinom tbinom sqrt over choose atop genfrac
hat widehat tilde widetilde bar overline underline vec dot ddot dddot ddddot
breve check acute grave mathring overbrace underbrace overset underset stackrel
overrightarrow overleftarrow underrightarrow underleftarrow overleftrightarrow
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
langle rangle lceil rceil lfloor rfloor lvert rvert lVert rVert vert Vert
backslash lbrace rbrace braces colon ratio prime backprime dots ldots cdots
vdots ddots dotsb dotsc dotsm dotso dotsi 
to gets mapsto longmapsto hookrightarrow hookleftarrow rightarrow leftarrow
leftrightarrow Rightarrow Leftarrow Leftrightarrow longrightarrow longleftarrow
longleftrightarrow Longrightarrow Longleftarrow Longleftrightarrow
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow nearrow searrow
swarrow nwarrow twoheadrightarrow twoheadleftarrow rightleftarrows leftrightarrows
rightrightarrows leftleftarrows rightleftharpoons leftrightharpoons
rightharpoonup rightharpoondown leftharpoonup leftharpoondown rightsquigarrow
leadsto multimap curvearrowleft curvearrowright circlearrowleft circlearrowright
dashrightarrow dashleftarrow xrightarrow xleftarrow xmapsto xRightarrow
id identity nolimits not mkern kern hspace vspace hfill vfill quad qquad
qquad thinspace medspace thickspace negthinspace enspace enskip nobreak
phantom hphantom vphantom smash strut mathstrut raisebox rule color textcolor
small tiny scriptsize footnotesize normalsize large Large LARGE huge Huge
par noindent indent newline linebreak pagebreak newpage clearpage
label ref eqref tag notag nonumber numberwithin substack shortstack
multicolumn multirow cline hline arraystretch tabcolsep displaybreak allowbreak
arrow ar draw path node coordinate fill filldraw clip foreach pgfextra
tikzset tikzcdset pgfmathsetmacro pgfmathparse
LaTeX TeX dag ddag S P copyright pounds euro dotsc
""".split())
KNOWN_COMMANDS = STATE_COMMANDS | COMMON_COMMANDS


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.information: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def info(self, message: str) -> None:
        self.information.append(message)

    def emit(self) -> int:
        for label, messages in (("ERROR", self.errors), ("WARNING", self.warnings),
                                ("INFO", self.information)):
            for message in messages:
                print(f"{label}: {message}")
        print(f"RESULT: {len(self.errors)} error(s), {len(self.warnings)} warning(s).")
        print("Scope: mechanical structure only; no visual or mathematical certification.")
        return int(bool(self.errors))


def escaped(text: str, position: int) -> bool:
    backslashes = 0
    position -= 1
    while position >= 0 and text[position] == "\\":
        backslashes += 1
        position -= 1
    return bool(backslashes % 2)


def without_comments(text: str) -> str:
    """Replace TeX comments with spaces while preserving offsets and newlines."""
    chars = list(text)
    comment = False
    for i, char in enumerate(text):
        if char == "\n":
            comment = False
        elif comment:
            chars[i] = " "
        elif char == "%" and not escaped(text, i):
            chars[i] = " "
            comment = True
    return "".join(chars)


def check_tex(path: Path, report: Report) -> tuple[str, set[str]]:
    text = path.read_text(encoding="utf-8")
    clean = without_comments(text)
    openings: list[int] = []
    for i, char in enumerate(clean):
        if char not in "{}" or escaped(clean, i):
            continue
        if char == "{":
            openings.append(i)
        elif openings:
            openings.pop()
        else:
            report.error(f"{path.name}:{clean.count(chr(10), 0, i) + 1}: unmatched closing brace")
    for i in openings:
        report.error(f"{path.name}:{clean.count(chr(10), 0, i) + 1}: unmatched opening brace")
    if re.search(r"\\documentclass\b|\\(?:begin|end)\s*\{document\}", clean):
        report.error(f"{path.name}: preamble/document wrapper in a required fragment")
    environments: list[tuple[str, int]] = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
        action, name = match.group(1, 2)
        if action == "begin":
            environments.append((name, match.start()))
        elif not environments or environments[-1][0] != name:
            report.error(f"{path.name}: unmatched or misnested end of {name}")
        else:
            environments.pop()
    for name, _ in environments:
        report.error(f"{path.name}: unclosed environment {name}")
    commands = {match.group(1) for match in re.finditer(r"\\([A-Za-z@]+)", clean)
                if not escaped(clean, match.start())}
    return clean, commands - KNOWN_COMMANDS


def collect_hashes(lines: list[str], source: str, report: Report) -> dict[str, str]:
    result: dict[str, str] = {}
    # A relative or absolute filename containing no whitespace, optionally quoted.
    filename = re.compile(r"(?:[A-Za-z]:)?[^\s`\"'<>:=]*\.tex\b")
    for line_number, line in enumerate(lines, 1):
        hashes = re.findall(r"\b[0-9a-fA-F]{64}\b", line)
        names = filename.findall(line)
        if not hashes:
            continue
        if len(hashes) != 1 or len(names) != 1:
            report.warn(f"{source}:{line_number}: could not associate SHA-256 with one .tex filename")
            continue
        name = names[0].lstrip("*")
        digest = hashes[0].lower()
        if name in result and result[name] != digest:
            report.error(f"{source}: conflicting recorded hashes for {name}")
        result[name] = digest
    return result


def validate_hashes(root: Path, recorded: dict[str, str], report: Report,
                    required_paths: set[Path] | None = None) -> None:
    covered: set[Path] = set()
    for name, digest in recorded.items():
        candidate = Path(name)
        if not candidate.is_absolute():
            candidate = root / candidate
        candidate = candidate.resolve()
        if not candidate.is_relative_to(root):
            report.error(f"Hash target outside package root: {name}")
            continue
        if not candidate.is_file():
            # Bare page filenames are an unambiguous supported shorthand.
            fallback = root / "pages" / Path(name).name
            if Path(name).name == name and fallback.is_file():
                candidate = fallback.resolve()
            else:
                report.error(f"Hash target missing: {name}")
                continue
        if not re.fullmatch(r"[0-9a-fA-F]{64}", digest):
            report.error(f"Invalid SHA-256 value for {name}")
            continue
        actual = hashlib.sha256(candidate.read_bytes()).hexdigest()
        if actual != digest.lower():
            report.error(f"SHA-256 mismatch: {name}")
        covered.add(candidate)
    if recorded:
        report.info(f"Checked {len(covered)} recorded SHA-256 target(s).")
    if required_paths is not None:
        for path in sorted(required_paths - covered):
            report.error(f"Missing frozen SHA-256 record: {path.relative_to(root)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--final", action="store_true", help="require all 45 pages and final records")
    parser.add_argument("--manifest", type=Path, help="additional SHA-256 text or JSON manifest")
    args = parser.parse_args()
    root = args.root.resolve()
    report = Report()
    if not root.is_dir():
        parser.error(f"package root does not exist: {root}")

    pages: dict[int, Path] = {}
    for path in sorted((root / "pages").glob("*.tex")):
        match = PAGE_RE.fullmatch(path.name)
        if not match:
            report.error(f"Unexpected page filename: {path.name}")
            continue
        scan = int(match.group(1))
        if scan not in EXPECTED_SET:
            report.error(f"Unexpected/excluded scan: {scan}")
        if scan in pages:
            report.error(f"Duplicate page for scan {scan}")
        pages[scan] = path
    existing = set(pages)
    if args.final:
        for scan in sorted(EXPECTED_SET - existing):
            report.error(f"Missing page: scan {scan}")
    else:
        report.info(f"Partial mode: {len(existing & EXPECTED_SET)} / 45 expected page files present.")
        ordered_present = sorted(existing & EXPECTED_SET)
        if ordered_present and ordered_present != list(EXPECTED[:len(ordered_present)]):
            report.warn("Existing pages do not form the required initial sequential run.")

    unknown: dict[str, set[int]] = {}
    for scan, path in sorted(pages.items()):
        clean, commands = check_tex(path, report)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if markers != [str(scan)]:
            report.error(f"{path.name}: expected exactly one matching scanpage marker; found {markers}")
        cote_markers = re.findall(r"\\cotefile\s*\{\s*([^}]+)\s*\}", clean)
        if scan == EXPECTED[0]:
            if cote_markers != [COTE]:
                report.error(f"{path.name}: first page must contain exactly one cotefile{{136}}")
            if not re.match(r"\s*\\cotefile\s*\{136\}\s*\\scanpage\s*\{328\}", clean):
                report.error(f"{path.name}: first fragment must start with cotefile then scanpage")
        else:
            if cote_markers:
                report.error(f"{path.name}: unexpected repeated cotefile marker")
            if not re.match(rf"\s*\\scanpage\s*\{{{scan}\}}", clean):
                report.error(f"{path.name}: fragment must start with its scanpage marker")
        if not path.read_bytes().endswith(b"\n"):
            report.warn(f"{path.name}: no final newline; exact concatenation may join adjacent tokens")
        for command in commands:
            unknown.setdefault(command, set()).add(scan)
    for command, scans in sorted(unknown.items()):
        report.info(f"Command outside convenience allow-list: \\{command} (scans {', '.join(map(str, sorted(scans)))})")

    combined = root / f"{PREFIX}_transcription.tex"
    if combined.is_file():
        expected_bytes = b"".join(path.read_bytes() for _, path in sorted(pages.items()))
        if combined.read_bytes() != expected_bytes:
            report.error("Combined transcription is not the exact byte concatenation of page files in scan order.")
        check_tex(combined, report)
    elif args.final:
        report.error(f"Missing combined transcription: {combined.name}")
    else:
        report.info("Combined transcription not yet present.")

    inventory = root / f"{PREFIX}_inventory.csv"
    inventory_scans: set[int] = set()
    if not inventory.is_file():
        report.error(f"Missing inventory: {inventory.name}")
    else:
        with inventory.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != COLUMNS:
                report.error(f"Inventory columns differ from required order: {reader.fieldnames}")
            identifiers: set[tuple[int, str]] = set()
            for number, row in enumerate(reader, 2):
                where = f"{inventory.name}:{number}"
                if None in row or any(value is None for value in row.values()):
                    report.error(f"{where}: malformed CSV row")
                    continue
                if row.get("cote", "").strip() != COTE:
                    report.error(f"{where}: cote must be 136")
                try:
                    scan = int(row.get("scan", ""))
                except ValueError:
                    report.error(f"{where}: invalid scan number")
                    continue
                inventory_scans.add(scan)
                if scan not in existing:
                    report.error(f"{where}: inventory refers to an absent page ({scan})")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    report.error(f"{where}: invalid sheet_kind {row.get('sheet_kind')!r}")
                if row.get("kind") not in ELEMENT_KINDS:
                    report.error(f"{where}: invalid kind {row.get('kind')!r}")
                if row.get("transcribed") != "yes":
                    report.error(f"{where}: transcribed must be exactly 'yes'")
                element = row.get("element", "")
                if not element:
                    report.error(f"{where}: missing element identifier")
                if (scan, element) in identifiers:
                    report.error(f"{where}: duplicate element identifier for scan {scan}: {element}")
                identifiers.add((scan, element))
                for key in ("position", "first_words_or_objects"):
                    if not row.get(key, "").strip():
                        report.warn(f"{where}: empty {key}")
        for scan in sorted(existing - inventory_scans):
            report.error(f"No inventory rows for existing page {scan}")

    log = root / "progress.log"
    hashes: dict[str, str] = {}
    frozen = False
    if not log.is_file():
        report.error("Missing progress.log")
    else:
        lines = log.read_text(encoding="utf-8").splitlines()
        if not lines:
            report.error("Empty progress.log")
        else:
            try:
                datetime.strptime(lines[0], "%Y-%m-%d %H:%M:%S UTC")
            except ValueError:
                report.error("First progress.log line is not a UTC timestamp in YYYY-MM-DD HH:MM:SS UTC form.")
        done: list[int] = []
        audited: list[int] = []
        freeze_lines: list[int] = []
        context_lines: list[int] = []
        for number, line in enumerate(lines, 1):
            match = re.match(r"136 scan (\d{3}) done (.+)$", line)
            audit = re.match(r"(?:136 )?scan (\d{3}) audited (.+)$", line)
            for found, destination in ((match, done), (audit, audited)):
                if found:
                    destination.append(int(found.group(1)))
                    try:
                        datetime.strptime(found.group(2), "%Y-%m-%d %H:%M:%S UTC")
                    except ValueError:
                        report.error(f"progress.log:{number}: invalid UTC completion/audit timestamp")
            if line.startswith("transcription frozen "):
                freeze_lines.append(number)
            if line.startswith("context opened "):
                context_lines.append(number)
        if done != sorted(set(done)):
            report.error("Page 'done' records are duplicated or out of scan order.")
        for scan in sorted(existing - set(done)):
            report.error(f"Missing done record for existing page {scan}")
        for scan in sorted((set(done) | set(audited)) - existing):
            report.error(f"Progress record refers to absent page {scan}")
        for scan, count in Counter(audited).items():
            if count > 1:
                report.warn(f"Scan {scan} has {count} audit records.")
        frozen = bool(freeze_lines)
        if frozen or args.final:
            for scan in sorted(EXPECTED_SET - set(audited)):
                report.error(f"Missing audit record for scan {scan}")
        if args.final and not frozen:
            report.error("Missing 'transcription frozen <UTC time>' record.")
        if context_lines and (not freeze_lines or min(context_lines) < min(freeze_lines)):
            report.error("Context-opened record occurs before transcription-frozen record.")
        if args.final and not context_lines:
            report.error("Missing 'context opened <UTC time>' record.")
        if args.final and not re.search(r"hash(?:es)?[^\n]*(?:unchanged|unchang[eé]|verified)",
                                        "\n".join(lines), re.IGNORECASE):
            report.warn("No recognizable final statement that frozen hashes were verified unchanged.")
        hashes.update(collect_hashes(lines, "progress.log", report))

    if args.manifest:
        manifest = args.manifest if args.manifest.is_absolute() else root / args.manifest
        if manifest.suffix.lower() == ".json":
            loaded = json.loads(manifest.read_text(encoding="utf-8"))
            if not isinstance(loaded, dict) or not all(isinstance(k, str) and isinstance(v, str)
                                                     for k, v in loaded.items()):
                report.error("JSON manifest must be an object mapping filenames to hash strings.")
                loaded = {}
        else:
            loaded = collect_hashes(manifest.read_text(encoding="utf-8").splitlines(),
                                    manifest.name, report)
        for name, digest in loaded.items():
            if name in hashes and hashes[name] != digest.lower():
                report.error(f"Manifest and progress.log disagree for {name}")
            hashes[name] = digest.lower()
    required_hash_paths = None
    if args.final or frozen:
        required_hash_paths = {path.resolve() for path in pages.values()} | {combined.resolve()}
    validate_hashes(root, hashes, report, required_hash_paths)

    if args.final:
        for suffix in ("doubts.md", "notes.md"):
            path = root / f"{PREFIX}_{suffix}"
            if not path.is_file() or not path.stat().st_size:
                report.error(f"Missing or empty required deliverable: {path.name}")
        report.info(f"Final mode: {len(existing & EXPECTED_SET)} / 45 expected page files present.")
    report.info(f"Inventory covers {len(inventory_scans & EXPECTED_SET)} expected scan(s).")
    return report.emit()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, UnicodeError, csv.Error, json.JSONDecodeError) as error:
        print(f"INPUT ERROR: {error}", file=sys.stderr)
        sys.exit(2)
