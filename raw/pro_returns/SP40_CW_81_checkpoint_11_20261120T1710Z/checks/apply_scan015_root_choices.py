"""Apply the expressly supplied scan015 root choices; keep unknown loci pending."""
import json,re,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'checks/scan015_record_draft.json'
d=json.loads(P.read_text());by={x['id']:x for x in d['decisions']}
log=ROOT/'checks/scan015_main_decisions.md';text=log.read_text()
sections={int(m.group(1)):{'heading':m.group(2),'body':m.group(3).strip()} for m in re.finditer(r'^## (\d+) — ([^\n]+)\n(.*?)(?=^## \d+ — |\Z)',text,re.M|re.S)}
applied={}
def choose(key,n,final,confidence,dc,dh,status=None,selection=None,remaining=None,scope=None):
 if n not in sections:return
 x=by['015-'+key];s=sections[n]
 crops=re.findall(r'`((?:readers|crops)/015/[^`]+\.png)`',s['body'])
 x.update(final=final,confidence=confidence,confidence_status='root supplied local confidence',diff_C=dc,diff_H=dh,count_status='root supplied choice; Boolean count from explicit physical parent and current witness comparison',main_approved=True,evidence=s['body'],root_decision_log='checks/scan015_main_decisions.md',root_decision_section=n,root_decision_heading=s['heading'],root_crop_paths=crops,log_decision=True)
 if crops:x['crop']=crops[0]
 if status is not None:x['C_doubt_status']=status
 if selection:x['selected_reader_source']=selection
 if remaining is not None:x['remaining_doubt']=remaining
 if scope:x['confidence_scope']=scope
 applied[x['id']]=n
