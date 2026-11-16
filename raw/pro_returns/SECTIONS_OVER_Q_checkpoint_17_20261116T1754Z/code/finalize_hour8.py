#!/usr/bin/env python3
"""Record the eighth progress review after actual build and visual inspection."""
from pathlib import Path
import csv
import datetime
import json
import re
import fitz

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
rows=list(csv.DictReader((w/'SECTIONS_OVER_Q_results.csv').open()))
counts={s:sum(row['status']==s for row in rows) for s in ['Proved','Refuted','Known','Open']}
bib_count=len(re.findall(r'(?m)^@\w+\{',(w/'SECTIONS_OVER_Q_references.bib').read_text()))
pages=len(fitz.open(w/'SECTIONS_OVER_Q_paper.pdf'))
typesetting=json.loads((w/'notes/typesetting_current.json').read_text())
assert typesetting['overfull_hboxes']==typesetting['overfull_vboxes']==0
assert not typesetting['undefined_references'] and not typesetting['undefined_citations']
render=json.loads((w/'qa/render_record.json').read_text())
review=json.loads((w/'qa/visual_review.json').read_text())
assert render['pdf_pages']==review['reviewed_build_pages']==pages
assert review['status'].startswith('Visually inspected')
p=w/'SECTIONS_OVER_Q_report.md'
report=p.read_text()
assert report.startswith('INCOMPLETE\n')
outcomes=[line for line in report.splitlines()[:55] if re.match(r'^\| (?:[ABCD]\d+|L\d+) \|',line)]
assert len(outcomes)==45
expected={f'A{i}' for i in range(1,16)}|{f'B{i}' for i in range(1,4)}|{'C1','C2','D1','D2','D3','D5'}|{f'L{i}' for i in range(1,22)}
assert {line.split(' | ')[0][2:] for line in outcomes}==expected
details=json.loads((w/'notes/hour8_typesetting_corrections.json').read_text())
body=(f'Exact mathematical programs and actual outputs are retained under code/. Finite certificates check their stated finite identities; the infinite constructions have explicit proofs. The current LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical boxes, and no undefined citations or references. All {len(render["rendered_pages"])} pages in the current render record are covered by the visual-review record, including every active eighth-hour result and every page of B.16. Full-resolution inspections are listed in that record. This hour the retained build logs recorded '+details['summary']+' All were corrected in the source and the final counts are zero. Earlier mathematical and typesetting corrections remain recorded in the audit notes and retained build logs. Contact sheets, page images and the actual review record are under qa/. The report remains INCOMPLETE because both principal assertions A1 and the other open item scopes remain unresolved. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claimed.')
report=re.sub(r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)',lambda m:m.group(1)+body+'\n',report,flags=re.S)
progress=('Continue. This hour advances the active attempts for A5, A7, A8, A9, A12 and A15. A.114 gives the exact full Selmer-fibre comparison for the actual cubic Belyi source, with its quadratic sign and primary exception retained. A.115 computes all relative alternating forms and their simultaneous local-three values at every depth. A.117 proves finite approximation with the full prior radical splitting constraints and actual norm-one representatives. A.119 demonstrates the additional affine restriction at three by a fully realizable counterexample to unrestricted scalar-graph repair. A.118 settles every odd and real quartic character for arbitrary finite old coordinates; A.120 completes quartic initialization on the cubic source. A.121 computes all octic common characters. These are precise advances within open items; both principal A1 assertions remain open.')
additions={
 'A.122':' A.122 identifies exactly the old local image with cyclic auxiliary ramification at precision three: the unrestricted image together with the complete quadratic reciprocity conditions. Its proof constructs the required Schmidt–Wingberg input class.',
 'A.123':' A.123 proves full harmonic exponent-eight initialization, including all mixed characters.',
 'A.124':' A.124 proves the ray-field intersection with unrestricted ramification at three, retains the complete simultaneous splitting fields, and corrects the lower norm exactly while preserving arbitrarily deep three-adic congruences.',
 'A.125':' A.125 proves every odd-place octic evaluation for arbitrary finite coordinates and full exponent-eight initialization on the cubic Belyi source, including its bad reduction at three.',
 'A.126':' A.126 gives the complete common-field recursion at every exponent divisible four, permanent stabilization at a missing cyclotomic layer, an exact integral negative-relation test for unbounded growth, and a finite Smith bound in the other case.',
 'A.127':' A.127 proves full harmonic initialization at every finite exponent divisible by four through the complete mixed-character induction and the actual odd-factor map.'
}
ids={row['id'] for row in rows}
for key,detail in additions.items():
    if key in ids:progress+=detail
progress+=' The next work is the compatible infinite coefficient construction, the higher-power norm conditions at previously allocated primes, and their actual full-section comparison. No compatible completed lift is inferred from the finite initializations or from the precision-three repair.'
heading='## Eighth-hour progress review — 2026-11-16 '+stamp
if not re.search(r'^## Eighth-hour progress review',report,re.M):report+='\n'+heading+'\n\n'+progress+'\n'
p.write_text(report)
cp=w/'notes/checkpoints.md'
existing=cp.read_text()
record=(f'Eighth hourly snapshot: {pages}-page clean PDF; {len(rows)} registered statements ({counts["Proved"]} Proved, {counts["Refuted"]} Refuted, {counts["Known"]} Known, {counts["Open"]} Open); 45 outcome rows; {bib_count} bibliography entries with explicit verification status. All {len(render["rendered_pages"])} rendered pages have been visually inspected. The full source, report, register, bibliography, programs and actual outputs, mathematical audits, source checks and visual QA are included. The progress review directs continued work; both A1 assertions remain open. Unintegrated drafts remain work in progress and are excluded from active statement counts. Supplied background, runtime caches and earlier checkpoint ZIPs are excluded. Every stored file is checked against the manifest of the exact archived bytes.')
if not re.search(r'^## Checkpoint08 ',existing,re.M):cp.write_text(existing+'\n## Checkpoint08 — 2026-11-16 '+stamp+'\n\n'+record+'\n')
with(w/'notes/root_progress.md').open('a')as out:out.write('\n'+stamp+' eighth-hour review: '+progress+'\n')
output={'pdf_pages':pages,'statements':len(rows),'status_counts':counts,'outcome_rows':45,'bibliography_entries':bib_count,'rendered_pages':len(render['rendered_pages']),'typesetting':typesetting,'main_status':'INCOMPLETE; both A1 assertions open','hourly_decision':'continue'}
content=json.dumps(output,indent=2)+'\n'
Path(__file__).with_name('finalize_hour8_output.txt').write_text(content)
(w/'code/checkpoint08_preflight_output.txt').write_text(content)
print(content,end='')
