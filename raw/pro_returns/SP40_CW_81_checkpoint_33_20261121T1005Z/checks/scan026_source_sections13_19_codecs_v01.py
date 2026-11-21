"""Finite root-authorized diagram and pair tuple maps, without ink decisions."""
from pathlib import Path
from itertools import product
import copy,json,runpy,sys
sys.dont_write_bytecode=True
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
api=runpy.run_path(str(OUT/'scan026_source_authority_tools.py'));save=api['save']
captures,root,auth,helper=api['capture']('sections13_19_v01',[f'{n:02d}' for n in range(13,20)])
maps={w:json.loads((BASE/f'out/readers/026/{w}/source_map.json').read_bytes()) for w in 'ABC'}
groups={w:{g['id']:g for g in maps[w][{'A':'local_groups','B':'source_groups','C':'groups'}[w]]} for w in 'ABC'}
pack=lambda v:json.dumps(v,ensure_ascii=False,separators=(',',':'))

# All twelve original A objects retain their actual order and raw field scope.
base_diagrams=copy.deepcopy(groups['A']['A026-D01']['complete_candidates']);assert len(base_diagrams)==12
minus=copy.deepcopy(groups['C']['C026-S15']['candidate_states']);plus=copy.deepcopy(groups['C']['C026-S16']['candidate_states'])
assert len(minus)==len(plus)==2
e_readings=[x.strip() for x in root['13']['locus_decisions']['L017']['reading'].split('|')];assert len(e_readings)==4
e_states=[]
for i,reading in enumerate(e_readings):
 independent=i>=2
 e_states.append({'complete_reading':reading,'body_and_lower_loop_hand':'his hand',
  'upper_run_hand':'undetermined hand' if independent else 'his hand',
  'upper_run_role':'independent upper run' if independent else 'detached top arm allocated to E',
  'upper_run_attachment':'detached short upper run above E',
  'lower_loop_assignment':'alpha index' if i%2==0 else 'E-foot flourish',
  'scope_source':'Root §13 L017; these are root component fields. Original A/B/C fields remain separately frozen.'})
point={k:root['13']['locus_decisions']['L019'][k] for k in ['reading','hand','role','attachment','surface_origin']}
assert all(point[k]=='undetermined' for k in ['role','attachment','surface_origin'])
base_lookup=[[[9,11],[8,10]],[[1,3],[0,2]],[[5,7],[4,6]]]
letters=['B','E',r'\Sigma'];relations=[r'\supseteq',r'\supset'];eloops=[r'E_\alpha','E with lower-right flourish']
diagram_tuples=[];diagram_full=[]
def diagram_expand(row):
 li,ri,ei,eh,mh,ph=row['tuple'];ai=base_lookup[li][ri][ei]
 assert row['original_A_candidate_index']==ai and row['E_state_index']==eh*2+ei
 base=base_diagrams[ai]
 return {'tuple':row['tuple'],'complete_base_reading':base['reading'],
  'cancelled_upper_label':r'\deleted{'+letters[li]+'}',
  'relation_state':relations[ri]+(' with extra lower retrace' if ri else ''),
  'E_complete_state':copy.deepcopy(e_states[eh*2+ei]),'S15_complete_state':copy.deepcopy(minus[mh]),
  'S16_complete_state':copy.deepcopy(plus[ph]),'detached_point_state':copy.deepcopy(point),
  'base_A_candidate_provenance':copy.deepcopy(base),
  'hand_scope_rule':'Current component hands are the E/S15/S16/point fields above; the complete original A parent object is retained as provenance.',
  'literal_drawing_source_group':'B026-DIAG'}
for values in product(range(3),range(2),range(2),range(2),range(2),range(2)):
 li,ri,ei,eh,mh,ph=values;ai=base_lookup[li][ri][ei]
 row={'tuple':list(values),'original_A_candidate_index':ai,'E_state_index':eh*2+ei,'S15_state_index':mh,'S16_state_index':ph}
 base=base_diagrams[ai]['reading']
 assert r'\deleted{'+letters[li]+'}' in base
 assert relations[ri]+eloops[ei]+r'\subset' in base
 diagram_tuples.append(row);diagram_full.append(diagram_expand(row))
assert len(diagram_tuples)==96 and len({pack(x) for x in diagram_full})==96
for row,value in zip(diagram_tuples,diagram_full):
 recovered={'tuple':value['tuple'],
  'original_A_candidate_index':next(i for i,x in enumerate(base_diagrams) if pack(x)==pack(value['base_A_candidate_provenance'])),
  'E_state_index':next(i for i,x in enumerate(e_states) if pack(x)==pack(value['E_complete_state'])),
  'S15_state_index':next(i for i,x in enumerate(minus) if pack(x)==pack(value['S15_complete_state'])),
  'S16_state_index':next(i for i,x in enumerate(plus) if pack(x)==pack(value['S16_complete_state']))}
 assert recovered==row and pack(diagram_expand(recovered))==pack(value)
diagram={'scope':'Complete root states only; original A/B/C reader sets are unchanged.',
 'axis_order':['cancelled_label','relation','E_loop','E_upper_run','S15_upper_run','S16_upper_run'],
 'axes':[letters,relations,eloops,['head/retrace','independent upper run'],['head/retrace','independent upper run'],['head/retrace','independent upper run']],
 'tuple_order':'Explicit table below; rightmost axis advances first.',
 'original_A_base_candidates':base_diagrams,'reordered_base_lookup':base_lookup,
 'root_E_states':e_states,'exact_C_S15_states':minus,'exact_C_S16_states':plus,'root_point_state':point,
 'tuple_to_complete_state':diagram_tuples,
 'decoder':'diagram_expand in scan026_source_sections13_19_codecs_v01.py; it copies the indexed whole objects and exact fixed fields without text normalization.',
 'finite_forward_inverse_all_96':True,'root_authority_refs':auth['13']}

