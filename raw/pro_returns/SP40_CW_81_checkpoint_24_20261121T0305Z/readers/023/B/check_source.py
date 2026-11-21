from pathlib import Path
import re,json
D=Path('/workspace/scratch/94548b74fbe0/out/readers/023/B')
s=(D/'reading.tex').read_text()
r=json.loads((D/'report.json').read_text())
m=json.loads((D/'source_map.json').read_text())
def uncomment(line):
 for i,c in enumerate(line):
  if c=='%':
   before=0;j=i-1
   while j>=0 and line[j]=='\\':before+=1;j-=1
   if before%2==0:return line[:i]
 return line
clean='\n'.join(uncomment(x) for x in s.splitlines())
# Lex control sequences, so a line-break command followed by du/sont is not misidentified.
controls=[];unescaped=[];i=0
while i<len(clean):
 c=clean[i]
 if c=='\\':
  j=i+1
  if j<len(clean) and clean[j].isalpha():
   while j<len(clean) and clean[j].isalpha():j+=1
   controls.append(clean[i+1:j]);i=j;continue
  if j<len(clean):controls.append(clean[j]);i=j+1;continue
 if c in '{}$':unescaped.append((c,i))
 i+=1
stack=[];brace_errors=[]
for c,pos in unescaped:
 if c=='{':stack.append(pos)
 elif c=='}':
  if stack:stack.pop()
  else:brace_errors.append({'unmatched_close':pos})
brace_errors += [{'unmatched_open':x} for x in stack]
envs=[];env_errors=[]
for mm in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
 op,en=mm.groups()
 if op=='begin':envs.append(en)
 elif not envs or envs.pop()!=en:env_errors.append({'at':mm.start(),'environment':en})
if envs:env_errors.append({'unclosed':envs})
math_display_errors=[];empty_display_lines=[];on=False
for n,line in enumerate(s.splitlines(),1):
 no=uncomment(line)
 if r'\[' in no:
  if on:math_display_errors.append(['nested',n])
  on=True
 if on and not line.strip():empty_display_lines.append(n)
 if r'\]' in no:
  if not on:math_display_errors.append(['extra_close',n])
  on=False
if on:math_display_errors.append(['unclosed'])
allowed={'scanpage','unsure','deleted','inserted','illegible','margin','figure','uline','begin','end','overline','widehat','beta','alpha','Sigma','cdot','in','setminus','cap','subset','varnothing','bigcup','bigvee','ne','Rightarrow','exists','Pi','circ','top','operatorname','geq','text','qquad','scriptstyle','reversemarginpar','normalmarginpar','rlap','phantom','shortstack','node','draw','fill','path','coordinate'}
unknown=sorted(set(x for x in controls if x.isalpha())-allowed)
anchor_failures=[]
for d in r['differences']:
 a=d.get('reading_tex_anchor')
 if a and a not in s:anchor_failures.append({'difference':d['id'],'anchor':a})
source_span_errors=[]
for g in m['groups']:
 sp=g['source_span'];body=s[sp['char_start_zero_based']:sp['char_end_exclusive']]
 if not body.startswith('% BEGIN '+g['id']+'\n') or not body.endswith('% END '+g['id']+'\n'):source_span_errors.append(g['id'])
 if g.get('complete_exact_source') is not None and body!=g['complete_exact_source']:source_span_errors.append(g['id']+' excerpt mismatch')
 for p in g.get('source_components',[]):
  exact=s[p['char_start_zero_based']:p['char_end_exclusive']]
  if not exact.startswith('% PATH '+p['owner']+':'):source_span_errors.append(p['owner'])
file_reference_errors=[]
for d in r['differences']:
 if d['readers_crop'] and not (D/d['readers_crop']).is_file():file_reference_errors.append(d['readers_crop'])
for c in r['crops']:
 if not (D/c['path']).is_file():file_reference_errors.append(c['path'])
row_errors=[]
for rr in r['C_doubt_source_rows']:
 ds=[d for d in r['differences'] if d.get('C_source_doubt_id')==rr['id']]
 if len(ds)!=1 or ds[0]['C_doubt_status'] not in ['resolved','retained']:row_errors.append(rr['id'])
valid_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
kind_errors=[d['id']+': '+d['kind'] for d in r['differences'] if d['kind'] not in valid_kinds]
views=r['view_audit']['views']
paths=[v['path'] for v in views]
view_errors=[]
if len(paths)!=len(set(paths)):view_errors.append('duplicate successful view path')
if len(paths)!=29:view_errors.append('successful-view count differs from three supplied images plus 26 crops')
if not all(c['target_viewed'] for c in r['crops']):view_errors.append('unviewed planned crop')
res={'method':'source-only structural and internal-consistency inspection; no TeX compiler or renderer','brace_errors':brace_errors,'environment_errors':env_errors,'math_display_errors':math_display_errors,'empty_physical_lines_inside_display_math':empty_display_lines,'dollar_sign_count':sum(c=='$' for c,_ in unescaped),'dollar_parity_even':sum(c=='$' for c,_ in unescaped)%2==0,'unknown_control_sequences':unknown,'reading_anchor_failures':anchor_failures,'source_span_errors':source_span_errors,'file_reference_errors':file_reference_errors,'C_source_row_errors':row_errors,'collation_kind_errors':kind_errors,'view_sequence_errors':view_errors,'commands_present':sorted(set(x for x in controls if x.isalpha())),'source_counts':{'unsure':controls.count('unsure'),'illegible':controls.count('illegible'),'deleted':controls.count('deleted'),'inserted':controls.count('inserted'),'graphic_groups':len(m['groups']),'C_source_rows':len(r['C_doubt_source_rows']),'differences':len(r['differences']),'pending_local_entries':len(r['doubts']),'inventory_items':len(r['inventory']),'successful_views':len(views),'unique_crops':len(r['crops'])},'limits':['Dollar parity is an administrative check, not TeX execution.','All graphic placement and path shapes are manual approximations; no rendered or metric validation is claimed.','Counts of macros include invisible state annotations and alternatives; they are not physical-locus counts.']}
res['passed']=not any([brace_errors,env_errors,math_display_errors,empty_display_lines,unknown,anchor_failures,source_span_errors,file_reference_errors,row_errors,kind_errors,view_errors]) and res['dollar_parity_even']
(D/'source_check.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(res,ensure_ascii=False,indent=2))
