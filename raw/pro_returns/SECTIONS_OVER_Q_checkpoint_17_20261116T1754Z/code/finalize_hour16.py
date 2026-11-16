#!/usr/bin/env python3
"""Finalize checkpoint16 after registration and actual final-build image review."""
from pathlib import Path
import csv, datetime, hashlib, json, re
import fitz

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
rows=list(csv.DictReader((w/'SECTIONS_OVER_Q_results.csv').open()))
counts={s:sum(r['status']==s for r in rows) for s in ['Proved','Refuted','Known','Open']}
for n in range(193,205):
    assert any(r['id']==f'A.{n}' and r['status']=='Proved' for r in rows)
assert len(rows)==238 and counts==dict(Proved=220,Refuted=13,Known=1,Open=4)
bib_count=len(re.findall(r'(?m)^@\w+\{',(w/'SECTIONS_OVER_Q_references.bib').read_text()))
pdf=w/'SECTIONS_OVER_Q_paper.pdf'
pages=len(fitz.open(pdf));pdf_sha=hashlib.sha256(pdf.read_bytes()).hexdigest()
typesetting=json.loads((w/'notes/typesetting_current.json').read_text())
assert typesetting['overfull_hboxes']==typesetting['overfull_vboxes']==0
assert not typesetting['undefined_references'] and not typesetting['undefined_citations']
render=json.loads((w/'qa/hour16/render_record.json').read_text())
review=json.loads((w/'qa/hour16/visual_review.json').read_text())
assert render['pdf_pages']==review['reviewed_build_pages']==pages
assert render['pdf_sha256']==review['pdf_sha256']==pdf_sha
assert review['status'].startswith('Visually inspected')
assert set(review['contact_parts_reviewed'])==set(render['contact_parts'])
assert set(review['rendered_pages'])==set(render['rendered_pages'])
assert set(render['required_full_resolution_pages'])<=set(review['full_resolution_pages_reviewed'])
corrections=json.loads((w/'notes/hour16_typesetting_corrections.json').read_text())
assert all(r['after_hbox_pt']==0 and r['final_page'] for r in corrections)
report_path=w/'SECTIONS_OVER_Q_report.md';report=report_path.read_text()
assert report.startswith('INCOMPLETE\n')
outcomes=[line for line in report.splitlines()[:55] if re.match(r'^\| (?:[ABCD]\d+|L\d+) \|',line)]
expected=({f'A{i}' for i in range(1,16)}|{f'B{i}' for i in range(1,4)}|
          {'C1','C2','D1','D2','D3','D5'}|{f'L{i}' for i in range(1,22)})
