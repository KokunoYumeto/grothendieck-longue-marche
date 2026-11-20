"""Mechanical scan015 union. No manuscript images or final ink decisions."""
import json, hashlib, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
OUT=ROOT/'checks'
def read(p): return p.read_text()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
reports={r:json.loads(read(ROOT/f'readers/015/{r}/report.json')) for r in 'ABC'}
tex={r:read(ROOT/f'readers/015/{r}/reading.tex') for r in 'ABC'}
md={r:read(ROOT/f'readers/015/{r}/reading.md') for r in 'ABC'}
packet={p.name:read(p) for p in (BASE/'packets/015').iterdir() if p.is_file()}
source_map=json.loads(read(OUT/'scan015_source_map.json'))
metadata=json.loads(packet['metadata.json'])
index={r:{x['id']:(i,x) for i,x in enumerate(reports[r]['differences'])} for r in 'ABC'}
manifest={}
def addfile(key,p):
 manifest[key]={'path':str(p.relative_to(BASE)),'sha256':sha(p),'bytes':p.stat().st_size}
for r in 'ABC':
 for name in ['report.json','reading.tex','reading.md']:addfile(r+'.'+name,ROOT/f'readers/015/{r}/{name}')
for p in (BASE/'packets/015').iterdir():
 if p.is_file():addfile('packet.'+p.name,p)
for name in ['scan015_source_map.json','scan015_witness_attention.md','scan015_source_geometry_attention.md']:
 addfile(name,OUT/name)
def ref(r,section,i):
 row=reports[r][section][i]
 return {'manifest':r+'.report.json','pointer':f'/{section}/{i}','row_id':row.get('id',row.get('element',f'{section}[{i}]'))}
def bbox(v):
 if isinstance(v,dict):return v.get('xyxy',v.get('coordinates'))
 return v
def cropref(r,x):
 n=x.get('readers_crop',x.get('crop'))
 if not n:return None
 p=ROOT/f'readers/015/{r}'/n
 return str(p.relative_to(ROOT)) if p.exists() else 'MISSING: '+str(p.relative_to(ROOT))
decisions=[]
def add(key,loc,aliases=None,C=None,H=None,parent_H=None,parent_C=None,parts=None,kind=None):
 aliases=aliases or {}
 rs={};refs={};evidence=[];boxes={};crops=[];proposals={};sources=[]
 for r,ids in aliases.items():
  if isinstance(ids,str):ids=[ids]
  rr=[];refs[r]=[];proposals[r]=[]
  for rid in ids:
   i,x=index[r][rid];rr.append(x.get('reading',''));refs[r].append(ref(r,'differences',i))
   proposals[r].append({k:x.get(k) for k in ['id','confidence','diff_C','diff_H','C_doubt_status','qualification','interpretation_confidence','boundary_limit'] if k in x})
   evidence.append({'reader':r,'source_id':rid,'excerpt':x.get('evidence','')})
   if x.get('bbox'):boxes[r+':'+rid]=bbox(x['bbox'])
   cr=cropref(r,x)
   if cr and cr not in crops:crops.append(cr)
   sr=x.get('C_source_row',x.get('C_source_doubt_row'))
   if sr and sr not in sources:sources.append(sr)
  rs[r]=' ; '.join(rr)
 primary=next((index[r][(ids if isinstance(ids,str) else ids[0])][1] for r,ids in aliases.items()),{})
 d={'id':'015-'+key,'location':loc,'C':C if C is not None else primary.get('C'),
    'H':H if H is not None else primary.get('H'),'final':'[PENDING ROOT INK DECISION]',
    'readers':rs,'reader_provenance':refs,'reader_proposals':proposals,
    'evidence':'Provisional mechanical union; root crop adjudication pending.',
    'reader_evidence':evidence,'crop':crops[0] if crops else None,'available_crops':crops,
    'full_scan_boxes':boxes,'confidence':'low','confidence_status':'pending root; individual returned confidences retained in reader_proposals',
    'kind':kind or primary.get('kind','other'),'diff_C':False,'diff_H':False,
    'count_status':'pending root','C_doubt_status':'pending root' if sources else None,
    'source_C_doubt_rows':sources,'marked_in_H':'pending exact source comparison',
    'mathematical_consequence':None,'main_approved':False,'log_decision':True,
    'final_source_attachment':None}
 if parent_H:d['H_count_parent']='015-'+parent_H;d['H_count_policy']='zero on child; one shared parent count'
 if parent_C:d['C_count_parent']='015-'+parent_C;d['C_count_policy']='zero on child; parent carries shared physical count'
 if parts:d['component_scope']=parts
 decisions.append(d);return d
common=[x['id'] for x in reports['A']['differences'][:24]]
for rid in common:
 a=index['A'][rid][1]
 add(rid,a['location'],{r:rid for r in 'ABC'},parent_H=('H-DRAW' if rid in ['D10','D11'] else 'H17' if rid=='D16' else None))
