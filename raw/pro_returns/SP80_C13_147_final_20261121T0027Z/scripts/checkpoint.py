"""Package work and evidence; omit supplied sources, native halves and older ZIPs."""
from pathlib import Path
from datetime import datetime,timezone
import sys,zipfile,hashlib
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
name=sys.argv[1]
dest=BASE/'deliverables'/name;dest.parent.mkdir(exist_ok=True)
if dest.exists():raise RuntimeError('Never overwrite an existing checkpoint or final ZIP')
files=[p for p in ROOT.rglob('*') if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(files):z.write(p,p.relative_to(ROOT))
with zipfile.ZipFile(dest) as z:
    bad=z.testzip()
    if bad:raise RuntimeError(bad)
print(dest)
print('files',len(files),'bytes',dest.stat().st_size,'sha256',hashlib.sha256(dest.read_bytes()).hexdigest())
