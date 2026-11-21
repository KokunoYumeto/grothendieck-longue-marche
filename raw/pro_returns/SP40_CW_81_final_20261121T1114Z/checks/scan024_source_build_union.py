#!/usr/bin/env python3
"""Build the scan024 source-only clerical union, without selecting any reading."""
from pathlib import Path
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("source_support", HERE / "scan024_source_support.py")
S = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S)
BASE = S.BASE

REPORTS = {}
MAPS = {}
TEXTS = {}
REGISTRY = {}
PARSERS = {}
SCOPES = {}
GROUPS = {}


def register(path, role):
    if path not in REGISTRY:
        REGISTRY[path], TEXTS[path] = S.source(path, role)
        if path.endswith(".json"):
            PARSERS[path] = S.JSONSpans(TEXTS[path])
    return REGISTRY[path]


def jref(path, pointer):
    a, b = PARSERS[path].spans[pointer]
    return S.ref(REGISTRY[path], TEXTS[path], a, b, pointer)


def tref(path, a, b):
    return S.ref(REGISTRY[path], TEXTS[path], a, b)


def spanref(path, span):
    a = span.get("char_start", span.get("character_start"))
    b = span.get("char_end_exclusive", span.get("character_end_exclusive"))
    assert TEXTS[path][a:b] == span["exact_tex"]
    return tref(path, a, b)


for reader in "ABC":
    for name, role in [("reading.tex", "actual_complete_TeX"), ("reading.md", "own_verbal_return"), ("report.json", "raw_report"), ("source_map.json", "raw_source_map")]:
        register(f"out/readers/024/{reader}/{name}", f"reader_{reader}_{role}")
    rp = f"out/readers/024/{reader}/report.json"
    mp = f"out/readers/024/{reader}/source_map.json"
    tp = f"out/readers/024/{reader}/reading.tex"
    REPORTS[reader] = PARSERS[rp].value
    MAPS[reader] = PARSERS[mp].value
    GROUPS[reader] = {}
    for i, group in enumerate(MAPS[reader]["groups"]):
        gid = group["id"]
        GROUPS[reader][gid] = {"id": gid, "reader": reader, "complete_metadata_ref": jref(mp, f"/groups/{i}"), "complete_TeX_ref": spanref(tp, group["source_span"])}
    units = MAPS[reader].get("units", MAPS[reader].get("plain_units", MAPS[reader]["groups"]))
    for unit in units:
        SCOPES[reader + ":" + unit["id"]] = spanref(tp, unit["source_span"])
    if reader == "A":
        end = TEXTS[tp].index("% BEGIN UNIT P1")
        SCOPES["A:ADMIN"] = tref(tp, 0, end)
    if reader == "C":
        SCOPES["C:ADMIN"] = tref(tp, 0, TEXTS[tp].index("\n") + 1)

for path, role in [
    ("packets/024/C.tex", "public_witness_C_literal"),
    ("packets/024/H.tex", "public_witness_H_literal"),
    ("packets/024/C_doubts.txt", "public_witness_C_doubt_table_with_original_compound_scope"),
    ("packets/024/C_inventory.json", "public_witness_C_inventory"),
    ("packets/024/C_notes.txt", "public_witness_C_notes"),
    ("packets/024/metadata.json", "packet_administration"),
    ("packets/024/notation.md", "shared_notation_exact_existing_scan_scopes"),
    ("out/checks/scan024_C_doubt_catalog.json", "root_canonical_source_row_identities_only"),
    ("out/checks/scan024_H_marker_catalog.json", "root_H_source_marker_catalog_only"),
    ("out/checks/scan024_S_scope.json", "root_S_source_only_scope_catalog"),
    ("out/briefs/source_record_brief_v07.md", "source_support_authority"),
    ("source/SP40_CW_81_witnesses/codex/J81-03/PREAMBLE.tex", "supplied_transcription_macro_conventions"),
    ("source/SP40_CW_81_witnesses/codex/J81-03/PROMPT.md", "supplied_historical_transcription_conventions"),
    ("out/readers/024/C/make_source_map.py", "reader_C_map_generation_provenance"),
    ("out/readers/024/C/group_metadata.json", "reader_C_raw_group_metadata"),
]:
    register(path, role)

