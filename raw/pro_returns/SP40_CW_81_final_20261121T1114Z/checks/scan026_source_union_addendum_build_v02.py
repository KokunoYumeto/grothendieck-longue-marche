"""Read-only input audit and separately named supplements; v01 stays frozen."""
from pathlib import Path
from collections import OrderedDict
import json, hashlib, re
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
sha=lambda b:hashlib.sha256(b).hexdigest()
pack=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))
def read(p):return json.loads((BASE/p).read_bytes())
def save(name,v):
 b=(json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode();(OUT/name).write_bytes(b)
 return {'path':str(OUT/name),'bytes':len(b),'sha256':sha(b)}
union=read('out/checks/scan026_source_union_v01.json')
pool=read('out/checks/scan026_source_union_state_pool_v01.json')
reports={w:read(f'out/readers/026/{w}/report.json') for w in 'ABC'}
maps={w:read(f'out/readers/026/{w}/source_map.json') for w in 'ABC'}
texts={w:(BASE/f'out/readers/026/{w}/reading.tex').read_text() for w in 'ABC'}
before={str(p):sha(p.read_bytes()) for p in OUT.glob('scan026_*union*v01*') if p.is_file()}

def raw_fields(w,ptr,keys):
 v=reports[w]
 for x in ptr.split('/')[1:]:v=v[int(x)] if isinstance(v,list) else v[x]
 return {'raw_ref':{'source':w+'.report','json_pointer':ptr},'exact_fields_in_raw_order':OrderedDict((k,v[k]) for k in v if k in keys)}

c05=next(g for g in maps['C']['groups'] if g['id']=='C026-S05')
hands=[v['hand'] for v in c05['candidate_states']]
hand_classes=[]
for hand in dict.fromkeys(hands):
 hand_classes.append({'exact_hand':hand,'candidate_indexes':[i for i,h in enumerate(hands) if h==hand]})
restored=[None]*len(hands)
for row in hand_classes:
 for i in row['candidate_indexes']:assert restored[i] is None;restored[i]=row['exact_hand']
assert restored==hands and len(hands)==24
c05_notes={'locus_id':'S05','scope':'Literal parent and candidate-local hand wording; no attribution is selected.',
 'raw_fields':[
 raw_fields('C','/inventory/10',['hand']),
 raw_fields('C','/differences/49',['id','qualification']),
 raw_fields('C','/differences/10',['id','candidate_hand']),
 raw_fields('C','/recurring_ring_occurrences/0',['source_group','hand'])],
 'candidate_hand_projection':{'raw_source':'C.map','raw_pointer':'/groups/'+str(maps['C']['groups'].index(c05))+'/candidate_states','field':'hand','exact_classes':hand_classes,'finite_inverse_restores_all_24_hand_fields':True},
 'scope_note':'The independent upper dark trace and the independent short upper run have separate hand phrases in the complete states. The inventory and G-S05 qualification retain their own parent wording, while D09c and the recurring-ring record retain their own local fields.'}

# Clarify punctuation that the v01 prose sentence leaves visually ambiguous.
label_row=next(x for x in union if x['locus_id']=='L047')
label_note={'locus_id':'L047','scope':'Exact existing source qualifier strings; v01 data unchanged.',
 'readers':{w:[s for s in label_row['reader_sources'][w]['local_source_spans'] if 'literal' in s] for w in 'ABC'},
 'literal_first_alternatives':{'A':'i.e.','B':'ie','C':'i.e'}}
for w,first in label_note['literal_first_alternatives'].items():
 assert any(s['literal'].startswith('\\unsure{'+first+'|') for s in label_note['readers'][w])

# An inventory-context link in v01 L005 spans the opening paragraph. Its raw
# position identifies the agreed earlier deletion; preserve that scope here.
intersection={'scope':'The three inventory records associated as broad context with v01 L005 concern the earlier deleted l’intersection before aucune. Their exact raw positions are below; they do not locate that deletion in the later topology clause.',
 'raw_inventory_records':[], 'source_spans':[], 'v01_modified':False}
for w,element in [('A','A026-I02'),('B','B026-DEL01'),('C','DEL01')]:
 i=next(i for i,x in enumerate(reports[w]['inventory']) if x['element']==element)
 intersection['raw_inventory_records'].append(raw_fields(w,'/inventory/'+str(i),list(reports[w]['inventory'][i])))
 literal="\\deleted{l'intersection}";start=texts[w].index(literal);end=start+len(literal)
 intersection['source_spans'].append({'source':w+'.tex','start_char':start,'end_char_exclusive':end,'start_line':texts[w].count('\n',0,start)+1,'literal':literal,'sha256':sha(literal.encode())})

qualifier_coverage={}
for w in 'ABC':
 spans=[s for row in union for s in row['reader_sources'][w]['local_source_spans'] if s['source']==w+'.tex']
 hits=list(re.finditer(r'\\(?:unsure|deleted|inserted|uline|ill)\b',texts[w]))
 outside=[m for m in hits if not any(s['start_char']<=m.start()<s['end_char_exclusive'] for s in spans)]
 assert len(outside)==1 and texts[w][outside[0].start():].startswith("\\deleted{l'intersection}")
 qualifier_coverage[w]={'source_macro_occurrences_including_source_annotations':len(hits),'covered_by_v01_local_spans':len(hits)-1,'additional_exact_common_deletion_span':intersection['source_spans']['ABC'.index(w)]}

addendum={'status':'Source-only supplemental scopes; v01 files stay unchanged. No root review or ink decision is claimed.',
 'C_S05_hand_scopes':c05_notes,'L047_exact_primary_strings':label_note,'earlier_common_deletion_inventory_context':intersection,
 'finite_qualifier_source_coverage':qualifier_coverage}
addendum_file=save('scan026_source_union_scope_addendum_v02.json',addendum)

# Crop metadata provenance only: these are all existing reader records.
# is_file checks the path metadata; no image bytes are read.
crop_directory=[]
for item in pool:
 ref=item['raw_ref']
 if not ref['source'].endswith('.crops'):continue
 w=ref['source'][0]
 value=OrderedDict((f['key'],f['value']) for f in item['ordered_fields'])
 path=BASE/'out/readers/026'/w/value['path']
 assert path.is_file()
 uses=[row['locus_id'] for row in union if item['record_id'] in row['reader_sources'][w]['declared_crop_records']]
 crop_directory.append({'reader':w,'pool_record':item['record_id'],'raw_ref':ref,
  'existing_path':str(path),'declared_bbox':value['bbox'],
  'rotation_fields_in_raw_order':OrderedDict((k,v) for k,v in value.items() if 'rotation' in k or k=='rotation' or k=='rotate_expand'),
  'declared_locus_references_in_v01':uses,
  'scope':'Declared reader metadata, not a newly inspected coverage determination.'})
assert len(crop_directory)==56
crop_file=save('scan026_source_union_crop_directory_v02.json',crop_directory)
chunks=[];chunk=[];size=0
for row in crop_directory:
 line=json.dumps(row,ensure_ascii=False)+'\n';n=len(line.encode())
 if chunk and size+n>8500:chunks.append(chunk);chunk=[];size=0
 chunk.append(line);size+=n
if chunk:chunks.append(chunk)
crop_review=[];recovered=[]
for i,lines in enumerate(chunks,1):
 name=f'scan026_source_union_crop_review_v02_{i:02}.jsonl';b=''.join(lines).encode();(OUT/name).write_bytes(b)
 recovered.extend(json.loads(line) for line in lines)
 crop_review.append({'path':str(OUT/name),'rows':len(lines),'bytes':len(b),'sha256':sha(b)})
assert pack(recovered)==pack(crop_directory)
crop_manifest=save('scan026_source_union_crop_review_manifest_v02.json',{'complete_chunks':crop_review,'exact_parse_concatenation_inverse':True,'full_directory_sha256':crop_file['sha256']})
after={str(p):sha(p.read_bytes()) for p in OUT.glob('scan026_*union*v01*') if p.is_file()}
assert before==after
proof={'v01_file_hashes_unchanged':before==after,'v01_files_checked':len(before),
 'candidate_hand_projection_inverse_exact':True,'all_new_qualifier_source_tokens_mapped':True,
 'unmapped_common_deletion_supplied_as_exact_context_span':True,'crop_metadata_records':len(crop_directory),
 'image_bytes_read':0,'root_crop_choices':0,'root_ink_choices':0,'artifacts':[addendum_file,crop_file,crop_manifest]}
save('scan026_source_union_scope_addendum_proof_v02.json',proof)
print(json.dumps(proof,ensure_ascii=False,indent=2))
