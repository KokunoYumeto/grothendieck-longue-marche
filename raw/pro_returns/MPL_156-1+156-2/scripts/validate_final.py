"""Final structural verification of the completed package; no source rewrites."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import json
import re

root=Path(__file__).resolve().parents[1]
name="MPL_156-1+156-2"
freeze=json.loads((root/"records/transcription_freeze.json").read_text())
for rel,digest in freeze["sha256"].items():
    assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==digest,rel
pages=[root/"pages"/f"{name}_{c}_scan{n:03}.tex" for c,total in [("156-1",27),("156-2",19)] for n in range(1,total+1)]
assert len(list((root/"pages").glob("*.tex")))==46
combined=(root/f"{name}_transcription.tex").read_text()
assert combined=="\n".join(p.read_text().rstrip()+"\n" for p in pages)
assert combined.startswith("\\cotefile{156-1}\n\\scanpage{1}")
assert re.findall(r"\\cotefile\{([^}]+)\}",combined)==["156-1","156-2"]
assert re.findall(r"\\scanpage\{(\d+)\}",combined)==[str(n) for total in [27,19] for n in range(1,total+1)]
assert "\\documentclass" not in combined
with (root/f"{name}_inventory.csv").open(newline="") as f:
    reader=csv.DictReader(f)
    assert reader.fieldnames==["cote","scan","sheet_kind","element","kind","position","first_words_or_objects","transcribed"]
    rows=list(reader)
assert len(rows)==955 and all(r["transcribed"]=="yes" for r in rows)
required={(c,str(n)) for c,total in [("156-1",27),("156-2",19)] for n in range(1,total+1)}
assert {(r["cote"],r["scan"]) for r in rows}==required
log=(root/"progress.log").read_text()
assert {(c,str(int(n))) for c,n in re.findall(r"(156-[12]) scan (\d{3}) audited ",log)}>=required
assert {(c,str(int(n))) for c,n in re.findall(r"(156-[12]) scan (\d{3}) done ",log)}>=required
unc=json.loads((root/"records/uncertainty_index.json").read_text())
counts=Counter(x["macro"] for x in unc)
assert counts=={"unsure":472,"illegible":1}
for macro,n in counts.items():
    assert len(re.findall(r"\\"+macro+r"\{",combined))==n
for x in unc:
    source=(root/"pages"/f"{name}_{x['cote']}_scan{x['scan']:03}.tex").read_text()
    assert "\\"+x["macro"]+"{"+x["argument"]+"}" in source,x
notes=(root/f"{name}_notes.md").read_text()
heads=list(re.finditer(r"^#{3,4} ([DABPT]\d{2}) — (.+)$",notes,re.M))
expected=[f"{prefix}{n:02}" for prefix,total in [("D",16),("A",29),("B",53),("P",16),("T",11)] for n in range(1,total+1)]
assert [h.group(1) for h in heads]==expected
for i,h in enumerate(heads):
    end=heads[i+1].start() if i+1<len(heads) else len(notes)
    block=notes[h.end():end]
    assert "**Source:**" in block and "**Kind:**" in block,h.group(1)
    assert any(x in block for x in ["**Quote:**","**Anchor:**","**Brief quote:**"]),h.group(1)
    assert "**Context:** search:" in block,h.group(1)
    if re.search(r"\*\*Kind:\*\*[^\n]*own idea",block):
        assert "confidence" in block.lower(),h.group(1)
ledger=json.loads((root/"records/research_context_searches.json").read_text())
assert [n["note_id"] for n in ledger["notes"]]==expected
assert len(ledger["standing_and_open_item_searches"])==35
assert all(x["returncode"] in [0,1] for x in ledger["notes"]+ledger["standing_and_open_item_searches"])
assert len(re.findall(r"^\| SF\d{2} \|",notes,re.M))==26
assert notes.count("### Primary manuscript evidence")==1
for p in root.rglob("*.md"):
    s=p.read_text()
    assert not any(ord(c)<32 and c not in "\n\r\t" for c in s),p
for p in root.rglob("*"):
    if p.is_file():
        assert p.suffix.lower() not in {".jpg",".jpeg",".png",".pdf",".zip"},p
now=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
result={"verified_utc":now,"frozen_utc":freeze["frozen_utc"],"unchanged_sha256_files":47,
        "scan_pages":46,"cote_counts":{"156-1":27,"156-2":19},"inventory_rows_all_yes":955,
        "uncertainty_occurrences":dict(counts),"research_note_entries":125,
        "standing_audit_entries":26,"open_register_items_compared":9,
        "actual_context_searches":160,"notes_word_count":len(notes.split()),
        "input_images_and_archives_excluded":True}
(root/"records/final_validation.json").write_text(json.dumps(result,indent=2)+"\n")
with (root/"progress.log").open("a") as f:
    f.write(f"final package validation passed {now}; 46 pages, 955 inventory rows all yes, 473 uncertainty marks, 125 research notes, 160 context searches; all 47 frozen hashes unchanged\n")
print(json.dumps(result,indent=2))
