from pathlib import Path
import json,re,hashlib
O=Path('/workspace/scratch/94548b74fbe0/out/readers/023/C')
r=json.loads((O/'report.json').read_text())
s=(O/'reading.tex').read_text()
# Inventory refinements preserve source item identities and interleave local trace components.
r['inventory']=[x for x in r['inventory'] if x['element'] not in {'023C.28a','023C.37a','023C.43a','023C.43b'}]
for x in r['inventory']:
    if x['element']=='023C.33': x['first_words_or_objects']='Cela ... précise / precise / provient / précise le / precise le ... du / des / sens'
extra={
'023C.28':[{'sheet_kind':'text','hand':'undetermined hand','element':'023C.28a','kind':'drawing','position':'S07, separated point above alpha, about (1387,1529)','first_words_or_objects':'One point; alpha-terminal versus independent-point role unresolved','transcribed':'yes','source_group':'C023-G10','path_owner':'C023-G10-P05'}],
'023C.37':[{'sheet_kind':'text','hand':'undetermined hand','element':'023C.37a','kind':'drawing','position':'S09, point above the i-like hook, about (1404,1834)','first_words_or_objects':'One point; attachment to i-like hook or retrace unresolved','transcribed':'yes','source_group':'C023-G14','path_owner':'C023-G14-P04'}],
'023C.43':[{'sheet_kind':'text','hand':'undetermined hand','element':'023C.43a','kind':'drawing','position':'S10, above-right of plus, about (1445,1914)','first_words_or_objects':'Upper small point; plus-retrace/independent-mark role unresolved','transcribed':'yes','source_group':'C023-G18','path_owner':'C023-G18-P06'},{'sheet_kind':'text','hand':'undetermined hand','element':'023C.43b','kind':'drawing','position':'S10, above-left of alpha, about (1424,1948)','first_words_or_objects':'Lower small point; alpha-retrace/independent-mark role unresolved','transcribed':'yes','source_group':'C023-G18','path_owner':'C023-G18-P03'}]
}
a=[]
for x in r['inventory']:
    a.append(x); a.extend(extra.get(x['element'],[]))
# Whole corollary region first, then its components in their supported page positions.
segment=['023C.39','023C.43','023C.43a','023C.43b','023C.40','023C.42','023C.41','023C.44']
start=next(i for i,x in enumerate(a) if x['element']=='023C.39')
parts={x['element']:x for x in a if x['element'] in segment}
a=[x for x in a if x['element'] not in segment]
a[start:start]=[parts[k] for k in segment]
r['inventory']=a
for d in r['differences']:
    if d['id'] in {'D21','D31','D34'}: d['trace_hand']='undetermined hand for the separately qualified point(s); main text is his hand'
# Exact source map: byte spans and path ownership, no rendering or geometric-extrema computation.
lines=s.splitlines(keepends=True)
starts=[];pos=0
for line in lines:
    starts.append(pos);pos+=len(line.encode('utf-8'))
stack=[];groups={};line_owner={}
for i,line in enumerate(lines,1):
    m=re.match(r'% BEGIN GROUP (C023-G\d+)\s*$',line)
    if m:
        g=m.group(1);groups[g]={'group_id':g,'parent_group':stack[-1] if stack else None,'source_file':'reading.tex','start_line':i,'start_byte_utf8':starts[i-1],'path_owners':[],'annotation_lines':[],'label_lines':[],'declaration_lines':[]};stack.append(g)
    if stack: line_owner[i]=stack[-1]
    if stack and line.startswith('%') and not re.match(r'% (BEGIN|END|path|label)',line): groups[stack[-1]]['declaration_lines'].append({'line':i,'text':line.rstrip()})
    m=re.match(r'% END GROUP (C023-G\d+)\s*$',line)
    if m:
        g=m.group(1);assert stack.pop()==g
        groups[g]['end_line']=i;groups[g]['end_byte_utf8']=starts[i-1]+len(line.encode('utf-8'))
assert not stack
active=None
for i,line in enumerate(lines,1):
    m=re.match(r'% path (C023-G\d+-P\d+):\s*(.*)',line)
    if m:
        owner=line_owner[i];active={'path_id':m.group(1),'group_owner':owner,'description':m.group(2).strip(),'comment_line':i,'commands':[]};groups[owner]['path_owners'].append(active)
    elif re.match(r'% (?:BEGIN GROUP|END GROUP|label)',line): active=None
    if active and re.match(r'\\(?:draw|fill)(?:\[|\s)',line): active['commands'].append({'line':i,'exact_source':line.rstrip()})
    owner=line_owner.get(i)
    if owner and '\\phantom{' in line: groups[owner]['annotation_lines'].append({'line':i,'exact_source':line.rstrip()})
    if owner and line.startswith('\\node') and '\\phantom' not in line: groups[owner]['label_lines'].append({'line':i,'exact_source':line.rstrip()})
for g in groups.values():
    raw=s.encode('utf-8')[g['start_byte_utf8']:g['end_byte_utf8']]
    g['span_sha256']=hashlib.sha256(raw).hexdigest()
    g['span_convention']='start byte inclusive, end byte exclusive; line numbers one-based and inclusive'
    g['manual_geometry']=True
