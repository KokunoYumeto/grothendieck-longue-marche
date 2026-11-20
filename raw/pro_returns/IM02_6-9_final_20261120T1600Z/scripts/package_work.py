#!/usr/bin/env python3
"""Validate and package the transcription deliverables; never include source attachments.
Checkpoint mode refuses to run before its scheduled 45-minute interval and never overwrites.
Saving the resulting archive to persistent storage is a separate authenticated upload.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,csv,hashlib,zipfile,collections,io
from review import W,D,source_rows,key,pagename,inspect,rebuild,write_tsv

def validate(final=False):
    source=source_rows();accepted={};pages={}
    for p in sorted((D/'reviews').glob('*.json')):
        report,orig,edited=inspect(p.stem,p)
        assert (D/'edited_pages'/f'{p.stem}.tex').read_bytes()==edited.encode('utf-8'),p.stem
        for r in report['rows']:
            assert key(r) not in accepted
            assert r.get('events') and r.get('what_the_ink_shows')
            if r['decision'] in 'bd' or r.get('unsettled'): assert r.get('note'),key(r)
            accepted[key(r)]=r
        assert not report.get('open_questions'),p.stem
        pages[p.stem]=report
    with (D/'placements.tsv').open(newline='') as f:placements=list(csv.DictReader(f,delimiter='\t'))
    assert [key(r) for r in placements]==[key(r) for r in source if key(r) in accepted]
    for r in placements:
        for field,value in r.items():assert value==str(accepted[key(r)][field]),(key(r),field)
    assert {p.stem for p in (D/'edited_pages').glob('*.tex')}==set(pages)
    if final:
        assert len(accepted)==92 and len(pages)==58
        assert set(accepted)=={key(r) for r in source}
        assert set(pages)=={pagename(r) for r in source}
    return source,accepted,pages

def package(mode):
    final=mode=='final';source,rows,pages=validate(final)
    dt=datetime.now(timezone.utc);start=datetime.strptime((D/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    out=W/'output';out.mkdir(exist_ok=True)
    if final:name='IM02_6-9.zip'
    else:
        prior=sorted(out.glob('IM02_6-9_checkpoint_*.zip'));n=len(prior)+1
        assert (dt-start).total_seconds()>=45*60*n,'Checkpoint is not due; no early checkpoint permitted'
        name=f'IM02_6-9_checkpoint_{n:02d}.zip'
    target=out/name
    assert not target.exists(),'Never overwrite an archive'
    ordered=[]
    for r in source:
        pn=pagename(r)
        if pn not in ordered:ordered.append(pn)
    status=[]
    for i,pn in enumerate(ordered,1):
        p=pages.get(pn)
        status.append({'order':i,'page':pn,'status':'complete' if p else 'pending','reader':p['reader'] if p else '', 'reader_returned_utc':p['completed_utc'] if p else '', 'main_reviewed_utc':p['main_review']['date'] if p else ''})
    write_tsv(D/'PAGE_STATUS.tsv',['order','page','status','reader','reader_returned_utc','main_reviewed_utc'],status)
    validation={'validated_utc':dt.strftime('%Y-%m-%d %H:%M:%S UTC'),'complete':final,'pages':len(pages),'rows':len(rows),'decisions':dict(collections.Counter(r['decision'] for r in rows.values())),'uncertain_rows':[list(key(r)) for r in rows.values() if r.get('unsettled')], 'checks':['Row coverage and original table order','Exact unique original replacement spans','Non-overlapping row replacements','Exact byte replay, including CRLF line endings','No unrecorded TeX changes','Required notes and check events','All referenced crops present','All main-reader decisions closed, including explicit retained doubts']}
    (D/'VALIDATION.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
    members={}
    for p in D.rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.name!='FILE_LIST.tsv':members[p.relative_to(D).as_posix()]=p
    for p in (W/'reviews').glob('*'):
        if p.is_file():members['reader_reports/'+p.name]=p
    manifest=io.StringIO(newline='');wr=csv.writer(manifest,delimiter='\t');wr.writerow(['path','bytes','sha256'])
    for name,p in sorted(members.items()):
        data=p.read_bytes();wr.writerow([name,len(data),hashlib.sha256(data).hexdigest()])
    (D/'FILE_LIST.tsv').write_text(manifest.getvalue())
    members['FILE_LIST.tsv']=D/'FILE_LIST.tsv'
    with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for name,p in sorted(members.items()):z.write(p,name)
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        assert not any(n.endswith('.zip') for n in z.namelist())
        assert 'placements.tsv' in z.namelist() and 'CHECK_EVENTS.tsv' in z.namelist()
        for name,p in members.items():assert z.read(name)==p.read_bytes(),name
    print(json.dumps({'path':str(target),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'member_count':len(members),**validation},ensure_ascii=False))

if __name__=='__main__':
    assert sys.argv[1] in ['validate','final','checkpoint']
    if sys.argv[1]=='validate':
        s,r,p=validate();print(json.dumps({'validated_pages':len(p),'validated_rows':len(r)}))
    else:package(sys.argv[1])
