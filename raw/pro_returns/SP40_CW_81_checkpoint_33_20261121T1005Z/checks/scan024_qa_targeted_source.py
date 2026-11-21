"""Clerical scan024 source audit. No image access, compilation or ink decisions."""
from pathlib import Path
import collections
import hashlib
import json
import re

BASE = Path('out/checks')
INPUTS = {
    'map': BASE/'scan024_source_record_initial_map_v01.json',
    'record': BASE/'scan024_source_record_initial_v01.json',
    'frames': BASE/'scan024_source_reader_frame_projection_initial_v01.json',
    'projection': BASE/'scan024_source_public_projection_initial_v01.json',
    'page': BASE/'scan024_final_draft.tex',
    'count': BASE/'scan024_root_count_authorization_v2.json',
    'journal': BASE/'scan024_root_decisions.json',
}
CACHE = {}
ERRORS = []
COUNTS = collections.Counter()

def textfile(path):
    p = Path(path)
    if p.suffix.lower() in {'.png','.jpg','.jpeg','.pdf','.tif','.tiff','.webp'}:
        raise ValueError('Non-text input prohibited: '+str(p))
    if not p.exists() and (Path('out')/p).exists():
        p = Path('out')/p
    key = str(p)
    if key not in CACHE:
        CACHE[key] = p.read_bytes().decode('utf-8')
    return CACHE[key]

