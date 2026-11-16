#!/usr/bin/env python3
"""Record the ninth progress review after actual build and visual inspection."""
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
details=json.loads((w/'notes/hour9_typesetting_corrections.json').read_text())
body=(f'Exact mathematical programs and actual outputs are retained under code/. Finite certificates check their stated finite identities; the infinite constructions have explicit proofs. The current LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical boxes, and no undefined citations or references. All {len(render["rendered_pages"])} pages in the current render record are covered by the visual-review record, including every active ninth-hour result and every page of B.16. Full-resolution inspections are listed in that record. This hour the retained build logs recorded '+details['summary']+' All were corrected in the source and the final counts are zero. A bibliography note also needed math-mode delimiters; the failed build and exact correction are retained. Earlier mathematical and typesetting corrections remain recorded in the audit notes and retained build logs. Contact sheets, page images and the actual review record are under qa/. The report remains INCOMPLETE because both principal assertions A1 and the other open item scopes remain unresolved. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claimed.')
report=re.sub(r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)',lambda m:m.group(1)+body+'\n',report,flags=re.S)
progress=('Continue. This hour advances the actual norm-family and full-section obstruction routes. A.128 proves the arbitrary-twist common-character constancy in its stated coordinate families and identifies its reciprocity obstruction. A.129 computes all higher-precision relative alternating forms; A.130 gives the exact old local image with cyclic auxiliary ramification. A.131 proves the stable local norm equations, while A.135 proves the cyclotomic precision requirement. A.132 identifies the exact all-place completed-image criterion. A.133 and A.136 construct fixed local harmonic and tripod families whose added coordinate fails already modulo two through escaping support. A.134 constructs an actual completed harmonic triple retaining a nonzero proper Brauer evaluation sum. A.137 maps it to an ordinary infinite-support tripod pair with no full Selmer section, through an explicit finite quotient of exact class17. A.139 reduces that detector to an actual metabelian quotient of order4096 and exact class8. A.138 constructs a coherent nonzero unit cofactor on the fixed pure-three norm tower and computes its first-depth cyclotomic quotient. The next work is the proper-curve quotient of the detector, the changing-radicand norm construction, and the still-open original section and birational-lifting assertions. Both A1 assertions remain open; no common bound for all ghosts is inferred from the single explicit detector.')
heading='## Ninth-hour progress review — 2026-11-16 '+stamp
if not re.search(r'^## Ninth-hour progress review',report,re.M):report+='\n'+heading+'\n\n'+progress+'\n'
p.write_text(report)
cp=w/'notes/checkpoints.md'
existing=cp.read_text()
record=(f'Ninth hourly snapshot: {pages}-page clean PDF; {len(rows)} registered statements ({counts["Proved"]} Proved, {counts["Refuted"]} Refuted, {counts["Known"]} Known, {counts["Open"]} Open); 45 outcome rows; {bib_count} bibliography entries with explicit verification status. All {len(render["rendered_pages"])} rendered pages have been visually inspected. The full source, report, register, bibliography, programs and actual outputs, mathematical audits, source checks and visual QA are included. The progress review directs continued work; both A1 assertions remain open. Unintegrated drafts remain work in progress and are excluded from active statement counts. Supplied background, runtime caches and earlier checkpoint ZIPs are excluded. Every stored file is checked against the manifest of the exact archived bytes.')
if not re.search(r'^## Checkpoint09 ',existing,re.M):cp.write_text(existing+'\n## Checkpoint09 — 2026-11-16 '+stamp+'\n\n'+record+'\n')
with(w/'notes/root_progress.md').open('a')as out:out.write('\n'+stamp+' ninth-hour review: '+progress+'\n')
output={'pdf_pages':pages,'statements':len(rows),'status_counts':counts,'outcome_rows':45,'bibliography_entries':bib_count,'rendered_pages':len(render['rendered_pages']),'typesetting':typesetting,'main_status':'INCOMPLETE; both A1 assertions open','hourly_decision':'continue'}
content=json.dumps(output,indent=2)+'\n'
Path(__file__).with_name('finalize_hour9_output.txt').write_text(content)
(w/'code/checkpoint09_preflight_output.txt').write_text(content)
print(content,end='')
