#!/usr/bin/env python3
"""Mechanical validation of the MPL 15/18 transcription package.

This program checks structure only. It does not interpret the manuscript,
assess reading accuracy, infer missing textual elements, or claim that an
inventory is exhaustive. It never opens source images or context archives.

Usage:
    python records/validate_structure.py --partial
    python records/validate_structure.py
    python records/validate_structure.py --json

The default package root is this script's parent directory's parent.
Preferred frozen-hash log format (one line for each page and the combined file):
    <64 hexadecimal SHA-256 digits>  <package-relative filename>
The event ``transcription frozen <UTC timestamp>`` activates complete frozen
hash coverage checks. Both initial and repeated identical hash records work.

Exit status: 0 = structural checks passed at the requested scope; 1 = errors;
2 = command-line usage error. A partial-mode pass NEVER means a complete
transcription. Unknown LaTeX command names are reported for human review, not
rejected as invented custom macros: a finite list cannot identify every
standard LaTeX or tikz-cd command.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


PREFIX = "MPL_15_195-228+18_002-017"
EXPECTED = tuple([(15, n) for n in range(195, 229)] +
                 [(18, n) for n in range(2, 18) if n != 8])
EXPECTED_SET = set(EXPECTED)
FIELDS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
SHEET_KINDS = {"text", "typed", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note",
                 "insertion", "deletion"}
CUSTOM = {"cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
          "uline", "uuline", "diagram", "figure", "unsure", "illegible"}
# This list is advisory, not a restrictive TeX whitelist.
COMMON = set("""
begin end frac dfrac tfrac cfrac binom dbinom tbinom sqrt root of over atop choose
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
mathbb mathcal mathfrak mathscr mathrm mathbf mathit mathsf mathtt boldsymbol bm
text textrm textbf textit textsf texttt textnormal emph underline overline bar
hat widehat tilde widetilde vec dot ddot dddot acute grave breve check mathring
overset underset stackrel overbrace underbrace phantom hphantom vphantom smash
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon
phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi
Omega digamma aleph beth gimel daleth ell hbar imath jmath wp Re Im partial nabla
infty emptyset varnothing forall exists nexists neg lnot top bot angle triangle
prime backprime degree o O S P L l i j aa AA ae AE oe OE ss LaTeX TeX
times otimes oplus ominus odot oslash circ bullet cdot ast star diamond bigcirc
div pm mp cap cup uplus sqcap sqcup setminus smallsetminus wedge vee land lor
bigcap bigcup biguplus bigsqcup bigwedge bigvee bigotimes bigoplus bigodot
sum prod coprod int iint iiint iiiint oint lim limsup liminf inf sup max min
ker dim hom Hom Ext Tor Aut End Gal Spec Proj Pic CH NS H R G Z Q C N D A
det deg gcd Pr mod bmod pmod pod sin cos tan cot sec csc sinh cosh tanh coth
arcsin arccos arctan exp log ln lg arg id tr rank span supp ord char codim
le leq leqslant ge geq geqslant ne neq equiv sim simeq cong approx asymp
propto ll gg lesssim gtrsim prec succ preceq succeq parallel perp mid nmid
in ni notin owns subset supset subseteq supseteq subsetneq supsetneq
sqsubset sqsupset sqsubseteq sqsupseteq vdash dashv models Vdash
to mapsto gets arrow ar ar[r] rightarrow leftarrow leftrightarrow
longrightarrow longleftarrow longleftrightarrow Longrightarrow Longleftarrow
Longleftrightarrow Rightarrow Leftarrow Leftrightarrow hookrightarrow
hookleftarrow twoheadrightarrow twoheadleftarrow rightleftarrows leftrightarrows
rightrightarrows leftleftarrows rightleftharpoons leftrightharpoons
longmapsto multimap nearrow searrow nwarrow swarrow uparrow downarrow updownarrow
Uparrow Downarrow Updownarrow leadsto rightsquigarrow xrightarrow xleftarrow
cdots ldots vdots ddots dots dotsc dotsb dotsm dotsi dotso colon coloneqq
langle rangle lbrace rbrace lvert rvert lVert rVert vert Vert backslash slash
quad qquad enspace thinspace medspace thickspace negthinspace hspace vspace
hfill vfill kern mkern noindent par newline linebreak pagebreak newpage clearpage
smallskip medskip bigskip strut ensuremath displaystyle textstyle scriptstyle
scriptscriptstyle limits nolimits nonumber notag tag label ref eqref footnote
footnotemark footnotetext index item hline cline multicolumn multirow hdotsfor
arraystretch arraycolsep tabcolsep centering raggedright raggedleft
small large Large LARGE huge Huge tiny scriptsize footnotesize normalsize
upshape itshape bfseries mdseries normalfont rm sf tt cal bf mit it sl sc
draw path node coordinate fill filldraw clip foreach matrix pgfextra
tikz tikzset tikzcdset pgfmathsetmacro pgfmathparse pgfmathresult
operatorname mathop mathrel mathbin mathord mathpunct mathopen mathclose
substack substacks sideset prescript accent H c d b r t u v k
textquotedblleft textquotedblright textquoteleft textquoteright
textendash textemdash textdegree textsuperscript textsuperscript textsuperscript
textsubscript textbackslash textasciicircum textasciitilde textbar textless
textgreater textbraceleft textbraceright verb protect relax null not
""".split())


def page_name(cote: int, scan: int) -> str:
    return f"{PREFIX}_{cote}_scan{scan:03d}.tex"


def without_comments(text: str) -> str:
    """Remove unescaped %-comments while preserving physical line numbers."""
    kept = []
    for line in text.splitlines(keepends=True):
        stop = len(line)
        for pos, char in enumerate(line):
            if char != "%":
                continue
            slash_count = 0
            j = pos - 1
            while j >= 0 and line[j] == "\\":
                slash_count += 1
                j -= 1
            if slash_count % 2 == 0:
                stop = pos
                break
        kept.append(line[:stop] + ("\n" if stop < len(line) and line.endswith("\n") else ""))
    return "".join(kept)


def brace_errors(text: str) -> list[str]:
    """Count grouping braces, skipping comments and escaped control symbols."""
    cleaned = without_comments(text)
    stack = []
    problems = []
    line = 1
    i = 0
    while i < len(cleaned):
        char = cleaned[i]
        if char == "\n":
            line += 1
        elif char == "\\":
            if cleaned.startswith("\\verb", i):
                j = i + 5
                if j < len(cleaned) and cleaned[j] == "*":
                    j += 1
                if j < len(cleaned) and not cleaned[j].isspace():
                    close = cleaned.find(cleaned[j], j + 1)
                    if close != -1:
                        line += cleaned[i:close + 1].count("\n")
                        i = close + 1
                        continue
            # In \{, \}, \%, and \\, the following char is a control symbol.
            if i + 1 < len(cleaned) and not cleaned[i + 1].isalpha():
                i += 2
                continue
        elif char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                problems.append(f"unmatched closing brace on line {line}")
        i += 1
    problems.extend(f"unmatched opening brace on line {n}" for n in stack)
    return problems


def expected_markers(present: set[tuple[int, int]]) -> list[tuple[str, int]]:
    output = []
    last = None
    for cote, scan in EXPECTED:
        if (cote, scan) not in present:
            continue
        if cote != last:
            output.append(("cotefile", cote))
            last = cote
        output.append(("scanpage", scan))
    return output


def markers(text: str) -> list[tuple[str, int]]:
    return [(kind, int(number)) for kind, number in
            re.findall(r"\\(cotefile|scanpage)\s*\{\s*(\d+)\s*\}",
                       without_comments(text))]


def extract_hash_record(line: str):
    patterns = [
        r"^\s*([0-9a-fA-F]{64})\s+\*?(.+?)\s*$",
        r"^\s*SHA[-_ ]?256\s+([0-9a-fA-F]{64})\s+\*?(.+?)\s*$",
        r"^\s*SHA[-_ ]?256\s*\((.+?)\)\s*=\s*([0-9a-fA-F]{64})\s*$",
        r"^\s*SHA[-_ ]?256\s+(.+?)\s+([0-9a-fA-F]{64})\s*$",
    ]
    for index, pattern in enumerate(patterns):
        match = re.match(pattern, line, flags=re.IGNORECASE)
        if match:
            if index < 2:
                digest, name = match.groups()
            else:
                name, digest = match.groups()
            return name.strip().strip('"'), digest.lower()
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true",
                        help="allow unfinished/missing expected deliverables; never claim completeness")
    parser.add_argument("--json", action="store_true", help="print one JSON report")
    parser.add_argument("--standard-command", action="append", default=[],
                        help="additional standard TeX command name for advisory reporting")
    args = parser.parse_args()
    root = args.root.resolve()
    errors = []
    warnings = []
    pending = []
    counts = {}
    command_counts = Counter()
    unresolved_commands = defaultdict(set)

    def absent(message):
        (pending if args.partial else errors).append(message)

    def read(path):
        try:
            return path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            errors.append(f"Cannot read {path.relative_to(root)}: {exc}")
            return None

    def check_tex(path, text):
        name = path.relative_to(root).as_posix()
        for issue in brace_errors(text):
            errors.append(f"{name}: {issue}")
        cleaned = without_comments(text)
        if re.search(r"\\documentclass\b|\\(?:begin|end)\s*\{document\}", cleaned):
            errors.append(f"{name}: document wrapper present; deliverable must be a fragment")
        for match in re.finditer(r"\\(?:newcommand|renewcommand|providecommand|DeclareRobustCommand|def|gdef|edef|xdef)\b", cleaned):
            errors.append(f"{name}: local command definition present ({match.group()})")
        if re.search(r"\\(?:input|include|includegraphics|includeonly)\b", cleaned):
            errors.append(f"{name}: external inclusion command present")
        found = Counter(re.findall(r"\\([A-Za-z]+)\*?", cleaned))
        if path.parent.name == "pages":
            command_counts.update({key: value for key, value in found.items() if key in CUSTOM})
        for command in found.keys() - CUSTOM - COMMON - set(args.standard_command):
            unresolved_commands[command].add(name)

    required = [
        f"{PREFIX}_transcription.tex", f"{PREFIX}_doubts.md",
        f"{PREFIX}_inventory.csv", f"{PREFIX}_notes.md", "progress.log",
    ]
    for name in required:
        if not (root / name).is_file():
            absent(f"Missing required deliverable: {name}")
    actual_paths = list((root / "pages").glob("*.tex")) if (root / "pages").is_dir() else []
    expected_names = {page_name(c, n) for c, n in EXPECTED}
    extra = sorted(path.name for path in actual_paths if path.name not in expected_names)
    if extra:
        errors.append("Unexpected page files: " + ", ".join(extra))
    present = set()
    page_texts = {}
    for cote, scan in EXPECTED:
        path = root / "pages" / page_name(cote, scan)
        if not path.is_file():
            absent(f"Missing page: cote {cote}, scan {scan:03d}")
            continue
        present.add((cote, scan))
        text = read(path)
        if text is None:
            continue
        page_texts[(cote, scan)] = text
        check_tex(path, text)
        found = markers(text)
        if [n for kind, n in found if kind == "scanpage"] != [scan]:
            errors.append(f"{path.name}: must contain exactly its own scanpage marker ({scan})")
        if any(n != cote for kind, n in found if kind == "cotefile"):
            errors.append(f"{path.name}: cotefile marker names a different cote")
        if sum(kind == "cotefile" for kind, _ in found) > 1:
            errors.append(f"{path.name}: repeated cotefile marker")
        remainder = re.sub(r"\\(?:cotefile|scanpage|mspage)\s*\{[^{}]*\}", "", without_comments(text))
        if not remainder.strip():
            errors.append(f"{path.name}: no transcription content beyond page markers")
    counts["expected_pages"] = len(EXPECTED)
    counts["page_files_present"] = len(present)
    counts["page_files_readable"] = len(page_texts)

    combined_path = root / required[0]
    if combined_path.is_file():
        combined = read(combined_path)
        if combined is not None:
            check_tex(combined_path, combined)
            found = markers(combined)
            target = expected_markers(present if args.partial else EXPECTED_SET)
            counts["combined_scanpage_markers"] = sum(k == "scanpage" for k, _ in found)
            if found != target:
                errors.append("Combined transcription cotefile/scanpage sequence does not match "
                              + ("the present pages in archive order" if args.partial else "all 49 pages in archive order"))
            stripped = without_comments(combined).lstrip()
            if stripped and not stripped.startswith("\\cotefile{15}"):
                errors.append("Combined transcription does not begin with \\cotefile{15}")
            # Compare each combined page body mechanically, allowing the cote
            # boundary marker to live either in a page file or in the assembly.
            def normalized_body(value):
                value = re.sub(r"\\cotefile\s*\{\s*\d+\s*\}", "", without_comments(value))
                return value.strip()
            chunks = re.split(r"(?=\\scanpage\s*\{\s*\d+\s*\})", without_comments(combined))
            for chunk in chunks[1:]:
                match = re.match(r"\\scanpage\s*\{\s*(\d+)\s*\}", chunk)
                if not match:
                    continue
                scan = int(match.group(1))
                candidates = [key for key in page_texts if key[1] == scan]
                if len(candidates) == 1 and normalized_body(chunk) != normalized_body(page_texts[candidates[0]]):
                    errors.append(f"Combined body differs from page file for cote {candidates[0][0]}, scan {scan:03d}")

    inventory_pages = set()
    inventory_count = 0
    inventory_path = root / required[2]
    if inventory_path.is_file():
        text = read(inventory_path)
        if text is not None:
            try:
                reader = csv.DictReader(io.StringIO(text, newline=""))
                if reader.fieldnames != FIELDS:
                    errors.append(f"Inventory columns differ from required ordered columns: {FIELDS}")
                seen_elements = set()
                page_sheets = defaultdict(set)
                for line, row in enumerate(reader, start=2):
                    inventory_count += 1
                    if None in row or any(row.get(name) is None for name in FIELDS):
                        errors.append(f"Inventory line {line}: malformed CSV row")
                        continue
                    try:
                        key = (int(row["cote"]), int(row["scan"]))
                    except (ValueError, KeyError):
                        errors.append(f"Inventory line {line}: cote/scan must be integers")
                        continue
                    inventory_pages.add(key)
                    if key not in EXPECTED_SET:
                        errors.append(f"Inventory line {line}: unexpected cote/scan {key}")
                    if row["transcribed"].strip() != "yes":
                        errors.append(f"Inventory line {line}: transcribed is not yes")
                    if row["sheet_kind"].strip() not in SHEET_KINDS:
                        errors.append(f"Inventory line {line}: unknown sheet_kind {row['sheet_kind']!r}")
                    if row["kind"].strip() not in ELEMENT_KINDS:
                        errors.append(f"Inventory line {line}: unknown kind {row['kind']!r}")
                    page_sheets[key].add(row["sheet_kind"].strip())
                    element = row["element"].strip()
                    element_key = (*key, element)
                    if not element:
                        errors.append(f"Inventory line {line}: empty element identifier")
                    elif element_key in seen_elements:
                        errors.append(f"Inventory line {line}: repeated element identifier {element_key}")
                    seen_elements.add(element_key)
                    for field in ("position", "first_words_or_objects"):
                        if not row[field].strip():
                            errors.append(f"Inventory line {line}: empty {field}")
                for key, kinds in page_sheets.items():
                    if len(kinds) > 1:
                        errors.append(f"Inventory has inconsistent sheet_kind on cote {key[0]}, scan {key[1]:03d}: {sorted(kinds)}")
            except csv.Error as exc:
                errors.append(f"Cannot parse inventory CSV: {exc}")
    counts["inventory_rows"] = inventory_count
    counts["inventory_pages"] = len(inventory_pages & EXPECTED_SET)
    for cote, scan in sorted(present - inventory_pages):
        errors.append(f"Existing page lacks inventory rows: cote {cote}, scan {scan:03d}")
    for cote, scan in sorted((inventory_pages & EXPECTED_SET) - present):
        errors.append(f"Inventory claims a page without a page file: cote {cote}, scan {scan:03d}")

    done = set()
    audited = set()
    frozen = False
    frozen_hashes = defaultdict(list)
    log_path = root / "progress.log"
    if log_path.is_file():
        log = read(log_path)
        if log is not None:
            first = log.splitlines()[0] if log.splitlines() else ""
            if not re.search(r"\d{4}-\d\d-\d\d[ T]\d\d:\d\d:\d\d(?:\s*UTC|Z|\+00:00)", first):
                errors.append("progress.log first line is not an explicit UTC timestamp")
            current_cote = None
            for line_number, line in enumerate(log.splitlines(), start=1):
                if re.search(r"\btranscription frozen\b", line, re.I):
                    frozen = True
                heading = re.match(r"\s*(?:cote(?:file)?|file|audit(?:ing)?(?:\s+cote)?)[\s:=]+(15|18)\b", line, re.I)
                if heading:
                    current_cote = int(heading.group(1))
                explicit = re.match(r"\s*(?:(?:cote|file)\s+)?(15|18)\s+scan\s+(\d+)\s+(done|audited)\b", line, re.I)
                bare = re.match(r"\s*scan\s+(\d+)\s+(done|audited)\b", line, re.I)
                key = None
                status = None
                if explicit:
                    cote, scan, status = explicit.groups()
                    key = (int(cote), int(scan))
                    current_cote = key[0]
                elif bare:
                    scan, status = bare.groups()
                    scan = int(scan)
                    if (current_cote, scan) in EXPECTED_SET:
                        key = (current_cote, scan)
                    else:
                        candidates = [value for value in EXPECTED if value[1] == scan]
                        if len(candidates) == 1:
                            key = candidates[0]
                        else:
                            errors.append(f"progress.log line {line_number}: audit/done record cannot be assigned to a cote")
                if key is not None:
                    if key not in EXPECTED_SET:
                        errors.append(f"progress.log line {line_number}: unexpected cote/scan {key}")
                    else:
                        (done if status.lower() == "done" else audited).add(key)
                record = extract_hash_record(line)
                if record:
                    name, digest = record
                    path = Path(name)
                    if not path.is_absolute():
                        path = root / path
                    path = path.resolve()
                    try:
                        relative = path.relative_to(root).as_posix()
                    except ValueError:
                        warnings.append(f"progress.log line {line_number}: ignoring hash outside package root")
                        continue
                    frozen_hashes[relative].append(digest)
    counts["done_log_pages"] = len(done)
    counts["audited_log_pages"] = len(audited)
    counts["frozen"] = frozen
    for cote, scan in sorted(present - done):
        errors.append(f"Existing page lacks done log record: cote {cote}, scan {scan:03d}")
    for cote, scan in sorted(done - present):
        errors.append(f"Done log record has no page file: cote {cote}, scan {scan:03d}")
    audit_target = EXPECTED_SET if not args.partial or frozen else set()
    for cote, scan in sorted(audit_target - audited):
        absent(f"Missing second-reading audit log record: cote {cote}, scan {scan:03d}")
    if audited - done:
        errors.append("Audit records exist for pages without done records")
    if not frozen:
        absent("Transcription not recorded as frozen")
    if frozen and present != EXPECTED_SET:
        errors.append("Transcription marked frozen before all 49 page files are present")
    hash_target = {"pages/" + page_name(c, n) for c, n in EXPECTED} | {required[0]}
    verified_hashes = 0
    for name, digests in frozen_hashes.items():
        if len(set(digests)) > 1:
            errors.append(f"Conflicting SHA-256 records for {name}")
        path = root / name
        if not path.is_file():
            errors.append(f"Hash record names missing file: {name}")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if any(digest != actual for digest in digests):
            errors.append(f"Frozen SHA-256 mismatch: {name}")
        else:
            verified_hashes += 1
    if frozen:
        for name in sorted(hash_target - frozen_hashes.keys()):
            errors.append(f"Missing frozen SHA-256 record: {name}")
    counts["hash_records_unique_files"] = len(frozen_hashes)
    counts["hashes_verified"] = verified_hashes

    if unresolved_commands:
        warnings.append("Unclassified LaTeX commands require human review; no error is inferred merely from their names")
    report = {
        "mode": "partial" if args.partial else "final",
        "root": str(root), "structural_checks_pass": not errors,
        "completeness_asserted": False,
        "scope_note": "Mechanical structure only; reading accuracy and inventory exhaustiveness require visual audit.",
        "counts": counts,
        "approved_custom_macro_occurrences_in_page_files": dict(sorted(command_counts.items())),
        "unclassified_commands": {key: sorted(value) for key, value in sorted(unresolved_commands.items())},
        "errors": errors, "pending": pending, "warnings": warnings,
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        state = "PASS" if not errors else "FAIL"
        print(f"{state}: {'partial' if args.partial else 'final'} structural validation")
        print(f"Page files: {len(present)}/49; inventory pages: {counts['inventory_pages']}/49; "
              f"done records: {len(done)}/49; audit records: {len(audited)}/49.")
        print(f"Inventory rows: {inventory_count}; frozen: {frozen}; verified hashes: {verified_hashes}.")
        print(report["scope_note"])
        if args.partial:
            print("Partial mode: this result does not certify a complete transcription.")
        for label, items in [("ERROR", errors), ("PENDING", pending), ("WARNING", warnings)]:
            for item in items:
                print(f"{label}: {item}")
        if unresolved_commands:
            print("Unclassified commands: " + ", ".join("\\" + value for value in sorted(unresolved_commands)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
