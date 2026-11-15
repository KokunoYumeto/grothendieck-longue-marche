#!/usr/bin/env python3
"""Check assembled research links, control bytes, context coverage and output totals."""
from pathlib import Path
import csv,json,re
ROOT=Path(__file__).resolve().parent.parent
R=ROOT/"research"
files=[ROOT/"MPL_72_035-081_notes.md"]+sorted(R.glob("*.md"))
errors=[]
for path in files:
    text=path.read_text()
    for n,line in enumerate(text.splitlines(),1):
        if any(ord(c)<32 and c!="\t" for c in line):
            errors.append({"file":str(path.relative_to(ROOT)),"line":n,"error":"control character"})
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)",text):
        dest=m.group(2)
        if dest.startswith(("http://","https://","#")) or "context/" in dest:continue
        if not (path.parent/dest).exists():
            errors.append({"file":str(path.relative_to(ROOT)),"error":"missing local link","target":dest})
manifest=json.loads((R/"context_search_manifest.json").read_text())
ids=[n["id"] for n in manifest["notes"]]
if len(ids)!=len(set(ids)):errors.append({"error":"duplicate context-audit item ID"})
enum=json.loads((R/"enumeration_checks.json").read_text())
inv=json.loads((R/"invariant_subspaces_results.json").read_text())
bridge=json.loads((R/"bridge_computation.json").read_text())
if enum["all_exact_checks_passed"] is not True:errors.append({"error":"enumeration check failure"})
if inv["totals"]["candidate_or_count_failures"]!=0:errors.append({"error":"classification/count comparison failure"})
facts={
    "markdown_files_checked":len(files),
    "combined_notes_words":len((ROOT/"MPL_72_035-081_notes.md").read_text().split()),
    "context_items":len(ids),"context_queries":sum(len(n["queries"]) for n in manifest["notes"]),
    "context_audit_rows":manifest["audit_rows"],
    "enumeration_exact_checks":len(enum["checks"]),
    "enumeration_literal_questions":enum["literal_questions"],
    "enumeration_catalogue_rows":len(list(csv.DictReader((R/"enumeration_catalogue.csv").open()))),
    "prose_case_rows":len(list(csv.DictReader((R/"case_catalogue.csv").open()))),
    "invariant_subspace_totals":inv["totals"],
    "bridge_levels":bridge["levels"],
}
result={"ok":not errors,"errors":errors,"facts":facts,
        "scope":"Structural checks and previously computed result totals; mathematical proofs and source readings require the accompanying human-readable audit."}
(R/"research_validation.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
print(json.dumps(result,indent=2,ensure_ascii=False))
raise SystemExit(bool(errors))
