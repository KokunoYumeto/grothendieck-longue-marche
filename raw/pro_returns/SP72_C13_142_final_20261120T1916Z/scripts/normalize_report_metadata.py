"""Normalize evidence metadata without altering any transcription reading."""
from pathlib import Path
import json
import re
from collections import Counter

out = Path(__file__).resolve().parents[1]
manifest = {m['file']: m for m in map(json.loads, (out/'crops/crop_manifest.jsonl').read_text().splitlines())}
changed = 0
for folder in [out/'documentation/reviews', out/'documentation/decided']:
    paths = folder.glob('scan*/report.json') if folder.name == 'reviews' else folder.glob('scan*.json')
    for path in sorted(paths):
        report = json.loads(path.read_text())
        for decision in report.get('decisions', []):
            old = decision.get('crop', '')
            match = re.match(r'^(crops/\S+\.(?:jpg|png))(?=\s|;|$)', old)
            if not match:
                continue
            name = match[1]
            if name not in manifest:
                raise ValueError((path, name))
            m = manifest[name]
            decision.setdefault('original_crop_reference', old)
            decision['crop'] = f"{name}; original-pixel crop box {m['box']}; rotation {m['rotation']} degrees"
        for event in report.get('check_events', []):
            if event['statement_id'] == '142-094-R2':
                event['type'] = "refuted, with the refined statement's id: 142-094-R3"
            elif event['statement_id'] == '142-098-R2':
                event['type'] = "refuted, with the refined statement's id: 142-098-R1"
        if report.get('main_review_complete'):
            report.setdefault('first_reader_open_places', report.get('unresolved_for_root', []))
            report['unresolved_for_root'] = []
            report.setdefault('original_error_counts', report.get('error_counts', {}))
            places = [c for c in report.get('changes', []) if c.get('c_changed') or c.get('h_changed')]
            report['error_counts'] = {
                'unit': 'substantive places differing from at least one witness, including retained disagreements',
                'total': len(places),
                'against_C': sum(bool(c.get('c_changed')) for c in places),
                'against_H': sum(bool(c.get('h_changed')) for c in places),
                'confidence': dict(Counter(c['confidence'] for c in places)),
                'categories': dict(Counter(c['category'] for c in places)),
            }
        new = json.dumps(report, ensure_ascii=False, indent=2)+'\n'
        if path.read_text() != new:
            path.write_text(new)
            changed += 1
print(f'Normalized evidence metadata in {changed} reports; no page text changed.')
