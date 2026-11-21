"""Apply only root-authorized scan023 public wording and identity-bound mirrors."""
from pathlib import Path
from collections import Counter,defaultdict
import copy,hashlib,json,re

ROOT=Path('/workspace/scratch/94548b74fbe0')
P=ROOT/'out/checks'
BASE='scan023_record_draft.json'
AUTH='scan023_root_public_repair_authorization.json'
AUDIT='scan023_source_audit.json'
SCOPE='scan023_root_public_repair_mirror_scope.json'
def read(name):return (P/name).read_text(encoding='utf-8')
def digest(value):return hashlib.sha256(value.encode('utf-8')).hexdigest()
def fref(name):return dict(path='out/checks/'+name,sha256=digest(read(name)))
def get(obj,pointer):
 cur=obj
 for k in pointer.split('/')[1:]:
  k=k.replace('~1','/').replace('~0','~')
  cur=cur[int(k)] if isinstance(cur,list) else cur[k]
 return cur
def put(obj,pointer,value):
 parts=[x.replace('~1','/').replace('~0','~') for x in pointer.split('/')[1:]]
 cur=obj
 for k in parts[:-1]:cur=cur[int(k)] if isinstance(cur,list) else cur[k]
 key=int(parts[-1]) if isinstance(cur,list) else parts[-1]
 cur[key]=copy.deepcopy(value)
def remove(obj,pointer):
 parts=[x.replace('~1','/').replace('~0','~') for x in pointer.split('/')[1:]]
 cur=obj
 for k in parts[:-1]:cur=cur[int(k)] if isinstance(cur,list) else cur[k]
 del cur[int(parts[-1]) if isinstance(cur,list) else parts[-1]]
def dumps(obj):return json.dumps(obj,ensure_ascii=False,indent=2)+'\n'

auth=json.loads(read(AUTH));audit=json.loads(read(AUDIT));scope=json.loads(read(SCOPE))
baseline_text=read(BASE);baseline=json.loads(baseline_text);current=copy.deepcopy(baseline)
assert digest(read(AUTH))=='988322521bcf2fd8b30c6f20b5760c94bd6e668f1a6ecc2d5241f807205ab97c'
assert digest(read(AUDIT))=='323eb5bfe03de3afff22ab8e100c9a1a12a4a9e4bfe40b727b10441c3ff3fdc7'
assert digest(baseline_text)==auth['baseline_record']['sha256']=='93bcfd5b78435a3d62f7853de218e218db4ff7998203c9a7a3d10ec90bf1440e'
assert digest((ROOT/'out/briefs/source_record_brief_v06.md').read_text())=='68c899416ff5c0a1093da36ce1304fb0883641dbe52ba54375d63530bd96d721'
assert scope['authorization_sha256']==digest(read(AUTH))
assert dumps(baseline)==baseline_text
bound_source={
 'scan023_final_draft.tex':digest(read('scan023_final_draft.tex')),
 'scan023_final_source_map.json':digest(read('scan023_final_source_map.json')),
 'scan023_root_count_authorization_v2.json':digest(read('scan023_root_count_authorization_v2.json')),
 'scan023_root_scope_authorization.json':digest(read('scan023_root_scope_authorization.json')),
 'scan023_source_audit.json':digest(read('scan023_source_audit.json')),
 'scan023_source_audit.md':digest(read('scan023_source_audit.md')),
 'scan023_record_bounded_closure.json':digest(read('scan023_record_bounded_closure.json')),
 'scan023_record_initial_gate.json':digest(read('scan023_record_initial_gate.json')),
 'scan023_record_initial_draft.json':digest(read('scan023_record_initial_draft.json'))
}
assert bound_source['scan023_final_draft.tex']=='b9a1249d12916f42eb5694e4e2433f2c95d5435083078cdb5f71db5ea7b69a1f'
assert bound_source['scan023_final_source_map.json']=='5c11242ea3f4fe19b14b70a8fb5707f7e36a6911cbce6525850a3201d86c41e3'

targets=[]
for finding in audit['findings']:
 for raw in finding['targets']:
  t=copy.deepcopy(raw);t['finding_id']=finding['id'];t['after']=t.pop('proposed_after')
  targets.append(t)
