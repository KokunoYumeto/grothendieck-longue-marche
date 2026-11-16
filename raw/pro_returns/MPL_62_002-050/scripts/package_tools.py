#!/usr/bin/env python3
"""Mechanical checks and packaging only; this program performs no OCR.

It cannot assess a reading, mathematical correctness, or completeness against ink.
It reads transcription text only when the primary agent explicitly invokes it.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

PACKAGE = "MPL_62_002-050"
EXPECTED = (2, *range(4, 18), *range(19, 27), *range(28, 51))
EXPECTED_SET = set(EXPECTED)
COLUMNS = ["cote", "scan", "sheet_kind", "element", "kind", "position",
           "first_words_or_objects", "transcribed"]
SHEET_KINDS = {"text", "reused_typed", "cancelled_draft", "cover"}
KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
EDITORIAL = {"cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
             "uline", "uuline", "diagram", "figure", "unsure", "illegible"}
FORBIDDEN = {"documentclass", "usepackage", "RequirePackage", "newcommand",
             "renewcommand", "providecommand", "def", "gdef", "input", "include",
             "includegraphics", "graphicspath", "marginnote", "marginpar", "unclear",
             "unreadable", "unread", "strikeout", "sout", "cancel", "textcolor"}
# Unknown commands are reported for review, not silently certified as standard.
KNOWN = set("""begin end label tag notag nonumber ref eqref emph text textit textbf
textrm textsf texttt textnormal underline overline bar hat widehat tilde widetilde
vec dot ddot acute grave check breve mathrm mathit mathbf mathsf mathtt mathcal
mathfrak mathbb mathscr operatorname operatornamewithlimits limits nolimits
frac dfrac tfrac binom dbinom tbinom sqrt left right middle big Big bigg Bigg
bigl bigr Bigl Bigr biggl biggr Biggl Biggr bigm Bigm biggm Biggm phantom
hphantom vphantom smash overset underset stackrel substack xrightarrow
xleftarrow to mapsto longmapsto hookrightarrow hookleftarrow twoheadrightarrow
twoheadleftarrow rightarrow leftarrow leftrightarrow longrightarrow longleftarrow
longleftrightarrow Rightarrow Leftarrow Leftrightarrow Longrightarrow Longleftarrow
Longleftrightarrow nearrow searrow swarrow nwarrow uparrow downarrow Uparrow
Downarrow updownarrow rightrightarrows leftleftarrows rightleftarrows leftrightarrows
rightharpoonup rightharpoondown leftharpoonup leftharpoondown leadsto rightsquigarrow
rightarrowtail leftarrowtail emptyset varnothing in notin ni owns subset supset
subseteq supseteq subsetneq supsetneq nsubseteq nsupseteq cup cap bigcup bigcap
sqcup sqcap bigsqcup setminus smallsetminus times otimes oplus ominus odot
bigotimes bigoplus bigodot ast star circ bullet cdot cdots ldots vdots ddots
le leq ge geq neq ne equiv sim simeq cong approx asymp propto ll gg prec succ
preceq succeq models vdash dashv parallel perp mid nmid pm mp div sum prod
coprod int iint iiint oint infinity infty partial nabla forall exists nexists
neg not land lor wedge vee bigwedge bigvee top bot aleph hbar ell wp Re Im
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon phi
varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
prime backprime vert Vert lvert rvert lVert rVert langle rangle lbrace rbrace
lceil rceil lfloor rfloor backslash angle triangle triangleleft triangleright
trianglelefteq trianglerighteq square Box Diamond dots dotsb dotsc dotsm dotso
ker coker hom Hom dim det gcd lcm inf sup lim liminf limsup injlim projlim
min max log ln exp sin cos tan cot sec csc sinh cosh tanh arctan arccos arcsin
Pr mod bmod pmod pod i j imath jmath dag ddag dagger ddagger S P AA aa AE ae
OE oe O o L l ss quad qquad enspace thinspace medspace thickspace negthinspace
hspace vspace hfill vfill smallskip medskip bigskip par noindent indent newpage
pagebreak linebreak newline raggedright centering hline cline multicolumn
multirow cr span omit displaystyle textstyle scriptstyle scriptscriptstyle
displaystyle ensuremath textcircled raisebox rule strut fbox framebox makebox
mbox phantom hbox vbox kern mkern mathbin mathrel mathop mathord mathopen
mathclose mathpunct mathinner choose atop over atopwithdelims buildrel
arrow ar draw path node coordinate fill filldraw clip scope matrix foreach
pgfmathsetmacro tikzset tikzcdset usetikzlibrary usetikzcdlibrary
endgroup begingroup bgroup egroup small footnotesize scriptsize tiny large
Large LARGE huge Huge normalsize bfseries itshape rmfamily sfamily ttfamily
upshape mdseries normalfont textsuperscript textsubscript
varinjlim varprojlim boxed diagdown diagup hrulefill k u H v r t b c d
leqslant geqslant underbrace overbrace tikztonodes tikztostart tikztotarget
""".split()) | EDITORIAL
ENVIRONMENTS = {"equation", "equation*", "align", "align*", "aligned", "alignedat",
                "alignat", "alignat*", "gather", "gather*", "gathered", "multline",
                "multline*", "split", "array", "matrix", "pmatrix", "bmatrix",
                "Bmatrix", "vmatrix", "Vmatrix", "cases", "smallmatrix", "tikzcd",
                "tikzpicture", "scope", "tabular", "tabular*", "center", "flushleft",
                "flushright", "minipage", "picture"}
EXCLUDED_DIRS = {"__pycache__", ".git", ".pytest_cache", "cache", "caches", "crops",
                 "renders", "scans", "context", "upload", "tex_build", "node_modules"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".jpg", ".jpeg", ".png", ".tif", ".tiff",
                     ".webp", ".zip", ".aux", ".toc", ".out", ".synctex.gz"}
UTC_PATTERN = "%Y-%m-%d %H:%M:%S UTC"


def utc_now():
    return datetime.now(timezone.utc)


def page_name(scan):
    return f"{PACKAGE}_62_scan{scan:03d}.tex"


def strip_comments(text):
    # TeX control symbols consume the following character, including escaped %.
    output, i = [], 0
    while i < len(text):
        if text[i] == "\\":
            output.append(text[i:i + 2])
            i += 2
        elif text[i] == "%":
            end = text.find("\n", i)
            if end < 0:
                break
            output.append("\n")
            i = end + 1
        else:
            output.append(text[i])
            i += 1
    return "".join(output)


def braced_argument(text, offset):
    while offset < len(text) and text[offset].isspace():
        offset += 1
    if offset >= len(text) or text[offset] != "{":
        return None
    start, depth, i = offset + 1, 1, offset + 1
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start:i]
        i += 1
    return None


def tex_checks(text, path, errors, warnings):
    clean = strip_comments(text)
    depth, i = 0, 0
    while i < len(clean):
        if clean[i] == "\\":
            i += 2
            continue
        if clean[i] == "{":
            depth += 1
        elif clean[i] == "}":
            depth -= 1
            if depth < 0:
                errors.append(f"{path}: unmatched closing brace near character {i}")
                depth = 0
        i += 1
    if depth:
        errors.append(f"{path}: {depth} unclosed brace(s)")
    stack = []
    for m in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", clean):
        action, env = m.groups()
        if action == "begin":
            stack.append(env)
            if env not in ENVIRONMENTS:
                warnings.append(f"{path}: review environment {env!r}")
        elif not stack or stack[-1] != env:
            errors.append(f"{path}: mismatched end of {env!r}")
        else:
            stack.pop()
    if stack:
        errors.append(f"{path}: unclosed environment(s): {', '.join(stack)}")
    unknown = set()
    for m in re.finditer(r"\\([A-Za-z]+|[^A-Za-z])", clean):
        name = m.group(1)
        if not name[0].isalpha():
            continue
        if name in FORBIDDEN:
            errors.append(f"{path}: prohibited/non-fragment command \\{name}")
        elif name not in KNOWN:
            unknown.add(name)
        if name in EDITORIAL:
            arg = braced_argument(clean, m.end())
            if arg is None or not arg.strip():
                errors.append(f"{path}: \\{name} needs a nonempty braced argument")
            elif name == "illegible" and not re.fullmatch(r"[1-9][0-9]*", arg.strip()):
                errors.append(f"{path}: \\illegible count is not a positive integer")
            elif name == "diagram" and not re.search(r"\\begin\s*\{(?:tikzcd|array|tabular\*?)\}", arg):
                errors.append(f"{path}: \\diagram must contain tikzcd or an array/table")
            elif name == "figure" and not re.search(r"\\begin\s*\{tikzpicture\}", arg):
                errors.append(f"{path}: \\figure must contain a TikZ drawing")
    if unknown:
        warnings.append(f"{path}: review commands not in mechanical whitelist: " +
                        ", ".join("\\" + n for n in sorted(unknown)))
    # Flag illegible inside explicit display/inline delimiters or math environments.
    math_patterns = [r"\\\[(.*?)\\\]", r"\\\((.*?)\\\)", r"(?<!\\)\$(.*?)(?<!\\)\$",
                     r"\\begin\{(equation\*?|align\*?|aligned|gather\*?|array|tikzcd)\}(.*?)\\end\{\1\}"]
    for pattern in math_patterns:
        for match in re.finditer(pattern, clean, re.S):
            if "\\illegible" in match.group(0):
                errors.append(f"{path}: \\illegible inside mathematics/diagram; use \\unsure")
    if "\\begin{document}" in clean or "\\end{document}" in clean:
        errors.append(f"{path}: must be a fragment, not a document")


def load_log(root):
    path = root / "progress.log"
    return path.read_text(encoding="utf-8") if path.exists() else ""


def existing_pages(root):
    directory = root / "pages"
    return {s: directory / page_name(s) for s in EXPECTED if (directory / page_name(s)).is_file()}


def combined_bytes(pages):
    # Never normalize content; add only a separating newline where necessary.
    chunks = []
    for s in EXPECTED:
        if s in pages:
            data = pages[s].read_bytes()
            chunks.append(data if data.endswith(b"\n") else data + b"\n")
    return b"\n".join(chunks)


def parse_hash_records(log):
    records = {}
    for line in log.splitlines():
        m = re.fullmatch(r"sha256\s+(\S+)\s+([0-9a-f]{64})", line.strip(), re.I)
        if m:
            records[m.group(1)] = m.group(2).lower()
        else:
            m = re.fullmatch(r"([0-9a-f]{64})\s+\*?(\S+)", line.strip(), re.I)
            if m:
                records[m.group(2)] = m.group(1).lower()
    return records


def validate(root, stage="draft"):
    errors, warnings = [], []
    pages = existing_pages(root)
    complete = stage in {"complete", "frozen"}
    if complete and set(pages) != EXPECTED_SET:
        errors.append("Missing scan page(s): " + ", ".join(f"{s:03d}" for s in EXPECTED if s not in pages))
    for p in (root / "pages").glob("*") if (root / "pages").exists() else []:
        if p.is_file() and p.name not in {page_name(s) for s in EXPECTED}:
            errors.append(f"Unexpected file in pages/: {p.name}")
    for scan, path in pages.items():
        t = path.read_text(encoding="utf-8")
        clean = strip_comments(t)
        tags = re.findall(r"\\scanpage\s*\{\s*([0-9]+)\s*\}", clean)
        if len(tags) != 1 or int(tags[0]) != scan:
            errors.append(f"{path.name}: exactly one matching \\scanpage is required")
        if scan == 2:
            if not re.match(r"\s*\\cotefile\{62\}\s*\\scanpage\{0*2\}", clean):
                errors.append(f"{path.name}: first page must start with \\cotefile{{62}} then \\scanpage{{2}}")
        elif not re.match(r"\s*\\scanpage\{0*" + str(scan) + r"\}", clean):
            errors.append(f"{path.name}: page must start with its \\scanpage marker")
        tex_checks(t, path.name, errors, warnings)
    inventory = root / f"{PACKAGE}_inventory.csv"
    row_count, covered, elements = 0, set(), set()
    if not inventory.exists():
        errors.append("Inventory is missing")
    else:
        with inventory.open(newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != COLUMNS:
                errors.append(f"Inventory columns must be exactly {COLUMNS!r}")
            for number, row in enumerate(reader, 2):
                row_count += 1
                if set(row) != set(COLUMNS):
                    errors.append(f"Inventory row {number}: malformed CSV row")
                    continue
                try:
                    scan = int(row["scan"])
                except (ValueError, TypeError):
                    errors.append(f"Inventory row {number}: invalid scan")
                    continue
                if scan not in EXPECTED_SET or row["cote"] != "62":
                    errors.append(f"Inventory row {number}: unexpected cote/scan")
                if row["sheet_kind"] not in SHEET_KINDS:
                    errors.append(f"Inventory row {number}: invalid sheet_kind")
                if row["kind"] not in KINDS:
                    errors.append(f"Inventory row {number}: invalid kind")
                if row["transcribed"] != "yes":
                    (errors if complete or scan in pages else warnings).append(
                        f"Inventory row {number}: transcribed is not yes")
                if any(not (row.get(c) or "").strip() for c in COLUMNS):
                    errors.append(f"Inventory row {number}: empty field")
                key = (scan, row["element"])
                if key in elements:
                    errors.append(f"Inventory row {number}: repeated element id for scan {scan:03d}")
                elements.add(key)
                covered.add(scan)
        for scan in pages:
            if scan not in covered:
                errors.append(f"Scan {scan:03d}: no inventory rows")
    log = load_log(root)
    if not log:
        errors.append("progress.log is missing or empty")
    else:
        try:
            datetime.strptime(log.splitlines()[0].strip(), UTC_PATTERN)
        except ValueError:
            errors.append("progress.log first line is not a UTC timestamp")
    done = {int(s) for s in re.findall(r"^62 scan (\d+) done .+$", log, re.M)}
    audited = {int(s) for s in re.findall(r"^scan (\d+) audited .+$", log, re.M)}
    for scan in pages:
        if scan not in done:
            errors.append(f"Scan {scan:03d}: missing done entry")
    if complete:
        for scan in EXPECTED:
            if scan not in audited:
                errors.append(f"Scan {scan:03d}: missing audit entry")
        for suffix in ["transcription.tex", "doubts.md", "notes.md"]:
            p = root / f"{PACKAGE}_{suffix}"
            if not p.is_file() or not p.stat().st_size:
                errors.append(f"Required complete deliverable missing/empty: {p.name}")
    combined = root / f"{PACKAGE}_transcription.tex"
    if combined.exists() and combined.read_bytes() != combined_bytes(pages):
        errors.append("Combined transcription differs from page-file assembly")
    if stage == "frozen":
        if not re.search(r"^transcription frozen .+$", log, re.M):
            errors.append("Missing transcription frozen entry")
        if "context opened " in log and "transcription frozen " in log and log.index("context opened ") < log.index("transcription frozen "):
            errors.append("Context was opened before freeze entry")
        hashes = parse_hash_records(log)
        targets = list(pages.values()) + ([combined] if combined.exists() else [])
        for p in targets:
            rel = p.relative_to(root).as_posix()
            expected = hashes.get(rel, hashes.get(p.name))
            if expected is None:
                errors.append(f"No frozen SHA-256 for {rel}")
            elif expected != hashlib.sha256(p.read_bytes()).hexdigest():
                errors.append(f"Frozen SHA-256 mismatch: {rel}")
    return {"stage": stage, "expected_pages": len(EXPECTED), "page_files": len(pages),
            "inventory_rows": row_count, "done_entries": len(done), "audit_entries": len(audited),
            "errors": errors, "warnings": warnings,
            "limits": "Mechanical checks do not certify readings or completeness against the images."}


def print_result(result):
    print(json.dumps(result, ensure_ascii=False, indent=2))


def assemble(root, partial=False):
    pages = existing_pages(root)
    if not partial and set(pages) != EXPECTED_SET:
        raise ValueError("Cannot assemble complete transcription until every page exists; use --partial for a working compilation")
    out = root / f"{PACKAGE}_transcription.tex"
    data = combined_bytes(pages)
    if "transcription frozen " in load_log(root) and (not out.exists() or out.read_bytes() != data):
        raise ValueError("Frozen transcription would change; assembly refused")
    out.write_bytes(data)
    return {"output": str(out), "pages": len(pages), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def make_zip(root, output, mode):
    output = output.resolve()
    if output.exists():
        raise ValueError("Output already exists; no ZIP is overwritten")
    if mode == "final":
        if output.name != f"{PACKAGE}.zip":
            raise ValueError("Final ZIP filename must be " + PACKAGE + ".zip")
        check = validate(root, "frozen")
        if check["errors"]:
            raise ValueError("Final validation failed:\n" + "\n".join(check["errors"]))
    else:
        m = re.fullmatch(re.escape(PACKAGE) + r"_checkpoint_(\d{2})\.zip", output.name)
        if not m:
            raise ValueError("Checkpoint ZIP filename must be " + PACKAGE + "_checkpoint_NN.zip")
        old = sorted(output.parent.glob(f"{PACKAGE}_checkpoint_??.zip"))
        numbers = [int(p.stem[-2:]) for p in old]
        if int(m.group(1)) != max(numbers, default=0) + 1:
            raise ValueError("Checkpoint number must be the next unused number")
        first = load_log(root).splitlines()[0]
        started = datetime.strptime(first.strip(), UTC_PATTERN).replace(tzinfo=timezone.utc)
        latest = max([started.timestamp()] + [p.stat().st_mtime for p in old])
        if utc_now().timestamp() - latest < 3600:
            raise ValueError("Checkpoint guard: less than one hour since start/previous checkpoint")
    output.parent.mkdir(parents=True, exist_ok=True)
    included, excluded = [], []
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted(root.rglob("*")):
            if not p.is_file() or p.is_symlink():
                continue
            rel = p.relative_to(root)
            if any(part in EXCLUDED_DIRS or part.endswith("_scans") or part.endswith("_context") for part in rel.parts):
                excluded.append(rel.as_posix())
                continue
            if p.suffix.lower() in EXCLUDED_SUFFIXES or p.name.endswith(".synctex.gz"):
                excluded.append(rel.as_posix())
                continue
            z.write(p, rel.as_posix())
            included.append(rel.as_posix())
    return {"output": str(output), "mode": mode, "files": len(included),
            "bytes": output.stat().st_size,
            "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
            "excluded": excluded}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("validate", help="Print mechanical validation JSON; make no changes")
    p.add_argument("--stage", choices=["draft", "complete", "frozen"], default="draft")
    p = sub.add_parser("assemble", help="Assemble the combined file without modifying pages")
    p.add_argument("--partial", action="store_true")
    sub.add_parser("hashes", help="Print log-ready SHA-256 records; do not write the log")
    p = sub.add_parser("zip", help="Create a new ZIP; never overwrite; no uploading")
    p.add_argument("--mode", choices=["checkpoint", "final"], required=True)
    p.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "validate":
            result = validate(root, args.stage)
            print_result(result)
            return int(bool(result["errors"]))
        if args.command == "assemble":
            print_result(assemble(root, args.partial))
        elif args.command == "hashes":
            paths = [root / "pages" / page_name(s) for s in EXPECTED]
            paths.append(root / f"{PACKAGE}_transcription.tex")
            missing = [str(p) for p in paths if not p.is_file()]
            if missing:
                raise ValueError("Cannot freeze incomplete transcription: " + ", ".join(missing))
            for p in paths:
                print("sha256", p.relative_to(root).as_posix(), hashlib.sha256(p.read_bytes()).hexdigest())
        elif args.command == "zip":
            print_result(make_zip(root, args.output, args.mode))
    except (ValueError, OSError, UnicodeError, csv.Error, zipfile.BadZipFile) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
