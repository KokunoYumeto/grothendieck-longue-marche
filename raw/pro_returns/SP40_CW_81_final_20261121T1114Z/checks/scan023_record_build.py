"""Build the scan023 review draft. Reads text only; writes record support only."""
from pathlib import Path
from collections import Counter
import copy,hashlib,json,re,sys
sys.dont_write_bytecode=True
from scan023_record_content import OBS,DATA,CROW_LOCUS,DOUBT_LOCI,KIND,ABSENT_MARKS,SILENT
ROOT=Path('/workspace/scratch/94548b74fbe0')
OUT=ROOT/'out/checks'
def text(p):return (ROOT/p).read_text(encoding='utf-8')
def sha(t):return hashlib.sha256(t.encode('utf-8')).hexdigest()
def js(p):return json.loads(text(p))
def fref(p,**more):return dict(path=p,sha256=sha(text(p)),**more)
def exact_ref(p,s,e):
 t=text(p);return dict(path=p,sha256=sha(t),char_start=s,char_end=e,
  body_sha256=sha(t[s:e]),line_start=t.count('\n',0,s)+1,
  line_end=t.count('\n',0,max(s,e-1))+1,literal=t[s:e])
UP='out/checks/scan023_source_union.json'
MP='out/checks/scan023_final_source_map.json'
DP='out/checks/scan023_final_draft.tex'
JP='out/checks/scan023_main_decisions.md'
AP='out/checks/scan023_root_count_authorization_v2.json'
SP='out/checks/scan023_root_scope_authorization.json'
PP='out/checks/scan023_root_assembly_plan.md'
U=js(UP);M=js(MP);page=text(DP);journal=text(JP);AUTH=js(AP);SCOPE=js(SP)
assert sha(page)=='b9a1249d12916f42eb5694e4e2433f2c95d5435083078cdb5f71db5ea7b69a1f'
assert sha(text(MP))=='5c11242ea3f4fe19b14b70a8fb5707f7e36a6911cbce6525850a3201d86c41e3'
assert sha(journal)=='e47c66e9ceb1a9823bfa73ee6544e6068d84def3a91dee1547ab2e83ab4f07af'
assert sha(text(AP))=='b11587fc4e86d8a5f6e269eebf320ed59080a45d8ce15b6a8f0945dcdd429827'
assert sha(text(SP))=='ab98ffb03ea44a0cfc6541f322c51a1571930a0e256633ed752bbccb269a7a03'
assert M['draft_sha256_utf8']==sha(page)
PROPOSAL=js('out/checks/scan023_record_count_proposal.json')
assert sha(text(PROPOSAL['source_union']['path']))==PROPOSAL['source_union']['sha256']
assert sha(text(AUTH['proposal']['path']))==AUTH['proposal']['sha256']
coverage={r:js(f'out/checks/scan023_{r}_source_coverage.json') for r in 'ABC'}
catalog=js('out/checks/scan023_C_doubt_catalog.json')
hcatalog=js('out/checks/scan023_H_marker_catalog.json')
sscope=js('out/checks/scan023_S_scope.json')
meta=js('packets/023/metadata.json')
mapped={x['locus_id']:x for x in M['source_locus_coverage']}
groups={x['group_id']:x for x in M['selected_groups']}
commands=M['exact_command_ownership']
def attach(s):
 a=s.get('char_start_zero_based',s.get('char_start'));b=s.get('char_end_exclusive',s.get('char_end'))
 assert page[a:b]==s.get('literal',page[a:b])
 return dict(path='checks/scan023_final_draft.tex',workspace_path=DP,sha256=sha(page),
  char_start=a,char_end=b,body_sha256=sha(page[a:b]),literal=page[a:b],
  manifest='scan023_final_source_map.json',source_map_reference=fref(MP))
def span(a,b):return attach(dict(char_start_zero_based=a,char_end_exclusive=b,literal=page[a:b]))
def exact(s):
 positions=[m.start() for m in re.finditer(re.escape(s),page)]
 assert len(positions)==1,(s,positions)
 return span(positions[0],positions[0]+len(s))
def between(a,b,include_b=False):
 s=page.index(a);e=page.index(b,s)+(len(b) if include_b else 0)
 return span(s,e)
def lrefs(n):return [attach(x) for x in mapped[f'U023-{n:02d}']['selected_source_spans']]
def gref(g):return attach(groups[g]['selected_source'])
def pathrefs(name):
 out=[attach(c['selected_source']) for c in commands if c['command'] in ('draw','fill') and (c.get('nearest_ownership_marker') or {}).get('id')==name]
 assert out,name
 return out
heads=list(re.finditer(r'^## (\d\d) — (.+)$',journal,re.M))
sections={}
for i,h in enumerate(heads):
 end=heads[i+1].start() if i+1<len(heads) else len(journal)
 raw=journal[h.start():end]
 crop=re.search('Viewed '+chr(96)+'([^'+chr(96)+']+)'+chr(96)+r' once\.',raw).group(1)
 sections[int(h.group(1))]=dict(id='ROOT023-'+h.group(1),crop=crop,
  exact_journal_source=exact_ref(JP,h.start(),end),raw_historical_journal=raw)
assert len(sections)==31

