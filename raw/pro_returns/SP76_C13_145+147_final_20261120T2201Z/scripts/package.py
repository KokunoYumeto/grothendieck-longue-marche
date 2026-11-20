from pathlib import Path
from datetime import datetime,timezone
from zipfile import ZipFile,ZIP_DEFLATED
import sys,json
W=Path(__file__).resolve().parents[1]
mode=sys.argv[1] if len(sys.argv)>1 else 'status'
start=datetime.strptime((W/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
now=datetime.now(timezone.utc)
saved=list(W.parent.glob('deliverables/SP76_C13_145+147_checkpoint_*.zip'))
elapsed=(now-start).total_seconds()
due=int(elapsed//2700)>len(saved)
if mode=='status':
    print(json.dumps({'elapsed_minutes':round(elapsed/60,1),'checkpoints_created':len(saved),'checkpoint_due':due}));raise SystemExit
dest=W.parent/'deliverables';dest.mkdir(exist_ok=True)
if mode=='checkpoint':
    if not due: raise SystemExit('Checkpoint not due: 45-minute interval not reached.')
    filename=f'SP76_C13_145+147_checkpoint_{len(saved)+1:02d}.zip'
elif mode=='final': filename='SP76_C13_145+147.zip'
else: raise SystemExit('mode must be status, checkpoint, or final')
out=dest/filename
if out.exists(): raise SystemExit('Refusing to overwrite existing ZIP')
files=[p for p in W.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ['.zip','.pyc']]
with ZipFile(out,'w',ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(files): z.write(p,p.relative_to(W))
print(json.dumps({'path':str(out),'size_bytes':out.stat().st_size,'members':len(files)},ensure_ascii=False))
