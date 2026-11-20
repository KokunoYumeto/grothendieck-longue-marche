"""Main-reader decisions after direct inspection of scan088's audit evidence."""
import json
import subprocess
import sys
from audit_support import load, replace_exact, commit, OUT

r, a, s = load(88)
adjudications = []
for i, change in enumerate(a['changes'], 1):
    s = replace_exact(s, change['before'], change['after'])
    row = {
        'id': f'088-A{i:02}', 'place': change['place'],
        'c': change['c'], 'h': change['h'], 'final': change['reading'],
        'c_changed': True, 'h_changed': True,
        'category': 'Omissions' if i == 6 else 'Words',
        'kind': 'omission' if i == 6 else 'misread word',
        'marked_in_H': False, 'confidence': change['confidence'],
        'scan_shows': change['scan_shows'], 'box': change['box'],
        'crop': change['crop'], 'consequential': False,
        'math_note': 'Local spelling or punctuation only; no mathematical assertion is changed.'
    }
    r['changes'].append(row)
    adjudications.append({
        'id': change['id'], 'decision': 'accepted', 'reading': change['reading'],
        'evidence': change['scan_shows'], 'crop': change['crop'],
        'confidence': change['confidence']
    })

for proposal, identifier, alternatives in [
    ('A088-04', 'D088-audit-first-connait', ['connaît']),
    ('A088-06', 'D088-audit-low-point-pair', ['incidental pair of pen-points; no punctuation'])
]:
    item = next(x for x in a['confirmed_doubts'] if x['id'] == proposal)
    r['doubts'].append({'scan': 88, 'place': item['place'],
        'reading': item['reading'], 'alternatives': alternatives,
        'confidence': item['confidence'], 'reason': item['evidence']})
    r['decisions'].append({'id': identifier, 'cote': '142', 'scan': 88,
        'decision': 'undecided', 'reading': item['reading'],
        'what_the_ink_shows': item['evidence'], 'crop': item['crop'],
        'confidence': item['confidence']})

for item in r['inventory']:
    item['position'] = item['position'].replace('sous-groupoïde', 'sous-groupoide')
new_element = dict(a['new_inventory'][0])
new_element['transcribed'] = 'yes'
insertion_index = next(i for i,x in enumerate(r['inventory']) if x['element'] == 'cancelled closing clause')
r['inventory'].insert(insertion_index, new_element)

for item, errors in zip(a['hand_log_additions'], [
    'Both C and H supply circumflex spellings at all four apparait/connait loci. Two apparait forms and the second connait are changed to plain i; the first connai-t retains both alternatives.',
    'Both C and H supply a diaeresis in sous-groupoïde; the later groupoï-/de has its own two points and remains accented.',
    'Neither witness is changed at lui-même. This confirmation limits any inference from absence of a detached caret.'
]):
    item = dict(item)
    item['witness_errors'] = errors
    r['hand_log'].append(item)

r['notes'].extend([
    'Second reading: both apparait forms and the second connait have compact i points. The first connai-t has a short oblique mark and remains unsure{connait|connaît}. The local sous-groupoide has one point, while the later divided groupoï-/de has two. These spellings are kept separately; no uniform spelling is imposed.',
    'Two small dark points occur below/right of the final t of the first connai-t, left of l’opération and distinctly above the next formula. Their low position leaves punctuation versus incidental pen-points unresolved. The transcription contains only an explicitly uncertain colon, and the points have their own inventory entry.',
    'The final lui-même retains a connected raised circumflex gesture. All four inherited doubtful readings and the resolved f and cancelled on are confirmed at the same certainty. No mathematical check was performed in the second reading.'
])

ledger_path = OUT/'documentation/root_view_ledger.json'
ledger = json.loads(ledger_path.read_text())
for crop in a['view_record']['new_crops']:
    if crop['path'] not in ledger['88']['crops_seen']:
        ledger['88']['crops_seen'].append(crop['path'])
ledger['88']['audit_native_bottom_seen'] = True
ledger_path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+'\n')

notation_path = OUT/'documentation/notation_audit_updates.json'
notation = json.loads(notation_path.read_text())
entry = next(x for x in notation if x.get('sign','').startswith('connait;'))
entry['pages'] = '082, 085–086, 088'
entry['evidence'] += ' On 088, the first connai-t remains uncertain with plain i preferred, while the second has a compact point and is transcribed connait. Both apparait forms also have compact points; the local sous-groupoide has one i point whereas later groupoï-/de has two. The connected raised ê gesture in lui-même is retained.'
notation_path.write_text(json.dumps(notation, ensure_ascii=False, indent=2)+'\n')
subprocess.run([sys.executable, str(OUT/'scripts/canonical_notation.py')], check=True)

commit(88, r, a, s,
    'Complete independent second reading by reader_a. The main reader inspected all six proposed loci on their saved crops, the comparison groupoid and même crops, and the native bottom half for placement of the low points. Accepted five local diacritic revisions and a separately uncertain colon. All nine inherited inventory elements and the new point-pair are accounted for; four old doubts and two new doubts remain explicit. No mathematical check event.',
    adjudications)
