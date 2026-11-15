#!/usr/bin/env python3
"""Read-only structural checks for MPL_136_235-281 deliverable text.

This utility does not open images, archives, or context materials. It cannot
judge transcription accuracy, completeness against the ink, or OCR provenance.
Supported freeze-log forms include:
    sha256 pages/MPL_136_235-281_136_scan235.tex <64-hex-digest>
    <64-hex-digest>  pages/MPL_136_235-281_136_scan235.tex
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

STEM = "MPL_136_235-281"
SCANS = [n for n in range(235, 282) if n != 243]
COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
           "first_words_or_objects", "transcribed"]
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
CUSTOM = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())
# This is a convenience vocabulary, not a complete TeX parser or an allowlist.
# Other commands are informational and do not cause validation failure.
COMMON = set("""
begin end text textrm textit textbf textsf texttt textsc emph underline overline
mathrm mathit mathbf mathsf mathtt mathcal mathscr mathfrak mathbb boldsymbol
operatorname DeclareMathOperator newcommand renewcommand def let input include
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
frac dfrac tfrac binom dbinom tbinom sqrt hat widehat tilde widetilde bar vec dot
ddot check breve acute grave overset underset stackrel substack limits nolimits
sum prod coprod int iint iiint oint lim limsup liminf sup inf min max det dim
ker coker Hom hom Ext Tor End Aut Spec Proj fun arg deg gcd log ln exp sin cos
tan cot sec csc sinh cosh tanh arcsin arccos arctan
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon phi
varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
in notin ni subset supset subseteq supseteq subsetneq supsetneq nsubseteq
le leq ge geq neq ne equiv sim simeq cong approx asymp propto ll gg prec succ
preceq succeq triangleleft triangleright unlhd unrhd parallel perp mid nmid
to gets mapsto longmapsto rightarrow leftarrow leftrightarrow Rightarrow
Leftarrow Leftrightarrow longrightarrow longleftarrow longleftrightarrow
Longrightarrow Longleftarrow Longleftrightarrow hookrightarrow hookleftarrow
rightarrowtail leftarrowtail twoheadrightarrow twoheadleftarrow uparrow
downarrow updownarrow Uparrow Downarrow Updownarrow nearrow searrow swarrow
nwarrow rightrightarrows leftleftarrows rightleftarrows leftrightarrows
leftrightharpoons rightleftharpoons xrightarrow xleftarrow
times cdot ast star circ bullet div pm mp oplus otimes odot ominus oslash
bigoplus bigotimes bigodot cup cap bigcup bigcap sqcup sqcap bigsqcup wedge vee
bigwedge bigvee land lor lnot neg setminus smallsetminus amalg wr
partial nabla infty emptyset varnothing forall exists nexists top bot aleph
ell hbar imath jmath Re Im wp prime backprime angle triangle square Box Diamond
langle rangle lceil rceil lfloor rfloor lbrace rbrace vert Vert lvert rvert
lVert rVert backslash ldots cdots vdots ddots dots dotsb dotsc dotsm dotsi dotso
quad qquad enspace thinspace medspace thickspace hspace vspace hfill vfill
phantom hphantom vphantom smash strut mathstrut null not
arraystretch multicolumn cline hline label ref eqref tag notag nonumber
small tiny scriptsize footnotesize normalsize large Large LARGE huge Huge
displaystyle textstyle scriptstyle scriptscriptstyle textnormal normalfont
newline linebreak par noindent indent centering raggedright raggedleft
footnote footnotemark footnotetext item itemsep enumerate description
arrow ar draw path node coordinate fill filldraw foreach scope tikz
endash textendash textemdash textquotesingle textquotedblleft textquotedblright
textbackslash textasciitilde textasciicircum textbar textless textgreater
LaTeX TeX ensuremath mbox fbox framebox shortstack rule raisebox
mathrel mathop natural sharp underbrace overbrace boxed textcircled varinjlim
varprojlim circledast textsuperscript flat rotatebox lhook joinrel boxtimes
""".split())


def clean_tex(s: str) -> str:
    """Remove comments while retaining newline locations and escaped percents."""
    out = []
    for line in s.splitlines(keepends=True):
        for i, ch in enumerate(line):
            if ch == "%":
                j = i - 1
                while j >= 0 and line[j] == "\\":
                    j -= 1
                if (i - j - 1) % 2 == 0:
                    line = line[:i] + ("\n" if line.endswith("\n") else "")
                    break
        out.append(line)
    return "".join(out)


def brace_errors(s: str) -> list[str]:
    stack, errors = [], []
    s = clean_tex(s)
    line, i = 1, 0
    while i < len(s):
        if s[i] == "\n":
            line += 1
        if s[i] == "\\":
            verb = re.match(r"\\verb\*?(.)", s[i:])
            if verb:
                delim = verb.group(1)
                stop = s.find(delim, i + len(verb.group(0)))
                if stop >= 0:
                    line += s[i:stop + 1].count("\n")
                    i = stop + 1
                    continue
            # A control symbol consumes its following character; commands do not.
            if i + 1 < len(s) and not s[i + 1].isalpha():
                i += 2
                continue
        elif s[i] == "{":
            stack.append(line)
        elif s[i] == "}":
            if stack:
                stack.pop()
            else:
                errors.append(f"unmatched closing brace at line {line}")
        i += 1
    errors.extend(f"unclosed opening brace at line {n}" for n in stack)
    return errors


def environment_errors(s: str) -> list[str]:
    """Check literal environments and math delimiters without expanding macros."""
    s = clean_tex(s)
    env, maths, errors = [], [], []
    token_pattern = r"\\begin\{([^}]+)\}|\\end\{([^}]+)\}|\\(?:[A-Za-z]+|.)|\$\$|\$"
    for match in re.finditer(token_pattern, s):
        token = match.group(0)
        line = s.count("\n", 0, match.start()) + 1
        if match.group(1):
            env.append((match.group(1), line))
        elif match.group(2):
            if not env or env[-1][0] != match.group(2):
                errors.append(f"environment mismatch at line {line}: {token}")
            else:
                env.pop()
        elif token in (r"\[", r"\("):
            if maths:
                errors.append(f"nested explicit math delimiter at line {line}: {token}")
            maths.append((token, line))
        elif token in (r"\]", r"\)"):
            expected = r"\[" if token == r"\]" else r"\("
            if not maths or maths[-1][0] != expected:
                errors.append(f"math delimiter mismatch at line {line}: {token}")
            else:
                maths.pop()
        elif token in ("$", "$$"):
            if maths and maths[-1][0] == token:
                maths.pop()
            else:
                maths.append((token, line))
    errors.extend(f"unclosed environment {name} from line {line}" for name, line in env)
    errors.extend(f"unclosed math delimiter {name} from line {line}" for name, line in maths)
    return errors


def validate(root: Path, final: bool) -> dict:
    errors, warnings, information = [], [], []
    completed, page_text, unclassified = [], {}, Counter()
    expected = {f"{STEM}_136_scan{n}.tex": n for n in SCANS}
    page_dir = root / "pages"
    actual = list(page_dir.glob("*.tex")) if page_dir.is_dir() else []
    for path in sorted(actual):
        if path.name not in expected:
            errors.append(f"unexpected page filename: {path.name}")
            continue
        n = expected[path.name]
        content = path.read_text(encoding="utf-8")
        page_text[n] = content
        completed.append(n)
        cleaned = clean_tex(content)
        scans = re.findall(r"\\scanpage\s*\{([^}]+)\}", cleaned)
        if scans != [str(n)]:
            errors.append(f"scan {n}: scanpage markers are {scans!r}")
        cote = re.findall(r"\\cotefile\s*\{([^}]+)\}", cleaned)
        if cote != (["136"] if n == 235 else []):
            errors.append(f"scan {n}: cotefile markers are {cote!r}")
        required_prefix = r"\cotefile{136}" if n == 235 else rf"\scanpage{{{n}}}"
        if not cleaned.lstrip().startswith(required_prefix):
            errors.append(f"scan {n}: missing expected initial marker {required_prefix}")
        errors.extend(f"scan {n}: {e}" for e in brace_errors(content))
        errors.extend(f"scan {n}: {e}" for e in environment_errors(content))
        # Consume control symbols too, so a row break followed by H is not
        # misreported as an undefined command named H.
        commands = [token[1:] for token in re.findall(r"\\(?:[A-Za-z]+|.)", cleaned)
                    if token[1:].isalpha()]
        unclassified.update(c for c in commands if c not in CUSTOM | COMMON)
        forbidden = sorted(set(commands) & {"includegraphics", "includepdf", "epsfig", "epsfbox"})
        if forbidden:
            errors.append(f"scan {n}: forbidden image inclusion commands: {forbidden}")
        if re.search(r"\b(?:OCR|pytesseract|tesseract)\b", content, re.I):
            warnings.append(f"scan {n}: contains an OCR-related string; inspect manually")
    completed.sort()
    missing = [n for n in SCANS if n not in page_text]
    if final and missing:
        errors.append(f"missing scan files: {missing}")
    elif missing:
        information.append(f"partial package: {len(missing)} expected pages not yet present")
    if completed and completed != SCANS[:len(completed)]:
        warnings.append("page files do not form the expected uninterrupted prefix")

    combined_path = root / f"{STEM}_transcription.tex"
    if combined_path.exists():
        combined = combined_path.read_text(encoding="utf-8")
        expected_combined = "".join(page_text[n] for n in completed)
        if combined != expected_combined:
            errors.append("combined transcription is not the exact ordered concatenation of page files")
        if completed and not clean_tex(combined).lstrip().startswith(r"\cotefile{136}"):
            errors.append("combined transcription does not begin with cotefile{136}")
        errors.extend(f"combined transcription: {e}" for e in brace_errors(combined))
    elif final:
        errors.append("combined transcription is missing")
    else:
        information.append("combined transcription is not yet present")

    inventory_path = root / f"{STEM}_inventory.csv"
    inventory_counts = Counter()
    inventory_seen = {}
    previous_scan = None
    if inventory_path.exists():
        with inventory_path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != COLUMNS:
                errors.append(f"inventory columns differ: {reader.fieldnames!r}")
            for rownum, row in enumerate(reader, 2):
                if row.get("transcribed") != "yes":
                    errors.append(f"inventory row {rownum}: transcribed is not yes")
                if row.get("cote") != "136":
                    errors.append(f"inventory row {rownum}: cote is not 136")
                try:
                    n = int(row.get("scan", ""))
                except (ValueError, TypeError):
                    errors.append(f"inventory row {rownum}: invalid scan")
                    continue
                if previous_scan is not None and n < previous_scan:
                    errors.append(f"inventory row {rownum}: scan order decreases from {previous_scan} to {n}")
                previous_scan = n
                element = row.get("element", "")
                element_key = (row.get("cote"), element)
                if not element:
                    errors.append(f"inventory row {rownum}: empty element ID")
                elif element_key in inventory_seen:
                    errors.append(f"inventory row {rownum}: duplicate element ID {element!r}; first at row {inventory_seen[element_key]}")
                else:
                    inventory_seen[element_key] = rownum
                inventory_counts[n] += 1
                if n not in SCANS:
                    errors.append(f"inventory row {rownum}: unexpected scan {n}")
                if row.get("sheet_kind") not in SHEET_KINDS:
                    errors.append(f"inventory row {rownum}: invalid sheet_kind {row.get('sheet_kind')!r}")
                if row.get("kind") not in KINDS:
                    errors.append(f"inventory row {rownum}: invalid kind {row.get('kind')!r}")
                if None in row:
                    errors.append(f"inventory row {rownum}: excess CSV fields")
        for n in completed:
            if not inventory_counts[n]:
                errors.append(f"scan {n}: no inventory rows")
        for n in inventory_counts:
            if n not in completed:
                errors.append(f"scan {n}: inventory rows exist but page file is missing")
    elif final or completed:
        errors.append("inventory is missing")

    log_path = root / "progress.log"
    hash_records, hashes_checked = {}, []
    frozen = False
    if log_path.exists():
        log = log_path.read_text(encoding="utf-8")
        frozen = bool(re.search(r"^transcription frozen\b", log, re.M))
        for line in log.splitlines():
            # Accept filename/hash in either order, with optional sha256 prefix.
            digest_match = re.search(r"\b[0-9a-fA-F]{64}\b", line)
            name_match = re.search(r"(?:pages/)?MPL_136_235-281_(?:136_scan\d{3}|transcription)\.tex", line)
            if digest_match and name_match:
                name = name_match.group(0)
                if "_136_scan" in name and not name.startswith("pages/"):
                    name = "pages/" + name
                digest = digest_match.group(0).lower()
                if name in hash_records and hash_records[name] != digest:
                    errors.append(f"conflicting recorded hashes: {name}")
                hash_records[name] = digest
        for name, digest in hash_records.items():
            path = root / name
            if not path.is_file():
                errors.append(f"recorded hash has missing file: {name}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                errors.append(f"SHA-256 mismatch: {name}")
            else:
                hashes_checked.append(name)
        if frozen or final:
            required_hashes = {f"pages/{name}" for name in expected}
            required_hashes.add(f"{STEM}_transcription.tex")
            missing_hashes = sorted(required_hashes - hash_records.keys())
            if missing_hashes:
                errors.append(f"freeze hashes missing for {len(missing_hashes)} files")
        if final and not frozen:
            errors.append("transcription frozen line is missing from progress.log")
    elif final:
        errors.append("progress.log is missing")

    if final:
        for suffix in ("doubts.md", "notes.md"):
            path = root / f"{STEM}_{suffix}"
            if not path.is_file() or not path.stat().st_size:
                errors.append(f"missing or empty deliverable: {path.name}")
    information.append("OCR provenance and visual fidelity cannot be determined from deliverable text; this validator performs no OCR.")
    return {"ok": not errors, "mode": "final" if final else "partial", "root": str(root),
            "completed_scans": completed, "missing_scans": missing,
            "inventory_rows": sum(inventory_counts.values()),
            "hashes_verified": len(hashes_checked), "frozen_marker_present": frozen,
            "errors": errors, "warnings": warnings, "information": information,
            "unclassified_commands_informational": dict(sorted(unclassified.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parent.parent)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--partial", action="store_true", help="allow pages and final deliverables not yet written (default)")
    mode.add_argument("--final", action="store_true", help="require all 46 pages, final deliverables, and freeze hashes")
    args = parser.parse_args()
    result = validate(args.root.resolve(), args.final)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
