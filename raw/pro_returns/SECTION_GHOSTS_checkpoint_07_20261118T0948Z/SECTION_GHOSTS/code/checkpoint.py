#!/usr/bin/env python3
"""Create a complete, immutable-name checkpoint package, excluding inputs and intermediates."""
from pathlib import Path
import csv,hashlib,io,sys,zipfile,datetime
p=Path(__file__).resolve().parents[1];n=int(sys.argv[1]);name=f'SECTION_GHOSTS_checkpoint_{n:02}.zip';out=p.parent/name
if out.exists():raise SystemExit('Refusing to overwrite an existing checkpoint')
files=[f for f in sorted(p.rglob('*')) if f.is_file() and 'build' not in f.relative_to(p).parts and '__pycache__' not in f.parts and f.suffix not in ['.zip','.pyc']]
buf=io.StringIO();w=csv.writer(buf,delimiter='\t');w.writerow(['path','bytes','sha256','contained_in'])
for f in files:
 w.writerow([str(f.relative_to(p)),f.stat().st_size,hashlib.sha256(f.read_bytes()).hexdigest(),name])
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for f in files:z.write(f,arcname='SECTION_GHOSTS/'+str(f.relative_to(p)))
 z.writestr('SECTION_GHOSTS/FILE_LIST.tsv',buf.getvalue())
assert out.stat().st_size<500_000_000
with zipfile.ZipFile(out) as z:assert z.testzip() is None
print('Created:',out);print('Files:',len(files)+1);print('Bytes:',out.stat().st_size);print('SHA256:',hashlib.sha256(out.read_bytes()).hexdigest())
print('Upload success must be recorded separately; creation alone does not persist the checkpoint.')
