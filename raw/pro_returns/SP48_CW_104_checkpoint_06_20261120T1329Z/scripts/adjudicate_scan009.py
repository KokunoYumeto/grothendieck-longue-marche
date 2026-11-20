#!/usr/bin/env python3
"""Assemble scan009 from C using the main reader's recorded choices only.

This helper reads text records only. It never opens an image, compiles TeX,
checks mathematics, or writes an authoritative page or cumulative record.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
RECORD = PROJECT / "records" / "scan009"
SOURCE = PROJECT.parent / "reader_inputs" / "scan009" / "C.tex"
OBSERVATIONS = RECORD / "main_observations.md"
CROP_PLAN = RECORD / "main_crop_plan.json"
DRAFT = RECORD / "page_draft.tex"

# Filled only after the main reader records and communicates the choices.
# Each numbered observation must have its own replacements and/or retained
# text assertions. An empty mapping intentionally cannot pass --final.
CHOICES: dict[int, dict[str, list]] = {
    1: {"retain": [
        r"i.e. on a, pour \(\deleted{x}\xi\in J_n(n')\) i.e. \(x\in J_n,\ \tau_n(x)=n'\)",
    ]},
    2: {
        "replace": [(r"\unsure{plus,|\deleted{plus,}}", "plus,")],
        "retain": [r"\deleted{De} plus, \unsure{fort|faut|fut} encore,"],
    },
    3: {"replace": [
        (r"\unsure{isom|iso}", "isom"),
        (r"Lorsque \(\unsure{n'|n}=n\)", r"Lorsque \(n'=n\)"),
    ], "retain": [r"\inserted{\(u_\xi\) induit un isom}"]},
    4: {
        "replace": [(
            r"encore, \(\underbrace{\text{on a :}}\)",
            r"""encore,
