"""Assemble the scan-007 draft from finalized, current-page main observations.

Authority: records/scan007/main_observations.md, observations 1--26.
The C/H packets and the three reader returns are text inputs only.  This script
does not open image/PDF files, invoke OCR or the web, or compile/render TeX.
It writes only records/scan007/page_draft.tex and its validation record; the
main reader is responsible for reviewing and installing the page.
"""
from pathlib import Path
import hashlib
import json
import re


OUT = Path(__file__).resolve().parents[1]
RECORDS = OUT / "records/scan007"
PAGE = RECORDS / "page_draft.tex"
PLAN = RECORDS / "main_crop_plan.json"
OBSERVATIONS = RECORDS / "main_observations.md"
REQUIRED_NUMBERS = set(range(1, 27))


TEX = r'''\scanpage{7}
\mspage{1}

% This entirely handwritten page has no handwriting envelope (briefv06).
% Main 01: certain accent, unresolved direction; two quotation ticks each side.
Soit \(M\) une catégorie (``\unsure{modèles|modéles}''). On suppose

% Main 02: accent direction remains uncertain; no point after monomorphique.
(i) Toute \unsure{flèche|fléche} de \(M\) est monomorphique

% Main 03: abbreviated old word, uncertain old stop, raised end without stop.
(ii) Tout \deleted{\unsure{autom|autom.}}\inserted{end} d'un élément de \(M\) est l'identité.

% Main 04: the reduced internal strokes do not resolve par.
Ex : \(M\) une catégorie définie \unsure{par} un ensemble ordonné

% Main 05: quotation ticks and a real blank, without a hyphen, in sous objets.
% Main 06: no point follows the terminal tilded D of the identification.
Pour tout \(D\in\mathrm{Ob}\,M\), soit \(\widetilde D\) l'ensemble (ordonné par ``inclusion'') des sous objets de \(D\). On identifie \(D\) au plus grand élément de \(\widetilde D\)

Soient \(D',D\in\mathrm{Ob}\,M\), alors l'application
% Main 07: a literal two-row map; M belongs under the final m of Hom.
% Lower u is indented; its barred shaft starts farther left and runs longer.
% The star is far left between row levels; the upper target has no comma.
\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=0pt,column sep=0pt]
{\begin{tikzpicture}[x=1em,y=1em,line width=.45pt,
 line cap=round,line join=round]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (homHo)
 at (0,0) {$\mathrm{Ho}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (homLast)
 at (homHo.base east) {$\mathrm m$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (homArgs)
 at (homLast.base east) {$(D',D)$};
\node[anchor=north,inner sep=0pt,outer sep=0pt]
 at ([yshift=-.12em]homLast.south) {$\scriptstyle M$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt]
 at (10,0) {$\widetilde D$};
\draw[->] ([xshift=.65em,yshift=.25em]homArgs.base east)--(9.5,.25);
\node[anchor=base west,inner sep=0pt,outer sep=0pt]
 at (1.65,-1.8) {$u$};
\draw[|->] (3,-1.55)--(9.5,-1.55);
\node[anchor=base west,inner sep=0pt,outer sep=0pt]
 at (10,-1.8) {$u(D')$};
\node[inner sep=0pt,outer sep=0pt] at (-2.4,-.65) {$(\ast)$};
\end{tikzpicture}}
\end{tikzcd}}
% Main 08: mixed first enclosure retained ahead of the two matched alternatives.
% Main 09: ens has no stop; the canceled de remains low-confidence;
% Phi is resolved, and inserted M- attaches before isomorphes.
est injective par \unsure{(i]|[i]|(i)}(ii), son image est formée de l'ens \deleted{\unsure{de}}
\(\Phi_{D'}(D)\subset\widetilde D\)
des sous-objets \(\Delta\) de \(D\) qui sont \inserted{\(M\)-}isomorphes à \(D'\).

\deleted{Soit \(K\) un ens. ordonné}

% Main 10--13 and 26: plain live N, deleted I, interlinear preordonne;
% the inserted sentence has only ordonne underlined; preceding M has its point.
Soit \(N\)\deleted{\(I\)} l'ens \inserted{préordonné} des classes d'isom. d'objets de \(M\). \inserted{Il est en fait \uline{ordonné}, grâce à (ii).}
% Main 14--18: unresolved forall/H, doubled N, canceled e/s, old D and live M;
% a raised star over n, and the first isom without a stop.
Pour \(\unsure{\forall|\mathrm H}\ n\in\mathbb N\), un\deleted{\unsure{e|s}} objet \(D_n\) de \deleted{\(D\)}\(M\) de classe \(\overset{\ast}{n}\) est déterminé à isom unique près,
% Main 19: reduced a/colon cluster plus a separate low down-right stroke.
% The literal stroke is neither a character candidate nor a therefore sign.
\begin{tikzpicture}[baseline=(causecluster.base),x=1em,y=1em,
 line width=.45pt,line cap=round]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (causecluster)
 at (0,0) {\unsure{à|:}};
\draw ([xshift=.12em,yshift=-.4em]causecluster.south east)
 --([xshift=.25em,yshift=-.62em]causecluster.south east);
\end{tikzpicture} cause de (ii),
% Main 20--22: ens without a stop; plain tilde D_n equals doubled J_n;
% resolved defini and the second isom without a stop.
donc l'ens ordonné \(\widetilde D_n=\mathbb J_n\) est défini à isom unique près.
% Main 23: dotted plui remains the first candidate; comma and old une are deleted.
On a donc \deleted{\unsure{plui|plus}, une}\inserted{une} famille
% Main 24: the family is a separate display.
\[
(\mathbb J_n)_{n\in\mathbb N}
\]
% Main 25: retain the observed footer wording and punctuation.
d'ens ordonnés, indexés par l'ensemble ordonné \(\mathbb N\).
% archive sheet number: 6
'''


