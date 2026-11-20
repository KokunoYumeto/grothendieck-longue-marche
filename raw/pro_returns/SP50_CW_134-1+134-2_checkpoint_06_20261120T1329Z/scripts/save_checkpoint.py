"""Create one due cumulative ZIP and save it durably. Never overwrite old ZIPs."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,csv
O=Path(__file__).resolve().parents[1];fmt='%Y-%m-%d %H:%M:%S UTC'
s=json.loads((O/'state.json').read_text());n=s['next_checkpoint'];name=f"{s['prefix']}_checkpoint_{n:02d}.zip";dest=O.parent/'deliveries'/name
pending=O/'checkpoint_pending.json'
if dest.exists():
    if not pending.exists():raise RuntimeError('Existing checkpoint has no upload-pending record; inspect before retry')
    meta=json.loads(pending.read_text());assert meta['path']==str(dest)
else:
    r=subprocess.run([sys.executable,str(O/'scripts/build_workflow.py')],capture_output=True,text=True,check=True)
    r=subprocess.run([sys.executable,str(O/'scripts/package.py'),'--checkpoint'],capture_output=True,text=True,check=True)
    meta=json.loads(r.stdout)
    if not meta['due']:print(json.dumps(meta));raise SystemExit(0)
    pending.write_text(json.dumps(meta,indent=2)+'\n')
request={'uploads':[{'local_path':str(dest),'purpose':'create_library_file','library_artifact_type':'other'}]}
r=subprocess.run([sys.executable,str(O/'scripts/library_helpers/library_upload.py')],input=json.dumps(request)+'\n',capture_output=True,text=True)
if r.returncode:raise RuntimeError('Durable upload failed: '+r.stderr)
response=json.loads(r.stdout);result=response['results'][0]
if result.get('status')!='succeeded':raise RuntimeError('Durable upload did not succeed: '+json.dumps(result))
file_id=result['library_file_id'];now=datetime.now(timezone.utc).strftime(fmt)
receipt={k:result[k] for k in ['status','library_file_id','file_id','file_name','version'] if k in result}
receipt.update(filename=name,created_utc=meta['created_utc'],saved_utc=now,bytes=dest.stat().st_size)
D=O/'save_receipts';D.mkdir(exist_ok=True);(D/f'checkpoint_{n:02d}.json').write_text(json.dumps(receipt,indent=2)+'\n')
with (O/'checkpoints.tsv').open('a',newline='') as f:csv.writer(f,delimiter='\t').writerow([n,name,meta['created_utc'],now,file_id,dest.stat().st_size])
with (O/'progress.log').open('a') as f:f.write(f'checkpoint saved {now} {name} {file_id}\n')
s['last_checkpoint_utc']=meta['created_utc'];s['next_checkpoint']=n+1;(O/'state.json').write_text(json.dumps(s,indent=2)+'\n')
pending.unlink()
print(json.dumps(receipt))