# Complete C/H source paragraphs, with source line breaks and macro states intact.
for witness in "CH":
    path = f"packets/024/{witness}.tex"
    t = TEXTS[path]
    opening = t.index("\n") + 1
    definition = t.index("\\[")
    definition_end = t.index("\\]") + 2
    if witness == "C":
        lemma = t.index("\\uline{Lemme} Cette")
        explanation = t.index("\\unsure{le|Le}")
        final = t.index("\\unsure{Soient|Soit}")
        archive = t.index("% archive sheet number: 23")
    else:
        lemma = t.index("\\emph{Lemme}")
        explanation = t.index("Le fait")
        final = t.index("Soient")
        archive = len(t)
    regions = {"opening": (opening, definition), "definition": (definition, definition_end), "lemma_heading": (lemma, explanation), "lemma_body": (lemma, explanation), "explanation": (explanation, final), "final": (final, archive), "admin_archive": (0, opening)}
    for key, (a, b) in regions.items():
        SCOPES[f"witness_{witness}:{key}"] = tref(path, a, b)
    if witness == "C":
        SCOPES["witness_C:archive_comment"] = tref(path, archive, len(t))

REGIONS = {
    "A": {"opening": ["P1"], "definition": ["D1"], "lemma_heading": ["P2"], "lemma_body": ["P3"], "explanation": ["P4"], "final": ["P5"], "admin_archive": ["ADMIN", "ARCHIVE"]},
    "B": {"opening": ["B024-P01", "B024-G01"], "definition": ["B024-DISPLAY"], "lemma_heading": ["B024-P02"], "lemma_body": ["B024-P03"], "explanation": ["B024-P04"], "final": ["B024-P05"], "admin_archive": ["B024-ADMIN", "B024-ARCHIVE"]},
    "C": {"opening": ["opening"], "definition": ["definition"], "lemma_heading": ["lemma"], "lemma_body": ["lemma"], "explanation": ["explanation"], "final": ["final_paragraph"], "admin_archive": ["ADMIN", "archive_comment"]},
}

# The index groups source location labels. It supplies no equality of readings,
# physical-count parent, source selection, confidence or ink result.
TABLE = """opening|opening first word|D01|B024-D01|C024-D01
opening|Pi exponent|D02|B024-C01|C024-R01
opening|union lower index and upper mark|D03|B024-C02a|C024-R02
opening|opening E index and upper mark|D04|B024-C02b|C024-R02b
opening|separate point above soit|||C024-D05
opening|opening ens punctuation|D05|B024-C03|C024-R03
opening|notées accent|D06||
opening|cancelled On wording and terminal state|D07|B024-C04|C024-R04,C024-D32
opening|second Considérons la|||
opening|old underlined heading and old quantifier|D08|B024-D02a|C024-D02
opening|raised relation capitalization and insertion scope|D09|B024-D02b,B024-D02c|C024-D03
opening|upper cancellation and underline paths|D10|B024-D02d|C024-D04
definition|overwritten predecessor with live continuation|D11|B024-C05|C024-R05,C024-D33
definition|high point above predecessor|D12|B024-D03|C024-D06
definition|definition arrow label|D13|B024-C06|C024-R06
definition|complete double-shaft arrow||B024-D04|C024-D07
definition|complete defining relation and RHS|||
lemma_heading|underlined Lemme and adjoining phrase|||
lemma_heading|complete tuple correction states|D14|B024-C07|C024-R07,C024-D08
lemma_body|lemma left rule|D15|B024-D07|C024-D09
lemma_body|separate pale left trace|D16|B024-D08|C024-D10
lemma_body|ens de or ens des phrase|D17|B024-C08|C024-R08
lemma_body|high point in sommets||B024-D05|
lemma_body|preposition before arêtes||B024-D06|
lemma_body|arêtes complete noun and accents|D18|B024-C09a|C024-R09
lemma_body|punctuation after arêtes|D19|B024-C09b|C024-R09p
lemma_body|cancelled Cette relation|D20||
lemma_body|complete Le/Ce and upper return|D21|B024-C16|C024-R16,C024-D11
lemma_body|underlined arbre and endpoint|D22|B024-D09|C024-D12
explanation|le/Le before fait|D23|B024-C17|C024-R17
explanation|pale trace below-left of fait|D25|B024-D11|C024-D14
explanation|complete qu'on a phrase and final point|D24|B024-D10|C024-D13
explanation|live Il cancelled existe/ex live y a|D26|B024-C10,B024-D12|C024-R10,C024-D15,C024-D16
explanation|pale entry between y and a||B024-D13|C024-D17
explanation|first exactement and full two-U condition|||
explanation|condition b full l'ens/l'une phrase|D27|B024-D14|C024-D18
final|lower paragraph initial Soient/Soit|D28|B024-C11|C024-R11
final|first complete signed Sigma|D29|B024-D15|C024-D2701
final|second complete signed Sigma|D30|B024-D16|C024-D2702
final|comp. and connexes/conn|D31|B024-C18|C024-R18
final|point below deux|D32||
final|complete précise word and accents|D33|B024-D17|
final|en and colon after précise|D34|B024-D18|C024-D19
final|a before lower adverb|D35||
final|exactemt/exactement|D36|B024-C12|C024-R12
final|live underlined un|D37|B024-D19|C024-D20
final|first complete signed U and sign state|D38|B024-C13|C024-R13,C024-D34
final|two small neighbours of first U sign|D39|B024-D20|C024-D29
final|contenu ending|D40|B024-D21|C024-D21
final|contained-in complete Sigma sign and index|D41|B024-C14|C024-R14,C024-D2703
final|first tel que|D42|B024-D22|C024-D22
final|first lower barred U with local sign states|D43||C024-D28
final|E index and point in first lower formula|D44||C024-D30
final|parenthetical de equals|D45|B024-D23|C024-D23
final|parenthetical complete signed Sigma|D46||C024-D2704
final|right-edge word before definit|D47|B024-C15|C024-R15
final|complete definit verb|D48|B024-D24|C024-D24
final|definit final-i upper components||B024-D25|
final|un before final inclusion|D49|B024-D26|C024-D25
final|final inclusion and complete Sigma||B024-D27|C024-D2705
final|final tel que|D50|B024-D28|C024-D26
final|complete final barred-U formula|||
final|final parenthesis and comma|D51||
admin_archive|scan wrapper and archive numeral|D52||C024-D31"""

