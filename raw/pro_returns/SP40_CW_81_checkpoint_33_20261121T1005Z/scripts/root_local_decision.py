#!/usr/bin/env python3
"""Append explicitly supplied root observations after successful local views."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import sys

payload = json.load(sys.stdin)
scan = int(payload['scan'])
n = f'{scan:03d}'
out = Path(__file__).resolve().parents[1]
audit_path = out / 'checks' / f'scan{n}_root_crop_audit.json'
audit = json.loads(audit_path.read_bytes())
journal_path = out / 'checks' / f'scan{n}_root_decisions.json'
journal = json.loads(journal_path.read_bytes()) if journal_path.exists() else {
    'scan': scan, 'author': '/root', 'source': 'Personal local-crop observations',
    'mathematical_check': False, 'decisions': []}
now = datetime.now(timezone.utc).isoformat()
for row in payload['decisions']:
    assert row['section'] not in {r['section'] for r in journal['decisions']}
    path = Path(row['crop_path'])
    relative = str(path.relative_to(out)) if path.is_absolute() else str(path)
    if relative.startswith('out/'):
        relative = relative[4:]
    assert relative not in {r['path'] for r in audit['viewed_once']}, relative
    full = out / relative
    digest = hashlib.sha256(full.read_bytes()).hexdigest()
    meta = row.get('crop_metadata', {})
    if relative.startswith(f'readers/{n}/'):
        reader = relative.split('/')[2]
        report = json.loads((out / 'readers' / n / reader / 'report.json').read_bytes())
        matches = [r for r in report['crops'] if Path(r['path']).name == full.name]
        assert len(matches) == 1
        meta = matches[0]
    event = {'path': relative, 'decision_sections': [row['section']],
             'sha256': digest, 'successful_display_count': 1,
             'bbox': meta.get('bbox'), 'rotation': meta.get('rotation', 0),
             'source_image': meta.get('source'),
             'source_coordinate_system': meta.get('coordinate_system', meta.get('coordinate_origin')),
             'created_by_root': relative.startswith('crops/'), 'recorded_utc': now}
    audit['viewed_once'].append(event)
    row.update(crop_path=relative, crop_sha256=digest, recorded_utc=now)
    journal['decisions'].append(row)
audit['total_distinct'] = len(audit['viewed_once'])
audit['last_decision_recorded_utc'] = now
for path, data in [(audit_path, audit), (journal_path, journal)]:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
md = ['# Root local decisions — scan ' + n, '',
      'All three complete returns and all three full pairwise TeX diffs were read before the first root image. Each listed local image was displayed once. The root saw no whole scan or supplied half. These are reading decisions, not proof checks.', '']
for row in journal['decisions']:
    md += ['## ' + row['section'] + ' — ' + row['title'], '',
           'Crop: `' + row['crop_path'] + '`; SHA-256 `' + row['crop_sha256'] + '`.', '',
           'Source locations: ' + ', '.join(row.get('source_loci', [])) + '.', '',
           '**Observed ink.** ' + row['evidence'], '',
           '**Decision.** ' + row['decision'], '',
           '**Assembly authority.** ' + row.get('assembly', 'Pending exact source assembly.'), '',
           'Confidence: ' + row['confidence'] + '.', '']
    if row.get('original_C_rows'):
        md += ['Original C row outcomes: ' + json.dumps(row['original_C_rows'], ensure_ascii=False) + '.', '']
(out / 'checks' / f'scan{n}_root_decisions.md').write_text('\n'.join(md))
progress_path = out / 'checks' / f'scan{n}_root_return_read_progress.json'
progress = json.loads(progress_path.read_bytes())
progress.update(root_image_views=audit['total_distinct'], updated_utc=now)
progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'scan': scan, 'recorded': [r['section'] for r in payload['decisions']],
                  'distinct_root_local_views': audit['total_distinct'], 'utc': now}))
