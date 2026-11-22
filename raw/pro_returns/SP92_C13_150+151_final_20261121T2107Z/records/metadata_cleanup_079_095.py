#!/usr/bin/env python3
"""Synchronize the specifically audited stale metadata; never change source readings.

Authority: parent-approved cleanup of the exact issues reported by reader_c.
Inputs: current page/record files and finalized root crop notes only.
No scan, witness, frozen TSV, comparison file, aggregate, or TeX engine is used.
Run with --apply to write; otherwise validate and report the proposed changes.
"""
from __future__ import annotations

import argparse
import copy
import datetime
import hashlib
import json
from pathlib import Path
import re

WORK = Path("/workspace/scratch/d7279cb02214/SP92_C13_150+151_work")
RECORD_PAGES = (81, 82, 83, 84, 85, 87, 88, 90, 91, 94, 95)
PROTECTED_KEYS = {"C", "H", "first", "second", "first_reading",
                  "second_reading", "second_boxes"}
original_bytes: dict[Path, bytes] = {}
original_json: dict[Path, object] = {}
documents: dict[Path, object] = {}
edits: list[dict] = []
root_notes: dict[int, dict] = {}


def record_path(n: int) -> Path:
    return WORK / "records" / f"150_scan{n:03d}.json"


def load_document(path: Path):
    if path not in documents:
        raw = path.read_bytes()
        original_bytes[path] = raw
        original_json[path] = json.loads(raw)
        documents[path] = copy.deepcopy(original_json[path])
    return documents[path]


def record(n: int):
    return load_document(record_path(n))


def root(n: int, box: str):
    if n not in root_notes:
        path = WORK / "second" / f"150_scan{n:03d}_root_crop_notes.json"
        root_notes[n] = json.loads(path.read_text(encoding="utf-8"))
    return root_notes[n][box]


def source(n: int, box: str) -> str:
    return f"second/150_scan{n:03d}_root_crop_notes.json#{box}"


def locate(document, keys):
    cursor = document
    for key in keys[:-1]:
        cursor = cursor[key]
    return cursor, keys[-1]


def set_path(path: Path, keys: tuple, value, evidence: str):
    cursor, key = locate(load_document(path), keys)
    old = cursor[key]
    if old == value:
        return
    assert not any(k in PROTECTED_KEYS for k in keys if isinstance(k, str)), keys
    cursor[key] = value
    edits.append({"file": str(path.relative_to(WORK)), "path": list(keys),
                  "old": old, "new": value, "authority": evidence})


def put(n: int, keys: tuple, value, box: str):
    set_path(record_path(n), keys, value, source(n, box))


def replace(n: int, keys: tuple, old: str, new: str, box: str):
    cursor, key = locate(record(n), keys)
    current = cursor[key]
    if old not in current:
        assert new in current, (n, keys, "expected text absent", old)
        return
    assert current.count(old) == 1, (n, keys, "non-unique replacement", old)
    put(n, keys, current.replace(old, new, 1), box)


def note(n: int, old: str, new: str, box: str):
    replace(n, ("notes",), old, new, box)


# 081: the superscripted canceled identity and the final de/donc doubt.
note(81,
     r"- The cancelled formula was reread in full, rather than only its last subscript. The exposed ending resembles J\cap J', but the beginning is crossed too heavily to certify a complete formula. C's full alternatives therefore remain.",
     r"- The canceled identity is now read with its L/L-prime superscripts and J/J-prime subscripts. The first raised L and initial NB remain locally uncertain; the earlier alternatives without superscripts are superseded by the final blind adjudication.",
     "B11")
note(81,
     "The final isolated word likewise remains de, without completing it to donc.",
     "The final isolated word remains uncertain between de and donc; neither ending is certified.",
     "B20")

# 082: the already-audited literal I in the coideal conclusion.
note(82,
     "- The lower L in *L est un coidéal* is overtraced but still has the L foot. No legible previous letter was invented beneath it.",
     "- The lower capital in *I est un coidéal* has the upper and lower bars of I, as established in the blind adjudication. The literal I is retained; no legible previous letter is invented beneath its retracing.",
     "B13")
