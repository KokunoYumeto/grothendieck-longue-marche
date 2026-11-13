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
    for key in ['queue','baseline','source_bindings','applied_repairs','source_reconciliation','scanner']:
        evidence=audit.get(key,{})
        p=ROOT/evidence.get('path','__missing__')
        if not p.is_file() or evidence.get('sha256')!=sha256(p):
            failures.append('Pagination supporting evidence is missing or stale: '+key)
    known=audit.get('known_detachments',[])
    if len(known)!=80 or len({r.get('id') for r in known})!=80:
        failures.append('Final pagination audit does not close all80 observed detachment instances')
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
    counts=audit.get('counts',{})
    if (counts.get('known_detachments')!=80 or counts.get('resolved_known_detachments')!=80 or
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

def report(allow_pending=False):
    REC.mkdir(parents=True,exist_ok=True);warnings=refresh_logs()
    results={};failures=[]
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
      'The final audit reruns the candidate scan over every page of all seven PDFs, requires an actual final-image observation for every known defect and every new primary candidate, and uses current all-page pixel comparisons for the two apparatus/master duplicates. Its records bind source fragments, PDF hashes and viewed-image hashes. `pagination_verification_final.json` records the final status; rendering alone does not resolve an item.','']
    if pagination:
        pc=pagination.get('counts',{})
        out+=table(['Pagination check','Count'],[
          ['Previously observed detachments resolved',str(pc.get('resolved_known_detachments',0))+' / 80'],
          ['Final primary candidates cleared',str(pc.get('cleared_primary_candidates',0))+' / '+str(pc.get('final_primary_candidates',0))],
          ['Final master candidates covered by exact pixel identity',str(pc.get('cleared_master_candidates',0))+' / '+str(pc.get('final_master_candidates',0))],
          ['Unresolved findings',pc.get('unresolved','not finalized')]])
    out+=['','The long-note renderer also keeps its heading with the first paragraph or diagram while allowing later paragraphs to break normally. Five previously detached diplomatic-note headings are checked on their actual final pages. Section V and its preliminary-data opening at140-3:548 are separately checked in all five primary readers. `heading_closure_final.json` retains the10 source-qualified, image-bound observations.','']
    out+=['### Additional native-image findings','',
      '`work/data/final_visual_issue_closure.json` retains each observed defect, its original image evidence, the exact repair identifiers and separate confirmations against every affected final book. The following counts distinguish an accepted isolated probe from closure on the actual publication PDF.','']
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
      'Complete final verification JSON, all-page bound tables, PDF link tables, source-projection outputs, exact layout manifests, full warning tables and sanitized logs are retained. Contact/overview sheets can be regenerated from the selected-page PNGs and the stored PDF. Identical master images may be represented once with a digest-backed alias inventory; the manifest states every such alias.','',
      'Curated repair evidence is retained under both `proofs/visual_repairs/` and `work/visual_repair_proofs/`. These byte-identical copies preserve the earlier archive references and the project-relative paths used by the saved audit scripts; neither set of those paths requires reconstruction.','',
      'The final archives contain exactly the seven publication PDFs. Development probe PDFs remain in the immutable checkpoints; their exact source/log records, accepted PNG proof images and hashes are retained. They are excluded because an isolated development proof is superseded by the complete final reader, even when its numerical checks pass. `development_pdf_exclusions.json` identifies each probe and its final replacement; `VISUAL_REPAIRS.tsv` distinguishes historical probe provenance from final-reader evidence.','',
      'Checkpoint ZIPs are never overwritten, renamed or deleted. `CHECKPOINT_RETENTION.tsv` lists every checkpoint entry, its original hash, its final archive/path and whether it is preserved byte for byte, superseded by a final version, or explicitly omitted with a reason. This inventory is the authoritative record for every development artifact not copied into the final ZIPs.','',
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
