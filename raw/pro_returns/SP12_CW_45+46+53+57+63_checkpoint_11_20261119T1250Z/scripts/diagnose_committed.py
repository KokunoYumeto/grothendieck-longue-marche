#!/usr/bin/env python3
"""Snapshot mechanical bookkeeping for committed outputs; never edit readings.

Reads output files and the explicitly permitted filename-map TSV only. It never
follows witness, scan, or context paths from that map, and never compiles TeX.
Writes timestamped diagnostics plus a tooling.log entry. Exit codes are 0 for
stable captured inputs with no structural findings, 1 for structural/tooling
errors, and 2 for an unstable capture. An incomplete archive
can have internally consistent committed outputs; the report keeps these facts
separate and does not claim visual, editorial, or full-archive verification.
"""

from __future__ import annotations

import argparse
import ast
import bisect
from collections import Counter
import csv
import hashlib
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import re
import stat
import sys


COLLATION = "folder their_page our_scan line their_reading codex_reading final_reading scan_shows kind marked_in_H confidence".split()
INVENTORY = "scan sheet_kind hand element kind position first_words_or_objects transcribed".split()
MAP_FIELDS = "folder cote our_scan their_page codex_file hua_has".split()
KINDS = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state (struck given live or live given struck)", "insertion or placement",
    "abbreviation expanded or spelling modernised", r"readable ink left as \ill{}",
    "drawing or diagram", "other",
}
INVENTORY_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover"}
CONFIDENCES = {"high", "medium", "low"}
# This is a recognition registry, not an exhaustive grammar or validity test.
STANDARD = set("""
begin end documentclass usepackage RequirePackage newcommand renewcommand providecommand
DeclareRobustCommand DeclareMathOperator newenvironment renewenvironment def gdef edef xdef
let if ifx ifnum ifdim ifmmode else fi csname endcsname catcode ExplSyntaxOn ExplSyntaxOff
par noindent indent medskip smallskip bigskip newpage clearpage pagebreak linebreak newline
begingroup endgroup strut parbox linewidth
hfill vfill quad qquad enspace enskip hspace vspace thinspace negthinspace label ref pageref
cite footnote footnotemark footnotetext marginpar normalmarginpar reversemarginpar
section subsection subsubsection paragraph subparagraph item setlength addtolength newlength
setcounter addtocounter newcounter textbf textit textsf texttt textrm textsl textsc textnormal
textup textmd emph uline uuline sout uwave xout normalfont bfseries itshape sffamily ttfamily
rmfamily mdseries scshape slshape upshape tiny scriptsize footnotesize small normalsize large
Large LARGE huge Huge centering raggedright raggedleft hline cline multicolumn multirow
toprule midrule bottomrule framebox mbox fbox raisebox rule phantom hphantom vphantom
color textcolor colorbox fcolorbox includegraphics caption captionof url href hyperref verb
left right middle big Big bigg Bigg bigl bigr bigm Bigl Bigr Bigm biggl biggr biggm Biggl
Biggr Biggm frac dfrac tfrac cfrac binom dbinom tbinom sqrt overline underline bar hat
widehat tilde widetilde vec acute grave breve check dot ddot dddot ddddot mathring
overrightarrow overleftarrow overleftrightarrow underbrace overbrace overset underset
stackrel substack operatorname operatornamewithlimits text mathrm mathbf mathit mathsf mathtt
mathcal mathscr mathbb mathfrak mathrel mathbin mathop mathord mathpunct mathopen mathclose
boldsymbol bm displaystyle textstyle scriptstyle scriptscriptstyle limits nolimits nonumber
notag tag eqref sideset colon pmod bmod mod pod
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa varkappa lambda
mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
sin cos tan cot sec csc sinh cosh tanh coth arcsin arccos arctan log ln exp lim limsup
liminf sup inf max min arg det dim gcd hom ker deg Pr varprojlim varinjlim
le leq leqslant ge geq geqslant neq ne equiv sim simeq cong approx asymp propto in ni notin
subset supset subseteq supseteq subsetneq supsetneq preceq succeq prec succ parallel perp
mid vdash dashv models smile frown doteq triangleq not
sum prod coprod int iint iiint oint oiint bigcup bigcap bigsqcup bigvee bigwedge bigotimes
bigoplus biguplus cup cap sqcup sqcap vee wedge uplus setminus smallsetminus land lor lnot
neg forall exists nexists emptyset varnothing complement infty partial nabla ell hbar
imath jmath aleph beth gimel daleth Re Im wp prime degree ldots cdots vdots ddots dots
dotsb dotsc dotsm dotsi dotso cdot times div pm mp ast star circ bullet oplus ominus otimes
oslash odot dagger ddagger amalg wr triangle Box Diamond diamond angle measuredangle
sphericalangle bot top flat natural sharp checkmark
rightarrow leftarrow leftrightarrow Rightarrow Leftarrow Leftrightarrow longrightarrow
longleftarrow longleftrightarrow Longrightarrow Longleftarrow Longleftrightarrow mapsto
longmapsto hookrightarrow hookleftarrow rightarrowtail leftarrowtail twoheadrightarrow
twoheadleftarrow rightsquigarrow leftrightsquigarrow nearrow searrow swarrow nwarrow uparrow
downarrow updownarrow Uparrow Downarrow Updownarrow to gets iff implies impliedby leadsto
rightharpoonup rightharpoondown leftharpoonup leftharpoondown rightleftharpoons leftrightharpoons
xrightarrow xleftarrow langle rangle lvert rvert vert lVert rVert Vert lceil rceil lfloor
rfloor backslash lbrace rbrace lbrack rbrack
tikz tikzset usetikzlibrary usepgflibrary draw path node coordinate fill filldraw clip shade
shadedraw pattern matrix foreach pgfmathsetmacro pgfmathsetlengthmacro pgfmathparse pgfmathresult
pgfplotsset addplot nodepart graph edge scope ar arrow rar lar uar dar drar dlar urar ular
tikzcdset tikzcdmatrixname
c v u H t b d r k o O aa AA ae AE oe OE ss i j S P textcircled textsuperscript textsubscript
""".split())
CONTROL_SYMBOLS = set("'\"`^~=.,;:!/-\\ ()[]{}%&#$_\n")
HELPERS = {"_tex_control", "_tex_group_end", "_active_tex_source", "_split_unsure_alternatives", "_unsure_entries", "_normalize_doubt_whitespace", "_unsure_confidence_detail", "_audit_source_text", "_audit_json_loads", "_validate_audit_confidence"}


def stamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def signature(path):
    try:
        value = path.lstat()
        return [value.st_mode, value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns]
    except FileNotFoundError:
        return None


def file_sets(root):
    result = {}
    for directory, suffix in (("pages", ".tex"), ("decisions", ".json")):
        parent = root / directory
        if parent.is_symlink():
            raise ValueError(f"Refusing symlinked output directory: {directory}")
        result[directory] = sorted(path.name for path in parent.glob("*" + suffix)) if parent.is_dir() else []
    return result


def capture(root, page_map):
    suffixes = ["transcription.tex", "changes.md", "collation.tsv", "doubts.md", "inventory.csv", "notes.md"]
    required = [f"{root.name}_{suffix}" for suffix in suffixes] + ["progress.log", "CHECK_EVENTS.tsv"]
    last = None
    for attempt in range(1, 4):
        names = file_sets(root)
        paths = {name: root / name for name in required + ["PREAMBLE.tex", "notation.md", "scripts/review.py", "audit_confidence.json"]}
        paths["@page_map_metadata"] = page_map
        for directory, filenames in names.items():
            paths.update({directory + "/" + name: root / directory / name for name in filenames})
        before = {name: signature(path) for name, path in paths.items()}
        content, raw_content, read_errors = {}, {}, []
        # Presence checks alone suffice for prose/log artifacts that are not
        # inputs to a structural comparison. Do not read their prose here.
        metadata_only = {f"{root.name}_{suffix}" for suffix in ("changes.md", "notes.md")} | {"progress.log"}
        started = stamp()
        for name, path in paths.items():
            if name == "audit_confidence.json" and before[name] is None:
                continue
            if before[name] is None or not stat.S_ISREG(before[name][0]):
                read_errors.append(f"Missing, symlinked, or non-regular input: {name}")
                continue
            if name in metadata_only:
                continue
            try:
                raw_content[name] = path.read_bytes()
                content[name] = raw_content[name].decode("utf-8-sig")
            except (OSError, UnicodeError) as exc:
                read_errors.append(f"Cannot read UTF-8 output/metadata {name}: {exc}")
        after = {name: signature(path) for name, path in paths.items()}
        stable = before == after and names == file_sets(root)
        last = {"started_utc": started, "ended_utc": stamp(), "attempt": attempt, "stable": stable,
                "required": required, "signatures": before, "content": content, "raw_content": raw_content,
                "names": names, "read_errors": read_errors}
        if stable:
            return last
    return last


def parse_table(text, delimiter, expected, label, errors):
    if text is None:
        return None
    try:
        rows = list(csv.reader(io.StringIO(text), delimiter=delimiter, strict=True))
    except csv.Error as exc:
        errors.append(f"{label}: malformed table ({exc}).")
        return None
    if not rows:
        errors.append(f"{label}: missing header.")
        return None
    headers = rows[0]
    if len(set(headers)) != len(headers) or any(not cell for cell in headers):
        errors.append(f"{label}: duplicate or empty header.")
    if expected is not None and headers != expected:
        errors.append(f"{label}: required columns/order differ.")
        return None
    result = []
    for number, row in enumerate(rows[1:], start=2):
        if not row or not any(row):
            continue
        if len(row) != len(headers):
            errors.append(f"{label}: wrong field count at record {number}.")
            continue
        result.append(dict(zip(headers, row)))
    return headers, result


