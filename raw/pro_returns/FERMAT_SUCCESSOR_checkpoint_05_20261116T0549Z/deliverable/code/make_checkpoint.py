"""Create one immutable hourly research checkpoint, excluding attached sources."""
from pathlib import Path
import csv, hashlib, json, sys, zipfile

ROOT=Path(__file__).resolve().parents[2]
number=int(sys.argv[1])
target=ROOT/f'FERMAT_SUCCESSOR_checkpoint_{number:02d}.zip'
if target.exists(): raise SystemExit('Refusing to overwrite checkpoint')
attached=set()
with (ROOT/'background'/'MANIFEST.tsv').open() as f:
    attached={r['sha256'] for r in csv.DictReader(f,delimiter='\t')}
files=[]; excluded=[]
for base in (ROOT/'deliverable',ROOT/'work'):
    for p in base.rglob('*'):
        if not p.is_file() or p.is_symlink(): continue
        rel=p.relative_to(ROOT)
        if base.name=='work' and (rel.parts[1] in ('primary','texformat') or rel.parts[1].startswith(('pari-','library_helpers_'))):
            continue
        if p.suffix.lower() in ('.pdf','.png','.jpg','.dvi','.tar','.xz') and base.name=='work':
            continue
        if '__pycache__' in rel.parts: continue
        # Archive exactly the bytes whose digest was recorded. Working notes
        # may continue to change after their snapshot has been read.
        payload=p.read_bytes()
        digest=hashlib.sha256(payload).hexdigest()
        if digest in attached:
            excluded.append({'path':str(rel),'reason':'identical to attached input source','sha256':digest});continue
        if p.name=='FERMAT_SUCCESSOR_paper.pdf':
            # A PDF is included only after an explicit layout-QA certificate exists.
            qa=ROOT/'deliverable'/'records'/'pdf_qa.json'
            if not qa.exists() or json.loads(qa.read_text()).get('pdf_sha256')!=digest:
                excluded.append({'path':str(rel),'reason':'working PDF not yet publication-verified','sha256':digest});continue
            build=ROOT/'deliverable'/'records'/'build_inputs.json'
            if number>=3:
                data=json.loads(build.read_text()) if build.exists() else {}
                stable=(data.get('pdf_sha256')==digest and data.get('sources_stable_during_build')
                        and all((ROOT/'deliverable'/name).exists()
                                and hashlib.sha256((ROOT/'deliverable'/name).read_bytes()).hexdigest()==sha
                                for name,sha in data.get('sources',{}).items()))
                if not stable:
                    excluded.append({'path':str(rel),'reason':'PDF is not certified against the current stable source inventory','sha256':digest});continue
        files.append((p,str(rel),digest,payload))
record={'checkpoint':number,'files':len(files),'excluded':excluded,
        'preservation':'Input attachments and raw third-party source files omitted; mathematical outputs, work notes and code retained.'}
record_path=ROOT/'deliverable'/'records'/f'checkpoint_{number:02d}_manifest.json'
record_path.write_text(json.dumps(record,indent=2))
payload=record_path.read_bytes()
files.append((record_path,str(record_path.relative_to(ROOT)),hashlib.sha256(payload).hexdigest(),payload))
with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
    for path,name,digest,payload in files: archive.writestr(name,payload)
    archive.writestr('SHA256SUMS.txt','\n'.join(d+'  '+n for _,n,d,_ in files)+'\n')
print(json.dumps({'path':str(target),'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'files':len(files)}))
