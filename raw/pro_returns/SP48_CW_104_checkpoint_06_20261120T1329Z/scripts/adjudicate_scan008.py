#!/usr/bin/env python3
"""Assemble the scan 008 draft from the main reader's recorded decisions.

This is a text-only operation.  It never reads an image or modifies a source,
reader report, authoritative page, decision record, or cumulative file.
"""

from pathlib import Path
import argparse
import json
import re


ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "records" / "scan008"
SOURCE = ROOT.parent / "reader_inputs" / "scan008" / "C.tex"
DESTINATION = RECORD / "page_draft.tex"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--final", action="store_true",
        help="require all 34 viewed crops and all 34 main observations",
    )
    args = parser.parse_args()

    plan = json.loads((RECORD / "main_crop_plan.json").read_text())
    log = (RECORD / "main_observations.md").read_text()
    matches = list(re.finditer(r"(?m)^(\d+)\.\s", log))
    observations = {}
    for index, match in enumerate(matches):
        number = int(match.group(1))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(log)
        if number in observations:
            raise ValueError(f"Duplicate main observation {number}")
        observations[number] = log[match.end():end].strip()

    expected = set(range(1, 35))
    if len(plan) != 34 or {row["number"] for row in plan} != expected:
        raise ValueError("Expected the fixed 34-locus main crop plan")
    if not set(observations) <= expected:
        raise ValueError("Unexpected numbered observation")
    viewed = {row["number"] for row in plan if row["viewed"] is True}
    for number, observation in observations.items():
        if number not in viewed:
            raise ValueError(f"Observation {number} is not marked viewed in the plan")
        if "inspected once" not in observation:
            raise ValueError(f"Observation {number} lacks its explicit inspection record")
    if args.final and (viewed != expected or set(observations) != expected):
        raise ValueError("Final draft requires all 34 viewed crops and observations")

    page = SOURCE.read_text()
    applied = []
    handled = set()

    def confirm(number, evidence):
        if number not in observations:
            return False
        if evidence not in observations[number]:
            raise ValueError(f"Main observation {number} does not confirm: {evidence}")
        handled.add(number)
        return True

    def decision(number, evidence, old, new):
        nonlocal page
        if not confirm(number, evidence):
            return
        if page.count(old) != 1:
            raise ValueError(f"Decision {number} does not have one exact source target")
        page = page.replace(old, new, 1)
        applied.append(number)

    # Add an amendment only after its numbered main observation exists.
    confirm(1, "The line reads De plus, se rappelant")
    decision(2, "Resolve unaccented definition", r"\unsure{definition|définition}", "definition")
    confirm(3, "plain J_n, not I_n or a doubled J")
    decision(4, "Resolve singular sous-objet", r"\unsure{sous-objet|sous-objets}", "sous-objet")
    decision(5, "encode unsure{H|forall}", r"\forall n\in", r"\unsure{\mathrm{H}|\forall} n\in")
    confirm(6, "no surrounding parentheses or closing quote")
    decision(7, "Resolve formée", r"\unsure{formée|formé}", "formée")
    confirm(8, "Retain l'ens")
    decision(
        9, "retain the point as a separate literal trace",
        r"\deleted{\(I_{\leq n}\) des} \(",
        r"\deleted{\(I_{\leq n}\) des} \tikz[baseline=.2ex]{\fill (0,0) circle (.025);}% detached point; no punctuation function assigned"
        "\n" + r"\(",
    )
    confirm(10, "plain J_n")
    confirm(11, "Preserve the open quotation")
    decision(12, "Read en tant", r"\unsure{en tant|en}", "en tant")
    decision(
        13, "Retain one low-confidence cluster",
        r"qu'\deleted{\unsure{est|il}}\unsure{on|on y}",
        r"\unsure{que je|qu'\deleted{est}on|qu'\deleted{il}on|qu'\deleted{est}on y|qu'\deleted{il}on y}",
    )
    confirm(14, "Encode it as an insertion there")
    decision(
        15, "remove C's supplied period",
        r"\deleted{Si \(n'\leq n\), alors pour tout \(x\in J_n\).}",
        r"\deleted{Si \(n'\leq n\), alors pour tout \(x\in J_n\)}",
    )
    confirm(16, "Retain deleted unsure{x in J|x in}")
    confirm(17, "Keep on inside the deletion")
    decision(18, "A single live considérons", r"\unsure{considérons|considérer}", "considérons")
    decision(
        18, "retain deleted unsure{via x|via (x)}",
        r"\unsure{via \(x\)|via \((x)\)|l'in}",
        r"\unsure{via \(x\)|via \((x)\)}",
    )
    decision(19, "plain D_n", r"\unsure{D|\mathbb D}_n", r"D_n")
    decision(
        19, "Preserve this modest horizontal displacement",
        r"u&\longmapsto u(d_{n'})",
        r"u&\mkern2mu\longmapsto u(d_{n'})",
    )
    confirm(20, "Retain l'ens")
    decision(21, "Retain unsure{4|ast}", r"^{\unsure{\ast|\prime}}", r"^{\unsure{4|\ast}}")
    confirm(22, "Retain each drawn bracket and lower label literally")
    decision(
        23, "Preserve both as small literal ink traces",
        r"{\widetilde D_n}\bigr)",
        r"{\widetilde D_n}\bigr)" + "\n "
        + r"\quad\raisebox{-3.5ex}{\tikz{\fill (0,.12) ellipse (.025 and .018);\fill (-.07,0) circle (.022);}}% detached points; no punctuation function assigned",
    )
    decision(24, "Resolve the canceled fragment bijec", r"\deleted{\unsure{bi ce|bi se}}", r"\deleted{bijec}")
    confirm(25, "Read unaccented def")
    confirm(26, "retain deleted unsure{(n')|(n)}")
    confirm(27, "The arrow label is rho_{n,n'}")
    decision(
        28, "they enclose the sign AND the Hom line",
        r"\underset{\substack{\rotatebox{90}{\(=\)}\\ {[\mathrm{Hom}(D_{n'},D_n)]}}}{\tau_n^{-1}(n')}",
        r"""% One uncertain physical relation: rotated simeq | rotated equals; literal strokes retained.
 \underset{\left[\begin{gathered}
   \unsure{\tikz[x=1em,y=1em,baseline=0pt]{
     \draw[line width=.35pt] (.12,.56) .. controls (.18,.37) and (-.08,.12) .. (.02,.03)
       .. controls (.07,-.02) and (.18,-.02) .. (.23,.03);
     \draw[line width=.35pt] (.43,.59)--(.43,.08);
     \fill (0,.61) circle (.025);}}\\
   \mathrm{Hom}(D_{n'},D_n)
 \end{gathered}\right]}{\tau_n^{-1}(n')}""",
    )
    confirm(29, "Preserve the four lines and their placement beneath the bracket")
    decision(30, "Resolve unaccented ou", r"\unsure{ou|où}", "ou")
    confirm(31, "no inserted ou")
    confirm(32, "Retain unsure{commutativité|commutativite}")
    confirm(33, "no de is present")
    decision(
        34, "Preserve both detached ends",
        r"([xshift=.25em,yshift=-.15em]\tikzcdmatrixname-1-1.south east)",
        r"([xshift=.15em,yshift=-1em]\tikzcdmatrixname-1-1.south east)",
    )
    decision(
        34, "do not connect the right end to a node corner",
        r"..(\tikzcdmatrixname-1-3.south west);}",
        r"..([xshift=-1em,yshift=-.75em]\tikzcdmatrixname-1-3.south west);}",
    )

    if args.final and handled != expected:
        raise ValueError(f"Unimplemented main observations: {sorted(expected - handled)}")

    # Small structural checks only; these do not compile or render the TeX.
    if not page.startswith(r"\scanpage{8}" + "\n"):
        raise ValueError("Page must start with its scan marker")
    if r"\handwritten" in page or r"\cotefile" in page or r"\mspage" in page:
        raise ValueError("Unexpected handwritten wrapper or page marker")
    if page.count("``") != 2 or "''" in page:
        raise ValueError("The two open quotation pairs must remain unclosed")
    if "% archive sheet number: 7" not in page:
        raise ValueError("Archive sheet comment is missing")
    if page.count(r"\[") != page.count(r"\]"):
        raise ValueError("Unbalanced display delimiters")
    if page.count(r"\(") != page.count(r"\)"):
        raise ValueError("Unbalanced inline math delimiters")
    environments = []
    for match in re.finditer(r"\\(begin|end)\{([^{}]+)\}", page):
        operation, environment = match.groups()
        if operation == "begin":
            environments.append(environment)
        elif not environments or environments.pop() != environment:
            raise ValueError("Mismatched TeX environments")
    if environments:
        raise ValueError("Unclosed TeX environment")
    depth = 0
    for match in re.finditer(r"(?<!\\)[{}]", page):
        depth += 1 if match.group() == "{" else -1
        if depth < 0:
            raise ValueError("Unbalanced TeX braces")
    if depth:
        raise ValueError("Unbalanced TeX braces")

    DESTINATION.write_text(page)
    print(json.dumps({
        "draft": str(DESTINATION),
        "final_gate": args.final,
        "viewed": len(viewed),
        "observations": len(observations),
        "applied_amendment_observations": applied,
        "handled_observations": sorted(handled),
        "pending_observations": sorted(expected - set(observations)),
    }))


if __name__ == "__main__":
    main()
