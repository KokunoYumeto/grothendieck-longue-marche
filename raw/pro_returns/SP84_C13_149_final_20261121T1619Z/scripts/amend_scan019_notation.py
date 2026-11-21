"""Apply root's recorded post-audit alphabet amendment to scan 019 only.

One use.  Preserve frozen comparison inputs and original adjudication evidence;
do not assemble, refreeze, reread images, or change another page.
"""
from copy import deepcopy
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
STEM = "149_scan019"
LOG = ROOT / "documentation/149_scan019_notation_amendment.json"
NOTE = ROOT / "documentation/149_scan019_notation_amendment.md"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def counts(report):
    material = [x for x in report["changes"] if x["against_C"] or x["against_H"]]
    return {
        "report_rows": len(report["changes"]),
        "counted_places": len(material),
        "against_C": sum(x["against_C"] for x in material),
        "against_H": sum(x["against_H"] for x in material),
        "confidence": {level: sum(x["confidence"] == level for x in material)
                       for level in ("high", "medium", "low")},
        "doubts": len(report["doubts"]),
        "audit_boxes": report["audit_boxes_read"],
        "audit_differing_boxes": report["audit_differing_boxes"],
        "audit_token_spans": report["audit_token_spans"],
        "audit_changed_boxes": report["audit_changed_boxes"],
    }


assert not LOG.exists() and not NOTE.exists(), "Amendment already recorded"
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
page_path = ROOT / f"pages/{STEM}.tex"
report_path = ROOT / f"reviews/{STEM}.json"
choices_path = ROOT / f"documentation/{STEM}_audit_choices.json"
adj_path = ROOT / f"second/{STEM}_adjudications.tsv"
report = json.loads(report_path.read_text())
before_report = deepcopy(report)
choices = json.loads(choices_path.read_text())
before_choices = deepcopy(choices)
with adj_path.open(newline="", encoding="utf-8") as stream:
    reader = csv.DictReader(stream, delimiter="\t")
    fields = reader.fieldnames
    adjudications = list(reader)
before_adj = deepcopy(adjudications)
by_box = {x["box"]: x for x in adjudications}
assert report["audited"] and report["audit_changed_boxes"] == 8
assert by_box["b09"]["changed"] == "no" and by_box["b22"]["changed"] == "yes"
assert len(adjudications) == 18
assert len(report["changes"]) == 32
original_completion = report["audit_completed_utc"]
c16_before = deepcopy(next(x for x in report["changes"] if x["id"] == "c16"))
assert c16_before["confidence"] == "low" and c16_before["against_C"] is True

protected = [ROOT / f"second/{STEM}_{suffix}" for suffix in (
    "boxes.tsv", "first.tsv", "second.tsv", "token_differences.tsv",
    "comparison_provenance.json", "second_notes.md", "crop_manifest.tsv")]
frozen_hashes = {str(p.relative_to(ROOT)): digest(p) for p in protected}
input_provenance = json.loads((ROOT / f"second/{STEM}_comparison_provenance.json").read_text())
for kind, expected in input_provenance["sha256"].items():
    assert digest(ROOT / f"second/{STEM}_{kind}.tsv") == expected

# Check the exact supplied witness text, including its TeX spelling and spaces.
witnesses = {}
for name in ("C", "H"):
    path = WORKSPACE / f"work/packets/{STEM}/{name}.tex"
    text = path.read_text()
    witnesses[name] = {"path": str(path.relative_to(WORKSPACE)),
                       "sha256": digest(path), "text": text}
c_q = r"$E_{\mathbb Q}\longleftarrow\Gamma_{\mathbb Q}$"
h_q = r"$E_{\mathbb{Q}} \simeq \Gamma_{\mathbb{Q}}$"
k_phrase = r"$E_K$, au-dessus"
assert c_q in witnesses["C"]["text"]
assert h_q in witnesses["H"]["text"]
assert all(k_phrase in x["text"] for x in witnesses.values())
for name, formula in (("C", c_q), ("H", h_q)):
    witnesses[name] = {k: v for k, v in witnesses[name].items() if k != "text"}
    witnesses[name].update(E_Q_exact=formula, E_K_with_following_phrase_exact=k_phrase)

