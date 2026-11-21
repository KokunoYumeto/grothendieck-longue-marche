"""Root §§04–12 source proposals, cumulative with the exact §§01–03 splice."""
from pathlib import Path
from collections import Counter
import copy,difflib,hashlib,json,re,runpy,sys
sys.dont_write_bytecode=True
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
api=runpy.run_path(str(OUT/'scan026_source_authority_tools.py'))
save=api['save'];sha=api['sha']
captures,root,auth,helper=api['capture']('sections04_12_v01',[f'{n:02d}' for n in range(4,13)])
exact=helper['exact'];pack=lambda v:json.dumps(v,ensure_ascii=False,separators=(',',':'))
T={w:(BASE/f'out/readers/026/{w}/reading.tex').read_text() for w in 'ABC'}
M={w:json.loads((BASE/f'out/readers/026/{w}/source_map.json').read_bytes()) for w in 'ABC'}
G={w:{g['id']:g for g in M[w][{'A':'local_groups','B':'source_groups','C':'groups'}[w]]} for w in 'ABC'}
old_plan=json.loads((OUT/'scan026_source_sections01_03_plan_v01.json').read_bytes())
edits=copy.deepcopy(old_plan['edits']);state_maps=[];selected_states={}

def add(eid,a,b,replacement,section,reason,source=None):
 piece={'source':source} if source is not None else {'literal':replacement,'purpose':reason,'root_authority_refs':auth[section]}
 edits.append({'edit_id':eid,'base_char_start':a,'base_char_end':b,'before':T['A'][a:b],
  'root_section':section,'root_authority_refs':auth[section],'replacement_pieces':[piece],
  'purpose':reason,'main_approved':False})
def local_literal(gid,old,new,section,eid,reason):
 g=G['A'][gid];a,b=g['source_char_start'],g['source_char_end_exclusive'];hits=[m.start()+a for m in re.finditer(re.escape(old),T['A'][a:b])]
 assert len(hits)==1,(gid,old,hits);add(eid,hits[0],hits[0]+len(old),new,section,reason)
def candidate_comment(gid,candidates,section):
 g=G['A'][gid];a,b=g['source_char_start'],g['source_char_end_exclusive']
 start=T['A'].index('% complete candidates: ',a,b);end=T['A'].index('\n',start,b)
 old=json.loads(T['A'][start+len('% complete candidates: '):end])
 value='% complete candidates: '+json.dumps(candidates,ensure_ascii=False)
 add('E026-'+section+'-'+gid+'-candidates',start,end,value,section,'Exact root complete-state comment; original A comment and all original reader map states remain provenance.')
 selected_states[gid]={'root_complete_candidates':copy.deepcopy(candidates),'original_comment_candidates':old,
  'original_A_map_complete_candidates':copy.deepcopy(g['complete_candidates']),'root_authority_refs':auth[section]}

# §05 imports exactly the C local accent qualifier, without moving A companions.
word="s'intéresse";qualified=r"\unsure{s'intéresse|s'intèresse|s'interesse}"
assert T['A'].count(word)==1 and T['C'].count(qualified)==1
a=T['A'].index(word);c=T['C'].index(qualified)
add('E026-05-L005-accent',a,a+len(word),qualified,'05','Exact C word qualifier; A surrounding wording stays byte-identical.',exact('out/readers/026/C/reading.tex',T['C'],c,c+len(qualified)))

# §06 is an explicit three-element permutation of the complete A map objects.
original=G['A']['A026-G01']['complete_candidates'];permutation=[1,0,2]
reordered=[copy.deepcopy(original[i]) for i in permutation]
inverse=[None]*len(original)
for new_index,old_index in enumerate(permutation):inverse[old_index]=copy.deepcopy(reordered[new_index])
assert pack(inverse)==pack(original)
candidate_comment('A026-G01',reordered,'06')
state_maps.append({'group':'A026-G01','scope':'Complete A map objects, including original attachment fields.','permutation_new_index_to_old_index':permutation,
 'exact_original_objects':original,'exact_selected_objects':reordered,'forward_inverse_key_order_equal':True,'root_authority_refs':auth['06']})

