"""Root-authorized source splices for sections20 through24, preserving all donors."""
from pathlib import Path
import copy,difflib,json,runpy,sys
sys.dont_write_bytecode=True
O=Path('/workspace/scratch/94548b74fbe0/out/checks')
api=runpy.run_path(str(O/'scan026_source_patch_support_v01.py'))
W=api['SourceWork']('sections20_24_v01',[str(n) for n in range(20,25)],'scan026_source_sections01_19_plan_v01.json')
replace=api['replace_once'];inverse=api['inverse'];comment=api['comment'];insert=api['insert_at']
states={};mutations=[]
def source_states(w,gid):
 values,pointer=W.candidates(w,gid)
 return {'reader':w,'source_path':f'out/readers/026/{w}/source_map.json','json_pointer':pointer,'exact_values':values}

# §20: complete q-bearing word, one exact donor span.
q,qs=W.gtext('B','B026-GQDESC')
W.literal("qu'elles",q,'20','E026-20-quelles','Exact B complete q loop, descender, and continuation.',donors=[qs])
states['L033']={'selected':source_states('B','B026-GQDESC'),'root_decision':copy.deepcopy(W.root['20']['locus_decisions']['L033'])}

# §21: parent origin and two points are linked by the exact recorded translation.
adjective,adj_source=W.gtext('B','B026-GADJ');adj_original=adjective;adj_changes=[]
points=source_states('A','A026-M03');point_scope={k:W.root['21']['locus_decisions']['L035'][k] for k in ['hand','role','attachment','surface_origin']}
old_points='\\fill (415,65) ellipse (1.3 and 1.3);\n\\fill (410,72) ellipse (1.3 and 1.3);'
new_points=(
 '% BEGIN R026-L035\n'
 '% Root complete point interpretations: '+json.dumps(points['exact_values'],ensure_ascii=False)+'\n'
 '% Root current component scope: '+json.dumps(point_scope,ensure_ascii=False)+'\n'
 '% Exact translation: parent (407,62) plus local (8,3)/(3,10) = original (415,65)/(410,72).\n'
 '\\node[anchor=north west,inner sep=0pt,outer sep=0pt] at (407,62) {\\unsure{\\begin{tikzpicture}[x=0.085mm,y=-0.085mm]\n'
 '\\path[use as bounding box] (0,0) rectangle (12,13);\n'
 '\\fill (8,3) ellipse (1.3 and 1.3);\n'
 '\\fill (3,10) ellipse (1.3 and 1.3);\n'
 '\\end{tikzpicture}}};\n'
 '% END R026-L035')
adjective=replace(adjective,old_points,new_points,adj_changes,'Root §21 exact common-unit translation and local point qualifier.')
assert inverse(adjective,adj_changes)==adj_original
a_points,a_source=W.gtext('A','A026-M03')
old_frame=r'\uline{non \unsure{panachées|penchées|parallèles}}\raisebox{-2mm}{$'+a_points+'$}'
W.literal(old_frame,adjective,'21','E026-21-adjective-points','Whole B adjective with one translated, qualified point pair; original A separate pair frame removed.',donors=[adj_source,a_source],changes=adj_changes)
word_states=source_states('B','B026-GADJ')
assert [x['reading'] for x in word_states['exact_values']]==['non panachées','non penchées','non parallèles','non panachees','non penchees','non paralleles']
point_map=[{'original':[415,65],'local':[8,3]},{'original':[410,72],'local':[3,10]}]
for row in point_map:
 assert [row['local'][0]+407,row['local'][1]+62]==row['original']
 assert [row['original'][0]-407,row['original'][1]-62]==row['local']
