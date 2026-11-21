"""Reversible review of every locus object; only TeX span metadata is derived."""
from pathlib import Path
import copy,hashlib,json
B=Path('/workspace/scratch/94548b74fbe0');O=B/'out/checks'
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
pack=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))
def span(text,path,a,b,scope):
 return {'path':path,'file_sha256':sha(text),'char_start':a,'char_end':b,
  'utf8_byte_start':len(text[:a].encode()),'utf8_byte_end':len(text[:b].encode()),
  'line_start':text.count('\n',0,a)+1,'line_end':text.count('\n',0,max(a,b-1))+1,
  'literal_sha256':sha(text[a:b]),'scope':scope}
def encode(rows):
 result=copy.deepcopy(rows)
 for row in result:
  row['selected_source_spans']=[{'$tex':[s['char_start'],s['char_end'],s['scope']]} for s in row['selected_source_spans']]
 return result
def decode(rows,path):
 text=(B/path).read_text();result=copy.deepcopy(rows)
 for row in result:
  row['selected_source_spans']=[span(text,path,*s['$tex']) for s in row['selected_source_spans']]
 return result
def save(name,raw):
 p=O/name
 if p.exists():assert p.read_bytes()==raw
 else:p.write_bytes(raw)
 return {'path':str(p.relative_to(B)),'bytes':len(raw),'sha256':sha(raw)}
def chunks(stem,rows):
 result=[];current=[];size=0;start=0
 def flush():
  r=save(f'{stem}_{len(result)+1:02d}.jsonl',b''.join(current));r.update({'first_row_index':start,'rows':len(current)});result.append(r)
 for i,row in enumerate(rows):
  line=(pack(row)+'\n').encode()
  if current and size+len(line)>8500:flush();current=[];size=0;start=i
  current.append(line);size+=len(line)
 if current:flush()
 replay=[json.loads(line) for r in result for line in (B/r['path']).read_text().splitlines()]
 assert pack(replay)==pack(rows)
 return result
def build():
 path='out/checks/scan026_source_selected_contract_v01.json';raw=(B/path).read_text();contract=json.loads(raw)
 assert sha(raw)=='31635052f19c29904453133ad8c18c7607dcb39b9ddbdb4ff45c54905fc0bc5b'
 tex=contract['final_staged_source']['path'];assert sha((B/tex).read_bytes())==contract['final_staged_source']['sha256']
 projected=encode(contract['loci']);decoded=decode(projected,tex)
 assert pack(decoded)==pack(contract['loci']) and pack(encode(decoded))==pack(projected)
 # Restore the exact pretty-printed raw /loci fragment in the frozen contract.
 a=raw.index('  "loci": ')+len('  "loci": ');_,b=json.JSONDecoder().raw_decode(raw,a)
 restored=json.dumps(decoded,ensure_ascii=False,indent=2).replace('\n','\n  ')
 assert restored==raw[a:b]
 locus_chunks=chunks('scan026_source_selected_contract_loci_review_v01',projected)
 files=[];file_indices={};index=[]
 for r in contract['reference_table']:
  if r['path'] not in file_indices:
   file_indices[r['path']]=len(files);files.append({'path':r['path'],'sha256':r['file_sha256']})
  index.append([r['reference_id'],file_indices[r['path']],r['json_pointer']])
 reconstructed_index=[{'reference_id':rid,'path':files[fi]['path'],'json_pointer':ptr} for rid,fi,ptr in index]
 expected=[{k:r[k] for k in ['reference_id','path','json_pointer']} for r in contract['reference_table']]
 assert pack(reconstructed_index)==pack(expected)
 ref_chunks=chunks('scan026_source_selected_contract_reference_review_v01',index)
 manifest={'scope':'All91 /loci objects, every field and field order, with only97 TeX span metadata objects represented by their exact character bounds and scope. The reference index maps every J ID to its exact frozen file and JSON pointer; full raw-span metadata remains in the bound contract.',
  'contract_path':path,'contract_sha256':sha(raw),'final_source':contract['final_staged_source'],
  'decoder':'out/checks/scan026_source_selected_contract_review_v01.py: decode',
  'locus_chunks':locus_chunks,'reference_files':files,'reference_chunks':ref_chunks,
  'target_raw_loci_fragment':{'char_start':a,'char_end':b,'sha256':sha(raw[a:b])},
  'all91_decoded_locus_objects_and_key_order_exact':True,'raw_loci_fragment_restored_byte_exact':True,
  'projection_encode_decode_encode_exact':True,'all364_reference_index_rows_exact':True,
  'selected_state_values_referenced_without_rewriting':True,'source_content_changed':False}
 save('scan026_source_selected_contract_review_manifest_v01.json',(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode())
 print(json.dumps({'locus_chunks':locus_chunks,'reference_chunks':ref_chunks,'reference_files':len(files),'all91_loci_inverse_exact':True},ensure_ascii=False,indent=2))
if __name__=='__main__':build()
