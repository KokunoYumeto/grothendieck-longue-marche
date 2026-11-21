"""Complete selected-source context inventory, retaining raw reader inventory scopes."""
from pathlib import Path
import hashlib,json,re
B=Path('/workspace/scratch/94548b74fbe0');O=B/'out/checks'
sha=lambda x:hashlib.sha256(x.encode() if isinstance(x,str) else x).hexdigest()
TEX='out/checks/scan026_source_sections01_27_proposal_v01.tex';P=(B/TEX).read_text();assert sha(P)=='318b043580aba18b302169e52d7c3570208e8211cc7f32f8828cc070ee743615'
C=json.loads((O/'scan026_source_selected_contract_v01.json').read_text());loci={r['locus_id']:r for r in C['loci']}
U=json.loads((O/'scan026_source_union_v01.json').read_text());pool=json.loads((O/'scan026_source_union_state_pool_v01.json').read_text())
pool_ref={(r['raw_ref']['source'],r['raw_ref']['json_pointer']):r['record_id'] for r in pool}
reports={w:json.loads((B/f'out/readers/026/{w}/report.json').read_text()) for w in 'ABC'}
maps=json.loads((O/'scan026_source_sections01_27_proposal_v01_map.json').read_text())
def sref(a,b,scope,path=TEX,text=P):
 return {'path':path,'file_sha256':sha(text),'char_start':a,'char_end':b,
  'utf8_byte_start':len(text[:a].encode()),'utf8_byte_end':len(text[:b].encode()),
  'line_start':text.count('\n',0,a)+1,'line_end':text.count('\n',0,max(a,b-1))+1,
  'literal_sha256':sha(text[a:b]),'scope':scope}
def group(gid):
 s=C['source_group_registry'][gid]['final_source'];return s['char_start'],s['char_end']
def exact(literal,scope):
 assert P.count(literal)==1,(scope,P.count(literal));a=P.index(literal);return sref(a,a+len(literal),scope)
def inventory_ref(w,i):
 r=reports[w]['inventory'][i]
 return {'reader':w,'report_file':f'out/readers/026/{w}/report.json','json_pointer':f'/inventory/{i}',
  'pool_record_id':pool_ref[(w+'.report',f'/inventory/{i}')],'raw_element_identity':r['element']}
contexts=[]
def add(cid,title,a,b,rawrefs,scope):
 assert 0<=a<b<=len(P)
 child_loci=[lid for lid,r in loci.items() if any(a<=s['char_start'] and s['char_end']<=b for s in r['selected_source_spans'])]
 context={'context_id':cid,'title':title,'selected_source':sref(a,b,scope),
  'original_inventory_refs':[inventory_ref(w,i) for w,i in rawrefs],
  'contained_or_partly_contained_locus_ids':child_loci,
  'intersecting_source_splice_ids':[e['edit_id'] for e in maps['literal_replacements'] if max(a,e['proposal_char_start'])<min(b,e['proposal_char_end'])],
  'attribution_scope':'The original inventory objects retain all their own hand/position/candidate fields. The selected locus contract retains every local child attribution. This context entry assigns no new hand or ink role.'}
 contexts.append(context);return context
header_end=P.index('\n')+1;p2=P.index('(car $');p3=P.index('Considérons deux décompositions binaires')
display_starts=[m.start() for m in re.finditer(r'\\\[',P)];display_ends=[m.end() for m in re.finditer(r'\\\]',P)]
assert len(display_starts)==len(display_ends)==2
d1,d2=display_starts;e1,e2=display_ends
assert P[e1:e1+1]==P[e2:e2+1]=='\n';e1+=1;e2+=1
add('CTX001','complete opening/main paragraph including its margin diagram',header_end,p2,
 [('A',0),('B',0),('B',1),('B',2),('B',6),('B',8),('B',30),('C',0),('C',1),('C',2),('C',4),('C',6),('C',23),('C',27),('C',32),('C',38)],
 'Complete selected paragraph up to the parenthetical paragraph; the terminating blank source line is included.')
add('CTX002','complete parenthetical paragraph',p2,p3,[('A',0),('B',30),('C',38),('C',42)],
 'Complete parenthetical paragraph, including all selected formulas, words, marks and final closer; the terminating blank line is included.')
add('CTX003','complete lower prose paragraph before the first display',p3,d1,[('A',36),('B',45),('C',46),('C',52),('C',61)],
 'Complete lower prose with pairs, corrections, guide, adjective/points and both prose Sigmas, ending immediately before the display opener.')
