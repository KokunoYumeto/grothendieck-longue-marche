#!/usr/bin/env python3
"""Assemble the final report from measured results and actual review records.

This script never generates visual observations. A strict release requires
current PDF hashes, all numerical gates, and attributed hash-bound reviews.
Use --allow-pending only to preserve an explicitly unfinished checkpoint.
"""
from __future__ import annotations
import argparse, collections, csv, datetime, hashlib, json, re
from pathlib import Path
from verify_pdf import sha256, sanitize, parse_log, read_visual_review

ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'work'; REC=WORK/'records'; DATA=WORK/'data'; VERIFY=WORK/'verification'
BOOKS=['LM_FR_diplomatique','LM_FR_corrige_apparat','LM_FR_texte_de_lecture',
       'LM_EN_corrected_apparatus','LM_EN_reading','LM_FR_master_annotated','LM_EN_master_annotated']

def read_json(p): return json.loads(Path(p).read_text())
def rows(p):
    p=Path(p)
    if not p.exists():return []
    with p.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def write_tsv(p,items,fields):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n',extrasaction='ignore')
        w.writeheader();w.writerows(items)
def cell(s):return str(s).replace('|',r'\|').replace('\n',' / ').replace('\r','')
def pages(xs):return ', '.join(str(x) for x in xs) if xs else 'none'
def table(headers,items):
    return ['| '+' | '.join(headers)+' |','|'+'|'.join('---' for _ in headers)+'|']+[
        '| '+' | '.join(cell(x) for x in r)+' |' for r in items]

def warning_blocks(raw):
    lines=raw.splitlines();out=[]
    pattern=re.compile(r'^(?:LaTeX(?: Font)?|Package [^\n]+?|Class [^\n]+?) Warning:')
    for i,line in enumerate(lines):
        if not pattern.match(line):continue
        block=[line];j=i+1
        while j<len(lines) and lines[j].strip() and (lines[j].startswith(('(', ' ', '\t'))):
            # Parenthesized package labels are warning continuations. File-open
            # records begin a new event and must not become warning prose.
            if lines[j].startswith(('(/','(./')):break
            block.append(lines[j]);j+=1
        message=sanitize('\n'.join(block))
        category=('margin placement' if 'Marginpar on page' in line else
                  'font substitution' if 'Font Warning' in line else
                  'unicode-math compatibility' if 'unicode-math Warning' in line else
                  'shell escape disabled' if 'epstopdf Warning' in line else 'other')
        out.append({'log_line':i+1,'category':category,'message':message})
    return out

def refresh_logs():
    warnings=[]
    for stage,directory in [('baseline',WORK/'baseline'),('final',WORK/'build')]:
        target=REC/'logs'/stage;target.mkdir(parents=True,exist_ok=True)
        for book in BOOKS:
            src=directory/(book+'.log')
            if not src.exists():continue
            raw=src.read_text(errors='replace')
            (target/src.name).write_text(sanitize(raw))
            for n,w in enumerate(warning_blocks(raw),1):warnings.append({'stage':stage,'reader':book,'warning':n,**w})
    write_tsv(REC/'LATEX_WARNINGS.tsv',warnings,['stage','reader','warning','log_line','category','message'])
    return warnings

def assess(book):
    vf=VERIFY/(book+'.verification.json');pdf=WORK/'build'/(book+'.pdf');tex=pdf.with_suffix('.tex')
    if not vf.exists() or not pdf.exists() or not tex.exists():return None,[book+': build or verification missing']
    v=read_json(vf);failures=[]
    if sha256(pdf)!=v['sha256']:failures.append(book+': verification PDF hash is stale')
    current_log=parse_log(pdf.with_suffix('.log'))
    if current_log!=v['log_after']:failures.append(book+': verification log is stale')
    visual=read_visual_review(VERIFY/book,v['sha256'],v['selected_pages'])
    v['visual_review']=visual;v['gates']['visual_review_complete']=visual['complete']
    vf.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
    for gate,passed in v['gates'].items():
        if not passed:failures.append(book+': '+gate)
    baseline=WORK/'verification_baseline'/(book+'.verification.json')
    if not baseline.exists():failures.append(book+': baseline measurement missing')
    return v,failures

def assess_pagination():
    """Require the final, actually reviewed, source-qualified pagination audit."""
    from pagination_extensions import frozen_extensions
    from verify_pagination_final import baseline_check, known_id, retained_tag_source_errors
    path=DATA/'pagination_verification_final.json';failures=[]
    if not path.exists():return {},['Final source-qualified pagination audit is missing']
    audit=read_json(path)
    if audit.get('status')!='PASS' or audit.get('unresolved'):
        failures.append('Final source-qualified pagination audit is not PASS')
    files=audit.get('files',[])
    if len(files)!=len(BOOKS) or {r.get('reader') for r in files}!=set(BOOKS):
        failures.append('Final pagination audit does not cover exactly the seven required PDFs')
    for r in files:
        if r.get('reader') not in BOOKS:continue
        if not r.get('stable_during_audit') or r.get('sha256')!=sha256(WORK/'build'/(r['reader']+'.pdf')):
            failures.append(r['reader']+': final pagination audit belongs to a different PDF')
    for key in ['queue','baseline','source_bindings','applied_repairs','source_reconciliation','scanner',
                'known_extensions','extension_initial_snapshot','extension_initial_inventory']:
        evidence=audit.get(key,{})
        p=ROOT/evidence.get('path','__missing__')
        if not p.is_file() or evidence.get('sha256')!=sha256(p):
            failures.append('Pagination supporting evidence is missing or stale: '+key)
    known=audit.get('known_detachments',[])
    try:
        baseline=read_json(DATA/'pagination_review_before_repairs.json');baseline_check(baseline)
        expected_original={known_id(r) for r in baseline['candidates'] if r['decision']=='confirmed detached tag'}
        extensions=frozen_extensions()
        expected_extensions={r['id'] for r in extensions['primary_witnesses']}
        expected_masters={r['id'] for r in extensions['master_witnesses']}
    except (ValueError,KeyError,TypeError,OSError):
        failures.append('The original pagination baseline or additive historical inventory is invalid')
        expected_original=set();expected_extensions=set();expected_masters=set()
    expected_known=expected_original|expected_extensions
    if (len(expected_original)!=80 or expected_original.intersection(expected_extensions) or
            len(known)!=len(expected_known) or {r.get('id') for r in known}!=expected_known):
        failures.append('Final pagination audit does not close the original80 and every additive observed instance')
    if any(r.get('status')!='RESOLVED_ON_FINAL_PDF' or r.get('validation_errors') for r in known):
        failures.append('A known equation-tag detachment lacks final-image closure')
    candidates=audit.get('final_candidates',[])
    for r in candidates:
        required='CLEARED_BY_MASTER_PIXEL_IDENTITY' if 'master' in r.get('reader','') else 'CLEARED_ON_FINAL_PDF'
        if r.get('status')!=required or r.get('validation_errors'):
            failures.append('A final equation-tag pagination candidate is unresolved: '+str(r.get('id')))
    for r in known+candidates:
        ob=r.get('final_observation')
        if ob:
            if not ob.get('reviewer') or not ob.get('observation') or ob.get('pdf_sha256')!=r.get('pdf_sha256'):
                failures.append('Final pagination image observation is incomplete: '+str(r.get('id')))
            if ob.get('classification')=='RETAINED_TAG_AFTER_FULLY_CANCELLED_DISPLAY':
                if ob.get('display_pages')!=[] or retained_tag_source_errors(r,ob):
                    failures.append('Retained empty equation tag lacks exact source justification: '+str(r.get('id')))
            elif not ob.get('display_pages') or set(ob['display_pages'])!={ob.get('tag_page')}:
                failures.append('Final equation number and complete display are not together: '+str(r.get('id')))
            for im in ob.get('images',[]):
                p=ROOT/im.get('path','__missing__')
                if not p.is_file() or im.get('sha256')!=sha256(p):
                    failures.append('Final pagination image changed: '+str(r.get('id')))
        elif 'master' not in r.get('reader',''):
            failures.append('Final pagination image observation is absent: '+str(r.get('id')))
    comparisons=audit.get('master_comparisons',[])
    if {r.get('master') for r in comparisons}!={'LM_FR_master_annotated','LM_EN_master_annotated'}:
        failures.append('Pagination master-identity evidence is incomplete')
    for r in comparisons+audit.get('observation_records',[]):
        p=ROOT/r.get('path','__missing__')
        if not p.is_file() or r.get('sha256')!=sha256(p):
            failures.append('Pagination review/comparison record is stale: '+str(r.get('path')))
        if 'master' in r and (r.get('status')!='PASS' or r.get('validation_errors')):
            failures.append('Pagination master-identity comparison is not PASS: '+r['master'])
    master_extensions=audit.get('known_master_transfers',[])
    if (len(master_extensions)!=len(expected_masters) or
            {r.get('id') for r in master_extensions}!=expected_masters):
        failures.append('Final pagination historical master transfers are incomplete or duplicated')
    by_id={r.get('id'):r for r in known};pdf_hashes={r.get('reader'):r.get('sha256') for r in files}
    for r in master_extensions:
        primary=by_id.get(r.get('source_known_id'),{})
        comparison=ROOT/r.get('master_comparison','__missing__')
        if (r.get('status')!='RESOLVED_BY_MASTER_PIXEL_IDENTITY' or r.get('validation_errors') or
                r.get('pdf_sha256')!=pdf_hashes.get(r.get('reader')) or
                primary.get('status')!='RESOLVED_ON_FINAL_PDF' or
                r.get('source_final_pdf_sha256')!=primary.get('pdf_sha256') or
                r.get('source_final_observation')!=primary.get('final_observation') or
                not r.get('final_pages') or r.get('final_pages')!=primary.get('final_pages') or
                not comparison.is_file() or r.get('master_comparison_sha256')!=sha256(comparison)):
            failures.append('An additive historical master witness lacks exact current closure: '+str(r.get('id')))
    counts=audit.get('counts',{})
    if (counts.get('known_detachments')!=len(expected_known) or counts.get('resolved_known_detachments')!=len(expected_known) or
            counts.get('original_known_detachments')!=80 or
            counts.get('extension_primary_witnesses')!=len(expected_extensions) or
            counts.get('extension_master_transfers')!=len(expected_masters) or
            counts.get('resolved_extension_master_transfers')!=len(expected_masters) or
            counts.get('final_primary_candidates')!=counts.get('cleared_primary_candidates') or
            counts.get('final_master_candidates')!=counts.get('cleared_master_candidates') or counts.get('unresolved')!=0):
        failures.append('Final pagination completion counts do not agree')
    return audit,failures

