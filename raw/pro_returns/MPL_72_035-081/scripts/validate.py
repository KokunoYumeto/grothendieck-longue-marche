#!/usr/bin/env python3
"""Mechanical checks only; this script never reads manuscript images or changes files."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

PREFIX = "MPL_72_035-081"
SCANS = tuple(range(35, 82))
COLUMNS = [
    "cote", "scan", "sheet_kind", "element", "kind", "position",
    "first_words_or_objects", "transcribed",
]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
ELEMENT_KINDS = {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion",
}
PAGE_RE = re.compile(rf"^{PREFIX}_72_scan(\d{{3}})\.tex$")
TIME_RE = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC"
HASH_RE = re.compile(r"(?<![0-9a-fA-F])([0-9a-fA-F]{64})(?![0-9a-fA-F])")
FILE_RE = re.compile(r"(?:pages/)?(?:MPL_72_035-081_72_scan\d{3}|MPL_72_035-081_transcription)\.tex")
FORBIDDEN = {
    "documentclass", "usepackage", "includegraphics", "input", "include",
    "write", "immediate", "openout", "read", "directlua",
}
CUSTOM = {
    "cotefile", "scanpage", "mspage", "deleted", "inserted", "margin", "uline",
    "uuline", "diagram", "figure", "unsure", "illegible",
}
# Unknown commands are advisory only. Standard LaTeX and TikZ vocabularies are open.
KNOWN = CUSTOM | set("""
begin end label ref eqref tag notag nonumber text textrm textsf texttt textbf
textit textsc textnormal emph underline overline bar hat widehat tilde widetilde
vec dot ddot dddot acute grave breve check mathring overbrace underbrace
frac dfrac tfrac binom dbinom tbinom cfrac sqrt root left right middle big Big
bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr limits nolimits
mathrm mathbf mathit mathsf mathtt mathcal mathfrak mathbb mathscr boldsymbol
operatorname stackrel overset underset substack smash phantom hphantom vphantom
ensuremath mbox hbox vbox fbox boxed centering center raggedright raggedleft
displaystyle textstyle scriptstyle scriptscriptstyle newpage clearpage par noindent
indent linebreak newline pagebreak nolinebreak nopagebreak hfill vfill hspace vspace
quad qquad enspace thinspace medspace thickspace negthinspace kern mkern relax
small tiny scriptsize footnotesize normalsize large Large LARGE huge Huge
rm bf it sl sc tt cal bmod pmod mod pod det dim ker coker hom Hom Aut End GL SL
lim limsup liminf colim sup inf max min log ln exp sin cos tan cot sec csc
sinh cosh tanh arcsin arccos arctan arg deg gcd Pr tr diag rank id
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon
phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
aleph beth gimel daleth hbar imath jmath ell wp Re Im partial nabla infty
emptyset varnothing top bot angle measuredangle sphericalangle triangle square Box
forall exists nexists neg lnot land wedge lor vee bigwedge bigvee cap cup bigcap
bigcup uplus biguplus sqcap sqcup bigsqcup setminus smallsetminus complement
in ni notin owns subset supset subseteq supseteq subsetneq supsetneq subsetneqq
supsetneqq nsubseteq nsupseteq sqsubset sqsupset sqsubseteq sqsupseteq
le leq leqslant ge geq geqslant ne neq lt gt ll gg lll ggg lesssim gtrsim
prec succ preceq succeq sim simeq approx approxeq asymp cong equiv propto
doteq triangleq coloneqq eqqcolon coloneq eqcolon not nmid mid parallel nparallel
perp models vdash dashv Vdash Vvdash bowtie smile frown Join
to gets mapsto longmapsto hookrightarrow hookleftarrow rightarrow leftarrow
leftrightarrow Rightarrow Leftarrow Leftrightarrow longrightarrow longleftarrow
longleftrightarrow Longrightarrow Longleftarrow Longleftrightarrow uparrow downarrow
updownarrow Uparrow Downarrow Updownarrow nearrow searrow swarrow nwarrow
rightarrowtail leftarrowtail twoheadrightarrow twoheadleftarrow rightsquigarrow
leftrightsquigarrow leadsto rightharpoonup rightharpoondown leftharpoonup
leftharpoondown rightleftarrows leftrightarrows rightleftharpoons leftrightharpoons
multimap looparrowright looparrowleft curvearrowright curvearrowleft
pm mp times div cdot cdotp ast star circ bullet diamond oplus ominus otimes
oslash odot bigoplus bigotimes bigodot amalg wr dagger ddagger setminus
sum prod coprod int iint iiint oint oiint iiiint dots ldots cdots vdots ddots
langle rangle lbrace rbrace lbrack rbrack lceil rceil lfloor rfloor lvert rvert
lVert rVert vert Vert backslash slash prime backprime surd colon checkmark
textquotedblleft textquotedblright textquoteleft textquoteright guillemotleft
guillemotright textdegree textendash textemdash textbackslash textasciitilde
textasciicircum textless textgreater textbar textbraceleft textbraceright textdagger
textdaggerdbl textbullet textellipsis copyright pounds S P dag ddag ae AE oe OE
aa AA o O ss i j l L TeX LaTeX euro c H k r t u v b d
arraystretch tabcolsep multicolumn multirow hline cline top rule midrule bottomrule
toprule addlinespace cmidrule arraybackslash shortstack makebox resizebox scalebox
rotatebox color textcolor colorbox rule raisebox pmb cancel bcancel xcancel
tikz node draw path coordinate fill filldraw clip foreach matrix arrow arrows ar
pgfmathsetmacro pgfmathtruncatemacro pgfmathparse pgfmathresult pgfplotsset
tikzset pgfkeys scope endscope pgftransformshift pgfpoint
endash emdash mathbin mathrel diagdown sharp textcircled xrightarrow xleftarrow
""".split())


def scan_tex(text: str):
    """Strip comments and count braces, respecting control symbols such as \\{ and \\%."""
    cleaned = []
    commands = []
    issues = []
    stack = []
    line = 1
    i = 0
    while i < len(text):
        char = text[i]
        if char == "%":
            end = text.find("\n", i)
            if end < 0:
                break
            i = end
            continue
        if char == "\\":
            start = i
            i += 1
            if i == len(text):
                issues.append(f"line {line}: trailing backslash")
                cleaned.append("\\")
                break
            if text[i].isalpha() or text[i] == "@":
                j = i
                while i < len(text) and (text[i].isalpha() or text[i] == "@"):
                    i += 1
                command = text[j:i]
                commands.append((command, line))
                if command == "verb":
                    if i < len(text) and text[i] == "*":
                        i += 1
                    if i < len(text):
                        delimiter = text[i]
                        end = text.find(delimiter, i + 1)
                        if end < 0:
                            issues.append(f"line {line}: unterminated \\verb")
                            end = len(text) - 1
                        line += text[i:end + 1].count("\n")
                        i = end + 1
                cleaned.append(text[start:i])
            else:
                if text[i] == "\n":
                    line += 1
                i += 1
                cleaned.append(text[start:i])
            continue
        if char == "{":
            stack.append(line)
        elif char == "}":
            if stack:
                stack.pop()
            else:
                issues.append(f"line {line}: unmatched closing brace")
        if char == "\n":
            line += 1
        cleaned.append(char)
        i += 1
    for opening_line in stack:
        issues.append(f"line {opening_line}: unmatched opening brace")
    return "".join(cleaned), commands, issues


def validate_tree(root: Path, mode="checkpoint", warn_unknown=False):
    root = root.resolve()
    result = {"root": str(root), "mode": mode, "errors": [], "warnings": [], "facts": {}}
    errors, warnings, facts = result["errors"], result["warnings"], result["facts"]
    found = {}
    page_dir = root / "pages"
    for path in sorted(page_dir.glob("*.tex")):
        match = PAGE_RE.match(path.name)
        if not match:
            errors.append(f"Unexpected page filename: {path.name}")
            continue
        scan = int(match[1])
        if scan not in SCANS:
            errors.append(f"Page outside requested scan range: {path.name}")
            continue
        found[scan] = path
    missing = [s for s in SCANS if s not in found]
    facts["page_count"] = len(found)
    facts["expected_page_count"] = len(SCANS)
    facts["missing_scans"] = missing
    if missing:
        message = "Missing page files: " + ", ".join(f"{s:03d}" for s in missing)
        (errors if mode == "final" else warnings).append(message)
    if found:
        gaps = [s for s in range(min(SCANS), max(found)) if s not in found]
        if gaps:
            errors.append("Gap before latest written page: " + ", ".join(map(str, gaps)))

    page_bytes = []
    page_cleaned = {}
    macros = Counter()
    for scan, path in sorted(found.items()):
        raw = path.read_bytes()
        page_bytes.append(raw)
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path.name}: invalid UTF-8 ({exc})")
            continue
        clean, commands, syntax_issues = scan_tex(text)
        page_cleaned[scan] = clean
        errors.extend(f"{path.name}: {item}" for item in syntax_issues)
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)
        if markers != [str(scan)]:
            errors.append(f"{path.name}: scanpage markers {markers!r}; expected [{str(scan)!r}]")
        for command, line in commands:
            macros[command] += 1
            if command in FORBIDDEN:
                errors.append(f"{path.name}:{line}: disallowed fragment command \\{command}")
        envs = []
        for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
            operation, environment = match.groups()
            line = clean[:match.start()].count("\n") + 1
            if operation == "begin":
                envs.append((environment, line))
            elif not envs or envs[-1][0] != environment:
                errors.append(f"{path.name}:{line}: unmatched or misordered end of {environment}")
            else:
                envs.pop()
        errors.extend(f"{path.name}:{line}: unclosed environment {env}" for env, line in envs)
        for match in re.finditer(r"\\illegible\s*\{([^{}]*)\}", clean):
            if not match[1].strip().isdigit():
                warnings.append(f"{path.name}: illegible argument is not an integer: {match[1]!r}")
    facts["custom_macro_counts"] = {name: macros[name] for name in sorted(CUSTOM)}
    unknown = sorted(set(macros) - KNOWN - FORBIDDEN)
    facts["unclassified_commands"] = unknown
    if warn_unknown and unknown:
        warnings.append("Commands requiring manual classification: " + ", ".join("\\" + x for x in unknown))

    combined = root / f"{PREFIX}_transcription.tex"
    if not combined.exists():
        (errors if mode == "final" else warnings).append("Combined transcription file is absent")
    else:
        combined_bytes = combined.read_bytes()
        candidates = {
            "direct byte concatenation": b"".join(page_bytes),
            "one newline between page files": b"\n".join(page_bytes),
            "two newlines between page files": b"\n\n".join(page_bytes),
        }
        style = next((name for name, value in candidates.items() if value == combined_bytes), None)
        facts["combined_concatenation"] = style
        if style is None:
            errors.append("Combined transcription differs from page files under all supported separator styles")
        try:
            clean, _, syntax_issues = scan_tex(combined_bytes.decode("utf-8"))
            errors.extend(f"Combined transcription: {item}" for item in syntax_issues)
            if not re.match(r"\s*\\cotefile\s*\{72\}\s*\\scanpage\s*\{35\}", clean):
                errors.append("Combined transcription must begin with cotefile{72}, then scanpage{35}")
            markers = [int(x) for x in re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", clean)]
            if markers != sorted(found):
                errors.append(f"Combined scanpage order differs from present page files: {markers}")
        except UnicodeDecodeError as exc:
            errors.append(f"Combined transcription: invalid UTF-8 ({exc})")

    inventory = root / f"{PREFIX}_inventory.csv"
    if not inventory.exists():
        (errors if mode == "final" else warnings).append("Inventory CSV is absent")
    else:
        counts = Counter()
        identifiers = set()
        try:
            with inventory.open(encoding="utf-8-sig", newline="") as stream:
                reader = csv.DictReader(stream)
                if reader.fieldnames != COLUMNS:
                    errors.append(f"Inventory header must be {COLUMNS!r}; found {reader.fieldnames!r}")
                for row_number, row in enumerate(reader, 2):
                    lead = f"Inventory row {row_number}"
                    if None in row:
                        errors.append(f"{lead}: surplus CSV fields")
                    if row.get("cote", "").strip() != "72":
                        errors.append(f"{lead}: cote must be 72")
                    try:
                        scan = int(row.get("scan", ""))
                    except (ValueError, TypeError):
                        errors.append(f"{lead}: invalid scan number")
                        continue
                    if scan not in SCANS:
                        errors.append(f"{lead}: scan {scan} outside requested range")
                    if scan not in found:
                        errors.append(f"{lead}: no page file for scan {scan}")
                    counts[scan] += 1
                    if row.get("sheet_kind") not in SHEET_KINDS:
                        errors.append(f"{lead}: unsupported sheet_kind {row.get('sheet_kind')!r}")
                    if row.get("kind") not in ELEMENT_KINDS:
                        errors.append(f"{lead}: unsupported element kind {row.get('kind')!r}")
                    if row.get("transcribed") != "yes":
                        errors.append(f"{lead}: transcribed must equal 'yes'")
                    for field in ("element", "position", "first_words_or_objects"):
                        if not (row.get(field) or "").strip():
                            errors.append(f"{lead}: empty {field}")
                    key = (scan, row.get("element"))
                    if key in identifiers:
                        warnings.append(f"{lead}: duplicate element identifier {key!r}")
                    identifiers.add(key)
        except (UnicodeError, csv.Error) as exc:
            errors.append(f"Inventory could not be parsed: {exc}")
        facts["inventory_row_count"] = sum(counts.values())
        facts["inventory_rows_by_scan"] = dict(sorted(counts.items()))
        for scan in found:
            if not counts[scan]:
                errors.append(f"No inventory rows for written scan {scan:03d}")

    for suffix in ("doubts.md", "notes.md"):
        path = root / f"{PREFIX}_{suffix}"
        if not path.exists():
            (errors if mode == "final" else warnings).append(f"Missing {path.name}")

    log_path = root / "progress.log"
    if not log_path.exists():
        (errors if mode == "final" else warnings).append("progress.log is absent")
    else:
        log = log_path.read_text(encoding="utf-8")
        lines = log.splitlines()
        if not lines or not re.fullmatch(TIME_RE, lines[0]):
            errors.append("progress.log first line must be a UTC time in YYYY-MM-DD HH:MM:SS UTC form")
        else:
            started = datetime.strptime(lines[0], "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
            facts["seconds_since_start"] = round((datetime.now(timezone.utc) - started).total_seconds())
        done = []
        audited = []
        audit_line_indices = {}
        for index, line in enumerate(lines):
            done_match = re.fullmatch(rf"72 scan (\d{{3}}) done ({TIME_RE})", line)
            if done_match:
                done.append(int(done_match[1]))
            audit_match = re.fullmatch(rf"scan (\d{{3}}) audited ({TIME_RE})", line)
            if audit_match:
                scan = int(audit_match[1])
                audited.append(scan)
                audit_line_indices.setdefault(scan, index)
        facts["done_log_scans"] = done
        facts["audited_log_scans"] = audited
        for scan in found:
            if scan not in done:
                errors.append(f"Written scan {scan:03d} has no correctly formatted done log line")
        for scan in done:
            if scan not in found:
                errors.append(f"Done log claims scan {scan:03d}, but its page file is absent")
        if done != sorted(set(done)):
            warnings.append("Done log lines contain repeated scans or are out of ascending scan order")
        frozen_indices = [i for i, line in enumerate(lines) if re.fullmatch(rf"transcription frozen {TIME_RE}", line)]
        context_indices = [i for i, line in enumerate(lines) if re.fullmatch(rf"context opened {TIME_RE}", line)]
        facts["frozen_log_line_count"] = len(frozen_indices)
        facts["context_opened_log_line_count"] = len(context_indices)
        if mode == "final" or frozen_indices or context_indices:
            for scan in SCANS:
                if scan not in audited:
                    errors.append(f"Scan {scan:03d} has no correctly formatted audited log line")
            if not frozen_indices:
                errors.append("No correctly formatted transcription frozen log line")
            if mode == "final" and not context_indices:
                errors.append("No correctly formatted context opened log line")
        if frozen_indices:
            frozen_index = frozen_indices[0]
            for scan, index in audit_line_indices.items():
                if index > frozen_index:
                    errors.append(f"Scan {scan:03d} was first audited after the freeze log line")
            if context_indices and min(context_indices) < frozen_index:
                errors.append("Context was opened before the transcription freeze log line")
            # Accept sha256sum lines and filename: digest / SHA-256 filename digest forms.
            frozen_hashes = {}
            freeze_boundary = min(context_indices) if context_indices else len(lines)
            for line in lines[:freeze_boundary]:
                hashes = HASH_RE.findall(line)
                paths = FILE_RE.findall(line)
                if len(hashes) == 1 and len(paths) == 1:
                    frozen_hashes[Path(paths[0]).name] = hashes[0].lower()
            required = list(found.values()) + ([combined] if combined.exists() else [])
            for path in required:
                recorded = frozen_hashes.get(path.name)
                if recorded is None:
                    errors.append(f"No pre-context SHA-256 recorded for {path.name}")
                else:
                    current = hashlib.sha256(path.read_bytes()).hexdigest()
                    if current != recorded:
                        errors.append(f"Frozen hash mismatch for {path.name}")
            facts["recorded_frozen_hash_count"] = len(frozen_hashes)
            if mode == "final":
                after_context = "\n".join(lines[min(context_indices) + 1:]) if context_indices else ""
                if not re.search(r"(?i)(hash(?:es)?|sha.?256).*(unchanged|match|verified)", after_context):
                    warnings.append("No recognized final hash-unchanged statement after opening context")
    facts["scope"] = (
        "Mechanical consistency only. No images are read; no claim is made about reading accuracy, "
        "element completeness, correct placement of doubt macros, or the adequacy of research notes."
    )
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--mode", choices=("checkpoint", "final"), default="checkpoint")
    parser.add_argument("--warn-unknown-macros", action="store_true")
    parser.add_argument("--json", action="store_true", help="Print the full result as JSON to stdout")
    args = parser.parse_args()
    result = validate_tree(args.root, args.mode, args.warn_unknown_macros)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Mechanical validation ({args.mode}): {len(result['errors'])} errors; {len(result['warnings'])} warnings")
        print(f"Page files: {result['facts'].get('page_count', 0)}/47")
        for item in result["errors"]:
            print("ERROR: " + item)
        for item in result["warnings"]:
            print("WARNING: " + item)
        print(result["facts"]["scope"])
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
