#!/usr/bin/env python3
"""Finalize checkpoint fourteen only after a clean build and actual visual review."""
from pathlib import Path
import csv, datetime, json, re
import fitz

w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
rows = list(csv.DictReader((w/'SECTIONS_OVER_Q_results.csv').open()))
counts = {s:sum(r['status']==s for r in rows) for s in ['Proved','Refuted','Known','Open']}
for number in [178,180,181,182,183,184]:
    assert any(r['id']==f'A.{number}' and r['status']=='Proved' for r in rows)
bib_count = len(re.findall(r'(?m)^@\w+\{',(w/'SECTIONS_OVER_Q_references.bib').read_text()))
pages = len(fitz.open(w/'SECTIONS_OVER_Q_paper.pdf'))
typesetting = json.loads((w/'notes/typesetting_current.json').read_text())
assert typesetting['overfull_hboxes']==typesetting['overfull_vboxes']==0
assert not typesetting['undefined_references'] and not typesetting['undefined_citations']
render = json.loads((w/'qa/render_record.json').read_text())
review = json.loads((w/'qa/visual_review.json').read_text())
assert render['pdf_pages']==review['reviewed_build_pages']==pages
assert review['status'].startswith('Visually inspected')
assert set(review['contact_parts_reviewed'])==set(render['contact_parts'])
assert set(review['rendered_pages'])==set(render['rendered_pages'])
assert set(render['prior_overflow_pages'])<=set(review['full_resolution_pages_reviewed'])
corrections = json.loads((w/'notes/hour14_typesetting_corrections.json').read_text())
assert all(r['after_hbox_pt']==0 for r in corrections)
report_path = w/'SECTIONS_OVER_Q_report.md'
report = report_path.read_text()
assert report.startswith('INCOMPLETE\n')
outcomes = [line for line in report.splitlines()[:55]
            if re.match(r'^\| (?:[ABCD]\d+|L\d+) \|',line)]
expected = ({f'A{i}' for i in range(1,16)} | {f'B{i}' for i in range(1,4)}
            | {'C1','C2','D1','D2','D3','D5'} | {f'L{i}' for i in range(1,22)})
assert len(outcomes)==45
assert {line.split(' | ')[0][2:] for line in outcomes}==expected
body = (
    f'Exact mathematical programs and their executed outputs are retained under code/. '
    f'The current LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical boxes, '
    f'and no undefined references or citations. All {len(render["rendered_pages"])} pages '
    'in the current render record were visually inspected, including every active '
    'fourteenth-hour result A.178 and A.180–A.184, the intervening A.179 proof, the '
    'references, the updated A.166 frontier and a distributed sample across the earlier Parts. '
    'Full-resolution inspection locations are recorded. The first A.181/A.182 build had '
    'one overfull display, A.181.1, at 43.12856 pt; the field and unit data were split into '
    'two gathered lines. All additional build corrections and final zero-overflow diagnostics '
    'are recorded in notes/hour14_typesetting_corrections.json. Every corrected overflow '
    'page and the earlier A.160/A.179 overflow locations were inspected at full resolution. '
    'The A.183 first complete attempt stopped on an undefined shorthand for the class '
    'group; replacing it by the explicit operator resolved that source error. '
    'The mathematical audits retain the actual metabelian finite-support maps, the full '
    'integer divisor and unit-defect comparison, the evaluated nonzero norm/cohomology '
    'class, all 21 Jacobian cotangent maps, finite-field counts and rank witnesses, the '
    'first-weight cup sign and explicit T^14 detection, and the all-height secondary '
    'global-unit character. Root and independent peers read the complete proofs and '
    'reran their exact certificates. The report remains INCOMPLETE because both '
    'principal A1 assertions and the other explicitly recorded open scopes remain '
    'unresolved. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claimed.'
)
report = re.sub(r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)',
                lambda m:m.group(1)+body+'\n', report, flags=re.S)