by_pointer={t['pointer']:t for t in targets}
assert len(by_pointer)==len(targets)
for override in auth['overrides']:
 t=by_pointer[override['pointer']]
 assert t['before']==override['before']
 t['audit_proposed_after_before_root_override']=t['after']
 t['after']=override['after'];t['root_override']=copy.deepcopy(override)
for extra in auth['additional_targets']:
 t=copy.deepcopy(extra);t.update(finding_id='ROOT-ADDITIONAL',defect=t.pop('reason'),
  current_mirror_pointers=dict(exact_current_value_mirrors=[],embedded_current_reading_mentions=[]))
 targets.append(t);by_pointer[t['pointer']]=t
assert len(targets)==92
for t in targets:assert get(baseline,t['pointer'])==t['before'],t['pointer']

decisions={d['id']:d for d in baseline['decisions']}
def origin_id(t):
 return baseline['decisions'][int(t['pointer'].split('/')[2])]['id']
def related(decision_id,origin):
 """Explicit current component containment, never equal text alone."""
 if decision_id==origin:return True
 return any(c['decision_id']==origin for c in decisions.get(decision_id,{}).get('selected_component_readings',[]))
def row_related(row,origin):
 return any(related(x,origin) for x in row.get('decision_ids',[]))
def identity_allows(pointer,target):
 parts=pointer.split('/')[1:]
 origin=origin_id(target);origin_reader='/readers/' in target['pointer']
 origin_witness=target['pointer'].split('/')[-1] in ('C','H') and not origin_reader
 if any(x in parts for x in ('provenance','reader_source_details','source_attachments','root_crop_evidence',
   'root_viewing_scope','complete_witness_contexts','witness_source_references','selected_source','source',
   'root_count_authorization','root_scope_authorization','source_map_reference','selected_source_map_reference')):
  return False,'Frozen source, attachment or history field.'
 if 'readers' in parts and not origin_reader:return False,'Independent own-reader quotation.'
 if origin_reader and 'readers' not in parts:return False,'Reader additions synchronize only public own-reader mirrors.'
 root=parts[0]
 if root=='decisions':
  index=int(parts[1]);other=baseline['decisions'][index]
  if origin_witness:return other['id']==origin,'Local witness cells are scoped to their own decision.'
  return related(other['id'],origin),'Explicit decision/component association.'
 if root=='source_locus_coverage':
  row=baseline[root][int(parts[1])]
  return row_related(row,origin),'Explicit locus/decision association.'
 if root=='doubts':
  row=baseline[root][int(parts[1])]
  return row_related(row,origin),'Explicit doubt/decision association.'
 if root=='inventory':
  row=baseline[root][int(parts[1])]
  return row_related(row,origin),'Explicit inventory/decision association.'
 if root=='selected_graphical_groups':
  row=baseline[root][int(parts[1])]
  # A particular current_readings entry must belong to the same decision or
  # its explicit containing frame; other entries of the group stay untouched.
  if len(parts)>3 and parts[2]=='current_readings':
   item=row['current_readings'][int(parts[3])]
   return related(item['decision_id'],origin),'Explicit selected group current-reading identity.'
  return row_related(row,origin),'Explicit selected group/decision association.'
 if root=='C_source_rows':
  row=baseline[root][int(parts[1])]
  if len(parts)>3 and parts[2]=='source_parts':
   return row_related(row['source_parts'][int(parts[3])],origin),'Exact canonical C part/decision association.'
  return False,'Canonical row provenance remains unchanged.'
 return False,'No explicit current decision/locus/group identity connects this value.'

suggested=defaultdict(list);accepted=[];excluded=[]
for t in targets:
 for kind,paths in t.get('current_mirror_pointers',{}).items():
  for pointer in paths:
   if pointer in by_pointer:
    excluded.append(dict(origin=t['pointer'],destination=pointer,reason='Explicit destination target has its own exact authorized replacement.'))
    continue
   ok,why=identity_allows(pointer,t)
   if not ok:
    excluded.append(dict(origin=t['pointer'],destination=pointer,reason=why));continue
   value=get(baseline,pointer)
   assert isinstance(value,str) and t['before'] in value,(t['pointer'],pointer)
   entry=dict(origin=t['pointer'],origin_locus=origin_id(t),destination=pointer,kind=kind,
    before=t['before'],after=t['after'],identity_basis=why)
   suggested[pointer].append(entry);accepted.append(entry)

