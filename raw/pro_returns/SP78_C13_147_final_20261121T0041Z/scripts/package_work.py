#!/usr/bin/env python3
"""Make a full checkpoint or final archive, excluding replaceable inputs/halves."""
from pathlib import Path
from datetime import datetime,timezone
import zipfile,sys,json,hashlib
root=Path(__file__).resolve().parents[1]
name=sys.argv[1]
dest=root.parent/'deliverables'/name
dest.parent.mkdir(exist_ok=True)
assert not dest.exists(),f'Refusing to overwrite {dest}'
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts:
            z.write(p,p.relative_to(root))
print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'time':datetime.now(timezone.utc).isoformat()}))
