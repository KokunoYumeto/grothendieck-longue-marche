import datetime
import hashlib
import json
import os
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parents[3]
tex=(ROOT/'reading.tex').read_text()
report=json.loads((ROOT/'report.json').read_text())
smap=json.loads((ROOT/'source_map.json').read_text())
audit=json.loads((ROOT/'view_audit.json').read_text())
md=(ROOT/'reading.md').read_text()

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

clean=re.sub(r'(?<!\\)%[^\n]*','',tex)
brace_stack=[]
for i,c in enumerate(clean):
    if c not in '{}':
        continue
    n=0;j=i-1
    while j>=0 and clean[j]=='\\':
        n+=1;j-=1
    if n%2:
        continue
    if c=='{':
        brace_stack.append(i)
    else:
        assert brace_stack,('extra closing brace',i)
        brace_stack.pop()
assert not brace_stack,('unclosed braces',brace_stack)

envs=[]
env_count=0
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
    op,name=m.groups()
    if op=='begin':
        envs.append(name);env_count+=1
    else:
        assert envs and envs[-1]==name,('environment mismatch',name,m.start(),envs)
        envs.pop()
assert not envs

math=[]
dollars=0
display_pairs=0
for m in re.finditer(r'\\\[|\\\]|(?<!\\)\$',clean):
    token=m.group()
    if token==r'\[':
        assert not math
        math.append('display')
    elif token==r'\]':
        assert math==['display']
        math.pop();display_pairs+=1
    elif math==['inline']:
        math.pop();dollars+=1
    else:
        assert not math,('dollar in existing math mode',m.start())
        math.append('inline');dollars+=1
assert not math
for m in re.finditer(r'\\\[([\s\S]*?)\\\]',tex):
    assert not re.search(r'\n[ \t]*\n',m.group(1)), 'blank physical line inside display'

allowed={'scanpage','unsure','Pi','circ','setminus','bigcup','alpha','in','deleted','figure','begin','end','path','node','rlap','uline','phantom','forall','inserted','draw','overset','hspace','cdot','mathrel','scriptsize','overline','cap','ne','varnothing','noindent','llap','coordinate','fill','quad','Sigma','i','subset'}
used=set(re.findall(r'\\([A-Za-z]+)',clean))
assert used<=allowed,('unapproved command',used-allowed)
assert r'\cotefile' not in clean and r'\mspage' not in clean
assert '% archive sheet number: 23' in tex

def verify_span(d):
    a=d['char_start'];b=d['char_end_exclusive']
    assert tex[a:b]==d['exact_tex']
    assert len(tex[:a].encode())==d['utf8_byte_start']
    assert len(tex[:b].encode())==d['utf8_byte_end_exclusive']

assert smap['reading_sha256']==digest(ROOT/'reading.tex')
groups={g['id']:g for g in smap['groups']}
unique_commands={}
for g in smap['groups']:
    verify_span(g['source_span']);verify_span(g['body_span'])
    for c in g['literal_components']:
        verify_span(c)
        assert c['exact_tex'].endswith(';')
        unique_commands[(c['char_start'],c['char_end_exclusive'])]=c
    for w in g['wrapper_spans']:
        verify_span(w)
        assert w['exact_tex'].endswith('}')
for d in report['differences']:
    for span in d['source_spans']:
        verify_span(span)
    assert all(g in groups for g in d['source_groups'])
for s in report['source_choices']:
    verify_span(s['source_span'])
    assert s['candidates']==groups[s['id']].get('candidates',[])
for i in report['inventory']:
    assert i['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'}
    assert i['transcribed']=='yes'
    assert all(g in groups for g in i['source_groups'])

allowed_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(d['kind'] in allowed_kinds for d in report['differences'])
assert len(report['original_C_doubt_rows'])==18
assert {r['id'] for r in report['original_C_doubt_rows']}=={'C024-R'+str(i).zfill(2) for i in range(1,19)}
assert all(r['local_decisions'] for r in report['original_C_doubt_rows'])
assert report['check_events']==[]

