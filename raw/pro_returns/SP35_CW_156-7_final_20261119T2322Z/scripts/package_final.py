#!/usr/bin/env python3
"""Package all deliverables and work documentation, excluding input attachments."""
from pathlib import Path
import argparse,hashlib,json,zipfile
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('destination');a=p.parse_args()
out=Path(a.destination).resolve()
if out.name!='SP35_CW_156-7.zip':raise SystemExit('Final ZIP must be named SP35_CW_156-7.zip')
if out.exists():raise SystemExit('Refusing to overwrite an existing final ZIP')
frozen=json.loads((root/'records/frozen_sha256.json').read_text())
for name,sha in frozen['files'].items():
 if hashlib.sha256((root/name).read_bytes()).hexdigest()!=sha:raise SystemExit('Frozen text changed: '+name)
files=[f for f in sorted(root.rglob('*')) if f.is_file() and f.suffix.lower()!='.zip' and '__pycache__' not in f.parts]
if any(f.relative_to(root).parts[0] in {'source','upload'} for f in files):raise SystemExit('Input attachment tree must not be packaged')
out.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.write(f,str(f.relative_to(root)))
with zipfile.ZipFile(out) as z:
 bad=z.testzip()
 if bad:raise SystemExit('ZIP integrity failure: '+bad)
 for name,sha in frozen['files'].items():
  if hashlib.sha256(z.read(name)).hexdigest()!=sha:raise SystemExit('Archived frozen text differs: '+name)
 if any(n.lower().endswith('.zip') for n in z.namelist()):raise SystemExit('Nested ZIP found')
result={'path':str(out),'bytes':out.stat().st_size,'files':len(files),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'zip_integrity':'verified','frozen_page_and_combined_hashes':'all nine verified inside final archive'}
print(json.dumps(result,indent=2))
