"""Exact 91-locus selected-source contract, without edits or new ink decisions."""
from pathlib import Path
import copy,hashlib,json,re,sys
sys.dont_write_bytecode=True
B=Path('/workspace/scratch/94548b74fbe0');O=B/'out/checks'
TEX='out/checks/scan026_source_sections01_27_proposal_v01.tex'
P=(B/TEX).read_text();SHA=hashlib.sha256((B/TEX).read_bytes()).hexdigest()
assert SHA=='318b043580aba18b302169e52d7c3570208e8211cc7f32f8828cc070ee743615'
sha=lambda s:hashlib.sha256(s.encode() if isinstance(s,str) else s).hexdigest()
pack=lambda v:json.dumps(v,ensure_ascii=False,separators=(',',':'))
cache={};refs=[];ref_ids={};texts={TEX:P}
def save(name,value):
 raw=(json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode();p=O/name
 if p.exists():assert p.read_bytes()==raw
 else:p.write_bytes(raw)
 return {'path':str(p.relative_to(B)),'sha256':sha(raw),'bytes':len(raw)}
def get(value,pointer):
 for token in pointer.split('/')[1:] if pointer else []:
  token=token.replace('~1','/').replace('~0','~');value=value[int(token)] if isinstance(value,list) else value[token]
 return value
def load(path):
 if path not in cache:
  raw=(B/path).read_bytes();text=raw.decode();value=json.loads(text);spans={};dec=json.JSONDecoder()
  def ws(i):
   while i<len(text) and text[i].isspace():i+=1
   return i
  def walk(i,pointer):
   i=ws(i);start=i
   if text[i]=='{':
    i=ws(i+1)
    while text[i]!='}':
     key,i=dec.raw_decode(text,i);i=ws(i);assert text[i]==':'
     esc=key.replace('~','~0').replace('/','~1');i=walk(i+1,pointer+'/'+esc);i=ws(i)
     if text[i]==',':i=ws(i+1)
     else:assert text[i]=='}';break
    end=i+1
   elif text[i]=='[':
    i=ws(i+1);index=0
    while text[i]!=']':
     i=walk(i,pointer+'/'+str(index));index+=1;i=ws(i)
     if text[i]==',':i=ws(i+1)
     else:assert text[i]==']';break
    end=i+1
   else:_,end=dec.raw_decode(text,i)
   spans[pointer]=(start,end);return end
  end=walk(0,'');assert not text[end:].strip()
  cache[path]={'raw':raw,'text':text,'value':value,'spans':spans,'sha256':sha(raw)}
 return cache[path]
def jref(path,pointer):
 key=(path,pointer)
 if key in ref_ids:return ref_ids[key]
 data=load(path);value=get(data['value'],pointer);a,b=data['spans'][pointer];raw=data['text'][a:b]
 assert pack(json.loads(raw))==pack(value)
 rid=f'J{len(refs)+1:04d}'
 row={'reference_id':rid,'path':path,'file_sha256':data['sha256'],'json_pointer':pointer,
  'raw_json_char_start':a,'raw_json_char_end':b,'raw_json_utf8_start':len(data['text'][:a].encode()),
  'raw_json_utf8_end':len(data['text'][:b].encode()),'raw_json_sha256':sha(raw),
  'ordered_decoded_value_sha256':sha(pack(value)),'type':type(value).__name__}
 if isinstance(value,list):row['array_length']=len(value)
 if isinstance(value,dict):row['original_key_order']=list(value)
 refs.append(row);ref_ids[key]=rid;return rid
def value_of(rid):
 r=refs[int(rid[1:])-1];return get(load(r['path'])['value'],r['json_pointer'])
def sref(a,b,scope):
 assert 0<=a<=b<=len(P)
 return {'path':TEX,'file_sha256':SHA,'char_start':a,'char_end':b,'utf8_byte_start':len(P[:a].encode()),
  'utf8_byte_end':len(P[:b].encode()),'line_start':P.count('\n',0,a)+1,'line_end':P.count('\n',0,max(a,b-1))+1,
  'literal_sha256':sha(P[a:b]),'scope':scope}
def locate(literal,lo=0,hi=None,scope='exact local literal'):
 hi=len(P) if hi is None else hi;hits=[lo+m.start() for m in re.finditer(re.escape(literal),P[lo:hi])]
 assert len(hits)==1,(scope,literal[:80],hits)
 return sref(hits[0],hits[0]+len(literal),scope)

maps={w:load(f'out/readers/026/{w}/source_map.json')['value'] for w in 'ABC'}
keys={'A':'local_groups','B':'source_groups','C':'groups'}
groups={w:{g['id']:(i,g) for i,g in enumerate(maps[w][keys[w]])} for w in 'ABC'}
def arr(w,gid):
 if w=='B':
  i=next(i for i,x in enumerate(maps[w]['complete_candidate_records']) if x['graphic_id']==gid)
  return jref(f'out/readers/026/{w}/source_map.json',f'/complete_candidate_records/{i}/complete_candidate_states')
 i,g=groups[w][gid];key='complete_candidates' if w=='A' else 'candidate_states'
 return jref(f'out/readers/026/{w}/source_map.json',f'/{keys[w]}/{i}/{key}')

# Complete source group spans include each frozen donor's own prefix/suffix.
group_registry={}
for match in re.finditer(r'% BEGIN ([ABCR]026-[A-Za-z0-9]+)\n',P):
 gid=match.group(1);marker='% BEGIN '+gid;end_marker='% END '+gid
 assert P.count(marker+'\n')==1 and P.count(end_marker+'\n')==1,gid
 a=match.start();end_at=P.index(end_marker,a);b=end_at+len(end_marker)
 original=None;origin_ref=None
 if gid[0] in groups and gid in groups[gid[0]]:
  w=gid[0];i,g=groups[w][gid];original=g[{'A':'source_excerpt','B':'literal_source','C':'source_exact'}[w]]
  origin_ref=jref(f'out/readers/026/{w}/source_map.json',f'/{keys[w]}/{i}')
  prefix=original[:original.index(marker)];suffix=original[original.index(end_marker)+len(end_marker):]
  assert P[a-len(prefix):a]==prefix,(gid,'prefix')
  assert P[b:b+len(suffix)]==suffix,(gid,'suffix',repr(suffix),repr(P[b:b+len(suffix)]))
  a-=len(prefix);b+=len(suffix)
 else:
  assert P[b:b+1]=='\n';b+=1
 group_registry[gid]={'group_id':gid,'final_source':sref(a,b,'complete group including its exact own qualifier framing'),
  'frozen_source_group_ref':origin_ref,'literal_unchanged_from_frozen_group':original==P[a:b] if original is not None else None}
for gid,row in group_registry.items():
 a,b=row['final_source']['char_start'],row['final_source']['char_end']
 row['enclosing_groups']=[other for other,r in group_registry.items() if other!=gid and r['final_source']['char_start']<=a and b<=r['final_source']['char_end']]
def gr(gid):return copy.deepcopy(group_registry[gid]['final_source'])
def bounds(gid):r=group_registry[gid]['final_source'];return r['char_start'],r['char_end']
def inside(gid,literal,scope):return locate(literal,*bounds(gid),scope)
def line_inside(gid,needle,scope):
 a,b=bounds(gid);lines=[line for line in P[a:b].splitlines(keepends=True) if needle in line and not line.lstrip().startswith('%')]
 assert len(lines)==1,(gid,needle,len(lines));return inside(gid,lines[0],scope)

union_path='out/checks/scan026_source_union_v01.json';U=load(union_path)['value'];union={row['locus_id']:(i,row) for i,row in enumerate(U)}
pool=load('out/checks/scan026_source_union_state_pool_v01.json')['value'];pool={r['record_id']:r for r in pool}
root_path='out/checks/scan026_root_decisions.json';root=load(root_path)['value'];roots={};root_refs={}
for i,section in enumerate(root['decisions']):
 for lid,decision in section.get('locus_decisions',{}).items():
  assert lid not in roots,lid;roots[lid]=(section['section'],decision)
  root_refs[lid]=jref(root_path,f'/decisions/{i}/locus_decisions/{lid}')
supp_path='out/checks/scan026_root_locus_supplement_v01.json';supp=load(supp_path)['value']
assert supp['physical_loci_total']==91
root_refs['L051']=jref(supp_path,'/agreed_locus');root_refs['L052']=jref(supp_path,'/new_locus')

F12='out/checks/scan026_source_sections04_12_state_maps_v01.json'
F19='out/checks/scan026_source_sections13_19_selected_states_v01.json'
F24='out/checks/scan026_source_sections20_24_selected_states_v01.json'
F27='out/checks/scan026_source_sections25_27_selected_states_v01.json'
DC='out/checks/scan026_source_diagram96_codec_v01.json';DE='out/checks/scan026_source_diagram96_expanded_v01.json'
PE='out/checks/scan026_source_pair16_expanded_v01.json'
selection={}
def array(lid,rid,**extra):
 value=value_of(rid);assert isinstance(value,list)
 selection[lid]={'kind':'exact_complete_candidate_array','array_ref':rid,'candidate_count':len(value),**extra}
def singleton(lid,rid,**extra):
 assert isinstance(value_of(rid),dict)
 selection[lid]={'kind':'singleton_exact_object','object_ref':rid,'candidate_count':1,**extra}
for lid in [row['locus_id'] for row in U]+['L052']:singleton(lid,root_refs[lid],source_scope='exact root fixed reading/scope object')
for n in range(1,40):
 lid=f'S{n:02d}';array(lid,arr('C' if n in [15,16] else 'A',('C' if n in [15,16] else 'A')+'026-'+lid))
for lid,(i,row) in union.items():
 refsA=row['reader_sources']['A']['source_group_records']
 if lid.startswith('L') and refsA:
  assert len(refsA)==1
  record=pool[refsA[0]];g=get(maps['A'],record['raw_ref']['json_pointer']);array(lid,arr('A',g['id']))
array('L001',jref('out/readers/026/A/report.json','/differences/15/complete_candidates'))
array('L003',arr('B','B026-EFAM'))
array('L005',jref('out/readers/026/C/report.json','/differences/4/candidate_states'))
array('L006',jref(F12,'/0/exact_selected_objects'))
for lid,i in [('S04',1),('S05',2),('S07',3)]:array(lid,jref(F12,f'/{i}/exact_selected_candidate_states'))
array('S08',jref(F12,'/4/exact_three_child_states'),parent_locus='L011')
array('L011',jref(F12,'/4/exact_three_parent_states'),child_loci=['S08'])
selection['L008']={'kind':'fixed_parent_with_scoped_child_candidates','root_scope_ref':root_refs['L008'],
 'original_A_parent_candidate_provenance_ref':arr('A','A026-G03'),'child_loci':['S03','S04','S05','S06'],
 'scope_rule':'Each child array retains its own complete state and attribution. The parent preserves the root-authorized placement/guide and fixed wording. No flat tuple array is introduced.'}
array('L013',arr('B','B026-M03'),root_current_component_scope_ref=root_refs['L013'],placement_ref=jref(F19,'/other_selected_scopes/main_composite'))
for n in [9,10,11,12,13]:array(f'S{n:02d}',jref(F19,f'/ring_states/A026-S{n:02d}/exact_selected_candidates'))
array('S14',jref(F19,'/other_selected_scopes/S14/exact_root_candidates'))
array('L015',jref(DE,''),codec_ref=jref(DC,''),child_loci=['L016','L017','L018','L019','S15','S16'])
selection['L016']={'kind':'exact_parent_component_projection','parent_array_ref':jref(DE,''),
 'ordered_value_refs':[jref(DE,f'/{i}/cancelled_upper_label') for i in [0,32,64]],
 'shared_root_scope_ref':root_refs['L016'],'candidate_count':3,'explicit_parent_indices':[0,32,64]}
array('L017',jref(DC,'/root_E_states'))
selection['L018']={'kind':'exact_parent_component_projection','parent_array_ref':jref(DE,''),
 'ordered_value_refs':[jref(DE,f'/{i}/relation_state') for i in [0,16]],
 'shared_root_scope_ref':root_refs['L018'],'candidate_count':2,'explicit_parent_indices':[0,16]}
singleton('L019',jref(DC,'/root_point_state'))
selection['L020']['root_current_component_scope_ref']=root_refs['L020']
for lid,children in [('L021',['S13','L022','L023','L024','L025']),('L025',['S14','L026','L027'])]:
 selection[lid]={'kind':'fixed_parent_text_with_scoped_child_candidates','root_scope_ref':root_refs[lid],'child_loci':children,
  'scope_rule':'The fixed clause order is the root decision. Each named child retains its complete independent local scope; no flat product or replacement parent reading is inferred.'}
array('L022',arr('B','B026-GPEUT'),child_component_candidate_refs=[arr('B','B026-M04')],root_current_component_scope_ref=root_refs['L022'])
array('L023',jref('out/readers/026/C/report.json','/differences/22/candidate_states'))
b_atwo=arr('B','B026-ATWO');assert [x['reading'] for x in value_of(b_atwo)]==['à',':']
selection['L024']={'kind':'whole_object_permutation','original_array_ref':b_atwo,'new_index_to_old_index':[1,0],
 'inverse_old_index_to_new_index':[1,0],'candidate_count':2,'root_scope_ref':root_refs['L024']}
array('L027',arr('C','C026-M02'),root_current_component_scope_ref=root_refs['L027'])
array('L029',jref(PE,''),codec_ref=jref('out/checks/scan026_source_pair16_codec_v01.json',''),child_loci=['S17','S18','L030','S19','S20','L031','L032'])
array('L033',jref(F24,'/L033/selected/exact_values'))
array('L034',jref(F24,'/L034/selected/exact_values'))
array('L035',jref(F24,'/L035/exact_interpretations/exact_values'),root_current_component_scope_ref=jref(F24,'/L035/root_current_component_scope'),placement_ref=jref(F24,'/L035'))
array('L036',jref(F24,'/L036/exact_selected_complete_states'),child_loci=['L037'])
array('L037',jref(F24,'/L037/selected/exact_values'))
array('L038',jref(F24,'/L038/exact_selected_complete_states'))
array('L039',jref('out/readers/026/A/report.json','/differences/29/complete_candidates'))
selection['L042']={'kind':'fixed_parent_text_with_scoped_child_candidates','root_scope_ref':root_refs['L042'],'child_loci':['L043'],
 'scope_rule':'The words on and alors retain their root fixed reading; the intervening reduced mark retains the complete L043 array.'}
for lid in ['L043','L044','L045','S31','S32','S34','S39','L048','L049','L050']:array(lid,jref(F27,'/'+lid+'/selected_complete_states'))
array('L047',jref('out/readers/026/C/report.json','/differences/41/candidate_states'))
singleton('L051',jref(supp_path,'/agreed_locus'))
singleton('L052',jref(supp_path,'/new_locus'),source_binding_closure_ref=jref(F19,'/other_selected_scopes/main_composite'))

# Exact selected source spans: complete groups plus explicitly narrow components.
spans={};group_for={}
for lid,(i,row) in union.items():
 for rid in row['reader_sources']['A']['source_group_records']:
  gid=get(maps['A'],pool[rid]['raw_ref']['json_pointer'])['id']
  if gid in group_registry:spans[lid]=[gr(gid)];group_for[lid]=[gid]
for lid,gid in {'L003':'B026-EFAM','L013':'B026-M03','L015':'B026-DIAG','L022':'B026-GPEUT','L024':'B026-ATWO',
 'L027':'C026-M02','L033':'B026-GQDESC','L034':'B026-GADJ','L035':'R026-L035','L037':'C026-G09a',
 'L048':'C026-G12','L049':'B026-CAPFINAL','L050':'B026-NEFINAL','L052':'R026-L052'}.items():
 spans[lid]=[gr(gid)];group_for[lid]=[gid]
planmap=load('out/checks/scan026_source_sections01_27_proposal_v01_map.json')['value'];edits=planmap['literal_replacements']
def mapped_boundary(pos):
 shift=0
 for e in edits:
  a,b=e['base_char_start'],e['base_char_end']
  if pos<a:return pos+shift
  if pos==a:return e['proposal_char_start']
  if pos==b:return e['proposal_char_end']
  if a<pos<b:raise ValueError(('boundary inside replaced interval',pos,e['edit_id']))
  shift+=len(e['replacement'])-(b-a)
 return pos+shift
for lid,(i,row) in union.items():
 if lid in spans:continue
 originals=row['reader_sources']['A']['local_source_spans']
 if originals:
  try:spans[lid]=[sref(mapped_boundary(x['start_char']),mapped_boundary(x['end_char_exclusive']),'mapped exact A local source interval') for x in originals]
  except ValueError:pass

# Six physical diagram components retain their one complete B drawing owner.
da,db=bounds('B026-DIAG')
label_start=P.index('\\node[anchor=base west,inner sep=0pt,outer sep=0pt] at(58,-15)',da)
label_end=P.index('\\end{tikzpicture}}};',label_start)+len('\\end{tikzpicture}}};')
spans['L016']=[sref(label_start,label_end,'complete crossed upper label, its phantom, paths and qualifier')]
e_start=P.index('\\node[anchor=base west,inner sep=0pt,outer sep=0pt] at(53,47)',da)
e_end=P.index('\\end{tikzpicture}}};',e_start)+len('\\end{tikzpicture}}};')
spans['L017']=[sref(e_start,e_end,'complete lower E group with top run, body, shared loop and qualifier')]
spans['L018']=[inside('B026-DIAG',r'\draw[line width=.6pt](5,25)..controls(31,24)and(40,42)..(7,48);'+'\n'+r'\draw[line width=.6pt](5,44)--(30,45);','both exact relation paths')]
spans['L019']=[line_inside('B026-DIAG','at(34,9)','complete detached point node with local qualifier')]
spans['S15']=[inside('B026-DIAG',r'\draw[line width=.4pt](-55,23)--(-28,23);'+'\n'+r'\draw[line width=.4pt](-53,27)--(-35,30)--(-41,37)--(-63,48)--(-35,46);'+'\n'+r'\draw[line width=.4pt](-25,26)--(-14,27);','complete minus-Sigma head, body and minus paths')]
spans['S16']=[inside('B026-DIAG',r'\draw[line width=.4pt](148,20)--(177,19);'+'\n'+r'\draw[line width=.45pt](149,24)--(166,27)--(159,34)--(142,47)--(174,46);'+'\n'+r'\draw[line width=.5pt](188,20)--(188,33);\draw[line width=.5pt](180,26)--(195,26);','complete plus-Sigma head, body and both plus paths')]
for lid in ['L016','L017','L018','L019','S15','S16']:group_for[lid]=['B026-DIAG']

# Exact local prose scopes and the new explicitly positioned point group.
s13a,_=bounds('A026-S13');s14a,s14b=bounds('A026-S14')
end_literal=r' ouvert $\ne\varnothing$ et $\ne X$)';end=P.index(end_literal,s14b)+len(end_literal)
start=P.rfind(', et $',0,s13a)+2;assert P[start:start+4]=='et $'
spans['L021']=[sref(start,end,'complete root-decided parenthetical ending with all named child scopes')]
start=P.rfind('car $',0,s14a);assert start>=0
spans['L025']=[sref(start,end,'complete final car clause, with S14/comma/un-mark child scopes')]
spans['L026']=[inside('A026-S14',r'\draw[line width=.25pt,black!50] (567,1491) .. controls (571,1499) and (569,1508) .. (563,1515);','one separate baseline comma path')]
group_for['L026']=['A026-S14']
unedit=next(x for x in edits if x['edit_id']=='E026-17-un-marks')
spans['L027'].insert(0,sref(unedit['proposal_char_start'],unedit['proposal_char_end'],'complete C underset frame with un and its exact mark group'))
spans['L031']=[line_inside('A026-G08',r'{\deleted{distinctes}}','resolved cancelled distinctes visible node')]
spans['L032']=[line_inside('A026-G08',r'\inserted{de $X$,}','complete inserted de X comma node'),
 line_inside('A026-G08',r'\draw[line width=.29pt] (135,145)','complete root-selected bent insertion guide')]
group_for['L031']=group_for['L032']=['A026-G08']
ga,gb=bounds('A026-G12');assert P[ga-4:ga]=='on $' and P[gb:gb+7]=='$ alors'
spans['L042']=[sref(ga-4,ga-2,'fixed word on before the separately owned mark'),sref(gb+2,gb+7,'fixed word alors after the separately owned mark')]
ins_a,ins_b=bounds('A026-G10');assert P[ins_a-3:ins_a]=='si '
spans['L036'].insert(0,sref(ins_a-3,ins_a,'baseline first si, outside the insertion group'))
g2a,g2b=bounds('A026-G02');assert P[g2a-1:g2a]=='('
spans['L007'].insert(0,sref(g2a-1,g2a,'opening parenthesis before et'))
_,neend=bounds('B026-NEFINAL');assert P[neend:neend+len(r'\varnothing')]==r'\varnothing'
spans['L050'].append(sref(neend,neend+len(r'\varnothing'),'unchanged following slashed-empty-set token'))
spans['L051']=[locate('% archive sheet number: 25',scope='exact agreed archive comment')]
spans['L023']=[locate(r'\unsure{être|etre}',scope='exact selected local accent macro')]

# Every registry reference resolves to the original key order and raw JSON span.
for ref in refs:
 data=load(ref['path']);raw=data['text'][ref['raw_json_char_start']:ref['raw_json_char_end']]
 assert sha(raw)==ref['raw_json_sha256']
 assert pack(json.loads(raw))==pack(get(data['value'],ref['json_pointer']))

parent_links={}
for parent,definition in selection.items():
 for child in definition.get('child_loci',[]):parent_links.setdefault(child,[]).append(parent)
rows=[]
order=[row['locus_id'] for row in U]+['L052']
assert len(order)==len(set(order))==91
for lid in order:
 assert lid in spans and spans[lid],('missing selected source span',lid)
 for span in spans[lid]:assert sha(P[span['char_start']:span['char_end']])==span['literal_sha256']
 raw_union=jref(union_path,'/'+str(union[lid][0])) if lid in union else None
 row={'locus_id':lid,'location':union[lid][1]['location'] if lid in union else supp['new_locus']['reading'],
  'root_decision_ref':root_refs[lid],'selected_state_binding':selection[lid],
  'selected_source_spans':spans[lid],'selected_source_groups':group_for.get(lid,[]),
  'parent_locus_scopes':parent_links.get(lid,[]),'frozen_all_reader_and_witness_union_ref':raw_union}
 if lid=='L052':row['reader_provenance_scope']='Root-observed supplemental locus, first bound in root sections14/15; no independent reader object is supplied.'
 rows.append(row)
assert len([x for x in rows if x['locus_id'].startswith('S')])==39
assert all(x['selected_state_binding']['candidate_count']>=1 for x in rows if 'candidate_count' in x['selected_state_binding'])
# Validate permutations both directions without rewriting any source object.
for row in rows:
 d=row['selected_state_binding']
 if d['kind']=='whole_object_permutation':
  original=value_of(d['original_array_ref']);current=[copy.deepcopy(original[i]) for i in d['new_index_to_old_index']]
  recovered=[current[i] for i in d['inverse_old_index_to_new_index']]
  assert pack(recovered)==pack(original)
 if d['kind']=='exact_parent_component_projection':
  parent=value_of(d['parent_array_ref']);field='cancelled_upper_label' if row['locus_id']=='L016' else 'relation_state'
  assert [value_of(r) for r in d['ordered_value_refs']]==[parent[i][field] for i in d['explicit_parent_indices']]
  assert len({pack(value_of(r)) for r in d['ordered_value_refs']})==d['candidate_count']
contract={'schema':'scan026-root-selected-source-contract-v1','source_only':True,'source_content_changed':False,
 'main_approved':False,'root_record_flags_chosen':False,
 'final_staged_source':{'path':TEX,'sha256':SHA,'bytes':len(P.encode())},
 'locus_order':'The frozen90-locus union order, followed by root supplemental L052; this is a provenance order.',
 'physical_loci':91,'sigma_loci':39,'reference_table':refs,'source_group_registry':group_registry,'loci':rows,
 'scope_rules':['Every array reference resolves to all fields in the exact referenced order.','Scoped parent bindings preserve each local child candidate array separately.','Singleton root objects retain every root field.','All original reader/witness values remain in the frozen union and pool; this contract supplies only selected bindings.','Root diff/count/H/C-row flags remain outside this source contract.'],
 'verification':{'all_json_raw_spans_parse_to_exact_ordered_values':True,'all_selected_tex_spans_hash_match':True,
 'permutations_forward_inverse_exact':True,'component_projection_values_exact':True,'complete_91_locus_coverage':True,'all_39_Sigma_occurrences_bound':True}}
artifact=save('scan026_source_selected_contract_v01.json',contract)
summary={'contract':artifact,'final_source_sha256':SHA,'loci':91,'sigma_loci':39,'json_references':len(refs),'source_groups':len(group_registry),
 'selected_source_spans':sum(len(x['selected_source_spans']) for x in rows),
 'state_binding_kinds':{kind:sum(x['selected_state_binding']['kind']==kind for x in rows) for kind in sorted({x['selected_state_binding']['kind'] for x in rows})},
 'source_content_changed':False,'images_read':0,'root_flags_chosen':0,'all_assertions_passed':True}
save('scan026_source_selected_contract_proof_v01.json',summary)
print(json.dumps(summary,ensure_ascii=False,indent=2))
