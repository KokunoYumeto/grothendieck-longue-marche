#!/usr/bin/env python3
"""One targeted structural pass over the assembled scan018 source/map."""
from pathlib import Path
import hashlib
import json
import re

BASE=Path('/workspace/scratch/94548b74fbe0')
DP=BASE/'out/checks/scan018_final_draft.tex'
MP=BASE/'out/checks/scan018_final_source_map.json'
AP=BASE/'out/checks/scan018_tex_assembly_audit.json'


def sha(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
draft=DP.read_text();raw_map=MP.read_text();mapping=json.loads(raw_map)
errors=[]
def require(condition,label):
    if not condition:errors.append(label)

require(mapping['draft_sha256_utf8']==sha(draft),'draft hash agrees with map')
require(''.join(b['emitted_literal_tex'] for b in mapping['blocks'])==draft,'complete block concatenation reproduces draft')
require(mapping['main_adjudicated'] is False,'main adjudication remains pending')

source_cache={}
def resolve(loc,label):
    path=loc['file']
    text=draft if path=='out/checks/scan018_final_draft.tex' else source_cache.setdefault(path,(BASE/path).read_text())
    a=loc['character_start'];b=loc['character_end_exclusive'];literal=text[a:b]
    require(literal==loc['literal_tex'],label+' exact span')
    require(sha(literal)==loc['literal_sha256_utf8'],label+' literal hash')
    require(sha(text)==loc['file_sha256_utf8'],label+' file hash')
    require(text.count('\n',0,a)+1==loc['start']['line'],label+' start line')
    require(text.count('\n',0,b)+1==loc['end_exclusive']['line'],label+' end line')

path_count=0
selected=[]
for block in mapping['blocks']:
    ident=block['id'];resolve(block['source'],ident+' source');resolve(block['draft'],ident+' draft')
    if block.get('complete_group_copied_without_changes'):
        selected.append(ident)
        require(block['source']['literal_tex']==block['emitted_literal_tex'],ident+' complete graphical source unchanged')
    for segment in block['source_to_draft_segments']:
        resolve(segment['source'],ident+' mapped source');resolve(segment['draft'],ident+' mapped draft')
        if segment['kind']=='unchanged':require(segment['source']['literal_tex']==segment['draft']['literal_tex'],ident+' unchanged segment')
    for component in block['literal_path_sources']:
        path_count+=1
        resolve(component['source'],ident+' path source');resolve(component['draft'],ident+' path draft')
        resolve(component['complete_support_source'],ident+' support source');resolve(component['complete_support_draft'],ident+' support draft')
        require(component['source']['literal_tex']==component['draft']['literal_tex'],ident+' literal path unchanged')
        require(component['complete_support_source']['literal_tex']==component['complete_support_draft']['literal_tex'],ident+' enclosing qualifier/state unchanged')
    for extra in block['additional_selected_sources']:
        resolve(extra,ident+' added-source support')
        if 'draft' in extra:resolve(extra['draft'],ident+' emitted added word')
require(selected==['B.G01','B.G02','C.G03','C.G04','B.G04','A.G05','C.G06','C.G07','A.G08'],'root-selected graphical block sequence')

# Strip only unescaped line comments for the TeX structural checks.
body='\n'.join(re.split(r'(?<!\\)%',line,maxsplit=1)[0] for line in draft.splitlines())
brace_stack=[]
for i,c in enumerate(body):
    if c in '{}':
        slash_count=0;j=i-1
        while j>=0 and body[j]=='\\':slash_count+=1;j-=1
        if slash_count%2:continue
        if c=='{':brace_stack.append(i)
        elif brace_stack:brace_stack.pop()
        else:errors.append('unmatched closing brace at '+str(i))
require(not brace_stack,'all source braces close')
env=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',body):
    kind,name=m.groups()
    if kind=='begin':env.append(name)
    elif env and env[-1]==name:env.pop()
    else:errors.append('environment nesting mismatch '+name)
require(not env,'all environments close')
math_stack=[]
for line in body.splitlines():
    require(not (not line.strip() and math_stack),'no physical paragraph blank inside math')
    for m in re.finditer(r'(?<!\\)\$|\\[\[\]()]',line):
        token=m.group()
        if token=='$':
            if math_stack and math_stack[-1]=='$':math_stack.pop()
            elif math_stack:errors.append('inline math delimiter inside another math delimiter')
            else:math_stack.append('$')
        elif token in [r'\[',r'\(']:math_stack.append(token)
        elif token in [r'\]',r'\)']:
            expected=r'\[' if token==r'\]' else r'\('
            if math_stack and math_stack[-1]==expected:math_stack.pop()
            else:errors.append('display math delimiter mismatch')
require(not math_stack,'all math delimiters close')
require(not re.search(r'\\(?:def|gdef|edef|xdef|newcommand|renewcommand|input|includegraphics|write18)\b',body),'no new macros, image substitution or external input')
require(len(re.findall(r'\\(?:draw|fill)\b',body))==path_count,'every emitted literal draw/fill has one selected component map')
require(path_count==17,'selected literal components total 17')
require(body.count(r'\unsure{\circ|0}')==1 and body.count(r'\Pi_J^\circ')==1,'Pi first-occurrence qualification retained once')
require(body.count(r'U_{\unsure{\alpha|x}}')==1 and body.count(r'U_\alpha')==1,'U first-occurrence qualification retained once')
require(body.count(r'\deleted{\Sigma}')==2,'each corrected-E predecessor emitted once')
require(r'\overline{E_i}' not in body,'ordinary overline source fully consumed by selected B graphic')
require(body.count('donnée')==1,'adjoining donnée occurs once')
require(body.count(r'\pi_0(X\setminus\Sigma_i)')==1,'C G06 includes the lower pi argument once')
require(body.count("l'\\unsure{é|e}l\\unsure{ê|é}ment")==1,'root singular-accent combination exact')
require(body.count(r'\deleted{\unsure{cela|OK|et}}')==1,'root cancelled-word combination exact')
require(draft.count('% archive sheet number: 17')==1,'archive comment retained once')

for collection,key,count in [('decision_coverage','decision_id',45),('inventory_coverage','inventory_id',31),('doubt_coverage','decision_id',23)]:
    rows=mapping[collection]
    require(len(rows)==count,collection+' expected count')
    require(len({r[key] for r in rows})==len(rows),collection+' distinct IDs')
    for row in rows:
        require(row['main_approved'] is False,row[key]+' approval pending')
        require(bool(row['final_source_attachments']),row[key]+' attachments present')
        for attachment in row['final_source_attachments']:resolve(attachment['draft'],row[key]+' attachment')

checks=['selected complete source blocks and literal path/support identity','exact source-to-draft replacements and added word source','braces and environment nesting','math delimiter balance and physical paragraph blanks','no new macros or image substitution','every emitted path component mapped once','first-occurrence qualifications','three critical word/formula joins','decision/inventory/doubt attachment offsets and hashes']
audit={'scan':18,'pass_scope':'One targeted assembler structural source pass only. No ink, mathematical, geometry, compiler or rendered validation.',
       'draft_file':str(DP.relative_to(BASE)),'draft_sha256_utf8':sha(draft),'input_map_sha256_utf8':sha(raw_map),
       'checks':checks,'selected_complete_graphical_groups':selected,'literal_draw_fill_components':path_count,
       'attachment_counts':mapping['attachment_counts'],'errors':errors,'passed':not errors,
       'compiler_or_renderer':False,'images_opened':0,'optional_geometry_calculations':0,'main_adjudicated':False}
if errors:
    AP.write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(audit,ensure_ascii=False));raise SystemExit(1)
mapping['structural_source_check']={'status':'passed one targeted assembler source pass','audit_file':str(AP.relative_to(BASE)),
    'checks':checks,'compiler_or_renderer':False,'mathematical_or_geometry_validation':False,
    'scope_limit':'Exact source and structural declarations only; manual graphical approximations remain unrendered and unmeasured.'}
MP.write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
audit['final_map_sha256_utf8']=sha(MP.read_text())
AP.write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'passed':True,'draft_sha256_utf8':audit['draft_sha256_utf8'],'map_sha256_utf8':audit['final_map_sha256_utf8'],
    'audit_sha256_utf8':sha(AP.read_text()),'attachment_counts':mapping['attachment_counts'],'literal_components':path_count},ensure_ascii=False))
