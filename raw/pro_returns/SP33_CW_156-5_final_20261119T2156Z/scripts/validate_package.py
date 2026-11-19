#!/usr/bin/env python3
"""Read-only structural checks for SP33_CW_156-5; never compiles or OCRs.

Run from any directory:
  python out/scripts/validate_package.py out
During transcription, --partial validates only the files already present.
All findings go to stdout; no input file is modified. A zero exit status means
the implemented structural checks passed, not that a reading is correct.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

PREFIX = "SP33_CW_156-5"
SCANS = list(range(2, 26))
COLLATION_FIELDS = [
    "folder", "their_page", "our_scan", "line", "their_reading",
    "codex_reading", "final_reading", "scan_shows", "kind",
    "marked_in_H", "confidence",
]
INVENTORY_FIELDS = [
    "scan", "sheet_kind", "hand", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
COLLATION_KINDS = {
    "misread word", "misread symbol or index", "omission",
    "text not on the page", "deletion state (struck given live or live given struck)",
    "insertion or placement", "abbreviation expanded or spelling modernised",
    r"readable ink left as \ill{}", "drawing or diagram", "other",
}
INVENTORY_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
SHEET_KINDS = {
    "text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover",
}

# Vocabulary supported by the supplied preamble, standard LaTeX/AMS, and TikZ.
# This is a lexical guard, not a mathematical check. Extend only for a verified
# standard/package command; manuscript notation must not define new commands.
ALLOWED_CONTROL_WORDS = set("""
cotefile scanpage mspage handwritten deleted inserted margin uline uuline
diagram figure unsure illegible begin end
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon phi
varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
mathbb mathcal mathfrak mathscr mathrm mathbf mathit mathsf mathtt mathnormal
operatorname operatornamewithlimits ensuremath text textrm textsf texttt textbf
textit textsl textsc textnormal emph underline overline widehat widetilde hat
tilde bar vec dot ddot acute grave check breve not frac dfrac tfrac binom
dbinom tbinom sqrt overset underset stackrel overbrace underbrace substack
displaystyle textstyle scriptstyle scriptscriptstyle limits nolimits
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
lvert rvert lVert rVert langle rangle lceil rceil lfloor rfloor vert Vert
sum prod coprod int iint iiint oint bigcup bigcap bigsqcup bigvee bigwedge
cup cap sqcup sqcap amalg boxtimes otimes oplus odot bullet cdot circ times
div pm mp ast star diamond triangle triangleleft triangleright
in ni notin subset supset subseteq supseteq subsetneq supsetneq
le leq ge geq ne neq ll gg prec succ preceq succeq preccurlyeq succcurlyeq
equiv sim simeq approx cong asymp propto doteq parallel shortparallel perp smile frown
to gets mapsto longmapsto arrow draw node path fill coordinate foreach
longrightarrow longleftarrow longleftrightarrow rightarrow leftarrow
leftrightarrow Rightarrow Leftarrow Leftrightarrow Longrightarrow
Longleftarrow Longleftrightarrow hookrightarrow hookleftarrow
twoheadrightarrow twoheadleftarrow rightrightarrows leftleftarrows
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow
emptyset varnothing infty partial nabla forall exists nexists neg lnot
land lor wedge vee setminus smallsetminus mid prime ell hbar imath jmath
ldots cdots vdots ddots dots colon bmod pmod mod gcd lim liminf limsup
log ln exp sin cos tan inf sup min max ker det dim hom arg deg Pr
quad qquad enspace thinspace medspace thickspace hspace vspace
phantom hphantom vphantom smash raisebox rule strut mathstrut
noindent par newline linebreak pagebreak newpage clearpage smallskip medskip
bigskip footnotesize scriptsize tiny small normalsize large Large LARGE
huge Huge textcircled tag label ref eqref footnote marginpar
mathrel mathbin mathord mathop mathopen mathclose mathpunct
ooalign hfil cr kern mkern mskip hskip vskip
tikztostart tikztotarget tikztonodes scope clip filldraw cycle
""".split())


def unknown_control_words(source: str) -> list[str]:
    text = clean_tex(source)
    failures = []
    i = 0
    while i < len(text):
        if text[i] != "\\":
            i += 1
            continue
        match = re.match(r"\\([A-Za-z@]+)", text[i:])
        if not match:
            i += 2
            continue
        name = match.group(1)
        if name not in ALLOWED_CONTROL_WORDS:
            line = text.count("\n", 0, i) + 1
            prefixes = [p for p in ALLOWED_CONTROL_WORDS if name.startswith(p) and len(p) < len(name)]
            hint = ""
            if prefixes:
                prefix = max(prefixes, key=len)
                hint = f"; possible missing command delimiter after \\{prefix}"
            failures.append(f"line {line}: unrecognized control word \\{name}{hint}")
        i += match.end()
    return failures


def folder(scan: int) -> str:
    return f"J156-5-{1 + (scan - 2) // 8:02d}"


def page_name(scan: int) -> str:
    return f"{folder(scan)}_156-5_scan{scan:03d}.tex"


def clean_tex(source: str) -> str:
    """Drop comments and verbatim inline literals, preserving newlines.

    Escape handling is lexical: escaped percent signs and braces survive;
    \verb literals are blanked. Verbatim environments are not part of the
    requested transcription format and deliberately receive no special case.
    """
    out = []
    i = 0
    while i < len(source):
        if source[i] == "%":
            end = source.find("\n", i)
            if end < 0:
                break
            out.append(" " * (end - i))
            i = end
        elif source[i] == "\\":
            verb = re.match(r"\\verb\*?(?=[^A-Za-z])", source[i:])
            if verb:
                start = i + verb.end()
                if start >= len(source):
                    out.append(source[i:])
                    break
                delimiter = source[start]
                end = source.find(delimiter, start + 1)
                if end < 0:
                    out.append(source[i:])
                    break
                out.append(" " * (end + 1 - i))
                i = end + 1
            else:
                out.append(source[i:i + 2])
                i += 2
        else:
            out.append(source[i])
            i += 1
    return "".join(out)


def tex_balance(source: str) -> list[str]:
    text = clean_tex(source)
    failures: list[str] = []
    braces: list[int] = []
    environments: list[tuple[str, int]] = []
    display: list[tuple[str, int]] = []
    dollars: list[tuple[str, int]] = []
    i = 0
    line = 1
    while i < len(text):
        c = text[i]
        if c == "\n":
            line += 1
            i += 1
            continue
        if c == "\\":
            token = text[i:i + 2]
            if token in (r"\[", r"\("):
                display.append((token, line))
                i += 2
                continue
            if token in (r"\]", r"\)"):
                expected = r"\[" if token == r"\]" else r"\("
                if not display or display[-1][0] != expected:
                    failures.append(f"line {line}: unmatched {token}")
                else:
                    display.pop()
                i += 2
                continue
            env = re.match(r"\\(begin|end)\s*\{([^{}]+)\}", text[i:])
            if env:
                operation, name = env.groups()
                if operation == "begin":
                    environments.append((name, line))
                elif not environments:
                    failures.append(f"line {line}: unmatched end of {name}")
                elif environments[-1][0] != name:
                    failures.append(
                        f"line {line}: end of {name} while {environments[-1][0]} is open"
                    )
                    environments.pop()
                else:
                    environments.pop()
                line += env.group(0).count("\n")
                i += env.end()
                continue
            command = re.match(r"\\[A-Za-z@]+\*?", text[i:])
            i += command.end() if command else min(2, len(text) - i)
            continue
        if c == "{":
            braces.append(line)
        elif c == "}":
            if braces:
                braces.pop()
            else:
                failures.append(f"line {line}: unmatched closing brace")
        elif c == "$":
            token = "$$" if text[i:i + 2] == "$$" else "$"
            if dollars and dollars[-1][0] == token:
                dollars.pop()
            elif dollars:
                failures.append(f"line {line}: mixed $ and $$ delimiter")
                dollars.pop()
            else:
                dollars.append((token, line))
            i += len(token)
            continue
        i += 1
    failures += [f"line {ln}: unclosed brace" for ln in braces]
    failures += [f"line {ln}: unclosed environment {name}" for name, ln in environments]
    failures += [f"line {ln}: unclosed delimiter {token}" for token, ln in display + dollars]
    return failures


def frozen_manifest_problems(root: Path, observed_hashes: dict[str, str], required: bool) -> tuple[list[str], int | None]:
    """Compare byte hashes already observed by the validator with freeze metadata."""
    path = root / "records" / "frozen_hashes.json"
    if not path.exists():
        return (["Missing records/frozen_hashes.json"] if required else []), None
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Cannot read frozen-hash manifest: {exc}"], None
    if not isinstance(manifest, dict) or not manifest:
        return ["Frozen-hash manifest must be a nonempty path-to-SHA256 mapping"], None
    failures = []
    if set(manifest) != set(observed_hashes):
        failures.append("Frozen-hash manifest does not cover exactly the observed page files and combined transcription")
    for name, digest in manifest.items():
        if not isinstance(digest, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", digest):
            failures.append(f"Invalid frozen SHA-256 for {name}")
        elif name in observed_hashes and observed_hashes[name] != digest.lower():
            failures.append(f"Frozen transcription hash mismatch: {name}")
    return failures, len(manifest)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--partial", action="store_true", help="Allow unfinished/missing deliverables")
    parser.add_argument("--json", action="store_true", help="Print machine-readable findings")
    parser.add_argument("--self-test", action="store_true", help="Check parser on synthetic examples only")
    args = parser.parse_args()
    if args.self_test:
        good = [
            r"\scanpage{2} Test $A_{ij}^!$.",
            "\\[\\begin{aligned} A&=B\\\\ C&=D \\end{aligned}\\]",
            "Escaped \\% and \\{ and \\$ % ignored } $\nnext",
            r"\verb|{$%}| \uline{abc}",
            r"\[A=\text{the $x$ here}\]",
        ]
        bad = [r"\uline{abc", r"A}", r"$A", r"\[A", r"\begin{x}\end{y}"]
        assert all(not tex_balance(s) for s in good), [(s, tex_balance(s)) for s in good]
        assert all(tex_balance(s) for s in bad)
        assert not unknown_control_words(r"\unsure{\ensuremath{=}|m} \preccurlyeq G")
        assert len(unknown_control_words(r"\preccurlyeqG \longrightarrowJ")) == 2
        assert not unknown_control_words("% \\bad\n\\\\bad")
        with tempfile.TemporaryDirectory(prefix="synthetic-manifest-check-") as temporary:
            root = Path(temporary)
            observed = {"pages/synthetic.tex": "a" * 64, "combined.tex": "b" * 64}
            assert not frozen_manifest_problems(root, observed, False)[0]
            assert frozen_manifest_problems(root, observed, True)[0]
            (root / "records").mkdir()
            manifest = root / "records" / "frozen_hashes.json"
            manifest.write_text(json.dumps(observed))
            assert frozen_manifest_problems(root, observed, True) == ([], 2)
            assert frozen_manifest_problems(root, {**observed, "combined.tex": "c" * 64}, True)[0]
            manifest.write_text(json.dumps({"combined.tex": "b" * 64}))
            assert frozen_manifest_problems(root, observed, True)[0]
        print("Synthetic lexical balance checks passed.")
        return 0

    root = args.directory.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    information: dict[str, object] = {"directory": str(root), "partial": args.partial}
    expected_names = {page_name(n) for n in SCANS}
    paths = sorted((root / "pages").glob("*.tex"))
    actual_names = {p.name for p in paths}
    extra = actual_names - expected_names
    missing = expected_names - actual_names
    if extra:
        errors.append("Unexpected page filenames: " + ", ".join(sorted(extra)))
    if missing and not args.partial:
        errors.append("Missing page filenames: " + ", ".join(sorted(missing)))
    information["page_count"] = len(paths)
    pages: dict[int, str] = {}
    observed_hashes: dict[str, str] = {}
    marks = {"unsure": 0, "illegible": 0, "deleted": 0}
    for scan in SCANS:
        path = root / "pages" / page_name(scan)
        if not path.exists():
            continue
        source = path.read_text(encoding="utf-8")
        observed_hashes[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        pages[scan] = source
        errors += [f"{path.name}: {s}" for s in tex_balance(source)]
        errors += [f"{path.name}: {s}" for s in unknown_control_words(source)]
        cleaned = clean_tex(source)
        scan_markers = re.findall(r"\\scanpage\s*\{([^{}]+)\}", cleaned)
        if scan_markers != [str(scan)]:
            errors.append(f"{path.name}: expected only scan marker {scan}; got {scan_markers}")
        for mark in marks:
            marks[mark] += len(re.findall(r"\\" + mark + r"\s*\{", cleaned))
    information["marks_in_page_files"] = marks
    combined = root / f"{PREFIX}_transcription.tex"
    if combined.exists():
        combined_source = combined.read_text(encoding="utf-8")
        errors += [f"{combined.name}: {s}" for s in tex_balance(combined_source)]
        cotefiles = re.findall(r"\\cotefile\s*\{([^{}]+)\}", clean_tex(combined_source))
        if cotefiles != ["156-5"]:
            errors.append(f"Combined transcription must have exactly one cotefile 156-5; got {cotefiles}")
        # Ignore separator blank lines only. Any non-whitespace textual difference fails.
        joined = "\n".join(pages[n].strip() for n in sorted(pages))
        canonical = lambda s: re.sub(r"\n\s*\n+", "\n", s.strip()).replace("\r\n", "\n")
        if canonical(combined_source) != canonical(joined):
            errors.append("Combined transcription differs from ordered concatenation of page files")
        information["combined_sha256"] = hashlib.sha256(combined.read_bytes()).hexdigest()
        observed_hashes[combined.relative_to(root).as_posix()] = information["combined_sha256"]
    elif not args.partial:
        errors.append(f"Missing {combined.name}")
    freeze_errors, freeze_count = frozen_manifest_problems(root, observed_hashes, not args.partial)
    errors.extend(freeze_errors)
    information["frozen_hash_entries"] = freeze_count
    information["frozen_hashes_match"] = freeze_count is not None and not freeze_errors

    def read_rows(name: str, delimiter: str, fields: list[str]) -> list[dict[str, str]]:
        path = root / name
        if not path.exists():
            if not args.partial:
                errors.append(f"Missing {name}")
            return []
        with path.open(newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream, delimiter=delimiter)
            if reader.fieldnames != fields:
                errors.append(f"{name}: columns {reader.fieldnames!r}; expected {fields!r}")
            rows = list(reader)
        for i, row in enumerate(rows, 2):
            if None in row or any(value is None for value in row.values()):
                errors.append(f"{name}:{i}: malformed field count")
        return rows

    inventory = read_rows(f"{PREFIX}_inventory.csv", ",", INVENTORY_FIELDS)
    covered: set[int] = set()
    element_ids: set[tuple[int, str]] = set()
    for i, row in enumerate(inventory, 2):
        label = f"inventory row {i}"
        try:
            scan = int(row.get("scan", ""))
        except (TypeError, ValueError):
            errors.append(f"{label}: invalid scan")
            continue
        covered.add(scan)
        if scan not in SCANS:
            errors.append(f"{label}: out-of-range scan {scan}")
        if row.get("kind") not in INVENTORY_KINDS:
            errors.append(f"{label}: invalid kind {row.get('kind')!r}")
        if row.get("sheet_kind") not in SHEET_KINDS:
            errors.append(f"{label}: invalid sheet_kind {row.get('sheet_kind')!r}")
        if row.get("transcribed") != "yes":
            errors.append(f"{label}: transcribed must equal yes")
        if not row.get("hand"):
            errors.append(f"{label}: missing hand")
        key = (scan, row.get("element", ""))
        if key in element_ids:
            errors.append(f"{label}: repeated element id {key}")
        element_ids.add(key)
    required_coverage = set(pages) if args.partial else set(SCANS)
    if required_coverage - covered:
        errors.append(f"Inventory lacks scans {sorted(required_coverage - covered)}")
    information["inventory_rows"] = len(inventory)

    collation = read_rows(f"{PREFIX}_collation.tsv", "\t", COLLATION_FIELDS)
    confidence_counts = {"high": 0, "medium": 0, "low": 0}
    for i, row in enumerate(collation, 2):
        label = f"collation row {i}"
        try:
            scan = int(row.get("our_scan", ""))
            their_page = int(row.get("their_page", ""))
        except (TypeError, ValueError):
            errors.append(f"{label}: invalid scan/page number")
            continue
        if scan not in SCANS or their_page != scan - 1:
            errors.append(f"{label}: incorrect scan/page mapping")
        if row.get("folder") != folder(scan):
            errors.append(f"{label}: incorrect Codex folder")
        if row.get("kind") not in COLLATION_KINDS:
            errors.append(f"{label}: invalid kind {row.get('kind')!r}")
        conf = row.get("confidence", "")
        if conf not in confidence_counts:
            errors.append(f"{label}: invalid confidence {conf!r}")
        else:
            confidence_counts[conf] += 1
        for field in ("line", "scan_shows", "marked_in_H"):
            if not row.get(field):
                errors.append(f"{label}: missing {field}")
    information["collation_rows"] = len(collation)
    information["collation_confidence"] = confidence_counts

    check_events = root / "CHECK_EVENTS.tsv"
    if check_events.exists():
        with check_events.open(newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream, delimiter="\t")
            fields = [re.sub(r"[ -]+", "_", x.lower().strip()) for x in (reader.fieldnames or [])]
            normalized = set(fields)
            if not {"statement_id", "date", "outcome"}.issubset(normalized):
                errors.append("CHECK_EVENTS.tsv lacks statement_id, date, or outcome")
            if not ({"who"}.issubset(normalized) or {"model", "effort", "run"}.issubset(normalized)):
                errors.append("CHECK_EVENTS.tsv lacks who or model/effort/run fields")
            if not {"type", "event_type", "check_type"} & normalized:
                errors.append("CHECK_EVENTS.tsv lacks an event-type field")
            events = list(reader)
            information["check_event_rows"] = len(events)
            if not events and not args.partial:
                errors.append("CHECK_EVENTS.tsv has no check events; final research documentation is unfinished")
            for i, row in enumerate(events, 2):
                if None in row or any(value is None for value in row.values()):
                    errors.append(f"CHECK_EVENTS.tsv:{i}: malformed field count")
                normalized_row = {re.sub(r"[ -]+", "_", k.lower().strip()): value for k, value in row.items() if isinstance(k, str)}
                required = ["statement_id", "date", "outcome"]
                required += ["who"] if "who" in normalized else ["model", "effort", "run"]
                event_fields = sorted({"type", "event_type", "check_type"} & normalized)
                required += event_fields[:1]
                for field in required:
                    if not isinstance(normalized_row.get(field), str) or not normalized_row[field].strip():
                        errors.append(f"CHECK_EVENTS.tsv:{i}: empty required field {field}")
    elif not args.partial:
        errors.append("Missing CHECK_EVENTS.tsv")

    for suffix in ("changes.md", "doubts.md", "notes.md"):
        name = f"{PREFIX}_{suffix}"
        if not (root / name).exists() and not args.partial:
            errors.append(f"Missing {name}")
        elif (root / name).exists() and not args.partial:
            content = (root / name).read_text(encoding="utf-8")
            if not content.strip():
                errors.append(f"{name} is empty")
            if suffix == "notes.md" and len(content.strip()) < 500:
                errors.append(f"{name} is shorter than 500 characters; appears unfinished for the 24-page research scope")
            # Narrow drafting markers only; mathematical words such as unverified
            # or conjectural are legitimate content and are deliberately ignored.
            placeholders = [
                r"\bTODO\b", r"\bTBD\b", r"\bPLACEHOLDER\b",
                r"None recorded yet\.",
                r"Assessment in progress; no claim of human verification\.",
            ]
            for pattern in placeholders:
                if re.search(pattern, content, flags=re.I):
                    errors.append(f"{name} contains drafting marker matching {pattern}")
    log_path = root / "progress.log"
    if log_path.exists():
        log = log_path.read_text(encoding="utf-8")
        done = set(map(int, re.findall(r"^scan (\d+) done\b", log, re.M)))
        audited = set(map(int, re.findall(r"^scan (\d+) audited\b", log, re.M)))
        information["done_scans"] = sorted(done)
        information["audited_scans"] = sorted(audited)
        if not args.partial:
            if set(SCANS) - done:
                errors.append(f"progress.log lacks done events for {sorted(set(SCANS) - done)}")
            if set(SCANS) - audited:
                errors.append(f"progress.log lacks audit events for {sorted(set(SCANS) - audited)}")
            frozen = log.find("transcription frozen ")
            context = log.find("context opened ")
            if frozen < 0 or context < 0 or frozen >= context:
                errors.append("progress.log lacks correctly ordered frozen/context-opened events")
    elif not args.partial:
        errors.append("Missing progress.log")

    information["errors"] = errors
    information["warnings"] = warnings
    information["passed"] = not errors
    if args.json:
        print(json.dumps(information, ensure_ascii=False, indent=2))
    else:
        for key, value in information.items():
            if key not in ("errors", "warnings"):
                print(f"{key}: {value}")
        for entry in warnings:
            print("WARNING: " + entry)
        for entry in errors:
            print("ERROR: " + entry)
        print("Structural validation PASSED." if not errors else "Structural validation FAILED.")
        print("This script does not assess the fidelity of a manuscript reading.")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
