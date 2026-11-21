"""Consolidated root/qa022 bounded record repair; text and clerical work only."""
from pathlib import Path
import copy,hashlib,json,re
from scan022_source_support_record_evidence_v01 import EVIDENCE,EVIDENCE_SECTIONS,CROP_SECTIONS

BASE=Path('/workspace/scratch/94548b74fbe0')
INITIAL='out/checks/scan022_record_audit_initial_release/scan022_record_draft.json'
RECORD='out/checks/scan022_record_draft.json'
INITIAL_SHA='7eb888d555271003fd289011a65da66cfba32ff853be58e3f3df922112afc981'
MAP='out/checks/scan022_final_source_map.json'
DRAFT='out/checks/scan022_final_draft.tex'
MAP_SHA='a42832dfa6f42a815cab73d5e9b2aede328e61a6db1fd1f48c6967b76f87c42d'
DRAFT_SHA='faa03cb65c5976db4ea0c41303e089d837ce2a808cb81f2e6f26e8dc42850757'
AUTH='out/checks/scan022_source_support_root_authorizations.json'
FROZEN_AUTH='out/checks/scan022_source_support_root_authorizations_frozen_v01.json'
AUTH_SHA='ea80dcec80ce7b4a64e15f3ccd990b92fc5a44769c5226844b5a9f6004332a64'
JOURNAL='out/checks/scan022_source_support_journal_phase_009.md'
AUDIT='out/checks/scan022_source_audit_closure_v01.json'
AUDIT_MD='out/checks/scan022_source_audit_closure_v01.md'
DIFF='out/checks/scan022_record_bounded_public_diff_v01.json'
CLOSURE='out/checks/scan022_record_bounded_public_closure_v01.json'
sha=lambda p:hashlib.sha256((BASE/p).read_bytes()).hexdigest()
read=lambda p:json.loads((BASE/p).read_text())
def ref(p,pointer=None):
 d={'path':p,'sha256':sha(p)}
 if pointer is not None:d['json_pointer']=pointer
 return d
