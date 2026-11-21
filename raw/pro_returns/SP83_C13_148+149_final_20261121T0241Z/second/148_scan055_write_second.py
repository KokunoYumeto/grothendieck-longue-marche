"""Write and seal all blind rows, without any first-reading input."""
import csv
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path('/workspace/scratch/f28c4f52d3ec/result/second')
PAGE = '148_scan055'
spec = importlib.util.spec_from_file_location('blind055', BASE/f'{PAGE}_second_work.py')
work = importlib.util.module_from_spec(spec)
spec.loader.exec_module(work)
with (BASE/f'{PAGE}_boxes.tsv').open(newline='') as f:
    rows = list(csv.DictReader(f,delimiter='\t'))
order = [r['box'] for r in rows]
assert order == [f'B{i:02d}' for i in range(1,13)]
assert set(order) == set(work.READINGS)
assert all(work.READINGS[k].strip() for k in order)
out = BASE/f'{PAGE}_second.tsv'
with out.open('w',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t')
    writer.writeheader()
    for bid in order:
        writer.writerow({'box':bid,'reading':work.READINGS[bid]})

manifest_path = BASE/f'{PAGE}_second_crop_manifest.json'
manifest = json.loads(manifest_path.read_text())
for item in manifest:
    assert Path(item['path']).is_file()
    item['viewed'] = True
    item['independent_second_reading'] = True
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
notes = {
    'page':PAGE,
    'phase':'blind second reading',
    'reader':'reader_a',
    'sealed_utc':datetime.now(timezone.utc).isoformat(),
    'first_reading_or_comparison_opened':False,
    'original_viewed':True,
    'canonical_crop_count':12,
    'canonical_crops_all_viewed':True,
    'orientation_helper_count':0,
    'notes':work.NOTES,
    'boundary_issues':{
        'B03':'The parenthetical continues outside the rectangle and is left open.',
        'B05':'Right boundary is close to the final word and does not securely retain following punctuation.',
        'B07':'Bottom edge clips parts of the lower baseline descenders; some terminal word shapes remain uncertain.',
        'B10':'Top-edge ascenders and bottom p descender are partly clipped; no missing context is supplied.',
    },
    'protocol':'Only the assigned original, boxes, generic guide and newly created blind working files/crops were used. No OCR, web or TeX compilation. No first text, witnesses, accepted/proposed text, prior crops, records, notes or notation were opened.',
}
(BASE/f'{PAGE}_second_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
with out.open(newline='') as f:
    check = list(csv.DictReader(f,delimiter='\t'))
assert [r['box'] for r in check] == order
assert all(r['reading'] == work.READINGS[r['box']] for r in check)
print(json.dumps({'tsv':str(out),'rows':len(check),'all_crops_viewed':True,
                  'first_or_comparison_seen':False},indent=2))
