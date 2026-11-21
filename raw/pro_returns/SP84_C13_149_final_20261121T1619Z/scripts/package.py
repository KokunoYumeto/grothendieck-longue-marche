"""Package the current edition, never including inputs, halves or older ZIPs."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,zipfile

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT.parent/'deliveries'

def package(name):
    DEST.mkdir(exist_ok=True)
    p=DEST/name
    if p.exists():raise FileExistsError(f'Refusing to overwrite {p}')
    files=sorted(x for x in ROOT.rglob('*') if x.is_file() and x.suffix!='.zip' and '__pycache__' not in x.parts)
    with zipfile.ZipFile(p,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for f in files:z.write(f,f.relative_to(ROOT))
    print(json.dumps({'path':str(p),'bytes':p.stat().st_size,'files':len(files),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))

if __name__=='__main__':package(sys.argv[1])
