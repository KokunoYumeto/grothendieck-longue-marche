from pathlib import Path
import zipfile,json,sys
from datetime import datetime,timezone,timedelta
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'out'
PREFIX='SP14_CW_13+15+26+35+48+66+97+123+162'
start=datetime(2026,11,19,4,4,7,tzinfo=timezone.utc)
n=int(sys.argv[1]);now=datetime.now(timezone.utc)
assert now>=start+timedelta(minutes=45*n),'Not yet due; do not create an early checkpoint.'
p=ROOT/'checkpoints'/f'{PREFIX}_checkpoint_{n:02d}.zip';p.parent.mkdir(exist_ok=True)
assert not p.exists(),'Never overwrite a checkpoint.'
pages=sorted((OUT/'pages').glob('*.tex'))
with (OUT/'progress.log').open('a') as f:f.write(f'checkpoint {n:02d} packaging {now.strftime("%Y-%m-%d %H:%M:%S UTC")} with {len(pages)} collated pages; scheduled interval {45*n} minutes\n')
files=[x for x in OUT.rglob('*') if x.is_file() and '__pycache__' not in x.parts and x.suffix!='.zip']
(OUT/'checkpoint_contents.txt').write_text('\n'.join(str(x.relative_to(OUT)) for x in files)+'\ncheckpoint_contents.txt\n')
with zipfile.ZipFile(p,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for x in files:z.write(x,x.relative_to(OUT))
 if OUT/'checkpoint_contents.txt' not in files:z.write(OUT/'checkpoint_contents.txt','checkpoint_contents.txt')
print(json.dumps({'path':str(p),'bytes':p.stat().st_size,'collated_pages':len(pages),'checkpoint':n}))
