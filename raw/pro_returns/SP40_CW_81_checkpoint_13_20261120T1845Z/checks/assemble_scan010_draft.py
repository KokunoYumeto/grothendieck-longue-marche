"""Mechanical, unadjudicated scan010 source assembly. Does not open images."""
from pathlib import Path
import json,hashlib,difflib,copy,re,datetime
R=Path('/workspace/scratch/94548b74fbe0')
OUT=R/'out/checks'
roles='ABC'
reports={r:json.loads((R/f'out/readers/010/{r}/report.json').read_text()) for r in roles}
readings={r:(R/f'out/readers/010/{r}/reading.tex').read_text() for r in roles}
audits={r:(R/f'out/readers/010/{r}/reading.md').read_text() for r in roles}
meta=json.loads((R/'packets/010/metadata.json').read_text())
base=(R/'packets/010/C.tex').read_text()
baselines=base.splitlines()
rows={r:{d['id']:d for d in reports[r]['differences']} for r in roles}
# IDs denote physical local identities, independent of report row granularity.
spec=[
('01','Lower-left graph, first endpoint of first edge',['A010-D01'],['B01'],['C010-D01'],1),
('02','Final middle disk, projecting trace and detached blob',['A010-D02'],['B02','B10'],['C010-D02a'],2),
('03','Foot, left angular trace crossing the final graph',['A010-D02'],['B02'],['C010-D02b'],2),
('04','Foot, right angular trace: existing principal paths',['A010-D02'],['B02'],['C010-D02c'],2),
('05','Lower second disk, diagonal-stroke state and graphic wrapper',['A010-D03'],['B03'],['C010-D03','C010-D03G'],3),
('06','Upper seventh graph, middle vertex and its projecting hook',['A010-D04'],['B04','B08'],['C010-D04'],4),
('07','Upper edge, paired detached traces and their geometry',['A010-D05','A010-D10'],['B05','B13','B14'],['C010-D05a','C010-D06'],5),
('08','Right middle open space, existing main pale curl',['A010-D05'],['B05'],['C010-D05b'],5),
('09','Right middle open space, existing pair of tiny flecks',['A010-D05'],['B05'],['C010-D05c'],5),
('10','Lower-middle graph, first vertex',['A010-D06'],['B06'],['C010-D12'],None),
('11','Final lower graph, first vertex',['A010-D07'],['B07'],['C010-D13'],None),
('12','Final middle disk, small detached spot above outer lower arch',['A010-D08'],['B09'],['C010-D10'],None),
('13','Upper variant disk, fragments and dots beside descending stroke',['A010-D09'],[],[],None),
('14','Right middle open space, smaller pale trace above-right of main curl',['A010-D11'],['B15'],['C010-D08'],None),
('15','Right angular foot group, internal pale diagonal',['A010-D12'],['B20'],['C010-D14'],None),
('16','Below right angular foot group, detached short dash',['A010-D13'],['B25'],[],None),
('17','Right angular foot group, upper dark upright fragment',['A010-D14'],['B21'],['C010-D15'],None),
('18','Right angular foot group, separate spot near (1567,921)',['A010-D14'],['B22'],['C010-D15'],None),
('19','Below/right of upper second graph, pale curved trace',['A010-D15'],['B16'],['C010-D07'],None),
('20','Gap between lower first and second disks, pale diagonal',['A010-D16'],['B18'],['C010-D09'],None),
('21','Far-right margin level with lower row, pale irregular patch',['A010-D17'],[],['C010-D17'],None),
('22','Lower first disk, faint left continuation of horizontal trace',['A010-D18'],['B19'],['C010-D16'],None),
('23','Lower second disk, small pendant at lower-left outline',['A010-D19'],['B11'],['C010-D11'],None),
('24','Lower second disk, pale descending trace above pendant',[],['B12'],[],None),
('25','Above upper fourth disk, pale descending trace',[],['B17'],[],None),
('26','Right angular foot group, detached upper-left spot near (1550,894)',[],['B23'],['C010-D15'],None),
('27','Right angular foot group, detached right patch near (1603,930)',[],['B24'],[],None),
('28','Final lower disk, detached short mark near (1165,877)',[],[],[],None),
]
def did(n):return '010-D'+str(n).zfill(2)
# Exact TeX extraction is purely positional/source based; no ink reading occurs here.
starts={
'02':['(1307,505)','(1328,433)','(1327,436)','(1340,332)','(1333,382)','(1328,430)'],
'03':['(1010,975)','(1041,1036)','(1073,1088)','(1215,1073)'],
'04':['(1345,934)','(1373,1014)','(1487,1054)','(1568,905)'],
'07':['(1018,','(1037,'], '08':['(1518,375)'],'09':['(1566,580)'],
'12':['(1317,544)','(1314,543)','(1314,544)'],
'13':['(1596,174)','(1584,198)'], '14':['(1567,351)','(1567,352)'],
'15':['(1444,1037)','(1436,1043)','(1440,1036)'],
'16':['(1435,1087)','(1435,1084)'], '17':['(1569,908)','(1568,908)','(1568,907)'],
'18':['(1568,921)','(1566,921)','(1567,921)'],
'19':['(415,242)','(416,241)','(414,240)'],
'20':['(369,743)','(368,743)','(377,751)'],
'22':['(249,826)','(252,825)','(250,826)','(276,827)','(278,827)'],
'23':['(490,916)','(491,912)','(490,911)'], '24':['(490,861)'],
'25':['(784,42)','(786,56)'],'26':['(1550,893)','(1550,894)'],'27':['(1603,930)'],'28':['(1166,875)']}
node_starts={'01':'at (222,1035)','06':'at (1152,251)','10':'at (563,1026)','11':'at (1075,1032)'}
def excerpt(lines,a,b):return {'line_start':a+1,'line_end':b,'exact_excerpt':'\n'.join(lines[a:b])}
def extract(tex,n):
 ls=tex.splitlines(); spans=[]
 if n in node_starts:
  for i,l in enumerate(ls):
   if node_starts[n] in l:
    j=i+1
    while j<len(ls) and r'\end{minipage}};' not in ls[j]:j+=1
    spans.append((i,j+1))
  if n=='06':
   spans += [(i,i+1) for i,l in enumerate(ls) if '(1153,251)' in l]
 elif n=='05':
  for i,l in enumerate(ls):
   if 'at (548,820)' in l:
    j=i+1
    while j<len(ls) and not ls[j].startswith(r'\draw (666,836)'):j+=1
    spans.append((i,j))
 elif n=='21':
  for i,l in enumerate(ls):
   if l.startswith(r'\filldraw'):
    j=i+1
    while ';' not in ls[j-1] and j<len(ls):j+=1
    if any('(162' in z for z in ls[i:j]):spans.append((i,j))
 else:
  for i,l in enumerate(ls):
   if any(s in l for s in starts.get(n,[])):spans.append((i,i+1))
 return [excerpt(ls,a,b) for a,b in spans]
