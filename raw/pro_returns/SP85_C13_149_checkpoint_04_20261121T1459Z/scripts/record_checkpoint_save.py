"""Record a successful bundled Library upload after verifying its local metadata."""
from pathlib import Path
import json,sys,hashlib,os,datetime
R=Path(__file__).resolve().parents[1];statepath=R/'records/next_steps.json';state=json.loads(statepath.read_text());name=state.get('checkpoint_pending_save');assert name,'No scheduled checkpoint is awaiting save'
p=R.parent/'deliverables'/name;receipt=json.loads(Path(sys.argv[1]).read_text())
ids=[]
def walk(x):
 if isinstance(x,dict):
  if x.get('library_file_id'):ids.append(x['library_file_id'])
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(receipt);ids=set(ids);assert len(ids)==1,ids
fileid=next(iter(ids));assert os.getxattr(p,'user.library-file-id').decode()==fileid
assert os.getxattr(p,'user.library-file-version')
meta=dict(name=name,library_file_id=fileid,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size)
assert not any(x['name']==name for x in state.get('checkpoints',[]))
state.setdefault('checkpoints',[]).append(meta);state.pop('checkpoint_pending_save');statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
with (R/'progress.log').open('a') as f:f.write('checkpoint saved '+datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+' '+name+' '+fileid+' sha256 '+meta['sha256']+'; bundled upload succeeded and both file metadata attributes verified\n')
print(json.dumps(meta))