% The brace has a double low notch and a long rising right return.
\(\begin{tikzpicture}[baseline=(ona.base),x=1em,y=1em]
 \node[inner sep=0pt] (ona) at (0,0) {$\text{on a :}$};
 \draw[line width=.35pt] (-1.65,-.30)
  .. controls (-1.15,-.22) and (-.70,-.18) .. (-.56,-.57)
  .. controls (-.49,-.48) and (-.42,-.44) .. (-.32,-.57)
  .. controls (-.20,-.64) and (-.17,-.30) .. (.02,-.26)
  .. controls (.45,-.32) and (1.05,-.18) .. (1.30,-.17)
  .. controls (1.68,-.12) and (1.43,.62) .. (1.72,1.45);
\end{tikzpicture}\)""",
        )],
        "retain": [r"\(J_{n'}\xrightarrow{\overset{u_\xi}{\sim}}(J_n)_{\leq\xi}\)"],
    },
    5: {"retain": [r"on a \(J_{n,n}=\{d_n\}\), et"]},
    6: {"retain": [r"u_{d_n}=\mathrm{id}_{J_n}"]},
    7: {"retain": [r"(J_n)_{n\in\mathbb N}"]},
    8: {"retain": [
        r"(\rho_{n,n'})_{\substack{(n',\deleted{\unsure{n'|m}}n)\in\mathbb N\times\mathbb N\\ n'\leq n}}",
    ]},
    9: {"retain": [
        r"\deleted{à peu de \unsure{chose|choses} près}",
        r"\deleted{essentiellement \unsure{la|le} sous-catégorie pleine}\inserted{la catégorie} \(M\)",
    ]},
    10: {"replace": [(
        r"\deleted{\unsure{il|à}} \unsure{équiv|équiva} près,",
        r"\deleted{il} équiv \unsure{prés|près},",
    )]},
    11: {"retain": [r"\deleted{\unsure{description|descripteur}} \inserted{condition}"]},
    12: {"retain": ["pour composer"]},
    13: {
        "replace": [(r"\unsure{standart|standard}", "standart")],
        "retain": ["les hom ``standart entre les"],
    },
    14: {"retain": [r"entre les \(J_n\), i.e ceux"]},
    15: {"replace": [
        (r"J_{n',\unsure{n|n'}}", r"J_{n',\unsure{n'|n^{4}|n}}"),
        (r"\deleted{\unsure{Donc|Don}}", r"\deleted{Donc}"),
    ], "retain": [r"J_{n',\unsure{n'|n^{4}|n}}\)."]},
    16: {"retain": ["On considère une situation"]},
}
REVIEWED_OBSERVATIONS_SHA256 = ""


def observation_numbers(text: str) -> set[int]:
    return {
        int(match.group(1))
        for match in re.finditer(
            r"^\s*(?:#{1,6}\s*)?(?:Observation\s+)?(\d+)[.) —:-]", text, re.M
        )
    }


def assemble(source: str) -> str:
    page = source
    for number, choice in sorted(CHOICES.items()):
        for before, after in choice.get("replace", []):
            count = page.count(before)
            if count != 1:
                raise ValueError(
                    f"Observation {number}: expected one source span, found {count}"
                )
            page = page.replace(before, after, 1)
        for token in choice.get("retain", []):
            if token not in page:
                raise ValueError(f"Observation {number}: retained span is absent")
    for number, choice in sorted(CHOICES.items()):
        targets = [after for _, after in choice.get("replace", [])]
        targets.extend(choice.get("retain", []))
        if not targets:
            raise ValueError(f"Observation {number}: no implementation assertion")
        for token in targets:
            if token not in page:
                raise ValueError(f"Observation {number}: selected span is absent")
    return page


def final_gate() -> None:
    if not OBSERVATIONS.is_file() or not CROP_PLAN.is_file():
        raise ValueError("Main observations and crop plan must both be saved")
    raw = OBSERVATIONS.read_bytes()
    numbers = observation_numbers(raw.decode("utf-8"))
    if not numbers or numbers != set(CHOICES):
        raise ValueError(
            f"Observation coverage differs: main={sorted(numbers)}, "
            f"implemented={sorted(CHOICES)}"
        )
    if not REVIEWED_OBSERVATIONS_SHA256 or hashlib.sha256(raw).hexdigest() != REVIEWED_OBSERVATIONS_SHA256:
        raise ValueError("Main observations changed or have not yet been bound to choices")
    plan = json.loads(CROP_PLAN.read_text(encoding="utf-8"))
    crops = plan["crops"] if isinstance(plan, dict) else plan
    if not isinstance(crops, list) or not crops:
        raise ValueError("Crop plan has no crop list")
    planned = {crop["number"] for crop in crops}
    if planned != numbers:
        raise ValueError("Every planned crop must have its numbered main observation")
    unviewed = [crop["number"] for crop in crops if crop.get("viewed") is not True]
    if unviewed:
        raise ValueError(f"Planned crops not recorded as viewed: {unviewed}")


def structural_check(page: str) -> None:
    if not page.startswith("\\scanpage{9}\n\\mspage{2}\n"):
        raise ValueError("Wrong selected-page or manuscript-folio header")
    if page.count("\\scanpage{") != 1 or "% archive sheet number: 8" not in page:
        raise ValueError("Page or archive marker is missing or duplicated")
    if re.search(r"\\(?:newcommand|renewcommand|providecommand|def|input|include|documentclass|usepackage)\b", page):
        raise ValueError("Draft must use the supplied preamble without new macros or inputs")
    plain = re.sub(r"(?<!\\)%[^\n]*", "", page)
    depth = 0
    for char in re.findall(r"(?<!\\)[{}]", plain):
        depth += 1 if char == "{" else -1
        if depth < 0:
            raise ValueError("Unbalanced closing TeX brace")
    if depth:
        raise ValueError("Unbalanced TeX braces")
    stack: list[str] = []
    for kind, name in re.findall(r"\\(begin|end)\{([^}]+)\}", plain):
        if kind == "begin":
            stack.append(name)
        elif not stack or stack.pop() != name:
            raise ValueError("Unbalanced TeX environments")
    if stack:
        raise ValueError("Unclosed TeX environment")
    for start, end in ((r"\[", r"\]"), (r"\(", r"\)")):
        opening = re.findall(r"(?<!\\)" + re.escape(start), plain)
        closing = re.findall(r"(?<!\\)" + re.escape(end), plain)
        if len(opening) != len(closing):
            raise ValueError("Unbalanced math delimiters")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final", action="store_true", help="Require all main choices and planned crop views")
    args = parser.parse_args()
    try:
        if args.final:
            final_gate()
        page = assemble(SOURCE.read_text(encoding="utf-8"))
        structural_check(page)
        DRAFT.write_text(page, encoding="utf-8")
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"scan009 assembly blocked: {error}\n")
    label = "All main choices applied" if args.final else "Provisional C-based draft"
    print(f"{label}: {DRAFT}")


if __name__ == "__main__":
    main()
