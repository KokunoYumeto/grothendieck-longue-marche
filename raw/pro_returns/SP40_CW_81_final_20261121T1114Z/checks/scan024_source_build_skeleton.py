#!/usr/bin/env python3
"""Prepare a role-aware source skeleton; all selected outcome fields stay unset."""
from pathlib import Path
import json
import hashlib
import importlib.util
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("source_support", HERE / "scan024_source_support.py")
S = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S)
BASE = S.BASE
FROZEN = HERE / "scan024_source_union_v01.json"
FROZEN_HASH = "c933d2361514761da9d136ec31c2427dce502e968dfca43b61786d6f01b7fea0"
assert S.sha(FROZEN.read_bytes()) == FROZEN_HASH
U = json.loads(FROZEN.read_bytes())
TEXTS = {p: (BASE / p).read_bytes().decode("utf-8") for p in U["sources"]}
PARSERS = {p: S.JSONSpans(t) for p, t in TEXTS.items() if p.endswith(".json")}
REFS = {}
LOOKUP = {}
VALIDATIONS = []


def ref_for(path, pointer):
    a, b = PARSERS[path].spans[pointer]
    return S.ref(U["sources"][path], TEXTS[path], a, b, pointer)


def add_ref(ref, role, scope_kind):
    """Deduplicate a reference only within its exact own-source semantic role."""
    key = json.dumps([role, scope_kind, ref], ensure_ascii=False, sort_keys=True)
    if key in LOOKUP:
        return LOOKUP[key]
    ident = f"REF{len(REFS) + 1:04}"
    p = ref["source_path"]
    a, b = ref["character_start"], ref["character_end_exclusive"]
    t = TEXTS[p]
    assert S.sha(t.encode("utf-8")) == ref["sha256_utf8"]
    assert len(t[:a].encode("utf-8")) == ref["utf8_byte_start"]
    assert len(t[:b].encode("utf-8")) == ref["utf8_byte_end_exclusive"]
    if "span_sha256_utf8" in ref:
        assert S.sha(t[a:b].encode("utf-8")) == ref["span_sha256_utf8"]
    value = {"semantic_role": role, "scope_kind": scope_kind, "exact_source_ref": ref}
    # Small exact excerpts are exposed directly. Longer scopes retain complete
    # proven pointers to the already-read immutable source, without shortening.
    if len(t[a:b]) <= 420:
        value["exact_literal"] = t[a:b]
    REFS[ident] = value
    LOOKUP[key] = ident
    VALIDATIONS.append({"ref_id": ident, "source_path": p, "source_character_span": [a, b], "literal_sha256_utf8": S.sha(t[a:b].encode("utf-8")), "source_role": role})
    return ident


GROUPS = {}
for r in "ABC":
    GROUPS[r] = {}
    report_path = f"out/readers/024/{r}/report.json"
    report = PARSERS[report_path].value
    meta_section = "public_graphical_readings" if r == "A" else "source_choices" if r == "B" else None
    for gid, source in U["complete_own_groups"][r].items():
        record = {
            "reader": r,
            "source_group_id": gid,
            "complete_own_TeX_ref": add_ref(source["complete_TeX_ref"], f"reader_{r}_actual_TeX", "complete_literal_group"),
            "complete_own_map_entry_ref": add_ref(source["complete_metadata_ref"], f"reader_{r}_source_map", "complete_group_metadata_and_components"),
        }
        if meta_section:
            matches = [(i, x) for i, x in enumerate(report[meta_section]) if x["id"] == gid]
            assert len(matches) == 1
            i, meta = matches[0]
            mp = report_path
            pointer = f"/{meta_section}/{i}"
            omitted_literal_fields = {"exact_tex", "source_span"}
        else:
            mp = "out/readers/024/C/group_metadata.json"
            pointer = "/" + gid
            meta = PARSERS[mp].value[gid]
            omitted_literal_fields = set()
        record["complete_own_candidate_state_entry_ref"] = add_ref(ref_for(mp, pointer), f"reader_{r}_own_candidate_state_metadata", "complete_raw_candidate_state_entry")
        # The exact original field names and values remain in their own role.
        # Components listed together in a source field remain listed together;
        # this script creates no new alternative combinations or shared scopes.
        record["raw_own_state_fields"] = {k: v for k, v in meta.items() if k not in omitted_literal_fields}
        record["raw_state_field_refs"] = {k: add_ref(ref_for(mp, pointer + "/" + S.ptr_part(k)), f"reader_{r}_own_candidate_state_metadata", "exact_original_field") for k in record["raw_own_state_fields"]}
        GROUPS[r][gid] = record


