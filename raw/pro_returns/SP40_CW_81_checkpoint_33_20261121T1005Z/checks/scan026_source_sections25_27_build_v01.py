"""Final journal source proposals: root sections25 through27, with exact inverses."""
from pathlib import Path
import copy,difflib,json,runpy,sys
sys.dont_write_bytecode=True
O=Path('/workspace/scratch/94548b74fbe0/out/checks');B=O.parents[1]
api=runpy.run_path(str(O/'scan026_source_patch_support_v01.py'))
W=api['SourceWork']('sections25_27_v01',['25','26','27'],'scan026_source_sections01_24_plan_v01.json')
replace=api['replace_once'];inverse=api['inverse'];comment=api['comment'];insert=api['insert_at']
states={};mutations=[]
def donor(w,gid):
 values,pointer=W.candidates(w,gid)
 return {'reader':w,'path':f'out/readers/026/{w}/source_map.json','pointer':pointer,'exact_values':values}
def finish(gid,new,old,source,changes,section,purpose):
 assert inverse(new,changes)==old
 W.add_group(gid,new,[section],purpose,[source],changes)
 mutations.append({'group':gid,'original_exact_source':source,'changes':changes,'inverse_exact':True})

# §25: the point-first order changes no literal polygon geometry.
text,source=W.gtext('A','A026-G12');old=text;changes=[];d=donor('A','A026-G12')
values=[copy.deepcopy(d['exact_values'][i]) for i in [1,0]]
text=comment(text,values,changes,'Exact A candidate permutation [1,0]; original fields preserved.')
finish('A026-G12',text,old,source,changes,'25','A polygon and local qualification remain exact; complete point-first state order.')
states['L043']={'selected_complete_states':values,'source':d,'permutation_new_to_old':[1,0],'finite_inverse_permutation':[1,0]}

# §25: C complete fields retain their original primary wording as source fields.
text,source=W.gtext('A','A026-G13');old=text;changes=[];d=donor('C','C026-G10')
values=[copy.deepcopy(d['exact_values'][i]) for i in [1,0,2]]
text=comment(text,values,changes,'Root C whole-object order [1,0,2]; each source field stays exact.')
text=replace(text,r'\unsure{\deleted{\cap}\subset|\subset}',r'\unsure{\subset|\deleted{\cap}\subset|\in}',changes,'Root phantom order and retained membership alternative.')
text=insert(text,text.index('\n')+1,'% Root primary index: 0; C source role wording is retained literally within the copied objects.\n',changes,'Separate root ordering from unchanged C source primary wording.')
finish('A026-G13',text,old,source,changes,'25','Exact three A paths with root-ordered complete C states.')
states['L044']={'selected_complete_states':values,'source':d,'permutation_new_to_old':[1,0,2],'finite_inverse_permutation':[1,0,2],'root_primary_index':0,'all_C_candidate_fields_unchanged':True}

# §25 resolved cancellation fields come from the explicit root clarification.
clar_path='out/checks/scan026_root_source_clarifications_v01.json';clar_text=(B/clar_path).read_text();clar=json.loads(clar_text)
clarification=next(x for x in clar['clarifications'] if x['locus']=='L045');assert clarification['group']=='A026-G14'
clar_ref=W.exact(clar_path,clar_text,0,len(clar_text))
text,source=W.gtext('A','A026-G14');old=text;changes=[];d=donor('A','A026-G14');values=copy.deepcopy(d['exact_values'])
assert len(values)==1
for row in clarification['source_field_maps']:
 assert values[0][row['field']]==row['old'];values[0][row['field']]=row['new']
text=comment(text,values,changes,'Exact current role/attachment strings from root source clarification; original fields remain in donor provenance.')
text=replace(text,r'\mathord{\unsure{\tikz',r'\mathord{\tikz',changes,'Remove only the resolved outer qualifier.')
text=replace(text,'\n}}}\n% END A026-G14','\n}}\n% END A026-G14',changes,'Remove matching outer qualifier close only.')
text=replace(text,r'\deleted{\unsure{\ne\varnothing}}',r'\deleted{\ne\varnothing}',changes,'Resolved phantom pair; cancellation stays.')
finish('A026-G14',text,old,source,changes,'25','Literal cancellation paths stay exact, with resolved two-sign wording.')
W.edits[-1]['root_authority_refs'].append(clar_ref)
assert W.edits[-1]['replacement_pieces'][0]['root_authority_refs'].count(clar_ref)==1
states['L045']={'selected_complete_states':values,'source':d,'exact_field_maps':copy.deepcopy(clarification['source_field_maps']),'clarification_source':clar_ref}
restored=copy.deepcopy(values)
for row in reversed(clarification['source_field_maps']):assert restored[0][row['field']]==row['new'];restored[0][row['field']]=row['old']
assert restored==d['exact_values']

