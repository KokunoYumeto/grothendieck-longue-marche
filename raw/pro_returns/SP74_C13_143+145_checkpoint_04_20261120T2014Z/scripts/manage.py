#!/usr/bin/env python3
"""Commit a visually adjudicated page or audit, make timed ZIPs, freeze hashes."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib,zipfile
from build_deliverables import ROOT,BASE,PREFIX,build

def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def log(s):
    with (ROOT/'progress.log').open('a') as f:f.write(s+'\n')
def commit(key,reader):
    report=ROOT/'reviews'/f'{key}_reader{reader}.json'; candidate=ROOT/'reviews'/f'{key}_reader{reader}.tex'
    r=json.loads(report.read_text()); assert r['key']==key
    r['accepted_at']=now();r['main_reader_review']='All disputed and unresolved loci visually adjudicated by main reader before commit.'
    (ROOT/'pages'/f'{key}.tex').write_text(candidate.read_text())
    (ROOT/'reviews'/f'{key}_accepted.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
    print(build());cote,scan=key.split('_scan');log(f'scan {scan} done {now()} cote {cote} reader {reader}')
def audit(key,reader):
    p=ROOT/'reviews'/f'{key}_accepted.json';r=json.loads(p.read_text());assert r['reader']!=reader
    auditpath=ROOT/'reviews'/f'{key}_audit{reader}.json';a=json.loads(auditpath.read_text());assert a['key']==key
    assert a.get('main_adjudication') and r.get('audit_adjudications'), 'Apply the main adjudication before marking this audit complete'
    r['audited_at']=now();r['audit_reader']=reader;r['audit_record']=str(auditpath.relative_to(ROOT))
    p.write_text(json.dumps(r,ensure_ascii=False,indent=2));print(build());_,scan=key.split('_scan');log(f'scan {scan} audited {now()} cote {key.split("_")[0]} reader {reader}')
def checkpoint(num):
    name=f'{PREFIX}_checkpoint_{int(num):02d}.zip';dest=BASE/'deliverables'/name;dest.parent.mkdir(exist_ok=True)
    if dest.exists():raise FileExistsError(dest)
    log(f'checkpoint {name} created {now()}')
    pack(dest);print(dest)
def pack(dest):
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip':z.write(p,p.relative_to(ROOT))
def freeze():
    files=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/f'{PREFIX}_transcription.tex']
    h={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    (ROOT/'transcription_hashes.json').write_text(json.dumps(h,indent=2))
    log('transcription frozen '+now())
    for p,d in h.items():log('SHA-256 '+d+' '+p)
def verify():
    h=json.loads((ROOT/'transcription_hashes.json').read_text())
    for p,d in h.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d,p
    log('frozen transcription hashes unchanged '+now());print(f'{len(h)} hashes unchanged')
if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='commit':commit(*sys.argv[2:])
    elif cmd=='audit':audit(*sys.argv[2:])
    elif cmd=='checkpoint':checkpoint(sys.argv[2])
    elif cmd=='freeze':freeze()
    elif cmd=='verify':verify()
    elif cmd=='build':print(build())
    elif cmd=='pack':pack(Path(sys.argv[2]))
