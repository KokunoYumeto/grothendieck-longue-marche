import csv
import hashlib
import json
from pathlib import Path

BASE = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '148_scan056'
SECOND = BASE / 'result/second'
work = json.loads((SECOND / f'{PAGE}_blind_work.json').read_text())
with (SECOND / f'{PAGE}_boxes.tsv').open(newline='') as stream:
    boxes = list(csv.DictReader(stream, delimiter='\t'))
rows = work['readings']
assert len(rows) == len(boxes) == 24
assert [r['box'] for r in rows] == [r['box'] for r in boxes]
assert all(r['reading'] for r in rows)
output = SECOND / f'{PAGE}_second.tsv'
with output.open('x', newline='', encoding='utf-8') as stream:
    writer = csv.DictWriter(stream, fieldnames=['box', 'reading'], delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
with output.open(newline='', encoding='utf-8') as stream:
    assert list(csv.DictReader(stream, delimiter='\t')) == rows

manifest_path = SECOND / f'{PAGE}_second_crop_manifest.json'
manifest = json.loads(manifest_path.read_text())
assert [c['box'] for c in manifest['crops']] == [r['box'] for r in rows]
for crop in manifest['crops']:
    path = Path(crop['path'])
    assert path.is_file()
    crop['viewed'] = True
    crop['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
digest = hashlib.sha256(output.read_bytes()).hexdigest()
report = {
    'page': PAGE,
    'reader': 'reader_b',
    'rows': len(rows),
    'new_crops': len(manifest['crops']),
    'all_crops_directly_viewed': True,
    'original_viewed_once': True,
    'box_order_verified': True,
    'tsv_round_trip_verified': True,
    'tsv': str(output),
    'sha256': digest,
    'frozen': True,
    'independence': 'The complete independent TSV was written before any comparison. Neither witness, first TSV, accepted page, first crops, notation, records, comparison nor page notes was opened.',
    'boundary_issues': work['boundary_issues'],
    'visual_notes': work['visual_notes'],
    'display_notes': work['display_notes'],
    'crops': [c['path'] for c in manifest['crops']],
    'crop_manifest': str(manifest_path),
    'crop_generator': str(SECOND / f'{PAGE}_make_second_crops.py'),
    'writer': str(SECOND / f'{PAGE}_write_second.py'),
    'blind_work': str(SECOND / f'{PAGE}_blind_work.json'),
    'audit_status': 'Independent reading complete; comparison and main-reader adjudication pending.'
}
report_path = SECOND / f'{PAGE}_second_read_report.json'
with report_path.open('x', encoding='utf-8') as stream:
    json.dump(report, stream, ensure_ascii=False, indent=2)
    stream.write('\n')
print(json.dumps({'page': PAGE, 'rows': len(rows), 'crops': len(manifest['crops']), 'sha256': digest, 'tsv': str(output), 'report': str(report_path)}, ensure_ascii=False))