# §§26/27: copy complete objects; only wrap the existing literal A geometry.
for common,section,mixed in [('S31','26',False),('S32','26',False),('S34','26',True),('S39','27',True)]:
 gid='A026-'+common;cd=donor('C','C026-'+common);ad=donor('A',gid)
 values=copy.deepcopy(cd['exact_values'])
 if mixed:values=[copy.deepcopy(ad['exact_values'][0])]+values
 assert len(values)==(3 if mixed else 2)
 text,source=W.gtext('A',gid);old=text;changes=[]
 text=comment(text,values,changes,'Root exact whole-object '+('A[0],C[0],C[1]' if mixed else 'C[0],C[1]')+' selection.')
 text=replace(text,r'\mathord{\tikz',r'\mathord{\unsure{\tikz',changes,'Root local in-place qualification; geometry untouched.')
 text=replace(text,'\n}}\n% END '+gid,'\n}}}\n% END '+gid,changes,'Close only the new local qualifier.')
 finish(gid,text,old,source,changes,section,'Complete root state selection and local qualifier around unchanged A drawing.')
 states[common]={'selected_complete_states':values,'original_A':ad,'original_C':cd,
  'new_index_to_source':[{'reader':'A','index':0}]+[{'reader':'C','index':i} for i in range(2)] if mixed else [{'reader':'C','index':i} for i in range(2)],
  'all_copied_candidate_fields_and_order_unchanged':True}

# §26: exact C punctuation macro, outside all neighboring groups.
old_macro=r'\unsure{i.e.|i.e|ie}';new_macro=r'\unsure{i.e|i.e.|ie}'
assert W.T['C'].count(new_macro)==1;at=W.T['C'].index(new_macro)
cs=W.exact('out/readers/026/C/reading.tex',W.T['C'],at,at+len(new_macro))
W.literal(old_macro,new_macro,'26','E026-26-ie','Exact C three-way abbreviation order.',donors=[cs])
states['L047']={'selected_macro':new_macro,'exact_C_source':cs,'ordered_complete_readings':['i.e','i.e.','ie'],'root_hand':'his hand'}

# §27: full C definition-label group, root permutation [1,0].
text,source=W.gtext('C','C026-G12');old=text;changes=[];d=donor('C','C026-G12');values=[copy.deepcopy(d['exact_values'][i]) for i in [1,0]]
text=replace(text,r'\unsure{\text{déf}|\text{def}}',r'\unsure{\text{def}|\text{déf}}',changes,'Only the phantom candidate order changes; every C literal component stays.')
text=insert(text,text.index('\n')+1,'% Root complete candidates: '+json.dumps(values,ensure_ascii=False)+'\n',changes,'Exact complete C state order [1,0], including point-specific hand string.')
assert inverse(text,changes)==old
W.add_group('A026-G15',text,['27'],'Full C definition-label point and equals, root ordered complete states.',[source],changes)
mutations.append({'group':'C026-G12','original_exact_source':source,'changes':changes,'inverse_exact':True})
states['L048']={'selected_complete_states':values,'source':d,'permutation_new_to_old':[1,0],'finite_inverse_permutation':[1,0]}

# §27: complete cap/slant parent and original child, linked without altering source fields.
text,source=W.gtext('B','B026-CAPFINAL');old=text;changes=[];parent=donor('B','B026-CAPFINAL');child=donor('B','B026-M06')
cap_states=[]
for parent_index,child_index in [(1,0),(0,1)]:
 state=copy.deepcopy(parent['exact_values'][parent_index]);state['slant_complete_state']=copy.deepcopy(child['exact_values'][child_index])
 state['root_component_scope']={'arch_hand':'his hand','slant_allocation':'independent low-left slant' if child_index==0 else 'detached continuation'}
 if child_index==0:state['root_component_scope']['independent_slant']={'hand':'undetermined hand','role':'undetermined','attachment':'undetermined','surface_origin':'undetermined'}
 state['hand_scope_rule']='The original B parent main field applies to the arch; the exact child object and root component scope retain the slant attribution separately.'
 cap_states.append(state)
text=replace(text,'% complete candidates: intersection arch with detached continuation || intersection arch with independent low-left slant',
 '% complete candidates: intersection arch with independent low-left slant || intersection arch with detached continuation',changes,'Root complete parent order only; original child order remains.')
text=insert(text,text.index('\n')+1,'% Root complete component states: '+json.dumps(cap_states,ensure_ascii=False)+'\n',changes,'Complete ordered parent/child state bindings; all original fields preserved.')
assert inverse(text,changes)==old
amark,amark_source=W.gtext('A','A026-M04')
W.literal(amark+r'\cap',text,'27','E026-27-capfinal','Complete B parent with M06 once replaces A separate mark and cap.',donors=[source,amark_source],changes=changes)
mutations.append({'group':'B026-CAPFINAL','original_exact_source':source,'changes':changes,'inverse_exact':True})
states['L049']={'selected_complete_states':cap_states,'original_parent':parent,'original_child':child,'explicit_parent_child_indices':[[1,0],[0,1]],'root_slant_scope_from_section':'27'}
for value,(pi,ci) in zip(cap_states,[(1,0),(0,1)]):
 assert {k:v for k,v in value.items() if k not in ['slant_complete_state','root_component_scope','hand_scope_rule']}==parent['exact_values'][pi]
 assert value['slant_complete_state']==child['exact_values'][ci]

