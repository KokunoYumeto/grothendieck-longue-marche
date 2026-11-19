#!/usr/bin/env python3
"""Mechanical bookkeeping only; all readings and decisions are supplied by the reader.
No OCR or automated manuscript recognition is used.
"""
from pathlib import Path
import csv, json, re, sys, hashlib
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
PREFIX=ROOT.name
WIT=BASE/'source'/(PREFIX+'_witnesses')
SCANS=BASE/'source'/(PREFIX+'_scans')
ROWS=list(csv.DictReader((WIT/'page_map.tsv').open(),delimiter='\t'))
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def row(cote,scan): return next(r for r in ROWS if int(r['cote'])==int(cote) and int(r['our_scan'])==int(scan))
def stem(r): return Path(r['codex_file']).stem
def hua(r):
    t=(WIT/r['hua_file']).read_text()
    pat=re.compile(r'\\page\s*\{\s*(\d+)\s*\}')
    marks=list(pat.finditer(t))
    for i,m in enumerate(marks):
        if int(m.group(1))==int(r['their_page']):
            return t[m.start():marks[i+1].start() if i+1<len(marks) else len(t)]
    return '[H has '+r['hua_has']+'; no page marker. No H textual collation rows.]'
def esc(x): return str(x).replace('|','&#124;').replace('\n',' / ')
def rebuild_changes():
    records=[]
    for r in ROWS:
        p=ROOT/'decisions'/(stem(r)+'.json')
        if p.exists(): records.append(json.loads(p.read_text()))
    table=['# Changes from witnesses C and H','', 'This log records visual decisions by the primary reader. Macro-only differences are excluded. A retained C doubt is logged even when its text is unchanged. H pages with descriptions or no text have no collation rows.','', '| Cote / scan | Against C | Against H | High | Medium | Low |','|---|---:|---:|---:|---:|---:|']
    totals=[0]*5
    for d in records:
        vals=[sum(bool(x.get('c_changed')) for x in d['decisions']),sum(bool(x.get('h_changed')) for x in d['decisions'])]+[sum(x.get('confidence')==c for x in d['decisions']) for c in ['high','medium','low']]
        totals=[a+b for a,b in zip(totals,vals)]
        table.append('| '+str(d['cote'])+' / '+str(d['scan'])+' | '+' | '.join(map(str,vals))+' |')
    table+=['| **Total** | '+' | '.join(map(str,totals))+' |','','## Consequential corrections','']
    for d in records:
        for x in d['decisions']:
            if x.get('consequential'):table.append('- '+str(d['cote'])+'/'+str(d['scan'])+', '+x['place']+': '+x['consequential'])
    if not any(x.get('consequential') for d in records for x in d['decisions']):table.append('None recorded so far.')
    for d in records:
        table+=['','## Cote '+str(d['cote'])+' — scan '+str(d['scan']), '',d.get('review',''),'', '| Place | C | H | Final | What the scan shows; crop | Confidence |','|---|---|---|---|---|---|']
        for x in d['decisions']:
            table.append('| '+' | '.join(esc(x.get(k,'')) for k in ['place','c','h','final','shows','confidence'])+' |')
        if not d['decisions']:table.append('| Whole page | Retained | '+d.get('h_status','')+' | C retained after visual reading | Whole and both half images; page-specific inspection recorded below | — |')
        table+=['','Unresolved: '+d.get('unresolved','None.'),'']
    (ROOT/(PREFIX+'_changes.md')).write_text('\n'.join(table)+'\n')
def _tex_control(text, start):
    """Return a literal TeX control token and its exclusive end offset."""
    match=re.match(r'\\([A-Za-z@]+|.)',text[start:],re.S)
    return (match.group(1),start+len(match.group(0))) if match else ('',start+1)
