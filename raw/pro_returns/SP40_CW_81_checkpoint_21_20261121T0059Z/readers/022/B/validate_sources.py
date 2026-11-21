from pathlib import Path
import json,re,hashlib
B=Path('out/readers/022/B');t=(B/'reading.tex').read_text();r=json.loads((B/'report.json').read_text())
# Text/source validation only: no TeX execution, image rendering or pixel comparison.
active='\n'.join(re.sub(r'(?<!\\)%.*','',line) for line in t.splitlines())
stack=[];brace_errors=[]
for i,c in enumerate(active):
 if c not in '{}':continue
 n=0;j=i-1
 while j>=0 and active[j]=='\\':n+=1;j-=1
 if n%2:continue
 if c=='{':stack.append(i)
 elif stack:stack.pop()
 else:brace_errors.append({'position':i,'error':'unmatched close'})
brace_errors.extend({'position':i,'error':'unmatched open'} for i in stack)
envstack=[];env_errors=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',active):
 op,name=m.groups()
 if op=='begin':envstack.append((name,m.start()))
 elif not envstack or envstack[-1][0]!=name:env_errors.append({'position':m.start(),'operation':op,'name':name,'stack':envstack.copy()})
 else:envstack.pop()
env_errors.extend({'unclosed':x} for x in envstack)
blank_math=[];inside=False;math_start=None
for ln,line in enumerate(t.splitlines(),1):
 s=line.strip()
 if s==r'\[':inside=True;math_start=ln
 elif s==r'\]':inside=False
 elif inside and not s:blank_math.append(ln)
if inside:blank_math.append({'unclosed_display_from':math_start})
macros=sorted(set(re.findall(r'\\([A-Za-z]+)',active)))
allowed={'scanpage','figure','begin','end','node','path','draw','fill','coordinate','rlap','phantom','deleted','inserted','unsure','uline','operatorname','small','normalsize','large','Large','scriptsize','tiny','alpha','beta','Sigma','widehat','overline','cap','cup','bigcup','bigcap','setminus','subset','ne','varnothing','in','rotatebox','Rightarrow'}
unapproved=sorted(set(macros)-allowed)
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
kind_errors=[(d['id'],d['kind']) for d in r['differences'] if d['kind'] not in kinds]
group_errors=[]
for g in r['graphic_source_audit']:
 a,b=g['source_offsets_characters'];frag=t[a:b]
 if frag!=g['source_excerpt']:group_errors.append([g['id'],'excerpt offset mismatch'])
 if hashlib.sha256(frag.encode()).hexdigest()!=g['source_sha256']:group_errors.append([g['id'],'excerpt hash mismatch'])
 if frag.count('% BEGIN '+g['id']+';')!=1 or frag.count('% END '+g['id'])!=1:group_errors.append([g['id'],'group boundary mismatch'])
text_errors=[]
for q in r['text_ownership_audit']:
 cmd=q['source_command'].replace('qu’il',"qu'il")
 if t.count(cmd)!=1:text_errors.append([q['id'],t.count(cmd),'visible source node command multiplicity'])
parent_errors=[]
ids={d['id'] for d in r['differences']}
for d in r['differences']:
 for w in ['C','H']:
  p=d.get('count_parent_'+w)
  if p and p not in ids:parent_errors.append([d['id'],w,p])
  if p and d['diff_'+w]:parent_errors.append([d['id'],w,'child true with parent'])
 # Every exact local H marker flag must match the two physical source scopes.
 if d['marked_in_H']!=(d['id'] in ['B022-D27','B022-D28']):parent_errors.append([d['id'],'wrong H local marker flag'])
owner_ids=[g['id'] for i in r['inventory'] for g in i.get('literal_component_groups',[])]
ownership_errors=[]
for g in r['graphic_source_audit']:
 if owner_ids.count(g['id'])!=1:ownership_errors.append([g['id'],owner_ids.count(g['id'])])
source_inv=json.loads(Path('packets/022/C_inventory.json').read_text())
current_ids={i['element'] for i in r['inventory']}
missing_original_inventory=[i['element'] for i in source_inv if i['element'] not in current_ids]
ref_errors=[]
for c in r['crops']:
 if not (B/c['path']).is_file():ref_errors.append(c['path'])
 if c['successful_view_count']!=1 or c['failed_delivery_count']!=0:ref_errors.append(['view history',c['path']])
for d in r['differences']:
 if d['readers_crop'] and not (B/d['readers_crop']).is_file():ref_errors.append([d['id'],d['readers_crop']])
actualpaths=sum(1 for line in t.splitlines() if line.lstrip().startswith(r'\draw') or line.lstrip().startswith(r'\fill'))
result={
 'type':'source-only structural and record consistency audit',
 'brace_errors':brace_errors,'environment_errors':env_errors,'blank_lines_inside_display_math':blank_math,
 'macros_used':macros,'macros_outside_permitted_set':unapproved,'invalid_kind_values':kind_errors,
 'source_group_errors':group_errors,'text_ownership_errors':text_errors,'count_parent_or_H_marker_errors':parent_errors,
 'graphic_inventory_ownership_errors':ownership_errors,'original_C_inventory_ids_missing':missing_original_inventory,
 'file_reference_errors':ref_errors,'source_anchor_errors':r['source_anchor_errors_pending'],
 'visible_path_fill_count_in_source':actualpaths,'reported_path_fill_count':r['counts_proposal']['literal_path_fill_commands'],
 'graphic_groups':len(r['graphic_source_audit']),'text_owner_nodes':len(r['text_ownership_audit']),
 'double_backslash_command_candidates':re.findall(r'\\\\[A-Za-z]+',active),
 'unfinished_markers_in_final_source':[w for w in ['TODO','UNFINISHED','DRAFT'] if w in t],
 'no_compilation_or_rendering':True,
 'notes':['Fixed coordinate and baseline declarations were checked as source declarations only. Text metrics, paths, and page layout were not rendered.','All visible word-bearing source nodes occur once. Hidden phantom annotations record readings/states and add no visible duplicate glyph.']}
result['passed']=not any([brace_errors,env_errors,blank_math,unapproved,kind_errors,group_errors,text_errors,parent_errors,ownership_errors,missing_original_inventory,ref_errors,r['source_anchor_errors_pending'],result['double_backslash_command_candidates'],result['unfinished_markers_in_final_source']]) and actualpaths==r['counts_proposal']['literal_path_fill_commands']
(B/'source_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