# §27: complete final relation drawing; existing point-state fields remain exact.
text,source=W.gtext('B','B026-NEFINAL');old=text;changes=[];parent=donor('B','B026-NEFINAL')
rows=W.M['B']['special_component_candidates'];pi=next(i for i,x in enumerate(rows) if x['id']=='B026-NEFINAL-point');points=copy.deepcopy(rows[pi]['states'])
ne_states=[]
for i,point in enumerate(points):
 state=copy.deepcopy(parent['exact_values'][i]);state['point_complete_state']=copy.deepcopy(point)
 state['root_component_scope']={'sign_strokes_hand':'his hand','point_hand':'his hand' if i==0 else 'undetermined hand'}
 if i==1:state['root_component_scope'].update({'point_role':'undetermined','point_attachment':'undetermined','point_surface_origin':'undetermined'})
 state['hand_scope_rule']='The original B main field applies to the three sign strokes; the exact point state and root component scope retain the detached point attribution separately.'
 ne_states.append(state)
text=insert(text,text.index('\n')+1,'% Root complete component states: '+json.dumps(ne_states,ensure_ascii=False)+'\n',changes,'Complete endpoint/independent-point states with root candidate-local scopes.')
assert inverse(text,changes)==old
last_group=W.G['A']['A026-S39'];start=last_group['source_char_end_exclusive'];assert W.T['A'][start:].count(r'\ne')==1
W.literal(r'\ne',text,'27','E026-27-nefinal','Complete B terminal relation and its one point; following varnothing remains.',within=(start,len(W.T['A'])),donors=[source],changes=changes)
mutations.append({'group':'B026-NEFINAL','original_exact_source':source,'changes':changes,'inverse_exact':True})
states['L050']={'selected_complete_states':ne_states,'original_parent':parent,'exact_original_point_states':points,
 'point_source_pointer':f'/special_component_candidates/{pi}/states','explicit_parent_child_indices':[[0,0],[1,1]],'root_component_scope_from_section':'27'}
for i,value in enumerate(ne_states):
 assert {k:v for k,v in value.items() if k not in ['point_complete_state','root_component_scope','hand_scope_rule']}==parent['exact_values'][i]
 assert value['point_complete_state']==points[i]

result,plan_artifact,P=W.stage('27');prior=(O/'scan026_source_sections01_24_proposal_v01.tex').read_text()
delta=''.join(difflib.unified_diff(prior.splitlines(keepends=True),P.splitlines(keepends=True),fromfile='out/checks/scan026_source_sections01_24_proposal_v01.tex',tofile='out/checks/scan026_source_sections01_27_proposal_v01.tex',n=3))
artifacts=[plan_artifact,W.save('scan026_source_sections25_27_selected_states_v01.json',states),
 W.save('scan026_source_sections25_27_donor_mutations_v01.json',mutations),W.save('scan026_source_sections25_27_delta_v01.diff',delta.encode(),True)]
mapping=json.loads(Path(result['map_path']).read_bytes())
audit={'scope':'All27 root decision sections are now represented in the cumulative source proposal; global flags remain pending.',
 'authority_captures':W.captures,'clarification_source':clar_ref,'source':result,'artifacts':artifacts,
 'exact_inverse_to_frozen_A':mapping['forward_and_inverse_restore_exact_A_bytes'],'cumulative_literal_replacements':len(mapping['literal_replacements']),
 'selected_state_counts':{k:len(v['selected_complete_states']) for k,v in states.items() if 'selected_complete_states' in v},
 'all_donor_changes_have_exact_inverses':True,'main_approved':False,'root_flags_chosen':0,'images_read':0,
 'B026_M06_occurrences':P.count('% BEGIN B026-M06'),'B026_NEFINAL_occurrences':P.count('% BEGIN B026-NEFINAL'),
 'removed_A_M04_occurrences':P.count('% BEGIN A026-M04'),'C026_G12_occurrences':P.count('% BEGIN C026-G12'),
 'archive_comment_occurrences':P.count('% archive sheet number: 25'),**api['validate'](P)}
assert audit['B026_M06_occurrences']==audit['B026_NEFINAL_occurrences']==audit['C026_G12_occurrences']==audit['archive_comment_occurrences']==1
assert audit['removed_A_M04_occurrences']==0
W.save('scan026_source_sections25_27_audit_v01.json',audit)
print(json.dumps(audit,ensure_ascii=False,indent=2))