assert len(outcomes)==45 and {line.split(' | ')[0][2:] for line in outcomes}==expected
body=(
 f'Exact mathematical programs and executed outputs are retained under code/. The current '
 f'LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical boxes, and no '
 f'undefined references or citations. All {len(render["rendered_pages"])} rendered pages '
 f'were visually inspected through {len(render["contact_parts"])} contact sheets; '
 f'{len(render["required_full_resolution_pages"])} designated pages were also inspected '
 'individually at full resolution. The review is bound to the final PDF hash. The '
 'sixteenth-hour builds exposed two horizontal overflows:1.20303pt in the A194 certificate '
 'paragraph on the then-page583, and27.69026pt in the A196 field/frame display on the '
 'then-page586. Shortening the certificate introduction and splitting the field/frame '
 'display into two gathered lines resolved them. The image review additionally found two '
 'contents titles touching their page numbers; shorter optional contents labels resolved '
 'them, with unchanged body headings and pagination. The two final repaired contents pages '
 'were inspected again, and an executed pixel-image hash comparison proves every other '
 'reviewed image unchanged. Both final overflow locations, every recorded '
 'historical overflow above2pt, the full front matter, every A193–A204 proof page, the '
 'references, and a distributed sample of earlier Parts were inspected. Exact before/after '
 'counts and live anchor locations are retained in notes/hour16_typesetting_corrections.json '
 'and notes/hour16_render_anchor_map.md. The mathematical audits cover the complete finite '
 'dyadic Selmer loci, the generalized-Jacobian torus maps and finite detector, both complete '
 'ninth-root unit orbits and their norm matrices, the least integral obstruction weight, '
 'the whole completed unit-line lifting image, the arbitrary fixed-quotient ghost construction, '
 'and the actual class-three/class-four lifting theorems with their strict continuous '
 'residue primitives. Full saved-source audits, independent executed certificates, precise '
 'primary-source readings, and failed exploratory attempts are retained. All statements '
 'throughA204 are active in the paper and register; later research notes remain work in '
 'progress. Both principal A1 assertions remain open, and the report remains INCOMPLETE. '
 'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority is claimed.'
)
pattern=r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)'
report,n=re.subn(pattern,lambda m:m.group(1)+body+'\n',report,flags=re.S)
assert n==1
progress=(
 'Continue. The active quotient-lifting and arithmetic norm routes have made concrete '
 'progress. A193 gives every finite dyadic Selmer locus and its actual finite metabelian '
 'detector. A198 identifies the residual torus through the degree16 generalized-Jacobian '
 'isogeny, constructs an exact norm-one family with point-three image at2, and proves '
 'its later point/cusp failure at571. A202 retains every prescribed finite quotient in '
 'the ordinary infinite-support construction and computes an exact later detector from '
 'the dyadic separation depth. A194, A197 and A199 complete the ninth-root unit module: '
 'the subfield-unit quotient is exactlyC3^6. A203 computes the two actual unit norm '
 'quotients, their field-norm support kernels, and the literal relative-unit character eta. '
 'Its comparison with the secondary obstruction map still needs the exact fractional-divisor '
 'gluing argument. A195 proves that the explicit continuous norm obstruction has least '
 'integral weight2. A196 gives the actual class-three quotient with all finite and all '
 'local lifts but no global continuous lift, and proves its local frame at3 has no ordinary '
 'or cusp image. A200 evaluates the whole completed exponent line: the three specified '
 'finite/local/class-two images are3Z3, whereas the global continuous class-three image '
 'is9Z3. A201 proves a global continuous class-three lift for every finite-locally matching '
 'class-two section overQ. A204 proves the actual next-layer obstruction lies in the '
 'unramified image in every weight, including its derived-limit contribution; at weight4, '
 'the real comparison and K6(Z)=0 give a global full profinite class-four lift. The next '
 'step is the actual global H1 localization and local correction problem, with geometric '
 'stabilizers and cusp choices retained. No local matching of those new global lifts is '
 'inferred. The full section equality, birational lifting, and the recorded unresolved '
 'scopes remain open. Research continues on these concrete comparisons; peripheral '
 'discovery work is not substituted for them.'
)
heading='## Sixteenth-hour progress review — 2026-11-16 '+stamp
assert not re.search(r'^## Sixteenth-hour progress review',report,re.M)
report+='\n'+heading+'\n\n'+progress+'\n';report_path.write_text(report)
cp=w/'notes/checkpoints.md';old=cp.read_text()
assert not re.search(r'^## Checkpoint16 ',old,re.M)
record=(f'Sixteenth hourly snapshot: {pages}-page clean PDF; {len(rows)} registered statements '
        f'({counts["Proved"]} Proved, {counts["Refuted"]} Refuted, {counts["Known"]} Known, '
        f'{counts["Open"]} Open);45 outcome rows; {bib_count} verified bibliography entries. '
        f'All {len(render["rendered_pages"])} rendered pages and all '
        f'{len(render["required_full_resolution_pages"])} required full-resolution locations '
        'were actually inspected. Source, PDF, register, references, report, every program '
        'and output, searches, proof audits, drafts and visual QA are retained. Supplied '
        'background, runtime caches and all earlier ZIPs are excluded. Both principal '
        'A1 assertions remain open. The hourly review directs continued work.')
cp.write_text(old+'\n## Checkpoint16 — 2026-11-16 '+stamp+'\n\n'+record+'\n')
with (w/'notes/root_progress.md').open('a') as f:f.write('\n'+stamp+' sixteenth-hour review: '+progress+'\n')
output=dict(pdf_pages=pages,pdf_sha256=pdf_sha,statements=len(rows),status_counts=counts,
            outcome_rows=45,bibliography_entries=bib_count,rendered_pages=len(render['rendered_pages']),
            full_resolution_pages=len(render['required_full_resolution_pages']),typesetting=typesetting,
            typesetting_corrections=corrections,main_status='INCOMPLETE; both A1 assertions open',
            hourly_decision='continue',active_results=[f'A.{i}' for i in range(193,205)])
out=json.dumps(output,indent=2)+'\n'
for p in [w/'code/finalize_hour16_output.txt',w/'code/checkpoint16_preflight_output.txt']:p.write_text(out)
print(out,end='')