def _tex_group_end(text, start):
    """Read a balanced brace/optional group without interpreting its contents."""
    if start>=len(text) or text[start] not in '{[':return None
    closing='}' if text[start]=='{' else ']'
    stack=[closing];i=start+1
    while i<len(text):
        char=text[i]
        if char=='\\':_,i=_tex_control(text,i);continue
        if char=='%':
            end=text.find('\n',i);i=len(text) if end<0 else end;continue
        if char=='{':stack.append('}')
        elif char=='[' and stack[-1]==']':stack.append(']')
        elif char==stack[-1]:
            stack.pop()
            if not stack:return i+1
        i+=1
    return None
def _active_tex_source(text):
    """Mask comments, verbatim regions and definitions; retain source offsets."""
    chars=list(text);i=0
    def mask(start,end):
        chars[start:end]=['\n' if c=='\n' else ' ' for c in text[start:end]]
    def space(position):
        while position<len(text) and text[position].isspace():position+=1
        return position
    definitions={'newcommand','renewcommand','providecommand','DeclareRobustCommand'}
    verbatim={'verbatim','verbatim*','Verbatim','lstlisting','minted','comment'}
    while i<len(text):
        if text[i]=='%':
            end=text.find('\n',i);end=len(text) if end<0 else end
            mask(i,end);i=end;continue
        if text[i]!='\\':i+=1;continue
        start=i;command,end=_tex_control(text,i)
        if command=='verb':
            cursor=end+int(end<len(text) and text[end]=='*')
            if cursor<len(text) and not text[cursor].isspace():
                finish=text.find(text[cursor],cursor+1)
                finish=len(text) if finish<0 else finish+1
                mask(start,finish);i=finish;continue
        if command=='begin':
            cursor=space(end);finish=_tex_group_end(text,cursor)
            environment=text[cursor+1:finish-1] if finish else ''
            if environment in verbatim:
                match=re.search(r'\\end\s*\{'+re.escape(environment)+r'\}',text[finish:])
                finish=len(text) if match is None else finish+match.end()
                mask(start,finish);i=finish;continue
        if command in definitions:
            cursor=space(end+int(end<len(text) and text[end]=='*'))
            if cursor<len(text) and text[cursor]=='{':cursor=_tex_group_end(text,cursor)
            elif cursor<len(text) and text[cursor]=='\\':_,cursor=_tex_control(text,cursor)
            else:cursor=None
            if cursor is not None:
                cursor=space(cursor)
                while cursor<len(text) and text[cursor]=='[':
                    cursor=_tex_group_end(text,cursor)
                    if cursor is None:break
                    cursor=space(cursor)
                if cursor is not None and cursor<len(text) and text[cursor]=='{':
                    finish=_tex_group_end(text,cursor)
                    if finish is not None:mask(start,finish);i=finish;continue
        if command in {'def','gdef','edef','xdef'}:
            cursor=end
            while cursor<len(text) and text[cursor]!='{':
                if text[cursor]=='\\':_,cursor=_tex_control(text,cursor)
                else:cursor+=1
            finish=_tex_group_end(text,cursor)
            if finish is not None:mask(start,finish);i=finish;continue
        i=end
    return ''.join(chars)
def _split_unsure_alternatives(argument):
    """Split unescaped top-level pipes, preserving nested and math delimiters."""
    parts=[];start=0;stack=[];math=None;i=0
    pairs={'{':'}','[':']','(':')'}
    sized={'left','right','middle','big','Big','bigg','Bigg','bigl','bigr','Bigl','Bigr','biggl','biggr','Biggl','Biggr'}
    while i<len(argument):
        char=argument[i]
        if char=='\\':
            command,end=_tex_control(argument,i)
            if command in {'(','['}:math=')' if command=='(' else ']'
            elif command in {')',']'} and math==command:math=None
            elif command in sized:
                cursor=end
                while cursor<len(argument) and argument[cursor].isspace():cursor+=1
                if cursor<len(argument) and argument[cursor]=='|':end=cursor+1
            i=end;continue
        if char=='$':
            delimiter='$$' if argument.startswith('$$',i) else '$'
            if math is None:math=delimiter
            elif math==delimiter:math=None
            i+=len(delimiter);continue
        if math is not None:i+=1;continue
        if char in pairs:stack.append(pairs[char])
        elif char in '}])':
            if not stack or stack[-1]!=char:return argument,[]
            stack.pop()
        elif char=='|' and not stack:
            parts.append(argument[start:i].strip());start=i+1
        i+=1
    if stack or math is not None or not parts:return argument,[]
    parts.append(argument[start:].strip())
    if any(not part for part in parts):return argument,[]
    return parts[0],parts[1:]
