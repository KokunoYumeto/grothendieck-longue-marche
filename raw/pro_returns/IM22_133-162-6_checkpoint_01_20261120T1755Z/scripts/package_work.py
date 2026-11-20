"""Validate completed decisions and package a timed checkpoint or final ZIP."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import csv,fcntl,hashlib,json,sys,zipfile,time
from review_and_commit import W,S,load
def utc():return datetime.now(timezone.utc)
def verify(final=False):
    rr=list(csv.DictReader((S/'IM22_133-162-6_corrections.tsv').open(),delimiter='\t'))
    placements=list(csv.DictReader((W/'placements.tsv').open(newline=''),delimiter='\t'))
    keys=lambda rows:[(r['id'],r['cote'],r['scan']) for r in rows]
    expected=keys(rr); got=keys(placements)
    assert len(got)==len(set(got)), 'Duplicate placement identity'
    assert got==[k for k in expected if k in set(got)], 'Wrong placement order'
    if final:assert got==expected, f'Incomplete rows {len(got)}/{len(expected)}'
    reviews=list((W/'reviews').glob('*.json'))
    if final:assert len(reviews)==309
    if final:
        # Read immutable attachment bytes for comparison without extracting again.
        with zipfile.ZipFile(W.parent/'upload/IM22_133-162-6.zip') as source_zip:
            for p in (S/'IM22_133-162-6_pages').glob('*.tex'):
                assert p.read_bytes()==source_zip.read('IM22_133-162-6_pages/'+p.name),('Source changed',p.name)
    for p in reviews:
        packet,result,original,revised=load(p.stem)
        rec=json.loads(p.read_text())
        assert (W/'edited_pages'/p.with_suffix('.tex').name).read_bytes()==revised.encode(),p.stem
        assert rec['original_sha256']==hashlib.sha256(original.encode()).hexdigest(),p.stem
        assert rec['edited_sha256']==hashlib.sha256(revised.encode()).hexdigest(),p.stem
        for row in result['rows']:
            recorded=next(r for r in placements if r['id']==row['id'] and r['cote']==packet['rows'][0]['cote'] and r['scan']==packet['rows'][0]['scan'])
            for k in ('decision','find','replace','what_the_ink_shows','confidence'):
                assert recorded[k]==row[k],(p.stem,row['id'],k)
    return {'rows':len(got),'pages':len(reviews),'total_rows':405,'total_pages':309}
def build(dest,final=False):
    status=verify(final)
    with (W/'dispatch.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        files=[p for p in sorted(W.rglob('*')) if p.is_file() and 'checkpoints' not in p.relative_to(W).parts and '__pycache__' not in p.parts and p.suffix not in ('.zip','.lock')]
        captured=[]
        for p in files:
            for attempt in range(6):
                before=p.stat();data=p.read_bytes();after=p.stat()
                if (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns):break
                time.sleep(.1)
            else:raise RuntimeError('Unstable file '+str(p))
            captured.append((p.relative_to(W).as_posix(),data))
        manifest={'created_utc':utc().isoformat(),'kind':'final' if final else 'checkpoint','status':status,'excluded_original_attachments':['IM22_133-162-6.zip','PROMPT(20261120-170721).md'],'files':[{'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()} for name,data in captured]}
        assert not dest.exists(), 'Never overwrite a checkpoint/final archive'
        with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
            for name,data in captured:z.writestr(name,data)
            z.writestr('MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        with zipfile.ZipFile(dest) as z:assert z.testzip() is None
    return dict(status,path=str(dest),bytes=dest.stat().st_size,sha256=hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='verify': print(json.dumps(verify('--final' in sys.argv)))
    elif mode=='checkpoint':
        start=datetime.strptime((W/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
        prior=list((W/'checkpoints').glob('IM22_133-162-6_checkpoint_*.zip'))
        n=len(prior)+1;due=start+timedelta(minutes=45*n)
        if utc()<due:
            print(json.dumps({'checkpoint_due_utc':due.isoformat(),'not_due':True}));sys.exit()
        path=W/'checkpoints'/f'IM22_133-162-6_checkpoint_{n:02d}.zip'
        print(json.dumps(build(path)))
    elif mode=='final':
        print(json.dumps(build(W.parent/'IM22_133-162-6.zip',final=True)))