# Explicit targets always win. Mirrors are transformed in one pass over each
# frozen old value; inserted replacements are never recursively rewritten.
changed_destinations={}
for t in targets:
 put(current,t['pointer'],t['after'])
 changed_destinations[t['pointer']]=dict(kind='explicit authorized target',origins=[t['pointer']])
for pointer,entries in suggested.items():
 old=get(baseline,pointer)
 substitutions={}
 for entry in entries:
  before,after=entry['before'],entry['after']
  if before in substitutions:assert substitutions[before]==after,(pointer,before)
  substitutions[before]=after
 pattern=re.compile('|'.join(re.escape(x) for x in sorted(substitutions,key=len,reverse=True)))
 new=pattern.sub(lambda match:substitutions[match.group(0)],old)
 assert new!=old,pointer
 put(current,pointer,new)
 changed_destinations[pointer]=dict(kind='identity-bound current mirror',
  origins=list(dict.fromkeys(e['origin'] for e in entries)))

# Root approved adding exact current local witness refs while preserving every
# pre-existing attachment and broad context. Existing pointer objects stay intact.
local_reference_additions=[]
for t in targets:
 parts=t['pointer'].split('/')
 if len(parts)!=4 or parts[-1] not in ('C','H'):continue
 n=int(parts[2]);who=parts[-1];authority=t.get('authority',{})
 if 'exact_local_source_refs' in authority:
  refs=copy.deepcopy(authority['exact_local_source_refs'])
 elif 'exact_cancelled_clause' in authority:
  old_context=baseline['decisions'][n]['complete_witness_contexts'][who]
  literal=authority['exact_cancelled_clause']
  offset=old_context['literal'].find(literal);assert offset>=0
  start=old_context['char_start_zero_based']+offset
  refs=[dict(path=old_context['path'],sha256_utf8=old_context['sha256_utf8'],
    char_start_zero_based=start,char_end_exclusive=start+len(literal),
    span_sha256_utf8=digest(literal),literal=literal)]
 elif t['finding_id']=='ROOT-ADDITIONAL':
  refs=[dict(path=authority['path'],sha256_utf8=authority['sha256'],
    char_start_zero_based=authority['char_start'],char_end_exclusive=authority['char_end'],
    span_sha256_utf8=digest(authority['literal']),literal=authority['literal'])]
 else:continue
 for ref in refs:
  source=(ROOT/ref['path']).read_text(encoding='utf-8')
  assert digest(source)==ref['sha256_utf8']
  assert source[ref['char_start_zero_based']:ref['char_end_exclusive']]==ref['literal']
  assert digest(ref['literal'])==ref['span_sha256_utf8']
 entry=dict(exact_local_sources=refs,corresponding_public_field=t['pointer'],
  retained_complete_context_pointer=f'/decisions/{n}/complete_witness_contexts/{who}',
  scope='Current exact local comparison references; all prior source attachments and complete original context remain unchanged.')
 current['decisions'][n].setdefault('public_local_witness_source_references',{})[who]=entry
 local_reference_additions.append(dict(pointer=f'/decisions/{n}/public_local_witness_source_references/{who}',after=entry,origin=t['pointer']))

# Verify only the authorized mutation, immutable fields, and exact inverse replay.
for t in targets:assert get(current,t['pointer'])==t['after'],t['pointer']
for old,new in zip(baseline['decisions'],current['decisions']):
 for field in ('id','diff_C','diff_H','physical_count_parent','confidence','marked_in_H',
  'H_marker_ids','C_doubt_status','C_source_row_ids','C_source_part_ids','main_approved',
  'source_attachments','reader_source_details','complete_witness_contexts','witness_source_references',
  'root_crop_evidence','root_count_authorization','provenance'):
  if field in old:assert new[field]==old[field],(old['id'],field)