# Explicit token mappings: no other candidate field or live upper alpha changes.
low_patterns=[(r'\Sigma_{\deleted{\alpha}}',r'\Sigma_{\deleted{\unsure{\alpha}}}'),(r'\Sigma_{\alpha}',r'\Sigma_{\unsure{\alpha}}')]
for gid,section,count in [('S04','07',4),('S05','07',24),('S07','10',2)]:
 original=G['C']['C026-'+gid]['candidate_states'];assert len(original)==count
 mapped=copy.deepcopy(original);changes=[]
 for i,(before,after) in enumerate(zip(original,mapped)):
  old=before['complete_reading'];matching=[(a,b) for a,b in low_patterns if old.startswith(a)];assert len(matching)==1
  lower_old,lower_new=matching[0];new=lower_new+old[len(lower_old):]
  upper_old=r'^{\deleted{\alpha}\alpha,';upper_new=r'^{\deleted{\unsure{\alpha}}\alpha,'
  upper_applied=gid=='S05' and upper_old in new
  if upper_applied:assert new.count(upper_old)==1;new=new.replace(upper_old,upper_new,1)
  after['complete_reading']=new
  assert list(before)==list(after)
  assert all(pack(before[k])==pack(after[k]) for k in before if k!='complete_reading')
  back=new
  if upper_applied:assert back.count(upper_new)==1;back=back.replace(upper_new,upper_old,1)
  assert back.startswith(lower_new);back=lower_old+back[len(lower_new):]
  assert back==old
  changes.append({'candidate_index':i,'old_complete_reading':old,'new_complete_reading':new,
   'lower_token_before':lower_old,'lower_token_after':lower_new,'cancelled_upper_token_changed':upper_applied,
   'all_other_fields_exact_and_in_original_order':True})
 assert sum(x['cancelled_upper_token_changed'] for x in changes)==(12 if gid=='S05' else 0)
 candidate_comment('A026-'+gid,mapped,section)
 state_maps.append({'group':'A026-'+gid,'source_candidate_group':'C026-'+gid,
  'source_candidate_pointer':f"/groups/{list(G['C']).index('C026-'+gid)}/candidate_states",
  'ordered_exact_changes':changes,'exact_original_candidate_states':copy.deepcopy(original),'exact_selected_candidate_states':mapped,
  'finite_forward_inverse_each_reading':True,'every_nonreading_field_and_key_order_preserved':True,'root_authority_refs':auth[section]})

# §11 supplies three ordered oval alternatives under the existing parent scope.
rings=['0',r'\circ','o'];parent_original=G['A']['A026-G05']['complete_candidates'];child_original=G['A']['A026-S08']['complete_candidates']
assert len(parent_original)==len(child_original)==1
parents=[];children=[]
for ring in rings:
 parent=copy.deepcopy(parent_original[0]);child=copy.deepcopy(child_original[0])
 for value in [parent,child]:
  assert value['reading'].count(r'\alpha,0}')==1
  value['reading']=value['reading'].replace(r'\alpha,0}',r'\alpha,'+ring+'}',1)
 parent_scope=parent['reading'];child['enclosing_complete_state']=parent_scope
 parents.append(parent);children.append(child)
assert parents[0]==parent_original[0]
assert {k:v for k,v in children[0].items() if k!='enclosing_complete_state'}==child_original[0]
for x in parents:assert all(x[k]==parent_original[0][k] for k in parent_original[0] if k!='reading')
for x in children:assert all(x[k]==child_original[0][k] for k in child_original[0] if k!='reading')
candidate_comment('A026-G05',parents,'11');candidate_comment('A026-S08',children,'11')
local_literal('A026-S08',r'{$\alpha,0$}',r'{$\alpha,\unsure{0|\circ|o}$}','11','E026-11-S08-visible-oval','Only the selected visible upper oval receives its exact root qualifier.')
local_literal('A026-S08',r'\phantom{$\Sigma_{\alpha}^{\alpha,0}$}',r'\phantom{$\Sigma_{\alpha}^{\alpha,\unsure{0|\circ|o}}$}','11','E026-11-S08-phantom-oval','Exact selected oval qualifier in the child annotation.')
local_literal('A026-G05',r'\phantom{\deleted{les $\Sigma_\alpha^{\alpha,0}$ connexes}}',r'\phantom{\deleted{les $\Sigma_\alpha^{\alpha,\unsure{0|\circ|o}}$ connexes}}','11','E026-11-G05-parent-oval-annotation','Propagate the same local oval qualifier through the parent deleted-clause annotation only.')
state_maps.append({'group':'A026-S08','parent_group':'A026-G05','ordered_ring_axis':rings,
 'original_child_candidate':child_original[0],'original_parent_candidate':parent_original[0],
 'exact_three_child_states':children,'exact_three_parent_states':parents,
 'enclosing_scope_binding':'The child enclosing_complete_state is the corresponding full parent reading at the same ring-axis index.',
 'primary_projection_restores_original_objects':True,'nonreading_fields_preserved':True,'root_authority_refs':auth['11']})

marker_path=OUT/'scan026_root_marker_pointer_correction.json';marker_bytes=marker_path.read_bytes();marker=json.loads(marker_bytes)
assert marker['section']=='09' and marker['before']==['U07'] and marker['after']==['U06']
assert root['09']['locus_decisions']['L009']['H_markers']==['U06']
plan={'scope':'Cumulative exact root-source proposals through §12. No section13 or later applied.',
 'base':copy.deepcopy(old_plan['base']),'edits':edits,'previous_source_plan':{'path':'out/checks/scan026_source_sections01_03_plan_v01.json','sha256':sha((OUT/'scan026_source_sections01_03_plan_v01.json').read_bytes())},
 'marker_pointer_correction_provenance':{'path':'out/checks/scan026_root_marker_pointer_correction.json','sha256':sha(marker_bytes),'raw_value':marker},
 'all_count_and_local_marker_booleans':'Unset; exact root H_markers lists and their source roles are preserved without assigning new flags.'}
