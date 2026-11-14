#!/usr/bin/env python3
"""Create immutable progress checkpoints and verified final edition archives.

Run at the project root. Every ZIP has an exact byte/hash manifest; checkpoint
names are allocated monotonically and are opened exclusively. Final packaging
requires the strict report's current PDF/TeX hashes and complete gates.
"""
from __future__ import annotations
import argparse, collections, csv, datetime, hashlib, io, json, re, zipfile, zlib
from pathlib import Path
import pymupdf as fitz
from verify_pdf import sha256, sanitize
from write_release_report import BOOKS, assess

ROOT=Path(__file__).resolve().parents[2];WORK=ROOT/'work';REC=WORK/'records';OUT=ROOT/'deliverables'
MAX_ARCHIVE_BYTES=536870912
TEXT_EXT={'.py','.lua','.tex','.json','.jsonl','.md','.tsv','.csv','.txt','.log','.aux','.out','.toc','.stdout'}
PATH_RE=re.compile(r'/(?:workspace|home|root|usr|opt|tmp|var)/[^\s"\'<>]+')
WIN_RE=re.compile(r'(?<![\w\\])[A-Za-z]:\\(?:Users|Windows|Program Files(?: \(x86\))?|texlive|workspace|home|Temp|tmp)(?:\\[^\s\n]*)?',re.I)
EMAIL_RE=re.compile(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}')
_COMPILER_CONTEXT_KEY=None
_COMPILER_CONTEXT=None

def compiler_context(force=False):
    """Cache only within an unchanged manifest; revalidate at archive gates."""
    global _COMPILER_CONTEXT_KEY,_COMPILER_CONTEXT
    import compiler_output_privacy as compiler
    manifest=ROOT/compiler.MANIFEST
    stamp=(manifest.stat().st_mtime_ns,manifest.stat().st_size) if manifest.exists() else None
    key=(str(ROOT.resolve()),stamp)
    if force or key!=_COMPILER_CONTEXT_KEY:
        _COMPILER_CONTEXT=compiler.load_context(ROOT)
        _COMPILER_CONTEXT_KEY=key
    return _COMPILER_CONTEXT

def rel(p):return Path(p).relative_to(ROOT).as_posix()
def digest(b):return hashlib.sha256(b).hexdigest()
def tsv_bytes(rows,fields):
    s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n',extrasaction='ignore')
    w.writeheader();w.writerows(rows);return s.getvalue().encode()
def payload(p):
    p=Path(p);data=p.read_bytes()
    try:name=p.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:name=None
    context=compiler_context()
    if name and context is not None:
        from compiler_output_privacy import payload_for_path
        projected=payload_for_path(ROOT,name,data,context)
        if projected is not None:return projected
    if p.suffix.lower() in {'.log','.stdout'}:data=sanitize(data.decode(errors='replace')).encode()
    return data
def privacy(name,data):
    ext=Path(name).suffix.lower();hits=[]
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

def measure_zip(items):
    """Exact deflate6 size for the ordinary deterministic ZIP writer below."""
    rows=[];compressed={};total=22
    for name,(src,role) in sorted(items.items()):
        data=src if isinstance(src,bytes) else payload(src);h=digest(data)
        if h not in compressed:
            encoder=zlib.compressobj(6,zlib.DEFLATED,-15)
            compressed[h]=len(encoder.compress(data)+encoder.flush())
        total+=76+2*len(name.encode('utf-8'))+compressed[h]
        rows.append({'path':name,'bytes':len(data),'sha256':h,'role':role})
    manifest=tsv_bytes(rows,['path','bytes','sha256','role'])
    encoder=zlib.compressobj(6,zlib.DEFLATED,-15)
    total+=76+2*len('MANIFEST.tsv')+len(encoder.compress(manifest)+encoder.flush())
    if len(rows)+1>65535:total+=76
    return {'zip_bytes':total,'logical_file_bytes':sum(r['bytes'] for r in rows),
            'files':len(rows),'unique_payloads':len(compressed),'limit_bytes':MAX_ARCHIVE_BYTES}

def require_archive_size(items,label,reserve_bytes=0):
    result=measure_zip(items)
    if result['zip_bytes']+reserve_bytes>MAX_ARCHIVE_BYTES:
        raise RuntimeError(label+' would exceed the delivery limit: '+str(result['zip_bytes'])+
                           ' bytes plus '+str(reserve_bytes)+' reserved metadata bytes.')
    return result