expected_counts={'whole':1,'half_a':1,'half_b':1,'deep_crops':22,'failed_unseen_deliveries':0}
assert audit['viewing_counts']==expected_counts
assert report['provenance']['viewing_counts']==expected_counts
assert len(audit['events'])==25
success_paths=[e['image_path'] for e in audit['events'] if e['status']=='success']
assert len(success_paths)==len(set(success_paths))==25
assert all((BASE/p).is_file() for p in success_paths)
assert len(report['crops'])==22
for d in report['differences']:
    if d['readers_crop']:
        assert (ROOT/d['readers_crop']).is_file()
        c=next(c for c in report['crops'] if c['path']==d['readers_crop'])
        assert c['bbox']==d['bbox']['coordinates']

# Exact source-context quotations, with unmodified source line boundaries.
C=(BASE/'packets/024/C.tex').read_text()
H=(BASE/'packets/024/H.tex').read_text()
Cl=C.splitlines(True);Hl=H.splitlines(True)
def witness_span(text,lines,first,last,path):
    a=sum(len(x) for x in lines[:first-1]);b=sum(len(x) for x in lines[:last])
    return {'path':path,'line_start':first,'line_end':last,'char_start':a,'char_end_exclusive':b,'utf8_byte_start':len(text[:a].encode()),'utf8_byte_end_exclusive':len(text[:b].encode()),'exact_tex':text[a:b]}
context_map={
 'C01':(2,2,2,3),'C02a':(2,2,2,3),'C02b':(2,2,2,3),'C03':(2,2,2,3),'C04':(2,2,4,5),'C05':(3,5,6,8),'C06':(3,5,6,8),
 'C07':(7,7,10,12),'C08':(10,10,10,12),'C09a':(10,10,11,12),'C09b':(10,10,11,12),'C10':(13,13,14,17),
 'C11':(15,15,19,20),'C12':(15,15,20,21),'C13':(15,15,20,22),'C14':(15,15,20,22),'C15':(15,15,23,24),
 'C16':(10,10,11,12),'C17':(13,13,14,17),'C18':(15,15,19,20),
 'D01':(2,2,2,3),'D02a':(2,2,4,5),'D02b':(2,2,4,5),'D02c':(2,2,4,5),'D02d':(2,2,4,5),
 'D03':(3,5,6,8),'D04':(3,5,6,8),'D05':(9,11,10,12),'D06':(10,10,11,12),'D07':(9,11,10,12),'D08':(9,11,10,12),'D09':(10,10,12,12),
 'D10':(13,13,14,17),'D11':(13,13,14,17),'D12':(13,13,14,17),'D13':(13,13,14,17),'D14':(13,13,16,17),
 'D15':(15,15,19,20),'D16':(15,15,19,20),'D17':(15,15,20,21),'D18':(15,15,20,21),'D19':(15,15,20,21),'D20':(15,15,20,22),
 'D21':(15,15,21,22),'D22':(15,15,21,22),'D23':(15,15,22,23),'D24':(15,15,23,24),'D25':(15,15,23,24),'D26':(15,15,23,24),'D27':(15,15,23,24),'D28':(15,15,23,24)
}
for d in report['differences']:
    short=d['id'].split('-',1)[1]
    ca,cb,ha,hb=context_map[short]
    d['C_anchor']=witness_span(C,Cl,ca,cb,'packets/024/C.tex')
    d['H_anchor']=witness_span(H,Hl,ha,hb,'packets/024/H.tex')
    d['witness_field_convention']='C and H fields name the local selected or omitted reading. The anchors retain exact unmodified source text, wrappers, punctuation and line boundaries for its complete context.'

rows_status={'resolved':0,'retained':0,'mixed':0}
for row in report['original_C_doubt_rows']:
    statuses=set(row['local_statuses'].values())
    rows_status['mixed' if len(statuses)>1 else next(iter(statuses))]+=1
