from pathlib import Path
import csv, json, runpy, hashlib
from datetime import datetime, timezone
ROOT=Path('/workspace/scratch/f28c4f52d3ec/result')
PAGE='148_scan063'
sec=ROOT/'second'
data=runpy.run_path(str(sec/f'{PAGE}_second_work.py'))
with (sec/f'{PAGE}_boxes.tsv').open(newline='') as f:
    boxes=list(csv.DictReader(f,delimiter='\t'))
order=[b['box'] for b in boxes]
assert len(order)==24 and set(order)==set(data['READINGS'])
assert all(data['READINGS'][b].strip() for b in order)
out=sec/f'{PAGE}_second.tsv'
assert not out.exists(), 'Refuse to overwrite a frozen independent TSV.'
with out.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t',lineterminator='\n')
    w.writeheader()
    for b in order:w.writerow({'box':b,'reading':data['READINGS'][b]})
with out.open(newline='') as f:
    written=list(csv.DictReader(f,delimiter='\t'))
assert [r['box'] for r in written]==order
assert all(r['reading']==data['READINGS'][r['box']] for r in written)
for manifest in [sec/f'{PAGE}_second_crop_manifest.json',sec/f'{PAGE}_second_helper_manifest.json']:
    entries=json.loads(manifest.read_text())
    for e in entries:
        assert Path(e['path']).exists()
        e['viewed']=True
        e['view_method']='Direct tools.view_image output successfully received by independent reader_a.'
        e['sha256']=hashlib.sha256(Path(e['path']).read_bytes()).hexdigest()
    manifest.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
sha=hashlib.sha256(out.read_bytes()).hexdigest()
notes={
    'page':PAGE,'reader':'reader_a','status':'independent reading frozen; not compared or adjudicated',
    'box_count':24,'canonical_crops_viewed':24,'same_box_helpers_viewed':7,
    'original_viewed':True,
    'allowed_inputs_only':True,'no_ocr':True,'no_web':True,'no_TeX_compilation':True,
    'witnesses_first_text_prior_crops_notes_notation_comparisons_opened':False,
    'initial_B01_B04_batch_output_truncated':'Not counted as seen; all four subsequently viewed successfully.',
    'box_notes':data['NOTES'],
    'boundary_issues':[
        'B02 initial L ascender meets top boundary; word remains readable.',
        'B08 top phrase lies close to the boundary, while lower following-line fragments are clipped context and excluded.',
        'B10 upper portions of 4 and tall letters meet/cross top boundary; 4°) remains readable.',
        'B20 possible old opening parenthesis has no visible matching close inside its exact box; no closing parenthesis supplied.',
        'B22 clipped upper-edge prose and a left contextual word excluded from the complete mathematical display target.',
        'Other box-edge fragments identified as neighbouring lines are recorded individually and not completed.'
    ],
    'frozen_utc':datetime.now(timezone.utc).isoformat(),
    'tsv_sha256':sha,
    'manifests':[f'second/{PAGE}_second_crop_manifest.json',f'second/{PAGE}_second_helper_manifest.json']
}
(sec/f'{PAGE}_second_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
(sec/f'{PAGE}_second.sha256').write_text(f'{sha}  {PAGE}_second.tsv\n')
print(json.dumps({'file':str(out),'rows':len(written),'sha256':sha,'canonical':24,'helpers':7},ensure_ascii=False))
