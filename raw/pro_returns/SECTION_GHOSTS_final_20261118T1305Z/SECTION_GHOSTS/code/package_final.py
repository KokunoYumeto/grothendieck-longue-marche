#!/usr/bin/env python3
"""Consolidate and verify the final incomplete deliverable; no new research."""
from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import csv,json,hashlib,re,zipfile
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parents[1]/"output";OUT.mkdir(exist_ok=True)
expected="fed1f30941dbbe05d50da29e95bc9d236b571e0ef449912bbcc4805fabcd3563"
pdf=ROOT/"SECTION_GHOSTS_paper.pdf"
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==expected
assert len(PdfReader(pdf).pages)==378
build=json.loads((ROOT/"code/final_build_verification.json").read_text())
assert build["build_exit_code"]==0 and build["overfull_boxes"]==0
assert build["undefined_citations_or_references"]==0 and build["all_fonts_embedded"]
assert not build["latex_warning_lines"] and not build["bibtex_warning_lines"]
review_paths={
"root":"qa/root/visual_review.json",
"ghost_audit":"qa/ghost/visual_QA.json",
"cohomology_audit":"qa/cohomology/visual_qa_report.json",
"literature":"qa/literature/visual_qa_findings.json"
}
page_keys={"root":"pages_rendered","ghost_audit":"viewed_pdf_pages","cohomology_audit":"physical_pages_actually_viewed","literature":"actually_viewed_pages"}
reviews={};viewed=set()
for who,name in review_paths.items():
    x=json.loads((ROOT/name).read_text())
    assert x.get("pdf_sha256",x.get("source_sha256"))==expected,name
    if who=="root":assert x["viewed"]
    pages=x[page_keys[who]];viewed.update(pages)
    reviews[who]={"pages_actually_viewed":pages,"report":name}
