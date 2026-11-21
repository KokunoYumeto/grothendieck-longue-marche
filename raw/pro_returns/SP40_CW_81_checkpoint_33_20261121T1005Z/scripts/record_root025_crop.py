#!/usr/bin/env python3
"""Record a root-authored decision after one successful existing-crop display."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.load(sys.stdin)
audit_path = root / 'checks/scan025_root_crop_audit.json'
journal_path = root / 'checks/scan025_root_journal.md'
audit = json.loads(audit_path.read_text())
section = data['section']
rel = data['path']
assert not any(row['path'] == rel for row in audit['viewed_once'])
assert f'## {section} —' not in journal_path.read_text()
row = {
    'path': rel,
    'decision_sections': [section],
    'sha256': hashlib.sha256((root / rel).read_bytes()).hexdigest(),
    'successful_display_count': 1,
    'bbox': data['bbox'],
    'rotation': 0,
    'source_image': 'source/SP40_CW_81_scans/J81-03_81_scan025.jpg',
    'source_coordinate_system': 'full scan, top-left origin, pixels',
    'created_by_root': False,
    'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
}
if data.get('recovered'):
    row['recovered_after_unseen_delivery'] = True
audit['viewed_once'].append(row)
audit['total_distinct'] = len(audit['viewed_once'])
body = f"## {section} — {data['title']}\n\nCrop: `{rel}`, full box {data['bbox']}, successfully viewed once.\n\n{data['body'].rstrip()}\n\n"
journal_path.write_text(journal_path.read_text() + body)
audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
print(f"Root section {section} recorded; {audit['total_distinct']} successful distinct crops.")