def _unsure_entries(text):
    """Extract active literal unsure arguments with physical source positions."""
    active=_active_tex_source(text);entries=[];notes=[];i=0
    while i<len(active):
        if active[i]!='\\':i+=1;continue
        start=i;command,i=_tex_control(active,i)
        if command!='unsure':continue
        line=active.count('\n',0,start)+1
        column=start-active.rfind('\n',0,start)
        cursor=i
        while cursor<len(active) and active[cursor].isspace():cursor+=1
        if cursor>=len(active) or active[cursor]!='{':
            notes.append((line,column,'An active unsure token has no braced argument; no reading was inferred.'));continue
        end=_tex_group_end(active,cursor)
        if end is None:
            notes.append((line,column,'An unsure argument has no matching closing brace; no reading was inferred.'));continue
        argument=active[cursor+1:end-1].strip()
        reading,alternatives=_split_unsure_alternatives(argument)
        entries.append({'line':line,'column':column,'argument':argument,
                        'macro':text[start:end],'reading':reading,'alternatives':alternatives})
    return entries,notes
def _doubt_literal(value):
    """Render source text literally in a Markdown table; fold source newlines."""
    value=value.replace('\r\n','\n').replace('\n',' ')
    if not value:return '(empty argument)'
    # Entity-escape TeX and Markdown punctuation so neither table parsing nor
    # inline emphasis can alter the displayed literal source characters.
    translations={ord(char):'&#'+str(ord(char))+';' for char in '&<>|\\`*_[]'}
    return '<code>'+value.translate(translations)+'</code>'
def _normalize_doubt_whitespace(value):
    """Collapse whitespace runs and trim ends; preserve every nonspace character."""
    return re.sub(r'\s+',' ',value).strip()
def _audit_source_text(page_bytes):
    """Use the same UTF-8/universal-newline convention as Path.read_text()."""
    if not isinstance(page_bytes,bytes):
        raise ValueError('Audit page context must contain exact page bytes.')
    return page_bytes.decode('utf-8').replace('\r\n','\n').replace('\r','\n')

def _audit_json_loads(text, label='audit_confidence.json'):
    """Parse strict JSON, including rejection of duplicate object keys."""
    if not isinstance(text,str):
        raise ValueError(label+': JSON input must be text.')
    def pairs(items):
        result={}
        for key,value in items:
            if key in result:
                raise ValueError(label+': duplicate JSON key '+repr(key)+'.')
            result[key]=value
        return result
    def constant(value):
        raise ValueError(label+': non-finite JSON constant '+value+' is forbidden.')
    try:
        return json.loads(text,object_pairs_hook=pairs,parse_constant=constant)
    except json.JSONDecodeError as exc:
        raise ValueError(label+': invalid JSON at line '+str(exc.lineno)+', column '+str(exc.colno)+'.') from exc

