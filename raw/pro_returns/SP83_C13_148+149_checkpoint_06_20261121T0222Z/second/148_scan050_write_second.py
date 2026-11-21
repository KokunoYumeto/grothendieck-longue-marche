"""Seal the independent reading; reads no first-reading or comparison file."""
import csv
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path('/workspace/scratch/f28c4f52d3ec/result/second')
stem = '148_scan050'
spec = importlib.util.spec_from_file_location('blind050', BASE / f'{stem}_second_work.py')
work = importlib.util.module_from_spec(spec)
spec.loader.exec_module(work)
with (BASE / f'{stem}_boxes.tsv').open(newline='') as src:
    boxes = list(csv.DictReader(src, delimiter='\t'))
order = [row['box'] for row in boxes]
assert order == [f'B{i:02d}' for i in range(1, 22)]
assert set(work.READINGS) == set(order)
assert all(work.READINGS[bid].strip() for bid in order)

out = BASE / f'{stem}_second.tsv'
with out.open('w', newline='') as dst:
    writer = csv.DictWriter(dst, fieldnames=['box', 'reading'], delimiter='\t')
    writer.writeheader()
    for bid in order:
        writer.writerow({'box': bid, 'reading': work.READINGS[bid]})

manifest_path = BASE / f'{stem}_second_crop_manifest.json'
manifest = json.loads(manifest_path.read_text())
angles = {'B06': -37, 'B07': -4, 'B08': -4, 'B09': -4, 'B10': -4}
for item in manifest:
    item['viewed'] = True
    item['independent_second_reading'] = True
    if item['box'] in angles:
        helper = BASE / f"{stem}_second_{item['box']}_rotated.png"
        assert helper.is_file()
        item['orientation_helper'] = {
            'path': str(helper),
            'same_original_box': True,
            'rotation_degrees_pillow': angles[item['box']],
            'viewed': True,
            'bytes': helper.stat().st_size,
        }
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

notes = {
    'page': stem,
    'phase': 'blind second reading',
    'reader': 'reader_a',
    'sealed_utc': datetime.now(timezone.utc).isoformat(),
    'first_reading_or_comparison_opened': False,
    'original_viewed': True,
    'canonical_crop_count': 21,
    'canonical_crops_all_viewed': True,
    'orientation_helpers_viewed': list(angles),
    'readings_file': str(out),
    'notes': work.NOTES,
    'boundary_issues': {
        'B12': 'Upper boundary clips ascenders of the following la donnée des fragment.',
        'B13': 'Lower map starts close to the bottom boundary; visible reading retained.',
        'B14': 'Upper boundary clips the top of the two tall l strokes in famille.',
        'B17': 'Far-right curved punctuation/parenthesis has uncertain attachment to the target insertion.',
        'B18': 'Right boundary clips the closing parenthesis of the lower-right diagram object.',
    },
    'incidental_context_clipping': ['B04','B05','B07','B08','B09','B10','B19'],
    'protocol': 'No OCR, web, TeX compilation, witnesses, proposal, accepted page, first TSV, notes, notation, prior crops, records, or comparison used.',
}
(BASE / f'{stem}_second_notes.json').write_text(json.dumps(notes, ensure_ascii=False, indent=2) + '\n')

with out.open(newline='') as src:
    check = list(csv.DictReader(src, delimiter='\t'))
assert [row['box'] for row in check] == order
assert all(row['reading'] == work.READINGS[row['box']] for row in check)
print(json.dumps({'tsv': str(out), 'rows': len(check), 'canonical_crops_viewed': 21,
                  'orientation_helpers_viewed': len(angles), 'sealed_before_comparison': True}, indent=2))