choose('D01a',1,r'\deleted{\unsure{I|V}}','low',False,True,'retained',remaining=True)
choose('D01b',1,'Version','high',True,False,'resolved',remaining=False)
choose('H-TITLE',1,r'\uline{\deleted{\unsure{I|V}}Version I}','high',False,True,remaining=False)
by['015-H-TITLE']['source_C_doubt_rows']=[]
by['015-H-TITLE']['related_C_source_row']=1
by['015-H-TITLE']['C_doubt_status']=None
choose('D02',2,r'\deleted{\unsure{\Sigma|S}}E_i','medium',False,True,'retained',remaining=True)
choose('D20',3,r'\inserted{\unsure{fermés|fermées}}','medium',False,True,'retained',remaining=True)
choose('G02',3,'A GUIDE01: curved opening insertion guide, literal selected path and local arrangement.','high',True,True,selection={'manifest':'A.reading.tex','anchor':'GUIDE01'},remaining=False)
choose('H01',4,'On suppose de plus que','high',False,True,remaining=False)
choose('D03',4,r'\unsure{tte|toute|tt}','low',False,True,'retained',remaining=True)
choose('D21a',4,'conn.','medium',True,False,'resolved',remaining=False)
choose('D21b',4,r'\unsure{\Sigma_i|\Sigma}','low',False,False,'retained',remaining=True)
choose('D04',4,'non','medium',True,True,'resolved',remaining=False)
choose('H-COMMA',4,r'\overline{\Sigma}_i\ne\Sigma_i$ i.e.','medium',False,True,remaining=False)
choose('H-ARROW',4,r'\nearrow','high',False,True,remaining=False)
choose('H04',5,r'\uline{NB}','high',False,True,remaining=False)
choose('G-NB-RULE',5,r'\overset{\unsure{\rule{.8em}{.35pt}}}{\Sigma}_i^+','medium',True,True,selection={'manifest':'B.reading.tex','anchor':'G02'},remaining=True,scope='medium shape confidence; hand, role, character and surface origin undetermined')
choose('D05',5,r'\Sigma_i^{\unsure{+|-|\ast}}','low',False,True,'retained',remaining=True)
choose('D06',5,r'X\setminus\Sigma_i','high',True,True,'resolved',remaining=False)
choose('H02',6,r'\operatorname{Card}','high',False,True,remaining=False)
choose('H03',6,r'\deleted{\Sigma}E_i','high',False,True,remaining=False)
choose('H05',7,r'\deleted{\Sigma}E_j','high',False,True,remaining=False)
choose('D07',8,r'X\setminus\deleted{\Sigma}E_i.','high',True,True,'resolved',remaining=False)
choose('D08',9,'automatiquement','medium',True,False,'resolved',remaining=False)
choose('H06',10,'Cette','high',False,True,remaining=False)
choose('H07',10,'automatiquement les','high',False,True,remaining=False)
choose('H08',10,r'\deleted{\Sigma}E_i','high',False,True,remaining=False)
choose('H09',11,'mutuellement','high',False,True,remaining=False)
choose('H10',12,r'\operatorname{Card}','high',False,True,remaining=False)
choose('D09a',12,r'\deleted{\unsure{(\mathrm{de})}}','low',False,True,'retained',remaining=True)
choose('D09b',12,r'\deleted{\unsure{\leq|=}}=','low',False,True,'retained',remaining=True)
choose('G03',12,'A RULE01: long wavy underline and separate short rule beneath 2.','high',True,True,selection={'manifest':'A.reading.tex','anchor':'RULE01'},remaining=False)
choose('H-DRAW',13,'C DRAW01: nine oval paths, two chords, three translated brace paths, six live labels, qualified cancelled label/right exponent, two cancellation paths and MARK01.','high',False,True,selection={'manifest':'C.reading.tex','anchor':'DRAW01'},remaining=False,scope='drawing presence and arrangement; local glyph and pale-path confidences are separately retained')
choose('G13',13,'C DRAW01 separated oval paths: gaps, pale right/lower runs and left hooked return.','medium',True,False,selection={'manifest':'C.reading.tex','anchor':'DRAW01 oval paths'},remaining=False,scope='medium for pale density and short lower-right intervals; high for dark paths and left hook; one C contour cluster count')
choose('D10',13,r'\deleted{\unsure{\Sigma_1^+|\Sigma_2^+}}','low',False,False,'retained',remaining=True)
choose('G04',13,'C DRAW01: two upper-left cancellation commands over one qualified label.','high',True,False,selection={'manifest':'C.reading.tex','anchor':'DRAW01 cancelled-label paths'},remaining=False)
choose('D11',13,r'\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}','low',False,False,'retained',remaining=True)
choose('D11-old',13,r'\deleted{\unsure{+}}','low',False,False,'retained',remaining=True)
choose('D11-live',13,r'\unsure{-}','low',False,False,'retained',remaining=True)
choose('G05',13,'C MARK01 literal filled contour under local uncertainty; fixed origin required.','medium',True,False,selection={'manifest':'C.reading.tex','anchor':'MARK01','wrapper_requirement':'fixed origin; retain literal filled contour'},remaining=True,scope='medium visible-shape confidence; role, hand and surface origin undetermined')
for key,final,conf in [('upper-right','C DRAW01 upper-right strong runs and visible gap','high'),('left-edge','C DRAW01 pale left run and short hooked return','medium'),('left-brace1','first C brace path retained through reader-C translation','high'),('left-brace2','second C brace path retained through reader-C translation','high'),('right-brace','right C brace path retained through reader-C translation','high'),('chord1','C DRAW01 upper chord','high'),('chord2','C DRAW01 lower chord','high')]:
 choose('DRAW-'+key,13,final,conf,False,False,selection={'manifest':'C.reading.tex','anchor':'DRAW01 '+key},remaining=False)
