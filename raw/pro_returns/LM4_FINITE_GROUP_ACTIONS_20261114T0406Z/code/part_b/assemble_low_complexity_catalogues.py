#!/usr/bin/env python3
"""Join the complete low-complexity catalogues, retaining the realization map.
Reads authoritative proof-program outputs and resolves every JSON pointer.
Package paths: code/part_b, code/part_c, code/root/higher_genus_output.
The workspace path mapper is the only environment-specific component.
"""
from pathlib import Path
from collections import Counter,defaultdict
import csv,json,hashlib,importlib.util
HERE=Path(__file__).resolve().parent
WORK=HERE.parents[1]
PACKAGED=HERE.name=='part_b' and HERE.parent.name=='code'

def local(package_path):
 p=Path(package_path);assert p.parts[0]=='code'
 if PACKAGED:return WORK/p
 if p.parts[1] in ('part_b','part_c'):return WORK/p.parts[1]/'code'/Path(*p.parts[2:])
 assert p.parts[1]=='root'
 return WORK/'root'/Path(*p.parts[2:])

def csvread(path):return list(csv.DictReader(local(path).open()))
CACHE={}
def jread(path):
 if path not in CACHE:CACHE[path]=json.loads(local(path).read_text())
 return CACHE[path]
def pointer(obj,path):
 if path=='':return obj
 assert path.startswith('/')
 for x in path[1:].split('/'):
  x=x.replace('~1','/').replace('~0','~')
  obj=obj[int(x)] if isinstance(obj,list) else obj[x]
 return obj

def select(path,container,key,value):
 arr=pointer(jread(path),container)
 matches=[i for i,x in enumerate(arr) if pointer(x,key)==value]
 assert len(matches)==1,(path,key,value,matches)
 ptr=container+'/'+str(matches[0])
 assert pointer(pointer(jread(path),ptr),key)==value
 return ptr

FIELDS=['realization_id','mapping_class_subgroup_id','surface_type','genus','punctures',
 'source_claim','source_row_id','source_positive_signature_pair_id',
 'positive_class_realization_id','positive_section_json','positive_section_pointer',
 'classification_certificate_json','classification_certificate_pointer','quotient_surface',
 'group_order','positive_subgroup_order','full_splitting_classes',
 'nontrivial_partial_splitting_classes','maximal_partial_classes_Phi','Gamma_orbits_on_Phi',
 'oval_section_classes','line_section_classes','actual_fixed_components',
 'source_table','section_json','section_pointer','shared_data_json','shared_data_pointer']
ROWS=[]

def geometric_section_kind(section):
 kind=section.get('kind',section.get('fixed_component_kind'))
 if kind=='algebraic section':kind=section.get('geometric_fixed_component_kind')
 return 'oval' if kind=='circle' else kind

def add(g,n,r,claim,table,detail,container='',key='/class_id',idkey='class_id',
        fieldmap=None,mapping_id=None,shared=None,positive='',quotient=''):
 typ=f'({g},{n})';sid=r[idkey];rid=f'g{g}n{n}:{sid}'
 base={'realization_id':rid,'mapping_class_subgroup_id':f'g{g}n{n}:{mapping_id or sid}',
  'surface_type':typ,'genus':g,'punctures':n,'source_claim':claim,'source_row_id':sid,
  'source_positive_signature_pair_id':positive,'quotient_surface':quotient,
  'positive_class_realization_id':'','positive_section_json':'','positive_section_pointer':'',
  'classification_certificate_json':'','classification_certificate_pointer':'',
  'source_table':table,'section_json':detail,
  'section_pointer':select(detail,container,key,sid),'shared_data_json':'','shared_data_pointer':''}
 aliases={'group_order':'order','positive_subgroup_order':'positive_order',
  'full_splitting_classes':'full_splitting_classes',
  'nontrivial_partial_splitting_classes':'nontrivial_partial_splitting_classes',
  'maximal_partial_classes_Phi':'maximal_partial_classes_Phi','Gamma_orbits_on_Phi':'Gamma_orbits_on_Phi',
  'oval_section_classes':'oval_section_classes','line_section_classes':'line_section_classes',
  'actual_fixed_components':'actual_fixed_components'}
 aliases.update(fieldmap or {})
 for dest,src in aliases.items():
  if src in r and r[src]!='':base[dest]=int(r[src])
  elif dest=='positive_subgroup_order':base[dest]=int(r['order'])
  elif dest=='actual_fixed_components':base[dest]=base['full_splitting_classes']
  else:base[dest]=0
 if shared:
  path,ct,ky,val=shared;base['shared_data_json']=path;base['shared_data_pointer']=select(path,ct,ky,val)
 assert set(base)==set(FIELDS),(sid,set(FIELDS)-set(base),set(base)-set(FIELDS))
 ROWS.append(base)