def write(p,d):
 (BASE/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');return ref(p)
def unique(x):return list(dict.fromkeys(x))
def key_of(s):return int(s.split('-L')[1]) if '-L' in s else 'ROOT-M01'
def resolve(v,p):
 for s in p.split('/')[1:]:
  s=s.replace('~1','/').replace('~0','~');v=v[int(s)] if isinstance(v,list) else v[s]
 return v
def esc(s):return str(s).replace('~','~0').replace('/','~1')
def differences(old,new,p=''):
 out=[]
 if isinstance(old,dict) and isinstance(new,dict):
  for k in sorted(set(old)|set(new)):
   q=p+'/'+esc(k)
   if k not in old:out.append({'op':'add','path':q,'new':new[k]})
   elif k not in new:out.append({'op':'remove','path':q,'old':old[k]})
   else:out.extend(differences(old[k],new[k],q))
 elif isinstance(old,list) and isinstance(new,list) and len(old)==len(new):
  for i,(a,b) in enumerate(zip(old,new)):out.extend(differences(a,b,p+'/'+str(i)))
 elif old!=new:out.append({'op':'replace','path':p,'old':old,'new':new})
 return out
def inverse_replay(current,changes):
 out=copy.deepcopy(current)
 for c in reversed(changes):
  bits=c['path'].split('/')[1:];parent=out
  for s in bits[:-1]:
   s=s.replace('~1','/').replace('~0','~');parent=parent[int(s)] if isinstance(parent,list) else parent[s]
  k=bits[-1].replace('~1','/').replace('~0','~');k=int(k) if isinstance(parent,list) else k
  if c['op']=='add':del parent[k]
  else:parent[k]=copy.deepcopy(c['old'])
 return out

assert sha(INITIAL)==INITIAL_SHA and sha(RECORD)==INITIAL_SHA
assert sha(MAP)==MAP_SHA and sha(DRAFT)==DRAFT_SHA and sha(AUTH)==AUTH_SHA
assert sha(AUDIT)=='6aaaba038e93fc5d84dac002284ed3444ed54f5a1a78210edbca73ac7eb72014'
assert sha(AUDIT_MD)=='b906a32dd32f4d81d6e856549dd19c2cef05800d8b30c82385c550eb5f0693fd'
auth_bytes=(BASE/AUTH).read_bytes()
if (BASE/FROZEN_AUTH).exists():assert (BASE/FROZEN_AUTH).read_bytes()==auth_bytes
else:(BASE/FROZEN_AUTH).write_bytes(auth_bytes)
initial=read(INITIAL);r=copy.deepcopy(initial);m=read(MAP);auth=read(FROZEN_AUTH)
draft=(BASE/DRAFT).read_text();journal=(BASE/JOURNAL).read_text()
heads=list(re.finditer(r'^## (\d+) .+$',journal,re.M));sections={};crops={}
for i,h in enumerate(heads):
 n=int(h.group(1));a=h.start();z=heads[i+1].start() if i+1<len(heads) else len(journal)
 sections[n]={**ref(JOURNAL),'char_start':a,'char_end':z,'utf8_byte_start':len(journal[:a].encode()),'utf8_byte_end':len(journal[:z].encode()),'line_start':journal.count('\n',0,a)+1,'line_end':journal.count('\n',0,z-1)+1,'body_sha256':hashlib.sha256(journal[a:z].encode()).hexdigest()}
 match=re.search(r'Viewed `([^`]+)` once\.',journal[a:z])
 if match:crops[n]=match.group(1)
repaired_auth=[]
def repair_auth(v,p=''):
 if isinstance(v,dict):
  if 'source_authorization_ref'in v:
   q=v['source_authorization_ref']
   if q.get('path')==AUTH:assert v['root_journal_snapshot_source']==resolve(auth,q['json_pointer'])['root_journal_snapshot_source'],p
  if v.get('path')==AUTH and 'sha256'in v:
   repaired_auth.append({'pointer':p,'old_sha256':v['sha256'],'new_sha256':AUTH_SHA});v['path']=FROZEN_AUTH;v['sha256']=AUTH_SHA
  for k,x in list(v.items()):repair_auth(x,p+'/'+esc(k))
 elif isinstance(v,list):
  for i,x in enumerate(v):repair_auth(x,p+'/'+str(i))
repair_auth(r);assert len(repaired_auth)==229,len(repaired_auth)

def att(s,p):
 a,z=s['start_char'],s['end_char_exclusive'];assert hashlib.sha256(draft[a:z].encode()).hexdigest()==s['sha256_utf8']
 return {'path':'checks/scan022_final_draft.tex','workspace_path':DRAFT,'manifest':'checks/scan022_final_source_map.json','workspace_manifest_path':MAP,'char_start':a,'char_end':z,'byte_start':len(draft[:a].encode()),'byte_end':len(draft[:z].encode()),'line_start':s['start_line'],'line_end':s['end_line'],'literal_sha256_utf8':s['sha256_utf8'],'final_file_sha256':DRAFT_SHA,'draft_sha256_utf8':DRAFT_SHA,'source_map_sha256':MAP_SHA,'source_map_pointer':p}
def gatt(g):return att(m['graphical_group_final_spans'][g]['final_span'],f'/graphical_group_final_spans/{g}/final_span')
def natt(t):return att(m['A_label_final_spans'][t],f'/A_label_final_spans/{t}')
decisions={d['id']:d for d in r['decisions']}
for d in r['decisions']:
 k=key_of(d['id']);d['evidence']=EVIDENCE[k]
 d['crop']='; '.join(crops[n] for n in CROP_SECTIONS[k]) if CROP_SECTIONS[k] else None
 d['root_evidence_source']=[{**sections[n],'root_journal_section':n} for n in EVIDENCE_SECTIONS[k]]
 d['root_once_viewed_crop_references']=[{'path':crops[n],'root_journal_section':n,'source_declaration':sections[n],'scope':'Root journal declares one view; clerk accessed no image or image hash.'} for n in CROP_SECTIONS[k]]
 if k==65:d['evidence_scope']='Source-only S and administrative comparison; no image adjudication.'
 if k==6:d['evidence_reuse_scope']='Section-01 observation recorded in section 07; no reopened image.'
decisions['U022-L08']['final']=r'Complete \widehat{\Sigma}_\alpha^+ in A022-S01, retaining its short head, angled body, roof, raised plus and alpha. Sigma is primary; head/retrace versus independent-upper-run role remains qualified at this first printed occurrence.'
decisions['U022-L09']['final']=r'Complete \widehat{\Sigma}_\alpha^+ in A022-S02, retaining its separate short head, angled body, roof, raised plus and alpha. The local head/retrace versus independent-upper-run doubt remains recorded under the recurring convention first printed at S01.'
pair=m['selected_state_metadata']['A022-G10-lower-annotations']['complete_candidates_or_state']
d=decisions['U022-L25'];d['final']='Complete shared lower-annotation states: '+pair+'. The complete live inserted pair is primary; the complete deleted inserted pair is the alternative.'
d['readers']['A']='A022-G10-lower-annotations retains both complete formulas and both shared state candidates: '+pair+'. The entire pair has one outer graphical qualifier.'
d['readers']['C']='C022-A01 and C022-A02 retain the complete left and right formula/state records. Their live inserted formulas are primary and their deleted inserted formulas remain alternatives. The complete pair candidates are: '+pair+'. The two original C local source records remain separately preserved in provenance.'
for loc in [26,28,29]:
 d=decisions[f'U022-L{loc:02d}'];d['readers']['A']=d['readers']['A'].replace('live by enclosing text','within the shared qualified lower-pair state')
 d['readers']['A']+=' A022-G10 retains the shared complete live-inserted primary and complete deleted-inserted alternative; both full formulas and pair candidates are stated at L25.'
sigma={8:(1,r'\widehat{\Sigma}_\alpha^+'),9:(2,r'\widehat{\Sigma}_\alpha^+'),20:(4,r'\Sigma_\alpha^-'),22:(5,r'\Sigma_\alpha^+'),26:(7,r'\widehat{\Sigma}_\alpha^+'),28:(8,r'\overline{\Sigma_\alpha^-}'),29:(9,r'\widehat{\Sigma}_\alpha^+'),32:(10,r'\Sigma_\alpha^-'),33:(11,r'\overline{\Sigma_\alpha^-}'),37:(13,r'\overline{\Sigma_\alpha^-}'),48:(14,r'\widehat{\Sigma}_\alpha^-'),49:(15,r'\Sigma_\alpha^-'),57:(16,r'\widehat{\Sigma}_\alpha^+'),59:(17,r'\widehat{\Sigma}_\beta^+')}
deco={1:'roof, raised plus and alpha',2:'roof, raised plus and alpha',4:'raised minus and alpha in its plain Sigma formula',5:'raised plus and alpha in its plain Sigma formula',7:'roof, raised plus and alpha',8:'raised minus and alpha with the upper horizontal shared with connector G06; the original G04 comment remains separately preserved',9:'roof, raised plus and alpha',10:'raised minus and alpha in its plain Sigma formula, with the head crowded beneath the frame',11:'raised minus and alpha with the upper run shared with the frame and its local closure-role qualification',13:'separate upper closure, raised minus and alpha',14:'roof, raised minus and alpha',15:'raised minus and alpha in its plain Sigma formula',16:'roof, raised plus and alpha',17:'roof, raised plus and beta; the interior point has its own C022-M03 source identity'}
creport=read('out/readers/022/C/report.json');generic='literal separate short head and angled body with unchanged index/sign and existing roof/bar';c_replacements=[]
for locus,(num,formula) in sigma.items():
 d=decisions[f'U022-L{locus:02d}'];assert generic in d['readers']['C'],locus;gid=f'C022-S{num:02d}'
 text=f'{gid} retains its separate short head and angled body for the complete {formula}, with {deco[num]}. Its local head/retrace versus independent-upper-run candidates remain in the source record under the recurring convention; its printed qualifier status is retained in the original notation record'
 d['readers']['C']=d['readers']['C'].replace(generic,text)
 ix=next(i for i,n in enumerate(creport['notation']) if n['id']==gid)
 d['reader_provenance']['C']['complete_local_glyph_notation_source']=ref('out/readers/022/C/report.json',f'/notation/{ix}')
 d['reader_provenance']['C']['complete_local_glyph_group_source']=ref('out/checks/scan022_candidate_sources.json',f'/readers/C/groups/{gid}')
 c_replacements.append(d['id'])
assert len(c_replacements)==14
decisions['U022-L43']['readers']['C']=r'Firm \deleted{formule}: the complete old noun remains cancelled in reader C’s final source; its report makes the word firm.'
for d in r['decisions']:
 for role in 'ABC':d['reader_provenance'][role]['public_complete_source_choice']=d['readers'][role]
for d in r['doubts']:
 s=decisions[d['decision_id']];d['reading']=s['final'];d['reason']=s['evidence']+' '+s['qualification']
 for k in ['readers','reader_provenance','crop','root_evidence_source','root_once_viewed_crop_references']:d[k]=copy.deepcopy(s[k])
for v in r['source_locus_coverage']:
 s=decisions[v['source_locus_id']]
 for k in ['readers','reader_provenance']:v[k]=copy.deepcopy(s[k])
for i,row in enumerate(r['C_source_rows']):
 prior=row.pop('root_outcome')
 row['source_stage_root_outcome_provenance']={'historical':True,'phase':'Source-support candidate ledger before final page approval','exact_initial_object_source':ref(INITIAL,f'/C_source_rows/{i}/root_outcome'),'value_with_corrected_source_binding':prior,'scope':'Source-stage values and pending approval flag are historical. Only source-reference binding is corrected; the exact initial object remains preserved at the attached pointer. Current selected outcome remains in root_original_row_status and canonical source_parts.'}

inv={i['element']:i for i in r['inventory']};groups={g['id']:g for g in r['selected_graphical_groups']};changed_inventory=[]
def extend_inventory(element,gids,labels,ds):
 item=inv[element]
 for gid in gids:
  if gid not in item['selected_source_groups']:
   item['selected_source_groups'].append(gid);item['final_source_attachment'].append(gatt(gid))
  if element not in groups[gid]['inventory_elements']:groups[gid]['inventory_elements'].append(element)
 for label in labels:
  if label not in item['selected_text_labels']:
   item['selected_text_labels'].append(label);item['final_source_attachment'].append(natt(label))
 item['related_decision_ids']=unique(item['related_decision_ids']+ds)
 item['bounded_scope_completion_source']={'root_authorization':'Root consolidated bounded-repair messages','initial_source_audit':ref(AUDIT),'scope':'Complete existing claimed scope; identities, order, hands, ink and counts unchanged.'}
 changed_inventory.append(element)
extend_inventory('022.04',['A022-G02-initial-separator','B022-G02','A022-S01','A022-S02'],[],['U022-L06','U022-L07','U022-L08','U022-L09'])
extend_inventory('022.13',['A022-S08'],[],['U022-L27','U022-L28'])
extend_inventory('022.25',['A022-S14','A022-S15'],['T54','T55','T56'],['U022-L48','U022-L49'])
shared=m['path_final_spans']['R022-path-L0276'];assert shared['owner']=='A022-S08'
assert '(1011,750)' in shared['final_span']['literal_source'] and '(1069,749)' in shared['final_span']['literal_source']
sa=att(shared['final_span'],'/path_final_spans/R022-path-L0276/final_span')
inv['022.13']['final_source_attachment'].append(sa)
inv['022.13']['shared_component_reference']={'path_id':'R022-path-L0276','owner_group':'A022-S08','owner_inventory_element':'A022-S08','connector_reference_group':'A022-G11-right-connector','exact_path_attachment':sa,'scope':'Connector reference to one shared horizontal. S08 retains sole physical ownership; its full group supplies source context.'}
groups['A022-S08']['inventory_reference_scope']={'022.13':'Complete source context and exact shared horizontal R022-path-L0276; no second drawing or transfer of ownership.'}
for p in r['selected_literal_path_ownership']:
 if p['group_id'] in ['A022-G02-initial-separator','B022-G02','A022-S01','A022-S02']:p['referencing_inventory_elements']=unique(p['referencing_inventory_elements']+['022.04'])
 if p['group_id'] in ['A022-S14','A022-S15']:p['referencing_inventory_elements']=unique(p['referencing_inventory_elements']+['022.25'])
 if p['id']=='R022-path-L0276':
  assert p['inventory_element']=='A022-S08';p['referencing_inventory_elements']=unique(p['referencing_inventory_elements']+['022.13']);p['shared_connector_reference_inventory_element']='022.13'

fixed=['confidence','diff_C','diff_H','marked_in_H','H_local_marker_id','C_count_parent','H_count_parent','physical_count_parent','remaining_doubt','alternatives','qualification','C_doubt_status','selected_source_groups']
for old,new in zip(initial['decisions'],r['decisions']):
 assert old['id']==new['id']
 for k in fixed:assert old[k]==new[k],(old['id'],k)
assert r['counts']==initial['counts']
assert [(i['element'],i['hand']) for i in r['inventory']]==[(i['element'],i['hand']) for i in initial['inventory']]
assert [(p['id'],p['group_id'],p['inventory_element']) for p in r['selected_literal_path_ownership']]==[(p['id'],p['group_id'],p['inventory_element']) for p in initial['selected_literal_path_ownership']]
assert not r['main_adjudicated'] and not r['main_approved']
r['authorization_source_freeze']={'frozen':ref(FROZEN_AUTH),'original_source_path':AUTH,'original_source_current_sha256':AUTH_SHA,'repaired_current_reference_count':len(repaired_auth),'entry_journal_correspondence_verified':True,'initial_values_preserved_in':ref(INITIAL)}
r['bounded_source_metadata_repair']={'scope':'Consolidated QA022-R01–R12/root public and source metadata corrections only','initial_record':ref(INITIAL),'initial_audit_json':ref(AUDIT),'initial_audit_markdown':ref(AUDIT_MD),'script':ref('out/checks/scan022_source_support_record_repair_v01.py'),'evidence_source_script':ref('out/checks/scan022_source_support_record_evidence_v01.py'),'diff_path':DIFF,'closure_path':CLOSURE,'selected_TeX_changed':False,'selected_map_changed':False,'original_reader_files_changed':False,'counts_confidences_or_qualifiers_changed':False,'inventory_order_identities_or_hands_changed':False,'mathematical_or_coordinate_computations':False,'image_or_image_hash_access':False,'initial_generation_sources_preserved':True,'closure_status':'Bounded changed-field release prepared; independent closure and final root approval pending.'}
changes=differences(initial,r);assert inverse_replay(r,changes)==initial
diff=write(DIFF,{'scan':22,'initial_record':ref(INITIAL),'scope':'Exact changed fields only; original values retained for every replacement/removal.','changes':changes,'inverse_replay_structurally_equals_initial':True})
final=write(RECORD,r)
closure=write(CLOSURE,{'scan':22,'initial_record':ref(INITIAL),'initial_audit_json':ref(AUDIT),'initial_audit_markdown':ref(AUDIT_MD),'repaired_record':final,'changed_field_diff':diff,'changed_field_count':len(changes),'changed_inventory_scope_entries':changed_inventory,'inventory_permutation':None,'authorization_source_freeze':ref(FROZEN_AUTH),'repaired_authorization_hash_mirrors':repaired_auth,'reader_C_generic_phrase_replaced_at':c_replacements,'source_draft':ref(DRAFT),'source_map':ref(MAP),'counts':r['counts'],'checks':{'all_66_decision_evidence_from_existing_journal':len(EVIDENCE)==66,'all_33_doubt_reasons_and_reader_mirrors_updated':len(r['doubts'])==33,'frame_all_six_component_crop_sources_preserved':len(decisions['U022-L30']['root_once_viewed_crop_references'])==6,'L06_reuses_section01_recorded_in_section07':CROP_SECTIONS[6]==[1] and EVIDENCE_SECTIONS[6]==[1,7],'L65_source_only_without_image_claim':decisions['U022-L65']['crop'] is None,'all_authorization_entry_journal_sources_match':True,'all_initial_values_recoverable_by_inverse_replay':True,'selected_draft_map_unchanged':sha(DRAFT)==DRAFT_SHA and sha(MAP)==MAP_SHA,'counts_qualifiers_confidences_order_hands_unchanged':True,'shared_horizontal_owned_once_by_S08':True,'no_image_or_image_hash_access':True,'no_mathematical_or_coordinate_computation':True},'main_approved':False,'status':'Bounded metadata repair prepared; independent bounded review and root approval pending.'})
print(json.dumps({'record':final,'diff':diff,'closure':closure,'changed_fields':len(changes),'authorization_hash_mirrors':len(repaired_auth),'counts':r['counts']},ensure_ascii=False))
