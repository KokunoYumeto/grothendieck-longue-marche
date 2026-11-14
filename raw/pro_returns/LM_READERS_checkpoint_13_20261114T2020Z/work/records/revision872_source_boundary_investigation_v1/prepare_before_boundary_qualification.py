#!/usr/bin/env python3
"""Stage the three accepted label-only refinements without changing live inputs."""
from __future__ import annotations

from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import shutil
import tempfile

import editorial
import layout_repairs
import mechanical_repairs
from audit_layout_repair_integrity import commands, MARKS

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "work/layout_probes/revision872_source_preflight_v1"
BASE = ROOT / "work/layout_probes/revision872_baseline_v1"
SPECS = (
    ("scan027_region_parenthesis", "revision872_scan027_region_parenthesis_v1",
     "266b6d23d0da89bf88d9cdc88910618ae70879f732f07bd7bba19e76a36c7474",
     "ce4e552d4163c6ef7869fe044605b4891ee46bc9854d72bb5e254cd5d54e1db4"),
    ("scan085_minus1", "revision872_scan085_minus1_v1",
     "7ba8148b09b9a63759b1338ef69c59643420aafc41dd0750fa89056c647558dd",
     "db372a615b72878c5d7dd09becbe12f8077b536d0042ea41a1c3a23b86b3a782"),
    ("scan085_zero", "revision872_scan085_zero_v1",
     "176f81a17ed58cca9efc252f5d0ef4a14c148f3376cd4e6fbffb1aee5752112d",
     "bc3e02af5d76778b296ae6a65163f81ba7eaca2797d0552731bf5ea3af1c7a7d"),
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def pin(path):
    return dict(path=path.relative_to(ROOT).as_posix(), sha256=sha(path), bytes=path.stat().st_size)


def exact(ref):
    path = ROOT / ref["path"]
    assert path.resolve().is_relative_to(ROOT)
    assert sha(path) == ref["sha256"], ref["path"]
    if "bytes" in ref:
        assert path.stat().st_size == ref["bytes"], ref["path"]
    return path


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def references(value):
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and isinstance(value.get("sha256"), str):
            yield value
        for child in value.values():
            yield from references(child)
    elif isinstance(value, list):
        for child in value:
            yield from references(child)


def proof(spec):
    name, directory, handoff_sha, root_sha = spec
    folder = ROOT / "work/layout_probes" / directory
    handoff_path, root_path = folder / "HANDOFF.json", folder / "ROOT_REVIEW.json"
    assert sha(handoff_path) == handoff_sha and sha(root_path) == root_sha
    handoff, root_review = read(handoff_path), read(root_path)
    assert root_review["status"].startswith("ACCEPTED_FOR_")
    for reference in list(references(handoff)) + list(references(root_review)):
        exact(reference)
    rows = read(exact(handoff["candidate"]))
    assert len(rows) == 2 and {row["language"] for row in rows} == {"fr", "en"}
    assert len({row["id"] for row in rows}) == 1
    validation = read(exact(handoff["validation"]))
    assert validation["candidate"] == handoff["candidate"]
    assert validation["actual_after_forms"] == 6
    assert all(validation[field] == 0 for field in ("compile_errors", "overfull_boxes", "missing_characters"))
    compiled = read(exact(validation["compile_validation"]))
    actual = read(exact(validation["actual_observations"]))
    preservation = read(exact(validation["source_preservation"]))
    assert preservation["status"] == "PASS_EXACT_SOURCE_TOKEN_PRESERVATION"
    assert len(preservation["checks"]) == 2
    for check in preservation["checks"]:
        assert all(check[field] is True for field in (
            "exact_full_package_inverse", "annotated_full_inverse", "editorial_fields_except_offsets_identical"))
    for document in (validation, compiled, actual, preservation):
        for reference in references(document):
            exact(reference)
    forms = {(row["language"], row["form"]): row for row in compiled["forms"]}
    observations = {(row["language"], row["form"]): row for row in actual["observations"] if row.get("phase") == "after"}
    expected = {(language, form) for language in ("fr", "en") for form in (0, 1, 2)}
    assert set(forms) == set(observations) == expected and len(compiled["forms"]) == 6
    for key, form in forms.items():
        assert all(form[field] == 0 for field in (
            "compile_exit_code", "error_count", "overfull_count", "missing_character_count"))
        observation = observations[key]
        assert observation["status"] == "PASS_ACTUAL_NATIVE_VISUAL_REVIEW"
        assert observation["reviewer"] and observation["observation"] and observation["images"]
        assert observation["pdf"] == form["pdf"] and observation["tex"] == form["tex"]
        after_images = [page["native"] for page in form["pages"] if page["phase"] == "after"]
        assert any(image["sha256"] == observed["sha256"] for image in after_images for observed in observation["images"])
    normalized = []
    for row in rows:
        source = exact(dict(path=row["source_path"], sha256=row["source_sha256"]))
        raw_bytes = source.read_bytes()
        raw = raw_bytes.decode()
        assert raw[row["source_offset_start"]:row["source_offset_end"]] == row["source_old"]
        assert raw_bytes[row["source_byte_start"]:row["source_byte_end"]].decode() == row["source_old"]
        assert row["source_old"] == row["old"] and raw.count(row["old"]) == 1
        assert row["variants"] == [dict(old=row["old"], new=row["new"])]
        normalized.append({**{field: row[field] for field in (
            "id", "language", "package", "scan", "kind", "reason", "variants")},
            "stage": "after_geometry", "candidate_source": name})
    return rows, normalized, dict(name=name, handoff=pin(handoff_path), root_review=pin(root_path),
        candidate=handoff["candidate"], validation=handoff["validation"], finding=handoff["finding"],
        actual_observations=validation["actual_observations"], source_preservation=validation["source_preservation"],
        accepted_after_forms=6, publication_confirmation_pending=True)


def inverse(text, rows):
    for row in reversed(rows):
        assert text.count(row["new"]) == 1
        text = text.replace(row["new"], row["old"], 1)
    return text


def stage():
    assert not OUT.exists() and not BASE.exists(), "Preserve previous attempts; use a new namespace."
    freeze_path = ROOT / "work/data/layout_release_checkpoint.json"
    build_path = ROOT / "work/data/final_build_inputs.json"
    freeze, build = read(freeze_path), read(build_path)
    assert freeze["records"] == build["source_records"] == 872
    assert freeze["exact_pagination_records"] == 524
    assert build["status"] == "TWO_PASS_BUILD_COMPLETE_INPUTS_UNCHANGED" and build["changed_inputs"] == []
    for name, digest in {**build["source_dependencies"], **build["assembly_dependencies"]}.items():
        assert sha(ROOT / name) == digest, name
    candidates, additions, accepted = [], [], []
    for spec in SPECS:
        rows, normalized, item = proof(spec)
        candidates.extend(rows); additions.extend(normalized); accepted.append(item)
    keys = {(row["id"], row["language"]) for row in candidates}
    assert len(keys) == len(candidates) == 6
    old_labels = read(ROOT / "work/data/layout_label_clearances.json")
    old_applied = read(ROOT / "work/data/layout_repairs_applied.json")
    assert len(old_labels) == 116 and len(old_applied) == 872
    assert not keys & {(row["id"], row["language"]) for row in old_applied}
    predicted_data = {"layout_label_clearances.json": old_labels + additions}
    for name in ("layout_expected_matches.json", "layout_geometry_expected_matches.json"):
        expected = read(ROOT / "work/data" / name)
        changed = copy.deepcopy(expected)
        increments = Counter((row["language"], row["package"], row["scan"]) for row in candidates)
        matched = set()
        for row in changed:
            key = row["language"], row["package"], row["scan"]
            if key in increments:
                row["expected_changes"] += increments[key]
                matched.add(key)
        assert matched == set(increments) and len(matched) == 4
        predicted_data[name] = changed
    scopes = sorted({(row["package"], row["language"]) for row in candidates})
    prior = {}
    for package, language in scopes:
        source = ROOT / ("sources/fr/texts/" + package + ".tex" if language == "fr"
                         else "sources/en/packages/" + package + "_en.tex")
        raw = source.read_text()
        mechanical = mechanical_repairs.repair(raw, package, language)[0]
        for label, source_view in (("raw", raw), ("mechanical", mechanical)):
            prior[package, language, label] = source_view, layout_repairs.repair(source_view, package, language)[0]
    predicted_scopes = {(row["package"], row["language"]): [] for row in old_applied}
    for row in old_applied:
        predicted_scopes[row["package"], row["language"]].append(row)
    audit = []
    original_root = layout_repairs.ROOT
    with tempfile.TemporaryDirectory(prefix="revision872-preflight-", dir=ROOT / "work") as temporary:
        isolated = Path(temporary)
        data = isolated / "work/data"
        data.mkdir(parents=True)
        (isolated / "sources").symlink_to(ROOT / "sources", target_is_directory=True)
        for name in freeze["sha256"]:
            source = ROOT / name
            if source.suffix == ".json":
                shutil.copyfile(source, data / source.name)
        for name, content in predicted_data.items():
            (data / name).write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n")
        try:
            layout_repairs.ROOT = isolated
            for (package, language, view), (source_view, before) in sorted(prior.items()):
                after, records = layout_repairs.repair(source_view, package, language)
                local = [row for row in candidates if (row["package"], row["language"]) == (package, language)]
                assert inverse(after, local) == before
                assert commands(after) == commands(before)
                assert all(before.count("\\" + mark + "{") == after.count("\\" + mark + "{") for mark in MARKS)
                before_annotated, before_entries, _ = editorial.annotate(before, package, language)
                after_annotated, after_entries, _ = editorial.annotate(after, package, language)
                assert inverse(after_annotated, local) == before_annotated
                fields = ("id", "kind", "manuscript", "corrected", "corrected_tex", "math_mode", "inherited_doubt")
                project = lambda entries: [{field: entry.get(field) for field in fields} for entry in entries]
                assert project(before_entries) == project(after_entries)
                if view == "raw":
                    old_records = predicted_scopes[package, language]
                    assert [row for row in records if (row["id"], row["language"]) not in keys] == old_records
                    predicted_scopes[package, language] = records
                    for candidate in local:
                        applied = next(row for row in records if row["id"] == candidate["id"])
                        for field in ("source_line", "source_offset_start", "source_offset_end", "source_byte_start", "source_byte_end", "source_old", "old", "new"):
                            assert applied[field] == candidate[field], (candidate["id"], language, field)
                audit.append(dict(package=package, language=language, view=view, status="PASS",
                    exact_full_source_inverse=True, exact_annotation_inverse=True,
                    editorial_projection_unchanged=True, source_marks_preserved=True,
                    named_commands_preserved=True, exact_replay_and_raw_source_offsets=True,
                    before_sha256=hashlib.sha256(before.encode()).hexdigest(),
                    after_sha256=hashlib.sha256(after.encode()).hexdigest(), records=len(records)))
        finally:
            layout_repairs.ROOT = original_root
    predicted = [row for language in ("fr", "en") for package in layout_repairs.COVERAGE
                 for row in predicted_scopes[package, language]]
    assert len(predicted) == 878
    assert [row for row in predicted if (row["id"], row["language"]) not in keys] == old_applied
    assert Counter(row["language"] for row in predicted) == {"fr": 439, "en": 439}
    for name, digest in {**build["source_dependencies"], **build["assembly_dependencies"]}.items():
        assert sha(ROOT / name) == digest, name
    baseline_names = set(build["source_dependencies"]) | set(build["assembly_dependencies"]) | {
        "work/data/layout_release_checkpoint.json", "work/data/final_build_inputs.json",
        "work/data/layout_repairs_applied.json", "work/data/layout_probe_validation.json",
        "work/data/layout_semantic_command_audit.json", "work/data/layout_exact_patches.json",
        "work/data/layout_pagination_reconciliation.json", "work/records/LAYOUT_REPAIR_DETAILS.tsv",
        "work/records/REVISION872_ADDITIVE_RELEASE_GATE_PASS.json", "work/scripts/revision864_additive_release_gate.py",
        "work/scripts/write_release_report.py"}
    BASE.mkdir(parents=True)
    files = []
    for name in sorted(baseline_names):
        source = ROOT / name; destination = BASE / "files" / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        assert sha(destination) == sha(source)
        files.append(dict(original=pin(source), preserved=pin(destination)))
    write(BASE / "MANIFEST.json", dict(schema="revision872-preserved-source-baseline-v1",
        status="PINNED_PREINTEGRATION_REVISION872", revision=872, files=files))
    OUT.mkdir(parents=True)
    targets = []
    for name, content in predicted_data.items():
        write(OUT / name, content)
        targets.append(dict(destination="work/data/" + name, before=pin(ROOT / "work/data" / name), proposed=pin(OUT / name)))
    write(OUT / "predicted_applied.json", predicted)
    write(OUT / "source_audit.json", dict(status="PASS", results=audit, affected_language_package_entries=4))
    write(OUT / "normalized_additions.json", additions)
    manifest = dict(schema="revision872-label-refinement-manifest-v1",
        status="ACCEPTED_EXACT_PAIRED_PROBES_AWAIT_INSTALL", base_records=872,
        expected_source_records=878, added_source_records=6, superseded_source_records=0,
        accepted_site_count=3, base_pagination_records=524, expected_pagination_records=524,
        observations_generated_by_script=False, pending_candidates=[], items=accepted,
        baseline_manifest=pin(BASE / "MANIFEST.json"), source_audit=pin(OUT / "source_audit.json"),
        predicted_applied=pin(OUT / "predicted_applied.json"), normalized_additions=pin(OUT / "normalized_additions.json"),
        files=targets, script=pin(Path(__file__)), existing_applied_rows_exact_and_order_preserved=True,
        existing_label_rows_exact_and_order_preserved=True, manuscript_sources_changed=False,
        production_dependencies_unchanged=True, publication_closure_claim=False,
        historical_gate=pin(ROOT / "work/records/REVISION872_ADDITIVE_RELEASE_GATE_PASS.json"))
    write(OUT / "HANDOFF.json", manifest)
    print(json.dumps(dict(status="PASS_EXACT_ADDITIVE_SOURCE_PREFLIGHT", handoff=pin(OUT / "HANDOFF.json"),
                         records=878, source_views=len(audit), unchanged_old_records=872)), flush=True)


if __name__ == "__main__":
    stage()