labels={'E1':r'E_1','E2':r'E_2','Sigma1plus':r'\Sigma_1^+','Sigma1minus':r'\Sigma_1^{\deleted{\unsure{+}}\unsure{-}}','Sigma2minus':r'\Sigma_2^-','Sigma2plus':r'\Sigma_2^+'}
for key,val in labels.items():choose('DRAW-label-'+key,13,val,'low' if key=='Sigma1minus' else 'high',False,False,selection={'manifest':'C.reading.tex','anchor':'DRAW01 live label '+key},remaining=False,scope='label audit; right-exponent local doubt is counted only at D11' if key=='Sigma1minus' else None)
choose('P01',14,'First cancelled inclusion left of équivaut à on one physical line; second cancelled inclusion follows on the next line.','high',True,False,remaining=False)
if 14 in sections:by['015-P01']['source_contradiction']={'reader':'B','report':{'manifest':'B.report.json','pointer':'/differences/36','row_id':'H13'},'returned_report_reading':'crossed inclusions on their own successive lines','tex':{'manifest':'B.reading.tex','exact_excerpt':r'ce qui \deleted{résulte de} équivaut à'},'root_observation':'Root section14 identifies a report/TeX physical-order contradiction; B TeX keeps wording before the first cancelled display. Both originals are retained.'}
choose('D12',14,r'\unsure{équivaut|èquivaut}','medium',False,False,'retained',selection={'manifest':'C.reading.tex','anchor':r'\unsure{équivaut|èquivaut}'},remaining=True)
choose('D12-accent',14,'acute/grave accent remains qualified in équivaut|èquivaut','medium',False,False,'retained',remaining=True)
choose('H11',14,'à','high',False,True,remaining=False)
choose('G14',14,'A CANCEL02: slightly rising cancellation path across first inclusion.','high',True,True,selection={'manifest':'A.reading.tex','anchor':'CANCEL02'},remaining=False)
choose('G07',14,'A MARK03: literal two-fill body above first inclusion relation, locally qualified.','medium',True,True,selection={'manifest':'A.reading.tex','anchor':'MARK03','wrapper_requirement':'fixed origin; retain both fill commands'},remaining=True,scope='medium shape confidence; role, hand and origin undetermined')
choose('D13',15,r'\deleted{\unsure{Car si|car si}}','low',True,True,'retained; primary capitalization changed',selection={'wording':'B.reading.tex Car si|car si','geometry':'A.reading.tex CANCEL03'},remaining=True,scope='low phrase/capitalization confidence carries one physical C/H cluster count; geometry child high')
choose('G06',15,'A CANCEL03: two literal cancellation paths, upper nearly level and lower bowed.','high',False,False,selection={'manifest':'A.reading.tex','anchor':'CANCEL03'},remaining=False)
by['015-G06'].update(C_count_parent='015-D13',H_count_parent='015-D13',C_count_policy='zero on local stroke child; D13 carries one physical Car-si count',H_count_policy='zero on local stroke child; D13 carries one physical Car-si count')
choose('P02',16,r'\deleted{Si on avait} before live comme on the same physical line','high',False,True,remaining=False)
choose('H12',17,'aussi à','high',False,True,remaining=False)
choose('D14',18,r'\unsure{et}','low',False,True,'retained',remaining=True)
choose('G-SYM-ACCENT',18,r'\unsure{symètriquement|symétriquement}','medium',True,True,selection={'manifest':'C.reading.tex','anchor':r'\unsure{symètriquement|symétriquement}'},remaining=True)
choose('H13',18,'à','high',False,True,remaining=False,scope='endpoint punctuation only; accent confidence recorded at G-SYM-ACCENT')

def source_only_geometry(key,loc,tokens,C,H,hparent,inventory_id):
 did='015-'+key
 if did not in by:
  x={'id':did,'location':loc,'C':C,'H':H,'final':'[PENDING ROOT INK DECISION]','readers':{},'reader_provenance':{},'reader_tex_provenance':{},'evidence':'','crop':None,'confidence':'low','kind':'drawing or diagram','diff_C':False,'diff_H':False,'C_doubt_status':None,'source_C_doubt_rows':[],'marked_in_H':'deletion retained; geometry covered by placement parent','mathematical_consequence':None,'main_approved':False,'log_decision':True,'H_count_parent':'015-'+hparent,'H_count_policy':'zero local H geometry count under phrase-placement parent','source_difference_scope':'additional local path identified in complete TeX by root; no dedicated original difference row','final_source_attachment':None,'full_scan_boxes':{},'available_crops':[]}
  d['decisions'].append(x);by[did]=x
 else:x=by[did]
 for r,token in tokens.items():
  t=(ROOT/f'readers/015/{r}/reading.tex').read_text();a=t.index(token);b=t.index(';',a)+1 if token.startswith('\\draw ') else a+len(token)
  x['readers'][r]=t[a:b]
  x['reader_tex_provenance'][r]=[{'manifest':r+'.reading.tex','char_start':a,'char_end':b,'line_start':t.count('\n',0,a)+1,'line_end':t.count('\n',0,b)+1}]
 z=next(z for z in d['inventory'] if z['element']==inventory_id)
 lc={'id':inventory_id+'-cancel','description':loc,'hand':'his hand','decision_id':did,'source':x['reader_tex_provenance']['B'][0],'scope':'explicit graphical component in selected B figure; source inventory remains the same physical phrase'}
 z.setdefault('local_components',[])
 if not any(v['id']==lc['id'] for v in z['local_components']):z['local_components'].append(lc)