def own_public(n,r,entry):
 parts=[]
 if r in SILENT.get(n,{}):parts.append(SILENT[n][r])
 for p in entry['actual_complete_source_spans']:
  if len(p['literal'])<=900:parts.append('Actual own TeX: '+p['literal'])
 for d in entry['reported_difference_rows']:
  raw=d['raw'];parts.append(d['id']+': '+raw['reading'])
  if 'alternatives' in raw:parts.append('Own reported alternatives: '+json.dumps(raw['alternatives'],ensure_ascii=False))
  for k in ('qualification','local_head_role','trace_hand','local_parts','recurring_qualification','component_scope','additional_local_changes'):
   if k in raw:parts.append('Own '+k+': '+json.dumps(raw[k],ensure_ascii=False))
 for x in entry['own_notation_rows']:
  parts.append('Own notation '+x['source_ref'].get('json_pointer','')+': '+json.dumps(x['raw'],ensure_ascii=False))
 for g in entry['graphical_source_groups']:
  raw=g['raw'];qual={k:v for k,v in raw.items() if k in ('reading','complete_reading','qualifiers','ownership','owned_words_and_labels')}
  if qual:parts.append('Own group '+g['id']+': '+json.dumps(qual,ensure_ascii=False))
  # Literal source comments retain local full states even where the source map
  # has path-owner fields rather than a separate compact reading field.
  literal=g['complete_tex_ref']['literal']
  comments=[line for line in literal.splitlines() if line.startswith('%') and re.search(r'candidate|state|role|qualif|Owns|owns|point|roof|head|alpha|beta|plus|word|period|hand|scope',line,re.I)]
  if comments:parts.append('Own exact local declarations: '+' / '.join(comments))
 if not parts:
  parts=['Actual complete own source: '+'\n'.join(p['literal'] for p in entry['actual_complete_source_spans'])]
 if entry['source_encoding_observation']:parts.append(entry['source_encoding_observation'])
 refs=['%s chars[%s,%s)'%(p['path'],p['char_start_zero_based'],p['char_end_exclusive']) for p in entry['actual_complete_source_spans']]
 parts.append('Exact own source: '+'; '.join(refs))
 return '\n'.join(dict.fromkeys(parts))

# These are literal source anchors; broad exact context remains attached.
ANCHOR={
1:('prouvons','prouvons'),2:("que l'on a","que l'on a"),
3:(r'\overline V\cap E_\beta=\varnothing',r'\overline{V}\cap E_{\beta}=\emptyset .'),
4:(r'$V$ ne \deleted{contient} \inserted{rencontre}',r'$V$ \struck{contient} ne rencontre'),
7:(r'\widehat{\deleted{\unsure{I|E}}\Sigma}_\alpha^+',r'\widehat{\Sigma}_{\alpha}^{+}'),
8:(r'\deleted{\unsure{donc si}}',r'\struck{donc si \ill{}}'),
9:('on a en fait','on a en fait'),13:("C'est trivial,","c'est trivial,"),
15:(r'$(i\in\unsure{I|J})$',r'($i\in I$)'),
16:('ce qui','qui prouve'),17:(r'\unsure{prouvera}','prouve'),
20:('Cela revient','Cela résulte'),21:(r'\unsure{au}','Cela résulte du'),
23:(r'\deleted{tel que les}',r'\struck{tel que les}'),
24:(r'\deleted{et} des','et des'),26:(r'\unsure{tels}','tels que'),
35:(None,'dans un'),36:(r'\inserted{$\exists\alpha\in K$ tel que}',r'$\exists\,\alpha\in K$, tel que'),
40:(r'Cela \deleted{signifie que}',r'Cela \struck{signifie que}'),
41:(r'\unsure{provient|précise|précise le}',r'\uncertain{provient}'),
42:(r'\unsure{du|des|sens}',r'\ill{}'),46:('hyp.','hyp.'),
47:(r'\unsure{préc.}','précédentes'),
48:(r'$(\Sigma_i^\alpha)_{\alpha\in\unsure{K|I}}$',r'$(\Sigma_{i}^{\alpha})_{\alpha\in K}$'),
49:(r'$(\Sigma_i^\alpha)_{\alpha\in\unsure{K|I}}$',r'$(\Sigma_{i}^{\alpha})_{\alpha\in K}$'),
50:(r'$(\Sigma_i^\alpha)_{\alpha\in\unsure{K|I}}$',r'$(\Sigma_{i}^{\alpha})_{\alpha\in K}$'),
51:(r'\Pi_K^{\unsure{\circ|0}}',r'\Pi_{K}^{0}'),
58:('Immédiat','Immédiat'),59:('récurrence','récurrence'),
61:(r'\operatorname{card} K\geq 0',r'\operatorname{card} K\geqslant0')
}
def witness(n,w,context):
 if n in ABSENT_MARKS:
  return 'No '+ABSENT_MARKS[n]+' is encoded in the attached complete '+w+' source span.',copy.deepcopy(context)
 if n==14 and w=='H':return 'No cancelled unreadable item occurs after trivial in the complete H marginal note.',copy.deepcopy(context)
 if n==35 and w=='C':return 'No separate dans un follows the cancelled clause in the attached complete C source span.',copy.deepcopy(context)
 if n==53 and w=='H':return 'No left marginal rule is encoded in the complete H corollary source or its union apparatus.',copy.deepcopy(context)
 if n==62 and w=='H':return 'H uses its editorial page selector22; no archive-number manuscript comment is supplied.',copy.deepcopy(context)
 anchor=ANCHOR.get(n,(None,None))[0 if w=='C' else 1]
 if anchor is not None and context:
  literal=context['literal'];at=[m.start() for m in re.finditer(re.escape(anchor),literal)]
  if len(at)==1:
   lo=context['char_start_zero_based']+at[0]
   return anchor,exact_ref(context['path'],lo,lo+len(anchor))
 return context['literal'] if context else 'Source-only administrative scope.',copy.deepcopy(context)

