from pathlib import Path
from datetime import datetime, timezone
import json,sys,subprocess
root=Path(__file__).resolve().parents[1]
page=sys.argv[1]
if (root/'state'/f'{page}_accepted.json').exists():
    raise SystemExit('Page already accepted; use a separately adjudicated audit for later changes.')
record_path=root/'readings'/f'{page}.json'
record=json.loads(record_path.read_text())
review=root/'state'/f'{page}_main_review.json'
if not review.exists(): raise SystemExit('Main-reader review record required.')
rv=json.loads(review.read_text())
if not rv.get('approved'): raise SystemExit('Main-reader approval missing.')
record['main_review']=rv
record['main_notes']=rv.get('notes','')
existing_events={e.get('statement_id') for e in record.get('check_events',[])}
for event in rv.get('additional_check_events',[]):
    if event.get('statement_id') in existing_events:
        raise SystemExit('Duplicate main-reader check-event statement id.')
    record.setdefault('check_events',[]).append(event)
    existing_events.add(event.get('statement_id'))
record['accepted_at']=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(root/'pages'/f'{page}.tex').write_text((root/'readings'/f'{page}.tex').read_text())
(root/'state'/f'{page}_accepted.json').write_text(json.dumps(record,ensure_ascii=False,indent=2))
subprocess.run([sys.executable,str(root/'scripts/build_reports.py')],check=True)
cote,scan=page.split('_scan')
with (root/'progress.log').open('a') as f: f.write(f'scan {scan} done {record["accepted_at"]} cote {cote}\n')
print('Accepted '+page)
