"""Package deliverables and reading evidence, never source scans or prior ZIPs."""
from pathlib import Path
import zipfile,sys
WORK=Path(__file__).resolve().parents[1]
dest=Path(sys.argv[1]).resolve()
assert dest.suffix=='.zip' and not dest.exists()
files=sorted(p for p in WORK.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip')
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,p.relative_to(WORK))
print(str(dest),dest.stat().st_size,'bytes',len(files),'files')
