#!/usr/bin/env python3
"""Derive mechanical report supplements without judging manuscript readings.

Run after the final workflow.rebuild()/audit(), because rebuild replaces the
reports. Default behavior is read-only. --apply-certainty replaces only the
'Certainty decisions' section of the doubts report, idempotently.
--apply-crop-register appends an idempotent register to the changes report;
it does not alter substantive change rows or their counts.

Example:
  python scripts/enrich_reports.py OUTPUT_ROOT SOURCE_TEXTS_ROOT \
      --apply-certainty --apply-crop-register --report OUTPUT_ROOT/mechanical_review.md \
      --deleted-review-tsv OUTPUT_ROOT/deleted_mark_review.tsv

Source page files are parsed only to locate uncertainty macros nested inside
deleted spans. They are not compared linguistically or adjudicated. The review
TSV is a queue for the sole reader, not a set of inferred dispositions.
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import io
import os
import re
import tempfile
from collections import Counter, defaultdict
from pathlib import Path


PFX = "SP67_C13_136"
SCANS = (330, 332, 333, 334, 335, 337, 338, 339, 340, 342, 343, 345,
         346, 348, 350, 351, 352, 355, 357, 358, 359, 360, 361, 362, 363)
HEADERS = {
    "decisions.tsv": ("id", "cote", "scan", "decision", "reading", "what the ink shows", "crop", "confidence"),
    f"{PFX}_collation.tsv": ("folder", "their_page", "our_scan", "line", "their_reading", "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H", "confidence"),
    f"{PFX}_inventory.csv": ("scan", "sheet_kind", "hand", "element", "kind", "position", "first_words_or_objects", "transcribed"),
    "CHECK_EVENTS.tsv": ("statement_id", "date", "who", "type", "outcome"),
}
RECORD_KEYS = {"scan", "decisions", "changes", "inventory", "note", "hand", "notation", "abbr", "checks", "unresolved"}
CHANGE_KEYS = {"place", "C", "H", "final", "ink", "kind", "dc", "dh", "confidence", "crop", "marked", "consequential"}
CONFIDENCE = {"high", "medium", "low"}
BOX = re.compile(r"\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)")
CONTROL = re.compile(r"\\([A-Za-z]+)")
STANDARD = set("""
begin end documentclass usepackage input include includeonly newcommand renewcommand
providecommand DeclareMathOperator def let newenvironment renewenvironment
par noindent indent medskip smallskip bigskip vspace hspace quad qquad hfill vfill
newline linebreak pagebreak newpage clearpage nobreak phantom hphantom vphantom
rule strut relax protect ensuremath allowbreak displaystyle textstyle scriptstyle
linewidth textwidth columnwidth textheight baselineskip lineskip parskip parindent
rotatebox scalebox resizebox reflectbox includegraphics
scriptscriptstyle limits nolimits displaylimits left right middle big Big bigg Bigg
bigl bigr Bigl Bigr biggl biggr Biggl Biggr bigm Bigm biggm Biggm
text textrm textsf texttt textbf textit textsl textsc textnormal emph mbox fbox framebox
mbox normalfont rmfamily sffamily ttfamily bfseries mdseries itshape upshape slshape scshape
small footnotesize scriptsize tiny normalsize large Large LARGE huge Huge
mathrm mathit mathsf mathtt mathbf mathcal mathbb mathfrak mathscr mathnormal
operatorname operatornamewithlimits mathop mathrel mathbin mathord mathopen mathclose mathpunct
frac dfrac tfrac cfrac genfrac binom dbinom tbinom sqrt root
boxed
over under atop choose brace brack overset underset stackrel sideset
overline underline widehat widetilde hat tilde bar vec dot ddot dddot ddddot acute grave
breve check mathring overbrace underbrace overrightarrow overleftarrow
overleftrightarrow underrightarrow underleftarrow underleftrightarrow
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa varkappa
lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
aleph beth gimel daleth ell hbar hslash imath jmath wp Re Im partial nabla eth
infty emptyset varnothing top bot perp angle measuredangle sphericalangle triangle
square Box Diamond diamond lozenge blacksquare blacktriangle blacktriangledown
blacktriangleleft blacktriangleright complement backslash prime flat natural sharp
sum prod coprod int iint iiint iiiint idotsint oint bigcup bigcap bigvee bigwedge
bigsqcup bigoplus bigotimes bigodot biguplus
sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh coth log ln lg exp
lim limsup liminf sup inf max min det dim ker hom arg gcd Pr deg mod bmod pmod pod
varinjlim varprojlim varliminf varlimsup
to mapsto longmapsto rightarrow leftarrow leftrightarrow longrightarrow longleftarrow
longleftrightarrow Rightarrow Leftarrow Leftrightarrow Longrightarrow Longleftarrow
Longleftrightarrow uparrow downarrow updownarrow Uparrow Downarrow Updownarrow
hookrightarrow hookleftarrow twoheadrightarrow twoheadleftarrow rightleftarrows
leftrightarrows rightrightarrows leftleftarrows rightarrowtail leftarrowtail
rightsquigarrow leftrightsquigarrow leadsto dashrightarrow dashleftarrow
nearrow searrow nwarrow swarrow xrightarrow xleftarrow rightharpoonup rightharpoondown
leftharpoonup leftharpoondown rightleftharpoons leftrightharpoons
curvearrowleft curvearrowright circlearrowleft circlearrowright
looparrowleft looparrowright multimap implies impliedby iff
le ge leq geq neq ne eqsim equiv sim simeq approx approxeq asymp cong doteq doteqdot
triangleq lesssim gtrsim lessapprox gtrapprox ll gg lll ggg prec succ preceq succeq
precsim succsim precapprox succapprox propto nless ngtr nleq ngeq nsim ncong
subset supset subseteq supseteq subsetneq supsetneq subsetneqq supsetneqq
subseteqq supseteqq nsubseteq nsupseteq sqsubset sqsupset sqsubseteq sqsupseteq
in ni owns notin parallel nparallel mid nmid models vdash dashv Vdash vDash Vvdash
not nvdash nvDash nVdash nVDash
cap cup sqcap sqcup uplus setminus smallsetminus land lor wedge vee
times div cdot ast star circ bullet odot oplus ominus otimes oslash
pm mp dotplus amalg wr ltimes rtimes leftthreetimes rightthreetimes
therefore because forall exists nexists neg lnot And
ldots cdots vdots ddots dots dotsb dotsc dotsi dotsm dotso
langle rangle lbrace rbrace lvert rvert lVert rVert vert Vert
lfloor rfloor lceil rceil ulcorner urcorner llcorner lrcorner
label ref pageref eqref cite footnote footnotemark footnotetext marginpar
section subsection subsubsection paragraph subparagraph title author date maketitle
item setlength addtolength setcounter value arabic roman Roman alph Alph
textsuperscript textsubscript
uline uuline uwave sout xout dashuline dotuline
color textcolor colorbox fcolorbox definecolor pagecolor
centering raggedright raggedleft multicolumn hline cline vline
nonumber notag tag intertext substack
vcenter vbox hbox raisebox kern mkern mspace smash mathstrut
H O o L l S P aa AA ae AE oe OE ss dh DH th TH
LaTeX TeX textbackslash textasciitilde textasciicircum textbar textless textgreater
textquotedblleft textquotedblright textquoteleft textquoteright textendash textemdash
arrow ar draw path node coordinate fill filldraw shade shadedraw clip foreach
pgfmathsetmacro pgfmathparse pgfmathresult pgfextra tikz tikzset
pgfkeys pgfsetlayers pgfonlayer endpgfonlayer pgfdeclarelayer
""".split())
ENVIRONMENTS = set("""
document center flushleft flushright quote quotation verse itemize enumerate description
equation equation* align align* alignat alignat* aligned alignedat gather gather*
gathered multline multline* split cases matrix pmatrix bmatrix Bmatrix vmatrix Vmatrix
smallmatrix array tabular tabular* displaymath math minipage tikzpicture tikzcd scope
pgfonlayer
""".split())


def masked_comments(text):
    """Preserve offsets and line numbers while masking TeX comments."""
    chars = list(text)
    i = 0
    while i < len(chars):
        if chars[i] == "\\":
            i += 2
        elif chars[i] == "%":
            while i < len(chars) and chars[i] != "\n":
                chars[i] = " "
                i += 1
        else:
            i += 1
    return "".join(chars)


def control_words(text):
    """Tokenize control words; a doubled backslash is a control symbol.

    Thus a row separator followed by q is not the control word q. Three
    backslashes followed by q, however, are a row separator and that control
    word. TeX comments should be masked before calling this function.
    """
    i = 0
    while i < len(text):
        if text[i] != "\\":
            i += 1
            continue
        match = CONTROL.match(text, i)
        if match:
            yield match
            i = match.end()
        else:
            i += 2


def argument_span(text, opening):
    if opening >= len(text) or text[opening] != "{":
        return None
    level = 1
    i = opening + 1
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "{":
            level += 1
        elif text[i] == "}":
            level -= 1
            if level == 0:
                return (opening + 1, i, i + 1)
        i += 1
    return None


def invocations(text, macro):
    masked = masked_comments(text)
    for match in re.finditer(r"\\" + re.escape(macro) + r"(?![A-Za-z])\s*", masked):
        # An escaped backslash is not the start of a control word.
        before = match.start() - 1
        slashes = 0
        while before >= 0 and masked[before] == "\\":
            slashes += 1
            before -= 1
        if slashes % 2:
            continue
        span = argument_span(masked, match.end())
        if span:
            a, b, end = span
            yield (match.start(), end, a, b, text[a:b])


def first_alternative(text):
    level = 0
    i = 0
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "{":
            level += 1
        elif text[i] == "}":
            level -= 1
        elif text[i] == "|" and level == 0:
            return text[:i]
        i += 1
    return text


def normalized(text):
    return re.sub(r"\s+", " ", text).strip()


def outer_unsure(text):
    text = text.strip()
    spans = list(invocations(text, "unsure"))
    for start, end, _, _, body in spans:
        if start == 0 and end == len(text):
            return body
    return None


def table(path, issues, expected=None):
    if not path.is_file():
        issues.append(("schema", f"Missing file: {path.name}"))
        return []
    try:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream, delimiter="," if path.suffix == ".csv" else "\t")
            fields = reader.fieldnames or []
            if expected and (set(fields) != set(expected) or len(fields) != len(set(fields))):
                issues.append(("schema", f"{path.name}: headers differ from the specified schema"))
            rows = list(reader)
            for number, row in enumerate(rows, 2):
                if None in row or any(value is None for value in row.values()):
                    issues.append(("schema", f"{path.name}:{number}: wrong number of fields"))
            return rows
    except (OSError, UnicodeError, csv.Error) as exc:
        issues.append(("schema", f"{path.name}: {exc}"))
        return []


def certainty_rows(marks, decisions):
    by_id = {row.get("id"): row for row in decisions}
    result = []
    for mark in marks:
        decision = by_id.get(mark.get("id"))
        if not decision:
            continue
        old = mark.get("the mark as written", "")
        old_body = outer_unsure(old)
        if old_body is None:
            continue  # resolving illegibility is a substantive reading change
        final = decision.get("reading", "")
        if normalized(old) == normalized(final):
            continue  # no change of either reading or certainty
        final_body = outer_unsure(final)
        final_first = first_alternative(final_body) if final_body is not None else final
        if normalized(first_alternative(old_body)) == normalized(final_first):
            result.append((mark, decision))
    return result


def escape_cell(text):
    return str(text).replace("|", "\\|").replace("\n", "<br>")


def certainty_section(rows, marks_count, decisions_count):
    lines = ["## Certainty decisions", "", (
        f"{len(rows)} changes below retain the first literal reading of an original "
        "live-text uncertainty mark; only its uncertainty wrapper or alternatives change. "
        "Each has one row. Substantive reading changes and unchanged marks are excluded. "
        f"The source has {marks_count} indexed marks; decisions.tsv currently contains {decisions_count} decisions."
    ), "", "| mark | scan | C mark | final reading | evidence | crop | confidence |",
        "| --- | --- | --- | --- | --- | --- | --- |"]
    for mark, decision in rows:
        values = [mark.get("id"), mark.get("scan"), mark.get("the mark as written"),
                  decision.get("reading"), decision.get("what the ink shows"),
                  decision.get("crop"), decision.get("confidence")]
        lines.append("| " + " | ".join(escape_cell(value) for value in values) + " |")
    return "\n".join(lines) + "\n\n"


def update_certainty(path, section):
    text = path.read_text(encoding="utf-8")
    match = re.search(r"(?m)^## Certainty decisions\s*$", text)
    if not match:
        raise ValueError("Doubts report has no '## Certainty decisions' section; no write performed")
    following = re.search(r"(?m)^## ", text[match.end():])
    end = match.end() + following.start() if following else len(text)
    path.write_text(text[:match.start()] + section + text[end:], encoding="utf-8")


def deleted_marks(text):
    spans = list(invocations(text, "deleted"))
    # Keep existing unsure-token ordinal IDs stable; append illegibility marks
    # so the review queue covers both kinds without renumbering earlier rows.
    for macro in ("unsure", "illegible"):
        for start, end, _, _, body in invocations(text, macro):
            if any(a <= start and end <= b for _, _, a, b, _ in spans):
                line = text.count("\n", 0, start) + 1
                column = start - text.rfind("\n", 0, start)
                yield dict(line=line, column=column, token=text[start:end])


def deleted_review_is_complete(row):
    """Check explicit ledger fields only; never infer a reading/disposition."""
    disposition = row.get("reader_disposition")
    note = row.get("reader_note")
    return (isinstance(disposition, str) and bool(disposition.strip())
            and disposition.strip().casefold() != "review required"
            and isinstance(note, str) and bool(note.strip()))


def load_records(root, issues):
    records = []
    for path in sorted((root / "records").glob("scan*.py")):
        try:
            record = ast.literal_eval(path.read_text(encoding="utf-8"))
            if set(record) != RECORD_KEYS:
                issues.append(("schema", f"{path.name}: record keys differ from workflow schema"))
            for index, change in enumerate(record.get("changes", []), 1):
                if set(change) != CHANGE_KEYS:
                    issues.append(("schema", f"{path.name}: change {index} keys differ from workflow schema"))
                if change.get("confidence") not in CONFIDENCE:
                    issues.append(("schema", f"{path.name}: change {index} has noncanonical confidence"))
            records.append(record)
        except (OSError, ValueError, SyntaxError, TypeError) as exc:
            issues.append(("schema", f"Cannot parse record {path.name}: {exc}"))
    return records


REGISTER_START = "<!-- BEGIN MECHANICAL CROP REGISTER -->"
REGISTER_END = "<!-- END MECHANICAL CROP REGISTER -->"


def crop_checks(root, records, decisions, issues, apply_register=False, require_register=False):
    logged = {}
    entries = []
    completed_scans = {int(record["scan"]) for record in records}
    progress = (root / "progress.log").read_text(encoding="utf-8") if (root / "progress.log").is_file() else ""
    for line_number, line in enumerate(progress.splitlines(), 1):
        match = re.match(r"crop scan (\d+) (.*?) box (\(.*?\)) rotation (.*)", line)
        if not match:
            continue
        box_match = BOX.search(match.group(3))
        if not box_match:
            issues.append(("crop", f"progress.log:{line_number}: unparseable crop box"))
            continue
        key = (int(match.group(1)), tuple(map(int, box_match.groups())))
        if key in logged:
            issues.append(("crop", f"progress.log:{line_number}: duplicate logged crop coordinates for scan {key[0]}"))
        logged[key] = (match.group(2), line_number)
        entries.append(dict(scan=key[0], box=key[1], label=match.group(2), rotation=match.group(4), log_line=line_number))
    used = defaultdict(list)
    for record in records:
        scan = int(record["scan"])
        for index, change in enumerate(record.get("changes", []), 1):
            ref = str(change.get("crop", ""))
            matches = list(BOX.finditer(ref))
            if ref.strip().lower() != "page" and not matches:
                issues.append(("crop", f"Scan {scan}, change {index}: crop reference has no recognizable coordinates"))
            for match in matches:
                key = (scan, tuple(map(int, match.groups())))
                used[key].append(f"change {index}")
                if key not in logged:
                    issues.append(("crop", f"Scan {scan}, change {index}: referenced box {key[1]} is absent from progress.log"))
    for decision in decisions:
        ref = str(decision.get("crop", ""))
        matches = list(BOX.finditer(ref))
        if ref.strip().lower() != "page" and not matches:
            issues.append(("crop", f"Decision {decision.get('id')}: crop reference has no recognizable coordinates"))
        for match in matches:
            key = (int(decision["scan"]), tuple(map(int, match.groups())))
            used[key].append(f"decision {decision.get('id')}")
            if key not in logged:
                issues.append(("crop", f"Decision {decision.get('id')}: referenced box {key[1]} is absent from progress.log"))
    register = [REGISTER_START, "## Crop register", "", "Every crop recorded in progress.log is listed below in scan order. These inspection records are separate from substantive changes and do not contribute to the change counts. Coordinates are original-image pixels (x0, y0, x1, y1); rotations are degrees used in preparing the view. A crop cited only by a certainty decision still appears here.", ""]
    for scan in sorted({entry["scan"] for entry in entries}):
        register.extend([f"### Scan {scan}", "", "| crop label | original pixel box | rotation | decision/change citations | progress line |", "| --- | --- | --- | --- | --- |"])
        for entry in entries:
            if entry["scan"] != scan:
                continue
            refs = used.get((scan, entry["box"]), [])
            values = [entry["label"], str(entry["box"]), entry["rotation"], "; ".join(refs) or "No matching change or decision citation", entry["log_line"]]
            register.append("| " + " | ".join(escape_cell(value) for value in values) + " |")
        register.append("")
    register.append(REGISTER_END)
    register_text = "\n".join(register)
    changes_path = root / f"{PFX}_changes.md"
    changes_text = changes_path.read_text(encoding="utf-8") if changes_path.is_file() else ""
    existing = re.search(re.escape(REGISTER_START) + r".*?" + re.escape(REGISTER_END), changes_text, flags=re.S)
    if apply_register:
        if not changes_path.is_file():
            raise ValueError("Changes report is missing; crop register was not written")
        if existing:
            changes_text = changes_text[:existing.start()] + register_text + changes_text[existing.end():]
        else:
            changes_text = changes_text.rstrip() + "\n\n" + register_text + "\n"
        changes_path.write_text(changes_text, encoding="utf-8")
        register_current = True
    else:
        register_current = bool(existing and existing.group(0) == register_text)
        if existing and not register_current:
            issues.append(("crop", "Changes report's mechanical crop register is stale; rerun --apply-crop-register after the final rebuild"))
        elif require_register and not existing:
            issues.append(("crop", "Changes report has no complete mechanical crop register; run --apply-crop-register after the final rebuild"))
    for key, (label, line) in logged.items():
        if key[0] not in completed_scans:
            continue  # the sole reader may still be reading this page
        refs = used.get(key, [])
        if not refs and not register_current:
            issues.append(("crop", f"Scan {key[0]}, crop {label}, box {key[1]}: logged at progress.log:{line}, not cited by any change or decision"))
        elif refs and not any(ref.startswith("change ") for ref in refs) and not register_current:
            issues.append(("crop", f"Scan {key[0]}, crop {label}, box {key[1]}: cited only in decisions, absent from changes-log rows"))
    return len(entries)


def report_enrichment_checks(root, source, issues):
    """Read-only final gate for exact, current certainty and crop enrichment.

    This reads only MARKS metadata, generated decisions/records, reports and
    progress.log. It never reads a scan or a witness page, assigns a reading,
    rewrites a report, or infers a missing disposition.
    """
    marks = table(source / "MARKS.tsv", issues)
    decisions = table(root / "decisions.tsv", issues, HEADERS["decisions.tsv"])
    records = load_records(root, issues)
    expected_decisions = [entry for record in records for entry in record.get("decisions", [])]
    if decisions != expected_decisions:
        issues.append(("schema", "decisions.tsv is not current with the ordered page-record decisions"))
    rows = certainty_rows(marks, decisions)
    expected = certainty_section(rows, len(marks), len(decisions)).strip()
    doubts_path = root / f"{PFX}_doubts.md"
    doubts_text = doubts_path.read_text(encoding="utf-8") if doubts_path.is_file() else ""
    section = re.search(r"(?ms)^## Certainty decisions\s*\n.*?(?=^## |\Z)", doubts_text)
    if not section or section.group(0).strip() != expected:
        issues.append(("certainty", "Certainty decisions section is missing or stale; run --apply-certainty after the final rebuild so every certainty-only change has its current individual row"))
    crop_count = crop_checks(root, records, decisions, issues, apply_register=False, require_register=True)
    return {"certainty_rows": len(rows), "crop_rows": crop_count}


def macro_checks(root, source, issues):
    preamble_path = source / "PREAMBLE.tex"
    preamble = preamble_path.read_text(encoding="utf-8") if preamble_path.is_file() else ""
    declared = set(re.findall(r"\\(?:newcommand|renewcommand|providecommand)\*?\s*\{?\\([A-Za-z]+)", preamble))
    declared.update(re.findall(r"\\DeclareMathOperator\*?\s*\{\\([A-Za-z]+)\}", preamble))
    allowed = STANDARD | declared
    unknown = defaultdict(list)
    for page in sorted((root / "pages").glob("*.tex")):
        text = masked_comments(page.read_text(encoding="utf-8"))
        for match in control_words(text):
            name = match.group(1)
            if name not in allowed:
                unknown[name].append(f"{page.name}:{text.count(chr(10), 0, match.start()) + 1}")
            if name == "begin":
                environment = re.match(r"\s*\{([^{}]+)\}", text[match.end():])
                if environment and environment.group(1) not in ENVIRONMENTS:
                    issues.append(("macro", f"Unrecognized environment {environment.group(1)!r} at {page.name}:{text.count(chr(10), 0, match.start()) + 1}"))
    for name, places in sorted(unknown.items()):
        issues.append(("macro", f"\\{name}: not declared in PREAMBLE.tex or the conservative standard/TikZ allowlist; occurrences: {', '.join(places)}"))
    return len(unknown)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("output_root", type=Path)
    parser.add_argument("source_texts_root", type=Path)
    parser.add_argument("--apply-certainty", action="store_true")
    parser.add_argument("--apply-crop-register", action="store_true")
    parser.add_argument("--report", type=Path, help="write mechanical findings as Markdown")
    parser.add_argument("--deleted-review-tsv", type=Path, help="write a reader-review queue with exact deleted uncertainty tokens")
    args = parser.parse_args()
    root, source = args.output_root, args.source_texts_root
    issues = []
    tables = {name: table(root / name, issues, headers) for name, headers in HEADERS.items()}
    marks = table(source / "MARKS.tsv", issues)
    decisions = tables["decisions.tsv"]
    records = load_records(root, issues)
    record_decisions = [decision for record in records for decision in record.get("decisions", [])]
    if decisions != record_decisions:
        issues.append(("schema", "decisions.tsv differs from the ordered decisions in page records"))
    record_checks = [event for record in records for event in record.get("checks", [])]
    if tables["CHECK_EVENTS.tsv"] != record_checks:
        issues.append(("schema", "CHECK_EVENTS.tsv differs from events in page records"))
    for decision in decisions:
        if decision.get("confidence") not in CONFIDENCE:
            issues.append(("schema", f"Decision {decision.get('id')}: noncanonical confidence"))
    rows = certainty_rows(marks, decisions)
    certainty = certainty_section(rows, len(marks), len(decisions))
    doubts_path = root / f"{PFX}_doubts.md"
    if args.apply_certainty:
        update_certainty(doubts_path, certainty)
    if doubts_path.is_file():
        doubts = doubts_path.read_text(encoding="utf-8")
        if "| see reading |" in doubts or "| unassigned |" in doubts:
            issues.append(("schema", "Doubts table has additional doubts without explicit confidence; the sole reader must assign high/medium/low values"))
        section_match = re.search(r"(?ms)^## Certainty decisions\s*\n(.*?)(?=^## |\Z)", doubts)
        section_text = section_match.group(1) if section_match else ""
        absent = [mark["id"] for mark, _ in rows if not re.search(r"(?m)^\|\s*" + re.escape(mark["id"]) + r"\s*\|", section_text)]
        if absent:
            issues.append(("certainty", f"{len(absent)} certainty-only decisions lack an individual doubts-file line; run --apply-certainty after the final rebuild"))
    review = []
    record_by_scan = {int(record["scan"]): record for record in records}
    final_page_count = 0
    for scan in SCANS:
        source_page = source / "pages" / f"136_scan{scan}.tex"
        final_page = root / "pages" / f"136_scan{scan}.tex"
        if not final_page.is_file():
            continue
        final_page_count += 1
        source_marks = list(deleted_marks(source_page.read_text(encoding="utf-8"))) if source_page.is_file() else []
        final_marks = list(deleted_marks(final_page.read_text(encoding="utf-8")))
        final_tokens = Counter(mark["token"] for mark in final_marks)
        for ordinal, mark in enumerate(source_marks, 1):
            identifier = f"D136-{scan}-{ordinal:02d}"
            count = final_tokens[mark["token"]]
            status = "identical token present in a final deleted span (no occurrence alignment)" if count else "identical token absent from final deleted spans"
            candidates = [str(index) for index, change in enumerate(record_by_scan.get(scan, {}).get("changes", []), 1) if mark["token"] in str(change.get("C", ""))]
            review.append(dict(review_id=identifier, scan=scan, origin="C", line=mark["line"], column=mark["column"], token=mark["token"], token_sha256=hashlib.sha256(mark["token"].encode()).hexdigest(), final_exact_count=count, candidate_change_rows=",".join(candidates), mechanical_status=status, reader_disposition="REVIEW REQUIRED", reader_note=""))
        source_tokens = Counter(mark["token"] for mark in source_marks)
        seen = Counter()
        for ordinal, mark in enumerate(final_marks, 1):
            seen[mark["token"]] += 1
            if seen[mark["token"]] > source_tokens[mark["token"]]:
                review.append(dict(review_id=f"DF136-{scan}-{ordinal:02d}", scan=scan, origin="final", line=mark["line"], column=mark["column"], token=mark["token"], token_sha256=hashlib.sha256(mark["token"].encode()).hexdigest(), final_exact_count=final_tokens[mark["token"]], candidate_change_rows="", mechanical_status="final deleted uncertainty token lacks an identical source-token counterpart", reader_disposition="REVIEW REQUIRED", reader_note=""))
    review_path = args.deleted_review_tsv or root / "deleted_mark_review.tsv"
    prior_bytes = review_path.read_bytes() if review_path.is_file() else None
    if prior_bytes is not None:
        prior = {(row.get("review_id"), row.get("token_sha256")): row for row in csv.DictReader(io.StringIO(prior_bytes.decode("utf-8-sig")), delimiter="\t")}
        for item in review:
            old = prior.get((item["review_id"], item["token_sha256"]))
            if old:
                item["reader_disposition"] = old.get("reader_disposition") or "REVIEW REQUIRED"
                item["reader_note"] = old.get("reader_note") or ""
    if args.deleted_review_tsv:
        fields = ("review_id", "scan", "origin", "line", "column", "token", "token_sha256", "final_exact_count", "candidate_change_rows", "mechanical_status", "reader_disposition", "reader_note")
        buffer = io.StringIO(newline="")
        writer = csv.DictWriter(buffer, fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(review)
        descriptor, temporary_name = tempfile.mkstemp(prefix=args.deleted_review_tsv.name + ".", suffix=".tmp", dir=args.deleted_review_tsv.parent)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as stream:
                stream.write(buffer.getvalue())
            current_bytes = args.deleted_review_tsv.read_bytes() if args.deleted_review_tsv.is_file() else None
            if current_bytes != prior_bytes:
                raise RuntimeError("Deleted-mark review changed concurrently; no reader dispositions were overwritten")
            os.replace(temporary_name, args.deleted_review_tsv)
        finally:
            if os.path.exists(temporary_name):
                os.unlink(temporary_name)
    crops = crop_checks(root, records, decisions, issues, args.apply_crop_register)
    unknown_macros = macro_checks(root, source, issues)
    completed_review = sum(deleted_review_is_complete(item) for item in review)
    pending_review = len(review) - completed_review
    summary = ["# Mechanical report review", "", "This report makes no manuscript reading or mathematical decision.", "",
        f"- Present final pages: {final_page_count}.", f"- Original indexed marks: {len(marks)}; current decisions: {len(decisions)}.",
        f"- Literal certainty-only changes: {len(rows)}.", f"- Deleted uncertainty review: {len(review)} entries; {completed_review} completed, {pending_review} pending (explicit disposition and note required).",
        f"- Logged crop boxes: {crops}.", f"- Potentially unsupported macro names: {unknown_macros}.",
        "", "## Findings", ""]
    if issues:
        for category, message in issues:
            summary.append(f"- **{category}**: {message}")
    else:
        summary.append("No schema, crop-reference, certainty-line, or allowlist issue found.")
    summary.extend(["", "## Deleted uncertainty review queue", "",
        "Exact-token identity and deletion nesting do not establish a reading or a documented disposition. The sole reader must review each item and record its resolution or retained doubt. A changed token is not inferred to be resolved.", ""])
    for item in review:
        disposition = item.get("reader_disposition", "").strip() or "REVIEW REQUIRED"
        disposition = disposition.replace("\n", "<br>")
        completion = "completed" if deleted_review_is_complete(item) else "pending"
        summary.append(f"- {item['review_id']}: {item['origin']} scan {item['scan']}, line {item['line']}, column {item['column']}; {item['mechanical_status']}. Recorded disposition: {disposition}. Review fields: {completion}.")
    summary.extend(["", "## Report limitations", "", "The macro allowlist is conservative and does not compile TeX. The source and final deleted-mark queues use literal matching, not contextual alignment. Certainty-only rows preserve the first literal alternative; mathematical or macro equivalence is not inferred. Run this helper after the last workflow rebuild, which otherwise replaces the enriched doubts section.", ""])
    result = "\n".join(summary)
    if args.report:
        args.report.write_text(result, encoding="utf-8")
    print(result)
    if args.apply_certainty:
        print("Certainty decisions section updated; page transcriptions and records were not modified.")
    if args.apply_crop_register:
        print("Crop register updated; substantive change rows and counts were not modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
