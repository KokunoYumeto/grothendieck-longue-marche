"""Finish documented metadata repairs and adopt the audited notation synthesis.

This is a one-time metadata operation, not an image reading or a page edit.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json

W = Path(__file__).resolve().parents[1]
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
history_path = W / 'audit/final_synthesis_repairs.json'
assert not history_path.exists()
history = {'utc': stamp, 'scope': 'Metadata only; no final page or original reading altered.', 'repairs': []}

def note(report, ident, transform):
    for i, old in enumerate(report['notes']):
        if old.startswith(ident + ':') or old.startswith(ident + '.'):
            new = transform(old)
            assert new != old, ident
            report['notes'][i] = new
            history['repairs'].append({'page': report['page'], 'target': ident, 'old': old, 'final': new})
            return
    raise AssertionError(ident)

for page in ['151_scan059', '151_scan060']:
    path = W / 'reports' / (page + '.json')
    r = json.loads(path.read_text())
    if page.endswith('059'):
        note(r, 'scan059.N2', lambda _: 'scan059.N2: The top indexed expression has a scripted V whose possible internal dot remains uncertain, a three-stroke approxeq, and an N with preferred check but an explicit tilde alternative, followed by restriction to D_{d_*}^*. Every d prime/star and the two subscript zeros were inspected together with the whole formula. The source reference p. 84 is retained without consulting that referenced page. See N13 for the final blind adjudication of the V and N alternatives.')
        note(r, 'scan059.N11', lambda s: s.replace('The whole page and both native halves', 'During the first reading, the whole page and both native halves').replace('No OCR, research, other-page image/report or TeX compilation was used.', 'The isolated first reader used no other-page image or report. No OCR, external research or TeX compilation was used at any stage. The later main-reader comparison with scan058 is documented in N13.'))
    else:
        note(r, 'scan060.N6', lambda s: s.replace('The parent will perform any cross-page check.', 'The completed main-reader endpoint check, with its qualifications, is recorded in scan060.N16.'))
        for h in r['hand']:
            if h['habit'] == 'Stops in abbreviations must be checked locally':
                old = copy.deepcopy(h)
                h['evidence'] = "The NB has a detached stop after its short form, now retained as succ./success.; loc. also has its stop. ps- has no dot before its hyphen, and l'ens has no final stop. These local forms are not normalized into a common style."
                h['misread_places'] = "Both witnesses add the dot in ps.- and the point in l'ens.; H expands the NB short form to est un successeur."
                history['repairs'].append({'page': page, 'target': 'hand/stops', 'old': old, 'final': h})
        row = next(x for x in r['changes'] if x['id'] == 'r04')
        old = {k: row[k] for k in ['c', 'h', 'final']}
        row.update(c='no exclamation mark', h='!', final='no exclamation mark')
        history['repairs'].append({'page': page, 'target': 'r04 comparison span', 'old': old, 'final': {k: row[k] for k in old}, 'counts_changed': False})
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')

old_notation = W / 'audit/notation_before_final_synthesis.md'
assert not old_notation.exists()
old_notation.write_bytes((W / 'notation.md').read_bytes())
candidate = (W / 'audit/notation_final_candidate.md').read_text()
final = candidate.replace('# Final notation table — candidate', '## Final notation table', 1)
final = final.replace('This candidate was synthesized', 'This table was synthesized')
final = final.replace('This file is a **candidate replacement** for `notation.md`. It changes neither that file nor any final page, original reading TSV, box list or comparison.', 'The main reader adopted this synthesis after checking its local qualifications against the completed adjudication records. This final consolidation changes no page reading, original reading TSV, box list or token comparison.')
final = final.replace('## Reading and encoding policy', '### Reading and encoding policy').replace('## Final review account', '### Final review account')
(W / 'notation.md').write_text(final)
history['notation'] = {'candidate': 'audit/notation_final_candidate.md', 'prior_table': str(old_notation.relative_to(W)), 'adopted_utc': stamp, 'final_sha256': hashlib.sha256(final.encode()).hexdigest(), 'new_image_claims': False}

# Preserve the earlier locator inventory unchanged and state its limited scope.
(W / 'audit/notation_inventory_scope.json').write_text(json.dumps({
    'utc': stamp,
    'historical_file': 'audit/notation_occurrence_inventory.json',
    'scope': 'Historical mechanical locator output created before the final blind adjudications; broad regex matches are search aids, not semantic classification or evidence that every match is doubtful.',
    'authoritative_final_synthesis': 'notation.md',
    'final_occurrence_readings': 'pages/151_scanNNN.tex',
    'evidence': 'reports/151_scanNNN.json and audit/151_scanNNN_adjudication.json',
    'old_inventory_preserved': True
}, ensure_ascii=False, indent=2) + '\n')

# Extend the cross-page record with decisions already made on the saved crops.
consistency = W / 'audit/construction_noun_consistency.json'
records = json.loads(consistency.read_text())
for page, boxes, final_reading in [('151_scan059', ['b04'], 'pierres at all three recorded occurrences'), ('151_scan061', ['b06'], 'pierres')]:
    decisions = json.loads((W / 'audit' / (page + '_adjudication.json')).read_text())
    records.append({'page': page, 'final': final_reading, 'scope': 'Final synthesis of the previously completed blind adjudication; no new image inspection.', 'adjudication_file': 'audit/' + page + '_adjudication.json', 'recorded_decisions': {b: decisions[b] for b in boxes if b in decisions}, 'utc': stamp})
consistency.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')

state = json.loads((W / 'run_state.json').read_text())
reports = [json.loads((W / 'reports' / (p + '.json')).read_text()) for p in state['order']]
totals = {k: sum(r['counts'][k] for r in reports) for k in ['audit_boxes', 'audit_token_differences', 'audit_changed_boxes', 'remaining_doubt_records', 'disagreement_places', 'differences_from_c', 'differences_from_h']}
totals.update(pages=len(reports), supplied_marks=sum(len(r['decisions']) for r in reports), inventory_elements=sum(len(r['inventory']) for r in reports), mathematical_check_events=sum(len(r.get('checks', [])) for r in reports))
(W / 'audit/final_run_totals.json').write_text(json.dumps({'utc': stamp, 'counts': totals, 'count_scope': 'Differences are distinct recorded physical places; overlaps between C and H are counted once in the union. Blind differences and changed totals are boxes, not tokens or additional C/H places.'}, indent=2) + '\n')

with (W / 'legibility_note.md').open('a') as f:
    f.write('\nAll 24 pages completed the independent second reading: 382 boxes, 302 differing box readings, and 85 boxes whose final text or uncertainty qualification changed. These box counts are not extra witness-comparison places. The final table retains 206 doubt records, including local punctuation, overwritten words and formula alternatives. A record can cover more than one occurrence or uncertainty; this is not a count of unreadable words.\n')

with (W / 'README.md').open('a') as f:
    f.write('\n## Completed scope and verification\n\nAll 24 pages have completed the first collation, main-reader adjudication, independent blind reading by a different reader, and main-reader decision on every recorded difference. The final records contain 851 substantive comparison places (244 against C and 717 against H, with overlap), 82 supplied-mark decisions, 410 inventoried elements, 382 blind boxes and 83 mathematical check events. The doubts file contains 206 remaining doubt records.\n\nThe original first and second readings and neutral box lists remain preserved; later decisions are recorded separately. Historical drafts, count snapshots, metadata-review findings and notation inventories document earlier stages and are explicitly distinguished from final records. The final notation table is at the start of the doubts file.\n\nValidation checks file completeness, source order, mark order, record totals, crop paths and boxes, reader separation, original reading integrity, and LaTeX fragment structure. No TeX compilation was performed, as requested. The SHA-256 freeze manifest is `audit/frozen_transcription_sha256.json`; final verification is recorded in `progress.log`.\n')

history_path.write_text(json.dumps(history, ensure_ascii=False, indent=2) + '\n')
with (W / 'progress.log').open('a') as f:
    f.write('final record synthesis ' + stamp + ': notation table adopted; final known metadata findings reconciled; historical inventory scope labelled; no final page or original reading changed\n')
print(json.dumps(totals, indent=2))