def _validate_audit_confidence(audit_text, page_contexts):
    """Validate primary-only occurrence values; return an exact keyed index.

    Contexts are supplied from committed output, never from paths in the JSON.
    Each context has page_bytes, decision_file and the parsed record. No
    reading, confidence, reference, coordinate or macro text is inferred.
    """
    if audit_text is None:return {}
    if not isinstance(page_contexts,dict):raise ValueError('Audit page contexts must be a mapping.')
    data=_audit_json_loads(audit_text)
    def object_fields(value, expected, where):
        if not isinstance(value,dict) or set(value)!=set(expected):
            raise ValueError(where+': required fields are '+', '.join(expected)+'; unknown or missing fields are forbidden.')
    def positive_integer(value, where):
        if type(value) is not int or value<1:
            raise ValueError(where+': must be a positive integer, not a boolean.')
    object_fields(data,('version','pages'),'audit_confidence.json')
    if type(data['version']) is not int or data['version']!=1:
        raise ValueError('audit_confidence.json: version must be integer 1.')
    if not isinstance(data['pages'],dict):
        raise ValueError('audit_confidence.json: pages must be an object.')
    index={};locations=set()
    for page_file,block in data['pages'].items():
        where='audit_confidence.json: '+page_file
        if not re.fullmatch(r'pages/[^/\\]+\.tex',page_file) or page_file not in page_contexts:
            raise ValueError(where+': unknown or uncommitted page path.')
        object_fields(block,('page_sha256','occurrences'),where)
        digest=block['page_sha256']
        if not isinstance(digest,str) or not re.fullmatch(r'[0-9a-f]{64}',digest):
            raise ValueError(where+': page_sha256 must be 64 lowercase hexadecimal characters.')
        context=page_contexts[page_file]
        page_bytes=context.get('page_bytes') if isinstance(context,dict) else None
        if not isinstance(page_bytes,bytes):
            raise ValueError(where+': exact current page bytes are unavailable.')
        if hashlib.sha256(page_bytes).hexdigest()!=digest:
            raise ValueError(where+': stale page_sha256; primary revalidation is required.')
        if not isinstance(block['occurrences'],list):
            raise ValueError(where+': occurrences must be an array.')
        expected_record='decisions/'+page_file[len('pages/'):-len('.tex')]+'.json'
        if context.get('decision_file')!=expected_record:
            raise ValueError(where+': mapped decision filename is inconsistent.')
        record=context.get('record')
        decisions=record.get('decisions') if isinstance(record,dict) else None
        if not isinstance(decisions,list):
            raise ValueError(where+': current mapped decision record is unavailable.')
        entries,notes=_unsure_entries(_audit_source_text(page_bytes))
        if notes:
            raise ValueError(where+': unsure parser warnings prevent exact audit validation.')
        available={(entry['line'],entry['column'],entry['macro']) for entry in entries}
        for number,item in enumerate(block['occurrences'],1):
            item_where=where+', occurrence '+str(number)
            object_fields(item,('line','column','macro','confidence','decision_ref'),item_where)
            positive_integer(item['line'],item_where+' line')
            positive_integer(item['column'],item_where+' column')
            location=(page_file,item['line'],item['column'])
            if location in locations:
                raise ValueError(item_where+': duplicate occurrence location.')
            locations.add(location)
            if not isinstance(item['macro'],str) or not item['macro']:
                raise ValueError(item_where+': macro must be the exact nonempty literal source string.')
            key=(item['line'],item['column'],item['macro'])
            if key not in available:
                raise ValueError(item_where+': coordinates and macro do not identify an exact active unsure occurrence; no relocation is allowed.')
            if not isinstance(item['confidence'],str) or item['confidence'] not in {'high','medium','low'}:
                raise ValueError(item_where+': confidence must be exactly high, medium or low.')
            reference=item['decision_ref']
            object_fields(reference,('file','number'),item_where+' decision_ref')
            if reference['file']!=expected_record:
                raise ValueError(item_where+': decision_ref must name this page\'s mapped record.')
            positive_integer(reference['number'],item_where+' decision_ref number')
            if reference['number']>len(decisions) or not isinstance(decisions[reference['number']-1],dict):
                raise ValueError(item_where+': decision_ref does not identify an existing decision object.')
            index[(page_file,)+key]={'confidence':item['confidence'],
                                   'decision_ref':{'file':expected_record,'number':reference['number']}}
    return index