# Four exceptional image groups, with all realization fibers retained.
table='code/part_b/exceptional_finite_subgroups_and_lifts.csv';detail='code/part_b/exceptional_sections.json'
for r in csvread(table):
 g,n=map(int,r['type'].strip('()').split(','))
 # Actual oval/line counts are obtained from the section record, since its
 # nonaspherical sphere rows intentionally distinguish algebraic sections.
 record=pointer(jread(detail),select(detail,'/catalogue','/action_class',r['action_class']))
 kinds=[geometric_section_kind(x) for x in record['sections']]
 r['oval_section_classes']=kinds.count('oval');r['line_section_classes']=kinds.count('line')
 add(g,n,r,'B.36',table,detail,'/catalogue','/action_class','action_class',
     {'maximal_partial_classes_Phi':'Phi','Gamma_orbits_on_Phi':'Phi_orbits'},
     r['mapping_class_subgroup'])
# All hyperbolic spheres; B25's redundant four-puncture table is a cross-check.
for n in range(3,7):
 table=f'code/part_b/type_0_{n}_orbifold_catalogue.csv';detail=f'code/part_b/type_0_{n}_orbifold_sections.json'
 for r in csvread(table):add(0,n,r,'B.26',table,detail,quotient=r['orbifold'])
# All punctured tori; the 13 GL2Z rows are not included twice.
for n in range(1,5):
 table=f'code/part_b/type_1_{n}_affine_catalogue.csv';detail=f'code/part_b/type_1_{n}_affine_sections.json'
 for r in csvread(table):
  add(1,n,r,'B.27',table,detail,'/catalogue',fieldmap={'maximal_partial_classes_Phi':'Phi','Gamma_orbits_on_Phi':'Phi_orbits','oval_section_classes':'ovals','line_section_classes':'lines'},
      shared=('code/part_b/torus_affine_normal_forms.json','','/affine_id',int(r['affine_id'])))
# All extended genus-two actions; the independent oriented table is not added.
closed='code/part_b/type_2_0_extended_sections.json'
for n in range(3):
 table=f'code/part_b/type_2_{n}_extended_catalogue.csv';detail=f'code/part_b/type_2_{n}_extended_sections.json'
 for r in csvread(table):
  add(2,n,r,'B.28' if n==0 else 'B.29',table,detail,'/catalogue',
      shared=(closed,'/hyperelliptic_extensions','/class_id',r['extension_id']))
