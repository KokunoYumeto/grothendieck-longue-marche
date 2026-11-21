"""Package work, excluding inputs, regenerable halves and earlier ZIPs."""
from pathlib import Path
import zipfile,sys,hashlib,datetime,json
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT.parent/'deliverables';DEST.mkdir(exist_ok=True)
name=sys.argv[1] if len(sys.argv)>1 else 'SP85_C13_149.zip'
assert name.endswith('.zip') and '/' not in name
path=DEST/name
assert not path.exists(),f'Refusing to overwrite an existing ZIP: {path}'
files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts and p.suffix!='.pyc']
with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for f in files:z.write(f,f.relative_to(ROOT))
with zipfile.ZipFile(path) as z:assert z.testzip() is None
print(json.dumps({'path':str(path),'bytes':path.stat().st_size,'members':len(files),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}))
