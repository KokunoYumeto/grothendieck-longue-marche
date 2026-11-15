#!/usr/bin/env python3
"""Mechanical checks only. Never interprets manuscript content.

Run after writing pages, inventory, and the concatenated transcription.
Use --partial for an unfinished package. A SHA-256 manifest may be supplied
with --manifest; otherwise conventional manifest names are detected.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

PREFIX = "MPL_93_002-046"
EXPECTED = [n for n in range(3, 47) if n not in (26, 35)]
HEADER = ["cote", "scan", "sheet_kind", "element", "kind", "position",
          "first_words_or_objects", "transcribed"]
CUSTOM = set("cotefile scanpage mspage deleted inserted margin uline uuline diagram figure unsure illegible".split())
# Standard LaTeX, common mathematical packages, and TikZ/tikz-cd commands.
# Unknown commands require human classification; --allow-standard records that
# classification without admitting an additional diplomatic custom macro.
STANDARD = set(r"""
begin end text textrm textit textbf textsf texttt textsc textnormal emph
mbox hbox vbox par noindent indent newline linebreak pagebreak newpage clearpage
boxed substack shortstack textup textsuperscript leqq geqq
smallskip medskip bigskip quad qquad enspace thinspace negthinspace hfill vfill
hspace vspace hphantom vphantom phantom smash raisebox rule strut mathstrut
relax protect leavevmode item label ref eqref pageref footnote footnotemark
footnotetext caption center centering raggedright raggedleft multicolumn multirow
hline cline vline arraystretch arraycolsep tabcolsep ensuremath nonumber notag tag
intertext shortintertext displaystyle textstyle scriptstyle scriptscriptstyle
mathrm mathit mathbf mathsf mathtt mathcal mathscr mathbb mathfrak mathnormal
boldsymbol bm boldmath unboldmath operatorname limits nolimits displaylimits
frac dfrac tfrac cfrac binom dbinom tbinom genfrac sqrt root of
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
bigm Bigm biggm Biggm over atop choose brace brack stackrel overset underset
overline underline widehat widetilde hat check breve acute grave tilde bar vec dot
ddot dddot ddddot mathring overbrace underbrace overrightarrow overleftarrow
overleftrightarrow underrightarrow underleftarrow underleftrightarrow
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon
phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
aleph beth gimel daleth hbar hslash imath jmath ell wp Re Im partial infty prime
backprime emptyset varnothing nabla surd top bot angle measuredangle sphericalangle
forall exists nexists neg lnot flat natural sharp clubsuit diamondsuit heartsuit
spadesuit complement eth Finv Game Bbbk mho digamma
sum prod coprod int iint iiint iiiint idotsint oint oiint oiiint smallint
bigcap bigcup bigsqcup bigvee bigwedge bigodot bigotimes bigoplus biguplus
cap cup sqcap sqcup vee wedge lor land uplus amalg setminus smallsetminus wr
times div cdot cdotp ast star circ bullet diamond triangleleft triangleright
bigtriangleup bigtriangledown triangle blacktriangle blacktriangledown
oplus ominus otimes oslash odot circledast circledcirc circleddash boxplus boxtimes
boxminus boxdot ltimes rtimes leftthreetimes rightthreetimes dotplus intercal
dagger ddagger pm mp oslash And
le leq leqslant ge geq geqslant neq ne equiv sim simeq approx approxeq asymp
cong propto doteq Doteq doteqdot eqcirc circeq triangleq bumpeq Bumpeq fallingdotseq
risingdotseq lesssim gtrsim lessapprox gtrapprox lessgtr gtrless lesseqgtr gtreqless
ll gg lll ggg prec succ preceq succeq preccurlyeq succcurlyeq precsim succsim
nprec nsucc npreceq nsucceq subset supset subseteq supseteq subsetneq supsetneq
subsetneqq supsetneqq subsetsim supsetsim nsubseteq nsupseteq sqsubset sqsupset
sqsubseteq sqsupseteq in ni notin owns not mid nmid parallel nparallel perp
vdash dashv models Vdash vDash Vvdash nvdash nVdash nvDash nVDash smile frown
bowtie Join between pitchfork nleq ngeq nleqslant ngeqslant nless ngtr nsim
ncong lvert rvert lVert rVert vert Vert | lbrace rbrace langle rangle lceil rceil
lfloor rfloor lmoustache rmoustache lgroup rgroup backslash slash
to gets mapsto longmapsto hookrightarrow hookleftarrow rightarrow leftarrow
leftrightarrow Rightarrow Leftarrow Leftrightarrow longrightarrow longleftarrow
longleftrightarrow Longrightarrow Longleftarrow Longleftrightarrow implies impliedby
iff uparrow downarrow updownarrow Uparrow Downarrow Updownarrow nearrow searrow
swarrow nwarrow rightleftarrows leftrightarrows rightleftharpoons leftrightharpoons
rightrightarrows leftleftarrows upuparrows downdownarrows twoheadrightarrow
twoheadleftarrow tailrightarrow tailleftarrow rightarrowtail leftarrowtail
looparrowright looparrowleft curvearrowright curvearrowleft circlearrowright
circlearrowleft rightsquigarrow leftrightsquigarrow leadsto multimap
rightharpoonup rightharpoondown leftharpoonup leftharpoondown upharpoonleft
upharpoonright downharpoonleft downharpoonright dashedrightarrow dashedleftarrow
dashrightarrow dashleftarrow xrightarrow xleftarrow xleftrightarrow
restriction nrightarrow nleftarrow nleftrightarrow nRightarrow nLeftarrow nLeftrightarrow
sin cos tan cot sec csc arcsin arccos arctan sinh cosh tanh coth log ln lg exp
lim limsup liminf varlimsup varliminf varinjlim varprojlim injlim projlim sup inf
max min det dim deg ker hom arg gcd Pr mod bmod pmod pod
ldots cdots vdots ddots dots dotsb dotsc dotsi dotsm dotso colon coloneqq eqqcolon
ldotp dcolon degree checkmark square Box blacksquare Diamond lozenge blacklozenge
S P copyright pounds aa AA ae AE oe OE o O ss l L i j
textbackslash textasciitilde textasciicircum textquotedblleft textquotedblright
textquoteleft textquoteright textendash textemdash textdegree textellipsis
guillemotleft guillemotright og fg LaTeX TeX
scriptsize tiny footnotesize small normalsize large Large LARGE huge Huge
rm it bf sf tt sc sl normalfont rmfamily sffamily ttfamily upshape itshape slshape
bfseries mdseries scshape selectfont fontsize
draw node path fill filldraw shade shadedraw clip coordinate matrix foreach
tikz tikzcd arrow ar pgfmathsetmacro pgfmathparse pgfmathresult pgfextra
pgfsetlinewidth pgfsetdash pgfpathmoveto pgfpathlineto pgfusepath
color textcolor colorbox fcolorbox rotatebox scalebox resizebox
""".split())
FORBIDDEN = set("documentclass usepackage newcommand renewcommand providecommand def gdef edef xdef newenvironment renewenvironment input include includegraphics".split())


def no_comments(s: str) -> str:
    """Drop unescaped comments, treating consecutive backslashes correctly."""
    out = []
    for line in s.splitlines(keepends=True):
        slash_run = 0
        for i, ch in enumerate(line):
            if ch == "%" and slash_run % 2 == 0:
                line = line[:i] + ("\n" if line.endswith("\n") else "")
                break
            slash_run = slash_run + 1 if ch == "\\" else 0
        out.append(line)
    return "".join(out)


def brace_error(s: str) -> str | None:
    depth, slash_run = 0, 0
    for i, ch in enumerate(s):
        if ch in "{}" and slash_run % 2 == 0:
            depth += 1 if ch == "{" else -1
            if depth < 0:
                return f"extra closing brace at character {i}"
        slash_run = slash_run + 1 if ch == "\\" else 0
    return f"{depth} unclosed brace(s)" if depth else None


def load_manifest(path: Path) -> dict[str, str]:
    if path.suffix == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        if "files" in payload:
            payload = payload["files"]
        if not isinstance(payload, dict):
            raise ValueError("JSON manifest must map relative filenames to SHA-256 values")
        return payload
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line)
        if not match:
            raise ValueError(f"invalid sha256sum manifest line: {line!r}")
        result[match[2]] = match[1]
    return result


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--partial", action="store_true")
    p.add_argument("--manifest", type=Path)
    p.add_argument("--allow-standard", action="append", default=[], metavar="COMMAND")
    args = p.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    expected_names = {f"{PREFIX}_93_scan{n:03d}.tex" for n in EXPECTED}
    files = sorted((root / "pages").glob("*.tex"))
    actual_names = {f.name for f in files}
    if actual_names - expected_names:
        errors.append(f"unexpected page files: {sorted(actual_names - expected_names)}")
    if not args.partial and expected_names - actual_names:
        errors.append(f"missing page files: {sorted(expected_names - actual_names)}")
    ordered = [root / "pages" / f"{PREFIX}_93_scan{n:03d}.tex"
               for n in EXPECTED if f"{PREFIX}_93_scan{n:03d}.tex" in actual_names]
    if not ordered:
        errors.append("no page files")
    present_scans = []
    allowed = STANDARD | CUSTOM | set(args.allow_standard)
    for f in ordered:
        n = int(re.search(r"scan(\d+)\.tex$", f.name)[1])
        present_scans.append(n)
        text = no_comments(f.read_text(encoding="utf-8"))
        markers = re.findall(r"\\scanpage\s*\{\s*(\d+)\s*\}", text)
        if [int(marker) for marker in markers] != [n]:
            errors.append(f"{f.name}: expected exactly \\scanpage{{{n}}}; found {markers}")
        cotes = re.findall(r"\\cotefile\s*\{\s*([^}]+)\s*\}", text)
        if cotes != (["93"] if n == EXPECTED[0] else []):
            errors.append(f"{f.name}: invalid cotefile markers {cotes}")
        if err := brace_error(text):
            errors.append(f"{f.name}: {err}")
        # Consume symbolic control sequences as well, especially \\\\: its
        # second backslash must not turn the following text into a command.
        tokens = list(re.finditer(r"\\([A-Za-z@]+|[^A-Za-z@])", text))
        commands = {m[1] for m in tokens if re.fullmatch(r"[A-Za-z@]+", m[1])}
        env_stack = []
        for match in tokens:
            command = match[1]
            following = text[match.end():].lstrip()
            line = text.count("\n", 0, match.start()) + 1
            if command in CUSTOM and not following.startswith("{"):
                errors.append(f"{f.name}:{line}: unbraced argument after \\{command}")
            if command in {"begin", "end"}:
                env = re.match(r"\{([^}]+)\}", following)
                if not env:
                    errors.append(f"{f.name}:{line}: missing environment name after \\{command}")
                elif command == "begin":
                    env_stack.append((env[1], line))
                elif not env_stack or env_stack[-1][0] != env[1]:
                    errors.append(f"{f.name}:{line}: mismatched end of {env[1]} environment")
                else:
                    env_stack.pop()
        for env, line in env_stack:
            errors.append(f"{f.name}:{line}: unclosed {env} environment")
        forbidden = commands & FORBIDDEN
        unknown = commands - allowed - FORBIDDEN
        if forbidden:
            errors.append(f"{f.name}: prohibited fragment commands {sorted(forbidden)}")
        if unknown:
            errors.append(f"{f.name}: unclassified commands {sorted(unknown)}; classify standard commands using --allow-standard")
    combined = root / f"{PREFIX}_transcription.tex"
    if combined.exists():
        if combined.read_bytes() != b"".join(f.read_bytes() for f in ordered):
            errors.append("combined transcription is not the exact byte concatenation of ordered page files")
    elif not args.partial:
        errors.append("combined transcription missing")
    inventory = root / f"{PREFIX}_inventory.csv"
    if inventory.exists():
        with inventory.open(newline="", encoding="utf-8-sig") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames != HEADER:
                errors.append(f"inventory header mismatch: {reader.fieldnames}")
            seen = set()
            row_count = 0
            for row_count, row in enumerate(reader, start=1):
                if row.get("transcribed") != "yes":
                    errors.append(f"inventory data row {row_count}: transcribed is not yes")
                try:
                    scan = int(row.get("scan", ""))
                    seen.add(scan)
                    if scan not in EXPECTED:
                        errors.append(f"inventory data row {row_count}: unexpected scan {scan}")
                except ValueError:
                    errors.append(f"inventory data row {row_count}: invalid scan")
                if row.get("cote") != "93":
                    errors.append(f"inventory data row {row_count}: cote is not 93")
                if row.get("sheet_kind") not in {"text", "typed", "reused_typed", "cancelled_draft", "cover"}:
                    errors.append(f"inventory data row {row_count}: invalid sheet_kind")
                if row.get("kind") not in {"text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}:
                    errors.append(f"inventory data row {row_count}: invalid element kind")
            missing = set(present_scans if args.partial else EXPECTED) - seen
            if missing:
                errors.append(f"inventory has no rows for scans {sorted(missing)}")
    elif not args.partial:
        errors.append("inventory missing")
    manifests = [args.manifest] if args.manifest else [root / name for name in
        ("frozen_sha256.json", "transcription_sha256.txt", "transcription.sha256", "SHA256SUMS")
        if (root / name).exists()]
    for manifest in manifests:
        try:
            entries = load_manifest(manifest)
            if not entries:
                errors.append(f"empty SHA-256 manifest: {manifest.name}")
            for filename, digest in entries.items():
                f = (root / filename).resolve()
                if not f.is_relative_to(root):
                    errors.append(f"manifest path outside work directory: {filename}")
                elif not re.fullmatch(r"[0-9a-fA-F]{64}", str(digest)):
                    errors.append(f"invalid SHA-256 in manifest for {filename}")
                elif not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest() != digest.lower():
                    errors.append(f"frozen SHA-256 mismatch or missing file: {filename}")
        except (OSError, ValueError, TypeError) as exc:
            errors.append(f"manifest {manifest}: {exc}")
    for error in errors:
        print("ERROR:", error)
    print(f"{'FAIL' if errors else 'PASS'}: {len(ordered)} page files; "
          f"{len(manifests)} SHA-256 manifest(s); partial={args.partial}; "
          "mechanical checks only, no claim of transcription completeness or accuracy")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
