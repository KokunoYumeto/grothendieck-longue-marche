"""Complete15-context review: all context values unchanged and reversible."""
from pathlib import Path
import json,runpy,sys
sys.dont_write_bytecode=True
B=Path('/workspace/scratch/94548b74fbe0');O=B/'out/checks'
api=runpy.run_path(str(O/'scan026_source_selected_contract_review_v01.py'))
source='out/checks/scan026_source_context_inventory_v01.json';text=(B/source).read_text();data=json.loads(text)
assert api['sha'](text)=='c068db61d244780140694ad776412aaf6946af51a1d9cbcb6693684c9c7f3819'
rows=data['contexts'];chunks=api['chunks']('scan026_source_context_inventory_review_v01',rows)
restored=[json.loads(line) for chunk in chunks for line in (B/chunk['path']).read_text().splitlines()]
assert api['pack'](restored)==api['pack'](rows)
a=text.index('  "contexts": ')+len('  "contexts": ');_,b=json.JSONDecoder().raw_decode(text,a)
raw_fragment=json.dumps(restored,ensure_ascii=False,indent=2).replace('\n','\n  ')
assert raw_fragment==text[a:b]
P=(B/data['selected_source']['path']).read_text();cursor=0;parts=[]
for entry in data['complete_source_partition']:
 s=entry['source'];assert s['char_start']==cursor;literal=P[s['char_start']:s['char_end']]
 assert api['sha'](literal)==s['literal_sha256'];parts.append(literal);cursor=s['char_end']
assert cursor==len(P) and ''.join(parts)==P
manifest={'scope':'Every field of all15 context objects, in original order. All262 inventory bindings remain unchanged in the bound supplement.',
 'source':source,'source_sha256':api['sha'](text),'selected_source':data['selected_source'],
 'context_chunks':chunks,'raw_context_fragment':{'char_start':a,'char_end':b,'sha256':api['sha'](text[a:b])},
 'complete_source_partition':data['complete_source_partition'],'raw_inventory_files':data['raw_inventory_files'],
 'coverage_proof':data['coverage_proof'],'all15_context_objects_and_key_order_exact':True,
 'raw_context_fragment_reconstructed_byte_exact':True,'complete_8_segment_source_concat_byte_exact':True,
 'new_hand_assignments':0,'new_ink_classifications':0,'source_content_changed':False}
api['save']('scan026_source_context_inventory_review_manifest_v01.json',(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode())
print(json.dumps({'chunks':chunks,'all15_contexts_inverse_exact':True,'complete_8_segment_source_concat_exact':True},ensure_ascii=False,indent=2))