states['L034']={'selected':word_states,'root_decision':copy.deepcopy(W.root['21']['locus_decisions']['L034'])}
states['L035']={'exact_interpretations':points,'root_current_component_scope':point_scope,'source_point_map':point_map,
 'parent_anchor':[407,62],'anchor':'north west','inner_sep':'0pt','outer_sep':'0pt','units':'x=0.085mm,y=-0.085mm',
 'radii_each':[1.3,1.3],'subpicture_declared_rectangle':[0,0,12,13],
 'rectangle_scope':'Display bounds enclosing the two fills; no ink-boundary measurement claimed.',
 'forward_inverse_coordinate_translation_exact':True}
mutations.append({'group':'B026-GADJ','source':adj_source,'changes':adj_changes,'inverse_exact':True})

# §22: exact C local three-run source, inside the existing A baseline node.
insertion,ins_source=W.gtext('A','A026-G10');ins_original=insertion;ins_changes=[]
on,on_source=W.gtext('C','C026-G09a');on_states=source_states('C','C026-G09a');a_parent=source_states('A','A026-G10')
parents=[]
for candidate in on_states['exact_values']:
 parents.append({'fixed_prefix':r'si \inserted{elles sont \uline{distinctes}, et si} ',
  'reduced_on_complete_state':copy.deepcopy(candidate),'fixed_suffix':' peut trouver',
  'fixed_text_and_guide_hand':'his hand','base_A_parent_candidate_provenance':copy.deepcopy(a_parent['exact_values'][0]),
  'scope_rule':'The reduced-on component retains its exact candidate-specific fields. The fixed prefix/suffix and guide retain the root section22 attribution.'})
insertion=comment(insertion,parents,ins_changes,'Complete root parent states use the exact C component object at the baseline location.')
insertion=replace(insertion,'{on peut trouver};','{'+on+' peut trouver};',ins_changes,'Only on is replaced by the complete literal C three-run group.')
assert inverse(insertion,ins_changes)==ins_original
W.add_group('A026-G10',insertion,['22'],'A insertion placement and guide with complete C reduced-on group.',[ins_source,on_source],ins_changes)
states['L036']={'exact_selected_complete_states':parents,'original_A_parent':a_parent,
 'fixed_source_geometry':'All A026-G10 draw/path commands stay exact; only its baseline node content and parent comment change.'}
states['L037']={'selected':on_states,'root_decision':copy.deepcopy(W.root['22']['locus_decisions']['L037'])}
mutations.append({'group':'A026-G10','source':ins_source,'changes':ins_changes,'inverse_exact':True})

# §23: exact root-selected split of one original body path.
s22,s22_source=W.gtext('A','A026-S22');s22_old=s22;s22_changes=[]
old_body=r'\draw[line width=.35pt,line cap=round,line join=round] (1418,1738) -- (1444,1744) -- (1419,1767) -- (1453,1767);'
new_body=(r'\draw[line width=.35pt,line cap=round,line join=round] (1418,1738) -- (1441,1743);'+'\n'+r'\draw[line width=.35pt,line cap=round,line join=round] (1445,1749) -- (1419,1767) -- (1453,1767);')
assert W.root['23']['locus_decisions']['S22']['body_paths']==[[[1418,1738],[1441,1743]],[[1445,1749],[1419,1767],[1453,1767]]]
s22=replace(s22,old_body,new_body,s22_changes,'Exact root section23 approximate native-coordinate body-path refinement.')
assert inverse(s22,s22_changes)==s22_old
W.add_group('A026-S22',s22,['23'],'Keep complete A scope and two states; split only the recorded body path.',[s22_source],s22_changes)
states['S22']={'selected':source_states('A','A026-S22'),'geometry_change':copy.deepcopy(s22_changes),'root_decision':copy.deepcopy(W.root['23']['locus_decisions']['S22'])}
mutations.append({'group':'A026-S22','source':s22_source,'changes':s22_changes,'inverse_exact':True})

