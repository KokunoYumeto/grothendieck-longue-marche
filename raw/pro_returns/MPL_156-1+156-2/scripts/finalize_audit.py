"""Consolidate final audit metadata without altering the transcription files."""
from pathlib import Path
from datetime import datetime, timezone
import collections
import csv
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
NAME = "MPL_156-1+156-2"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

# Earlier readings are retained in the record history but are not competing
# current entries in the final register.
SUPERSEDED = {
    ("156-1", 6): {"left dated margin phrase"},
    ("156-1", 10): {"first map element arrow"},
    ("156-1", 14): {"near bottom parenthesis"},
    ("156-1", 23): {"left margin after régulières"},
    ("156-2", 2): {"middle phrase ces ... propriétés"},
    ("156-2", 5): {"upper triangular margin parenthesis", "six main subspace initials", "faint paper lettering"},
    ("156-2", 9): {"definition at bottom, heavily retraced symbol"},
    ("156-2", 10): {"upper left marginal opening", "parenthesis after disjoints"},
    ("156-2", 12): {"parenthesis after pour P"},
}
records = []
for path in sorted((ROOT / "records").glob(f"{NAME}_*.json")):
    rec = json.loads(path.read_text())
    key = rec["cote"], rec["scan"]
    old = rec.get("doubts", [])
    removed = [d for d in old if d[0] in SUPERSEDED.get(key, set())]
    if removed:
        rec.setdefault("superseded_doubts", []).extend(removed)
        rec["doubts"] = [d for d in old if d not in removed]
    if key == ("156-1", 9):
        for doubt in rec.get("doubts", []):
            if doubt[0] == "NB acronym/sign":
                doubt[:] = ["NB acronym", "DPS", "acronym or compressed words; the accompanying equality sign was resolved in the second audit", "low"]
    if removed or key == ("156-1", 9):
        rec["doubts_consolidated_utc"] = NOW
        path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
    records.append(rec)

notation = {}
abbreviations = {}
for rec in records:
    notation.update(rec.get("notation", {}))
    abbreviations.update(rec.get("abbreviations", {}))

notation.update({
    "Set of lieux, handwritten looped capital": r"$L$ in the abstract segment axioms of 156-1; $\mathcal L$ for the more fully looped collection of lieux of a ficelle in 156-2 scans 007, 010 and 012. These are visual alphabet choices, not a claim that every cursive capital L belongs to a distinct mathematical alphabet.",
    "Tilde over segment letter": r"$\tilde I$; compared with bars and circles throughout both readings. Later bare $I$ is retained where actually written.",
    "Membership annotation written vertically": r"x above \rotatebox{-90}{$\in$} above \delta I; the rotation follows the ink (156-1 scan 017).",
    "Orientation quotient with an underline": r"$\underline{\omega}$; element $\omega\in\underline{\omega}$. The three stand-alone occurrences in 156-1 scan 016 and the quotient/element distinction in scan 018 were compared; $\omega_S$ and $\omega_L$ remain un-underlined.",
    "Revised complementary subspaces in 156-2 scan 5": r"\unsure{\deleted{U}\inserted{X}|\deleted{X}\inserted{U}} at each of the six overwritten initials; the direction of revision is not treated as certain. Later clean X and marginal U remain as written.",
    "Vertical equality with definition label": r"\unsure{\Vert|\text{''}}\,\text{déf}; the paired strokes are placed in the label stack, with both equality-like and ditto readings recorded.",
    "Ordered set of lieux, heavily retraced first occurrence": r"\unsure{\mathcal F_C|F_C} at 156-2 scan 009; the earlier tentative \mathcal L_C was superseded on visual audit, without inferring a recoverable deletion sequence.",
    "Prime versus exclamation-mark exponents": r"Genuine primes include I', W'_t and \rho'. The marginal \beta at 156-2 scan 011 has \unsure{\beta'|\beta}. No exclamation-mark exponent was identified in these 46 scans; the explicit uniqueness mark in \exists! is retained.",
    "Mathematical accents and grouping": r"Accented operator/text labels use \text{déf} and \operatorname{\text{Cône}}; grouping around {\unsure{\mathbb F_2}}_{U} prevents a TeX double subscript without changing its written indices.",
    "Diagram cell separators inside state macros": r"tikz-cd uses ampersand replacement=\& and \& between cells because each diagram is the argument of \diagram; the array on 156-1 scan 022 is enclosed in display math. These are syntax repairs only.",
})
notation.pop("Vertical paired strokes below branch expressions", None)