ORIGINAL_C = {}
for original in U["original_C_rows"]:
    ident = original["source_id"]
    ORIGINAL_C[ident] = {
        "source_id": ident,
        "canonical_source_parts": original["canonical_source_parts"],
        "exact_witness_C_doubt_row_ref": add_ref(original["exact_original_table_row_ref"], "public_witness_C_original_doubt_row", "complete_original_row_with_compound_scope"),
        "canonical_source_identity_ref": add_ref(original["canonical_catalog_entry_ref"], "root_source_identity_catalog", "complete_original_row_identity"),
        "reader_raw_outcome_refs": {r: add_ref(ref, f"reader_{r}_raw_C_row_report", "raw_reported_row_status_and_scope") for r, ref in original["reader_raw_row_refs"].items()},
    }


def raw_entry_id(ref):
    p = ref["source_path"]
    a, b = ref["character_start"], ref["character_end_exclusive"]
    return json.loads(TEXTS[p][a:b])


def reported_c_ids(entry):
    ids = entry.get("C_source_doubt_ids", entry.get("C_source_doubt_rows", []))[:]
    if entry.get("source_row_id"):
        ids.append(entry["source_row_id"])
    return ids


def literal_ref(role, literal):
    path = f"packets/024/{role}.tex"
    text = TEXTS[path]
    assert text.count(literal) == 1, (role, literal, text.count(literal))
    a = text.index(literal)
    return S.ref(U["sources"][path], text, a, a + len(literal))