def assess_heading_closure():
    path=DATA/'heading_closure_final.json';failures=[]
    if not path.exists():return {},['Final marginal-note/section heading audit is missing']
    audit=read_json(path);readers=audit.get('readers',[]);witnesses=audit.get('witnesses',[])
    if audit.get('status')!='PASS' or audit.get('expected_witnesses')!=10 or audit.get('pass_count')!=10:
        failures.append('Final marginal-note/section heading audit is not PASS for all10 witnesses')
    primary={b+'.pdf' for b in BOOKS if 'master' not in b}
    if len(readers)!=5 or {r.get('file') for r in readers}!=primary:
        failures.append('Heading audit does not cover exactly the five primary readers')
    hashes={r.get('file','').removesuffix('.pdf'):r.get('sha256') for r in readers}
    for r in readers:
        if r.get('file') not in primary:continue
        pdf=WORK/'build'/r['file']
        if r.get('sha256')!=sha256(pdf) or r.get('tex_sha256')!=sha256(pdf.with_suffix('.tex')):
            failures.append(r['file']+': heading audit belongs to different final bytes')
    if len(witnesses)!=10 or len({r.get('key') for r in witnesses})!=10:
        failures.append('Heading witness inventory is incomplete')
    for r in witnesses:
        if (r.get('status')!='PASS' or not r.get('reviewer') or not r.get('observation') or
                not r.get('source_id') or not r.get('evidence') or r.get('pdf_sha256')!=hashes.get(r.get('reader'))):
            failures.append('Heading witness lacks hash-bound actual review: '+str(r.get('key')))
        for e in r.get('evidence',[]):
            p=ROOT/e.get('image','__missing__')
            if not p.is_file() or e.get('sha256')!=sha256(p):
                failures.append('Heading evidence image is stale: '+str(r.get('key')))
        p=ROOT/r.get('source_path','__missing__')
        if not p.is_file() or r.get('source_file_sha256')!=sha256(p):
            failures.append('Heading source witness is stale: '+str(r.get('key')))
    return audit,failures

def assess_visual_issue_closure():
    path=DATA/'final_visual_issue_closure.json';failures=[]
    if not path.exists():return {},['Final native-image issue closure record is missing']
    audit=read_json(path)
    if audit.get('status')!='PASS':failures.append('Final native-image issue closure is not PASS')
    # The import manifest pins the pre-commit central ledger deliberately.
    # That one input must match the exclusive backup; all other pinned inputs
    # must still match their current files. Never waive the ledger hash check.
    import_path=DATA/'native_closure_import_check.json'
    if not import_path.is_file():
        failures.append('Committed native-image importer provenance is missing')
    else:
        try:
            provenance=read_json(import_path)
            if (provenance.get('schema')!='native-closure-import-check-v1' or
                    provenance.get('status')!='PASS' or provenance.get('action')!='COMMITTED' or
                    provenance.get('publication_ledger_changed') is not True or
                    provenance.get('visual_observations_generated_by_script') is not False or
                    provenance.get('errors')!=[]):
                failures.append('Native-image importer provenance is not a successful committed import')
            if provenance.get('ledger_sha256')!=sha256(path):
                failures.append('Native-image importer does not name the current central ledger bytes')
            def evidence_path(name):
                if not isinstance(name,str) or not name or Path(name).is_absolute():
                    raise ValueError('Importer evidence path is not project-relative')
                resolved=(ROOT/name).resolve()
                resolved.relative_to(ROOT.resolve())
                return resolved
            def protected_digest(ledger):
                protected=[{k:v for k,v in row.items() if k not in {'status','publication_confirmations'}}
                           for row in ledger['findings']]
                return hashlib.sha256(json.dumps(protected,sort_keys=True,ensure_ascii=False,
                                                 separators=(',',':')).encode()).hexdigest()
            prior=provenance.get('prior_ledger_sha256')
            backup=provenance.get('backup',{})
            backup_path=evidence_path(backup.get('path'))
            if (not isinstance(prior,str) or not re.fullmatch(r'[0-9a-f]{64}',prior) or
                    backup_path==path.resolve() or not backup_path.is_file() or
                    backup.get('sha256')!=prior or sha256(backup_path)!=prior):
                failures.append('Native-image importer prior-ledger backup is missing or stale')
            else:
                if protected_digest(read_json(backup_path))!=protected_digest(audit):
                    failures.append('Native-image importer changed original finding definitions or detected evidence')
            metadata=audit.get('native_finalization',{})
            if (metadata.get('schema')!='native-ledger-import-v1' or
                    metadata.get('prior_ledger_sha256')!=prior or
                    metadata.get('confirmations_imported_by_script') is not True or
                    metadata.get('visual_observations_generated_by_script') is not False or
                    metadata.get('protected_findings_sha256')!=protected_digest(audit) or
                    provenance.get('protected_findings_sha256')!=protected_digest(audit)):
                failures.append('Native-image importer finalization identity differs from the central ledger')
            pinned=provenance.get('inputs',[])
            input_paths=[evidence_path(item.get('path')) for item in pinned]
            required={path.resolve(),(ROOT/'sources/en/MANIFEST.json').resolve(),
                      (DATA/'layout_repairs_applied.json').resolve(),
                      (DATA/'generated_heading_repairs.json').resolve()}
            required.update((WORK/'build'/(book+suffix)).resolve()
                            for book in BOOKS for suffix in ('.pdf','.tex','.lm-scans.tsv'))
            required.update((WORK/'build'/(language+'_source_marks.json')).resolve()
                            for language in ('fr','en'))
            primary=[book for book in BOOKS if 'master' not in book]
            required.update((DATA/directory/(book+'.json')).resolve() for book in primary
                            for directory in ('final_native_closure_queues','final_native_closure_validated'))
            required.update((VERIFY/(language+'_MASTER_PIXEL_IDENTITY.json')).resolve()
                            for language in ('FR','EN'))
            if (not pinned or len(input_paths)!=len(set(input_paths)) or
                    not required<=set(input_paths) or input_paths.count(path.resolve())!=1 or
                    backup_path in input_paths):
                failures.append('Native-image importer pinned input inventory is incomplete or ambiguous')
            for item,input_path in zip(pinned,input_paths):
                expected=item.get('sha256')
                if input_path==path.resolve():
                    if expected!=prior or backup.get('sha256')!=expected:
                        failures.append('Native-image importer pre-commit ledger pin does not match its backup')
                elif not input_path.is_file() or expected!=sha256(input_path):
                    failures.append('Native-image importer input is missing or stale: '+str(item.get('path')))
        except (ValueError,KeyError,TypeError,OSError,AttributeError):
            failures.append('Native-image importer commit provenance is malformed or unreadable')
    finding_ids=[r.get('id') for r in audit.get('findings',[])]
    if not finding_ids or len(finding_ids)!=len(set(finding_ids)):
        failures.append('Final native-image finding inventory is empty or has duplicate identities')
    for r in audit.get('findings',[]):
        if r.get('status')!='RESOLVED' or not r.get('repair_record_ids'):
            failures.append('Unresolved native-image finding: '+str(r.get('id')))
        confirmations=r.get('publication_confirmations',[])
        if len(confirmations)!=len(r.get('affected_books',[])) or {c.get('reader') for c in confirmations}!=set(r.get('affected_books',[])):
            failures.append('Native-image finding lacks all affected final-book confirmations: '+str(r.get('id')))
        for c in confirmations:
            if c.get('reader') not in BOOKS:continue
            if c.get('pdf_sha256')!=sha256(WORK/'build'/(c['reader']+'.pdf')) or not c.get('reviewer') or not c.get('observation'):
                failures.append('Native-image closure is missing or stale: '+str(r.get('id'))+' / '+c['reader'])
            evidence=c.get('images',[])+c.get('comparison_records',[])
            if not evidence:failures.append('Native-image closure has no viewed-image/comparison evidence: '+str(r.get('id'))+' / '+c['reader'])
            for e in evidence:
                p=ROOT/e.get('path','__missing__')
                if not p.is_file() or e.get('sha256')!=sha256(p):
                    failures.append('Native-image closure evidence is stale: '+str(r.get('id'))+' / '+c['reader'])
    return audit,failures

