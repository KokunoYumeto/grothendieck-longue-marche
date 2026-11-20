#!/usr/bin/env python3
"""Apply the main reader's consistent category for absent catalogue targets.
Positive page identifications remain recorded. No TeX bytes change.
"""
import json
from review import W, D, now, rebuild

CHANGES = [
    ('6_scan042', 'L1319', True, 'The correction targets an external Hodge-Tate classification, which is absent from this page and its TeX: final decision d. The existing transcription correctly records the printed page 15, n°357 and the locally compact group/function-space text. Those are positive local findings. The broader spectral-theory attribution, reuse history, scan range and SA15-12 catalogue identity remain supplied identification.'),
    ('7_scan001', 'L740', True, 'The correction targets an external list of cover locations, which is absent from the TeX: final decision d. The page itself is positively identified as the IMAG cover and already represented by its figure. Main-reader cross-location check also directly identified scan 019 as the handwritten Tests décisifs page, so the cover location actually seen is cote 7, scan 001.'),
    ('8_scan001', 'L750', True, 'The correction targets an external document inventory, absent from the page TeX: final decision d. The local image is positively identified as the IMAG cover and already represented by its figure. The main reader has also directly inspected Tribu n°66 at cote 8, scan 019. Other inventory claims are not established by the cover image.'),
    ('8_scan003', 'L741', True, 'The correction targets an external attribution of this leaf to the manuscript author’s own notes, which is absent from its TeX: final decision d. The local typescript is positively identified by printed page 132 and §24, Explicit description of pseudo-rational double points; these are already transcribed. Lipman, Publ. IHES 36 (1969), is the supplied bibliographic identification, not independently authenticated by this image. The main reader has also directly inspected the cancelled mu_2-torsor and rigidity note at cote 8, scan 017; it is distinct from this typescript.'),
    ('8_scan017', 'L744', False, 'The correction targets an external topic/page list, absent from this page and its TeX: final decision d. Positively, the local handwritten note on indeterminacy, mu_2-torsors and enriched equivalences is cancelled with long diagonal strokes, and the existing outer deleted macro correctly records that state. Other listed page identifications and the proposed sequence are supplied catalogue information, not findings from this one page.'),
    ('8_scan025', 'L745', False, 'The correction targets an external Dieudonné-Manin topic description and page grouping, absent from this page and its TeX: final decision d. Positively, the underlined heading Groupes de Barsotti-Tate ordinaires and the category C data are already correctly represented in the transcription. The supplied global claim about cote 8, the proposed Lubin-Tate grouping and the descriptions of other leaves have not been independently verified from this sheet. Preserve all existing text and markup.'),
]

for page, statement, accepted, note in CHANGES:
    path = (D if accepted else W) / 'reviews' / (page + '.json')
    report = json.loads(path.read_text())
    row = next(r for r in report['rows'] if r['id'] == statement)
    if row.get('catalogue_category_reconciled'):
        continue
    assert row['decision'] == 'c' and not row['find'] and not row['replace']
    row['previous_decision'] = row['decision']
    row['previous_note'] = row['note']
    row['decision'] = 'd'
    row['note'] = note
    row['catalogue_category_reconciled'] = True
    row['main_adjudication'] = 'Category d describes the absent external correction target; positive agreement of local manuscript content is recorded separately. This replaces the initial category c without changing the transcription.'
    row.setdefault('events', []).append({
        'date': now(),
        'who': 'GPT-6 Astra Pro; effort not exposed; main reader; run IM02_6-9_20261120',
        'type': 'used and rechecked in this run',
        'outcome': f'Cote {row["cote"]}, scan {int(row["scan"]):03d}: reconciled category c to d after reviewing the actual correction target. ' + row['main_adjudication'],
    })
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')

path = W / 'reviews/8_scan004.json'
report = json.loads(path.read_text())
if report.get('open_questions'):
    report['reader_open_questions'] = report['open_questions']
    report['open_questions'] = []
    report['main_adjudication'] = 'L1366 is decided d: the date/cover locus is absent. An alternate location not found in supplied evidence does not leave this page decision open.'
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')

print(rebuild())
with (D / 'progress.log').open('a') as f:
    f.write('catalogue-target classifications reconciled ' + now() + '; no TeX bytes changed\n')
