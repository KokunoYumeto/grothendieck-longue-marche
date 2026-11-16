#!/usr/bin/env python3
"""Finalize checkpoint17 only after the final PDF and actual image reviews agree."""
from pathlib import Path
import csv
import datetime
import hashlib
import json
import re
import fitz

w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
rows = list(csv.DictReader((w/'SECTIONS_OVER_Q_results.csv').open()))
counts = {s: sum(r['status'] == s for r in rows) for s in ['Proved','Refuted','Known','Open']}
active = sorted(int(r['id'][2:]) for r in rows if r['id'].startswith('A.') and int(r['id'][2:]) >= 205)
assert active == list(range(205,max(active)+1)) and max(active) >= 210
assert all(r['status']=='Proved' for r in rows if r['id'] in {f'A.{n}' for n in active})
assert len(rows) == 238+len(active)
assert counts == dict(Proved=220+len(active),Refuted=13,Known=1,Open=4)
bib_count = len(re.findall(r'(?m)^@\w+\{',(w/'SECTIONS_OVER_Q_references.bib').read_text()))
assert bib_count >= 107
pdf = w/'SECTIONS_OVER_Q_paper.pdf'
pages = len(fitz.open(pdf))
pdf_sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
typesetting = json.loads((w/'notes/typesetting_current.json').read_text())
assert typesetting['overfull_hboxes'] == typesetting['overfull_vboxes'] == 0
assert not typesetting['undefined_references'] and not typesetting['undefined_citations']
render = json.loads((w/'qa/hour17/render_record.json').read_text())
review = json.loads((w/'qa/hour17/visual_review.json').read_text())
assert render['pdf_pages'] == review['reviewed_build_pages'] == pages
assert render['pdf_sha256'] == review['pdf_sha256'] == pdf_sha
assert set(map(int,render['new_statement_pages'])) == set(active)
assert review['status'].startswith('Visually inspected')
assert set(review['contact_parts_reviewed']) == set(render['contact_parts'])
assert set(review['rendered_pages']) == set(render['rendered_pages'])
assert set(render['required_full_resolution_pages']) <= set(review['full_resolution_pages_reviewed'])
corrections = json.loads((w/'notes/hour17_typesetting_corrections.json').read_text())
assert all(r['after_hbox_pt']==0 and r.get('final_page') for r in corrections)
report_path = w/'SECTIONS_OVER_Q_report.md'
report = report_path.read_text()
assert report.startswith('INCOMPLETE\n')
outcomes = [line for line in report.splitlines()[:55] if re.match(r'^\| (?:[ABCD]\d+|L\d+) \|',line)]
expected = ({f'A{i}' for i in range(1,16)} | {f'B{i}' for i in range(1,4)} |
            {'C1','C2','D1','D2','D3','D5'} | {f'L{i}' for i in range(1,22)})
assert len(outcomes)==45 and {line.split(' | ')[0][2:] for line in outcomes}==expected

if corrections:
    correction_text = (f'This hour recorded {len(corrections)} repaired horizontal overflows; '
                       f'the largest was {max(r["before_hbox_pt"] for r in corrections)}pt. '
                       'Every repaired location is anchor-resolved in the final PDF and was opened at full resolution. ')
else:
    correction_text = 'The seventeenth-hour final builds have zero horizontal and vertical overflows; no new overflow repair was required. '