# Exact local identities for doubt provenance; shared crop names never establish an identity.
doubt_map={
'A':{1:['01'],2:['06'],3:['05'],4:['02','03','04'],5:['07','08','09'],6:['10'],7:['11'],8:['19','20','21']},
'B':{1:['01'],2:['06'],3:['10'],4:['11'],5:['05'],6:['02','03','04'],7:['07','08','09'],8:['19','20','25']},
'C':{1:['01'],2:['02'],3:['03'],4:['04'],5:['05'],6:['06'],7:['07'],8:['08'],9:['09'],10:['19'],11:['14'],12:['20'],13:['10'],14:['11'],15:['15'],16:['17','18','26'],17:['21']}}
decisions=[]
for n,loc,a,b,c,cd in spec:
 maps=dict(zip(roles,[a,b,c])); prov={}; choices={}; croprefs=[]
 for role in roles:
  src=[copy.deepcopy(rows[role][s]) for s in maps[role]]
  ex=extract(readings[role],n)
  choices[role]='; '.join(s['id']+': '+s['reading'] for s in src) if src else ('Reader TeX local excerpt: '+ '\n'.join(z['exact_excerpt'] for z in ex) if ex else 'No local report row or separately added path in this reader TeX.')
  prov[role]={'report_path':f'out/readers/010/{role}/report.json','source_row_ids':maps[role],'source_rows':src,'choice_source':'exact report rows and exact local reader TeX','tex_path':f'out/readers/010/{role}/reading.tex','tex_excerpts':ex,'reported_diff_C':[s['diff_C'] for s in src], 'scope_note':'Compound source rows are retained verbatim; this decision uses only the physical local identity named by location.'}
  for s in src:
   for p in [s.get('readers_crop')]+s.get('additional_crops',[]):
    if p:croprefs.append(f'out/readers/010/{role}/{p}')
 sources=[]
 for role in roles:
  for index,ns in doubt_map[role].items():
   if n in ns:sources.append({'reader':role,'source_doubt_index':index,'doubt_exact':copy.deepcopy(reports[role]['doubts'][index-1]),'local_identity':loc,'compound_source':len(ns)>1})
 cb=extract(base,n)
 concise_C=next((s['C'] for role in roles for s in prov[role]['source_rows']), 'No separate path at this local identity in witness C.tex.')
 decisions.append({'id':did(n),'location':loc,'C':concise_C,'C_tex_excerpts':cb,'H':None,'final':None,'evidence':None,'crop':None,'confidence':None,'kind':'drawing or diagram','diff_C':None,'diff_H':False,'marked_in_H':'not applicable: hua_has=desc','C_doubt_status':None,'C_doubt_source_row':cd,'root_decided':False,'main_approval_pending':True,'readers':choices,'reader_provenance':prov,'candidate_crop_references':list(dict.fromkeys(croprefs)),'source_doubts':sources,'count_locus_key':f'scan010-physical-{n}','main_counting_decision_pending':True})