rows=[
 ('H01','upper-left note opening',{'A':'H01','B':'H01','C':'H02'}),
 ('H02','condition (a): Card capitalization',{'A':'H02','B':'H08','C':'H05'}),
 ('H03','condition (a): covered Sigma',{'A':'H03','B':'H05','C':'H06'}),
 ('H04','upper-right NB underline',{'A':'H04','B':'H10','C':'H08'}),
 ('H05','condition (b): first covered Sigma/E_j',{'A':'H05','B':'H06','C':'H07'}),
 ('H06','main NB: Cette capitalization',{'A':'H06','B':'H03','C':'H09'}),
 ('H07','main NB: ill placeholder and si between automatiquement and les',{'A':'H07','B':'H02','C':'H10'}),
 ('H08','main NB: covered Sigma under first E_i',{'A':'H08','B':'H07','C':'H11'}),
 ('H09','main NB: endpoint after mutuellement',{'A':'H09','B':'H11','C':'H12'}),
 ('H10','case heading: Card capitalization',{'A':'H10','B':'H09','C':'H13'}),
 ('P01','first cancelled inclusion relative to équivaut à',{'A':'P01','B':'H13','C':'G07'}),
 ('H11','first équivaut à: terminal colon',{'A':'H11','B':'H14','C':'H14'}),
 ('P02','cancelled Si on avait: placement',{'A':'P02','B':'H17','C':'H15'}),
 ('H12','aussi à: terminal colon',{'A':'H12','B':'H15','C':'H16'}),
 ('H13','symmetry phrase: terminal colon',{'A':'H13','B':'H16','C':'H17'}),
 ('P07','cancelled vois. ouvert: raised placement',{'A':'P07','B':'H18','C':'H18'}),
 ('P08','inserted i.e. clause above cancelled il contient les: state and placement',{'A':'P08','B':'H19','C':'H19'}),
 ('H14','inserted vois.: underline span and abbreviation point',{'A':'H14'}),
 ('H15','on a: last letter qualification',{'A':'H15','B':'H20','C':'H20'}),
 ('H17','lower slanted note: entire tail represented by H ill placeholder',{'A':'H17','B':'H04','C':'H26'}),
 ('H18','final justification: Car capitalization',{'A':'H18','B':'H21','C':'H21'}),
 ('P09','l\'ouvert insertion: wording and placement before Sigma',{'A':'P09','B':'H23','C':'H23'}),
 ('G01','detached oval left of opening Soient',{'A':'G01','B':'G01'}),
 ('G02','curved opening insertion guide',{'A':'G02','B':'GUIDE01','C':'G01'}),
 ('G03','case underline: long run and separate run under 2',{'A':'G03','B':'G11','C':'G02'}),
 ('G04','crossed upper drawing label: local cancellation paths',{'A':'G04','B':'G09','C':'G04'}),
 ('G05','detached dot above right drawing exponent',{'A':'G05','B':'G03','C':'G05'}),
 ('G06','cancelled car si: two crossing runs',{'A':'G06','B':'G10','C':'G06'}),
 ('G07','two detached points above first cancelled inclusion',{'A':'G07'}),
 ('G08','two detached spots far right of display (2)',{'A':'G08','B':'G04'}),
 ('G09','detached short curve below cancelled vois. ouvert',{'A':'G09','B':'G05','C':'G09'}),
 ('G10a','lower slanted note: short curved arrow',{'A':'G10'}),
 ('G10b','lower slanted note/display: separate longer bent curve',{'A':'G10','B':'G06','C':'G10'}),
 ('G11','Car closure-intersection formula: underline span and shape',{'A':'G11','B':'H22','C':'H22'}),
 ('G12','final cancelled group: full crossing-path cluster',{'A':'G12','C':'G12'}),
 ('G13','central drawing: lower-right rim continuity',{'A':'G13','B':'G08','C':'G03'}),
 ('G14','first cancelled inclusion: cancellation-line geometry',{'A':'G14'}),
 ('H-TITLE','heading: underline includes predecessor',{'B':'D01a','C':'H01'}),
 ('H-ARROW','upper-left note: arrow to (a)',{'C':'H03'}),
 ('H-COMMA','upper-left note: comma before second i.e.',{'B':'H12','C':'H04'}),
 ('G-NB-RULE','right NB: separate stroke above first Sigma',{'B':'G02'}),
 ('G-REMNANT','final cancelled group: upper remnant paths',{'B':'G07','A':'G12','C':'G12'}),
 ('G-SYM-ACCENT','symmetry word: acute/grave accent',{'C':'G08'}),
 ('G-LOUVERT','curved guide beneath l\'ouvert',{'A':'P09','B':'G12','C':'G11'}),
 ('H-DRAW','central drawing: one H descriptive-apparatus parent',{'B':'H24','C':'G03'}),
]
for key,loc,aliases in rows:
 hp='H-DRAW' if key in ['G04','G05','G13'] else 'H17' if key in ['G10a','G10b'] else 'D13' if key=='G06' else 'D19' if key in ['G12','G-REMNANT'] else 'P09' if key=='G-LOUVERT' else None
 cp='G12' if key=='G-REMNANT' else None
 add(key,loc,aliases,parent_H=hp,parent_C=cp)
add('D12-accent','équivaut: acute/grave accent component',{'A':'D12','B':'D12','C':'D12'},parent_C='D12',parts='Accent component is independently documented; source C row12 stays one actual row.')
add('D11-old','right drawing exponent: covered plus state',{'A':'D11','B':'D11','C':'D11'},parent_C='D11',parent_H='H-DRAW',parts='Covered predecessor, separately qualified from live minus; same physical exponent parent.')
add('D11-live','right drawing exponent: live minus qualification',{'A':'D11','B':'D11','C':'D11'},parent_C='D11',parent_H='H-DRAW',parts='Live minus, separately qualified from covered plus; same physical exponent parent.')
add('H15-colon','on a: terminal colon',{'A':'H15','B':'H20','C':'H20'},C='on a',H='on a :',parent_C='H15',parent_H='H15',parts='Terminal punctuation independent of A\'s newly qualified last a; one shared on-a endpoint count.')
add('P09-apostrophe','inserted l\'ouvert: apostrophe qualification',{'A':'P09','B':'H23','C':'H23'},parent_C='P09',parent_H='P09',parts='C-reader qualifies apostrophe only; retain its local confidence.')
add('P09-commas','l\'ouvert insertion: surrounding commas',{'A':'P09','B':'H23','C':'H23'},parent_C='P09',parent_H='P09',parts='H supplies comma after Sigma and within added ouvert; reader text has neither comma.')
for key,loc in [('upper-right','upper-right rim gap'),('left-edge','left rim and hooked return'),('left-brace1','first left-brace run'),('left-brace2','second retraced left-brace run'),('right-brace','right brace'),('chord1','upper chord'),('chord2','lower chord')]:
 add('DRAW-'+key,'central drawing: '+loc,{'B':'H24','C':'G03'},parent_C='G13' if key in ['upper-right','left-edge'] else None,parent_H='H-DRAW',parts='Local component of broad B H24/C G03 report rows; inspect exact literal drawing paths. No independent absent reading inferred from a missing dedicated report row.')
