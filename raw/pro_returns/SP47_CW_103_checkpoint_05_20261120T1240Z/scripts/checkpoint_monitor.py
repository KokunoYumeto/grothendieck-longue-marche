"""Keep active-run checkpoint deadlines across long tool calls/context transitions.

This process only runs during this transcription session. It creates no page-boundary
archives. Touch records/checkpoint_monitor.stop after final delivery to terminate it.
All durable writes use the official Library upload helper already obtained for this run.
"""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import subprocess,sys,time,json

R=Path(__file__).resolve().parents[1]
HELPER=R.parent/'library_helpers/library_upload.py'
STOP=R/'records/checkpoint_monitor.stop'
STATE=R/'records/checkpoint_monitor.json'
START=datetime.strptime((R/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
def stamp():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def state(**kw):STATE.write_text(json.dumps({'updated_utc':stamp(),**kw},indent=2))

while not STOP.exists():
 history=json.loads((R/'records/checkpoints.json').read_text())
 target=START+timedelta(seconds=2700*(len(history)+1))
 state(status='waiting',next_target_utc=target.strftime('%Y-%m-%d %H:%M:%S UTC'))
 while datetime.now(timezone.utc)<target and not STOP.exists():
  time.sleep(max(.01,min(5,(target-datetime.now(timezone.utc)).total_seconds())))
 if STOP.exists():break
 result=subprocess.run([sys.executable,str(R/'scripts/checkpoint.py')],text=True,capture_output=True)
 if result.returncode:state(status='checkpoint_error',output=result.stdout,error=result.stderr);raise SystemExit(result.returncode)
 info=json.loads(result.stdout.splitlines()[-1])
 if not info.get('checkpoint_due'):continue
 path=Path(info['path']);n=int(path.stem.rsplit('_',1)[1]);log=R/f'records/checkpoint_{n:02}_upload.log'
 state(status='uploading',checkpoint=path.name)
 while not STOP.exists():
  with log.open('w') as f:
   uploaded=subprocess.run([sys.executable,str(HELPER)],input=json.dumps({'uploads':[{'local_path':str(path),'purpose':'create_library_file','library_artifact_type':'other'}]}),text=True,stdout=f,stderr=subprocess.STDOUT)
  lines=log.read_text().splitlines()
  payload=next((json.loads(l) for l in reversed(lines) if l.startswith('{"results"')),None)
  ok=payload and payload['results'][0].get('status')=='succeeded'
  if ok:break
  state(status='upload_retry_pending',checkpoint=path.name,returncode=uploaded.returncode)
  for _ in range(12):
   if STOP.exists():break
   time.sleep(5)
 if not ok:break
 item=payload['results'][0]
 (R/f'records/checkpoint_{n:02}_upload_result.json').write_text(json.dumps(payload,indent=2))
 history=json.loads((R/'records/checkpoints.json').read_text())
 row=next(h for h in history if h['filename']==path.name)
 row.update(library_status='succeeded',library_file_id=item['library_file_id'],file_id=item['file_id'],bytes=info['size'],sha256=info['sha256'],scheduled_utc=target.strftime('%Y-%m-%d %H:%M:%S UTC'))
 (R/'records/checkpoints.json').write_text(json.dumps(history,indent=2))
 with (R/'progress.log').open('a') as f:f.write('checkpoint '+path.name+' upload succeeded '+stamp()+'; SHA256 '+info['sha256']+'\n')
 print(json.dumps({'checkpoint':path.name,'status':'saved','utc':stamp(),'sha256':info['sha256']}),flush=True)
state(status='stopped')
