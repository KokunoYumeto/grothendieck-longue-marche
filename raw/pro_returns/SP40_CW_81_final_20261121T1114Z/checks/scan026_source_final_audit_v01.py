"""Lexical/source audit only: no compilation, rendering, image reads or edits."""
from pathlib import Path
from collections import Counter
import hashlib,json,re
B=Path('/workspace/scratch/94548b74fbe0');O=B/'out/checks'
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
TEX='out/checks/scan026_source_sections01_27_proposal_v01.tex';raw=(B/TEX).read_bytes();P=raw.decode()
assert sha(raw)=='318b043580aba18b302169e52d7c3570208e8211cc7f32f8828cc070ee743615'
C=json.loads((O/'scan026_source_selected_contract_v01.json').read_text())
M=json.loads((O/'scan026_source_sections01_27_proposal_v01_map.json').read_text())
def mask_comments(text):
 result=[];ranges=[];offset=0
 for line in text.splitlines(keepends=True):
  for i,ch in enumerate(line):
   if ch!='%':continue
   j=i-1
   while j>=0 and line[j]=='\\':j-=1
   if (i-j-1)%2==0:
    end=len(line.rstrip('\r\n'));ranges.append([offset+i,offset+end]);line=line[:i]+' '*(end-i)+line[end:];break
  result.append(line);offset+=len(line)
 out=''.join(result);assert len(out)==len(text)
 return out,ranges
clean,comments=mask_comments(P)
def escaped(text,i):
 j=i-1
 while j>=0 and text[j]=='\\':j-=1
 return (i-j-1)%2==1
stack=[];pairs=0
for i,ch in enumerate(clean):
 if escaped(clean,i):continue
 if ch=='{':stack.append(i)
 elif ch=='}':assert stack,('unmatched close',i);stack.pop();pairs+=1
assert not stack
environments=Counter();env=[];env_pairs=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
 action,name=m.group(1),m.group(2)
 if action=='begin':env.append((name,m.start()));environments[name]+=1
 else:
  assert env and env[-1][0]==name,(name,env);opening=env.pop();env_pairs.append([name,opening[1],m.start()])
assert not env
dollars=[i for i,ch in enumerate(clean) if ch=='$' and not escaped(clean,i)];assert len(dollars)%2==0
assert '$$' not in clean
display=[];display_pairs=[]
for m in re.finditer(r'\\([\[\]])',clean):
 if m.group(1)=='[':display.append(m.start())
 else:assert display;display_pairs.append([display.pop(),m.end()])
assert not display
for a,b in display_pairs:assert not re.search(r'\n[ \t]*\n',P[a:b])
token_re=re.compile(r'\\([A-Za-z@]+|.)');tokens=list(token_re.finditer(clean));macro_counts=Counter(m.group(1) for m in tokens)
reader_hashes={};known=set()
expected={'A':'c5079dace4d580a4695749bb745d382e3828681f98e8c037785fc6ac985b5513',
 'B':'1c36f765e58e84962435ac4afe055eb55e561b9f6927f8d09cc139d0562e7289',
 'C':'7c05f3fc0f28985e2cd66c3fbe6486eaf7d38ab20a4a2f7fbf29b1742868b951'}
for w in 'ABC':
 data=(B/f'out/readers/026/{w}/reading.tex').read_bytes();reader_hashes[w]=sha(data);assert reader_hashes[w]==expected[w]
 code,_=mask_comments(data.decode());known.update(m.group(1) for m in token_re.finditer(code))
new_tokens=sorted(set(macro_counts)-known);assert not new_tokens
groups=[]
for gid,g in C['source_group_registry'].items():
 s=g['final_source'];a,b=s['char_start'],s['char_end']
 assert sha(P[a:b])==s['literal_sha256']
 assert P.count('% BEGIN '+gid+'\n')==P.count('% END '+gid+'\n')==1
 contained=[other['final_source'] for other_id,other in C['source_group_registry'].items() if other_id!=gid and a<=other['final_source']['char_start'] and other['final_source']['char_end']<=b]
 total=Counter(m.group(1) for m in tokens if a<=m.start()<b)
 direct=Counter(m.group(1) for m in tokens if a<=m.start()<b and not any(q['char_start']<=m.start()<q['char_end'] for q in contained))
 groups.append({'group':gid,'char_start':a,'char_end':b,'begin_count':1,'end_count':1,
  'direct_literal_primitives':{k:direct[k] for k in ['draw','fill','path','coordinate','node']},
  'including_nested_group_primitives':{k:total[k] for k in ['draw','fill','path','coordinate','node']}})