def literal_json(text, label, errors):
    duplicate_keys = []
    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                duplicate_keys.append(key)
            result[key] = value
        return result
    try:
        result = json.loads(text, object_pairs_hook=hook)
    except (ValueError, TypeError) as exc:
        errors.append(f"{label}: invalid JSON ({exc}).")
        return None
    if duplicate_keys:
        errors.append(f"{label}: duplicate JSON keys {sorted(set(duplicate_keys))}.")
        return None
    if not isinstance(result, dict):
        errors.append(f"{label}: decision record must be an object.")
        return None
    return result


def load_helpers(source):
    # Execute only the existing pure parser helpers. In particular, do not run
    # review.py's top-level witness-map loader, commit(), or any rebuild method.
    tree = ast.parse(source)
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in HELPERS]
    if {node.name for node in functions} != HELPERS:
        raise ValueError("The required literal parser helpers are absent from scripts/review.py.")
    namespace = {"re": re, "json": json, "hashlib": hashlib}
    exec(compile(ast.Module(body=functions, type_ignores=[]), "<literal-output-parser>", "exec"), namespace)
    return namespace


def without_comments(text, control):
    result = list(text)
    index = 0
    while index < len(text):
        if text[index] == "\\":
            _, index = control(text, index)
        elif text[index] == "%":
            end = text.find("\n", index)
            end = len(text) if end < 0 else end
            result[index:end] = " " * (end - index)
            index = end
        else:
            index += 1
    return "".join(result)


def custom_commands(preamble, control):
    text = without_comments(preamble, control)
    commands = set()
    pattern = r"\\(?:newcommand|renewcommand|providecommand|DeclareRobustCommand)\*?\s*(?:\{\s*\\([A-Za-z@]+)\s*\}|\\([A-Za-z@]+))"
    for match in re.finditer(pattern, text):
        commands.add(match.group(1) or match.group(2))
    commands.update(re.findall(r"\\(?:def|gdef|edef|xdef)\s*\\([A-Za-z@]+)", text))
    return commands


def tex_checks(text, page, helpers, allowed):
    active = helpers["_active_tex_source"](text)
    starts = [0] + [match.end() for match in re.finditer("\n", active)]
    def location(index):
        line = bisect.bisect_right(starts, index)
        return {"file": page, "line": line, "column": index - starts[line - 1] + 1}
    stack, braces, unknown, scan_markers = [], [], [], []
    index = 0
    while index < len(active):
        char = active[index]
        if char == "\\":
            start = index
            command, index = helpers["_tex_control"](active, index)
            if command not in allowed and command not in CONTROL_SYMBOLS:
                unknown.append({"command": command, **location(start)})
            if command == "scanpage":
                cursor = index
                while cursor < len(active) and active[cursor].isspace():
                    cursor += 1
                end = helpers["_tex_group_end"](active, cursor)
                if end and active[cursor] == "{":
                    scan_markers.append(active[cursor + 1:end - 1].strip())
            continue
        if char == "{":
            stack.append(index)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                braces.append({"problem": "unmatched closing brace", **location(index)})
        index += 1
    braces.extend({"problem": "unmatched opening brace", **location(index)} for index in stack)
    entries, notes = helpers["_unsure_entries"](text)
    return braces, unknown, scan_markers, entries, notes


def csv_value(value):
    return "" if value is None else str(value)


def compare_rows(actual, expected, headers, label, errors):
    if actual is None:
        return {"checked": False}
    tuples = [tuple(row[key] for key in headers) for row in actual]
    expected = [tuple(csv_value(cell) for cell in row) for row in expected]
    if tuples != expected:
        errors.append(f"{label}: rows/order differ from existing decision metadata ({len(tuples)} actual; {len(expected)} expected).")
    return {"checked": True, "actual_rows": len(tuples), "expected_rows": len(expected),
            "exact_order_match": tuples == expected,
            "missing_row_instances": sum((Counter(expected) - Counter(tuples)).values()),
            "extra_row_instances": sum((Counter(tuples) - Counter(expected)).values())}


def doubts_table_shape(text):
    """Recognize the generated table outside fenced/indented code examples."""
    expected = ["scan", "line/place", "reading", "alternatives", "confidence"]
    active, fence = [], None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is None and not line.startswith(("    ", "\t")):
            active.append(stripped)
    for index, line in enumerate(active[:-1]):
        if [cell.strip() for cell in line.strip("|").split("|")] != expected:
            continue
        separators = [cell.strip() for cell in active[index + 1].strip("|").split("|")]
        if len(separators) != 5 or not all(re.fullmatch(r":?-{3,}:?", cell) for cell in separators):
            continue
        rows, malformed = 0, 0
        for data in active[index + 2:]:
            if not data.startswith("|"):
                break
            rows += 1
            malformed += len(data.strip("|").split("|")) != 5
        return {"present": True, "data_rows": rows, "malformed_rows": malformed}
    return {"present": False, "data_rows": 0, "malformed_rows": 0}


