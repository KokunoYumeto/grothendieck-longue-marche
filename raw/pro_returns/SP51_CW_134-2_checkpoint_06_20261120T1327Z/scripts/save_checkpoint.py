"""Create a due checkpoint and persist it with the official Library upload helper."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,sys,json,time
root=Path(__file__).resolve().parents[1];base=root.parent
if sys.argv[1:]==['wait-if-close']:
 statep=root/'records/checkpoint_state.json'
 state=json.loads(statep.read_text()) if statep.exists() else {'last_time':(root/'progress.log').read_text().splitlines()[0]}
 last=datetime.strptime(state['last_time'],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
 remaining=2700-(datetime.now(timezone.utc)-last).total_seconds()
 if 0<remaining<=60:time.sleep(remaining+.05)
 elif remaining>60:raise SystemExit('Checkpoint is not yet close to its interval')
r=subprocess.run([sys.executable,str(root/'scripts/checkpoint.py')],capture_output=True,text=True,check=True)
d=json.loads(r.stdout);print(json.dumps(d),flush=True)
if not d['due']:raise SystemExit
helper=base/'.library-helper/library_upload.py'
request={'uploads':[{'local_path':d['path'],'purpose':'create_library_file','library_artifact_type':'other'}]}
response=base/'.library-helper'/f'checkpoint_{d["number"]:02}_response.json'
u=subprocess.run([sys.executable,str(helper)],input=json.dumps(request),capture_output=True,text=True)
response.write_text(u.stdout)
if u.stderr:(base/'.library-helper'/f'checkpoint_{d["number"]:02}_stderr.txt').write_text(u.stderr)
print(json.dumps({'upload_returncode':u.returncode,'response_path':str(response),'stderr_bytes':len(u.stderr)}),flush=True)
if u.returncode==0:
 result=json.loads(u.stdout)
 entries=result.get('results',[])
 if len(entries)!=1 or entries[0].get('status')!='succeeded' or not entries[0].get('local_metadata_applied'):raise RuntimeError('Checkpoint upload was not fully confirmed')
 entry=entries[0];stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 import csv
 journal=root/'records/checkpoint_saves.tsv'
 with journal.open('a',newline='') as f:
  w=csv.writer(f,delimiter='\t')
  if journal.stat().st_size==0:w.writerow(['number','filename','saved_at_utc','library_file_id','status','local_metadata_applied'])
  w.writerow([d['number'],entry['file_name'],stamp,entry['library_file_id'],entry['status'],entry['local_metadata_applied']])
 with (root/'progress.log').open('a') as f:f.write(f"checkpoint {d['number']:02} saved {stamp} {entry['file_name']} {entry['library_file_id']}\n")
 print(json.dumps({'saved':True,'library_file_id':entry['library_file_id'],'filename':entry['file_name']}),flush=True)
raise SystemExit(u.returncode)
