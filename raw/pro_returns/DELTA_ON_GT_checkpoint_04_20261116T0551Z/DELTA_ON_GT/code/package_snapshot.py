"""Create a non-overwriting checkpoint or final ZIP; do not include supplied inputs."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,zipfile,json,hashlib,shutil
p=argparse.ArgumentParser();p.add_argument('name');p.add_argument('--include-history',action='store_true');a=p.parse_args()
r=Path(__file__).resolve().parents[1]
# Retain executable copies under code while preserving original audit modules.
for module in ['agent_five','agent_literature','agent_lifting']:
    for f in (r/module).rglob('*'):
        if f.is_file() and f.suffix in ['.py','.out','.json'] and '__pycache__' not in f.parts:
            dest=r/'code'/module/f.relative_to(r/module);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,dest)
excluded=[];files=[]
for f in r.rglob('*'):
    if not f.is_file():continue
    rel=f.relative_to(r)
    third_party=(f.name.startswith('drinfeld') or
                 (f.name.startswith('ihara_RIMS1224') and f.suffix in ['.pdf','.ps','.txt']) or
                 f.name in ['schneps_automorphisms.pdf','schneps_657.png'] or
                 (f.name.startswith('furusho_') and f.suffix in ['.pdf','.png','.txt']) or
                 (f.name.lower().startswith('petrov') and f.suffix in ['.pdf','.png','.txt']))
    omit_zip=f.suffix=='.zip' and not (a.include_history and rel.parts[0]=='history')
    if '__pycache__' in f.parts or third_party or omit_zip:
        excluded.append(str(rel));continue
    files.append(f)
record={'created_utc':datetime.now(timezone.utc).isoformat(),'name':a.name,'files':len(files),'omissions':excluded,'reason':'Bytecode and third-party source PDF/OCR/images are not deliverables; verified source URLs and loci remain. Supplied background is outside this directory.'}
(r/'records'/'latest_packaging.json').write_text(json.dumps(record,indent=2)+'\n')
if r/'records'/'latest_packaging.json' not in files:files.append(r/'records'/'latest_packaging.json')
out=r.parent/(a.name+'.zip')
if out.exists():raise SystemExit('Refusing to overwrite '+str(out))
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=7) as z:
    for f in sorted(files):z.write(f,Path('DELTA_ON_GT')/f.relative_to(r))
print(json.dumps({'path':str(out),'size':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'files':len(files)}))
