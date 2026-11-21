from pathlib import Path
import json,hashlib
base=Path('/workspace/scratch/94548b74fbe0');checks=base/'out/checks';r=json.loads((checks/'scan023_record_draft.json').read_text());replacements=[];blocks=[]
for d in r['decisions']:
 lines=[f"## {d['id']} — {d['location']}"]
 for k in ('C','H','final','alternatives','evidence','qualification','confidence','kind','diff_C','diff_H','physical_count_parent','marked_in_H','H_marker_ids','H_marker_basis','C_doubt_status','C_source_row_ids','C_source_part_ids','selected_group_ids','inventory_ids','mathematical_consequence','S_id','S_status','root_ink_choice_applied','root_source_audit_choice_applied'):
  if k in d:lines.append(k+': '+(d[k] if isinstance(d[k],str) else json.dumps(d[k],ensure_ascii=False)))
 for role,value in d['readers'].items():
  original=value
  for ref in d.get('reader_source_details',{}).get(role,{}).get('actual_complete_source_spans',[]):
   path=base/ref['path'];text=path.read_text();a,z=ref['char_start_zero_based'],ref['char_end_exclusive'];literal=text[a:z]
   assert hashlib.sha256(path.read_bytes()).hexdigest()==ref['sha256_utf8']
   assert literal==ref['literal']
   needle=literal.rstrip()
   if needle and needle in value:
    token=f"[EXACT ALREADY-READ TEX: {ref['path']} chars[{a},{z}); SHA {hashlib.sha256(literal.encode()).hexdigest()}]"
    before=value;value=value.replace(needle,token)
    replacements.append({'decision':d['id'],'role':role,'source':ref,'needle':needle,'token':token,'count':before.count(needle)})
  restored=value
  for x in reversed([x for x in replacements if x['decision']==d['id'] and x['role']==role]):restored=restored.replace(x['token'],x['needle'])
  assert restored==original,(d['id'],role)
  lines.append('Reader '+role+': '+value)
 blocks.append('\n\n'.join(lines)+'\n')
parts=[];current=''
for b in blocks:
 if current and len(current)+len(b)>19000:parts.append(current);current=''
 current+=b
if current:parts.append(current)
for i,text in enumerate(parts,1):(checks/f'scan023_root_public_decisions_{i:02d}.md').write_text(text)
manifest={'source_record_sha256':hashlib.sha256((checks/'scan023_record_draft.json').read_bytes()).hexdigest(),'scope':'Current public fields remain verbatim. Exact already-read reader TeX spans alone are replaced in this root review projection by reversible source tokens. The record and public output are unchanged.','replacements':replacements,'parts':[{'path':f'out/checks/scan023_root_public_decisions_{i:02d}.md','characters':len(text),'sha256':hashlib.sha256(text.encode()).hexdigest()} for i,text in enumerate(parts,1)]}
(checks/'scan023_root_record_projection_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'parts':manifest['parts'],'exact_replacements':len(replacements)},ensure_ascii=False))