decisions=[]
for n,loc in enumerate(U['loci'],1):
 a=AUTH['rows'][n-1];assert a['locus_id']==loc['locus_id']
 final,alternatives,sec,gs=DATA[n]
 c,cr=witness(n,'C',loc['witness_contexts'].get('C'))
 h,hr=witness(n,'H',loc['witness_contexts'].get('H'))
 ev=' '.join(OBS[s]+' Once-viewed crop: '+sections[s]['crop']+'.' for s in sec)
 if not sec:ev='Source-only composition choice supported by the exact complete reader returns and frozen root assembly plan; no new root image observation is asserted.'
 if n in (19,22,29,32,38,40,45,52,62):
  ev+=' Unchanged surrounding text is attached in full from the selected source; any frame citation is the union of these local component views.'
 ev+=' The completed selected source contains: '+final+'.'
 if gs:ev+=' Completed selected group identities: '+', '.join(gs)+'.'
 cro=[x for x,l in CROW_LOCUS.items() if l==n]
 markid={8:'H023-ILL01',41:'H023-UNC01',42:'H023-ILL02'}.get(n)
 marker=next((x for x in hcatalog['markers'] if x['marker_id']==markid),None)
 qualification=PROPOSAL['rows'][n-1]['qualifier_and_count_basis']
 # Current fields use selected outcomes, not proposed count language.
 qualification=re.sub(r'\bproposed C count\b','authorized C count',qualification)
 qualification=qualification.replace('H proposal concerns','The H count concerns')
 if n==54:qualification+=' '+SCOPE['root_selected_scope']
 d=dict(id=loc['locus_id'],location=loc['location'],C=c,H=h,final=final,
  alternatives=alternatives,readers={r:own_public(n,r,loc['readers'][r]) for r in 'ABC'},
  evidence=ev,qualification=qualification,confidence=a['confidence'],kind=KIND.get(n,'other'),
  diff_C=a['diff_C'],diff_H=a['diff_H'],physical_count_parent=a['count_parent'],
  root_count_basis=a['root_count_basis'],count_status='Counts and scalar confidence authorized by root; selected record approval pending.',
  root_count_authorization=fref(AP,json_pointer=f'/rows/{n-1}'),
  marked_in_H=bool(marker),H_marker_ids=[markid] if marker else [],
  H_marker_basis=(dict(actual_marker=copy.deepcopy(marker),source=fref('packets/023/H.tex'),
    scope='Exact marker only: extra placeholder at U08, verb at U41, following short word at U42.')
    if marker else dict(source=hr,scope='No actual uncertainty or illegibility marker at this local H locus; markers elsewhere in the complete context do not transfer here.')),
  C_doubt_status=AUTH['C_outcomes'][f'C023-R{cro[0]:02d}'] if cro else None,
  C_source_row_ids=[f'C023-R{x:02d}' for x in cro],
  C_source_part_ids=[f'C023-R{x:02d}-1' for x in cro],
  crop=[sections[s]['crop'] for s in sec],root_crop_evidence=[dict(journal=sections[s]['exact_journal_source'],
    crop=sections[s]['crop'],successful_display_count=1,observation=OBS[s]) for s in sec],
  root_ink_choice_applied=bool(sec),root_source_audit_choice_applied=True,main_approved=False,
  log_decision=True,selected_group_ids=list(gs),source_attachments=lrefs(n),
  root_source_attachment_status='Exact frozen selected-source spans attached; root final review pending.',
  selected_source_map_reference=fref(MP,json_pointer=f'/source_locus_coverage/{n-1}'),
  witness_source_references=dict(C=cr,H=hr),complete_witness_contexts=copy.deepcopy(loc['witness_contexts']),
  reader_source_details=copy.deepcopy(loc['readers']),
  provenance=dict(source_union_reference=fref(UP,json_pointer=f'/loci/{n-1}'),
    raw_source_stage_locus=copy.deepcopy(loc),raw_count_proposal=copy.deepcopy(PROPOSAL['rows'][n-1]),
    root_historical_journal=[sections[s]['exact_journal_source'] for s in sec]))
 if n==54:d['selected_extra_run_scope_authorization']=fref(SP)
 decisions.append(d)

# Seven S identities remain source-only. No local glyph reading or ink choice is fabricated.
for i,s in enumerate(sscope['row_scopes'],1):
 decisions.append(dict(id=f'S023-{i:02d}',location='Supplied S scope: '+s['where'],
  S_id=s['id'],S_status='source-only review; no quoted scan023 local correction',
  C='No local scan023 correction is quoted by this S row.',H='No local scan023 correction is quoted by this S row.',
  final='Retain the exact supplied S scope without adopting a scan023 ink confirmation or mathematical conclusion.',
  readers={r:'Source-only S administration; the complete released '+r+' page remains attached as provenance, with no S-specific local reading assigned.' for r in 'ABC'},
  evidence=sscope['scope_result'],confidence='high',confidence_scope='Exact source scope only.',
  kind='other',diff_C=False,diff_H=False,marked_in_H=False,H_marker_ids=[],
  H_marker_basis=dict(scope='This source-only S row has no local H uncertainty marker.'),
  physical_count_parent=f'S023-{i:02d}',root_count_basis=AUTH['S_scope_authorization'],
  root_count_authorization=fref(AP,json_pointer='/S_scope_authorization'),
  count_status='Root authorized zero S counts; selected record approval pending.',
  C_doubt_status=None,crop=[],root_crop_evidence=[],root_ink_choice_applied=False,
  root_source_audit_choice_applied=True,main_approved=False,log_decision=True,
  selected_group_ids=[],source_attachments=[],root_source_attachment_status='Administrative scope; exact S source reference attached.',
  S_source_reference=fref('out/checks/scan023_S_scope.json',json_pointer=f'/row_scopes/{i-1}'),
  provenance=dict(raw_S_row=copy.deepcopy(s),raw_scope_record=copy.deepcopy(sscope),
   reader_page_sources={r:coverage[r]['source_files'] for r in 'ABC'})))
DEC={d['id']:d for d in decisions}
for parent,children in {12:[11],22:[23,24,25,26],29:[28,30,31],32:[33],38:[39],45:[46,47],50:[48,49],52:[51,53,54,55,56,57]}.items():
 d=DEC[f'U023-{parent:02d}']
 d['selected_component_readings']=[dict(decision_id=f'U023-{n:02d}',reading=DEC[f'U023-{n:02d}']['final'],
   alternatives=copy.deepcopy(DEC[f'U023-{n:02d}']['alternatives']),
   qualification=DEC[f'U023-{n:02d}']['qualification'],
   source_attachments=copy.deepcopy(DEC[f'U023-{n:02d}']['source_attachments'])) for n in children]
 d['evidence']+=' Complete component states: '+'; '.join(x['reading']+
   ('; alternatives '+json.dumps(x['alternatives'],ensure_ascii=False) if x['alternatives'] else '')+
   '; '+x['qualification'] for x in d['selected_component_readings'])

