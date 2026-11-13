#!/usr/bin/env python3
"""Create immutable progress checkpoints and verified final edition archives.

Run at the project root. Every ZIP has an exact byte/hash manifest; checkpoint
names are allocated monotonically and are opened exclusively. Final packaging
requires the strict report's current PDF/TeX hashes and complete gates.
"""
from __future__ import annotations
import argparse, collections, csv, datetime, hashlib, io, json, re, zipfile
from pathlib import Path
import pymupdf as fitz
from verify_pdf import sha256, sanitize
from write_release_report import BOOKS, assess

ROOT=Path(__file__).resolve().parents[2];WORK=ROOT/'work';REC=WORK/'records';OUT=ROOT/'deliverables'
TEXT_EXT={'.py','.lua','.tex','.json','.jsonl','.md','.tsv','.csv','.txt','.log','.aux','.out','.toc','.stdout'}
PATH_RE=re.compile(r'/(?:workspace|home|root|usr|opt|tmp|var)/[^\s"\'<>]+')
WIN_RE=re.compile(r'(?<![\w\\])[A-Za-z]:\\(?:Users|Windows|Program Files(?: \(x86\))?|texlive|workspace|home|Temp|tmp)(?:\\[^\s\n]*)?',re.I)
EMAIL_RE=re.compile(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}')

def rel(p):return Path(p).relative_to(ROOT).as_posix()
def digest(b):return hashlib.sha256(b).hexdigest()
def tsv_bytes(rows,fields):
    s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n',extrasaction='ignore')
    w.writeheader();w.writerows(rows);return s.getvalue().encode()
def payload(p):
    p=Path(p);data=p.read_bytes()
    if p.suffix in {'.log','.stdout'}:data=sanitize(data.decode(errors='replace')).encode()
    return data
def privacy(name,data):
    ext=Path(name).suffix;hits=[]
    if ext=='.pdf':
        with fitz.open(stream=data,filetype='pdf') as doc:
            content=json.dumps(doc.metadata,ensure_ascii=False)+'\n'+'\n'.join(p.get_text() for p in doc)
    elif ext in TEXT_EXT:
        content=data.decode('utf-8',errors='replace')
        # The executable interpreter directive is a portable program convention,
        # not a copied private machine path. All actual record content is tested.
        if ext=='.py':content=re.sub(r'^#![^\n]*\n','',content,count=1)
    else:return hits
    for kind,pattern in [('local path',PATH_RE),('Windows path',WIN_RE),('email address',EMAIL_RE)]:
        for m in pattern.finditer(content):hits.append({'file':name,'kind':kind,'value':m.group(0)[:200]})
    return hits

def common_items(include_images=False,include_proofs=False,include_probe_pdfs=True):
    items={}
    current_images=set()
    if include_images:
        for ledger in (WORK/'verification').glob('*/VISUAL_REVIEW.tsv'):
            with ledger.open(newline='') as f:
                for row in csv.DictReader(f,delimiter='\t'):
                    current_images.add(ledger.parent/row['full_page_image'])
    for directory in ['work/scripts','work/data','work/records']:
        for p in sorted((ROOT/directory).rglob('*')):
            if not p.is_file() or '__pycache__' in p.parts or 'cache' in p.parts:continue
            if p.name in {'ARCHIVE_MANIFESTS.json','PRIVACY_AUDIT.json','IMAGE_ALIASES.tsv','CHECKPOINT_RETENTION.tsv'}:continue
            items[rel(p)]=(p,'edition script/data/record')
    for name in ['LM_FR_MANIFEST.tsv','LM_EN_MANIFEST.tsv','LM_TYPESET_MANIFEST.tsv']:
        items['input_manifests/'+name]=(ROOT/'sources'/name,'original supplied manifest')
    for p in sorted((WORK/'build').glob('*')):
        if p.is_file() and (p.name.endswith(('_provenance.json','_source_marks.json','.lm-links.tsv','.lm-scans.tsv'))):
            items[rel(p)]=(p,'final build audit output')
    for dirname in ['verification','verification_baseline']:
        for p in sorted((WORK/dirname).rglob('*')):
            if not p.is_file():continue
            if p.suffix in {'.json','.jsonl','.tsv'}:
                items[rel(p)]=(p,'PDF verification output')
            elif include_images and dirname=='verification' and p in current_images:
                items[rel(p)]=(p,'selected-page visual evidence')
    if include_proofs:
        for p in sorted((WORK/'visual_repair_proofs').rglob('*')):
            if p.is_file() and (include_probe_pdfs or p.suffix.lower()!='.pdf'):
                items['proofs/visual_repairs/'+p.relative_to(WORK/'visual_repair_proofs').as_posix()]=(p,'curated visual-repair evidence; development PDFs remain in checkpoints')
                if not include_probe_pdfs:
                    # Keep both historical archive references and the original
                    # project-relative paths used by hash-bound audit scripts.
                    items[rel(p)]=(p,'same curated evidence at its reproducible project path')
        for directory in ['layout_probes','layout_repaired','layout_cell_validation','layout_margin495_validation','layout_pair_validation','margin_collision_probes','verification_before_repairs']:
            for p in sorted((WORK/directory).rglob('*')):
                if not p.is_file() or p.suffix not in {'.pdf','.png','.tex','.json','.tsv','.log','.py'}:continue
                if p.suffix=='.pdf' and p.stat().st_size==0:continue
                if p.suffix=='.pdf' and not include_probe_pdfs:continue
                items[rel(p)]=(p,'source-local repair proof or prior visual evidence')
    return items