assert current['counts']==baseline['counts']
assert current['provenance']==baseline['provenance']
assert current['main_approved'] is False and current['main_adjudicated'] is False
for field in ('source_attachments','source_map_reference','provenance'):
 for group0,group1 in zip(baseline['selected_graphical_groups'],current['selected_graphical_groups']):
  if field in group0:assert group0[field]==group1[field]
for row0,row1 in zip(baseline['C_source_rows'],current['C_source_rows']):
 assert row0['selected_outcome']==row1['selected_outcome']
 for part0,part1 in zip(row0['source_parts'],row1['source_parts']):
  for field in ('part_id','selected_status','outcome','decision_status','original_source_decision_status',
   'physical_count_parent','source_attachments','main_approved'):
   assert part0[field]==part1[field],(row0['source_id'],field)

operations=[]
def delta(old,new,path=''):
 if old==new:return
 if isinstance(old,dict) and isinstance(new,dict):
  for key in sorted(set(old)|set(new)):
   pointer=path+'/'+key.replace('~','~0').replace('/','~1')
   if key not in old:operations.append(dict(op='add',path=pointer,after=copy.deepcopy(new[key])))
   elif key not in new:operations.append(dict(op='remove',path=pointer,before=copy.deepcopy(old[key])))
   else:delta(old[key],new[key],pointer)
 elif isinstance(old,list) and isinstance(new,list) and len(old)==len(new):
  for index,(a,b) in enumerate(zip(old,new)):delta(a,b,path+'/'+str(index))
 else:operations.append(dict(op='replace',path=path,before=copy.deepcopy(old),after=copy.deepcopy(new)))
delta(baseline,current)
assert all(op['op']!='remove' for op in operations)
for op in operations:
 if op['path'] in changed_destinations:continue
 assert op['path'].endswith('/public_local_witness_source_references'),op['path']
forward=copy.deepcopy(baseline)
for op in operations:
 if op['op']=='remove':remove(forward,op['path'])
 else:put(forward,op['path'],op['after'])
new_text=dumps(current)
assert dumps(forward)==new_text
inverse=copy.deepcopy(current)
for op in reversed(operations):
 if op['op']=='add':remove(inverse,op['path'])
 else:put(inverse,op['path'],op['before'])
assert dumps(inverse)==baseline_text
for name,expected in bound_source.items():assert digest(read(name))==expected,name

# Construct full current public review from the repaired record, without running
# the original builder or any broad source audit.
review=['# Scan023 current record for root review','',
 'Bounded public-field repairs follow the frozen audit and root authorization; source/map/counts remain frozen. Final approval remains false.','',
 '## Current decisions','']
for d in current['decisions']:
 review.extend(['### '+d['id']+' — '+d['location'],'',
  'C: '+d['C'],'','H: '+d['H'],'','Selected: '+d['final'],'',
  'Complete alternatives: '+json.dumps(d.get('alternatives',[]),ensure_ascii=False),'',
  'Confidence: '+d['confidence']+'; C/H counts: '+str(int(d['diff_C']))+'/'+str(int(d['diff_H']))+
   '; parent '+d['physical_count_parent']+'; marked_in_H '+str(d['marked_in_H'])+'.','',
  'Evidence: '+d['evidence'],'','Qualification: '+d.get('qualification','Source-only S scope.'),''])
 for role in 'ABC':review.extend(['Own '+role+': '+d['readers'][role],''])
review.extend(['## Current doubts',''])
for d in current['doubts']:review.extend(['### '+d['id']+' — '+d['location'],'',d['reading'],'',
 'Alternatives: '+json.dumps(d['alternatives'],ensure_ascii=False),'','Confidence: '+d['confidence'],'',d['reason'],''])
review.extend(['## Selected inventory, interleaved',''])
for i in current['inventory']:review.extend([i['element']+' — '+i['kind']+' — '+i['hand']+' — '+i['position'],
 i['first_words_or_objects'],'Decision coverage: '+', '.join(i['decision_ids']),''])