body = (
    f'Exact mathematical programs and executed outputs are retained under code/. The current '
    f'LuaLaTeX PDF has {pages} pages, zero overfull horizontal or vertical boxes, and no '
    f'undefined references or citations. All {len(render["rendered_pages"])} rendered pages '
    f'were visually inspected through {len(render["contact_parts"])} contact sheets. '
    f'All {len(render["required_full_resolution_pages"])} designated full-resolution pages '
    'were also actually opened and inspected, including every new proof page, every '
    'recorded historical overflow location, and the complete front matter. The review '
    'is bound to the final PDF hash. ' + correction_text +
    'The bibliography reconciliation preserves all 106 previous entries and their expanded '
    'verification notes, retains the richer existing local reciprocity note, and adds '
    'the opened Darmon class-number formula. Its canonical source fragments now rebuild '
    'the complete bibliography without dropping later parent-only additions. '
    'The mathematical audits cover the actual compact central correction torsor, the '
    'full fourth-weight cohomology and local CRT map, the complete ninth-root class '
    'group and capitulation, the secondary unit-support class map and ordinary divisor '
    'principalization, the complete quadratic norm Selmer group, and the explicit '
    'same-pair dihedral local obstruction with its entire C16 correction coset. '
    f'All statements through A.{max(active)} are active in the paper and register. '
    'Full saved-source audits, executed independent certificates, primary-source '
    'readings, retained exploratory attempts and current unintegrated research notes '
    'are included. Both principal A1 assertions remain open. AI-produced by GPT-6 Astra '
    '(OpenAI, ChatGPT Pro mode); no priority is claimed.'
)
pattern = r'(## Computations and typesetting\n\n).*?(?=\n## Fourth-hour progress review)'
report,n = re.subn(pattern,lambda m:m.group(1)+body+'\n',report,flags=re.S)
assert n==1
progress = (
    'Continue. The active quotient-matching and arithmetic norm routes have made concrete '
    'progress on the recorded open items. A205 constructs the complete actual central '
    'correction fibre, including its real geometric stabilizer action and compact local '
    'conditions. The fourth-weight global correction group is exactly C240 in each of '
    'three Hall coordinates, with explicit localization and finite witnesses for failure. '
    'A207 constructs one ordinary infinite-support completed pair with a continuous '
    'global class-four lift and a prescribed ordinary residue at 1129. A209 computes '
    'the entire quadratic norm Selmer group of the smaller coefficient module and '
    'excludes every local sheet in the actual order 32, class 2 quotient. A210 then '
    'evaluates the mismatch at 1129 alone for every global class-two lift of that same '
    'pair. The exact integral tame relation confines the dihedral difference to the '
    'eight quadratic characters supported at 2, 3, all split at 1129. The rational degree 8 '
    'cover has trivial point-three Frobenius and central-involution Frobenius at the '
    'prescribed residue. The full local central differences are exactly the eight '
    'odd classes of C16, each three times among the 24 global lifts, and the global '
    'correction map is exactly k to 6k. This proves the first continuous nilpotent '
    'local-matching failure for this specific ordinary pair occurs at class 2, while '
    'its global class-four lift remains proved. The norm route also advances: A206 '
    'computes the full ordinary three-class group C3^4, the exact norm kernel, full '
    'cyclotomic capitulation and localized norm isomorphism. A208 identifies the '
    'actual unit-support quotient with the minus ideal-class group, principalizes '
    'the entire cyclic-nine Hilbert–90 divisor, evaluates the secondary character '
    'as twice the two changed-prime valuations, and computes the complete next '
    'unit norm-character matrix of rank 3. Its final unit alignment remains explicit. '
)
if 211 in active:
    progress += (
        'A211 further normalizes the actual cyclotomic Hilbert–90 factor into the base '
        'field, constructs the associated capitulating lower ideal class, and determines '
        'the full necessary invariant anti-unit cubeclass space by the certified unit '
        'action and norm maps. The remaining unit norm equation still has to select '
        'its evaluated coordinates; equality of the two secondary maps is not inferred. '
    )
progress += (
    'The full section classification, birational lifting and the other recorded '
    'unresolved scopes remain open. These exact local correction and divisor maps '
    'move the active open items forward; research continues on their remaining '
    'comparison, with peripheral work stopped.'
)
assert not re.search(r'^## Seventeenth-hour progress review',report,re.M)
report += '\n## Seventeenth-hour progress review — 2026-11-16 '+stamp+'\n\n'+progress+'\n'
report_path.write_text(report)
cp=w/'notes/checkpoints.md'
old=cp.read_text()
assert not re.search(r'^## Checkpoint17 ',old,re.M)
record = (
    f'Seventeenth hourly snapshot: {pages}-page clean PDF; {len(rows)} registered '
    f'statements ({counts["Proved"]} Proved, 13 Refuted, 1 Known, 4 Open); 45 outcome '
    f'rows; {bib_count} bibliography entries with verification notes. All '
    f'{len(render["rendered_pages"])} rendered pages and all '
    f'{len(render["required_full_resolution_pages"])} required full-resolution pages '
    'were actually inspected. Source, PDF, register, bibliography, report, every '
    'research program and output, notes, searches, proof audits, drafts and visual QA '
    'are retained. Supplied background, runtime caches and every earlier ZIP are '
    'excluded. Both principal A1 assertions remain open. The hourly review directs '
    'continued work on the active exact comparisons.'
)
cp.write_text(old+'\n## Checkpoint17 — 2026-11-16 '+stamp+'\n\n'+record+'\n')
with (w/'notes/root_progress.md').open('a') as f:
    f.write('\n'+stamp+' seventeenth-hour review: '+progress+'\n')
output = dict(pdf_pages=pages,pdf_sha256=pdf_sha,statements=len(rows),status_counts=counts,
              outcome_rows=45,bibliography_entries=bib_count,
              rendered_pages=len(render['rendered_pages']),
              full_resolution_pages=len(render['required_full_resolution_pages']),
              typesetting=typesetting,typesetting_corrections=corrections,
              main_status='INCOMPLETE; both A1 assertions open',hourly_decision='continue',
              active_results=[f'A.{n}' for n in active])
out=json.dumps(output,indent=2)+'\n'
for p in [w/'code/finalize_hour17_output.txt',w/'code/checkpoint17_preflight_output.txt']:
    p.write_text(out)
print(out,end='')
