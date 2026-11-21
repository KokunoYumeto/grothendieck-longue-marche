#!/usr/bin/env python3
"""Bounded Q01-Q08 metadata closure only; never reruns the selected-source audit."""
from __future__ import annotations

import collections
import copy
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
OLD_MAP = "79e4b3af563b5ff38df37e3b7b317f7bad9c48f6b1151fe7c2f6046bd367dcf9"
NEW_MAP = "f235a85c0e71d1dc1f519e72abe2db85a7ff2d2a9ee6460fb3c2435d551f0bc4"
TEX = "96772b7d5d36792f72827807deffaa39e746d1876f771e9dd498cbcf0238ddce"
EXPECTED = {
    "scan021_final_draft.tex": TEX,
    "scan021_qa_frozen_final_draft.tex": TEX,
    "scan021_final_source_map.json": NEW_MAP,
    "scan021_qa_frozen_final_source_map.json": OLD_MAP,
    "scan021_record_draft.json": "382810422b9f27ccc871d1066f3d6d240a42b5239875b36f9280f29574a50b83",
    "scan021_qa_frozen_record_draft.json": "f12eb52fa52759e4693dcaecf840f26779ea06bb9966dea281744db5e2bd3ca0",
    "scan021_source_audit.md": "c575c4567a76c9b588ebf5633e4ab87447d6b12cbcb9d2355ebae5ef79708ac1",
    "scan021_source_qa_results.json": "12d8738adf349784d792faa9007e27361727f12e60c8306ea130cd40c39f7a88",
    "scan021_source_qa.py": "4f12e46b765aa7309ddaf9fb4249e9e45a446637dbeacf199b66fb7284d9fc4c",
    "scan021_map_bounded_repair_v01.json": "2852226eac0220ae3dcd681261f62b0d53392595d1d86fc73466a6aa0ee8d40e",
    "scan021_record_bounded_repair_v01.json": "ec94b423229636bfba6f56c90db4cfd3230fcb0919687880ff38d355a45f311f",
    "scan021_root_source_review.md": "034036a7a63552c4edf7147b40e029cef50c1996567d087898cef8b65b78b7b3",
}
errors: list[str] = []
checks: list[str] = []


def check(condition: bool, description: str) -> None:
    (checks if condition else errors).append(description)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name: str):
    return json.loads((BASE / name).read_text())


def parts(pointer: str) -> list[str]:
    return [p.replace("~1", "/").replace("~0", "~") for p in pointer.lstrip("/").split("/")]


MISSING = object()


def at(obj, pointer: str):
    for part in parts(pointer):
        if isinstance(obj, list):
            obj = obj[int(part)]
        else:
            if part not in obj:
                return MISSING
            obj = obj[part]
    return obj


def put(obj, pointer: str, value, present: bool = True) -> None:
    path = parts(pointer)
    for part in path[:-1]:
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    key = int(path[-1]) if isinstance(obj, list) else path[-1]
    if present:
        obj[key] = copy.deepcopy(value)
    else:
        del obj[key]


actual_hashes = {name: sha(BASE / name) for name in EXPECTED}
for name, expected in EXPECTED.items():
    check(actual_hashes[name] == expected, "frozen hash: " + name)

om = read("scan021_qa_frozen_final_source_map.json")
nm = read("scan021_final_source_map.json")
old = read("scan021_qa_frozen_record_draft.json")
new = read("scan021_record_draft.json")
ml = read("scan021_map_bounded_repair_v01.json")
rl = read("scan021_record_bounded_repair_v01.json")

# Apply only the eight logged map fields and compare the complete JSON values.
map_forward, map_inverse = copy.deepcopy(om), copy.deepcopy(nm)
map_paths = set()
for patch in ml["field_patches"]:
    p = patch["pointer"]
    check(p not in map_paths, "unique map patch: " + p)
    map_paths.add(p)
    check(at(om, p) == patch["before"] and at(nm, p) == patch["after"], "map before/after: " + p)
    put(map_forward, p, patch["after"])
    put(map_inverse, p, patch["before"])
check(map_forward == nm and map_inverse == om, "map forward and inverse replay; all other values unchanged")
check(map_paths == {"/selected_groups/3/decision_ids", "/selected_groups/7/decision_ids"}
      | {f"/selected_unit_transfers/{i}/scope" for i in range(6)}, "exact authorized eight map fields")

# Check the explicit old/new inventory identity permutation without geometry work.
order = rl["inventory_order_change"]
old_ids = [x["element"] for x in old["inventory"]]
new_ids = [x["element"] for x in new["inventory"]]
check(order["old_order"] == old_ids and order["new_order"] == new_ids, "logged inventory orders match snapshots")
check(len(old_ids) == len(new_ids) == len(set(new_ids)) == 58 and set(old_ids) == set(new_ids), "all 58 inventory identities retained once")
check(order["permutation"] == [{"element": e, "old_position": i + 1, "new_position": new_ids.index(e) + 1}
                               for i, e in enumerate(old_ids)], "exact 58-identity old/new permutation")
