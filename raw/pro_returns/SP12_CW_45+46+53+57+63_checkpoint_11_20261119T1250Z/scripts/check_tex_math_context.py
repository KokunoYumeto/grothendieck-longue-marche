#!/usr/bin/env python3
"""Report conservative math-context risks in committed editorial arguments.

This is a static source check, not TeX expansion, compilation, or transcription
review. It reads only named output pages, output helper code, and filename-map
metadata. It never follows the original paths named by that metadata.
"""
from __future__ import annotations

import argparse
import ast
import bisect
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re


TARGETS = {"unsure", "deleted"}
MATH_ENVIRONMENTS = {
    "math", "displaymath", "equation", "equation*", "align", "align*",
    "alignat", "alignat*", "flalign", "flalign*", "gather", "gather*",
    "multline", "multline*", "eqnarray", "eqnarray*",
}
TEXT_ENVIRONMENTS = {
    "center", "flushleft", "flushright", "minipage", "picture",
}
CONDITIONALS = set("""
if ifcat ifnum ifdim ifodd ifvmode ifhmode ifmmode ifinner ifvoid ifhbox ifvbox
ifx ifeof iftrue iffalse ifcase ifdefined ifcsname iffontchar
""".split())
MATH_REQUIRED_ENVIRONMENTS = {
    "array", "matrix", "pmatrix", "bmatrix", "Bmatrix", "vmatrix", "Vmatrix",
    "smallmatrix", "cases", "aligned", "alignedat", "gathered", "split",
}
INHERITED_WRAPPERS = {
    "handwritten", "inserted", "underline", "phantom", "vphantom", "hphantom",
    "smash", "color", "textcolor",
}
MATH_ONLY = set("""
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
varkappa lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi
varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
frac dfrac tfrac cfrac sqrt sum prod coprod int iint iiint oint lim limsup liminf
sin cos tan cot sec csc sinh cosh tanh log ln exp max min sup inf det dim gcd
to gets mapsto longmapsto rightarrow leftarrow leftrightarrow Rightarrow
Leftarrow Leftrightarrow longrightarrow longleftarrow longleftrightarrow
Longrightarrow Longleftarrow Longleftrightarrow hookrightarrow hookleftarrow
uparrow downarrow updownarrow Uparrow Downarrow Updownarrow nearrow searrow
swarrow nwarrow cdot times div ast star circ bullet otimes oplus odot ominus
oslash land lor wedge vee partial nabla in notin ni subset supset subseteq
supseteq subsetneq supsetneq le leq ge geq ne neq equiv sim simeq approx cong
propto parallel nparallel perp cup cap bigcup bigcap setminus smallsetminus
infty emptyset varnothing forall exists nexists neg lnot bot top ell hbar
Im Re wp aleph mathbb mathcal mathfrak mathscr mathbf mathrm mathit mathsf
mathtt boldsymbol operatorname stackrel overset underset overline overbrace
underbrace widehat widetilde hat bar vec dot ddot tilde breve check acute grave
left right middle big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr
mathord mathop mathbin mathrel mathopen mathclose mathpunct mathinner mathchoice
limits nolimits displaystyle textstyle scriptstyle scriptscriptstyle colon
angle triangle square boxminus boxtimes diamond uplus sqcup sqcap sqsubset
sqsupset sqsubseteq sqsupseteq models vdash dashv Vdash Vvdash therefore because
""".split())