def assess_generated_heading_repairs():
    """Require a current occurrence inventory for shared formatting repairs."""
    path=DATA/'generated_heading_repairs.json';failures=[]
    if not path.exists():return {},['Generated-heading source-occurrence inventory is missing']
    audit=read_json(path);items=audit.get('rows',[])
    if (audit.get('status')!='INTEGRATED_SOURCE_INVENTORY' or
            audit.get('source_readings_changed') is not False or
            audit.get('visual_review_claim') is not False):
        failures.append('Generated-heading inventory is not an integrated formatting-only inventory')
    expected_dependencies={'work/scripts/book_preamble.tex','work/scripts/build_readers.py',
                           'work/build/fr_provenance.json','work/build/en_provenance.json',
                           'work/records/MARGINAL_NOTE_CONTEXTS.tsv'}
    dependencies=audit.get('dependencies',[])
    if (len(dependencies)!=len(expected_dependencies) or
            {r.get('path') for r in dependencies}!=expected_dependencies):
        failures.append('Generated-heading inventory has incomplete source dependencies')
    for r in dependencies:
        p=ROOT/r.get('path','__missing__')
        if not p.is_file() or r.get('sha256')!=sha256(p):
            failures.append('Generated-heading inventory dependency is stale: '+str(r.get('path')))
    if not items or {r.get('reader') for r in items}!=set(BOOKS):
        failures.append('Generated-heading occurrence inventory does not cover all seven books')
    identities=[(r.get('reader'),r.get('id')) for r in items]
    if len(identities)!=len(set(identities)):
        failures.append('Generated-heading occurrence inventory has duplicate reader/repair identities')
    categories={'apparatus heading guard','retained heading guard',
                'scan-range heading guard','conditional marginal-note heading guard'}
    counts=collections.Counter(r.get('what_was_wrong') for r in items)
    if set(counts)!=categories or dict(counts)!=audit.get('counts'):
        failures.append('Generated-heading occurrence category counts disagree')
    ranges=collections.Counter(r.get('reader') for r in items
                               if r.get('what_was_wrong')=='scan-range heading guard')
    if dict(ranges)!={book:116 for book in BOOKS if book not in
                     {'LM_FR_texte_de_lecture','LM_EN_reading'}}:
        failures.append('Generated range guards are not recorded once per package and applicable book')
    for r in items:
        if any(not r.get(k) for k in ['reader','language','package','cote','source_path',
                                      'source_line','id','what_was_wrong','what_was_done',
                                      'old','new','generator_path','generator_line','applicability']):
            failures.append('Generated-heading occurrence is incomplete: '+str(r.get('id')))
            break
    return audit,failures

def assess_generated_heading_closure():
    """Recheck the all-page generated-heading audit and its actual evidence."""
    path=DATA/'generated_heading_audit_final.json';failures=[]
    if not path.exists():return {},['Final all-page generated-heading audit is missing']
    audit=read_json(path)
    if (audit.get('schema')!='generated-heading-audit-v1' or
            audit.get('status')!='PASS' or audit.get('unresolved')):
        failures.append('Final all-page generated-heading audit is not PASS')
    files=audit.get('files',[])
    if len(files)!=7 or {r.get('reader') for r in files}!=set(BOOKS):
        failures.append('Generated-heading audit does not cover exactly the seven required PDFs')
    hashes={r.get('reader'):r.get('sha256') for r in files}
    for r in files:
        if r.get('reader') not in BOOKS:continue
        pdf=WORK/'build'/(r['reader']+'.pdf')
        v=read_json(VERIFY/(r['reader']+'.verification.json'))
        if (not r.get('stable_during_audit') or r.get('sha256')!=sha256(pdf) or
                r.get('pages')!=v.get('pages')):
            failures.append(r['reader']+': all-page generated-heading audit is stale')
    def evidence(record,label):
        p=ROOT/record.get('path','__missing__')
        if not p.is_file() or record.get('sha256')!=sha256(p):
            failures.append('Generated-heading supporting evidence is stale: '+label)
            return None
        return p
    for key in ['scanner','candidate_inventory','witness_inventory']:
        evidence(audit.get(key,{}),key)
    source_inputs=audit.get('source_inputs',[])
    required_sources={'work/scripts/book_preamble.tex','work/scripts/build_readers.py'}|{
        'work/build/'+book+'.tex' for book in BOOKS}
    if not required_sources<={r.get('path') for r in source_inputs}:
        failures.append('Generated-heading audit has incomplete final source dependencies')
    for r in source_inputs+audit.get('review_inputs',[])+audit.get('comparisons',[]):
        evidence(r,str(r.get('path')))
    primary=audit.get('primary_candidates',[])
    masters=audit.get('master_candidates',[])
    witnesses=audit.get('witnesses',[])
    for label,items in [('primary candidates',primary),('master candidates',masters),('known witnesses',witnesses)]:
        ids=[r.get('id') for r in items]
        if len(ids)!=len(set(ids)) or any(not ident for ident in ids):
            failures.append('Generated-heading '+label+' have missing or duplicate identities')
    for r in primary+witnesses:
        expected='CLEARED_ON_FINAL_PDF' if r in primary else 'RESOLVED_ON_FINAL_PDF'
        if (r.get('status')!=expected or not r.get('reviewer') or not r.get('observation') or
                r.get('reader') not in BOOKS or r.get('pdf_sha256')!=hashes.get(r.get('reader')) or
                not isinstance(r.get('heading_page'),int) or
                r.get('heading_page')!=r.get('first_content_page') or
                r.get('rule_page',r.get('heading_page'))!=r.get('heading_page') or not r.get('images')):
            failures.append('Generated-heading actual closure is incomplete: '+str(r.get('id')))
        for im in r.get('images',[]):evidence(im,str(r.get('id')))
    for r in masters:
        if (r.get('status')!='CLEARED_BY_IDENTICAL_RENDER' or
                r.get('reader') not in {'LM_FR_master_annotated','LM_EN_master_annotated'} or
                r.get('pdf_sha256')!=hashes.get(r.get('reader'))):
            failures.append('Generated-heading master transfer is incomplete: '+str(r.get('id')))
    counts=audit.get('counts',{})
    expected_counts={'files':7,'primary_candidates':len(primary),'primary_cleared':len(primary),
                     'master_candidates':len(masters),'master_cleared':len(masters),
                     'expected_witnesses':len(witnesses),'witnesses_resolved':len(witnesses),'unresolved':0}
    if any(counts.get(k)!=v for k,v in expected_counts.items()) or not witnesses:
        failures.append('Generated-heading audit completion counts do not agree')
    inventory_path=ROOT/audit.get('candidate_inventory',{}).get('path','__missing__')
    if inventory_path.is_file():
        candidates=read_json(inventory_path).get('candidates',[])
        if {r.get('id') for r in primary+masters}!={r.get('id') for r in candidates}:
            failures.append('Generated-heading final candidate coverage is incomplete')
    witness_path=ROOT/audit.get('witness_inventory',{}).get('path','__missing__')
    if witness_path.is_file():
        known=read_json(witness_path);known_rows=known.get('witnesses',[])
        known_ids=[r.get('id') for r in known_rows]
        if (witness_path!=DATA/'generated_heading_known_witnesses.json' or
                known.get('schema')!='generated-heading-known-witnesses-v1' or
                known.get('status')!='FROZEN_ACTUAL_BEFORE_WITNESSES' or
                not known_rows or len(set(known_ids))!=len(known_rows) or
                any(not ident for ident in known_ids) or
                known.get('count')!=len(known_rows) or
                audit.get('witness_inventory',{}).get('count')!=len(known_rows) or
                len(witnesses)!=len(known_rows) or
                counts.get('expected_witnesses')!=len(known_rows) or
                counts.get('witnesses_resolved')!=len(known_rows) or
                {r.get('id') for r in witnesses}!=set(known_ids)):
            failures.append('Generated-heading known-witness closure coverage is incomplete')
        # The closure total grows additively. The original 48 actual witnesses
        # are a fixed historical baseline and must remain byte-exact row data.
        original_ref=known.get('original_inventory',{})
        original_path=evidence(original_ref,'immutable original heading witnesses')
        if (original_ref.get('path')!='work/data/generated_heading_known_witnesses_revision512.json' or
                original_ref.get('count')!=48):
            failures.append('Generated-heading original 48-witness baseline reference is invalid')
        if original_path:
            original=read_json(original_path);original_rows=original.get('witnesses',[])
            by_id={r.get('id'):r for r in known_rows}
            if (original.get('schema')!='generated-heading-known-witnesses-v1' or
                    original.get('status')!='FROZEN_ACTUAL_BEFORE_WITNESSES' or
                    original.get('count')!=48 or len(original_rows)!=48 or
                    len({r.get('id') for r in original_rows})!=48 or
                    any(by_id.get(r.get('id'))!=r for r in original_rows)):
                failures.append('Generated-heading original actual witnesses were dropped, duplicated or modified')
        for r in known_rows:
            for record in r.get('before_images',[])+[r.get('source',{}),r.get('observation_source',{})]:
                evidence(record,'historical heading witness '+str(r.get('id')))
    return audit,failures