def audit(root, snapshot):
    content = snapshot["content"]
    errors = list(snapshot["read_errors"])
    if not snapshot["stable"]:
        errors.append("Inputs changed during all capture attempts; this snapshot is unstable and comparisons are provisional.")
    missing_required = [name for name in snapshot["required"] if snapshot["signatures"].get(name) is None or not stat.S_ISREG(snapshot["signatures"][name][0])]
    empty_required = [name for name in snapshot["required"] if snapshot["signatures"].get(name) and snapshot["signatures"][name][3] == 0]
    errors.extend("Empty required artifact: " + name for name in empty_required)
    parsed_map = parse_table(content.get("@page_map_metadata"), "\t", None, "page-map metadata", errors)
    if parsed_map is None or not set(MAP_FIELDS).issubset(parsed_map[0]):
        raise ValueError("The permitted page-map metadata lacks required filename/identity columns.")
    # Deliberately discard the context and witness-text filename fields.
    rows = [{field: row[field] for field in MAP_FIELDS} for row in parsed_map[1]]
    page_names = [Path(row["codex_file"]).name for row in rows]
    if len(set(page_names)) != len(page_names):
        errors.append("Page-map metadata contains duplicate output filenames.")
    page_set = set(snapshot["names"]["pages"])
    record_set = set(snapshot["names"]["decisions"])
    errors.extend("Unmapped committed page: " + name for name in sorted(page_set - set(page_names)))
    expected_records = {Path(name).stem + ".json" for name in page_names}
    errors.extend("Unmapped decision record: " + name for name in sorted(record_set - expected_records))
    helpers = load_helpers(content["scripts/review.py"])
    audit_name = "audit_confidence.json"
    if snapshot["signatures"].get(audit_name) is not None and audit_name not in content:
        raise ValueError("audit_confidence.json exists but is not a readable regular UTF-8 file.")
    audit_text = snapshot.get("raw_content", {}).get(audit_name)
    audit_text = audit_text.decode("utf-8") if audit_text is not None else None
    supplied = helpers["_audit_json_loads"](audit_text) if audit_text is not None else None
    requested = supplied.get("pages") if isinstance(supplied, dict) else None
    contexts = {}
    if isinstance(requested, dict) and requested:
        for mapped_row, mapped_name in zip(rows, page_names):
            page_key = "pages/" + mapped_name
            if page_key not in requested:
                continue
            record_key = "decisions/" + Path(mapped_name).stem + ".json"
            if page_key not in snapshot.get("raw_content", {}) or record_key not in content:
                continue
            candidate = helpers["_audit_json_loads"](content[record_key], label=record_key)
            if not isinstance(candidate, dict) or str(candidate.get("cote")) != mapped_row["cote"] or str(candidate.get("scan")) != mapped_row["our_scan"]:
                raise ValueError(record_key + ": audited decision identity differs from page-map metadata.")
            contexts[page_key] = {"page_bytes": snapshot["raw_content"][page_key],
                                  "decision_file": record_key, "record": candidate}
    audit_entries = helpers["_validate_audit_confidence"](audit_text, contexts)
    primary_confidence_rows = []
    custom = custom_commands(content.get("PREAMBLE.tex", ""), helpers["_tex_control"])
    allowed = STANDARD | custom
    inventory_table = parse_table(content.get(root.name + "_inventory.csv"), ",", INVENTORY, "inventory", errors)
    collation_table = parse_table(content.get(root.name + "_collation.tsv"), "\t", COLLATION, "collation", errors)
    event_table = parse_table(content.get("CHECK_EVENTS.tsv"), "\t", None, "CHECK_EVENTS", errors)
    inventory = inventory_table[1] if inventory_table else None
    collation = collation_table[1] if collation_table else None
    enum_issues = []
    def enum(value, allowed_values, file, record, field):
        if not isinstance(value, str) or value not in allowed_values:
            enum_issues.append({"file": file, "record": record, "field": field, "value": value})
    for number, item in enumerate(inventory or [], start=2):
        enum(item["kind"], INVENTORY_KINDS, "inventory", number, "kind")
        enum(item["sheet_kind"], SHEET_KINDS, "inventory", number, "sheet_kind")
        if item["transcribed"] != "yes":
            errors.append(f"Inventory record {number}: transcribed is not exactly yes.")
    for number, item in enumerate(collation or [], start=2):
        enum(item["kind"], KINDS, "collation", number, "kind")
        enum(item["confidence"], CONFIDENCES, "collation", number, "confidence")
    duplicate_collation = sum(count - 1 for count in Counter(tuple(item[key] for key in COLLATION) for item in collation or []).values() if count > 1)
    if duplicate_collation:
        errors.append(f"Collation contains {duplicate_collation} duplicate row instances.")
    expected_inventory, expected_collation, combined_parts = [], [], []
    braces, unknown, extraction_notes, pending = [], [], [], []
    mapping_counts, coverage, defaults = Counter(), {}, Counter()
    committed_flags = []
    committed_records = 0
    source_entries = 0
    unresolved_pages = 0
    for row, name in zip(rows, page_names):
        coverage.setdefault(row["cote"], {"mapped": 0, "committed": 0})["mapped"] += 1
        # A discovered pathname alone is not a usable committed input.
        committed = name in page_set and "pages/" + name in content
        committed_flags.append(committed)
        record_name = Path(name).stem + ".json"
        record_key = "decisions/" + record_name
        record = literal_json(content[record_key], record_key, errors) if record_key in content else None
        identity_ok = False
        if record is not None:
            identity_ok = str(record.get("cote")) == row["cote"] and str(record.get("scan")) == row["our_scan"]
            if not identity_ok:
                errors.append(f"{record_key}: cote/scan identity differs from the filename map.")
            enum(record.get("sheet_kind"), SHEET_KINDS, record_key, "page", "sheet_kind")
            if not isinstance(record.get("inventory"), list) or not isinstance(record.get("decisions"), list):
                errors.append(f"{record_key}: inventory/decisions must be arrays.")
                record = None
        if committed != (record is not None):
            errors.append(f"Readable page/usable decision presence mismatch: {name} / {record_name}.")
        if record is not None:
            committed_records += 1
            if record.get("unresolved") not in (None, "", "None."):
                unresolved_pages += 1
            for number, element in enumerate(record["inventory"], start=1):
                if not isinstance(element, list) or len(element) not in (3, 4):
                    errors.append(f"{record_key}: inventory element {number} must have three or four fields.")
                    continue
                kind, position, words, *hand = element
                if not all(isinstance(value, str) for value in element):
                    errors.append(f"{record_key}: inventory element {number} contains a non-string field.")
                enum(kind, INVENTORY_KINDS, record_key, number, "inventory.kind")
                expected_inventory.append([row["cote"] + "/" + row["our_scan"], record.get("sheet_kind"), hand[0] if hand else record.get("hand"), f"{number:03}", kind, position, words, "yes"])
            for number, decision in enumerate(record["decisions"], start=1):
                if not isinstance(decision, dict):
                    errors.append(f"{record_key}: decision {number} must be an object.")
                    continue
                for flag in ("c_changed", "h_changed"):
                    if flag in decision and not isinstance(decision[flag], bool):
                        errors.append(f"{record_key}: decision {number} field {flag} must be boolean when present.")
                if "kind" not in decision:
                    defaults["missing decision.kind uses existing builder default other"] += 1
                enum(decision.get("kind", "other"), KINDS, record_key, number, "kind")
                enum(decision.get("confidence"), CONFIDENCES, record_key, number, "confidence")
                if decision.get("h_changed"):
                    for field in ("place", "final", "shows"):
                        if not isinstance(decision.get(field), str):
                            errors.append(f"{record_key}: collated decision {number} requires a string {field} field.")
                    if row["hua_has"] != "text":
                        errors.append(f"{record_key}: decision {number} has h_changed although map hua_has is not text.")
                    expected_collation.append([row["folder"], row["their_page"], row["our_scan"], decision.get("place"), decision.get("h", ""), decision.get("c", ""), decision.get("final"), decision.get("shows"), decision.get("kind", "other"), decision.get("marked_in_H", "no"), decision.get("confidence")])
        if not committed:
            continue
        coverage[row["cote"]]["committed"] += 1
        page_key = "pages/" + name
        if page_key not in content:
            continue
        text = content[page_key]
        combined_parts.append(text.rstrip())
        parser_text = helpers["_audit_source_text"](snapshot["raw_content"][page_key]) if page_key in snapshot.get("raw_content", {}) else text
        page_braces, page_unknown, scan_markers, entries, notes = tex_checks(parser_text, page_key, helpers, allowed)
        braces.extend(page_braces)
        unknown.extend(page_unknown)
        if scan_markers != [row["our_scan"]]:
            errors.append(f"{page_key}: scanpage marker does not uniquely match map scan {row['our_scan']}.")
        extraction_notes.extend({"file": page_key, "line": line, "column": column, "note": note} for line, column, note in notes)
        source_entries += len(entries)
        decisions = record["decisions"] if record is not None and identity_ok else []
        for entry in entries:
            # Share the same mechanical rule as the generated doubts table.
            # Retained-C matching requires unique decisions and occurrences;
            # whitespace normalization never removes an internal separator.
            if record is not None and not identity_ok:
                match = {"basis": "pending", "confidence": "not assessed", "pending_reason": "record_identity_mismatch", "decision_numbers_1_based": []}
            else:
                match = helpers["_unsure_confidence_detail"](entry, record or {}, entries, audit_entries=audit_entries, page_file=page_key)
            matches = [{"decision_number_1_based": number, "place": decisions[number - 1].get("place", ""), "recorded_confidence": decisions[number - 1].get("confidence")}
                       for number in match["decision_numbers_1_based"]]
            status = match["basis"] if match["basis"] != "pending" else match["pending_reason"] or "not_assessed"
            mapping_counts[status] += 1
            if match["basis"] == "primary_occurrence":
                primary_confidence_rows.append({"scan": row["cote"] + "/" + row["our_scan"],
                                                "page_file": page_key, "tex_line": entry["line"], "tex_column": entry["column"],
                                                "macro_sha256": hashlib.sha256(entry["macro"].encode("utf-8")).hexdigest(),
                                                "confidence": match["confidence"], "basis": "primary_occurrence",
                                                "decision_ref": match["audit_decision_ref"]})
            if match["confidence"] == "not assessed":
                pending.append({"scan": row["cote"] + "/" + row["our_scan"], "page_file": page_key,
                                "tex_line": entry["line"], "tex_column": entry["column"], "macro": entry["macro"],
                                "reading": entry["reading"], "alternatives": entry["alternatives"],
                                "decision_file": record_key, "match_status": status, "candidates": matches})
    if len(primary_confidence_rows) != len(audit_entries):
        raise ValueError("Some validated primary occurrence entries were not consumed exactly once.")
    if enum_issues:
        errors.append(f"{len(enum_issues)} values fall outside required enums; see JSON details.")
    if braces:
        errors.append(f"{len(braces)} unmatched literal TeX braces were found.")
    if extraction_notes:
        errors.append(f"{len(extraction_notes)} unsure-parser warnings require review.")
    expected_combined = "\n\n".join(combined_parts) + "\n"
    combined_match = content.get(root.name + "_transcription.tex") == expected_combined
    if not combined_match:
        errors.append("Combined transcription differs from committed page texts joined in metadata-map order.")
    first_missing = next((index for index, present in enumerate(committed_flags) if not present), len(rows))
    committed_prefix = not any(committed_flags[first_missing:])
    if not committed_prefix:
        errors.append("Committed pages are not a contiguous prefix of page-map order.")
    doubts_shape = doubts_table_shape(content.get(root.name + "_doubts.md", ""))
    doubts_schema = doubts_shape["present"] and doubts_shape["malformed_rows"] == 0
    if not doubts_schema:
        errors.append("Doubts Markdown lacks a correctly shaped five-column table outside code examples.")
    inventory_check = compare_rows(inventory, expected_inventory, INVENTORY, "Inventory", errors)
    collation_check = compare_rows(collation, expected_collation, COLLATION, "Collation", errors)
    return {
        "scope": "Mechanical snapshot of committed outputs only; no visual/editorial review, source-text reading, or TeX compilation.",
        "snapshot": {key: snapshot[key] for key in ("started_utc", "ended_utc", "attempt", "stable")},
        "mapped_pages": len(rows), "committed_pages": sum(committed_flags), "uncommitted_pages": len(rows) - sum(committed_flags),
        "discovered_page_paths": len(page_set), "discovered_decision_paths": len(record_set),
        "decision_records": committed_records, "coverage_by_cote": coverage, "committed_prefix": committed_prefix,
        "required_artifact_count": len(snapshot["required"]), "missing_required": missing_required, "empty_required": empty_required,
        "inventory": inventory_check, "collation": collation_check, "duplicate_collation_rows": duplicate_collation,
        "combined_normalized_text_match": combined_match,
        "combined_comparison_convention": "UTF-8-sig decoding; each page rstrip(); two LF separators; one final LF. This is normalized text agreement using the existing builder's separator convention.",
        "doubts_required_columns_present": doubts_schema, "doubts_table_shape": doubts_shape,
        "check_events_columns": event_table[0] if event_table else [], "check_events_rows": len(event_table[1]) if event_table else None,
        "check_events_check_scope": "Header presence/uniqueness and record widths/count only; required event-column names were not supplied to this diagnostic.",
        "metadata_defaults_mirrored_for_comparison_only": dict(defaults),
        "custom_commands_from_preamble": sorted(custom), "brace_findings": braces, "unknown_macro_review": unknown,
        "enum_findings": enum_issues, "extraction_notes": extraction_notes, "unsure_entries": source_entries,
        "confidence_mapping_counts": dict(mapping_counts), "pending_confidence_rows": len(pending),
        "audit_confidence_file_present": audit_text is not None,
        "audit_confidence_entries": len(audit_entries),
        "audit_confidence_pages": len({key[0] for key in audit_entries}),
        "primary_confidence_rows": primary_confidence_rows,
        "pages_with_recorded_unresolved_prose": unresolved_pages, "structural_issues": errors,
        "metadata_map": rows, "pending_confidence": pending,
        "input_file_metadata": snapshot["signatures"],
    }


