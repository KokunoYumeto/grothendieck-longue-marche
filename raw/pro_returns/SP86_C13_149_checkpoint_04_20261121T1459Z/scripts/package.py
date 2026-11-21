from pathlib import Path
import zipfile,json,sys,hashlib
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]
def package(name):
 dest=ROOT/'deliverables'/name;dest.parent.mkdir(exist_ok=True)
 if dest.exists():raise FileExistsError(dest)
 files=[p for p in sorted(BASE.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
 with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in files:z.write(p,p.relative_to(BASE))
 with zipfile.ZipFile(dest) as z:
  bad=z.testzip()
  if bad:raise ValueError(bad)
 return {'path':str(dest),'bytes':dest.stat().st_size,'entries':len(files),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
if __name__=='__main__':print(json.dumps(package(sys.argv[1])))
