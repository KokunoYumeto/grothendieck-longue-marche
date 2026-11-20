from pathlib import Path
from datetime import datetime,timezone
import json,sys,zipfile,hashlib,shutil
ED=Path(__file__).resolve().parents[1];ROOT=ED.parent
mode=sys.argv[1]
now=datetime.now(timezone.utc)
if mode=='checkpoint':
    state=json.loads((ROOT/'state.json').read_text())
    last=datetime.strptime(state.get('last_checkpoint',state['started']),'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    if (now-last).total_seconds()<2700:
        print(json.dumps({'due':False,'remaining_seconds':round(2700-(now-last).total_seconds())}));raise SystemExit
    index=state['next_checkpoint'];name=f'SP75_C13_145_checkpoint_{index:02d}.zip'
    state['last_checkpoint']=now.strftime('%Y-%m-%d %H:%M:%S UTC');state['next_checkpoint']=index+1
    (ROOT/'state.json').write_text(json.dumps(state,indent=2))
    with (ED/'progress.log').open('a') as f:f.write('checkpoint prepared '+name+' '+state['last_checkpoint']+'\n')
elif mode=='final':name='SP75_C13_145.zip'
else:raise SystemExit(mode)
dest=ROOT/'deliverables';dest.mkdir(exist_ok=True)
path=dest/name
if path.exists():raise SystemExit('Refusing to overwrite '+str(path))
shutil.copyfile(ROOT/'state.json',ED/'run_state.json')
for guide in ['reader_guidance.md','reader_output_instructions.md']:
    shutil.copyfile(ROOT/guide,ED/'scripts'/guide)
(ED/'FILE_LIST.txt').touch(exist_ok=True)
files=[p for p in sorted(ED.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith('.pyc')]
manifest='\n'.join(str(p.relative_to(ED)) for p in files)+'\n'
(ED/'FILE_LIST.txt').write_text(manifest)
files=[p for p in sorted(ED.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and not p.name.endswith('.pyc')]
with zipfile.ZipFile(path,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,p.relative_to(ED))
print(json.dumps({'due':True,'path':str(path),'files':len(files),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}))
