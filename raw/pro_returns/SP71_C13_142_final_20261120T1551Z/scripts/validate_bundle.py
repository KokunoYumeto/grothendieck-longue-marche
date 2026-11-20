#!/usr/bin/env python3
"""Structural validation only for SP71_C13_142; never OCR or TeX compilation.

This program does not assess manuscript readings.  It examines the deliverables'
structure, coverage, record ordering and frozen byte identities.  Its input
MARKS.tsv supplies only mark IDs, cote and scan; no source witness page is read.

Usage:
    python scripts/validate_bundle.py --mode partial
    python scripts/validate_bundle.py --mode final --archive ../SP71_C13_142.zip

Exit status: 0 = no errors or incomplete checks; 1 = errors; 2 = incomplete only.
REVIEW items are intentionally non-fatal and require human/model assessment.
The default work directory is the parent of this script's directory.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import sys
import zipfile
from collections import Counter
from datetime import datetime
from pathlib import Path, PurePosixPath


PREFIX = "SP71_C13_142"
SCANS = tuple(range(52, 65)) + tuple(range(66, 77))
PAGE_NAMES = tuple(f"142_scan{n:03d}.tex" for n in SCANS)
REQUIRED = (
    f"{PREFIX}_transcription.tex", f"{PREFIX}_changes.md",
    f"{PREFIX}_collation.tsv", "decisions.tsv", f"{PREFIX}_doubts.md",
    f"{PREFIX}_inventory.csv", f"{PREFIX}_notes.md", "CHECK_EVENTS.tsv",
    "progress.log", f"{PREFIX}_sheet_feedback.md", f"{PREFIX}_hand_log.md",
)
HEADERS = {
    f"{PREFIX}_collation.tsv": (
        "folder", "their_page", "our_scan", "line", "their_reading",
        "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H",
        "confidence",
    ),
    "decisions.tsv": (
        "id", "cote", "scan", "decision", "reading", "what the ink shows",
        "crop", "confidence",
    ),
    f"{PREFIX}_inventory.csv": (
        "scan", "sheet_kind", "hand", "element", "kind", "position",
        "first_words_or_objects", "transcribed",
    ),
}
COLLATION_KINDS = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state", "deletion state (struck given live or live given struck)",
    "insertion or placement", "abbreviation expanded or spelling modernised",
    r"readable ink left as \ill{}", r"readable ink left as `\ill{}`",
    "drawing or diagram", "other",
}
SHEET_KINDS = {
    "text", "reused_typed", "typescript", "letter", "list", "cancelled_draft",
    "cover",
}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion",
    "deletion",
}
CONFIDENCES = {"high", "medium", "low"}
EVENT_TYPES = {
    "targeted proof check", "independent re-proof", "computation or formal certificate",
    "used and rechecked in this run", "carried as background without fault found",
}
PICTURE_SUFFIXES = {
    ".jpg", ".jpeg", ".png", ".gif", ".tif", ".tiff", ".bmp", ".webp",
    ".svg", ".pdf", ".heic", ".heif", ".avif", ".jpe", ".jfif", ".jp2",
    ".j2k", ".jxl", ".ps", ".eps", ".ppm", ".pgm", ".pbm", ".pnm", ".ico",
    ".raw", ".dng", ".psd", ".xcf",
}
# Conservative list: unknown commands generate REVIEW, never a false assertion
# that a custom macro is valid.  Control-symbol commands (e.g. \{, \\, \!)
# are standard lexical forms and are not matched by the word-command regex.
STANDARD_COMMANDS = set("""
begin end par noindent indent newline linebreak pagebreak newpage clearpage
medskip smallskip bigskip quad qquad enspace thinspace negthinspace hfill vfill
hspace vspace kern hbox mbox makebox raisebox rule phantom hphantom vphantom
text textnormal textrm textsf texttt textit textsl textsc textbf emph normalfont
textsuperscript textsuperscript textsubscript tiny scriptsize footnotesize small
normalsize large Large LARGE huge Huge centering raggedright raggedleft
item label ref eqref pageref tag notag nonumber footnote footnotemark footnotetext
marginpar multicolumn multirow substack overset underset stackrel atop choose
frac dfrac tfrac binom dbinom tbinom sqrt left right middle big Big bigg Bigg
bigl bigr Bigl Bigr biggl biggr Biggl Biggr operatorname mathop mathbin mathrel
mathord mathopen mathclose mathpunct limits nolimits displaylimits
displaystyle textstyle scriptstyle scriptscriptstyle
mathrm mathsf mathtt mathit mathbf mathcal mathscr mathbb boldsymbol pmb
underline overline widehat widetilde hat tilde bar vec dot ddot dddot ddddot
acute grave breve check mathring overbrace underbrace overrightarrow
overleftarrow overleftrightarrow underrightarrow underleftarrow
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon
phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
aleph beth gimel daleth hbar hslash ell wp Re Im imath jmath partial nabla
infty emptyset varnothing forall exists nexists neg lnot top bot angle triangle
square Box Diamond diamond lozenge blacksquare blacktriangle blacktriangledown
prime backprime degree surd complement
sum prod coprod int iint iiint iiiint oint bigcap bigcup bigsqcup bigvee bigwedge
bigodot bigotimes bigoplus biguplus lim limsup liminf sup inf max min det dim
ker hom gcd deg Pr log ln exp sin cos tan cot sec csc arcsin arccos arctan
sinh cosh tanh coth arg bmod pmod mod pod
cdot cdots ldots dots vdots ddots times div pm mp ast star circ bullet odot
otimes oplus ominus oslash cap cup sqcap sqcup uplus vee wedge setminus
smallsetminus amalg wr land lor dagger ddagger dag ddag
le leq leqslant ge geq geqslant ne neq eq equiv sim simeq cong approx asymp
propto doteq dotplus lesssim gtrsim ll gg prec succ preceq succeq preccurlyeq
succcurlyeq nleq ngeq nless ngtr nsim ncong triangleq coloneqq eqcolon
in ni notin owns subset supset subseteq supseteq subsetneq supsetneq
subsetneqq supsetneqq nsubseteq nsupseteq sqsubset sqsupset sqsubseteq
sqsupseteq parallel nparallel perp mid nmid vdash dashv models Vdash Vvdash
dashrightarrow dashleftarrow to gets mapsto longmapsto hookrightarrow
hookleftarrow rightarrow leftarrow leftrightarrow Rightarrow Leftarrow
Leftrightarrow longrightarrow longleftarrow longleftrightarrow Longrightarrow
Longleftarrow Longleftrightarrow iff implies impliedby
rightarrowtail leftarrowtail twoheadrightarrow twoheadleftarrow
leftharpoonup leftharpoondown rightharpoonup rightharpoondown rightleftarrows
leftrightarrows rightleftharpoons leftrightharpoons curvearrowright
curvearrowleft circlearrowright circlearrowleft updownarrow uparrow downarrow
Uparrow Downarrow Updownarrow nearrow searrow swarrow nwarrow
xrightarrow xleftarrow
langle rangle lbrace rbrace lvert rvert lVert rVert vert Vert lfloor rfloor
lceil rceil backslash colon
uline uuline uwave ulem sout xout dashuline dotuline color textcolor
tikz tikzset node draw path fill filldraw clip coordinate matrix foreach
scope endscope pgfmathsetmacro pgfmathtruncatemacro pgfmathparse pgfmathresult
pgfextra arrow arrowext ar
pgfsetlinewidth pgfsetroundcap pgfsetroundjoin
useasboundingbox addplot plot cycle
TeX LaTeX copyright textbackslash textbar textasciitilde textasciicircum
textless textgreater textendash textemdash textquoteleft textquoteright
textquotedblleft textquotedblright guillemotleft guillemotright
ae AE oe OE aa AA o O l L ss i j c v u H k b d r t
protect relax unskip null strut mathstrut ensuremath
""".split())
KNOWN_WRAPPERS = {
    "cotefile", "scanpage", "mspage", "unsure", "illegible", "handwritten",
    "deleted", "inserted", "margin", "diagram", "figure",
}
FORBIDDEN_FRAGMENT_COMMANDS = {
    "documentclass", "usepackage", "newcommand", "renewcommand", "providecommand",
    "def", "gdef", "edef", "xdef", "input", "include", "includegraphics",
    "write", "openout", "read", "csname", "endcsname",
}


class Report:
    def __init__(self, mode: str):
        self.mode = mode
        self.items: list[tuple[str, str]] = []

    def add(self, level: str, message: str):
        self.items.append((level, message))

    def missing(self, message: str):
        self.add("ERROR" if self.mode == "final" else "INCOMPLETE", message)

    def finish(self) -> int:
        for level, message in self.items:
            print(f"{level}: {message}")
        counts = Counter(level for level, _ in self.items)
        print("SUMMARY: " + ", ".join(f"{x}={counts[x]}" for x in
              ("OK", "REVIEW", "INCOMPLETE", "ERROR")))
        print("Scope: structural checks only; no claim about ink fidelity or mathematical correctness.")
        return 1 if counts["ERROR"] else 2 if counts["INCOMPLETE"] else 0


def tex_without_comments(text: str) -> str:
    """Strip unescaped percent comments, retaining newlines and command symbols."""
    out = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\\" and i + 1 < len(text):
            out.extend(text[i:i + 2])
            i += 2
        elif ch == "%":
            j = text.find("\n", i)
            if j < 0:
                break
            out.append("\n")
            i = j + 1
        else:
            out.append(ch)
            i += 1
    return "".join(out)


def check_tex(path: Path, allow: set[str], report: Report):
    text = tex_without_comments(path.read_text(encoding="utf-8"))
    braces = []
    i = 0
    line = 1
    while i < len(text):
        ch = text[i]
        if ch == "\\" and i + 1 < len(text):
            i += 2
            continue
        if ch == "\n":
            line += 1
        elif ch == "{":
            braces.append(line)
        elif ch == "}":
            if braces:
                braces.pop()
            else:
                report.add("ERROR", f"{path.name}:{line}: unmatched closing brace")
        i += 1
    if braces:
        report.add("ERROR", f"{path.name}: unclosed braces from lines {braces}")
    commands = set(re.findall(r"\\([A-Za-z@]+)", text))
    forbidden = sorted(commands & FORBIDDEN_FRAGMENT_COMMANDS)
    if forbidden:
        report.add("ERROR", f"{path.name}: non-fragment commands: {', '.join(forbidden)}")
    unknown = sorted(commands - allow - FORBIDDEN_FRAGMENT_COMMANDS)
    if unknown:
        report.add("REVIEW", f"{path.name}: commands outside static allowlist: {', '.join(unknown)}")
    stack = []
    for m in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", text):
        if m[1] == "begin":
            stack.append(m[2])
        elif not stack or stack[-1] != m[2]:
            report.add("ERROR", f"{path.name}: mismatched environment end {m[2]}")
        else:
            stack.pop()
    if stack:
        report.add("ERROR", f"{path.name}: unclosed environments {stack}")


def read_table(path: Path, report: Report, header=None):
    if not path.exists():
        return []
    try:
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f, delimiter="," if path.suffix == ".csv" else "\t")
            actual = reader.fieldnames
            rows = list(reader)
        if header is not None and actual != list(header):
            report.add("ERROR", f"{path.name}: header is {actual!r}; expected {list(header)!r}")
        elif actual:
            report.add("OK", f"{path.name}: header and {len(rows)} data rows parsed")
        else:
            report.missing(f"{path.name}: no header")
        for n, row in enumerate(rows, 2):
            if None in row or any(v is None for v in row.values()):
                report.add("ERROR", f"{path.name}:{n}: wrong number of columns")
        return rows
    except (OSError, UnicodeError, csv.Error) as exc:
        report.add("ERROR", f"{path.name}: cannot parse: {exc}")
        return []


def integer(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def check_decisions(root, marks_path, report):
    rows = read_table(root / "decisions.tsv", report, HEADERS["decisions.tsv"])
    if marks_path.exists():
        # Do not read source page files or use mark readings to judge the text.
        with marks_path.open(encoding="utf-8-sig", newline="") as f:
            marks = [{k: r[k] for k in ("id", "cote", "scan")}
                     for r in csv.DictReader(f, delimiter="\t")]
    else:
        report.add("REVIEW", "Original MARKS.tsv unavailable; checking fixed 138-ID sequence only")
        marks = [{"id": f"M{i:04d}"} for i in range(163, 301)]
    expected = [r["id"] for r in marks]
    actual = [r.get("id") for r in rows]
    if len(expected) != 138:
        report.add("ERROR", f"MARKS.tsv: expected 138 source rows, got {len(expected)}")
    if actual == expected:
        report.add("OK", "decisions.tsv: all 138 mark IDs present in source order")
    elif actual == expected[:len(actual)]:
        report.missing(f"decisions.tsv: {len(actual)}/{len(expected)} ordered marks completed")
    else:
        report.add("ERROR", "decisions.tsv: IDs duplicate, missing internally, out of order, or unexpected")
    by_id = {r["id"]: r for r in marks}
    for n, row in enumerate(rows, 2):
        loc = f"decisions.tsv:{n}"
        if row.get("decision") not in {"first", "alternative", "other", "undecided"}:
            report.add("ERROR", f"{loc}: invalid decision {row.get('decision')!r}")
        if row.get("confidence") not in CONFIDENCES:
            report.add("ERROR", f"{loc}: invalid confidence {row.get('confidence')!r}")
        for k in ("reading", "what the ink shows", "crop"):
            if not row.get(k, "").strip():
                report.add("ERROR", f"{loc}: empty {k}")
        mark = by_id.get(row.get("id"), {})
        for k in ("scan", "cote"):
            if k in mark and integer(row.get(k)) != integer(mark[k]):
                report.add("ERROR", f"{loc}: {k} does not match original mark metadata")


def check_tables(root, report):
    collation = read_table(root / f"{PREFIX}_collation.tsv", report,
                           HEADERS[f"{PREFIX}_collation.tsv"])
    seen_scans = []
    for n, row in enumerate(collation, 2):
        loc = f"collation.tsv:{n}"
        scan = integer(row.get("our_scan"))
        seen_scans.append(scan)
        if scan not in SCANS or scan == 66:
            report.add("ERROR", f"{loc}: invalid scan or forbidden H-less scan {scan}")
        if integer(row.get("folder")) != 142:
            report.add("ERROR", f"{loc}: folder must be 142")
        if scan and integer(row.get("their_page")) != scan - 1:
            report.add("ERROR", f"{loc}: H page should be scan minus one")
        if row.get("kind") not in COLLATION_KINDS:
            report.add("ERROR", f"{loc}: invalid kind {row.get('kind')!r}")
        if row.get("confidence") not in CONFIDENCES:
            report.add("ERROR", f"{loc}: invalid confidence")
        if str(row.get("marked_in_H", "")).lower() not in {"yes", "no", "true", "false"}:
            report.add("ERROR", f"{loc}: marked_in_H must explicitly say yes/no")
    if all(x is not None for x in seen_scans) and seen_scans != sorted(seen_scans):
        report.add("ERROR", "collation.tsv: rows are not in scan order")
    inventory = read_table(root / f"{PREFIX}_inventory.csv", report,
                           HEADERS[f"{PREFIX}_inventory.csv"])
    coverage = set()
    for n, row in enumerate(inventory, 2):
        loc = f"inventory.csv:{n}"
        scan = integer(row.get("scan"))
        if scan not in SCANS:
            report.add("ERROR", f"{loc}: invalid scan {row.get('scan')!r}")
        coverage.add(scan)
        if row.get("sheet_kind") not in SHEET_KINDS:
            report.add("ERROR", f"{loc}: invalid sheet_kind")
        if row.get("kind") not in ELEMENT_KINDS:
            report.add("ERROR", f"{loc}: invalid element kind")
        if row.get("transcribed") != "yes":
            report.add("ERROR", f"{loc}: transcribed must be yes")
        for key in ("hand", "element", "position", "first_words_or_objects"):
            if not row.get(key, "").strip():
                report.add("ERROR", f"{loc}: empty {key}")
    missing = sorted(set(SCANS) - coverage)
    if missing:
        report.missing(f"inventory.csv: no elements yet for scans {missing}")
    else:
        report.add("OK", "inventory.csv: all 24 scans represented")
    path = root / "CHECK_EVENTS.tsv"
    events = read_table(path, report)
    if path.exists():
        with path.open(encoding="utf-8-sig", newline="") as f:
            header = next(csv.reader(f, delimiter="\t"), [])
        normalized = {x.strip().lower().replace(" ", "_") for x in header}
        if not {"statement_id", "date", "who", "type", "outcome"} <= normalized:
            report.add("ERROR", "CHECK_EVENTS.tsv: needs statement_id, date, who, type, outcome columns")
        for n, row in enumerate(events, 2):
            norm = {k.strip().lower().replace(" ", "_"): v for k, v in row.items() if k}
            event_type = norm.get("type", "")
            if event_type not in EVENT_TYPES and not event_type.startswith("refuted"):
                report.add("ERROR", f"CHECK_EVENTS.tsv:{n}: unsupported event type {event_type!r}")
            for key in ("statement_id", "date", "who", "outcome"):
                if not norm.get(key, "").strip():
                    report.add("ERROR", f"CHECK_EVENTS.tsv:{n}: empty {key}")


def check_apparatus_counts(root, report):
    """Cross-check rendered counts without judging or interpreting readings."""
    changes_path = root / f"{PREFIX}_changes.md"
    if not changes_path.exists():
        return
    changes = changes_path.read_text(encoding="utf-8")
    top = changes.split("## Consequential readings", 1)[0]
    counts = {}
    total = None
    for line in top.splitlines():
        cells = [x.strip() for x in line.split("|")[1:-1]]
        if len(cells) != 6 or not (cells[0] == "Total" or re.fullmatch(r"\d{3}", cells[0])):
            continue
        if not all(re.fullmatch(r"\d+", x) for x in cells[1:]):
            report.add("ERROR", f"changes.md: non-integer count row for {cells[0]}")
            continue
        values = tuple(int(x) for x in cells[1:])
        if cells[0] == "Total":
            total = values
        else:
            scan = int(cells[0])
            if scan in counts:
                report.add("ERROR", f"changes.md: duplicate count row for scan {scan}")
            counts[scan] = values
    if not counts:
        report.missing("changes.md: no per-scan count table")
        return
    invalid = sorted(set(counts) - set(SCANS))
    if invalid:
        report.add("ERROR", f"changes.md: unexpected scans in count table: {invalid}")
    missing = sorted(set(SCANS) - set(counts))
    if missing:
        report.missing(f"changes.md: no count rows yet for scans {missing}")
    body_counts = Counter()
    body_confidence = Counter()
    for line in changes.splitlines():
        match = re.match(r"^\|\s*(\d{3})\.\d+\s*—", line)
        if match:
            scan = int(match[1])
            body_counts[scan] += 1
            confidence = line.rsplit("|", 2)[-2].strip()
            body_confidence[scan, confidence] += 1
    h_counts = Counter()
    collation_path = root / f"{PREFIX}_collation.tsv"
    if collation_path.exists():
        with collation_path.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                h_counts[integer(row.get("our_scan"))] += 1
    errors_before = sum(level == "ERROR" for level, _ in report.items)
    for scan, (against_c, against_h, high, medium, low) in counts.items():
        places = high + medium + low
        if not max(against_c, against_h) <= places <= against_c + against_h:
            report.add("ERROR", f"changes.md: scan {scan} counts cannot describe a union of C/H differences")
        if body_counts[scan] != places:
            report.add("ERROR", f"changes.md: scan {scan} has {body_counts[scan]} rows but {places} counted places")
        if tuple(body_confidence[scan, c] for c in ("high", "medium", "low")) != (high, medium, low):
            report.add("ERROR", f"changes.md: scan {scan} confidence totals do not match row confidences")
        if collation_path.exists() and h_counts[scan] != against_h:
            report.add("ERROR", f"changes.md: scan {scan} H count {against_h} differs from {h_counts[scan]} collation rows")
    summed = tuple(sum(values[i] for values in counts.values()) for i in range(5))
    if total is None:
        report.missing("changes.md: total count row absent")
    elif total != summed:
        report.add("ERROR", f"changes.md: total row {total} differs from summed page counts {summed}")
    doubts_path = root / f"{PREFIX}_doubts.md"
    if doubts_path.exists():
        headings = [line for line in doubts_path.read_text(encoding="utf-8").splitlines()
                    if line.startswith("#")]
        if "## Decisions that change certainty only" in headings:
            report.add("ERROR", "doubts.md: obsolete misleading heading for all C-mark decisions")
        if "## Disposition of witness C doubt marks" not in headings:
            report.add("REVIEW", "doubts.md: expected C-mark disposition heading is absent")
    errors_after = sum(level == "ERROR" for level, _ in report.items)
    if errors_after == errors_before:
        report.add("OK", "Changes counts, confidence totals, row counts, and H collation counts agree")


def parse_stamp(s):
    try:
        return datetime.fromisoformat(s.strip().replace(" UTC", "+00:00").replace("Z", "+00:00"))
    except ValueError:
        return None


def check_progress(root, report):
    path = root / "progress.log"
    if not path.exists():
        return
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or parse_stamp(lines[0]) is None:
        report.add("ERROR", "progress.log: first line must be a current UTC timestamp")
    for state in ("done", "audited"):
        pattern = re.compile(rf"^scan\s+(\d+)\s+{state}\s+(.+)$")
        entries = []
        for line in lines:
            match = pattern.match(line)
            if not match:
                continue
            scan, tail = int(match[1]), match[2]
            stamp = re.sub(r"\s+cote\s+\d+\s*$", "", tail)
            if parse_stamp(stamp) is None:
                report.add("ERROR", f"progress.log: malformed {state} timestamp for scan {scan}")
            if state == "done" and not re.search(r"\s+cote\s+142\s*$", tail):
                report.add("ERROR", f"progress.log: done record for scan {scan} lacks cote 142")
            entries.append(scan)
        if entries == list(SCANS):
            report.add("OK", f"progress.log: all 24 scans {state} in order")
        elif entries == list(SCANS[:len(entries)]):
            report.missing(f"progress.log: {len(entries)}/24 scans {state}")
        else:
            report.add("ERROR", f"progress.log: {state} scans are duplicated, out of order or unexpected: {entries}")
    done_lines = [i for i, l in enumerate(lines) if re.match(r"^scan\s+\d+\s+done\s", l)]
    audit_lines = [i for i, l in enumerate(lines) if re.match(r"^scan\s+\d+\s+audited\s", l)]
    if done_lines and audit_lines and min(audit_lines) < max(done_lines):
        report.add("ERROR", "progress.log: second reading began before the final first-reading done record")
    freeze = [(i, l) for i, l in enumerate(lines) if l.startswith("transcription frozen ")]
    if not freeze:
        report.missing("progress.log: transcription is not yet frozen")
        return
    if len(freeze) > 1:
        report.add("REVIEW", "progress.log: multiple freeze declarations; verify their explanation")
    freeze_i, freeze_line = freeze[-1]
    if parse_stamp(freeze_line[len("transcription frozen "):]) is None:
        report.add("ERROR", "progress.log: malformed transcription frozen timestamp")
    if audit_lines and freeze_i < max(audit_lines):
        report.add("ERROR", "progress.log: frozen before final audit")
    hashes = {}
    for line in lines:
        m = re.fullmatch(r"(?:sha256\s+)?([0-9a-fA-F]{64})\s+\*?(.+?)\s*", line)
        if m:
            name = m[2].removeprefix("./")
            p = Path(name)
            if p.is_absolute():
                try:
                    name = p.relative_to(root).as_posix()
                except ValueError:
                    continue
            hashes[name] = m[1].lower()
    expected = [f"pages/{name}" for name in PAGE_NAMES] + [f"{PREFIX}_transcription.tex"]
    missing = [x for x in expected if x not in hashes]
    if missing:
        report.missing(f"progress.log: missing frozen SHA-256 records for {missing}")
    for name in expected:
        if name in hashes and (root / name).exists():
            actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
            if actual != hashes[name]:
                report.add("ERROR", f"Frozen SHA-256 changed: {name}")
    if not missing and all((root / n).exists() and hashlib.sha256((root / n).read_bytes()).hexdigest() == hashes[n] for n in expected):
        report.add("OK", "All 25 frozen transcription SHA-256 values match current bytes")
    tail = "\n".join(lines[freeze_i + 1:]).lower()
    if not re.search(r"(?:hash(?:es)?|sha.?256).*(?:unchanged|match|verified)|unchanged.*hash", tail):
        report.missing("progress.log: no post-freeze declaration that hashes were checked unchanged")


def forbidden_path(name):
    p = PurePosixPath(name)
    low = name.lower()
    if p.is_absolute() or ".." in p.parts:
        return "unsafe archive path"
    if p.suffix.lower() in PICTURE_SUFFIXES:
        return "image or facsimile included"
    if p.suffix.lower() == ".zip":
        return "nested ZIP/checkpoint included"
    if any(part.lower().endswith(("_scans", "_texts")) for part in p.parts):
        return "original attachment directory included"
    if any(part.lower() in {"source", "upload", "hua", "__pycache__"} for part in p.parts):
        return "source/witness/cache directory included"
    if p.name in {"MARKS.tsv", "PREAMBLE.tex"}:
        return "original attached text included"
    if p.name.startswith("hua_"):
        return "original H witness included"
    if p.suffix.lower() in {".pyc", ".pyo"}:
        return "bytecode cache included"
    return None


def check_archive(root, archive, report):
    try:
        with zipfile.ZipFile(archive) as z:
            bad_crc = z.testzip()
            if bad_crc:
                report.add("ERROR", f"Archive CRC failure: {bad_crc}")
            names = [i.filename for i in z.infolist() if not i.is_dir()]
            if len(set(names)) != len(names):
                report.add("ERROR", "Archive contains duplicate member names")
            # Both a flat bundle and one wrapping directory are structurally valid.
            common = names[0].split("/")[0] if names else ""
            strip = common + "/" if common and all(n.startswith(common + "/") for n in names) else ""
            relative = {n[len(strip):]: n for n in names}
            for name in names:
                issue = forbidden_path(name)
                if issue:
                    report.add("ERROR", f"Archive member {name}: {issue}")
            for name in list(REQUIRED) + [f"pages/{p}" for p in PAGE_NAMES]:
                if name not in relative:
                    report.missing(f"Archive missing required member {name}")
                elif (root / name).exists() and z.read(relative[name]) != (root / name).read_bytes():
                    report.add("ERROR", f"Archive member differs from validated working file: {name}")
            report.add("OK", f"Archive inspected: {archive.name}, {len(names)} files")
    except (OSError, zipfile.BadZipFile) as exc:
        report.add("ERROR", f"Cannot read archive: {exc}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--mode", choices=("partial", "final"), default="partial")
    parser.add_argument("--marks", type=Path)
    parser.add_argument("--preamble", type=Path)
    parser.add_argument("--archive", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    report = Report(args.mode)
    source = root.parent / "source" / f"{PREFIX}_texts"
    marks_path = args.marks or source / "MARKS.tsv"
    preamble_path = args.preamble or source / "PREAMBLE.tex"
    for name in REQUIRED:
        if not (root / name).is_file():
            report.missing(f"Required file absent: {name}")
        elif (root / name).stat().st_size == 0:
            report.missing(f"Required file empty: {name}")
    actual = {p.name for p in (root / "pages").glob("*.tex")}
    missing = sorted(set(PAGE_NAMES) - actual)
    extra = sorted(actual - set(PAGE_NAMES))
    if missing:
        report.missing(f"Page files not yet present: {missing}")
    if extra:
        report.add("ERROR", f"Unexpected page files: {extra}")
    if not missing and not extra:
        report.add("OK", "Exactly the 24 required scan page files are present")
    wrappers = KNOWN_WRAPPERS.copy()
    if preamble_path.exists():
        preamble = tex_without_comments(preamble_path.read_text(encoding="utf-8"))
        wrappers |= set(re.findall(r"\\(?:newcommand|renewcommand|providecommand)\s*\{\\([A-Za-z@]+)\}", preamble))
    allow = STANDARD_COMMANDS | wrappers
    for name in PAGE_NAMES:
        path = root / "pages" / name
        if path.exists():
            check_tex(path, allow, report)
            text = tex_without_comments(path.read_text(encoding="utf-8"))
            expected_scan = int(name[8:11])
            scan_markers = re.findall(r"\\scanpage\s*\{(\d+)\}", text)
            if scan_markers != [str(expected_scan)]:
                report.add("ERROR", f"{name}: expected one \\scanpage{{{expected_scan}}}, got {scan_markers}")
    combined = root / f"{PREFIX}_transcription.tex"
    if combined.exists() and not missing:
        expected = b"".join((root / "pages" / n).read_bytes() for n in PAGE_NAMES)
        if combined.read_bytes() != expected:
            report.add("ERROR", "Combined transcription differs from exact ordered concatenation of page fragments")
        else:
            report.add("OK", "Combined transcription is the exact ordered concatenation of all 24 pages")
        check_tex(combined, allow, report)
    check_decisions(root, marks_path, report)
    check_tables(root, report)
    check_apparatus_counts(root, report)
    check_progress(root, report)
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        name = path.relative_to(root).as_posix()
        issue = forbidden_path(name)
        if issue:
            # When an actual ZIP is supplied, its membership is authoritative;
            # incidental working caches can legitimately have been excluded.
            level = "REVIEW" if args.archive else "ERROR"
            report.add(level, f"Working-tree member {name} must stay outside the ZIP: {issue}")
    if args.archive:
        check_archive(root, args.archive, report)
    return report.finish()


if __name__ == "__main__":
    sys.exit(main())