review.extend(['## Brief attributed note','',current['notes'],'','## Abbreviations',''])
for a in current['abbreviations']:review.append(a['form']+' — probable '+a['expansion'])
new_review='\n'.join(review)+'\n'

# Preserve all four frozen baseline files under additional names before writes.
backups={}
for original,suffix in [('scan023_record_draft.json','draft.json'),('scan023_record_review.md','review.md'),
 ('scan023_record_gate.json','gate.json'),('scan023_record_release.json','release.json')]:
 snapshot='scan023_record_pre_public_repair_'+suffix
 original_text=read(original)
 if (P/snapshot).exists():assert read(snapshot)==original_text
 else:(P/snapshot).write_text(original_text,encoding='utf-8')
 backups[original]=dict(snapshot=fref(snapshot),original_path='out/checks/'+original,original_sha256=digest(original_text))

new_record_hash=digest(new_text)
closure=dict(scan=23,scope='Root-authorized bounded public reporting repair; no source, ink, count, confidence, parent, outcome or approval change.',
 authorization=fref(AUTH),identity_mirror_authorization=fref(SCOPE),frozen_audit=fref(AUDIT),
 frozen_audit_markdown=fref('scan023_source_audit.md'),
 brief=dict(path='out/briefs/source_record_brief_v06.md',sha256='68c899416ff5c0a1093da36ce1304fb0883641dbe52ba54375d63530bd96d721'),
 baseline_files=backups,
 current_record=dict(path='out/checks/scan023_record_draft.json',sha256=new_record_hash),
 exact_authorized_targets=targets,
 mirror_selection=dict(rule=scope['scope'],accepted_current_mirrors=accepted,excluded_equality_candidates=excluded,
  note='Every explicit target has precedence. Identity-based selection prevents one local witness excerpt from being applied to another locus sharing a broad old context. Replacements use one pass over each frozen old string.'),
 local_reference_addition_authorization='Root message: Approved those exact local reference additions at the repaired decisions. Preserve every pre-existing attachment and broad original context; include the added field pointers and exact source hashes/spans in the bounded closure. No new approval fields are needed.',
 local_reference_additions=local_reference_additions,
 forward_operations=operations,forward_replay_exact_utf8_sha256=digest(dumps(forward)),
 inverse_replay_exact_utf8_sha256=digest(dumps(inverse)),
 forward_replay_matches_current_bytes=True,inverse_replay_matches_frozen_baseline_bytes=True,
 unchanged_text_files={name:dict(path='out/checks/'+name,sha256=value) for name,value in bound_source.items()},
 unchanged_counts=copy.deepcopy(current['counts']),main_approved=False,
 necessary_gate_scope='Authorized target equality; identity-bound current mirrors; exact added local witness spans; immutable selected/count/source/provenance fields; forward/inverse byte correspondence. No repeated broad audit.')
closure_text=dumps(closure);closure_hash=digest(closure_text)
gate=copy.deepcopy(json.loads(read('scan023_record_gate.json')))
gate['record']=dict(path='out/checks/scan023_record_draft.json',sha256=new_record_hash)
gate['bounded_public_repair']=dict(authorization=fref(AUTH),identity_scope=fref(SCOPE),
 frozen_previous_gate=backups['scan023_record_gate.json']['snapshot'],
 closure=dict(path='out/checks/scan023_record_public_repair_closure.json',sha256=closure_hash),
 authorized_targets_applied=len(targets),changed_field_operations=len(operations),
 selected_source_map_counts_and_flags_unchanged=True,all_prior_attachments_and_contexts_unchanged=True,
 added_exact_local_witness_fields=len(local_reference_additions),
 forward_inverse_byte_correspondence=True,root_approved=False)
gate['verification_scope']='Original required source/attachment gate preserved under its frozen snapshot; this current gate adds only the necessary authorized public-repair and byte-closure checks.'
gate_text=dumps(gate);gate_hash=digest(gate_text)

