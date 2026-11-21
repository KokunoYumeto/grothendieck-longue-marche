from pathlib import Path
import json, hashlib, collections, sys
BASE=Path('/workspace/scratch/94548b74fbe0/out/checks/notation026_new_review_')
SRC=Path('/workspace/scratch/94548b74fbe0/out/checks/notation026_new_assertions_v01.json')
EXPECTED='16708619cece52654f3fec993aa066bfee267badc7b3f43489987e185211cc6b'
def out(s): return Path(str(BASE)+s)
assert not out('manifest.json').exists(), 'Projection already generated; preserve existing outputs'
def dump(x): return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def full(x): return (json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
def sha(b): return hashlib.sha256(b).hexdigest()
raw=SRC.read_bytes()
assert sha(raw)==EXPECTED
root=json.loads(raw)
assert full(root)==raw, 'Exact source formatting was not reproduced.'
# Type-tagged ordered subtree identity. No object key sorting or scalar coercion.
def freeze(x):
 if isinstance(x,dict):return ('object',tuple((k,freeze(v)) for k,v in x.items()))
 if isinstance(x,list):return ('array',tuple(freeze(v) for v in x))
 return (type(x).__name__,dump(x))
nodes=[];node_seen={}
def visit(x):
 if not isinstance(x,(dict,list)):return ['value',x]
 key=freeze(x)
 if key in node_seen:return ['node',node_seen[key]]
 rec=['object',[[k,visit(v)] for k,v in x.items()]] if isinstance(x,dict) else ['array',[visit(v) for v in x]]
 i=len(nodes);nodes.append(rec);node_seen[key]=i
 return ['node',i]
root_ref=visit(root)
# A member alias is precisely one JSON object grammar member (key and value).
# It is never a patch, replacement, default, union, or reordered record.
member_counts=collections.Counter(dump(p) for typ,vs in nodes if typ=='object' for p in vs)
member_ids={p:i for i,p in enumerate(p for p,n in member_counts.items() if n>1)}
members=[json.loads(p) for p in member_ids]
nodes2=[]
for typ,vs in nodes:
 if typ=='object':vs=[['member',member_ids[dump(p)]] if dump(p) in member_ids else ['inline',p] for p in vs]
 nodes2.append([typ,vs])
# Pool only repeated exact decoded string literals after member/subtree sharing.
string_counts=collections.Counter()
def count_ref(r):
 if r[0]=='value' and isinstance(r[1],str):string_counts[r[1]]+=1
for k,r in members:count_ref(r)
for typ,vs in nodes2:
 if typ=='array':
  for r in vs:count_ref(r)
 else:
  for mode,p in vs:
   if mode=='inline':count_ref(p[1])
strings=[s for s,n in string_counts.items() if n>1 and len(s)>=20]
string_ids={s:i for i,s in enumerate(strings)}
def string_ref(r):
 return ['string',string_ids[r[1]]] if r[0]=='value' and isinstance(r[1],str) and r[1] in string_ids else r
members2=[[k,string_ref(r)] for k,r in members]
nodes3=[]
for typ,vs in nodes2:
 if typ=='array':vs=[string_ref(r) for r in vs]
 else:vs=[[mode,[p[0],string_ref(p[1])] if mode=='inline' else p] for mode,p in vs]
 nodes3.append([typ,vs])
codec={'codec':'exact-ordered-json-dag-v1','source_format':{'encoding':'utf-8','ensure_ascii':False,'indent':2,'trailing_newline':'\n','object_member_order':'stored order','allow_scalar_coercion':False},'source_sha256':sha(raw),'source_byte_length':len(raw),'strings':strings,'members':members2,'nodes':nodes3,'root':root_ref}
out('data.json').write_bytes(full(codec))
def decode(c):
 active=set();cache={}
 def ref(r):
  mode,v=r
  if mode=='value':return v
  if mode=='string':return c['strings'][v]
  assert mode=='node'
  if v in cache:return cache[v]
  assert v not in active, 'cycle';active.add(v)
  typ,vs=c['nodes'][v]
  if typ=='array':ans=[ref(r) for r in vs]
  else:
   pairs=[c['members'][p] if mode=='member' else p for mode,p in vs]
   assert len({k for k,r in pairs})==len(pairs), 'duplicate key'
   ans={k:ref(r) for k,r in pairs}
  active.remove(v);cache[v]=ans;return ans
 return ref(c['root'])
replayed=full(decode(json.loads(out('data.json').read_bytes())))
out('reconstructed.json').write_bytes(replayed)
assert replayed==raw
assert freeze(decode(codec))==freeze(root)
# Exhaustive occurrence paths, including every alias occurrence after expansion.
paths={'node':collections.defaultdict(list),'member':collections.defaultdict(list),'string':collections.defaultdict(list)}
inline_values=0;all_keys=0;types=collections.Counter();source_unique_strings=set();source_unique_keystrings=set()
def ptr(p,k):return p+'/'+str(k).replace('~','~0').replace('/','~1')
def trace(r,p):
 global inline_values,all_keys
 mode,v=r
 if mode in paths:paths[mode][v].append(p)
 if mode=='string':types['str']+=1;source_unique_strings.add(strings[v]);return
 if mode=='value':
  inline_values+=1;types[type(v).__name__]+=1
  if isinstance(v,str):source_unique_strings.add(v)
  return
 typ,vs=nodes3[v];types['dict' if typ=='object' else 'list']+=1
 if typ=='array':
  for i,rr in enumerate(vs):trace(rr,ptr(p,i))
 else:
  for m,pp in vs:
   k,rr=members2[pp] if m=='member' else pp
   q=ptr(p,k);all_keys+=1;source_unique_keystrings.add(k)
   if m=='member':paths['member'][pp].append(q)
   trace(rr,q)
trace(root_ref,'')
with out('paths.jsonl').open('w',encoding='utf-8') as f:
 for typ in ('string','member','node'):
  for i,ps in sorted(paths[typ].items()):f.write(dump({'alias':{'string':'S','member':'M','node':'N'}[typ]+f'{i:04d}','paths':ps})+'\n')
# Human projection is itself machine-decodable: every definition RHS is JSON.
# S values are literal strings. M RHS=[literal key, reference]. N RHS is
# [kind, members/refs]; notation is defined in the reading guide.
# A second, easier-to-read exact projection uses @S/@M/@N references.
def rr(r):
 mode,v=r
 return {'node':'@N','string':'@S'}[mode]+f'{v:04d}' if mode!='value' else dump(v)
def member_text(p):return dump(p[0])+': '+rr(p[1])
def node_text(i,node):
 typ,vs=node;start=f'N{i:04d} = '
 if typ=='array':
  atoms=[rr(r) for r in vs]
  one='['+', '.join(atoms)+']'
  return start+one+'\n' if len(one)<180 else start+'[\n'+''.join('  '+a+(',' if j+1<len(atoms) else '')+'\n' for j,a in enumerate(atoms))+']\n'
 atoms=[f'@M{p:04d}' if mode=='member' else member_text(p) for mode,p in vs]
 one='{'+', '.join(atoms)+'}'
 return start+one+'\n' if len(one)<180 else start+'{\n'+''.join('  '+a+(',' if j+1<len(atoms) else '')+'\n' for j,a in enumerate(atoms))+'}\n'
blocks=[]
blocks.append('EXACT NOTATION026 REVIEW PROJECTION\nEvery S alias is one exact string. Every M alias is one exact ordered JSON member (key:value). Every N alias is one exact ordered object or array subtree. Expand @S/@M/@N recursively, preserving the displayed array/member order. Quoted strings use JSON escaping. Numbers, booleans and null retain their JSON scalar types. Member aliases stand in place of one complete property, never a patch. Empty root JSON pointer is the entire document. This projection adds no notation or ink interpretation.\nROOT = '+rr(root_ref)+'\n\n')
blocks.append('STRING DEFINITIONS\n')
blocks.extend(f'S{i:04d} = {dump(s)}\n' for i,s in enumerate(strings))
blocks.append('\nMEMBER DEFINITIONS\n')
blocks.extend(f'M{i:04d} = {member_text(p)}\n' for i,p in enumerate(members2))
blocks.append('\nORDERED SUBTREE DEFINITIONS\n')
blocks.extend(node_text(i,n) for i,n in enumerate(nodes3))
# No definition is split. 18,000-character files bound ordinary token load.
pages=[];current=''
for block in blocks:
 if current and len(current)+len(block)>18000:pages.append(current);current=''
 current+=block
if current:pages.append(current)
projection_names=[]
for i,page in enumerate(pages,1):
 name=f'projection_{i:02d}.txt';out(name).write_text(page,encoding='utf-8');projection_names.append(out(name).name)
# Verify projection text literals and definitions are complete by their exact
# machine records, independently from reconstructed-source byte comparison.
all_ids=[]
for line in ''.join(pages).splitlines():
 if len(line)>=8 and line[0] in 'SMN' and line[1:5].isdigit() and line[5:8]==' = ':all_ids.append(line[:5])
expected_ids=[f'S{i:04d}' for i in range(len(strings))]+[f'M{i:04d}' for i in range(len(members2))]+[f'N{i:04d}' for i in range(len(nodes3))]
assert all_ids==expected_ids
# Canonical shape equality is independently represented as a type-tagged tree.
# Actual exact byte equality is checked above, not inferred from SHA equality.
manifest={'source':str(SRC),'source_sha256':sha(raw),'expected_sha256':EXPECTED,'expected_sha256_matches':sha(raw)==EXPECTED,'source_byte_length':len(raw),'reconstructed_byte_length':len(replayed),'byte_for_byte_equal':replayed==raw,'ordered_type_tagged_tree_equal':freeze(decode(codec))==freeze(root),'key_order_preserved':True,'source_value_type_counts':dict(types),'source_member_occurrences':all_keys,'unique_source_value_strings':len(source_unique_strings),'unique_source_key_strings':len(source_unique_keystrings),'unique_source_strings_including_keys':len(source_unique_strings|source_unique_keystrings),'string_aliases':len(strings),'member_aliases':len(members2),'subtree_aliases':len(nodes3),'alias_occurrences':{k:sum(len(p) for p in d.values()) for k,d in paths.items()},'all_definition_ids_exactly_once_and_in_order':all_ids==expected_ids,'root_reference':rr(root_ref),'projection_files':projection_names,'projection_total_characters':sum(len(p) for p in pages),'path_map_file':out('paths.jsonl').name,'data_file':out('data.json').name,'reconstructed_file':out('reconstructed.json').name,'projection_build_script':'notation026_new_projection_build_v01.py','projection_file_characters':[len(p) for p in pages],'no_claim_of_root_review':True}
manifest['file_sha256']={name:sha((BASE.parent/name).read_bytes()) for name in projection_names+[out('paths.jsonl').name,out('data.json').name,out('reconstructed.json').name]}
out('manifest.json').write_bytes(full(manifest))
proof='''FINITE FORWARD/INVERSE PROOF\n\nInput is the frozen review-input byte string B. Its UTF-8 JSON parse T keeps the original object insertion order. Direct comparison establishes J(T)=B, where J is Python JSON serialization with ensure_ascii=False, indent=2, and exactly one trailing LF, encoded UTF-8. This compares actual bytes, not object equality or hashes alone.\n\nF traverses finite T. Each object is identified by its complete ordered list of key/value subtrees; each array by its complete ordered child list; each scalar by its exact Python type and exact JSON literal. Repeated equal containers receive one N alias. Each repeated member receives one M alias for its exact key and exact value reference. Selected repeated string literals receive one S alias for the whole exact string. No sorting, trimming, case change, whitespace change inside a string, scalar coercion, default insertion, candidate merging, role assignment, or semantic equivalence is used.\n\nG expands an S alias to its literal string; an M alias to its one literal-key/value member; an N array to its ordered expanded values; and an N object to its ordered expanded members. By induction on each finite node height, G(F(t)) equals t with scalar types and complete key order intact: scalar and string cases are literal identity; array cases preserve each ordinal child; object cases preserve each ordinal key/member and recursively its value. The decoder additionally rejects duplicate keys and cycles. Thus G(F(T))=T as a typed ordered tree.\n\nThe inverse byte map is J after G. The build read codec data back from disk, decoded it, wrote reconstructed.json, and directly compared it with B. Equality held at every byte. Consequently J(G(F(T)))=B for this complete frozen review input. SHA-256 independently identifies the source and reconstructed bytes as 16708619cece52654f3fec993aa066bfee267badc7b3f43489987e185211cc6b.\n\nThe text projection prints every S, M, N definition exactly once, in enumerated order. Every inline scalar literal and every literal key occurs inside a displayed definition. Every root-reachable alias is fully defined inside that same projection. The separate paths.jsonl enumerates all expanded RFC 6901 JSON-pointer occurrence paths of every S/M/N alias, with empty pointer for the root. This mapping is generated by full expansion, retaining all repeated source appearances. It does not collapse repeated candidate occurrences. The manifest records source type counts, complete member/alias counts, projection checksums and byte equality.\n\nREADING ORDER\nRead projection_01.txt through the final numbered projection file. Each file ends on a definition boundary. The first file defines the grammar. S definitions contain pooled whole-string literals; M definitions contain pooled whole members; N definitions preserve complete ordered object/array states. The final N is the review root. Alias IDs have no semantic labels. The complete supplemental rows, states, comparisons, proofs and subsequent status are in these definitions.\n\nNo notation interpretation, ink decision, source-image access, OCR, research, compilation, rendering, or claim of root review was made by this codec.\n'''
out('proof.txt').write_text(proof,encoding='utf-8')
print(json.dumps({k:manifest[k] for k in ['source_sha256','source_byte_length','byte_for_byte_equal','string_aliases','member_aliases','subtree_aliases','alias_occurrences','projection_total_characters','projection_file_characters','root_reference']},ensure_ascii=False,indent=2))
