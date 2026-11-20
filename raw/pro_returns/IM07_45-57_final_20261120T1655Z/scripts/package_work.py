#!/usr/bin/env python3
"""Package all current deliverables/documentation, never input or prior ZIPs."""
import argparse,csv,hashlib,json
from pathlib import Path
from datetime import datetime,timezone
from zipfile import ZipFile,ZIP_DEFLATED

ROOT=Path(__file__).resolve().parents[1]
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()
def files():
    names=['placements.tsv','notes.md','CHECK_EVENTS.tsv','progress.log','CHECKPOINTS.tsv']
    result=[ROOT/n for n in names if (ROOT/n).exists()]
    for folder in ('edited_pages','crops','scripts','review'):
        result += [p for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ('.pyc','.zip') and p.name!='archive_manifest.tsv']
    return sorted(result,key=lambda p:p.relative_to(ROOT).as_posix())
p=argparse.ArgumentParser();p.add_argument('output');p.add_argument('--checkpoint',type=int);a=p.parse_args()
out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
assert not out.exists(),f'Never overwrite an archive: {out}'
meta=json.loads((ROOT/'review/run_metadata.json').read_text())
if a.checkpoint is not None:
    elapsed=(datetime.now(timezone.utc)-datetime.fromisoformat(meta['started_utc'].replace('Z','+00:00'))).total_seconds()
    assert elapsed >= a.checkpoint*45*60,'Checkpoint not due yet'
    assert a.checkpoint == len(meta['checkpoints'])+1,'Checkpoint sequence mismatch'
    meta['checkpoints'].append({'number':a.checkpoint,'filename':out.name,'created_utc':now(),'durable_save':'pending; receipt is recorded in the subsequent checkpoint/final archive'})
    (ROOT/'review/run_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
items=files()
manifest=ROOT/'review/archive_manifest.tsv'
with manifest.open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['path','bytes','sha256'])
    for item in items:w.writerow([item.relative_to(ROOT).as_posix(),item.stat().st_size,digest(item)])
items.append(manifest)
with ZipFile(out,'x',compression=ZIP_DEFLATED,compresslevel=6) as z:
    for item in items:z.write(item,item.relative_to(ROOT).as_posix())
with ZipFile(out) as z:
    assert z.testzip() is None,'ZIP CRC failure'
print(json.dumps({'file':str(out),'bytes':out.stat().st_size,'members':len(items),'sha256':digest(out),'created_utc':now()}))