for key in ['E1','E2','Sigma1plus','Sigma1minus','Sigma2minus','Sigma2plus']:
 add('DRAW-label-'+key,'central drawing: live label '+key,parent_H='H-DRAW',parts='Audit of individually retained live label from all three reading.tex drawings; overwritten sign handled at D11.')
add('S-NOTE-FIRST','lower-left note: first closure/intersection and inequality audit',C=r'\overline{\Sigma_1^+}\cap E_1\ne\varnothing',H=r'\overline{\Sigma_1^+}\cap E_1\neq\emptyset',kind='other')
add('S-NOTE-SECOND','lower-left note: closure inequality after i.e.',{'A':'H17','B':'H04','C':'H26'},C=r'\overline{\Sigma_1^+}\ne\Sigma_1^+',H=r'\ill{}',parent_H='H17',kind='other')
add('S-FINAL','final prose: closure/intersection overbar audit',C=r'\underline{\overline{\Sigma_1^+}\cap E_1}\ne\varnothing',H=r'\overline{\Sigma_1^+}\cap E_1\neq\emptyset',kind='other')
for d in decisions:
 if d['id'] in ['015-S-NOTE-FIRST','015-S-NOTE-SECOND','015-S-FINAL']:
  d.update(S_id=source_map['S_id'],S_status='pending root ink confirmation; current C and H bar comparison retained locally')
 for r in 'ABC':
  if r not in d['readers']:d['readers'][r]='[No dedicated report row mapped; complete-source attachment pending]'
byid={d['id']:d for d in decisions}
byid['015-H-DRAW'].update(C='Oval, two chords, three brace paths, six live labels, crossed label and corrected right exponent; packet.C.tex drawing block',H='Descriptive drawing apparatus: disk, two horizontal chords E_1/E_2, four Sigma region labels, left and right braces; packet.H.tex drawing block',count_policy='one H parent count for the entire descriptive drawing; all local children have zero H count')
byid['015-H17'].update(H=r'\ill{}',H_span='Final marginal note: immediately after first barred Sigma intersection E_1 inequality; covers i.e., second closure inequality, instruction before avant, and local attached guides.',count_policy='one H count for this entire placeholder; D16, G10a, G10b and S-NOTE-SECOND have zero H count')
crosswalk=[]
for r in 'ABC':
 for i,x in enumerate(reports[r]['differences']):
  targets=[d['id'] for d in decisions if any(z['pointer']==f'/differences/{i}' for z in d['reader_provenance'].get(r,[]))]
  assert targets,(r,i,x['id'])
  crosswalk.append({'reader':r,'pointer':f'/differences/{i}','source_id':x['id'],'loci':targets})
actual=[]
for row in source_map['source_doubt_rows']:
 n=row['source_row'];targets=[d['id'] for d in decisions if n in d['source_C_doubt_rows']]
 actual.append({'source_row':n,'source_line':row['source_line'],'source_manifest':'packet.C_doubts.txt','local_loci':row.get('local_loci'), 'decision_ids':targets,'status':'pending root'})
def esc(s):return str(s).replace('|','\\|').replace('\n','<br>')
lines=['# Scan015 — compact provisional union','', 'Source-only assembly; no manuscript image inspected and no final ink choice made. Stable IDs identify independently variable local components. Source rows may map to multiple component records; that mapping does not multiply physical difference counts.','',f'Coverage: A60 + B61 + C60 = {len(crosswalk)} source difference rows; 21 actual C doubt rows / 24 primary local loci. Every raw source row remains linked by manifest key and JSON pointer.','', 'H drawing: 015-H-DRAW is the one H count parent. H lower-note placeholder: 015-H17 is the one H count parent. All child rows explicitly log decisions while carrying zero H count.','', '| Locus | C source row | Physical location / components | C | H | A | B | C-reader | Full-scan boxes / existing crop paths |','|---|---|---|---|---|---|---|---|---|']
for d in decisions:
 loc=d['location']
 if d.get('H_count_parent'):loc+='; H parent '+d['H_count_parent']
 if d.get('C_count_parent'):loc+='; C parent '+d['C_count_parent']
 vals=[d['id'],','.join(map(str,d['source_C_doubt_rows'])) or '—',loc,d['C'],d['H'],*[d['readers'][r] for r in 'ABC'],json.dumps(d['full_scan_boxes'],ensure_ascii=False)+'; '+'; '.join(d['available_crops'])]
 lines.append('| '+' | '.join(esc(x) for x in vals)+' |')