# Exact, complete local witness phrases. Every backslash, space, source line
# break and cancellation/insertion state below is checked against that witness.
WITNESS_LOCAL = {
    "C": {
        "opening_word": r"Considérons la partition",
        "opening_formula": r"la partition $\Pi_I^{\unsure{\circ|0}}$ de $X\setminus\bigcup_{\unsure{\alpha'|i}\in I}E_{\alpha'}$,",
        "classes": r"soit $S$ l'\unsure{ens|ens.} des classes, notées $U_s$ $(s\in S)$.",
        "cancelled_On": r"\deleted{\unsure{On a}} Considérons la",
        "upper_revision": r"Considérons la \deleted{\uline{Lemme} $\forall i\in I$,} \inserted{Relation $R$ entre $S$ et $I$}",
        "lemma_heading": r"\uline{Lemme} Cette relation fait de $(S,I\unsure{)\deleted{R})|\deleted{)}{,}R)}$",
        "sommets": r"un graphe strict ayant $S$ comme \unsure{ens des|ens de} sommets, $I$ comme ens.",
        "aretes": r"$I$ comme ens. d'\unsure{arêtes|arètes|aretes}.) \deleted{Cette relation}",
        "graphe_arbre": r"\deleted{Cette relation} \unsure{Le|Ce} graphe est un \uline{arbre}",
        "explanation_opening": r"\unsure{le|Le} fait qu'on a un graphe strict signifie que a) $\forall i\in I$,",
        "Il_existe_ya": r"Il \deleted{\unsure{existe|ex}} y a exactement deux $U_s$ tels que",
        "condition_a": r"exactement deux $U_s$ tels que $\overline{U_s}\cap E_i\ne\varnothing$,",
        "condition_b": r"et b) $i$ est caractérisé par l'ens de ces deux $U_s$.",
        "signed_components": r"\unsure{Soient|Soit} $\Sigma_i^+,\Sigma_i^-$ les deux comp. \unsure{connexes} de $X\setminus E_i$,",
        "refinement": "alors a) se précise en : il y a",
        "adverb_un_U": r"il y a \unsure{exactement|exactemt} \uline{un} $U_{s_{\unsure{+|-}}}$",
        "first_containment": r"$U_{s_{\unsure{+|-}}}$ contenu dans $\Sigma_i^{\unsure{+|-}}$ tel que $\overline{U_{s_+}}\cap E_i\ne\varnothing$",
        "first_barred_formula": r"tel que $\overline{U_{s_+}}\cap E_i\ne\varnothing$",
        "parenthesis_opening": r"(et de $=$ pour $\Sigma_i^-$,",
        "edge_word": r"\unsure{dé|qui}",
        "final_verb_inclusion": r"définit un $U_{s_-}\subset\Sigma_i^-$ tel que",
        "final_formula_endpoint": r"tel que $\overline{U_{s_-}}\cap E_i\ne\varnothing$),",
    },
    "H": {
        "opening_word": r"Considérons la partition",
        "opening_formula": "la partition $\\Pi_{I}^{0}$ de $X\\smallsetminus\\bigcup_{i\\in\nI}E_{i}$,",
        "classes": r"soit $S$ l'ens.\ des classes, notées $U_{s}$ ($s\in S$).",
        "cancelled_On": r"\struck{On} Considérons la",
        "upper_revision": "Considérons la \\struck{relation $R$ entre} \\struck{$\\forall\ni\\in I$,} \\add{relation $R$ entre} $S$ et $I$",
        "lemma_heading": r"\emph{Lemme} Cette relation fait de $(S,I,R)$",
        "sommets": "un graphe strict ayant $S$\ncomme ens.\\ de sommets, $I$ comme ens.\\ ",
        "aretes": "$I$ comme ens.\\ d'arêtes. \\struck{Cette relation}",
        "graphe_arbre": "\\struck{Cette relation}\nCe graphe est un \\emph{arbre}.",
        "explanation_opening": r"Le fait que c'est un graphe strict signifie que a) $\forall i\in I$,",
        "Il_existe_ya": "\\struck{il y a} il y a exactement deux $U_{s}$ tels que",
        "condition_a": "exactement deux $U_{s}$ tels que\n$\\overline{U_{s}}\\cap E_{i}\\neq\\emptyset$,",
        "condition_b": "et b) $i$ est caractérisé par\nl'une de ces deux $U_{s}$.",
        "signed_components": "Soient $\\Sigma_{i}^{+}$, $\\Sigma_{i}^{-}$ les deux comp.\\ conn.\\ de\n$X\\smallsetminus E_{i}$,",
        "refinement": "alors a) se précise ainsi : il y a",
        "adverb_un_U": "il y a exactement\n\\struck{une} une $U_{s_{+}}$",
        "first_containment": "$U_{s_{+}}$ contenue dans $\\Sigma_{i}^{+}$ telle que\n$\\overline{U_{s_{+}}}\\cap E_{i}\\neq\\emptyset$",
        "first_barred_formula": "telle que\n$\\overline{U_{s_{+}}}\\cap E_{i}\\neq\\emptyset$",
        "parenthesis_opening": "(et de même pour\n$\\Sigma_{i}^{-}$,",
        "edge_word": r"\ill{}",
        "final_verb_inclusion": "définit une $U_{s_{-}}\\subset\\Sigma_{i}^{-}$ telle\nque",
        "final_formula_endpoint": "telle\nque $\\overline{U_{s_{-}}}\\cap E_{i}\\neq\\emptyset$),",
    },
}
LOCAL_NAMES = {
    1:"opening_word",2:"opening_formula",3:"opening_formula",4:"opening_formula",5:"classes",6:"classes",7:"classes",8:"cancelled_On",9:"upper_revision",10:"upper_revision",11:"upper_revision",12:"upper_revision",
    18:"lemma_heading",19:"lemma_heading",22:"sommets",23:"sommets",24:"aretes",25:"aretes",26:"aretes",27:"graphe_arbre",28:"graphe_arbre",29:"graphe_arbre",
    30:"explanation_opening",31:"explanation_opening",32:"explanation_opening",33:"Il_existe_ya",34:"Il_existe_ya",35:"condition_a",36:"condition_b",
    37:"signed_components",38:"signed_components",39:"signed_components",40:"signed_components",41:"signed_components",42:"refinement",43:"refinement",44:"adverb_un_U",45:"adverb_un_U",46:"adverb_un_U",47:"first_containment",48:"first_containment",49:"first_containment",50:"first_containment",51:"first_barred_formula",52:"first_barred_formula",53:"first_barred_formula",54:"parenthesis_opening",55:"parenthesis_opening",56:"edge_word",57:"final_verb_inclusion",58:"final_verb_inclusion",59:"final_verb_inclusion",60:"final_verb_inclusion",61:"final_formula_endpoint",62:"final_formula_endpoint",63:"final_formula_endpoint",
}
LOCAL_REF_IDS = {w: {name: add_ref(literal_ref(w, literal), f"public_witness_{w}_actual_TeX", "complete_local_literal_phrase_or_state") for name, literal in fields.items()} for w, fields in WITNESS_LOCAL.items()}