DIFF_INDEX = {r: {v["id"]: i for i, v in enumerate(REPORTS[r]["differences"])} for r in "ABC"}
ASSIGNED = {r: {} for r in "ABC"}
UNION = []
for ordinal, line in enumerate(TABLE.splitlines(), 1):
    region, label, *mapping = line.split("|")
    uid = f"SRC024-L{ordinal:02}"
    row = {"source_locus_id": uid, "source_location_label": label, "region": region, "role": "source_only_clerical_correspondence", "readers": {}, "witnesses": {}, "root_evidence": []}
    for r, cell in zip("ABC", mapping):
        ids = cell.split(",") if cell else []
        rp = f"out/readers/024/{r}/report.json"
        localgroups = []
        for ident in ids:
            index = DIFF_INDEX[r][ident]
            assert ident not in ASSIGNED[r]
            ASSIGNED[r][ident] = uid
            entry = REPORTS[r]["differences"][index]
            localgroups += entry.get("source_groups", [])
            if entry.get("source_group"):
                localgroups.append(entry["source_group"])
        row["readers"][r] = {
            "semantic_role": f"reader_{r}_own_complete_source",
            "complete_TeX_scope_ids": [r + ":" + x for x in REGIONS[r][region]],
            "raw_difference_entry_refs": [jref(rp, f"/differences/{DIFF_INDEX[r][x]}") for x in ids],
            "raw_difference_ids": ids,
            "own_complete_group_ids": list(dict.fromkeys(localgroups)),
            "difference_list_absence_basis": jref(rp, "/differences") if not ids else None,
            "reading_rule": "The actual complete own TeX scope and own group/state metadata supply this reader's reading. The difference list supplies its raw report only; its silence supplies no reading or absence of ink.",
        }
    for w in "CH":
        row["witnesses"][w] = {"semantic_role": f"public_witness_{w}_own_literal", "complete_TeX_scope_ids": [f"witness_{w}:{region}"], "rule": "Keep this witness's own literal words, formula spellings, line breaks, deletion/insertion states and local marker scope. Reader report paraphrases remain raw provenance."}
    if region == "admin_archive":
        row["witnesses"]["C"]["complete_TeX_scope_ids"].append("witness_C:archive_comment")
    UNION.append(row)

for r in "ABC":
    assert set(ASSIGNED[r]) == set(DIFF_INDEX[r]), (r, set(DIFF_INDEX[r]) - set(ASSIGNED[r]))