def _unsure_confidence_detail(entry, record, page_entries=None, *, audit_entries=None, page_file=None):
    """Resolve recorded confidence mechanically, with an explicit pending reason."""
    def result(basis='pending',reason=None,matches=(),confidence='not assessed'):
        return {'confidence':confidence,'basis':basis,'pending_reason':reason,
                'decision_numbers_1_based':[number for number,_ in matches]}
    def copied(basis,matches):
        confidence=matches[0][1].get('confidence')
        if not isinstance(confidence,str) or confidence not in {'high','medium','low'}:
            return result(reason='matched_record_has_invalid_confidence',matches=matches)
        return result(basis=basis,matches=matches,confidence=confidence)
    if audit_entries:
        if not isinstance(page_file,str):
            raise ValueError('Explicit occurrence resolution requires the mapped page filename.')
        primary=audit_entries.get((page_file,entry['line'],entry['column'],entry['macro']))
        if primary is not None:
            reference=primary['decision_ref']
            return {'confidence':primary['confidence'],'basis':'primary_occurrence',
                    'pending_reason':None,'decision_numbers_1_based':[reference['number']],
                    'audit_decision_ref':dict(reference)}
    records=[(number,item) for number,item in enumerate(record.get('decisions',[]),start=1)
             if isinstance(item,dict)]
    candidates={entry[key].strip() for key in ('macro','argument','reading') if entry[key].strip()}
    direct=[(number,item) for number,item in records
            if isinstance(item.get('final'),str) and item['final']!='C retained'
            and item['final'].strip() in candidates]
    if direct:
        if len(direct)!=1:return result(reason='ambiguous_final_records',matches=direct)
        return copied('direct_final',direct)
    if page_entries is None:return result(reason='page_occurrences_not_supplied')
    expression=entry['macro']
    retained=[(number,item) for number,item in records
              if item.get('final')=='C retained' and isinstance(item.get('c'),str)]
    exact=[(number,item) for number,item in retained if item['c']==expression]
    if exact:
        if len(exact)!=1:return result(reason='ambiguous_retained_c_records',matches=exact)
        if sum(item['macro']==expression for item in page_entries)!=1:
            return result(reason='ambiguous_retained_c_occurrences',matches=exact)
        return copied('c_retained_exact',exact)
    normalized=_normalize_doubt_whitespace(expression)
    matches=[(number,item) for number,item in retained
             if _normalize_doubt_whitespace(item['c'])==normalized]
    if not matches:return result(reason='no_matching_record')
    if len(matches)!=1:return result(reason='ambiguous_retained_c_records',matches=matches)
    if sum(_normalize_doubt_whitespace(item['macro'])==normalized for item in page_entries)!=1:
        return result(reason='ambiguous_retained_c_occurrences',matches=matches)
    return copied('c_retained_whitespace',matches)
def _unsure_confidence(entry, record, page_entries=None, *, audit_entries=None, page_file=None):
    """Return existing recorded confidence or the explicit not-assessed marker."""
    return _unsure_confidence_detail(entry,record,page_entries,audit_entries=audit_entries,page_file=page_file)['confidence']