# Closed genus-three positive actions from the complete primary-source census.
table='code/root/higher_genus_output/oriented_higher_genus_catalogue.csv'
detail='code/root/higher_genus_output/oriented_higher_genus_sections.json'
positive_records=[r for r in csvread(table) if r['genus']=='3' and r['punctures']=='0']
POSITIVE_GROUPED=defaultdict(list)
for r in positive_records:POSITIVE_GROUPED[r['source_pair']].append(r)
POSITIVE={key:rs[0] for key,rs in POSITIVE_GROUPED.items()}
assert len(positive_records)==55 and len(POSITIVE)==49
POSITIVE_DETAIL=detail
# The source's 49 group/signature pairs contain 55 positive action classes.
# Recover the exact Aut(G)-vector-index -> topological-action map, retaining
# all extra orbits instead of identifying rows merely by source_pair.
rootcode=local('code/root/catalogue_higher_genus.py')
spec=importlib.util.spec_from_file_location('catalogue_higher_genus_index',rootcode)
positive_module=importlib.util.module_from_spec(spec);spec.loader.exec_module(positive_module)
actions=jread('code/root/research_data/actions-genus3.json')['actions']
positive_orbit_route={};positive_orbit_certificates=[]
for src,rs in POSITIVE_GROUPED.items():
 if len(rs)==1:continue
 ai=int(src.split('.')[1]);action=actions[ai-1];assert action['gamma']==0
 G=positive_module.Group([tuple(x-1 for x in p) for p in action['autgreps'][0]])
 orbits=positive_module.decoration_orbits(G,action,0,True)
 root_vector_keys={}
 for r in rs:
  rec=pointer(jread(POSITIVE_DETAIL),select(POSITIVE_DETAIL,'','/summary/id',r['id']))
  assert rec['group_elements']==[list(x) for x in G.el]
  root_vector_keys[G.tuple_key(rec['generating_vector'])]=r['id']
 assert len(root_vector_keys)==len(rs)==len(orbits)
 for orb in orbits:
  indices=sorted(st[0] for st in orb)
  matches={root_vector_keys[k] for i in indices
           if (k:=G.tuple_key(G.ids_of(action['autgreps'][i]))) in root_vector_keys}
  assert len(matches)==1,(src,indices,matches)
  cid=matches.pop()
  for i in indices:
   assert (src,i) not in positive_orbit_route
   positive_orbit_route[src,i]=cid
  positive_orbit_certificates.append({'source_pair':src,'positive_class':cid,
    'original_primary_autg_vector_indices':indices})
for r in positive_records:
 add(3,0,r,'B.33',table,detail,key='/summary/id',idkey='id',
     fieldmap={'full_splitting_classes':'full_sections','nontrivial_partial_splitting_classes':'nontrivial_partial_sections',
       'maximal_partial_classes_Phi':'phi_points','Gamma_orbits_on_Phi':'phi_orbits'},
     positive=r['source_pair'],quotient='orientable_genus_'+r['quotient_genus'])
# The five mutually disjoint mixed blocks.
blocks=[
 ('B.37','code/part_c/type_3_0_reflection_quotient_sections_catalogue.csv',
  'code/part_c/type_3_0_reflection_quotient_sections.json','','positive_action','disc',0,145),
 ('B.39','code/part_c/type_3_0_projective_quotient_catalogue.csv',
  'code/part_c/type_3_0_projective_quotient_sections.json','','positive_action','projective_plane',0,11),
 ('B.40','code/part_c/type_3_0_torus_mirrors_sections_catalogue.csv',
  'code/part_c/type_3_0_torus_mirrors_sections.json','','positive_action',None,1,57),
 ('B.41','code/part_b/type_3_0_klein_quotient_catalogue.csv',
  'code/part_b/type_3_0_klein_quotient_sections.json','/catalogue','positive_source','klein_bottle',1,6),
 ('B.38','code/part_b/type_3_0_free_positive_and_anti_catalogue.csv',
  'code/part_b/type_3_0_free_positive_and_anti_sections.json','/catalogue','positive_source',None,None,18)]
for claim,table,detail,ct,poskey,quot,pgamma,count in blocks:
 rs=csvread(table);assert len(rs)==count
 for r in rs:
  src=r[poskey];assert src in POSITIVE
  assert int(r['order'])==2*int(POSITIVE[src]['order'])
  assert int(r['positive_order'])==int(POSITIVE[src]['order'])
  if pgamma is not None:assert int(POSITIVE[src]['quotient_genus'])==pgamma
  else:assert src in ('O3.1','O3.2')
  quotient=quot or r.get('quotient')
  if not quotient:
   quotient=('orientable' if r['quotient_orientable']=='True' else 'nonorientable')+'_genus_'+r['quotient_genus_or_crosscaps']+'_mirrors_'+r['mirror_boundary_components']
  add(3,0,r,claim,table,detail,ct,positive=src,quotient=quotient)