source_only_geometry('G-VOIS-CANCEL','single crossing path across raised cancelled vois. ouvert',{'A':r'\deleted{vois. ouvert}','B':r'\draw (209,37)','C':r'\deleted{\unsure{vois. ouvert}}'},r'\deleted{\unsure{vois. ouvert}}',r'\struck{vois.\ ouvert}','P07','015-I49')
source_only_geometry('G-IL-CANCEL','crossing path across cancelled il contient les',{'A':r'\deleted{il contient les}','B':r'\draw (557,91)','C':r'\deleted{il contient les}'},r'\deleted{il contient les}',r'\struck{il contient les}','P08','015-I51')
choose('D15',19,r'\deleted{\unsure{vois. ouvert}}','medium',False,False,'retained',remaining=True)
choose('P07',19,'Cancelled vois. ouvert above first Sigma_2^- and ahead of E_1','high',False,True,remaining=False)
choose('G09',19,'C MARK02 literal short rising curved path; fixed full origin (510,2061).','medium',True,True,selection={'manifest':'C.reading.tex','anchor':'MARK02','fixed_full_origin':[510,2061],'within_B_group_anchor':[291,52]},remaining=True,scope='medium shape confidence; role, hand and origin undetermined')
choose('G-VOIS-CANCEL',19,'B lower correction figure: literal draw (209,37) through (410,36), without extra generic strike.','high',True,False,selection={'manifest':'B.reading.tex','anchor':r'\draw (209,37)'},remaining=False)
choose('P08',20,'Raised i.e. clause above crossed il contient les; B lower correction arrangement subject to selected local text/mark changes.','high',False,True,selection={'manifest':'B.reading.tex','anchor':'Lower correction group'},remaining=False)
choose('G-IL-CANCEL',20,'B lower correction figure: literal draw (557,91) through (997,82), without extra generic strike.','high',True,False,selection={'manifest':'B.reading.tex','anchor':r'\draw (557,91)'},remaining=False)
choose('H14',20,r'\uline{vois}.','high',True,True,remaining=False)
choose('H15',20,r'on \unsure{a}','low',True,False,remaining=True,scope='new low-confidence local qualification of a; unchanged primary letter')
choose('H15-colon',20,r'on \unsure{a}','high',False,True,remaining=False,scope='high-confidence terminal punctuation; separate H count from C letter qualification')
for field in ['H_count_parent','H_count_policy','C_count_parent','C_count_policy']:by['015-H15-colon'].pop(field,None)

if '015-G10-GROUP' not in by:
 x={'id':'015-G10-GROUP','location':'lower marginal note: short arrow and longer curved guide cluster','C':'text-only marginal note; no separate guide paths','H':r'\ill{} for note tail','final':'[PENDING ROOT INK DECISION]','readers':{r:'See separate local components 015-G10a and 015-G10b; each returned guide source is retained.' for r in 'ABC'},'reader_provenance':{},'evidence':'','crop':None,'confidence':'low','kind':'drawing or diagram','diff_C':False,'diff_H':False,'C_doubt_status':None,'source_C_doubt_rows':[],'marked_in_H':'within ill placeholder','mathematical_consequence':None,'main_approved':False,'log_decision':True,'H_count_parent':'015-H17','H_count_policy':'zero H on graphics parent; whole tail placeholder counted once','component_decisions':['015-G10a','015-G10b'],'final_source_attachment':None,'full_scan_boxes':{'A:short':[233,2067,277,2133],'C:long':[183,2162,301,2223]},'available_crops':['readers/015/C/17_lower_margin.png']}
 d['decisions'].append(x);by[x['id']]=x