def rebuild_doubts():
    """Register committed markup; strictly validate any primary audit first."""
    front=(ROOT/'notation.md').read_text(encoding='utf-8').rstrip()
    table=[front,'','# Remaining doubts','',
           '**Preliminary legibility note:** This register is extracted mechanically from committed transcription markup. Final legibility synthesis is pending; this rebuild makes no new visual findings.','',
           'Line/place identifies physical TeX source lines and columns. Source newlines are folded for table display. Alternatives are split only at unescaped top-level pipes; a dash means no separate alternatives are encoded. Confidence is copied from one matching recorded final reading under the existing boundary-trimmed comparison. For otherwise pending entries, a decision whose final is exactly “C retained” may supply its existing confidence only when its C field uniquely matches the full unsure expression and that expression occurs once on the page. Exact comparison is tried first; whitespace comparison only collapses whitespace runs to one space and trims ends. It removes no internal separator and changes no nonspace character. Ambiguous or unmatched entries remain pending as “not assessed.” No macro expansion or new confidence assessment is performed.','',
           '| scan | line/place | reading | alternatives | confidence |','|---|---|---|---|---|']
    details=[];extraction_notes=[];count=0;page_count=0;confidence_rows=[]
    contexts={};page_rows=[]
    audit_path=ROOT/'audit_confidence.json'
    if audit_path.is_symlink():raise ValueError('audit_confidence.json must not be a symlink.')
    if audit_path.exists() and not audit_path.is_file():raise ValueError('audit_confidence.json must be a regular file.')
    audit_text=audit_path.read_text(encoding='utf-8') if audit_path.exists() else None
    supplied=_audit_json_loads(audit_text) if audit_text is not None else None
    requested=supplied.get('pages') if isinstance(supplied,dict) else None
    requested=requested if isinstance(requested,dict) else {}
    for r in ROWS:
        p=ROOT/'decisions'/(stem(r)+'.json');d={}
        if p.exists():
            if p.is_symlink():raise ValueError('Decision file must not be a symlink: '+p.name)
            record_text=p.read_text(encoding='utf-8')
            page_key='pages/'+Path(r['codex_file']).name
            d=_audit_json_loads(record_text,label='decisions/'+p.name) if page_key in requested else json.loads(record_text)
            if str(d.get('cote'))!=r['cote'] or str(d.get('scan'))!=r['our_scan']:
                raise ValueError('Decision identity does not match the page map: '+p.name)
            unresolved=d.get('unresolved','None.')
            if not isinstance(unresolved,str):raise ValueError('Unresolved text must be a string: '+p.name)
            details+=['','## Cote '+r['cote']+' — scan '+r['our_scan'],'',unresolved,'']
        page=ROOT/'pages'/Path(r['codex_file']).name
        if not page.exists():
            if d:extraction_notes.append(r['cote']+'/'+r['our_scan']+': decision metadata exists but the committed page file is missing.')
            continue
        if page.is_symlink():raise ValueError('Committed page must not be a symlink: '+page.name)
        page_bytes=page.read_bytes()
        entries,notes=_unsure_entries(_audit_source_text(page_bytes))
        page_file='pages/'+page.name
        contexts[page_file]={'page_bytes':page_bytes,'decision_file':'decisions/'+p.name,'record':d}
        page_rows.append((r,p,page,entries,notes,d))
        for line,column,note in notes:
            extraction_notes.append(r['cote']+'/'+r['our_scan']+', line '+str(line)+', column '+str(column)+': '+note)
    # This completes before the sole output write: invalid entries cannot fall
    # through to first-pass matching or leave a partly rewritten doubts file.
    audit_entries=_validate_audit_confidence(audit_text,contexts)
    if audit_entries:
        table[6]+=' Validated primary occurrence entries take precedence at their exact page, line, column and macro text; their confidence is supplied explicitly by the primary reader. Decision references provide traceability, and no confidence is inferred from them.'
    for r,p,page,entries,notes,d in page_rows:
        page_count+=1
        for entry in entries:
            alternatives='<br>'.join(_doubt_literal(value) for value in entry['alternatives']) if entry['alternatives'] else '—'
            confidence=_unsure_confidence_detail(entry,d,entries,audit_entries=audit_entries,page_file='pages/'+page.name)
            table.append('| '+esc(r['cote']+'/'+r['our_scan'])+' | line '+str(entry['line'])+', column '+str(entry['column'])+' | '+_doubt_literal(entry['reading'])+' | '+alternatives+' | '+esc(confidence['confidence'])+' |')
            confidence_rows.append({'scan':r['cote']+'/'+r['our_scan'],'page_file':'pages/'+page.name,
                                    'line':entry['line'],'column':entry['column'],
                                    'decision_file':'decisions/'+p.name,**confidence})
            count+=1
    if not count:table+=['','No active braced unsure entries were found in the committed page files.']
    table+=['','# Page detail from decision records','']+details
    if not details:table.append('No decision records are present.')
    if extraction_notes:table+=['','# Mechanical extraction notes','']+['- '+note for note in extraction_notes]
    # Do not emit values validated against a page that changed during rebuild.
    for page_file in {key[0] for key in audit_entries}:
        if (ROOT/page_file).read_bytes()!=contexts[page_file]['page_bytes']:
            raise ValueError('Audited page changed during rebuild: '+page_file)
    if audit_entries and audit_path.read_text(encoding='utf-8')!=audit_text:
        raise ValueError('audit_confidence.json changed during rebuild.')
    (ROOT/(PREFIX+'_doubts.md')).write_text('\n'.join(table)+'\n',encoding='utf-8')
    return {'page_count':page_count,'entries':count,'rows':confidence_rows,'extraction_notes':extraction_notes,
            'audit_confidence_entries':len(audit_entries),
            'audit_confidence_pages':len({key[0] for key in audit_entries})}

