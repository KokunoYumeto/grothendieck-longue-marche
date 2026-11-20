"""Package all current deliverables/documentation only at 45-minute intervals."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import zipfile,json,argparse
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'out'
NAME='SP57_CW_97+123+162-1+162-6'
p=argparse.ArgumentParser();p.add_argument('--final',action='store_true');a=p.parse_args()
now=datetime.now(timezone.utc)
start=datetime.strptime((OUT/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
state=ROOT/'checkpoint_state.json'
data=json.loads(state.read_text()) if state.exists() else {'saved':[]}
nextnum=len(data['saved'])+1
due=start+timedelta(minutes=45*nextnum)
if not a.final and now<due:
 print(json.dumps({'due':False,'next_due':due.isoformat(),'now':now.isoformat()}));raise SystemExit
dest=ROOT/'deliverables';dest.mkdir(exist_ok=True)
filename=NAME+'.zip' if a.final else NAME+f'_checkpoint_{nextnum:02d}.zip'
path=dest/filename
assert not path.exists(),str(path)
paths=sorted(f for f in OUT.rglob('*') if f.is_file() and f.suffix!='.zip' and '__pycache__' not in f.parts)
manifest='\n'.join(str(f.relative_to(OUT)) for f in paths)+'\n'
(OUT/'checkpoint_file_list.txt').write_text(manifest)
with (OUT/'progress.log').open('a') as f:
 f.write(('final package ' if a.final else 'checkpoint package ')+filename+' '+now.strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
with zipfile.ZipFile(path,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in paths:z.write(f,f.relative_to(OUT))
 if not any(f.name=='checkpoint_file_list.txt' for f in paths):z.write(OUT/'checkpoint_file_list.txt','checkpoint_file_list.txt')
if not a.final:
 data['saved'].append({'name':filename,'path':str(path),'created':now.isoformat(),'library_status':'pending'})
 state.write_text(json.dumps(data,indent=2))
print(json.dumps({'due':True,'path':str(path),'bytes':path.stat().st_size,'files':len(paths)}))
