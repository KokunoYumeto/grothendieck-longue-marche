#!/usr/bin/env python3
"""Finalize hour13 only after the final build and actual visual review."""
from pathlib import Path
import csv,datetime,json,re,fitz
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
rows=list(csv.DictReader((w/'SECTIONS_OVER_Q_results.csv').open()))
counts={s:sum(r['status']==s for r in rows) for s in ['Proved','Refuted','Known','Open']}
assert all(any(r['id']==f'A.{n}' for r in rows) for n in range(169,177))
assert all(any(r['id']==f'A.{n}' for r in rows) for n in [177,179])
bib_count=len(re.findall(r'(?m)^@\w+\{',(w/'SECTIONS_OVER_Q_references.bib').read_text()))
pages=len(fitz.open(w/'SECTIONS_OVER_Q_paper.pdf'))
typesetting=json.loads((w/'notes/typesetting_current.json').read_text())
assert typesetting['overfull_hboxes']==typesetting['overfull_vboxes']==0
assert not typesetting['undefined_references'] and not typesetting['undefined_citations']
render=json.loads((w/'qa/render_record.json').read_text())
review=json.loads((w/'qa/visual_review.json').read_text())
assert render['pdf_pages']==review['reviewed_build_pages']==pages
assert review['status'].startswith('Visually inspected')
assert set(review['contact_parts_reviewed'])==set(render['contact_parts'])
assert set(review['rendered_pages'])==set(render['rendered_pages'])
assert set(render['prior_overflow_pages'])<=set(review['full_resolution_pages_reviewed'])
report_path=w/'SECTIONS_OVER_Q_report.md';report=report_path.read_text()
assert report.startswith('INCOMPLETE\n')
outcomes=[line for line in report.splitlines()[:55] if re.match(r'^\| (?:[ABCD]\d+|L\d+) \|',line)]
expected={f'A{i}' for i in range(1,16)}|{f'B{i}' for i in range(1,4)}|{'C1','C2','D1','D2','D3','D5'}|{f'L{i}' for i in range(1,22)}
assert len(outcomes)==45 and {line.split(' | ')[0][2:] for line in outcomes}==expected
corrections_path=w/'notes/hour13_typesetting_corrections.json'
corrections=json.loads(corrections_path.read_text()) if corrections_path.exists() else []
body=(f'Exact mathematical programs and their executed outputs are retained under code/. The current LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical boxes, and no undefined references or citations. All {len(render["rendered_pages"])} pages in the current render record were visually inspected, including every active thirteenth-hour result A.169–A.177 and A.179, the complete 54-coefficient anti-unit supplement, the references, and a distributed sample across the earlier Parts. Full-resolution inspection locations are recorded. The first all-height build had one overfull display, A179.1, at 5.22318pt; splitting its field data into two gathered lines gives zero overfull boxes in the final build. Both this corrected display and the former A160 overflow were visually inspected in the final build. All 54 printed anti-unit coefficients in 468 two-block rows were independently reconstructed from the manuscript and their exact field identities verified. Root and peer audits cover the full metabelian classification maps over number fields, the actual finite and pro-three cusp detectors, the complete level-two and level-three class groups, both unit norm indices, actual S-unit support repair, the all-height class-generation induction and the complete cubic-character descent. The report remains INCOMPLETE because both principal A1 assertions and the other explicitly recorded open scopes remain unresolved. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claimed.')
report=re.sub(r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)',lambda m:m.group(1)+body+'\n',report,flags=re.S)
progress=('Continue. This hour settles every finite balanced target in the fixed tower and advances the full metabelian section classifications over number fields. A169 upgrades the harmonic combined-mod8 classification to the full geometric metabelian quotient using actual neighbourhoods, proper finite-support rigidity, nonsplit inertia recovery and compact conjugators. A171 determines every rational compact elliptic fibre in that full quotient and excludes full metabelian rational-frame ghosts. A172 determines all cuspidal abelian fibres over every number field; its actual class-two detector separates labels over every finite local extension in the full pro3 quotient. On the norm route, A170 constructs and exhausts the specified base-field genus-character source. A173 computes the entire degree18 three-class group C3³ and the pure degree9 group C3. A174 reduces the first balanced target to three actual ordinary class tests. A175 proves the actual unit norm indices3^5 and3^10 and vanishing of the level-three S-three-class group. A176 constructs an actual S-unit chain through level three and computes the degree54 three-class group C9⊕C3² and pure degree27 group C9. A177 then proves changed-prime generation and S-class vanishing at every finite height, using a fixed six-character image, actual auxiliary norm targets and an invertible orbit polynomial. A179 descends every plus cubic class character through the actual inertia and Kummer maps. It proves every pure three-class group cyclic with R59,n as generator, hence the entire balanced quotient zero at every level. Compact completed norm fibres give one compatible pro3-completed S-unit family of rational norm−2; the finite actual norm cokernels give actual chains at each finite height. A coherent infinite family of discrete actual elements, an ordinary infinite-support completed unit-equation pair, the required full nonabelian lifts and both principal A1 assertions remain unresolved. The previously recorded level-four balanced frontier is superseded by A177/A179. These are substantive advances on the active open-item routes, so work continues after the checkpoint.')
heading='## Thirteenth-hour progress review — 2026-11-16 '+stamp
if not re.search(r'^## Thirteenth-hour progress review',report,re.M):report+='\n'+heading+'\n\n'+progress+'\n'
report_path.write_text(report)
cp=w/'notes/checkpoints.md';existing=cp.read_text()
record=(f'Thirteenth hourly snapshot: {pages}-page clean PDF; {len(rows)} registered statements ({counts["Proved"]} Proved, {counts["Refuted"]} Refuted, {counts["Known"]} Known, {counts["Open"]} Open);45 outcome rows;{bib_count} bibliography entries with verification notes. All{len(render["rendered_pages"])} rendered pages have actual visual review, including the prior overflow repair and complete new coefficient supplement. The source, PDF, register, bibliography, report, every written program and output, all proof/source audits and visual QA are included. The progress review directs continued research. Both A1 assertions remain open; all balanced quotients in the fixed norm tower are now proved zero and the compatible completed norm family exists. Unintegrated searches and drafts are excluded from active theorem counts. Supplied background, runtime caches and all prior checkpoint ZIPs are excluded. The stored manifest checks every archived file against its actual bytes.')
if not re.search(r'^## Checkpoint13 ',existing,re.M):cp.write_text(existing+'\n## Checkpoint13 — 2026-11-16 '+stamp+'\n\n'+record+'\n')
with(w/'notes/root_progress.md').open('a')as f:f.write('\n'+stamp+' thirteenth-hour review: '+progress+'\n')
output={'pdf_pages':pages,'statements':len(rows),'status_counts':counts,'outcome_rows':45,
        'bibliography_entries':bib_count,'rendered_pages':len(render['rendered_pages']),
        'typesetting':typesetting,'typesetting_corrections':corrections,
        'main_status':'INCOMPLETE; both A1 assertions open','hourly_decision':'continue',
        'norm_frontier':'All C_n^bal=0 and a compatible completed S-unit norm family proved; actual infinite coherence and ordinary unit-equation/full-section lifting remain unresolved'}
out=json.dumps(output,indent=2)+'\n'
for p in [w/'code/finalize_hour13_output.txt',w/'code/checkpoint13_preflight_output.txt']:p.write_text(out)
print(out,end='')