lines+=['','## Exact source-row crosswalk','','| Source | JSON pointer | Source row ID | Union local component IDs |','|---|---|---|---|']
for row in crosswalk:lines.append('| '+' | '.join(map(esc,[row['reader']+'.report.json',row['pointer'],row['source_id'],', '.join(row['loci'])]))+' |')
lines+=['','## C source categories','','21 actual doubtful-reading rows remain doubts. Seven notation rows, three slips-retained rows, and seven abbreviation rows remain in their original categories. The three compound doubtful-reading rows retain identities 1 (predecessor/Version), 9 (parenthetical/relation), and 21 (abbreviation/index).','', '## Pending root actions','','Resolve every local reading against crops; settle physical count parents and confidences; supply exact final-source attachments; confirm hand choices; inspect S overbar targets. Reader crop boundaries are recorded in the reports and remain limitations of those particular reader returns. The draft never turns a missing dedicated source row into reader unanimity.']
(OUT/'scan015_union.md').write_text('\n'.join(lines)+'\n')
draft={'scan':15,'folder':metadata['folder'],'their_page':metadata['their_page'],'hua_has':metadata['hua_has'],'filename':'J81-02_81_scan015.tex','brief_version':source_map['brief_version'],'main_adjudicated':False,'decisions':decisions,'doubts':[],'inventory':[],'notes':'Version I introduces an indexed family and two written conditions, marginal notes, a two-member case, a labelled drawing, relations and a final closure argument. No mathematical proof or computation is recorded by any of the three readers.','abbreviations':[],'check_events':[],'workflow_note':'Mechanical provisional union of all three finalized independent returns. No manuscript images, OCR, research, compiler, renderer or mathematical computation used by record clerk. Root reading decisions and final-source synchronization remain pending.','source_counts':{'reader_differences':{r:len(reports[r]['differences']) for r in 'ABC'},'reader_inventory':{r:len(reports[r]['inventory']) for r in 'ABC'},'C_inventory':len(json.loads(packet['C_inventory.json'])),'C_doubt_rows':21,'C_primary_local_doubts':24},'source_difference_crosswalk':crosswalk,'actual_C_doubt_map':actual,'source_manifest':'checks/scan015_reader_fingerprints.json','root_decision_log':'checks/scan015_main_decisions.md','root_actions_pending':['all ink decisions','all final-source attachments','inventory union and ordered placement (mechanical assembly underway)']}
(OUT/'scan015_record_draft.json').write_text(json.dumps(draft,ensure_ascii=False,indent=2)+'\n')
fingerprints={'scan':15,'files':manifest,'readers':{r:{'agent':source_map['reader_agents'][r],'start_utc':reports[r].get('start_utc'),'end_utc':reports[r].get('end_utc'),'full_image_viewed':reports[r].get('full_image_viewed'),'halves_viewed':reports[r].get('halves_viewed'),'complete_visual_read':reports[r].get('complete_visual_read'),'model':reports[r].get('model'),'reasoning_effort':reports[r].get('reasoning_effort'),'metadata_status':'Model/effort fields are absent from these report files; no values invented.'} for r in 'ABC'},'recorded_launch_metadata':{k:source_map[k] for k in ['fresh_readers','fork_turns','model_override','brief_version']},'provenance_policy':'Original source files unchanged; file hashes occur once here; row attachments cite manifest keys and JSON pointers.'}
(OUT/'scan015_reader_fingerprints.json').write_text(json.dumps(fingerprints,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'union_loci':len(decisions),'source_rows':len(crosswalk),'C_doubt_rows':len(actual),'outputs':['scan015_union.md','scan015_record_draft.json','scan015_reader_fingerprints.json']}))

# Exact textual attachments use character/line spans in immutable source files.
def span(key,text,token,occ=0,until=None):
 starts=[m.start() for m in re.finditer(re.escape(token),text)]
 if not starts:return None
 a=starts[occ];b=a+len(token)
 if until is not None:
  q=text.find(until,b)
  if q>=0:b=q+len(until)
 return {'manifest':key,'char_start':a,'char_end':b,'line_start':text.count('\n',0,a)+1,'line_end':text.count('\n',0,b)+1,'excerpt':text[a:b] if b-a<=160 else text[a:a+120]+'… [exact span retained by offsets]'}
def texspan(r,token,occ=0,until=None):return span(r+'.reading.tex',tex[r],token,occ,until)
def supplement(key,r,reading,token,occ=0,until=None,scope=None):
 d=byid['015-'+key];s=texspan(r,token,occ,until)
 assert s,(key,r,token)
 d.setdefault('reader_tex_provenance',{}).setdefault(r,[]).append(s)
 if r not in d['reader_provenance']:
  d['readers'][r]=reading
  d.setdefault('reader_reading_source',{})[r]='complete reading.tex; no dedicated difference row'
 if scope:d.setdefault('source_scope_notes',{})[r]=scope
for r in 'BC':supplement('H14',r,r'\uline{vois.}',r'\uline{vois.}')
supplement('H-TITLE','A',r'\uline{\deleted{\unsure{I|V}}Version I}',r'\uline{\deleted{\unsure{I|V}}Version I}')
for r in 'AB':supplement('H-ARROW',r,r'\nearrow',r'\nearrow')
supplement('H-COMMA','A',r'\overline{\Sigma}_i\ne\Sigma_i$ i.e.',r'\overline{\Sigma}_i\ne\Sigma_i$ i.e.')
supplement('G01','C','No detached opening mark encoded in the complete heading-to-Soient source span.',r'\uline{',until='un ens. de',scope='This is a textual-source absence at this locus, not a claimed negative image observation.')
for r in 'BC':
 supplement('G07',r,'First cancelled inclusion encoded without a separate two-point mark.',r'\deleted{\Sigma_1^-\supset\Sigma_2^+}',scope='No separate MARK03 analogue occurs in this complete formula source.')
 supplement('G14',r,r'\deleted{\Sigma_1^-\supset\Sigma_2^+}',r'\deleted{\Sigma_1^-\supset\Sigma_2^+}')
