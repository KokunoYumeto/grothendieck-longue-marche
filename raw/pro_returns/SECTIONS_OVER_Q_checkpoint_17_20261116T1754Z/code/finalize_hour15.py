#!/usr/bin/env python3
"""Finalize checkpoint15 only after exact registration and actual final-PDF review."""
from pathlib import Path
import csv, datetime, hashlib, json, re
import fitz

w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
rows=list(csv.DictReader((w/'SECTIONS_OVER_Q_results.csv').open()))
counts={s:sum(r['status']==s for r in rows) for s in ['Proved','Refuted','Known','Open']}
ids={r['id'] for r in rows}
for number in range(185,192):
    assert any(r['id']==f'A.{number}' and r['status']=='Proved' for r in rows)
bib_count=len(re.findall(r'(?m)^@\w+\{',(w/'SECTIONS_OVER_Q_references.bib').read_text()))
pdf=w/'SECTIONS_OVER_Q_paper.pdf'
pages=len(fitz.open(pdf));pdf_sha=hashlib.sha256(pdf.read_bytes()).hexdigest()
typesetting=json.loads((w/'notes/typesetting_current.json').read_text())
assert typesetting['overfull_hboxes']==typesetting['overfull_vboxes']==0
assert not typesetting['undefined_references'] and not typesetting['undefined_citations']
render=json.loads((w/'qa/hour15/render_record.json').read_text())
review=json.loads((w/'qa/hour15/visual_review.json').read_text())
assert render['pdf_pages']==review['reviewed_build_pages']==pages
assert render['pdf_sha256']==review['pdf_sha256']==pdf_sha
assert review['status'].startswith('Visually inspected')
assert set(review['contact_parts_reviewed'])==set(render['contact_parts'])
assert set(review['rendered_pages'])==set(render['rendered_pages'])
assert set(render['required_full_resolution_pages'])<=set(review['full_resolution_pages_reviewed'])
corrections=json.loads((w/'notes/hour15_typesetting_corrections.json').read_text())
assert all(r['after_hbox_pt']==0 for r in corrections)
report_path=w/'SECTIONS_OVER_Q_report.md'
report=report_path.read_text()
assert report.startswith('INCOMPLETE\n')
outcomes=[line for line in report.splitlines()[:55]
          if re.match(r'^\| (?:[ABCD]\d+|L\d+) \|',line)]
expected=({f'A{i}' for i in range(1,16)}|{f'B{i}' for i in range(1,4)}|
          {'C1','C2','D1','D2','D3','D5'}|{f'L{i}' for i in range(1,22)})
assert len(outcomes)==45
assert {line.split(' | ')[0][2:] for line in outcomes}==expected
extra=(' A.192 additionally determines the full dyadic genus-two intersection and transfers it through its literal cyclic-eight cover, with its complete proof and audit retained.'
       if 'A.192' in ids else '')
body=(
    f'Exact mathematical programs and executed outputs are retained under code/. '
    f'The current LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical '
    f'boxes, and no undefined references or citations. All {len(render["rendered_pages"])} '
    'pages in the final render record were actually inspected, covering every active '
    'fifteenth-hour proof, the references, the corrected overflow and a distributed '
    'sample of the earlier Parts. The final PDF hash is bound to that review. '
    'The first A.189/A.190 build had one overfull statement line of30.042pt on page566; '
    'moving the completed Mordell–Weil identity into its own display resolved it. '
    'The nine-unit natural-basis table uses explicit column spacing. Every corrected '
    'overflow and the retained earlier overflow locations were inspected at full '
    'resolution. All before/after counts and locations are recorded in '
    'notes/hour15_typesetting_corrections.json. '
    'The mathematical audits include the exact six elliptic isogeny images, six complete '
    'genus-two descents and their literal completed generators, all Prym/Selmer maps, '
    'the integral multiplier16 reverse map, the full relevant dyadic Chabauty intersection, '
    'the rank-two quadratic-field regulator with infinite-tail bounds, and the actual '
    'ninth-root localized class norm quotient. Complete source audits and independent '
    'certificate reruns are retained. The exploratory nested PARI reads and invalid '
    'ideal-reduction attempts are recorded with their precise corrections and without '
    'arithmetic consequences.'+extra+' The report remains INCOMPLETE because both '
    'principal A1 assertions and the other recorded open scopes remain unresolved. '
    'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority is claimed.'
)
report=re.sub(r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)',
              lambda m:m.group(1)+body+'\n',report,flags=re.S)
