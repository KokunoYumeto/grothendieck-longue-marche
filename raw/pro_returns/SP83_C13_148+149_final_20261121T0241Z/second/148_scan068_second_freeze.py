"""Write and freeze the independently completed second reading, once only."""
from pathlib import Path
import csv, hashlib, json, runpy
from datetime import datetime, timezone

ROOT=Path('/workspace/scratch/f28c4f52d3ec')
DIR=ROOT/'result/second'
PAGE='148_scan068'
target=DIR/f'{PAGE}_second.tsv'
if target.exists():
    raise RuntimeError('The second TSV already exists; do not overwrite a frozen reading.')
work=runpy.run_path(str(DIR/f'{PAGE}_second_work.py'))
readings,notes=work['READINGS'],work['NOTES']
with (DIR/f'{PAGE}_boxes.tsv').open(newline='') as f:
    boxes=list(csv.DictReader(f,delimiter='\t'))
order=[r['box'] for r in boxes]
assert len(order)==17 and len(set(order))==17
assert set(readings)==set(order) and set(notes)==set(order)
for b in order:
    text=readings[b]
    assert text.strip(), b
    assert text.count('{')==text.count('}'), b
    assert text.count(r'\begin{tikzpicture}')==text.count(r'\end{tikzpicture}'), b
with target.open('w',newline='') as f:
    writer=csv.writer(f,delimiter='\t',lineterminator='\n')
    writer.writerow(['box','reading'])
    writer.writerows((b,readings[b]) for b in order)
with target.open(newline='') as f:
    roundtrip=list(csv.DictReader(f,delimiter='\t'))
assert [r['box'] for r in roundtrip]==order
assert all(r['reading']==readings[r['box']] for r in roundtrip)

# These flags are the reader's record of successful displayed images, not inferred from file creation.
mp=DIR/f'{PAGE}_second_crop_manifest.json'
manifest=json.loads(mp.read_text())
for row in manifest:
    row['viewed']=True
    row['viewed_via']=row.get('transport_path',row['path'])
    row['sha256']=hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()
    if row['box']=='B06':
        row['visibility_note']='Canonical PNG exceeded transport cap; identical-pixel lossless WebP successfully viewed. Pixel identity separately verified.'
    elif row['box']=='B09':
        row['visibility_note']='First batched output discarded this image; it was subsequently viewed successfully in a separate call.'
    else:
        row['visibility_note']='Canonical exact-box crop successfully displayed and directly read.'
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
hp=DIR/f'{PAGE}_second_helper_manifest.json'
helpers=json.loads(hp.read_text())
assert len(helpers)==14
for row in helpers:
    row['viewed']=True
    row['sha256']=hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()
hp.write_text(json.dumps(helpers,ensure_ascii=False,indent=2)+'\n')

digest=hashlib.sha256(target.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
record={
    'page':PAGE,
    'reader':'reader_a',
    'status':'independent second reading frozen before comparison',
    'frozen_utc':now,
    'sha256':digest,
    'box_count':len(order),
    'canonical_crops_viewed':17,
    'same_box_helpers_viewed':14,
    'original_viewed_once':True,
    'first_reading_materials_consulted':False,
    'ocr_used':False,
    'tex_compiled':False,
    'boundary_summary':'No prescribed target was clipped in a way that prevented its complete reading. Overlapping drawing fragments and printed rules/hatch at edges were treated as context. Some internal drawing junctions remain uncertain under the printer pattern and are explicitly retained as doubts.',
    'boxes':[{'box':b,'note':notes[b]} for b in order],
}
(DIR/f'{PAGE}_second_notes.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(DIR/f'{PAGE}_second.sha256').write_text(digest+'  '+target.name+'\n')
target.chmod(0o444)
print(json.dumps({'path':str(target),'sha256':digest,'boxes':len(order),'bytes':target.stat().st_size,'canonical_crops_viewed':17,'same_box_helpers_viewed':14},indent=2))
