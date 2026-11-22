from pathlib import Path
import json,sys,csv,datetime,shutil
from neutralize_boxes import write_boxes
R=Path(__file__).resolve().parents[1]
page=sys.argv[1]
d=json.loads((R/'records'/f'{page}.json').read_text())
packet=json.loads((R.parent/'reading_packets'/page/'packet.json').read_text())
assert d.get('root_reviewed'), 'Root review must be recorded before finalizing.'
assert {x['id'] for x in d['decisions']}=={x['id'] for x in packet['marks']},'Mark coverage mismatch'
assert {x['diff_id'] for x in d['diff_coverage']}=={x['diff_id'] for x in packet['differences']},'Difference coverage mismatch'
for x in d['decisions']:
    assert x['decision']=='undecided' or x.get('crop'),f"Resolved mark without crop: {x['id']}"
for x in d['changes']:
    if x.get('crop'):assert (R/x['crop']).exists(),x['crop']
assert d['inventory'] and all(x['transcribed']=='yes' for x in d['inventory'])
shutil.copyfile(R/'records'/f'{page}.tex',R/'pages'/f'{page}.tex')
write_boxes(page,d)
for suffix,columns in [('first',['box','reading'])]:
    with (R/'second'/f'{page}_{suffix}.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=columns,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(d['second_boxes'])
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
num=len(list((R/'crops').glob(f'{page}_*.png')))
with (R/'progress.log').open('a') as f:f.write(f"scan {int(d['scan']):03} done {now} cote {d['cote']}: {d['line_count']} lines read, {num} places cropped, {len(d['changes'])} rows\n")
print(page,'finalized')