ROWS = []
for original in U["source_locus_union"]:
    ident = original["source_locus_id"]
    ordinal = int(ident.rsplit("L", 1)[1])
    row = {
        "id": ident,
        "location": original["source_location_label"],
        "region": original["region"],
        "source_only": True,
        "C": {},
        "H": {},
        "readers": {},
        "original_C_source_row_ids": [],
        "original_C_contextual_row_ids": ["C024-R13"] if ordinal == 52 else [],
        "final": None,
        "evidence": None,
        "alternatives": None,
        "confidence": None,
        "hand": None,
        "role": None,
        "kind": None,
        "marked_in_H": None,
        "main_adjudicated": False,
        "main_approved": False,
    }
    cids = []
    for w in "CH":
        ws = original["witnesses"][w]
        row[w] = {
            "semantic_role": f"public_witness_{w}_own_literal",
            "complete_own_literal_scope_refs": [add_ref(U["complete_TeX_scopes"][x], f"public_witness_{w}_actual_TeX", "complete_witness_phrase_or_frame_context") for x in ws["complete_TeX_scope_ids"]],
            "scope_ids": ws["complete_TeX_scope_ids"],
            "source_state_rule": "The exact literal scope retains its original source punctuation, line breaks, deletion/insertion macros and uncertainty scope. Reader-reported paraphrases are retained under that reader's raw report references.",
        }
        if ordinal in LOCAL_NAMES:
            row[w]["containing_context_scope_refs"] = row[w]["complete_own_literal_scope_refs"]
            row[w]["complete_own_literal_scope_refs"] = [LOCAL_REF_IDS[w][LOCAL_NAMES[ordinal]]]
            row[w]["local_phrase_name"] = LOCAL_NAMES[ordinal]
    for r in "ABC":
        own = original["readers"][r]
        raw_refs = own["raw_difference_entry_refs"]
        for ref in raw_refs:
            cids += reported_c_ids(raw_entry_id(ref))
        doubts = [x for x in U["report_coverage"][r]["doubts"] if x["source_locus_id"] == ident]
        own_scopes = [add_ref(U["complete_TeX_scopes"][x], f"reader_{r}_actual_TeX", "complete_containing_prose_or_frame_context") for x in own["complete_TeX_scope_ids"]]
        row["readers"][r] = {
            "semantic_role": f"reader_{r}_own_reading_and_own_candidates",
            "complete_own_literal_scope_refs": own_scopes,
            "scope_ids": own["complete_TeX_scope_ids"],
            "complete_own_group_ids": own["own_complete_group_ids"],
            "raw_own_difference_ids": own["raw_difference_ids"],
            "raw_own_difference_refs": [add_ref(ref, f"reader_{r}_raw_report", "complete_raw_difference_entry_including_reported_witness_fields") for ref in raw_refs],
            "raw_own_doubt_ids": [x["id"] for x in doubts],
            "raw_own_doubt_refs": [add_ref(x["complete_raw_entry_ref"], f"reader_{r}_raw_report", "complete_raw_doubt_entry") for x in doubts],
            "difference_list_absence_basis_ref": add_ref(own["difference_list_absence_basis"], f"reader_{r}_raw_report", "complete_inspected_difference_list") if own["difference_list_absence_basis"] else None,
            "scope_rule": "Complete group candidates apply to their own complete group. The local report/doubt reference supplies this row's sub-scope. The containing context preserves adjoining words and live/cancelled continuations; its other local qualifications remain attached to their own source loci. Report silence supplies no reading."
        }
    row["original_C_source_row_ids"] = list(dict.fromkeys(cids))
    for c in row["original_C_source_row_ids"]:
        assert c in ORIGINAL_C
    row["C"]["original_C_candidate_scope_ids"] = row["original_C_source_row_ids"]
    row["C"]["original_C_contextual_scope_ids"] = row["original_C_contextual_row_ids"]
    # H's catalogue has one locally identified marker. Its copied source scope
    # remains separate from the broad containing final-paragraph context.
    hpath = "out/checks/scan024_H_marker_catalog.json"
    row["H"]["local_marker_ids"] = ["H024-ILL01"] if ordinal == 56 else []
    row["H"]["complete_marker_catalog_ref"] = add_ref(U["sources"][hpath], "public_witness_H_marker_catalog", "complete_source_marker_catalog")
    if ordinal == 56:
        row["H"]["exact_local_marker_ref"] = add_ref(ref_for(hpath, "/markers/0"), "public_witness_H_marker_catalog", "exact_local_marker_identity_and_scope")
    ROWS.append(row)


