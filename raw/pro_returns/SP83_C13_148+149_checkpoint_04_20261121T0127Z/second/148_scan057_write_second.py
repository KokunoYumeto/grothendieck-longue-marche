"""Seal all scan057 blind readings without opening any first-pass material."""
import csv,json,importlib.util
from datetime import datetime,timezone
from pathlib import Path
BASE=Path('/workspace/scratch/f28c4f52d3ec/result/second')
PAGE='148_scan057'
spec=importlib.util.spec_from_file_location('blind057',BASE/f'{PAGE}_second_work.py')
work=importlib.util.module_from_spec(spec)
spec.loader.exec_module(work)
with (BASE/f'{PAGE}_boxes.tsv').open(newline='') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
order=[r['box'] for r in rows]
assert order==[f'B{i:02d}' for i in range(1,12)]
assert set(order)==set(work.READINGS)
assert all(work.READINGS[k].strip() for k in order)
out=BASE/f'{PAGE}_second.tsv'
with out.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t')
    writer.writeheader()
    for bid in order:
        writer.writerow({'box':bid,'reading':work.READINGS[bid]})
mp=BASE/f'{PAGE}_second_crop_manifest.json'
manifest=json.loads(mp.read_text())
for item in manifest:
    assert Path(item['path']).is_file()
    item['viewed']=True
    item['independent_second_reading']=True
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
notes={'page':PAGE,'phase':'blind second reading','reader':'reader_a',
       'sealed_utc':datetime.now(timezone.utc).isoformat(),
       'first_reading_or_comparison_opened':False,'original_viewed':True,
       'canonical_crop_count':11,'canonical_crops_all_viewed':True,
       'orientation_helper_count':0,'notes':work.NOTES,
       'boundary_issues':{
           'B04':'Upper boundary clips portions of opérateurs ascenders; word retained.',
           'B05':'Outer opening parenthesis lies at the left edge but is recognizable.',
           'B06':'Upper boundary clips some tall letters; no additional context supplied.',
           'B07':'Top edge clips part of opération; right edge lies near the uncertain split multiplicateur.',
           'B08':'Upper ascenders in the first line touch the boundary; readable target retained.'},
       'incidental_context_clipping':['B01','B03','B09','B10'],
       'protocol':'Only assigned original, boxes, generic guide and new independent working files/crops used. No OCR, web, TeX compilation, witnesses, first TSV, accepted/proposed text, prior crops, notation, records, comparisons or first notes opened.'}
(BASE/f'{PAGE}_second_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
with out.open(newline='') as f:
    check=list(csv.DictReader(f,delimiter='\t'))
assert [r['box'] for r in check]==order
assert all(r['reading']==work.READINGS[r['box']] for r in check)
print(json.dumps({'tsv':str(out),'rows':len(check),'canonical_crops_viewed':11,
                  'sealed_before_comparison':True},indent=2))
