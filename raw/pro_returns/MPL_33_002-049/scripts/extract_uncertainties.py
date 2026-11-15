#!/usr/bin/env python3
"""Extract uncertainty macros without changing or interpreting transcription.

Default: print counts only. With --write, update two mechanical TSV reports
under records/. Math-delimiter and macro-spelling findings are heuristic
review prompts, not assertions that the transcription is wrong.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import Counter
import csv
import difflib
import json
from pathlib import Path
import re

PREFIX = "MPL_33_002-049"
UNCERTAINTY_FIELDS = ["filename", "scan", "source_line", "macro", "content"]
FINDING_FIELDS = ["filename", "scan", "source_line", "kind", "detail"]
EDITORIAL = {
    "cotefile", "scanpage", "mspage", "deleted", "inserted", "margin",
    "uline", "uuline", "diagram", "figure", "unsure", "illegible",
}
# This is only a safeguard against flagging common commands as editorial typos.
# It is not a list of commands permitted in the transcription.
COMMON = set("""
begin end frac dfrac tfrac sqrt text textrm textit textbf textsf texttt
mathrm mathit mathbf mathsf mathtt mathcal mathscr mathfrak operatorname
underline overline underbrace overbrace widehat widetilde hat tilde bar vec
dot ddot acute grave breve check ring emph quad qquad enspace hspace vspace
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau upsilon phi
varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
arrow arrows ar node draw path fill coordinate foreach scope
to mapsto longmapsto rightarrow leftarrow leftrightarrow Rightarrow Leftarrow
Leftrightarrow longrightarrow longleftarrow longleftrightarrow Longrightarrow
Longleftarrow Longleftrightarrow hookrightarrow hookleftarrow twoheadrightarrow
twoheadleftarrow uparrow downarrow updownarrow Uparrow Downarrow Updownarrow
nearrow searrow nwarrow swarrow rightrightarrows leftleftarrows rightleftarrows
leftrightarrows rightsquigarrow leadsto xrightarrow xleftarrow overset underset
sim simeq cong approx equiv neq ne le leq ge geq ll gg subset supset subseteq
supseteq nsubseteq nsupseteq in notin ni owns cap cup bigcap bigcup sqcap sqcup
emptyset varnothing setminus smallsetminus land lor wedge vee neg lnot forall
exists nexists top bot vdash dashv models perp parallel mid nmid colon
times div cdot ast star circ bullet oplus otimes odot bigoplus bigotimes
sum prod coprod int iint iiint oint lim liminf limsup inf sup min max
ker coker hom Hom dim det rank codim deg gcd lcm log ln exp sin cos tan
arcsin arccos arctan sinh cosh tanh Pr Re Im arg span Tr tr
infty partial nabla ell hbar wp aleph beth gimel daleth imath jmath
ldots cdots vdots ddots dots ldotp cdotp prime backprime degree
lfloor rfloor lceil rceil langle rangle lvert rvert lVert rVert vert Vert
label ref eqref tag notag nonumber multicolumn multirow hline cline vline
small tiny scriptsize footnotesize normalsize large Large LARGE huge Huge
limits nolimits displaystyle textstyle scriptstyle scriptscriptstyle
intertext shortintertext boxed phantom hphantom vphantom smash strut mathstrut
prescript sideset substack genfrac binom dbinom tbinom pmod bmod mod
space newline linebreak noindent par smallskip medskip bigskip
boldsymbol bm ensuremath mathrel mathbin mathop mathord mathpunct mathopen mathclose
varinjlim varprojlim injlim projlim directlua verb Verb url href
""".split())


def mask_comments(text: str) -> str:
    """Replace comments by spaces while preserving offsets and line numbers."""
    out = list(text)
    i = 0
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text):
            i += 2
        elif text[i] == "%":
            end = text.find("\n", i)
            if end < 0:
                end = len(text)
            out[i:end] = " " * (end - i)
            i = end
        else:
            i += 1
    return "".join(out)


def closing_brace(text: str, start: int) -> int | None:
    """Locate a balanced argument's closing brace; text has comments masked."""
    depth = 1
    i = start + 1
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text):
            i += 2
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if not depth:
                return i
        i += 1
    return None