# A signature describes arguments before and including a text body. Optional
# arguments and nonbody arguments are still scanned in their inherited mode.
TEXT_WRAPPERS = {
    name: ("body",) for name in {
        "text", "mbox", "hbox", "vbox", "vtop", "fbox", "textnormal",
        "textrm", "textsf", "texttt", "textmd", "textbf", "textup",
        "textit", "textsl", "textsc", "emph", "textsuperscript",
        "textsubscript", "margin", "diagram", "figure", "illegible",
        "cotefile", "scanpage", "mspage",
    }
}
TEXT_WRAPPERS.update({
    "makebox": ("opt", "opt", "body"),
    "framebox": ("opt", "opt", "body"),
    "parbox": ("opt", "opt", "opt", "arg", "body"),
    "raisebox": ("arg", "opt", "opt", "body"),
    "rotatebox": ("opt", "arg", "body"),
    "scalebox": ("arg", "opt", "body"),
    "resizebox": ("arg", "arg", "body"),
    "shortstack": ("opt", "body"),
    "marginpar": ("opt", "body"),
    "footnote": ("opt", "body"),
    "caption": ("opt", "body"),
    "colorbox": ("arg", "body"),
    "fcolorbox": ("arg", "arg", "body"),
    "section": ("opt", "body"),
    "subsection": ("opt", "body"),
    "subsubsection": ("opt", "body"),
    "paragraph": ("opt", "body"),
    "subparagraph": ("opt", "body"),
})