alphabet = r"\unsure{\mathcal E|E}"
q_formula = "$" + alphabet + r"_{\mathbb Q}\longleftarrow\Gamma_{\mathbb Q}$"
k_final = "$" + alphabet + r"_K$, \unsure{au-dessus|--- disons|--- dessus}"
b09_final = q_formula + " (pro-gr)"
b22_final = "Par le groupe extérieur " + k_final
comparison_evidence = (
    "Root's final cross-page visual review: the item-3 E_K (019 b22) and "
    "Q-indexed E (019 b09) share an open upper curve, inward waist and lower "
    "returning foot with 020 c10 and the exterior-group forms in 020 c14. "
    "This construction differs from the stemmed, separately three-barred "
    "ordinary E comparators in 013 c12 and 014 c13. Calligraphic E is favored "
    "at these two 019 sites, with ordinary E retained as an explicit alternative. "
    "Curvature alone does not settle the alphabet throughout the cote; the "
    "earlier Gamma-equivalent E forms on 006/008/009 are outside this amendment. "
    "Root personally reopened the named existing crops; the implementer made "
    "no further image reading."
)
b09_tail = before_choices["b09"]["evidence"].split("Each Q", 1)
assert len(b09_tail) == 2
b09_evidence = comparison_evidence + " Each Q" + b09_tail[1]
b22_tail = before_choices["b22"]["evidence"].split("The crop extends", 1)
assert len(b22_tail) == 2
b22_evidence = comparison_evidence + " The crop extends" + b22_tail[1]
for box, final, evidence in (("b09", b09_final, b09_evidence),
                             ("b22", b22_final, b22_evidence)):
    choices[box].update(selection="custom", final=final, evidence=evidence, changed="yes")
    by_box[box].update(final_reading=final, evidence=evidence, changed="yes")

page_before = page_path.read_text()
page = page_before
assert page.count("$E_K$") == 1 and page.count(c_q) == 1
page = page.replace("$E_K$", "$" + alphabet + "_K$")
page = page.replace(c_q, q_formula)
assert page.count(alphabet) == 3

changes = {x["id"]: x for x in report["changes"]}
old_c08 = deepcopy(changes["c08"])
old_b22_place = deepcopy(changes["audit_b22_phrase"])
changes["c08"].update(
    C=c_q, H=h_q, final=q_formula,
    evidence=old_c08["evidence"] + " " + comparison_evidence,
    confidence="low", against_C=True, against_H=True)
# Reuse the existing b22 locus; broaden it to the glyph and following phrase.
# The following words keep their former preferred reading, so no new row is added.
changes["audit_b22_phrase"].update(
    place="Item3, exterior-group symbol E_K and following words",
    C=k_phrase, H=k_phrase, final=k_final, evidence=b22_evidence,
    confidence="low", against_C=True, against_H=True,
    kind="misread symbol or index", error_category="Symbols and indices",
    mathematical=True)

item4_evidence = (
    "The complete map has an open two-lobed first glyph, a single rightward "
    "shaft whose terminal remains arrow/plain-shaft uncertain after audit b12, "
    "and Gamma with the full Q-bar/Q extension index. The item-4 alphabet "
    "remains undecided with calligraphic E first and ordinary E retained; an "
    "epsilon-like shape remains a visual possibility. Root's final cross-page "
    "review now gives the two item-3 exterior-group symbols the same favored "
    "calligraphic-E/ordinary-E order on positive stroke comparisons (019 b09/b22; "
    "020 c10/c14; ordinary comparators 013 c12 and 014 c13). Neither mathematical "
    "identification nor curvature alone resolves the alphabet."
)
assert report["decisions"][0]["id"] == "M1010"
report["decisions"][0]["evidence"] = item4_evidence
changes["c25"]["evidence"] = item4_evidence + (
    " The provisional difference from H remains counted; the favored reading "
    "and the unresolved decision have not changed.")

