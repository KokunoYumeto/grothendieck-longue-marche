r"""Read-only verification of source coverage, annotated masters and readers.

This verifier never regenerates a reader, cache or provenance file. It writes
only MASTER_INTEGRITY.md and its own machine-readable report. All source paths
reported are archive-relative. Use --stage baseline for a development audit or
--stage build for the final seven-book audit.
"""
from __future__ import annotations
import argparse, collections, csv, hashlib, json, re
from pathlib import Path
import editorial, mechanical_repairs, instrument_marks

ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'work';SOURCES=ROOT/'sources'
BOOKS={
 'LM_FR_diplomatique':('fr',0),'LM_FR_corrige_apparat':('fr',1),
 'LM_FR_texte_de_lecture':('fr',2),'LM_EN_corrected_apparatus':('en',1),
 'LM_EN_reading':('en',2),'LM_FR_master_annotated':('fr',1),
 'LM_EN_master_annotated':('en',1)}
CORE_MARKS={'scanpage','unsure','illegible'}
LITERAL_CACHE={}
STATIC_CACHE={}

LINK_KINDS={'scanpage':'scan','unsure':'unsure','illegible':'illegible','LMdoubtcopy':'residual-unsure','LMuncertaindeletion':'cancelled-anchor'}


def sha(text):return hashlib.sha256(text.encode()).hexdigest()
def safe_error(error):return str(error).replace(str(ROOT)+'/', '')
def read_tsv(path):
    with path.open() as f:return list(csv.DictReader(f,delimiter='\t'))

def split_scans(text):
    mask=editorial.blank_comments(text);ms=list(re.finditer(r'\\scanpage\{(\d+)\}',mask))
    return [(int(m[1]),m.start(),ms[i+1].start() if i+1<len(ms) else len(text)) for i,m in enumerate(ms)]

def mark_counts(text):
    out=collections.Counter();scan=0
    for m in editorial.spans(text,CORE_MARKS):
        if m['name']=='scanpage':scan=int(m['argument'])
        out[(scan,m['name'])]+=1
    return out

def totals(counts):return {k:sum(v for (scan,kind),v in counts.items() if kind==k) for k in sorted(CORE_MARKS)}

def replay_layout(text,records):
    for r in records:
        ranges={n:(a,b) for n,a,b in split_scans(text)}
        a,b=ranges[int(r['scan'])];part=text[a:b]
        old=r.get('old',r.get('before'));new=r.get('new',r.get('after'))
        count=part.count(old)
        if count!=1:raise ValueError(f"layout record {r.get('id','')} has {count} matches in scan {r['scan']}")
        text=text[:a]+part.replace(old,new,1)+text[b:]
    return text


def macro_args(s,pos,count):
    args=[]
    for _ in range(count):
        while pos<len(s) and s[pos].isspace():pos+=1
        if pos>=len(s) or s[pos]!='{':raise ValueError('Missing braced generated-macro argument')
        end=editorial.brace_end(s,pos);args.append((pos+1,end-1));pos=end
    return args,pos


