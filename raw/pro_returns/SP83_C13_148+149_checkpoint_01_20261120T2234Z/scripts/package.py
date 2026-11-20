"""Package deliverables and documentation; exclude inputs, halves and old ZIPs."""
from pathlib import Path
import zipfile,sys,json
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'result'
ID='SP83_C13_148+149'
suffix=sys.argv[1] if len(sys.argv)>1 else 'final'
name=f'{ID}.zip' if suffix=='final' else f'{ID}_checkpoint_{int(suffix):02}.zip'
dest=ROOT/'deliverables'/name;dest.parent.mkdir(exist_ok=True)
if dest.exists():raise FileExistsError('Archive names are immutable: '+str(dest))
files=[]
with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(OUT.rglob('*')):
        if not p.is_file() or '__pycache__' in p.parts or p.suffix=='.zip':continue
        arc=str(p.relative_to(OUT));z.write(p,arc);files.append(arc)
    for p in sorted((ROOT/'proposed').glob('*')):
        if p.is_file() and p.suffix!='.zip':
            arc='work/proposed/'+p.name;z.write(p,arc);files.append(arc)
    z.writestr('ARCHIVE_CONTENTS.txt','\n'.join(files)+'\n')
print(json.dumps({'path':str(dest),'size':dest.stat().st_size,'files':len(files),'time':datetime.now(timezone.utc).isoformat()}))
