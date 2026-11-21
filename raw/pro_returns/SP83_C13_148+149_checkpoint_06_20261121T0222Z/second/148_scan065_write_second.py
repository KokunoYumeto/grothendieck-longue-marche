from pathlib import Path
import csv,json,runpy,hashlib
from datetime import datetime,timezone
ROOT=Path('/workspace/scratch/f28c4f52d3ec/result')
PAGE='148_scan065'
sec=ROOT/'second'
data=runpy.run_path(str(sec/f'{PAGE}_second_work.py'))
with (sec/f'{PAGE}_boxes.tsv').open(newline='') as f:boxes=list(csv.DictReader(f,delimiter='\t'))
order=[b['box'] for b in boxes]
assert len(order)==7 and set(order)==set(data['READINGS'])
assert all(data['READINGS'][b].strip() for b in order)
out=sec/f'{PAGE}_second.tsv'
assert not out.exists(),'Refuse to overwrite frozen TSV'
with out.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t',lineterminator='\n')
    writer.writeheader()
    for b in order:writer.writerow({'box':b,'reading':data['READINGS'][b].strip()})
with out.open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
assert [r['box'] for r in rows]==order
assert all(r['reading']==data['READINGS'][r['box']].strip() for r in rows)
for filename in [f'{PAGE}_second_crop_manifest.json',f'{PAGE}_second_helper_manifest.json']:
    p=sec/filename
    entries=json.loads(p.read_text())
    for e in entries:
        e['viewed']=True
        e['view_method']='Direct tools.view_image output successfully received by independent reader_a.'
        e['sha256']=hashlib.sha256(Path(e['path']).read_bytes()).hexdigest()
    p.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
sha=hashlib.sha256(out.read_bytes()).hexdigest()
notes={'page':PAGE,'reader':'reader_a','status':'independent reading frozen; not compared or adjudicated','box_count':7,'canonical_crops_viewed':7,'same_box_helpers_viewed':3,'original_viewed':True,'allowed_inputs_only':True,'no_ocr':True,'no_web':True,'no_TeX_compilation':True,'witnesses_first_text_prior_crops_notes_notation_comparisons_opened':False,'box_notes':data['NOTES'],'boundary_issues':['B04 and B06 include clipped preceding-line tails at their top edges; these are context and excluded.','No target formula, insertion, number, or parenthesis is clipped by a supplied rectangle. Remaining uncertainty is handwriting ambiguity.'],'frozen_utc':datetime.now(timezone.utc).isoformat(),'tsv_sha256':sha,'manifests':[f'second/{PAGE}_second_crop_manifest.json',f'second/{PAGE}_second_helper_manifest.json']}
(sec/f'{PAGE}_second_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
(sec/f'{PAGE}_second.sha256').write_text(f'{sha}  {PAGE}_second.tsv\n')
print(json.dumps({'file':str(out),'rows':len(rows),'sha256':sha,'canonical':7,'helpers':3}))
