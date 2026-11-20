#!/usr/bin/env python3
"""Record a later main-reader amendment without losing its previous check event."""
import argparse, csv, hashlib, json
from accept_page import ROOT, load_original, reconstruct, refresh, stamp

p=argparse.ArgumentParser()
p.add_argument('page')
p.add_argument('--note',required=True)
a=p.parse_args()
path=ROOT/'review'/f'{a.page}.accepted.json'
old=json.loads(path.read_text())
new=json.loads((ROOT/'review'/f'{a.page}.final.json').read_text())
assert [(r['row_index'],r['id']) for r in old['rows']]==[(r['row_index'],r['id']) for r in new['rows']]
original=load_original(a.page)
text,edits=reconstruct(original,new['rows'])
prior=ROOT/'review'/f'{a.page}.before_amendment_{len(list((ROOT/"review").glob(a.page+".before_amendment_*.json")))+1:02}.json'
assert not prior.exists()
prior.write_bytes(path.read_bytes())
event_path=ROOT/'review/additional_check_events.json'
extras=json.loads(event_path.read_text()) if event_path.exists() else []
with (ROOT/'CHECK_EVENTS.tsv').open(newline='',encoding='utf-8') as f:
    for event in csv.DictReader(f,delimiter='\t'):
        if event['date']==old['accepted_utc'] and a.page in event['who'] and 'main reader' in event['who'] and event not in extras:
            extras.append(event)
event_path.write_text(json.dumps(extras,ensure_ascii=False,indent=2)+'\n')
new.update({'accepted_utc':stamp(),'review_note':a.note,'original_sha256':hashlib.sha256(original.encode()).hexdigest(),'edited_sha256':hashlib.sha256(text.encode()).hexdigest(),'unique_edit_count':len(edits),'supersedes_record':prior.relative_to(ROOT).as_posix()})
(ROOT/'edited_pages'/f'{a.page}.tex').write_bytes(text.encode())
(ROOT/'review'/f'{a.page}.main_revised.tex').write_bytes(text.encode())
path.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
refresh()
cote,scan=a.page.split('_scan')
with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
    f.write(f'scan {scan} amended {new["accepted_utc"]} cote {cote}: later visual comparison; prior record retained\n')
print(json.dumps({'amended':a.page,'decisions':[r['decision'] for r in new['rows']],'unique_edits':len(edits),'utc':new['accepted_utc']}))
