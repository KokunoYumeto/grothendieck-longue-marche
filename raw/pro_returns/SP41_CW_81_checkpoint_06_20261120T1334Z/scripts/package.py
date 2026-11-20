from pathlib import Path
from datetime import datetime,timezone
import zipfile,sys,hashlib,json
root=Path(__file__).resolve().parents[2];w=root/'work';out=root/'deliveries';out.mkdir(exist_ok=True)
name=sys.argv[1]
if Path(name).name!=name or not name.endswith('.zip'):raise SystemExit('Expected archive basename')
target=out/name
if target.exists():raise SystemExit('Refusing to overwrite archive')
files=sorted(p for p in w.rglob('*') if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts)
manifest={'archive':name,'created_utc':datetime.now(timezone.utc).isoformat(),'files':[]}
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:
        data=p.read_bytes();rel=str(p.relative_to(w))
        manifest['files'].append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        z.writestr(rel,data)
    z.writestr('ARCHIVE_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps({'path':str(target),'bytes':target.stat().st_size,'files':len(files),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}))