def make_doubt(n,suffix='',reading=None,alternatives=None,component=None,scope=None):
 d=DEC[f'U023-{n:02d}']
 item=dict(id=f'Q023-{n:02d}'+suffix,decision_ids=[d['id']],location=d['location']+((' — '+scope) if scope else ''),
  reading=reading or d['final'],alternatives=d['alternatives'] if alternatives is None else alternatives,
  confidence=d['confidence'],reason=d['evidence']+' '+d['qualification'],
  crop=copy.deepcopy(d['crop']),root_crop_evidence=copy.deepcopy(d['root_crop_evidence']),
  selected_group_ids=copy.deepcopy(d['selected_group_ids']),source_attachments=pathrefs(component) if component else copy.deepcopy(d['source_attachments']),
  physical_count_parent=d['physical_count_parent'],C_source_row_ids=copy.deepcopy(d.get('C_source_row_ids',[])),
  main_approved=False,readers=copy.deepcopy(d['readers']),reader_source_details=copy.deepcopy(d['reader_source_details']),
  local_role_hand_origin_scope=scope,root_scope_authorization=fref(SP) if component=='C023-G18-P05' else None)
 item['confidence_scope']=(
  'Low confidence concerns state/identity; the root journal separately records high confidence in the visible geometry.'
  if n in (6,7,28,48,49,54) else
  'Low confidence concerns accent direction/attachment; word-body confidence remains medium.'
  if n in (58,59) else
  'Scalar confidence follows the root-authorized locus; unassigned role, hand, attachment or origin remains expressly undetermined.')
 return item
doubts=[make_doubt(n) for n in DOUBT_LOCI]
doubts.extend([
 make_doubt(33,'a','Complete alpha with its separated terminal point',['Complete alpha accompanied by an independent point'],
  'C023-G10-P05','alpha-point attachment, hand and surface origin remain undetermined'),
 make_doubt(48,'a','Lower i-like hook with its detached point',['Foot retrace accompanied by an independent point'],
  'B023-G08.p4','one point with separate attachment, role, hand and origin scope'),
 make_doubt(54,'a','Lower point above-left of retraced alpha',['Predecessor-i dot','Alpha-associated trace','Independent point'],
  'C023-G18-P03','lower point has independently undetermined attachment, hand and origin'),
 make_doubt(54,'b','Upper point above-right of plus',['Plus-associated retrace','Independent point'],
  'C023-G18-P06','upper point has independently undetermined attachment, hand and origin'),
 make_doubt(54,'c','Short additional upper run of plus',['Retrace role','Unassigned additional run'],
  'C023-G18-P05','root-selected extra-run role, local hand and origin remain undetermined')
])
# Preserve page order and subcomponent adjacency without deriving physical coordinates.
doubts.sort(key=lambda x:(int(x['id'][5:7]),x['id'][7:]))

original_rows=[]
for row in catalog['rows']:
 item=copy.deepcopy(row);number=int(row['source_id'][-2:]);n=CROW_LOCUS[number];d=DEC[f'U023-{n:02d}']
 item['provenance']=dict(original_catalog_row=copy.deepcopy(row),
  original_source_stage_reader_returns=copy.deepcopy(U['actual_C_doubt_rows'][number-1]),
  catalog=fref('out/checks/scan023_C_doubt_catalog.json',json_pointer=f'/rows/{number-1}'))
 item['selected_outcome']=AUTH['C_outcomes'][row['source_id']]
 item['source_parts']=[]
 for part in row['source_parts']:
  p=copy.deepcopy(part);p.update(original_source_decision_status=part['decision_status'],
   decision_status='Root ink outcome recorded; selected record approval pending.',
   selected_status=item['selected_outcome'],outcome=item['selected_outcome'],
   decision_ids=[d['id']],physical_count_parent=d['physical_count_parent'],
   selected_reading=d['final'],complete_alternatives=d['alternatives'],
   source_attachments=copy.deepcopy(d['source_attachments']),
   root_journal_sources=[x['journal'] for x in d['root_crop_evidence']],
   root_count_authorization=fref(AP,json_pointer='/C_outcomes/'+row['source_id']),main_approved=False)
  item['source_parts'].append(p)
 original_rows.append(item)