def expected_mark_ids(body,form):
    """Statically select the literal linked marks executed by one form.

    This is intentionally limited to the edition's documented form switches
    and branch macros. Original package texts contain no TeX conditionals.
    Mathchoice repetitions share one literal ID and therefore count once.
    """
    s=editorial.blank_comments(body);found={};problems=[]
    conditional=re.compile(r'\\(ifnum|if[a-zA-Z]+|else|fi)\b')
    def branch(start,end):
        depth=1;middle=None
        for m in conditional.finditer(s,start,end):
            if m[1].startswith('if'):depth+=1
            elif m[1]=='fi':
                depth-=1
                if not depth:return middle,m.start(),m.end()
            elif m[1]=='else' and depth==1:middle=(m.start(),m.end())
        raise ValueError('Unclosed edition conditional')
    def walk(a,b,current=''):
        i=a
        while i<b:
            if s[i]!='\\':i+=1;continue
            m=editorial.COMMAND.match(s,i)
            if not m:i+=1;continue
            cmd=m[1];i=m.end()
            if cmd=='ifnum':
                q=re.match(r'\s*\\LMform\s*([=<>])\s*([012])',s[i:b])
                if not q:raise ValueError('Unknown conditional in common body')
                begin=i+q.end();mid,finish,after=branch(begin,b)
                relation=q[1];number=int(q[2]);take=(form==number if relation=='=' else form<number if relation=='<' else form>number)
                if take:walk(begin,mid[0] if mid else finish,current)
                elif mid:walk(mid[1],finish,current)
                i=after;continue
            if cmd in ('else','fi'):continue
            if cmd=='LMsourceMark':
                args,end=macro_args(s,i,2);identifier=s[slice(*args[0])];walk(*args[1],identifier);i=end;continue
            if cmd=='var':
                args,end=macro_args(s,i,4);walk(*args[0 if form==0 else 1],current);i=end;continue
            if cmd=='LMarchivefooter':
                args,end=macro_args(s,i,3);walk(*args[1],current);i=end;continue
            if cmd=='LMpagefigure':
                args,end=macro_args(s,i,2)
                if form!=2:walk(*args[0],current)
                else:walk(*args[1],current)
                i=end;continue
            if cmd=='LMdoubtdata':
                _,i=macro_args(s,i,1);continue
            if cmd=='LMcancelledDoubts':
                _,i=macro_args(s,i,1)
                if form==2:
                    if not current:problems.append('unidentified cancelled-anchor')
                    else:found[current]='cancelled-anchor'
                continue
            if cmd in LINK_KINDS:
                args,end=macro_args(s,i,1)
                if not current:problems.append('unidentified '+cmd)
                else:found[current]=LINK_KINDS[cmd]
                walk(*args[0],current);i=end;continue
    walk(0,len(s))
    return found,problems