put(82, ("deletion_insertion_review", 8, "item"), "Overtraced lower I", "B13")
put(82, ("deletion_insertion_review", 8, "state"),
    "The final blind adjudication identifies upper and lower bars of I, matching the later I and contrasting with the bottom-line L. The retracing does not establish a separately readable canceled token.", "B13")
put(82, ("deletion_insertion_review", 8, "attachment"),
    "Subject of the literal I est un coidéal de I′.", "B13")

# 083: main-display 69 and the local proespace/old-t state doubt.
note(83, "contains (69), the phrase équiv. d’homotopie",
     "contains the phrase équiv. d’homotopie", "B13")
note(83, "The handwritten formula labels on this page are (68) and the marginal (69).",
     "The handwritten formula labels on this page are (68) and (69); (69) belongs to the main restricted-union display.", "B13")
put(83, ("changes", 25, "evidence"), root(83, "B13")["evidence"], "B13")
note(83,
     "- The first p of proespace is heavily retraced. The rest of the word is readable. No separate underlying cancelled letter can be isolated, so no additional guessed glyph is supplied.",
     "- The rest of proespace is readable. Its tall initial and transverse crossing leave a local uncertainty between a retraced p and an older canceled t; the current transcription preserves proespace versus canceled-t-plus-proespace without certifying the older letter.",
     "B03")
put(83, ("deletion_insertion_review", 10, "state"),
    root(83, "B03")["evidence"], "B03")
put(83, ("deletion_insertion_review", 10, "reading"),
    r"\unsure{proespace|\deleted{t}proespace}", "B03")

# 084: the canceled au lieu de and the live des proespaces.
put(84, ("deletion_insertion_review", 10, "final"),
    root(84, "B13")["final"], "B13")
note(84,
     "The cancelled les/Vijk, recollement and avec les flèches de retain their doubts.",
     "The cancelled les/Vijk, recollement and au lieu de retain their doubts.",
     "B13")
replace(84, ("changes", 19, "evidence"),
        "after de proespaces", "after des proespaces", "B10")
replace(84, ("deletion_insertion_review", 6, "state"),
        "following de proespaces", "following des proespaces", "B10")
replace(84, ("deletion_insertion_review", 7, "attachment"),
        "after de proespaces", "after des proespaces", "B10")
replace(84, ("inventory", 12, "position"),
        "Above de proespaces", "Above des proespaces", "B10")
note(84, "attaches after de proespaces", "attaches after des proespaces", "B10")

# 085: On trouve and the first map index s_j.
note(85, "On a même, sauf erreur", "On trouve, sauf erreur", "B07")
replace(85, ("diff_coverage", 36, "reason"),
        "readable introductory On a même", "readable introductory On trouve", "B07")
replace(85, ("deletion_insertion_review", 7, "bounds"),
        "The parenthesis, s_ij and b_ij that follow are live.",
        "The parenthesis, s_j and b_ij that follow are live.", "B08")

# 087: canceled multi-character superscript; square inner bracket / outer brace.
put(87, ("inventory", 8, "first_words_or_objects"),
    r"\deleted{\unsure{I'-J|I'\setminus J}}", "B05")
put(87, ("inventory", 10, "element"),
    "E11 two-line definition, square-ended inner bracket and outer underbrace", "B07")
note(87, "displays two underbrace annotations",
     "displays a square-ended inner bracket and an outer underbrace", "B07")
note(87, "all displayed letters, primes and indices, both underbrace annotations,",
     "all displayed letters, primes and indices, the inner bracket and outer underbrace,", "B07")

# 088: restore the already-audited uncertainty of the first j index.
note(88, "The first j index is a capped upright 1.",
     "The first j index has a retraced cap and retains the local 1/q uncertainty.",
     "B02")
note(88, r"so i_{\unsure{0|q}} is retained.",
     r"so i_{\unsure{q|0}} is retained, with q favored but 0 still possible.", "B02")