def md(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")


def write_reports(root, out_dir, result):
    out_dir.mkdir(parents=True, exist_ok=True)
    identifier = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")
    stem = "committed_diagnostics_" + identifier
    report = out_dir / (stem + ".md")
    details = out_dir / (stem + ".json")
    pending = out_dir / (stem + "_pending_confidence.tsv")
    metadata = out_dir / (stem + "_page_map_metadata.tsv")
    with pending.open("x", encoding="utf-8", newline="") as handle:
        fields = ["scan", "page_file", "tex_line", "tex_column", "macro", "reading", "alternatives_json", "decision_file", "match_status", "candidates_json"]
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for entry in result["pending_confidence"]:
            row = dict(entry)
            row["alternatives_json"] = json.dumps(row.pop("alternatives"), ensure_ascii=False)
            row["candidates_json"] = json.dumps(row.pop("candidates"), ensure_ascii=False)
            writer.writerow(row)
    with metadata.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MAP_FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(result["metadata_map"])
    result["report_files"] = {"report": report.name, "details": details.name, "pending_confidence": pending.name, "page_map_metadata": metadata.name}
    with details.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    unknown_counts = Counter(item["command"] for item in result["unknown_macro_review"])
    lines = ["# Committed-output diagnostics — preliminary snapshot", "",
             f"Captured **{result['snapshot']['started_utc']}–{result['snapshot']['ended_utc']}**. Input metadata remained stable during capture: **{result['snapshot']['stable']}**.", "",
             f"This snapshot covers **{result['committed_pages']} of {result['mapped_pages']} mapped pages**; **{result['uncommitted_pages']} remain uncommitted**. It checks output bookkeeping only. It does not establish visual accuracy, editorial resolution, or full-archive completion. No scans, witness text, or context files were opened; only permitted filename-map metadata was read outside the output tree. Report snapshots are excluded from required-artifact and page counts.", "",
             "## Structural summary", "", "| Check | Snapshot result |", "|---|---|",
             f"| Required named artifacts | {result['required_artifact_count'] - len(result['missing_required'])}/{result['required_artifact_count']} regular files; {len(result['empty_required'])} empty |",
             f"| Readable page/usable decision coverage | {result['committed_pages']} pages; {result['decision_records']} records |",
             f"| Committed prefix / combined normalized-text order | {result['committed_prefix']} / {result['combined_normalized_text_match']} |",
             f"| Inventory rows / exact record agreement | {result['inventory'].get('actual_rows', 'unchecked')} / {result['inventory'].get('exact_order_match', False)} |",
             f"| Collation rows / exact record agreement | {result['collation'].get('actual_rows', 'unchecked')} / {result['collation'].get('exact_order_match', False)} |",
             f"| Duplicate collation rows / enum findings | {result['duplicate_collation_rows']} / {len(result['enum_findings'])} |",
             f"| TeX brace findings / unrecognized token occurrences | {len(result['brace_findings'])} / {len(result['unknown_macro_review'])} |",
             f"| Doubts columns / parser warnings | {result['doubts_required_columns_present']} / {len(result['extraction_notes'])} |",
             f"| CHECK_EVENTS data rows | {result['check_events_rows']} |", "",
             "## Coverage", "", "| Cote | Committed | Mapped |", "|---|---:|---:|"]
    for cote, counts in result["coverage_by_cote"].items():
        lines.append(f"| {md(cote)} | {counts['committed']} | {counts['mapped']} |")
    lines += ["", "## Structural findings", ""]
    lines += ["- " + md(message) for message in result["structural_issues"]] or ["No structural inconsistencies were found in the captured committed subset."]
    lines += ["", "Combined-file comparison uses decoded text with UTF-8 BOMs removed, and joins pages with the existing builder's trailing-whitespace removal, two LF separators, and final LF. This is text agreement under that convention. CHECK_EVENTS is checked for a usable header and consistent record widths; its column names are reported without asserting an independently supplied schema."]
    if result["metadata_defaults_mirrored_for_comparison_only"]:
        lines += ["", "Optional metadata defaults mirrored for comparison only: " + "; ".join(key + "=" + str(value) for key, value in result["metadata_defaults_mirrored_for_comparison_only"].items()) + ". No metadata is changed."]
    lines += ["", "## Macro and confidence review", "",
              "Custom commands are taken from PREAMBLE.tex. The standard LaTeX/TikZ recognition registry is limited: an unrecognized token is a review item, not a declaration of invalid TeX. Brace and macro checks are lexical; no compilation, macro expansion, or catcode interpretation is performed.", ""]
    if result.get("recognition_registry_update"):
        lines += ["Macro recognition was refreshed from the saved token findings after adding the listed standard LaTeX/AMS commands to the registry. The captured source files were not reread. Registry update: " + ", ".join("`\\" + name + "`" for name in result["recognition_registry_update"]["recognized_commands"]) + ".", ""]
    if unknown_counts:
        lines += ["| Token | Count | Output locations |", "|---|---:|---|"]
        for command, count in sorted(unknown_counts.items()):
            locations = [item["file"] + ":" + str(item["line"]) + ":" + str(item["column"]) for item in result["unknown_macro_review"] if item["command"] == command]
            lines.append("| `\\" + md(command) + "` | " + str(count) + " | " + md("; ".join(locations[:8])) + ("; …" if len(locations) > 8 else "") + " |")
    else:
        lines.append("No unrecognized control tokens were found by this registry.")
    if result.get("audit_confidence_entries", 0):
        lines += ["", f"**Primary-supplied occurrence confidence:** {result['audit_confidence_entries']} explicit entries across {result['audit_confidence_pages']} pages passed raw-page-hash, exact physical-coordinate/macro, enum, and decision-reference validation. They take precedence at those exact occurrences. Their provenance is recorded under primary_confidence_rows in the JSON; no confidence is inferred from a decision reference."]
    lines += ["", f"The literal parser found **{result['unsure_entries']} unsure entries**. **{result['pending_confidence_rows']} entries** need confidence-mapping review. Counts: " + "; ".join(key + "=" + str(value) for key, value in sorted(result["confidence_mapping_counts"].items())) + ".", "",
              "Matching shares the generated doubts table's rule. The existing direct-final comparison trims boundary whitespace. For otherwise pending entries, final must be exactly C retained, and the recorded C field must uniquely match the full unsure expression on the same page. Exact comparison is tried first; the fallback collapses whitespace runs to one space and trims ends, preserving internal separators and every nonspace character. Both a unique candidate decision and a unique page occurrence are required. Ambiguities remain pending even when recorded confidence values agree. This diagnostic assigns or changes no confidence; it reports existing records only. Recorded unresolved prose remains in the doubts document.", "",
              f"Review [{pending.name}]({pending.name}) for pending locations, existing text, and any exact candidate records. The full machine-readable findings are in [{details.name}]({details.name}); permitted filename metadata is copied to [{metadata.name}]({metadata.name}).", "",
              "CHECK_EVENTS row count is reported as bookkeeping evidence only; an empty log does not establish that external checks were completed.", ""]
    with report.open("x", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
    with (root / "tooling.log").open("a", encoding="utf-8") as handle:
        action = "Refreshed recognition from saved diagnostic snapshot" if result.get("recognition_registry_update") else "Ran diagnose_committed.py"
        handle.write(stamp() + " | " + action + ": " + json.dumps({"report": str(report.relative_to(root)) if report.is_relative_to(root) else str(report), "stable": result["snapshot"]["stable"], "committed_pages": result["committed_pages"], "mapped_pages": result["mapped_pages"], "structural_issues": len(result["structural_issues"]), "unknown_token_occurrences": len(result["unknown_macro_review"]), "pending_confidence_rows": result["pending_confidence_rows"], "scope": "mechanical snapshot only; no page/decision/derived-output changes"}, ensure_ascii=False) + "\n")
    return report, details, pending, metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--page-map", type=Path, help="Permitted metadata TSV; no referenced source files are opened.")
    parser.add_argument("--out-dir", type=Path, help="Diagnostic snapshot destination; defaults to ROOT/diagnostics.")
    args = parser.parse_args()
    try:
        if args.root.is_symlink() or not args.root.is_dir():
            raise ValueError("Output root must be an existing non-symlinked directory.")
        root = args.root.resolve()
        page_map = args.page_map or root.parent / "source" / (root.name + "_witnesses") / "page_map.tsv"
        result = audit(root, capture(root, page_map))
        paths = write_reports(root, args.out_dir or root / "diagnostics", result)
        print(json.dumps({"stable": result["snapshot"]["stable"], "committed_pages": result["committed_pages"], "mapped_pages": result["mapped_pages"], "structural_issues": result["structural_issues"], "unknown_tokens": dict(Counter(item["command"] for item in result["unknown_macro_review"])), "pending_confidence_rows": result["pending_confidence_rows"], "reports": [str(path) for path in paths]}, ensure_ascii=False, indent=2))
        return 2 if not result["snapshot"]["stable"] else 1 if result["structural_issues"] else 0
    except (OSError, ValueError, KeyError, TypeError, SyntaxError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
