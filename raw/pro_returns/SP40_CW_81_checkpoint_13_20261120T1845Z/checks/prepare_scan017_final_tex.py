#!/usr/bin/env python3
"""Source-only preparation and later root-selected assembly of scan017.

The preparatory catalog contains alternatives, not ink selections.  Final draft
generation stays disabled until root has selected every disputed local source.
This script never reads images, invokes TeX, evaluates mathematical claims, or
changes a reader return, approved page, or record.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
CHECKS = ROOT / "out/checks"
DRAFT = CHECKS / "scan017_final_draft.tex"
MAP = CHECKS / "scan017_final_source_map.json"
AUDIT = CHECKS / "scan017_tex_assembly_audit.json"
CATALOG = CHECKS / "scan017_assembly_candidates.json"
JOURNAL = CHECKS / "scan017_main_decisions.md"
SOURCES = {r: ROOT / f"out/readers/017/{r}/reading.tex" for r in "ABC"}
SOURCES["packet_C"] = ROOT / "packets/017/C.tex"
SOURCES["packet_H"] = ROOT / "packets/017/H.tex"
SOURCES["packet_C_doubts"] = ROOT / "packets/017/C_doubts.txt"
SOURCES["root"] = JOURNAL
TEXT = {r: p.read_text(encoding="utf-8") for r, p in SOURCES.items()}
ROOT_SELECTIONS_COMPLETE = True
SOURCE_SYNC_PASS = 2
COMMENT_REPAIR = {
    "previous_draft_sha256_utf8": "07d9b01084b6738be8bf92b86d11fcfaa6ea2fdf64215d9e4134fdaa1983402f",
    "old_literal": "primary literal retraced cup, alternative amalg.",
    "new_literal": "literal retraced cup; source alternative amalg is retained in the decision record.",
    "reason": "Root's complete selected-body read found one stale explanatory G01 comment after resolving the join; root authorized this exact comment-only repair.",
}
BLOCKS: list[dict] = []
COVERAGE: list[dict] = []
DECISION_COVERAGE: list[dict] = []


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def position(text: str, offset: int) -> dict:
    previous = text.rfind("\n", 0, offset)
    return {"line": text.count("\n", 0, offset) + 1,
            "column_zero_based": offset - previous - 1}


def span(text: str, start: int, end: int) -> dict:
    literal = text[start:end]
    return {
        "character_start": start,
        "character_end_exclusive": end,
        "offset_convention": "zero-based Unicode code-point offsets in UTF-8 decoded file; end-exclusive",
        "start": position(text, start),
        "end_exclusive": position(text, end),
        "covering_lines_inclusive": [position(text, start)["line"],
                                     position(text, max(start, end - 1))["line"]],
        "literal_tex": literal,
        "literal_sha256_utf8": sha(literal),
    }


def unique_at(text: str, literal: str, occurrence: int | None = None) -> int:
    offsets = [m.start() for m in re.finditer(re.escape(literal), text)]
    if occurrence is None:
        if len(offsets) != 1:
            raise ValueError(f"Expected one occurrence, found {len(offsets)}: {literal!r}")
        return offsets[0]
    if occurrence < 1 or occurrence > len(offsets):
        raise ValueError(f"Unavailable occurrence {occurrence}: {literal!r}")
    return offsets[occurrence - 1]


def reference(reader: str, literal: str, purpose: str,
              occurrence: int | None = None) -> dict:
    text = TEXT[reader]
    start = unique_at(text, literal, occurrence)
    return {
        "reader": reader,
        "file": str(SOURCES[reader].relative_to(ROOT)),
        "file_sha256_utf8": sha(text),
        "purpose": purpose,
        **span(text, start, start + len(literal)),
    }


def part(reader: str, start: str | None, end: str | None,
         start_occurrence: int | None = None) -> tuple[str, int, int]:
    text = TEXT[reader]
    begin = 0 if start is None else unique_at(text, start, start_occurrence)
    finish = len(text) if end is None else text.index(end, begin + len(start or ""))
    return text[begin:finish], begin, finish


def add_block(block_id: str, reader: str, start: str | None, end: str | None,
              decision_ids: list[str], inventory_ids: list[str],
              components: list[str], changes: list[tuple[str, str, str]] | None = None,
              additional_sources: list[dict] | None = None,
              coordinate_map: dict | None = None,
              selected_paths: list[tuple[str, str, str]] | None = None,
              start_occurrence: int | None = None) -> None:
    original, first, last = part(reader, start, end, start_occurrence)
    emitted = original
    transformations = []
    for old, new, reason in changes or []:
        at = unique_at(emitted, old)
        transformations.append({
            "description": reason,
            "before_block_character_start": at,
            "before_block_character_end_exclusive": at + len(old),
            "old_literal_tex": old,
            "new_literal_tex": new,
            "old_sha256_utf8": sha(old),
            "new_sha256_utf8": sha(new),
        })
        emitted = emitted[:at] + new + emitted[at + len(old):]
    if selected_paths is None:
        selected_paths = [(reader, match.group(), "selected literal graphical command")
                          for match in re.finditer(r"\\(?:draw|fill)\b[^;]*;", original)]
    paths = [reference(who, literal, purpose)
             for who, literal, purpose in selected_paths]
    BLOCKS.append({
        "id": block_id,
        "decision_ids": decision_ids,
        "inventory_ids": inventory_ids,
        "components": components,
        "source": {
            "reader": reader,
            "file": str(SOURCES[reader].relative_to(ROOT)),
            "file_sha256_utf8": sha(TEXT[reader]),
            **span(TEXT[reader], first, last),
        },
        "emitted_literal_tex": emitted,
        "transformations": transformations,
        "additional_selected_sources": additional_sources or [],
        "coordinate_map": coordinate_map,
        "literal_path_sources": paths,
    })


def cover(inventory_id: str, block_id: str, literal: str | None = None,
          occurrence: int | None = None, note: str | None = None) -> None:
    COVERAGE.append({"inventory_id": inventory_id, "block_id": block_id,
                     "literal": literal, "occurrence": occurrence, "note": note})


def decision(decision_id: str, block_id: str, literal: str | None = None,
             occurrence: int | None = None, note: str | None = None) -> None:
    DECISION_COVERAGE.append({"decision_id": decision_id, "block_id": block_id,
                              "literal": literal, "occurrence": occurrence, "note": note})


def assemble_root_choices() -> None:
    add_block(
        "opening", "B", None, "\\[\n\\begin{aligned}",
        ["017-D01a", "017-D01b", "017-D01c", "017-H01", "017-H02", "017-H03", "017-D02"],
        ["017-I01", "017-I02", "017-I03", "017-I04", "017-I05"],
        ["complete heading and opening paragraph", "B subject and verb qualifications",
         "root-selected firm rare", "complete raised on ait and si complement",
         "B/C qualified cancelled trouve"],
        changes=[
            (r"\unsure{rare|dense}", "rare", "Root section01 resolves only the adjective, using A/C's firm rare."),
        ],
        additional_sources=[
            reference("A", "rare", "Root section01 selected firm adjective"),
            reference("C", "rare", "Independent identical firm adjective"),
        ],
    )
    cover("017-I01", "opening", r"\uline{Cas particuliers}")
    cover("017-I02", "opening", r"Supposons que $\forall i\in I$,")
    cover("017-I02", "opening", r"(si $\Sigma_i^+\ \Sigma_i^-$ sont les deux comp. conn. de $X\setminus\Sigma_i$)")
    cancelled_clause = r"\deleted{$\unsure{E_i|\Sigma_i}$ \unsure{est|soit} rare dans $X$.}"
    cover("017-I03", "opening", cancelled_clause)
    cover("017-I04", "opening", r"\inserted{on ait}")
    cover("017-I05", "opening", r"\deleted{Alors on \unsure{trouve} que}")
    for ident, literal in [
        ("017-D01a", r"\unsure{E_i|\Sigma_i}"),
        ("017-D01b", r"\unsure{est|soit}"),
        ("017-D01c", "rare"),
        ("017-H01", "(si"),
        ("017-H02", r"dans $X$.}"),
        ("017-H03", r"\inserted{on ait}"),
        ("017-D02", r"\deleted{Alors on \unsure{trouve} que}"),
    ]:
        decision(ident, "opening", literal)

    add_block(
        "upper_equalities", "C", "\\[\n\\begin{aligned}", "Alors je dis qu'on a",
        ["017-H04", "017-S01", "017-S02", "017-G13", "017-P01"],
        ["017-I06", "017-I39"],
        ["complete two-row signed closure equalities", "first endpoint without comma",
         "complete C M01 point/period qualification and original hspace"],
        coordinate_map={
            "M01_source_origin": [1172, 557],
            "M01_path_to_source": "(x,y) -> (x+1172,y+557)",
            "M01_tikz_units_cm": [0.01, -0.01],
            "M01_fixed_rectangle": [[0, 0], [7, 7]],
            "M01_baseline": "monebase=(0,6)",
            "placement": r"original \hspace{1.5cm} after the second E_i; no second endpoint glyph",
            "qualification": "original local literal triangular graphic with period alternative",
        },
    )
    cover("017-I06", "upper_equalities")
    m01, _, _ = part("C", r"\hspace{1.5cm}", r"\end{aligned}")
    cover("017-I39", "upper_equalities", m01)
    decision("017-G13", "upper_equalities", m01)
    decision("017-H04", "upper_equalities", r"\overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i\\",
             note="Root section03 selects this complete first-row endpoint without a comma.")
    decision("017-P01", "upper_equalities", note="The complete source aligned display preserves the selected two-row layout; noncount layout audit.")

    add_block(
        "third_equality", "C", "Alors je dis qu'on a", "% G02:",
        ["017-H05", "017-S03", "017-D03", "017-D03-shape"],
        ["017-I07", "017-I08", "017-I26"],
        ["complete prose qu'on a and Sigma12 equality", "C G01 exact three draw commands",
         "root-selected resolved retraced-cup state; outer unsure/amalg alternative removed"],
        changes=[
            (r"\mathbin{\unsure{\begin{tikzpicture}", r"\mathbin{\begin{tikzpicture}",
             "Root section05 removes only the outer interpretation qualification from C G01."),
            (r"\end{tikzpicture}|\amalg}}E_1", r"\end{tikzpicture}}E_1",
             "Root section05 removes C G01's unselected amalg alternative, preserving mathbin and the complete picture."),
            (COMMENT_REPAIR["old_literal"], COMMENT_REPAIR["new_literal"],
             "Root's subsequent complete draft read requested this explanatory comment-only repair; selected manuscript text and paths stay unchanged."),
        ],
        coordinate_map={
            "G01_source_origin": [947, 783],
            "G01_path_to_source": "(x,y) -> (x+947,y+783)",
            "G01_tikz_units_cm": [0.01, -0.01],
            "G01_fixed_rectangle": [[0, 0], [33, 32]],
            "G01_baseline": "joinbase=(0,29)",
            "components": "three original literal paths: separate left stem, inner return, outer return",
        },
    )
    cover("017-I07", "third_equality", "Alors je dis qu'on a")
    third_display = BLOCKS[-1]["emitted_literal_tex"]
    third_display = third_display[third_display.index(r"\["):]
    cover("017-I08", "third_equality", third_display)
    g01, _, _ = part("C", r"\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(joinbase)]", r"\end{tikzpicture}")
    g01 += r"\end{tikzpicture}"
    cover("017-I26", "third_equality", r"\mathbin{" + g01 + "}")
    decision("017-H05", "third_equality", "Alors je dis qu'on a")
    decision("017-D03", "third_equality", r"\mathbin{" + g01 + "}")
    decision("017-D03-shape", "third_equality", g01,
             note="The exact three C literal draw commands remain together in their original picture.")

    add_block(
        "separator", "C", "% G02:", "% slanted",
        ["017-G02"], ["017-I27"],
        ["C complete G02 figure", "one literal curved rule", "wide fixed placement rectangle"],
        coordinate_map={
            "G02_source_origin": [300, 887],
            "G02_path_to_source": "(x,y) -> (x+300,y+887)",
            "G02_tikz_units_cm": [0.01, -0.01],
            "G02_fixed_rectangle": [[0, 0], [1300, 25]],
            "placement": "C's complete original figure and wide rectangle retained",
        },
    )
    cover("017-I27", "separator")
    decision("017-G02", "separator")

    add_block(
        "margin_and_soit", "A", "% slanted", "Considerons la partition",
        ["017-H06", "017-D04a", "017-D04b", "017-G12", "017-H-MARGIN-ILL"],
        ["017-I09", "017-I10", "017-I28", "017-I11", "017-I12"],
        ["complete A slanted note with introduire and qualified Pi/Sigma",
         "complete cancelled Supposons and Soit line",
         "B wedge source proposal represented through the selected ordinary Soit letter once"],
    )
    margin = r"\margin{introduire la partition $\unsure{\Pi|\pi}_j=\{\deleted{\unsure{\Sigma}}E_j,\Sigma_j^+,\Sigma_j^-\}$}"
    marginal_predecessor = r"\deleted{\unsure{\Sigma}}E_j"
    soit = r"Soit $J\subset I$ tel que $I=J\amalg\{i\}$."
    cover("017-I09", "margin_and_soit", margin)
    cover("017-I10", "margin_and_soit", marginal_predecessor)
    cover("017-I28", "margin_and_soit", "Soit",
          note="Root section07 identifies B's proposed separate wedge as a component of this existing S; it is represented once through Soit.")
    cover("017-I11", "margin_and_soit", r"\deleted{Supposons}")
    cover("017-I12", "margin_and_soit", soit)
    decision("017-H06", "margin_and_soit", "introduire")
    decision("017-D04a", "margin_and_soit", r"\unsure{\Pi|\pi}_j")
    decision("017-D04b", "margin_and_soit", marginal_predecessor)
    decision("017-G12", "margin_and_soit", "Soit",
             note="Selected attachment is the existing S in Soit; no separate B wedge path is emitted.")
    decision("017-H-MARGIN-ILL", "margin_and_soit", margin,
             note="One H marginal parent attaches to the selected complete note and its predecessor; the exact intended referent of H's terminal placeholder remains unspecified.")
    BLOCKS[-1]["unselected_source_proposals"] = [
        reference("B", r"\fill (0,0) -- (0.4,3) -- (2.2,2) -- cycle;",
                  "Root section07 attaches this reported component to the S of Soit; no independent margin glyph selected"),
    ]

    add_block(
        "main_opening", "A", "Considerons la partition", "% G04:",
        ["017-N03", "017-G03", "017-D05", "017-N04", "017-D07a", "017-D06a", "017-D06b"],
        ["017-I13", "017-I14", "017-I29", "017-I15", "017-I16", "017-I17"],
        ["A complete opening prose with unaccented Considerons and both definie forms",
         "A complete G03 insertion/guide/de group", "C qualified main E predecessor",
         "C complete et state qualification", "root-composed lower-case-primary intersection case qualification"],
        changes=[
            (r"$\deleted{\Sigma}E_j$", r"$\deleted{\unsure{\Sigma}}E_j$",
             "Root section11 selects C's qualified predecessor while preserving the live E_j."),
            (r"\deleted{et}", r"\unsure{\deleted{et}|et}",
             "Root section12 selects C's complete cancelled/live et state qualification."),
            (r"\unsure{Intersection|intersection}", r"\unsure{intersection|Intersection}",
             "Root section12 retains A's two cases in the explicitly selected lower-case-primary order."),
        ],
        additional_sources=[
            reference("C", r"$\deleted{\unsure{\Sigma}}E_j$", "Root section11 selected qualified main predecessor"),
            reference("C", r"\unsure{\deleted{et}|et}", "Root section12 selected complete et state"),
            reference("root", r"\unsure{intersection|Intersection}", "Root section12 exact composed case qualification"),
        ],
        coordinate_map={
            "G03_source_origin": [1215, 1100],
            "G03_path_to_source": "(x,y) -> (x+1215,y+1100)",
            "G03_tikz_units_cm": [0.008, -0.008],
            "G03_fixed_rectangle": [[0, 0], [175, 135]],
            "G03_baseline": "pide.base; live de anchor=(105,124)",
            "G03_text_nodes": "original base-west, inner sep=0pt, outer sep=0pt; raised Pi_J at (6,65), de at (105,124)",
            "attachment": "live de occurs in the selected picture; the following X occurs once outside it",
        },
    )
    cover("017-I13", "main_opening")
    cover("017-I14", "main_opening", r"\inserted{$\Pi_J$}")
    g03, _, _ = part("A", "% G03:", "$X$ ")
    cover("017-I29", "main_opening", g03)
    cover("017-I15", "main_opening", r"\deleted{definie}")
    cover("017-I16", "main_opening", r"$\deleted{\unsure{\Sigma}}E_j$")
    cover("017-I17", "main_opening", r"\unsure{\deleted{et}|et}")
    for ident, literal in [
        ("017-N03", "Considerons"),
        ("017-G03", g03),
        ("017-D05", r"\deleted{definie}"),
        ("017-N04", "definie par les"),
        ("017-D07a", r"$\deleted{\unsure{\Sigma}}E_j$"),
        ("017-D06a", r"\unsure{\deleted{et}|et}"),
        ("017-D06b", r"\unsure{intersection|Intersection}"),
    ]:
        decision(ident, "main_opening", literal)

    add_block(
        "ternaires_and_later_sign", "A", "% G04:", "\\[\nX=E_j",
        ["017-G04", "017-N05", "017-D07b", "017-H-LATER-ILL"],
        ["017-I13", "017-I18", "017-I30", "017-I19"],
        ["A complete G04 inserted ternaires/guide/de group", "one following X and quantified continuation",
         "A/B unaccented plural definies", "B complete later-sign alternatives"],
        changes=[
            (r"\deleted{$\unsure{\in|E}$}", r"$\unsure{\deleted{\in}|\deleted{E}|\notin}$",
             "Root section15 selects B's complete later-sign glyph/state alternatives as one physical cluster."),
        ],
        additional_sources=[
            reference("B", r"$\unsure{\deleted{\in}|\deleted{E}|\notin}$", "Root section15 selected complete later-sign state"),
        ],
        coordinate_map={
            "G04_source_origin": [970, 1345],
            "G04_path_to_source": "(x,y) -> (x+970,y+1345)",
            "G04_tikz_units_cm": [0.0075, -0.0075],
            "G04_fixed_rectangle": [[0, 0], [335, 135]],
            "G04_baseline": "terde.base; live de anchor=(270,118)",
            "G04_text_nodes": "original base-west, inner sep=0pt, outer sep=0pt; insertion at (0,57), de at (270,118)",
            "attachment": "de occurs in the selected picture; X follows once outside the group",
            "path": "one selected A literal draw command retains both arms and the low meeting point",
        },
    )
    cover("017-I13", "ternaires_and_later_sign")
    cover("017-I18", "ternaires_and_later_sign", r"\inserted{ternaires $\Pi_j$}")
    g04, _, _ = part("A", "% G04:", "$X$ ")
    cover("017-I30", "ternaires_and_later_sign", g04)
    later_sign = r"$\unsure{\deleted{\in}|\deleted{E}|\notin}$"
    cover("017-I19", "ternaires_and_later_sign", later_sign)
    decision("017-G04", "ternaires_and_later_sign", g04)
    decision("017-N05", "ternaires_and_later_sign", "definies par les")
    decision("017-D07b", "ternaires_and_later_sign", later_sign)
    decision("017-H-LATER-ILL", "ternaires_and_later_sign", later_sign,
             note="One H main-text ill parent; the complete selected alternatives remain in this one final span.")

    add_block(
        "coproduct_and_right_pair", "C", "\\[\nX=E_j", "-- c'est aussi la partition",
        ["017-G05", "017-G05-index", "017-G11", "017-G11-upper", "017-G11-lower"],
        ["017-I20", "017-I31", "017-I32"],
        ["complete C indexed coproduct display", "complete C M03 Sigma/dotless-j/alpha/point arrangement",
         "complete C M02a/M02b pair with original hspace and raisebox"],
        coordinate_map={
            "M03_outer_source_origin": [1145, 1624],
            "M03_outer_path_to_source": "(x,y) -> (x+1145,y+1624)",
            "M03_tikz_units_cm": [0.01, -0.01],
            "M03_outer_fixed_rectangle": [[0, 0], [110, 88]],
            "M03_outer_baseline": "sigbase=(0,70)",
            "M03_formula_node": "original base-west, zero inner/outer separation at (0,70); Sigma with dotless j and alpha",
            "M03_inner_parent_anchor": [47, 3],
            "M03_inner_source_origin": [1192, 1627],
            "M03_inner_path_to_source": "(x,y) -> (x+1192,y+1627)",
            "M03_inner_wrapper": "original base-west, zero inner/outer separation; mthreebase=(0,0); rectangle (0,0)-(7,7)",
            "M02_source_origin": [1568, 1738],
            "M02_path_to_source": "(x,y) -> (x+1568,y+1738)",
            "M02_tikz_units_cm": [0.01, -0.01],
            "M02_fixed_rectangle": [[0, 0], [13, 17]],
            "M02_baseline": "mtwobase=(0,0)",
            "M02_placement": r"original \hspace{3cm} and \raisebox{-0.45cm}; both literal fills in one local unsure group",
            "single_point_policy": "The selected complete M03 contains dotless j and one separate qualified fill; no regular dotted-j or A prime/dot candidate is added.",
        },
    )
    cover("017-I20", "coproduct_and_right_pair")
    m03, _, _ = part("C", "% M03:", r"\hspace{3cm}")
    m02, _, _ = part("C", r"\hspace{3cm}", "\\]\n\n-- c'est")
    upper_fill = r"\fill (8,3) -- (10,0) -- (12,3) -- (11,5) -- (8,6) -- cycle;"
    lower_fill = r"\fill (1,11) -- (4,10) -- (6,12) -- (3,15) -- (1,14) -- cycle;"
    index_node = r"\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,70) {$\Sigma_{\jmath}^{\alpha}$};"
    cover("017-I31", "coproduct_and_right_pair", m03)
    cover("017-I32", "coproduct_and_right_pair", m02)
    decision("017-G05", "coproduct_and_right_pair", m03,
             note="Root section16 selects the complete dotless-index/alpha/qualified-point arrangement; the point's attachment remains open.")
    decision("017-G05-index", "coproduct_and_right_pair", index_node)
    decision("017-G11", "coproduct_and_right_pair", m02)
    decision("017-G11-upper", "coproduct_and_right_pair", upper_fill)
    decision("017-G11-lower", "coproduct_and_right_pair", lower_fill)

    add_block(
        "lower_opening_and_point", "B", "-- c'est aussi la partition", "% G07:",
        ["017-N06", "017-G06"], ["017-I21", "017-I33"],
        ["complete lower opening prose with unaccented definie", "B G06 exact qualified mathord/fill",
         "first ordinary indexed bigcup and its E_j", "complete en les E_j, et la partition continuation"],
        coordinate_map={
            "G06_source_origin": [734, 1902],
            "G06_full_source_scope_shift": [-734, -1902],
            "G06_full_source_path_map": "(x,y) -> (x-734,y-1902) in the picture; source path coordinates remain (x,y)",
            "G06_tikz_units_cm": [0.025, -0.025],
            "G06_fixed_rectangle": [[0, 0], [9, 7]],
            "G06_baseline": "baseline=0pt",
            "G06_wrapper": "complete original local unsure/mathord group before the ordinary indexed union",
        },
    )
    cover("017-I21", "lower_opening_and_point")
    baseline_point, _, _ = part("B", r"\unsure{\mathord{\begin{tikzpicture}[x=0.025cm", r"\bigcup")
    cover("017-I33", "lower_opening_and_point", baseline_point)
    decision("017-N06", "lower_opening_and_point", "definie")
    decision("017-G06", "lower_opening_and_point", baseline_point)

    add_block(
        "lower_pi_and_guide", "B", "% G07:", r"$\displaystyle X\setminus",
        ["017-D08a", "017-G07"], ["017-I22", "017-I34"],
        ["B complete G07 raised Pi_J ring/guide/de group", "first local circle/zero qualification"],
        coordinate_map={
            "G07_source_origin": [752, 1973],
            "G07_full_source_scope_shift": [-752, -1973],
            "G07_full_source_path_map": "(x,y) -> (x-752,y-1973) in the picture; source path coordinates remain (x,y)",
            "G07_tikz_units_cm": [0.01, -0.01],
            "G07_fixed_rectangle": [[0, 0], [168, 110]],
            "G07_baseline": "live.base; de anchor=(91,80)",
            "G07_nodes": "original base-west, zero inner/outer separation; insertion at (15,40), de at (91,80)",
            "attachment": "the live de occurs once in the selected group",
        },
    )
    cover("017-I22", "lower_pi_and_guide", r"\inserted{$\Pi_J^{\unsure{\circ|0}}$}")
    cover("017-I34", "lower_pi_and_guide")
    decision("017-D08a", "lower_pi_and_guide", r"\Pi_J^{\unsure{\circ|0}}",
             note="Original R08 first local ring retains its explicit qualification here.")
    decision("017-G07", "lower_pi_and_guide")

    middle_start = r"$\displaystyle X\setminus\mathop{\unsure{\begin{tikzpicture}"
    add_block(
        "middle_union", "C", middle_start, "intersection des partitions binaires",
        ["017-D11", "017-D11-shape", "017-D11-role"], ["017-I35"],
        ["C complete G06 cup/transverse-stroke picture", "original local unsure/mathop wrapper",
         "complete complement, limits and E_j"],
        coordinate_map={
            "G06_source_origin": [1115, 1975],
            "G06_path_to_source": "(x,y) -> (x+1115,y+1975)",
            "G06_tikz_units_cm": [0.01, -0.01],
            "G06_fixed_rectangle": [[0, 0], [70, 62]],
            "G06_baseline": "unionbase=(0,58)",
            "qualification": "selected source unsure wrapper remains local to the full literal union group; the two original draw commands remain unchanged",
        },
    )
    middle_picture, _, _ = part("C", r"\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=(unionbase)]", r"\end{tikzpicture}")
    middle_picture += r"\end{tikzpicture}"
    middle_qualified = r"\mathop{\unsure{" + middle_picture + "}}"
    cover("017-I35", "middle_union", middle_qualified)
    decision("017-D11", "middle_union")
    decision("017-D11-shape", "middle_union", middle_picture)
    decision("017-D11-role", "middle_union", middle_qualified)

    add_block(
        "binary_ring_and_condition", "B", "intersection des partitions binaires", "% G10:",
        ["017-D08b", "017-G09", "017-G09-open"],
        ["017-I21", "017-I23", "017-I36"],
        ["complete binary partition wording", "second ring printed as the first candidate with its independent retained source doubt",
         "B complete G09 condition/induites/guide group"],
        coordinate_map={
            "G09_source_origin": [1234, 2070],
            "G09_full_source_scope_shift": [-1234, -2070],
            "G09_full_source_path_map": "(x,y) -> (x-1234,y-2070) in the picture; source path coordinates remain (x,y)",
            "G09_tikz_units_cm": [0.009, -0.009],
            "G09_fixed_rectangle": [[0, 0], [320, 110]],
            "G09_baseline": "live.base; induites anchor=(50,84)",
            "G09_nodes": "original base-west, zero inner/outer separation; inserted condition at (45,35), induites at (50,84)",
            "attachment": "one continuous selected guide; quantifier parentheses and live induites retained once",
        },
    )
    binary_name = r"intersection des partitions binaires $\Pi_{J,j}^{\circ}$"
    g09, _, _ = part("B", "% G09:", "% G10:")
    cover("017-I21", "binary_ring_and_condition", binary_name)
    cover("017-I23", "binary_ring_and_condition", r"\inserted{$(j\in J)$}")
    cover("017-I36", "binary_ring_and_condition", g09)
    decision("017-D08b", "binary_ring_and_condition", r"\Pi_{J,j}^{\circ}",
             note="Original R08 explicitly includes this second physical ring. Root section25 corrects the wrapper instruction: the first candidate is printed under the first-occurrence convention while this local circle/zero doubt remains retained separately.")
    decision("017-G09", "binary_ring_and_condition", g09)
    decision("017-G09-open", "binary_ring_and_condition", g09,
             note="Root section20 attaches H's extra prose opening-parenthesis interpretation to this continuous guide; the inserted quantifier's own parentheses remain.")

    add_block(
        "u_guide_and_ending", "B", "% G10:", None,
        ["017-D12", "017-D12-final", "017-G10", "017-G10-state", "017-D09", "017-H07", "017-D10", "017-ARCHIVE"],
        ["017-I24", "017-I25", "017-I37", "017-I21", "017-I38"],
        ["B complete G10 raised U/state/guide/sur group", "complete third complement and final prose",
         "qualified final g/j", "one closing parenthesis and period", "firm Pour", "archive numeral comment"],
        coordinate_map={
            "G10_source_origin": [311, 2140],
            "G10_full_source_scope_shift": [-311, -2140],
            "G10_full_source_path_map": "(x,y) -> (x-311,y-2140) in the picture; source path coordinates remain (x,y)",
            "G10_tikz_units_cm": [0.01, -0.01],
            "G10_fixed_rectangle": [[0, 0], [151, 165]],
            "G10_baseline": "live.base; sur anchor=(20,123)",
            "G10_nodes": "original base-west, zero inner/outer separation; raised U at (56,75), sur at (20,123)",
            "attachment": "complete original descending guide and one live sur; the following X complement remains outside the group",
            "subscript": "all three complete selected states retained; no independent cancellation path or arrowhead added",
        },
    )
    u_insert = r"\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}"
    u_state = r"\unsure{\deleted{J}J|\deleted{j}J|J}"
    g10, _, _ = part("B", "% G10:", r"$\displaystyle X\setminus")
    ending = r"$\displaystyle X\setminus\bigcup_{j\in J}E_j$ par les $\Pi_j$ $(\unsure{g|j}\in J)$. Pour"
    cover("017-I24", "u_guide_and_ending", u_insert)
    cover("017-I25", "u_guide_and_ending", u_state)
    cover("017-I37", "u_guide_and_ending", g10)
    cover("017-I21", "u_guide_and_ending", ending)
    cover("017-I38", "u_guide_and_ending", "% archive sheet number: 16")
    decision("017-D12", "u_guide_and_ending", u_state)
    decision("017-D12-final", "u_guide_and_ending", u_state,
             note="Root section21 confirms the final capital J component across the complete explicitly retained state alternatives.")
    decision("017-G10", "u_guide_and_ending", g10)
    decision("017-G10-state", "u_guide_and_ending", u_insert)
    decision("017-D09", "u_guide_and_ending", r"\unsure{g|j}")
    decision("017-H07", "u_guide_and_ending", r"$(\unsure{g|j}\in J)$. Pour",
             note="Root section22 retains the single closing parenthesis and separate period.")
    decision("017-D10", "u_guide_and_ending", "Pour")
    decision("017-ARCHIVE", "u_guide_and_ending", "% archive sheet number: 16")


def resolved_coverage(items: list[dict], draft: str, blocks: dict[str, dict]) -> list[dict]:
    result = []
    for item in items:
        block = blocks[item["block_id"]]
        text = block["emitted_literal_tex"]
        literal = item["literal"]
        local_start = 0 if literal is None else unique_at(text, literal, item["occurrence"])
        length = len(text) if literal is None else len(literal)
        absolute_start = block["draft"]["character_start"] + local_start
        result.append({
            **{k: v for k, v in item.items() if k not in ("literal", "occurrence")},
            "draft": span(draft, absolute_start, absolute_start + length),
        })
    return result


def macro_group_spans(text: str, command: str) -> list[tuple[int, int]]:
    result = []
    for match in re.finditer(re.escape(command) + r"\{", text):
        depth = 1
        cursor = match.end()
        while cursor < len(text) and depth:
            if text[cursor] in "{}" and text[cursor - 1] != "\\":
                depth += 1 if text[cursor] == "{" else -1
            cursor += 1
        if depth:
            raise ValueError(f"Unclosed argument: {command}")
        result.append((match.start(), cursor))
    return result


def overbar_coverage(draft: str) -> list[dict]:
    final = macro_group_spans(draft, r"\overline")
    witness = macro_group_spans(TEXT["packet_C"], r"\overline")[:3]
    if len(final) != 3 or len(witness) != 3:
        raise ValueError("The three selected Sigma closure-bar occurrences must attach separately.")
    return [{
        "decision_id": f"017-S{i:02d}",
        "source": {"file": "packets/017/C.tex",
                   "file_sha256_utf8": sha(TEXT["packet_C"]),
                   **span(TEXT["packet_C"], *source_span)},
        "draft": span(draft, *final_span),
        "scope": "source-command position and its literal argument only; current-witness confirmation",
    } for i, (final_span, source_span) in enumerate(zip(final, witness), 1)]


def original_doubt_scope(decisions: list[dict]) -> list[dict]:
    original_map = json.loads((CHECKS / "scan017_source_map.json").read_text(encoding="utf-8"))
    source_rows = original_map["categories"]["Doubtful readings"]
    primary_ids = [
        ["017-D01a", "017-D01b", "017-D01c"], ["017-D02"], ["017-D03"],
        ["017-D04a", "017-D04b"], ["017-D05"], ["017-D06a", "017-D06b"],
        ["017-D07a", "017-D07b"], ["017-D08a", "017-D08b"], ["017-D09"],
        ["017-D10"], ["017-D11"], ["017-D12"],
    ]
    result = []
    for original, identifiers in zip(source_rows, primary_ids):
        if len(original["local_loci"]) != len(identifiers):
            raise ValueError("Original source-row/local-locus mapping changed.")
        result.append({
            "source_row": original["source_row"],
            "source": reference("packet_C_doubts", original["literal"], "Exact original C doubtful-reading row; original row identity retained"),
            "local_parts": [
                {"decision_id": ident, "original_local_scope": locus,
                 "final_source_attachments": [row for row in decisions if row["decision_id"] == ident]}
                for ident, locus in zip(identifiers, original["local_loci"])
            ],
        })
    return result


def recurring_ring_scope(decisions: list[dict]) -> dict:
    return {
        "original_source_row": 8,
        "policy": "Root source-only section25 applies first-occurrence qualification: both local circle/zero doubts remain independently recorded; only the first carries the printed unsure wrapper.",
        "local_parts": [
            {"decision_id": "017-D08a", "location": "raised inserted Pi_J",
             "source_C_tex": reference("packet_C", r"\Pi_J^{\unsure{\circ|0}}", "Original first ring and qualification"),
             "final_source_attachments": [row for row in decisions if row["decision_id"] == "017-D08a"],
             "retained_local_candidates": [r"\circ", "0"], "printed_qualification": True},
            {"decision_id": "017-D08b", "location": "binary Pi_J,j name",
             "source_C_tex": reference("packet_C", r"\Pi_{J,j}^{\circ}", "Original second ring; its uncertainty is explicit in original C row8"),
             "final_source_attachments": [row for row in decisions if row["decision_id"] == "017-D08b"],
             "retained_local_candidates": [r"\circ", "0"], "printed_qualification": False},
        ],
    }


def journal_sections() -> dict[int, dict]:
    journal = TEXT["root"]
    matches = list(re.finditer(r"^## (\d+) —[^\n]*", journal, re.M))
    result = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(journal)
        result[int(match.group(1))] = {
            "reader": "root", "file": str(JOURNAL.relative_to(ROOT)),
            "file_sha256_utf8": sha(journal),
            **span(journal, match.start(), end),
        }
    return result


def prepare_catalog() -> None:
    """Record literal alternatives and an ordered structural plan; make no selection."""
    rows = []
    for reader in "ABC":
        text = TEXT[reader]
        rows.append({
            "reader": reader,
            "file": str(SOURCES[reader].relative_to(ROOT)),
            "file_sha256_utf8": sha(text),
            "complete_source": span(text, 0, len(text)),
            "literal_graphical_commands": [span(text, m.start(), m.end())
                                            for m in re.finditer(r"\\(?:draw|fill)\b[^;]*;", text)],
            "group_comments": [span(text, m.start(), m.end())
                               for m in re.finditer(r"^% (?:G|M)\d+[^\n]*", text, re.M)],
        })
    common_literals = [
        r"\scanpage{17}" + "\n" + r"\uline{Cas particuliers}",
        r"Supposons que $\forall i\in I$,",
        r"\inserted{on ait} (si $\Sigma_i^+\ \Sigma_i^-$ sont les deux comp. conn. de $X\setminus\Sigma_i$)",
        r"\overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i\\",
        r"\overline{\Sigma_i^-} &= \Sigma_i^-\cup E_i",
        "Alors je dis qu'on a",
        r"\overline{\Sigma_{12}}=\Sigma_{12}",
        r"E_1\cup E_2",
        r"\normalmarginpar" + "\n" + r"\deleted{Supposons}",
        r"Soit $J\subset I$ tel que $I=J\amalg\{i\}$.",
        r"\inserted{$\Pi_J$}",
        r"\inserted{ternaires $\Pi_j$}",
        r"X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}",
        r"\inserted{$\Pi_J^{\unsure{\circ|0}}$}",
        r"intersection des partitions binaires $\Pi_{J,j}^{\circ}$",
        r"\inserted{$(j\in J)$}",
        r"\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}",
        r"$\displaystyle X\setminus\bigcup_{j\in J}E_j$ par les $\Pi_j$ $(\unsure{g|j}\in J)$. Pour",
        "% archive sheet number: 16",
    ]
    common = [{"literal_tex": literal,
               "literal_sha256_utf8": sha(literal),
               "sources": [reference(r, literal, "complete identical source string; no ink selection")
                           for r in "ABC"]}
              for literal in common_literals]
    skeleton = [
        {"slot": "heading", "scope": "scan marker and underlined heading"},
        {"slot": "opening", "scope": "complete Supposons clause; cancelled R01 subject/verb/adjective; raised on ait; si complement and punctuation"},
        {"slot": "upper_equalities", "scope": "cancelled Alors on trouve que; two complete signed closure rows; first endpoint and selected second endpoint representation"},
        {"slot": "sigma12_equality", "scope": "Alors je dis qu'on a; complete closure equality with selected first-join body and qualification; final ordinary cup"},
        {"slot": "separator", "scope": "one selected complete rule source group"},
        {"slot": "margin", "scope": "slanted note wording, partition name and predecessor; explicit selection for the proposed terminal wedge/attachment"},
        {"slot": "soit", "scope": "cancelled Supposons; complete Soit J subset I line"},
        {"slot": "main_opening", "scope": "local Considerons accent; upper Pi_J group; de X once; cancelled and live definie accents; first E predecessor; et glyph/state; live intersection"},
        {"slot": "ternaires", "scope": "selected whole insertion group; de X once; indexed continuation; local definies accent; later sign/state; final quantified parenthesis"},
        {"slot": "coproduct", "scope": "complete indexed partition display; entire selected Sigma/index/alpha/extra-mark cluster"},
        {"slot": "right_marks", "scope": "explicit choice for two detached right shapes and their qualification/placement"},
        {"slot": "lower_opening", "scope": "c'est aussi prose; local definie accent; explicit first-union point selection; first complete indexed union and continuation"},
        {"slot": "lower_pi", "scope": "lower inserted Pi_J ring plus guide; de once; R08 first-ring qualification"},
        {"slot": "middle_union", "scope": "complete complement with selected cup/transverse paths and local qualification; limits and E_j"},
        {"slot": "binary_name", "scope": "intersection des partitions binaires; R08 second-ring local source scope despite first-occurrence macro convention"},
        {"slot": "induites", "scope": "selected inserted quantifier and guide group; induites once; exact absence/presence of separate prose parenthesis"},
        {"slot": "u_sur", "scope": "selected complete U state/guide group; sur once; third complete indexed union and prose"},
        {"slot": "ending", "scope": "last g/j, endpoint parentheses/period, final Pour/Puis, archive comment"},
    ]
    result = {
        "scan": 17,
        "status": "source-only candidate catalog; root ink and group-source selections pending",
        "final_generation_enabled": ROOT_SELECTIONS_COMPLETE,
        "locator_policy": "Exact zero-based Unicode code-point offsets, end-exclusive; file hashes, endpoints, literal text and literal hashes are retained.",
        "sources": rows,
        "identical_common_fragments": common,
        "ordered_structural_skeleton": skeleton,
        "scope_notes": [
            "No candidate is designated the selected final reading or drawing.",
            "All three returned complete TeX bodies are retained exactly in this preparatory source catalog.",
            "Root's explicit selections will control final group bases and every local change.",
            "R08 has two independently documented local ring occurrences; the recurring first-occurrence macro convention does not remove the second local doubt.",
            "C's M03 dotless-index and extra-mark arrangement is one whole candidate cluster; a source fill alone does not select that arrangement.",
            "Ordinary attachment words de, de X, induites and sur must occur once at their chosen groups.",
            "No empty physical line may be introduced inside a display or math environment.",
        ],
        "images_opened": False,
        "compiled": False,
        "rendered": False,
        "mathematical_checks": False,
        "geometric_or_numeric_image_comparison": False,
    }
    CATALOG.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"catalog": str(CATALOG), "selected_final_generated": False,
                      "source_readers": [r["reader"] for r in rows],
                      "common_fragments": len(common), "structural_slots": len(skeleton)},
                     ensure_ascii=False, indent=2))


def structural_source_pass(draft: str) -> dict:
    """One selected-body synchronization, using literal source text only."""
    issues = []
    uncommented = re.sub(r"(?<!\\)%[^\n]*", "", draft)
    depth = 0
    for i, char in enumerate(uncommented):
        if char in "{}" and (i == 0 or uncommented[i - 1] != "\\"):
            depth += 1 if char == "{" else -1
            if depth < 0:
                issues.append("Closing brace precedes its opening brace.")
                break
    if depth != 0:
        issues.append(f"Unbalanced group depth: {depth}")
    stack = []
    for command, name in re.findall(r"\\(begin|end)\{([^}]+)\}", uncommented):
        if command == "begin":
            stack.append(name)
        elif not stack or stack.pop() != name:
            issues.append(f"Environment close mismatch: {name}")
    if stack:
        issues.append(f"Unclosed environments: {stack}")
    if uncommented.count(r"\[") != uncommented.count(r"\]"):
        issues.append("Unpaired display delimiters.")
    if len(re.findall(r"(?<!\\)\$", uncommented)) % 2:
        issues.append("Odd dollar-delimiter count.")
    for match in re.finditer(r"\\\[(.*?)\\\]", draft, re.S):
        if re.search(r"\n[ \t]*\n", match.group(1)):
            issues.append("Empty physical line inside a display.")
    for env in ["aligned", "align", "align*", "gather", "gather*", "equation", "equation*"]:
        pattern = re.escape(r"\begin{" + env + "}") + r"(.*?)" + re.escape(r"\end{" + env + "}")
        for match in re.finditer(pattern, draft, re.S):
            if re.search(r"\n[ \t]*\n", match.group(1)):
                issues.append(f"Empty physical line inside {env}.")
    allowed = set(re.findall(r"\\([A-Za-z]+)", "\n".join(TEXT.values())))
    allowed.update(re.findall(r"\\([A-Za-z]+)", (ROOT / "out/PREAMBLE.tex").read_text()))
    unknown = sorted(set(re.findall(r"\\([A-Za-z]+)", uncommented)) - allowed)
    if unknown:
        issues.append(f"Commands outside supplied source/preamble vocabulary: {unknown}")
    selected_paths = [p["literal_tex"] for b in BLOCKS for p in b["literal_path_sources"]]
    emitted_paths = [m.group() for m in re.finditer(r"\\(?:draw|fill)\b[^;]*;", draft)]
    if selected_paths != emitted_paths:
        issues.append("Selected/emitted literal graphical-command sequence differs.")
    if any(count != 1 for count in Counter(emitted_paths).values()):
        issues.append("A selected literal graphical command has multiple occurrences.")
    for literal, label in [(r"\scanpage{17}", "scan marker"),
                           ("% archive sheet number: 16", "archive comment")]:
        if draft.count(literal) != 1:
            issues.append(f"The {label} does not occur once.")
    record = json.loads((CHECKS / "scan017_record_draft.json").read_text(encoding="utf-8"))
    expected_inventory = {r["element"] for r in record["inventory"]}
    actual_inventory = {r["inventory_id"] for r in COVERAGE}
    if actual_inventory != expected_inventory:
        issues.append(f"Inventory attachment mismatch: {sorted(expected_inventory ^ actual_inventory)}")
    expected_decisions = {r["id"] for r in record["decisions"]}
    actual_decisions = {r["decision_id"] for r in DECISION_COVERAGE} | {"017-S01", "017-S02", "017-S03"}
    if actual_decisions != expected_decisions:
        issues.append(f"Decision attachment mismatch: {sorted(expected_decisions ^ actual_decisions)}")
    for literal in [
        r"\uline{Cas particuliers}",
        r"\inserted{on ait}",
        r"\Sigma_i^+\ \Sigma_i^-",
        r"X\setminus\Sigma_i",
        r"\overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i",
        r"\overline{\Sigma_i^-} &= \Sigma_i^-\cup E_i",
        "Alors je dis qu'on a",
        r"\overline{\Sigma_{12}}=\Sigma_{12}",
        r"E_1\cup E_2",
        r"\deleted{Supposons}",
        r"Soit $J\subset I$ tel que $I=J\amalg\{i\}$.",
        r"\inserted{$\Pi_J$}",
        r"\inserted{ternaires $\Pi_j$}",
        r"X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}",
        r"intersection des partitions binaires $\Pi_{J,j}^{\circ}$",
        r"\inserted{$(j\in J)$}",
        r"$\displaystyle X\setminus\bigcup_{j\in J}E_j$ par les $\Pi_j$",
    ]:
        if draft.count(literal) != 1:
            issues.append(f"Common complete body fragment does not occur once: {literal!r}")
    return {
        "pass_count": SOURCE_SYNC_PASS,
        "additional_pass_reason": COMMENT_REPAIR["reason"],
        "method": "exact source strings, literal paths, group/environment/delimiter balance, physical math-line and coverage synchronization only",
        "issues": issues,
        "passed": not issues,
        "draw_commands": len(re.findall(r"\\draw\b", uncommented)),
        "fill_commands": len(re.findall(r"\\fill\b", uncommented)),
        "overline_commands": uncommented.count(r"\overline"),
        "inventory_ids_attached": len(actual_inventory),
        "decision_ids_attached_including_three_overbars": len(actual_decisions),
        "compiled": False,
        "rendered": False,
        "images_opened": False,
        "mathematical_checks": False,
        "curve_bound_calculations": False,
        "geometric_or_numeric_image_comparison": False,
    }


def main() -> None:
    if sys.argv[1:] == ["--prepare"]:
        prepare_catalog()
        return
    if sys.argv[1:]:
        raise ValueError("Supported preparatory option: --prepare")
    if not ROOT_SELECTIONS_COMPLETE:
        raise RuntimeError("Root selections are incomplete; final draft generation is disabled.")
    previous_draft = DRAFT.read_text(encoding="utf-8")
    previous_map = json.loads(MAP.read_text(encoding="utf-8"))
    assemble_root_choices()
    draft = "".join(b["emitted_literal_tex"] for b in BLOCKS)
    repaired_at = unique_at(draft, COMMENT_REPAIR["new_literal"])
    restored_previous = (draft[:repaired_at] + COMMENT_REPAIR["old_literal"]
                         + draft[repaired_at + len(COMMENT_REPAIR["new_literal"]):])
    if sha(restored_previous) != COMMENT_REPAIR["previous_draft_sha256_utf8"]:
        raise ValueError("Restoring the exact explanatory comment must recover the root-reviewed draft hash.")
    if previous_draft not in (restored_previous, draft):
        raise ValueError("The authorized second synchronization must change exactly the one recorded explanatory comment.")
    initial_sync = previous_map.get("source_comment_repair", {}).get(
        "initial_source_synchronization", previous_map["structural_source_synchronization"])
    repair_audit = {
        **COMMENT_REPAIR,
        "repaired_draft_sha256_utf8": sha(draft),
        "exact_single_comment_replacement_verified": True,
        "selected_manuscript_body_changed": False,
        "literal_graphical_commands_changed": False,
        "initial_source_synchronization": initial_sync,
    }
    journal_sources = journal_sections()
    block_sections = {
        "opening": [1, 2, 24], "upper_equalities": [3], "third_equality": [4, 5],
        "separator": [6], "margin_and_soit": [7, 26], "main_opening": [8, 9, 10, 11, 12],
        "ternaires_and_later_sign": [13, 14, 15], "coproduct_and_right_pair": [16],
        "lower_opening_and_point": [17, 18], "lower_pi_and_guide": [19],
        "middle_union": [19], "binary_ring_and_condition": [20, 25],
        "u_guide_and_ending": [21, 22, 23],
    }
    offset = 0
    for block in BLOCKS:
        emitted = block["emitted_literal_tex"]
        block["draft"] = span(draft, offset, offset + len(emitted))
        block["root_decision_sources"] = [journal_sources[n] for n in block_sections[block["id"]]]
        for path in block["literal_path_sources"]:
            at = unique_at(emitted, path["literal_tex"])
            path["draft"] = span(draft, offset + at, offset + at + len(path["literal_tex"]))
        for source in block["additional_selected_sources"]:
            at = unique_at(emitted, source["literal_tex"])
            source["draft"] = span(draft, offset + at, offset + at + len(source["literal_tex"]))
        offset += len(emitted)
    blocks = {b["id"]: b for b in BLOCKS}
    inventory = resolved_coverage(COVERAGE, draft, blocks)
    decisions = resolved_coverage(DECISION_COVERAGE, draft, blocks)
    overbars = overbar_coverage(draft)
    doubt_scope = original_doubt_scope(decisions)
    ring_scope = recurring_ring_scope(decisions)
    validation = structural_source_pass(draft)
    if validation["issues"]:
        raise RuntimeError(json.dumps(validation, ensure_ascii=False, indent=2))
    journal = JOURNAL.read_text(encoding="utf-8")
    result = {
        "scan": 17,
        "status": "root-selected source draft; pending root approval/commit",
        "draft_file": str(DRAFT.relative_to(ROOT)),
        "draft_sha256_utf8": sha(draft),
        "root_decision_journal": {"file": str(JOURNAL.relative_to(ROOT)),
                                  "sha256_utf8": sha(journal)},
        "source_files": {r: {"file": str(p.relative_to(ROOT)),
                              "sha256_utf8": sha(TEXT[r])}
                         for r, p in SOURCES.items()},
        "locator_policy": "Exact zero-based Unicode code-point spans, end-exclusive; literal text and SHA accompany every source and draft span. Covering line ranges are supplemental. A positive starting column explicitly identifies a mid-line excerpt.",
        "coordinate_policy": "Only declared source-coordinate translations and units are recorded. No image dimensions, curve bounds, font extents or rendered-layout conclusions are computed.",
        "visible_copy_policy": "Selected visible payloads occur once; explicitly selected phantom deletion annotations stay in their invisible scope; insertion attachment words occur once.",
        "blocks": BLOCKS,
        "inventory_coverage": inventory,
        "decision_coverage": decisions,
        "overbar_coverage": overbars,
        "original_C_doubt_row_coverage": doubt_scope,
        "recurring_ring_source_scope": ring_scope,
        "source_comment_repair": repair_audit,
        "assembly_audit_file": str(AUDIT.relative_to(ROOT)),
        "structural_source_synchronization": validation,
    }
    DRAFT.write_text(draft, encoding="utf-8")
    MAP.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    audit = {
        "scan": 17,
        "scope": "source assembly and one root-authorized explanatory comment repair",
        "draft_file": str(DRAFT.relative_to(ROOT)),
        "source_map_file": str(MAP.relative_to(ROOT)),
        "source_map_sha256_utf8": hashlib.sha256(MAP.read_bytes()).hexdigest(),
        "assembler_file": str(Path(__file__).relative_to(ROOT)),
        "assembler_sha256_utf8": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "root_decision_journal": result["root_decision_journal"],
        "source_comment_repair": repair_audit,
        "current_source_synchronization": validation,
    }
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"draft": str(DRAFT), "source_map": str(MAP),
                      "sha256": sha(draft), "source_map_sha256_utf8": audit["source_map_sha256_utf8"],
                      "assembly_audit": str(AUDIT), "validation": validation},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