def make_zip(path,items,extra=None,exclusive=True):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    if exclusive and path.exists():raise FileExistsError(path.name+' already exists; never overwrite a checkpoint')
    contents=dict(items);contents.update(extra or {});manifest=[];hits=[]
    # ZIP records are assembled from the exact byte string hashed here. An
    # independently edited input cannot produce a stale entry hash.
    mode='x' if exclusive else 'w'
    try:
        with zipfile.ZipFile(path,mode,compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
            for name,(src,role) in sorted(contents.items()):
                if name.startswith('/') or '..' in Path(name).parts:raise ValueError('Unsafe ZIP path: '+name)
                data=src if isinstance(src,bytes) else payload(src)
                hits+=privacy(name,data)
                if hits:raise ValueError('Privacy check failed: '+json.dumps(hits,ensure_ascii=False))
                zi=zipfile.ZipInfo(name,(2026,11,13,0,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=0o100644<<16
                z.writestr(zi,data)
                manifest.append({'path':name,'bytes':len(data),'sha256':digest(data),'role':role})
            z.writestr('MANIFEST.tsv',tsv_bytes(manifest,['path','bytes','sha256','role']))
        with zipfile.ZipFile(path) as z:
            if z.testzip():raise RuntimeError('ZIP CRC verification failed')
            for row in manifest:
                data=z.read(row['path'])
                if len(data)!=row['bytes'] or digest(data)!=row['sha256']:raise RuntimeError('ZIP manifest mismatch')
    except Exception:
        # A failed new file is not an accepted checkpoint; keep it clearly
        # distinguished for diagnosis instead of overwriting a prior success.
        if path.exists():path.rename(path.with_suffix(path.suffix+'.failed'))
        raise
    return {'filename':path.name,'bytes':path.stat().st_size,'sha256':sha256(path),'entries':len(manifest),'manifest':manifest}

def checkpoint(part,finished_reader=None):
    OUT.mkdir(exist_ok=True)
    if finished_reader:
        _,failures=assess(finished_reader)
        if failures:raise RuntimeError('Cannot checkpoint an unfinished reader: '+str(failures))
    previous=json.loads((REC/'CHECKPOINT_STATUS.json').read_text()) if (REC/'CHECKPOINT_STATUS.json').exists() else {}
    finished=list(previous.get('finished_readers',[]))
    if finished_reader and finished_reader not in finished:finished.append(finished_reader)
    status={'part':part,'finished_readers':finished,'provisional_readers':[b for b in BOOKS if b not in finished],
      'saved_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'note':'A checkpoint preserves current work. Only readers named finished_readers have passed their final gates. Rebuild any provisional source and rerun checks before publication.',
      'images':'Selected-page PNGs and contact sheets are reproducible from the saved PDFs. Their hashes and actual inspection histories are retained; this checkpoint omits the large raster duplicates.'}
    (REC/'CHECKPOINT_STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
    nums=[int(m[1]) for p in OUT.glob('LM_READERS_checkpoint_*.zip') if (m:=re.fullmatch(r'LM_READERS_checkpoint_(\d+)\.zip',p.name))]
    n=max(nums,default=0)+1;path=OUT/f'LM_READERS_checkpoint_{n:02d}.zip'
    items=common_items(False,True)
    for book in BOOKS:
        for ext in ['.tex','.pdf']:
            p=WORK/'build'/(book+ext)
            if p.exists():items[rel(p)]=(p,'current reader/master; consult checkpoint status')
    result=make_zip(path,items)
    ledger=REC/'checkpoint_archives.jsonl'
    with ledger.open('a') as f:f.write(json.dumps({k:v for k,v in result.items() if k!='manifest'},ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='manifest'},ensure_ascii=False))

def final_maps():
    maps={'LM_READERS_FR.zip':{},'LM_READERS_EN.zip':{},'LM_READERS_RECORDS.zip':common_items(True,True,False)}
    for book in BOOKS:
        lang='FR' if '_FR_' in book else 'EN'
        for ext in ['.tex','.pdf']:maps['LM_READERS_'+lang+'.zip'][book+ext]=(WORK/'build'/(book+ext),'self-contained reader/master')
    for lang in ['FR','EN']:
        for name in ['README.md','APPARATUS_COUNTS.md','CHANGES_'+lang+'.tsv']:
            maps['LM_READERS_'+lang+'.zip'][name]=(REC/name,'edition overview or change record')
    return maps

def retention(maps):
    candidates={};hash_to_target={}
    exclusion_file=WORK/'data/development_pdf_exclusions.json'
    exclusions=json.loads(exclusion_file.read_text()) if exclusion_file.exists() else {}
    if isinstance(exclusions,list):exclusions={r['path']:r for r in exclusions}
    for archive,items in maps.items():
        for path,(src,role) in items.items():
            h=digest(src if isinstance(src,bytes) else payload(src))
            candidates.setdefault(path,[]).append((archive,path,h));hash_to_target.setdefault(h,(archive,path,h))
    out=[]
    for checkpoint in sorted(OUT.glob('LM_READERS_checkpoint_*.zip')):
        with zipfile.ZipFile(checkpoint) as z:
            for old in sorted(z.namelist()):
                if old.endswith('/'):continue
                data=z.read(old);h=digest(data);target=hash_to_target.get(h)
                reason='Byte-for-byte identical content retained.';state='preserved'
                if not target:
                    possible=candidates.get(old,[])
                    if not possible and old.startswith('work/build/'):
                        possible=candidates.get(Path(old).name,[])
                    if possible:
                        target=possible[0];state='superseded';reason='Superseded by the final source, measurements or record at the indicated path; development version remains in its immutable checkpoint.'
                    elif old in exclusions:
                        ex=exclusions[old]
                        target=next((t for t in candidates.get(ex['final_path'],[]) if t[0]==ex['final_archive']),None)
                        if target is None:raise RuntimeError('Missing final replacement for excluded development PDF: '+old)
                        state='omitted';reason=ex['reason']
                    else:
                        target=('','','');state='omitted'
                        reason=('Checkpoint-specific container manifest; MANIFEST.tsv in LM_READERS_FR.zip, LM_READERS_EN.zip and LM_READERS_RECORDS.zip inventories the final files.' if old=='MANIFEST.tsv' else
                                'Development-only output superseded by the final build and its verification records; retained in the original checkpoint for historical recovery.')
                out.append({'checkpoint':checkpoint.name,'checkpoint_path':old,'checkpoint_bytes':len(data),'checkpoint_sha256':h,
                  'disposition':state,'final_archive':target[0],'final_path':target[1],'final_sha256':target[2],'reason':reason})
    return out

def preflight(maps):
    """Check the complete release before creating any of its three ZIPs."""
    expected={b+'.pdf' for b in BOOKS}
    pdfs=[(archive,path) for archive,items in maps.items() for path in items if path.endswith('.pdf')]
    if len(pdfs)!=len(expected) or {path for _,path in pdfs}!=expected:
        raise RuntimeError('Final archives must contain exactly the seven publication PDFs')
    if any(archive=='LM_READERS_RECORDS.zip' for archive,_ in pdfs):
        raise RuntimeError('Development PDFs must not enter the final records archive')
    existing=[name for name in maps if (OUT/name).exists()]
    if existing:raise FileExistsError('Final archive names already exist: '+', '.join(existing))
    hits=[];files=0;total_bytes=0
    for archive,items in maps.items():
        for path,(src,role) in items.items():
            if path.startswith('/') or '..' in Path(path).parts:
                raise ValueError('Unsafe final ZIP path: '+path)
            data=src if isinstance(src,bytes) else payload(src)
            hits+=privacy(path,data);files+=1;total_bytes+=len(data)
    if hits:raise ValueError('Release preflight privacy check failed: '+json.dumps(hits,ensure_ascii=False))
    retained=retention(maps)
    unexplained=[r for r in retained if r['disposition']=='omitted' and not r['final_path'] and r['checkpoint_path']!='MANIFEST.tsv']
    if unexplained:
        raise RuntimeError('Checkpoint entries lack a specific final replacement: '+json.dumps(unexplained,ensure_ascii=False))
    return {'status':'PASS','files':files,'uncompressed_bytes':total_bytes,'publication_pdfs':len(pdfs),
            'checkpoint_entries':len(retained),'unexplained_omissions':0,'privacy_findings':0}

def final():
    status=json.loads((REC/'release_status.json').read_text())
    if status.get('status')!='COMPLETE' or status.get('failures'):raise RuntimeError('Strict release report is not complete')
    for book in BOOKS:
        v,failures=assess(book)
        if failures:raise RuntimeError(str(failures))
        for kind in ['pdf','tex']:
            if sha256(WORK/'build'/(book+'.'+kind))!=status['books'][book][kind+'_sha256']:raise RuntimeError('Stale release hash: '+book)
    maps=final_maps()
    pdf_privacy=json.loads((WORK/'data/pdf_privacy_audit.json').read_text())
    if pdf_privacy.get('status')!='PASS' or pdf_privacy.get('findings'):
        raise RuntimeError('Expanded PDF privacy audit is not PASS')
    expected_pdfs={(archive,path):src for archive,items in maps.items() for path,(src,role) in items.items() if path.endswith('.pdf')}
    audited_pdfs={(r.get('archive'),r.get('path')):r for r in pdf_privacy.get('files',[])}
    if set(audited_pdfs)!=set(expected_pdfs):raise RuntimeError('Expanded PDF privacy inventory is stale')
    for key,src in expected_pdfs.items():
        audit=audited_pdfs[key]
        if not audit.get('stable_during_audit') or audit.get('sha256')!=sha256(src):
            raise RuntimeError('Expanded PDF privacy hash is stale: '+key[1])
    # Store identical selected-page PNG bytes once, with an explicit recovery
    # map. This primarily deduplicates the two masters against apparatus books.
    images={};aliases=[];record_items=maps['LM_READERS_RECORDS.zip']
    for path in sorted(list(record_items)):
        if not path.endswith('.png'):continue
        if path.startswith(('proofs/visual_repairs/','work/visual_repair_proofs/')):continue
        src,_=record_items[path];h=sha256(src)
        if h in images:
            aliases.append({'alias_path':path,'stored_path':images[h],'sha256':h,'bytes':Path(src).stat().st_size});del record_items[path]
        else:images[h]=path
    alias_data=tsv_bytes(aliases,['alias_path','stored_path','sha256','bytes']);(REC/'IMAGE_ALIASES.tsv').write_bytes(alias_data)
    record_items['work/records/IMAGE_ALIASES.tsv']=(alias_data,'exact duplicate-image recovery inventory')
    retained=retention(maps);retained_data=tsv_bytes(retained,['checkpoint','checkpoint_path','checkpoint_bytes','checkpoint_sha256','disposition','final_archive','final_path','final_sha256','reason'])
    (REC/'CHECKPOINT_RETENTION.tsv').write_bytes(retained_data)
    record_items['work/records/CHECKPOINT_RETENTION.tsv']=(retained_data,'file-by-file checkpoint retention and supersession')
    readme=(REC/'README.md').read_bytes();record_items['README.md']=(readme,'top-level edition overview')
    privacy_report={'status':'PASS','scope':'Every packaged text file plus every PDF text layer and metadata; ZIP bytes match manifest digests. The additional hash-bound PDF audit covers object dictionaries, decoded strings, annotation/action targets and embedded-file absence. Binary font/image streams are not interpreted. Interpreter shebangs are executable conventions, not private paths.','expanded_pdf_audit':'work/data/pdf_privacy_audit.json','expanded_pdf_count':len(audited_pdfs),'local_path_findings':[],'email_findings':[]}
    record_items['work/records/PRIVACY_AUDIT.json']=(json.dumps(privacy_report,indent=2).encode(),'privacy-check scope and result')
    checks=preflight(maps)
    record_items['work/records/FINAL_ARCHIVE_PREFLIGHT.json']=(json.dumps(checks,indent=2).encode(),'whole-release preflight before any final archive is created')
    results=[]
    for archive,items in maps.items():
        result=make_zip(OUT/archive,items,exclusive=True);results.append({k:v for k,v in result.items() if k!='manifest'})
        print(json.dumps(results[-1],ensure_ascii=False),flush=True)
    (REC/'ARCHIVE_MANIFESTS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest='command',required=True)
    c=sp.add_parser('checkpoint');c.add_argument('--part',required=True);c.add_argument('--finished-reader',choices=BOOKS)
    sp.add_parser('final');a=ap.parse_args()
    if a.command=='checkpoint':checkpoint(a.part,a.finished_reader)
    else:final()