choose('D16',21,r'\unsure{à sign.ler|à signaler} avant','medium',True,False,'retained; primary candidate order changed',selection={'manifest':'C.reading.tex','anchor':r'\unsure{à sign.ler|à signaler}'},remaining=True,scope='root crop includes the complete ending; A/B boundary limitations remain reader-specific')
choose('H17',21,r'i.e. $\overline{\Sigma_1^+}\ne\Sigma_1^+$ \unsure{à sign.ler|à signaler} avant, with short/long local guides','medium',False,True,selection={'layout':'A.reading.tex lower-note canvas','instruction':'C.reading.tex reversed candidates','short_guide':'A GUIDE02','long_guide':'C GUIDE02'},remaining=False,scope='whole ill placeholder recovery; local doubtful instruction and guides recorded in separate children')
choose('G10-GROUP',21,'A GUIDE02 short arrow and C GUIDE02 longer curve, separately qualified and each appearing once.','medium',True,False,remaining=True,scope='one C graphical cluster count; both local components retain medium shape confidence and undetermined role/attachment/hand/origin')
choose('G10a',21,'A GUIDE02 short curved arrow and arrowhead under local uncertainty.','medium',False,False,selection={'manifest':'A.reading.tex','anchor':'GUIDE02'},remaining=True,scope='medium shape confidence; role, attachment, hand and origin undetermined')
choose('G10b',21,'C GUIDE02 literal curve body and rectangle under local uncertainty; fixed full origin (180,2158).','medium',False,False,selection={'manifest':'C.reading.tex','anchor':'GUIDE02','fixed_full_origin':[180,2158],'within_A_note_anchor':[163,196]},remaining=True,scope='medium shape confidence; role, attachment, hand and origin undetermined')
for key in ['G10a','G10b']:by['015-'+key].update(C_count_parent='015-G10-GROUP',C_count_policy='zero local C count; the pair of guides shares the explicit graphical cluster parent')
choose('S-NOTE-FIRST',21,r'\overline{\Sigma_1^+}\cap E_1\ne\varnothing','high',False,False,remaining=False,scope='bar directly confirmed by root; both current C and H already contain this first bar')
choose('S-NOTE-SECOND',21,r'\overline{\Sigma_1^+}\ne\Sigma_1^+','high',False,False,remaining=False,scope='bar directly confirmed by root; current C contains it; H recovery belongs only to the whole tail placeholder')
for key in ['S-NOTE-FIRST','S-NOTE-SECOND']:
 if 21 in sections:
  by['015-'+key]['S_status']='confirmed from ink in root section21; current witness comparison preserved'
  by['015-'+key]['confidence_status']='root confirms reading; high is proposed for audit only because section21 did not explicitly state a confidence for these two formula audits'
  by['015-'+key]['root_confidence_pending']=True
if 21 in sections:
 arch=next(z for z in d['inventory'] if z['element']=='015-I65');arch.update(hand='undetermined hand',root_reading='% archive sheet number: 14',root_reading_confidence='high',root_decision_section=21,root_approved=True,archive_comment_only=True,diff_C=False)
 for iid in ['015-I55','015-I56']:
  z=next(z for z in d['inventory'] if z['element']==iid);z.update(hand='undetermined hand',hand_status='root section21: role/attachment/hand/origin undetermined',root_decision_section=21,root_approved=True)
choose('H18',22,'Car','high',False,True,remaining=False)
choose('G11',22,'A RULE02 short curved underline with two hooked ends, ending before the E_1 index.','high',True,True,selection={'manifest':'A.reading.tex','anchor':'RULE02'},remaining=False)
choose('S-FINAL',22,r'\overline{\Sigma_1^+}\cap E_1\ne\varnothing','high',False,False,remaining=False,scope='upper bar audit only; both current C and H already carry it, while lower underline has separate G11 count')
if 22 in sections:by['015-S-FINAL']['S_status']='confirmed from ink in root section22; current C/H already barred'