put(88, ("inventory", 2, "first_words_or_objects"),
    r"(80) (j_{\unsure{1|q}}...j_p l_1...l_q); i_{\unsure{q|0}}...i_p in J", "B02")
put(88, ("notation", 0, "sign"),
    r"i_{\unsure{q|0}}...i_p versus j_{\unsure{1|q}}...j_p", "B02")

# 090: no separately transcribed pour; retain equals as the first alternative.
note(90, "Que overlaps the main-line canceled pour.",
     "The marginal tels que overlaps the main text; no separate canceled pour is transcribed.",
     "B04")
note(90, "The initial pour and old une propriété remain low-confidence canceled candidates.",
     "The old une propriété remains a low-confidence canceled candidate. The apparent separate pour belongs to the already-transcribed marginal tels que formula.",
     "B04")
put(90, ("changes", 18, "evidence"),
    root(90, "B14")["evidence"].split(" The next inclusion", 1)[0], "B14")
put(90, ("notation", 2, "reading"),
    "Heavy first lower relation remains ambiguous; equals is the first alternative.",
    "B14")
note(90,
     r"The tight crop shows a substantial connected left curve, favoring subset, but the prose equals abbreviation elsewhere has a left pen return too. The candidate therefore retains \unsure{\subset|=} and does not force either sign from the mathematical argument.",
     r"The blind adjudication compares the linked relation with the prose equals sign, while its curved join still admits subset. The candidate therefore retains \unsure{=|\subset}, with equals first, without forcing either sign from the mathematical argument.",
     "B14")

# 091: canceled opening alternatives, indicée, recouvrt/reco underline, coproduct.
put(91, ("diff_coverage", 2, "reason"),
    "The blind audit narrows the canceled noun to uncertain filtration: the initial f/l strokes exclude stratification, while middle joins remain obscured in D01. Historical C/H witness strings are retained unchanged.", "B02")
put(91, ("diff_coverage", 3, "reason"),
    "The raised, then canceled adjective remains indicée|indicielle|induite in D02. The former ordinaire alternative is not retained; the crossed occurrence is not certified from the separate live heading.", "B02")
put(91, ("diff_coverage", 4, "reason"),
    "The separate live adjective reads indicée after the blind audit. C01 and M0716 record the other reading, independently of the still-doubtful crossed adjective.", "B03")
put(91, ("deletion_insertion_review", 0, "evidence"),
    root(91, "B02")["evidence"], "B02")
put(91, ("deletion_insertion_review", 1, "item"),
    "Raised indicée|indicielle|induite inside the opening cancelled phrase", "B02")
put(91, ("deletion_insertion_review", 2, "item"),
    "Strat 1 est un recouvrt", "B05")
put(91, ("deletion_insertion_review", 2, "evidence"),
    "The long upper curve attaches the raised recouvrt before loc; its independent short underline stops beneath reco. The longer curves are insertion leaders, not an underline of the full abbreviation or of loc! fini(e).", "B05")
put(91, ("changes", 4, "evidence"),
    "The long upper curve attaches est un recouvrt before loc; the lower curve attaches de X after the adjective. Neither independently underlines loc/fini. The abbreviation recouvrt has a separate short underline beneath reco only.", "B05")
replace(91, ("changes", 5, "evidence"),
        "Est un recouvrement is raised above the line",
        "Est un recouvrt is raised above the line", "B05")
put(91, ("deletion_insertion_review", 5, "item"),
    "Canceled les-like word before the live coproduct and its lower index", "B11")
put(91, ("deletion_insertion_review", 5, "state"),
    "The doubtful les-like word is deleted; the following coproduct and its lower d-in-Drap-I index are live.", "B11")
put(91, ("deletion_insertion_review", 5, "attachment"),
    "The canceled word stands after alors. The lower d-in-Drap-I label belongs to the following live coproduct, which precedes X_d.", "B11")
put(91, ("deletion_insertion_review", 5, "evidence"),
    root(91, "B11")["evidence"], "B11")
replace(91, ("deletion_insertion_review", 6, "attachment"),
        "Between forment un", "Between forme un", "B11")
