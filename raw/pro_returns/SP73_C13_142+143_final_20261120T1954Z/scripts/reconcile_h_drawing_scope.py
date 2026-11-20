"""Apply the main reader's documentary H-scope rulings; never alter source TeX.

The supplied H files contain prose descriptions rather than their external
drawing files. A missing local detail in that prose is not a demonstrated
omission in the unavailable drawing. Positive local claims remain comparable.
"""
from pathlib import Path
from datetime import datetime, timezone
import json

root = Path(__file__).resolve().parents[1]
rulings = {
    '142_scan106': ['142_scan106_D' + f'{n:02}' for n in [2,3,4,5,7,8,9,10,12]],
    '142_scan108': ['142_scan108D' + f'{n:02}' for n in [1,2,11,12,13,14,16,22,23,24,25]],
    '142_scan110': ['142_scan110_D' + f'{n:02}' for n in [10,11,12,13,15,16,17,18,20,21,22,23,24,25,26,29,33,35,36,37,38,39,40,41,42,43]],
    '142_scan113': ['142_scan113_D' + f'{n:02}' for n in [1,3,4,5,9]],
    '142_scan114': ['142_scan114D' + f'{n:02}' for n in [29,30,31,32]],
    '142_scan116': ['142_scan116_D' + f'{n:02}' for n in [26,27,28,29,30]],
    '142_scan117': ['142_scan117D30'],
    '142_scan118': ['142_scan118D23'],
    '142_scan121': ['142_scan121D25'],
}
receipt = root / 'state' / 'h_drawing_scope_reconciliation.json'
if receipt.exists():
    raise SystemExit('This documentary reconciliation has already been applied.')
records = {}
for page, ids in rulings.items():
    path = root / 'state' / (page + '_accepted.json')
    data = json.loads(path.read_text())
    index = {c['id']: c for c in data['changes']}
    for ident in ids:
        if ident not in index or not index[ident].get('differs_h'):
            raise SystemExit('Unexpected comparison state: ' + ident)
    records[page] = (path, data, index)

stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
reason = ('Not locally specified in the supplied H drawing description; the separate '
          'drawing file is unavailable. No H discrepancy is established at this detail.')
log = []
for page, ids in rulings.items():
    path, data, index = records[page]
    for ident in ids:
        row = index[ident]
        log.append({'page': page, 'id': ident, 'place': row['place'],
                    'old_h_summary': row.get('h', ''),
                    'old_differs_h': True, 'new_differs_h': False,
                    'differs_c_unchanged': bool(row.get('differs_c')), 'reason': reason})
        row['h_original_summary'] = row.get('h', '')
        row['h'] = reason
        row['differs_h'] = False
        row['h_scope_review'] = {'date': stamp, 'reader': '/root', 'reason': reason}
    data['h_drawing_scope_review'] = {
        'date': stamp, 'reader': '/root', 'corrected_ids': ids,
        'method': ('Main reread the complete supplied H source descriptions and compared '
                   'each claimed local difference with their actual scope. No new ink '
                   'reading, image view, mathematical check or TeX edit is claimed.')}
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
receipt.write_text(json.dumps({'date': stamp, 'reader': '/root', 'rulings': log},
                              ensure_ascii=False, indent=2) + '\n')
with (root / 'progress.log').open('a') as f:
    f.write(f'H drawing comparison scope reconciled {stamp}: {len(log)} unsupported '
            'H flags removed; ink readings and all C flags unchanged; see '
            'state/h_drawing_scope_reconciliation.json\n')
print(f'Reconciled {len(log)} H flags without changing transcription files.')
