"""Timed, nonblocking checkpoint monitor for this active transcription run.

It never creates an early checkpoint and never overwrites an existing ZIP.
The interactive exec session returns while this process waits in short intervals.
Final packaging or a stop marker terminates the monitor.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, io, json, subprocess, sys, time, zipfile

out=Path(__file__).resolve().parents[1]
root=out.parent
start=datetime.strptime((out/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
print('Timed checkpoint monitor started; anchored at '+start.isoformat(),flush=True)
while not (root/'SP42_CW_29.zip').exists() and not (root/'stop_checkpoint_monitor').exists():
    index=len(list(root.glob('SP42_CW_29_checkpoint_*.zip')))+1
    due=start.timestamp()+2700*index
    remaining=due-time.time()
    if remaining>0:
        time.sleep(min(30,remaining))
        continue
    run=subprocess.run([sys.executable,str(out/'scripts/checkpoint_upload.py')],capture_output=True,text=True)
    print(run.stdout,flush=True)
    if run.returncode:
        print('Checkpoint upload failed; review the saved error before retrying this same archive.',flush=True)
        sys.exit(run.returncode)
    receipt_path=root/f'checkpoint_{index:02d}_upload_result.json'
    receipt=json.loads(receipt_path.read_text())
    item=receipt['results'][0]
    if item.get('status')!='succeeded':
        print('Checkpoint was created but upload did not report success. The same ZIP must be retried.',flush=True)
        sys.exit(1)
    archive=root/f'SP42_CW_29_checkpoint_{index:02d}.zip'
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        manifest=list(csv.DictReader(io.StringIO(z.read('PACKAGE_CONTENTS.tsv').decode()),delimiter='\t'))
        for row in manifest:
            data=z.read(row['path'])
            assert len(data)==int(row['bytes'])
            assert hashlib.sha256(data).hexdigest()==row['sha256']
    now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    digest=hashlib.sha256(archive.read_bytes()).hexdigest()
    with (out/'progress.log').open('a') as f:
        f.write(f'checkpoint {index:02d} durably saved {now}; library_file_id={item["library_file_id"]}; SHA-256 {digest}; ZIP and all manifest entries verified\n')
    with (out/'upload_receipts.tsv').open('a') as f:
        f.write('\t'.join([archive.name,now,item.get('file_id',''),item['library_file_id'],digest])+'\n')
    print(json.dumps({'checkpoint':index,'saved_utc':now,'library_file_id':item['library_file_id'],'sha256':digest,'verified_entries':len(manifest)}),flush=True)
print('Timed checkpoint monitor stopped.',flush=True)
