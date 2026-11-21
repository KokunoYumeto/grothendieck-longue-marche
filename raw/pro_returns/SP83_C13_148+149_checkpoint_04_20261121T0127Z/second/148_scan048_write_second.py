from pathlib import Path
import csv
import hashlib
import json

BASE = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '148_scan048'
work = json.loads((BASE/'result/second'/f'{PAGE}_blind_work.json').read_text())
with (BASE/'result/second'/f'{PAGE}_boxes.tsv').open() as fh:
    boxes = list(csv.DictReader(fh, delimiter='\t'))
assert [r['box'] for r in work['rows']] == [r['box'] for r in boxes]
assert len(work['rows']) == 18
dest = BASE/'result/second'/f'{PAGE}_second.tsv'
if dest.exists():
    raise FileExistsError('Do not overwrite a completed blind reading')
with dest.open('w', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=['box','reading'], delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(work['rows'])
with dest.open(newline='') as fh:
    recovered = list(csv.DictReader(fh, delimiter='\t'))
assert recovered == work['rows']
manifest_path = BASE/'result/second'/f'{PAGE}_second_crop_manifest.json'
manifest = json.loads(manifest_path.read_text())
for crop in manifest['crops']:
    assert Path(crop['path']).is_file()
    crop['viewed'] = True
    crop['viewed_by'] = 'reader_b via tools.view_image; successful direct display'
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
report = {'page': PAGE, 'reader': 'reader_b', 'rows': len(recovered),
          'tsv': str(dest), 'sha256': hashlib.sha256(dest.read_bytes()).hexdigest(),
          'independence': 'Completed before any first-pass reading or comparison was seen. The TSV is now frozen.',
          'crop_count': len(manifest['crops']), 'crop_paths': [c['path'] for c in manifest['crops']],
          'boundaries': work['boundaries']}
(BASE/'result/second'/f'{PAGE}_second_read_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'page':PAGE,'rows':len(recovered),'crops':len(manifest['crops']),'sha256':report['sha256'],'boundary_notes':len(work['boundaries'])},indent=2))