def extract_file(path: Path) -> tuple[list[dict], list[dict], Counter]:
    raw = path.read_text(encoding="utf-8")
    clean = mask_comments(raw)
    newlines = [i for i, char in enumerate(raw) if char == "\n"]
    match = re.search(r"_scan(\d+)\.tex$", path.name)
    scan = match.group(1) if match else ""
    occurrences = []
    findings = []
    commands = Counter()
    bracket_stack = []
    dollar_open = {"$": None, "$$": None}

    def base(position: int) -> dict:
        return {"filename": path.name, "scan": scan,
                "source_line": bisect_right(newlines, position) + 1}

    def finding(position: int, kind: str, detail: str) -> None:
        findings.append({**base(position), "kind": kind, "detail": detail})

    i = 0
    while i < len(clean):
        char = clean[i]
        if char == "\\" and i + 1 < len(clean):
            following = clean[i + 1]
            if following.isalpha() and following.isascii():
                match = re.match(r"[A-Za-z]+", clean[i + 1:])
                command = match.group(0)
                end_command = i + 1 + len(command)
                commands[command] += 1
                if command in {"unsure", "illegible"}:
                    start = end_command
                    while start < len(clean) and clean[start].isspace():
                        start += 1
                    if start == len(clean) or clean[start] != "{":
                        finding(i, "uncertainty_argument_missing", f"\\{command} is not followed by a braced argument")
                    else:
                        end = closing_brace(clean, start)
                        if end is None:
                            finding(i, "uncertainty_argument_unclosed", f"\\{command} argument has no balanced closing brace")
                        else:
                            occurrences.append({**base(i), "macro": "\\" + command,
                                                "content": raw[start + 1:end]})
                elif command not in EDITORIAL and command not in COMMON:
                    near = difflib.get_close_matches(command, EDITORIAL, n=2, cutoff=0.80)
                    if near:
                        finding(i, "editorial_macro_near_miss",
                                f"\\{command}; similar known macro(s): " + ", ".join("\\" + name for name in near))
                # Advance past the name only, so nested uncertainty macros are found too.
                i = end_command
                continue
            token = "\\" + following
            if token in {r"\(", r"\["}:
                bracket_stack.append((token, i))
            elif token in {r"\)", r"\]"}:
                expected = r"\(" if token == r"\)" else r"\["
                if bracket_stack and bracket_stack[-1][0] == expected:
                    bracket_stack.pop()
                else:
                    finding(i, "math_delimiter_unmatched_close", token)
            i += 2
            continue
        if char == "$":
            token = "$$" if clean.startswith("$$", i) else "$"
            if dollar_open[token] is None:
                dollar_open[token] = i
            else:
                dollar_open[token] = None
            i += len(token)
            continue
        i += 1
    for token, position in bracket_stack:
        finding(position, "math_delimiter_unmatched_open", token)
    for token, position in dollar_open.items():
        if position is not None:
            finding(position, "math_delimiter_unpaired_dollar", token)
    findings.sort(key=lambda row: row["source_line"])
    return occurrences, findings, commands


def write_tsv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, nargs="?", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true", help="Update mechanical reports under records/")
    args = parser.parse_args()
    root = args.root.resolve()
    pages = sorted((root / "pages").glob(f"{PREFIX}_33_scan[0-9][0-9][0-9].tex"))
    occurrences = []
    findings = []
    commands = Counter()
    for page in pages:
        local_occurrences, local_findings, local_commands = extract_file(page)
        occurrences.extend(local_occurrences)
        findings.extend(local_findings)
        commands.update(local_commands)
    paths = []
    if args.write:
        uncertainty_path = root / "records" / "uncertainty_occurrences.tsv"
        findings_path = root / "records" / "latex_mechanical_findings.tsv"
        write_tsv(uncertainty_path, occurrences, UNCERTAINTY_FIELDS)
        write_tsv(findings_path, findings, FINDING_FIELDS)
        paths = [str(uncertainty_path), str(findings_path)]
    summary = {
        "page_files_scanned": len(pages),
        "balanced_uncertainty_occurrences": len(occurrences),
        "by_macro": dict(sorted(Counter(row["macro"] for row in occurrences).items())),
        "files_with_uncertainty": len({row["filename"] for row in occurrences}),
        "mechanical_findings": len(findings),
        "findings_by_kind": dict(sorted(Counter(row["kind"] for row in findings).items())),
        "distinct_control_words": len(commands),
        "written_reports": paths,
        "scope": "Exact source extraction only; no interpretation, confidence rating, or transcription change. Math and spelling checks are heuristic review prompts. TSV fields use standard CSV quoting, including embedded newlines when present.",
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