add('CTX004','complete first lower display',d1,e1,[('A',48),('B',62),('C',63)],
 'Complete literal display including delimiters, first relation, d’où qualifier, both E groups and final parenthesis.')
add('CTX005','complete on … alors bridge',e1,d2,[('A',58),('B',73),('C',70)],
 'Complete bridge from the first display end to the next display opener, preserving the separately qualified reduced mark.')
add('CTX006','complete final three-row display',d2,e2,[('A',54),('B',68),('B',78),('B',84),('C',73)],
 'Complete aligned display with all three rows, current candidate scopes, corrections, definitions and terminal relation.')
add('CTX007','archive-number source comment',e2,len(P),[('A',77),('B',93),('C',86)],
 'Exact agreed archive-number comment and final source newline; its public placement remains the root-selected comment.')
deleted=exact(r"\deleted{l'intersection}",'common original deletion before aucune')
deletion=add('CTX008','common deleted l’intersection',deleted['char_start'],deleted['char_end'],[('A',2),('B',5),('C',5)],
 'Exact unchanged local deletion in the first definition paragraph, before aucune.')
deletion['equal_selected_and_three_reader_literals']=True;deletion['reader_tex_sources']=[]
for w in 'ABC':
 path=f'out/readers/026/{w}/reading.tex';t=(B/path).read_text();literal=r"\deleted{l'intersection}";assert t.count(literal)==1
 a=t.index(literal);assert t[a:a+len(literal)]==P[deleted['char_start']:deleted['char_end']]
 deletion['reader_tex_sources'].append(sref(a,a+len(literal),'exact common deletion in this reader',path,t))
deletion['original_C_inventory_apostrophe_scope']='The C inventory first_words_or_objects uses l’intersection; its exact TeX source uses the literal straight apostrophe retained above. Both raw forms remain unchanged.'

# Complete smaller source containers corresponding to original broad inventory units.
s1a,s1b=group('A026-S01');family_start=P.rfind('$(',0,s1a);assert family_start>=0
name="(les ``hémisphères'')";family_end=P.index(name,s1b)+len(name)
add('CTX009','complete opening family and quoted naming',family_start,family_end,[('B',2),('C',2)],
 'Complete family formula and its following quoted naming phrase, preserving each selected child state.')
topological=P.index('Quand $X$ est un espace topologique')
add('CTX010','definition continuation through the equator parenthesis',family_end,topological,[('A',0),('B',6),('C',4)],
 'Exact explanatory definition text following the family naming, including the common deletion, none-containment wording, equator name and emptiness parenthesis.')
main_a,main_b=group('R026-GMAIN');conclusion_start=P.rfind('que $',0,main_a);assert conclusion_start>=0
diagram_a,diagram_b=group('B026-DIAG');conclusion_end=diagram_a
add('CTX011','complete main closure conclusion before the diagram source',conclusion_start,conclusion_end,[('A',0),('B',30),('C',38)],
 'Full selected inline conclusion with the common-coordinate Sigma/arc/fleck composite and E group; diagram has its own selected parent scope.')
s12a,s12b=group('A026-S12');assert P[s12b:s12b+1]=='$'
add('CTX012','first parenthetical closure equality',p2,s12b+1,[('B',30),('C',38)],
 'Exact first parenthetical formula through its closing dollar, containing all three local Sigma scopes.')
aligned_start=P.index('\\begin{aligned}\n',d2)+len('\\begin{aligned}\n');aligned_end=P.index('\\end{aligned}',aligned_start)
separators=list(re.finditer(r'(?m)^\\\\[ \t]*\n',P[aligned_start:aligned_end]));assert len(separators)==2
rowbounds=[aligned_start]+[aligned_start+m.end() for m in separators]+[aligned_end]
for i,(a,b) in enumerate(zip(rowbounds,rowbounds[1:]),1):
 add('CTX01'+str(i+2),f'complete bottom display row {i}',a,b,[('A',54),('B',{1:68,2:78,3:84}[i]),('C',73)],
  'Complete selected aligned row; a following literal row separator is included where present.')

# A total byte partition retains all TeX source including its page header.
main_partition=[{'context_id':'SOURCE_HEADER','source':sref(0,header_end,'page header source metadata')}]
main_partition.extend({'context_id':c['context_id'],'source':c['selected_source']} for c in contexts[:7])
cursor=0;pieces=[]
for row in main_partition:
 s=row['source'];assert s['char_start']==cursor;pieces.append(P[s['char_start']:s['char_end']]);cursor=s['char_end']