# A readable primary-target review accompanies the exhaustive old/new operation
# list. Both identify every actual current destination, including embedded edits.
changed_report=['# Scan023 bounded public reporting changes','',
 'Root authorized the exact frozen-audit replacements, the U56 final override, U62/C archive comparison, and exact local witness reference additions. Source, map, counts, confidence, parents, C outcomes, H markers and false approval flags remain unchanged.','',
 '## Exact primary changes','']
for t in targets:
 changed_report.extend(['### '+t['finding_id']+' — '+t['pointer'],'',t['defect'],'',
  'Before:','',t['before'],'','After:','',t['after'],'',
  'Identity-bound current mirror destinations:'])
 dest=[pointer for pointer,info in changed_destinations.items() if t['pointer'] in info['origins'] and pointer!=t['pointer']]
 changed_report.extend(['- '+x for x in dest] or ['- None beyond this explicit target.'])
 changed_report.append('')
changed_report.extend(['## Added exact local witness references',''])
for addition in local_reference_additions:
 changed_report.extend(['### '+addition['pointer'],'','Before: field absent.','',
  'After:','',json.dumps(addition['after'],ensure_ascii=False,indent=2),''])
changed_report.extend(['## Complete actual field-change inventory','',
 'The closure JSON retains the complete exact old/new value of every operation below. Each scalar change is listed here with its full before/after value. Existing source/provenance objects are unchanged.',''])
for op in operations:
 changed_report.extend(['### '+op['op']+' '+op['path'],'',
  'Before:','',json.dumps(op.get('before','FIELD ABSENT'),ensure_ascii=False,indent=2),'',
  'After:','',json.dumps(op['after'],ensure_ascii=False,indent=2),''])
changed_text='\n'.join(changed_report)+'\n'

(P/BASE).write_text(new_text,encoding='utf-8')
(P/'scan023_record_review.md').write_text(new_review,encoding='utf-8')
(P/'scan023_record_gate.json').write_text(gate_text,encoding='utf-8')
(P/'scan023_record_public_repair_closure.json').write_text(closure_text,encoding='utf-8')
(P/'scan023_record_public_repair_review.md').write_text(changed_text,encoding='utf-8')
release=dict(scan=23,stage='frozen after root-authorized bounded public reporting repair',
 main_adjudicated=False,main_approved=False,
 current_files={name:fref(name) for name in ['scan023_record_draft.json','scan023_record_review.md','scan023_record_gate.json',
  'scan023_record_public_repair_closure.json','scan023_record_public_repair_review.md','scan023_record_public_repair.py']},
 preserved_baseline_files=backups,original_release_history=backups['scan023_record_release.json']['snapshot'],
 frozen_audit=fref(AUDIT),authorization=fref(AUTH),identity_mirror_authorization=fref(SCOPE),
 selected_source=fref('scan023_final_draft.tex'),selected_source_map=fref('scan023_final_source_map.json'),
 counts=copy.deepcopy(current['counts']),original_C_outcomes=dict(resolved=4,retained=12,canonical_parts=16),
 repair=dict(explicit_targets=len(targets),changed_field_operations=len(operations),added_local_witness_fields=len(local_reference_additions),
  forward_replay_exact=True,inverse_replay_exact=True,identity_bound_mirrors=True),
 remaining_issues=[],freeze='No further writes without root bounded-repair direction. This release makes no final approval or ink decision.')
(P/'scan023_record_release.json').write_text(dumps(release),encoding='utf-8')
assert digest(read(BASE))==new_record_hash
for name,expected in bound_source.items():assert digest(read(name))==expected,name
for original,b in backups.items():
 assert digest((ROOT/b['snapshot']['path']).read_text())==b['original_sha256']
print(json.dumps(dict(record=fref(BASE),review=fref('scan023_record_review.md'),
 gate=fref('scan023_record_gate.json'),closure=fref('scan023_record_public_repair_closure.json'),
 changed_review=fref('scan023_record_public_repair_review.md'),release=fref('scan023_record_release.json'),
 targets=len(targets),operations=len(operations),local_reference_fields=len(local_reference_additions),
 accepted_mirror_destinations=len(suggested),excluded_equality_candidates=len(excluded),
 counts=current['counts'],source_unchanged=True,approval=False),ensure_ascii=False,indent=2))
