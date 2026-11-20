#!/usr/bin/env python3
"""Source-only assembly of scan016 from the root's explicit selections.

The script writes the review draft and exact source map only. It never reads
images, invokes TeX, evaluates mathematical claims, or edits reader returns.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
CHECKS = ROOT / "out/checks"
DRAFT = CHECKS / "scan016_final_draft.tex"
MAP = CHECKS / "scan016_final_source_map.json"
JOURNAL = CHECKS / "scan016_main_decisions.md"
SOURCES = {r: ROOT / f"out/readers/016/{r}/reading.tex" for r in "ABC"}
SOURCES["packet_C"] = ROOT / "packets/016/C.tex"
SOURCES["packet_H"] = ROOT / "packets/016/H.tex"
SOURCES["root"] = JOURNAL
TEXT = {r: p.read_text(encoding="utf-8") for r, p in SOURCES.items()}
ROOT_SELECTIONS_COMPLETE = True
BLOCKS: list[dict] = []
COVERAGE: list[dict] = []
DECISION_COVERAGE: list[dict] = []


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def position(text: str, offset: int) -> dict:
    """One-based line and zero-based character column; UTF-8 decoded text."""
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
    paths = []
    if selected_paths is None:
        selected_paths = [(reader, match.group(), "selected literal graphical command")
                          for match in re.finditer(r"\\(?:draw|fill)\b[^;]*;", original)]
    for who, literal, purpose in selected_paths:
        paths.append(reference(who, literal, purpose))
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
    opening_ids = ["016-D01", "016-D02", "016-D03", "016-D04a", "016-D04b",
                   "016-D05", "016-D06", "016-D10a", "016-D10b", "016-N01a",
                   "016-N01b", "016-G01", "016-G02", "016-G03", "016-G02-return"]
    add_block(
        "opening", "A", None, "L'intersection des deux partitions",
        opening_ids, [f"016-I{i:02d}" for i in range(1, 12)],
        ["complete opening figure and text", "two raised insertions",
         "A STROKE01 one draw with two disconnected subpaths", "A GUIDE01",
         "A GUIDE02", "one ordinary comma node", "root composed accent/ending",
         "B-primary qfd|cqfd"],
        changes=[
            ("at (642,333) {égale};", r"at (642,333) {\unsure{é|ê}gal\unsure{|e}};",
             "Root section03: accent and endpoint selected independently, in the exact composed literal."),
            ("at (243,446) {cqfd};", r"at (243,446) {\unsure{qfd|cqfd}};",
             "Root section04 selects B's qualified abbreviation candidate order."),
        ],
        additional_sources=[
            reference("C", r"\unsure{é|ê}gal\unsure{e|}", "C's separate accent and endpoint qualification syntax"),
            reference("B", r"\unsure{égal|égale}", "B's absence-of-final-e primary word reading"),
            reference("root", r"\unsure{é|ê}gal\unsure{|e}", "Root's exact selected composition"),
            reference("B", r"\unsure{qfd|cqfd}", "Root-selected abbreviation"),
        ],
        coordinate_map={
            "outer_source_origin": [225, 65],
            "full_source_scope_shift": [-225, -65],
            "full_source_path_map": "(x,y) -> (x-225,y-65) in the picture; source coordinates remain (x,y)",
            "tikz_units_cm": [0.0085, -0.0085],
            "STROKE01_inner_source_origin": [1515, 147],
            "STROKE01_path_to_source": "(x,y) -> (x+1515,y+147)",
            "STROKE01_wrapper": "baseline=0pt; bbox (0,0)-(155,14); base-west; inner/outer sep=0pt",
            "GUIDE01_and_GUIDE02": "unchanged literal full-source coordinates under the existing scope translation",
        },
    )
    cover("016-I01", "opening")
    opening_inventory_literals = {
        "016-I02": r"\Sigma_{\deleted{\unsure{2}}1}^+",
        "016-I03": r"\deleted{\unsure{sera|sont}} est",
        "016-I04": r"\draw[line width=0.23pt] (0,4) .. controls (18,0) and (36,3) .. (54,2)" "\n"
                    r"    (58,3) .. controls (90,3) and (129,8) .. (155,10);",
        "016-I05": r"\inserted{la comp. conn.}",
        "016-I06": r"\draw[line width=0.28pt] (1166,177) .. controls (1167,197) and (1187,198) .. (1233,200)" "\n"
                    r"   .. controls (1295,203) and (1358,203) .. (1385,209)" "\n"
                    r"   .. controls (1399,213) and (1399,226) .. (1398,234);",
        "016-I07": r"\inserted{de $X\unsure{/|\setminus}E_{\unsure{2}}$}",
        "016-I08": r"\draw[line width=0.22pt] (1533,246) .. controls (1535,229) and (1552,221) .. (1570,220)" "\n"
                    r"   .. controls (1603,221) and (1641,233) .. (1670,235);",
        "016-I09": r"\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1520,263) {,};",
        "016-I10": r"\deleted{\unsure{c'est}}",
        "016-I11": r"\unsure{qfd|cqfd}",
    }
    for ident, literal in opening_inventory_literals.items():
        cover(ident, "opening", literal)
    opening_decision_literals = {
        "016-D01": opening_inventory_literals["016-I02"],
        "016-D02": opening_inventory_literals["016-I03"],
        "016-D03": r"\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1463,144) {connexe};",
        "016-D04a": r"X\unsure{/|\setminus}E_{\unsure{2}}",
        "016-D04b": r"E_{\unsure{2}}",
        "016-D05": opening_inventory_literals["016-I10"],
        "016-D06": opening_inventory_literals["016-I11"],
        "016-D10a": r"\unsure{:|à}",
        "016-D10b": r"\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1115,340) {donc};",
        "016-N01a": r"\unsure{é|ê}",
        "016-N01b": r"\unsure{é|ê}gal\unsure{|e}",
        "016-G01": opening_inventory_literals["016-I06"],
        "016-G02": opening_inventory_literals["016-I08"],
        "016-G03": opening_inventory_literals["016-I04"],
        "016-G02-return": opening_inventory_literals["016-I09"],
    }
    for ident, literal in opening_decision_literals.items():
        decision(ident, "opening", literal)
    partitions, _, _ = part("A", "L'intersection des deux partitions", "% The next display")
    add_block(
        "two_partitions", "A", "L'intersection des deux partitions", "% The next display",
        ["016-D07a", "016-N05", "016-P01"],
        ["016-I12", "016-I13", "016-I14", "016-I15"],
        ["common complete heading", "common two partition rows",
         "qualified first E predecessor", "common de X est"],
        additional_sources=[
            reference("B", partitions, "Identical complete common text/formula fragment"),
            reference("C", partitions, "Identical complete common text/formula fragment"),
        ],
    )
    cover("016-I12", "two_partitions", "L'intersection des deux partitions")
    cover("016-I13", "two_partitions",
          r"\begin{aligned}" "\n"
          r" X&=\deleted{\unsure{E}}\Sigma_1^+\amalg E_1\amalg\Sigma_1^-\\" "\n"
          r" X&=\Sigma_2^+\amalg E_2\amalg\Sigma_2^-" "\n"
          r" \end{aligned}")
    cover("016-I14", "two_partitions", r"\deleted{\unsure{E}}\Sigma_1^+")
    cover("016-I15", "two_partitions", "de $X$ est")
    decision("016-D07a", "two_partitions", r"\deleted{\unsure{E}}\Sigma_1^+")
    decision("016-N05", "two_partitions",
             r"X&=\deleted{\unsure{E}}\Sigma_1^+\amalg E_1\amalg\Sigma_1^-\\",
             note="The exact first-row endpoint has no comma before the line-break command.")
    decision("016-P01", "two_partitions", note="The common two-row source layout is preserved.")
    add_block(
        "central_partition", "A", "% The next display", "avec\n",
        ["016-D07b", "016-BR01", "016-BR02", "016-BR-PAIR", "016-G04"],
        [f"016-I{i:02d}" for i in range(16, 21)],
        ["complete five-term partition with four joins", "deleted E under Sigma12",
         "A BRACE01 and upper Sigma2-minus label", "A BRACE02 and lower Sigma1-minus label",
         "A SPOT01 local qualification and exact fill"],
        coordinate_map={
            "outer_source_origin": [500, 795],
            "outer_path_to_source": "(x,y) -> (x+500,y+795)",
            "tikz_units_cm": [0.008, -0.008],
            "SPOT01_inner_parent_anchor": [637, 43],
            "SPOT01_inner_source_origin": [1137, 838],
            "SPOT01_path_to_source": "(x,y) -> (x+1137,y+838)",
            "SPOT01_wrapper": "baseline=0pt; bbox (0,0)-(8,9); base-west; inner/outer sep=0pt",
        },
    )
    cover("016-I16", "central_partition")
    upper, _, _ = part("A", " % BRACE01:", " % BRACE02:")
    lower, _, _ = part("A", " % BRACE02:", " % SPOT01:")
    central_point, _, _ = part("A", " % SPOT01:", "\n\\end{tikzpicture}}\navec")
    cover("016-I17", "central_partition", upper)
    cover("016-I18", "central_partition", lower)
    cover("016-I19", "central_partition", r"\deleted{E}\Sigma_{12}")
    cover("016-I20", "central_partition", central_point)
    decision("016-D07b", "central_partition", r"\deleted{E}\Sigma_{12}")
    decision("016-BR01", "central_partition", upper)
    decision("016-BR02", "central_partition", lower)
    decision("016-BR-PAIR", "central_partition", upper + lower,
             note="Root section06's single H parent attaches to the literal brace pair and both labels.")
    decision("016-G04", "central_partition", central_point)
    definition_start = "\\[\n \\Sigma_{12}\\overset{\\text{def}}{=}"
    add_block(
        "avec_point", "C", "% G05: the isolated point below/right of avec.", definition_start,
        ["016-G05"], ["016-I21", "016-I23"],
        ["C complete avec group", "C G05 exact local fill and unsure wrapper"],
        coordinate_map={
            "outer_source_origin": [257, 1034],
            "outer_path_to_source": "(x,y) -> (x+257,y+1034)",
            "tikz_units_cm": [0.012, -0.012],
            "G05_inner_parent_anchor": [171, 92],
            "G05_inner_source_origin": [428, 1126],
            "G05_path_to_source": "(x,y) -> (x+428,y+1126)",
            "G05_wrapper": "baseline=0pt; bbox (0,0)-(5,5); base-west; inner/outer sep=0pt",
        },
    )
    avec_node = r"\node[anchor=base west,inner sep=0pt,outer sep=0pt] (avec) at (14,47) {avec};"
    point_with_wrapper, _, _ = part(
        "C", r" \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (171,92)",
        "\n\\end{tikzpicture}\n\\[")
    cover("016-I21", "avec_point", avec_node)
    cover("016-I23", "avec_point", point_with_wrapper)
    decision("016-G05", "avec_point", point_with_wrapper)
    add_block(
        "definition_and_dans", "A", definition_start, "% Three closure rows:",
        ["016-N02", "016-N03", "016-D08", "016-N04"],
        ["016-I22", "016-I24", "016-I25"],
        ["common complete definition with unaccented def and no endpoint period",
         "common complete Dans prose and indexed term lists", "qualified O predecessor",
         "ouverts endpoint without comma"],
    )
    definition = (r"\Sigma_{12}\overset{\text{def}}{=}\Sigma_1^-\cap\Sigma_2^-")
    dans = (r"\deleted{\unsure{O}}Dans cette partition, $\Sigma_1^+,\Sigma_{12},\Sigma_2^+$ "
            "sont ouverts $E_1,E_2$ sont fermés, et on a")
    cover("016-I22", "definition_and_dans", definition)
    cover("016-I24", "definition_and_dans", dans)
    cover("016-I25", "definition_and_dans", r"\deleted{\unsure{O}}Dans")
    decision("016-N02", "definition_and_dans", r"\overset{\text{def}}{=}")
    decision("016-N03", "definition_and_dans", definition + "\n\\]",
             note="The complete endpoint has no period before its display-closing delimiter.")
    decision("016-D08", "definition_and_dans", r"\deleted{\unsure{O}}Dans")
    decision("016-N04", "definition_and_dans", "sont ouverts $E_1,E_2$",
             note="The exact surviving endpoint has no comma after ouverts.")
    add_block(
        "closure_rows", "A", "% Three closure rows:", "Notons aussi que",
        [f"016-S{i:02d}" for i in range(1, 6)] + ["016-G06"],
        ["016-I26", "016-I27", "016-I28", "016-I29"],
        ["A complete three-row closure figure and all formula nodes",
         "A SPOTS02a/b two exact fill commands in the existing local wrapper"],
        coordinate_map={
            "outer_source_origin": [150, 1430],
            "full_source_scope_shift": [-150, -1430],
            "outer_coordinates": "full-source coordinates translated by (-150,-1430)",
            "tikz_units_cm": [0.008, -0.008],
            "SPOTS02ab_inner_source_origin": [1617, 1727],
            "SPOTS02ab_path_to_source": "(x,y) -> (x+1617,y+1727)",
            "SPOTS02ab_wrapper": "baseline=0pt; bbox (0,0)-(12,15); base-west; inner/outer sep=0pt",
        },
    )
    first_closure = r"\Sigma_1^+\subsetneq\overline{\Sigma_1^+}\subset\Sigma_1^+\cup E_1"
    middle_closure = (r"\overline{\Sigma_{12}}\subset\overline{\Sigma_1^-}\cap\overline{\Sigma_2^-}"
                      r"\subset(\Sigma_1^-\cup E_1)\cap(\Sigma_2^-\cup E_2)\subset\Sigma_{12}\cup E_1\cup E_2")
    third_closure = r"\Sigma_2^+\subsetneq\overline{\Sigma_2^+}\subset\Sigma_2^+\cup E_2"
    pair, _, _ = part("A", "  % SPOTS02a/b:", "\n \\end{scope}")
    for ident, literal in [("016-I26", first_closure), ("016-I27", middle_closure),
                           ("016-I28", third_closure), ("016-I29", pair)]:
        cover(ident, "closure_rows", literal)
    decision("016-G06", "closure_rows", pair)
    add_block(
        "notons_conditions", "A", "Notons aussi que", "Car si on avait",
        ["016-S06", "016-S07", "016-G07"],
        ["016-I30", "016-I31", "016-I32"],
        ["Notons aussi que", "both complete nonempty-intersection expressions and comma",
         "A SPOT03 exact fill, fixed origin and local qualification"],
        coordinate_map={
            "outer_source_origin": [320, 1885],
            "full_source_scope_shift": [-320, -1885],
            "outer_coordinates": "full-source coordinates translated by (-320,-1885)",
            "tikz_units_cm": [0.008, -0.008],
            "SPOT03_inner_source_origin": [926, 1891],
            "SPOT03_path_to_source": "(x,y) -> (x+926,y+1891)",
            "SPOT03_wrapper": "baseline=0pt; bbox (0,0)-(7,9); base-west; inner/outer sep=0pt",
        },
    )
    both_conditions, _, _ = part(
        "A", r"  \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (332,1995)",
        "  % SPOT03:")
    condition_point, _, _ = part("A", "  % SPOT03:", "\n \\end{scope}")
    cover("016-I30", "notons_conditions", "Notons aussi que")
    cover("016-I31", "notons_conditions", both_conditions)
    cover("016-I32", "notons_conditions", condition_point)
    decision("016-G07", "notons_conditions", condition_point)
    add_block(
        "car_hypothesis", "A", "Car si on avait", "% CANCEL01:",
        ["016-D07c", "016-D07d", "016-S08"],
        ["016-I33", "016-I34", "016-I35"],
        ["complete Car si on avait p. ex. prose through on",
         "qualified E and Sigma predecessors", "complete barred hypothesis and comma"],
    )
    cover("016-I33", "car_hypothesis")
    lower_E = r"\overline{\deleted{\unsure{E}}\Sigma_{12}}"
    lower_Sigma = r"\deleted{\unsure{\Sigma}}E_1"
    cover("016-I34", "car_hypothesis", lower_E)
    cover("016-I35", "car_hypothesis", lower_Sigma)
    decision("016-D07c", "car_hypothesis", lower_E)
    decision("016-D07d", "car_hypothesis", lower_Sigma)
    add_block(
        "lower_cancellation", "A", "% CANCEL01:", "\\[\n \\big[",
        ["016-D09", "016-D11", "016-G08", "016-S09"],
        ["016-I36", "016-I37", "016-I38", "016-I47"],
        ["A complete CANCEL01 arrangement", "locally qualified en|on and firm conclurait",
         "six visible cancelled payload nodes with original invisible annotations",
         "one literal A cancellation path", "complete live continuation and comma"],
        changes=[
            (r"\inserted{en conclurait}", r"\inserted{\unsure{en|on} conclurait}",
             "Root section16 selects en|on qualification and firm conclurait in A's existing node."),
        ],
        additional_sources=[
            reference("C", r"\inserted{\unsure{en|on} conclurait}", "Root-selected exact raised wording"),
        ],
        coordinate_map={
            "outer_source_origin": [279, 2104],
            "outer_path_to_source": "(x,y) -> (x+279,y+2104)",
            "tikz_units_cm": [0.007, -0.007],
            "cancellation": "unchanged literal CANCEL01 path; all six original node anchors retained",
            "visible_deletion_payloads": "six rlap payloads; matching deleted annotations remain inside phantom",
        },
    )
    cancelled_payload, _, _ = part(
        "A", r" \node[anchor=base west,inner sep=0pt,outer sep=0pt] at (25,91)",
        r" \draw[line width=0.35pt]")
    cancellation_path = (
        r"\draw[line width=0.35pt] (26,106) .. controls (96,103) and (141,96) .. (188,96)" "\n"
        r"  .. controls (234,95) and (283,82) .. (319,81)" "\n"
        r"  .. controls (437,81) and (555,77) .. (650,80)" "\n"
        r"  .. controls (695,82) and (740,81) .. (773,85);"
    )
    live_continuation = r"$\overline{\Sigma_1^-}\cap E_1=\varnothing$,"
    cover("016-I36", "lower_cancellation", r"\inserted{\unsure{en|on} conclurait}")
    cover("016-I37", "lower_cancellation", cancelled_payload,
          note="One visible rlap payload per node; the matching phantom deleted copy remains invisible.")
    cover("016-I38", "lower_cancellation", cancellation_path)
    cover("016-I47", "lower_cancellation", live_continuation)
    decision("016-D09", "lower_cancellation", "conclurait")
    decision("016-D11", "lower_cancellation", r"\unsure{en|on}")
    decision("016-G08", "lower_cancellation", cancellation_path)
    g09, _, _ = part("C", " % G09: local origin (1090,2228)",
                     r" \cup E_2\cup\overline{\Sigma_{12}}")
    g10, _, _ = part("C", " % G10: closing-bracket candidate;", r" \end{aligned}")
    generic_underbrace = r"\underbrace{\overline{\Sigma_2^+}}_{\subset\,\Sigma_2^+\cup E_2}"
    selected_bottom_paths = [
        ("C", match.group(), "Root section19 selected G09 underbrace literal path")
        for match in re.finditer(r"\\draw\b[^;]*;", g09)
    ] + [
        ("C", match.group(), "Root section19 selected G10 partial-bracket literal return")
        for match in re.finditer(r"\\draw\b[^;]*;", g10)
    ]
    add_block(
        "bottom_argument", "A", "\\[\n \\big[", "ce qui n'est pas.",
        ["016-D12a", "016-D12a-old", "016-D12a-live", "016-D12b", "016-D12b-old",
         "016-D12b-live", "016-D13", "016-D13-shape", "016-G09"]
        + [f"016-S{i:02d}" for i in range(10, 15)],
        ["016-I39", "016-I40", "016-I41", "016-I42", "016-I43", "016-I44"],
        ["complete common bottom argument from A", "both A complete-state join qualifications",
         "C complete G09 formula/underbrace/label group", "C complete qualified G10 partial graphic"],
        changes=[
            (" " + generic_underbrace, g09,
             "Root section19 selects C's complete G09 group; replace the source indentation too so no blank math line is introduced."),
            (r"\unsure{\big]}" + "\n", "\n" + g10,
             "Root section19 selects C's G10 group; consume the source trailing newline so no blank math line precedes the display close."),
        ],
        additional_sources=[
            reference("C", g09, "Complete root-selected G09 group including its formula and annotation label"),
            reference("C", g10, "Complete root-selected G10 qualified partial-bracket group"),
        ],
        selected_paths=selected_bottom_paths,
        coordinate_map={
            "G09_source_origin": [1090, 2228],
            "G09_path_to_source": "(x,y) -> (x+1090,y+2228)",
            "G09_tikz_units_cm": [0.012, -0.012],
            "G09_formula_and_label": "Original base-west nodes with inner/outer sep=0pt and original anchors retained",
            "G10_source_origin": [1630, 2215],
            "G10_path_to_source": "(x,y) -> (x+1630,y+2215)",
            "G10_tikz_units_cm": [0.012, -0.012],
            "G10_wrapper": "Standalone local unsure picture; baseline=0pt; bbox (0,0)-(41,116); both literal paths retained",
            "placement": "Both C groups retain their original local coordinate systems in the surrounding common formula text.",
        },
    )
    cover("016-I39", "bottom_argument")
    joined = r"\unsure{\deleted{\amalg}\cup|\amalg}"
    cover("016-I40", "bottom_argument", joined, occurrence=1)
    cover("016-I41", "bottom_argument", joined, occurrence=2)
    cover("016-I42", "bottom_argument", g10)
    cover("016-I43", "bottom_argument", g09)
    cover("016-I44", "bottom_argument", r"\scriptstyle\subset\Sigma_2^+\cup E_2")
    for which, occurrence in [("a", 1), ("b", 2)]:
        for suffix in ["", "-old", "-live"]:
            decision(f"016-D12{which}{suffix}", "bottom_argument", joined, occurrence=occurrence,
                     note="The complete-state qualifier encloses the old/live choice; component attachments preserve that scope.")
    decision("016-D13", "bottom_argument", g10)
    decision("016-D13-shape", "bottom_argument", g10)
    decision("016-G09", "bottom_argument", g09)
    add_block(
        "footer_and_archive", "A", "ce qui n'est pas.", None,
        [], ["016-I45", "016-I46"],
        ["common complete footer and final point", "archive sheet number 15 comment"],
    )
    cover("016-I45", "footer_and_archive", "ce qui n'est pas.")
    cover("016-I46", "footer_and_archive", "% archive sheet number: 15")
    section_map = {
        "opening": [1, 2, 3, 4], "two_partitions": [5, 16], "central_partition": [6],
        "avec_point": [8], "definition_and_dans": [7, 9, 10], "closure_rows": [11, 12],
        "notons_conditions": [13, 14], "car_hypothesis": [15], "lower_cancellation": [16, 17],
        "bottom_argument": [18, 19], "footer_and_archive": [18],
    }
    for block in BLOCKS:
        block["root_decision_sections"] = section_map[block["id"]]


def resolved_coverage(rows: list[dict], draft: str, blocks: dict) -> list[dict]:
    result = []
    for item in rows:
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
    """Locate a command and its one braced argument without altering the text."""
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
    witness = macro_group_spans(TEXT["packet_C"], r"\overline")
    if len(final) != 14 or len(witness) != 14:
        raise ValueError("Fourteen exact overline occurrences required in packet and draft.")
    rows = []
    for i, (final_span, source_span) in enumerate(zip(final, witness), 1):
        rows.append({
            "decision_id": f"016-S{i:02d}",
            "source": {"file": "packets/016/C.tex",
                       "file_sha256_utf8": sha(TEXT["packet_C"]),
                       **span(TEXT["packet_C"], *source_span)},
            "draft": span(draft, *final_span),
            "scope": "source-command position and its literal argument only",
        })
    return rows


def structural_source_pass(draft: str) -> dict:
    """One synchronization pass, with structural checks only."""
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
    for left, right in [(r"\[", r"\]")]:
        if uncommented.count(left) != uncommented.count(right):
            issues.append("Unpaired display delimiters.")
    if len(re.findall(r"(?<!\\)\$", uncommented)) % 2:
        issues.append("Odd dollar-delimiter count.")
    allowed = set(re.findall(r"\\([A-Za-z]+)", "\n".join(TEXT.values())))
    allowed.update(re.findall(r"\\([A-Za-z]+)", (ROOT / "out/PREAMBLE.tex").read_text()))
    unknown = sorted(set(re.findall(r"\\([A-Za-z]+)", uncommented)) - allowed)
    if unknown:
        issues.append(f"Commands outside supplied source/preamble vocabulary: {unknown}")
    selected_paths = [p["literal_tex"] for b in BLOCKS for p in b["literal_path_sources"]]
    emitted_paths = [m.group() for m in re.finditer(r"\\(?:draw|fill)\b[^;]*;", draft)]
    if selected_paths != emitted_paths:
        issues.append("Selected/emitted literal graphical-command sequence differs.")
    duplicate_paths = [p for p, count in Counter(emitted_paths).items() if count != 1]
    if duplicate_paths:
        issues.append("A selected literal graphical command has multiple occurrences.")
    if draft.count(r"\scanpage{16}") != 1:
        issues.append("Scan marker does not occur once.")
    if draft.count("% archive sheet number: 15") != 1:
        issues.append("Archive-number comment does not occur once.")
    if uncommented.count(r"\overline") != 14:
        issues.append("The selected text does not contain fourteen overline commands.")
    expected_inventory = {f"016-I{i:02d}" for i in range(1, 48)}
    actual_inventory = {r["inventory_id"] for r in COVERAGE}
    if actual_inventory != expected_inventory:
        issues.append(f"Inventory attachment mismatch: {sorted(expected_inventory ^ actual_inventory)}")
    expected_decisions = {
        "016-D01", "016-D02", "016-D03", "016-D04a", "016-D04b", "016-D05", "016-D06",
        "016-D07a", "016-D07b", "016-D07c", "016-D07d", "016-D08", "016-D09",
        "016-D10a", "016-D10b", "016-D11", "016-D12a", "016-D12a-old", "016-D12a-live",
        "016-D12b", "016-D12b-old", "016-D12b-live", "016-D13", "016-D13-shape",
        "016-N01a", "016-N01b", "016-N02", "016-N03", "016-N04", "016-N05",
        "016-G01", "016-G02", "016-G03", "016-G02-return", "016-G04", "016-G05",
        "016-G06", "016-G07", "016-G08", "016-G09", "016-BR01", "016-BR02", "016-BR-PAIR",
        "016-P01",
    }
    actual_decisions = {r["decision_id"] for r in DECISION_COVERAGE}
    if actual_decisions != expected_decisions:
        issues.append(f"Decision attachment mismatch: {sorted(expected_decisions ^ actual_decisions)}")
    return {
        "pass_count": 1,
        "method": "source strings, literal paths, balance and coverage only",
        "issues": issues,
        "passed": not issues,
        "draw_commands": len(re.findall(r"\\draw\b", uncommented)),
        "fill_commands": len(re.findall(r"\\fill\b", uncommented)),
        "overline_commands": uncommented.count(r"\overline"),
        "inventory_ids_attached": len(actual_inventory),
        "decision_ids_attached_including_fourteen_overbars": len(actual_decisions) + 14,
        "compiled": False,
        "rendered": False,
        "images_opened": False,
        "mathematical_checks": False,
        "curve_bound_calculations": False,
    }


def main() -> None:
    if not ROOT_SELECTIONS_COMPLETE:
        raise RuntimeError("Root selections are incomplete; final draft generation is disabled.")
    assemble_root_choices()
    draft = "".join(b["emitted_literal_tex"] for b in BLOCKS)
    offset = 0
    for block in BLOCKS:
        emitted = block["emitted_literal_tex"]
        block["draft"] = span(draft, offset, offset + len(emitted))
        for path in block["literal_path_sources"]:
            at = unique_at(emitted, path["literal_tex"])
            path["draft"] = span(draft, offset + at, offset + at + len(path["literal_tex"]))
        offset += len(emitted)
    blocks = {b["id"]: b for b in BLOCKS}
    inventory = resolved_coverage(COVERAGE, draft, blocks)
    decisions = resolved_coverage(DECISION_COVERAGE, draft, blocks)
    overbars = overbar_coverage(draft)
    validation = structural_source_pass(draft)
    if validation["issues"]:
        raise RuntimeError(json.dumps(validation, ensure_ascii=False, indent=2))
    journal = JOURNAL.read_text(encoding="utf-8")
    result = {
        "scan": 16,
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
        "visible_copy_policy": "Selected visible payloads occur once; explicitly selected phantom deletion annotations are retained only in their original invisible scope.",
        "blocks": BLOCKS,
        "inventory_coverage": inventory,
        "decision_coverage": decisions,
        "overbar_coverage": overbars,
        "structural_source_synchronization": validation,
    }
    DRAFT.write_text(draft, encoding="utf-8")
    MAP.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"draft": str(DRAFT), "source_map": str(MAP),
                      "sha256": sha(draft), "validation": validation}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
