#!/usr/bin/env python3
"""Mechanical validation only: this script does not assess readings or proofs.

Run from any directory. Exit status: 0 complete/pass, 1 structural failure,
2 incomplete work with no structural failure. Reports are printed; files are
written only when --json-report or --text-report is explicitly supplied.

The combined fragment must equal b''.join(page_bytes_in_scan_order).
Freeze records in progress.log may use normal sha256sum syntax or
``SHA256 relative/path HEXDIGEST``. All 25 transcription files must be recorded.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

PREFIX = "SP31_CW_156-3"
SCANS = tuple(range(2, 26))
INVENTORY_HEADER = "scan,sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed".split(",")
COLLATION_HEADER = "folder,their_page,our_scan,line,their_reading,codex_reading,final_reading,scan_shows,kind,marked_in_H,confidence".split(",")
CHECK_HEADER = "statement_id,date,who,type,outcome".split(",")
COLLATION_KINDS = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state (struck given live or live given struck)",
    "insertion or placement", "abbreviation expanded or spelling modernised",
    r"readable ink left as \ill{}", "drawing or diagram", "other",
}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
SHEET_KINDS = {"text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover"}
CHECK_TYPES = {"targeted proof check", "independent re-proof", "computation or formal certificate",
               "used and rechecked in this run", "carried as background without fault found"}
DIPLOMATIC_COMMANDS = set("cotefile scanpage mspage unsure illegible handwritten deleted inserted margin diagram figure".split())
STANDARD_COMMANDS = set("""
begin end text textrm textsf texttt textup textit textsl textsc textbf textmd emph
mathrm mathsf mathtt mathnormal mathit mathbf mathcal mathscr mathfrak mathbb operatorname
mathord mathop mathbin mathrel mathopen mathclose mathpunct mathinner
frac dfrac tfrac binom dbinom tbinom cfrac genfrac sqrt root over atop choose
left right middle big Big bigg Bigg bigl bigr bigm Bigl Bigr Bigm biggl biggr biggm Biggl Biggr Biggm
overline underline widehat widetilde hat tilde bar vec dot ddot dddot ddddot acute grave breve check
overbrace underbrace overset underset stackrel substack boxed phantom hphantom vphantom smash
quad qquad enspace thinspace medspace thickspace hspace vspace hfill vfill hskip vskip kern mkern
rule raisebox rotatebox scalebox resizebox makebox framebox mbox fbox parbox llap rlap
par noindent indent newline linebreak pagebreak newpage clearpage smallskip medskip bigskip
tiny scriptsize footnotesize small normalsize large Large LARGE huge Huge
displaystyle textstyle scriptstyle scriptscriptstyle limits nolimits displaylimits
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
aleph hbar imath jmath ell wp Re Im partial nabla infty prime emptyset varnothing complement
forall exists nexists neg lnot top bot angle measuredangle sphericalangle triangle square Box Diamond
in notin ni owns subset subseteq subsetneq subsetneqq nsubseteq sqsubset sqsubseteq
supset supseteq supsetneq supsetneqq nsupseteq sqsupset sqsupseteq
le leq leqslant leqq ge geq geqslant geqq ne neq nleq ngeq nless ngtr lesssim gtrsim ll gg
equiv sim simeq approx cong asymp propto doteq prec preceq succ succeq parallel nparallel perp mid nmid
cup cap bigcup bigcap uplus biguplus sqcup sqcap bigsqcup setminus smallsetminus
wedge vee land lor bigwedge bigvee times div cdot ast star circ bullet odot oplus otimes ominus oslash
bigodot bigoplus bigotimes dagger ddagger amalg wr pm mp triangleleft triangleright lhd rhd unlhd unrhd
sum prod coprod int iint iiint iiiint oint oiint bigtriangleup bigtriangledown
to mapsto longmapsto gets leftarrow rightarrow leftrightarrow longleftarrow longrightarrow longleftrightarrow
Leftarrow Rightarrow Leftrightarrow Longleftarrow Longrightarrow Longleftrightarrow
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow nearrow searrow swarrow nwarrow
hookrightarrow hookleftarrow twoheadrightarrow twoheadleftarrow rightleftarrows leftrightarrows
rightrightarrows leftleftarrows rightleftharpoons leftrightharpoons harpoonleft harpoonright
longleftrightarrow xrightarrow xleftarrow leadsto rightsquigarrow dashrightarrow dashleftarrow
langle rangle lbrace rbrace lceil rceil lfloor rfloor lvert rvert lVert rVert vert Vert backslash
ldots cdots vdots ddots dots dotsc dotsb dotsm dotsi dotso
sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh coth log ln exp det dim gcd hom ker
Pr deg arg lim liminf limsup inf sup max min injlim projlim varliminf varlimsup varinjlim varprojlim
textcircled textquotedbl textquoteleft textquoteright textquotedblleft textquotedblright textasciicircum textasciitilde
textbackslash textbar textless textgreater textendash textemdash textsuperscript textsubscript
uline uuline uwave sout xout dashuline dotuline normalem checkmark blacksquare blacktriangle blacktriangledown
item label ref eqref pageref footnote footnotemark footnotetext marginpar caption multicolumn intertext shortintertext
color textcolor colorbox fcolorbox ensuremath protect relax unskip strut mathstrut boldsymbol pmb
tikz draw node coordinate path fill filldraw clip shade shadedraw foreach matrix arrow ar
pgfmathsetmacro pgfmathsetlengthmacro pgfmathparse pgfmathresult pgfextra pgfresetboundingbox
tikzset pgfsetarrows pgfsetlinewidth pgftransformrotate pgftransformshift
verb documentclass usepackage newcommand renewcommand
""".split())


def control_words(text: str) -> list[tuple[str,int,int]]:
    """Lex actual TeX control words; a row break followed by X is not \\X."""
    result=[];i=0;line=1
    while i<len(text):
        if text[i]=='\n':line+=1;i+=1
        elif text[i]=='%':
            j=text.find('\n',i);i=len(text) if j<0 else j
        elif text[i]=='\\':
            m=re.match(r'\\([A-Za-z@]+)',text[i:])
            if not m:i+=2;continue
            name=m.group(1);result.append((name,line,i));i+=len(m.group(0))
            if name=='verb':
                if i<len(text) and text[i]=='*':i+=1
                if i<len(text):
                    j=text.find(text[i],i+1)
                    if j>=0:line+=text[i:j+1].count('\n');i=j+1
        else:i+=1
    return result


def expected_filename(scan: int) -> str:
    batch = 1 if scan < 10 else 2 if scan < 18 else 3
    return f"J156-3-{batch:02d}_156-3_scan{scan:03d}.tex"


def latex_structure(text: str) -> list[str]:
    """Check delimiters with TeX comments/control sequences respected.

    This is a structural check, not a TeX engine. It permits nested math
    delimiters within text-like braces of an enclosing formula. It ignores
    verb/verbatim bodies and treats a control symbol (including \\%, \\{ and
    \\}) as one lexical token. Environment names must match in LIFO order.
    """
    errors: list[str] = []
    braces: list[int] = []
    envs: list[tuple[str, int]] = []
    math: list[tuple[str, int, int]] = []
    i, line, n = 0, 1, len(text)

    def math_token(token: str) -> None:
        depth = len(braces)
        if token in ("$", "$$"):
            if math and math[-1][0] == token and math[-1][2] == depth:
                math.pop()
            else:
                math.append((token, line, depth))
        elif token in (r"\(", r"\["):
            math.append((token, line, depth))
        else:
            opener = {r"\)": r"\(", r"\]": r"\["}[token]
            if math and math[-1][0] == opener and math[-1][2] == depth:
                math.pop()
            else:
                errors.append(f"line {line}: unmatched math closer {token}")

    while i < n:
        char = text[i]
        if char == "\n":
            line += 1
            i += 1
        elif char == "%":
            eol = text.find("\n", i)
            i = n if eol == -1 else eol
        elif char == "\\":
            if i + 1 >= n:
                errors.append(f"line {line}: terminal backslash")
                i += 1
                continue
            if text[i + 1] in "()[]":
                math_token(text[i:i + 2])
                i += 2
                continue
            command = re.match(r"\\([A-Za-z@]+)", text[i:])
            if not command:
                i += 2
                continue
            name = command.group(1)
            j = i + len(command.group(0))
            if name == "verb":
                if j < n and text[j] == "*":
                    j += 1
                if j >= n or text[j] == "\n":
                    errors.append(f"line {line}: missing verb delimiter")
                    i = j
                    continue
                close = text.find(text[j], j + 1)
                eol = text.find("\n", j)
                if close < 0 or (eol >= 0 and eol < close):
                    errors.append(f"line {line}: unterminated verb")
                    i = n if eol < 0 else eol
                else:
                    i = close + 1
                continue
            if name in {"begin", "end"}:
                arg = re.match(r"\s*\{([^{}]+)\}", text[j:])
                if not arg:
                    errors.append(f"line {line}: malformed {name} environment token")
                    i = j
                    continue
                env = arg.group(1)
                token_end = j + len(arg.group(0))
                if name == "begin" and env in {"verbatim", "verbatim*", "Verbatim", "lstlisting"}:
                    end_token = r"\end{" + env + "}"
                    end = text.find(end_token, token_end)
                    if end < 0:
                        errors.append(f"line {line}: unclosed environment {env}")
                        break
                    next_i = end + len(end_token)
                    line += text[i:next_i].count("\n")
                    i = next_i
                    continue
                if name == "begin":
                    envs.append((env, line))
                elif envs and envs[-1][0] == env:
                    envs.pop()
                else:
                    expected = envs[-1][0] if envs else "none"
                    errors.append(f"line {line}: end {env}, expected {expected}")
                line += text[i:token_end].count("\n")
                i = token_end
                continue
            i = j
        elif char == "{":
            braces.append(line)
            i += 1
        elif char == "}":
            if not braces:
                errors.append(f"line {line}: unmatched closing brace")
            else:
                depth = len(braces)
                while math and math[-1][2] >= depth:
                    token, opened, _ = math.pop()
                    errors.append(f"line {opened}: unclosed math {token} before closing brace on line {line}")
                braces.pop()
            i += 1
        elif char == "$":
            token = "$$" if text.startswith("$$", i) else "$"
            math_token(token)
            i += len(token)
        else:
            i += 1
    errors.extend(f"line {where}: unclosed brace" for where in braces)
    errors.extend(f"line {where}: unclosed environment {env}" for env, where in envs)
    errors.extend(f"line {where}: unclosed math {token}" for token, where, _ in math)
    return errors


def validate(out: Path) -> dict:
    report = {"status": "pass", "errors": [], "incomplete": [], "warnings": [], "counts": {}}
    errors, incomplete, warnings = report["errors"], report["incomplete"], report["warnings"]
    allowed_commands=STANDARD_COMMANDS|DIPLOMATIC_COMMANDS
    for preamble in [out/'PREAMBLE.tex',out.parent/'source/SP31_CW_156-3_witnesses/codex/J156-3-01/PREAMBLE.tex']:
        if preamble.exists():
            allowed_commands.update(re.findall(r'\\(?:newcommand|renewcommand)\*?\s*\{?\\([A-Za-z@]+)',preamble.read_text(encoding='utf-8')))
    unknown_commands=[]
    expected = [out / "pages" / expected_filename(s) for s in SCANS]
    found = set((out / "pages").glob("*.tex"))
    extra = found - set(expected)
    errors.extend(f"unexpected page file: {p.name}" for p in sorted(extra))
    page_bytes = []
    marks = {"unsure": 0, "illegible": 0, "deleted": 0, "inserted": 0}
    for scan, path in zip(SCANS, expected):
        if not path.exists():
            incomplete.append(f"missing scan {scan:03d}: {path.name}")
            continue
        raw = path.read_bytes()
        page_bytes.append(raw)
        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"{path.name}: not UTF-8")
            continue
        if not content.strip():
            errors.append(f"{path.name}: empty file")
        errors.extend(f"{path.name}: {e}" for e in latex_structure(content))
        for command,line,_ in control_words(content):
            if command not in allowed_commands:
                unknown_commands.append({'file':path.name,'line':line,'command':command})
                message=f"{path.name}: line {line}: control word \\{command} is absent from PREAMBLE and the standard allowlist"
                if re.fullmatch(r'(?:in|notin|subset|subseteq|supset|supseteq|to|le|leq|ge|geq|neq|simeq|cong|times|cap|cup|land|lor|wedge|vee|setminus|rightarrow|leftarrow)[A-Z][A-Za-z]*',command):
                    errors.append(message+'; likely missing delimiter after an operator')
                else:warnings.append(message+'; inspect without assuming a replacement')
        scan_tags = re.findall(r"\\scanpage\{(\d+)\}", content)
        if scan_tags != [str(scan)]:
            errors.append(f"{path.name}: expected one scanpage tag {scan}, found {scan_tags}")
        if re.search(r"\\(?:documentclass|newcommand|renewcommand|usepackage)\b", content):
            errors.append(f"{path.name}: preamble/macro definition inside fragment")
        for mark in marks:
            marks[mark] += len(re.findall(r"\\" + mark + r"\s*\{", content))
    report["counts"]["pages"] = len(page_bytes)
    report["counts"]["marks"] = marks
    report['unknown_control_words']=unknown_commands
    combined = out / f"{PREFIX}_transcription.tex"
    if not combined.exists():
        incomplete.append(f"missing {combined.name}")
    elif combined.read_bytes() != b"".join(page_bytes):
        errors.append("combined fragment is not exact byte concatenation of available pages in scan order (rerun after any concurrent page save)")

    def table(filename: str, expected_header: list[str], delimiter: str) -> list[dict]:
        path = out / filename
        if not path.exists():
            incomplete.append(f"missing {filename}")
            return []
        try:
            with path.open(encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f, delimiter=delimiter)
                header = reader.fieldnames
                if header != expected_header:
                    errors.append(f"{filename}: header {header!r}; expected {expected_header!r}")
                    return []
                rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"{filename}: {exc}")
            return []
        for index, row in enumerate(rows, 2):
            if None in row or any(value is None for value in row.values()):
                errors.append(f"{filename}: row {index} has wrong field count")
        report["counts"][filename] = len(rows)
        return rows

    inventory = table(f"{PREFIX}_inventory.csv", INVENTORY_HEADER, ",")
    inventory_scans = set()
    inventory_ids = set()
    for index, row in enumerate(inventory, 2):
        where = f"inventory row {index}"
        try:
            scan = int(row["scan"])
            inventory_scans.add(scan)
            if scan not in SCANS:
                errors.append(f"{where}: out-of-range scan {scan}")
        except (TypeError, ValueError):
            errors.append(f"{where}: invalid scan")
        if row["kind"] not in ELEMENT_KINDS:
            errors.append(f"{where}: unknown element kind {row['kind']!r}")
        if row["sheet_kind"] not in SHEET_KINDS:
            errors.append(f"{where}: unknown sheet_kind {row['sheet_kind']!r}")
        if row["transcribed"] != "yes":
            incomplete.append(f"{where}: transcribed is not yes")
        if any(not row.get(k) for k in INVENTORY_HEADER):
            errors.append(f"{where}: empty required field")
        key=(row["scan"],row["element"])
        if key in inventory_ids:
            errors.append(f"{where}: duplicate scan/element identifier {key!r}")
        inventory_ids.add(key)
    for scan in SCANS:
        if scan not in inventory_scans:
            incomplete.append(f"inventory has no element for scan {scan:03d}")

    collation = table(f"{PREFIX}_collation.tsv", COLLATION_HEADER, "\t")
    for index, row in enumerate(collation, 2):
        where = f"collation row {index}"
        try:
            scan, their_page = int(row["our_scan"]), int(row["their_page"])
            if scan not in SCANS or their_page != scan - 1:
                errors.append(f"{where}: invalid our_scan/their_page mapping")
            expected_folder = expected_filename(scan).split("_", 1)[0]
            if row["folder"] != expected_folder:
                errors.append(f"{where}: folder does not match scan")
        except (TypeError, ValueError):
            errors.append(f"{where}: invalid scan/page number")
        if row["kind"] not in COLLATION_KINDS:
            errors.append(f"{where}: invalid kind {row['kind']!r}")
        if row["confidence"] not in {"high", "medium", "low"}:
            errors.append(f"{where}: invalid confidence")
        if row["marked_in_H"] not in {"yes", "no"}:
            errors.append(f"{where}: marked_in_H must be yes or no")
        if any(not row.get(k) for k in ["folder","their_page","our_scan","line","scan_shows","kind","marked_in_H","confidence"]):
            errors.append(f"{where}: empty required location/evidence/classification field")
    events=table("CHECK_EVENTS.tsv", CHECK_HEADER, "\t")
    for index,row in enumerate(events,2):
        where=f"CHECK_EVENTS.tsv row {index}"
        if any(not row.get(k) for k in CHECK_HEADER):
            errors.append(f"{where}: empty required field")
        event_type=row.get("type") or ""
        if event_type not in CHECK_TYPES and not re.match(r"^refuted(?:\b|[,;:])",event_type):
            errors.append(f"{where}: unsupported check-event type {event_type!r}")
        if not re.match(r"^\d{4}-\d\d-\d\d(?:[ T].*)?$",row.get("date") or ""):
            warnings.append(f"{where}: date is not ISO-formatted; verify it manually")
    for name in [f"{PREFIX}_changes.md", f"{PREFIX}_doubts.md", f"{PREFIX}_notes.md", "progress.log"]:
        path = out / name
        if not path.exists() or not path.stat().st_size:
            incomplete.append(f"missing or empty {name}")

    log_path = out / "progress.log"
    if log_path.exists():
        log = log_path.read_text(encoding="utf-8")
        first_line=log.splitlines()[0] if log.splitlines() else ""
        if not re.fullmatch(r"\d{4}-\d\d-\d\d[ T]\d\d:\d\d:\d\d(?: UTC|Z|\+00:00)",first_line):
            errors.append("progress.log first line is not a recognized UTC timestamp")
        freeze_marker=re.search(r"(?m)^transcription frozen .+$",log)
        context_marker=re.search(r"(?m)^context opened .+$",log)
        frozen = bool(freeze_marker)
        hashes = {}
        for line in log.splitlines():
            match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line)
            if match:
                digest, path = match.groups()
            else:
                match = re.fullmatch(r"(?:SHA-?256|sha-?256)\s+(.+?)\s+([0-9a-fA-F]{64})", line)
                if match:
                    path, digest = match.groups()
                else:
                    continue
            if path in hashes and hashes[path] != digest.lower():
                errors.append(f"conflicting recorded hashes for {path}")
            hashes[path] = digest.lower()
        for name, digest in hashes.items():
            path = Path(name)
            path = path if path.is_absolute() else out / path
            if not path.exists():
                errors.append(f"frozen hash path missing: {name}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                errors.append(f"frozen hash mismatch: {name}")
        if frozen:
            resolved_hashed = {(Path(name) if Path(name).is_absolute() else out / name).resolve() for name in hashes}
            for path in expected + [combined]:
                if path.resolve() not in resolved_hashed:
                    errors.append(f"frozen transcription lacks hash for {path.relative_to(out)}")
            if context_marker and context_marker.start() < freeze_marker.start():
                errors.append("progress log records context opening before freeze")
        else:
            incomplete.append("transcription not yet recorded as frozen")
            if context_marker:
                errors.append("progress log records context opening without a transcription freeze")
        if not context_marker:
            incomplete.append("context opening not yet recorded")
        unchanged=re.search(r"(?im)^.*(?:hash[^\n]*unchanged|unchanged[^\n]*hash).*$",log)
        if not unchanged:
            incomplete.append("final confirmation that frozen hashes remain unchanged not yet recorded")
        elif context_marker and unchanged.start()<context_marker.start():
            incomplete.append("unchanged-hash confirmation predates context opening; final confirmation still needed")
        first_done={};first_audited={}
        for scan in SCANS:
            for phase in ("done", "audited"):
                match=re.search(rf"(?m)^scan {scan:03d} {phase} .+$", log)
                if not match:
                    incomplete.append(f"progress log lacks scan {scan:03d} {phase} record")
                else:
                    (first_done if phase=='done' else first_audited)[scan]=match.start()
            if scan in first_done and scan in first_audited and first_audited[scan]<first_done[scan]:
                errors.append(f"scan {scan:03d}: audited record precedes done record")
        for phase,positions in [('done',first_done),('audited',first_audited)]:
            ordered=[positions[s] for s in sorted(positions)]
            if ordered!=sorted(ordered):
                errors.append(f"first {phase} records are not in scan order")
        if first_audited and (len(first_done)<len(SCANS) or min(first_audited.values())<max(first_done.values())):
            errors.append("second-reading audit started before all first-pass done records")
        if freeze_marker and first_audited and freeze_marker.start()<max(first_audited.values()):
            errors.append("freeze marker precedes completion of recorded second-reading audits")
        report["counts"]["hash_records"] = len(hashes)
    report["status"] = "fail" if errors else "incomplete" if incomplete else "pass"
    return report


def render_text(report: dict) -> str:
    lines = [f"Mechanical validation: {report['status'].upper()}", json.dumps(report["counts"], ensure_ascii=False, indent=2)]
    for label in ("errors", "incomplete", "warnings"):
        lines.append(f"{label}: {len(report[label])}")
        lines.extend("  - " + message for message in report[label])
    lines.append("This report checks structure and recorded workflow only; it is not evidence of visual reading or mathematical verification.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json-report", type=Path)
    parser.add_argument("--text-report", type=Path)
    args = parser.parse_args()
    report = validate(args.out.resolve())
    rendered = render_text(report)
    print(rendered, end="")
    if args.json_report:
        args.json_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.text_report:
        args.text_report.write_text(rendered, encoding="utf-8")
    return {"pass": 0, "fail": 1, "incomplete": 2}[report["status"]]


if __name__ == "__main__":
    sys.exit(main())
