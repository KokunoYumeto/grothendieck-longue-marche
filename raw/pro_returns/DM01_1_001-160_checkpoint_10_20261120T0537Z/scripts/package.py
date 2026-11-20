#!/usr/bin/env python3
"""Create complete, non-nested checkpoint or final ZIPs. No reading inference."""
import argparse,csv,datetime as dt,fcntl,hashlib,json,re,shutil,subprocess,sys,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'deliverable'
UTC=dt.timezone.utc
FMT='%Y-%m-%d %H:%M:%S UTC'
def now(): return dt.datetime.now(UTC)
def parse(t): return dt.datetime.strptime(t,FMT).replace(tzinfo=UTC)
def checkpoints():
 p=OUT/'audit/checkpoints.tsv'
 return list(csv.DictReader(p.open(),delimiter='\t')) if p.exists() else []
def write_history(history):
 p=OUT/'audit/checkpoints.tsv'
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['number','filename','created_utc','sha256'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(history)
def status():
 start=parse((OUT/'progress.log').read_text().splitlines()[0]); history=checkpoints()
 previous=parse(history[-1]['created_utc']) if history else start
 due=previous+dt.timedelta(minutes=45)
 return {'start_utc':start.strftime(FMT),'previous_utc':previous.strftime(FMT),'next_due_utc':due.strftime(FMT),'due':now()>=due,'seconds_to_due':round((due-now()).total_seconds()),'next_number':len(history)+1}
def capture_pending(label):
 """Keep complete current-page submissions; do not promote them to decisions."""
 committed={int(p.stem.removeprefix('scan')) for p in (OUT/'audit/receipts').glob('scan*.json')}
 captured=[]
 for path in sorted((ROOT/'work').glob('*')):
  if not path.is_file() or path.suffix not in {'.json','.py','.md','.tsv','.log'}:continue
  match=re.search(r'(?:^|_)scan(\d+)',path.name)
  if not match:continue
  if path.suffix=='.json' and int(match.group(1)) in committed:continue
  try:
   data=path.read_bytes()
   if path.suffix=='.json':json.loads(data)
  except (ValueError,OSError):continue
  target=OUT/'audit/checkpoint_drafts'/label/path.name
  target.parent.mkdir(parents=True,exist_ok=True)
  if target.exists():raise RuntimeError('Refusing to overwrite draft snapshot '+str(target))
  target.write_bytes(data)
  captured.append({'source':str(path.relative_to(ROOT)),'archive_path':str(target.relative_to(OUT)),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'status':'uncommitted snapshot' if int(match.group(1)) not in committed else 'reader script'})
 if captured:
  target=OUT/'audit/checkpoint_drafts'/label/'MANIFEST.tsv'
  with target.open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(captured[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(captured)
 return len(captured)
def build(final=False):
 s=status()
 if not final and not s['due']: return s
 cmd=[sys.executable,str(OUT/'scripts/reconcile.py'),'verify']
 if final: cmd+=['--final']
 result=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
 if result.returncode: raise RuntimeError(result.stdout+result.stderr)
 stamp=now().strftime(FMT)
 pending_count=capture_pending('final' if final else f"{s['next_number']:02}")
 name='DM01_1_001-160.zip' if final else f"DM01_1_001-160_checkpoint_{s['next_number']:02}.zip"
 destination=ROOT/name
 if destination.exists(): raise RuntimeError('Refusing to overwrite '+str(destination))
 if not final:
  history=checkpoints()
  history.append({'number':str(s['next_number']),'filename':name,'created_utc':stamp,'sha256':''})
  write_history(history)
 included=sorted(p for p in OUT.rglob('*') if p.is_file() and p.suffix not in {'.zip','.pyc'} and '__pycache__' not in p.parts and not p.name.endswith('.tmp'))
 with zipfile.ZipFile(destination,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in included: z.write(p,p.relative_to(OUT))
 receipt={'file':str(destination),'filename':name,'created_utc':stamp,'size_bytes':destination.stat().st_size,'sha256':hashlib.sha256(destination.read_bytes()).hexdigest(),'file_count':len(included),'pending_snapshots':pending_count,'kind':'final' if final else 'checkpoint','number':s['next_number'] if not final else ''}
 if not final:
  history[-1]['sha256']=receipt['sha256']
  write_history(history)
 (ROOT/'work/latest_package.json').write_text(json.dumps(receipt,indent=2)+'\n')
 return receipt
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('action',choices=['status','checkpoint','final']);args=parser.parse_args()
 with (ROOT/'work/reconcile.lock').open('a') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX)
  print(json.dumps(status() if args.action=='status' else build(args.action=='final'),ensure_ascii=False))