check(new_ids[-1] == "021.ARCHIVE", "archive-comment inventory remains last")

# Every record patch is checked at both snapshot pointers; apply it before reordering.
forward, inverse = copy.deepcopy(old), copy.deepcopy(new)
old_paths, new_paths = set(), set()
finding_counts = collections.Counter()
for patch in rl["field_changes"]:
    op, np = patch["old_pointer"], patch["new_pointer"]
    finding_counts[patch["finding"]] += 1
    check(op not in old_paths and np not in new_paths, "unique record patch: " + patch["identity_pointer"])
    old_paths.add(op)
    new_paths.add(np)
    bp, ap = patch.get("before_present", True), patch.get("after_present", True)
    check((at(old, op) == patch["before"] if bp else at(old, op) is MISSING)
          and (at(new, np) == patch["after"] if ap else at(new, np) is MISSING),
          "record before/after: " + patch["identity_pointer"])
    put(forward, op, patch["after"], ap)
    put(inverse, np, patch["before"], bp)
    if patch["finding"] == "current map binding":
        check(patch["before"] == OLD_MAP and patch["after"] == NEW_MAP,
              "literal map-hash substitution: " + np)
        check(patch["identity_pointer"].endswith("/source_map_sha256")
              or patch["identity_pointer"] == "/selected_source_map/sha256", "binding field scope: " + np)
    elif patch["finding"] == "bounded repair provenance":
        check(patch["identity_pointer"] == "/bounded_source_metadata_repair" and not bp and ap,
              "single added bounded-repair provenance field")
    else:
        check(patch["finding"] in {"Q01", "Q03", "Q04", "Q05", "Q06", "Q08"},
              "named current metadata finding: " + patch["identity_pointer"])

frows = {x["element"]: x for x in forward["inventory"]}
irows = {x["element"]: x for x in inverse["inventory"]}
forward["inventory"] = [frows[e] for e in new_ids]
inverse["inventory"] = [irows[e] for e in old_ids]
check(forward == new and inverse == old, "record exact forward/inverse replay; no unlogged changes")
expected_counts = {"current map binding": 1296, "bounded repair provenance": 1,
                   "Q01": 8, "Q03": 86, "Q04": 12, "Q05": 14, "Q06": 1, "Q08": 16}
check(dict(finding_counts) == expected_counts and len(rl["field_changes"]) == 1434,
      "record patch finding counts")

# Named current-field semantics and their exact mirrors.
groups = {x["id"]: x for x in nm["selected_groups"]}
rgroups = {x["id"]: x for x in new["selected_graphical_groups"]}
decisions = {x["id"]: x for x in new["decisions"]}
inventory = {x["element"]: x for x in new["inventory"]}
for group, decision, element in [("C021-G02a", "L021-13", "021.G04"), ("B021-G03", "L021-18", "021.G08")]:
    check(groups[group]["decision_ids"] == rgroups[group]["decision_ids"] == [decision], "Q01 map/record reverse link " + group)
    check(group in decisions[decision]["actual_final_group_ids"]
          and inventory[element]["related_decision_ids"] == [decision], "Q01 decision/inventory reverse link " + group)
    for ref in inventory[element]["root_decision_sources"]:
        source = (ROOT / ref["path"]).read_text()
        excerpt = source[ref["char_start"]:ref["char_end"]]
        check(excerpt == ref["excerpt"] and hashlib.sha256(excerpt.encode()).hexdigest() == ref["literal_sha256_utf8"],
              "Q01 added exact journal attachment " + element)

for transfer in nm["selected_unit_transfers"]:
    child, parent = groups[transfer["group"]], groups[transfer["parent"]]
    check(transfer["old_literal"] == transfer["source"]["literal"], "Q02 original literal declaration " + transfer["group"])
    check(any(transfer["new_literal"] in s for s in child["tikz_declaration_lines"])
          and any(transfer["new_literal"] in s for s in parent["tikz_declaration_lines"]),
          "Q02 named parent and nested selected declarations " + transfer["group"])
    check("(x_new,y_new)=(x_old,y_old)" in transfer["scope"]
          and transfer["new_literal"] in transfer["scope"]
          and transfer["parent"] in transfer["scope"]
          and "source pointers" in transfer["scope"], "Q02 explicit copied-coordinate and parent-unit statement " + transfer["group"])

expected_true = {"L021-01", "L021-14", "L021-15", "L021-18", "L021-19"}
expected_false_changes = {"L021-20", "L021-45", "L021-46", "L021-68"} | {f"L021-{i}" for i in range(30, 41)}
check({d["id"] for d in new["decisions"] if d["marked_in_H"]} == expected_true, "Q03 exact five H doubt flags")
changed_flags = {a["id"] for a, b in zip(old["decisions"], new["decisions"]) if a["marked_in_H"] != b["marked_in_H"]}
check(changed_flags == expected_false_changes, "Q03 exact fifteen H doubt flag changes")
check(sum(a["marked_in_H_basis"] != b["marked_in_H_basis"] for a, b in zip(old["decisions"], new["decisions"])) == 71,
      "Q03 all 71 local source bases updated")