def sha(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()

def getjson(path):
    return json.loads(textfile(path))

def check(ok, where, expected=None, actual=None):
    if not ok:
        ERRORS.append(dict(where=where, expected=expected, actual=actual))

def pointer(obj, ptr):
    for bit in ptr.split('/')[1:]:
        bit = bit.replace('~1','/').replace('~0','~')
        obj = obj[int(bit)] if isinstance(obj,list) else obj[bit]
    return obj

def walk(obj, where):
    if isinstance(obj,dict):
        path = obj.get('workspace_path') or obj.get('path') or obj.get('source_path')
        a = obj.get('char_start',obj.get('character_start'))
        b = obj.get('char_end',obj.get('character_end_exclusive'))
        if isinstance(path,str) and isinstance(a,int) and isinstance(b,int):
            COUNTS['exact_source_refs'] += 1
            t = textfile(path)
            v = t[a:b]
            check(0<=a<=b<=len(t),where+'/bounds')
            for field in ['sha256','sha256_utf8','source_sha256_utf8']:
                if field in obj: check(sha(t)==obj[field],where+'/'+field,obj[field],sha(t))
            for field in ['body_sha256','span_sha256_utf8']:
                if field in obj: check(sha(v)==obj[field],where+'/'+field,obj[field],sha(v))
            if 'literal' in obj: check(v==obj['literal'],where+'/literal')
            for field,value in [('character_start',a),('character_end_exclusive',b),
                                ('utf8_byte_start',len(t[:a].encode('utf-8'))),
                                ('utf8_byte_end',len(t[:b].encode('utf-8'))),
                                ('utf8_byte_end_exclusive',len(t[:b].encode('utf-8'))),
                                ('line_start',t.count('\n',0,a)+1),
                                ('line_end',t.count('\n',0,max(a,b-1))+1)]:
                if field in obj: check(obj[field]==value,where+'/'+field,obj[field],value)
            if 'json_pointer' in obj:
                check(json.loads(v)==pointer(json.loads(t),obj['json_pointer']),where+'/json_pointer')
        for k,v in obj.items(): walk(v,where+'/'+k.replace('~','~0').replace('/','~1'))
    elif isinstance(obj,list):
        for i,v in enumerate(obj): walk(v,where+'/'+str(i))

data = {k:(textfile(p) if k=='page' else getjson(p)) for k,p in INPUTS.items()}
M,R,F,P,AUTH,J,PAGE = [data[x] for x in ['map','record','frames','projection','count','journal','page']]
for label in ['map','record','frames']:
    before = COUNTS['exact_source_refs']
    walk(data[label],label)
    COUNTS[label+'_exact_refs'] = COUNTS['exact_source_refs']-before

# Exact edit replay and complete selected-source partition.
A = textfile('out/readers/024/A/reading.tex')
out = []; last = 0
for e in M['literal_replacements']:
    a,b = e['original_start'],e['original_end']
    check(last<=a<=b,'edit_order/'+e['edit_id'])
    out += [A[last:a],e['replacement']]
    check(PAGE[e['selected_start']:e['selected_end']]==e['replacement'],'edit_selected/'+e['edit_id'])
    for side,off in [('start',e['selected_start']),('end',e['selected_end'])]:
        q=e['splice_boundaries'][side]
        for k,v in [('char_offset',off),('preceding_character',PAGE[off-1:off]),
                    ('following_character',PAGE[off:off+1]),
                    ('preceding_last_byte_hex',PAGE[:off].encode('utf-8')[-1:].hex()),
                    ('following_first_byte_hex',PAGE[off:].encode('utf-8')[:1].hex())]:
            check(q[k]==v,'splice/'+e['edit_id']+'/'+side+'/'+k)
        check(PAGE[:off].endswith(q['literal_before']),'splice_before/'+e['edit_id']+'/'+side)
        check(PAGE[off:].startswith(q['literal_after']),'splice_after/'+e['edit_id']+'/'+side)
    last=b
out += [A[last:]]
check(''.join(out)==PAGE,'forward_edit_replay')
back=PAGE
for e in reversed(M['literal_replacements']):
    back=back[:e['selected_start']]+A[e['original_start']:e['original_end']]+back[e['selected_end']:]
check(back==A,'inverse_edit_replay')
last=0
for p in M['complete_selected_source_partition']:
    check(p['selected_start']==last,'partition/continuity')
    if p['kind']=='unchanged_A': check(p['source']['literal']==p['selected_source']['literal'],'partition/source_copy')
    last=p['selected_end']
check(last==len(PAGE),'partition/complete')

# Literal command boundaries; comments do not become commands or math delimiters.
masked=list(PAGE); i=0
while i<len(PAGE):
    if PAGE[i]=='\\': i+=2;continue
    if PAGE[i]=='%':
        z=PAGE.find('\n',i);z=len(PAGE) if z<0 else z
        masked[i:z]=[' ']*(z-i);i=z
    i+=1
MASK=''.join(masked)
found=[]
for m in re.finditer(r'\\(node|draw|fill|path)\b',MASK):
    i=m.end();depth=0
    while i<len(MASK):
        if MASK[i]=='\\': i+=2;continue
        if MASK[i]=='{':depth+=1
        elif MASK[i]=='}':depth-=1
        elif MASK[i]==';' and depth==0:break
        i+=1
    found.append((m.start(),i+1,m.group(1)))
reported=[(x['selected_source']['char_start'],x['selected_source']['char_end'],x['command']) for x in M['exact_command_ownership']]
check(found==reported,'literal_command_complete_coverage',len(found),len(reported))
groups={g['id']:g for g in M['selected_groups']}
for c in M['exact_command_ownership']:
    s=c['selected_source'];a,b=s['char_start'],s['char_end']
    containing=[g for g in groups.values() if g['source']['char_start']<=a and b<=g['source']['char_end']]
    containing.sort(key=lambda g:g['source']['char_end']-g['source']['char_start'])
    check(c['owner_group']==containing[0]['id'],'command_owner/'+c['id'])
    for f in c['exact_donor_matches']: check(f['literal']==s['literal'],'command_donor/'+c['id'])
    check(bool(c['exact_donor_matches']) != bool(c['root_authorized_composite']),'command_authority/'+c['id'])

# Source syntax only: paired environments and math delimiters, paragraph/comment boundaries.
depth=0;math=[];env=[];i=0;dollars=0;displays=0
while i<len(MASK):
    c=MASK[i]
    if c=='\\':
        if MASK[i:i+2] in ['\\[','\\]']:
            tok=MASK[i:i+2]
            if tok=='\\[': check(not math,'display_open');math.append('display');displays+=1
            else: check(math==['display'],'display_close');math.pop()
            i+=2;continue
        m=re.match(r'\\(begin|end)\{([^}]+)\}',MASK[i:])
        if m:
            typ,name=m.groups()
            if typ=='begin':env.append(name)
            else:check(bool(env) and env.pop()==name,'environment_close/'+name)
            i+=len(m.group());continue
        i+=2;continue
    if c=='{':depth+=1
    elif c=='}':depth-=1;check(depth>=0,'negative_brace_depth')
    elif c=='$':
        dollars+=1
        if math and math[-1]=='inline':math.pop()
        else:math.append('inline')
    if c=='\n' and i+1<len(MASK) and MASK[i+1]=='\n':check(not math,'paragraph_inside_math/'+str(i))
    i+=1
check(depth==0 and not env and not math,'source_delimiter_terminal_state')
for line in PAGE.splitlines():
    if re.search(r'% (?:BEGIN|END) ',line):check(line.startswith('%'),'marker_line_start/'+line)

# Physical count authority and local source/crop roles.
D={d['id']:d for d in R['decisions']}
for a in AUTH['rows']:
    d=D[a['id']]
    for key in ['source_locus_id','location','diff_C','diff_H','confidence','root_count_basis']:
        check(d[key]==a[key],'count_authority/'+a['id']+'/'+key)
    check(d['physical_count_parent']==a['count_parent'],'count_parent/'+a['id'])
check(len(D)==72 and len(AUTH['rows'])==65,'decision_counts')
for w in ['C','H']:check(sum(d['diff_'+w] for d in D.values())==AUTH['counts'][w],'count_sum/'+w)
check([d['id'] for d in D.values() if d['marked_in_H']]==['SRC024-L56'],'sole_H_marker')
S=[d for d in D.values() if 'S_id' in d]
check(len(S)==7 and all(not d['diff_C'] and not d['diff_H'] and not d['root_ink_choice_applied'] and d['S_status'] for d in S),'S_scope_zero')
ROOT={l:x for x in J['decisions'] for l in x['source_loci']}
for d in D.values():
    check(set(d['readers'])==set('ABC') and all(isinstance(v,str) and v for v in d['readers'].values()),'reader_fields/'+d['id'])
    check(d['main_approved'] is False,'pending_approval/'+d['id'])
    if d['source_locus_id'] in ROOT:
        j=ROOT[d['source_locus_id']]
        check(d['evidence']==j['evidence']+' Once-viewed crop: '+j['crop_path']+'.','root_evidence/'+d['id'])
        check(d['qualification']==j['decision'],'root_qualification/'+d['id'])
    for g in d['selected_group_ids']:check(d['id'] in groups[g]['decision_ids'],'decision_group/'+d['id']+'/'+g)
    for w in ['C','H']:
        for f in d.get('witness_source_references',{}).get(w,[]):
            if f['path']==f'packets/024/{w}.tex':
                check(f['literal'] in d[w],'witness_literal_in_public/'+d['id']+'/'+w)
            else:
                check(d['id']=='SRC024-L04' and w=='C' and f['path']=='packets/024/C_doubts.txt','extra_witness_scope/'+d['id']+'/'+w)
                check(f['literal'].rstrip('\n') in d[w],'extra_witness_literal/'+d['id']+'/'+w)
    for role,detail in d.get('reader_source_details',{}).items():
        for key in ['complete_own_literal_scope_refs','raw_own_difference_refs','raw_own_doubt_refs']:
            for rid in detail[key]:
                f=R['provenance']['source_reference_pool'][rid]['exact_source_ref']
                check(f'/024/{role}/' in f['source_path'],'own_reader_role/'+d['id']+'/'+role+'/'+rid)

for g in groups.values():
    for did in g['decision_ids']:
        check(g['id'] in D[did]['selected_group_ids'],'group_decision/'+g['id']+'/'+did)
        check(g['selected_readings'][did]==D[did]['final'],'group_final/'+g['id']+'/'+did)
for x in R['source_locus_coverage']:
    for did in x['decision_ids']:check(x['selected_readings'][did]==D[did]['final'],'coverage_final/'+did)
for q in R['doubts']:
    check(all(k in q for k in ['location','reading','alternatives','confidence','reason']),'doubt_fields/'+q['id'])
    check(q['reading']==D[q['decision_id']]['final'],'doubt_final/'+q['id'])
for inv in R['inventory']:
    check(all(k in inv for k in ['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']),'inventory_fields/'+inv['element'])
    check(inv['transcribed']=='yes' and bool(inv['source_attachments']),'inventory_selected/'+inv['element'])
    for g in inv['selected_group_ids']:check(inv['element'] in groups[g]['inventory_ids'],'inventory_group/'+inv['element']+'/'+g)
check([x['page_order'] for x in R['inventory']]==list(range(1,len(R['inventory'])+1)),'inventory_page_order')
check(isinstance(R['notes'],str),'notes_string')
check(all('form' in x and 'expansion' in x for x in R['abbreviations']),'abbreviation_fields')
check(R['check_events']==[],'no_math_check_events')

# Reversible reader and public projections, comparing source bytes, not ink.
for key,f in F['frames'].items():
    exact=f['exact_source']['literal']
    prefix='Complete own containing source frame (graphical blocks use explicitly editorial own-source descriptions; other words/macros retain source order):\n'
    body=f['public'][len(prefix):].split('\nExact own frame: ',1)[0]
    for q in reversed(f['group_projection']):body=body[:q['public_start']]+q['original_literal']+body[q['public_end']:]
    check(body==exact,'frame_inverse/'+key)
def restore(x):
    if isinstance(x,dict) and set(x)=={'concat'}:return ''.join(P['values'][k] for k in x['concat'])
    if isinstance(x,dict):return {k:restore(v) for k,v in x.items()}
    if isinstance(x,list):return [restore(v) for v in x]
    return x
public=restore(P['public_fields'])
for section,rows in public.items():
    if isinstance(rows,list):
        for i,row in enumerate(rows):
            for k,v in row.items():
                source_value=R[section][i][k]
                if section=='C_source_rows' and k=='source_parts':
                    source_value=[{pk:pv for pk,pv in p.items() if pk!='source_attachments'} for p in source_value]
                check(source_value==v,'public_replay/'+section+'/'+str(i)+'/'+k)
    else:check(rows==R[section],'public_replay/'+section)

REPORT=dict(scope='Source-only targeted mechanical replay of the preserved initial record; no ink, image, render, compile, proof or optional test.',
    inputs={str(p):sha(textfile(p)) for p in INPUTS.values()},
    exact_reference_counts=dict(COUNTS),
    selected_source_counts=dict(literal_replacements=len(M['literal_replacements']),partition_spans=len(M['complete_selected_source_partition']),graphical_groups=len(groups),commands=len(found),commands_with_exact_donor=sum(bool(c['exact_donor_matches']) for c in M['exact_command_ownership']),authorized_composites=[c['id'] for c in M['exact_command_ownership'] if c['root_authorized_composite']],inline_delimiters=dollars,display_pairs=displays,reader_frames=len(F['frames'])),
    counts=AUTH['counts'],errors=ERRORS,
    manual_findings_recorded_separately=True,
    prior_audit_preserved=dict(path='out/checks/scan024_qa_targeted_source_initial_v01.json',sha256=sha(textfile(BASE/'scan024_qa_targeted_source_initial_v01.json')),diagnostic_corrections=['Two flat-math-parser diagnostics omitted the nested inline math in TikZ node text inside the display; delimiter nesting is now tracked.','Two witness diagnostics did not allow L04 explicitly attributed C notation-row reference; exact source note is now checked.','Eighteen public projection diagnostics compared intentionally omitted source_attachments; exact projected fields are now compared.']))
target=BASE/'scan024_qa_targeted_source_initial_v02.json'
if target.exists():raise FileExistsError('Preserve prior QA audit: '+str(target))
target.write_text(json.dumps(REPORT,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(output=str(target),sha256=sha(textfile(target)),counts=dict(COUNTS),error_count=len(ERRORS),errors=ERRORS[:20]),ensure_ascii=False))