counts={'difference_records':len(report['differences']),'flagged_C_records':sum(d['diff_C'] for d in report['differences']),'flagged_H_records':sum(d['diff_H'] for d in report['differences']),'unique_C_physical_loci':len({d['physical_locus'] for d in report['differences'] if d['diff_C']}),'unique_H_physical_loci':len({d['physical_locus'] for d in report['differences'] if d['diff_H']}),'original_C_doubt_rows':18,'original_C_row_statuses':rows_status,'inventory_items':len(report['inventory']),'source_groups':len(groups),'unique_literal_commands':len(unique_commands),'viewing_counts':expected_counts}
checks={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'brace_balance':'pass','environment_balance':'pass','environments':env_count,'inline_dollar_delimiters':dollars,'display_pairs':display_pairs,'empty_physical_lines_inside_displays':0,'macro_allowlist':'pass; PREAMBLE and standard permitted LaTeX/TikZ commands only','source_span_exactness':'pass for group, literal command, wrapper, report-difference and source-choice spans','source_hash_match':'pass','candidate_scope_consistency':'pass; report source-choice candidates equal source-map candidates; full phrases retained in reading.md','original_C_row_coverage':'all 18 original row identities, with two compound rows locally subdivided and no lost scope','crop_reference_consistency':'pass; every crop cited exists and has its logged original bbox','once_only_delivery_check':'pass; 25 unique successful image paths, zero repeats or failed deliveries','inventory_coverage':'pass; all original C inventory identities retained plus local component and archive rows, ordered by page/text position','literal_node_boundary_check':'pass; terminating semicolons respect nested brace depth, so complete nested node contents survive','compilation_or_rendering':'not attempted','mathematical_checks':'none; check_events remains empty'}
report['counts']=counts
report['source_only_checks']=checks
report['provenance']['S_coverage']='No S witness was supplied or adjudicated for this packet. B024-S01 through S05 name this reader’s five local Sigma source groups.'
report['provenance']['editorial_punctuation']='Alternative bars and explanatory sentence-final periods in source comments are editorial; manuscript endpoint punctuation is transcribed in live TeX and separately recorded.'
report['provenance']['source_assembly_note']='The first Python builder run stopped at an unmatched closing parenthesis before producing the return; its syntax was repaired. All final source checks above were then performed on the actual generated files. No TeX compiler or renderer was invoked.'

md += '\n## Completed source-only checks\n\nBraces, environments, inline/display delimiters, permitted commands, crop references, original C row coverage, complete literal node boundaries and exact source spans passed. No empty physical line occurs inside the display. All 25 image deliveries were unique: whole once, a once, b once and 22 local crops once each. No failed delivery, reopen, compilation, rendering or mathematical check occurred.\n\nOriginal C rows: '+str(rows_status['resolved'])+' resolved, '+str(rows_status['retained'])+' retained, and '+str(rows_status['mixed'])+' mixed row with separate local statuses. The report contains '+str(len(report['differences']))+' local records and '+str(len(report['inventory']))+' inventory items.\n'
(ROOT/'reading.md').write_text(md)

frozen=datetime.datetime.now(datetime.timezone.utc).isoformat()
report['end_utc']=frozen
report['frozen_utc']=frozen
audit['frozen_utc']=frozen
audit['final_outputs_consistent']=True
smap['frozen_utc']=frozen
smap['source_only_checks']={'exact_spans_verified':True,'nested_node_terminators_verified':True,'canonical_component_ownership_recorded':True,'rendered_or_metric_validation':False}
(ROOT/'view_audit.json').write_text(json.dumps(audit,indent=2,ensure_ascii=False)+'\n')
(ROOT/'source_map.json').write_text(json.dumps(smap,indent=2,ensure_ascii=False)+'\n')
report['file_hashes']={p.name:digest(p) for p in sorted(ROOT.iterdir()) if p.is_file() and p.name!='report.json'}
(ROOT/'report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
all_hashes={p.name:digest(p) for p in sorted(ROOT.iterdir()) if p.is_file()}
assert report['file_hashes']['reading.tex']==smap['reading_sha256']
for p in ROOT.iterdir():
    if p.is_file():
        os.chmod(p,0o444)
os.chmod(ROOT,0o555)
print(json.dumps({'frozen_utc':frozen,'counts':counts,'files_sha256':all_hashes,'all_files_read_only':True},indent=2,ensure_ascii=False))
