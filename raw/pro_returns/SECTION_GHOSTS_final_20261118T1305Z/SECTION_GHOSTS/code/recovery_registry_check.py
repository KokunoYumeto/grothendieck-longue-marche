#!/usr/bin/env python3
"""Verify the final source/register/citation correspondence without new research."""
from pathlib import Path
from collections import Counter
import csv,json,re
ROOT=Path(__file__).resolve().parents[1]
main=(ROOT/"SECTION_GHOSTS_paper.tex").read_text()
parts=[ROOT/"SECTION_GHOSTS_paper.tex"]
parts += [ROOT/(s if s.endswith(".tex") else s+".tex") for s in re.findall(r"\\input\{([^}]+)\}",main)]
assert all(p.exists() for p in parts)
ids=[]
for p in parts:
    ids += [(a,b,str(p.relative_to(ROOT))) for a,b in re.findall(r"\\begin\{result\}\{([^}]+)\}\{([^}]+)\}",p.read_text())]
with (ROOT/"SECTION_GHOSTS_results.csv").open(newline="") as f:
    reader=csv.DictReader(f);fields=reader.fieldnames;rows=list(reader)
assert len(ids)==len(set(a for a,b,c in ids))
assert {r["id"]:r["status"] for r in rows}=={a:b for a,b,c in ids}
for row in rows:
    if row["status"]=="Open":
        assert all(k in row["notes"] for k in ["Cases proved:","Computations:","Exact obstruction:"]),row["id"]
alltext="\n".join(p.read_text() for p in parts)
keys=set(re.findall(r"(?m)^@\w+\s*\{\s*([^,\s]+)\s*,",(ROOT/"SECTION_GHOSTS_references.bib").read_text()))
cites=set()
for x in re.findall(r"\\cite\w*(?:\[[^\]]*\])?(?:\[[^\]]*\])?\{([^}]+)\}",alltext):
    cites.update(y.strip() for y in x.split(","))
assert not(cites-keys),cites-keys
with (ROOT/"CHECK_EVENTS.tsv").open(newline="") as f:events=list(csv.DictReader(f,delimiter="\t"))
out={
"included_tex_files":len(parts),"results_in_sources":len(ids),"result_registry_exact_match":True,
"status_counts":dict(Counter(r["status"] for r in rows)),
"bibliography_keys":len(keys),"cited_keys":len(cites),"missing_citation_keys":sorted(cites-keys),
"open_ids":[r["id"] for r in rows if r["status"]=="Open"],"check_events":len(events),
"recovery_output_json_is_object":isinstance(json.loads((ROOT/"code/verify_primitive_five_recovery.json").read_text()),dict)
}
(ROOT/"code/recovery_registry_check.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
