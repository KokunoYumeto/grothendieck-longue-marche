#!/usr/bin/env python3
"""Create the scheduled complete checkpoint ZIP (never includes source attachments)."""
from pathlib import Path
from datetime import datetime,timezone
import json,zipfile,sys
root=Path(__file__).resolve().parents[1]; meta=json.loads((root/'run_metadata.json').read_text())
now=datetime.now(timezone.utc);last=datetime.fromisoformat(meta.get('last_checkpoint_utc') or meta['start_utc'])
due=(now-last).total_seconds()>=2700
if not due:
    print(json.dumps({'due':False,'seconds_until_due':round(2700-(now-last).total_seconds())}));sys.exit()
num=meta['checkpoint_number']+1;name=f'SP37_CW_71_checkpoint_{num:02d}.zip'
dest=root.parent.parent/'deliverables'/name;dest.parent.mkdir(exist_ok=True)
if dest.exists():raise RuntimeError('Refuse overwrite of an earlier checkpoint')
meta['checkpoint_number']=num;meta['last_checkpoint_utc']=now.isoformat()
(root/'run_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
with (root/'progress.log').open('a') as f:f.write(f'checkpoint {num:02d} created {now.isoformat()} {name}\n')
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.suffix!='.zip':z.write(p,p.relative_to(root))
print(json.dumps({'due':True,'file':str(dest),'size':dest.stat().st_size}))
