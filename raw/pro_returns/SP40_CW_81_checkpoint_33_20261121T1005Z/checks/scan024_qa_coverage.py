"""Clerical QA only. Reads text sources and writes this QA's own findings.

No image access, ink adjudication, mathematical checks, compilation, or rendering.
"""
import collections
import datetime
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
CHECKS = BASE / "out/checks"
PREFIX = CHECKS / "scan024_qa_coverage"
TEXT_CACHE = {}
JSON_CACHE = {}


def text_at(path):
    path = str(path)
    if path not in TEXT_CACHE:
        p = BASE / path
        if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".pdf", ".gif", ".webp"}:
            raise ValueError("Image/PDF access is excluded from this source-only QA")
        TEXT_CACHE[path] = p.read_bytes().decode("utf-8")
    return TEXT_CACHE[path]


def doc(path):
    path = str(path)
    if path not in JSON_CACHE:
        JSON_CACHE[path] = json.loads(text_at(path))
    return JSON_CACHE[path]


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def ptr(value, pointer):
    for part in pointer.split("/")[1:]:
        part = part.replace("~1", "/").replace("~0", "~")
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value


def walk(value, pointer=""):
    yield pointer, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, pointer + "/" + key.replace("~", "~0").replace("/", "~1"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, pointer + "/" + str(index))


def resolve(ref):
    s = text_at(ref["source_path"])
    return s[ref["character_start"]:ref["character_end_exclusive"]]


def ref_value(ref):
    return ptr(doc(ref["source_path"]), ref["json_pointer"])


input_paths = [
    "upload/PROMPT(20261120-085055).md",
    "out/briefs/source_record_brief_v07.md",
    "out/checks/scan024_root_decisions.json",
    "out/checks/scan024_root_decisions.md",
    "out/checks/scan024_root_crop_audit.json",
    "out/checks/scan024_root_preimage_gate.json",
    "out/checks/scan024_C_doubt_catalog.json",
    "out/checks/scan024_H_marker_catalog.json",
    "out/checks/scan024_S_scope.json",
    "out/checks/scan024_source_union_v01.json",
    "out/checks/scan024_source_crosswalk_v01.jsonl",
    "out/checks/scan024_source_group_candidate_crosswalk.json",
    "out/checks/scan024_source_inventory_scope_crosswalk.json",
    "out/checks/scan024_source_row_skeleton_v01.json",
]
u = doc("out/checks/scan024_source_union_v01.json")
sk = doc("out/checks/scan024_source_row_skeleton_v01.json")
gc = doc("out/checks/scan024_source_group_candidate_crosswalk.json")
ic = doc("out/checks/scan024_source_inventory_scope_crosswalk.json")
root = doc("out/checks/scan024_root_decisions.json")
crop_audit = doc("out/checks/scan024_root_crop_audit.json")
cat = doc("out/checks/scan024_C_doubt_catalog.json")
hcat = doc("out/checks/scan024_H_marker_catalog.json")
sscope = doc("out/checks/scan024_S_scope.json")
compact = [json.loads(line) for line in text_at("out/checks/scan024_source_crosswalk_v01.jsonl").splitlines()]
errors = []


def check(ok, code, source, detail):
    if not ok:
        errors.append({"code": code, "source": source, "detail": detail})