source_row_coverage={r:[] for r in roles}
for role in roles:
 for row in reports[role]['differences']:
  ids=[d['id'] for d in decisions if row['id'] in d['reader_provenance'][role]['source_row_ids']]
  assert ids,(role,row['id'])
  source_row_coverage[role].append({'source_row_id':row['id'],'decision_ids':ids,'reading_exact':row['reading'],'reported_diff_C':row['diff_C'],'reported_diff_H':row['diff_H'],'C_doubt_status':row.get('C_doubt_status'),'source_row_count':1})
# One record per actual source-table row, with local subloci explicitly listed.
doubts_source=(R/'packets/010/C_doubts.txt').read_text().splitlines()
actual=[];active=False
local_cd={1:['01'],2:['02','03','04'],3:['05'],4:['06'],5:['07','08','09']}
for lineno,line in enumerate(doubts_source,1):
 if line=='## Doubtful readings':active=True;continue
 if active and line.startswith('## '):active=False
 if active and line.startswith('| 10 |'):
  rownum=len(actual)+1
  rr={}
  for role in roles:
   sr=[]
   for row in reports[role]['differences']:
    if row.get('C_doubt_status'):
     found=[d for d in decisions if d['C_doubt_source_row']==rownum and row['id'] in d['reader_provenance'][role]['source_row_ids']]
     if found:sr.append(row)
   rr[role]={'source_row_ids':[x['id'] for x in sr],'statuses':[x['C_doubt_status'] for x in sr]}
  actual.append({'source_path':'packets/010/C_doubts.txt','source_line':lineno,'source_row':rownum,'source_row_count':1,'exact_source_row':line,'decision_ids':[did(n) for n in local_cd[rownum]],'local_subloci':[{'decision_id':did(n),'location':next(d['location'] for d in decisions if d['id']==did(n))} for n in local_cd[rownum]],'root_status':None,'reader_statuses':rr})