choose('P09',23,r'\inserted{\unsure{l\'ouvert|louvert}} before \Sigma_1^+','medium',True,True,selection={'arrangement':'B.reading.tex final local insertion figure','wording':'C.reading.tex qualified l\'ouvert|louvert','guide':'B GUIDE02'},remaining=True,scope='one physical insertion-and-guide C/H parent; apostrophe and placement qualification medium, guide child high')
choose('P09-apostrophe',23,r"\inserted{\unsure{l'ouvert|louvert}}",'medium',False,False,remaining=True,scope='local apostrophe qualification within P09 parent')
choose('P09-commas',23,r"(sinon \inserted{\unsure{l'ouvert|louvert}} \Sigma_1^+ serait",'medium',False,False,remaining=False,scope='local wording/attachment cluster inherits root medium parent confidence; no flanking commas')
choose('G-LOUVERT',23,'B GUIDE02 literal bent guide with right end rising then briefly turning left.','high',False,False,selection={'manifest':'B.reading.tex','anchor':'GUIDE02','group_origin':[1278,2080]},remaining=False)
by['015-G-LOUVERT'].update(C_count_parent='015-P09',C_count_policy='zero local guide count; P09 carries shared physical insertion-and-guide count')
choose('D17',24,r'\inserted{un}','medium',True,True,'resolved',remaining=False)
choose('D18',24,r'\unsure{donc|puis}','low',False,False,'retained',remaining=True)
choose('D19',24,r'\deleted{\unsure{\Sigma_1^+\text{ serait}|\Sigma_1^+\ne\varnothing}}','low',True,True,'retained; H formula survives as alternative',selection={'wording':'C.reading.tex final cancelled group','paths':'C CANCEL03 three literal paths','upright':'B G07 second command only'},remaining=True,scope='one whole final-cancelled-cluster C count for added geometry and one H count for qualified primary reading; local shape confidences below')
choose('G12',24,'C CANCEL03: three literal paths, long diagonal, angular upper crossing and longer low crossing.','medium',False,False,selection={'manifest':'C.reading.tex','anchor':'CANCEL03'},remaining=False,scope='selected C-reader medium geometry confidence; glyph and upright uncertainty remain separate')
by['015-G12'].update(C_count_parent='015-D19',C_count_policy='zero local overstrike count; D19 carries whole physical final-cluster count')
choose('G-REMNANT',24,r'B G07 second command only: \draw (24,6) -- (26,16); under local uncertainty.','medium',False,False,selection={'manifest':'B.reading.tex','anchor':'G07 second draw command','fixed_full_origin':[932,2239],'within_C_group_anchor':[12,1]},remaining=True,scope='medium visible-shape confidence; hand, role and origin unresolved')
by['015-G-REMNANT'].update(location='final cancelled group: separately retained short upper upright',C_count_parent='015-D19',C_count_policy='zero local upright count; D19 carries whole physical final-cluster count')
for key,loc,aliases,sourcerow in [('D19-glyph','final cancelled group: glyph/formula alternatives',{'A':'D19','B':'D19','C':'D19'},[19]),('G-REMNANT-ANGULAR','final cancelled group: overlapping angular region',{'A':'G12','B':'G07','C':'G12'},[])]:
 did='015-'+key
 if did not in by:
  x={'id':did,'location':loc,'C':by['015-D19']['C'] if key=='D19-glyph' else 'generic deletion geometry','H':by['015-D19']['H'] if key=='D19-glyph' else 'within final cancelled cluster','final':'[PENDING ROOT INK DECISION]','readers':{},'reader_provenance':{},'evidence':'','crop':None,'confidence':'low','kind':'other' if key=='D19-glyph' else 'drawing or diagram','diff_C':False,'diff_H':False,'C_doubt_status':'retained' if sourcerow else None,'source_C_doubt_rows':sourcerow,'marked_in_H':'struck group','mathematical_consequence':None,'main_approved':False,'log_decision':True,'C_count_parent':'015-D19','H_count_parent':'015-D19','C_count_policy':'zero local count under whole final-cluster parent','H_count_policy':'zero local count under whole final-cluster parent','final_source_attachment':None,'full_scan_boxes':{},'available_crops':[]}
  for r,rid in aliases.items():
   rr=json.loads((ROOT/f'readers/015/{r}/report.json').read_text());i,rx=next((i,v) for i,v in enumerate(rr['differences']) if v['id']==rid)
   x['readers'][r]=rx['reading'];x['reader_provenance'][r]=[{'manifest':r+'.report.json','pointer':f'/differences/{i}','row_id':rid}]
   bb=rx.get('bbox');x['full_scan_boxes'][r]=bb.get('xyxy') if isinstance(bb,dict) else bb
  d['decisions'].append(x);by[did]=x
choose('D19-glyph',24,r'\deleted{\unsure{\Sigma_1^+\text{ serait}|\Sigma_1^+\ne\varnothing}}','low',False,False,'retained',remaining=True,scope='glyph alternatives, low; H candidate retained')
choose('G-REMNANT-ANGULAR',24,'C CANCEL03 angular path represents the same upper angular region identified by B G07 first component; retain the region once.','medium',False,False,selection={'manifest':'C.reading.tex','anchor':'CANCEL03 angular draw command','overlap_reference':'B.reading.tex G07 first command'},remaining=False,scope='source overlap audit; individual literal B/C strokes are not equated')
choose('G01',25,'A MARK01 literal small tilted filled oval under local uncertainty.','high',True,True,selection={'manifest':'A.reading.tex','anchor':'MARK01'},remaining=True,scope='high visible-shape confidence; role, character, hand and surface origin undetermined')
choose('G08',26,'A MARK04 literal two-fill body, diagonal upper-right/lower-left pair, under local uncertainty.','high',True,True,selection={'manifest':'A.reading.tex','anchor':'MARK04'},remaining=True,scope='high visible-shape confidence; role, character, hand and surface origin undetermined')
if 'S confidence supplements' in text:
 for key in ['S-NOTE-FIRST','S-NOTE-SECOND']:
  by['015-'+key].update(confidence='high',confidence_status='root supplied high confidence in Placement maps and S confidence supplements',root_confidence_pending=False)
 by['015-G05']['selected_reader_source'].update(fixed_full_origin=[526,1191],within_C_DRAW01_anchor=[507,153])
 by['015-G07']['selected_reader_source'].update(fixed_full_origin=[859,1404],within_first_inclusion_anchor=[155,16])
 by['015-G10a']['selected_reader_source'].update(wrapper_origin_in_A_note=[211,103],inverse_local_scope_shift=[-211,-103],scope='two original A GUIDE02 commands unchanged; declared placement, no path-bound calculation')