reference_checks = {}
for name, tree in [("source_union", u), ("candidate_crosswalk", gc), ("inventory_crosswalk", ic), ("typed_skeleton", sk)]:
    count = 0
    for pointer, r in walk(tree):
        if not isinstance(r, dict) or not {"source_path", "character_start", "character_end_exclusive"} <= r.keys():
            continue
        count += 1
        source = name + "#" + pointer
        s = text_at(r["source_path"])
        start, end = r["character_start"], r["character_end_exclusive"]
        part = s[start:end]
        check(0 <= start <= end <= len(s), "span_bounds", source, r["source_path"])
        check(sha(s) == r["sha256_utf8"], "source_hash", source, r["source_path"])
        for key, expected in [
            ("span_sha256_utf8", sha(part)),
            ("utf8_byte_start", len(s[:start].encode("utf-8"))),
            ("utf8_byte_end_exclusive", len(s[:end].encode("utf-8"))),
            ("line_start", s.count("\n", 0, start) + 1),
            ("line_end", s.count("\n", 0, max(start, end - 1)) + 1),
        ]:
            if key in r:
                check(r[key] == expected, key, source, {"recorded": r[key], "actual": expected})
        if "json_pointer" in r:
            check(json.loads(part) == ref_value(r), "json_pointer_value", source, r["json_pointer"])
    reference_checks[name] = count

root_by_locus = collections.defaultdict(list)
for index, entry in enumerate(root["decisions"]):
    for locus in entry["source_loci"]:
        root_by_locus[locus].append(entry["section"])
    matches = [v for v in crop_audit["viewed_once"] if v["path"] == entry["crop_path"]]
    check(len(matches) == 1, "root_crop_unique", f"root_decisions#/decisions/{index}", entry["crop_path"])
    if matches:
        match = matches[0]
        check(match["sha256"] == entry["crop_sha256"], "root_crop_recorded_hash", entry["section"], entry["crop_path"])
        check(match["successful_display_count"] == 1, "root_crop_display_count", entry["section"], match["successful_display_count"])
        check(entry["section"] in match["decision_sections"], "root_crop_section", entry["section"], entry["crop_path"])
check(len(root["decisions"]) == crop_audit["total_distinct"] == len(crop_audit["viewed_once"]) == 30,
      "root_crop_count", "root_crop_audit", "30 root sections and 30 recorded crop references")

union_rows = {r["source_locus_id"]: r for r in u["source_locus_union"]}
skeleton_rows = {r["id"]: r for r in sk["rows"]}
compact_rows = {r["source_locus_id"]: r for r in compact[1:]}
check(set(union_rows) == set(skeleton_rows) == set(compact_rows), "locus_identity", "all_indexes", "64 identical locus identities")
coverage = []
raw_counts = {}
for who in "ABC":
    report = doc(f"out/readers/024/{who}/report.json")
    reported_diff_ids = [r["id"] for r in report["differences"]]
    attached_diff_ids = [v for row in u["source_locus_union"] for v in row["readers"][who]["raw_difference_ids"]]
    check(collections.Counter(reported_diff_ids) == collections.Counter(attached_diff_ids),
          "difference_identity", who, {"reported": reported_diff_ids, "attached": attached_diff_ids})
    doubt_ids = [r["id"] for r in report["doubts"]]
    attached_doubt_ids = [v for row in sk["rows"] for v in row["readers"][who]["raw_own_doubt_ids"]]
    check(collections.Counter(doubt_ids) == collections.Counter(attached_doubt_ids),
          "doubt_identity", who, {"reported": doubt_ids, "attached": attached_doubt_ids})
    inv_entries = [e for e in ic["entries"] if e["reader"] == who]
    check(len(inv_entries) == len(report["inventory"]), "inventory_count", who, len(inv_entries))
    check({e["complete_raw_inventory_ref"]["json_pointer"] for e in inv_entries} ==
          {f"/inventory/{i}" for i in range(len(report["inventory"]))}, "inventory_identity", who, "every raw inventory pointer")
    raw_counts[who] = {"differences": len(reported_diff_ids), "doubts": len(doubt_ids), "inventory": len(inv_entries),
                       "complete_groups": len(u["complete_own_groups"][who])}

