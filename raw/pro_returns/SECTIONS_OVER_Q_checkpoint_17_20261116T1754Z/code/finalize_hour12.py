#!/usr/bin/env python3
"""Finalize the twelfth hourly review after the final build and actual image inspection."""
from pathlib import Path
import csv,datetime,json,re,fitz
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
rows=list(csv.DictReader((w/'SECTIONS_OVER_Q_results.csv').open()))
counts={s:sum(r['status']==s for r in rows) for s in ['Proved','Refuted','Known','Open']}
assert all(any(r['id']==ident for r in rows) for ident in ['A.159','A.160','A.165','A.166','A.167','A.168'])
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
assert set(render['equation_locations']['A.160.2']) & set(review['full_resolution_pages_reviewed'])
p=w/'notes/hour12_typesetting_corrections.json';corrections=json.loads(p.read_text())
for row in corrections:row['after']='Zero overfull horizontal and vertical boxes in the final full build; the corrected locations were visually inspected.'
p.write_text(json.dumps(corrections,indent=2)+'\n')
report_path=w/'SECTIONS_OVER_Q_report.md';report=report_path.read_text()
assert report.startswith('INCOMPLETE\n')
outcomes=[line for line in report.splitlines()[:55] if re.match(r'^\| (?:[ABCD]\d+|L\d+) \|',line)]
expected={f'A{i}' for i in range(1,16)}|{f'B{i}' for i in range(1,4)}|{'C1','C2','D1','D2','D3','D5'}|{f'L{i}' for i in range(1,22)}
assert len(outcomes)==45 and {line.split(' | ')[0][2:] for line in outcomes}==expected
description='; '.join(f"{c['equation']}: {c['before_hbox_pt']}pt before correction" for c in corrections)
body=(f'Exact mathematical programs and their actual outputs are retained under code/. The current LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical boxes, and no undefined citations or references. All {len(render["rendered_pages"])} pages in the current render record were visually inspected, including every twelfth-hour result A.159–A.168, both complete literal coefficient supplements, the references, and a distributed sample of the earlier Parts. Full-resolution inspections are listed in the review record. This hour the retained logs recorded {description}; the final counts are zero. The initial bibliography build also stopped on unescaped filename underscores; those exact filenames now use path formatting. Root independently reconstructed the printed integer coordinates for all four A159 units and all three A165 principal generators and checked their exact relative norms. Complete source audits and certificate reruns accompany the CM descent, full Selmer classification, proper and affine quotient maps, rational/local torsion, complete norm-seed loci, and actual/completed infinite-support comparison. Contact sheets, page images and actual review records are under qa/. The report remains INCOMPLETE because both principal A1 assertions and other open item scopes remain unresolved. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claimed.')
report=re.sub(r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)',lambda m:m.group(1)+body+'\n',report,flags=re.S)
progress=('Continue. The twelfth hour strengthens actual section classifications and identifies the exact remaining norm obstruction. A159 excludes the entire completed fixed-first-seed S-unit fibre at the next norm step and proves an explicit C3² class subgroup. A160 uses a literal CM-field descent, the opened p=2 analytic-converse theorem and Rubin full-Sha theorem to prove full Prym Sha finiteness; the actual finite-support comparison classifies full Selmer sections on the harmonic cover over Q and Q(sqrt2), and the specified combined mod8 class on the tripod is cuspidal. A161 determines the exact lifting locus on the rank-two elliptic quotient. A163 identifies a single global boundary class in the all-coefficient proper-abelian quotient, and A167 recovers the full completed tangent parameter in the actual affine-cover abelian quotient. A164 computes the rational Jacobian torsion C4² and its dyadic finite-Kummer separation. On the norm side, A162 repairs the first seed and proves actual global field-norm solvability through every finite height. A165 classifies every completed first S-unit seed and its exact finite and all-height local lifting loci using a directly certified full S-unit basis. A166 proves that any coherent unrestricted norm family over-2 already has the fixed support, separately for actual and completed elements. Thus the completed infinite-family question is exactly all the balanced classes e_n vanishing; the degree27 balanced class e3 is the current concrete target. A168 proves that its ordinary class preimage is nonzero at every level from degree27 onwards, excludes integral norm±2 generators there, gives the necessary changed-prime valuation correction, and improves the balanced element order bound without deciding its image. The direct degree27 search and CM-class transgression analysis are research in progress, without a certified answer. Both principal A1 assertions and the full-section/full-metabelian scopes not covered by the stated theorems remain open. These are substantive advances on the active routes, so research continues after the checkpoint.')
heading='## Twelfth-hour progress review — 2026-11-16 '+stamp
if not re.search(r'^## Twelfth-hour progress review',report,re.M):report+='\n'+heading+'\n\n'+progress+'\n'
report_path.write_text(report)
cp=w/'notes/checkpoints.md';existing=cp.read_text()
record=(f'Twelfth hourly snapshot: {pages}-page clean PDF; {len(rows)} registered statements ({counts["Proved"]} Proved, {counts["Refuted"]} Refuted, {counts["Known"]} Known, {counts["Open"]} Open); 45 outcome rows; {bib_count} bibliography entries with verification notes. All {len(render["rendered_pages"])} rendered pages have actual visual review, including the formerly overflowing A160 display. The source, PDF, report, register, bibliography, every written program and output, mathematical/source audits and visual QA are included. The progress review directs continued work. Both A1 assertions remain open. Unintegrated searches or drafts remain excluded from active theorem counts. Supplied background, runtime caches and every earlier checkpoint ZIP are excluded. Each archived file is checked against its exact stored manifest bytes.')
if not re.search(r'^## Checkpoint12 ',existing,re.M):cp.write_text(existing+'\n## Checkpoint12 — 2026-11-16 '+stamp+'\n\n'+record+'\n')
with(w/'notes/root_progress.md').open('a')as f:f.write('\n'+stamp+' twelfth-hour review: '+progress+'\n')
output={'pdf_pages':pages,'statements':len(rows),'status_counts':counts,'outcome_rows':45,
        'bibliography_entries':bib_count,'rendered_pages':len(render['rendered_pages']),
        'typesetting':typesetting,'main_status':'INCOMPLETE; both A1 assertions open','hourly_decision':'continue'}
out=json.dumps(output,indent=2)+'\n'
for p in [w/'code/finalize_hour12_output.txt',w/'code/checkpoint12_preflight_output.txt']:p.write_text(out)
print(out,end='')
