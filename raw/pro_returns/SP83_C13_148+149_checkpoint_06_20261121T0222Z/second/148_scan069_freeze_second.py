from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
from PIL import Image, ImageChops

BASE = Path(__file__).resolve().parents[2]
PAGE = '148_scan069'
SECOND = BASE / 'result' / 'second'
WORK_PATH = SECOND / f'{PAGE}_second_work.json'
MANIFEST_PATH = SECOND / f'{PAGE}_second_crop_manifest.json'
BOXES_PATH = SECOND / f'{PAGE}_boxes.tsv'
OUT_PATH = SECOND / f'{PAGE}_second.tsv'
SHA_PATH = SECOND / f'{PAGE}_second.sha256'
REPORT_PATH = SECOND / f'{PAGE}_second_view_report.json'

def sha256(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

for target in (OUT_PATH, SHA_PATH, REPORT_PATH):
    if target.exists():
        raise RuntimeError(f'Refusing to overwrite frozen output: {target}')

work = json.loads(WORK_PATH.read_text(encoding='utf-8'))
manifest = json.loads(MANIFEST_PATH.read_text(encoding='utf-8'))
with BOXES_PATH.open(encoding='utf-8', newline='') as handle:
    boxes = list(csv.DictReader(handle, delimiter='\t'))
assert [x['box'] for x in boxes] == ['B01', 'B02']
assert [x['box'] for x in work['readings']] == ['B01', 'B02']
views = {v['box']: v for v in work['actual_current_session_views']}
assert set(views) == {'B01', 'B02'}
assert all(v['success'] for v in views.values())

source = BASE / work['permitted_inputs'][0]
with Image.open(source) as image:
    assert list(image.size) == manifest['source_size']

crop_report = []
for box, crop in zip(boxes, manifest['crops']):
    assert box['box'] == crop['box']
    coordinates = [int(box[k]) for k in ('x0', 'y0', 'x1', 'y1')]
    assert coordinates == crop['original_box']
    canonical = Path(crop['path'])
    display = Path(crop.get('display_path', crop['path']))
    with Image.open(canonical) as png:
        assert list(png.size) == crop['output_size']
        if display != canonical:
            with Image.open(display) as transport:
                assert transport.size == png.size
                assert ImageChops.difference(png.convert('RGB'), transport.convert('RGB')).getbbox() is None
    crop['viewed'] = True
    crop['actual_view'] = views[box['box']]
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
        'displayed_utc': views[box['box']]['displayed_utc'],
        'display_transport': views[box['box']]['transport'],
    })

rows = []
for item in work['readings']:
    reading = ((BASE / item['reading_file']).read_text(encoding='utf-8').rstrip()
               if 'reading_file' in item else item['reading'])
    assert reading
    rows.append({'box': item['box'], 'reading': reading})

# Syntax-only brace balance and TSV round trip; no TeX compilation or rendering.
for row in rows:
    balance = 0
    text = row['reading']
    for index, char in enumerate(text):
        if char not in '{}':
            continue
        preceding = 0
        pos = index - 1
        while pos >= 0 and text[pos] == '\\':
            preceding += 1
            pos -= 1
        if preceding % 2:
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

manifest['frozen_tsv'] = str(OUT_PATH.relative_to(BASE))
manifest['frozen_tsv_sha256'] = digest
manifest['all_prescribed_crops_directly_viewed'] = True
manifest['frozen_utc'] = frozen_utc
MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

report = {
    'page': PAGE,
    'reader': 'reader_b',
    'status': 'Blind second reading complete and frozen before comparison; parent adjudication pending.',
    'box_count': len(rows),
    'box_order': [r['box'] for r in rows],
    'source': str(source.relative_to(BASE)),
    'source_sha256': sha256(source),
    'boxes_sha256': sha256(BOXES_PATH),
    'tsv': str(OUT_PATH.relative_to(BASE)),
    'tsv_sha256': digest,
    'tsv_bytes': OUT_PATH.stat().st_size,
    'frozen_utc': frozen_utc,
    'all_crops_visible': True,
    'no_clipped_target': True,
    'canonical_crops': crop_report,
    'boundaries': work['crop_boundaries'],
    'uncertainties': work['unresolved'],
    'view_provenance': {
        'current_session_successful_views': work['actual_current_session_views'],
        'earlier_session_report': work['earlier_view_attempts'],
        'original_view': work['original_view'],
    },
    'retained_generators': [
        f'result/second/{PAGE}_make_second_crops.py',
        f'result/second/{PAGE}_freeze_second.py',
    ],
    'retained_working_documentation': [
        f'result/second/{PAGE}_second_drawing.tex',
        f'result/second/{PAGE}_second_work.json',
        f'result/second/{PAGE}_second_crop_manifest.json',
    ],
    'transport_note': work['technical_limits']['transport_note'],
    'prohibited_inputs_consulted': False,
    'no_ocr': True,
    'no_research': True,
    'no_tex_compile': True,
    'first_reading_comparison_seen': False,
}
with REPORT_PATH.open('x', encoding='utf-8') as handle:
    json.dump(report, handle, ensure_ascii=False, indent=2)
    handle.write('\n')
print(json.dumps({
    'tsv': str(OUT_PATH),
    'sha256': digest,
    'box_count': len(rows),
    'all_crops_visible': True,
    'clipped_targets': 0,
    'view_report': str(REPORT_PATH),
}, indent=2))
