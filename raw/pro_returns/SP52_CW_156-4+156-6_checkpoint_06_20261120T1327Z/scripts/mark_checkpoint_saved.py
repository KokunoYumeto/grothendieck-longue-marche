from pathlib import Path
import json,sys,datetime,hashlib
O=Path(__file__).resolve().parents[1]
n=int(sys.argv[1]);file_id=sys.argv[2]
if not file_id.startswith('libfile_'):raise SystemExit('Pass the exact Library id returned by a successful save')
p=O/'checkpoint_records.json';records=json.loads(p.read_text());r=next(x for x in records if x['number']==n)
z=O.parent/r['filename'];now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
r.update(status='saved',library_file_id=file_id,saved_utc=now,sha256=hashlib.sha256(z.read_bytes()).hexdigest(),size=z.stat().st_size)
p.write_text(json.dumps(records,indent=2)+'\n')
with (O/'progress.log').open('a') as f:f.write(f'checkpoint {n:02d} saved {now} {file_id} SHA256 {r["sha256"]}\n')
print(json.dumps({'number':n,'status':'saved','library_file_id':file_id,'sha256':r['sha256']}))
