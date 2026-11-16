#!/usr/bin/env python3
"""Finalize the sixth checkpoint report after the actual PDF review."""
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
text=(f'Exact mathematical programs and actual outputs are retained under code/. Finite certificates check their stated finite identities; the infinite constructions have explicit proofs. The current LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical boxes, and no undefined citations or references. All {len(render["rendered_pages"])} pages in the current render record are covered by the visual-review record, including every sixth-hour result and every page of B.16. The full-resolution inspections are listed there. During this hour A.93 initially had one9.35667pt overflow; a later build found two A.96 overflows of6.26230pt and10.96935pt. These were split in the source, and the final counts are zero. Seventeen missing display terminators in A.97 were also restored before the successful full build. Earlier mathematical and typesetting corrections remain recorded in the audit notes and retained build logs. Contact sheets, page images and the actual review record are under qa/. The report remains INCOMPLETE because both principal assertions A1 and the other open item scopes remain unresolved. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claimed.')
report=re.sub(r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)',lambda m:m.group(1)+text+'\n',report,flags=re.S)
heading='## Sixth-hour progress review — 2026-11-16 06:47 UTC'
progress=('Continue. The sixth hour has produced substantive advances in A5, A7, A9, A12 and A15. A.93 locates the completed four-puncture obstruction in an explicit finite metabelian quotient. A.95 constructs one fixed norm tower with dense compatible-divisor image. A.96 settles two-coordinate quartic initialization, and A.97 gives the exact coefficient-rigidity criteria. A.98 proves that a specified norm representative can fail to extend even for a rational pair with an explicit compatible family. A.99–A.101 repair finite support while preserving lower norm classes and compute the simultaneous representative-radical fields needed for the next step. A.102 constructs the actual congruence-plus-abelian quotient matching every bad place and uses the good prime47 to prove recognition of254. Both assertions A1 remain open. The next main work is to solve the coupled local unit norm conditions at the fresh support primes and obtain a single coherent infinite norm family; the puncture route is testing the exact harmonic degree-two comparison, and the congruence route is extending the coefficient-to-good-prime constraints.')
if heading not in report:report+='\n'+heading+'\n\n'+progress+'\n'
search_heading='## Harmonic tripod comparison: exact searches retained'
if search_heading not in report:
    report+='\n'+search_heading+'\n\nThe actual map T↦4T(1−T) from the four-punctured line with third finite puncture1/2 to the tripod is finite etale of degree2. The work notes retain its exact completed Kummer and finite-quotient comparisons. The required new arithmetic obstruction has not been obtained. The doubling family search checked140 admissible covers,1,178,342 local trials and259,197 actual local points, with no nonzero evaluation. A second test from two exact points on y²=x³−1156x checked38,468 trials and17,303 actual local points, again without a nonzero evaluation. The code and outputs are retained; these finite searches prove no general constancy or nonexistence assertion.\n'
p.write_text(report)
cp=w/'notes/checkpoints.md'
existing=cp.read_text()
cpheading='## Checkpoint06 — 2026-11-16 '+stamp
record=(f'Sixth hourly snapshot: {pages}-page clean PDF; {len(rows)} registered statements ({counts["Proved"]} Proved, {counts["Refuted"]} Refuted, {counts["Known"]} Known, {counts["Open"]} Open);45 outcome rows;{bib_count} bibliography entries with explicit verification status. All {len(render["rendered_pages"])} rendered pages have been visually inspected. The full source, report, register, bibliography, programs and actual outputs, mathematical audits, source checks and visual QA are included. The progress review directs continued work; both A1 assertions remain open. Unintegrated drafts are retained as work in progress and excluded from active statement counts. Supplied background, runtime caches and earlier checkpoint ZIPs are excluded. Every stored file is checked against the manifest of the exact archived bytes.')
if not re.search(r'^## Checkpoint06 ',existing,re.M):cp.write_text(existing+'\n'+cpheading+'\n\n'+record+'\n')
with (w/'notes/root_progress.md').open('a') as out:out.write('\n'+stamp+' sixth-hour review: '+progress+'\n')
output={'pdf_pages':pages,'statements':len(rows),'status_counts':counts,'outcome_rows':45,'bibliography_entries':bib_count,'rendered_pages':len(render['rendered_pages']),'typesetting':typesetting,'main_status':'INCOMPLETE; both A1 assertions open','hourly_decision':'continue'}
content=json.dumps(output,indent=2)+'\n'
Path(__file__).with_name('finalize_hour6_output.txt').write_text(content)
(w/'code/checkpoint06_preflight_output.txt').write_text(content)
print(content,end='')
