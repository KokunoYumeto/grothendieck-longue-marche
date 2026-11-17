#!/usr/bin/env python3
"""Read-only structural checks for MPL_64_002-039.

Usage:
    python records/validate_package.py
    python records/validate_package.py --partial
    python records/validate_package.py --require-frozen --json

No image reading or OCR is performed. Passing these checks does not establish
visual completeness, fidelity to handwriting, or mathematical correctness.

Recommended progress.log hash format, before the freeze marker:
    sha256 <64 lowercase hexadecimal digits> pages/<page filename>
    sha256 <64 lowercase hexadecimal digits> MPL_64_002-039_transcription.tex
    transcription frozen YYYY-MM-DD HH:MM:SS UTC
After research:
    frozen hashes unchanged YYYY-MM-DD HH:MM:SS UTC

The validator never writes into the package. Unknown commands are warnings:
TeX's standard vocabulary is extensible. --strict-commands makes those errors;
--allow-command NAME permits an additionally reviewed standard command.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

PREFIX = "MPL_64_002-039"
SCANS = set(range(2, 40))
STATE = {
    "cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
    "uline", "uuline", "diagram", "figure", "unsure", "illegible",
}
STANDARD = {"textcircled", "boxed", "ltimes", "linewidth"} | set("""
begin end text textrm textsf texttt textbf textit textsl textsc emph mbox
mathrm mathrm mathsf mathtt mathbf mathit mathcal mathfrak mathbb mathnormal
boldsymbol bm operatorname operatornamewithlimits ensuremath
frac dfrac tfrac cfrac binom dbinom tbinom sqrt root over choose atop
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
bigm Bigm biggm Biggm
overline underline widehat widetilde hat tilde bar vec dot ddot dddot check
acute grave breve overbrace underbrace overset underset stackrel
phantom hphantom vphantom smash mathstrut strut
quad qquad enspace thinspace medspace thickspace negthinspace hspace vspace
hfill vfill hfil vfil kern mkern
textstyle displaystyle scriptstyle scriptscriptstyle
displaystyle limits nolimits substack mathop mathbin mathrel mathord mathpunct
mathopen mathclose displaylimits
tag notag label ref eqref numberwithin nonumber
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon phi
varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
ell hbar imath jmath Re Im wp aleph beth gimel daleth partial nabla infinity
infty emptyset varnothing bot top angle triangle square Box Diamond
forall exists nexists neg land lor lnot wedge vee bigwedge bigvee
cap cup bigcap bigcup sqcap sqcup bigsqcup uplus biguplus setminus smallsetminus
in ni notin subset supset subseteq supseteq subsetneq supsetneq
sqsubset sqsupset sqsubseteq sqsupseteq subsetneqq supsetneqq
le ge leq geq neq ne ll gg lesssim gtrsim lessgtr lesseqgtr
sim simeq cong approx asymp equiv propto doteq coloneqq eqcolon
times div cdot ast star circ bullet pm mp oplus ominus otimes oslash odot
bigoplus bigotimes bigodot amalg wr
sum prod coprod int iint iiint oint
to gets mapsto longmapsto hookrightarrow hookleftarrow
rightarrow leftarrow leftrightarrow longrightarrow longleftarrow
longleftrightarrow Rightarrow Leftarrow Leftrightarrow
Longrightarrow Longleftarrow Longleftrightarrow
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow
nearrow searrow swarrow nwarrow
xrightarrow xleftarrow xleftrightarrow xmapsto
twoheadrightarrow twoheadleftarrow rightleftarrows leftrightarrows
rightrightarrows leftleftarrows rightleftharpoons leftrightharpoons
rightharpoonup rightharpoondown leftharpoonup leftharpoondown
rightsquigarrow leadsto multimap
longrightsquigarrow
vert Vert mid parallel perp models vdash dashv Vdash Vvdash
langle rangle lceil rceil lfloor rfloor lbrace rbrace lvert rvert lVert rVert
colon cdots ldots vdots ddots dots dotsc dotsb dotsm dotsi dotso
prime backprime dagger ddagger checkmark surd
not
sin cos tan cot sec csc sinh cosh tanh coth arcsin arccos arctan
log ln exp lim limsup liminf min max inf sup det dim ker hom deg gcd Pr
arg
arraystretch arraycolsep tabcolsep hline cline multicolumn multirow
hdashline intertext shortintertext
newline linebreak nolinebreak noindent indent par medskip smallskip bigskip
centering raggedright raggedleft rule vrule hrule
item setlength addtolength
tikz draw path node coordinate fill filldraw clip foreach matrix
scope endscope arrow ar pgfmathsetmacro pgfmathtruncatemacro
pgfsetlayers
endinput
""".split())
FORBIDDEN = {
    "documentclass", "usepackage", "input", "include", "includegraphics",
    "newcommand", "renewcommand", "def", "gdef", "xdef",
    "sout", "strike", "strikethrough", "red", "add", "del", "gap",
    "missing", "unclear", "addition", "deletion", "annotation",
}
INVENTORY_COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
MATH_ENVS = {
    "math", "displaymath", "equation", "equation*", "align", "align*",
    "gather", "gather*", "multline", "multline*", "eqnarray", "eqnarray*",
}
CHECK_TYPES = {
    "targeted proof check", "independent re-proof",
    "computation or formal certificate", "used and rechecked in this run",
    "carried as background without fault found",
}
COMMAND_RE = re.compile(r"\\([A-Za-z]+|.)", re.S)


def without_comments(text):
    """Replace comments with spaces, keeping offsets and line numbers."""
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


def braced_argument(text, offset):
    while offset < len(text) and text[offset].isspace():
        offset += 1
    if offset == len(text) or text[offset] != "{":
        return None
    start = offset
    depth = 1
    offset += 1
    while offset < len(text):
        if text[offset] == "\\":
            offset += 2
            continue
        if text[offset] == "{":
            depth += 1
        elif text[offset] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:offset], start, offset + 1
        offset += 1
    return None


def array_columns(spec):
    """Identify ordinary math columns versus p/m/b paragraph columns."""
    result = []
    i = 0
    while i < len(spec):
        char = spec[i]
        if char in "clr":
            result.append(False)
        elif char in "pmb":
            width = braced_argument(spec, i + 1)
            result.append(True)
            if width:
                i = width[2]
                continue
        elif char == "*":
            count = braced_argument(spec, i + 1)
            repeated = braced_argument(spec, count[2]) if count else None
            if count and repeated and count[0].strip().isdigit():
                result.extend(array_columns(repeated[0]) * int(count[0]))
                i = repeated[2]
                continue
        elif char in "@!><":
            modifier = braced_argument(spec, i + 1)
            if modifier:
                i = modifier[2]
                continue
        i += 1
    return result


def paragraph_cells(text, start, end, columns):
    """Locate top-level paragraph cells; ignore nested alignments and groups."""
    result = []
    cell_start = start
    column = 0
    braces = 0
    nested_envs = 0
    i = start

    def finish(stop):
        if columns and column < len(columns) and columns[column] and cell_start < stop:
            result.append((cell_start, stop))

    while i < end:
        if text[i] == "\\":
            match = COMMAND_RE.match(text, i)
            if not match:
                i += 1
                continue
            command = match[1]
            if command in {"begin", "end"}:
                arg = braced_argument(text, match.end())
                if arg:
                    nested_envs += 1 if command == "begin" else -1
                    i = arg[2]
                    continue
            if command in {"\\", "cr"} and not braces and not nested_envs:
                finish(i)
                column = 0
                cell_start = match.end()
            i = match.end()
            continue
        if text[i] == "{":
            braces += 1
        elif text[i] == "}":
            braces -= 1
        elif text[i] == "&" and not braces and not nested_envs:
            finish(i)
            column += 1
            cell_start = i + 1
        i += 1
    finish(end)
    return result


def text_mode_ranges(text):
    """Text arguments and array paragraph cells establish fresh math contexts.

    This is a lexical approximation, not a replacement for a TeX compiler.
    Explicit column modifiers that themselves change math mode are not expanded.
    """
    text_commands = {
        "text", "mbox", "hbox", "textrm", "textsf", "texttt", "textbf",
        "textit", "textsl", "textsc", "textnormal", "textup", "emph",
    }
    result = []
    stack = []
    for match in COMMAND_RE.finditer(text):
        command = match[1]
        arg = braced_argument(text, match.end())
        if command in text_commands and arg:
            result.append((arg[1] + 1, arg[2] - 1))
        if command == "begin" and arg:
            env = arg[0]
            array_info = None
            if env == "array":
                position = arg[2]
                while position < len(text) and text[position].isspace():
                    position += 1
                if position < len(text) and text[position] == "[":
                    close = text.find("]", position)
                    position = close + 1 if close != -1 else position
                spec = braced_argument(text, position)
                if spec:
                    array_info = (spec[2], array_columns(spec[0]))
            stack.append((env, array_info))
        elif command == "end" and arg and stack and stack[-1][0] == arg[0]:
            _, array_info = stack.pop()
            if array_info:
                start, columns = array_info
                result.extend(paragraph_cells(text, start, match.start(), columns))
    return sorted(set(result), key=lambda item: (item[0], -item[1]))


def check_tex(path, scan, report, strict_commands, extra_commands):
    original = path.read_text(encoding="utf-8")
    text = without_comments(original)
    name = str(path.name)
    counts = Counter()
    arguments = defaultdict(list)
    ranges = []
    for match in COMMAND_RE.finditer(text):
        command = match.group(1)
        line = text.count("\n", 0, match.start()) + 1
        if command in FORBIDDEN:
            report("error", f"{name}:{line}: forbidden command \\{command}")
        elif command.isalpha() and command not in STATE | STANDARD | extra_commands:
            report("error" if strict_commands else "warning",
                   f"{name}:{line}: review command \\{command}; not in standard allowlist")
        if command in STATE:
            counts[command] += 1
            argument = braced_argument(text, match.end())
            if argument is None:
                report("error", f"{name}:{line}: \\{command} needs a balanced braced argument")
            else:
                value, start, end = argument
                arguments[command].append(value)
                ranges.append((command, start, end, line))
                if command == "illegible" and not re.fullmatch(r"\s*\d+\s*", value):
                    report("error", f"{name}:{line}: illegible word count is not an integer")

    expected_prefix = (rf"\cotefile{{64}}\scanpage{{{scan}}}"
                       if scan == 2 else rf"\scanpage{{{scan}}}")
    if not re.sub(r"\s+", "", text).startswith(expected_prefix):
        report("error", f"{name}: wrong opening page markers")
    if arguments["scanpage"] != [str(scan)]:
        report("error", f"{name}: expected exactly one \\scanpage{{{scan}}}")
    if arguments["cotefile"] != (["64"] if scan == 2 else []):
        report("error", f"{name}: cote marker must occur only on the first page")

    braces = []
    environments = []
    math_ranges = []
    math_open = None
    text_scopes = defaultdict(list)
    for start, end in text_mode_ranges(text):
        if start < end:
            text_scopes[start].append(end)
    parent_math = []
    i = 0
    while i < len(text):
        while parent_math and i >= parent_math[-1][0]:
            if math_open:
                report("error", f"{name}: unclosed {math_open[0]} within text argument or paragraph cell")
            _, math_open = parent_math.pop()
        for end in sorted(text_scopes.get(i, []), reverse=True):
            parent_math.append((end, math_open))
            math_open = None
        ch = text[i]
        line = text.count("\n", 0, i) + 1
        if ch == "\\":
            match = COMMAND_RE.match(text, i)
            if match is None:
                i += 1
                continue
            cmd = match.group(1)
            if cmd in {"begin", "end"}:
                arg = braced_argument(text, match.end())
                if arg:
                    env = arg[0]
                    if env == "document":
                        report("error", f"{name}:{line}: document environment is not a fragment")
                    if cmd == "begin":
                        environments.append((env, i, line))
                    elif not environments or environments[-1][0] != env:
                        report("error", f"{name}:{line}: mismatched end of {env}")
                    else:
                        opened, start, _ = environments.pop()
                        if opened in MATH_ENVS or opened == "tikzcd":
                            math_ranges.append((start, arg[2]))
            if cmd in {"[", "("}:
                if math_open is not None:
                    report("warning", f"{name}:{line}: nested math delimiters require review")
                else:
                    math_open = (cmd, i)
            elif cmd in {"]", ")"}:
                wanted = "[" if cmd == "]" else "("
                if math_open is None or math_open[0] != wanted:
                    report("error", f"{name}:{line}: mismatched math delimiter \\{cmd}")
                else:
                    math_ranges.append((math_open[1], match.end()))
                    math_open = None
            i = match.end()
            continue
        if ch == "{":
            braces.append(line)
        elif ch == "}":
            if braces:
                braces.pop()
            else:
                report("error", f"{name}:{line}: unmatched closing brace")
        elif ch == "$":
            delim = "$$" if text[i:i + 2] == "$$" else "$"
            if math_open is None:
                math_open = (delim, i)
            elif math_open[0] == delim:
                math_ranges.append((math_open[1], i + len(delim)))
                math_open = None
            else:
                report("error", f"{name}:{line}: mismatched dollar math delimiter")
            i += len(delim)
            continue
        i += 1
    while parent_math:
        if math_open:
            report("error", f"{name}: unclosed {math_open[0]} within text argument or paragraph cell")
        _, math_open = parent_math.pop()
    if braces:
        report("error", f"{name}: unclosed braces opened on lines {braces}")
    if environments:
        report("error", f"{name}: unclosed environments {environments}")
    if math_open:
        report("error", f"{name}: unclosed math delimiter {math_open[0]}")
    diagram_ranges = [(s, e) for cmd, s, e, _ in ranges if cmd == "diagram"]
    for cmd, start, end, line in ranges:
        if cmd == "illegible" and any(s <= start < e for s, e in math_ranges + diagram_ranges):
            report("error", f"{name}:{line}: \\illegible occurs inside mathematics or a diagram")
    for sentinel in ("TODO", "PLACEHOLDER", "TRANSCRIBE HERE"):
        if sentinel in text:
            report("error", f"{name}: unresolved drafting marker {sentinel!r}")
    return original, counts


def parse_utc(value):
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S UTC")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true", help="Check saved pages without requiring all 38")
    parser.add_argument("--require-frozen", action="store_true")
    parser.add_argument("--strict-commands", action="store_true")
    parser.add_argument("--allow-command", action="append", default=[])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    diagnostics = []

    def report(severity, message):
        diagnostics.append({"severity": severity, "message": message})

    files = {}
    for path in sorted((root / "pages").glob("*.tex")):
        match = re.fullmatch(re.escape(PREFIX) + r"_64_scan(\d{3})\.tex", path.name)
        if not match or int(match[1]) not in SCANS:
            report("error", f"Unexpected page filename: {path.name}")
            continue
        files[int(match[1])] = path
    target = set(files) if args.partial else SCANS
    for scan in sorted(SCANS - set(files)):
        if not args.partial:
            report("error", f"Missing page: scan {scan:03d}")
    if not files:
        report("error", "No page files present")
    if files and set(files) != set(range(2, max(files) + 1)):
        report("error", "Saved pages do not form a continuous sequence beginning with scan 002")

    contents, macro_counts = {}, {}
    for scan, path in sorted(files.items()):
        try:
            contents[scan], macro_counts[scan] = check_tex(
                path, scan, report, args.strict_commands, set(args.allow_command))
        except (OSError, UnicodeError) as exc:
            report("error", f"Cannot read {path.name}: {exc}")
    combined = root / f"{PREFIX}_transcription.tex"
    if not combined.is_file():
        report("error", "Combined transcription is missing")
    else:
        expected = "".join(contents[n] + "\n" for n in sorted(contents))
        if combined.read_text(encoding="utf-8") != expected:
            report("error", "Combined transcription is not the exact ordered page concatenation "
                   "with one extra newline after each page file")

    inventory_counts = defaultdict(Counter)
    inventory_rows = 0
    inventory = root / f"{PREFIX}_inventory.csv"
    if not inventory.is_file():
        report("error", "Inventory CSV is missing")
    else:
        with inventory.open(newline="", encoding="utf-8") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != INVENTORY_COLUMNS:
                report("error", f"Wrong inventory columns: {reader.fieldnames}")
            seen = set()
            for line, row in enumerate(reader, 2):
                inventory_rows += 1
                try:
                    scan = int(row.get("scan", ""))
                except (ValueError, TypeError):
                    report("error", f"Inventory line {line}: invalid scan")
                    continue
                if scan not in target or row.get("cote") != "64":
                    report("error", f"Inventory line {line}: wrong or unsaved cote/scan")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    report("error", f"Inventory line {line}: invalid sheet_kind")
                kind = row.get("kind")
                if kind not in KINDS:
                    report("error", f"Inventory line {line}: invalid element kind {kind!r}")
                if row.get("transcribed") != "yes":
                    report("error", f"Inventory line {line}: transcribed must be yes")
                for field in ("element", "position", "first_words_or_objects"):
                    if not (row.get(field) or "").strip():
                        report("error", f"Inventory line {line}: empty {field}")
                identity = (scan, row.get("element"))
                if identity in seen:
                    report("error", f"Inventory line {line}: duplicate element id {identity}")
                seen.add(identity)
                inventory_counts[scan][kind] += 1
        for scan in sorted(target):
            if not inventory_counts[scan]:
                report("error", f"No inventory rows for scan {scan:03d}")
        mapping = {"diagram": "diagram", "figure": "drawing", "margin": "margin note",
                   "inserted": "insertion", "deleted": "deletion"}
        for scan, counts in macro_counts.items():
            for macro, kind in mapping.items():
                if counts[macro] > inventory_counts[scan][kind]:
                    report("warning", f"Scan {scan:03d}: {counts[macro]} \\{macro} macros "
                           f"but {inventory_counts[scan][kind]} {kind} inventory rows; review coverage")

    for filename in [f"{PREFIX}_doubts.md", "CHECK_EVENTS.tsv", "progress.log"]:
        if not (root / filename).is_file():
            report("error", f"Missing required file: {filename}")
    if not args.partial and not (root / f"{PREFIX}_notes.md").is_file():
        report("error", "Research notes file is missing")
    check_events = root / "CHECK_EVENTS.tsv"
    events = 0
    if check_events.is_file():
        with check_events.open(newline="", encoding="utf-8") as stream:
            reader = csv.DictReader(stream, delimiter="\t")
            if reader.fieldnames != ["statement_id", "date", "who", "type", "outcome"]:
                report("error", f"Unexpected CHECK_EVENTS.tsv columns: {reader.fieldnames}")
            for line, row in enumerate(reader, 2):
                events += 1
                if any(not (row.get(k) or "").strip()
                       for k in ("statement_id", "date", "who", "type", "outcome")):
                    report("error", f"CHECK_EVENTS.tsv line {line}: missing required value")
                kind = row.get("type", "")
                if kind not in CHECK_TYPES and not kind.startswith("refuted"):
                    report("warning", f"CHECK_EVENTS.tsv line {line}: review event type {kind!r}")

    frozen = False
    verified_hashes = 0
    log = root / "progress.log"
    if log.is_file():
        lines = log.read_text(encoding="utf-8").splitlines()
        try:
            parse_utc(lines[0])
        except (ValueError, IndexError):
            report("error", "First progress.log line is not a UTC timestamp")
        freezes = [(i, value) for i, value in enumerate(lines)
                   if value.startswith("transcription frozen ")]
        context_lines = [i for i, value in enumerate(lines) if value.startswith("context opened ")]
        if len(freezes) > 1:
            report("error", "More than one transcription freeze marker")
        frozen = bool(freezes)
        if args.require_frozen and not frozen:
            report("error", "Transcription has no freeze marker")
        if context_lines and (not frozen or min(context_lines) < freezes[0][0]):
            report("error", "Context-opening marker precedes the transcription freeze")
        done, audited = {}, {}
        for i, value in enumerate(lines):
            match = re.fullmatch(r"64 scan (\d{3}) done (.+)", value)
            audit = re.fullmatch(r"scan (\d{3}) audited (.+)", value)
            for found, dest, label in [(match, done, "done"), (audit, audited, "audited")]:
                if found:
                    try:
                        parse_utc(found[2])
                    except ValueError:
                        report("error", f"Bad UTC timestamp in {label} event on log line {i+1}")
                    dest[int(found[1])] = i
        for scan in sorted(target):
            if scan not in done:
                report("error", f"No done log entry for scan {scan:03d}")
            if frozen and (scan not in audited or audited[scan] > freezes[0][0]):
                report("error", f"Scan {scan:03d} lacks an audit entry before freeze")
            if frozen and scan in done and done[scan] > freezes[0][0]:
                report("error", f"Scan {scan:03d} marked done after freeze")
        if frozen:
            freeze_index, freeze_line = freezes[0]
            try:
                parse_utc(freeze_line.removeprefix("transcription frozen "))
            except ValueError:
                report("error", "Freeze marker has invalid UTC timestamp")
            hashes = {}
            for value in lines[:freeze_index]:
                match = re.fullmatch(r"(?:sha256|SHA256|SHA-256)\s+([0-9a-fA-F]{64})\s+(.+)", value)
                if not match:
                    match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", value)
                if match:
                    digest, filename = match.groups()
                    if filename in hashes and hashes[filename] != digest.lower():
                        report("error", f"Conflicting pre-freeze hashes for {filename}")
                    hashes.setdefault(filename, digest.lower())
            expected_paths = [f"pages/{files[n].name}" for n in sorted(files)] + [combined.name]
            for filename in expected_paths:
                if filename not in hashes:
                    report("error", f"Missing pre-freeze SHA-256 in log for {filename}")
                    continue
                path = root / filename
                actual = hashlib.sha256(path.read_bytes()).hexdigest()
                if actual != hashes[filename]:
                    report("error", f"FROZEN HASH CHANGED: {filename}")
                else:
                    verified_hashes += 1
            if context_lines and not any("unchanged" in v.lower()
                                         for v in lines[max(context_lines) + 1:]):
                report("warning", "No final unchanged-hashes assertion after context-opening marker")
    result = {
        "scope": "Structural checks only; not visual completeness or transcription accuracy.",
        "root": str(root), "mode": "partial" if args.partial else "complete",
        "pages": len(files), "inventory_rows": inventory_rows, "check_events": events,
        "frozen": frozen, "verified_hashes": verified_hashes,
        "errors": sum(d["severity"] == "error" for d in diagnostics),
        "warnings": sum(d["severity"] == "warning" for d in diagnostics),
        "diagnostics": diagnostics,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["scope"])
        print(f"{len(files)} page files; {inventory_rows} inventory rows; "
              f"{events} check events; {verified_hashes} unchanged frozen hashes")
        for item in diagnostics:
            print(f'{item["severity"].upper()}: {item["message"]}')
        print(f'{result["errors"]} errors; {result["warnings"]} warnings')
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