assert len(actual)==5
# Inventory: preserve the 51 source identities, split compound objects explicitly,
# then merge only objects whose exact positions identify the same local mark.
cinv=json.loads((R/'packets/010/C_inventory.json').read_text())
inv=[]
for k,src in enumerate(cinv,1):
 item={f:src[f] for f in ['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']}
 item['element']=f'010.I{k:02}'
 item['hand']='undetermined hand' if k in [1,29,34,50,51] else 'his hand'
 item['transcribed']=None
 item['source_inventory']={}
 item['source_element_ids']={r:[] for r in ['witness_C',*roles]}
 item['decision_ids']=[]
 item['main_approval_pending']=True
 inv.append(item)
# Refined descriptions are inventory labels, with the source descriptions retained below.
for k,text in {11:'grouping brace below upper disks 4 and 5',22:'ou',33:'crossed disk and two lower arches; superposed traces separately inventoried',34:'existing main pale curl',47:'final lower disk with two adjoining thickened segments; readers differ in inventory wording of stroke count'}.items():inv[k-1]['first_words_or_objects']=text
extras=[
(52,'drawing','below upper disks 4 and 5','oval enclosing three dots','his hand',[]),
(53,'drawing','around upper-right variant','two drawn parentheses enclosing ou and variant disk','his hand',[]),
(54,'drawing','above final middle disk','projecting broken dark/pale trace','undetermined hand',['02']),
(55,'drawing','inside final middle disk left of crossing','detached tapered dark blob','undetermined hand',['02']),
(56,'drawing','inside final middle disk above outer lower arch','small detached dark spot','undetermined hand',['12']),
(57,'drawing','right middle open space below main curl','two tiny detached flecks','undetermined hand',['09']),
(58,'drawing','right middle open space above-right of main curl','separate smaller pale trace','undetermined hand',['14']),
(59,'drawing','below/right of upper second graph','pale detached curved trace','undetermined hand',['19']),
(60,'drawing','between lower first and second disks','pale diagonal trace','undetermined hand',['20']),
(61,'drawing','below lower-left outline of lower second disk','small pendant stroke','undetermined hand',['23']),
(62,'drawing','inside right angular foot group','separate pale diagonal','undetermined hand',['15']),
(63,'drawing','upper part of right angular foot group','short darker upright fragment','undetermined hand',['17']),
(64,'drawing','beside upper right angular-foot fragment near (1567,921)','separate small dot','undetermined hand',['18']),
(65,'drawing','above-left of upper right angular-foot endpoint near (1550,894)','small gray spot','undetermined hand',['26']),
(66,'drawing','right of upper right angular-foot endpoint near (1603,930)','small gray patch','undetermined hand',['27']),
(67,'drawing','inside first lower disk','pale horizontal trace with faint left continuation','undetermined hand',['22']),
(68,'drawing','far-right margin level with lower row','pale irregular patch','undetermined hand',['21']),
(69,'text','lower-left archive margin','9; % archive sheet number: 9','another unnamed hand',[]),
(70,'drawing','beside descending stroke of upper variant disk','short fragments and two detached dots','undetermined hand',['13']),
(71,'drawing','lower second disk above its small pendant','pale descending vertical trace','undetermined hand',['24']),
(72,'drawing','above upper fourth disk','broken pale descending trace and darker small piece','undetermined hand',['25']),
(73,'drawing','below right angular foot group','detached short slanted dash','undetermined hand',['16']),
(74,'drawing','above/right of middle vertex under upper seventh disk','projecting short hook','his hand',['06']),
(75,'drawing','below lower rim of first middle disk','existing pale descending continuation from about (192,503) to (195,556)','undetermined hand',[]),
(76,'drawing','above/left of upper variant disk','existing pale curved arc from about (1548,116) toward (1584,102)','undetermined hand',[]),
(77,'drawing','inside final lower disk near (1165,877)','small detached short upright/slanted mark','undetermined hand',['28']),
]
for k,kind,pos,desc,hand,ds in extras:inv.append({'sheet_kind':'text','hand':hand,'element':f'010.I{k:02}','kind':kind,'position':pos,'first_words_or_objects':desc,'transcribed':None,'source_inventory':{},'source_element_ids':{r:[] for r in ['witness_C',*roles]},'decision_ids':[did(n) for n in ds],'main_approval_pending':True})
invbase={'01':['07'],'18':['06'],'34':['08'],'40':['01'],'41':['05'],'42':['05'],'46':['10'],'49':['11'],'50':['03'],'51':['04']}
for k,ds in invbase.items():inv[int(k)-1]['decision_ids']=[did(n) for n in ds]
extra_maps={
'A':{'010.52':[69],'010.53':[56],'010.54':[70],'010.55':[62],'010.56':[73],'010.57':[63,64],'010.58':[59],'010.59':[60],'010.60':[68],'010.61':[67],'010.62':[61]},
'B':{'010.B.52':[53],'010.B.53':[69],'010.B.54':[55],'010.B.55':[54],'010.B.56':[56],'010.B.57':[74],'010.B.58':[61],'010.B.59':[71],'010.B.60':[72],'010.B.61':[59],'010.B.62':[60],'010.B.63':[58],'010.B.64':[67],'010.B.65':[62],'010.B.66':[63],'010.B.67':[64],'010.B.68':[65],'010.B.69':[66],'010.B.70':[73]},
'C':{'010.11a':[52],'010.22a':[53],'010.33a':[54],'010.33b':[55],'010.33c':[56],'010.34a':[57],'010.34b':[58],'010.52':[59],'010.53':[60],'010.54':[61],'010.55':[62],'010.56':[63,64,65],'010.57':[67],'010.58':[68],'010.59':[69]}}
inv_coverage={r:[] for r in ['witness_C',*roles]}
for role,items in [('witness_C',cinv)]+[(r,reports[r]['inventory']) for r in roles]:
 for source in items:
  sid=source['element']
  if sid in extra_maps.get(role,{}):targets=extra_maps[role][sid]
  else:
   k=int(sid.split('.')[1]);targets=[k]
   if k==11 and role!='C':targets=[11,52]
   if k==22 and role in ['witness_C','A']:targets=[22,53]
   if k==33 and role in ['witness_C','A']:targets=[33,55]
   if k==34:targets=[34,57,58] if role=='A' else [34] if role=='C' else [34,57]
   if k==24:targets=[24,75]
   if k==23:targets=[23,76]
  inv_coverage[role].append({'source_element_id':sid,'merged_element_ids':[f'010.I{k:02}' for k in targets],'source_item_exact':copy.deepcopy(source)})
  for k in targets:
   inv[k-1]['source_element_ids'][role].append(sid)
   inv[k-1]['source_inventory'].setdefault(role,[]).append(copy.deepcopy(source))