# §24: two complete A states, then a complete B state with its own point component.
relation,rel_source=W.gtext('A','A026-G11');relation_old=relation;rel_changes=[]
avalues,aptr=W.candidates('A','A026-G11');bvalues,bptr=W.candidates('B','B026-CAP1')
point_rows=W.M['B']['special_component_candidates'];pi=next(i for i,x in enumerate(point_rows) if x['id']=='B026-CAP1-point')
point=copy.deepcopy(point_rows[pi]['states'][1])
third=copy.deepcopy(bvalues[1]);third['point_complete_state']=point
third['hand_scope_rule']='The original B main field applies to the sign; the exact B point state supplies the separate point hand, role and attachment.'
current=[copy.deepcopy(avalues[1]),copy.deepcopy(avalues[0]),third]
relation=comment(relation,current,rel_changes,'Root exact order A[1], A[0], B cap-independent-point state with complete child scope.')
relation=replace(relation,r'\unsure{\cap|\wedge}',r'\unsure{\wedge|\cap}',rel_changes,'Root phantom candidate order only.')
assert inverse(relation,rel_changes)==relation_old
assert {k:v for k,v in third.items() if k not in ['point_complete_state','hand_scope_rule']}==bvalues[1]
assert current[0]==avalues[1] and current[1]==avalues[0] and third['point_complete_state']==point_rows[pi]['states'][1]
W.add_group('A026-G11',relation,['24'],'Exact A drawing with three root candidate scopes and wedge-first phantom.',[rel_source],rel_changes)
states['L038']={'exact_selected_complete_states':current,'ordered_source_map':[
 {'reader':'A','path':'out/readers/026/A/source_map.json','pointer':aptr+'/1'},
 {'reader':'A','path':'out/readers/026/A/source_map.json','pointer':aptr+'/0'},
 {'reader':'B','path':'out/readers/026/B/source_map.json','parent_pointer':bptr+'/1','point_pointer':f'/special_component_candidates/{pi}/states/1','added_fields':['point_complete_state','hand_scope_rule']}],
 'original_A_values':avalues,'original_B_values':bvalues,'finite_forward_inverse_exact':True}
mutations.append({'group':'A026-G11','source':rel_source,'changes':rel_changes,'inverse_exact':True})

result,plan_artifact,P=W.stage('24');prior=(O/'scan026_source_sections01_19_proposal_v01.tex').read_text()
delta=''.join(difflib.unified_diff(prior.splitlines(keepends=True),P.splitlines(keepends=True),fromfile='out/checks/scan026_source_sections01_19_proposal_v01.tex',tofile='out/checks/scan026_source_sections01_24_proposal_v01.tex',n=3))
artifacts=[plan_artifact,W.save('scan026_source_sections20_24_selected_states_v01.json',states),
 W.save('scan026_source_sections20_24_donor_mutations_v01.json',mutations),
 W.save('scan026_source_sections20_24_delta_v01.diff',delta.encode(),True)]
mapping=json.loads(Path(result['map_path']).read_bytes())
audit={'scope':'Root source-only proposals through24; all decisions come from root journal.',
 'authority_captures':W.captures,'source':result,'artifacts':artifacts,
 'exact_inverse_to_frozen_A':mapping['forward_and_inverse_restore_exact_A_bytes'],
 'cumulative_literal_replacements':len(mapping['literal_replacements']),
 'point_translation_forward_inverse':True,'point_group_R026_L035_count':P.count('% BEGIN R026-L035'),
 'old_separate_A_M03_count':P.count('% BEGIN A026-M03'),
 'q_group_count':P.count('% BEGIN B026-GQDESC'),'C_reduced_on_group_count':P.count('% BEGIN C026-G09a'),
 'L038_exact_state_count':len(current),'root_flags_chosen':0,'images_read':0,'main_approved':False,
 **api['validate'](P)}
assert audit['point_group_R026_L035_count']==1 and audit['old_separate_A_M03_count']==0
assert audit['q_group_count']==audit['C_reduced_on_group_count']==1
W.save('scan026_source_sections20_24_audit_v01.json',audit)
print(json.dumps(audit,ensure_ascii=False,indent=2))