def readiness():
    """Require every planned view and every numbered main observation."""
    plan = json.loads(PLAN.read_text())
    observations = OBSERVATIONS.read_text()
    plan_numbers = [row.get("number") for row in plan]
    observation_numbers = [int(number) for number in
                           re.findall(r"^(\d+)\.\s", observations, re.M)]
    errors = []
    if set(plan_numbers) != REQUIRED_NUMBERS or len(plan_numbers) != 26:
        errors.append("Crop plan must contain each number 1--26 exactly once")
    unviewed = [row.get("number") for row in plan if row.get("viewed") is not True]
    if unviewed:
        errors.append(f"Unviewed crop-plan entries: {unviewed}")
    missing = sorted(REQUIRED_NUMBERS - set(observation_numbers))
    if missing:
        errors.append(f"Missing main observations: {missing}")
    duplicates = sorted({number for number in observation_numbers
                         if observation_numbers.count(number) > 1})
    if duplicates:
        errors.append(f"Duplicate main observations: {duplicates}")
    unresolved = sorted(set(re.findall(r"@@MAIN\d+@@", TEX)))
    if unresolved:
        errors.append(f"Unassembled finalized decisions: {unresolved}")
    return {"errors": errors, "plan_entries": len(plan),
            "viewed_entries": len(plan) - len(unviewed),
            "observation_numbers": observation_numbers,
            "authority_sha256": hashlib.sha256(observations.encode()).hexdigest(),
            "crop_plan_sha256": hashlib.sha256(PLAN.read_bytes()).hexdigest()}


