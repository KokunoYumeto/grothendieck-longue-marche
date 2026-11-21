"""One-use root-approved presentation amendment; never redo the visual reading."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'documentation/epsilon_allograph_amendment.json'
assert not DEST.exists(), 'This documented amendment has already been applied.'
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
log = {'time_utc': now, 'authority': 'main reader; personal crop comparison',
       'scope': 'Presentation of the epsilon alternative only; favored calligraphic E and all prime doubts remain unchanged.',
       'evidence': 'The upper open curve, inward waist and lower returning curve in scan013 c09/c13/c15 and scan014 c13/c19 match the two-open-lobed epsilon alternative already represented by varepsilon in scan021 c05/c14. This standardizes the printed allograph of the same alternative letter; it neither settles E versus epsilon nor identifies a new symbol.',
       'accounting': 'No new substantive witness difference. Frozen inputs and audit-time adjudication readings/counts are retained; current page/report readings use varepsilon.',
       'scans': []}
note = ('Final notation presentation: the two-open-lobed epsilon alternative is printed '
        'with \\varepsilon, consistently with scan021. The favored \\mathcal E and all '
        'prime doubts are unchanged. Historical audit-time readings retain \\epsilon; '
        'see documentation/epsilon_allograph_amendment.json for exact changes. '
        'This is a presentation amendment, not a newly settled reading or a further mathematical check.')
for n in (13, 14):
    stem = f'149_scan{n:03d}'
    report_path = ROOT / f'reviews/{stem}.json'
    page_path = ROOT / f'pages/{stem}.tex'
    report = json.loads(report_path.read_text())
    before = page_path.read_text()
    after = before.replace(r'\epsilon', r'\varepsilon')
    assert after != before
    changes = []
    def replace_field(obj, key, path):
        value = obj.get(key)
        if isinstance(value, str) and r'\epsilon' in value:
            new = value.replace(r'\epsilon', r'\varepsilon')
            changes.append({'path': path + '/' + key, 'before': value, 'after': new})
            obj[key] = new
    for group, field in [('changes', 'final'), ('decisions', 'reading'),
                         ('notation', 'rendering'), ('doubts', 'reading')]:
        for i, row in enumerate(report[group]):
            replace_field(row, field, f'/{group}/{i}')
    for i, row in enumerate(report['doubts']):
        for j, value in enumerate(row.get('alternatives', [])):
            if r'\epsilon' in value:
                new = value.replace(r'\epsilon', r'\varepsilon')
                changes.append({'path': f'/doubts/{i}/alternatives/{j}',
                                'before': value, 'after': new})
                row['alternatives'][j] = new
    report['notes'].append(note)
    report.setdefault('presentation_amendments', []).append({
        'time_utc': now, 'record': 'documentation/epsilon_allograph_amendment.json',
        'audit_readings_and_counts_unchanged': True})
    audit = ROOT / f'second/{stem}_adjudications.tsv'
    audit_bytes = audit.read_bytes()
    affected = [row['box'] for row in csv.DictReader(audit.open(), delimiter='\t')
                if r'\epsilon' in row['final_reading']]
    page_path.write_text(after)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    assert audit.read_bytes() == audit_bytes
    log['scans'].append({'scan': n, 'page_before_sha256': hashlib.sha256(before.encode()).hexdigest(),
                         'page_after_sha256': hashlib.sha256(after.encode()).hexdigest(),
                         'page_before': before, 'page_after': after,
                         'report_fields': changes, 'affected_historical_audit_boxes': affected,
                         'audit_file_sha256_unchanged': hashlib.sha256(audit_bytes).hexdigest(),
                         'audit_changed_boxes_unchanged': report['audit_changed_boxes']})
DEST.write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
with (ROOT / 'progress.log').open('a') as f:
    f.write(f'notation presentation amended {now}: scans013/014 epsilon alternative uses varepsilon; '
            'favored readings, witness counts, frozen inputs and audit-time changed-box counts unchanged; '
            'see documentation/epsilon_allograph_amendment.json.\n')
print(json.dumps({'scans': [13, 14], 'record': str(DEST), 'presentation_only': True}))