# Source TeX variants retain every non-equal opcode, including comments and boxing.
texaudit={}
for role in roles:
 q=readings[role].splitlines(); blocks=[]
 for idx,(tag,a,b,c,d) in enumerate(difflib.SequenceMatcher(a=baselines,b=q,autojunk=False).get_opcodes(),1):
  if tag=='equal':continue
  matched=[]
  for decision in decisions:
   ex=decision['reader_provenance'][role]['tex_excerpts']
   bx=decision['C_tex_excerpts']
   if any(max(c+1,z['line_start'])<=min(d,z['line_end']) for z in ex) or any(max(a+1,z['line_start'])<=min(b,z['line_end']) for z in bx):matched.append(decision['id'])
  content='\n'.join(q[c:d]+baselines[a:b])
  comments_only=all(not x.strip() or x.lstrip().startswith('%') for x in q[c:d]+baselines[a:b])
  blocks.append({'opcode_id':f'{role}-T{len(blocks)+1:02}','operation':tag,'C_line_start':a+1,'C_line_end':b,'reader_line_start':c+1,'reader_line_end':d,'C_exact':'\n'.join(baselines[a:b]),'reader_exact':'\n'.join(q[c:d]),'decision_ids':matched,'classification':'editorial comments only' if comments_only else 'local source variant; final treatment pending','mapped':bool(matched) or comments_only,'source_only_check':True})
 texaudit[role]=blocks
