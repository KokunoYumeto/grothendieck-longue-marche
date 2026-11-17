from record_page import ROOT,utc,rebuild
import json

def audited(scan,note=''):
 p=ROOT/'records'/f'scan{scan:03d}.json'
 r=json.loads(p.read_text())
 if 'audit_utc' in r:raise ValueError('Already audited')
 stamp=utc();r['audit_utc']=stamp;r['audit_note']=note
 p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} audited {stamp}\n')
 if note:
  with (ROOT/'records'/'second_reading.md').open('a') as f:f.write(f'- Scan {scan:03d} ({stamp}): {note}\n')
 print(f'Audited {scan:03d}')

def metadata(scan,**changes):
 p=ROOT/'records'/f'scan{scan:03d}.json';r=json.loads(p.read_text());r.update(changes)
 p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');rebuild()