def assess_frozen_build():
    path=DATA/'final_build_inputs.json';failures=[]
    if not path.exists():return {},['Frozen two-pass build record is missing']
    audit=read_json(path)
    if (audit.get('status')!='TWO_PASS_BUILD_COMPLETE_INPUTS_UNCHANGED' or
            audit.get('compile_passes')!=2 or audit.get('books')!=7 or
            audit.get('return_code')!=0 or audit.get('changed_inputs')):
        failures.append('Frozen seven-book two-pass build is not complete with unchanged inputs')
    freeze_path=ROOT/audit.get('freeze_record','__missing__')
    if not freeze_path.is_file() or audit.get('freeze_sha256')!=sha256(freeze_path):
        failures.append('Canonical source freeze differs from the full-build input record')
    else:
        freeze=read_json(freeze_path)
        if (audit.get('source_records')!=freeze.get('records') or
                audit.get('source_dependencies')!=freeze.get('sha256')):
            failures.append('Full-build repair inventory does not match the canonical source freeze')
    for section in ['source_dependencies','assembly_dependencies']:
        dependencies=audit.get(section,{})
        if not dependencies:failures.append('Frozen build dependency inventory is empty: '+section)
        for name,expected in dependencies.items():
            p=ROOT/name
            if not p.is_file() or sha256(p)!=expected:
                failures.append('Frozen build input changed: '+name)
    return audit,failures

def _assess_revision578_discovery(expected_frozen_records=None):
    """Require every discovery in its canonical current-publication gate."""
    from write_visual_residual578_proofs import FINDINGS, separate_closure_inventory
    path=DATA/'layout_residual_batch_revision578.json'
    if not path.exists():return {},[]
    batch=read_json(path);failures=[]
    if batch.get('pending_candidates'):
        failures.append('Source-qualified residual discoveries still have pending probes or manifest acceptance')
    integration_path=DATA/'layout_residual_revision578_integration_result.json'
    if not integration_path.exists():
        failures.append('The accepted residual-discovery batch is not yet integrated into the complete books')
        return batch,failures
    integration=read_json(integration_path)
    if (integration.get('status')!='INTEGRATED_EXACT_SOURCE_AUDITS_PASS_AWAIT_FROZEN_BUILD'
            or integration.get('manifest_sha256')!=sha256(path)
            or integration.get('actual_records')!=batch.get('expected_source_records')):
        failures.append('Residual-discovery integration is incomplete or belongs to a different manifest')
    freeze=read_json(DATA/'layout_release_checkpoint.json')
    if freeze.get('records')!=(expected_frozen_records if expected_frozen_records is not None else batch.get('expected_source_records')):
        failures.append('The frozen publication sources do not include the complete residual-discovery batch')
    ledger=read_json(DATA/'final_visual_issue_closure.json')
    known={r['id'] for r in ledger['findings']}
    for item in batch.get('items',[]):
        for field in ('candidate','validation'):
            source=ROOT/item[field]
            if not source.is_file() or sha256(source)!=item[field+'_sha256']:
                failures.append('Residual-discovery evidence changed: '+item[field])
        canonical=None
        if item['name'] in FINDINGS:
            try:
                canonical=separate_closure_inventory(item,read_json(ROOT/item['candidate']))
                if not canonical['witness_ids']:
                    raise ValueError('Empty canonical witness inventory')
            except (AssertionError,KeyError,ValueError,OSError) as exc:
                failures.append('Residual canonical pagination or heading mapping is incomplete: '+item['name']+' '+str(exc))
        for reference in item['finding_records']:
            source=ROOT/reference['path']
            if not source.is_file() or sha256(source)!=reference['sha256']:
                failures.append('Source-qualified residual finding changed: '+reference['path'])
            if item['name'] in FINDINGS:
                if reference['id']!=FINDINGS[item['name']][0]:
                    failures.append('Residual canonical finding identity differs: '+reference['id'])
                # The complete current-PDF pagination and generated-heading
                # audits are independently mandatory below. These three
                # canonical findings never belonged to the original36 native
                # scope and must keep their separate frozen witness identities.
            elif reference['id'] not in known:
                failures.append('A qualified residual finding is absent from the final native ledger: '+reference['id'])
    return batch,failures

def assess_residual_discovery():
    from revision872_additive_release_gate import assess_revision872
    latest,failures=assess_revision872(ROOT)
    original,previous_failures=_assess_revision578_discovery(expected_frozen_records=878)
    batches=[]
    if latest:
        historical=latest.get('historical_discovery_batches',[])
        if [item.get('revision') for item in historical]==[724,864]:
            batches.extend(historical)
        else:
            failures=failures+['Revision872 reporting lacks the exact separately identified historical revision724 and revision864 batches.']
        batches.append(latest)
    if batches:
        original=dict(original,following_discovery_batches=batches)
    return original,previous_failures+failures