supplement('G08','C','No far-right pair encoded between (2) and the symmetry phrase.',r'\tag*{(2)}',until=r'\unsure{symètriquement|symétriquement}')
for r in 'BC':
 supplement('G10a',r,'Lower note and longer curved guide are encoded; no separate short arrow component is supplied.',r'\margin{$\overline{\Sigma_1^+}',until=r'\normalmarginpar')
for r in 'AC':supplement('G-NB-RULE',r,r'\Sigma_i^+ (no separately encoded upper rule)',r'\margin{\uline{NB}',until='sont ouvertes dans $X$}')
for r in 'AB':supplement('G-SYM-ACCENT',r,'symétriquement',r'\unsure{et} symétriquement, à')
supplement('G12','B','Two outer oblique cancellation commands, plus separately qualified G07 local remnants.',r'% Final deleted group:',until=r'$X$ serait disconnexe),')
supplement('H-DRAW','A','C-derived oval, two chords, two left-brace runs, right brace, six live labels, crossed label, qualified exponent, local crossing paths and dot.',r'% Drawing coordinates',until=r'\end{tikzpicture}}')
for key in ['upper-right','left-edge','left-brace1','left-brace2','right-brace','chord1','chord2']:
 token={'upper-right':r'\draw (182,89)','left-edge':r'\draw (376,226)','left-brace1':r'\draw (44,9)','left-brace2':r'\draw (41,109)','right-brace':r'\draw (428,86)','chord1':r'\draw[line width=.8pt] (181,89)','chord2':r'(174,218)'}[key]
 supplement('DRAW-'+key,'A','Exact selected-source path candidate beginning '+token,token,until=';')
 # B/C broad report rows are augmented with local path anchors to avoid attributing all components to one undivided description.
 tokensB={'upper-right':r'\draw (182,89)','left-edge':r'\draw (355,266)','left-brace1':r'\draw (44,9)','left-brace2':r'\draw (41,109)','right-brace':r'\draw (428,86)','chord1':r'\draw[line width=.8pt] (181,89)','chord2':r'(174,218)'}
 tokensC={'upper-right':r'\draw (403,168)','left-edge':r'\draw (168,193)','left-brace1':r'\draw (44,9)','left-brace2':r'\draw (41,109)','right-brace':r'\draw (428,86)','chord1':r'\draw[line width=.8pt] (186,122)','chord2':r'(176,250)'}
 for r,t in [('B',tokensB[key]),('C',tokensC[key])]:supplement('DRAW-'+key,r,'Local path: '+t,t,until=';')
labels={'E1':r'$E_1$','E2':r'$E_2$','Sigma1plus':r'$\Sigma_1^+$','Sigma1minus':r'$\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}$','Sigma2minus':r'$\Sigma_2^-$','Sigma2plus':r'$\Sigma_2^+$'}
for key,token in labels.items():
 for r in 'ABC':
  m=next((line for line in tex[r].splitlines() if '\\node' in line and token in line),None)
  assert m,(r,key)
  supplement('DRAW-label-'+key,r,token,m)
for r in 'ABC':
 supplement('S-NOTE-FIRST',r,r'\overline{\Sigma_1^+}\cap E_1\ne\varnothing',r'\overline{\Sigma_1^+}\cap E_1\ne\varnothing')
 supplement('S-NOTE-SECOND',r,r'\overline{\Sigma_1^+}\ne\Sigma_1^+',r'\overline{\Sigma_1^+}\ne\Sigma_1^+')
 token=r'\overline{\Sigma_1^+}\cap E_1'
 supplement('S-FINAL',r,token,token,occ=-1)
source_literal={
 'D01a':(r'\deleted{\unsure{I|V}}',r'\struck{V}'),
 'D01b':(r'\unsure{Version}','Version'),
 'D02':(r'\deleted{\unsure{\Sigma|S}}E_i',r'(E_i)_{i\in I}'),
 'D03':(r'\unsure{tte|toute|tt}',r'\uncertain{toute}'),
 'D04':(r'\unsure{non}',r"\uncertain{n'est pas}"),
 'D05':(r'\Sigma_i^{\unsure{+|-|\ast}}',r'\Sigma_i^-'),
 'D06':(r'X\setminus\unsure{\Sigma|E}_i',r'X\setminus E_i'),
 'D07':(r'X\setminus\deleted{\unsure{\Sigma}}E_i.',r'X\setminus E_i.'),
 'D08':(r'\unsure{automatiquement}','automatiquement'),
 'D09a':(r'\deleted{\unsure{(\mathrm{de})}}','[no cancelled parenthetical supplied]'),
 'D09b':(r'\deleted{\unsure{\leq|=}}=2',r'(I)=2'),
 'D10':(r'\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}','[no cancelled label supplied in drawing description]'),
 'D11':(r'\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}',r'\Sigma_1^-'),
 'D12':(r'\unsure{équivaut}','équivaut'),
 'D13':(r'\deleted{\unsure{car si}}','[omitted]'),
 'D14':(r'\unsure{et}','[omitted]'),
 'D15':(r'\deleted{\unsure{vois. ouvert}}',r'\struck{vois.\ ouvert}'),
 'D16':(r'\unsure{à signaler|à sign.ler}',r'\ill{}'),
 'D17':(r'\inserted{\unsure{un|une}}','[omitted]'),
 'D18':(r'\unsure{donc|puis}','donc'),
 'D19':(r'\deleted{\unsure{\Sigma_1^+\text{ serait}}}',r'\struck{$\Sigma_1^+\neq\emptyset$}'),
 'D20':(r'\inserted{\unsure{fermés|fermées}}',r'\add{fermées}'),
 'D21a':(r'\unsure{conn.|connex.}',r'conn.'),
 'D21b':(r'\Sigma_{\unsure{i}}',r'\Sigma_i'),
}
for key,(cv,hv) in source_literal.items():
 d=byid['015-'+key];d['C']=cv;d['H']=hv;d['witness_provenance']={}
 for w,v in [('C',cv),('H',hv)]:
  s=span('packet.'+w+'.tex',packet[w+'.tex'],v)
  d['witness_provenance'][w]=s if s else {'manifest':'packet.'+w+'.tex','scope_note':v}
