"""Record completed fresh visible inspection; this script does not inspect images."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re

root=Path(__file__).resolve().parents[1]
m=json.loads((root/'records/checkpoint23_metrics.json').read_text())
assert m['statements']==283 and m['pages']>=439
assert m['statuses']=={'Known':6,'Proved':239,'Refuted':19,'Open':19}
assert m['bibliography_entries']==111 and m['task_rows']==49
assert not m['overfull'] and not m['warnings'] and not m['errors']
assert hashlib.sha256((root/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==m['pdf_sha256']
bbl=(root/'LM4_SUCCESSOR_paper.bbl').read_text()
assert len(re.findall(r'\\bibitem',bbl))==111
qa=root/'records/pdf_qa'
manifest=json.loads((qa/'checkpoint23_final/render_manifest.json').read_text())
pages=manifest['rendered_pages']
assert manifest['page_count']==m['pages']
individual=[1,2]+list(range(337,352))+list(range(435,m['pages']+1))
assert set(individual)<=set(pages)
sheets=sorted((qa/'checkpoint23_final').glob('contact-*.png'))
assert len(sheets)==6
before=(qa/'checkpoint23_before_bibliography_inclusion/LM4_SUCCESSOR_paper.log').read_text()
assert not re.findall(r'Overfull \\hbox',before)
failed=(qa/'checkpoint23_bibliography_path_failure/LM4_SUCCESSOR_paper.log').read_text()
assert 'Missing $ inserted' in failed
now=datetime.now(timezone.utc).isoformat()
record=f'''# Twenty-third-hour final typesetting and visible verification

Final PDF SHA-256:{m['pdf_sha256']}.
Final size:{m['pdf_bytes']} bytes;{m['pages']} pages.
Register:283 statements;239 Proved,19 Refuted,19 Open,6 Known.
Bibliography:111 entries in both the source database and printed bbl.
Task/lead rows:49. Visual review: PASS.

The first combined build compiled cleanly in439 pages. We inspected
six contact sheets covering46 pages and19 individual pages,including
every page337--351 of B112--B114. No layout defect was found. That
inspection exposed a bibliography inclusion issue: two opened research
references existed in the111-entry database but were not printed because
they were not formally cited. We added explicit nocite entries. The
second build then failed at an unescaped underscore in those two note
paths. Its genuine log,bbl,source bibliography and driver are preserved.
The established breakable path command repaired both paths. The third
complete build was clean but printed102 references. A direct bibitem count
identified nine older research-audit entries that were also uncited. We
then included the complete database explicitly. The fourth build
exposed a previously unprinted undated entry whose empty year was
incompatible with natbib author-year labels. Its exact source,log,bbl
and auxiliary are preserved. We used the truthful date label n.d. and
regenerated the stale auxiliary. The fifth complete build is final,with
all111 printed references; the clean third PDF,source,bbl,log and metrics
are separately retained.

Initial/final combined overfull counts:0/0,also0/0 above2pt.
Maximum initial/final overflow:0pt/0pt. The intermediate second-build
failure was one observed TeX Missing-dollar error,not a completed PDF.
The fourth attempt also failed author-year validation; neither failed
attempt is described as a successful final build.
Final log:zero overfull boxes,warnings,undefined references anderrors.

B112's private component had a genuine initial runtime-format failure,
then a10.80762pt display overflow before its clean seven-page build.
B114's earlier component retained an orphan proof-ending symbol and
the opposite-lift interpretation; both were corrected before integration.
All component sources,attempts,logs and renders remain with their own
QA records. They are not counted as root's final combined inspection.

We freshly rendered the FINAL PDF and inspected all six final contact
sheets,covering{len(pages)} pages across every Part and the bibliography.
We then opened{len(individual)} final pages individually:the title and
continued abstract/contents,every complete new mathematical page337--351,
and the final bibliography pages435--{m['pages']},including both newly
printed scope-audit references. Equations,tags,tables,proof endings and
record paths fit. No clipping,overlap,missing glyph or layout defect
was found. The earlier first-build inspection is retained separately;
none of it substitutes for a fresh final view.

Rendered pages:{pages}
Individually inspected final pages:{individual}
Contact sheets inspected:6,all from the final PDF.

Genuine drivers:checkpoint23_build1_driver.log,
checkpoint23_build2_driver.log,checkpoint23_build3_driver.log,
checkpoint23_build4_driver.log,checkpoint23_build5_driver.log.
Complete genuine TeX/BibTeX passes:records/build_passes/.
Final metrics:records/checkpoint23_metrics.json.
First-build renders:records/pdf_qa/checkpoint23_first_build/.
Final renders:records/pdf_qa/checkpoint23_final/.
Recorded at{now}.
'''
(root/'records/checkpoint23_typesetting.txt').write_text(record)
(root/'records/checkpoint23_visual_review.json').write_text(json.dumps({
 'recorded_at':now,'pdf_sha256':m['pdf_sha256'],
 'rendered_pages':pages,'individually_inspected_pages':individual,
 'contact_sheets_inspected':6,'combined_overfull_before':0,
 'combined_overfull_after':0,'intermediate_observed_build_errors':['Missing $ inserted from unescaped bibliography path; repaired with path command.','Undated entry produced incompatible natbib author-year label; explicitly marked n.d. with unknown-date note retained.'],
 'printed_bibliography_entries':111,'visual_review':'PASS'
},indent=2)+'\n')
p=root/'LM4_SUCCESSOR_report.md';s=p.read_text()
marker='### Twenty-third-hour final typesetting verification'
assert marker not in s
s+=f'''\n{marker}

The final paper has{m['pages']} pages,283 statements and111 PRINTED
bibliography entries. Its SHA-256 is{m['pdf_sha256']}; size
{m['pdf_bytes']} bytes. Initial/final combined overfull counts are0/0,
including beyond2pt. A second-build bibliography path error was preserved
and repaired with breakable path commands. A formerly unprinted undated
entry was marked n.d. to retain author-year citations; build5 is
clean,with zero warnings,undefined references anderrors.

Six fresh final contact sheets cover{len(pages)} pages across all Parts.
We inspected{len(individual)} final pages individually,including all
pages337--351 of B112--B114 and the new printed references. No clipping,
overlap,missing glyph or layout defect was found. Complete first/final
inspection and genuine repair history:records/checkpoint23_typesetting.txt
and records/checkpoint23_visual_review.json. Both main decisions remain Open.
'''
p.write_text(s)
print('PASS fresh final visual review recorded:',m['pages'],'pages;',len(pages),'sampled;',len(individual),'individual views;111 printed references.')
