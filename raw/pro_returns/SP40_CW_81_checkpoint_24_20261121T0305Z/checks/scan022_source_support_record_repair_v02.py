"""Two root-authorized reader-C wording corrections; exact current mirrors."""
from pathlib import Path
import copy,hashlib,json
BASE=Path('/workspace/scratch/94548b74fbe0')
RECORD='out/checks/scan022_record_draft.json'
PRIOR='out/checks/scan022_record_bounded_v01_release/scan022_record_draft.json'
SHA='a76a497a924697010554ac5e7f671e0f3d0134acabf419d62591b8e5266eaab2'
DIFF='out/checks/scan022_record_bounded_public_diff_v02.json'
CLOSURE='out/checks/scan022_record_bounded_public_closure_v02.json'
def sha(p):return hashlib.sha256((BASE/p).read_bytes()).hexdigest()
def ref(p):return {'path':p,'sha256':sha(p)}
def write(p,v):
 (BASE/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');return ref(p)
assert sha(RECORD)==SHA
prior_bytes=(BASE/RECORD).read_bytes();(BASE/PRIOR).parent.mkdir(parents=True,exist_ok=True)
if (BASE/PRIOR).exists():assert (BASE/PRIOR).read_bytes()==prior_bytes
else:(BASE/PRIOR).write_bytes(prior_bytes)
old=json.loads(prior_bytes);r=copy.deepcopy(old);changes=[]
def parent_for(value,p):
 bits=p.split('/')[1:]
 for bit in bits[:-1]:
  bit=bit.replace('~1','/').replace('~0','~');value=value[int(bit)] if isinstance(value,list) else value[bit]
 key=bits[-1].replace('~1','/').replace('~0','~');return value,int(key) if isinstance(value,list) else key
def assign(p,new):
 parent,key=parent_for(r,p)
 if key in parent:
  previous=copy.deepcopy(parent[key])
  if previous==new:return
  changes.append({'op':'replace','path':p,'old':previous,'new':copy.deepcopy(new)})
 else:changes.append({'op':'add','path':p,'new':copy.deepcopy(new)})
 parent[key]=copy.deepcopy(new)

left=r'\overline V\cap\widehat{\Sigma}_\alpha^+'
right=r'\overline{\Sigma_\alpha^-}\cap\widehat{\Sigma}_\alpha^+'
c25=(r'C022-A01 has its own outer qualifier over the complete local alternatives '
     +r'\inserted{'+left+r'} (live inserted primary) | \deleted{\inserted{'+left+r'}} (deleted inserted alternative). '
     +r'C022-A02 has its own separate outer qualifier over the complete local alternatives '
     +r'\inserted{'+right+r'} (live inserted primary) | \deleted{\inserted{'+right+r'}} (deleted inserted alternative). '
     +'These remain two separately qualified source formula records.')
c32=(r'C022-S10 retains the complete \Sigma_\alpha^- with its head and angled-body paths, minus and alpha. '
     +'Its source comment states that the upper head lies immediately below the crossing frame and exact joining is crowded.')
for sid,text in [('U022-L25',c25),('U022-L32',c32)]:
 for field,idkey in [('decisions','id'),('doubts','decision_id'),('source_locus_coverage','source_locus_id')]:
  index=next(i for i,v in enumerate(r[field]) if v[idkey]==sid)
  assign(f'/{field}/{index}/readers/C',text)
  assign(f'/{field}/{index}/reader_provenance/C/public_complete_source_choice',text)
assert len(changes)==12
assign('/bounded_source_metadata_repair/followup_closure_path',CLOSURE)

# Every other existing value remains from the frozen v01 release.
replayed=copy.deepcopy(r)
for c in reversed(changes):
 parent,key=parent_for(replayed,c['path'])
 if c['op']=='add':del parent[key]
 else:parent[key]=copy.deepcopy(c['old'])
assert replayed==old
assert r['counts']==old['counts'] and r['inventory']==old['inventory']
for a,b in zip(old['decisions'],r['decisions']):
 for key in ['final','confidence','alternatives','qualification','evidence','crop','diff_C','diff_H','marked_in_H','C_count_parent','H_count_parent']:
  assert a.get(key)==b.get(key),(a['id'],key)
 assert a['readers']['A']==b['readers']['A'] and a['readers']['B']==b['readers']['B']
assert r['selected_graphical_groups']==old['selected_graphical_groups']
assert r['selected_literal_path_ownership']==old['selected_literal_path_ownership']
assert not r['main_adjudicated'] and not r['main_approved']
diff=write(DIFF,{'scan':22,'prior_record':ref(PRIOR),'scope':'Only L25/L32 current public C readings and their exact mirrors; one followup-closure pointer.','changes':changes,'inverse_replay_restores_prior_object':True})
record=write(RECORD,r)
closure=write(CLOSURE,{'scan':22,'prior_record':ref(PRIOR),'repaired_record':record,'changed_field_diff':diff,'changed_field_count':len(changes),'public_string_changes':12,'public_source_scopes':['U022-L25 reader C: two separately qualified complete local formula alternatives','U022-L32 reader C: exact crowded-joining source scope'],'authority':'Root confirmed exact immutable C reading.tex 166–282 and authorized these two bounded corrections after qa022 comparison.','initial_source_scope':'C022-A01/A02 original outer qualifiers and C022-S10 crowded-joining comment remain unchanged.','script':ref('out/checks/scan022_source_support_record_repair_v02.py'),'prior_closure':ref('out/checks/scan022_record_bounded_public_closure_v01.json'),'historical_path_correspondence':{'original_v01_record_path':RECORD,'original_v01_record_sha256':SHA,'immutable_preserved_copy':PRIOR},'checks':{'forward_changed_fields_applied':True,'inverse_replay_restores_prior_object':True,'selected_A_shared_pair_unchanged':True,'complete_selected_final_states_unchanged':True,'evidence_crop_confidence_count_and_qualifier_fields_unchanged':True,'inventory_order_identities_hands_and_attachments_unchanged':True,'all_graphical_and_literal_path_ownership_unchanged':True,'source_TeX_and_map_unchanged':True,'no_image_or_image_hash_access':True,'no_mathematical_or_coordinate_computation':True},'counts':r['counts'],'main_approved':False,'status':'Two bounded source-reading corrections prepared; independent closure and root approval pending.'})
print(json.dumps({'record':record,'diff':diff,'closure':closure,'prior_record':ref(PRIOR),'changed_fields':len(changes),'new_public_C_L25':c25,'new_public_C_L32':c32},ensure_ascii=False))