# Complete selected spans for whole inventory regions, independent of component counts.
regions={
 '023C.01':between("Soit maintenant",r'\['+'\n% BEGIN B023-G05'),
 '023C.11':between('je dis que si',r'\['+'\n% BEGIN B023-G05'),
 '023C.12':between(r'\['+'\n% BEGIN B023-G05',r'\]'+'\n% slanted',True),
 '023C.13':between('% slanted',r'\unsure{ce qui|qui}'),
 '023C.15':between(r'\unsure{ce qui|qui}',r'\uline{Lemme}'),
 '023C.17':exact(r'\uline{Lemme}'),
 '023C.18':between(r'Soit $K\subset I$',r'\reversemarginpar\margin{%'+'\n% BEGIN B023-M02'),
 '023C.22':span(page.index(r'\['+'\n'+r'\alpha'+'\n% BEGIN GROUP C023-G07'),page.index(r'\]'+'\nSoit')+2),
 '023C.27':between(r'Soit $i\in I\setminus K$',r'Cela \deleted{signifie que}'),
 '023C.33':between(r'Cela \deleted{signifie que}',r'\reversemarginpar\margin{%'+'\n% BEGIN B023-M04'),
 '023C.36':between(r'\uline{Corollaire}','% BEGIN GROUP C023-G15'),
 '023C.39':gref('C023-G15'),
 '023C.45':between('% BEGIN GROUP C023-G20','% archive sheet number: 22'),
 '023C.47':exact('% archive sheet number: 22')
}
INVLOCI={
 '01':[1,2,3,4,5,6,7,8,9,10],'02':[4],'03':[4],'04':[5],'05':[6],'06':[6],'07':[7],'08':[7],
 '09':[8],'10':[10],'11':[8,9,10],'12':[11,12],'13':[13,14,15],'14':[14],
 '15':[16,17,18,19,20,21],'16':[18],'17':[22],'18':[22,23,24,25,26],
 '19':[23],'20':[24],'21':[25],'22':[28,29,30,31],'23':[28],'24':[28],
 '25':[30],'26':[31],'27':[32,33,34,35,36,37,38,39],'28':[33],'28a':[33],
 '29':[34],'30':[34,36,37],'31':[34,36],'32':[39],'33':[40,41,42,43],'34':[40],'35':[43],
 '36':[45,46,47,48,49,50],'37':[48,49,50],'37a':[48],'38':[49],'39':[51,52,53,54,55,56,57],
 '40':[53],'41':[51],'42':[55,56],'43':[54],'43a':[54],'43b':[54],'44':[57],
 '45':[58,59,60,61],'46':[60],'47':[62]}
INVDESC={
 '01':'Complete opening prose/formulas, qualified prouvons and literal a, correction, first cup/S01, cancelled donc si, whole qualified on a and separate traces.',
 '02':'Cancelled contient, with live ne before it and separate raised rencontre.',
 '03':'Raised inserted rencontre, following live ne and above cancelled contient; aucun remains live.',
 '06':'Qualified deleted-bigvee/live-cup versus retraced-live-cup states; full alpha-in-K limit remains in the same operator.',
 '08':'Complete hatted deleted-I/Sigma, deleted-E/Sigma and live-Sigma/retrace states, with plus and alpha.',
 '10':'Separate ochre oblique; role, hand and surface origin undetermined; outside the whole on a qualifier.',
 '11':'je dis que si ... qualified whole on a with one literal a/point-shaped form ... en fait; separate ochre child retained.',
 '12':'Complete E_beta inclusion, including the E foot-loop group, ordinary S02 and (ouvert disjoint de V).',
 '13':"Complete slanted three-line C'est trivial note, cancelled unreadable item, E_i (i in I/J) and sont disjoints.",
 '15':"Qualified ce qui/qui and prouvera/prouve, complete l'assertion/point, upper inclusion, Cela revient and qualified au.",
 '18':'Complete lemma introduction: K subset I; cancelled tel que les and et; full S04 and (alpha in K); firm tels que.',
 '22':'Complete first relation-state alternatives, beta in K, repeated alpha ne beta, implication, full S05 cap S06, equals empty-set and period.',
 '26':'Complete B023-S06 joined-head/shared-beta glyph, with Sigma_beta^+ and Sigma_beta^top candidates; no supplied upper arm.',
 '27':'Complete lemma antecedent and S07/terminal point, corrected old clause and raised replacement, live final inclusion/S08 and period.',
 '29':'Whole deleted E_i est contenu/contenue, retaining both participles within all four full correction states.',
 '30':'Complete raised exists alpha in K tel que; que primary live with deleted alternative; no comma after K.',
 '31':'One cancellation rule with pale beginning and dark continuation, reaching raised que; target remains qualified.',
 '33':'Cela, cancelled signifie que, primary precise with précise/provient/precise le/précise le, firm du and two far-right points.',
 '36':'Underlined Corollaire; complete Avec les hyp. préc. sur lead and whole selected family with four external-index states.',
 '37':'Complete B023-G08 family, both parentheses, detached head, hook/one point, raised alpha, external-alpha junction, four index states and comma.',
 '37a':'One B023-G08.p4 point; attachment to i-like hook versus foot-retrace/independent-point role remains qualified.',
 '38':'Whole family K, I, deleted-I-then-K and deleted-K-then-I alternatives; primary K with chronology unresolved.',
 '39':'Complete two-line corollary, all words/formulas/period once; Pi/K/ring, shared full formée/cup, S10 with both points/extra run, S11 and interrupted left rule.',
 '40':'One B023-G10 marginal rule: six literal runs and one bead, pale interruptions and curved lower ending; within C023-G15 units.',
 '41':'Complete Pi head, attached left stem/return, detached right stem, hooked lower K and qualified circle/zero ring with entry hook.',
 '42':'Complete formée and accent, shared f/cup junction, interrupted upper-left stalk, definite high cross with unresolved role, and complete lower limit.',
 '43':'Complete joined S10, retraced alpha, Sigma_alpha^+ versus deleted-i-then-alpha state, both separate points and short extra plus run.',
 '43a':'Upper point above-right of plus; separate retrace/independent-point attachment, hand and origin scope.',
 '43b':'Lower point above-left of alpha; predecessor-i/alpha-associated/independent-point attachment, hand and origin scope.',
 '44':'Complete S11 with definite roof, detached short head, angular body, plus and continuous alpha; local head role remains qualified.',
 '45':'Complete final assertion: Immédiat/Immèdiat/Immediat, par, récurrence/rècurrence/recurrence, sur card K geqslant0 and period; capital-side hook included once.',
 '46':'Faint short capital-side hook, with role, hand and origin undetermined.',
 '47':'Archive sheet number22 in a source comment only; no root image claim and undetermined hand.'
}
selected_inventory={}
for old in coverage['C']['inventory']:
 raw=old['raw'];key=old['id'].split('.',1)[1];ns=INVLOCI[key]
 row=copy.deepcopy(raw);row['first_words_or_objects']=INVDESC.get(key,raw['first_words_or_objects'])
 row.update(main_approved=False,selection_status='Selected frozen source attached; root record approval pending.',
  decision_ids=[f'U023-{n:02d}' for n in ns],source_attachments=[regions[old['id']]] if old['id'] in regions else [q for n in ns for q in lrefs(n)],
  selected_group_ids=list(dict.fromkeys(g for n in ns for g in DATA[n][3])),
  source_inventory_identity=old['id'],provenance=dict(raw_reader_inventory=copy.deepcopy(old),reader='C'),
  hand_status='Selected local hand scopes retained; root final record approval pending.')
 if raw.get('source_group')=='C023-G09':row['source_group']='B023-S06'
 if raw.get('source_group')=='C023-G14':row['source_group']='B023-G08'
 if key=='37a':row.update(path_owner='B023-G08.p4',source_attachments=pathrefs('B023-G08.p4'))
 if key=='28a':row['source_attachments']=pathrefs('C023-G10-P05')
 if key in ('43a','43b'):row['source_attachments']=pathrefs('C023-G18-P06' if key=='43a' else 'C023-G18-P03')
 if key=='40':row.update(source_group='B023-G10',source_attachments=[gref('B023-G10')])
 if key=='11':row['source_group']='C023-G04 contains R023-ON and separately qualified ochre child'
 if key in ('01','11','15','27','28','33','36','37','39','43','45'):
  row['hand']='his hand; separately identified local traces: undetermined hand'
  row['hand_scope']='Main writing remains in his hand. Each attached trace/point retains its own undetermined hand, attachment and origin; containing coverage confers no hand attribution.'
 if key=='43':
  row['hand_scope']+=' '+SCOPE['root_selected_scope']
  row['selected_extra_run_scope_authorization']=fref(SP)
 selected_inventory[old['id']]=row
