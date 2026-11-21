"""Reversible source-only splice helper for explicit root-journal proposals.

No entry point runs on import. Call stage(plan, output_stem) only after the plan
has exact authority spans and source edits. Outputs remain scan026_source_*.
This helper neither selects an edit nor writes root/final/committed files.
"""
from pathlib import Path
import copy, hashlib, json

BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
pretty=lambda v:(json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()

def checked_text(ref):
 path=ref['path'];p=Path(path)
 if not p.is_absolute():p=BASE/p
 assert p.resolve().is_relative_to(BASE)
 b=p.read_bytes();assert sha(b)==ref['sha256'],('source hash changed',path)
 t=b.decode();a,c=ref['char_start'],ref['char_end'];assert 0<=a<=c<=len(t)
 literal=t[a:c]
 if 'literal' in ref:assert ref['literal']==literal
 if 'body_sha256' in ref:assert ref['body_sha256']==sha(literal)
 if 'utf8_byte_start' in ref:assert ref['utf8_byte_start']==len(t[:a].encode())
 if 'utf8_byte_end' in ref:assert ref['utf8_byte_end']==len(t[:c].encode())
 return literal

def exact(path,text,a,b):
 return {'path':path,'sha256':sha(text),'char_start':a,'char_end':b,
  'utf8_byte_start':len(text[:a].encode()),'utf8_byte_end':len(text[:b].encode()),
  'line_start':text.count('\n',0,a)+1,'line_end':text.count('\n',0,max(a,b-1))+1,
  'body_sha256':sha(text[a:b]),'literal':text[a:b]}

def authority(ref):
 relative=str(Path(ref['path']).relative_to(BASE)) if Path(ref['path']).is_absolute() else ref['path']
 direct=relative.startswith('out/checks/scan026_root_')
 snapshot=relative.startswith('out/checks/scan026_source_authority_')
 assert direct or snapshot,('root authority or exact captured root source required',relative)
 assert relative.endswith(('.md','.json','.jsonl','.txt'))
 value=checked_text(ref);assert value.strip(),'empty authority span'
 if snapshot:
  original=ref['original_root_path'];assert original.startswith('out/checks/scan026_root_')
  assert ref['original_root_sha256_at_capture']==ref['sha256'],'snapshot must be a byte-exact complete root-file capture'
  current=(BASE/original).read_text()
  if 'original_json_pointer' in ref:
   obj=json.loads(current)
   for token in ref['original_json_pointer'].split('/')[1:]:
    token=token.replace('~1','/').replace('~0','~');obj=obj[int(token)] if isinstance(obj,list) else obj[token]
   assert json.dumps(obj,ensure_ascii=False,separators=(',',':'))==json.dumps(json.loads(value),ensure_ascii=False,separators=(',',':')),'root authority value changed'
  else:
   assert current[ref['char_start']:ref['char_end']]==value,'root authority text span changed'
 return copy.deepcopy(ref)

def boundary(text,p):
 return {'char_offset':p,'preceding_character':text[p-1:p],'following_character':text[p:p+1],
  'preceding_last_utf8_byte_hex':text[:p].encode()[-1:].hex(),
  'following_first_utf8_byte_hex':text[p:].encode()[:1].hex(),
  'preceding_local_source':text[max(0,p-100):p],'following_local_source':text[p:p+100]}

def source_proposal(plan):
 """Apply supplied literal spans in memory; return exact reversible evidence."""
 base=plan['base'];base_path=base['path'];p=Path(base_path)
 if not p.is_absolute():p=BASE/p
 raw=p.read_bytes();assert sha(raw)==base['sha256'];text=raw.decode()
 assert base_path in ['out/readers/026/A/reading.tex','out/checks/scan026_source_A_spine_v01.tex'],base_path
 assert base['sha256']=='c5079dace4d580a4695749bb745d382e3828681f98e8c037785fc6ac985b5513'
 edits=[]
 for original in plan['edits']:
  e=copy.deepcopy(original);a,b=e['base_char_start'],e['base_char_end']
  assert 0<=a<=b<=len(text)
  assert e['before']==text[a:b],(e['edit_id'],'before literal mismatch')
  assert e['root_authority_refs'],(e['edit_id'],'root authority is required')
  e['root_authority_refs']=[authority(r) for r in e['root_authority_refs']]
  pieces=[];piece_map=[];pos=0
  for piece in e['replacement_pieces']:
   assert ('source' in piece)^('literal' in piece)
   if 'source' in piece:
    source=piece['source'];rel=source['path']
    assert rel.startswith(('out/readers/026/','out/checks/scan026_source_')) and rel.endswith('.tex')
    value=checked_text(source);binding={'kind':'exact_donor_source','source':copy.deepcopy(source)}
   else:
    assert piece.get('purpose') and piece.get('root_authority_refs')
    value=piece['literal'];assert isinstance(value,str)
    binding={'kind':'explicit_authorized_literal','literal':value,'purpose':piece['purpose'],
             'root_authority_refs':[authority(r) for r in piece['root_authority_refs']]}
   binding.update(replacement_char_start=pos,replacement_char_end=pos+len(value),body_sha256=sha(value))
   pos+=len(value);pieces.append(value);piece_map.append(binding)
  e['replacement']=''.join(pieces);e['piece_map']=piece_map
  e['original_source']=exact(base_path,text,a,b);edits.append(e)
 edits.sort(key=lambda e:(e['base_char_start'],e['base_char_end']))
 assert len({e['edit_id'] for e in edits})==len(edits)
 for left,right in zip(edits,edits[1:]):
  assert left['base_char_end']<=right['base_char_start'],('overlapping explicit edits',left['edit_id'],right['edit_id'])
  assert not (left['base_char_start']==left['base_char_end']==right['base_char_start']==right['base_char_end']),('two insertions require one explicit order',left['edit_id'],right['edit_id'])
 pieces=[];partition=[];cursor=position=0
 for e in edits:
  a,b=e['base_char_start'],e['base_char_end']
  if cursor<a:
   literal=text[cursor:a];pieces.append(literal)
   partition.append({'kind':'unchanged_A','original_source':exact(base_path,text,cursor,a),'proposal_char_start':position,'proposal_char_end':position+len(literal)})
   position+=len(literal)
  literal=e['replacement'];pieces.append(literal);e['proposal_char_start']=position;e['proposal_char_end']=position+len(literal)
  partition.append({'kind':'explicit_root_authorized_source_edit','edit_id':e['edit_id'],'proposal_char_start':position,'proposal_char_end':position+len(literal)})
  position+=len(literal);cursor=b
 if cursor<len(text):
  literal=text[cursor:];pieces.append(literal)
  partition.append({'kind':'unchanged_A','original_source':exact(base_path,text,cursor,len(text)),'proposal_char_start':position,'proposal_char_end':position+len(literal)})
 proposal=''.join(pieces)
 inverse=proposal
 for e in reversed(edits):
  a,b=e['proposal_char_start'],e['proposal_char_end'];assert inverse[a:b]==e['replacement']
  inverse=inverse[:a]+e['before']+inverse[b:]
 assert inverse.encode()==raw
 for e in edits:e['actual_proposal_boundaries']={k:boundary(proposal,e['proposal_char_'+k]) for k in ['start','end']}
 return proposal,{'schema':'scan026-explicit-source-proposal-v1','base':copy.deepcopy(base),'base_bytes':len(raw),
  'source_only':True,'main_adjudicated':False,'main_approved':False,'root_approval_claimed':False,
  'literal_replacements':edits,'complete_proposal_partition':partition,
  'forward_and_inverse_restore_exact_A_bytes':True,'proposal_sha256_utf8':sha(proposal),
  'root_crop_choices':0,'image_bytes_read':0,'automatic_candidate_or_hand_changes':0,
  'scope':'Only the supplied source edits are applied. Exact authority references are retained for root review; this helper does not decide their ink meaning.'}

def stage(plan,output_stem):
 assert output_stem.startswith('scan026_source_') and '/' not in output_stem and '..' not in output_stem
 proposal,mapping=source_proposal(plan)
 tex_name=output_stem+'.tex';map_name=output_stem+'_map.json'
 mapping['proposal_path']='out/checks/'+tex_name
 for e in mapping['literal_replacements']:
  e['proposal_source']=exact(mapping['proposal_path'],proposal,e['proposal_char_start'],e['proposal_char_end'])
 for part in mapping['complete_proposal_partition']:
  part['proposal_source']=exact(mapping['proposal_path'],proposal,part['proposal_char_start'],part['proposal_char_end'])
 payloads=[(tex_name,proposal.encode()),(map_name,pretty(mapping))]
 for name,body in payloads:
  path=OUT/name
  if path.exists():assert path.read_bytes()==body,('immutable proposal already differs',name)
  else:path.write_bytes(body)
 return {'proposal_path':str(OUT/tex_name),'proposal_sha256':sha(proposal),'map_path':str(OUT/map_name),'map_sha256':sha(pretty(mapping))}