def report(allow_pending=False):
    REC.mkdir(parents=True,exist_ok=True);warnings=refresh_logs()
    results={};failures=[]
    residual_discovery,residual_failures=assess_residual_discovery();failures+=residual_failures
    for book in BOOKS:
        v,failed=assess(book);failures+=failed
        if v:results[book]=v
    master=read_json(DATA/'master_integrity_build.json')
    source=read_json(DATA/'source_integrity.json')
    if master.get('status')!='PASS' or master.get('errors'):failures.append('Master/source projection audit is not PASS')
    if source.get('integrity_failures'):failures.append('Original source integrity has failures')
    master_readers=master.get('readers',[])
    expected_reader_files={book+'.tex' for book in BOOKS}
    if len(master_readers)!=len(BOOKS) or {r.get('file') for r in master_readers}!=expected_reader_files:
        failures.append('Master integrity report does not cover exactly the seven required TeX books')
    for r in master_readers:
        if r.get('file') not in expected_reader_files:continue
        tex_path=WORK/'build'/r['file']
        if r.get('tex_sha256')!=sha256(tex_path):
            failures.append(r['file']+': source integrity report belongs to different TeX bytes')
        text=tex_path.read_text()
        m=re.search(r'^% COMMON MASTER BODY SHA256 ([0-9a-f]{64})\n',text,re.M)
        end=text.rfind(r'\end{document}')
        actual=hashlib.sha256(text[m.end():end].encode()).hexdigest() if m and end>=m.end() else None
        if not m or actual!=m[1] or actual!=r.get('actual_body_sha256'):
            failures.append(r['file']+': master integrity report belongs to a different body')
    semantic=read_json(DATA/'layout_semantic_command_audit.json')
    for key in ['paired_stable_ids_equal','all_source_marks_preserved','all_raw_source_offsets_valid']:
        if not semantic.get(key):failures.append('Layout audit: '+key)
    size_gate=semantic.get('local_size_gate',{})
    if not size_gate.get('all_added_sizes_pass') or size_gate.get('added_resizebox_calls')!=0:
        failures.append('Local font-size/scaling audit is absent or fails the 70% floor')
    collision_file=DATA/'margin_collision_candidates.json'
    if not collision_file.exists():failures.append('Final marginal-line collision audit is missing')
    else:
        unresolved=[r for r in read_json(collision_file) if r.get('status') not in {'visually cleared','repaired and verified'}]
        if unresolved:failures.append(f'{len(unresolved)} marginal-line collision candidates remain unresolved')
    collision_manifest=DATA/'margin_collision_audit.json'
    if not collision_manifest.exists():failures.append('Hash-bound final marginal-line collision audit is missing')
    else:
        audit=read_json(collision_manifest);audited=audit.get('readers',[])
        expected_pdf_files={book+'.pdf' for book in BOOKS}
        if (audit.get('status')!='COMPLETE' or len(audited)!=len(BOOKS) or
                {r.get('file') for r in audited}!=expected_pdf_files):
            failures.append('Marginal-line collision audit does not cover exactly the seven required PDFs')
        for r in audited:
            if r.get('file') not in expected_pdf_files:continue
            pdf=WORK/'build'/r['file']
            if not pdf.exists() or r.get('sha256')!=sha256(pdf):
                failures.append(r['file']+': marginal-line collision audit belongs to a different PDF')
    privacy_file=DATA/'pdf_privacy_audit.json'
    pdf_privacy=read_json(privacy_file) if privacy_file.exists() else {}
    if pdf_privacy.get('status')!='PASS' or pdf_privacy.get('findings'):
        failures.append('Expanded PDF privacy audit is missing or has findings')
    else:
        audited_privacy={(r.get('archive'),r.get('path')):r for r in pdf_privacy.get('files',[])}
        for book in BOOKS:
            archive='LM_READERS_'+('FR' if '_FR_' in book else 'EN')+'.zip'
            r=audited_privacy.get((archive,book+'.pdf'),{})
            if not r.get('stable_during_audit') or r.get('sha256')!=sha256(WORK/'build'/(book+'.pdf')):
                failures.append(book+': expanded privacy audit belongs to a different PDF')
    pagination,pagination_failures=assess_pagination();failures+=pagination_failures
    heading,heading_failures=assess_heading_closure();failures+=heading_failures
    visual_issues,visual_issue_failures=assess_visual_issue_closure();failures+=visual_issue_failures
    generated_repairs,generated_repair_failures=assess_generated_heading_repairs();failures+=generated_repair_failures
    generated_headings,generated_heading_failures=assess_generated_heading_closure();failures+=generated_heading_failures
    frozen_build,frozen_build_failures=assess_frozen_build();failures+=frozen_build_failures
    if not allow_pending and failures:
        raise RuntimeError('Release remains incomplete:\n'+'\n'.join(failures))
    status='COMPLETE' if not failures else 'PROVISIONAL — NOT A FINISHED RELEASE'
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    out=['# Typesetting and verification report','',f'**Status: {status}.**','',
      'Edition date: 13 November 2026. This report is assembled from the saved log, link, source and painted-bound measurements and the attributed visual-review records. Each PDF is identified by its SHA-256 below. Page numbers in this report are physical PDF pages, starting at 1; manuscript and scan numbers remain separate.','',
      '## 1. Coverage and editorial decisions','',
      'The original three archive manifests contain 1,022 files; every length and digest was verified. Both language masters contain all 116 packages and all 1,588 scans in order. All 245 English translation units reconstruct their source packages byte for byte. French unit assembly is exact after the original reader’s newline normalization; 44 packages use CRLF in their raw source. `SOURCE_INTEGRITY.md`, `SOURCE_SCAN_MARKS.tsv` and `SOURCE_UNIT_ASSEMBLY.tsv` give the checks and the supplied historical exceptions.','',
      'One common annotated body generates every form of each language. It records 10,888 effective authorial variants: 6,702 deletions and 4,186 insertions. Another 380 nested edits wholly inside cancelled passages remain in their complete outer entries. No new conjectural manuscript reading or slip correction was introduced. The English has one additional recorded glossary correction, “structure with loops” → “loop structure” at 140-2:296. `CHANGES_FR.tsv`, `CHANGES_EN.tsv`, `APPARATUS_COUNTS.md` and `MASTER_INTEGRITY.md` document the exact projections.','',
      'Every original doubtful and illegible mark remains. The reading forms retain uncertainty from cancelled passages in scan-end fragments, with a dagger at the originating line. Short notes are measured against the three-line margin rule; longer notes form labelled, ruled, breakable blocks. All 237 archive-footer occurrences are listed in `ARCHIVE_FOOTERS.tsv`: the institutional line is omitted, and each independently transcribed manuscript-page number is retained.','',
      'The supplied translation has documented mathematical comparison exceptions; this edition does not misdescribe it as literally byte-identical mathematical source. The independent formula audit accounts for the nine historical changed/missing cases, raised abbreviation endings, translated diagram prose and the written-out m-bar shorthand. No unexplained additional mathematical difference was found. The glossary report inventories all 117 entries. Of these, 94 have multiple paragraph-aligned candidate spellings or forms, including inflection; these matches are not all translation inconsistencies.','',
      'One inherited spacing limitation remains in the supplied English at cote 140-4, scan 71: adjacent insertion commands contain no interword space between “the” and “surjective homomorphism”. The edition preserves the checked words and their insertion/deletion segmentation, including this source-preserved join. The exact source assessment is `work/data/root_revision724_source_spacing_assessment.json`; the pagination repair changes no reading or editorial mark and does not claim normal interword spacing at this place.','',
      '## 2. Before and after: compilation and painted bounds','',
      '“Before” means the actual baseline of the newly assembled form, before its source-local width repairs. It already includes the common annotated-edition infrastructure and mechanical compile repairs. It is not the original draft. The separate supplied English draft had 382 overfull boxes, maximum 331.94247 pt; all 382 records and all 93 previous fit-pass records were mapped back to scans and covered by the final selection. Sanitized complete baseline and final logs are in `work/records/logs/`.','']
    stats=[]
    for book,v in results.items():
        b=read_json(WORK/'verification_baseline'/(book+'.verification.json'))
        for label,r in [('before',b),('after',v)]:
            l=r['log_after'];pb=r['page_bounds']
            stats.append([book,label,r['pages'],l['overfull_count'],l['overfull_gt_2pt'],l['maximum_overfull_pt'],l['error_count'],l['missing_character_count'],len(pb['off_sheet_pages']),len(pb['outside_type_area_pages'])])
    out+=table(['PDF stem','Stage','Pages','Overfull boxes','Above 2 pt','Widest pt','Errors','Missing glyphs','Outside sheet','Outside permitted area'],stats)
    out+=['','The painted-bound check runs on every page using MuPDF’s native bounding-box device, including text, strokes, fills and images. It uses the supplied geometry: 25 mm margins, a 20 mm right note column with 10 pt separation, 12 pt head allowance, and the ordinary footer allowance. The supplied tolerances are retained: 1.5 pt at permitted-area edges and 0.5 pt at sheet edges. Landscape pages are measured in their underlying unrotated sheet coordinates. These tolerances are disclosed, not increased to hide failures. See `VERIFICATION_METHOD.md` for the algorithm and calibration.','',
      'No blanket scaling callback is used, and `hfuzz` and `vfuzz` remain zero. Source repairs are recorded individually: changed row/column gaps, label offsets and arrow routes, mathematical line breaks, and three landscape diagrams per book. Explicit local diagram sizes are 8.2, 8.5, 9 and 10 pt against the original 11 pt; the smallest is about 74.5%. One physical sketch per language uses a recorded factor of 0.90. The source-size audit checks that every added size or scaling factor meets the 70% floor. The bold Gamma glyph repair preserves the requested notation through a working Unicode math glyph.','',
      '### Pages with boundary violations, before and after','']
    for book,v in results.items():
        b=read_json(WORK/'verification_baseline'/(book+'.verification.json'))
        out += [f'**{book}.pdf**','',f"Before: beyond sheet — {pages(b['page_bounds']['off_sheet_pages'])}; outside permitted area — {pages(b['page_bounds']['outside_type_area_pages'])}.",'',
          f"After: beyond sheet — {pages(v['page_bounds']['off_sheet_pages'])}; outside permitted area — {pages(v['page_bounds']['outside_type_area_pages'])}. Accepted single-letter exceptions: {len(v['accepted_single_letter_overhangs'])}.",'']
    out+=['## 3. Links and source marks','',
      'Original source counts are 1,588 scan marks, 17,117 doubtful marks and 1,261 illegible marks in each language. Literal marks in alternate master branches, executed source IDs, macro expansions and painted PDF annotation rectangles are distinct quantities. A wrapped mark may produce several rectangles; nested marks may share one. The audit independently reconstructs each marked occurrence’s target and physical-page set from PDF annotations, then compares them with the LuaLaTeX trace and the selected master branch.','']
    out+=table(['PDF stem','Archive annotations','All external URI annotations','Distinct scans','Executed source IDs','Macro expansions','Unlinked marked IDs'],[
      [b,v['links']['archive_scan_links'],v['links']['total_external_uri_links'],v['links']['distinct_scan_pages'],v['links']['distinct_source_ids'],v['links']['macro_expansion_count'],sum(k['unlinked_marks'] for k in v['links']['per_kind'].values())] for b,v in results.items()])
    out+=['','### Per-cote target coverage','']
    out+=table(['PDF stem','Cote','Expected scans','Distinct linked scans','Annotation rectangles','Missing / unexpected scans'],[
      [b,c,k['expected_distinct_scans'],k['actual_distinct_scans'],k['annotation_count'],str(k['missing_scans'])+' / '+str(k['unexpected_scans'])] for b,v in results.items() for c,k in v['links']['per_cote'].items()])
    out+=['','### Per-kind executed marks and links','']
    out+=table(['PDF stem','Kind','Executed IDs','Linked IDs','Unlinked IDs','Run / page mismatches'],[
      [b,c,k['expanded_marks'],k['pdf_linked_marks'],k['unlinked_marks'],str(k['trace_run_mismatches'])+' / '+str(k['trace_page_mismatches'])] for b,v in results.items() for c,k in v['links']['per_kind'].items()])
    out+=['','The reading forms have 4,969 cancellation-anchor marks and 110 explicit inherited-uncertainty marks in addition to the original primary marks. They keep the doubts in omitted passages visible and linked. In all forms, the source-ID audit tests the exact branch selected, rather than assuming that all literal master branches execute.','',
      '## 4. Warnings and font decisions','',
      'The complete warning messages, including continuation lines, are in `LATEX_WARNINGS.tsv`. The complete sanitized logs retain the surrounding diagnostics. Underfull boxes are reported separately from overfull boxes. Margin-placement warnings indicate LaTeX adjusted a margin box vertically; they do not establish that text was lost. The all-page ink audit and the additional margin-line collision audit check the resulting layout.','']
    out+=table(['PDF stem','Warnings','Margin-placement warnings','Other warnings','Underfull boxes','Undefined references / citations'],[
      [b,v['log_after']['warning_count'],sum(w['stage']=='final' and w['reader']==b and w['category']=='margin placement' for w in warnings),sum(w['stage']=='final' and w['reader']==b and w['category']!='margin placement' for w in warnings),v['log_after']['underfull_count'],len(v['log_after']['undefined_reference_warnings'])] for b,v in results.items()])
    out+=['','The ordinary remaining package warnings concern unicode-math’s compatibility definitions, disabled shell escape for an unused EPS converter, and the legacy OMS font shape used by `textcircled`. The actual circled glyph is present and was visually checked. `FONT_REPAIRS.tsv` and `audit_fonts.py` document the separate bold-Gamma correction. Missing-character counts are measured independently; a font substitution is not presented as a missing-glyph diagnostic.','',
      '## 5. Visual inspection and local collision repairs','',
      'Required pages include every historic overflow site and previous scaling/rotation site mapped by scan, every landscape page, all current nontrivial layout repairs, and forty evenly spread physical pages per book. Selection extends through a scan’s continuation and the next scan boundary. Selected pages were rendered and inspected; dense diagrams and ambiguous labels were also enlarged. The individual observations below retain the actual reviewer and basis.','',
      'Review status is tied to the PDF hash, PNG-file hash and decoded RGB-pixel hash. On rebuild, a review carries forward only when both image hashes are identical. A master may inherit an apparatus-reader observation only after a fresh all-page pixel comparison and equality of its actual selected-page PNG; its different title page is inspected separately. Rendering by itself never creates a completed review.','']
    out+=table(['PDF stem','Required pages','Rendered','Reviewed','Close-check inventory','Landscape pages'],[
      [b,len(v['selected_pages']),v['visual_review']['rendered_pages'],v['visual_review']['reviewed_pages'],len(v['close_review_pages']),pages(v['page_bounds']['landscape_pages'])] for b,v in results.items()])
    out+=['','### Equation numbers and page breaks','',
      'A separate page-break audit examined106 nonmaster candidates in the preceding complete build. Actual native page-pair inspection confirmed80 detached equation-number instances and cleared26 candidates whose formulas were already on the same page. The repairs are exact paired source bindings: local page-break penalties keep each unchanged number with its complete diagram. No equation text or geometry is changed by those pagination bindings. `PAGINATION_REVIEW_BEFORE.tsv`, the source-binding inventory and the source reconciliation retain the historical observations and their source locations.','',
      'The revision578 review added three actually observed primary-book detachments at two source sites, plus two master witnesses supported by exact image identity to the inspected apparatus pages. `work/data/pagination_known_extensions.json` preserves those observations, their source fragments and immutable before-image evidence while keeping the original106-inspection baseline unchanged. All original and additive witnesses require closure on the final PDFs.','',
      'The final audit reruns the candidate scan over every page of all seven PDFs, requires an actual final-image observation for every known defect and every new primary candidate, and uses current all-page pixel comparisons for the two apparatus/master duplicates. Its records bind source fragments, PDF hashes and viewed-image hashes. `pagination_verification_final.json` records the final status; rendering alone does not resolve an item.','']
    if pagination:
        pc=pagination.get('counts',{})
        out+=table(['Pagination check','Count'],[
          ['Previously observed primary detachments resolved',str(pc.get('resolved_known_detachments',0))+' / '+str(pc.get('known_detachments',0))],
          ['Additive historical master witnesses resolved',str(pc.get('resolved_extension_master_transfers',0))+' / '+str(pc.get('extension_master_transfers',0))],
          ['Final primary candidates cleared',str(pc.get('cleared_primary_candidates',0))+' / '+str(pc.get('final_primary_candidates',0))],
          ['Final master candidates covered by exact pixel identity',str(pc.get('cleared_master_candidates',0))+' / '+str(pc.get('final_master_candidates',0))],
          ['Unresolved findings',pc.get('unresolved','not finalized')]])
    out+=['','The long-note renderer also keeps its heading with the first paragraph or diagram while allowing later paragraphs to break normally. Five previously detached diplomatic-note headings are checked on their actual final pages. Section V and its preliminary-data opening at140-3:548 are separately checked in all five primary readers. `heading_closure_final.json` retains the10 source-qualified, image-bound observations.','']
    out+=['### Additional native-image findings','',
      '`work/data/final_visual_issue_closure.json` retains each observed defect, its original image evidence, the exact repair identifiers and separate confirmations against every affected final book. The following counts distinguish an accepted isolated probe from closure on the actual publication PDF.','']
    if residual_discovery:
        integrated_path=DATA/'layout_residual_revision578_integration_result.json'
        integration_state=(read_json(integrated_path).get('status','UNKNOWN') if integrated_path.exists()
                           else 'AWAITING_BATCH_INTEGRATION')
        out += [
          'The revision578 discovery manifest preserves the additional source-qualified findings and their attributed isolated proofs. Its original before-image records stay immutable; publication closure is recorded separately. The two initial equation-tag findings retain their frozen pagination witnesses, and the range-heading finding retains its generated-heading witnesses. All later findings use the native ledger. Every applicable current-publication gate is required. The generated range-heading repair is a formatting case with no manuscript source row. Exact larger bindings identify every earlier wrapper they supersede, and the complete accepted manifest must be integrated.','']
        out += table(['Residual-discovery batch','Recorded state'],[
          ['Accepted repair sites',residual_discovery.get('accepted_site_count',0)],
          ['Added source-language rows',residual_discovery.get('added_source_records',0)],
          ['Explicitly superseded source rows',residual_discovery.get('superseded_source_records',0)],
          ['Expected total source-layout rows',residual_discovery.get('expected_source_records',0)],
          ['Pending probe/acceptance records',len(residual_discovery.get('pending_candidates',[]))],
          ['Integration',integration_state]])
        out += ['','Manifest: `work/data/layout_residual_batch_revision578.json`. Integration and exact-source audit: `work/data/layout_residual_revision578_integration_result.json`.','']
    for later in residual_discovery.get('following_discovery_batches',[]):
        revision=later['revision']
        if revision==724:
            out += ['','The revision724 selected-page discovery sweep added the following source-local opening repairs. Its immutable discovery snapshot preserves the complete five-reader selected-page review and explicitly deferred native/canonical queues. It is not a final-publication approval. The later frozen build, complete final visual closure and exact current source checks are independently required. Previously complete inner bindings remain explicit dependencies; any replaced wrapper has a source-qualified supersession history.','',
              'The unchanged revision724 proof gate was executed through the additive wrapper in a bounded historical view of the preserved revision864 inputs before installation of the reviewed native-history importer change. Only the pagination-binding and applied-layout inventories use their exact preserved baseline bytes. The four original stress fields and all185 original native-finding definitions remain protected in the current files, whose complete actual hashes are recorded at each execution. This historical check does not claim a new revision872 stress compilation or current-publication inspection. For the current revision878 checks, the additive gate reuses the exact pre-installation historical PASS preserved in `work/records/REVISION878_PRECEDING_PROOFS_PREFLIGHT.json`; it does not execute the old gate again after the reviewed native-history importer change. Each current check freshly validates the complete 1,037-input inventory: 1,035 exact byte identities, including the two explicit preserved-baseline substitutions, and two protected current-file projections. The ten recorded project-module identities are also rechecked. `revision872_historical_gate_qualification.py` separately verifies the exact reviewed importer change and the unchanged current-publication and ledger-mutation functions. Current878 source checks and publication closure remain independently required.','']
        elif revision==864:
            out += ['','The revision864 discovery batch adds four paired source bindings and one separate generated range-heading reservation. Its eight new source-language rows bring the applied inventory from864 to872 and the pagination-binding inventory from516 to524. Every old source-record object and its relative order remain exact; each new wrapper preserves the supplied inner source span. The generated C4:77 guard adds no manuscript source row. Accepted isolated probes and the unchanged historical gate remain separate from closure on every affected current publication PDF.','',
              'The separately pinned FR308 boundary qualification records the unchanged mapper’s inclusion of exactly one carriage return after the accepted raw span; the following line feed and prose remain outside. Candidate and mapped source slices are both exact and separately recorded in `work/data/revision864_final_review/section308_fr_crlf_boundary_qualification_v1.json`. No other new source coordinate or historical record is relaxed. The complete preserved872 applied objects must equal their preceding real-mapper prediction; the current878 objects are checked separately by the following additive gate. Exact JSON objects and serialized byte identities remain separately identified.','']
        elif revision==872:
            out += ['','The revision872 native review identified three further label contacts. Six paired French/English source records raise the applied inventory from872 to878, with all872 preceding objects and their relative order unchanged. At C1:27 the entire uncertain category label moves upward by6pt, retaining its parenthesis, lettering, doubt span and incident connections. At C3:85 the minus-one label moves left by6pt and the zero label left by10pt; all40 sphere drawing paths remain exact in the isolated six-form proofs. These local placements change no manuscript reading or editorial entry.','',
              'The preserved revision872 snapshot contains all4511 selected-page observations, all five completed historical native queues, the two honestly unresolved French-apparatus observations, the canonical and special-heading checks, and all seven original PDF files. Exact historical-image transfer may reuse only an individually RESOLVED observation whose complete registered image evidence remains identical; the two ISSUE observations cannot transfer. The rebuilt878 publication must independently close every current finding.','',
              'Two separately recorded French CRLF boundaries concern only the minus-one and zero source literals. The unchanged mapper includes the carriage return immediately after each exact accepted literal; the following line feed remains outside. The six candidate replacements, all source starts, every other coordinate and all prior source records remain unchanged. The preceding872 source prediction is checked against the actual preserved872 baseline, while the current878 objects are checked directly against the new real-mapper prediction. No historical stress compilation is relabelled as current.','']
        else:
            raise ValueError('Unexpected later-discovery report scope')
        counts=[
          ['Accepted repair sites',later.get('accepted_site_count',0)],
          ['Added paired-language source rows',later.get('added_source_records',0)],
          ['Superseded source rows',later.get('superseded_source_records',0)],
          ['Resulting active source-layout rows',later.get('expected_source_records',0)],
          ['Pending accepted candidates',len(later.get('pending_candidates',[]))]]
        if revision==864:
            counts[1:1]=[
              ['Accepted raw-source sites',later.get('accepted_raw_site_count',0)],
              ['Generated formatting sites',later.get('generated_site_count',0)],
              ['Generated paired proof records',later.get('added_generated_proof_records',0)]]
        out += table(['Later discovery batch '+str(revision),'Count'],counts)
        out += ['',f"Manifest: `{later['manifest_path']}`. Exact source integration: `{later['integration_path']}`. The manifest pins every accepted isolated proof and the complete reservation-disposition inventories.",'']
    out+=table(['Finding','Source site','Status','Affected books','Final-book confirmations'],[
      [r['id'],str(r.get('cote','generated'))+':'+str(r.get('scan','all applicable occurrences')),
       r.get('status',''),len(r.get('affected_books',[])),len(r.get('publication_confirmations',[]))]
      for r in visual_issues.get('findings',[])])
    out+=['','The common apparatus, retained-uncertainty, package-range and conditional marginal-note heading guards are formatting repairs. `work/data/generated_heading_repairs.json` and the corresponding occurrence rows in `TYPESETTING_FIXES.tsv` identify the generator implementation, original source place and applicable book. They do not add manuscript variants or apparatus entries. The conditional marginal-note rows record where the block renderer can apply; they do not assert that every note prints as a block in every form.','']
    out+=table(['Generated formatting repair','Recorded source/book occurrences'],[
      [kind,count] for kind,count in sorted(generated_repairs.get('counts',{}).items())])
    out+=['','The separate all-page generated-heading audit searches every publication page for a detached apparatus or retained-doubt heading, a detached separator rule, and a package-range heading without following source content. It closes the actually observed earlier witnesses and accounts for every current candidate. Its source, PDF, image and master-comparison hashes are recorded in `work/data/generated_heading_audit_final.json`.','']
    ghc=generated_headings.get('counts',{})
    out+=table(['Generated-heading closure check','Count'],[
      ['Publication PDFs audited',ghc.get('files','pending')],
      ['Known witnesses resolved',str(ghc.get('witnesses_resolved',0))+' / '+str(ghc.get('expected_witnesses','pending'))],
      ['Current primary candidates cleared',str(ghc.get('primary_cleared',0))+' / '+str(ghc.get('primary_candidates','pending'))],
      ['Current master candidates covered by identical render',str(ghc.get('master_cleared',0))+' / '+str(ghc.get('master_candidates','pending'))],
      ['Unresolved findings',ghc.get('unresolved','pending')]])
    out+=['','`VISUAL_REPAIRS.tsv` records the confirmed label, edge and marginal-note collisions, their paired source repairs and the isolated proofs. These include defects wholly inside the permitted area, which a bounding-box test alone cannot find. `LAYOUT_REPAIR_DETAILS.tsv`, `TYPESETTING_FIXES.tsv` and the exact replacement manifests retain source positions and before/after text. The complete per-page review records are in `work/verification/<PDF stem>/VISUAL_REVIEW.tsv`; the following is their readable transcription.','']
    for book,v in results.items():
        out += [f'### {book}.pdf','',f"PDF SHA-256: `{v['sha256']}`.",'']
        rs=rows(VERIFY/book/'VISUAL_REVIEW.tsv')
        out+=table(['Physical page','Status','Selection reason','Reviewer and inspection basis','Observation'],[
          [r['page'],r['status'],r['reasons'],r.get('reviewer','')+'; '+r.get('review_basis',''),r.get('observations','')] for r in rs])
        out.append('')
    out+=['## 6. Reproducibility, privacy and checkpoint retention','',
      'Each delivered TeX book is self-contained and compiles twice with LuaLaTeX on a full standard TeX Live installation, with shell escape disabled. The embedded Lua writes only relative audit sidecars. Rebuilding the edition from the original three supplied ZIPs uses the `sources/` and `work/` project structure and scripts described in `README.md`. Original manuscript source packages were not edited.','',
      'Complete final verification JSON, all-page bound tables, PDF link tables, source-projection outputs, exact layout manifests, full warning tables and sanitized logs are retained. Historical indexed contact/overview grids omitted from the ordinary final archives have separate per-file rows in `INDEXED_REVIEW_GRID_OMISSIONS.tsv` and exact evidence in `INDEXED_REVIEW_GRID_QUALIFICATIONS.json`, distinct from the full-page raster inventories. Each qualification retains the unchanged pending-page index and discovery snapshot, component PDF/page/PNG/dimensioned-RGB identities, and historical inspection records. The named final book and its complete current selected-page review ledger supersede the grid at whole-book scope; no correspondence between historical and final page numbers or pixels is claimed. The independently recoverable numbered checkpoint preserves the original grid PNG bytes and decoded RGB, directly or through verified self-contained reconstruction. Identical master images may be represented once with a digest-backed alias inventory; the manifest states every such alias. These storage dispositions create no visual-review claim.','',
      'Curated native proof PNG payloads remain physically stored, byte for byte. Unambiguously French or English proof assets are held at their unchanged relative paths in the corresponding language archive; shared or ambiguous assets, reports, scripts and audit data remain in RECORDS. After safe common assembly of all three archives, exact aliases restore both `proofs/visual_repairs/` and `work/visual_repair_proofs/` paths from the stored canonical bytes. `FINAL_PROOF_ASSET_DISTRIBUTION.tsv` records each move and `FINAL_RECORDS_LOGICAL_MANIFEST.tsv` records its final archive and path. `assemble_release.py` validates every archive manifest, CRC and hash, preserves the original manifests under `archive_manifests/`, merges only identical common paths and invokes the pinned alias helper. This storage distribution neither re-encodes native proof images nor creates new inspection claims.','',
      'The final archives contain exactly the seven publication PDFs. Development probe PDFs remain in the immutable checkpoints; their exact source/log records, accepted PNG proof images and hashes are retained. They are excluded because an isolated development proof is superseded by the complete final reader, even when its numerical checks pass. `development_pdf_exclusions.json` identifies each probe and its final replacement; `VISUAL_REPAIRS.tsv` distinguishes historical probe provenance from final-reader evidence. Imported historical whole-book PDFs keep their `.pdf` identity and explicit registry, original archive, complete ordinary manifest and exact member provenance. Their source-qualified dispositions name the final whole-book replacement without claiming page or pixel correspondence; `FINAL_RECORDS_POLICY.json` and `CHECKPOINT_RETENTION.tsv` record those dispositions. Their original bytes remain independently recoverable from the numbered checkpoints. They are excluded as additional final PDF payloads rather than renamed as opaque binary files.','',
      'Checkpoint ZIPs are never overwritten, renamed or deleted. `CHECKPOINT_RETENTION.tsv` lists every checkpoint entry, its original hash, its final archive/path and whether it is preserved byte for byte, superseded by a final version, or explicitly omitted with a reason. This inventory is the authoritative record for every development artifact not copied into the final ZIPs.','',
      'The separate `FAILED_CHECKPOINT02_MEMBER_DISPOSITIONS.tsv` accounts for all 287 CRC-readable members of the unsaved `LM_READERS_checkpoint_02.zip.failed` artifact. Its 286 exact counterparts in successful checkpoint02 follow the final routes recorded in `CHECKPOINT_RETENTION.tsv`; the remaining 504-entry JSON is retained byte for byte at `work/data/audit_history/failed_checkpoint02/unique_member/work/data/fr_app_review_detail_notes.json`. All 504 notes remain unchanged in successful checkpoint02; this historical evidence is not a current publication approval. Checkpoint07 was not durably saved, but checkpoint08 explicitly recovered and accounted for all 14,243 of its entries. The original failed ZIP remains unchanged.','',
      'Original compiler-output leaf hashes remain historical identities. The manifest-pinned privacy registry pairs each exact relative path, original SHA-256 and byte count with its approved portable SHA-256 and byte count after sanitizer idempotence and equality of the complete parsed diagnostics are proved. Copies require exact PLAN or snapshot authority. The extension covers 32 explicitly inventoried companion-log-bound console transcripts and their original snapshot copies; 125 earlier projected snapshot rows retain their original v2 disclosures and are verified through exact registry continuity. The registry covers 140 fixed proof outputs and seven separately scoped revision724 publication logs; it neither approves later build bytes nor changes compile outcomes or attributed observations.','',
      'All delivered text and PDF text/metadata are checked for local filesystem paths and email addresses. An additional hash-bound audit covers PDF object dictionaries, decoded strings, annotation/action targets and embedded-file absence; `pdf_privacy_audit.json` records its complete inventory and scope. Binary font/image streams are not interpreted. Sanitized logs use an explicit omission marker for machine paths. Relative paths inside the reproducibility project and public archive URLs remain intact. Credit and rights text follows the supplied published record; see `CREDITS_AUDIT.md`.','']
    if failures:out+=['## Unfinished conditions','']+['- '+x for x in failures]+['']
    (REC/'TYPESETTING_REPORT.md').write_text('\n'.join(out)+'\n')
    release={'status':status,'generated_at_utc':now,'failures':failures,'books':{
      b:{'pdf_sha256':v['sha256'],'tex_sha256':sha256(WORK/'build'/(b+'.tex')),'pages':v['pages'],'gates':v['gates'],'review':v['visual_review']} for b,v in results.items()}}
    (REC/'release_status.json').write_text(json.dumps(release,ensure_ascii=False,indent=2)+'\n')
    readme=REC/'README.md';text=readme.read_text()
    start=text.index('## Final build and inspection status');end=text.index('## Credits, sources and rights',start)
    section=['## Final build and inspection status','',f'**{status}.**','']
    section+=table(['PDF','Pages','LaTeX errors','Warnings','Overfull boxes / widest pt','Missing characters','Outside sheet / permitted area','Archive links','Scans linked','Reviewed / required pages'],[
      [b+'.pdf',v['pages'],v['log_after']['error_count'],v['log_after']['warning_count'],str(v['log_after']['overfull_count'])+' / '+str(v['log_after']['maximum_overfull_pt']),v['log_after']['missing_character_count'],str(len(v['page_bounds']['off_sheet_pages']))+' / '+str(len(v['page_bounds']['outside_type_area_pages'])),v['links']['archive_scan_links'],v['links']['distinct_scan_pages'],str(v['visual_review']['reviewed_pages'])+' / '+str(len(v['selected_pages']))] for b,v in results.items()])
    section+=['','`TYPESETTING_REPORT.md` gives before/after measurements, complete page-specific visual observations and warning interpretation. `LATEX_WARNINGS.tsv` and `logs/` retain the complete warnings and sanitized logs. `CHECKPOINT_RETENTION.tsv` explains every checkpoint entry retained or superseded.','']
    if failures:section+=['Unfinished conditions are listed explicitly in the report; this checkpoint is not a final publication.','']
    readme.write_text(text[:start]+'\n'.join(section)+'\n'+text[end:])
    print(json.dumps({'status':status,'books':len(results),'unfinished_conditions':failures,'report': 'work/records/TYPESETTING_REPORT.md'},ensure_ascii=False))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--allow-pending',action='store_true');a=ap.parse_args();report(a.allow_pending)