plan_file=save('scan026_source_sections01_12_plan_v01.json',plan)
state_file=save('scan026_source_sections04_12_state_maps_v01.json',state_maps)
result=helper['stage'](plan,'scan026_source_sections01_12_proposal_v01')
P=Path(result['proposal_path']).read_text();mapping=json.loads(Path(result['map_path']).read_bytes())

# Bind exact preserved geometry commands. Node changes remain explicit source edits.
catalog=json.loads((OUT/'scan026_source_state_catalog_v01.json').read_bytes());geometry=[]
def shifted(p):return p+sum(len(e['replacement'])-(e['base_char_end']-e['base_char_start']) for e in mapping['literal_replacements'] if e['base_char_end']<=p)
for cmd in catalog['literal_source_commands']:
 if cmd['reader']!='A' or cmd['command']=='node':continue
 s=cmd['exact_source'];a,b=s['char_start'],s['char_end']
 assert not any(e['base_char_start']<b and a<e['base_char_end'] for e in mapping['literal_replacements'])
 pa,pb=shifted(a),shifted(b);assert P[pa:pb]==T['A'][a:b]
 geometry.append({'command_id':cmd['command_id'],'exact_original_source':s,'exact_proposal_source':exact('out/checks/scan026_source_sections01_12_proposal_v01.tex',P,pa,pb)})
geometry_file=save('scan026_source_sections01_12_geometry_bindings_v01.json',geometry)

# These source edits are the only new spans. A complete ndiff inverse is finite.
prior=(OUT/'scan026_source_sections01_03_proposal_v01.tex').read_text()
diff=''.join(difflib.unified_diff(prior.splitlines(keepends=True),P.splitlines(keepends=True),fromfile='out/checks/scan026_source_sections01_03_proposal_v01.tex',tofile='out/checks/scan026_source_sections01_12_proposal_v01.tex',n=3))
diff_file=save('scan026_source_sections04_12_delta_v01.diff',diff.encode(),True)
nd=list(difflib.ndiff(prior.splitlines(keepends=True),P.splitlines(keepends=True)))
assert ''.join(difflib.restore(nd,1))==prior and ''.join(difflib.restore(nd,2))==P

bindings=[];slots=json.loads((OUT/'scan026_source_record_scaffold_v01.json').read_bytes())['pending_decision_slots']
for section in sorted(root):
 for locus,value in root[section]['locus_decisions'].items():
  slot=next(s for s in slots if s['source_locus_id']==locus)
  bindings.append({'source_locus_id':locus,'root_section':section,'exact_root_locus_value':copy.deepcopy(value),'root_authority_refs':auth[section],
   'all_three_raw_reader_states':copy.deepcopy(slot['reader_source_bundles']),
   'original_C_source_row_ids':copy.deepcopy(slot['C_source_row_ids']),'original_C_source_part_ids':copy.deepcopy(slot['C_source_part_ids']),
   'local_C_status_from_root':{k:copy.deepcopy(v) for k,v in root[section].get('original_C_rows',{}).items() if k in slot['C_source_row_ids']},
   'C_status_scope':'The raw section value is preserved exactly; part/occurrence outcomes require their named local binding and are not flattened.',
   'diff_C':None,'diff_H':None,'physical_count_parent':None,'marked_in_H':None,'main_approved':False})
records=save('scan026_source_sections04_12_record_bindings_v01.json',{'scope':'Exact root-local authority and frozen own-reader bindings. Scalar count and H-flag assembly remains pending.','bindings':bindings,'selected_state_fields':selected_states})
audit={'scope':'Source-only literal proposal through root §12','authority_captures':captures,
 'all_A_non_node_geometry_commands_exact':len(geometry),'A_paths_fills_coordinates_rescaled_or_redrawn':0,
 'root_S04_C_states':4,'root_S05_C_states':24,'S05_cancelled_upper_token_mappings':12,'root_S07_C_states':2,
 'every_C_candidate_nonreading_field_and_order_preserved':True,'G01_permutation':[1,0,2],'S08_child_and_parent_ring_states':3,
 'C_source_parent_or_part_ids_changed':0,'C_original_R15_parts':1,'root_H_pointer_correction_retained':marker,
 'forward_and_inverse_restore_exact_A':mapping['forward_and_inverse_restore_exact_A_bytes'],'old_and_new_partial_source_sequence_replay':True,
 'literal_replacements_cumulative':len(mapping['literal_replacements']),'image_bytes_read':0,'root_or_final_files_written':0,
 'main_approved':False,'proposal':result,'artifacts':[plan_file,state_file,geometry_file,diff_file,records]}
save('scan026_source_sections04_12_audit_v01.json',audit)
print(json.dumps(audit,ensure_ascii=False,indent=2))
