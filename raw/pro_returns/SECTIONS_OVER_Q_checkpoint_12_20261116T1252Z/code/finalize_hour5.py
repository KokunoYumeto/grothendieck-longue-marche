#!/usr/bin/env python3
"""Finalize the fifth hourly report only after the actual visual review."""
from pathlib import Path
import csv, json, re
import fitz
w=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((w/'SECTIONS_OVER_Q_results.csv').open()))
counts={status:sum(r['status']==status for r in rows) for status in ('Proved','Refuted','Known','Open')}
bib=(w/'SECTIONS_OVER_Q_references.bib').read_text()
bib_count=len(re.findall(r'(?m)^@\w+\{',bib))
pages=len(fitz.open(w/'SECTIONS_OVER_Q_paper.pdf'))
typesetting=json.loads((w/'notes/typesetting_current.json').read_text())
assert typesetting['overfull_hboxes']==0 and typesetting['overfull_vboxes']==0
assert not typesetting['undefined_references'] and not typesetting['undefined_citations']
review=json.loads((w/'qa/visual_review.json').read_text())
assert review['reviewed_build_pages']==pages
assert review['status'].startswith('Visually inspected')
render=json.loads((w/'qa/render_record.json').read_text())
assert render['pdf_pages']==pages
p=w/'SECTIONS_OVER_Q_report.md'; report=p.read_text()
assert report.startswith('INCOMPLETE\n')
outcomes=[line for line in report.splitlines()[:55] if re.match(r'^\| (?:[ABCD]\d+|L\d+) \|',line)]
assert len(outcomes)==45, len(outcomes)
expected={f'A{i}' for i in range(1,16)}|{f'B{i}' for i in range(1,4)}|{'C1','C2','D1','D2','D3','D5'}|{f'L{i}' for i in range(1,22)}
assert {line.split(' | ')[0][2:] for line in outcomes}==expected
new_paragraph=(f'Exact mathematical programs and actual outputs are retained under code/. Finite certificates check their stated finite identities; the infinite constructions have explicit proofs. The current LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical boxes, and no undefined citations or references. All {len(render["rendered_pages"])} pages in the current render record are covered by the visual-review record, including the new fifth-hour arguments and every page of B.16. The full-resolution inspections are listed there. Earlier mathematical and typesetting corrections remain recorded in the audit notes and retained build logs. The contact sheets, page images and review record are under qa/. The report remains INCOMPLETE because both principal assertions A1 and the other open item scopes remain unresolved. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claimed.')
report=re.sub(r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)',lambda m:m.group(1)+new_paragraph+'\n',report,flags=re.S)
lines=report.splitlines()
for i,line in enumerate(lines[:55]):
 if line.startswith(('| A7 |','| L15 |')):
  line=line.replace('A.64 adds ±16p^n under full H-conjugacy.','A.64 proves the initial ±16p^n result, and A.91 removes its H-conjugacy hypothesis.')
  line=line.replace('A.64 additionally recognizes lambda=±16p^n for odd primesp and n≥1 under H-conjugacy.','A.91 recognizes lambda=±16p^n for odd primesp and n≥1 under arbitrary labeled integral comparison.')
  extra=' A.87 also recognizes every3^n+1 without H, and A.91 fixes all contact-four dyadic labels and removes the H proviso for ±16p^n and its six transforms.'
  if extra not in line:line=line[:-2]+extra+' |'
  lines[i]=line
report='\n'.join(lines)+'\n'
heading='## Fifth-hour progress review — 2026-11-16 05:52 UTC'
progress=('Continue. The fifth hour advances A5, A7, A9, A12 and A15 through substantive compatibility and recognition results. A.90 constructs fully completed old-coordinate data through a specified Brauer-obstructed neighborhood and proves that its fourth rational coordinate is impossible even modulo2. A.86, A.89 and A.92 turn the one-variable obstruction into a concrete compatible ideal-class problem, compute the exact local correction modules, and prove the finite class-generation equality. A.87 and A.91 remove earlier comparison hypotheses from entire recognition families. B.16 constructs two integral coefficient systems sharing every local elliptic curve and having infinite common ramification away from coefficient-prime exceptions. Both assertions A1 remain open. The next work targets compatible split-prime corrections for the same norm-tower class, the exact finite-quotient detection of the completed puncture obstruction, and further structural recognition of the remaining cusp equations.')
if heading not in report:report+='\n'+heading+'\n\n'+progress+'\n'
p.write_text(report)
checkpoint_heading='## Checkpoint05 — 2026-11-16 05:52 UTC'
record=(f'Fifth hourly snapshot: {pages}-page clean PDF; {len(rows)} registered statements ({counts["Proved"]} Proved, {counts["Refuted"]} Refuted, {counts["Known"]} Known, {counts["Open"]} Open);45 required outcome rows;{bib_count} explicitly verified/unverified bibliography entries; all current notes, sources, certificates and actual outputs, code, build logs and visual QA. The {len(render["rendered_pages"])} rendered pages are covered by the recorded visual review. The fifth-hour progress review directs continued work because the main routes and open items have advanced. A1 remains unresolved and the report begins INCOMPLETE. Drafts not active in the main TeX are retained as work in progress and excluded from the statement counts. The archive excludes supplied background, runtime caches and earlier checkpoint ZIPs. The checkpoint writer hashes the exact bytes that it stores and verifies every saved manifest entry.')
cp=w/'notes/checkpoints.md'; existing=cp.read_text()
if checkpoint_heading not in existing:cp.write_text(existing+'\n'+checkpoint_heading+'\n\n'+record+'\n')
with (w/'notes/root_progress.md').open('a') as f:f.write('\n05:52 UTC progress review: '+progress+'\n')
out={'pdf_pages':pages,'statements':len(rows),'status_counts':counts,'outcome_rows':45,'bibliography_entries':bib_count,'rendered_pages':len(render['rendered_pages']),'typesetting':typesetting,'main_status':'INCOMPLETE; both A1 assertions open','hourly_decision':'continue'}
text=json.dumps(out,indent=2)+'\n'
Path(__file__).with_name('finalize_hour5_output.txt').write_text(text)
(w/'code/checkpoint05_preflight_output.txt').write_text(text)
print(text,end='')
