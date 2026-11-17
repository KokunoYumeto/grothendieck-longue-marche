#!/usr/bin/env python3
"""Validate and package the deliverable without changing frozen transcription."""
from pathlib import Path
from collections import Counter
import argparse
import csv
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
STEM = ROOT.name
parser = argparse.ArgumentParser()
parser.add_argument("--utc", required=True)
args = parser.parse_args()

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

expected = [(12, n) for n in range(150, 169)]
expected += [(15, n) for n in list(range(2, 15)) + list(range(16, 25)) + [26,28,30,32]]
pages = [ROOT / "pages" / f"{STEM}_{c}_scan{n:03d}.tex" for c, n in expected]
assert len(pages) == 45
assert set(pages) == set((ROOT / "pages").glob("*.tex"))

frozen = json.loads((ROOT / "records/frozen_sha256.json").read_text())
assert len(frozen["sha256"]) == 46
hash_checks = {name: sha(ROOT / name) == value for name, value in frozen["sha256"].items()}
assert all(hash_checks.values()), {k:v for k,v in hash_checks.items() if not v}

combined_path = ROOT / f"{STEM}_transcription.tex"
combined = combined_path.read_text()
assert combined == "\n\n".join(p.read_text().rstrip() for p in pages) + "\n"
assert combined.startswith("\\cotefile{12}\n\\scanpage{150}")
assert not any(x in combined for x in ["\\documentclass", "\\newcommand", "\\includegraphics"])
sequence = []
cote = None
for m in re.finditer(r"\\(cotefile|scanpage)\{(\d+)\}", combined):
    if m[1] == "cotefile":
        cote = int(m[2])
    else:
        sequence.append((cote, int(m[2])))
assert sequence == expected
for page in pages:
    s = page.read_text()
    stack = []
    for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", s):
        if m[1] == "begin":
            stack.append(m[2])
        else:
            assert stack and stack.pop() == m[2], page.name
    assert not stack, page.name
    depth = 0
    i = 0
    while i < len(s):
        if s[i] == "\\" and i+1 < len(s) and s[i+1] in "{}\\":
            i += 2
            continue
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            assert depth >= 0, page.name
        i += 1
    assert depth == 0, page.name

with (ROOT / f"{STEM}_inventory.csv").open(newline="") as f:
    reader = csv.DictReader(f)
    assert reader.fieldnames == ["cote","scan","sheet_kind","element","kind","position","first_words_or_objects","transcribed"]
    rows = list(reader)
assert len(rows) == 842
assert all(r["transcribed"] == "yes" for r in rows)
assert len({r["element"] for r in rows}) == len(rows)
assert {(int(r["cote"]),int(r["scan"])) for r in rows} == set(expected)
sheet_counts = Counter()
for c,n in expected:
    kinds = {r["sheet_kind"] for r in rows if int(r["cote"])==c and int(r["scan"])==n}
    assert len(kinds) == 1
    sheet_counts.update(kinds)
assert dict(sheet_counts) == {"text":34,"reused_typed":10,"cover":1}
doubt_count = len(re.findall(r"\\(?:unsure|illegible)\{", combined))
assert doubt_count == 354
assert len(re.findall(r"\\illegible\{", combined)) == 2

log_path = ROOT / "progress.log"
log = log_path.read_text()
done = [(int(c),int(n)) for c,n in re.findall(r"(?m)^(\d+) scan (\d+) done ", log)]
audited = [(int(c),int(n)) for c,n in re.findall(r"(?m)^(\d+) scan (\d+) audited ", log)]
assert done == expected
assert audited == expected
assert log.index("transcription frozen ") < log.index("context opened ")

notes_path = ROOT / f"{STEM}_notes.md"
notes = notes_path.read_text()
manifest = json.loads((ROOT / "records/notes_manifest.json").read_text())
expected_ids = [f"M{i:02}" for i in range(1,33)] + [f"FF{i:02}" for i in range(1,23)]
expected_ids += [f"D{i:02}" for i in range(1,31)] + [f"R{i:02}" for i in range(1,17)]
assert [m["id"] for m in manifest] == expected_ids
allowed = {"conjecture","unproved claim","unpursued implication","own idea","reading question","self-flagged","withdrawn in the same text"}
assert all(m["kind"] in allowed for m in manifest)
heads = list(re.finditer(r"(?m)^#{2,3} .+$", notes))
sentence_counts = {}
for i,h in enumerate(heads):
    m = re.match(r"### ([A-Z]+\d+) —", h[0])
    if not m:
        continue
    item = notes[h.start():heads[i+1].start() if i+1 < len(heads) else len(notes)]
    assert re.search(r"\*\*(?:Witness|Witness and quotation):", item), m[1]
    assert re.search(r"\*\*(?:RS|Register|Results ledger|RESULTS_STATE|Relation and RS):", item), m[1]
    assert "**Search terms:**" in item, m[1]
    if "**Kind:** own idea" in item:
        assert "Confidence" in item, m[1]
    body = item.split("\n\n", 2)[2].strip()
    body = re.sub(r"\\\[.*?\\\]|\\\(.*?\\\)", "MATH", body, flags=re.S)
    body = re.sub(r"\b(?:p|pp|e\.g|i\.e|resp|cf|Th|Prop)\.", lambda m:m[0].replace(".",""), body)
    body = re.sub(r"\b\d+\.\d+(?:\.\d+)*\b", "N", body)
    count = len(re.findall(r"""[.!?](?:[”’"')\]]*)?(?=\s+[A-ZÀ-ÖØ-Þ*]|\s*$)""", body))
    assert 1 <= count <= 4, (m[1],count)
    sentence_counts[m[1]] = count