def cell(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")

def code(value):
    return "<code>" + html.escape(str(value)).replace("|", "&#124;").replace("\n", " ") + "</code>"

lines = [
    "# Notation table", "",
    "This table records the conventions used across the complete package. Recurring signs were compared during the page audits and in a final cross-page pass before the transcription was frozen; a genuine change of notation is retained, and unresolved visual alternatives remain marked in place.", "",
    "| Manuscript sign or convention | LaTeX transcription and audit decision |",
    "|---|---|",
]
for k, v in notation.items():
    lines.append(f"| {cell(k)} | {cell(v)} |")

lines += [
    "", "# Reading doubts", "",
    "Positions in this first table refer to approximate manuscript locations. Confidence is a qualitative reading judgment, not a calibrated probability; superseded first-pass alternatives are retained in the individual JSON records under `superseded_doubts`, rather than presented here as current readings.", "",
    "| Cote | Scan | Approximate line / position | Reading | Alternatives | Confidence |",
    "|---|---:|---|---|---|---|",
]
for rec in records:
    for doubt in rec.get("doubts", []):
        lines.append("| " + " | ".join(cell(x) for x in [rec["cote"], rec["scan"], *doubt]) + " |")

def escaped(s, i):
    count = 0
    i -= 1
    while i >= 0 and s[i] == "\\":
        count += 1
        i -= 1
    return count % 2 == 1

def contents(s, opening):
    depth = 1
    for i in range(opening + 1, len(s)):
        if s[i] == "{" and not escaped(s, i):
            depth += 1
        elif s[i] == "}" and not escaped(s, i):
            depth -= 1
            if depth == 0:
                return s[opening + 1:i], i
    raise ValueError(f"Unclosed macro at {opening}")

def alternatives(s):
    depth = 0
    cuts = []
    for i, ch in enumerate(s):
        if ch == "{" and not escaped(s, i):
            depth += 1
        elif ch == "}" and not escaped(s, i):
            depth -= 1
        elif ch == "|" and depth == 0 and not escaped(s, i):
            cuts.append(i)
    if not cuts:
        return s, "No second decipherment supplied."
    return s[:cuts[0]], s[cuts[0] + 1:]

index = []
for rec in records:
    path = ROOT / "pages" / f'{NAME}_{rec["cote"]}_scan{rec["scan"]:03}.tex'
    source = path.read_text()
    for match in re.finditer(r"\\(unsure|illegible)\{", source):
        argument, end = contents(source, match.end() - 1)
        reading, alternative = alternatives(argument)
        if match.group(1) == "illegible":
            reading = f"Physically unreadable: estimated {argument} words"
            alternative = "Only scattered strokes survive; see 156-2 scan 002 cancelled lower-left margin."
        confidence = "low"
        # Only an exact matching recorded reading can promote the index row.
        # Otherwise the conservative label does not pretend to recover precision.
        for d in rec.get("doubts", []):
            if reading == d[1]:
                confidence = d[3]
                break
        if "EXTRA STRONG" in argument:
            confidence = "low"
        index.append({
            "cote": rec["cote"], "scan": rec["scan"],
            "source_line": source.count("\n", 0, match.start()) + 1,
            "macro": match.group(1), "argument": argument,
            "reading": reading, "alternative": alternative,
            "confidence": confidence,
        })

counts = collections.Counter(x["macro"] for x in index)
lines += [
    "", "# Complete in-place uncertainty index", "",
    f'This supplementary index contains every occurrence of `\\unsure` ({counts["unsure"]}) and `\\illegible` ({counts["illegible"]}) in the 46 page files, including nested occurrences and the 88 faint paper legends. It is extracted with balanced-brace parsing from the final page files; the wording is the exact frozen LaTeX, not an editorial correction.', "",
    "The locator is explicitly a **LaTeX source line**, not a counted manuscript line: paragraph reflow makes a source-line number more reproducible than an invented handwritten line count. The manuscript-position table above supplies visual locations; where no exact confidence match is available there, this exhaustive index conservatively uses **low**, rather than claiming additional certainty.", "",
    "| Cote | Scan | Source line | Macro | Reading | Alternative(s) | Confidence |",
    "|---|---:|---:|---|---|---|---|",
]
for x in index:
    lines.append(f'| {x["cote"]} | {x["scan"]} | {x["source_line"]} | {code(x["macro"])} | {code(x["reading"])} | {code(x["alternative"])} | {x["confidence"]} |')
(ROOT / "records" / "uncertainty_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")

lines += [
    "", "# Abbreviations", "",
    "Expansions here are editorial proposals only; the transcription retains the written abbreviations. A raised ending is described rather than silently expanded, and doubtful readings remain doubtful.", "",
    "| Abbreviation | Proposed expansion |", "|---|---|",
]
for k, v in abbreviations.items():
    lines.append(f"| {cell(k)} | {cell(v)} |")

lines += [
    "", "# Legibility and limits", "",
    "All 46 whole-page scans and both supplied overlapping halves were read visually by the same transcriber, in the specified order; no OCR was used. Every page received a second visual audit before the context archive was opened. The principal running text and most displays are reasonably legible, but this remains a difficult diplomatic reading, not a claim of error-free decipherment.", "",
    "The least secure material is small rotated marginal writing, multi-layer corrections, and heavily cancelled drafts: especially 156-1 scans 002, 005–007, 023 and 026, and 156-2 scans 002, 005, 007, 010, 011 and 018. In ambiguous corrections, the visible alternatives are retained without asserting an unsupported order of revision. The one physically unreadable span, estimated at two words in the cancelled lower-left margin of 156-2 scan 002, was retained as `\\deleted{\\illegible{2}}` after enlarged visual attempts; doubtful formula symbols instead receive proposed readings under `\\unsure`.", "",
    "The 44 manuscript sheets each show two low-contrast paper legends, recorded as doubtful `EXTRA STRONG`, with reversal and rotation preserved; these 88 nonmathematical occurrences account for a substantial part of the uncertainty count. The two institutional cover scans are also transcribed. TikZ drawings preserve topology, relative placement, strokes and visible labels as closely as the available images permit, but they are approximations of hand-drawn geometry; diagram-arrow and plain-stroke distinctions remain explicit.", "",
    "Unbalanced punctuation, unfinished clauses, surprising equalities or quantifiers, differing notations and explicit retractions have not been repaired from mathematical expectations. Any mathematical proposal or possible correction belongs only in the separate research notes. The exact uncertainty index above makes small doubtful items searchable even when the manuscript-position table groups several such items together.",
]
(ROOT / f"{NAME}_doubts.md").write_text("\n".join(lines) + "\n")

inventory = list(csv.DictReader((ROOT / f"{NAME}_inventory.csv").open()))
assert len(records) == 46 and len({(r["cote"], r["scan"]) for r in records}) == 46
assert all(row["transcribed"] == "yes" for row in inventory)
assert counts["illegible"] == 1
with (ROOT / "progress.log").open("a") as log:
    log.write(f"final notation audit completed {NOW}; recurring alphabet, tilde/interior, orientation underline, prime/paired-stroke, arrowhead and abbreviation families compared before context access\n")
    log.write(f"doubts consolidated {NOW}; {counts['unsure']} unsure occurrences and {counts['illegible']} illegible occurrence indexed; {len(inventory)} inventory rows all yes\n")
print(json.dumps({"page_records": len(records), "inventory_rows": len(inventory), "uncertainty_macros": counts}, indent=2))