def rebuild_tables():
    """Rebuild inventory/collation from metadata without changing page records."""
    # Rewrite tables from the manually entered per-page records, preserving page order.
    with (ROOT/(PREFIX+'_inventory.csv')).open('w',newline='') as f, (ROOT/(PREFIX+'_collation.tsv')).open('w',newline='') as g:
        iw=csv.writer(f);cw=csv.writer(g,delimiter='\t')
        iw.writerow('scan sheet_kind hand element kind position first_words_or_objects transcribed'.split())
        cw.writerow('folder their_page our_scan line their_reading codex_reading final_reading scan_shows kind marked_in_H confidence'.split())
        for rr in ROWS:
            p=ROOT/'decisions'/(stem(rr)+'.json')
            if not p.exists():continue
            dd=json.loads(p.read_text())
            for n,e in enumerate(dd['inventory'],1):
                kind,pos,words,*hand=e
                iw.writerow([rr['cote']+'/'+rr['our_scan'],dd['sheet_kind'],hand[0] if hand else dd['hand'],f'{n:03}',kind,pos,words,'yes'])
            for x in dd['decisions']:
                if x.get('h_changed'):
                    assert rr['hua_has']=='text'
                    cw.writerow([rr['folder'],rr['their_page'],rr['our_scan'],x['place'],x.get('h',''),x.get('c',''),x['final'],x['shows'],x.get('kind','other'),x.get('marked_in_H','no'),x['confidence']])
def commit(d):
    r=row(d['cote'],d['scan']); target=ROOT/'pages'/Path(r['codex_file']).name
    if target.exists() and not d.get('amend'):raise ValueError('Page already committed; explicit amend required')
    t=(WIT/r['codex_file']).read_text() if not target.exists() else target.read_text()
    if 'text' in d:t=d['text']
    for old,new in d.get('replace',[]):
        if old not in t:raise ValueError('Replacement source not found: '+old)
        t=t.replace(old,new)
    target.write_text(t)
    d['h_status']=r['hua_has'];d['committed_utc']=now()
    (ROOT/'decisions'/(stem(r)+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    rebuild_tables()
    rebuild_changes()
    rebuild_doubts()
    with (ROOT/'progress.log').open('a') as f:f.write(f"cote {r['cote']} scan {int(r['our_scan']):03d} {'amended' if d.get('amend') else 'done'} {now()}\n")
    completed=[ROOT/'pages'/Path(rr['codex_file']).name for rr in ROWS]
    (ROOT/(PREFIX+'_transcription.tex')).write_text('\n\n'.join(p.read_text().rstrip() for p in completed if p.exists())+'\n')
    print('Committed',r['cote'],r['our_scan'],';',len(d['decisions']),'decisions;',len(d['inventory']),'inventory elements')
if __name__=='__main__':
    if sys.argv[1]=='show':
        r=row(sys.argv[2],sys.argv[3]);print(json.dumps(r,ensure_ascii=False));print('\nWITNESS C\n'+(WIT/r['codex_file']).read_text());print('\nWITNESS H\n'+hua(r))
    elif sys.argv[1]=='commit':commit(json.load(sys.stdin))
    elif sys.argv[1]=='status':
        print('Completed',len(list((ROOT/'pages').glob('*.tex'))),'of',len(ROWS));print((ROOT/'progress.log').read_text().splitlines()[-1])
