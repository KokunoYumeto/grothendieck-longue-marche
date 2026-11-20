"""Package the current deliverables without images, inputs, caches or nested archives."""
from reading_support import *
import argparse
p=argparse.ArgumentParser();p.add_argument('--checkpoint',action='store_true');a=p.parse_args()
if a.checkpoint:
 due,minutes,number=checkpoint_due()
 if not due:raise SystemExit('Checkpoint not due')
 name=f'{PREFIX}_checkpoint_{number:02}.zip'
 log('checkpoint '+name+' snapshot started')
else:name=PREFIX+'.zip'
if a.checkpoint:
 assemble();build_changes()
else:
 # A final package must preserve the already frozen fragment bytes.
 hashes=ROOT/'transcription_hashes.sha256'
 if not hashes.exists():raise SystemExit('Freeze the transcription before final packaging')
 for line in hashes.read_text().splitlines():
  digest,relative=line.split('  ',1)
  if hashlib.sha256((ROOT/relative).read_bytes()).hexdigest()!=digest:raise SystemExit('Frozen hash changed: '+relative)
 log('final packaging: all frozen transcription hashes verified unchanged')
out=WORK/'deliverables';out.mkdir(exist_ok=True)
path=out/name
if path.exists():raise SystemExit('Refusing to overwrite '+str(path))
files=[q for q in sorted(ROOT.rglob('*')) if q.is_file() and '__pycache__' not in q.parts and q.suffix.lower() not in {'.pyc','.zip','.jpg','.jpeg','.png','.gif','.webp','.tiff','.tif','.bmp','.svg','.avif','.pdf'}]
manifest=ROOT/'package_file_list.txt'
files=sorted(set(files+[manifest]))
manifest.write_text('\n'.join(str(q.relative_to(ROOT)) for q in files)+'\n')
with zipfile.ZipFile(path,'x',zipfile.ZIP_DEFLATED) as z:
 for q in files:z.write(q,str(q.relative_to(ROOT)))
with zipfile.ZipFile(path) as z:
 if z.testzip() is not None:raise RuntimeError('ZIP CRC verification failed')
 if sorted(z.namelist())!=sorted(str(q.relative_to(ROOT)) for q in files):raise RuntimeError('ZIP file list mismatch')
 for q in files:
  if z.read(str(q.relative_to(ROOT)))!=q.read_bytes():raise RuntimeError('ZIP contents mismatch: '+str(q))
 if not a.checkpoint:
  for line in (ROOT/'transcription_hashes.sha256').read_text().splitlines():
   digest,relative=line.split('  ',1)
   if hashlib.sha256(z.read(relative)).hexdigest()!=digest:raise RuntimeError('Frozen ZIP transcription differs: '+relative)
print(path)
print('Files:',len(files))
print('ZIP contents and frozen transcription hashes verified unchanged.' if not a.checkpoint else 'ZIP contents verified.')
