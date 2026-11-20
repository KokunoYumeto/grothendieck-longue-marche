#!/usr/bin/env python3
"""Maintain the requested checkpoint cadence during the active transcription run."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,time,sys
b=Path(__file__).resolve().parent.parent.parent;o=b/'out';w=b/'work'
stop=w/'stop_checkpoint_watch'
while not stop.exists():
    state=w/'checkpoint_state.json'
    if not state.exists() and (o/'records/checkpoint_schedule.json').exists():state=o/'records/checkpoint_schedule.json'
    if state.exists():last=datetime.fromisoformat(json.loads(state.read_text())['last'])
    else:last=datetime.strptime((o/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    remain=2700-(datetime.now(timezone.utc)-last).total_seconds()
    if remain>0:
        time.sleep(min(20,max(0.1,remain)));continue
    res=subprocess.run([sys.executable,str(o/'scripts/make_checkpoint.py')],capture_output=True,text=True)
    if res.returncode:
        (w/'checkpoint_failure.txt').write_text(res.stdout+'\n'+res.stderr);print('CHECKPOINT CREATION FAILED',flush=True);break
    record=json.loads(res.stdout)
    if not record.get('due'):continue
    path=record['file']
    upload=subprocess.run([sys.executable,str(w/'library_helpers/library_upload.py')],input=json.dumps({'uploads':[{'local_path':path,'purpose':'create_library_file','library_artifact_type':'other'}]}),capture_output=True,text=True)
    receipt=w/(Path(path).stem+'_upload_receipt.json');receipt.write_text(upload.stdout)
    (w/(Path(path).stem+'_upload_stderr.txt')).write_text(upload.stderr)
    public={'filename':Path(path).name,'size_bytes':record['size_bytes'],'sha256':record['sha256'],'receipt':receipt.name,'helper_exit_code':upload.returncode,'utc':datetime.now(timezone.utc).isoformat()}
    log=o/'records/checkpoint_deliveries.json';items=json.loads(log.read_text()) if log.exists() else [];items.append(public);log.write_text(json.dumps(items,indent=2))
    print(json.dumps(public),flush=True)
    if upload.returncode:
        (w/'checkpoint_failure.txt').write_text('Inspect '+str(receipt)+' and associated stderr before retrying.');break
print('Checkpoint watcher stopped.',flush=True)