for row in UNION:
    for r in "ABC":
        assert all(k in SCOPES for k in row["readers"][r]["complete_TeX_scope_ids"])
        assert all(k in GROUPS[r] for k in row["readers"][r]["own_complete_group_ids"])

# Additional own-source groups remain attached where another reader's list is silent.
EXTRA = {52:{"B":["B024-P05"]},53:{"B":["B024-P05"]},55:{"B":["B024-S04"]},58:{"A":["A024-G21"]},60:{"C":["C024-S05"]},63:{"B":["B024-P05"]},27:{"B":["B024-P03"],"C":["C024-G07"]}}
for ordinal, readers in EXTRA.items():
    for r, ids in readers.items():
        bucket = UNION[ordinal - 1]["readers"][r]["own_complete_group_ids"]
        bucket[:] = list(dict.fromkeys(bucket + ids))

INDEX = {}
for r in "ABC":
    rp = f"out/readers/024/{r}/report.json"
    report = REPORTS[r]
    INDEX[r] = {"complete_report_ref": REGISTRY[rp], "all_report_sections": {}, "differences": [], "doubts": [], "inventory": []}
    for key, value in report.items():
        pointer = "/" + S.ptr_part(key)
        section = {"complete_raw_section_ref": jref(rp, pointer)}
        if isinstance(value, list):
            section["entry_refs"] = [jref(rp, pointer + "/" + str(i)) for i in range(len(value))]
        elif isinstance(value, dict):
            section["entry_refs"] = {k: jref(rp, pointer + "/" + S.ptr_part(k)) for k in value}
        INDEX[r]["all_report_sections"][key] = section
    for i, entry in enumerate(report["differences"]):
        INDEX[r]["differences"].append({"id": entry["id"], "source_locus_id": ASSIGNED[r][entry["id"]], "complete_raw_entry_ref": jref(rp, f"/differences/{i}")})
    for i, entry in enumerate(report["doubts"]):
        did = entry["id"][2:] if r == "A" and entry["id"].startswith("Q-") else entry["id"]
        INDEX[r]["doubts"].append({"id": entry["id"], "source_locus_id": ASSIGNED[r].get(did), "complete_raw_entry_ref": jref(rp, f"/doubts/{i}")})
    for i, entry in enumerate(report["inventory"]):
        ids = entry.get("source_refs", entry.get("source_groups", []))
        if entry.get("source_group"):
            ids = ids + [entry["source_group"]]
        INDEX[r]["inventory"].append({"id": entry["element"], "complete_raw_entry_ref": jref(rp, f"/inventory/{i}"), "raw_own_source_ids": ids, "hand_is_raw_reader_value": True, "containing_and_component_scopes_remain_separate": True})

cat_path = "out/checks/scan024_C_doubt_catalog.json"
cat = PARSERS[cat_path].value
ORIGINAL_ROWS = []
for i, row in enumerate(cat["rows"]):
    ident = row["source_id"]
    witnesses = "packets/024/C_doubts.txt"
    assert TEXTS[witnesses][row["char_start"]:row["char_end"]] == row["literal"]
    item = {"source_id": ident, "canonical_catalog_entry_ref": jref(cat_path, f"/rows/{i}"), "exact_original_table_row_ref": tref(witnesses, row["char_start"], row["char_end"]), "canonical_source_parts": row["source_parts"], "reader_raw_row_refs": {}}
    for r, key in [("A", "source_doubt_rows"), ("B", "original_C_doubt_rows"), ("C", "C_source_doubts")]:
        entries = REPORTS[r][key]
        matches = [j for j, x in enumerate(entries) if x["id"] == ident]
        assert len(matches) == 1
        item["reader_raw_row_refs"][r] = jref(f"out/readers/024/{r}/report.json", f"/{key}/{matches[0]}")
    ORIGINAL_ROWS.append(item)

