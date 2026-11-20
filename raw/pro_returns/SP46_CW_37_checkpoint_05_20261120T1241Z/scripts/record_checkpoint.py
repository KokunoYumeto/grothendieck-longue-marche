"""Verify an already-persisted checkpoint and append its save receipt, without changing the ZIP."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,zipfile
O=Path(__file__).resolve().parents[1]
data=json.load(sys.stdin);n=int(data['number'])
library_id=data['library_file_id'];assert library_id.startswith('libfile_')
p=O.parent/f'SP46_CW_37_checkpoint_{n:02}.zip';assert p.is_file()
with zipfile.ZipFile(p) as z:
    assert z.testzip() is None,'Checkpoint failed CRC validation.'
    names=z.namelist()
    assert not any(x.endswith('.zip') for x in names),'Nested ZIP forbidden.'
    assert not any(x.split('/')[0] in ['source','upload','packets'] for x in names),'Input attachments must not be copied.'
    for required in ['SP46_CW_37_transcription.tex','SP46_CW_37_changes.md','SP46_CW_37_collation.tsv','SP46_CW_37_inventory.csv','SP46_CW_37_doubts.md','SP46_CW_37_notes.md','SP46_CW_37_workflow.md','CHECK_EVENTS.tsv','progress.log']:
        assert required in names,f'Missing deliverable {required}'
h=hashlib.sha256()
with p.open('rb') as f:
    for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
t=data.get('saved_utc') or datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
q=O/'checkpoints.json';records=json.loads(q.read_text())
assert not any(x['number']==n for x in records),'Do not replace an existing checkpoint receipt.'
assert n==len(records)+1,'Checkpoint numbers must be consecutive.'
rec=dict(number=n,name=p.name,saved_utc=t,library_file_id=library_id,bytes=p.stat().st_size,sha256=h.hexdigest())
records.append(rec);q.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
with (O/'progress.log').open('a') as f:f.write(f'checkpoint {n:02} saved {t}; {p.name}; {library_id}; {rec["bytes"]} bytes; SHA-256 {rec["sha256"]}; CRC and exclusion checks passed\n')
print(json.dumps(dict(rec,members=len(names)),ensure_ascii=False))