progress=(
    'Continue. The positive-rank route now has an exact arithmetic local intersection '
    'and its actual global compact two-adic class. A.185 computes the three rational '
    'elliptic ranks and the quadratic Prym ranks1,2,2. A.186 proves rank1, torsionC2, '
    'a two-dimensional2-Selmer group and zero2-primary Sha for each of the six genus-two '
    'factors, and supplies their exact completed generators by twelve displayed square '
    'witnesses. The genus21 Jacobian has exact rank14. A.187 proves the full continuous '
    'two-adic Selmer image is its completed Mordell–Weil group. A.188 gives the literal '
    'reverse map with both composites[16], so32 kills its two-primary Sha and a '
    'five-level finite Selmer transition has exactly the rational Kummer image. '
    'A.189 proves the complete relevant dyadic genus-two locus and determines '
    'C8(Q)={(±1,±1)}. In the specified finite Kummer class, each locally matching '
    'full metabelian section has dyadic centre3. A.190 proves localization injective '
    'on all twelve completed factor groups and on the full Jacobian, using an exact '
    'quadratic-field regulator and the actual reverse isogenies. Its continuous '
    'two-adic Selmer/curve intersection consists exactly of the four rational point '
    'pairs, including their global coefficient classes. '+extra+
    ' The norm route also advances: A.191 proves a fully saturated ninth-root base '
    'unit calculation and identifies the actual ordinary and localized root '
    'coinvariants with C3³ through the cyclotomic ideal norm. The least detecting '
    'weight and the next secondary-unit values still require the retained global '
    'augmentation comparison; the local Bockstein and lower-field cube-root data '
    'are recorded without asserting that missing value. The full section equality, '
    'birational lifting and actual infinite minus-two norm family remain open. '
    'These active routes have made concrete progress, so research continues after '
    'the checkpoint; bounded discovery failures are not promoted to conclusions.'
)
heading='## Fifteenth-hour progress review — 2026-11-16 '+stamp
if not re.search(r'^## Fifteenth-hour progress review',report,re.M):
    report+='\n'+heading+'\n\n'+progress+'\n'
report_path.write_text(report)
cp=w/'notes/checkpoints.md';old=cp.read_text()
record=(f'Fifteenth hourly snapshot: {pages}-page clean PDF; {len(rows)} registered '
        f'statements ({counts["Proved"]} Proved, {counts["Refuted"]} Refuted, '
        f'{counts["Known"]} Known, {counts["Open"]} Open);45 outcome rows; '
        f'{bib_count} bibliography entries with verification notes. '
        f'All {len(render["rendered_pages"])} rendered pages were actually inspected, '
        'including the repaired overflow and retained earlier overflow locations. '
        'Source, PDF, register, references, report, all programs and outputs, searches, '
        'proof audits, drafts and visual QA are included. Supplied background, runtime '
        'caches and all prior ZIPs are excluded. Both principal A1 assertions remain '
        'open. The progress review directs continued work.')
if not re.search(r'^## Checkpoint15 ',old,re.M):
    cp.write_text(old+'\n## Checkpoint15 — 2026-11-16 '+stamp+'\n\n'+record+'\n')
with (w/'notes/root_progress.md').open('a') as f:
    f.write('\n'+stamp+' fifteenth-hour review: '+progress+'\n')
output={'pdf_pages':pages,'pdf_sha256':pdf_sha,'statements':len(rows),'status_counts':counts,
        'outcome_rows':45,'bibliography_entries':bib_count,
        'rendered_pages':len(render['rendered_pages']),'typesetting':typesetting,
        'typesetting_corrections':corrections,'main_status':'INCOMPLETE; both A1 assertions open',
        'hourly_decision':'continue','active_results':[f'A.{i}' for i in range(185,193) if f'A.{i}' in ids]}
out=json.dumps(output,indent=2)+'\n'
for p in [w/'code/finalize_hour15_output.txt',w/'code/checkpoint15_preflight_output.txt']:
    p.write_text(out)
print(out,end='')