classification_paths={
 'B.37':'code/part_c/type_3_0_reflection_quotient_certificates.json',
 'B.39':'code/part_c/type_3_0_projective_quotient_certificates.json',
 'B.40':'code/part_c/type_3_0_torus_mirrors_certificates.json'}
positive_routing_checks=[]
for r in ROWS:
 if r['surface_type']!='(3,0)':continue
 src=r['source_positive_signature_pair_id'];rs=POSITIVE_GROUPED[src]
 cert=None
 if r['source_claim'] in classification_paths:
  path=classification_paths[r['source_claim']]
  ptr=select(path,'','/class_id',r['source_row_id'])
  cert=pointer(jread(path),ptr)
  assert src==f"O3.{cert['positive_action']}"
  r['classification_certificate_json']=path
  r['classification_certificate_pointer']=ptr
 if r['source_claim']=='B.33':cid=r['source_row_id']
 elif len(rs)==1:cid=rs[0]['id']
 else:
  assert cert is not None and cert['kernel_orbit']
  found={positive_orbit_route[src,i] for i in cert['kernel_orbit']}
  assert len(found)==1,(r['source_row_id'],found)
  cid=found.pop()
  positive_routing_checks.append({'mixed_class':r['source_row_id'],
    'source_pair':src,'positive_class':cid,'certificate':r['classification_certificate_json'],
    'certificate_pointer':r['classification_certificate_pointer'],
    'original_primary_autg_vector_indices':cert['kernel_orbit']})
 assert cid in {a['id'] for a in rs}
 r['positive_class_realization_id']='g3n0:'+cid
 r['positive_section_json']=POSITIVE_DETAIL
 r['positive_section_pointer']=select(POSITIVE_DETAIL,'','/summary/id',cid)

ROWS.sort(key=lambda r:(r['genus'],r['punctures'],r['group_order'],r['positive_subgroup_order'],r['realization_id']))
assert len({r['realization_id'] for r in ROWS})==len(ROWS)==889
fibers=defaultdict(list)
for r in ROWS:fibers[r['mapping_class_subgroup_id']].append(r)
assert len(fibers)==882
expected={(0,0):(2,3),(0,1):(2,2),(0,2):(5,7),(0,3):(10,10),(0,4):(30,30),(0,5):(20,20),(0,6):(57,57),
          (1,0):(13,17),(1,1):(13,13),(1,2):(40,40),(1,3):(38,38),(1,4):(115,115),
          (2,0):(92,92),(2,1):(32,32),(2,2):(121,121),(3,0):(292,292)}
assert set(expected)=={(g,n) for g in range(4) for n in range(7) if 2*g+n<=6}
index=[]
for (g,n),(subgroups,actions) in expected.items():
 rs=[r for r in ROWS if (r['genus'],r['punctures'])==(g,n)]
 assert len(rs)==actions and len({r['mapping_class_subgroup_id'] for r in rs})==subgroups
 index.append({'surface_type':f'({g},{n})','genus':g,'punctures':n,'mapping_class_subgroup_classes':subgroups,
   'injectively_realized_action_classes':actions,'paper_claims':';'.join(sorted({r['source_claim'] for r in rs})),
   'source_tables':';'.join(sorted({r['source_table'] for r in rs})),
   'section_json_files':';'.join(sorted({r['section_json'] for r in rs})),
   'shared_data_json_files':';'.join(sorted({r['shared_data_json'] for r in rs if r['shared_data_json']}))})