# §19: two original parent readings, with only distinctes qualification removed.
parent_original=copy.deepcopy(groups['A']['A026-G08']['complete_candidates']);parents=copy.deepcopy(parent_original)
for item in parents:
 assert item['reading'].count(r'\deleted{\unsure{distinctes}}')==1
 item['reading']=item['reading'].replace(r'\deleted{\unsure{distinctes}}',r'\deleted{distinctes}',1)
for old,new in zip(parent_original,parents):
 assert all(pack(old[k])==pack(new[k]) for k in old if k!='reading')
 assert new['reading'].replace(r'\deleted{distinctes}',r'\deleted{\unsure{distinctes}}',1)==old['reading']
heads={gid:copy.deepcopy(groups['A'][gid]['complete_candidates']) for gid in ['A026-S17','A026-S18','A026-S19','A026-S20','A026-G09']}
assert [len(heads[g]) for g in heads]==[1,2,2,2,2]
pair_tuples=[];pair_full=[]
def pair_expand(row):
 opener,h18,h19,h20=row['tuple']
 return {'tuple':row['tuple'],'complete_base_reading':parents[opener]['reading'],
  'opener_complete_state':copy.deepcopy(heads['A026-G09'][opener]),
  'S17_complete_state':copy.deepcopy(heads['A026-S17'][0]),
  'S18_complete_state':copy.deepcopy(heads['A026-S18'][h18]),'S19_complete_state':copy.deepcopy(heads['A026-S19'][h19]),
  'S20_complete_state':copy.deepcopy(heads['A026-S20'][h20]),
  'base_A_parent_candidate_provenance':copy.deepcopy(parent_original[opener]),
  'hand_scope_rule':'The exact local child fields retain every independent-run hand. Original broad A parent attribution remains raw provenance.',
  'fixed_text_state':r'\deleted{distinctes} \inserted{de X,}',
  'literal_drawing_source_group':'A026-G08'}
for values in product(range(2),repeat=4):
 row={'tuple':list(values)};pair_tuples.append(row);pair_full.append(pair_expand(row))
assert len(pair_tuples)==16 and len({pack(x) for x in pair_full})==16
for row,value in zip(pair_tuples,pair_full):
 recovered={'tuple':[next(i for i,x in enumerate(heads[gid]) if pack(x)==pack(value[field])) for gid,field in [('A026-G09','opener_complete_state'),('A026-S18','S18_complete_state'),('A026-S19','S19_complete_state'),('A026-S20','S20_complete_state')]]}
 assert recovered==row and pack(pair_expand(recovered))==pack(value)
pair={'scope':'Root parent expansion with original A child states intact.',
 'axis_order':['opener','S18_head','S19_head','S20_head'],'axes':[['[','('],['head/retrace','independent upper run'],['head/retrace','independent upper run'],['head/retrace','independent upper run']],
 'original_A_parent_candidates':parent_original,'resolved_parent_base_candidates':parents,
 'exact_A_local_states':heads,'tuple_to_complete_state':pair_tuples,
 'decoder':'pair_expand in scan026_source_sections13_19_codecs_v01.py; no original child object is altered.',
 'finite_forward_inverse_all_16':True,'root_authority_refs':auth['19']}

artifacts=[save('scan026_source_diagram96_codec_v01.json',diagram),save('scan026_source_diagram96_expanded_v01.json',diagram_full),
 save('scan026_source_pair16_codec_v01.json',pair),save('scan026_source_pair16_expanded_v01.json',pair_full)]
# Compact complete source-comment representation: definitions and explicit tuples.
def comment_lines(kind,codec):
 result=[f'% ROOT {kind}: finite component codec; definitions and every tuple are explicit below.\n']
 for key,value in codec.items():
  if key=='root_authority_refs':continue
  if isinstance(value,list):
   result.append('% ROOT '+kind+' '+key+' BEGIN\n')
   for i,v in enumerate(value):result.append('% ROOT '+kind+' '+key+'['+str(i)+'] '+json.dumps(v,ensure_ascii=False)+'\n')
   result.append('% ROOT '+kind+' '+key+' END\n')
  else:result.append('% ROOT '+kind+' '+key+' '+json.dumps(value,ensure_ascii=False)+'\n')
 return ''.join(result)
save('scan026_source_diagram96_comments_v01.txt',comment_lines('DIAGRAM96',diagram).encode(),True)
save('scan026_source_pair16_comments_v01.txt',comment_lines('PAIR16',pair).encode(),True)
proof={'source_only':True,'diagram_tuples':96,'pair_tuples':16,'forward_inverse_all_expanded_objects_exact':True,
 'C_S15_S16_candidate_fields_unchanged':True,'A_pair_child_candidate_fields_unchanged':True,'root_hand_fields_scoped_by_component':True,
 'original_reader_files_modified':0,'images_opened':0,'root_ink_choices':0,'authority_captures':captures,'artifacts':artifacts}
save('scan026_source_sections13_19_codec_proof_v01.json',proof)
print(json.dumps(proof,ensure_ascii=False,indent=2))
