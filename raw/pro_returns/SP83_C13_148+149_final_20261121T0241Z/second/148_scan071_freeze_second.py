from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
from PIL import Image, ImageChops

BASE = Path(__file__).resolve().parents[2]
PAGE = '148_scan071'
SECOND = BASE / 'result' / 'second'
WORK_PATH = SECOND / f'{PAGE}_second_work.json'
MANIFEST_PATH = SECOND / f'{PAGE}_second_crop_manifest.json'
BOXES_PATH = SECOND / f'{PAGE}_boxes.tsv'
OUT_PATH = SECOND / f'{PAGE}_second.tsv'
SHA_PATH = SECOND / f'{PAGE}_second.sha256'
REPORT_PATH = SECOND / f'{PAGE}_second_view_report.json'

def sha256(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            result.update(block)
    return result.hexdigest()

for path in (OUT_PATH, SHA_PATH, REPORT_PATH):
    if path.exists():
        raise RuntimeError(f'Refusing to overwrite frozen output: {path}')

work = json.loads(WORK_PATH.read_text(encoding='utf-8'))
manifest = json.loads(MANIFEST_PATH.read_text(encoding='utf-8'))
with BOXES_PATH.open(encoding='utf-8', newline='') as handle:
    boxes = list(csv.DictReader(handle, delimiter='\t'))
expected = [f'B{index:02d}' for index in range(1, 10)]
assert [box['box'] for box in boxes] == expected
assert [row['box'] for row in work['readings']] == expected
assert [crop['box'] for crop in manifest['crops']] == expected
assert [view['box'] for view in work['actual_views']] == expected
assert all(view['success'] for view in work['actual_views'])
assert work['original_view']['success']
assert work['original_view']['count'] == 1
assert work['prohibited_material_consulted'] is False

source = BASE / work['permitted_inputs'][0]
with Image.open(source) as image:
    assert list(image.size) == manifest['source_size']

crop_report = []
for box, crop, view in zip(boxes, manifest['crops'], work['actual_views']):
    coordinates = [int(box[key]) for key in ('x0', 'y0', 'x1', 'y1')]
    assert coordinates == crop['original_box']
    canonical = Path(crop['path'])
    display = Path(crop['display_path'])
    assert view['canonical_path'] == str(canonical)
    assert view['display_path'] == str(display)
    with Image.open(canonical) as png:
        assert list(png.size) == crop['output_size']
        if canonical != display:
            with Image.open(display) as transport:
                assert transport.size == png.size
                assert ImageChops.difference(png.convert('RGB'), transport.convert('RGB')).getbbox() is None
    crop['viewed'] = True
    crop['actual_view'] = view
    crop['canonical_sha256'] = sha256(canonical)
    crop_report.append({
        'box': box['box'],
        'kind': box['kind'],
        'coordinates': coordinates,
        'canonical_png': str(canonical.relative_to(BASE)),
        'canonical_sha256': crop['canonical_sha256'],
        'output_size': crop['output_size'],
        'directly_viewed': True,
        'display_path': str(display.relative_to(BASE)),
        'displayed_utc': view['displayed_utc'],
        'display_transport': view['transport'],
    })

rows = [{'box': row['box'], 'reading': row['reading'].rstrip()} for row in work['readings']]
for row in rows:
    assert row['reading']
    balance = 0
    for index, char in enumerate(row['reading']):
        if char not in '{}':
            continue
        preceding_slashes = 0
        pos = index - 1
        while pos >= 0 and row['reading'][pos] == '\\':
            preceding_slashes += 1
            pos -= 1
        if preceding_slashes % 2:
            continue
        balance += 1 if char == '{' else -1
        assert balance >= 0, (row['box'], index)
    assert balance == 0, row['box']

buffer = io.StringIO(newline='')
writer = csv.DictWriter(buffer, fieldnames=['box', 'reading'], delimiter='\t', lineterminator='\n')
writer.writeheader()
writer.writerows(rows)
payload = buffer.getvalue()
roundtrip = list(csv.DictReader(io.StringIO(payload, newline=''), delimiter='\t'))
assert roundtrip == rows

frozen_utc = datetime.now(timezone.utc).isoformat()
with OUT_PATH.open('x', encoding='utf-8', newline='') as handle:
    handle.write(payload)
digest = sha256(OUT_PATH)
with SHA_PATH.open('x', encoding='utf-8') as handle:
    handle.write(f'{digest}  {OUT_PATH.name}\n')
OUT_PATH.chmod(0o444)
SHA_PATH.chmod(0o444)

manifest['all_prescribed_crops_directly_viewed'] = True
manifest['frozen_tsv'] = str(OUT_PATH.relative_to(BASE))
manifest['frozen_tsv_sha256'] = digest
manifest['frozen_utc'] = frozen_utc
MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

report = {
    'page': PAGE,
    'reader': 'reader_b',
    'status': 'Blind second reading complete and frozen before comparison; parent adjudication pending.',
    'box_count': len(rows),
    'box_order': expected,
    'source': str(source.relative_to(BASE)),
    'source_sha256': sha256(source),
    'boxes_sha256': sha256(BOXES_PATH),
    'tsv': str(OUT_PATH.relative_to(BASE)),
    'tsv_sha256': digest,
    'tsv_bytes': OUT_PATH.stat().st_size,
    'frozen_utc': frozen_utc,
    'all_crops_directly_visible': True,
    'canonical_crops': crop_report,
    'boundaries': work['crop_boundaries'],
    'boundary_flagged_boxes': [entry['box'] for entry in work['crop_boundaries'] if not entry['target_complete']],
    'no_boundary_extensions': True,
    'uncertainties': work['unresolved'],
    'view_provenance': {
        'original_view': work['original_view'],
        'successful_crop_views': work['actual_views'],
        'failed_or_discarded_crop_views': [],
    },
    'retained_generators': [
        f'result/second/{PAGE}_make_second_crops.py',
        f'result/second/{PAGE}_freeze_second.py',
    ],
    'retained_working_documentation': [
        f'result/second/{PAGE}_second_work.json',
        f'result/second/{PAGE}_second_crop_manifest.json',
        f'result/second/{PAGE}_second_B08_text.tex',
        f'result/second/{PAGE}_second_B08_background.tex',
    ],
    'transport_note': work['technical_limits']['transport_note'],
    'prohibited_inputs_consulted': False,
    'first_reading_comparison_seen': False,
    'no_ocr': True,
    'no_web': True,
    'no_tex_compilation': True,
}
with REPORT_PATH.open('x', encoding='utf-8') as handle:
    json.dump(report, handle, ensure_ascii=False, indent=2)
    handle.write('\n')
print(json.dumps({
    'tsv': str(OUT_PATH),
    'sha256': digest,
    'box_count': len(rows),
    'all_crops_directly_visible': True,
    'boundary_flagged_boxes': report['boundary_flagged_boxes'],
    'view_report': str(REPORT_PATH),
}, indent=2))