put(91, ("inventory", 1, "first_words_or_objects"),
    r"Une \unsure{filtration} ... de type I", "B02")
put(91, ("inventory", 2, "first_words_or_objects"),
    "indicée|indicielle|induite; added and then cancelled", "B02")
put(91, ("inventory", 4, "first_words_or_objects"),
    "Une Stratification indicée, de type I, de X, est une application", "B03")
put(91, ("inventory", 8, "first_words_or_objects"),
    "est un recouvrt; only reco is underlined", "B05")

# 094: distinguish the source-bearing enclosure from H's editorial narration.
assert record(94)["diff_coverage"][36]["diff_id"] == "D0647"
assert record(94)["changes"][37]["id"] == "C38"
put(94, ("diff_coverage", 36, "classification"), "reading", "B14")
put(94, ("diff_coverage", 36, "change_ids"), ["C38"], "B14")
put(94, ("diff_coverage", 36, "reason"),
    "H's description of the enclosing NB frame is source-bearing and is collated by C38: the current transcription preserves the enclosure around the whole note. Any residual positional or explanatory editorial prose is not copied as manuscript wording.", "B14")

# 095: partial insertion, current canceled alternatives and local on-a doubts.
put(95, ("deletion_insertion_review", 0, "attachment"),
    "The raised replacement portion is récipro; the surviving que continues on the original baseline before est vraie.", "B02")
put(95, ("deletion_insertion_review", 1, "place"),
    "First line, raised récipro prefix", "B02")
put(95, ("deletion_insertion_review", 1, "final_state"),
    "inserted; live récipro only, with que retained on the baseline", "B02")
put(95, ("deletion_insertion_review", 1, "attachment"),
    "The raised prefix is above the canceled material after la; baseline que follows it before est vraie.", "B02")
put(95, ("deletion_insertion_review", 1, "evidence"),
    root(95, "B02")["evidence"], "B02")
put(95, ("inventory", 3, "element"), "Raised replacement prefix récipro", "B02")
put(95, ("inventory", 3, "first_words_or_objects"),
    r"\inserted{récipro}que", "B02")
put(95, ("deletion_insertion_review", 4, "final_state"),
    r"deleted; \unsure{Sous les|Sur les|donc les}", "B05")
put(95, ("deletion_insertion_review", 4, "evidence"),
    root(95, "B05")["evidence"], "B05")
put(95, ("inventory", 6, "first_words_or_objects"),
    "Sous les | Sur les | donc les", "B05")
put(95, ("diff_coverage", 18, "reason"),
    "The canceled opening remains uncertain between Sous les, Sur les and donc les. The blind adjudication does not support the tall t required by H's Soient; C08 preserves the current alternatives.", "B05")
replace(95, ("hand_log", 7, "places"),
        "Sur les/Soient les", "Sous les/Sur les/donc les", "B05")
put(95, ("changes", 13, "final"),
    r", \unsure{on a|$\mathord{\cdot}\mathord{-}\mathord{\cdot}$}", "B08")
put(95, ("changes", 13, "evidence"), root(95, "B08")["evidence"], "B08")
put(95, ("changes", 13, "confidence"), record(95)["doubts"][7]["confidence"], "B08")
put(95, ("deletion_insertion_review", 6, "final_state"),
    r"deleted; cela \unsure{revient|veut|vaut}", "B10")
put(95, ("deletion_insertion_review", 6, "attachment"),
    "The canceled group precedes an uncrossed low group, uncertain between on a and point-rule-point, to the left of the equivalence on the same baseline.", "B10")
put(95, ("deletion_insertion_review", 6, "evidence"),
    root(95, "B10")["evidence"], "B10")
note(95,
     "The separately cancelled numeral below the first label remains uncertain as 96.",
     "The separately canceled group below the first label remains uncertain between 96 and Or/Où.",
     "B09")
note(95,
     "The prose before the lower display has **n’a pas de chance** and a literal colon after équivalente, with no quotation marks.",
     "The prose before the lower display has **n’a pas de chance|chances**, with the ending still uncertain, and a literal colon after équivalente, with no quotation marks.",
     "B11")
