"""Create a cumulative checkpoint when due, or the final ZIP on request."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import argparse,zipfile,json
OUT=Path(__file__).resolve().parents[1]
ROOT=OUT.parent
def utc():return datetime.now(timezone.utc)
def parse(s):return datetime.strptime(s,'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
p=argparse.ArgumentParser();p.add_argument('--final',action='store_true');args=p.parse_args()
start=parse((OUT/'progress.log').read_text().splitlines()[0])
index=(OUT/'checkpoint_index.tsv').read_text().splitlines()[1:]
last=parse(index[-1].split('\t')[1]) if index else start
now=utc()
if not args.final and now-last<timedelta(minutes=45):
 print(json.dumps({'due':False,'next_due':(last+timedelta(minutes=45)).isoformat()}));raise SystemExit
n=len(index)+1
name='SP43_CW_29+32.zip' if args.final else f'SP43_CW_29+32_checkpoint_{n:02}.zip'
dest=ROOT/'deliverables'/name;dest.parent.mkdir(exist_ok=True)
if dest.exists():raise RuntimeError('Never overwrite a checkpoint or final package')
files=sorted(x for x in OUT.rglob('*') if x.is_file() and x.suffix!='.zip' and '__pycache__' not in x.parts and x.name!='PREAMBLE.tex')
manifest='\n'.join(str(x.relative_to(OUT)) for x in files)+'\n'
(OUT/'PACKAGE_FILES.txt').write_text(manifest)
if OUT/'PACKAGE_FILES.txt' not in files:files.append(OUT/'PACKAGE_FILES.txt')
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.write(f,f.relative_to(OUT))
print(json.dumps({'due':True,'final':args.final,'number':n,'UTC':now.strftime('%Y-%m-%d %H:%M:%S UTC'),'file':str(dest),'bytes':dest.stat().st_size,'files':len(files)}))