pool = sk["source_reference_pool"]
for locus, row in union_rows.items():
    skrow = skeleton_rows[locus]
    crow = compact_rows[locus]
    has_report = any(row["readers"][who]["raw_difference_ids"] for who in "ABC")
    has_doubt = any(skrow["readers"][who]["raw_own_doubt_ids"] for who in "ABC")
    check(not (has_report or has_doubt) or bool(root_by_locus[locus]), "missing_root_section", locus, row["source_location_label"])
    for who in "ABC":
        own = row["readers"][who]
        slot = skrow["readers"][who]
        check(own["raw_difference_ids"] == slot["raw_own_difference_ids"] == crow["readers"][who]["report_ids"],
              "difference_crosswalk", locus + "/" + who, "ordered raw identities")
        check(own["complete_TeX_scope_ids"] == slot["scope_ids"] == crow["readers"][who]["complete_TeX_scope_ids"],
              "scope_crosswalk", locus + "/" + who, "ordered complete source scopes")
        check(own["own_complete_group_ids"] == slot["complete_own_group_ids"] == crow["readers"][who]["own_group_ids"],
              "group_crosswalk", locus + "/" + who, "ordered own group identities")
        for field in ["complete_own_literal_scope_refs", "raw_own_difference_refs", "raw_own_doubt_refs"]:
            for refid in slot[field]:
                ref = pool[refid]["exact_source_ref"]
                check(f"/readers/024/{who}/" in ref["source_path"], "reader_field_owner", locus + "/" + who + "/" + field, refid)
        for gid in own["own_complete_group_ids"]:
            check(gid in u["complete_own_groups"][who], "reader_group_owner", locus + "/" + who, gid)
    for who in "CH":
        for refid in skrow[who]["complete_own_literal_scope_refs"]:
            ref = pool[refid]["exact_source_ref"]
            check(ref["source_path"] == f"packets/024/{who}.tex", "witness_field_owner", locus + "/" + who, refid)
    coverage.append({"locus": locus, "label": row["source_location_label"], "root_sections": root_by_locus[locus],
                     "raw_difference_ids": {w: row["readers"][w]["raw_difference_ids"] for w in "ABC"},
                     "raw_doubt_ids": {w: skrow["readers"][w]["raw_own_doubt_ids"] for w in "ABC"}})

group_checks = []
for index, entry in enumerate(gc["entries"]):
    who, gid = entry["reader"], entry["group_id"]
    raw_ref = entry["complete_own_candidate_state_ref"]
    raw_value = ref_value(raw_ref)
    tg = sk["complete_own_group_candidate_scopes"][who][gid]
    typed_ref = pool[tg["complete_own_candidate_state_entry_ref"]]["exact_source_ref"]
    check(raw_ref == typed_ref, "typed_group_candidate_ref", gid, "exact source reference")
    for key, value in tg["raw_own_state_fields"].items():
        check(raw_value[key] == value, "typed_candidate_value", gid + "/" + key, "own raw field")
        field_ref = pool[tg["raw_state_field_refs"][key]]["exact_source_ref"]
        check(ref_value(field_ref) == value, "typed_candidate_leaf", gid + "/" + key, field_ref["json_pointer"])
    own_group = entry["own_TeX_group"]
    check(own_group == u["complete_own_groups"][who][gid], "complete_group_identity", gid, "union exact group")
    for r in [raw_ref, own_group["complete_metadata_ref"], own_group["complete_TeX_ref"]]:
        check(f"/readers/024/{who}/" in r["source_path"], "group_source_owner", gid, r["source_path"])
    for value in [raw_value.get("exact_tex"), raw_value.get("source_span", {}).get("exact_tex")]:
        if value is not None:
            check(value == resolve(own_group["complete_TeX_ref"]), "candidate_tex_literal", gid, "complete own literal")
    group_checks.append({"reader": who, "group_id": gid, "candidate_source": raw_ref["source_path"],
                         "candidate_pointer": raw_ref["json_pointer"], "source_tex_lines": [own_group["complete_TeX_ref"]["line_start"], own_group["complete_TeX_ref"]["line_end"]]})
check({(e["reader"], e["group_id"]) for e in gc["entries"]} ==
      {(w, g) for w in "ABC" for g in u["complete_own_groups"][w]}, "all_group_refs", "group_crosswalk", "all 69 own groups")