for bid,n in [('B023-I02',2),('B023-I13',11),('B023-I21',27),('B023-I36',44)]:
 old=next(x for x in coverage['B']['inventory'] if x['id']==bid)
 row=copy.deepcopy(old['raw']);row.update(main_approved=False,selection_status='Selected frozen source attached; root record approval pending.',
  source_inventory_identity=bid,decision_ids=[f'U023-{n:02d}'],source_attachments=lrefs(n),
  selected_group_ids=DATA[n][3],provenance=dict(raw_reader_inventory=copy.deepcopy(old),reader='B'),
  first_words_or_objects=DATA[n][0],hand_status='Selected scope; root record approval pending.')
 if n==2:row.update(hand='undetermined hand',hand_scope='Root selected local role, hand, attachment and surface-origin uncertainty; B original his-hand field remains in provenance.')
 selected_inventory[bid]=row
selected_inventory['R023-ON']=dict(sheet_kind='text',hand='his hand; final a-shaped trace: undetermined hand',
 element='R023-ON',kind='drawing',position='Whole on a before en fait; ochre child remains separate',
 first_words_or_objects='Complete qualified on a, visible on once and B final-a fill once; primary a versus point-shaped mark.',
 transcribed='yes',main_approved=False,decision_ids=['U023-09'],selected_group_ids=['R023-ON'],
 source_attachments=[gref('R023-ON')],selection_status='Root-composed selected source; final record approval pending.',
 hand_status='Main on writing and final trace retain separate hand scopes.',provenance=dict(root_plan=fref(PP),donor='B023-G04.p1'))
selected_inventory['R023-S10-extra']=dict(sheet_kind='text',hand='undetermined hand',
 element='R023-S10-extra',kind='drawing',position='Short extra upper-left run on S10 plus',
 first_words_or_objects='Short additional plus run: retrace/unassigned-run role; independently undetermined local hand and origin.',
 transcribed='yes',main_approved=False,decision_ids=['U023-54'],selected_group_ids=['C023-G18'],
 source_attachments=pathrefs('C023-G18-P05'),selection_status='Selected frozen component; root record approval pending.',
 hand_status='Root-selected scope; C raw point-only hand statement remains in provenance.',
 provenance=dict(scope_authorization=fref(SP),raw_scope=copy.deepcopy(SCOPE)))
order=['023C.01','B023-I02','023C.02','023C.03','023C.04','023C.05','023C.06','023C.07','023C.08','023C.09',
 '023C.11','R023-ON','023C.10','023C.12','B023-I13','023C.13','023C.14','023C.15','023C.16',
 '023C.17','023C.18','023C.19','023C.20','023C.21','B023-I21','023C.22','023C.23','023C.24','023C.25','023C.26',
 '023C.27','023C.28','023C.28a','023C.29','023C.30','023C.31','023C.32','023C.33','023C.34','023C.35','B023-I36',
 '023C.36','023C.37','023C.37a','023C.38','023C.39','023C.40','023C.41','023C.42','023C.43','023C.43a','023C.43b',
 'R023-S10-extra','023C.44','023C.45','023C.46','023C.47']
assert set(order)==set(selected_inventory) and len(order)==len(selected_inventory)
inventory=[selected_inventory[x] for x in order]
for index,i in enumerate(inventory,1):i['page_order']=index
for d in decisions:
 d['inventory_ids']=[i['element'] for i in inventory if d['id'] in i['decision_ids']]

selected_groups=[]
for index,g in enumerate(M['selected_groups']):
 gid=g['group_id'];ds=[d['id'] for d in decisions if gid in d['selected_group_ids']]
 inv=[i['element'] for i in inventory if gid in i['selected_group_ids']]
 assert ds and inv,(gid,ds,inv)
 selected_groups.append(dict(group_id=gid,id=gid,parent_group=g['parent_group'],
  selected_source=gref(gid),decision_ids=ds,inventory_ids=inv,child_group_ids=g['child_group_ids'],
  direct_command_ids=g['direct_command_ids'],contained_command_ids=g['contained_command_ids'],
  wrapper_ids=g['wrapper_ids'],context_ids=g['context_ids'],entry_parent_context_id=g['entry_parent_context_id'],
  current_readings=[dict(decision_id=x,reading=DEC[x]['final'],alternatives=DEC[x]['alternatives'],qualification=DEC[x]['qualification']) for x in ds],
  evidence=' '.join(dict.fromkeys(DEC[x]['evidence'] for x in ds)),
  source_map_reference=fref(MP,json_pointer=f'/selected_groups/{index}'),main_approved=False,
  physical_ownership=g['physical_ownership'],
  provenance=dict(frozen_selected_map_record=copy.deepcopy(g))))