assert len(groups)==71
named_sigmas=[g['group'] for g in groups if re.fullmatch(r'A026-S\d{2}',g['group'])];assert len(named_sigmas)==37
sigma_rows=[r for r in C['loci'] if r['locus_id'].startswith('S')];assert len(sigma_rows)==39
for r in sigma_rows:
 assert len(r['selected_source_spans'])==1
 if r['locus_id'] in ['S15','S16']:assert r['selected_source_groups']==['B026-DIAG']
 else:assert r['selected_source_groups']==['A026-'+r['locus_id']]
literal_checks={
 'root_new_fleck':r'\fill[gray] (0,0) ellipse (1.3 and 1.5);',
 'diagram_detached_point':r'\fill(2,2)circle(1.1);',
 'adjective_point_one':r'\fill (8,3) ellipse (1.3 and 1.3);',
 'adjective_point_two':r'\fill (3,10) ellipse (1.3 and 1.3);',
 'final_low_left_slant':r'\draw[line width=0.25pt,draw=gray] (7,7) -- (9,11);',
 'final_relation_point':r'\fill (43,26) ellipse (1 and 1);',
 'definition_raised_point':r'\fill (634,2260) ellipse (0.8 and 1.2);',
 'S22_first_body_fragment':r'\draw[line width=.35pt,line cap=round,line join=round] (1418,1738) -- (1441,1743);',
 'S22_second_body_fragment':r'\draw[line width=.35pt,line cap=round,line join=round] (1445,1749) -- (1419,1767) -- (1453,1767);',
 'S14_baseline_comma':r'\draw[line width=.25pt,black!50] (567,1491) .. controls (571,1499) and (569,1508) .. (563,1515);'}
occurrences=[]
for name,literal in literal_checks.items():
 assert clean.count(literal)==1,(name,clean.count(literal));at=clean.index(literal)
 occurrences.append({'component':name,'literal':literal,'count':1,'char_start':at,'char_end':at+len(literal)})
removed=['A026-D01','A026-M01','A026-M03','A026-G15','A026-M04']
assert all(P.count('% BEGIN '+gid+'\n')==0 for gid in removed)
# The complete forward splice and inverse use the immutable A bytes.
A=(B/'out/readers/026/A/reading.tex').read_text();pieces=[];cursor=0
for e in M['literal_replacements']:
 a,b=e['base_char_start'],e['base_char_end'];assert A[a:b]==e['before'];pieces.extend([A[cursor:a],e['replacement']]);cursor=b
pieces.append(A[cursor:]);assert ''.join(pieces)==P
inverse=P
for e in reversed(M['literal_replacements']):
 a,b=e['proposal_char_start'],e['proposal_char_end'];assert inverse[a:b]==e['replacement'];inverse=inverse[:a]+e['before']+inverse[b:]
assert inverse==A
audit={'scope':'Lexical/source checks only; source TeX and all readers remain unchanged.',
 'source':{'path':TEX,'sha256':sha(raw),'bytes':len(raw)},'reader_hashes':reader_hashes,
 'source_brace_pairs':pairs,'brace_stack_empty':True,'environment_counts':dict(environments),'environment_stack_empty':True,
 'dollar_delimiters':len(dollars),'sequential_dollar_pairs':len(dollars)//2,'display_spans':display_pairs,
 'physical_blank_lines_outside_displays':True,'comment_ranges_masked':len(comments),
 'literal_macro_token_counts':dict(sorted(macro_counts.items())),'macro_names_absent_from_all_frozen_readers':new_tokens,
 'macro_scope':'Lexical token names and counts; frozen-reader containment is verified. No TeX execution is performed.',
 'source_groups':groups,'source_group_count':71,'named_A_Sigma_groups':37,'diagram_component_Sigmas':2,'physical_Sigma_loci':39,
 'specific_literal_component_occurrences':occurrences,'removed_original_group_markers':removed,
 'complete_splice_count':len(M['literal_replacements']),'forward_source_exact':True,'inverse_restores_exact_frozen_A':True,
 'compiled':False,'rendered':False,'images_read':0,'root_flags_chosen':0}
body=(json.dumps(audit,ensure_ascii=False,indent=2)+'\n').encode();path=O/'scan026_source_final_audit_v01.json'
if path.exists():assert path.read_bytes()==body
else:path.write_bytes(body)
print(json.dumps({'path':str(path.relative_to(B)),'sha256':sha(body),'bytes':len(body),'brace_pairs':pairs,
 'environments':dict(environments),'macro_names':len(macro_counts),'groups':71,'specific_components_once':len(occurrences),
 'all39_source_splices_forward_inverse_exact':True,'all_assertions_passed':True},ensure_ascii=False,indent=2))