subgroup_rows=[]
for mid,rs in sorted(fibers.items()):
 assert len({(r['surface_type'],r['group_order'],r['positive_subgroup_order']) for r in rs})==1
 subgroup_rows.append({'mapping_class_subgroup_id':mid,'surface_type':rs[0]['surface_type'],
  'group_order':rs[0]['group_order'],'positive_subgroup_order':rs[0]['positive_subgroup_order'],
  'realization_fiber_size':len(rs),'realization_ids':json.dumps([r['realization_id'] for r in rs]),
  'full_section_counts_in_fiber':json.dumps(sorted({r['full_splitting_classes'] for r in rs})),
  'partial_section_counts_in_fiber':json.dumps(sorted({r['nontrivial_partial_splitting_classes'] for r in rs})),
  'Phi_counts_in_fiber':json.dumps(sorted({r['maximal_partial_classes_Phi'] for r in rs})),
  'fixed_component_counts_in_fiber':json.dumps(sorted({r['actual_fixed_components'] for r in rs}))})
# Every external route has already been read and selected; verify again from
# the pointers, including the shared model identifiers used by section IDs.
route_count=0;section_record_checks=0
for r in ROWS:
 record=pointer(jread(r['section_json']),r['section_pointer']);assert isinstance(record,dict);route_count+=1
 if 'sections' in record:
  sections=record['sections']
  assert len(sections)==r['nontrivial_partial_splitting_classes'],r['realization_id']
  assert sum(bool(s['maximal']) for s in sections)==r['maximal_partial_classes_Phi'],r['realization_id']
  assert len(record['Phi_orbits'])==r['Gamma_orbits_on_Phi'],r['realization_id']
  full=sum(len(s['image_elements'])==r['group_order'] for s in sections) if r['group_order']>1 else 1
  assert full==r['full_splitting_classes'],r['realization_id']
  kinds=[geometric_section_kind(s) for s in sections]
  assert kinds.count('oval')==r['oval_section_classes'],r['realization_id']
  assert kinds.count('line')==r['line_section_classes'],r['realization_id']
 else:
  assert r['source_claim']=='B.33'
  assert len(record['partial_section_classes'])==r['nontrivial_partial_splitting_classes']
  assert len(record['maximal_sections'])==r['maximal_partial_classes_Phi']
  assert record['full_sections']==r['full_splitting_classes']
 section_record_checks+=1
 if r['shared_data_json']:
  record=pointer(jread(r['shared_data_json']),r['shared_data_pointer']);assert isinstance(record,dict);route_count+=1
 for stem in ('positive_section','classification_certificate'):
  if r[stem+'_json']:
   record=pointer(jread(r[stem+'_json']),r[stem+'_pointer']);assert isinstance(record,dict);route_count+=1

# C's independent master is assembled from the same disjoint mathematical
# blocks with a separate field adapter; compare every source ID and count.
independent=csvread('code/part_c/type_3_0_complete_catalogue.csv')
independent={r['class_id']:r for r in independent}
g3=[r for r in ROWS if r['surface_type']=='(3,0)'];assert len(g3)==len(independent)==292
assert {r['source_row_id'] for r in g3}==set(independent)
count_fields=['full_splitting_classes','nontrivial_partial_splitting_classes',
 'maximal_partial_classes_Phi','Gamma_orbits_on_Phi','oval_section_classes','line_section_classes']
for r in g3:
 other=independent[r['source_row_id']]
 for field in count_fields:assert r[field]==int(other[field]),(r['source_row_id'],field)
 assert r['source_claim']==other['source_result']
 assert r['source_positive_signature_pair_id']==other['positive_source']
 assert r['group_order']==int(other['order']) and r['positive_subgroup_order']==int(other['positive_order'])

def write(name,rs,fields=None):
 with (HERE/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rs[0]));w.writeheader();w.writerows(rs)
write('low_complexity_all_realizations.csv',ROWS,FIELDS)
write('low_complexity_mapping_class_subgroups.csv',subgroup_rows)
write('low_complexity_catalogue_index.csv',index)
write('type_3_0_master_catalogue.csv',g3,FIELDS)
blockcounts=Counter(r['source_claim'] for r in g3)
assert blockcounts=={'B.33':55,'B.37':145,'B.39':11,'B.40':57,'B.41':6,'B.38':18}
sourcecounts=Counter(r['source_positive_signature_pair_id'] for r in g3 if r['group_order']!=r['positive_subgroup_order'])
positiveclasscounts=Counter(r['positive_class_realization_id'] for r in g3 if r['group_order']!=r['positive_subgroup_order'])
source_paths={r['source_table'] for r in ROWS}|set(CACHE)|{'code/root/catalogue_higher_genus.py',
 'code/part_c/type_3_0_complete_catalogue.csv'}