assert list(sentence_counts) == expected_ids
for filename in [f"{STEM}_notes.md", f"{STEM}_doubts.md", "README_DELIVERY.md"]:
    expected_columns = None
    for i,line in enumerate((ROOT / filename).read_text().splitlines(), 1):
        if line.startswith("|"):
            columns = len(re.findall(r"(?<!\\)\|", line))-1
            if expected_columns is None:
                expected_columns = columns
            assert columns == expected_columns, (filename,i,columns,expected_columns)
        else:
            expected_columns = None
for heading in [
    "## Steps the manuscript itself marks as unverified",
    "## Title sheets, headings, and page counts",
    "## The required table: linear statement, non-linear statement",
    "### Standard-conjecture dictionary",
    "### S15: the modern comparisons, claim by claim",
    "## Effect on the supplied results register",
    "## References and exact editions consulted",
]:
    assert heading in notes, heading
searches = json.loads((ROOT / "records" / f"{STEM}_notes_context_searches.json").read_text())
assert [n["id"] for n in searches["notes"]] == expected_ids
assert not [n for n in searches["notes"] if "error" in n]
for name, value in searches["context_files"].items():
    assert sha(ROOT.parent / "context" / name) == value

report = {
    "validated_utc": args.utc,
    "pages": 45,
    "page_order_and_combined_equality": True,
    "frozen_utc": frozen["frozen_utc"],
    "frozen_hashes_unchanged": hash_checks,
    "completed_and_audited_in_order": True,
    "inventory_rows": len(rows),
    "all_inventory_rows_transcribed": True,
    "sheet_counts": dict(sheet_counts),
    "doubt_occurrences": doubt_count,
    "illegible_cancelled_prose_spans": 2,
    "notes": len(manifest),
    "allowed_note_kinds": True,
    "each_note_has_witness_context_search_and_register": True,
    "each_own_idea_has_confidence": True,
    "note_body_sentence_counts": sentence_counts,
    "note_sentence_count_check": "Automated punctuation check, supplementing the item-by-item research review; not a semantic proof.",
    "context_searches": 100,
    "context_queries_without_literal_hits": [n["id"] for n in searches["notes"] if not n["hit_counts"]],
    "context_input_hashes_unchanged": True,
    "markdown_table_columns": "consistent",
    "latex_structural_checks": "balanced braces/environments; correct page markers; no preamble or source images",
    "compiled_rendering": "unavailable: TeX format/package tree absent; no successful compilation claimed",
}
(ROOT / "records/final_validation.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
with log_path.open("a") as f:
    f.write(f"research notes complete {args.utc}: 100 numbered items; 100 per-item context searches; independent mathematical and quotation checks recorded\n")
    f.write(f"final verification {args.utc}: all 45 page SHA-256 hashes and the combined transcription SHA-256 are unchanged from the pre-context freeze\n")
    f.write(f"final verification {args.utc}: 45 ordered page files; 842 inventory rows all yes; 354 uncertainty occurrences; requested notes sections present\n")
    f.write(f"final ZIP prepared {args.utc}: supplied scans, attached source archives and context sources excluded; no additional milestone checkpoint\n")

def deliverable_files():
    return [p for p in sorted(ROOT.rglob("*")) if p.is_file()
            and "__pycache__" not in p.parts and p.suffix != ".pyc"]

file_manifest = {
    "created_utc": args.utc,
    "scope": "All enclosed files except this self-referential manifest; supplied scans and context sources excluded.",
    "files": {str(p.relative_to(ROOT)):sha(p) for p in deliverable_files()
              if p.name != "delivery_manifest.json"}
}
(ROOT / "records/delivery_manifest.json").write_text(
    json.dumps(file_manifest,ensure_ascii=False,indent=2)+"\n")
archive = ROOT.parent / f"{STEM}.zip"
files = deliverable_files()
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in files:
        z.write(p, str(p.relative_to(ROOT.parent)))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(files)
    for name,value in frozen["sha256"].items():
        assert hashlib.sha256(z.read(STEM+"/"+name)).hexdigest() == value
print(json.dumps({
    "archive":str(archive),
    "bytes":archive.stat().st_size,
    "sha256":sha(archive),
    "files":len(files),
    "archive_crc_and_frozen_hashes_verified":True,
    "validation_record":"records/final_validation.json",
},ensure_ascii=False))
