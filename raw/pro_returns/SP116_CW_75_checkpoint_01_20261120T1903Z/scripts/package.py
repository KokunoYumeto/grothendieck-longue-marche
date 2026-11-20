"""Package current deliverables and evidence, without inputs or older archives."""
from pathlib import Path
import zipfile, sys, datetime, json
root=Path(__file__).resolve().parents[1]
out=root.parent/'output';out.mkdir(exist_ok=True)
name=sys.argv[1] if len(sys.argv)>1 else 'SP116_CW_75.zip'
target=out/name
if target.exists():raise SystemExit(f'Refusing to overwrite existing archive: {target}')
files=[p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.zip','.pyc'}]
with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(files):z.write(p,p.relative_to(root))
with zipfile.ZipFile(target) as z:
    bad=z.testzip()
    if bad:raise SystemExit('Archive check failed: '+bad)
print(json.dumps({'file':str(target),'files':len(files),'bytes':target.stat().st_size,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}))