summary={'surface_types':16,'mapping_class_subgroup_rows':882,'realization_rows':889,
 'realization_map_excess':7,'genus3_rows':292,'genus3_positive':55,'genus3_mixed':237,
 'genus3_by_claim':dict(blockcounts),'genus3_mixed_by_positive_source':dict(sorted(sourcecounts.items())),
 'genus3_mixed_by_exact_positive_class':dict(sorted(positiveclasscounts.items())),
 'genus3_positive_source_pairs':49,'genus3_positive_action_classes':55,
 'multiple_class_source_pairs':sorted(src for src,rs in POSITIVE_GROUPED.items() if len(rs)>1),
 'mixed_rows_in_multiple_class_source_pairs_resolved':len(positive_routing_checks),
 'independent_genus3_master_row_and_count_matches':292,
 'resolved_section_and_shared_json_pointers':route_count,'all_routes_resolved':True,
 'section_record_counts_reconciled':section_record_checks,
 'all_types_2g_plus_nu_le_6_present':True,'duplicate_realization_ids':0,
 'independent_crosscheck_catalogues_added_to_master':False,
 'input_sha256':{p:hashlib.sha256(local(p).read_bytes()).hexdigest() for p in sorted(source_paths)},
 'section_count_convention':'Full and nontrivial partial sections counted separately; trivial partial section excluded from Phi.'}
(HERE/'low_complexity_catalogue_validation.json').write_text(json.dumps(summary,indent=2)+'\n')
(HERE/'low_complexity_catalogue_routes.json').write_text(json.dumps({'schema':FIELDS,
 'package_path_convention':'Paths are relative to the root of the deliverable ZIP.',
 'pointer_convention':'RFC6901 JSON Pointer; every pointer was resolved against its exact source file.',
 'section_records':[{'realization_id':r['realization_id'],'section_json':r['section_json'],
   'section_pointer':r['section_pointer'],'shared_data_json':r['shared_data_json'],
   'shared_data_pointer':r['shared_data_pointer'],
   'positive_class_realization_id':r['positive_class_realization_id'],
   'positive_section_json':r['positive_section_json'],'positive_section_pointer':r['positive_section_pointer'],
   'classification_certificate_json':r['classification_certificate_json'],
   'classification_certificate_pointer':r['classification_certificate_pointer']} for r in ROWS]},indent=2)+'\n')
(HERE/'type_3_0_positive_class_routing.json').write_text(json.dumps({
 'source':'code/root/research_data/actions-genus3.json',
 'index_convention':'Zero-based indices in the source action.autgreps array; colored braid and mirror orbits use root catalogue_higher_genus.decoration_orbits.',
 'multiple_class_pair_positive_orbits':positive_orbit_certificates,
 'mixed_action_routing_checks':positive_routing_checks},indent=2)+'\n')
required=sorted(source_paths|{'code/part_b/assemble_low_complexity_catalogues.py'})
assert all(local(p).is_file() for p in required)
(HERE/'low_complexity_catalogue_required_paths.json').write_text(json.dumps({
 'path_base':'Root of the extracted deliverable ZIP',
 'required_for_assembler':required,'all_required_inputs_present':True,
 'generated_outputs':['code/part_b/'+name for name in (
  'low_complexity_all_realizations.csv','low_complexity_mapping_class_subgroups.csv',
  'low_complexity_catalogue_index.csv','type_3_0_master_catalogue.csv',
  'low_complexity_catalogue_validation.json','low_complexity_catalogue_routes.json',
  'type_3_0_positive_class_routing.json','low_complexity_catalogue_required_paths.json')],
 'documentation':'code/part_b/low_complexity_catalogue_README.md'},indent=2)+'\n')
print(json.dumps(summary,indent=2))