note(95,
     "The two raised insertions replace the unreadable opening word and attach the equality after the baseline X_J^* respectively.",
     "The opening replacement has only récipro raised, with que continuing on the baseline; the second raised insertion attaches the equality after the baseline X_J^*.",
     "B02")
note(95,
     "Six cancelled groups are preserved: the unreadable first word, i.e., the Sur les/Soient les opening, the tentative numeral 96, cela revient, and comme.",
     "Six canceled groups are preserved: the unreadable first group, i.e., the Sous les/Sur les/donc les opening, the doubtful 96/Or/Où group, readable cela with an uncertain revient/veut/vaut, and doubtful comme.",
     "B05")
note(95,
     "The live on a after cela revient is on the left of the unnumbered equivalence; H’s placement after that display is not followed.",
     "The uncrossed on-a/point-rule-point group after the canceled cela phrase is on the left of the unnumbered equivalence; H’s placement after that display is not followed.",
     "B10")

# Syntax-only repair in current finals. Original first/second fields stay intact.
syntax_authority = "Parent-authorized delimiter repair: existing \\quad followed by literal i"
for path, keys in [
    (record_path(94), ("audit_changes", 0, "final")),
    (WORK / "second" / "150_scan094_root_crop_notes.json", ("B01", "final")),
    (WORK / "second" / "150_scan094_adjudications.json",
     ("adjudications", 0, "final")),
]:
    cursor, key = locate(load_document(path), keys)
    value = cursor[key]
    assert value.count(r"\quadi") <= 1
    if r"\quadi" in value:
        set_path(path, keys, value.replace(r"\quadi", r"\quad i"), syntax_authority)
    else:
        assert r"\quad i'\in\bar j" in value

text_outputs: dict[Path, str] = {}
for folder in ("pages", "records"):
    path = WORK / folder / "150_scan094.tex"
    raw = path.read_bytes()
    original_bytes[path] = raw
    text = raw.decode("utf-8")
    assert text.count(r"\quadi") <= 1
    if r"\quadi" in text:
        text_outputs[path] = text.replace(r"\quadi", r"\quad i")
        edits.append({"file": str(path.relative_to(WORK)), "path": ["text"],
                      "old": r"\quadi", "new": r"\quad i",
                      "authority": syntax_authority})
    else:
        assert r"\quad i'\in\bar j" in text


def protected_values(value, path=()):
    found = {}
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = path + (key,)
            if key in PROTECTED_KEYS:
                found[child_path] = child
            else:
                found.update(protected_values(child, child_path))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            found.update(protected_values(child, path + (i,)))
    return found


def leaf_changes(before, after, path=()):
    if type(before) is not type(after):
        return {path}
    if isinstance(before, dict):
        assert set(before) == set(after), ("unexpected key change", path)
        return set().union(*(leaf_changes(before[k], after[k], path + (k,))
                             for k in before))
    if isinstance(before, list):
        if len(before) != len(after):
            return {path}
        return set().union(*(leaf_changes(x, y, path + (i,))
                             for i, (x, y) in enumerate(zip(before, after))))
    return {path} if before != after else set()


allowed_paths: dict[str, set] = {}
for edit in edits:
    allowed_paths.setdefault(edit["file"], set()).add(tuple(edit["path"]))

for path, document in documents.items():
    assert protected_values(document) == protected_values(original_json[path]), path
    changed = leaf_changes(original_json[path], document)
    allowed = allowed_paths.get(str(path.relative_to(WORK)), set())
    # A whole list replacement (D0647 change_ids) permits its changed descendants.
    assert all(any(k == a or k[:len(a)] == a for a in allowed) for k in changed), (
        path, changed, allowed)

page94 = text_outputs.get(WORK / "pages" / "150_scan094.tex",
                          (WORK / "pages" / "150_scan094.tex").read_text())
candidate94 = text_outputs.get(WORK / "records" / "150_scan094.tex",
                               (WORK / "records" / "150_scan094.tex").read_text())
