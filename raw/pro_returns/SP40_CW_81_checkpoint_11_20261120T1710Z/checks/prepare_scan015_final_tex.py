#!/usr/bin/env python3
"""Mechanically assemble scan015 from the root's completed source selections.

This script writes only the review draft and its source map.  It reads no image,
uses no TeX processor, and makes no ink-reading decision.  The final page and the
three independent reader returns are never written by this script.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
CHECKS = ROOT / "out/checks"
DRAFT = CHECKS / "scan015_final_draft.tex"
MAP = CHECKS / "scan015_final_source_map.json"
DECISIONS = CHECKS / "scan015_main_decisions.md"
SOURCES = {
    who: ROOT / f"out/readers/015/{who}/reading.tex" for who in "ABC"
}
TEXT = {who: path.read_text(encoding="utf-8") for who, path in SOURCES.items()}
BLOCKS: list[dict] = []

# Root's completion message and sections 01--26 have been read.
ROOT_SELECTIONS_COMPLETE = True


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def source_part(who: str, start: str | None, end: str | None) -> tuple[str, int, int]:
    value = TEXT[who]
    begin = 0 if start is None else value.index(start)
    finish = len(value) if end is None else value.index(end, begin + len(start or ""))
    return value[begin:finish], begin, finish


def substitution(value: str, old: str, new: str, description: str) -> tuple[str, dict]:
    matches = value.count(old)
    if matches != 1:
        raise ValueError(f"{description}: expected one source occurrence, found {matches}")
    return value.replace(old, new, 1), {
        "description": description,
        "source_tex": old,
        "emitted_tex": new,
    }


def add(
    block_id: str,
    who: str,
    start: str | None,
    end: str | None,
    decisions: list[int],
    components: list[str],
    changes: list[tuple[str, str, str]] | None = None,
    coordinate_map: dict | None = None,
    extra_sources: list[dict] | None = None,
    path_selection: list[tuple[str, str]] | None = None,
) -> None:
    original, begin, finish = source_part(who, start, end)
    emitted = original
    performed = []
    for old, new, description in changes or []:
        emitted, change = substitution(emitted, old, new, description)
        performed.append(change)
    source = TEXT[who]
    BLOCKS.append(
        {
            "id": block_id,
            "root_decision_sections": decisions,
            "components": components,
            "source_reader": who,
            "source_file": str(SOURCES[who].relative_to(ROOT)),
            "source_lines_inclusive": [
                source.count("\n", 0, begin) + 1,
                source.count("\n", 0, finish - 1) + 1,
            ],
            "source_literal_tex": original,
            "emitted_literal_tex": emitted,
            "transformations": performed,
            "additional_selected_sources": extra_sources or [],
            "coordinate_map": coordinate_map,
            "selected_path_override": path_selection,
        }
    )


def read_reference(who: str, literal: str, purpose: str) -> dict:
    at = TEXT[who].index(literal)
    return {
        "source_reader": who,
        "source_file": str(SOURCES[who].relative_to(ROOT)),
        "source_lines_inclusive": [
            TEXT[who].count("\n", 0, at) + 1,
            TEXT[who].count("\n", 0, at + len(literal) - 1) + 1,
        ],
        "selected_literal_tex": literal,
        "purpose": purpose,
    }


def assemble_selected_blocks() -> None:
    add("page_and_heading", "A", None, "% MARK01:", [1],
        ["page/group setup", "whole heading underline", "deleted I|V", "Version I"])

    add("opening_detached_mark", "A", "% MARK01:", "Soient $X$", [25],
        ["A MARK01 literal fill", "local unsure", "original relative spacing"],
        coordinate_map={
            "source_locus_origin_from_A": [191, 141],
            "local_picture_baseline": "0pt",
            "local_bbox": "(0,0)-(74,8), retained for relative spacing",
            "placement": "ordinary text flow relative to Soient; no full-page typeset-origin assertion",
            "tikz_units_cm": [0.013, -0.013],
        })
    add("opening_prose", "A", "Soient $X$", "% GUIDE01:", [2],
        ["Soient opening and complete indexed family", "deleted Sigma|S before E_i"])
    add("opening_guide", "A", "% GUIDE01:", "(noté indiciellement)", [3],
        ["inserted fermés|fermées", "de X", "A GUIDE01 literal path"],
        coordinate_map={
            "declared_source_origin": [372, 177],
            "path_to_source": "(x,y) -> (x+372,y+177)",
            "tikz_units_cm": [0.013, -0.013],
            "ordinary_text_placement": "relative; no full-scan font-bound assertion",
        })
    add("opening_tail_and_upper_note", "A", "(noté indiciellement)", "\\[", [3, 4],
        ["opening sentence tail", "complete slanted upper-left note", "attachment arrow",
         "tte|toute|tt", "conn.", "Sigma_i|Sigma", "non", "both closure formulas"])
    add("condition_a", "A", "\\[", "\\margin{\\uline{NB}", [6],
        ["complete condition (a)", "Card", "deleted Sigma before E_i", "tag (a)"])
    add("upper_right_nb", "B", "% G02:", "\\[", [5],
        ["complete upper-right NB", "NB underline", "B G02 qualified overset rule",
         "second exponent +|-|star", "written X minus Sigma_i"],
        coordinate_map={
            "rule_body": r"\rule{.8em}{.35pt}",
            "placement": "relative overset above first Sigma; no source-font or closure assertion",
        })
    add("condition_b_and_main_nb", "A", "\\[\n \\begin{aligned}",
        "On se propose", [7, 8, 9, 10, 11],
        ["complete condition (b)", "both deleted Sigma predecessors", "tag (b)",
         "complete NB paragraph", "Cette", "automatiquement les", "mutuellement without stop"])
    add("purpose", "A", "On se propose", "% RULE01:", [],
        ["complete purpose paragraph; unchanged common text"])
    add("case_heading", "A", "% RULE01:", "Soit $\\Sigma_i^+$", [12],
        ["complete case heading text", "deleted (de)", "deleted <=|=", "A RULE01 long path",
         "A RULE01 separate short path under 2"],
        coordinate_map={
            "declared_source_origin": [501, 996],
            "path_to_source": "(x,y) -> (x+501,y+996)",
            "tikz_units_cm": [0.013, -0.013],
            "ordinary_text_placement": "relative; no full-scan font-bound assertion",
        })
    add("case_setup", "A", "Soit $\\Sigma_i^+$", "% Drawing coordinates", [],
        ["complete Soit sentence before drawing; unchanged common text"])

    old_mark = (
        r"\node[inner sep=0pt] at (509,156) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]"
    )
    new_mark = (
        "% Fixed inner origin: parent (507,153), full source (526,1191).\n"
        "% Baseline 0 and base-west/zero-separation anchor map the inner origin exactly.\n"
        r"\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (507,153) {\unsure{\begin{tikzpicture}[baseline=0pt,x=.013cm,y=-.013cm]"
    )
    add("main_drawing", "C", "% DRAW01:", "\n\\[", [13],
        ["C DRAW01 nine oval paths", "C DRAW01 two-chord command",
         "three original C brace commands in shift (5,33)",
         "one cancelled upper-left label plus its two crossing paths",
         "six live labels including qualified right exponent", "C MARK01 literal fill body"],
        changes=[(old_mark, new_mark, "Root's fixed-origin conversion of C MARK01; filled path unchanged")],
        coordinate_map={
            "drawing_origin_full": [19, 1038],
            "drawing_path_to_source": "(x,y) -> (x+19,y+1038)",
            "brace_shift_in_drawing": [5, 33],
            "brace_path_to_source": "(x,y) -> (x+24,y+1071)",
            "mark_origin_in_drawing": [507, 153],
            "mark_origin_full": [526, 1191],
            "mark_path_to_source": "(x,y) -> (x+526,y+1191)",
            "mark_wrapper": "baseline=0pt; bbox (0,0)-(4,6); base-west node; inner/outer sep 0pt",
            "tikz_units_cm": [0.013, -0.013],
            "font_geometry": "Label anchor coordinates are retained; glyph bounds are not asserted.",
        })
    add("equation_1_and_ce_qui", "A", "\\[\n \\Sigma_1^+\\cap\\Sigma_2^+=", "\\[\n \\begin{aligned}\n &\\begin{tikzpicture}", [14],
        ["complete formula (1) and tag", "ce qui", "deleted résulte de"])

    old_points = r"\node[inner sep=0] at (157,19) {\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm]"
    new_points = (
        "% Fixed inner origin: parent (155,16), full source (859,1404).\n "
        r"\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (155,16) {\unsure{\begin{tikzpicture}[baseline=0pt,x=.013cm,y=-.013cm]"
    )
    accent = r"\unsure{équivaut|èquivaut}"
    add("cancelled_inclusions_and_equivalence", "A", "\\[\n \\begin{aligned}\n &\\begin{tikzpicture}", "% CANCEL03:", [14],
        ["first cancelled inclusion rendered once", "A CANCEL02 literal crossing path",
         "A MARK03 literal two-fill body", "C qualified équivaut|èquivaut à",
         "second cancelled inclusion", "live inclusion with union E_2 and et"],
        changes=[
            (old_points, new_points, "Root's fixed-origin conversion of A MARK03; both fill bodies unchanged"),
            (r"\text{équivaut à}", r"\text{\unsure{équivaut|èquivaut} à}", "Use root-selected C accent alternatives"),
        ],
        extra_sources=[read_reference("C", accent, "selected qualified word")],
        coordinate_map={
            "inclusion_group_origin_full": [704, 1388],
            "crossing_path_to_source": "(x,y) -> (x+704,y+1388)",
            "mark_origin_in_group": [155, 16],
            "mark_origin_full": [859, 1404],
            "mark_path_to_source": "(x,y) -> (x+859,y+1404)",
            "mark_wrapper": "baseline=0pt; bbox (0,0)-(5,8); base-west node; inner/outer sep 0pt",
            "tikz_units_cm": [0.013, -0.013],
            "ordinary_text_placement": "relative; no full-scan font-bound assertion",
        })
    car_si_a = r"\unsure{car si|Car si}"
    car_si_b = r"\unsure{Car si|car si}"
    # The reading occurs twice solely because the second copy is in phantom.
    add("car_si", "A", "% CANCEL03:", "\\deleted{Si on avait}", [15],
        ["B-primary Car si|car si", "one visible label plus invisible deletion annotation",
         "A CANCEL03 two literal crossing paths"],
        changes=[
            (r"\rlap{" + car_si_a + r"}\phantom{\deleted{" + car_si_a + "}}",
             r"\rlap{" + car_si_b + r"}\phantom{\deleted{" + car_si_b + "}}",
             "Use B-primary capitalization in visible text and its invisible annotation"),
        ],
        extra_sources=[read_reference("B", car_si_b, "root-selected capitalization alternatives")],
        coordinate_map={
            "declared_source_origin": [202, 1435],
            "path_to_source": "(x,y) -> (x+202,y+1435)",
            "tikz_units_cm": [0.013, -0.013],
            "ordinary_text_placement": "relative; no full-scan font-bound assertion",
        })

    add("si_on_avait_through_equation_2", "A", "\\deleted{Si on avait}", "% MARK04:", [16, 17],
        ["deleted Si on avait before comme", "complete comme/cela équivaut aussi à line",
         "complete formula (2) and tag"])
    add("right_detached_pair", "A", "% MARK04:", "\\unsure{et} symétriquement", [26],
        ["A MARK04 two literal fill commands", "local unsure", "relative right-margin placement"],
        coordinate_map={
            "source_locus_bbox_from_A": [1603, 1778, 1610, 1786],
            "placement": "relative margin placement; no full-page typeset-origin or observed-bound assertion",
            "tikz_units_cm": [0.013, -0.013],
        })
    add("symmetry_and_equation_2_prime", "C", r"\unsure{et} \unsure{symètriquement|symétriquement}",
        "Comme\n", [18],
        ["unsure et", "C symètriquement|symétriquement", "comma and à without colon",
         "complete formula (2 prime) and tag"])

    b_mark = (
        "% G05: detached slant below the struck words, visible (510,2076)--(526,2063).\n"
        r"\node[inner sep=0] at (299,61) {\unsure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round]" "\n"
        r"\path[use as bounding box] (0,0) rectangle (16,13);" "\n"
        r"\draw (0,13) .. controls (5,6) and (10,1) .. (16,0);" "\n"
        r"\end{tikzpicture}}};"
    )
    c_mark_body = (
        r"\path[use as bounding box] (0,0) rectangle (19,16);" "\n"
        r"\draw[line width=.6pt] (1,15) .. controls (8,7) and (13,3) .. (18,2);"
    )
    c_mark_fixed = (
        "% Selected C MARK02 body; fixed inner full origin (510,2061).\n"
        "% Parent origin (219,2009), anchor (291,52); wrapper units match the parent.\n"
        r"\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (291,52) {\unsure{\begin{tikzpicture}[baseline=0pt,x=.009cm,y=-.009cm,line cap=round]" "\n"
        + c_mark_body + "\n" + r"\end{tikzpicture}}};"
    )
    lower_first_crossing = r"\draw (209,37) .. controls (270,33) and (334,38) .. (410,36);"
    lower_slant = r"\draw[line width=.6pt] (1,15) .. controls (8,7) and (13,3) .. (18,2);"
    lower_second_crossing = r"\draw (557,91) .. controls (705,95) and (858,86) .. (997,82);"
    add("lower_correction_group", "B", "% Lower correction group:", "% slanted\n\\reversemarginpar\n\\margin{$\\overline{\\Sigma_1^+}", [19, 20],
        ["complete B lower correction arrangement", "Comme", "raised cancelled unsure vois. ouvert",
         "B first literal cancellation path", "Sigma_2^- superset E_1 and comma",
         "fixed-origin C MARK02 literal path", "cancelled il contient les",
         "B second literal cancellation path", "complete inserted i.e. clause",
         "underline under vois excluding point", "on unsure a"],
        changes=[
            (b_mark, c_mark_fixed, "Use selected C MARK02 body with root-declared fixed origin and enclosing B units"),
            (r"\uline{vois.}", r"\uline{vois}.", "Root-selected underline span excludes the point"),
            ("{on a};", r"{on \unsure{a}};", "Root-selected local qualification of a"),
        ],
        extra_sources=[
            read_reference("C", c_mark_body, "selected MARK02 local bbox and literal path"),
            read_reference("A", r"\uline{vois}.", "selected underline span"),
            read_reference("A", r"on \unsure{a}", "selected a qualification"),
        ],
        path_selection=[("B", lower_first_crossing), ("C", lower_slant), ("B", lower_second_crossing)],
        coordinate_map={
            "lower_group_origin_full": [219, 2009],
            "cancellation_paths_to_source": "(x,y) -> (x+219,y+2009)",
            "mark_origin_in_group": [291, 52],
            "mark_origin_full": [510, 2061],
            "mark_path_to_source": "(x,y) -> (x+510,y+2061)",
            "mark_wrapper": "baseline=0pt; bbox (0,0)-(19,16); base-west node; inner/outer sep 0pt",
            "mark_wrapper_units_change": "C's .013cm,-.013cm wrapper is replaced by B group's .009cm,-.009cm units; literal selected draw command is unchanged.",
            "tikz_units_cm": [0.009, -0.009],
            "ordinary_text_placement": "relative; no full-scan font-bound assertion",
        })

    a_short_curve = (
        r"\draw (257,110) .. controls (224,103) and (211,125) .. (217,144)" "\n"
        r" .. controls (222,149) and (233,150) .. (237,168);"
    )
    a_short_head = r"\draw (237,168) -- (227,162) (237,168) -- (238,156);"
    a_short = a_short_curve + "\n" + a_short_head
    a_short_fixed = (
        "% A GUIDE02 locally qualified; its attachment/role/hand/origin remain undetermined.\n"
        "% Wrapper anchor and opposite inner shift preserve the two original path bodies.\n"
        r"\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (211,103) {\unsure{\begin{tikzpicture}[baseline=0pt,x=.009cm,y=-.009cm,line cap=round]" "\n"
        r"\path[use as bounding box] (0,0) rectangle (50,70);" "\n"
        r"\begin{scope}[shift={(-211,-103)}]" "\n"
        + a_short + "\n"
        r"\end{scope}" "\n"
        r"\end{tikzpicture}}};"
    )
    a_long = (
        "% GUIDE03 observed near (187,2149)-(300,2200).\n"
        r"\draw (171,238) .. controls (155,210) and (204,200) .. (245,196)" "\n"
        r" .. controls (265,193) and (276,193) .. (282,187);"
    )
    c_long_path = (
        r"\draw[black!65] (7,59) .. controls (0,34) and (22,28) .. (60,21)" "\n"
        r" .. controls (87,18) and (105,13) .. (118,7);"
    )
    c_long_body = r"\path[use as bounding box] (0,0) rectangle (125,67);" "\n" + c_long_path
    c_long_fixed = (
        "% Selected C GUIDE02 replaces A GUIDE03; one longer curve is supplied.\n"
        "% Fixed inner origin in note (163,196), full source (180,2158).\n"
        r"\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (163,196) {\unsure{\begin{tikzpicture}[baseline=0pt,x=.009cm,y=-.009cm,line cap=round]" "\n"
        + c_long_body + "\n" + r"\end{tikzpicture}}};"
    )
    add("lower_slanted_note", "A", "% slanted; local note", "\\[\n \\Sigma_2^-\\cap\\Sigma_1^+", [21],
        ["complete A slanted-note text-node arrangement", "both closure formulas and i.e.",
         "C-primary à sign.ler|à signaler", "avant", "A GUIDE02 short curve and arrowhead",
         "C GUIDE02 longer pale curve replacing A GUIDE03"],
        changes=[
            ("% GUIDE02 and GUIDE03 are separate observed curved strokes, without a supplied mathematical role.",
             "% A GUIDE02 short arrow and C GUIDE02 long curve are separate locally qualified components.",
             "Update component identifiers after the selected long-guide replacement"),
            (r"\unsure{à signaler|à sign.ler}", r"\unsure{à sign.ler|à signaler}", "Use C-primary instruction candidates"),
            (a_short, a_short_fixed, "Qualify A short guide locally while preserving its path coordinates through opposite wrapper translations"),
            (a_long, c_long_fixed, "Replace A long curve with root-selected C long-curve literal bbox/path"),
        ],
        extra_sources=[
            read_reference("C", r"\unsure{à sign.ler|à signaler}", "selected candidate order"),
            read_reference("C", c_long_body, "selected long-guide bbox and literal path"),
        ],
        path_selection=[("A", a_short_curve), ("A", a_short_head), ("C", c_long_path)],
        coordinate_map={
            "note_origin_full": [17, 1962],
            "note_path_to_source": "(x,y) -> (x+17,y+1962)",
            "short_guide_wrapper_anchor": [211, 103],
            "short_guide_inner_shift": [-211, -103],
            "short_guide_composition": "(x,y) -> (x-211,y-103) -> (x,y) in note coordinates -> (x+17,y+1962) in source coordinates",
            "short_wrapper_bbox": "(0,0)-(50,70), declared for typesetting; no observed-bound assertion",
            "long_guide_origin_in_note": [163, 196],
            "long_guide_origin_full": [180, 2158],
            "long_guide_path_to_source": "(x,y) -> (x+180,y+2158)",
            "long_guide_wrapper": "baseline=0pt; bbox (0,0)-(125,67); base-west node; inner/outer sep 0pt",
            "long_guide_units_change": "C's .013cm,-.013cm wrapper is replaced by the A note's .009cm,-.009cm units; literal path and bbox remain unchanged.",
            "tikz_units_cm": [0.009, -0.009],
            "ordinary_text_placement": "relative; no full-scan font-bound assertion",
        })
    add("lower_display_and_car_formula", "A", "\\[\n \\Sigma_2^-\\cap\\Sigma_1^+", "% GUIDE04:", [21, 22, 23],
        ["complete lower intersection display", "Car", "overline Sigma_1^+ intersect E_1",
         "A RULE02 literal hooked underline", "nonempty relation"],
        changes=[
            (r"$\ne\varnothing$ (sinon", r"$\ne\varnothing$", "The selected B final-insertion group supplies (sinon once"),
        ],
        coordinate_map={
            "rule_source_origin_approx_from_A_report": [854, 2217],
            "path_to_source_approx": "(x,y) -> (x+854,y+2217)",
            "tikz_units_cm": [0.013, -0.013],
            "ordinary_text_placement": "relative; no full-scan font-bound assertion",
        })

    add("final_insertion_group", "B", "% Final local insertion:", "serait \\inserted", [23],
        ["complete B final-insertion arrangement", "opening parenthesis and sinon once",
         "C qualified inserted l'ouvert|louvert", "Sigma_1^+", "B GUIDE02 literal hooked path"],
        changes=[
            (r"\inserted{l'ouvert}", r"\inserted{\unsure{l'ouvert|louvert}}", "Use C-qualified insertion text in B's selected layout"),
        ],
        extra_sources=[read_reference("C", r"\inserted{\unsure{l'ouvert|louvert}}", "selected qualified insertion")],
        coordinate_map={
            "declared_source_origin": [1278, 2080],
            "path_to_source": "(x,y) -> (x+1278,y+2080)",
            "tikz_units_cm": [0.013, -0.013],
            "ordinary_text_placement": "relative; no full-scan font-bound assertion",
        })
    add("final_un_and_connector", "A", "serait \\inserted{un}", "% CANCEL04:", [24],
        ["serait", "inserted un", "fermé dans X and comma", "unsure donc|puis"])
    upright = r"\draw (24,6) -- (26,16);"
    upright_box = r"\path[use as bounding box] (0,0) rectangle (37,24);"
    upright_fixed = (
        "% Only B G07's second short upright is added; C's angular path remains once.\n"
        "% Fixed inner origin in C's group (12,1), full source (932,2239).\n"
        r"\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (12,1) {\unsure{\begin{tikzpicture}[baseline=0pt,x=.013cm,y=-.013cm,line cap=round]" "\n"
        + upright_box + "\n" + upright + "\n" + r"\end{tikzpicture}}};"
    )
    last_end = r"\end{tikzpicture} $X$ serait disconnexe),"
    add("final_cancelled_group_and_ending", "C", "% CANCEL03: full-scan origin (920,2238)", None, [21, 24],
        ["C complete qualified cancelled glyph/word group with neq emptyset alternative",
         "C CANCEL03 three literal crossing paths", "B G07 second literal upright only",
         "final X serait disconnexe),", "closing group", "exact final archive-sheet-14 comment"],
        changes=[
            (last_end, upright_fixed + "\n" + last_end, "Add only root-selected B G07 upright using fixed-origin local unsure wrapper"),
        ],
        extra_sources=[
            read_reference("B", upright, "selected second G07 path; first angular B path is omitted"),
            read_reference("B", upright_box, "retained local wrapper rectangle for the selected upright"),
        ],
        path_selection=[
            ("C", r"\draw (14,31) -- (53,9);"),
            ("C", r"\draw (8,25) -- (18,5) -- (24,29) -- (39,23);"),
            ("C", r"\draw (24,32) .. controls (60,23) and (105,29) .. (164,39);"),
            ("B", upright),
        ],
        coordinate_map={
            "final_group_origin_full": [920, 2238],
            "C_crossing_paths_to_source": "(x,y) -> (x+920,y+2238)",
            "B_upright_origin_in_group": [12, 1],
            "B_upright_origin_full": [932, 2239],
            "B_upright_path_to_source": "(x,y) -> (x+932,y+2239)",
            "upright_wrapper": "baseline=0pt; bbox (0,0)-(37,24); base-west node; inner/outer sep 0pt",
            "tikz_units_cm": [0.013, -0.013],
            "ordinary_text_placement": "relative; no full-scan font-bound assertion",
        })


def without_comments(value: str) -> str:
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in value.splitlines())


def path_commands(value: str) -> list[str]:
    return re.findall(r"\\(?:draw|fill)\b[^;]*;", without_comments(value))


def verify_once(final_tex: str) -> dict:
    """The single final structural/source-report pass, after all root choices."""
    clean = without_comments(final_tex)
    brace_depth = 0
    for match in re.finditer(r"(?<!\\)[{}]", clean):
        brace_depth += 1 if match.group() == "{" else -1
        if brace_depth < 0:
            raise ValueError("Unmatched closing brace")
    if brace_depth:
        raise ValueError("Unbalanced braces")
    environments = []
    for action, name in re.findall(r"\\(begin|end)\{([^{}]+)\}", clean):
        if action == "begin":
            environments.append(name)
        elif not environments or environments.pop() != name:
            raise ValueError(f"Environment mismatch at {name}")
    if environments:
        raise ValueError(f"Unclosed environments: {environments}")
    if clean.count(r"\[") != clean.count(r"\]"):
        raise ValueError("Unpaired display delimiters")
    if len(re.findall(r"(?<!\\)\$", clean)) % 2:
        raise ValueError("Unpaired dollar delimiters")
    if not final_tex.endswith("\\endgroup\n% archive sheet number: 14\n"):
        raise ValueError("Final group/archive comment changed")
    covered_sections = {section for block in BLOCKS for section in block["root_decision_sections"]}
    if covered_sections != set(range(1, 27)):
        raise ValueError(f"Root decision-section coverage mismatch: {sorted(covered_sections)}")
    for block in BLOCKS:
        override = block.pop("selected_path_override")
        original = [literal for _who, literal in override] if override is not None else path_commands(block["source_literal_tex"])
        emitted = path_commands(block["emitted_literal_tex"])
        if original != emitted:
            raise ValueError(f"Selected literal path commands changed in {block['id']}")
        block["literal_path_commands"] = emitted
        block["literal_path_sources"] = [
            read_reference(who, literal, "selected literal path command")
            for who, literal in (override if override is not None else [(block["source_reader"], p) for p in original])
        ]
        block["literal_path_preservation"] = "exact source command strings, same order"
    # All emitted bytes are accounted for by the ordered, source-linked blocks.
    if "".join(block["emitted_literal_tex"] for block in BLOCKS) != final_tex:
        raise ValueError("Source map does not cover the complete draft")
    return {
        "performed_once": True,
        "method": "Direct source parsing and exact selected-path/common-block comparisons",
        "balanced_braces": True,
        "nested_environments": True,
        "paired_math_delimiters": True,
        "archive_sheet_14_comment": "exact and final",
        "all_selected_path_commands": "exact source strings preserved in source order",
        "source_map_coverage": "all emitted source, including unchanged common text",
        "root_decision_sections": "01--26 represented",
        "compiler_or_renderer": False,
        "images_opened": False,
        "numerical_bounds_or_extrema": False,
        "coordinate_work": "Root-declared translations and fixed-origin wrapper maps are recorded. The short-guide wrapper uses opposite translations (211,103) and (-211,-103), whose composition preserves the original path coordinates. This is source-coordinate bookkeeping; no numerical bounds or extrema calculation or mathematical proof was performed.",
    }


def compact_reference(reference: dict) -> dict:
    result = dict(reference)
    literal = result.get("selected_literal_tex", "")
    if re.search(r"\\(?:draw|fill|path)\b", literal):
        result.pop("selected_literal_tex")
        result["selected_fragment_sha256"] = sha256_text(literal)
        result["literal_location"] = "retained source range; selected path command appears once in this block's literal_path_sources"
    return result


def compact_block(block: dict) -> dict:
    """Keep paths once per actual selected component, never once per inventory row."""
    result = {key: value for key, value in block.items() if key not in {
        "source_literal_tex", "emitted_literal_tex", "literal_path_commands", "transformations",
        "additional_selected_sources",
    }}
    result["source_fragment_sha256"] = sha256_text(block["source_literal_tex"])
    result["emitted_fragment_sha256"] = sha256_text(block["emitted_literal_tex"])
    result["complete_literal_text_location"] = "retained source range and emitted draft range above; exact text changes below"
    result["additional_selected_sources"] = [compact_reference(ref) for ref in block["additional_selected_sources"]]
    changes = []
    for change in block["transformations"]:
        item = dict(change)
        combined = item["source_tex"] + item["emitted_tex"]
        if re.search(r"\\(?:draw|fill|path)\b", combined) or len(combined) > 800:
            item["source_fragment_sha256"] = sha256_text(item.pop("source_tex"))
            item["emitted_fragment_sha256"] = sha256_text(item.pop("emitted_tex"))
            item["exact_wrapper_location"] = "emitted draft range; declared wrapper/translation in coordinate_map"
        changes.append(item)
    result["transformations"] = changes
    return result


def main() -> None:
    if not ROOT_SELECTIONS_COMPLETE:
        raise SystemExit("Root selections remain pending; no draft or map was written.")
    assemble_selected_blocks()
    final_tex = "".join(block["emitted_literal_tex"] for block in BLOCKS)
    verification = verify_once(final_tex)
    line = 1
    for block in BLOCKS:
        value = block["emitted_literal_tex"]
        block["draft_lines_inclusive"] = [line, line + value.count("\n") - (1 if value.endswith("\n") else 0)]
        position = 0
        for reference in block["literal_path_sources"]:
            literal = reference["selected_literal_tex"]
            at = value.index(literal, position)
            reference["draft_lines_inclusive"] = [
                line + value.count("\n", 0, at),
                line + value.count("\n", 0, at + len(literal) - 1),
            ]
            position = at + len(literal)
        line += value.count("\n")
    reports = {}
    for who in "ABC":
        path = ROOT / f"out/readers/015/{who}/report.json"
        reports[who] = {
            "file": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
    result = {
        "scan": 15,
        "status": "mechanical assembly for independent root source review",
        "decision_authority": str(DECISIONS.relative_to(ROOT)),
        "decision_log_sha256": hashlib.sha256(DECISIONS.read_bytes()).hexdigest(),
        "source_files": {
            who: {"path": str(path.relative_to(ROOT)), "sha256": sha256_text(TEXT[who])}
            for who, path in SOURCES.items()
        },
        "reader_reports": reports,
        "preamble": "out/PREAMBLE.tex; unchanged",
        "draft": str(DRAFT.relative_to(ROOT)),
        "draft_sha256": sha256_text(final_tex),
        "coordinate_scope": (
            "Declared source-pixel translations describe selected graphical paths. "
            "Printed text is placed relative to those components or ordinary TeX flow. "
            "No full-scan font-bound equivalence is asserted. Fixed inner origins use "
            "baseline=0pt, use-as-bounding-box, and zero-separation base-west anchors."
        ),
        "workflow": (
            "Source-only mechanical assembly; no images, ink choices, OCR, research, "
            "TeX compilation/rendering, installation, final-page writes, or commits."
        ),
        "structural_source_report_pass": verification,
        "component_manifest": [compact_block(block) for block in BLOCKS],
    }
    DRAFT.write_text(final_tex, encoding="utf-8")
    MAP.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"draft": str(DRAFT), "source_map": str(MAP), "blocks": len(BLOCKS), "verification": verification}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
