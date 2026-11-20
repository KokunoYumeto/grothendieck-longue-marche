#!/usr/bin/env python3
"""Structural validation of the SP66 C13 diplomatic-transcription package.

This script never reads scan pixels, performs OCR, or evaluates manuscript
readings.  Source witnesses are used only for filenames, mark identifiers and
the permitted preamble definitions.  It does not invoke a TeX compiler.

Example:
  python scripts/validate_package.py --root . --source ../source
  python scripts/validate_package.py --root . --source ../source \
      --archive ../SP66_C13_16+120+136.zip

--partial is useful while pages are still being completed. Missing deliverables
are then warnings; malformed data or inconsistent completed files remain errors.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path

PREFIX = "SP66_C13_16+120+136"
DECISION_FIELDS = ["id", "cote", "scan", "decision", "reading", "what the ink shows", "crop", "confidence"]
COLLATION_FIELDS = ["folder", "their_page", "our_scan", "line", "their_reading", "codex_reading", "final_reading", "scan_shows", "kind", "marked_in_H", "confidence"]
INVENTORY_FIELDS = ["scan", "sheet_kind", "hand", "element", "kind", "position", "first_words_or_objects", "transcribed"]
DECISIONS = {"first", "alternative", "other", "undecided"}
CONFIDENCES = {"high", "medium", "low"}
KINDS = {
    "misread word", "misread symbol or index", "omission", "text not on the page",
    "deletion state (struck given live or live given struck)",
    "insertion or placement", "abbreviation expanded or spelling modernised",
    r"readable ink left as \ill{}", "drawing or diagram", "other",
}
# The short form is also explicitly used in the task's description of this kind.
KINDS.add("deletion state")
SHEET_KINDS = {"text", "reused_typed", "typescript", "letter", "list", "cancelled_draft", "cover"}
ELEMENT_KINDS = {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".tif", ".tiff", ".bmp", ".svg", ".avif", ".heic", ".ico"}

# A conservative vocabulary of ordinary LaTeX plus the supplied packages.
# Unknown commands are warnings by default and errors with --strict-macros.
STANDARD_COMMANDS = set("""
begin end par medskip smallskip bigskip noindent indent newpage clearpage pagebreak
nopagebreak linebreak nolinebreak newline vspace hspace vfill hfill quad qquad
enspace thinspace negthinspace text textnormal textrm textsf texttt textit textsl
textbf textsc textup emph mbox hbox fbox framebox makebox raisebox rule phantom
hphantom vphantom smash strut footnote footnotemark footnotetext marginpar
footnotesize scriptsize tiny small normalsize large Large LARGE huge Huge
textsuperscript textsuperscript textsubscript textcircled centering raggedright
raggedleft section subsection subsubsection paragraph subparagraph item label
ref pageref eqref url href caption title author date maketitle today
mathrm mathsf mathit mathtt mathbf mathcal mathbb mathfrak mathscr mathnormal
boldsymbol pmb bm operatorname operatornamewithlimits mathop mathbin mathrel
mathord mathopen mathclose mathpunct mathinner ensuremath displaystyle textstyle
scriptstyle scriptscriptstyle limits nolimits displaylimits
frac dfrac tfrac cfrac binom dbinom tbinom sqrt over under choose atop brace
brack overset underset stackrel substack sideset genfrac mod bmod pmod pod
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
bigm Bigm biggm Biggm vert Vert lvert rvert lVert rVert langle rangle lceil
rceil lfloor rfloor lbrace rbrace lbrack rbrack backslash setminus smallsetminus
aa AA ae AE oe OE o O ss l L S P dag ddag pounds copyright textbackslash
c d b H k r t u v
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon
phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi
Omega digamma
infty partial nabla ell hbar imath jmath wp Re Im aleph beth gimel daleth
emptyset varnothing complement angle measuredangle sphericalangle triangle
square Box Diamond lozenge blacksquare blacklozenge top bot perp parallel
nparallel shortparallel mid nmid not neg lnot forall exists nexists therefore because
in ni notin owns subset supset subseteq supseteq nsubseteq nsupseteq subsetneq
supsetneq subsetneqq supsetneqq sqsubset sqsupset sqsubseteq sqsupseteq
le leq ge geq neq ne lt gt ll gg leqq geqq leqslant geqslant lesssim gtrsim
lessapprox gtrapprox lneq gneq lneqq gneqq nleq ngeq prec succ preceq succeq
precsim succsim sim simeq approx approxeq asymp cong equiv propto doteq doteqdot
triangleq circeq bumpeq Bumpeq models vdash dashv Vdash vDash VDdash
times otimes oplus ominus odot oslash circ bullet cdot ast star diamond
bigcirc boxplus boxminus boxtimes boxdot cup cap uplus sqcup sqcap vee wedge
lor land amalg wr ltims rtimes ltimes div pm mp dotplus circledast circledcirc
circleddash intercal dagger ddagger
sum prod coprod int iint iiint iiiint oint oiint smallint intop
bigcup bigcap bigvee bigwedge bigsqcup biguplus bigodot bigoplus bigotimes
to gets mapsto mapstochar relbar longmapsto rightarrow leftarrow leftrightarrow longrightarrow
longleftarrow longleftrightarrow Rightarrow Leftarrow Leftrightarrow
Longrightarrow Longleftarrow Longleftrightarrow implies impliedby iff
joinrel lhook hookrightarrow hookleftarrow twoheadrightarrow twoheadleftarrow
rightarrowtail leftarrowtail rightsquigarrow leftrightsquigarrow
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow nearrow searrow
nwarrow swarrow xrightarrow xleftarrow overrightarrow overleftarrow
overleftrightarrow underleftarrow underrightarrow
rightleftarrows leftrightarrows rightrightarrows leftleftarrows
rightharpoonup rightharpoondown leftharpoonup leftharpoondown rightleftharpoons
leftrightharpoons leadsto looparrowright looparrowleft curvearrowright
curvearrowleft circlearrowright circlearrowleft multimap
hat widehat tilde widetilde bar overline underline vec dot ddot dddot ddddot
acute grave breve check ring mathring overbrace underbrace overbracket
underbracket cancel bcancel xcancel
prime backprime degree ldots cdots vdots ddots dots dotsc dotsb dotsm dotsi
dotso colon coloneqq eqqcolon
sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh coth exp log ln
lg lim limsup liminf sup inf max min det dim ker hom gcd Pr arg deg
injlim projlim varinjlim varprojlim varlimsup varliminf
color textcolor colorbox fcolorbox definecolor rotatebox
uline uuline sout xout uwave dashuline dotuline normalem ULon
diagram figure arrow ar node draw path fill filldraw clip coordinate
foreach scope endscope matrix graph tikz tikzset pgfsetarrows pgfmathsetmacro
pgfmathtruncatemacro pgfmathparse pgfmathresult pgfsetlinewidth
usetikzlibrary usepgflibrary pgfdeclarelayer pgfsetlayers
""".split())


class Validator:
    def __init__(self, partial: bool = False, strict_macros: bool = False):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.partial = partial
        self.strict_macros = strict_macros

    def error(self, message: str):
        self.errors.append(message)

    def warn(self, message: str):
        self.warnings.append(message)

    def missing(self, message: str):
        (self.warn if self.partial else self.error)(message)

    def table(self, path: Path, fields: list[str], delimiter: str) -> list[dict[str, str]]:
        if not path.is_file():
            return []
        try:
            with path.open(encoding="utf-8-sig", newline="") as stream:
                reader = csv.DictReader(stream, delimiter=delimiter)
                if reader.fieldnames != fields:
                    self.error(f"{path.name}: headers {reader.fieldnames!r}; expected {fields!r}")
                rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as exc:
            self.error(f"{path.name}: cannot read table: {exc}")
            return []
        for line, row in enumerate(rows, 2):
            if None in row or any(value is None for value in row.values()):
                self.error(f"{path.name}:{line}: wrong number of columns")
        return rows

    def allowed(self, path: str, rows: list[dict[str, str]], field: str, values: set[str]):
        for line, row in enumerate(rows, 2):
            if row.get(field) not in values:
                self.error(f"{path}:{line}: invalid {field}={row.get(field)!r}")


def without_comments(text: str) -> str:
    """Strip TeX comments while retaining escaped percent signs and line counts."""
    result = []
    for line in text.splitlines(keepends=True):
        for i, char in enumerate(line):
            if char == "%":
                backslashes = len(line[:i]) - len(line[:i].rstrip("\\"))
                if backslashes % 2 == 0:
                    line = line[:i] + ("\n" if line.endswith("\n") else "")
                    break
        result.append(line)
    return "".join(result)


def check_tex(v: Validator, path: Path, permitted: set[str]):
    text = without_comments(path.read_text(encoding="utf-8"))
    stack: list[int] = []
    for i, char in enumerate(text):
        if char not in "{}":
            continue
        backslashes = len(text[:i]) - len(text[:i].rstrip("\\"))
        if backslashes % 2:
            continue
        line = text.count("\n", 0, i) + 1
        if char == "{":
            stack.append(line)
        elif not stack:
            v.error(f"{path.name}:{line}: unmatched closing brace")
        else:
            stack.pop()
    if stack:
        v.error(f"{path.name}: unclosed braces originating on lines {stack}")
    environments: list[tuple[str, int]] = []
    for match in re.finditer(r"\\(begin|end)\s*\{([^{}]+)\}", text):
        line = text.count("\n", 0, match.start()) + 1
        op, env = match.groups()
        if op == "begin":
            environments.append((env, line))
        elif not environments or environments[-1][0] != env:
            v.error(f"{path.name}:{line}: mismatched end of {env}")
        else:
            environments.pop()
    if environments:
        v.error(f"{path.name}: unclosed environments {environments}")
    unknown = sorted(set(re.findall(r"\\([A-Za-z]+)", text)) - permitted)
    if unknown:
        (v.error if v.strict_macros else v.warn)(
            f"{path.name}: commands outside validator's basic vocabulary: "
            + ", ".join("\\" + x for x in unknown)
        )
    forbidden = set(re.findall(r"\\(documentclass|usepackage|newcommand|renewcommand|def|input|include)\b", text))
    if forbidden:
        v.error(f"{path.name}: fragment contains preamble/definition/input commands: {sorted(forbidden)}")


def page_order(source: Path, input_zip: Path | None) -> list[str]:
    if input_zip is None:
        candidate = source.parent / "upload" / (PREFIX + ".zip")
        input_zip = candidate if candidate.is_file() else None
    if input_zip is not None:
        with zipfile.ZipFile(input_zip) as archive:
            return [Path(n).name for n in archive.namelist()
                    if f"{PREFIX}_texts/pages/" in n and n.endswith(".tex")]
    # The archive's specified order is numeric cote, then numeric scan.
    texts = source / (PREFIX + "_texts")
    return [p.name for p in sorted((texts / "pages").glob("*.tex"),
            key=lambda p: tuple(map(int, re.fullmatch(r"(\d+)_scan(\d+)\.tex", p.name).groups())))]


def check_frozen_hashes(v: Validator, root: Path, names: list[str]):
    log = root / "progress.log"
    if not log.is_file():
        return
    text = log.read_text(encoding="utf-8")
    frozen = "transcription frozen" in text
    digests: dict[str, str] = {}
    for line in text.splitlines():
        match = re.search(r"(?<![0-9a-f])([0-9a-f]{64})(?![0-9a-f])", line, re.I)
        if match:
            for name in names:
                if name in line:
                    digests[name] = match.group(1).lower()
    if frozen:
        for name in names:
            if name not in digests:
                v.error(f"progress.log: frozen transcription has no SHA-256 for {name}")
    elif not v.partial:
        v.error("progress.log: no 'transcription frozen' entry")
    for name, digest in digests.items():
        path = root / name
        if path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            v.error(f"{name}: SHA-256 no longer matches progress.log")
    if frozen and not re.search(r"hash(?:es)?.*(?:unchanged|verified|match)|(?:unchanged|verified|match).*hash", text, re.I):
        v.warn("progress.log: could not identify the final hash-unchanged statement")


def check_archive(v: Validator, archive: Path, root: Path, required: list[str]):
    with zipfile.ZipFile(archive) as z:
        files = [info for info in z.infolist() if not info.is_dir()]
        names = [info.filename for info in files]
        duplicate = [name for name, count in Counter(names).items() if count > 1]
        if duplicate:
            v.error(f"archive: duplicate members {duplicate}")
        # Accept either a flat archive or one encompassing top-level directory.
        prefix = ""
        if "progress.log" not in names:
            candidates = [n[:-len("progress.log")] for n in names if n.endswith("/progress.log")]
            if len(candidates) == 1:
                prefix = candidates[0]
        normalized = {n[len(prefix):] if n.startswith(prefix) else n: n for n in names}
        for name in names:
            p = Path(name)
            if p.is_absolute() or ".." in p.parts:
                v.error(f"archive: unsafe member path {name}")
            if p.suffix.lower() in IMAGE_SUFFIXES:
                v.error(f"archive: image present: {name}")
            if p.suffix.lower() == ".zip":
                v.error(f"archive: nested ZIP present: {name}")
            if "_scans/" in name or "_texts/" in name or p.name in {"MARKS.tsv", "PREAMBLE.tex"}:
                v.error(f"archive: attached source material present: {name}")
        for name in required:
            if name not in normalized:
                v.error(f"archive: missing required member {name}")
        for relative, member in normalized.items():
            local = root / relative
            if local.is_file() and z.read(member) != local.read_bytes():
                v.error(f"archive: {relative} differs from current deliverable")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, required=True, help="Deliverables directory")
    parser.add_argument("--source", type=Path, required=True, help="Directory containing the extracted *_texts folder")
    parser.add_argument("--input-zip", type=Path, help="Original ZIP, to obtain its authoritative page order")
    parser.add_argument("--archive", type=Path, help="Completed deliverable ZIP to check as well")
    parser.add_argument("--partial", action="store_true", help="Permit incomplete work, with warnings")
    parser.add_argument("--strict-macros", action="store_true", help="Treat unknown macro vocabulary as errors")
    args = parser.parse_args()
    root, source = args.root.resolve(), args.source.resolve()
    v = Validator(args.partial, args.strict_macros)
    texts = source / (PREFIX + "_texts")
    try:
        pages = page_order(source, args.input_zip)
        with (texts / "MARKS.tsv").open(encoding="utf-8-sig", newline="") as stream:
            marks = [(r["id"], r["cote"], r["scan"]) for r in csv.DictReader(stream, delimiter="\t")]
        preamble = without_comments((texts / "PREAMBLE.tex").read_text(encoding="utf-8"))
    except (OSError, KeyError, ValueError, zipfile.BadZipFile) as exc:
        print(f"ERROR: unable to load source metadata: {exc}", file=sys.stderr)
        return 2
    if len(pages) != 25 or len(set(pages)) != 25:
        v.error(f"source metadata: expected 25 distinct pages, found {len(pages)}")
    required = [
        PREFIX + "_transcription.tex", PREFIX + "_changes.md", PREFIX + "_collation.tsv",
        "decisions.tsv", PREFIX + "_doubts.md", PREFIX + "_inventory.csv",
        PREFIX + "_notes.md", "CHECK_EVENTS.tsv", "progress.log",
        PREFIX + "_sheet_feedback.md", PREFIX + "_hand_log.md",
    ] + ["pages/" + name for name in pages]
    for name in required:
        if not (root / name).is_file():
            v.missing("missing file: " + name)
    actual = {p.name for p in (root / "pages").glob("*.tex")}
    for name in sorted(actual - set(pages)):
        v.error("unexpected page file: " + name)
    decisions = v.table(root / "decisions.tsv", DECISION_FIELDS, "\t")
    wanted = [x[0] for x in marks]
    got = [r.get("id") for r in decisions]
    if got != wanted:
        if args.partial and got == wanted[:len(got)]:
            v.warn(f"decisions.tsv: {len(got)} of {len(wanted)} marks completed")
        else:
            v.error("decisions.tsv: mark IDs are not exactly in MARKS.tsv order; "
                    f"missing={sorted(set(wanted) - set(got))}; "
                    f"extra={sorted(str(x) for x in set(got) - set(wanted))}; "
                    f"duplicates={[x for x, n in Counter(got).items() if n > 1]}")
    metadata = {mid: (cote, scan) for mid, cote, scan in marks}
    for line, row in enumerate(decisions, 2):
        if row.get("id") in metadata:
            expect = metadata[row["id"]]
            try:
                actual_meta = (str(int(row.get("cote", ""))), str(int(row.get("scan", ""))))
            except (ValueError, TypeError):
                actual_meta = None
            if actual_meta != expect:
                v.error(f"decisions.tsv:{line}: cote/scan does not match mark metadata {expect}")
        for field in ["reading", "what the ink shows", "crop"]:
            if not row.get(field, "").strip():
                v.error(f"decisions.tsv:{line}: empty {field}")
    v.allowed("decisions.tsv", decisions, "decision", DECISIONS)
    v.allowed("decisions.tsv", decisions, "confidence", CONFIDENCES)
    collation = v.table(root / (PREFIX + "_collation.tsv"), COLLATION_FIELDS, "\t")
    v.allowed(PREFIX + "_collation.tsv", collation, "kind", KINDS)
    v.allowed(PREFIX + "_collation.tsv", collation, "confidence", CONFIDENCES)
    for line, row in enumerate(collation, 2):
        try:
            if int(row.get("their_page", "")) + 1 != int(row.get("our_scan", "")):
                v.error(f"collation.tsv:{line}: their_page + 1 is not our_scan")
            if int(row.get("folder", "")) == 120 and int(row.get("our_scan", "")) == 2:
                v.error(f"collation.tsv:{line}: H has no text for cote 120 scan 002")
        except (ValueError, TypeError):
            v.error(f"collation.tsv:{line}: folder/their_page/our_scan must be numeric")
    inventory = v.table(root / (PREFIX + "_inventory.csv"), INVENTORY_FIELDS, ",")
    v.allowed("inventory.csv", inventory, "sheet_kind", SHEET_KINDS)
    v.allowed("inventory.csv", inventory, "kind", ELEMENT_KINDS)
    v.allowed("inventory.csv", inventory, "transcribed", {"yes"})
    permitted = STANDARD_COMMANDS | set(re.findall(r"\\(?:newcommand|renewcommand)\s*\{\\([A-Za-z]+)\}", preamble))
    for name in pages:
        path = root / "pages" / name
        if path.is_file():
            check_tex(v, path, permitted)
    combined = root / (PREFIX + "_transcription.tex")
    if combined.is_file():
        check_tex(v, combined, permitted)
        completed = [root / "pages" / name for name in pages if (root / "pages" / name).is_file()]
        whole = combined.read_text(encoding="utf-8").strip()
        # Inter-page blank lines may vary; the contents of each page must be exact.
        cursor = 0
        for page in completed:
            content = page.read_text(encoding="utf-8").strip()
            while cursor < len(whole) and whole[cursor].isspace():
                cursor += 1
            if not whole.startswith(content, cursor):
                v.error(f"combined transcription does not match page {page.name} at offset {cursor}")
                break
            cursor += len(content)
        else:
            if whole[cursor:].strip():
                v.error("combined transcription contains extra content after the completed pages")
    check_frozen_hashes(v, root, ["pages/" + name for name in pages] + [PREFIX + "_transcription.tex"])
    if args.archive:
        if not args.archive.is_file():
            v.error("requested archive does not exist: " + str(args.archive))
        else:
            try:
                check_archive(v, args.archive, root, required)
            except (OSError, zipfile.BadZipFile) as exc:
                v.error(f"cannot inspect completed archive: {exc}")
    for warning in v.warnings:
        print("WARNING:", warning)
    for error in v.errors:
        print("ERROR:", error)
    print(f"Structural validation: {len(v.errors)} errors, {len(v.warnings)} warnings; "
          f"{len(actual)}/{len(pages)} pages, {len(decisions)}/{len(marks)} decisions, "
          f"{len(collation)} collation rows, {len(inventory)} inventory rows.")
    print("This is a structural check only; it does not certify any manuscript reading.")
    return 1 if v.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