for di, qi in [(42, 27), (52, 32)]:
    d, q, coverage = new["decisions"][di], new["doubts"][qi], new["source_locus_coverage"][di]
    check(d["readers"] == q["readers"] == coverage["readers"], "Q04/Q05 exact A/B/C current mirrors " + d["id"])
    check(d["evidence"] == q["reason"], "Q04/Q05 exact evidence/doubt mirror " + d["id"])
check("tiny pale point" in decisions["L021-43"]["evidence"]
      and "tiny pale point" in inventory["021.G24"]["first_words_or_objects"], "Q04 selected tiny point explicit")
check(new["doubts"][32]["reading"] == decisions["L021-53"]["final"], "Q05 final/doubt upright reading mirror")
for value in [decisions["L021-53"]["final"], decisions["L021-53"]["evidence"],
              inventory["021.G28"]["first_words_or_objects"]]:
    check("upright" in value and "point-only" not in value, "Q05 selected upright wording")
check(decisions["L021-65"]["mathematical_consequence"] ==
      r"The final corollary line writes comp. de $X\setminus\Sigma_\alpha$; H gives comp. de $X\setminus E_\alpha$.",
      "Q06 attributed literal source-symbol correction")
mixed = {"021.04", "021.08", "021.12", "021.17", "021.G03", "021.G10", "021.G15", "021.G27"}
for element in mixed:
    check(inventory[element]["hand"] == "his hand for the main writing; undetermined hand for the detached trace(s)"
          and "remains undetermined" in inventory[element]["hand_scope"], "Q08 explicit mixed hand scope " + element)

# Companion files receive current map bindings only; compare every other value unchanged.
companion_results = []
for item in rl["companion_output_changes"]:
    before_path, after_path = ROOT / item["preserved_before_path"], ROOT / item["path"]
    check(sha(before_path) == item["before_sha256"] and sha(after_path) == item["after_sha256"],
          "companion frozen hashes " + item["path"])
    before, after = json.loads(before_path.read_text()), json.loads(after_path.read_text())
    binding_paths = []

    def replace_bindings(obj, pointer=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                p = pointer + "/" + key.replace("~", "~0").replace("/", "~1")
                if key == "source_map_sha256" and value == OLD_MAP:
                    obj[key] = NEW_MAP
                    binding_paths.append(p)
                else:
                    replace_bindings(value, p)
        elif isinstance(obj, list):
            for i, value in enumerate(obj):
                replace_bindings(value, pointer + "/" + str(i))

    replace_bindings(before)
    check(before == after, "companion exact current-map binding-only change " + item["path"])
    companion_results.append({"path": item["path"], "binding_count": len(binding_paths),
                              "before_sha256": item["before_sha256"], "after_sha256": item["after_sha256"]})

# These are unchanged-value checks covered by inverse replay, not new broad-source checks.
check(old["counts"] == new["counts"] == rl["preserved_counts"], "count/confidence object unchanged")
check(new["counts"]["C"] == 45 and new["counts"]["H"] == 24, "retained physical totals C45/H24")
check(old["check_events"] == new["check_events"] == [], "mathematical check events remain empty")
check(new["bounded_source_metadata_repair"]["first_pass_audit"]["sha256"] == actual_hashes["scan021_source_audit.md"],
      "initial audit path still resolves to its recorded unchanged hash")

result = {
    "scope": "Only root-authorized Q01-Q08 metadata changes, exact inventory permutation, current mirrors and map-hash bindings against retained snapshots.",
    "status": "pass" if not errors else "remaining defects",
    "input_sha256": actual_hashes,
    "map_field_patch_count": len(ml["field_patches"]),
    "record_field_patch_count": len(rl["field_changes"]),
    "record_field_findings": dict(finding_counts),
    "inventory_order_change": order,
    "companion_binding_results": companion_results,
    "unchanged_counts": new["counts"],
    "preserved_C_outcomes_from_repair_log": rl["preserved_C_outcomes"],
    "true_H_doubt_mark_ids": sorted(expected_true),
    "changed_H_doubt_mark_ids": sorted(changed_flags),
    "checks_passed": len(checks),
    "errors": errors,
    "initial_audit_and_result_preserved_byte_identically": True,
    "broad_audit_rerun": False,
    "images_opened_or_hashed": False,
    "rendering_or_geometry_or_mathematical_checks_performed": False,
    "selected_approval_fields_changed": False,
    "root_approval_claimed": False,
    "script_sha256": sha(Path(__file__).resolve()),
}
output = BASE / "scan021_source_closure_v01.json"
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"status": result["status"], "errors": errors, "checks_passed": len(checks),
                  "map_fields": len(ml["field_patches"]), "record_fields": len(rl["field_changes"]),
                  "companion_bindings": companion_results, "result_sha256": sha(output)}, ensure_ascii=False))
raise SystemExit(1 if errors else 0)
