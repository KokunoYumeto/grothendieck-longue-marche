"""Timed immutable checkpoint: each ZIP member and manifest hash use the same bytes."""
from pathlib import Path
import zipfile,datetime,sys,json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'out';DEST=ROOT/'deliverables';DEST.mkdir(exist_ok=True)
num=int(sys.argv[1]);name=f'SP36_CW_71_checkpoint_{num:02d}.zip';dest=DEST/name
if dest.exists():raise SystemExit('Checkpoint exists; never overwrite.')
now=datetime.datetime.now(datetime.timezone.utc)
with (OUT/'progress.log').open('a') as f:f.write('checkpoint '+name+' assembled '+now.strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
lists=OUT/'checkpoint_file_lists';lists.mkdir(exist_ok=True);listing=lists/f'checkpoint_{num:02d}.tsv'
if listing.exists():raise SystemExit('Checkpoint manifest exists; never overwrite.')
files=[p for p in sorted(OUT.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts and p!=listing]
rows=['relative_path\tbytes\tsha256']; count=0
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in files:
  # Re-read only if the file changed while being captured; never pause the readers.
  for attempt in range(4):
   before=p.stat();data=p.read_bytes();after=p.stat()
   if before.st_mtime_ns==after.st_mtime_ns and before.st_size==after.st_size==len(data):break
  else:raise RuntimeError('File changing during snapshot: '+str(p))
  rel=str(p.relative_to(OUT));z.writestr(rel,data);count+=1
  rows.append(rel+'\t'+str(len(data))+'\t'+hashlib.sha256(data).hexdigest())
 manifest='\n'.join(rows)+'\n';listing.write_text(manifest);z.writestr(str(listing.relative_to(OUT)),manifest);count+=1
with zipfile.ZipFile(dest) as z:
 for row in rows[1:]:
  rel,size,sha=row.split('\t');data=z.read(rel)
  if len(data)!=int(size) or hashlib.sha256(data).hexdigest()!=sha:raise RuntimeError('Checkpoint member mismatch: '+rel)
print(json.dumps({'path':str(dest),'files':count,'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'utc':now.isoformat(),'manifest_verified':True}))