source_map={'scan':23,'reader':'C','file':'reading.tex','file_sha256':hashlib.sha256(s.encode()).hexdigest(),'coordinate_convention':'Declared original full-scan top-left pixel origins; local y points down through negative TikZ y units. Fixed rectangles, explicit baselines and base-west zero-separation anchors keep nested source origins stable. No metric or rendering validation is claimed.','groups':list(groups.values()),'ownership_note':'Each physical path belongs to the innermost listed group. C023-G15 is the complete corollary parent; G16–G19 are its contained complete component groups. Main lexical context outside a mark-only group is explicitly identified in its declaration. Annotation text inside phantom boxes is invisible; actual literal marks and visible labels occur once.'}
(O/'source_map.json').write_text(json.dumps(source_map,ensure_ascii=False,indent=2)+'\n')
# Required structural checks only.
clean='\n'.join(re.sub(r'(?<!\\)%.*$','',x) for x in s.splitlines())
brace=0;minbrace=0
for c in re.sub(r'\\[{}]','',clean):
    if c=='{':brace+=1
    elif c=='}':brace-=1;minbrace=min(minbrace,brace)
envs=[];env_errors=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
    op,name=m.groups()
    if op=='begin':envs.append(name)
    elif not envs or envs.pop()!=name:env_errors.append((op,name))
math_dollars=len(re.findall(r'(?<!\\)\$',clean))
displays=(clean.count('\\['),clean.count('\\]'))
blank_in_math=[];dollar_open=False;display_open=False
for n,line in enumerate(s.splitlines(),1):
    l=re.sub(r'(?<!\\)%.*$','',line)
    if not line.strip() and (dollar_open or display_open):blank_in_math.append(n)
    for m in re.finditer(r'\\\[|\\\]|(?<!\\)\$',l):
        if m.group()=='\\[':display_open=True
        elif m.group()=='\\]':display_open=False
        else:dollar_open=not dollar_open
commands=sorted(set(re.findall(r'(?<!\\)\\([A-Za-z]+)',clean)))
allowed={'circ','qquad','alpha','begin','beta','bigcup','bigvee','cap','deleted','draw','end','exists','figure','fill','geq','illegible','in','inserted','linewidth','makebox','margin','mathop','mathrel','mid','ne','node','normalmarginpar','operatorname','overline','path','phantom','Pi','quad','reversemarginpar','Rightarrow','rlap','rotatebox','scanpage','scriptstyle','setminus','shortstack','Sigma','subset','text','textbar','uline','unsure','varnothing','widehat'}
unknown=sorted(set(commands)-allowed)
kind_allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
invalid_kinds=[(x['id'],x['kind']) for x in r['differences'] if x['kind'] not in kind_allowed]
inv_allowed={'text','display','diagram','drawing','margin note','insertion','deletion'}
invalid_inv=[x['element'] for x in r['inventory'] if x['kind'] not in inv_allowed or x['transcribed']!='yes']
missing_crops=[d['readers_crop'] for d in r['differences'] if d['readers_crop'] and not (O/d['readers_crop']).is_file()]
missing_groups=[g for d in r['differences'] for g in d['source_groups'] if g not in groups]
paths=[p for g in groups.values() for p in g['path_owners']]
missing_path_commands=[p['path_id'] for p in paths if not p['commands']]
views=json.loads((O/'view_audit.json').read_text())
view_paths=[v['path'] for v in views]
struct={
'brace_balance':brace,'minimum_brace_balance':minbrace,'unclosed_environments':envs,'environment_errors':env_errors,'dollar_count':math_dollars,'dollars_even':math_dollars%2==0,'display_open_close_counts':displays,'blank_physical_lines_inside_math':blank_in_math,'unknown_control_words':unknown,'invalid_difference_kinds':invalid_kinds,'invalid_inventory_items':invalid_inv,'missing_crop_files':missing_crops,'missing_source_groups':missing_groups,'literal_group_count':len(groups),'owned_path_ids':len(paths),'literal_draw_fill_command_count':sum(len(p['commands']) for p in paths),'path_ids_without_commands':missing_path_commands,'successful_view_count':len(views),'duplicate_view_paths':len(view_paths)-len(set(view_paths)),'source_macro_counts_including_invisible_annotations':{m:len(re.findall(r'\\'+m+r'\b',clean)) for m in ('unsure','illegible','deleted','inserted')},'scope':'Source-only syntax, ownership and report-reference checks. No TeX engine, renderer, OCR or mathematical check was run.'}
struct['passed']=not any([brace,minbrace,envs,env_errors,math_dollars%2,displays[0]!=displays[1],blank_in_math,unknown,invalid_kinds,invalid_inv,missing_crops,missing_groups,missing_path_commands,len(view_paths)-len(set(view_paths))])
(O/'source_checks.json').write_text(json.dumps(struct,ensure_ascii=False,indent=2)+'\n')
r['provenance']['source_map_file']='source_map.json'
r['provenance']['source_checks_file']='source_checks.json'
r['provenance']['source_only_validation']=struct
r['provenance']['view_events']=views
r['provenance']['C_original_doubt_row_count']=len(r['C_doubt_source_rows'])
r['provenance']['C_doubt_status_counts']={k:sum(k in x['status'] for x in r['C_doubt_source_rows']) for k in ('resolved','retained')}
r['provenance']['raw_difference_flag_counts']={'C':sum(d['diff_C'] for d in r['differences']),'H':sum(d['diff_H'] for d in r['differences']),'note':'Raw local flags; physical-parent grouping is explicit in individual rows and must be preserved when tallying clusters.'}
(O/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(struct,ensure_ascii=False,indent=2))