for doubt in report["doubts"]:
    if doubt["place"] == "L15, M1010 source of the whole map":
        doubt["reason"] = item4_evidence
    elif doubt["place"] == "Item3, phrase after E_K":
        doubt["reason"] = b22_evidence
report["doubts"].extend([
    {"place": "Item3, alphabet of E_K (audit b22)",
     "reading": alphabet + "_K", "alternatives": [r"\mathcal E_K", "E_K"],
     "confidence": "low", "reason": comparison_evidence},
    {"place": "Item3, alphabet of the Q-indexed exterior group (audit b09)",
     "reading": alphabet + r"_{\mathbb Q}",
     "alternatives": [r"\mathcal E_{\mathbb Q}", r"E_{\mathbb Q}"],
     "confidence": "low", "reason": comparison_evidence},
])

for entry in report["notation"]:
    if entry["written"] == "rounded two-lobed E-like letter":
        entry.update(
            written="open upper curve, inward waist and lower returning foot",
            rendering=alphabet + "_K, " + alphabet + r"_{\mathbb Q}; " + alphabet,
            meaning="The two exterior-group symbols in item 3 and the source of the homomorphism in item 4; calligraphic E favored, ordinary E retained.",
            evidence=comparison_evidence + " Item-4 M1010 remains undecided; its whole map is in c08.")
for entry in report["hand"]:
    if entry["habit"] == "The E-like form can have two rounded open lobes.":
        entry.update(
            habit="The exterior-group glyph has an open upper curve, inward waist and lower returning foot.",
            consistency="The item-3 symbols in 019 b09/b22 and the item-4 map source agree locally. Root compared their construction with 020 c10/c14 and the ordinary stemmed/three-bar E comparators 013 c12 and 014 c13; calligraphic E is favored, but ordinary E remains an alternative at all three 019 sites. This is not a global alphabet substitution.",
            misread="C and H both give ordinary E at the two item-3 sites; H also gives ordinary E at M1010, where C already retained the alphabet doubt.")
for entry in report["inventory"]:
    if entry["element"] == "e09":
        entry["first_words_or_objects"] = (
            "3) Par le groupe extérieur " + k_final +
            " du groupe extérieur " + q_formula + " (pro-gr)")
for entry in report["diff_coverage"]:
    if entry["row"] == 10:
        assert entry["change_id"] == "c08"
        entry.update(final=q_formula, reason=(
            "The same whole-relation locus now includes root's final alphabet "
            "amendment: calligraphic E is favored with ordinary E retained, "
            "and the clear single leftward arrow remains unchanged. Both C "
            "and H have ordinary E; H also substitutes an isomorphism sign."))
for entry in report["audit_boxes"]:
    if entry["box"] == "b09":
        entry["reading"] = b09_final
    elif entry["box"] == "b22":
        entry["reading"] = b22_final

report["audit_changed_boxes"] = 9
report["audit_last_amended_utc"] = now
report.setdefault("audit_amendments", []).append({
    "utc": now, "authority": "root final cross-page notation review",
    "boxes": ["b09", "b22"], "changed_boxes_before": 8,
    "changed_boxes_after": 9,
    "record": "documentation/149_scan019_notation_amendment.json",
    "note": "documentation/149_scan019_notation_amendment.md",
})
report["notes"].append(
    f"Post-audit notation amendment {now}: root personally reopened the exact "
    "existing crops and favored calligraphic E, retaining ordinary E, at both "
    "item-3 sites (b09, b22). This matches the existing favored item-4 alphabet "
    "and the exterior-group forms on 020, with stemmed ordinary E comparators "
    "on 013/014. Earlier Gamma-equivalent E on 006/008/009 is not changed. The "
    "whole-relation row c08 and the existing b22 phrase locus are reused; no "
    "new counted place is split off. The b22 locus now includes its E_K "
    "symbol. Both witnesses use ordinary E at these two sites. Current audit "
    "K is 9: b09 changes no to yes, while b22 stays yes. The original completion "
    "record (8 changed boxes) and all original row evidence remain preserved "
    "in progress.log and documentation/149_scan019_notation_amendment.json. "
    "The mutable report's b09/b22 readings track the current adopted text; "
    "canonical first/second/box TSVs, token differences and original audit "
    "completion time remain untouched. The two new local alphabet doubts "
    "bring the current doubt list to 17. No new image reading or mathematical "
    "check was performed by the implementer.")