CAUTIONS = [
    {"id":"C-SCOPE-01", "observation":"C source_map invisible_annotation is true for phantom itself only. Nested deleted/unsure entries retain false, while their exact containing phantom remains in TeX. That Boolean supplies no claim of printed visibility for descendants.", "source_ref":REGISTRY["out/readers/024/C/make_source_map.py"], "examples":[jref("out/readers/024/C/source_map.json","/wrappers/4"),jref("out/readers/024/C/source_map.json","/wrappers/5"),jref("out/readers/024/C/source_map.json","/wrappers/6")]},
    {"id":"C-SCOPE-02", "observation":"Raw geometry reading fields D08, D11, D16, D17, D32, D33 and D34 carry primary forms while their own linked complete groups retain additional states or local qualifications. Preserve raw fields as provenance and use the complete own group/state scope for reader C.", "source_entry_ids":["C024-D08","C024-D11","C024-D16","C024-D17","C024-D32","C024-D33","C024-D34"], "complete_group_ids":["C024-G06","C024-G08","C024-G11","C024-G02","C024-G04","C024-U01"]},
    {"id":"C-SCOPE-03", "observation":"C inventory records his hand on containing text/whole-glyph rows and undetermined hand on separate child marks. Whole-group assembly must carry those existing component scopes; it cannot infer a new component hand from its container.", "examples":[jref("out/readers/024/C/report.json","/inventory/13"),jref("out/readers/024/C/report.json","/inventory/15"),jref("out/readers/024/C/report.json","/inventory/17"),jref("out/readers/024/C/report.json","/inventory/18")]},
    {"id":"C-SCOPE-04", "observation":"Original C024-R13 has its first-U local sign and its contextual later barred-U mention. C map lists U01 and U02; C report explicitly retains only R13 as the original local entry and maps the later occurrence to D28. Keep the canonical original row/part and the contextual later occurrence separate.", "report_ref":jref("out/readers/024/C/report.json","/C_source_doubts/12"), "map_ref":jref("out/readers/024/C/source_map.json","/original_doubt_source_spans/12")},
    {"id":"ALL-SCOPE-05", "observation":"Raw C/H fields inside reader reports include paraphrases, shortened TeX spellings and absence descriptions. Their exact role is the reader's report. Public C/H fields take their own complete literal packet spans, including H's source line breaks and local ill marker. No cross-role equal-string substitution is authorized.", "witness_C_ref":REGISTRY["packets/024/C.tex"], "witness_H_ref":REGISTRY["packets/024/H.tex"]},
]

result = {
    "scan":24,
    "source_only":True,
    "status":"complete source-entry union for root review; no ink outcome or final assembly",
    "offset_convention":"Zero-based Python Unicode-character and UTF-8 byte offsets, half-open; one-based inclusive lines; every reference includes complete source hash and local span hash.",
    "union_convention":"The source-location union is clerical. It retains every reader difference/doubt/inventory/source-choice section and every complete map group/component through exact immutable pointers. Its rows are not physical-count loci and supply no confidence or root choice. Complete own-source scopes support report-silent readings; a missing report entry supplies no reading. All source alternatives remain attributed to their own reader/witness.",
    "sources":REGISTRY,
    "complete_TeX_scopes":SCOPES,
    "complete_own_groups":GROUPS,
    "report_coverage":INDEX,
    "source_locus_union":UNION,
    "original_C_rows":ORIGINAL_ROWS,
    "source_role_cautions":CAUTIONS,
    "H_local_marker_catalog_ref":REGISTRY["out/checks/scan024_H_marker_catalog.json"],
    "S_scope":{"source_only":True,"exact_scope_ref":REGISTRY["out/checks/scan024_S_scope.json"],"local_scan024_quote_supplied":False,"root_ink_choice_applied":False},
    "coverage_validation":{"every_raw_difference_has_one_clerical_locus":True,"every_raw_doubt_has_exact_pointer":True,"every_raw_inventory_has_exact_pointer":True,"every_report_field_has_complete_exact_section_pointer":True,"all_18_original_C_rows_and_canonical_parts_preserved":True,"all_readers_present_in_every_union_row":True,"every_TeX_scope_and_group_literal_matches_own_source":True},
    "limits":"No image or crop was opened. No OCR, compilation, rendering, installation, research, mathematical normalization, theorem check or image/coordinate computation was performed. No reader original was edited. No final page, public record, count, confidence or approval was supplied.",
}
info = S.put("union_v01.json", result)
summary = {
    "source_union":info,
    "scope":"Every complete raw report section; all differences, doubts and inventory entries; complete A/B/C map groups; all canonical original C rows; exact complete own-source TeX scopes; source-only S/H catalogs.",
    "source_role_cautions":CAUTIONS,
    "report_source_cardinality_only":{r:{k:len(REPORTS[r][k]) for k in ["differences","doubts","inventory"]} for r in "ABC"},
    "limits":result["limits"],
}
print(json.dumps(info,ensure_ascii=False))
print(json.dumps(S.put("union_v01_summary.json",summary),ensure_ascii=False))
