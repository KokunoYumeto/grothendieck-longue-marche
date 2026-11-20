"""Package deliverables/documentation, never original inputs or earlier ZIPs."""
from pathlib import Path
import argparse,datetime,zipfile,hashlib,csv
W=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--checkpoint',action='store_true');a=p.parse_args()
now=datetime.datetime.now(datetime.timezone.utc)
if a.checkpoint:
 history=W/'checkpoint_history.tsv';previous=[]
 if history.exists():
  with history.open(newline='') as f: previous=list(csv.DictReader(f,delimiter='\t'))
 last=previous[-1]['packaged_utc'] if previous else (W/'progress.log').read_text().splitlines()[0]
 last=datetime.datetime.fromisoformat(last.replace('Z','+00:00'))
 assert (now-last).total_seconds()>=2700,'No checkpoint before 45 minutes have elapsed'
 name=f'IM03_9-12_checkpoint_{len(previous)+1:02}.zip';out=W.parent/name
 assert not out.exists(),'Never overwrite a checkpoint'
 with history.open('a',newline='') as f:
  wr=csv.writer(f,delimiter='\t',lineterminator='\n')
  if not previous: wr.writerow(['filename','packaged_utc'])
  wr.writerow([name,now.strftime('%Y-%m-%dT%H:%M:%SZ')])
else: out=W.parent/'IM03_9-12.zip'
files=[]
for path in sorted(W.rglob('*')):
 if not path.is_file(): continue
 rel=path.relative_to(W)
 if rel.parts[0]=='source' or '__pycache__' in rel.parts or path.suffix=='.zip': continue
 if rel.parts[0]=='reviews' and path.name=='rows.tsv': continue
 files.append(path)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for path in files: z.write(path,path.relative_to(W))
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
 assert all(not x.startswith('source/') and not x.endswith('.zip') for x in z.namelist())
print(out)
print('files',len(files),'bytes',out.stat().st_size,'sha256',hashlib.sha256(out.read_bytes()).hexdigest())