def common_items(include_images=False,include_proofs=False,include_probe_pdfs=True):
    items={}
    context=compiler_context(force=True)
    current_images=set()
    if include_images:
        for ledger in (WORK/'verification').glob('*/VISUAL_REVIEW.tsv'):
            with ledger.open(newline='') as f:
                for row in csv.DictReader(f,delimiter='\t'):
                    current_images.add(ledger.parent/row['full_page_image'])
    for directory in ['work/scripts','work/data','work/records']:
        for p in sorted((ROOT/directory).rglob('*')):
            if not p.is_file() or '__pycache__' in p.parts or 'cache' in p.parts:continue
            if p.name in {'ARCHIVE_MANIFESTS.json','PRIVACY_AUDIT.json','IMAGE_ALIASES.tsv','FILE_ALIASES.tsv',
                          'CHECKPOINT_RETENTION.tsv','FULL_PAGE_RASTER_OMISSIONS.tsv','FULL_PAGE_RASTER_QUALIFICATIONS.json',
                          'INDEXED_REVIEW_GRID_OMISSIONS.tsv','INDEXED_REVIEW_GRID_QUALIFICATIONS.json',
                          'FINAL_RECORDS_LOGICAL_MANIFEST.tsv','FINAL_RECORDS_POLICY.json','README_RECORDS_STORAGE.md',
                          'FINAL_ARCHIVE_PREFLIGHT.json','NONPUBLICATION_PDF_EXCLUSIONS.json',
                          'FINAL_PROOF_ASSET_DISTRIBUTION.tsv','FINAL_PROOF_ASSET_DISTRIBUTION.json',
                          'README_RELEASE_ASSEMBLY.md'}:continue
            items[rel(p)]=(p,'edition script/data/record')
    for name in ['LM_FR_MANIFEST.tsv','LM_EN_MANIFEST.tsv','LM_TYPESET_MANIFEST.tsv']:
        items['input_manifests/'+name]=(ROOT/'sources'/name,'original supplied manifest')
    for p in sorted((WORK/'build').glob('*')):
        if p.is_file() and (p.name.endswith(('_provenance.json','_source_marks.json','.lm-links.tsv','.lm-scans.tsv'))):
            items[rel(p)]=(p,'final build audit output')
    for dirname in ['verification','verification_baseline']:
        for p in sorted((WORK/dirname).rglob('*')):
            if not p.is_file():continue
            if p.suffix.lower() in {'.json','.jsonl','.tsv'}:
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
                if not p.is_file() or p.suffix.lower() not in {'.pdf','.png','.tex','.json','.tsv','.log','.py'}:continue
                if p.suffix.lower()=='.pdf' and p.stat().st_size==0:continue
                if p.suffix.lower()=='.pdf' and not include_probe_pdfs:continue
                items[rel(p)]=(p,'source-local repair proof or prior visual evidence')
    if context is not None:
        from compiler_output_privacy import required_files,verify_reference,packaged_bytes,SNAPSHOT_USAGE
        exclusion_path=WORK/'data/development_pdf_exclusions.json'
        proof_exclusions=json.loads(exclusion_path.read_text()) if exclusion_path.exists() else {}
        for name,ref in required_files(context).items():
            verify_reference(ROOT,ref,context)
            if not include_probe_pdfs and Path(name).suffix.lower()=='.pdf':
                row=proof_exclusions.get(name)
                if (not row or row.get('source_pdf_sha256')!=ref['sha256'] or
                        row.get('source_pdf_bytes')!=ref.get('bytes')):
                    raise RuntimeError('A required historical PDF lacks an exact final-development disposition: '+name)
                continue
            items[name]=(ROOT/name,'exact manifest-required compiler-output evidence or explicitly pinned sidecar')
        # These seven paths are transient: capture the approved current bytes
        # only. A later build must not acquire the older log's qualification.
        book_logs={'work/build/'+book+'.log' for book in BOOKS}
        for entry in context.data['entries']:
            if entry.get('usage')!=SNAPSHOT_USAGE:continue
            ref=entry['raw'];name=ref['path'];p=ROOT/name
            if name not in book_logs:raise RuntimeError('Unapproved snapshot-only compiler-output path: '+name)
            if not p.is_file():continue
            current=p.read_bytes()
            if (digest(current),len(current)) not in {(r['sha256'],r['bytes']) for r in (ref,entry['portable'])}:continue
            verify_reference(ROOT,ref,context)
            items[name]=(packaged_bytes(ROOT,ref,context),'exact qualified current-build snapshot log; later unmatched bytes are not included by this rule')
    # Current logs may have later bytes than the snapshot-only registry. The
    # existing payload hook then uses ordinary sanitization, not old approval.
    from compiler_output_privacy import diagnostics
    for book in sorted(BOOKS):
        p=WORK/'build'/(book+'.log')
        if not p.is_file():continue
        name=rel(p);raw=p.read_bytes();portable=payload(p)
        if portable!=sanitize(raw.decode(errors='replace')).encode():
            raise RuntimeError('Current build log differs from standard sanitization: '+name)
        if sanitize(portable.decode(errors='replace')).encode()!=portable:
            raise RuntimeError('Current build log sanitization is not idempotent: '+name)
        if diagnostics(raw)!=diagnostics(portable):
            raise RuntimeError('Current build log sanitization changes diagnostics: '+name)
        if p.read_bytes()!=raw:
            raise RuntimeError('Current build log changed during collection: '+name)
        # Retain Path inputs so compact packaging also pins the raw file bytes.
        items[name]=(p,'current build log; standard portable sanitization with identical diagnostics')
    return items

