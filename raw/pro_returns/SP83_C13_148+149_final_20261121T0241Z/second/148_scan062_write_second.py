from pathlib import Path
import csv
import hashlib
import json
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parents[2]
PAGE = '148_scan062'
SECOND = BASE / 'result' / 'second'
work_path = SECOND / f'{PAGE}_second_work.json'
views_path = SECOND / f'{PAGE}_second_views.json'
boxes_path = SECOND / f'{PAGE}_boxes.tsv'
manifest_path = SECOND / f'{PAGE}_second_crop_manifest.json'
tsv_path = SECOND / f'{PAGE}_second.tsv'
report_path = SECOND / f'{PAGE}_second_read_report.json'

for path in (tsv_path, report_path):
    if path.exists():
        raise SystemExit(f'Refusing to overwrite frozen output: {path}')

work = json.loads(work_path.read_text(encoding='utf-8'))
views = json.loads(views_path.read_text(encoding='utf-8'))
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
with boxes_path.open(encoding='utf-8', newline='') as handle:
    boxes = list(csv.DictReader(handle, delimiter='\t'))

expected = [row['box'] for row in boxes]
readings = work['readings']
assert len(expected) == 21
assert [row['box'] for row in readings] == expected
assert all(set(row) == {'box', 'reading'} and row['reading'] for row in readings)
successful = {row['box']: row for row in views['crop_displays'] if row['success']}
assert list(successful) == expected
assert [row['box'] for row in manifest['crops']] == expected

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

for specification, crop in zip(boxes, manifest['crops']):
    assert crop['original_box'] == [int(specification[k]) for k in ('x0', 'y0', 'x1', 'y1')]
    path = Path(crop['path'])
    assert path.is_file()
    assert successful[crop['box']]['path'] == str(path)
    crop['viewed'] = True
    crop['view_record'] = str(views_path)
    crop['sha256'] = sha256(path)
manifest['viewed_count'] = 21
manifest['independent_reading_complete'] = True
manifest['audit_status'] = 'Awaiting main-reader comparison and adjudication.'
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

with tsv_path.open('x', encoding='utf-8', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=['box', 'reading'], delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(readings)
with tsv_path.open(encoding='utf-8', newline='') as handle:
    checked = list(csv.DictReader(handle, delimiter='\t'))
assert checked == readings

report = {
    'page': PAGE,
    'reader': '/root/reader_b',
    'mode': 'Independent blind second reading',
    'frozen': True,
    'frozen_utc': datetime.now(timezone.utc).isoformat(),
    'tsv': str(tsv_path),
    'tsv_sha256': sha256(tsv_path),
    'row_count': len(readings),
    'box_order': expected,
    'unique_successful_crop_views': len(successful),
    'crop_display_attempts': len(views['crop_displays']),
    'original_views': views['original']['count'],
    'crop_paths': [row['path'] for row in manifest['crops']],
    'crop_manifest': str(manifest_path),
    'actual_view_record': str(views_path),
    'work_record': str(work_path),
    'crop_generator': str(SECOND / f'{PAGE}_make_second_crops.py'),
    'writer': str(Path(__file__).resolve()),
    'source_sha256': sha256(manifest['source']),
    'boxes_sha256': sha256(boxes_path),
    'boundaries': work['boundaries'],
    'independence': work['independence'],
    'display_limit': views['failed_attempt_note'],
    'boundary_policy': views['boundary_policy'],
    'audit_status': 'Not adjudicated. Main reader must compare and adjudicate; frozen independent TSV must not be edited after exposure to first readings.'
}
with report_path.open('x', encoding='utf-8') as handle:
    json.dump(report, handle, ensure_ascii=False, indent=2)
    handle.write('\n')
print(json.dumps({k: report[k] for k in ('page', 'row_count', 'unique_successful_crop_views', 'tsv_sha256', 'frozen')}, ensure_ascii=False))
