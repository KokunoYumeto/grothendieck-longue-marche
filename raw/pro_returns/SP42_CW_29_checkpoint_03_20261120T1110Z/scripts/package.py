from pathlib import Path
from datetime import datetime,timezone
import sys,zipfile,hashlib,json
OUT=Path(__file__).resolve().parents[1];ROOT=OUT.parent
mode=sys.argv[1];now=datetime.now(timezone.utc)
if mode=='checkpoint':
 start=datetime.strptime((OUT/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
 prior=sorted(ROOT.glob('SP42_CW_29_checkpoint_*.zip'))
 index=len(prior)+1
 due=start.timestamp()+2700*index
 if now.timestamp()<due:raise SystemExit('Not due: checkpoints are only made at 45-minute intervals')
 name=f'SP42_CW_29_checkpoint_{index:02d}.zip'
 with (OUT/'progress.log').open('a') as f:f.write(f'checkpoint {index:02d} packaging {now:%Y-%m-%d %H:%M:%S UTC}; includes all current deliverables and documentation; earlier checkpoints: '+', '.join(p.name for p in prior)+'\n')
elif mode=='final':
 hashes=json.loads((OUT/'frozen_hashes.json').read_text())
 for rel,h in hashes.items():assert hashlib.sha256((OUT/rel).read_bytes()).hexdigest()==h,rel
 with (OUT/'progress.log').open('a') as f:f.write('frozen hashes unchanged '+now.strftime('%Y-%m-%d %H:%M:%S UTC')+'; verified all page files and combined transcription\n')
 name='SP42_CW_29.zip'
else:raise SystemExit('checkpoint or final required')
dest=ROOT/name
assert not dest.exists(),'Never overwrite a checkpoint or final package'
files=[]
for p in sorted(OUT.rglob('*')):
 if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts and p.name!='PACKAGE_CONTENTS.tsv':
  files.append(p)
manifest=['path\tbytes\tsha256\n']
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in files:
  # A reader may be writing an in-progress return at checkpoint time.
  # Hash and archive the same captured bytes, not two separate file reads.
  data=p.read_bytes();rel=str(p.relative_to(OUT))
  manifest.append(f'{rel}\t{len(data)}\t{hashlib.sha256(data).hexdigest()}\n')
  z.writestr(rel,data)
 contents=''.join(manifest)
 (OUT/'PACKAGE_CONTENTS.tsv').write_text(contents)
 z.writestr('PACKAGE_CONTENTS.tsv',contents)
print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'files':len(files),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