# Keep source-row status and local components separate from original-row counts.
primary=['D01a','D01b','D02','D03','D04','D05','D06','D07','D08','D09a','D09b','D10','D11','D12','D13','D14','D15','D16','D17','D18','D19','D20','D21a','D21b']
for row in d['actual_C_doubt_map']:
 row['primary_local_decision_ids']=['015-'+k for k in primary if row['source_row'] in by['015-'+k]['source_C_doubt_rows']]
 row['component_decision_ids']=[x['id'] for x in d['decisions'] if row['source_row'] in x['source_C_doubt_rows'] and x['id'] not in row['primary_local_decision_ids']]
 row['decision_ids']=row['primary_local_decision_ids']+row['component_decision_ids']
 row['local_statuses']={k:by[k]['C_doubt_status'] for k in row['decision_ids']}
 row['status']='root supplied every primary local choice' if all(by[k]['main_approved'] for k in row['primary_local_decision_ids']) else 'at least one primary local choice pending root'
# Rebuild remaining doubts from all returned source rows, retaining unapproved questions.
source_doubts={}
raw_reports={r:json.loads((ROOT/f'readers/015/{r}/report.json').read_text()) for r in 'ABC'}
for cross in d['source_doubt_crosswalk']:
 r=cross['reader'];i=int(cross['pointer'].rsplit('/',1)[1]);raw=raw_reports[r]['doubts'][i];did=cross['locus'];sid=cross['source_difference'];rd=next((v for v in raw_reports[r]['differences'] if v['id']==sid),{})
 bb=rd.get('bbox');bb=bb.get('xyxy') if isinstance(bb,dict) else bb
 component={'reader':r,'source':{'manifest':r+'.report.json','pointer':cross['pointer'],'row_id':sid},'location':raw['location'],'reading':raw['reading'],'alternatives':raw.get('alternatives',[]),'confidence':raw['confidence'],'reason':raw.get('reason',''),'qualification':raw.get('qualification'),'bbox':bb,'crop':f'readers/015/{r}/'+raw['crop'] if raw.get('crop') else None}
 z=source_doubts.setdefault(did,{'decision_id':did,'location':by[did]['location'],'reading':'[pending root]','confidence':'low','reason':'Provisional source doubt union','alternatives':[],'reader_components':[],'final_status':'pending root'})
 z['reader_components'].append(component);z['alternatives']+=raw.get('alternatives',[])
for x in d['decisions']:
 if x['main_approved'] and x.get('remaining_doubt') is False:source_doubts.pop(x['id'],None)
 if x['main_approved'] and x.get('remaining_doubt') is True and x['id'] not in ['015-D11-old','015-D11-live','015-D12-accent','015-D19-glyph']:
  z=source_doubts.setdefault(x['id'],{'decision_id':x['id'],'location':x['location'],'alternatives':[],'reader_components':[]})
  z.update(reading=x['final'],confidence=x['confidence'],confidence_status=x['confidence_status'],reason='Root section '+str(x['root_decision_section'])+': '+x['evidence'],crop=x['crop'],root_decision_section=x['root_decision_section'],final_status='root retains this doubt')
  if x['id']=='015-D11':z['local_components']=[{'id':k,'location':by[k]['location'],'reading':by[k]['final'],'confidence':by[k]['confidence'],'position':by[k]['full_scan_boxes']} for k in ['015-D11-old','015-D11-live']]
  if x['id']=='015-D12':z['local_components']=[{'id':'015-D12-accent','location':by['015-D12-accent']['location'],'reading':by['015-D12-accent']['final'],'confidence':'medium','position':by['015-D12-accent']['full_scan_boxes']}]