for key in ['D12-accent','D11-old','D11-live']:
 parent=key.split('-')[0];byid['015-'+key]['source_C_doubt_rows']=byid['015-'+parent]['source_C_doubt_rows']

# Every returned remaining-doubt row is linked once to its local union entry.
doubt_alias={'A':{'H15':'H15'},'B':{'G01':'G01','G02':'G-NB-RULE','G03':'G05','G04':'G08','G05':'G09','G06':'G10b','G07':'G-REMNANT','G08':'G13'},'C':{'H23':'P09-apostrophe','G05':'G05','G08':'G-SYM-ACCENT','G09':'G09','G10':'G10b'}}
remaining={};dcross=[]
for r in 'ABC':
 for i,x in enumerate(reports[r]['doubts']):
  sid=x.get('difference_id',x.get('source_difference'))
  key=doubt_alias[r].get(sid,sid);did='015-'+key
  assert did in byid,(r,i,sid)
  original=index[r][sid][1] if sid in index[r] else {}
  component={'reader':r,'source':ref(r,'doubts',i),'location':x['location'],'reading':x['reading'],'alternatives':x.get('alternatives',[]),'confidence':x['confidence'],'reason':x.get('reason',''),'qualification':x.get('qualification'),'bbox':bbox(original.get('bbox')),'crop':cropref(r,x)}
  remaining.setdefault(did,[]).append(component)
  dcross.append({'reader':r,'pointer':f'/doubts/{i}','source_difference':sid,'locus':did})
draft['doubts']=[]
for did,components in remaining.items():
 d=byid[did]
 draft['doubts'].append({'decision_id':did,'location':d['location'],'reading':'[PENDING ROOT: returned candidates retained in reader_components]','alternatives':list(dict.fromkeys(str(z) for c in components for z in c['alternatives'])),'confidence':'low','confidence_status':'pending root; every actual local source confidence preserved below','reason':'Provisional union of reader doubts. '+'; '.join(f"{c['reader']}: {c['location']}, full-scan {c['bbox']}, {c['confidence']}: {c['reason']}" for c in components),'reader_components':components,'final_status':'pending root'})
draft['source_doubt_crosswalk']=dcross

# Inventory union: A's 65 stable elements plus the separately proposed NB rule.
wmap=[[1],[2],[4],[5],[6],[8,9],[10],[11],[12],[14],[15],[16],[17],[18],[19],[20],[21],[22],[24],[25],[27],[29],[31],[32,37],[33],[34],[38],[39],[40],[42],[43],[44],[46],[47],[48],[49],[51],[52],[54],[57],[58],[60],[62],[63]]
bmap=[[1,2],[2],[4],[3],[5],[6],[7],[12],[13],[10],[11],[66],[8,9],[14],[15],[16],[17],[18],[19],[24],[20],[21],[22],[25,26],[27],[23],[30],[29],[31],[32,37],[33],[34],[40,41],[38],[39],[43],[42],[44],[45],[46],[47],[54],[49],[52],[50],[51],[48],[60],[56],[61],[58],[57],[59],[63],[64],[62],[65]]
cmap=[[1],[2],[4],[5],[6,7],[8,9],[10],[11],[12,13],[14],[15],[16],[17],[18],[19],[20,23],[21],[22],[24],[25],[27,28],[29],[31],[32,37],[33],[34],[38],[39],[40,41],[42],[43],[44],[46],[47],[48],[49],[51],[52],[54],[57],[58],[60,61],[62],[63,64],[7],[23],[30],[50],[56],[61],[65]]
assert [len(wmap),len(bmap),len(cmap)]==[44,57,51]
inv=[]
for i,x in enumerate(reports['A']['inventory']):
 y=dict(x);y['element']=f'015-I{i+1:02d}';y['source_inventory']=[ref('A','inventory',i)];y['reader_hand_proposals']={'A':x['hand']};y['source_element_ids']={'A':[x['element']]};y['root_page_sources']=[];y['transcribed']='pending final-source attachment';y['hand_status']='proposed from actual returned labels; pending root';y['source_sort_coordinates']=[]
 if i+1 in [23,59]:y['kind']='text';y['kind_scope']='underlining'
 inv.append(y)
