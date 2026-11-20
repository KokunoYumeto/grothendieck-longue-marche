"""Record a successfully persisted checkpoint; call only after a Library success."""
from pathlib import Path
from datetime import datetime,timezone
import json,argparse,hashlib
W=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('archive');p.add_argument('library_file_id');a=p.parse_args()
archive=Path(a.archive).resolve();state=json.loads((W/'state.json').read_text())
num=int(archive.stem.rsplit('_',1)[1]);assert num==state['checkpoint_number']+1
assert a.library_file_id.startswith('libfile_')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
receipt={'number':num,'filename':archive.name,'library_file_id':a.library_file_id,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'saved_utc':now,'completed_scans':state['done']}
rp=W/'records/checkpoint_receipts.json';rr=json.loads(rp.read_text()) if rp.exists() else []
assert all(x['number']!=num for x in rr);rr.append(receipt);rp.write_text(json.dumps(rr,indent=2))
state['checkpoint_number']=num;state['last_checkpoint_utc']=now;(W/'state.json').write_text(json.dumps(state,indent=2))
with (W/'progress.log').open('a') as f:f.write(f'checkpoint {num:02} saved {now}; {archive.name}; sha256 {receipt["sha256"]}; {a.library_file_id}\n')
print(json.dumps(receipt))
