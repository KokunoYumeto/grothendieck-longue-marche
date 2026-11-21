from pathlib import Path
import zipfile,datetime,re,sys,hashlib
W=Path(__file__).resolve().parents[1];R=W.parent;P='SP89_C13_149+150'
final='--final' in sys.argv
D=R/'deliverables';D.mkdir(exist_ok=True)
existing=sorted(D.glob(P+'_checkpoint_*.zip'))
n=len(existing)+1
name=P+'.zip' if final else f'{P}_checkpoint_{n:02d}.zip'
out=D/name
if out.exists():raise RuntimeError('Never overwrite an archive')
tmp=D/(name+'.partial')
if tmp.exists():raise RuntimeError('Investigate incomplete archive before retrying: '+str(tmp))
manifest=W/'MANIFEST.tsv'
files=[p for p in W.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip' and p!=manifest]
entries=['path\tbytes\tsha256\n']
with zipfile.ZipFile(tmp,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(files):
  for attempt in range(4):
   before=p.stat();data=p.read_bytes();after=p.stat()
   if (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns) and len(data)==after.st_size:break
  else:raise RuntimeError('File was changing during snapshot: '+str(p))
  name=str(p.relative_to(W))
  z.writestr(name,data)
  entries.append(f'{name}\t{len(data)}\t{hashlib.sha256(data).hexdigest()}\n')
 manifest_data=''.join(entries)
 z.writestr('MANIFEST.tsv',manifest_data)
tmp.rename(out)
manifest.write_text(manifest_data)
print(out, out.stat().st_size, 'bytes',len(files)+1,'files')