assert report["audit_completed_utc"] == original_completion
assert next(x for x in report["changes"] if x["id"] == "c16") == c16_before
assert report["checks"] == before_report["checks"]
assert len(report["changes"]) == 32 and len(report["doubts"]) == 17
assert len(report["diff_coverage"]) == 29
assert sum(x["changed"] == "yes" for x in adjudications) == 9
for old, new in zip(before_adj, adjudications):
    if old["box"] not in ("b09", "b22"):
        assert old == new
    for key in ("first_reading", "second_reading", "crop", "pixel_box"):
        assert old[key] == new[key]
for change in report["changes"]:
    if change["id"] not in ("c08", "c25", "audit_b22_phrase"):
        assert change == next(x for x in before_report["changes"] if x["id"] == change["id"])

before_counts, after_counts = counts(before_report), counts(report)
assert (after_counts["against_C"], after_counts["against_H"], after_counts["counted_places"]) == (10, 26, 28)
before_hashes = {str(p.relative_to(ROOT)): digest(p)
                 for p in (page_path, report_path, choices_path, adj_path)}
log = {
    "scan": 19, "utc": now,
    "status": "post-audit amendment authorized by root; not a new independent reading",
    "authority": comparison_evidence,
    "implementation_scope": "Scan019 only. No image rereading, new crops, assembly or freezing.",
    "witness_exact_checks": witnesses,
    "original_audit_completed_utc": original_completion,
    "original_progress_history_preserved": True,
    "counts_before": before_counts, "counts_after": after_counts,
    "frozen_and_protected_sha256": frozen_hashes,
    "files_before_sha256": before_hashes,
    "adjudication_rows": [
        {"box": box,
         "old": next(x for x in before_adj if x["box"] == box),
         "new": by_box[box],
         "old_choice": before_choices[box], "new_choice": choices[box]}
        for box in ("b09", "b22")],
    "report_changes": [
        {"id": cid,
         "old": next(x for x in before_report["changes"] if x["id"] == cid),
         "new": changes[cid]}
        for cid in ("c08", "audit_b22_phrase", "c25")],
    "report_context_before": {k: before_report[k] for k in (
        "decisions", "notation", "hand", "notes", "doubts", "inventory",
        "diff_coverage", "audit_boxes")},
    "report_context_after": {k: report[k] for k in (
        "decisions", "notation", "hand", "notes", "doubts", "inventory",
        "diff_coverage", "audit_boxes")},
    "preserved_c16": c16_before,
    "row_reuse": "c08 retains the complete E_Q relation. Existing audit_b22_phrase broadens to E_K plus its following phrase; no report row is added.",
}

# Record the old/new evidence before changing current authoritative files.
LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n")
page_path.write_text(page)
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
choices_path.write_text(json.dumps(choices, ensure_ascii=False, indent=2) + "\n")
with adj_path.open("w", newline="", encoding="utf-8") as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t")
    writer.writeheader()
    writer.writerows(adjudications)
assert all(digest(ROOT / name) == value for name, value in frozen_hashes.items())
log["files_after_sha256"] = {str(p.relative_to(ROOT)): digest(p)
                             for p in (page_path, report_path, choices_path, adj_path)}
LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n")

note = f"""# Scan 019: final cross-page notation amendment

Recorded {now}, on root's explicit instruction. This is a post-audit amendment,
not a new independent reading. Root personally reopened the existing evidence;
the implementer did not reread images, generate crops, assemble or freeze files.

## Adopted scope and evidence

{comparison_evidence}

- Item 3, b09: `{before_adj[[x['box'] for x in before_adj].index('b09')]['final_reading']}`
  becomes `{b09_final}`; changed **no → yes**.
- Item 3, b22: `{before_adj[[x['box'] for x in before_adj].index('b22')]['final_reading']}`
  becomes `{b22_final}`; changed remains **yes**.

The clear leftward arrow, Q/Gamma indices, abbreviation and following phrase
are unchanged. The existing item-4 alphabet remains undecided in its previous
order. No global alphabet replacement has been applied to other pages.

## Witness and report accounting

Exact packet checks confirm that both C and H give ordinary E at both item-3
sites. C's whole Q-indexed relation is `{c_q}`; H's is `{h_q}`. Both give
`{k_phrase}` at the preceding site.

The existing c08 whole-relation record absorbs the Q-indexed alphabet change.
The existing audit_b22_phrase locus is broadened to E_K and its following words;
its ID is retained, so no new report row is added. Both affected records now
count against C and H. The earlier c16 correction remains low-confidence with
against_C=true and against_H=true.

| Measure | Before | After |
| --- | ---: | ---: |
| Current report rows | {before_counts['report_rows']} | {after_counts['report_rows']} |
| Counted substantive places | {before_counts['counted_places']} | {after_counts['counted_places']} |
| Against C | {before_counts['against_C']} | {after_counts['against_C']} |
| Against H | {before_counts['against_H']} | {after_counts['against_H']} |
| High confidence counted places | {before_counts['confidence']['high']} | {after_counts['confidence']['high']} |
| Medium confidence counted places | {before_counts['confidence']['medium']} | {after_counts['confidence']['medium']} |
| Low confidence counted places | {before_counts['confidence']['low']} | {after_counts['confidence']['low']} |
| Localized doubts | {before_counts['doubts']} | {after_counts['doubts']} |
| Audit changed boxes K | 8 | 9 |

The audit still covers 22 boxes, 18 differing boxes and 89 token-difference
spans. Original completion time `{original_completion}` is unchanged. A new
audit-amended progress entry records the current K rather than rewriting the
original completion entry.

## Preservation and synchronization

`149_scan019_notation_amendment.json` preserves complete old/new adjudication
rows and choices, including the original evidence, exact witness excerpts,
affected report rows and context, protected SHA-256 hashes and before/after
file hashes. The page, current report, choices and current adjudication rows
are synchronized. Report notation, hand observations, doubts, relevant
inventory, difference coverage and mutable b09/b22 readings reflect the
adopted amendment. The frozen box/first/second TSVs, comparison provenance,
token differences, second-reader notes and crop manifest are unchanged.

Generated aggregate tables are left for root's final assembly. The first
proposed page in reviews/ is historical and is not overwritten.
"""
NOTE.write_text(note, encoding="utf-8")
with (ROOT / "progress.log").open("a", encoding="utf-8") as stream:
    stream.write(
        f"scan 019 audit-amended {now}: 22 boxes read, 18 differences, "
        "89 token-difference spans, 9 changed (was 8); root cross-page notation "
        "amendment b09 no->yes and b22 yes->yes. Current report: 32 rows, "
        "28 counted places, C=10, H=26, confidence high=15 medium=2 low=11, "
        "17 doubts. Original audit history and frozen inputs preserved; "
        "evidence/old-new rows: documentation/149_scan019_notation_amendment.json.\n")
print(json.dumps({"scan": 19, "utc": now, "counts": after_counts,
                  "frozen_inputs_unchanged": True, "c16_preserved": True}, indent=2))