# No selected reading, confidence, hand, kind, marker flag or root evidence is
# created by this source scaffold. Every reader role remains explicit.
for row in ROWS:
    assert list(row["readers"]) == list("ABC")
    for field in ["final", "evidence", "alternatives", "confidence", "hand", "role", "kind", "marked_in_H"]:
        assert row[field] is None
    for r, reading in row["readers"].items():
        assert reading["complete_own_literal_scope_refs"]
        assert all(g in GROUPS[r] for g in reading["complete_own_group_ids"])

RESULT = {
    "scan": 24,
    "format": "scan024-role-aware-source-row-skeleton-v1",
    "source_only": True,
    "brief_authority": U["sources"]["out/briefs/source_record_brief_v07.md"],
    "frozen_source_union": {"path": str(FROZEN.relative_to(BASE)), "sha256_utf8": FROZEN_HASH},
    "schema_note": "C/H and readers.A/B/C are role-aware exact-source objects in this source scaffold. Their references are complete literal own-source scopes, not generated public reading strings. Root's selected final/evidence and selected hand/confidence remain null. The public builder receives its final reader strings only through later authorized assembly from these exact own sources.",
    "reference_resolution": "Each reference has an immutable own-source path/hash and zero-based, half-open character/UTF-8 byte spans. Longer scopes are retained by complete pointers. Each original candidate field is reproduced under its original field name and has an exact field reference. No equality-based substitution crosses semantic roles.",
    "source_reference_pool": REFS,
    "complete_own_group_candidate_scopes": GROUPS,
    "canonical_original_C_rows": ORIGINAL_C,
    "rows": ROWS,
    "source_role_cautions": U["source_role_cautions"],
    "source_only_S_scope": U["S_scope"],
    "main_adjudicated": False,
    "main_approved": False,
    "limits": "Source correspondence and exact reference verification only. No image/crop access, ink decision, source selection, physical-count assignment, final confidence/hand assignment, rendering, compilation, coordinate/image computation or mathematical transformation.",
}
INFO = S.put("row_skeleton_v01.json", RESULT)
readable = HERE / "scan024_source_row_skeleton_v01.jsonl"
lines = [json.dumps({"format": RESULT["format"], "skeleton_path": INFO["path"], "skeleton_sha256_utf8": INFO["sha256_utf8"], "schema_note": RESULT["schema_note"], "reference_pool": "source_reference_pool", "candidate_scope_pool": "complete_own_group_candidate_scopes"}, ensure_ascii=False, separators=(",", ":"))]
lines += [json.dumps(row, ensure_ascii=False, separators=(",", ":")) for row in ROWS]
readable.write_text("\n".join(lines) + "\n", encoding="utf-8")
compact = HERE / "scan024_source_row_skeleton_v01_compact.jsonl"
row_defaults = {k: ROWS[0][k] for k in ["source_only", "final", "evidence", "alternatives", "confidence", "hand", "role", "kind", "marked_in_H", "main_adjudicated", "main_approved"]}
reader_defaults = {r: {k: ROWS[0]["readers"][r][k] for k in ["semantic_role", "scope_rule"]} for r in "ABC"}
witness_defaults = {w: {k: ROWS[0][w][k] for k in ["semantic_role", "source_state_rule"]} for w in "CH"}
compact_rows = []
restored_rows = []
for row in ROWS:
    short = {k: v for k, v in row.items() if k not in row_defaults}
    short["readers"] = {r: {k: v for k, v in row["readers"][r].items() if k not in reader_defaults[r]} for r in "ABC"}
    for w in "CH":
        short[w] = {k: v for k, v in row[w].items() if k not in witness_defaults[w]}
    restored = {**row_defaults, **short}
    restored["readers"] = {r: {**reader_defaults[r], **short["readers"][r]} for r in "ABC"}
    for w in "CH":
        restored[w] = {**witness_defaults[w], **short[w]}
    assert restored == row
    compact_rows.append(short)
    restored_rows.append(restored)