progress = (
    'Continue. This hour evaluates a previously unevaluated continuous norm obstruction '
    'and identifies an explicit finite integral quotient that detects it, while advancing '
    'the section and positive-rank-cover routes. A.178 proves finite-support classification '
    'in the actual level-three abelian-cover quotient and in the full geometric metabelian '
    'quotient over every number field; its rational Abel–Jacobi fibre statement includes '
    'the exact full cusp parameter. A.180 identifies the actual infinite norm fibre through '
    'one stable integer profile, the full ordinary ideal classes and a norm-one-unit lim1 '
    'defect, and determines all completed profiles. A.181 constructs an explicit unit '
    'U^3 that is an actual field norm from every finite height but has no actual or '
    'completed infinite norm family. Its nonzero derived-limit class maps to the '
    'specified continuous one-variable metabelian obstruction, with all local and finite '
    'coefficient images zero. A.183 proves its first integral quotient D_A/T has zero '
    'image and its quotient D_A/T^14 has nonzero image: the least detecting index lies '
    'between 2 and 14. The nonzero finite-set coefficient test, integral inflation and '
    'zero absolute finite-coefficient tests are related by explicit maps. A.184 proves '
    'the relative-unit residue lemma at every height and constructs the secondary '
    'character whose kernel is exactly the two-step global-unit norm image, including '
    'completion. A.182 constructs all twelve rationally simple factors of the genus 21 '
    'pointed Fermat-eight Jacobian, proves each has positive rank, and rules out every '
    'nonconstant map over a number field to an abelian variety with finite points over '
    'that field via the actual Weil-restriction/Jacobian map. The total rank upper bound '
    'and least detecting norm weight are being attacked in separate retained notes. '
    'The actual infinite norm family over −2, the relevant full nonabelian lifts, the '
    'remaining ordinary infinite-support unit-equation tests and both principal A1 '
    'assertions remain unresolved. These are substantive advances on active open-item '
    'routes, so research continues after the checkpoint.'
)
heading = '## Fourteenth-hour progress review — 2026-11-16 '+stamp
if not re.search(r'^## Fourteenth-hour progress review',report,re.M):
    report += '\n'+heading+'\n\n'+progress+'\n'
report_path.write_text(report)
cp = w/'notes/checkpoints.md'
existing = cp.read_text()
record = (
    f'Fourteenth hourly snapshot: {pages}-page clean PDF; {len(rows)} registered statements '
    f'({counts["Proved"]} Proved, {counts["Refuted"]} Refuted, {counts["Known"]} Known, '
    f'{counts["Open"]} Open ); 45 outcome rows; {bib_count} bibliography entries with verification '
    f'notes. All {len(render["rendered_pages"])} rendered pages have actual visual review, '
    'including every corrected overflow page. Source, PDF, register, bibliography, report, '
    'every written program and output, all searches, proof audits, drafts and visual QA '
    'are included. Supplied background, runtime caches and all prior checkpoint ZIPs '
    'are excluded. The manifest checks every archived file against its actual bytes. '
    'Both A1 assertions remain open. The progress review directs continued research.'
)
if not re.search(r'^## Checkpoint14 ',existing,re.M):
    cp.write_text(existing+'\n## Checkpoint14 — 2026-11-16 '+stamp+'\n\n'+record+'\n')
with (w/'notes/root_progress.md').open('a') as f:
    f.write('\n'+stamp+' fourteenth-hour review: '+progress+'\n')
output = {'pdf_pages':pages,'statements':len(rows),'status_counts':counts,
          'outcome_rows':45,'bibliography_entries':bib_count,
          'rendered_pages':len(render['rendered_pages']),
          'typesetting':typesetting,'typesetting_corrections':corrections,
          'main_status':'INCOMPLETE; both A1 assertions open','hourly_decision':'continue',
          'norm_frontier':'Evaluated nonzero continuous norm obstruction; first weight zero, quotient T14 nonzero; actual infinite minus-two fibre unresolved',
          'fermat_frontier':'Complete positive-rank factor decomposition at level 8; rank upper bound and remaining section classification unresolved'}
out = json.dumps(output,indent=2)+'\n'
for p in [w/'code/finalize_hour14_output.txt',w/'code/checkpoint14_preflight_output.txt']:
    p.write_text(out)
print(out,end='')