x=reports['B']['inventory'][11]
inv.append({'sheet_kind':'text','hand':'undetermined hand','element':'015-I66','kind':'drawing','position':x['position'],'first_words_or_objects':x['first_words_or_objects'],'transcribed':'pending root selection and final-source attachment','source_inventory':[],'reader_hand_proposals':{},'source_element_ids':{},'root_page_sources':[],'hand_status':'proposed from actual returned label; pending root','source_sort_coordinates':[],'decision_id':'015-G-NB-RULE'})
icross=[{'source':'A.report.json','pointer':f'/inventory/{i}','source_id':x['element'],'targets':[f'015-I{i+1:02d}']} for i,x in enumerate(reports['A']['inventory'])]
for r,mapping in [('B',bmap),('C',cmap)]:
 for i,targets in enumerate(mapping):
  x=reports[r]['inventory'][i];rr=ref(r,'inventory',i)
  icross.append({'source':r+'.report.json','pointer':f'/inventory/{i}','source_id':x['element'],'targets':[f'015-I{j:02d}' for j in targets],'scope':'overlapping local remnant component' if r=='B' and i==54 else 'exact named element or explicitly contained component'})
  for n in targets:
   z=inv[n-1];z['source_inventory'].append(rr);z['reader_hand_proposals'][r]=x['hand'];z['source_element_ids'].setdefault(r,[]).append(x['element'])
   if x.get('position_y') is not None:z['source_sort_coordinates'].append({'source':rr,'reported_position_y':x['position_y'],'scope':'reader ordering coordinate; not calculated glyph or path bound'})
witness_inventory=json.loads(packet['C_inventory.json'])
for i,targets in enumerate(wmap):
 x=witness_inventory[i];rr={'manifest':'packet.C_inventory.json','pointer':f'/{i}','row_id':x['element']}
 icross.append({'source':'packet.C_inventory.json','pointer':f'/{i}','source_id':x['element'],'targets':[f'015-I{j:02d}' for j in targets]})
 for n in targets:
  z=inv[n-1];z['source_inventory'].append(rr);z['source_element_ids'].setdefault('witness_C',[]).append(x['element']);z.setdefault('witness_hand_labels',{})['C']=x['hand']
contained={'witness_C':{8:[13],15:[23],19:[26],20:[28],25:[35],28:[41],37:[53],40:[59],43:[64]},'B':{24:[28],43:[53],53:[64]},'C':{19:[26],37:[53],40:[59]}}
for r,rows2 in contained.items():
 for i,targets in rows2.items():
  rr=ref(r,'inventory',i) if r!='witness_C' else {'manifest':'packet.C_inventory.json','pointer':f'/{i}','row_id':witness_inventory[i]['element']}
  for n in targets:inv[n-1].setdefault('contained_component_links',[]).append({'source':rr,'relationship':'same physical cluster; actual source representation/geometry remains as returned, not equated with another reader\'s literal paths'})
inv[55]['hand']='undetermined hand';inv[55]['hand_status']='A says his hand; B and C say undetermined hand; unresolved attribution retained'
inv[63]['local_components']=[{'id':'015-I64-remnant','description':'B G07 upper angular/looped remnants within final cancelled cluster','hand':'undetermined hand','source_inventory':ref('B','inventory',54),'decision_id':'015-G-REMNANT','overlap':'A CANCEL04 and C CANCEL03 cover this physical area with their own crossing paths; identity of individual strokes is not equated.'}]
inv[64]['archive_comment_only']=True;inv[64]['diff_C']=False;inv[64]['scope']='Archive numeral already present in packet.C.tex as a comment; the C inventory repair creates no text difference.'
extra_boxes={28:('A','G04'),35:('A','G14'),36:('A','G07'),37:('A','D12'),53:('A','H14'),64:('A','G12'),66:('B','G02')}
for n,(r,rid) in extra_boxes.items():
 i,x=index[r][rid];inv[n-1]['source_sort_coordinates'].append({'source':ref(r,'differences',i),'observed_bbox':bbox(x['bbox']),'scope':'reported full-scan observed locus; no path/font bound computation'})
inv[54]['source_sort_coordinates'].append({'source':{'manifest':'A.report.json','pointer':'/notes/drawing_component_map/5'},'observed_bbox':[233,2067,277,2133],'scope':'copied observed box of A GUIDE02; no path/font bounds claimed'})
for z in inv:
 vals=[v.get('observed_bbox',[None,None])[1] if 'observed_bbox' in v else v['reported_position_y'] for v in z['source_sort_coordinates']]
 z['sort_y']=min(vals) if vals else None
 z['sort_basis']='minimum supplied ordering/observed-locus y among attached sources; exact typographic upper extent remains unspecified'
# Full-scan upper extents explicitly present in the reports for broad drawing and lower note.
for n,r,rid in [(25,'C','G03'),(54,'C','H26')]:
 i,x=index[r][rid];b=bbox(x['bbox']);inv[n-1]['source_sort_coordinates'].append({'source':ref(r,'differences',i),'observed_bbox':b,'scope':'broad observed-locus box'});inv[n-1]['sort_y']=b[1]
for z in inv:
 if z['sort_y'] is None:
  # Every A baseline element is supported by a supplied B y or the local report boxes above except arrow/labels.
  if z['element']=='015-I09':z['sort_y']=inv[7]['sort_y'];z['sort_basis']='within upper-note parent; exact arrow upper extent pending root'
  elif z['element']=='015-I26':z['sort_y']=inv[24]['sort_y'];z['sort_basis']='within drawing parent; exact aggregate-label upper extent pending root'
inv.sort(key=lambda z:(z['sort_y'] is None,z['sort_y'] if z['sort_y'] is not None else 99999,z['element']))
draft['inventory']=inv;draft['source_inventory_crosswalk']=icross
assert len(icross)==217
assert all(z['source_inventory'] for z in inv)

def sections(txt):
 result={};section=None
 for i,line in enumerate(txt.splitlines(),1):
  if line.startswith('## '):section=line[3:].strip();result[section]=[]
  elif line.startswith('| 15 |') and section:
   cells=[z.strip() for z in line.strip().strip('|').split(' | ')]
   result[section].append({'source_manifest':'packet.C_doubts.txt','source_line':i,'cells':cells,'exact':line})
 return result