locus_coverage=[]
for n,loc in enumerate(M['source_locus_coverage'],1):
 d=DEC[loc['locus_id']]
 locus_coverage.append(dict(locus_id=loc['locus_id'],location=loc['location'],decision_ids=[d['id']],
  selected_group_ids=d['selected_group_ids'],inventory_ids=d['inventory_ids'],
  source_attachments=d['source_attachments'],reader_source_details=copy.deepcopy(d['reader_source_details']),
  readers=copy.deepcopy(d['readers']),reading=d['final'],alternatives=d['alternatives'],
  evidence=d['evidence'],qualification=d['qualification'],confidence=d['confidence'],
  physical_count_parent=d['physical_count_parent'],main_approved=False,
  provenance=dict(frozen_map_locus=copy.deepcopy(loc))))

abbreviations=[]
for form,expansion,n in [('hyp.','hypothèses',46),('préc.','précédentes',47),('card','cardinal',61)]:
 token=r'\operatorname{card}' if form=='card' else form
 abbreviations.append(dict(form=form,expansion=expansion,expansion_status='Probable expansion; transcription remains abbreviated.',
  source_attachments=[exact(token)],decision_ids=[f'U023-{n:02d}'],main_approved=False,
  expansion_source=fref('out/readers/023/B/report.json',json_pointer='/notes/abbreviations/'+form)))
notes=("The manuscript writes the opening target $\\overline V\\cap E_\\beta=\\varnothing$ and then writes “mieux, je dis que” before a single-alpha inclusion. "
 "Its marginal note says “C'est trivial” and includes a cancelled unreadable item. Underlined Lemme and Corollaire headings organize the next assertions; "
 "the corollary names the partition $\\Pi_K^\\circ$, with $\\Pi_K^0$ retained as the complete alternative. "
 "The final sentence reads “Immédiat par récurrence sur $\\operatorname{card} K\\geqslant 0$,” with both accent-qualified words preserved.\n\n"
 "The sheet corrects contient to raised rencontre, cancels donc si, tel que les and et, and replaces the cancelled E_i est contenu/contenue clause by a raised existential whose que has a qualified cancellation target. "
 "Its unfinished Cela line retains precise, précise, provient, precise le and précise le before firm du. The repeated relation, crowded family index, decorated Sigma glyphs and shared formée/cup strokes remain as transcribed. "
 "The written hyp., préc. and card remain abbreviated. Archive number22 appears only in the source comment. These are attributed manuscript readings; no mathematical check event was performed.")
content_spans=[p for n in [3,13,19,22,29,32,34,38,40,41,42,45,48,51,52,58,59,61,62] for p in lrefs(n)]
content_note=dict(text=notes,source_attachments=content_spans,attribution='Manuscript statements as transcribed; unverified.',
 main_approved=False,check_event_performed=False,root_plan=fref(PP))
support_names=['scan023_A_source_coverage.json','scan023_B_source_coverage.json','scan023_C_source_coverage.json',
 'scan023_witness_source_coverage.json','scan023_source_union.json','scan023_source_union.md','scan023_source_union_summary.json',
 'scan023_C_doubt_catalog.json','scan023_H_marker_catalog.json','scan023_S_scope.json',
 'scan023_record_count_proposal.json','scan023_record_count_proposal.md','scan023_root_count_authorization.json',
 'scan023_root_count_authorization_v2.json','scan023_root_scope_authorization.json','scan023_main_decisions.md',
 'scan023_root_assembly_plan.md','scan023_source_assembly_release.json','scan023_source_assembly_gate.json']
record=dict(scan=23,folder=meta['folder'],their_page=meta['their_page'],hua_has=meta['hua_has'],
 filename='J81-03_81_scan023.tex',brief_version='v21 / source-record v05',main_adjudicated=False,main_approved=False,
 decisions=decisions,doubts=doubts,inventory=inventory,C_source_rows=original_rows,
 selected_graphical_groups=selected_groups,source_locus_coverage=locus_coverage,
 abbreviations=abbreviations,notes=notes,attributed_content_note=content_note,
 root_selected_content_note=copy.deepcopy(content_note),check_events=[],
 counts=dict(C=33,H=37,decision_loci=len(decisions),inventory_elements=len(inventory),remaining_doubt_loci=len(doubts),check_events=0),
 count_status='Root authorized all C/H physical counts and scalar confidences; selected record approval remains pending.',
 root_count_authorization=fref(AP),root_scope_authorization=fref(SP),
 pending_root_decision_ids=[],root_actions_pending=['Review complete current record and exact selected source; approve and run the structural commit gate.'],
 root_approval_status='Selected source and record pending root approval.',
 source_attachment_status='Byte-exact selected draft attachments are complete; final root review pending.',
 selected_draft=fref(DP),selected_source_map=fref(MP),source_assembly_release=fref('out/checks/scan023_source_assembly_release.json'),
 root_crop_audit='checks/scan023_root_crop_audit.json',
 root_viewing_scope=dict(whole_or_halves_seen_by_root=False,total_distinct=31,
  viewed_once=[dict(path=s['crop'],journal=s['exact_journal_source'],successful_display_count=1) for s in sections.values()],
  source='Frozen root journal; no image or image metadata opened by this source-only helper.'),
 workflow_note='All three complete released reader returns and full pairwise TeX diffs preceded root local images. Root journal records31 unique once-viewed targets. Source-only helpers preserved originals, literal paths and qualifications; no mathematical check event.',
 provenance=dict(source_support_files=[fref('out/checks/'+n) for n in support_names],
  reader_original_text_source_hashes={r:coverage[r]['source_files'] for r in 'ABC'},
  source_stage_original_C_rows=copy.deepcopy(U['actual_C_doubt_rows']),
  source_stage_original_S_scope=copy.deepcopy(sscope),original_count_proposal=copy.deepcopy(PROPOSAL),
  original_count_authorization=fref('out/checks/scan023_root_count_authorization.json'),
  exact_bounded_count_correction=copy.deepcopy(AUTH['bounded_source_wording_correction']),
  original_inventory_order=[x['id'] for x in coverage['C']['inventory']],selected_inventory_order=order,
  inventory_order_basis='Interleaved supplied page regions and declared component ownership; no coordinate calculation.',
  source_assembly_map=fref(MP),literal_component_ownership_reference=fref(MP,json_pointer='/exact_command_ownership'),
  wrapper_ownership_reference=fref(MP,json_pointer='/exact_wrapper_ownership'),
  layout_context_reference=fref(MP,json_pointer='/layout_contexts'),
  declared_import_correspondences=copy.deepcopy(M['declared_import_correspondences']),
  separate_selected_scopes=copy.deepcopy(M['separate_local_qualification_scopes']),
  precise_prior_process_deviation=coverage['B']['process_deviation'],
  operations='Read/write text and exact source offsets/hashes only. No images, image metadata, OCR, crops, rendering, compilation, external research, delegation, mathematical check or coordinate computation.'))