def inspect_reader(path,lang,form):
    text=path.read_text();match=re.search(r'^% COMMON MASTER BODY SHA256 ([0-9a-f]{64})\n',text,re.M)
    if not match:raise ValueError('Missing common-body hash header')
    end=text.rfind(r'\end{document}')
    if end<match.end():raise ValueError('Missing document end after common body')
    body=text[match.end():end];actual=sha(body)
    clean=editorial.blank_comments(text)
    external=re.findall(r'\\(?:input|include|includegraphics|bibliography|addbibresource|includepdf)\b[^\n]*',clean)
    lua_external=re.findall(r'\b(?:dofile|loadfile)\s*\([^\n]*',clean)
    # A URL path is not a local filesystem path. These patterns capture
    # machine-specific roots and drive paths, not manuscript slash notation.
    privacy=[]
    patterns=[r'(?:[/]workspace[/]|[/]home[/]|[/]Users[/]|[/]tmp[/]|[/]root[/]|[/]opt[/]|[/]usr[/]share[/])[^\s}\]"<>]*',r'\b[A-Za-z]:\\(?:Users|Documents|Windows|Program Files|Temp|home|workspace)\\[^\s}]*',r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b']
    for pattern in patterns:
        for m in re.finditer(pattern,text):privacy.append({'line':text.count('\n',0,m.start())+1,'class':'local path or email'})
    wrapper_safe=r'\newcommand\LMsourceMark[2]{{' in text
    declared=re.search(r'\\LMform\s*=\s*([012])',text[:match.start()])
    if (actual,form) not in STATIC_CACHE:STATIC_CACHE[(actual,form)]=expected_mark_ids(body,form)
    static,problems=STATIC_CACHE[(actual,form)]
    if actual not in LITERAL_CACHE:
        LITERAL_CACHE[actual]=dict(collections.Counter(r['kind'] for r in instrument_marks.instrument(instrument_marks.deinstrument(body))[1]))
    record={'file':path.name,'tex_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'language':lang,'form':form,'declared_body_sha256':match[1],
            'actual_body_sha256':actual,'body_hash_matches':actual==match[1],
            'declared_form_matches':bool(declared and int(declared[1])==form),
            'single_file_portable':not external and not lua_external,
            'external_dependencies':external+lua_external,'privacy_hits':privacy,
            'unbraced_script_wrapper_grouped':wrapper_safe,
            'literal_body_mark_counts':LITERAL_CACHE[actual],
            'expected_executed_mark_counts':dict(collections.Counter(static.values())),
            'expected_executed_markers':len(static),'static_mark_problems':problems}
    ledger=path.with_suffix('.lm-links.tsv')
    if ledger.exists():
        rows=read_tsv(ledger);observed={r['source_id']:r['kind'] for r in rows}
        missing=sorted(set(static)-set(observed));extra=sorted(set(observed)-set(static))
        wrong=[k for k in set(static)&set(observed) if static[k]!=observed[k]]
        record['compiled_marker_ledger']={
            'executed_unique_markers':len(rows),'counts_by_kind':dict(collections.Counter(r['kind'] for r in rows)),
            'expected_ids_missing':missing,'unexpected_ids':extra,'kind_mismatches':wrong,
            'unlinked_ids':[r['source_id'] for r in rows if int(r['linked_runs'])==0],
            'extra_math_or_measurement_expansions':sum(max(0,int(r.get('expansions','1'))-1) for r in rows),
            'distinct_scans':len({(r['cote'],r['scan']) for r in rows})}
    return record,body


def unit_reassembly(index):
    man=json.loads((SOURCES/'en/MANIFEST.json').read_text());units={u['id']:u for u in man['units']};results=[]
    for pk in man['packages']:
        package=pk['package'];frpieces=[];enpieces=[];unit_ok=True
        for uid in pk['units']:
            u=units[uid];fr=(SOURCES/'en/french_units'/(uid+'.tex')).read_text()
            en=(SOURCES/'en/units'/package/(uid+'.tex')).read_text()
            frpieces.append(fr);enpieces.append(u['lead']+en.strip('\n')+u['trail'])
            unit_ok&=(re.findall(r'\\scanpage\{(\d+)\}',fr)==u['scans'] and re.findall(r'\\scanpage\{(\d+)\}',en)==u['scans'])
        results.append({'package':package,'units':len(pk['units']),
            'french_units_reassemble':''.join(frpieces)==(SOURCES/'fr/texts'/(package+'.tex')).read_text(),
            'english_units_reassemble':''.join(enpieces)==(SOURCES/'en/packages'/(package+'_en.tex')).read_text(),
            'unit_scan_sequences_match':bool(unit_ok)})
    return {'units':len(units),'packages':len(results),'results':results,
            'all_pass':len(units)==245 and len(results)==116 and all(r['french_units_reassemble'] and r['english_units_reassemble'] and r['unit_scan_sequences_match'] for r in results)}


def glossary_annotations(annotation,entries,language,package,glossary):
    if language!='en':return annotation,entries
    for g in glossary:
        if g['package']!=package:continue
        if annotation.count(g['old'])!=g['expected_occurrences']:raise ValueError('Glossary original does not match exactly')
        annotation=annotation.replace(g['old'],r'\var{'+g['old']+'}{'+g['new']+'}{glossary consistency}{'+g['id']+'}')
        entries.append(dict(id=g['id'],package=package,cote=g['cote'],scan=int(g['scan']),source_line=g['source_line'],source_path=g['source'],place=g['id'],manuscript=g['old'],corrected=g['new'],corrected_tex=g['new'],kind=g['kind'],reason=g['reason'],argument=g['old'],math_mode=False,doubts=[],parent_id='',inherited_doubt=False))
    return annotation,entries


def rebuild_body(index,packages,language,stage='build'):
    """Reproduce documented framing without writing a root build artifact."""
    import build_readers as builder
    pieces=[];cote=None
    for row in index:
        package=row['package'];ann,entries,prov=packages[package]
        if cote!=row['cote']:
            cote=row['cote'];pieces += [r'\clearpage\LMcote{'+cote+'}',r'\section*{Cote '+cote+r'}\addcontentsline{toc}{section}{Cote '+cote+'}']
        pieces += ['% BEGIN PACKAGE '+package,r'\ifnum\LMform<2\Needspace{11\baselineskip}\subsection*{Scans '+row['scans'].replace('-','--')+r'}\fi']
        scans=split_scans(ann)
        if scans and scans[0][1]:pieces.append(ann[:scans[0][1]])
        for scan,a,b in scans:
            scan_text=ann[a:b].rstrip();deferred_spacing=''
            # The source-local scan495 reservation must follow the generated
            # apparatus for scan494. This is framing, not a source reading.
            if package=='LM_C3-492-510' and scan==494 and stage!='baseline':
                reservation=re.search(r'(\\Needspace\{(?:6|18)\\baselineskip\})\s*$',scan_text)
                if reservation:
                    deferred_spacing=reservation.group(1)
                    scan_text=scan_text[:reservation.start()].rstrip()
            pieces.append(scan_text+'\n')
            pieces.append(r'\LMflushnotes\LMflushpages'+'\n'+builder.apparatus([e for e in entries if e['scan']==scan],language))
            kinds={'landscape layout','landscape diagram','inline formula displayed','inline formula moved to display'}
            placements=[r for r in prov['layout'] if r.get('scan')==scan and (r.get('kind') in kinds or r.get('id') in ('140-2-302-D1','140-2-344-D1','140-3-561-D1','140-2-348-M1'))]
            if placements:
                pieces += [r'\ifnum\LMform=1',r'\par\begingroup\footnotesize']
                for r in placements:
                    reason=r.get('reason','')
                    if language=='fr':reason=('Diagramme reporté sur une page en paysage, avec un repère à son emplacement; les objets, flèches et lectures restent identiques.' if 'landscape' in r.get('kind','') else 'Formule du texte courant disposée sur deux lignes, avec un repère à son emplacement; les symboles et lectures restent identiques.')
                    pieces.append(r'\noindent\texttt{'+r.get('id','')+r'} \textit{'+('Disposition' if language=='fr' else 'Layout placement')+'}. '+builder.esc(reason)+r'\par')
                pieces += [r'\endgroup\fi']
            if deferred_spacing:pieces.append(deferred_spacing)
        pieces += ['% END PACKAGE '+package]
    body='\n'.join(pieces)+'\n';return instrument_marks.instrument(body)


def verify(stage='build',recipe=True):
    index=read_tsv(SOURCES/'fr/records/CURRENT_TEXT_INDEX.tsv');glossary=json.loads((WORK/'data/glossary_edits.json').read_text())
    directory=WORK/stage;result={'stage':stage,'source_units':unit_reassembly(index),'readers':[],'languages':{},'errors':[],'warnings':[]}
    bodies={};archive_manifests={lang:{r['path']:r for r in read_tsv(SOURCES/('LM_'+lang.upper()+'_MANIFEST.tsv'))} for lang in ('fr','en')}
    for book,(lang,form) in BOOKS.items():
        path=directory/(book+'.tex')
        if not path.exists():result['errors'].append('Missing reader '+path.name);continue
        try:
            r,body=inspect_reader(path,lang,form);result['readers'].append(r);bodies[book]=body
            print('Reader checked',book,flush=True)
        except Exception as e:result['errors'].append(book+': '+safe_error(e));continue
        if not r['body_hash_matches']:result['errors'].append(book+': common-body hash mismatch')
        if not r['declared_form_matches']:result['errors'].append(book+': declared form differs from requested edition')
        if not r['single_file_portable']:result['errors'].append(book+': external source dependency')
        if r['privacy_hits']:result['errors'].append(book+': local path or email')
        if not r['unbraced_script_wrapper_grouped']:result['errors'].append(book+': unsafe unbraced-script instrumentation wrapper')
        if r['static_mark_problems']:result['errors'].append(book+': static linked mark lacks a source ID')
        ledger=r.get('compiled_marker_ledger')
        if ledger:
            if ledger['expected_ids_missing'] or ledger['unexpected_ids'] or ledger['kind_mismatches']:result['errors'].append(book+': expected/executed source-mark ID mismatch')
            if ledger['unlinked_ids']:result['errors'].append(book+': unlinked executed source mark')
        else:result['warnings' if stage=='baseline' else 'errors'].append(book+': no completed compiled-marker ledger yet')
    paired_ids={}
    for lang in ('fr','en'):
        pp=directory/(lang+'_provenance.json')
        if not pp.exists():result['errors'].append('Missing '+pp.name);continue
        prov=json.loads(pp.read_text());pmap={p['package']:p for p in prov['packages']};allpackages={};canonical=[];package_checks=[]
        source_totals=collections.Counter();cote_totals=collections.defaultdict(collections.Counter);current_entries=[]
        for row in index:
            package=row['package'];relative=('fr/texts/'+package+'.tex' if lang=='fr' else 'en/packages/'+package+'_en.tex')
            rawbytes=(SOURCES/relative).read_bytes();raw=(SOURCES/relative).read_text();p=pmap.get(package)
            check={'package':package,'cote':row['cote'],'source_path':relative,'checks':{},'errors':[]}
            def test(key,value):
                check['checks'][key]=bool(value)
                if not value:check['errors'].append(key)
            try:
                if p is None:raise ValueError('Package missing from provenance')
                test('archive_sha256',hashlib.sha256(rawbytes).hexdigest()==archive_manifests[lang][relative]['sha256'])
                test('source_sha256',sha(raw)==p['source_sha256'])
                scans=re.findall(r'\\scanpage\{(\d+)\}',editorial.blank_comments(raw));a,b=map(int,row['scans'].split('-'))
                test('scan_sequence',scans==[str(n) for n in range(a,b+1)]==p['scan_sequence'])
                counts=mark_counts(raw);source_totals.update(totals(counts));cote_totals[row['cote']].update(totals(counts))
                fixed,mechanical=mechanical_repairs.repair(raw,package,lang)
                test('mechanical_exact_reversal',mechanical_repairs.verify_reversal(raw,fixed,mechanical))
                old_mechanical=p.get('mechanical',[])
                fields=('stage','before','after','offset_before','offset_after')
                test('mechanical_records_match',[[r[k] for k in fields] for r in mechanical]==[[r[k] for k in fields] for r in old_mechanical])
                layout=replay_layout(fixed,p.get('layout',[]))
                test('layout_record_replay_hash',sha(layout)==p['layout_source_sha256'])
                test('layout_preserves_scan_and_doubt_counts',mark_counts(layout)==counts)
                if recipe:
                    import layout_repairs
                    current,_=(layout_repairs.repair_empty_cells(fixed,package,lang) if stage=='baseline' else layout_repairs.repair(fixed,package,lang))
                    test('current_layout_recipe_matches',current==layout)
                annotation,entries,metadata=editorial.annotate(layout,package,lang)
                test('editorial_exact_source_projection',editorial.project(annotation,'source')==layout)
                test('corrected_projection_mark_counts',mark_counts(editorial.project(annotation,'corrected'))==counts)
                raw_annotation,raw_entries,raw_meta=editorial.annotate(raw,package,lang);canonical+=raw_entries
                test('variant_ids_unchanged_by_layout',[e['id'] for e in entries]==[e['id'] for e in raw_entries])
                annotation,entries=glossary_annotations(annotation,entries,lang,package,glossary)
                test('annotated_package_sha256',sha(annotation)==p['master_body_sha256'])
                test('variant_count',len(entries)==p['variants'])
                test('all_variants_typed_and_reasoned',all(e.get('kind') and e.get('reason') and e.get('id') for e in entries))
                current_entries+=entries;allpackages[package]=(annotation,entries,p)
            except Exception as e:check['errors'].append(safe_error(e))
            package_checks.append(check)
            if check['errors']:result['errors'].append(lang+'/'+package+': '+', '.join(check['errors']))
        language={'packages':len(pmap),'source_counts':dict(source_totals),'source_counts_by_cote':{c:dict(v) for c,v in cote_totals.items()},'package_checks':package_checks,
                  'authorial_variants':len(canonical),'all_variants':len(current_entries),'variant_kinds':dict(collections.Counter(e['kind'] for e in current_entries))}
        test_expected=116 if lang=='fr' else 116
        if len(pmap)!=test_expected:result['errors'].append(lang+': package total is not 116')
        if dict(source_totals)!={'illegible':1261,'scanpage':1588,'unsure':17117}:result['errors'].append(lang+': source-mark totals differ')
        if len(canonical)!=10888:result['errors'].append(lang+': authorial variant total differs')
        paired_ids[lang]=[e['id'] for e in canonical]
        logpath=WORK/'records'/('CHANGES_'+lang.upper()+'.tsv')
        if logpath.exists():
            changes=read_tsv(logpath);byid={r['id']:r for r in changes};mismatches=[]
            for e in canonical:
                r=byid.get(e['id'])
                if r is None or any(r.get(k)!=str(e[k]) for k in ('manuscript','corrected','kind','reason')):mismatches.append(e['id'])
            extras=sorted(set(byid)-{e['id'] for e in canonical})
            expected_extras={g['id'] for g in glossary} if lang=='en' else set()
            language['raw_source_change_log']={'rows':len(changes),'authorial_rows_match':not mismatches,'mismatched_ids':mismatches,'additional_ids':extras,'expected_translation_only_ids':sorted(expected_extras)}
            if mismatches:result['errors'].append(lang+': change-log readings do not match raw source')
            if set(extras)!=expected_extras:result['warnings' if stage=='baseline' else 'errors'].append(lang+': translation-only change-log rows are not finalized')
        langbodies=[body for book,body in bodies.items() if BOOKS[book][0]==lang]
        hashes={sha(body) for body in langbodies};language['shared_actual_body_hashes']=sorted(hashes)
        language['all_forms_share_one_body']=len(hashes)==1
        if len(hashes)!=1:result['errors'].append(lang+': reader forms do not share one body')
        if hashes and prov['body_sha256'] not in hashes:result['errors'].append(lang+': provenance common-body hash differs')
        if len(allpackages)==116:
            expected,marks=rebuild_body(index,allpackages,lang,stage)
            language['recomputed_body_sha256']=sha(expected);language['recomputed_body_matches']=all(body==expected for body in langbodies)
            language['literal_mark_records']=len(marks);language['literal_counts_by_kind']=dict(collections.Counter(r['kind'] for r in marks))
            if not language['recomputed_body_matches']:result['errors'].append(lang+': assembled common body differs from the verified source pipeline')
            mpath=directory/(lang+'_source_marks.json')
            if mpath.exists():
                language['instrumentation_ledger_matches']=json.loads(mpath.read_text())==marks
                if not language['instrumentation_ledger_matches']:result['errors'].append(lang+': literal source-mark ledger differs')
        result['languages'][lang]=language
        print('Language stages checked',lang,flush=True)
    result['paired_authorial_variant_ids_match']=paired_ids.get('fr')==paired_ids.get('en') and len(paired_ids.get('fr',[]))==10888
    if not result['paired_authorial_variant_ids_match']:result['errors'].append('French/English authorial variant IDs differ')
    if not result['source_units']['all_pass']:result['errors'].append('Translation-unit source reconstruction failed')
    result['status']='PASS' if not result['errors'] else 'FAIL'
    return result


def markdown(result):
    out=['# Master and reader source integrity','',f"Audit stage: `{result['stage']}`. **{result['status']}**.",'',
         'This audit reconstructs every package from its immutable source, checks every recorded mechanical and layout stage, reverses editorial annotation and link instrumentation, and compares the complete common body in every form. Compilation, visual layout and PDF annotation geometry are reported separately.','',
         '## Source coverage','',f"The unit manifest contains {result['source_units']['units']} translation units in {result['source_units']['packages']} packages. Exact French-unit and English-unit reassembly: **{'PASS' if result['source_units']['all_pass'] else 'FAIL'}**.",'',
         '| Language | Packages | Scans | Doubtful marks | Illegible marks | Authorial variants | All variants |','|---|---:|---:|---:|---:|---:|---:|']
    for lang,d in result['languages'].items():
        c=d['source_counts'];out.append(f"| {lang.upper()} | {d['packages']} | {c.get('scanpage',0)} | {c.get('unsure',0)} | {c.get('illegible',0)} | {d['authorial_variants']} | {d['all_variants']} |")
    out+=['',f"The paired French/English authorial variant ID sequence agrees: **{'PASS' if result['paired_authorial_variant_ids_match'] else 'FAIL'}**.",'',
          '## Shared master bodies','', '| Language | One body shared by all forms | Recomputed source pipeline matches | SHA-256 |','|---|---|---|---|']
    for lang,d in result['languages'].items():out.append('| '+lang.upper()+' | '+str(d['all_forms_share_one_body'])+' | '+str(d.get('recomputed_body_matches',False))+' | '+', '.join('`'+h+'`' for h in d['shared_actual_body_hashes'])+' |')
    out+=['','Original ZIP bytes are checked against their manifest hashes. Text processing uses Python newline normalization (CRLF to LF); this changes no printed content. The source-reading fields in the change logs are checked against annotations of the raw checked package texts, before typesetting modifications. A layout wrapper is therefore not mistaken for a new manuscript reading. Each source-local layout replacement is replayed within its recorded scan.','',
          '## Mark counts and their meaning','',
          'Original source marks, literal master occurrences, executed source IDs, TeX expansions and PDF link runs are different counts. The common master contains both variant branches and the apparatus/carryover alternatives. Its literal mark count is consequently larger than the original-source count. The form selector identifies the exact literal IDs that should execute in each reader. LuaLaTeX may expand an identified mark several times while measuring mathematics; those expansions reuse the same source ID. A marked passage may occupy several PDF link rectangles. No equality between these distinct quantities is assumed.','',
          '| Reader | Expected executed source IDs | Ledger source IDs | Missing expected IDs | Unexpected IDs | Unlinked IDs |','|---|---:|---:|---:|---:|---:|']
    for r in result['readers']:
        l=r.get('compiled_marker_ledger')
        out.append('| '+r['file']+' | '+str(r['expected_executed_markers'])+' | '+(str(l['executed_unique_markers']) if l else 'pending')+' | '+(str(len(l['expected_ids_missing'])) if l else 'pending')+' | '+(str(len(l['unexpected_ids'])) if l else 'pending')+' | '+(str(len(l['unlinked_ids'])) if l else 'pending')+' |')
    out+=['','## Portability and privacy','',
          '| Reader | Actual body hash agrees | No external source/assets | No local paths or email addresses | Safe grouping for unbraced scripts |','|---|---|---|---|---|']
    for r in result['readers']:out.append(f"| {r['file']} | {r['body_hash_matches']} | {r['single_file_portable']} | {not r['privacy_hits']} | {r['unbraced_script_wrapper_grouped']} |")
    out+=['','The files may load standard TeX Live packages and fonts. Their Lua code is embedded; relative audit-output filenames do not constitute external input dependencies. The instrumentation wrapper uses literal TeX grouping, so original constructions such as an unbraced `_{\\unsure}`-style script do not acquire a forbidden `\\begingroup` token at the math-field boundary.','', '## Exceptions','']
    if result['errors']:out += ['- '+e for e in result['errors']]
    else:out.append('No failed source-integrity checks.')
    if result['warnings']:out+=['','Development or completion notes:','']+['- '+e for e in result['warnings']]
    return '\n'.join(out)+'\n'


def refresh_ledgers(stage):
    """Refresh runtime ledgers without repeating an unchanged source replay."""
    path=WORK/'data'/('master_integrity_'+stage+'.json')
    result=json.loads(path.read_text());old={r['file']:r for r in result['readers']}
    names=tuple(BOOKS)
    result['errors']=[e for e in result['errors'] if not any(e.startswith(name+':') for name in names)]
    result['warnings']=[e for e in result['warnings'] if not any(e.startswith(name+':') for name in names)]
    result['readers']=[]
    glossary=json.loads((WORK/'data/glossary_edits.json').read_text())
    for lang,language in result['languages'].items():
        changes=read_tsv(WORK/'records'/('CHANGES_'+lang.upper()+'.tsv'))
        expected={g['id']:g for g in glossary} if lang=='en' else {}
        extra={r['id']:r for r in changes if r['kind']=='glossary consistency'}
        message=lang+': translation-only change-log rows are not finalized'
        valid=set(extra)==set(expected) and all(
            extra[k]['manuscript']==g['old'] and extra[k]['corrected']==g['new'] and
            extra[k]['reason']==g['reason'] and extra[k]['source_path']==g['source']
            for k,g in expected.items())
        if valid:
            result['errors']=[e for e in result['errors'] if e!=message]
            result['warnings']=[e for e in result['warnings'] if e!=message]
        elif message not in result['errors']:result['errors'].append(message)
        log=language['raw_source_change_log'];log['rows']=len(changes)
        log['additional_ids']=sorted(extra);log['translation_only_rows_match']=valid
    for book,(lang,form) in BOOKS.items():
        try:r,body=inspect_reader(WORK/stage/(book+'.tex'),lang,form)
        except Exception as e:result['errors'].append(book+': '+safe_error(e));continue
        result['readers'].append(r)
        if old.get(r['file'],{}).get('actual_body_sha256')!=r['actual_body_sha256']:
            result['errors'].append(book+': common body changed; repeat the full source replay')
        for key,message in [('body_hash_matches','common-body hash mismatch'),('declared_form_matches','declared form mismatch'),('single_file_portable','external input dependency'),('unbraced_script_wrapper_grouped','unsafe script grouping')]:
            if not r[key]:result['errors'].append(book+': '+message)
        if r['privacy_hits']:result['errors'].append(book+': local path or email')
        if r['static_mark_problems']:result['errors'].append(book+': unidentified static mark')
        ledger=r.get('compiled_marker_ledger')
        if ledger:
            if ledger['expected_ids_missing'] or ledger['unexpected_ids'] or ledger['kind_mismatches']:result['errors'].append(book+': expected/executed source-mark ID mismatch')
            if ledger['unlinked_ids']:result['errors'].append(book+': unlinked executed source mark')
        else:result['errors'].append(book+': missing compiled source-mark ledger')
        print('Ledger refreshed',book,flush=True)
    result['status']='PASS' if not result['errors'] else 'FAIL'
    return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--stage',default='build');ap.add_argument('--skip-current-recipe',action='store_true');ap.add_argument('--ledgers-only',action='store_true');args=ap.parse_args()
    result=refresh_ledgers(args.stage) if args.ledgers_only else verify(args.stage,not args.skip_current_recipe)
    (WORK/'data'/('master_integrity_'+args.stage+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    (WORK/'records/MASTER_INTEGRITY.md').write_text(markdown(result))
    print(json.dumps({'stage':args.stage,'status':result['status'],'readers':len(result['readers']),'errors':result['errors'],'warnings':result['warnings']},ensure_ascii=False,indent=2))
    return 0 if result['status']=='PASS' else 1

if __name__=='__main__':raise SystemExit(main())