cats=sections(packet['C_doubts.txt'])
draft['source_categories']={k:cats[k] for k in ['Notation table','Slips retained','Abbreviations']}
draft['abbreviations']=[{'form':x['cells'][1],'expansion':x['cells'][2],'source':{'manifest':x['source_manifest'],'line':x['source_line']}} for x in cats['Abbreviations']]
draft['root_actions_pending']=['Supply all crop-adjudicated choices and exact local confidences; all final/count fields remain provisional.','Approve one H drawing parent, one lower-note H ill parent, and all shared C physical count parents.','Attach every retained inventory component and decision to exact final source spans after root supplies that source.','Resolve A/B/C graphic overlap and hand conflicts using the preserved source identities.','Confirm S SA01-K81-06 local overbars against ink.']
draft['source_counts'].update(reader_remaining_doubt_rows={r:len(reports[r]['doubts']) for r in 'ABC'},source_inventory_rows=217,union_inventory_elements=len(inv),union_decision_entries=len(decisions),provisional_remaining_doubt_loci=len(draft['doubts']))
draft['mechanical_verification']={'all_181_source_difference_rows_mapped':True,'all_66_source_doubt_rows_mapped':len(dcross)==66,'all_217_inventory_rows_mapped':True,'source_doubt_identity':'21 actual source rows; primary local map has 24 entries; component/audit children do not add source rows','no_reader_file_changed':all(sha(BASE/v['path'])==v['sha256'] for k,v in manifest.items() if k[0] in 'ABC' and k.endswith(('.json','.tex','.md'))),'no_image_viewed_by_clerk':True,'proof_events':0,'numerical_geometry_checks':0}
assert all(not d['diff_H'] for d in decisions if d.get('H_count_parent'))
assert all(d['log_decision'] for d in decisions if d.get('H_count_parent') or d.get('C_count_parent'))
(OUT/'scan015_record_draft.json').write_text(json.dumps(draft,ensure_ascii=False,indent=2)+'\n')

# Refresh the compact human crosswalk after complete-source supplements.
head=lines[:lines.index('| Locus | C source row | Physical location / components | C | H | A | B | C-reader | Full-scan boxes / existing crop paths |')]
head+=['| Locus | C source row | Physical location / components | C | H | A | B | C-reader | Full-scan boxes / existing crop paths |','|---|---|---|---|---|---|---|---|---|']
for d in decisions:
 loc=d['location']+(' ; H parent '+d['H_count_parent'] if d.get('H_count_parent') else '')+(' ; C parent '+d['C_count_parent'] if d.get('C_count_parent') else '')
 vals=[d['id'],','.join(map(str,d['source_C_doubt_rows'])) or '—',loc,d['C'],d['H'],*[d['readers'][r] for r in 'ABC'],json.dumps(d['full_scan_boxes'],ensure_ascii=False)+'; '+'; '.join(d['available_crops'])]
 head.append('| '+' | '.join(esc(x) for x in vals)+' |')
tail=lines[lines.index('## Exact source-row crosswalk')-1:]
head+=tail+['','## Complete remaining-doubt crosswalk','','| Source | Pointer | Source difference | Local union |','|---|---|---|---|']
for z in dcross:head.append('| '+' | '.join(map(esc,[z['reader']+'.report.json',z['pointer'],z['source_difference'],z['locus']]))+' |')
head+=['','## Inventory crosswalk','','All 217 source inventory rows map below. Broad source rows may name several explicit components; each source-row identity occurs once. Final-source attachment is still pending root.','', '| Source | Pointer | Original element ID | Union element(s) |','|---|---|---|---|']
for z in icross:head.append('| '+' | '.join(map(esc,[z['source'],z['pointer'],z['source_id'],', '.join(z['targets'])]))+' |')
head+=['','The 66 union elements retain all distinct components. B.G07 is an explicit local component within 015-I64, with its own undetermined-hand attribution and overlapping A/C path coverage. 015-I66 is B’s separate right-NB upper rule. Underlining items use kind=text. All archive numeral14 source comments are retained; its missing old inventory row creates no C text change.','', '## Source-level disagreements that require root attention','', 'The detailed source readings above preserve letter/state/placement disagreements, including A/B/C confidence differences. C-reader D12 adds an accent alternative; B D13 reverses car/Car priority; A resolves cancelled vois. ouvert while B/C retain its doubt; C-reader D16 reverses signaler/sign.ler priority; B retains un/une while A/C resolve un; B resolves donc and the first marginal i while A/C retain them. C-reader preserves H’s final cancelled formula as an alternative. A qualifies on a and excludes the abbreviation point from the vois underline. C-reader qualifies the symmetry accent and l’ouvert apostrophe. A’s Car-formula underline is shorter than the B/C full-expression underline. B’s extra NB rule, A’s short lower-note arrow, all detached marks, all contour changes, and B’s upper remnants need their own ink choices.','', 'No new mathematical check, coordinate computation, proof event, model setting, or timestamp was inferred.']
(OUT/'scan015_union.md').write_text('\n'.join(head)+'\n')
print(json.dumps({'complete_mechanical_union':True,'decisions':len(decisions),'doubt_source_rows':len(dcross),'provisional_doubt_loci':len(draft['doubts']),'inventory_source_rows':len(icross),'inventory_union_elements':len(inv),'all_reader_values_attached':all(not any('attachment pending' in v for v in d['readers'].values()) for d in decisions)}))