original_outcomes = collections.defaultdict(list)
for d in root["decisions"]:
    for key, value in d.get("original_C_rows", {}).items():
        original_outcomes[key].append({"root_section": d["section"], "outcome_literal": value})
canonical_ids = {r["source_id"] for r in cat["rows"]}
check(canonical_ids == set(original_outcomes) == set(sk["canonical_original_C_rows"]), "C_row_identity", "original_C_rows", "all 18 canonical rows")
original_rows = []
for index, r in enumerate(cat["rows"]):
    identity = r["source_id"]
    source = text_at(r["source_path"])
    check(source[r["char_start"]:r["char_end"]] == r["literal"], "C_exact_row_literal", identity, r["source_path"])
    check(len(original_outcomes[identity]) == 1, "C_one_parent_outcome", identity, original_outcomes[identity])
    check(r["source_parts"] == sk["canonical_original_C_rows"][identity]["canonical_source_parts"], "C_part_identity", identity, "canonical source part unchanged")
    original_rows.append({"source_id": identity, "source_line": r["line"], "root_outcomes": original_outcomes[identity],
                          "local_loci": [x["id"] for x in sk["rows"] if identity in x["original_C_source_row_ids"]],
                          "contextual_loci": [x["id"] for x in sk["rows"] if identity in x["original_C_contextual_row_ids"]]})

marker_loci = {r["id"]: r["H"]["local_marker_ids"] for r in sk["rows"] if r["H"]["local_marker_ids"]}
check(marker_loci == {"SRC024-L56": ["H024-ILL01"]}, "H_marker_scope", "typed_skeleton", marker_loci)
for marker in hcat["markers"]:
    check(text_at(hcat["source_path"])[marker["char_start"]:marker["char_end"]] == marker["literal"], "H_marker_literal", marker["marker_id"], hcat["source_path"])

findings = [
    {"id": "QA024-I01", "status": "coverage_recorded", "scope": "All 161 raw difference records and all 88 raw doubts have their original own-reader identity in the typed source index and a mapped root journal section.", "source": "out/checks/scan024_source_union_v01.json#/source_locus_union"},
    {"id": "QA024-I02", "status": "source_only_unmapped_context", "loci": ["SRC024-L17", "SRC024-L18", "SRC024-L35"], "scope": "These three loci have no dedicated root crop section. Complete A/B/C sources were inspected; their literal core defining RHS, lemma lead-in and first exactly-two passage are present. No raw difference or doubt record is attached to these three loci. Preserve them as complete consensus context in source coverage, without inventing another crop or proof event.", "source": "out/checks/scan024_source_row_skeleton_v01.json#/rows"},
    {"id": "QA024-I03", "status": "canonical_parent_scopes_preserved", "scope": "R02 keeps both index occurrences at L03/L04; R09 keeps noun/accent L25 and endpoint L26 under its original parent; R13 is the first-U sign at L47 and only contextual at L52. Root literal outcomes record two resolved rows, fifteen retained rows, and one mixed row (R09).", "source": "out/checks/scan024_root_decisions.json#/decisions"},
    {"id": "QA024-I04", "status": "own_candidate_scopes_preserved_in_typed_index", "scope": "All 69 complete own groups and every copied raw candidate/state leaf match their own exact source references. The final assembled public fields have not yet been released for this audit.", "source": "out/checks/scan024_source_row_skeleton_v01.json#/complete_own_group_candidate_scopes"},
    {"id": "QA024-I05", "status": "local_H_scope_preserved", "scope": "The sole H ill marker is attached to L56, the right-edge word preceding definit. Its marker does not attach to the verb or adjoining formulas.", "source": "out/checks/scan024_H_marker_catalog.json#/markers/0"},
    {"id": "QA024-I06", "status": "source_only_S_scope", "scope": "S catalog has zero direct scan024 reading rows and seven recorded source row scopes. Its source-only review remains outside the crop journal's local ink decisions.", "source": "out/checks/scan024_S_scope.json"},
]