assert page94 == candidate94
assert r"\quadi" not in page94 and r"\quad i'\in\bar j" in page94
brace_text = page94.replace(r"\{", "").replace(r"\}", "")
assert brace_text.count("{") == brace_text.count("}")
environment_stack = []
for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", page94):
    action, name = match.groups()
    if action == "begin":
        environment_stack.append(name)
    else:
        assert environment_stack and environment_stack.pop() == name
assert not environment_stack

root94 = load_document(WORK / "second" / "150_scan094_root_crop_notes.json")
adjudications94 = load_document(WORK / "second" / "150_scan094_adjudications.json")
final94 = record(94)["audit_changes"][0]["final"]
assert root94["B01"]["final"] == final94
assert adjudications94["adjudications"][0]["box"] == "B01"
assert adjudications94["adjudications"][0]["final"] == final94
assert r"\quadi" not in final94
assert record(94)["diff_coverage"][36]["change_ids"] == ["C38"]
assert record(94)["diff_coverage"][36]["classification"] == "reading"
assert record(95)["changes"][13]["confidence"] == record(95)["doubts"][7]["confidence"]
assert record(95)["changes"][13]["final"] in (
    WORK / "pages" / "150_scan095.tex").read_text(encoding="utf-8")

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--apply", action="store_true")
args = parser.parse_args()
outputs = {}
for path, document in documents.items():
    if document != original_json[path]:
        outputs[path] = (json.dumps(document, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
for path, text in text_outputs.items():
    outputs[path] = text.encode("utf-8")
assert all(p.suffix in {".json", ".tex"} and p.name != "150_scan094_comparison.json"
           for p in outputs)
assert all("/second/" not in str(p) or p.name in {
    "150_scan094_root_crop_notes.json", "150_scan094_adjudications.json"
} for p in outputs)

if args.apply:
    # Fail before writing anything if another process changed a loaded target.
    for path in outputs:
        assert path.read_bytes() == original_bytes[path], ("concurrent edit", path)
    for path, raw in outputs.items():
        temporary = path.with_name(path.name + ".metadata_cleanup_tmp")
        temporary.write_bytes(raw)
        temporary.replace(path)
    for path, raw in outputs.items():
        assert path.read_bytes() == raw
        if path.suffix == ".json":
            assert json.loads(raw) == documents[path]
    log = {
        "task": "Authorized metadata cleanup 150_scan079–095",
        "reader": "reader_c",
        "completed_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "mode": "applied",
        "changed_files": [
            {"file": str(p.relative_to(WORK)),
             "before_sha256": hashlib.sha256(original_bytes[p]).hexdigest(),
             "after_sha256": hashlib.sha256(raw).hexdigest()}
            for p, raw in sorted(outputs.items())
        ],
        "changes": [
            {"file": e["file"], "path": e["path"], "authority": e["authority"]}
            for e in edits
        ],
        "checks": {
            "all_writes_within_explicit_target_paths": True,
            "historical_C_H_fields_unchanged": True,
            "original_first_second_fields_unchanged": True,
            "second_boxes_unchanged": True,
            "frozen_and_sealed_TSVs_not_opened_or_written": True,
            "no_scan_or_image_opened": True,
            "no_new_manuscript_decisions": True,
            "page94_matches_candidate94": True,
            "page94_braces_and_environments_balanced": True,
            "page94_root_and_adjudication_finals_match_audit_final": True,
            "fused_quadi_absent_from_current94_targets": True,
            "D0647_links_C38_as_reading": True,
            "JSON_round_trip_valid": True,
            "aggregates_not_assembled": True,
            "TeX_not_run": True,
        },
    }
    log_path = WORK / "records" / "metadata_cleanup_079_095.json"
    log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
print(json.dumps({
    "mode": "applied" if args.apply else "validated_dry_run",
    "changed_file_count": len(outputs),
    "metadata_or_final_field_edits": len(edits),
    "changed_files": [str(p.relative_to(WORK)) for p in sorted(outputs)],
    "protected_fields_verified": True,
    "current94_final_fields_synchronized": True,
}, ensure_ascii=False))
