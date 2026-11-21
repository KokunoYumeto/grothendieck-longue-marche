"""Seal the complete independent scan059 TSV before any comparison."""
import csv,json,importlib.util
from datetime import datetime,timezone
from pathlib import Path
BASE=Path('/workspace/scratch/f28c4f52d3ec/result/second')
PAGE='148_scan059'
spec=importlib.util.spec_from_file_location('blind059',BASE/f'{PAGE}_second_work.py')
work=importlib.util.module_from_spec(spec)
spec.loader.exec_module(work)
with (BASE/f'{PAGE}_boxes.tsv').open(newline='') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
order=[r['box'] for r in rows]
assert order==[f'B{i:02d}' for i in range(1,16)]
assert set(order)==set(work.READINGS)
assert all(work.READINGS[k].strip() for k in order)
out=BASE/f'{PAGE}_second.tsv'
with out.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t')
    writer.writeheader()
    for bid in order:
        writer.writerow({'box':bid,'reading':work.READINGS[bid]})
details={
    'B10':[('right',[1980,0,3000,306]),('left',[0,0,1200,306])],
    'B11':[('formula',[700,0,1650,279])],
}
mp=BASE/f'{PAGE}_second_crop_manifest.json'
manifest=json.loads(mp.read_text())
for item in manifest:
    assert Path(item['path']).is_file()
    item['viewed']=True
    item['independent_second_reading']=True
    if item['box'] in details:
        item['same_box_detail_helpers']=[]
        for name,bounds in details[item['box']]:
            helper=BASE/f"{PAGE}_second_{item['box']}_{name}_detail.png"
            assert helper.is_file()
            item['same_box_detail_helpers'].append({'path':str(helper),'viewed':True,
                'canonical_crop_pixel_box':bounds,'additional_scale':2,
                'new_source_area':False,'bytes':helper.stat().st_size})
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
notes={'page':PAGE,'phase':'blind second reading','reader':'reader_a',
    'sealed_utc':datetime.now(timezone.utc).isoformat(),
    'first_reading_or_comparison_opened':False,'original_viewed':True,
    'canonical_crop_count':15,'canonical_crops_all_viewed':True,
    'same_box_details_viewed':3,'notes':work.NOTES,
    'boundary_issues':{
        'B08':'Right edge reaches the split prélimi- and bottom edge clips the low part of naire.',
        'B10':'Some lower descenders are clipped; the crowded symbolic readings remain uncertain.',
        'B11':'Initial b lies at the left/top boundary; cancelled formula itself is contained.',
        'B13':'Top of the t ascender in autre is clipped; word and final period remain readable.'},
    'incidental_context_clipping':['B03','B04','B14'],
    'protocol':'Only assigned source, boxes, generic guide and new independent working files/crops used. No OCR, web, TeX compilation, witnesses, first TSV, accepted/proposed text, prior crops, notation, records, comparisons or first-reading notes opened.'}
(BASE/f'{PAGE}_second_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
with out.open(newline='') as f:
    check=list(csv.DictReader(f,delimiter='\t'))
assert [r['box'] for r in check]==order
assert all(r['reading']==work.READINGS[r['box']] for r in check)
print(json.dumps({'tsv':str(out),'rows':len(check),'canonical_crops_viewed':15,
                  'same_box_details_viewed':3,'sealed_before_comparison':True},indent=2))
