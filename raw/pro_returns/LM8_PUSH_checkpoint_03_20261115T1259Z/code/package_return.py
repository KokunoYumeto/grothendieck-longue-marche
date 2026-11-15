#!/usr/bin/env python3
"""Create a fresh, immutable hourly checkpoint or final ZIP.

Usage: python code/package_return.py checkpoint 01
       python code/package_return.py final
The command refuses to overwrite any existing archive.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,zipfile
root=Path(__file__).resolve().parents[1]
mode=sys.argv[1]
if mode=='checkpoint':
    serial=f'{int(sys.argv[2]):02d}'
    name=f'LM8_PUSH_checkpoint_{serial}.zip'
elif mode=='final':name='LM8_PUSH.zip'
else:raise SystemExit('mode must be checkpoint or final')
dest=root.parent/name
if dest.exists():raise SystemExit('Refusing to overwrite '+str(dest))
excluded=('build/tex-cache/','__pycache__/')
files=[]
for p in sorted(root.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(root).as_posix()
    if any(rel.startswith(x) or ('/'+x) in rel for x in excluded):continue
    if p.suffix=='.pyc':continue
    files.append((p,rel))
manifest={'created_utc':datetime.now(timezone.utc).isoformat(),
          'kind':mode,'file_count':len(files),'files':[
    {'path':rel,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    for p,rel in files],
    'exclusions':['User-supplied background archive and extracted sources',
                  'Reproducible local TeX installation and font cache; installation script and checksums retained']}
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p,rel in files:z.write(p,rel)
    z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
    z.write(root.parent/'upload'/'PROMPT(1).md','inputs/PROMPT.md')
    if mode=='final':
        for checkpoint in sorted(root.parent.glob('LM8_PUSH_checkpoint_*.zip')):
            z.write(checkpoint,'checkpoint_history/'+checkpoint.name)
with zipfile.ZipFile(dest) as z:
    bad=z.testzip()
    if bad:raise RuntimeError('ZIP CRC failure: '+bad)
print(json.dumps({'file':str(dest),'bytes':dest.stat().st_size,
                  'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
                  'files':len(files)},indent=2))
