#!/usr/bin/env python3
"""Finalize the eleventh hourly review only after actual PDF and image checks."""
from pathlib import Path
import csv,datetime,json,re,fitz
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
rows=list(csv.DictReader((w/'SECTIONS_OVER_Q_results.csv').open()))
counts={s:sum(r['status']==s for r in rows) for s in ['Proved','Refuted','Known','Open']}
assert any(r['id']=='A.158' for r in rows)
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
assert set(render['rendered_pages'])==set(review['rendered_pages'])
p=w/'notes/hour11_typesetting_corrections.json';corrections=json.loads(p.read_text())
for row in corrections:row['after']='Zero overfull horizontal and vertical boxes in the final full build.'
p.write_text(json.dumps(corrections,indent=2)+'\n')
report_path=w/'SECTIONS_OVER_Q_report.md';report=report_path.read_text()
assert report.startswith('INCOMPLETE\n')
outcomes=[line for line in report.splitlines()[:55] if re.match(r'^\| (?:[ABCD]\d+|L\d+) \|',line)]
expected={f'A{i}' for i in range(1,16)}|{f'B{i}' for i in range(1,4)}|{'C1','C2','D1','D2','D3','D5'}|{f'L{i}' for i in range(1,22)}
assert len(outcomes)==45 and {line.split(' | ')[0][2:] for line in outcomes}==expected
description='; '.join(f"{c['equation']}: {c['before_hbox_pt']}pt before correction" for c in corrections)
body=(f'Exact mathematical programs and their actual outputs are retained under code/. The current LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical boxes, and no undefined citations or references. All {len(render["rendered_pages"])} pages in the current render record were visually inspected, including every active eleventh-hour result A.150–A.158 and a distributed sample of the earlier Parts. Full-resolution inspections are listed in that record. This hour the retained logs recorded {description}; both were fixed in the source, and the final counts are zero. The initial A.154 build also exposed an undefined Sha macro; its explicit operator definition repairs that diagnostic. Mathematical corrections before integration included the A.152 finite-reduction residue column, the complete split-prime denominator support in the Fisher calculation, and removal of the false A.155 precision bound based only on the order of its distinguished class. The last correction has an executed C9 counterexample. Every local witness, exact norm, unit-residue and finite-module calculation used in the active proofs is retained, with independent audits. Contact sheets, page images and actual review records are under qa/. The report remains INCOMPLETE because both principal A1 assertions and other open item scopes remain unresolved. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claimed.')
report=re.sub(r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)',lambda m:m.group(1)+body+'\n',report,flags=re.S)
progress=('Continue. The eleventh hour establishes exact complementary Prym arithmetic and strengthens the actual section obstruction. A.150 constructs the Prym maps and computes both isogeny Selmer groups. A.152 proves dyadic Kummer injectivity by the exact duplication valuations. A.154 combines a rank-four isogeny pairing with a separately certified nonzero full two-cover pairing to prove rank zero, full2-Selmer order8, and Sha[2∞]=C2², without an analytic rank or full-Sha finiteness assumption. Its finite-to-continuous comparison forces dyadic cuspidality for full Selmer sections on the harmonic cover. A.157 computes the whole proper pro2 homology quotient and excludes every ordinary completed pair in the combined modulo8 class from locally matching full and pro2 metabelian sections, with no nine-centre constraint. A.158 gives point-dependent finite tests with quotient order2^(6n+9) and exact class4n+6, including the one-centre−899 test of order32768 and class10. On the norm side, A.151 and A.153 prove that the nonzero class quotient persists even after every fixed finite support enlargement. A.155 identifies the precise target class and pairing at every finite coefficient precision. A.156 proves an exact two-level S-unit norm extension of the fixed first seed, and proves that its displayed second representative fails the next local norm at11 and59. The remaining work is substantive: a local unit computation is being audited for a complete repair obstruction, and an exact CM-field descent is being checked against primary analytic-converse and Sha results for a possible all-coefficient upgrade. Those continuations are not counted as active results until audited and integrated. Both principal A1 assertions, the coherent infinite-support metabelian construction and the other listed open scopes remain open.')
heading='## Eleventh-hour progress review — 2026-11-16 '+stamp
if not re.search(r'^## Eleventh-hour progress review',report,re.M):report+='\n'+heading+'\n\n'+progress+'\n'
report_path.write_text(report)
cp=w/'notes/checkpoints.md';existing=cp.read_text()
record=(f'Eleventh hourly snapshot: {pages}-page clean PDF; {len(rows)} registered statements ({counts["Proved"]} Proved, {counts["Refuted"]} Refuted, {counts["Known"]} Known, {counts["Open"]} Open); 45 outcome rows; {bib_count} bibliography entries with verification notes. All {len(render["rendered_pages"])} rendered pages have actual visual review. The source, PDF, report, register, bibliography, every written program and output, mathematical/source audits and visual QA are included. The progress review directs continued work. Both A1 assertions remain open. Unintegrated research notes or drafts remain excluded from active theorem counts. Supplied background, runtime caches and every earlier checkpoint ZIP are excluded. Each archived file is checked against its exact stored manifest bytes.')
if not re.search(r'^## Checkpoint11 ',existing,re.M):cp.write_text(existing+'\n## Checkpoint11 — 2026-11-16 '+stamp+'\n\n'+record+'\n')
with(w/'notes/root_progress.md').open('a')as f:f.write('\n'+stamp+' eleventh-hour review: '+progress+'\n')
output={'pdf_pages':pages,'statements':len(rows),'status_counts':counts,'outcome_rows':45,
        'bibliography_entries':bib_count,'rendered_pages':len(render['rendered_pages']),
        'typesetting':typesetting,'main_status':'INCOMPLETE; both A1 assertions open',
        'hourly_decision':'continue'}
out=json.dumps(output,indent=2)+'\n'
for p in [w/'code/finalize_hour11_output.txt',w/'code/checkpoint11_preflight_output.txt']:p.write_text(out)
print(out,end='')