source_doubt_coverage={r:[{'source_doubt_index':i,'decision_ids':[did(n) for n in ns],'doubt_exact':copy.deepcopy(reports[r]['doubts'][i-1]),'mapping_basis':'exact local identity from location/difference_id; crop sharing alone unused'} for i,ns in doubt_map[r].items()] for r in roles}
sourcepaths=[f'out/readers/010/{r}/{f}' for r in roles for f in ['reading.tex','report.json','reading.md']]+['packets/010/'+f for f in ['C.tex','H.tex','C_doubts.txt','C_notes.txt','metadata.json','C_inventory.json']]
fingerprints={p:{'sha256':hashlib.sha256((R/p).read_bytes()).hexdigest(),'bytes':(R/p).stat().st_size} for p in sourcepaths}
assert all(not r.get('check_events') for r in reports.values()),'Reader checks require exact event schema mapping; do not infer or discard.'
record={'scan':10,'folder':meta['folder'],'their_page':meta['their_page'],'hua_has':meta['hua_has'],'filename':'J81-01_81_scan010.tex','brief_version':None,'main_adjudicated':False,'main_approved_utc':None,'draft_status':'Mechanical source assembly; root crop adjudication pending.','decisions':decisions,'doubts':[], 'proposed_doubts':[{'decision_id':d['id'],'location':d['location'],'reading':None,'alternatives':None,'confidence':None,'reason':None,'source_doubts':d['source_doubts'],'root_status':None} for d in decisions if d['source_doubts']], 'inventory':inv,'notes':None,'abbreviations':[{'form':'OK','expansion':'okay','source':'packets/010/C_doubts.txt, Abbreviations; literal OK retained in all reader TeX'}],'check_events':[],'workflow_note':'Mechanical assembly reads textual packet/report/TeX sources only. No image, crop, ink, mathematical, compilation, or final-page decision made.','source_reports':reports,'source_readings':readings,'source_audits':audits,'source_fingerprints':fingerprints,'root_adjudication_notes_exact':None,'root_page_text_exact':None,'actual_C_doubt_map':actual,'C_doubt_source_classification':{'actual_doubt_count':5,'actual_doubt_source_lines':[x['source_line'] for x in actual],'notation_source_lines':[i for i,x in enumerate(doubts_source,1) if x.startswith('| 10 |') and i<actual[0]['source_line']],'source_doubt_counting':'Five source-table rows; rows 2 and 5 each have three explicit local subloci. Local subloci do not inflate the source-row count.'},'source_row_coverage':source_row_coverage,'source_doubt_coverage':source_doubt_coverage,'inventory_coverage':inv_coverage,'reader_tex_difference_coverage':texaudit,'unchanged_audit':[{'location':'Archive numeral in TeX comment','C':'% archive sheet number: 9','readers':{r:[excerpt(readings[r].splitlines(),i,i+1) for i,l in enumerate(readings[r].splitlines()) if l=='% archive sheet number: 9'] for r in roles},'inventory_element':'010.I69','diff_C':False,'diff_H':False,'note':'Retained exact comment in all three readers; no display-page numeral introduced by this draft.'}],'counting_policy':'Main final fields remain null. Source report rows count once even when compound rows map to several identities. A decision denotes one physical local identity; state/boxing at the overdrawn disk share D05, middle-vertex fill/hook share D06, and paired upper traces share D07 with explicit component evidence. No separate C change is assigned for repeat phantom paths, comments, or macro syntax. H desc supplies no H text-collation rows.','counts':{'decision_loci':len(decisions),'C_difference_loci':None,'H_difference_loci':0,'actual_C_doubt_source_rows':5,'actual_C_doubt_local_subloci':9,'actual_C_doubts_retained':None,'actual_C_doubts_resolved':None,'remaining_doubt_or_graphic_uncertainty_loci':None,'inventory_elements':len(inv),'source_difference_rows':{r:len(reports[r]['differences']) for r in roles},'source_inventory_rows':{r:len(reports[r]['inventory']) for r in roles},'source_doubt_rows':{r:len(reports[r]['doubts']) for r in roles},'check_events':0},'assembly_timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'assembly_revision':'initial mapped draft; coverage review ongoing','approval_followups':[]}
(OUT/'scan010_record_draft.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
md=['# Scan 010 — mechanical source coverage','', 'Draft only. `main_adjudicated=false`; final readings, crop decisions, confidence, and C differences are null. H status is `desc`; every H field is null and every `diff_H` is false.','',f"27 local decision records; 66 report rows (A 19, B 25, C 22); 74 merged inventory elements. Five original C doubt rows map to nine local subloci without increasing their source-row count.",'','## Physical-locus / source-row map','','| Decision | Local identity | A rows | B rows | C-reader rows | Original C doubt row |','| --- | --- | --- | --- | --- | --- |']
for d in decisions:md.append('| '+' | '.join([d['id'],d['location'],*[', '.join(d['reader_provenance'][r]['source_row_ids']) or 'TeX only / no separate path' for r in roles],str(d['C_doubt_source_row'] or '—')])+' |')
md+=['','## TeX-difference coverage','','Every non-equal source opcode is retained verbatim in `reader_tex_difference_coverage`. Boxing duplicates and source comments are retained without creating new physical-change loci.','', '| Reader | Non-equal opcodes | Mapped or editorial | Pending unmapped |','| --- | --- | --- | --- |']
for r in roles:md.append(f"| {r} | {len(texaudit[r])} | {sum(x['mapped'] for x in texaudit[r])} | {', '.join(x['opcode_id'] for x in texaudit[r] if not x['mapped']) or 'none'} |")
md+=['','## Inventory map','','| Merged element | Object / local identity | Witness C IDs | A IDs | B IDs | C-reader IDs |','| --- | --- | --- | --- | --- | --- |']
for i in inv:md.append('| '+' | '.join([i['element'],i['position']+' — '+i['first_words_or_objects'],*[', '.join(i['source_element_ids'][r]) or '—' for r in ['witness_C',*roles]]])+' |')
md+=['','## Source-doubt identity safeguards','','Original C doubt row 2 maps only to final-middle trace/blob, left foot trace, and right foot trace (D02–D04). Original C doubt row 5 maps only to the upper pair, existing right curl, and right flecks (D07–D09). Newly added spots and traces retain their own decisions. No lower-graph endpoint doubt is attached to a foot-trace decision merely because they share a crop.','', 'Every source inventory row is retained verbatim with its original identifier. Unknown detached and residual marks use `undetermined hand`; the archive 9 comment uses the readers’ `another unnamed hand`. Inventory transcription status remains pending root approval.','', 'Reader checks are empty. No mathematical check is inferred from the question mark, OK labels, or structural checks.','', 'Exact candidate-order disagreement: D10 lower-middle first vertex A/C `\\circ|\\bullet`, B `\\bullet|\\circ`; D11 final-lower first vertex A `\\circ|\\bullet`, B/C `\\bullet|\\circ`. A has no outer unsure wrapper on the overdrawn disk; B/C do. All exact TeX is preserved.','']
(OUT/'scan010_mapping.md').write_text('\n'.join(md))
print(json.dumps({'draft':str(OUT/'scan010_record_draft.json'),'decisions':len(decisions),'source_rows':{r:len(reports[r]['differences']) for r in roles},'inventory':len(inv),'unmapped_tex_opcodes':{r:[x['opcode_id'] for x in texaudit[r] if not x['mapped']] for r in roles},'checks':0}))
