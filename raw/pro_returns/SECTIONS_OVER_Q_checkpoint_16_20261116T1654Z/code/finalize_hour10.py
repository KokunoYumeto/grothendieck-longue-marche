#!/usr/bin/env python3
"""Record the tenth progress review after actual clean build and visual review."""
from pathlib import Path
import csv,datetime,json,re,fitz
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
rows=list(csv.DictReader((w/'SECTIONS_OVER_Q_results.csv').open()))
counts={s:sum(r['status']==s for r in rows) for s in ['Proved','Refuted','Known','Open']}
assert any(r['id']=='A.149' for r in rows)
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
p=w/'notes/hour10_typesetting_corrections.json'
corrections=json.loads(p.read_text())
for row in corrections:row['after']='Zero overfull horizontal and vertical boxes in the final full build.'
p.write_text(json.dumps(corrections,indent=2)+'\n')
report_path=w/'SECTIONS_OVER_Q_report.md';report=report_path.read_text()
assert report.startswith('INCOMPLETE\n')
outcomes=[line for line in report.splitlines()[:55] if re.match(r'^\| (?:[ABCD]\d+|L\d+) \|',line)]
expected={f'A{i}' for i in range(1,16)}|{f'B{i}' for i in range(1,4)}|{'C1','C2','D1','D2','D3','D5'}|{f'L{i}' for i in range(1,22)}
assert len(outcomes)==45
assert {line.split(' | ')[0][2:] for line in outcomes}==expected
description='; '.join(f"{c['equation']}: {c['before_hbox_pt']}pt before correction" for c in corrections)
body=(f'Exact mathematical programs and their actual outputs are retained under code/. Finite certificates check their stated finite identities; the infinite constructions have explicit proofs. The current LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical boxes, and no undefined citations or references. All {len(render["rendered_pages"])} pages in the current render record were visually inspected, including every active tenth-hour result from A.140 through A.149 and a distributed sample of the earlier Parts. Full-resolution inspections are listed in that record. This hour the retained logs recorded {description}; all were corrected in the source, and the final counts are zero. The new finite witness correction at eleven replaces roots of minus two by their inverses when giving the actual old-cover Y-coordinate; the final source and executed certificate use 2 and 9. Earlier mathematical and typesetting corrections remain in the retained logs and audit notes. Contact sheets, page images and the actual review record are under qa/. The report remains INCOMPLETE because both principal A1 assertions and other open item scopes remain unresolved. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claimed.')
report=re.sub(r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)',lambda m:m.group(1)+body+'\n',report,flags=re.S)
progress=('Continue. The tenth hour advances both exact norm compatibility and full-section obstruction routes. A.140 proves the actual wild-place norm maps after a radicand change. A.141 removes the boundary inertia from the finite Brauer detector, obtaining an explicit quotient of order 512 and exact class 6. A.142 constructs a fixed-local tripod pair whose additional coordinate satisfies every restricted-product condition but fails quadratic reciprocity. A.143 computes the actual rank-two elliptic factor and its zero central L-value, and excludes non-torsion finite-primary completed classes from full Selmer lifts. A.144 passes every finite norm test in one explicit changed tower. A.145 proves the uniform nine-place detector and a compact Cantor family of continuum many infinite-support ordinary pairs excluded through the same quotient. A.146 excludes an explicit infinite-primary subgroup, including classes with every primary component nonzero, by exact integral reduction and a positive-density sieve. A.147 proves actual pure-tower unit norm surjectivity and a coherent completed prime-generator family, with its exact scalar comparison. A.148 excludes all profinite unit multiples on the two explicit elliptic lines and retains 846 necessary finite residue tests with their propagated divisibilities. A.149 resolves compatibility in the specific changed tower for 3*11^24: a ray-class/inertia calculation, finite PT duality, diagonal coefficient limits and actual Shapiro maps produce one completed global S-unit norm family with its prescribed first representative and norm -2 over Q. This last result is three-primary and one-variable; it does not supply an ordinary infinite-support pair or a full metabelian lift. Next work computes the actual two-prime class pairing needed to iterate this update and the complementary Prym factors and Selmer groups, while retaining the original A1 and generic-reconstruction problems. Both A1 assertions remain open.')
heading='## Tenth-hour progress review — 2026-11-16 '+stamp
if not re.search(r'^## Tenth-hour progress review',report,re.M):report+='\n'+heading+'\n\n'+progress+'\n'
report_path.write_text(report)
cp=w/'notes/checkpoints.md';existing=cp.read_text()
record=(f'Tenth hourly snapshot: {pages}-page clean PDF; {len(rows)} registered statements ({counts["Proved"]} Proved, {counts["Refuted"]} Refuted, {counts["Known"]} Known, {counts["Open"]} Open); 45 outcome rows; {bib_count} bibliography entries with verification notes. All {len(render["rendered_pages"])} rendered pages have actual visual review. The source, PDF, report, register, bibliography, every program and output, mathematical/source audits and visual QA are included. The progress review directs continued work. Both A1 assertions remain open. Unintegrated research notes or drafts remain excluded from active theorem counts. Supplied background, runtime caches and every earlier checkpoint ZIP are excluded. Each archived file is checked against the exact stored manifest bytes.')
if not re.search(r'^## Checkpoint10 ',existing,re.M):cp.write_text(existing+'\n## Checkpoint10 — 2026-11-16 '+stamp+'\n\n'+record+'\n')
with(w/'notes/root_progress.md').open('a')as f:f.write('\n'+stamp+' tenth-hour review: '+progress+'\n')
output={'pdf_pages':pages,'statements':len(rows),'status_counts':counts,'outcome_rows':45,
        'bibliography_entries':bib_count,'rendered_pages':len(render['rendered_pages']),
        'typesetting':typesetting,'main_status':'INCOMPLETE; both A1 assertions open',
        'hourly_decision':'continue'}
out=json.dumps(output,indent=2)+'\n'
for p in [w/'code/finalize_hour10_output.txt',w/'code/checkpoint10_preflight_output.txt']:p.write_text(out)
print(out,end='')