def validate(text):
    """Check source structure and the explicit decisions, without compilation."""
    errors = []
    clean = "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0]
                      for line in text.splitlines())
    brace = 0
    for token in re.findall(r"\\.|[{}]", clean):
        if token == "{":
            brace += 1
        elif token == "}":
            brace -= 1
            if brace < 0:
                errors.append("Closing brace before opening brace")
                break
    if brace:
        errors.append(f"Brace balance is {brace}")
    stack = []
    environments = {}
    for match in re.finditer(r"\\(begin|end)\{([^{}]+)\}", clean):
        operation, env = match.groups()
        if operation == "begin":
            stack.append(env)
            environments[env] = environments.get(env, 0) + 1
        elif not stack or stack.pop() != env:
            errors.append(f"Mismatched environment {env}")
    if stack:
        errors.append(f"Unclosed environments {stack}")
    diagrams = re.findall(r"\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}", clean, re.S)
    if len(diagrams) != 1:
        errors.append("Expected exactly one tikzcd mapping container")
    for diagram in diagrams:
        if "ampersand replacement=\\&" not in diagram:
            errors.append("tikzcd lacks ampersand replacement")
        if re.search(r"(?<!\\)&", diagram):
            errors.append("Bare ampersand inside tikzcd")
    for left, right, name in ((r"\[", r"\]", "display"),
                              (r"\(", r"\)", "inline")):
        depth = 0
        pattern = r"(?<!\\)(?:" + re.escape(left) + "|" + re.escape(right) + ")"
        for token in re.findall(pattern, clean):
            depth += 1 if token == left else -1
            if depth not in (0, 1):
                errors.append(f"Improper {name} delimiter ordering")
                break
        if depth:
            errors.append(f"Unbalanced {name} delimiters: {depth}")
    dollar_count = len(re.findall(r"(?<!\\)\$", clean))
    if dollar_count % 2:
        errors.append(f"Odd dollar delimiter count: {dollar_count}")
    if re.findall(r"\\scanpage\{([^}]*)\}", clean) != ["7"]:
        errors.append("Scan marker must be exactly scanpage{7}")
    if re.findall(r"\\mspage\{([^}]*)\}", clean) != ["1"]:
        errors.append("Own folio must be exactly mspage{1}")
    if clean.count(r"\handwritten{") != 0:
        errors.append("Entirely handwritten pages have no handwriting envelope")
    if text.count("% archive sheet number: 6") != 1:
        errors.append("Expected one archive-number comment for 6")
    for forbidden in (r"\cotefile{", r"\newcommand", r"\renewcommand", r"\def",
                      r"\illegible{", r"\unsure{}", r"\therefore", r"\mathscr L",
                      "automorphisme", "choisi", "comme dans", "@@MAIN"):
        if forbidden in clean:
            errors.append(f"Unexpected token {forbidden}")
    mapping = {
        1: [r"(``\unsure{modèles|modéles}'')"],
        2: [r"Toute \unsure{flèche|fléche} de \(M\) est monomorphique\n".replace(r"\n", "\n")],
        3: [r"\deleted{\unsure{autom|autom.}}\inserted{end}"],
        4: [r"définie \unsure{par} un ensemble ordonné"],
        5: [r"par ``inclusion'') des sous objets"],
        6: [r"au plus grand élément de \(\widetilde D\)\n".replace(r"\n", "\n")],
        7: [r"at (homHo.base east) {$\mathrm m$}",
            r"at (homLast.base east) {$(D',D)$}",
            r"at ([yshift=-.12em]homLast.south) {$\scriptstyle M$}",
            r"at (10,0) {$\widetilde D$}",
            r"\draw[->] ([xshift=.65em,yshift=.25em]homArgs.base east)--(9.5,.25)",
            r"at (1.65,-1.8) {$u$}",
            r"\draw[|->] (3,-1.55)--(9.5,-1.55)",
            r"at (10,-1.8) {$u(D')$}",
            r"at (-2.4,-.65) {$(\ast)$}"],
        8: [r"\unsure{(i]|[i]|(i)}(ii),"],
        9: [r"l'ens \deleted{\unsure{de}}", r"\Phi_{D'}(D)\subset\widetilde D",
            r"qui sont \inserted{\(M\)-}isomorphes"],
        10: [r"Soit \(N\)\deleted{\(I\)}"],
        11: [r"l'ens \inserted{préordonné}"],
        12: [r"\inserted{Il est en fait \uline{ordonné}, grâce à (ii).}"],
        13: [r"d'objets de \(M\). \inserted"],
        14: [r"\unsure{\forall|\mathrm H}\ n\in\mathbb N"],
        15: [r"un\deleted{\unsure{e|s}} objet"],
        16: [r"de \deleted{\(D\)}\(M\) de classe"],
        17: [r"de classe \(\overset{\ast}{n}\)"],
        18: [r"est déterminé à isom unique près,"],
        19: [r"at (0,0) {\unsure{à|:}}",
             r"\draw ([xshift=.12em,yshift=-.4em]causecluster.south east)",
             r"--([xshift=.25em,yshift=-.62em]causecluster.south east)",
             r"\end{tikzpicture} cause de (ii),"],
        20: [r"donc l'ens ordonné"],
        21: [r"\(\widetilde D_n=\mathbb J_n\)"],
        22: [r"est défini à isom unique près."],
        23: [r"\deleted{\unsure{plui|plus}, une}\inserted{une} famille"],
        24: [r"(\mathbb J_n)_{n\in\mathbb N}"],
        25: [r"d'ens ordonnés, indexés par l'ensemble ordonné \(\mathbb N\)."],
        26: [r"des classes d'isom. d'objets"],
    }
    decision_checks = []
    for number, required in mapping.items():
        missing = [token for token in required if token not in text]
        if missing:
            errors.append(f"Main {number} tokens missing: {missing}")
        decision_checks.append({"main_observation": number, "required_tokens": required,
                                "missing_tokens": missing, "passed": not missing})
    return {
        "page": str(PAGE.relative_to(OUT)),
        "authority": "records/scan007/main_observations.md, observations 1–26",
        "scope": "Text-only draft assembly and structural/source-decision validation. "
                 "No image/PDF/OCR/web/compilation/rendering or mathematical check.",
        "errors": errors,
        "environment_counts": environments,
        "dollar_delimiters": dollar_count,
        "unsure_count": clean.count(r"\unsure{"),
        "deleted_count": clean.count(r"\deleted{"),
        "inserted_count": clean.count(r"\inserted{"),
        "diagram_count": clean.count(r"\diagram{"),
        "handwritten_blocks": clean.count(r"\handwritten{"),
        "own_folio": 1,
        "archive_sheet_number_comment": 6,
        "decision_checks": decision_checks,
        "preamble_sha256": hashlib.sha256((OUT / "PREAMBLE.tex").read_bytes()).hexdigest(),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
    }


if __name__ == "__main__":
    gate = readiness()
    if gate["errors"]:
        print(json.dumps({"status": "blocked_without_writing", **gate},
                         indent=2, ensure_ascii=False))
        raise SystemExit(2)
    result = validate(TEX)
    result["readiness"] = gate
    if result["errors"]:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        raise SystemExit(1)
    PAGE.write_text(TEX)
    (RECORDS / "assembler_validation.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"page": result["page"], "errors": result["errors"],
                      "main_decisions_checked": len(result["decision_checks"]),
                      "sha256": result["sha256"]}, ensure_ascii=False))
