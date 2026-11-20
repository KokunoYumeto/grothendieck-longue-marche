"""Save only a due timed checkpoint, then persist it through the Library helper."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
out=Path(__file__).resolve().parents[1];root=out.parent
start=datetime.strptime((out/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
index=len(list(root.glob('SP42_CW_29_checkpoint_*.zip')))+1
wait=start.timestamp()+2700*index-time.time()
if wait>60:raise SystemExit('Checkpoint is not due within one minute; do not create early.')
if wait>0:time.sleep(wait)
r=subprocess.run([sys.executable,str(out/'scripts/package.py'),'checkpoint'],capture_output=True,text=True,check=True)
package=json.loads(r.stdout);print(json.dumps(package),flush=True)
request={'uploads':[{'local_path':package['path'],'purpose':'create_library_file','library_artifact_type':'other'}]}
receipt=root/f'checkpoint_{index:02d}_upload_result.json'
with receipt.open('w') as f:
 u=subprocess.run([sys.executable,str(root/'library_helpers/library_upload.py')],input=json.dumps(request),stdout=f,stderr=subprocess.PIPE,text=True)
print(json.dumps({'upload_exit_code':u.returncode,'receipt_path':str(receipt)}),flush=True)
if u.returncode:
 (root/f'checkpoint_{index:02d}_upload_error.txt').write_text(u.stderr)
 sys.exit(u.returncode)
