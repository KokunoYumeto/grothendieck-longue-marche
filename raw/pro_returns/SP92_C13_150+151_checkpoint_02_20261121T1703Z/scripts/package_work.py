"""Create the final ZIP or a scheduled checkpoint; exclude source attachments and halves."""
from pathlib import Path
import zipfile,sys,datetime,json
R=Path(__file__).resolve().parents[1]
base=R.parent
mode=sys.argv[1] if len(sys.argv)>1 else 'final'
now=datetime.datetime.now(datetime.timezone.utc)
dest=base/'deliverables';dest.mkdir(exist_ok=True)
if mode=='checkpoint':
    log=R/'CHECKPOINTS.tsv'
    entries=log.read_text().splitlines()[1:] if log.exists() else []
    if entries:
        last=datetime.datetime.fromisoformat(entries[-1].split('\t')[1])
    else:
        last=datetime.datetime.strptime((R/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=datetime.timezone.utc)
    if (now-last).total_seconds()<2700:
        print(json.dumps({'due':False,'minutes_until_due':round((2700-(now-last).total_seconds())/60,2)}));sys.exit(0)
    n=len(entries)+1
    name=f'SP92_C13_150+151_checkpoint_{n:02}.zip'
    if not log.exists():log.write_text('filename\tcreated_utc\tlibrary_file_id\n')
    with log.open('a') as f:f.write(f'{name}\t{now.isoformat()}\tpending upload\n')
else:
    name='SP92_C13_150+151.zip'
out=dest/name
if out.exists():raise SystemExit('Refusing to overwrite an existing package: '+str(out))
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip' and not p.name.endswith('.tmp')]
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(files):z.write(p,p.relative_to(R))
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
print(json.dumps({'path':str(out),'files':len(files),'bytes':out.stat().st_size,'mode':mode}))
