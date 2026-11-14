"""Verify the frozen deliverable and research structure without altering any TeX."""
from pathlib import Path
import collections
import csv
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "MPL_121_049-073+153+155"
UTC = sys.argv[1]
assert re.fullmatch(r"\d{4}-\d\d-\d\d \d\d:\d\d:\d\d UTC", UTC)

expected = [(121, n) for n in range(49, 74) if n not in (53, 64, 69)]
expected += [(c, n) for c in (153, 155) for n in range(1, 12)]
paths = [ROOT / "pages" / f"{PREFIX}_{c}_scan{n:03}.tex" for c, n in expected]
assert len(paths) == 44
assert set(paths) == set((ROOT / "pages").glob("*.tex"))
frozen = json.loads((ROOT / "freeze_manifest.json").read_text())
hash_checks = []
for name, digest in frozen["sha256"].items():
    actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    hash_checks.append({"file": name, "sha256": actual, "unchanged": actual == digest})
assert len(hash_checks) == 45 and all(x["unchanged"] for x in hash_checks)
combined = (ROOT / f"{PREFIX}_transcription.tex").read_text()
assert combined == "\n".join(p.read_text() for p in paths)
assert combined.startswith("\\cotefile{121}\n\\scanpage{49}")
assert "\\documentclass" not in combined and "\\begin{document}" not in combined
current, order = None, []
for m in re.finditer(r"\\(cotefile|scanpage)\{(\d+)\}", combined):
    if m[1] == "cotefile":
        current = int(m[2])
    else:
        order.append((current, int(m[2])))
assert order == expected

with (ROOT / f"{PREFIX}_inventory.csv").open() as f:
    reader = csv.DictReader(f)
    assert reader.fieldnames == ["cote", "scan", "sheet_kind", "element", "kind",
                                 "position", "first_words_or_objects", "transcribed"]
    inventory = list(reader)
assert len(inventory) == 871
assert all(r["transcribed"] == "yes" for r in inventory)
assert set((int(r["cote"]), int(r["scan"])) for r in inventory) == set(expected)
assert set(r["kind"] for r in inventory) <= {
    "text", "display", "diagram", "drawing", "margin note", "insertion", "deletion"}
assert set(r["sheet_kind"] for r in inventory) <= {
    "text", "reused_typed", "cancelled_draft", "cover"}
audits = [json.loads(x) for x in (ROOT / "audit_records.jsonl").read_text().splitlines()]
assert len(audits) == 44
assert [(a["cote"], a["scan"]) for a in audits] == expected
log = (ROOT / "progress.log").read_text()
done = [(int(c), int(n)) for c,n in re.findall(r"^(\d+) scan (\d+) done ", log, re.M)]
assert done == expected
assert len(re.findall(r"scan \d+ audited ", log)) == 44
assert log.index("transcription frozen") < log.index("context opened")
validation = json.loads((ROOT / "tex_validation.json").read_text())
assert len(validation["results"]) == 44 and all(r["passed"] for r in validation["results"])
pre = json.loads((ROOT / "pre_freeze_verification.json").read_text())
assert pre["supplied_images"] == 132 and pre["ocr_used"] is False

notes = (ROOT / f"{PREFIX}_notes.md").read_text()
matches = list(re.finditer(r"^### ((?:R121-|H|TC|A|T)\d+) — .*$", notes, re.M))
ids = [m[1] for m in matches]
assert len(ids) == len(set(ids)) == 124
allowed_kinds = ("conjecture", "unproved claim", "unpursued implication",
                 "own idea", "reading question", "self-flagged", "withdrawn in the same text")
note_checks = []
for i,m in enumerate(matches):
    end = matches[i+1].start() if i+1 < len(matches) else notes.index("\n## Standing question", m.end())
    chunk = notes[m.start():end]
    paragraphs = chunk.split("\n\n")
    meta, body = paragraphs[1], paragraphs[2]
    kind = re.search(r"(?:\*\*Kind:\*\* |kind: )([^;\n]+)", meta)
    assert kind and any(kind[1].lower().startswith(k) for k in allowed_kinds), (m[1],meta)
    assert re.search(r"Context|context/", chunk), m[1]
    assert re.search(r"Register|register|INTAKE|EXIT_ONE_TYPE|WG2", chunk), m[1]
    if "own idea" in kind[1].lower():
        assert re.search(r"confidence", chunk, re.I), m[1]
    cleaned = re.sub(r"\\\(.*?\\\)|\$[^$]+\$|`[^`]+`", "MATH", body)
    cleaned = re.sub(r"\([^()]*\)", "PAREN", cleaned)
    cleaned = re.sub(r"\b[A-Z]\.\d+|\b(?:p|pp|n|d)\.", "REF", cleaned)
    sentences = len(re.findall(r"[.!?](?=\s+[A-Z]|$)", cleaned))
    assert 1 <= sentences <= 4, (m[1], sentences)
    note_checks.append({"id": m[1], "interpretive_sentence_count_heuristic": sentences,
                        "kind": kind[1], "context_and_register_present": True})
assert notes.count("\\(") == notes.count("\\)") and notes.count("$") % 2 == 0
context = [json.loads(s) for s in (ROOT / "research/context_search_log.jsonl").read_text().splitlines()]
assert len(context) == 744 and set(x["note"] for x in context) == set(ids)
assert all(n == 6 for n in collections.Counter(x["note"] for x in context).values())
assert len({(x["note"],x["source"]) for x in context}) == 744
evidence = json.loads((ROOT / "research/image_evidence_manifest.json").read_text())
assert len(evidence["images"]) == 27
doubt_records = [json.loads(s) for s in (ROOT / "doubt_records.jsonl").read_text().splitlines()]

report = {
    "verified_utc": UTC,
    "frozen_utc": frozen["frozen_utc"],
    "frozen_hashes_unchanged": True,
    "frozen_file_count": 45,
    "page_count": 44,
    "page_order": expected,
    "combined_equals_ordered_page_join": True,
    "inventory_count": len(inventory),
    "inventory_all_yes": True,
    "inventory_kinds": dict(collections.Counter(r["kind"] for r in inventory)),
    "page_done_records": len(done),
    "second_reading_records": len(audits),
    "supplied_images_inspected_before_freeze": pre["supplied_images"],
    "ocr_executed_on_supplied_images": False,
    "transcription_and_audit_single_stream": True,
    "context_opened_only_after_freeze": True,
    "latex_syntax_passes_before_freeze": 44,
    "latex_test_limit": pre["latex_test_mode"],
    "research_note_count": len(ids),
    "research_word_count": len(notes.split()),
    "context_search_records": len(context),
    "external_research_image_hashes": len(evidence["images"]),
    "doubt_record_count": len(doubt_records),
    "unresolved_requested_glossary_first_introduction": True,
    "exact_date_of_cote151_repair_unestablished": True,
    "frozen_hash_checks": hash_checks,
    "research_note_checks": note_checks,
}
(ROOT / "final_verification.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
with (ROOT / "progress.log").open("a") as f:
    f.write(f"post-freeze research completed {UTC}\n")
    f.write(f"research verification 124 notes; 744 per-note context-search records; separate 153 and 155 chapters {UTC}\n")
    f.write(f"final verification 44 pages; 132 supplied images read before freeze; 871 inventory elements all yes; 44 second-reading records {UTC}\n")
    f.write(f"frozen SHA-256 hashes rechecked: all 44 page files and the combined transcription unchanged {UTC}\n")
print(json.dumps({"verified_utc":UTC,"pages":44,"unchanged_hashes":45,
                  "inventory_yes":871,"notes":124,"context_search_records":744}))