def make_zip(path,items,extra=None,exclusive=True,expected_size=None):
    compiler_context(force=True)
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    if exclusive and path.exists():raise FileExistsError(path.name+' already exists; never overwrite a checkpoint')
    contents=dict(items);contents.update(extra or {});manifest=[];hits=[]
    # ZIP records are assembled from the exact byte string hashed here. An
    # independently edited input cannot produce a stale entry hash.
    mode='x' if exclusive else 'w'
    created=False
    try:
        with zipfile.ZipFile(path,mode,compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
            created=True
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
        compiler_context(force=True)
        if expected_size is not None and path.stat().st_size!=expected_size:
            raise RuntimeError('Archive byte count differs from its exact size preflight.')
    except Exception:
        # A failed new file is not an accepted checkpoint; keep it clearly
        # distinguished for diagnosis instead of overwriting a prior success.
        if created and path.exists():
            failed=path.with_suffix(path.suffix+'.failed');number=1
            while failed.exists():failed=path.with_suffix(path.suffix+'.failed'+str(number));number+=1
            path.rename(failed)
        raise
    return {'filename':path.name,'bytes':path.stat().st_size,'sha256':sha256(path),'entries':len(manifest),'manifest':manifest}

def make_compact_zip(path,items,source_checkpoint,measure_only=False,pdf_delta_plan=None):
    """Exact logical checkpoint with separately qualified lossless PNG recipes."""
    import restore_checkpoint as recovery
    import native_checkpoint_recipes as native
    import overview_checkpoint_recipes as overview
    import checkpoint_historical_pdf_imports as historical
    import checkpoint_zip_compression as compression
    compiler_context(force=True)
    recovery.require_engine()
    path=Path(path);source_checkpoint=Path(source_checkpoint)
    if path.exists():raise FileExistsError('Never overwrite a checkpoint: '+path.name)
    if not source_checkpoint.is_file():raise FileNotFoundError('A complete prior checkpoint is required for coverage.')
    inherited=None
    with zipfile.ZipFile(source_checkpoint) as prior_format:
        prior_compact=recovery.DESCRIPTOR in prior_format.namelist()
    if prior_compact:
        from checkpoint_inheritance import expand
        prior=recovery.CompactArchive(source_checkpoint)
        try:items,inherited=expand(items,prior,payload)
        finally:prior.close()
    items,historical_imports=historical.import_missing(items,ROOT,payload)
    if (inherited or {}).get('historical_pdf_imports') and not historical_imports:
        raise RuntimeError('Historical PDF import authority was lost during compact inheritance.')
    entries={};groups=collections.defaultdict(list);raw_inputs={};hits=[]
    registry_path=ROOT/historical.DEFAULT_REGISTRY
    if historical_imports and registry_path.is_file():raw_inputs[registry_path]=sha256(registry_path)
    for name,(src,role) in sorted(items.items()):
        recovery.safe_name(name)
        if name in {recovery.DESCRIPTOR,recovery.LOGICAL,recovery.ALIASES,recovery.RECIPES,recovery.SOURCE_DISPOSITIONS,recovery.README,recovery.HELPER,recovery.PHYSICAL} or name.startswith('objects/'):
            raise ValueError('Logical path conflicts with compact recovery metadata: '+name)
        data=src if isinstance(src,bytes) else payload(src)
        # Extension-based privacy MUST use every original logical name, never
        # the suffix-free content-addressed object name.
        hits+=privacy(name,data)
        if hits:raise ValueError('Logical-payload privacy check failed: '+json.dumps(hits,ensure_ascii=False))
        h=digest(data)
        if groups[h]:
            prior=items[groups[h][0]][0];prior_data=prior if isinstance(prior,bytes) else payload(prior)
            if prior_data!=data:raise RuntimeError('A claimed exact duplicate differs in bytes.')
        entries[name]={'path':name,'bytes':len(data),'sha256':h,'role':role}
        groups[h].append(name)
        if not isinstance(src,bytes):raw_inputs[Path(src)]=sha256(src)
    helper_source=ROOT/'work/scripts/restore_checkpoint.py';helper_data=helper_source.read_bytes();helper_hash=digest(helper_data)
    if 'work/scripts/restore_checkpoint.py' not in entries or entries['work/scripts/restore_checkpoint.py']['sha256']!=helper_hash:
        raise RuntimeError('The portable recovery helper must be included in the logical checkpoint.')
    pdf_delta_recipes={};pdf_delta_streams={};pdf_delta_proof=None
    if pdf_delta_plan is not None:
        import checkpoint_pdf_deltas as pdf_delta
        plan_path=Path(pdf_delta_plan).resolve()
        plan_name=rel(plan_path);plan_data=plan_path.read_bytes()
        if (plan_name not in entries or entries[plan_name]['sha256']!=digest(plan_data) or
                entries[plan_name]['bytes']!=len(plan_data)):
            raise RuntimeError('The exact PDF-delta plan must already be a collected logical payload.')
        pdf_delta_recipes,pdf_delta_streams,pdf_delta_proof=pdf_delta.qualify(items,entries,groups,payload,
            json.loads(plan_data),source_checkpoint,pdf_delta.book_authorities(entries,inherited))
        pdf_delta_proof['plan']={'logical_path':plan_name,'sha256':digest(plan_data),'bytes':len(plan_data)}
        raw_inputs[plan_path]=digest(plan_data)
    pdfs=[];documents={};eligible=collections.defaultdict(list);png_hashes={r['sha256'] for n,r in entries.items() if n.endswith('.png')}
    for book in BOOKS:
        name='work/build/'+book+'.pdf';row=entries.get(name)
        if not row:raise RuntimeError('Compact checkpoint requires all seven current PDFs.')
        src=items[name][0];data=src if isinstance(src,bytes) else payload(src)
        if digest(data)!=row['sha256']:raise RuntimeError('Current PDF changed during compact preparation.')
        documents[book]=fitz.open(stream=data,filetype='pdf')
        pdfs.append({'reader':book,'logical_path':name,'bytes':row['bytes'],'sha256':row['sha256'],'pages':len(documents[book])})
        ledger_name='work/verification/'+book+'/VISUAL_REVIEW.tsv'
        if ledger_name not in entries:continue
        ledger_src=items[ledger_name][0];ledger_data=ledger_src if isinstance(ledger_src,bytes) else payload(ledger_src)
        if digest(ledger_data)!=entries[ledger_name]['sha256']:raise RuntimeError('Review ledger changed during compact preparation.')
        for review in csv.DictReader(io.StringIO(ledger_data.decode()),delimiter='\t'):
            if (review.get('status')!='reviewed' or not review.get('reviewer','').strip() or not review.get('observations','').strip()
                or review.get('pdf_sha256')!=row['sha256'] or review.get('image_width')!='900'
                or review.get('png_sha256') not in png_hashes):continue
            if not re.fullmatch(r'page_\d+\.png',review.get('full_page_image','')):continue
            image_path=WORK/'verification'/book/review['full_page_image']
            eligible[review['png_sha256']].append((book,review,ledger_name,image_path))
    recipes={};rejected=[]
    try:
        for index,(h,choices) in enumerate(sorted(eligible.items()),1):
            accepted=None;errors=[]
            for book,review,ledger_name,image_path in choices:
                try:
                    original=image_path.read_bytes()
                    if digest(original)!=h:raise ValueError('review image hash differs')
                    representative=items[groups[h][0]][0]
                    representative=representative if isinstance(representative,bytes) else payload(representative)
                    if representative!=original:raise ValueError('logical PNG bytes differ from the actual reviewed image')
                    number=int(review['page']);doc=documents[book]
                    if not 1<=number<=len(doc):raise ValueError('page outside saved PDF')
                    page=doc[number-1];scale=900/page.rect.width
                    pix=page.get_pixmap(matrix=fitz.Matrix(scale,scale),colorspace=fitz.csRGB,alpha=False,annots=True,clip=None)
                    regenerated=pix.tobytes('png');rgb=recovery.rgb_record(pix)
                    decoded=recovery.rgb_record(fitz.Pixmap(original))
                    if (regenerated!=original or rgb!=decoded or rgb['width']!=int(review['image_width']) or
                        rgb['height']!=int(review['image_height']) or rgb['dimensioned_rgb_sha256']!=review['rendered_pixel_sha256']):
                        raise ValueError('native PNG bytes or dimensioned RGB differ')
                    pdf=entries['work/build/'+book+'.pdf']
                    accepted={'id':'png-'+h,'kind':'pymupdf-full-page-rgb-png',
                      'source_pdf':{'logical_path':pdf['path'],'logical_path_at_capture':pdf['path'],'bytes':pdf['bytes'],'sha256':pdf['sha256']},
                      'physical_page':number,'page_rect_pt':list(page.rect),'page_rotation':page.rotation,
                      'render':{'target_width_px':900,'scale_hex':scale.hex(),'matrix':[scale,0,0,scale,0,0],
                        'colorspace':'DeviceRGB','alpha':False,'annotations':True,'clip':None,'full_page':True,'png_writer':"Pixmap.tobytes('png')"},
                      'expected':{'bytes':len(original),'png_sha256':h,**rgb},
                      'engine':{'pymupdf':recovery.PYMUPDF_VERSION,'mupdf':recovery.MUPDF_VERSION},
                      'qualification':{'ledger_logical_path':ledger_name,'ledger_sha256':entries[ledger_name]['sha256'],
                        'reviewed_row':review,'review_image_original_path':rel(image_path),
                        'actual_png_bytes_compared':True,'decoded_dimensioned_rgb_compared':True,
                        'new_visual_review_claims':False}}
                    trace_name='work/verification/'+book+'.verification.json'
                    if trace_name in entries:
                        trace_src=items[trace_name][0];trace=trace_src if isinstance(trace_src,bytes) else payload(trace_src)
                        if json.loads(trace).get('sha256')==pdf['sha256']:
                            accepted['source_scan_trace']={'logical_path':trace_name,'bytes':len(trace),
                              'sha256':digest(trace),'pdf_sha256':pdf['sha256']}
                    raw_inputs[image_path]=h
                    break
                except (ValueError,OSError,KeyError) as error:errors.append(str(error))
            if accepted:recipes[h]=accepted
            else:rejected.append({'png_sha256':h,'disposition':'stored original payload','reasons':errors})
            if index%100==0:print('Proved compact PNG hashes: '+str(index)+'/'+str(len(eligible)),flush=True)
    finally:
        for doc in documents.values():doc.close()
    if inherited:
        old_documents={}
        try:
            candidates=[(h,r) for h,r in inherited['recipes'].items() if h not in recipes]
            for index,(h,recipe) in enumerate(candidates,1):
                def read_inherited(pin):
                    src=items[pin['logical_path']][0]
                    data=src if isinstance(src,bytes) else payload(src)
                    if digest(data)!=pin['sha256'] or len(data)!=pin['bytes']:
                        raise RuntimeError('Inherited immutable recovery input changed.')
                    return data
                regenerated=recovery.recover_recipe(recipe,read_inherited,read_inherited,old_documents)
                src=items[groups[h][0]][0];original=src if isinstance(src,bytes) else payload(src)
                if regenerated!=original or recovery.rgb_record(fitz.Pixmap(original))!={k:recipe['expected'][k] for k in ('width','height','dimensioned_rgb_sha256')}:
                    raise RuntimeError('Inherited PNG recipe differs from the current logical payload.')
                recipe['inheritance_revalidation']={'native_png_bytes_compared':True,
                  'decoded_dimensioned_rgb_compared':True,'new_visual_review_claims':False}
                recipes[h]=recipe
                if index%100==0:print('Reproved inherited PNG hashes: '+str(index)+'/'+str(len(candidates)),flush=True)
        finally:
            for doc in old_documents.values():doc.close()
    native_recipes,extra_items,native_inputs,native_report=native.qualify(items,entries,groups,payload,recipes)
    def add_recovery_items(extra_items):
        for name,(content,role) in extra_items.items():
            recovery.safe_name(name)
            hits=privacy(name,content)
            if hits:raise ValueError('Recovery input privacy check failed: '+json.dumps(hits,ensure_ascii=False))
            h=digest(content)
            if name in entries:
                if entries[name]['sha256']!=h or entries[name]['bytes']!=len(content):
                    raise RuntimeError('A literal recovery-input path changed.')
            else:
                items[name]=(content,role)
                entries[name]={'path':name,'bytes':len(content),'sha256':h,'role':role}
                groups[h].append(name)
    add_recovery_items(extra_items)
    recipes.update(native_recipes)
    rejected+=native_report['rejected_candidates_stored_in_full']
    overview_recipes,overview_extras,overview_inputs,overview_report=overview.qualify(items,entries,groups,payload,recipes)
    add_recovery_items(overview_extras)
    recipes.update(overview_recipes)
    rejected+=overview_report['rejected_candidates_stored_in_full']
    # Literal canvases and all non-PNG input objects must remain blobs, even
    # in the unlikely case that one shares an image hash with a candidate.
    forced_blobs={r['canvas']['sha256'] for r in recipes.values() if r['kind'] in {recovery.COMPOSITE_KIND,recovery.OVERVIEW_KIND}}
    for h in forced_blobs:recipes.pop(h,None)
    logical=[];aliases=[];objects={};canonical={}
    for h,names in sorted(groups.items()):
        name='work/scripts/restore_checkpoint.py' if h==helper_hash else sorted(names)[0]
        canonical[h]=name
        for member in sorted(names):
            row=dict(entries[member],storage_kind='',object_path='',target_path='',recipe_id='')
            if member!=name:
                row.update(storage_kind='alias',target_path=name)
                aliases.append({'alias_path':member,'target_path':name,'bytes':row['bytes'],'sha256':h})
            elif h in pdf_delta_recipes:
                row.update(storage_kind='pdf_delta',object_path=pdf_delta_recipes[h]['target_object_path'],recipe_id=pdf_delta_recipes[h]['id'])
            elif h in recipes:row.update(storage_kind='png_recipe',recipe_id=recipes[h]['id'])
            else:
                object_path=recovery.HELPER if h==helper_hash else 'objects/sha256/'+h
                row.update(storage_kind='blob',object_path=object_path)
                objects[object_path]=(items[member][0],row)
            logical.append(row)
    by_name={r['path']:r for r in logical}
    for recipe in recipes.values():
        native.bind_object_pins(recipe,by_name)
        if recipe['kind'] in {recovery.COMPOSITE_KIND,recovery.OVERVIEW_KIND}:
            for panel in recipe['panels']:
                source=panel.get('source_png',{})
                if source.get('recipe_id'):
                    dependency=recipes[source['sha256']]
                    if dependency['kind'] not in {recovery.FULL_PAGE_KIND,recovery.NATIVE_KIND}:
                        raise RuntimeError('A composed sheet may depend only on a direct PDF/PNG primitive.')
    logical_data=tsv_bytes(sorted(logical,key=lambda r:r['path']),recovery.LOGICAL_FIELDS)
    alias_data=tsv_bytes(aliases,['alias_path','target_path','bytes','sha256'])
    recipe_data=(json.dumps({'schema':'lm-checkpoint-png-recipes-v3','recipes':list(recipes.values()),
      'rejected_candidates_stored_in_full':rejected,'rendering_is_not_visual_inspection':True},ensure_ascii=False,indent=2)+'\n').encode()
    source_sha=sha256(source_checkpoint);source_size=source_checkpoint.stat().st_size;dispositions=[]
    if inherited:prior_inventory=inherited['prior_inventory']
    else:
        prior_inventory=[]
        with zipfile.ZipFile(source_checkpoint) as oldzip:
            oldnames=oldzip.namelist()
            if len(oldnames)!=len(set(oldnames)):raise RuntimeError('Prior checkpoint has duplicated ZIP paths.')
            oldmanifest={r['path']:r for r in csv.DictReader(io.StringIO(oldzip.read('MANIFEST.tsv').decode()),delimiter='\t')}
            if set(oldmanifest)!=set(oldnames)-{'MANIFEST.tsv'}:raise RuntimeError('Prior checkpoint manifest is incomplete.')
            for name in sorted(oldnames):
                data=oldzip.read(name);h=digest(data)
                if name!='MANIFEST.tsv' and (h!=oldmanifest[name]['sha256'] or len(data)!=int(oldmanifest[name]['bytes'])):
                    raise RuntimeError('Prior checkpoint payload differs from its manifest.')
                prior_inventory.append({'path':name,'bytes':len(data),'sha256':h,'namespace':'ordinary'})
    for prior_row in sorted(prior_inventory,key=lambda r:r['path']):
            name=prior_row['path'];h=prior_row['sha256']
            if prior_row.get('exact_target_path'):
                target=by_name[prior_row['exact_target_path']];namespace='logical'
                state='PRESERVED_EXACT_AT_OTHER_PATH';reason='Exact prior compact container metadata is retained at its immutable history path.'
            elif name=='MANIFEST.tsv' and not inherited:
                target={'path':recovery.LOGICAL,'bytes':len(logical_data),'sha256':digest(logical_data)}
                state='SUPERSEDED_CONTAINER_MANIFEST';namespace='container';reason='The compact logical inventory supersedes the earlier physical payload inventory.'
            elif name in by_name:
                target=by_name[name];namespace='logical'
                state='PRESERVED_EXACT' if h==target['sha256'] else 'SUPERSEDED_CURRENT_LOGICAL_PATH'
                reason='Exact prior bytes recover at the same logical path.' if state=='PRESERVED_EXACT' else 'The current checkpoint deliberately records the updated script, status or audit at the same logical path; the prior checkpoint remains immutable.'
            elif h in canonical:
                target=by_name[canonical[h]];namespace='logical';state='PRESERVED_EXACT_AT_OTHER_PATH';reason='Exact prior bytes recover through the named content-identical logical payload.'
            else:raise RuntimeError('Prior checkpoint entry has no exact preservation or explicit current replacement: '+name)
            dispositions.append({'source_archive':source_checkpoint.name,'source_namespace':prior_row['namespace'],'source_path':name,'source_bytes':prior_row['bytes'],'source_sha256':h,
              'disposition':state,'target_namespace':namespace,'target_path':target['path'],'target_bytes':target['bytes'],
              'target_sha256':target['sha256'],'reason':reason})
    disposition_data=tsv_bytes(dispositions,['source_archive','source_namespace','source_path','source_bytes','source_sha256','disposition','target_namespace','target_path','target_bytes','target_sha256','reason'])
    def reference(name,data,**extra):return {'path':name,'bytes':len(data),'sha256':digest(data),**extra}
    descriptor={'schema':recovery.SCHEMA,'checkpoint_kind':'compact exact-recovery progress checkpoint',
      'logical_manifest':reference(recovery.LOGICAL,logical_data,count=len(logical)),
      'alias_inventory':reference(recovery.ALIASES,alias_data,count=len(aliases)),
      'png_recipes':reference(recovery.RECIPES,recipe_data,count=len(recipes)),
      'source_checkpoint_dispositions':reference(recovery.SOURCE_DISPOSITIONS,disposition_data,count=len(dispositions),unaccounted_prior_entries=0),
      'source_checkpoint':{'filename':source_checkpoint.name,'bytes':source_size,'sha256':source_sha,'entries':len(dispositions)},
      'source_pdfs':pdfs,'recovery_helper':reference(recovery.HELPER,helper_data),
      'engine':{'pymupdf':recovery.PYMUPDF_VERSION,'mupdf':recovery.MUPDF_VERSION},
      'logical_payload_bytes':sum(r['bytes'] for r in logical),'stored_unique_payload_objects':len(objects),
      'proved_recipe_png_hashes':len(recipes),'exact_duplicate_aliases':len(aliases),
      'source_checkpoint_required_for_recovery':False,'logical_payload_privacy_checked':True,
      'all_recipe_pngs_rendered_and_compared_before_omission':True,'new_visual_review_claims':False}
    if pdf_delta_recipes:
        descriptor['pdf_delta_recovery']={'schema':recovery.PDF_DELTA_SCHEMA,'codec':recovery.PDF_DELTA_KIND,
          'maximum_depth':1,'generator_required_for_recovery':False,'new_visual_review_claims':False,
          'recipes':list(pdf_delta_recipes.values())}
        descriptor['pdf_delta_fresh_proof']=pdf_delta_proof
    if historical_imports:descriptor['historical_pdf_imports']=historical_imports
    all_native_inputs={row['path']:row for row in (inherited or {}).get('native_recovery_inputs',[])}
    all_native_inputs.update({row['path']:row for row in native_inputs})
    all_native_inputs.update({row['path']:row for row in overview_inputs})
    descriptor['native_recovery_inputs']=list(all_native_inputs.values())
    descriptor['native_recovery']={'kind_counts':dict(collections.Counter(r['kind'] for r in recipes.values())),
      'fresh_reproof':native_report,'maximum_composite_dependency_depth':1,'composite_engine':recovery.composite_engine(),
      'native_pngs_remain_physical_in_final_delivery':True,'new_visual_review_claims':False}
    descriptor['indexed_overview_recovery']={'kind':recovery.OVERVIEW_KIND,
      'fresh_reproof':overview_report,'maximum_primitive_dependency_depth':1,
      'separate_from_native_no_resize_proofs':True,'new_visual_review_claims':False}
    descriptor['zip_compression_profile']=compression.PROFILE
    if inherited:
        descriptor['source_checkpoint'].update(inventory_kind='compact logical payloads and exact control metadata',
          logical_manifest_sha256=inherited['origin']['logical_manifest_sha256'],
          logical_entries=sum(r['namespace']=='logical' for r in prior_inventory),
          container_entries=sum(r['namespace']=='container' for r in prior_inventory))
        descriptor['inherited_recovery_inputs']=inherited['recovery_inputs']
        descriptor['preserved_prior_controls']=inherited['preserved_control_metadata']
        descriptor['inherited_recipe_count']=sum('inherited_from' in r for r in recipes.values())
    descriptor_data=(json.dumps(descriptor,ensure_ascii=False,indent=2)+'\n').encode()
    readme=('''# Exact compact checkpoint recovery

This progress checkpoint preserves every logical path, byte count, SHA256 and role in LOGICAL_MANIFEST.tsv. It is not a publication approval. Exact duplicates are stored once. Separately qualified recipes recover reviewed900px pages, native PDF proof images, bounded unresized proof sheets, and explicitly indexed supporting overview grids. Every recipe is freshly proved against the original PNG bytes and decoded dimensioned RGB before the payload is omitted. Unsupported or nonidentical images remain stored in full. Historical observations are unchanged; no new visual review is claimed.

Install Python, PyMuPDF==1.26.6 (MuPDF1.26.11), and Pillow==13.0.0 with zlib compile/runtime1.3.2. Extract only restore_checkpoint.py to a working directory, then run:

    python restore_checkpoint.py CHECKPOINT.zip --output-dir restored_checkpoint --verify --report restore_validation.json

The helper validates the ordinary physical MANIFEST.tsv, all logical objects/aliases, and every PNG recipe before writing logical destinations. It refuses symlinked paths and any existing file whose bytes differ; identical existing files are left intact. It then verifies every restored logical hash and emits a machine-readable report. No earlier checkpoint file is required.

COMPACT_CHECKPOINT.json pins the complete logical inventory, alias and recipe inventories, exact seven current source PDFs, engine versions and recovery helper. Older recipes additionally retain immutable PDF and attributed-ledger objects under checkpoint_recovery_inputs; rebuilt work/build filenames never substitute for those bytes. Every inherited recipe is rerendered and compared before omission. ALIASES.tsv points directly to a canonical stored payload or qualified recipe. PNG_RECIPES.json pins PDF bytes, physical page, full-page scale/matrix, RGB/no-alpha/annotation settings, native PNG bytes and dimensioned RGB. SOURCE_CHECKPOINT_DISPOSITIONS.tsv accounts for the prior ordinary members or compact logical files plus exact container metadata. Historical compact control files are retained at immutable checkpoint_history paths. Ordinary unzipping alone does not restore the logical directory tree; use the helper.

Native recipes have a separate exact archived-metadata qualification and do not relax the attributed900px review rule. Sheet recipes retain literal header/background pixels and paste only unresized stored-PNG or direct-PDF primitives at pinned integer offsets. Composite-to-composite references, resizing and font recreation are forbidden. PDF objects, metadata, literal canvases and primitive dependencies are self-contained; recovery does not use an earlier archive or the original workspace. Native proof PNGs remain physical evidence in final ordinary delivery; these compact recipes change checkpoint storage only.

Indexed overview recipes have a distinct kind and do not change the native no-resize contract. They retain the exact pending-review index, immutable discovery snapshot, original source900px PNG/RGB identities, and literal header/background pixels. Only the two original indexed profiles are permitted:900px two-by-two without resizing, or550px four-by-four using the pinned Pillow LANCZOS transform. Both retain exact final PNG bytes and dimensioned RGB. Source pages are inline PDF primitives or direct stored/primitive PNG inputs; composed-sheet dependencies and recreated fonts are forbidden. Historical book PDFs needed for these recipes are explicitly registered whole PDFs, retained with their complete original ordinary-checkpoint MANIFEST and exact member identities. Recovery does not need the source ordinary archives.

An explicitly supplied PDF-delta plan may additionally store up to sixteen named book PDFs as exact depth-one COPY/LITERAL streams against already retained full PDF objects. Every target is reconstructed and byte/SHA256 compared before omission. The inline descriptor inventory pins each base, stream and original target; base/target sets are disjoint and chains are forbidden. Recovery uses only Python's standard library for the delta and requires no Git executable or earlier archive. All original PDF logical paths, byte counts and SHA256 values remain exact, and PNG renderer/recipe contracts are unchanged. The recovery helper verifies every delta target before writing any logical destination. Ordinary final publication PDFs remain complete unchanged PDFs.

Only this compact checkpoint uses a bounded standard ZIP compression profile: qualified UTF-8 text and the fixed root controls use method14 LZMA when its exact stream is smaller than deflate6. All PDF/PNG objects retain deflate6. The ordinary physical MANIFEST and every logical file hash still describe the original payload bytes. Python's standard ZIP reader supports both methods; the standalone recovery helper requires no separate compression utility.
''').encode()
    metadata={recovery.LOGICAL:(logical_data,'complete logical checkpoint payload inventory'),
      recovery.ALIASES:(alias_data,'exact duplicate logical payload aliases'),recovery.RECIPES:(recipe_data,'proved exact PNG recovery recipes'),
      recovery.SOURCE_DISPOSITIONS:(disposition_data,'complete prior checkpoint path dispositions'),
      recovery.DESCRIPTOR:(descriptor_data,'compact checkpoint descriptor'),recovery.README:(readme,'portable exact-recovery instructions')}
    physical_items={name:(src,'unique exact logical payload; see LOGICAL_MANIFEST.tsv') for name,(src,row) in objects.items()}
    physical_items.update({name:(data,'exact depth-one PDF-delta stream; original PDF bytes remain in the logical manifest') for name,data in pdf_delta_streams.items()})
    physical_items.update(metadata)
    for name,(content,_) in metadata.items():
        if privacy(name,content):raise RuntimeError('Compact metadata privacy check failed: '+name)
    prepared=compression.plan(physical_items,payload,
      logical_paths_by_object={name:list(groups[row['sha256']]) for name,(_,row) in objects.items()},
      control_names=[name for name in compression.CONTROL_NAMES if name in physical_items or name==recovery.PHYSICAL])
    if privacy(recovery.PHYSICAL,prepared.manifest):raise RuntimeError('Compact physical manifest privacy check failed.')
    predicted=dict(prepared.summary,limit_bytes=MAX_ARCHIVE_BYTES)
    if predicted['zip_bytes']>MAX_ARCHIVE_BYTES:
        raise RuntimeError(path.name+' would exceed the delivery limit: '+str(predicted['zip_bytes'])+' bytes before ZIP creation.')
    print('Compact archive size preflight: '+str(predicted['zip_bytes'])+' bytes',flush=True)
    if measure_only:
        compiler_context(force=True)
        for src,h in raw_inputs.items():
            if sha256(src)!=h:raise RuntimeError('A measured checkpoint input changed during preparation.')
        if sha256(source_checkpoint)!=source_sha or source_checkpoint.stat().st_size!=source_size:
            raise RuntimeError('Prior checkpoint changed during size planning.')
        return {'status':'MEASURED_WITHOUT_ARCHIVE_WRITE','planned_filename':path.name,**predicted,
          'logical_entries':len(logical),'png_recipes':len(recipes),'alias_entries':len(aliases),
          'inherited_recipe_count':sum('inherited_from' in r for r in recipes.values()),
          'source_checkpoint_sha256':source_sha,'unaccounted_prior_entries':0,
          'native_recovery':descriptor['native_recovery'],
          'indexed_overview_recovery':descriptor['indexed_overview_recovery'],
          'compression_profile':compression.PROFILE,'compression_summary':prepared.summary,
          'pdf_delta_fresh_proof':pdf_delta_proof}
    manifest=prepared.manifest_rows;path.parent.mkdir(parents=True,exist_ok=True);created=False
    try:
        with zipfile.ZipFile(path,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
            created=True
            compression.write_members(z,physical_items,payload,prepared)
        compression.verify_archive(path,prepared)
        for src,h in raw_inputs.items():
            if sha256(src)!=h:raise RuntimeError('A checkpoint input changed during compact packaging.')
        if sha256(source_checkpoint)!=source_sha or source_checkpoint.stat().st_size!=source_size:
            raise RuntimeError('Prior checkpoint changed during compact packaging.')
        compiler_context(force=True)
        checked=recovery.CompactArchive(path);checked.close()
        if path.stat().st_size!=predicted['zip_bytes']:
            raise RuntimeError('Compact archive size differs from its exact preflight.')
    except Exception:
        if created and path.exists():
            failed=path.with_suffix(path.suffix+'.failed');number=1
            while failed.exists():
                failed=path.with_suffix(path.suffix+'.failed'+str(number));number+=1
            path.rename(failed)
        raise
    return {'filename':path.name,'bytes':path.stat().st_size,'sha256':sha256(path),'entries':len(manifest),
      'manifest':manifest,'compact':True,'logical_entries':len(logical),'logical_manifest_sha256':digest(logical_data),
      'png_recipes':len(recipes),'alias_entries':len(aliases),'source_checkpoint_sha256':source_sha,
      'source_checkpoint_entries':len(dispositions),'unaccounted_prior_entries':0,
      'native_recovery':descriptor['native_recovery'],
      'indexed_overview_recovery':descriptor['indexed_overview_recovery'],
      'compression_profile':compression.PROFILE,'compression_summary':prepared.summary,
      'pdf_delta_fresh_proof':pdf_delta_proof}

def checkpoint(part,finished_reader=None,compact=False,source_checkpoint=None,pdf_delta_plan=None):
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
    if compact:status['images']='Every logical PNG payload is retained exactly as a stored object, an exact alias, or a freshly proved self-contained PDF/sheet recipe with immutable inputs. Use the top-level recovery helper; no review claim is added.'
    (REC/'CHECKPOINT_STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
    nums=[int(m[1]) for p in OUT.glob('LM_READERS_checkpoint_*.zip') if (m:=re.fullmatch(r'LM_READERS_checkpoint_(\d+)\.zip',p.name))]
    n=max(nums,default=0)+1;path=OUT/f'LM_READERS_checkpoint_{n:02d}.zip'
    items=common_items(compact,True)
    for book in BOOKS:
        for ext in ['.tex','.pdf']:
            p=WORK/'build'/(book+ext)
            if p.exists():items[rel(p)]=(p,'current reader/master; consult checkpoint status')
    if compact:
        prior=Path(source_checkpoint) if source_checkpoint else OUT/f'LM_READERS_checkpoint_{n-1:02d}.zip'
        result=make_compact_zip(path,items,prior,pdf_delta_plan=pdf_delta_plan)
    else:
        measured=require_archive_size(items,path.name)
        result=make_zip(path,items,expected_size=measured['zip_bytes'])
    ledger=REC/'checkpoint_archives.jsonl'
    with ledger.open('a') as f:f.write(json.dumps({k:v for k,v in result.items() if k!='manifest'},ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='manifest'},ensure_ascii=False))

def final_maps():
    maps={'LM_READERS_FR.zip':{},'LM_READERS_EN.zip':{},'LM_READERS_RECORDS.zip':common_items(True,True,False)}
    from publication_pdf_scope import exclude
    excluded=exclude(maps['LM_READERS_RECORDS.zip'],ROOT,payload)
    maps['LM_READERS_RECORDS.zip']['work/records/NONPUBLICATION_PDF_EXCLUSIONS.json']=(
      (json.dumps({'schema':'lm-exact-nonpublication-pdf-exclusions-v1','records':excluded,
        'scope':'Exact source-qualified working-tree PDFs excluded from the final publication collection. Current final target hashes are joined by the final storage policy and retention table.'},ensure_ascii=False,indent=2)+'\n').encode(),
      'exact working-tree recovery and interrupted PDF scope dispositions')
    for book in BOOKS:
        lang='FR' if '_FR_' in book else 'EN'
        for ext in ['.tex','.pdf']:maps['LM_READERS_'+lang+'.zip'][book+ext]=(WORK/'build'/(book+ext),'self-contained reader/master')
    for lang in ['FR','EN']:
        for name in ['README.md','APPARATUS_COUNTS.md','CHANGES_'+lang+'.tsv']:
            maps['LM_READERS_'+lang+'.zip'][name]=(REC/name,'edition overview or change record')
    return maps

def retention(maps):
    candidates={};hash_to_target={}
    record_items=maps['LM_READERS_RECORDS.zip']
    omitted={};indexed_omitted={};indexed_by_hash={};older_recovery={}
    omission_name='work/records/FULL_PAGE_RASTER_OMISSIONS.tsv'
    if omission_name in record_items:
        src=record_items[omission_name][0];content=src if isinstance(src,bytes) else payload(src)
        for row in csv.DictReader(io.StringIO(content.decode()),delimiter='\t'):omitted.setdefault(row['sha256'],row)
    indexed_name='work/records/INDEXED_REVIEW_GRID_OMISSIONS.tsv'
    if indexed_name in record_items:
        src=record_items[indexed_name][0];content=src if isinstance(src,bytes) else payload(src)
        for row in csv.DictReader(io.StringIO(content.decode()),delimiter='\t'):
            key=(row['path'],row['sha256'],int(row['bytes']))
            if key in indexed_omitted:raise RuntimeError('Duplicate indexed-overview per-file disposition.')
            if (row.get('classification')!='SUPERSEDED_INDEXED_REVIEW_GRID' or
                    row.get('qualification_record')!='work/records/INDEXED_REVIEW_GRID_QUALIFICATIONS.json'):
                raise RuntimeError('Unknown indexed-overview retention qualification.')
            indexed_omitted[key]=row
            previous=indexed_by_hash.get(row['sha256'])
            if previous and any(previous[k]!=row[k] for k in ('bytes','qualification_id','final_archive','final_path','final_sha256')):
                raise RuntimeError('Conflicting indexed-overview exact-hash replacements.')
            indexed_by_hash[row['sha256']]=row
    policy_name='work/records/FINAL_RECORDS_POLICY.json'
    if policy_name in record_items:
        src=record_items[policy_name][0];content=src if isinstance(src,bytes) else payload(src)
        policy=json.loads(content)
        for row in policy.get('older_recovery_pdf_dispositions',[]):older_recovery[(row['path'],row['sha256'])]=row
        for row in policy.get('nonpublication_pdf_dispositions',[]):older_recovery[(row['path'],row['source_pdf_sha256'])]=row
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
            compact='COMPACT_CHECKPOINT.json' in z.namelist()
            if compact:
                import restore_checkpoint as recovery
                checked=recovery.CompactArchive(checkpoint)
                inventory=[(r['path'],int(r['bytes']),r['sha256'],r['storage_kind'],False) for r in checked.logical.values()]
                controls={recovery.DESCRIPTOR,recovery.LOGICAL,recovery.ALIASES,recovery.RECIPES,recovery.SOURCE_DISPOSITIONS,recovery.README,recovery.HELPER,recovery.PHYSICAL}
                inventory += [(name,len(z.read(name)),digest(z.read(name)),'compact container metadata',True) for name in controls]
                checked.close()
            else:
                inventory=[(name,len(z.read(name)),digest(z.read(name)),'ordinary ZIP member',False) for name in sorted(z.namelist()) if not name.endswith('/')]
            for old,nbytes,h,storage,container in sorted(inventory):
                target=hash_to_target.get(h)
                reason='Byte-for-byte identical content retained.';state='preserved'
                if not target:
                    raster=omitted.get(h) if Path(old).suffix.lower()=='.png' else None
                    indexed_raster=indexed_omitted.get((old,h,nbytes)) if Path(old).suffix.lower()=='.png' else None
                    if indexed_raster is None and Path(old).suffix.lower()=='.png':
                        exact_alias=indexed_by_hash.get(h)
                        if exact_alias and int(exact_alias['bytes'])==nbytes:indexed_raster=exact_alias
                    recovery_input=older_recovery.get((old,h))
                    possible=candidates.get(old,[])
                    if not possible and old.startswith('work/build/'):
                        possible=candidates.get(Path(old).name,[])
                    if raster or indexed_raster or recovery_input:
                        replacement=raster or indexed_raster or recovery_input
                        target=next((t for t in candidates.get(replacement['final_path'],[]) if t[0]==replacement['final_archive'] and t[2]==replacement['final_sha256']),None)
                        if target is None:raise RuntimeError('Missing exact publication replacement for packaging disposition: '+old)
                        state='omitted';reason=replacement['reason']
                        if raster:reason+=' Exact raster qualification '+raster['qualification_id']+' is recorded in work/records/FULL_PAGE_RASTER_QUALIFICATIONS.json; original ledger '+raster['retained_ledger_path']+' remains unchanged.'
                        if indexed_raster and not raster:
                            reason+=' EXPLICIT_INDEXED_REVIEW_GRID_OMISSION: exact grid qualification '+indexed_raster['qualification_id']+' is recorded in '+indexed_raster['qualification_record']+'; retained index '+indexed_raster['retained_index_path']+' and snapshot '+indexed_raster['retained_snapshot_path']+' remain unchanged. The named whole-book replacement and current complete ledger '+indexed_raster['final_review_ledger_path']+' do not assert historical-to-final page or pixel identity.'
                    elif possible:
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
                        if container:
                            target=('LM_READERS_RECORDS.zip','MANIFEST.tsv','');state='superseded container metadata'
                            reason='Compact checkpoint recovery/container metadata, not an omitted logical payload. The immutable checkpoint retains its recovery inventories; the final ZIP MANIFEST.tsv inventories the final physical files.'
                if compact and not container:reason+=' The checkpoint logical file is recovered through its verified '+storage+' mapping.'
                out.append({'checkpoint':checkpoint.name,'checkpoint_path':old,'checkpoint_bytes':nbytes,'checkpoint_sha256':h,
                  'disposition':state,'final_archive':target[0],'final_path':target[1],'final_sha256':target[2],'reason':reason})
    return out

def preflight(maps):
    """Check the complete release before creating any of its three ZIPs."""
    expected={b+'.pdf' for b in BOOKS}
    pdfs=[(archive,path) for archive,items in maps.items() for path in items if Path(path).suffix.lower()=='.pdf']
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
    sizes={name:require_archive_size(items,name,65536) for name,items in maps.items()}
    return {'status':'PASS','files':files,'uncompressed_bytes':total_bytes,'publication_pdfs':len(pdfs),
            'checkpoint_entries':len(retained),'unexplained_omissions':0,'privacy_findings':0,
            'archive_size_preflight':sizes,'reserved_for_preflight_record_bytes':65536,
            'size_gate':'Each final ZIP is measured again after adding this record and must match its exact deflate size.'}

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
    expected_pdfs={(archive,path):src for archive,items in maps.items() for path,(src,role) in items.items() if Path(path).suffix.lower()=='.pdf'}
    audited_pdfs={(r.get('archive'),r.get('path')):r for r in pdf_privacy.get('files',[])}
    if set(audited_pdfs)!=set(expected_pdfs):raise RuntimeError('Expanded PDF privacy inventory is stale')
    for key,src in expected_pdfs.items():
        audit=audited_pdfs[key]
        if not audit.get('stable_during_audit') or audit.get('sha256')!=sha256(src):
            raise RuntimeError('Expanded PDF privacy hash is stale: '+key[1])
    from final_records_policy import apply as apply_records_policy
    policy=apply_records_policy(maps,ROOT,payload,privacy,tsv_bytes)
    from final_language_proof_assets import apply as distribute_proof_assets
    distribution=distribute_proof_assets(maps,policy,ROOT,payload,tsv_bytes)
    record_items=maps['LM_READERS_RECORDS.zip']
    for name,content in policy['generated'].items():(REC/name).write_bytes(content)
    retained=retention(maps);retained_data=tsv_bytes(retained,['checkpoint','checkpoint_path','checkpoint_bytes','checkpoint_sha256','disposition','final_archive','final_path','final_sha256','reason'])
    (REC/'CHECKPOINT_RETENTION.tsv').write_bytes(retained_data)
    record_items['work/records/CHECKPOINT_RETENTION.tsv']=(retained_data,'file-by-file checkpoint retention and supersession')
    readme=(REC/'README.md').read_bytes();record_items['README.md']=(readme,'top-level edition overview')
    privacy_report={'status':'PASS','scope':'Every packaged text file plus every PDF text layer and metadata; ZIP bytes match manifest digests. The additional hash-bound PDF audit covers object dictionaries, decoded strings, annotation/action targets and embedded-file absence. Binary font/image streams are not interpreted. Interpreter shebangs are executable conventions, not private paths.','expanded_pdf_audit':'work/data/pdf_privacy_audit.json','expanded_pdf_count':len(audited_pdfs),'local_path_findings':[],'email_findings':[]}
    record_items['work/records/PRIVACY_AUDIT.json']=(json.dumps(privacy_report,indent=2).encode(),'privacy-check scope and result')
    checks=preflight(maps)
    record_items['work/records/FINAL_ARCHIVE_PREFLIGHT.json']=(json.dumps(checks,indent=2).encode(),'whole-release preflight before any final archive is created')
    exact_sizes={archive:require_archive_size(items,archive) for archive,items in maps.items()}
    results=[]
    for archive,items in maps.items():
        result=make_zip(OUT/archive,items,exclusive=True,expected_size=exact_sizes[archive]['zip_bytes']);results.append({k:v for k,v in result.items() if k!='manifest'})
        print(json.dumps(results[-1],ensure_ascii=False),flush=True)
    (REC/'ARCHIVE_MANIFESTS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')

def final_size():
    """Read-only size plan; run only after current PDFs and traces are stable."""
    from final_records_policy import apply as apply_records_policy
    maps=final_maps();policy=apply_records_policy(maps,ROOT,payload,privacy,tsv_bytes)
    from final_language_proof_assets import apply as distribute_proof_assets
    distribution=distribute_proof_assets(maps,policy,ROOT,payload,tsv_bytes)
    sizes={name:measure_zip(items) for name,items in maps.items()}
    print(json.dumps({'policy':policy['summary'],'distribution':distribution['summary'],'archives':sizes,
      'all_within_limit_before_final_retention_metadata':all(r['zip_bytes']<=MAX_ARCHIVE_BYTES for r in sizes.values()),
      'note':'Read-only collection plan; final() additionally includes exact checkpoint retention, privacy and preflight records and remeasures every archive.'},ensure_ascii=False,indent=2))

def checkpoint_size(source_checkpoint,pdf_delta_plan=None):
    """Prove and measure the current compact collection without writing a ZIP."""
    nums=[int(m[1]) for p in OUT.glob('LM_READERS_checkpoint_*.zip') if (m:=re.fullmatch(r'LM_READERS_checkpoint_(\d+)\.zip',p.name))]
    n=max(nums,default=0)+1;path=OUT/f'LM_READERS_checkpoint_{n:02d}.zip'
    prior=Path(source_checkpoint) if source_checkpoint else OUT/f'LM_READERS_checkpoint_{n-1:02d}.zip'
    items=common_items(True,True)
    for book in BOOKS:
        for ext in ['.tex','.pdf']:
            p=WORK/'build'/(book+ext)
            if p.exists():items[rel(p)]=(p,'current reader/master; consult checkpoint status')
    print(json.dumps(make_compact_zip(path,items,prior,measure_only=True,pdf_delta_plan=pdf_delta_plan),ensure_ascii=False,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();sp=ap.add_subparsers(dest='command',required=True)
    c=sp.add_parser('checkpoint');c.add_argument('--part',required=True);c.add_argument('--finished-reader',choices=BOOKS)
    c.add_argument('--compact',action='store_true',help='Exact-deduplicated checkpoint with proved full-page PNG recipes and portable recovery.')
    c.add_argument('--source-checkpoint',help='Prior ordinary or compact checkpoint to account for; defaults to the preceding checkpoint.')
    c.add_argument('--pdf-delta-plan',help='Explicit exact depth-one book-PDF plan; compact checkpoints only.')
    sp.add_parser('final');sp.add_parser('final-size')
    s=sp.add_parser('checkpoint-size');s.add_argument('--source-checkpoint');s.add_argument('--pdf-delta-plan')
    a=ap.parse_args()
    if a.command=='checkpoint':
        if a.source_checkpoint and not a.compact:ap.error('--source-checkpoint is only used with --compact')
        if a.pdf_delta_plan and not a.compact:ap.error('--pdf-delta-plan is only used with --compact')
        checkpoint(a.part,a.finished_reader,a.compact,a.source_checkpoint,a.pdf_delta_plan)
    elif a.command=='final-size':final_size()
    elif a.command=='checkpoint-size':checkpoint_size(a.source_checkpoint,a.pdf_delta_plan)
    else:final()
