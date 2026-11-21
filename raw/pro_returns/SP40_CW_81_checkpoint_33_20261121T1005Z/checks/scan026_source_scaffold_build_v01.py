"""Create an unchanged A spine and pending source/record scaffolding.

This is source bookkeeping only. It reads no image, chooses no state, imports no
root decision, writes no root/final file, and leaves every decision scalar unset.
"""
from pathlib import Path
from collections import OrderedDict, Counter
import copy, hashlib, json, re

BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
sha=lambda b:hashlib.sha256(b.encode('utf-8') if isinstance(b,str) else b).hexdigest()
packed=lambda v:json.dumps(v,ensure_ascii=False,separators=(',',':'))
def load(path):return json.loads((BASE/path).read_bytes())
def write(name,value,raw=False):
 assert name.startswith('scan026_source_') and '/' not in name
 body=value if raw else (json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode()
 assert isinstance(body,bytes)
 path=OUT/name
 if path.exists():assert path.read_bytes()==body,('frozen scaffold differs',name)
 else:path.write_bytes(body)
 return {'path':str(path.relative_to(BASE)),'sha256':sha(body),'bytes':len(body)}

registry=load('out/checks/scan026_source_union_sources_v01.json')
union=load('out/checks/scan026_source_union_v01.json')
pool=load('out/checks/scan026_source_union_state_pool_v01.json')
subtargets=load('out/checks/scan026_source_union_C_rows_v01.json')
hmarkers=load('out/checks/scan026_source_union_H_marker_bindings_v01.json')
texts={};objects={};frozen_bytes={}
for key,entry in registry.items():
 b=(BASE/entry['path']).read_bytes();assert sha(b)==entry['sha256']
 frozen_bytes[key]=b;texts[key]=b.decode()
 if entry['path'].endswith('.json'):objects[key]=json.loads(b)
def pointer(obj,path):
 for token in path.split('/')[1:]:
  token=token.replace('~1','/').replace('~0','~');obj=obj[int(token)] if isinstance(obj,list) else obj[token]
 return obj
def resolve(ref):return pointer(objects[ref['source']],ref['json_pointer'])
def exact(key,a,b,include=False):
 t=texts[key];lit=t[a:b]
 v={'path':registry[key]['path'],'sha256':registry[key]['sha256'],
    'char_start':a,'char_end':b,'utf8_byte_start':len(t[:a].encode()),'utf8_byte_end':len(t[:b].encode()),
    'line_start':t.count('\n',0,a)+1,'line_end':t.count('\n',0,max(a,b-1))+1,'body_sha256':sha(lit)}
 if include:v['literal']=lit
 assert frozen_bytes[key][v['utf8_byte_start']:v['utf8_byte_end']]==lit.encode()
 return v

# Locate raw JSON values without rewriting any number, string, key or spacing.
decoder=json.JSONDecoder();json_spans={}
def json_locations(text):
 locations={};n=len(text)
 def ws(i):
  while i<n and text[i] in ' \r\n\t':i+=1
  return i
 def parse(i,path):
  i=ws(i);a=i
  if text[i]=='{':
   i=ws(i+1)
   if text[i]!='}':
    while True:
     key,i=decoder.raw_decode(text,i);assert isinstance(key,str)
     i=ws(i);assert text[i]==':';i=parse(i+1,path+'/'+key.replace('~','~0').replace('/','~1'));i=ws(i)
     if text[i]=='}':break
     assert text[i]==',';i=ws(i+1)
   b=i+1
  elif text[i]=='[':
   i=ws(i+1);k=0
   if text[i]!=']':
    while True:
     i=parse(i,path+'/'+str(k));k+=1;i=ws(i)
     if text[i]==']':break
     assert text[i]==',';i=ws(i+1)
   b=i+1
  else:_,b=decoder.raw_decode(text,i)
  assert path not in locations;locations[path]=(a,b);return b
 end=parse(0,'');assert ws(end)==n
 return locations
for key in objects:json_spans[key]=json_locations(texts[key])

raw_bindings=[];pool_by_id={}
for item in pool:
 ref=item['raw_ref'];original=resolve(ref)
 if 'ordered_fields' in item:
  value=OrderedDict((f['key'],copy.deepcopy(f['value']) if 'value' in f else copy.deepcopy(resolve(f['exact_value_ref']))) for f in item['ordered_fields'])
 else:value=copy.deepcopy(item['value'])
 assert packed(value)==packed(original)
 a,b=json_spans[ref['source']][ref['json_pointer']]
 bound=exact(ref['source'],a,b);bound['json_pointer']=ref['json_pointer']
 assert packed(json.loads(texts[ref['source']][a:b]))==packed(original)
 raw_bindings.append({'record_id':item['record_id'],'raw_value_source':bound,'raw_ref':ref})
 pool_by_id[item['record_id']]=item

group_keys={'A':'local_groups','B':'source_groups','C':'groups'}
groups=[];by_reader={w:[] for w in 'ABC'};by_id={}
for w in 'ABC':
 for i,g in enumerate(objects[w+'.map'][group_keys[w]]):
  if w=='A':a,b=g['source_char_start'],g['source_char_end_exclusive'];literal=g['source_excerpt']
  elif w=='B':a,b=g['start_char'],g['end_char'];literal=g['literal_source']
  else:a,b=g['source_span']['start_character'],g['source_span']['end_character_exclusive'];literal=g['source_exact']
  assert texts[w+'.tex'][a:b]==literal
  ref={'source':w+'.map','json_pointer':f'/{group_keys[w]}/{i}'}
  row={'id':g['id'],'reader':w,'raw_group_ref':ref,'exact_source':exact(w+'.tex',a,b),
       'raw_group_pool_record':next(x['record_id'] for x in pool if x['raw_ref']==ref),
       'candidate_state_scope':'Complete original fields remain at raw_group_ref; no state or local hand is selected.',
       'containing_source_groups':[],'contained_source_groups':[],'root_selected':None,'main_approved':False}
  groups.append(row);by_reader[w].append(row);by_id[g['id']]=row
for w,items in by_reader.items():
 for g in items:
  a,b=g['exact_source']['char_start'],g['exact_source']['char_end']
  for other in items:
   if other is g:continue
   c,d=other['exact_source']['char_start'],other['exact_source']['char_end']
   if c<=a and b<=d:g['containing_source_groups'].append(other['id'])
   if a<=c and d<=b:g['contained_source_groups'].append(other['id'])

# Every character is bound once in a non-overlapping partition. Nested source
# scopes are retained as containing-group identities, not duplicated text.
partitions={}
for w,items in by_reader.items():
 ends=sorted({0,len(texts[w+'.tex'])}|{q for g in items for q in (g['exact_source']['char_start'],g['exact_source']['char_end'])})
 rows=[]
 for a,b in zip(ends,ends[1:]):
  owners=[g['id'] for g in items if g['exact_source']['char_start']<=a and b<=g['exact_source']['char_end']]
  rows.append({'exact_source':exact(w+'.tex',a,b),'containing_source_groups':owners})
 recovered=''.join(texts[w+'.tex'][r['exact_source']['char_start']:r['exact_source']['char_end']] for r in rows)
 assert recovered==texts[w+'.tex'];partitions[w]=rows

def commented(text,at):
 start=text.rfind('\n',0,at)+1
 for i in range(start,at):
  if text[i]=='%':
   j=i-1
   while j>=start and text[j]=='\\':j-=1
   if (i-j-1)%2==0:return True
 return False
def command_end(text,start):
 depth=0;comment=False
 for i in range(start,len(text)):
  ch=text[i];j=i-1
  while j>=0 and text[j]=='\\':j-=1
  escaped=(i-j-1)%2==1
  if ch=='%' and not escaped:comment=True
  if ch=='\n':comment=False
  if comment:continue
  if ch=='{' and not escaped:depth+=1
  if ch=='}' and not escaped:depth-=1
  if ch==';' and depth==0:return i+1
 raise ValueError(('unclosed command',start))
commands=[]
for w in 'ABC':
 t=texts[w+'.tex'];count=0
 for m in re.finditer(r'\\(draw|fill|path|coordinate|node|useasboundingbox)\b',t):
  if commented(t,m.start()):continue
  a,b=m.start(),command_end(t,m.start());count+=1
  containers=[g for g in by_reader[w] if g['exact_source']['char_start']<=a and b<=g['exact_source']['char_end']]
  containers.sort(key=lambda g:g['exact_source']['char_end']-g['exact_source']['char_start'])
  commands.append({'command_id':f'{w}026-SOURCE-CMD{count:03d}','reader':w,'command':m.group(1),'exact_source':exact(w+'.tex',a,b),
   'smallest_containing_source_group':containers[0]['id'] if containers else None,
   'all_containing_source_groups':[g['id'] for g in containers],
   'scope':'Literal source containment only; raw ownership and hand fields stay in the original group.',
   'root_selected':None,'main_approved':False})

spine=write('scan026_source_A_spine_v01.tex',frozen_bytes['A.tex'],raw=True)
assert spine['sha256']==registry['A.tex']['sha256']
state_catalog={'schema':'scan026-frozen-own-state-bindings-v1','source_only':True,'sources':registry,
 'raw_pool_file':{'path':'out/checks/scan026_source_union_state_pool_v01.json','sha256':sha((OUT/'scan026_source_union_state_pool_v01.json').read_bytes())},
 'raw_pool_value_bindings':raw_bindings,'reader_groups':groups,'complete_source_partitions':partitions,
 'literal_source_commands':commands,'root_decisions_applied':0,'images_opened':0}
catalog=write('scan026_source_state_catalog_v01.json',state_catalog)
spine_map={'schema':'scan026-initial-A-spine-v1','scan':26,'source_only':True,'initial_source_only':True,'main_adjudicated':False,'main_approved':False,
 'spine':spine,'original':registry['A.tex'],'byte_for_byte_identity':True,
 'root_authority_applied':[],'literal_replacements':[],
 'source_partitions':partitions['A'],'source_groups':[g for g in groups if g['reader']=='A'],
 'literal_source_commands':[c for c in commands if c['reader']=='A'],
 'candidate_catalog':catalog,'selected_groups':[],
 'limits':'The A bytes are an initial spine only. A group or candidate has no final selection from its presence in this scaffold.'}
spine_map_file=write('scan026_source_spine_map_v01.json',spine_map)

# Root-dependent values stay null. They cannot be consumed as a selected record.
decision_slots=[]
for row in union:
 bundles={}
 for w,own in row['reader_sources'].items():
  bundles[w]={'reader':w,'raw_locus_fields':copy.deepcopy(own),
   'scope':'Only this reader supplies these fields. Raw witness flags, report rows, own complete candidates and local hand fields retain their separate source roles.',
   'complete_reader_source':registry[w+'.tex'],'complete_own_partition_catalog':{'path':catalog['path'],'json_pointer':'/complete_source_partitions/'+w}}
 slot={'slot_id':'SOURCE026-'+row['locus_id'],'source_locus_id':row['locus_id'],'location':row['location'],
   'C':None,'H':None,'final':None,'alternatives':None,'readers':{w:None for w in 'ABC'},'reader_source_bundles':bundles,
   'evidence':None,'qualification':None,'confidence':None,'kind':None,'diff_C':None,'diff_H':None,
   'physical_count_parent':None,'root_count_authorization':None,'marked_in_H':None,
   'H_marker_ids':None,'H_source_scope_ids':[resolve(pool_by_id[rid]['raw_ref'])['source_id'] for rid in row['H_source_marker_records']],
   'H_marker_basis':{'literal_scope_records':copy.deepcopy(row['H_source_marker_records']),'root_local_flag_pending':True},
   'C_source_row_ids':copy.deepcopy(row['original_C_source_rows']),'C_doubt_status':None,'C_source_part_ids':[],
   'crop':None,'root_crop_evidence':None,'source_attachments':[],'selected_group_ids':[],
   'root_ink_choice_applied':False,'root_source_audit_choice_applied':False,'main_approved':False,
   'pending':'Root journal selection, local evidence, public own-reader/witness fields, count parent and exact selected-source binding.'}
 for parent in subtargets:
  if row['locus_id'] not in parent['loci']:continue
  canon=resolve(pool_by_id[parent['canonical_record']]['raw_ref'])
  if canon['source_id']=='C026-R02':
   slot['C_source_part_ids'].extend(x['canonical_part'] for x in parent['four_local_part_correspondences'] if x['locus']==row['locus_id'])
  elif canon['source_id']=='C026-R15':
   slot['C_source_part_ids'].append('C026-R15-1')
   slot['C_recurrence_binding']=copy.deepcopy(next(x for x in parent['eight_local_recurrences'] if x['locus']==row['locus_id']))
  else:slot['C_source_part_ids'].extend(x['part_id'] for x in canon['source_parts'])
 decision_slots.append(slot)

canonical=[]
for parent in subtargets:
 raw=copy.deepcopy(resolve(pool_by_id[parent['canonical_record']]['raw_ref']))
 raw['original_source_parts']=copy.deepcopy(raw['source_parts'])
 raw['selected_outcome']=None;raw['decision_ids']=[];raw['source_bindings']=copy.deepcopy(parent)
 for part in raw['source_parts']:
  part['original_decision_status']=part['decision_status'];part['selected_outcome']=None
  part['decision_ids']=[];part['source_attachments']=[];part['root_authority']=None;part['main_approved']=False
 canonical.append(raw)
assert len(canonical)==15 and len(canonical[1]['source_parts'])==4 and len(canonical[14]['source_parts'])==1

metadata=load('packets/026/metadata.json')
record={'schema':'scan026-pending-record-scaffold-v1','scan':26,'folder':metadata['folder'],'their_page':metadata['their_page'],'hua_has':metadata['hua_has'],
 'filename':'J81-03_81_scan026.tex','main_adjudicated':False,'main_approved':False,'scaffold_only':True,
 'decisions':[],'doubts':[],'inventory':[],'selected_graphical_groups':[],'source_locus_coverage':[],
 'C_source_rows':canonical,'abbreviations':[],'notes':'','attributed_content_note':None,'root_selected_content_note':None,'check_events':[],
 'counts':{'C':None,'H':None,'decision_loci':None,'inventory_elements':None,'remaining_doubt_loci':None,'check_events':None},
 'pending_root_decision_ids':[x['slot_id'] for x in decision_slots],
 'pending_decision_slots':decision_slots,'H_exact_marker_scopes':hmarkers,
 'S_source_only_context':copy.deepcopy(objects['S.scope']),
 'source_attachment_status':'Pending selected source; exact raw source bindings are ready.',
 'root_approval_status':'No root approval represented by this scaffold.',
 'initial_spine':spine,'initial_spine_map':spine_map_file,'frozen_state_catalog':catalog,
 'root_authority':{'journal_path':'out/checks/scan026_root_journal.md','decision_path':'out/checks/scan026_root_decisions.json','snapshot':None,'applied_sections':[]},
 'limits':'No root decision, count, confidence, hand, H-marker flag or final reading is inferred from the initial spine or reader majority.'}
record_file=write('scan026_source_record_scaffold_v01.json',record)

contract={'schema_sources':[],
 'public_decision_fields':['id','location','C','H','final','readers','evidence','confidence','kind','diff_C','diff_H','marked_in_H'],
 'public_final_rule':'final itself must contain every root-supported complete surviving state and its local qualification/hand/role/attachment scope; the delivery builder does not print alternatives in that final column.',
 'public_readers_rule':'A, B and C each require an exact complete local source and own candidate state; report silence supplies no alternate reading. Long common prose can use local exact spans and explicit frozen provenance.',
 'doubt_fields':['location','reading','alternatives','confidence','reason'],
 'inventory_fields':['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],
 'abbreviation_fields':['form','expansion'],'notes_type':'string',
 'attachment_fields':['path','workspace_path','sha256','char_start','char_end','utf8_byte_start','utf8_byte_end','line_start','line_end','body_sha256','literal','source_map_reference'],
 'eventual_attachment_path':'checks/scan026_final_draft.tex','eventual_workspace_path':'out/checks/scan026_final_draft.tex',
 'eventual_source_map_path':'out/checks/scan026_final_source_map.json','required_map_hash_field':'draft_sha256_utf8',
 'count_rule':'Every final scalar and physical count parent must cite explicit root authority; all scaffold values remain null.',
 'C_identity_rule':'15 actual parent rows; R02 four actual parts. R15 has one original part plus eight local occurrence bindings, with no invented extra source parents.',
 'H_rule':'Keep source-local uncertainty/illegibility scope separate from physical count parents and broad diagram or note descriptions.',
 'source_change_rule':'Root-authorized literal edits require exact before spans, complete donor/source bytes, exact authority spans, non-overlap, actual splice boundary bytes and finite forward/inverse replay.',
 'write_scope':'Only out/checks/scan026_source_* scaffolding/proposals; no root file, selected final draft, page, committed record or cumulative file write.'}
for p in ['out/checks/scan025_source_assemble.py','out/checks/scan025_source_build_record.py','out/checks/scan025_source_apply_record_closure.py','out/briefs/source_record_brief_v07.md','out/scripts/build_records.py','out/scripts/approve_page.py','out/scripts/validate.py']:
 contract['schema_sources'].append({'path':p,'sha256':sha((BASE/p).read_bytes())})
contract_file=write('scan026_source_record_contract_v01.json',contract)

assert all((BASE/registry[k]['path']).read_bytes()==b for k,b in frozen_bytes.items())
audit={'scope':'Finite source scaffolding checks only','A_spine_exact_original_bytes':True,
 'raw_JSON_value_bindings':len(raw_bindings),'raw_values_replayed_in_key_order':True,
 'reader_groups':{w:len(v) for w,v in by_reader.items()},'source_partition_counts':{w:len(v) for w,v in partitions.items()},
 'literal_commands':dict(Counter(x['reader'] for x in commands)),'all_three_source_partitions_reconstruct_exact_text':True,
 'C_parents':15,'C_R02_actual_parts':4,'C_R15_original_parts':1,'C_R15_occurrence_bindings':8,
 'pending_locus_slots':len(decision_slots),'root_decisions_applied':0,'selected_inventory_rows':0,'images_opened':0,
 'root_or_committed_files_written':0,'frozen_sources_unchanged':True,
 'artifacts':[spine,catalog,spine_map_file,record_file,contract_file]}
audit_file=write('scan026_source_scaffold_audit_v01.json',audit)
print(json.dumps(audit,ensure_ascii=False,indent=2))