def load_helpers(path: Path) -> dict:
    """Load only three pure parser definitions; never initialize review.py."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    names = {"_tex_control", "_tex_group_end", "_active_tex_source"}
    selected = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    if {n.name for n in selected} != names:
        raise ValueError("The required pure parser helpers are missing")
    namespace = {"re": re}
    exec(compile(ast.Module(body=selected, type_ignores=[]), str(path), "exec"), namespace)
    return namespace


def analyze_text(text: str, helpers: dict) -> dict:
    """Inspect a supplied string without file access or inferred readings."""
    active = helpers["_active_tex_source"](text)
    control = helpers["_tex_control"]
    group_end = helpers["_tex_group_end"]
    line_starts = [0] + [m.end() for m in re.finditer("\n", active)]
    result = {"targets": [], "findings": [], "notes": []}

    def position(offset):
        index = bisect.bisect_right(line_starts, offset) - 1
        return {"line": index + 1, "column": offset - line_starts[index] + 1}

    def note(offset, message):
        result["notes"].append({**position(offset), "message": message})

    def argument(cursor, limit, optional=False):
        while cursor < limit and active[cursor].isspace():
            cursor += 1
        if cursor >= limit:
            return None
        if optional and active[cursor] != "[":
            return None
        if active[cursor] == "{" or (optional and active[cursor] == "["):
            end = group_end(active, cursor)
            return (cursor + 1, end - 1, end, cursor) if end and end <= limit else None
        if optional:
            return None
        end = control(active, cursor)[1] if active[cursor] == "\\" else cursor + 1
        return cursor, end, end, cursor

    def finding(offset, token, contexts, reason, kind="math-only control"):
        if not contexts:
            return
        target = contexts[-1]
        result["findings"].append({
            **position(offset), "token": token, "kind": kind,
            "target": target["macro"], "target_line": target["line"],
            "target_column": target["column"], "target_sha256": target["macro_sha256"],
            "mode_reason": reason,
            "enclosing_targets": [f"{c['macro']}@{c['line']}:{c['column']}" for c in contexts],
        })

    def conditional_end(cursor, limit):
        depth = 1
        while cursor < limit:
            if active[cursor] != "\\":
                cursor += 1
                continue
            start = cursor
            command, cursor = control(active, cursor)
            if command in CONDITIONALS:
                depth += 1
            elif command == "fi":
                depth -= 1
                if depth == 0:
                    return start, cursor
        return None

    def walk(start, end, initial_math, initial_reason, contexts=(), opaque=False):
        frames = [{"kind": "base", "math": initial_math, "reason": initial_reason}]
        tainted = False
        if initial_math is None and contexts:
            note(start, "Part of an editorial argument has unknown mode; no definite warning is assigned to inherited content.")
        i = start
        while i < end:
            frame = frames[-1]
            math = None if tainted else frame["math"]
            reason = "uncertain after a conflicting local delimiter" if tainted else frame["reason"]
            char = active[i]
            if char == "{":
                finish = group_end(active, i)
                if finish is None or finish > end:
                    note(i, "Unbalanced group; remaining local context is not classified.")
                    return
                walk(i + 1, finish - 1, math, reason, contexts, opaque or tainted)
                i = finish
                continue
            if char == "$":
                delimiter = "$$" if active.startswith("$$", i) else "$"
                if frame["kind"] == "delimiter" and frame["name"] == delimiter:
                    frames.pop()
                elif math is False:
                    frames.append({"kind": "delimiter", "name": delimiter, "math": True,
                                   "reason": f"explicit {delimiter} delimiter", "offset": i})
                elif math is None and not tainted:
                    if contexts:
                        note(i, "A dollar-delimited span starts in unknown mode; its inherited content remains unclassified.")
                    frames.append({"kind": "delimiter", "name": delimiter, "math": None,
                                   "reason": "dollar-delimited span with unknown entry mode", "offset": i})
                else:
                    note(i, "Dollar delimiter encountered in an inherited or different math context.")
                    frames[-1] = {**frame, "math": None, "reason": "uncertain after conflicting dollar delimiter"}
                    tainted = True
                i += len(delimiter)
                continue
            if char in "_^" and math is False and not (opaque or tainted):
                finding(i, char, contexts, reason, "math script character")
            if char != "\\":
                i += 1
                continue
            token_start = i
            command, i = control(active, i)
            if command == "catcode":
                note(token_start, "Category-code assignment makes the remaining local source opaque; no later local mode findings are inferred.")
                return
            if command in CONDITIONALS:
                finish = conditional_end(i, end)
                if finish is not None:
                    walk(i, finish[0], None, "unexpanded conditional branch", contexts, True)
                    i = finish[1]
                else:
                    note(token_start, "Conditional has no matching local fi; remaining local mode is unknown.")
                    frames[-1] = {**frame, "math": None, "reason": "unclosed conditional"}
                continue
            if command in {"(", "["}:
                if math:
                    note(token_start, "Opening math delimiter inside an existing math context.")
                    tainted = True
                frames.append({"kind": "delimiter", "name": ")" if command == "(" else "]",
                               "math": True, "reason": f"explicit \\{command} delimiter",
                               "offset": token_start})
                continue
            if command in {")", "]"}:
                if frame["kind"] == "delimiter" and frame["name"] == command:
                    frames.pop()
                else:
                    note(token_start, "Closing math delimiter has no matching local opener.")
                    frames[-1] = {**frame, "math": None, "reason": "uncertain after unmatched math delimiter"}
                    tainted = True
                continue
            if command in {"begin", "end"}:
                arg = argument(i, end)
                if arg is None or active[arg[3]] != "{":
                    note(token_start, "Environment token has no readable braced name.")
                    continue
                name = active[arg[0]:arg[1]].strip()
                i = arg[2]
                if command == "begin":
                    if name in MATH_REQUIRED_ENVIRONMENTS and math is False and not (opaque or tainted):
                        finding(token_start, "\\begin{" + name + "}", contexts, reason)
                    mode = True if name in MATH_ENVIRONMENTS else False if name in TEXT_ENVIRONMENTS else math if name in MATH_REQUIRED_ENVIRONMENTS else None
                    if mode is None and contexts:
                        note(token_start, f"Environment {name} has unknown argument or cell mode; no definite warning is assigned to inherited content.")
                    frames.append({"kind": "environment", "name": name, "math": mode,
                                   "reason": f"{name} environment" if name in MATH_ENVIRONMENTS | TEXT_ENVIRONMENTS else reason if name in MATH_REQUIRED_ENVIRONMENTS else f"unknown mode in {name} environment",
                                   "offset": token_start})
                elif frame["kind"] == "environment" and frame["name"] == name:
                    frames.pop()
                else:
                    note(token_start, "Environment close has no matching local opener; classification is conservative.")
                    frames[-1] = {**frame, "math": None, "reason": "uncertain after unmatched environment close"}
                    tainted = True
                continue
            if command in TARGETS:
                arg = argument(i, end)
                if arg is None or active[arg[3]] != "{":
                    note(token_start, f"Active \\{command} has no balanced braced argument.")
                    continue
                target = {**position(token_start), "macro": command, "math_at_entry": None if opaque or tainted else math,
                          "macro_sha256": hashlib.sha256(text[token_start:arg[2]].encode("utf-8")).hexdigest()}
                result["targets"].append(target)
                if math is None or opaque or tainted:
                    note(token_start, f"\\{command} occurs in an unknown mode context; no definite mode warning is assigned to inherited content.")
                walk(arg[0], arg[1], math, reason, (*contexts, target), opaque or tainted)
                i = arg[2]
                continue
            if command in MATH_ONLY and math is False and not (opaque or tainted):
                finding(token_start, "\\" + command, contexts, reason)
            if command == "ensuremath":
                arg = argument(i, end)
                if arg is not None:
                    walk(arg[0], arg[1], True, "argument to \\ensuremath", contexts, opaque or tainted)
                    i = arg[2]
                else:
                    note(token_start, "ensuremath argument could not be delimited.")
                continue
            if command in TEXT_WRAPPERS:
                cursor = i + int(i < end and active[i] == "*")
                if command in {"hbox", "vbox", "vtop"}:
                    while cursor < end and active[cursor].isspace():
                        cursor += 1
                    if re.match(r"(?:to|spread)\b", active[cursor:end]):
                        while cursor < end and active[cursor] != "{":
                            cursor = control(active, cursor)[1] if active[cursor] == "\\" else cursor + 1
                    if cursor >= end or active[cursor] != "{":
                        note(token_start, f"Nonbraced \\{command} syntax has unknown local argument mode.")
                        frames[-1] = {**frame, "math": None, "reason": f"unrecognized \\{command} syntax"}
                        continue
                segments = []
                for kind in TEXT_WRAPPERS[command]:
                    arg = argument(cursor, end, optional=kind == "opt")
                    if arg is None:
                        if kind == "opt":
                            continue
                        segments = []
                        note(token_start, f"Argument syntax for \\{command} was not recognized; no mode override was inferred.")
                        break
                    segments.append((kind, arg))
                    cursor = arg[2]
                if segments:
                    for kind, arg in segments:
                        walk(arg[0], arg[1], False if kind == "body" else math,
                             f"argument to \\{command}" if kind == "body" else reason, contexts, opaque or tainted)
                    i = cursor
                continue
            if command not in MATH_ONLY | INHERITED_WRAPPERS:
                # Unknown commands may establish their own argument mode. Only
                # explicitly delimited immediate arguments are treated as opaque;
                # this pass does not guess command arity or expand definitions.
                cursor = i
                while cursor < end:
                    while cursor < end and active[cursor].isspace():
                        cursor += 1
                    if cursor >= end or active[cursor] not in "{[":
                        break
                    arg = argument(cursor, end, optional=active[cursor] == "[")
                    if arg is None:
                        break
                    walk(arg[0], arg[1], None, f"unknown argument mode for \\{command}", contexts, opaque or tainted)
                    cursor = arg[2]
                    i = cursor
        for unclosed in frames[1:]:
            note(unclosed["offset"], "Unclosed local math delimiter or environment; review the static context.")

    walk(0, len(active), False, "page text")
    return result


def run(root: Path, page_map: Path, out_dir: Path) -> dict:
    root = root.resolve()
    out_dir = out_dir.resolve()
    if not out_dir.is_relative_to(root):
        raise ValueError("Diagnostics must be written within the explicit output root")
    if (root / "pages").is_symlink():
        raise ValueError("The output pages directory must not be a symlink")
    helpers = load_helpers(root / "scripts/review.py")
    with page_map.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    pages = []
    seen = set()
    for row in rows:
        name = Path(row.get("page_file") or row.get("codex_file") or "").name
        if not name or name in seen:
            raise ValueError("Map has a missing or duplicate output filename")
        seen.add(name)
        path = root / "pages" / name
        if not path.exists():
            continue
        if path.is_symlink() or not path.is_file() or path.suffix != ".tex":
            raise ValueError("Mapped output page is not a regular TeX file")
        pages.append((row, path, path.read_bytes()))
    actual = {p.name for p in (root / "pages").glob("*.tex")}
    if actual != {p.name for _, p, _ in pages}:
        raise ValueError("An output page is absent from the permitted filename map")
    report = {
        "created_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "scope": "Mechanical static context only; no expansion, compilation, visual or semantic review.",
        "limitations": "A finite list of known math-only controls and known mode boundaries is checked. Unknown braced macro arguments, TikZ/TikZ-cd and configurable table environments receive unknown coverage, not definite mode findings. Custom expansion, branch selection, category-code changes and unrecognized syntax are not evaluated. Findings require primary syntax review and do not authorize reading changes.",
        "page_count": len(pages), "target_count": 0, "page_summary": [], "findings": [], "notes": [], "page_sha256": {},
        "preamble_sha256": hashlib.sha256((root / "PREAMBLE.tex").read_bytes()).hexdigest(),
        "parser_sha256": hashlib.sha256((root / "scripts/review.py").read_bytes()).hexdigest(),
    }
    for row, path, data in pages:
        relative = path.relative_to(root).as_posix()
        scan = f"{row['cote']}/{row['our_scan']}"
        text = data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
        checked = analyze_text(text, helpers)
        report["target_count"] += len(checked["targets"])
        report["page_summary"].append({"scan": scan, "page_file": relative,
            "target_count": len(checked["targets"]), "review_flags": len(checked["findings"]),
            "context_notes": len(checked["notes"]), "entry_modes": {
                "math": sum(t["math_at_entry"] is True for t in checked["targets"]),
                "text": sum(t["math_at_entry"] is False for t in checked["targets"]),
                "unknown": sum(t["math_at_entry"] is None for t in checked["targets"]),
            }})
        report["page_sha256"][relative] = hashlib.sha256(data).hexdigest()
        for kind in ("findings", "notes"):
            report[kind].extend({"scan": scan, "page_file": relative, **item} for item in checked[kind])
    if actual != {p.name for p in (root / "pages").glob("*.tex")} or any(path.read_bytes() != data for _, path, data in pages):
        raise ValueError("Output pages changed during capture; no diagnostic was written")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = out_dir / f"tex_math_context_{stamp}"
    json_path, md_path = stem.with_suffix(".json"), stem.with_suffix(".md")
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Static math-context diagnostic", "", report["created_utc"], "", report["scope"], "",
             f"Captured **{report['page_count']} committed pages**, **{report['target_count']} editorial macro occurrences**, **{len(report['findings'])} token-level review flags**, and **{len(report['notes'])} parser/context notes**.", "",
             "The current output definitions of `\\unsure` and `\\deleted` inherit their surrounding math/text mode. A flagged control or script character appears in a text context under the recognized static boundaries; no text was changed.", "",
             "## Review flags", "", "| Scan | TeX line:column | Token | Enclosing macro at | Text context |",
             "|---|---|---|---|---|"]
    for f in report["findings"]:
        lines.append(f"| {f['scan']} | {f['line']}:{f['column']} | `{f['token']}` | `{f['target']}` {f['target_line']}:{f['target_column']} | {f['mode_reason']} |")
    if not report["findings"]:
        lines.append("| — | — | No flagged tokens | — | — |")
    lines.extend(["", "## Context notes", ""])
    lines.extend(f"- {n['scan']} {n['line']}:{n['column']}: {n['message']}" for n in report["notes"])
    if not report["notes"]:
        lines.append("No parser/context notes.")
    lines.extend(["", "## Limits", "", report["limitations"], "", "The JSON companion records exact captured page hashes. This report covers the committed subset and makes no claim of archive completeness.", ""])
    md_path.write_text("\n".join(lines), encoding="utf-8")
    event = {"event": "STATIC_MATH_CONTEXT_DIAGNOSTIC", "page_count": len(pages),
             "target_count": report["target_count"], "review_flags": len(report["findings"]),
             "context_notes": len(report["notes"]), "report": str(md_path.relative_to(root)),
             "json": str(json_path.relative_to(root)), "page_bytes_preserved": True}
    with (root / "tooling.log").open("a", encoding="utf-8") as handle:
        handle.write(report["created_utc"] + " " + json.dumps(event, sort_keys=True) + "\n")
    return event


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--page-map", type=Path, required=True, help="Permitted filename metadata TSV only")
    parser.add_argument("--out-dir", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(run(args.root, args.page_map, args.out_dir or args.root / "diagnostics"), indent=2))
    except (OSError, ValueError, KeyError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