d['doubts']=list(source_doubts.values())
if 21 in sections:
 group=source_doubts['015-G10-GROUP']
 group['reader_components']=source_doubts.get('015-G10a',{}).get('reader_components',[])+source_doubts.get('015-G10b',{}).get('reader_components',[])
 group['local_components']=[{'id':k,'location':by[k]['location'],'reading':by[k]['final'],'confidence':by[k]['confidence'],'position':([233,2067,277,2133] if k.endswith('a') else [183,2162,301,2223]),'reason':by[k]['confidence_scope']} for k in ['015-G10a','015-G10b']]
 group['reason']='Root section21 keeps two distinct guide components under one graphical cluster. Short arrow: observed box [233,2067,277,2133], medium shape confidence. Longer curve: observed box [183,2162,301,2223], medium shape confidence. Each role, attachment, hand and origin remains undetermined; exact selected literal bodies and origins are preserved in local component decisions.'
 source_doubts.pop('015-G10a',None);source_doubts.pop('015-G10b',None);d['doubts']=list(source_doubts.values())
if 23 in sections:
 z=source_doubts['015-P09'];child=source_doubts.pop('015-P09-apostrophe',None)
 if child:z['reader_components']+=child.get('reader_components',[])
 z['local_components']=[{'id':'015-P09-apostrophe','reading':by['015-P09-apostrophe']['final'],'confidence':'medium','position':by['015-P09-apostrophe']['full_scan_boxes'],'reason':'initial l visible; small apostrophe remains crowded'}]
if 24 in sections:
 z=source_doubts['015-D19'];child=source_doubts.pop('015-G-REMNANT',None)
 if child:z['reader_components']+=child.get('reader_components',[])
 z['local_components']=[{'id':'015-D19-glyph','reading':by['015-D19-glyph']['final'],'confidence':'low','position':by['015-D19-glyph']['full_scan_boxes'],'reason':'crowded glyph/formula alternatives remain qualified'}, {'id':'015-G-REMNANT','reading':by['015-G-REMNANT']['final'],'confidence':'medium','declared_full_origin':[932,2239],'literal_local_command':r'\draw (24,6) -- (26,16);','reason':'visible upright shape retained; role, hand and origin undetermined'}]
 z['reason']='Root section24 groups the final cancelled physical cluster once. Glyph/formula component: low confidence, positions in local_components; H formula retained as alternative. Separate upper upright: medium shape confidence, declared origin (932,2239) and unchanged local command (24,6)--(26,16); role, hand and origin undetermined. The selected C three-path overstrikes remain visible geometry rather than a new unresolved wording component.'
d['doubts']=list(source_doubts.values())
d['main_adjudicated']=False
d['root_choices_applied_through_section']=max(applied.values())
d['root_sections_present']=max(sections)
d['root_approved_decision_entries']=sum(x['main_approved'] for x in d['decisions'])
d['source_counts']['union_decision_entries']=len(d['decisions'])
d['pending_root_decision_ids']=[x['id'] for x in d['decisions'] if not x['main_approved']]
d['provisional_counts']={w:sum(bool(x['diff_'+w]) for x in d['decisions']) for w in ['C','H']}
d['provisional_counts']['scope']='Only expressly applied root choices; all pending choices still false. Not final page totals.'
d['root_actions_pending']=['Complete remaining ink choices: '+', '.join(d['pending_root_decision_ids']),'Attach every retained inventory and decision to the exact final selected source.','Complete root approval after source attachment; main_adjudicated remains false.']
P.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
fp=ROOT/'checks/scan015_reader_fingerprints.json';f=json.loads(fp.read_text());f['files']['root.main_decisions.md']={'path':str(log.relative_to(ROOT.parent)),'sha256':hashlib.sha256(log.read_bytes()).hexdigest(),'bytes':log.stat().st_size};fp.write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n')
union=ROOT/'checks/scan015_union.md';u=union.read_text();marker='\n## Applied root choices\n';u=u.split(marker)[0]
u+=marker+'\nThe following decisions are authoritative root choices from the current decision log. Other union rows remain pending; the full record preserves each independent return.\n\n| Locus | Root section | Final | Confidence | C count | H count | C doubt |\n|---|---|---|---|---|---|---|\n'
def esc(v):return str(v).replace('|','\\|').replace('\n','<br>')
for x in d['decisions']:
 if x['main_approved']:u+='| '+' | '.join(esc(v) for v in [x['id'],x['root_decision_section'],x['final'],x['confidence'],int(x['diff_C']),int(x['diff_H']),x['C_doubt_status']])+' |\n'
union.write_text(u)
print(json.dumps({'root_sections_present':max(sections),'approved_decisions':d['root_approved_decision_entries'],'pending_decisions':len(d['pending_root_decision_ids']),'provisional_counts':d['provisional_counts']},ensure_ascii=False))
