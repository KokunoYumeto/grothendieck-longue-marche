from pathlib import Path
import json,re
B=Path('out/readers/020/B')
t=(B/'reading.tex').read_text()
r=json.loads((B/'report.json').read_text())
# Normalize only the report's required editorial category spelling, never manuscript text.
for d in r['differences']:
 d['kind']=d['kind'].replace(chr(92)*2+'ill',chr(92)+'ill')
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as '+chr(92)+'ill{}','drawing or diagram','other'}
assert all(d['kind'] in allowed for d in r['differences'])
# Strip comments, tokenize TeX control sequences without misreading \\\\ followed by si as \\si.
code='\n'.join(line.split('%',1)[0] for line in t.splitlines())
stack=[];controls=[];i=0
while i<len(code):
 c=code[i]
 if c=='\\':
  i+=1
  if i<len(code) and code[i].isalpha():
   j=i
   while i<len(code) and code[i].isalpha():i+=1
   controls.append(code[j:i]);continue
  i+=1;continue
 if c=='{':stack.append(i)
 elif c=='}':
  assert stack,('Unmatched closing brace',i)
  stack.pop()
 i+=1
assert not stack,('Unclosed braces',stack)
env=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',code):
 if m[1]=='begin':env.append(m[2])
 else:assert env and env.pop()==m[2],('Environment mismatch',m.group())
assert not env
assert code.count('\\[')==code.count('\\]')==2
assert code.count('$')%2==0
assert '\n\n' not in code[code.index('\\['):code.index('\\]')]
for match in re.finditer(r'\\\[(.*?)\\\]',code,re.S):assert not re.search(r'\n\s*\n',match[1])
allowed_controls={'scanpage','Pi','unsure','circ','deleted','Sigma','cap','quad','begin','end','path','node','rlap','phantom','draw','overline','ne','varnothing','operatorname','fill','uline','text','small','alpha','in','scriptsize','inserted','widehat','cup','setminus','reversemarginpar','margin','shortstack','normalmarginpar','forall','mathrel','Rightarrow','to','pi','beta','Longleftrightarrow'}
assert set(controls)<=allowed_controls,sorted(set(controls)-allowed_controls)
for x in r['differences']:
 if x['readers_crop']:assert (B/x['readers_crop']).is_file()
for x in r['crops']:assert (B/x['path']).is_file()
assert len(r['C_doubt_source_map'])==11
assert [x['actual_source_order'] for x in r['C_doubt_source_map']]==list(range(1,12))
assert sum(x['status']=='resolved' for x in r['C_doubt_source_map'])==1
assert r['check_events']==[]
assert len(r['image_audit']['local_views'])==14
assert r['image_audit']['failed_unseen_deliveries']==[]
anchors=[r'\Pi_I^{\unsure{\circ|0}}',r'\Pi_J^\circ',r'\unsure{clas.|deux.}',r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+',r'\unsure{\Sigma_j|\Sigma_i}',r'E_{\unsure{i|j}}','On sait donc','est en',r'\deleted{\unsure{tout|est}}','ce qui achève',r'\unsure{aussi|ainsi}',r'\unsure{dèm.|dém.|dem.}','par récurrence',r'\alpha\in\unsure{\deleted{I}K|K}',r'\phantom{\deleted{non vide}}',r'\deleted{on a}',r'|\deleted{\Rightarrow}\in|\deleted{\to}\in|\in','% archive sheet number: 19']
assert all(a in t for a in anchors)
# These counts concern source commands, not geometric identity or connected visible components.
audit={'method':'Source-only lexical and consistency checks; no TeX compiler, rendering, pixel comparison or geometric calculation.','balanced_braces':True,'balanced_environments':True,'balanced_display_delimiters':True,'even_inline_dollar_count':True,'no_empty_physical_line_inside_display_math':True,'all_macro_names_allowed':True,'crop_references_exist':True,'actual_C_source_rows_preserved':True,'required_reading_report_anchors_present':True,'image_history_matches_manifest':True,'math_check_events_empty':True,'visible_draw_commands':len(re.findall(r'\\draw\b',code)),'visible_fill_commands':len(re.findall(r'\\fill\b',code)),'graphic_component_map_count':sum(len(x['components']) for x in r['graphic_groups']),'source_macro_names':sorted(set(controls)),'full_source_excerpts':{},'limitations':'Path and node placements are manual approximations. Lexical checks establish no mathematical proof, rendered appearance, metric identity or exact image correspondence.'}
for gid in ['B_G01','B_G02','B_G03','B_G04','B_G05']:
 start=t.index('% '+gid)
 group_begin=t.index(r'\begin{tikzpicture}',start)
 depth=0
 group_end=None
 for em in re.finditer(r'\\(begin|end)\{tikzpicture\}',t[group_begin:]):
  depth+=1 if em[1]=='begin' else -1
  if depth==0:
   group_end=group_begin+em.end();break
 assert group_end is not None
 if gid=='B_G03':group_end+=3
 if gid=='B_G05':group_end=t.index(r'\pi_0',group_end)
 audit['full_source_excerpts'][gid]=t[start:group_end]
assert audit['visible_draw_commands']==13
assert audit['visible_fill_commands']==1
assert audit['graphic_component_map_count']==14
r['structural_validation']={'status':'passed source-only checks','compiled':False,'rendered':False,'mathematical_validation':False,'audit_file':'source_audit.json','checked':['braces','environment nesting','math delimiters','no blank line inside display math','permitted macro names','crop file references','C row identities/statuses','complete reading/report anchors','image-view audit consistency','literal graphic command/component counts']}
(B/'source_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
(B/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'validation':'passed source-only','counts':r['counts'],'visible_draw_commands':audit['visible_draw_commands'],'visible_fill_commands':audit['visible_fill_commands'],'kind_backslash_count':next(x['kind'] for x in r['differences'] if x['kind'].startswith('readable')).count(chr(92))},ensure_ascii=False))