# One necessary draft gate: exact attachment text, complete coverage and reciprocal associations.
issues=[]
def check_refs(v):
 if isinstance(v,dict):
  if v.get('path')=='checks/scan023_final_draft.tex' and 'char_start' in v:
   a,b=v['char_start'],v['char_end']
   if not (0<=a<b<=len(page) and v['sha256']==sha(page) and page[a:b]==v['literal'] and sha(page[a:b])==v['body_sha256']):
    issues.append('selected attachment mismatch')
  for x in v.values():check_refs(x)
 elif isinstance(v,list):
  for x in v:check_refs(x)
check_refs(record)
assert not issues,issues
assert len(decisions)==69 and len(locus_coverage)==62
assert all(set(d['readers'])==set('ABC') for d in decisions)
assert sum(d['diff_C'] for d in decisions)==33 and sum(d['diff_H'] for d in decisions)==37
assert len({d['id'] for d in decisions})==len(decisions)
assert len({i['element'] for i in inventory})==len(inventory)
assert all(i['source_attachments'] and i['transcribed']=='yes' for i in inventory)
assert all(d['reason'] and d['source_attachments'] for d in doubts)
assert Counter(AUTH['C_outcomes'].values())==dict(resolved=4,retained=12)
for g in selected_groups:
 for did in g['decision_ids']:assert g['group_id'] in DEC[did]['selected_group_ids']
 for iid in g['inventory_ids']:assert g['group_id'] in selected_inventory[iid]['selected_group_ids']
for d in decisions:
 assert d['kind'] in {'misread word','misread symbol or index','omission','text not on the page',
  'deletion state (struck given live or live given struck)','insertion or placement',
  'abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
 assert isinstance(d['marked_in_H'],bool)
record_path=OUT/'scan023_record_draft.json'
record_path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
gate=dict(scan=23,record=fref('out/checks/scan023_record_draft.json'),draft=fref(DP),source_map=fref(MP),
 current_count_authorization=fref(AP),scope_authorization=fref(SP),counts=record['counts'],
 C_outcomes=dict(Counter(AUTH['C_outcomes'].values())),
 all_69_decisions_have_own_ABC_fields=True,all_62_loci_bound=True,
 exact_selected_attachment_check='pass',reciprocal_group_decision_inventory='pass',
 all_selected_inventory_has_complete_spans=True,source_originals_untouched=True,
 root_approved=False,remaining_issues=issues,
 verification_scope='Required record source/attachment/coverage gate only; no images, rendering, mathematical checks or coordinate computations.')
(OUT/'scan023_record_gate.json').write_text(json.dumps(gate,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

review=['# Scan023 current record for root review','',
 'Counts/confidences are root-authorized; final source/record approval remains false. Exact raw source records and full attachment literals are retained in the JSON.','',
 '## Current decisions','']
for d in decisions:
 review.extend(['### '+d['id']+' — '+d['location'],'',
  'C: '+d['C'],'','H: '+d['H'],'','Selected: '+d['final'],'',
  'Complete alternatives: '+json.dumps(d.get('alternatives',[]),ensure_ascii=False),'',
  'Confidence: '+d['confidence']+'; C/H counts: '+str(int(d['diff_C']))+'/'+str(int(d['diff_H']))+'; parent '+d['physical_count_parent']+'; marked_in_H '+str(d['marked_in_H'])+'.','',
  'Evidence: '+d['evidence'],'','Qualification: '+d.get('qualification','Source-only S scope.'),''])
 for r in 'ABC':review.extend(['Own '+r+': '+d['readers'][r],''])
review.extend(['## Current doubts',''])
for d in doubts:review.extend(['### '+d['id']+' — '+d['location'],'',d['reading'],'',
 'Alternatives: '+json.dumps(d['alternatives'],ensure_ascii=False),'','Confidence: '+d['confidence'],'',d['reason'],''])
review.extend(['## Selected inventory, interleaved',''])
for i in inventory:review.extend([i['element']+' — '+i['kind']+' — '+i['hand']+' — '+i['position'],
 i['first_words_or_objects'],'Decision coverage: '+', '.join(i['decision_ids']),''])
review.extend(['## Brief attributed note','',notes,'','## Abbreviations',''])
for a in abbreviations:review.append(a['form']+' — probable '+a['expansion'])
(OUT/'scan023_record_review.md').write_text('\n'.join(review)+'\n',encoding='utf-8')
print(json.dumps(gate,ensure_ascii=False,indent=2))