result = {
    "scan": 24,
    "reviewer": "/root/qa024",
    "phase": "source coverage and canonical identities before assembled draft release",
    "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "source_only": True,
    "ink_adjudication_performed": False,
    "mathematical_check_performed": False,
    "images_opened": 0,
    "originals_and_root_authorities_edited": False,
    "inputs": {p: {"sha256_utf8": sha(text_at(p)), "bytes": len(text_at(p).encode("utf-8"))} for p in input_paths},
    "text_reference_replay_counts": reference_checks,
    "raw_reader_counts": raw_counts,
    "root_sections": len(root["decisions"]),
    "root_crop_record_consistency": "30 distinct recorded crop paths, each with one successful display and matching journal metadata; image bytes were not opened",
    "source_locus_count": len(union_rows),
    "source_loci_with_root_section": sum(bool(v["root_sections"]) for v in coverage),
    "source_locus_coverage": coverage,
    "all_complete_group_candidate_refs": group_checks,
    "canonical_C_row_coverage": original_rows,
    "H_marker_loci": marker_loci,
    "S_direct_row_count": len(sscope["direct_page_24_reading_rows"]),
    "findings": findings,
    "mechanical_errors": errors,
    "limits": "Clerical consistency only. Root remains responsible for ink decisions, approvals and counts. No assembled draft or public record was validated in this phase; no image or PDF was opened, no OCR, compilation, rendering, research, installation or mathematical proof check was performed.",
}
PREFIX.with_suffix(".json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
md = ["# Scan024 source coverage QA", "", "Scope: clerical coverage and canonical identities, before assembled draft release. Images opened: 0. Ink and mathematics decisions: none.", "", "## Results", "", f"- Exact text references replayed: {sum(reference_checks.values())} ({', '.join(f'{k}: {v}' for k, v in reference_checks.items())}).", f"- Mechanical reference/identity errors: {len(errors)}.", "- Root journal: 30 sections, with 30 once-viewed crop references consistent with the crop audit.", "- Source loci: 64; 61 carry root section references. All 161 raw reader differences and all 88 raw reader doubts have journal coverage.", "- Complete candidate/state groups: 69 (A 22, B 25, C 22); inventory identities: 132 (A 49, B 39, C 44).", "- Original C rows: all 18 parents retained, including the two index occurrences in R02, accent/punctuation scope in R09, and first-U target of R13.", "", "## Findings", ""]
for finding in findings:
    md += [f"### {finding['id']} — {finding['status']}", "", finding["scope"], "", f"Source: `{finding['source']}`.", ""]
if errors:
    md += ["## Mechanical errors", "", "```json", json.dumps(errors, ensure_ascii=False, indent=2), "```", ""]
md += ["## Audit bindings", "", f"Root journal SHA-256: `{result['inputs']['out/checks/scan024_root_decisions.json']['sha256_utf8']}`.", "", f"Source union SHA-256: `{result['inputs']['out/checks/scan024_source_union_v01.json']['sha256_utf8']}`.", "", f"Typed skeleton SHA-256: `{result['inputs']['out/checks/scan024_source_row_skeleton_v01.json']['sha256_utf8']}`.", "", "The JSON companion retains every locus-to-section mapping, all 69 exact candidate-source pointers, original C row outcomes, input hashes, and reference replay counts. The source originals, frozen source index and root authorities remain unchanged.", ""]
PREFIX.with_suffix(".md").write_text("\n".join(md), encoding="utf-8")
print(json.dumps({"mechanical_errors": errors, "reference_counts": reference_checks, "reader_counts": raw_counts,
                  "root_covered_loci": result["source_loci_with_root_section"], "findings_json_sha256": sha(PREFIX.with_suffix('.json').read_bytes().decode('utf-8')),
                  "findings_md_sha256": sha(PREFIX.with_suffix('.md').read_bytes().decode('utf-8'))}, ensure_ascii=False, indent=2))