compact_header = {"source_only": True, "skeleton_path": INFO["path"], "skeleton_sha256_utf8": INFO["sha256_utf8"], "reconstruction": "Merge row_defaults into each row; merge reader_defaults[reader] into each row.readers[reader]; merge witness_defaults[witness] into each row[witness]. These exact merges reconstruct all 64 original row values. Source/candidate reference pools remain in the full skeleton.", "row_defaults": row_defaults, "reader_defaults": reader_defaults, "witness_defaults": witness_defaults}
compact.write_text("\n".join(json.dumps(x, ensure_ascii=False, separators=(",", ":")) for x in [compact_header] + compact_rows) + "\n", encoding="utf-8")
AUDIT = {
    "source_only": True,
    "skeleton": INFO,
    "readable_rows": {"path": str(readable.relative_to(BASE)), "sha256_utf8": S.sha(readable.read_bytes())},
    "compact_rows": {"path": str(compact.relative_to(BASE)), "sha256_utf8": S.sha(compact.read_bytes()), "exact_semantic_row_reconstruction": restored_rows == ROWS},
    "frozen_union_hash_unchanged": S.sha(FROZEN.read_bytes()) == FROZEN_HASH,
    "all_64_correspondence_ids_preserved": [x["id"] for x in ROWS] == [x["source_locus_id"] for x in U["source_locus_union"]],
    "every_row_has_own_A_B_C_sources": True,
    "selected_outcome_fields_all_unset": True,
    "canonical_original_C_row_ids_and_parts_preserved": True,
    "reference_verifications": VALIDATIONS,
    "source_role_policy": "Reference interning keys include the exact semantic role, source path, span and source hash. The script neither rewrites raw sources nor substitutes equal strings between roles.",
}
AINFO = S.put("row_skeleton_v01_audit.json", AUDIT)
print(json.dumps({"skeleton": INFO, "readable_rows": AUDIT["readable_rows"], "compact_rows": AUDIT["compact_rows"], "audit": AINFO, "verified_reference_objects": len(VALIDATIONS)}, ensure_ascii=False))
