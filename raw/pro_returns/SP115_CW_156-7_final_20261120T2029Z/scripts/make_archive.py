#!/usr/bin/env python3
"""Package current deliverables, excluding supplied inputs and older archives."""
from pathlib import Path
import argparse,datetime,hashlib,json,zipfile
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('destination',type=Path);args=p.parse_args()
if args.destination.exists():raise SystemExit('Refusing to overwrite an existing archive')
files=[x for x in sorted(root.rglob('*')) if x.is_file() and x.suffix!='.zip' and '__pycache__' not in x.parts]
snapshots={x:x.read_bytes() for x in files}
manifest={'created_utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'files':[{'path':str(x.relative_to(root)),'bytes':len(snapshots[x]),'sha256':hashlib.sha256(snapshots[x]).hexdigest()} for x in files]}
args.destination.parent.mkdir(exist_ok=True,parents=True)
with zipfile.ZipFile(args.destination,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.writestr(str(f.relative_to(root)),snapshots[f])
 z.writestr('ARCHIVE_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(args.destination) as z:
 bad=z.testzip()
 if bad:raise SystemExit('CRC failure: '+bad)
print(json.dumps({'archive':str(args.destination.resolve()),'files':len(files)+1,'bytes':args.destination.stat().st_size,'sha256':hashlib.sha256(args.destination.read_bytes()).hexdigest(),'crc':'passed'}))