assert len(viewed)==56
with (ROOT/"SECTION_GHOSTS_results.csv").open(newline="") as f:rows=list(csv.DictReader(f))
assert len(rows)==228 and sum(r["status"]=="Open" for r in rows)==9
with (ROOT/"CHECK_EVENTS.tsv").open(newline="") as f:events=list(csv.DictReader(f,delimiter="\t"))
assert len(events)==796
assert (ROOT/"SECTION_GHOSTS_report.md").read_text().splitlines()[0]=="INCOMPLETE"
reg=json.loads((ROOT/"code/recovery_registry_check.json").read_text())
assert reg["result_registry_exact_match"] and reg["missing_citation_keys"]==[]
now=datetime.now(timezone.utc)
summary={
"status":"INCOMPLETE","research_stopped_utc":"2026-11-18T12:45:16+00:00",
"packaging_verification_utc":now.isoformat(),"packaging_verification_cet":now.astimezone(ZoneInfo("Europe/Berlin")).isoformat(),
"paper":build,"registry":reg,"visual_reviews":reviews,
"distinct_pages_actually_viewed":sorted(viewed),"distinct_viewed_page_count":len(viewed),
"visual_scope":"All post-checkpoint proof additions, historical-register/bibliography pages, front matter and representative older body pages; not a whole-document visual review.",
"historical_audit":{"total":90,"confirmed":87,"repaired":2,"pending":1,"pending_item":"GT_TOWER_CHECK A4.57"},
"original_checkpoint08_sha256":"3f67e030dc6328440381bb3c9e78b688991bc376ec4408df37b00837694b49b5",
"exact_lost_bytes":"See notes/final_reconstruction_boundary.md; no byte recovery of original post-checkpoint E214/E215 Python certificates is claimed."
}
(ROOT/"code/final_package_verification.json").write_text(json.dumps(summary,indent=2)+"\n")
verification=f"""# Final verification record

**Research status: INCOMPLETE.** The second consecutive no-movement review stopped research at 12:45:16 UTC (13:45:16 CET),18 November2026.

## Current paper and metadata

- PDF:378pages,2,671,609bytes.
- PDF SHA-256:{expected}.
- LuaLaTeX/BibTeX:successful final settling build;0 overfull boxes,0 unresolved citations/references,0 LaTeX warnings,0 BibTeX warnings,0 missing-character messages.
- Fonts:all29 embedded.
- Result registry:228 exact source-matched IDs;201 Proved,15 Known,3 Refuted,9 Open.
- Bibliography:98 keys,89 cited; no missing citation key.
- Check events:796 records, comprising the exact775-event checkpoint08 baseline and21 accurately scoped recovery records.
- Historical audit:90 rows;87 confirmed,2 repaired,1 pending. The exact66-item E.2 list is audited.

## Actual visual inspection

The four readers actually opened rendered images covering **56 distinct pages** of this exact PDF. The reviewed pages are:

{", ".join(map(str,sorted(viewed)))}.

These include every added proof from P.16 and E.214-E.218, the catalog/gluing addendum, the historical-register and bibliography pages, front matter, the C.7 wording clarification, and representative earlier body pages. This is not a claim that all378 pages were visually inspected.

No clipping, overlap, missing mathematical glyph, equation-tag collision, heading collision or footer intrusion was found on the reviewed pages. The individual reports and actual viewed montages are retained in qa/. Source text extraction and build logs were not substituted for image viewing.

## Reproduction and recovery scope

Use code/build.py on a complete TeX Live installation, or code/tex_recovery_bootstrap.py with the documented stripped-runtime prerequisites. The latter uses bundled hash-verified upstream archives without network downloads.

The canonical final source files and current PDF are included. Some post-checkpoint proofs are faithful mathematical transcriptions, not restored original bytes. The original E.214/E.215 Python certificate files and their original output bytes remain unavailable; their actual earlier execution evidence and retained hashes are recorded. The separately executed recovery JavaScript and actual output are included under distinct names.

The current results are internally checked AI-produced work. Agreement among readers is not external mathematical certification. No full-pronilpotent ordinary ghost, full pro-prime ordinary ghost, universal finite-support theorem, or unconditional manuscript-conjecture resolution is claimed.

Verification recorded at {now.isoformat()}.
"""
(ROOT/"FINAL_VERIFICATION.md").write_text(verification)
report=ROOT/"SECTION_GHOSTS_report.md"
text=report.read_text()
marker="\n## Final consolidated artifact verification\n"
if marker in text:text=text.split(marker)[0]
text+=marker+"""
The final paper has378 pages and was rebuilt with LuaLaTeX after restoration. The final settling build has zero overfull boxes, zero unresolved citations/references, zero LaTeX/BibTeX warnings and zero missing-character messages; all29 fonts are embedded. The exact PDF SHA-256 is fed1f30941dbbe05d50da29e95bc9d236b571e0ef449912bbcc4805fabcd3563.

The source and CSV agree on all228 result IDs:201 Proved,15 Known,3 Refuted and9 Open. There are98 bibliography keys,89 cited, and796 actual check-event records. The exact historical register remains90 rows:87 confirmed,2 repaired and1 pending.

Four readers actually viewed rendered images of56 distinct pages, including all post-checkpoint proof additions and the full historical-register/bibliography range. No visible layout defect was found on the inspected pages. This is not a claim of whole-document visual inspection.

The exact original E.214 and E.215 post-checkpoint Python checker/output bytes were not recovered. Their earlier executed evidence and hashes, the separately executed JavaScript recovery verifier, and faithful full proof transcriptions are clearly distinguished. This is a consolidated current deliverable, not a claim of byte-for-byte recovery of every lost working file.

See FINAL_VERIFICATION.md, code/final_package_verification.json, and notes/final_reconstruction_boundary.md for the exact scope.
"""
report.write_text(text)
ledger=ROOT/"PROGRESS_LEDGER.md"
ledger.write_text(ledger.read_text()+"\n\n## Final consolidation and verification\n\n"+
now.isoformat()+": Research remains stopped. The current378-page paper builds cleanly;228 source/CSV IDs agree;56 distinct pages were actually visually inspected. Final packaging contains the restored checkpoint, recovered full proofs and explicit lost-byte provenance. No new main-question movement or status closure is claimed.\n")
# The manifest excludes its own self-referential hash.
manifest=ROOT/"FILE_LIST.tsv"
files=sorted(p for p in ROOT.rglob("*") if p.is_file() and p!=manifest)
with manifest.open("w",newline="") as f:
    w=csv.writer(f,delimiter="\t");w.writerow(["relative_path","size_bytes","sha256"])
    for p in files:w.writerow([p.relative_to(ROOT).as_posix(),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest()])
allfiles=sorted(p for p in ROOT.rglob("*") if p.is_file())
archive=OUT/"SECTION_GHOSTS_final.zip"
with zipfile.ZipFile(archive,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in allfiles:z.write(p,Path("SECTION_GHOSTS")/p.relative_to(ROOT))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(allfiles)
    assert z.read("SECTION_GHOSTS/SECTION_GHOSTS_report.md").startswith(b"INCOMPLETE\n")
    with manifest.open(newline="") as f:
        for row in csv.DictReader(f,delimiter="\t"):
            b=z.read("SECTION_GHOSTS/"+row["relative_path"])
            assert len(b)==int(row["size_bytes"])
            assert hashlib.sha256(b).hexdigest()==row["sha256"]
receipt={"archive":str(archive),"bytes":archive.stat().st_size,"sha256":hashlib.sha256(archive.read_bytes()).hexdigest(),"files":len(allfiles),"zip_integrity":"PASS","manifest_verification":"Every included file except the manifest itself verified byte-for-byte","paper_pages":378,"results":228,"open":9,"check_events":796,"distinct_pages_actually_viewed":56}
(OUT/"SECTION_GHOSTS_final_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