assert cursor==len(P) and ''.join(pieces)==P

# Preserve all262 raw inventory bindings and the exact broad context associations.
usage={}
for row in U:
 for w in 'ABC':
  for rid in row['reader_sources'][w]['inventory_records']:usage.setdefault(rid,[]).append(row['locus_id'])
explicit={}
for context in contexts:
 for ref in context['original_inventory_refs']:explicit.setdefault((ref['reader'],ref['json_pointer']),[]).append(context['context_id'])
inventory_rows=[]
for w in 'ABC':
 for i,value in enumerate(reports[w]['inventory']):
  ref=inventory_ref(w,i);existing=usage.get(ref['pool_record_id'],[])
  bound=explicit.get((w,ref['json_pointer']),[])
  inherited=[]
  for context in contexts[:7]:
   if any(lid in context['contained_or_partly_contained_locus_ids'] for lid in existing):inherited.append(context['context_id'])
  inventory_rows.append({'reader':w,'inventory_index':i,'pool_record_id':ref['pool_record_id'],
   'raw_inventory_pointer':ref['json_pointer'],'raw_element_identity':value['element'],
   'existing_union_locus_associations':existing,'explicit_raw_context_refs':bound,
   'selected_source_container_associations':inherited})
assert len(inventory_rows)==262 and all(x['existing_union_locus_associations'] for x in inventory_rows)
assert all(x['selected_source_container_associations'] or x['explicit_raw_context_refs'] for x in inventory_rows)

# Complement is source bookkeeping only; the interval labels imply no new ink unit.
intervals=sorted((s['char_start'],s['char_end']) for r in C['loci'] for s in r['selected_source_spans']);merged=[]
for a,b in intervals:
 if merged and a<=merged[-1][1]:merged[-1][1]=max(b,merged[-1][1])
 else:merged.append([a,b])
gaps=[];cursor=0
for a,b in merged:
 if cursor<a:gaps.append(sref(cursor,a,'selected-source interval outside the91 locus spans; source bookkeeping'))
 cursor=max(cursor,b)
if cursor<len(P):gaps.append(sref(cursor,len(P),'selected-source interval outside the91 locus spans; source bookkeeping'))
result={'schema':'scan026-complete-selected-source-context-inventory-v1','source_only':True,
 'selected_source':{'path':TEX,'sha256':sha(P),'bytes':len(P.encode())},
 'selected_locus_contract':{'path':'out/checks/scan026_source_selected_contract_v01.json','sha256':sha((O/'scan026_source_selected_contract_v01.json').read_bytes())},
 'contexts':contexts,'complete_source_partition':main_partition,
 'raw_inventory_files':{w:{'path':f'out/readers/026/{w}/report.json','sha256':sha((B/f'out/readers/026/{w}/report.json').read_bytes()),'array_pointer':'/inventory','array_length':len(reports[w]['inventory'])} for w in 'ABC'},
 'all262_raw_inventory_pointer_bindings':inventory_rows,'source_intervals_outside_locus_spans':gaps,
 'coverage_proof':{'main_partition_concat_restores_all_selected_source_bytes':True,'raw_inventory_counts':{w:len(reports[w]['inventory']) for w in 'ABC'},
  'raw_inventory_bindings':262,'every_raw_inventory_record_has_source_context_association':True,
  'common_deletion_equal_in_all_three_readers_and_final':True,'source_chars_total':len(P),'context_partition_chars_total':sum(x['source']['char_end']-x['source']['char_start'] for x in main_partition)},
 'new_hand_assignments':0,'new_ink_classifications':0,'source_content_changed':False,
 'scope_note':'Context containers cover complete selected paragraphs/displays, including their separately qualified child loci. Original inventory metadata retains its own scope and is never promoted to a blanket attribution across those child states.'}
raw=(json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode();out=O/'scan026_source_context_inventory_v01.json'
if out.exists():assert out.read_bytes()==raw
else:out.write_bytes(raw)
print(json.dumps({'path':str(out.relative_to(B)),'sha256':sha(raw),'bytes':len(raw),'contexts':len(contexts),'complete_partition_segments':len(main_partition),'raw_inventory_bindings':len(inventory_rows),'source_only_gaps':len(gaps),'all_assertions_passed':True},ensure_ascii=False,indent=2))
