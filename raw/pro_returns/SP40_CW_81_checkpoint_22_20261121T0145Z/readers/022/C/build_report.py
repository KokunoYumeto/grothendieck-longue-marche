from pathlib import Path
import json,re,hashlib,collections

ROOT=Path('/workspace/scratch/94548b74fbe0'); OUT=ROOT/'out/readers/022/C'
def read(p):return (ROOT/p).read_text()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
C=read('packets/022/C.tex');H=read('packets/022/H.tex');T=(OUT/'reading.tex').read_text()
sig=json.loads((OUT/'sigma_groups.json').read_text()); groups=json.loads((OUT/'source_groups.json').read_text()); crops=json.loads((OUT/'crop_manifest.json').read_text())
diff=[]
def row(id,location,c,h,r,e,kind,dc,dh,crop=None,bbox=None,cs=None,confidence='high',cluster=None,hmark=None,qualified=False,source_ids=None):
    diff.append(dict(id=id,location=location,C=c,H=h,reading=r,evidence=e,confidence=confidence,kind=kind,diff_C=dc,diff_H=dh,C_doubt_status=cs,readers_crop=crop,bbox=bbox,physical_cluster=cluster or id,marked_in_H=bool(hmark),H_local_doubt_marker=hmark,H_marker_scope='actual local marker only; plain struck state and descriptive apparatus are not doubt markers',qualified_difference=qualified,source_group_ids=source_ids or []))

row('D01','opening cancelled initial word','On','Un',r'\unsure{On|Un}','The first tall oval is open at its upper approach and has a low n-like continuation. On remains strongest; the open top also supports H’s Un. The source retains both whole words.','misread word',True,True,'c01_opening.png',[290,75,381,128],confidence='medium',qualified=True)
row('D02','opening cancelled verb','procède','procédé',r'\unsure{procède|procéde|procédé}','A short raised mark appears over the medial e region. Its direction and the terminal e region are crowded by the crossing stroke. Procède remains first; procédé and the locally accented procéde remain explicit alternatives.','misread word',True,True,'c01_opening.png',[409,97,643,152],confidence='low',qualified=True)
row('D03','interlinear On note d’abord que',r'\inserted{On note d\'abord que}',"On note d'abord que",r'\inserted{On note d\'abord que}','The live sentence occupies the line between the two struck openings. H places it after a continuous struck sequence and supplies no add marker.','insertion or placement',False,True,'c01_opening.png',[310,140,816,191])
row('D04','small opening curve before alpha in K',r'\unsure{(}',r'($\alpha\in K$)',r'(','The tall separate left curve is visible before the low alpha and is longer than alpha’s own curved entry.','other',True,False,'c02_top_right.png',[1528,180,1555,222],cs='resolved')
row('D05','right-edge curve after K','no closing curve after K',r'($\alpha\in K$)',r'qualified partial ) graphic; blank role alternative retained','A pale oblique curve starts to the right of K and continues into the physical right edge. The surviving segment is drawn without completing its unseen end. H’s primary closing parenthesis is retained with qualification, so this is no H qualifier-only count.','omission',True,False,'c02_top_right.png',[1658,207,1679,241],confidence='medium',qualified=True,source_ids=['C022-G02'])
row('D06','top-right final word',r'\unsure{disjoints|disjointes}','disjoints',r'\unsure{disjoints|disjointes}','The final t/short returning ending meets the large closing parenthesis; the crop leaves the e/no-e distinction open.','other',False,False,'c02_top_right.png',[1530,239,1676,298],cs='retained',confidence='medium',qualified=True)
row('D07','bracket below X minus union',r'\underbrace{X\setminus\bigcup...}',r'\note{sous l\'accolade qui souligne ...}', 'flat-bottomed bracket with upturned ends and two separate descending ticks','The observed lower guide has a nearly flat horizontal bottom and rounded upturned ends. No central downward cusp is visible. Its two equality ticks are reproduced separately. H’s generic descriptive accolade is compatible with this geometry.','drawing or diagram',True,False,'c02_top_right.png',[1076,250,1269,304],source_ids=['C022-G01'])
row('D08','left brace beside two conditions',r'\left\{',r'\left\{','literal upper arm, closed small middle loop, and lower arm','The middle turn closes a small oval before continuing into the lower arm. An ordinary brace does not reproduce that loop.','drawing or diagram',True,True,'c03_first_conditions.png',[534,288,563,480],source_ids=['C022-G04'])
row('D09','first cancelled relation in lower condition',r'\deleted{\unsure{\ne|=}\varnothing}',r'\note{... le $\neq$ remplace un $=$ biffé}',r'deleted neq primary / deleted equals alternative; complete literal relation strokes','Two short horizontal levels, a hooked descending stroke and heavier crossing runs survive. The descending stroke supports neq but can also participate in the cancellation. H’s equals remains an explicit alternative. The geometry is new in the proposed source; the original C doubt is retained.','misread symbol or index',True,True,'c03_first_conditions.png',[795,415,862,454],cs='retained',confidence='low',cluster='CL_OLD_CONDITION',qualified=True,source_ids=['C022-G03'])
row('D10','old empty-set shape beside cancelled relation',r'\deleted{...\varnothing}', 'only replacement empty set; note names an old equals', 'old oval/slash and its superposed cancelling diagonals, followed by the live neq empty set','The struck old oval and slash occupy a separate position before the replacement. Their crossing diagonals are drawn once together with the old relation.','omission',True,True,'c03_first_conditions.png',[871,384,922,477],cluster='CL_OLD_CONDITION',source_ids=['C022-G03'])
row('D11','words between the two lower conditions','alors que','dès que','alors que','The first word has the ascending l followed by the low ors run. It is visible independently on half a.','misread word',False,True,None,{'image':'half a','origin':[0,0],'bbox':[1090,401,1300,484]})
row('D12','arrow from trivial',r'\longrightarrow with a comment that it crosses the brace',r'\marginal{trivial}; note says left of second line','thin shaft crossing the brace, with two short right-pointing head segments','The shaft starts at the end of trivial and crosses the lower brace arm before its arrowhead. H records the word’s position but omits the arrow. C already specifies the crossing arrow.','omission',False,True,'c03_first_conditions.png',[479,426,587,449],source_ids=['C022-G04'])
row('D13','lower-left annotation under precise equality',r'\inserted{\overline V\cap\widehat\Sigma_\alpha^+}',r'\note{au-dessous, une ligne biffée d\'un trait: « $=\overline V\cap\widehat\Sigma_\alpha^+$ » sous le membre de gauche}',r'live inserted formula primary; deleted inserted formula alternative','The upper cancellation boundary passes through the V tip and immediately below the rest of the small formula. Its intended scope remains open. The complete state alternatives are retained in the local source annotation.','deletion state (struck given live or live given struck)',True,True,'c04_main_annotations.png',[684,742,876,810],confidence='low',cluster='CL_ANNOTATION_LEFT',qualified=True,source_ids=['C022-A01'])
row('D14','connector above small right annotation',r'\rotatebox{90}{$\unsure{\deleted{=}|=|\Rightarrow}$}', 'note gives the right formula but no local connector glyph', 'qualified shared horizontal plus three short oblique ticks; deleted vertical equals / equals / implication candidates','A horizontal run and three local ticks are visible. The two right ticks support the vertical equality reading, while the left short oblique and shared run leave the cancellation/bar role open. The long horizontal is owned once, not duplicated as a second bar.','drawing or diagram',True,True,'c04_main_annotations.png',[1007,734,1074,757],cs='retained',confidence='low',cluster='CL_ANNOTATION_RIGHT',qualified=True,source_ids=['C022-G06'])
row('D15','complete lower-right annotation',r'\inserted{\overline{\Sigma_\alpha^-}\cap\widehat\Sigma_\alpha^+}',r'\note{une ligne biffée ... « $\overline{\Sigma_\alpha^-}\cap\widehat\Sigma_\alpha^+$ » sous celui de droite}', 'live inserted formula primary; deleted inserted formula alternative','The lower boundary crosses the small alpha region and runs directly under the formula. The whole formula receives a local qualifier, with complete live/cancelled state alternatives in its invisible annotation.','deletion state (struck given live or live given struck)',True,True,'c04_main_annotations.png',[998,725,1185,801],confidence='low',cluster='CL_ANNOTATION_RIGHT',qualified=True,source_ids=['C022-A02'])
row('D16','connected cancellation of the abandoned proof','generic deleted text and displays',r'\note{tout ce passage est encadré d\'un trait et barré de plusieurs longues diagonales}', 'complete connected top/left/bottom boundary runs, bent returns, interior diagonals and local strikes','The boundary has successive bent returns around rencontre, the old noun and l’espace, and a final lower loop around disjointes. Long interior diagonals cross several lines. The exact drawn source is new; H already describes the global cancelled state. This H row is one drawing-description replacement parent.','drawing or diagram',True,True,None,{'image':'full plus halves a/b','origin':[0,0],'bbox':[260,770,1603,1850]},cluster='CL_CANCELLATION_FRAME',source_ids=['C022-G05-PATHS'])
row('D17','endpoint of cancelled inverse inclusion',r'\deleted{\overline{\Sigma_\alpha^-}\cap E_\alpha\subset\overline V\cap E_\alpha}',r'\struck{$\overline{\Sigma_\alpha^-}\cap E_\alpha\subset\overline V\cap E_\alpha$.}', 'same cancelled expression without a terminal full stop','After the final alpha there is clear paper before the separate remote diagonal; no period is supported at the expression endpoint.','text not on the page',False,True,'c05_cancelled_upper.png',[1025,1020,1200,1110])
row('D18','endpoint after rencontre', 'rencontre',r'rencontre \ill{}.', 'rencontre, followed by the bent frame and no supplied additional word or full stop','Half b shows the final low ending of rencontre and the line curving away toward the next restart. No separate character candidate is supported in the gap. The H ill and attached point are one endpoint cluster.','text not on the page',False,True,None,{'image':'half b','origin':[0,1101],'bbox':[245,258,680,330]},hmark=r'\ill{} immediately after rencontre')
row('D19','small cancelled word after Or',r'\deleted{\unsure{on}}',r'\struck{Or \ill{} par construction ...}',r'\deleted{\unsure{on}}','A small oval followed by an n-like returning stroke survives below a short local strike. On remains tentative. The H ill-placeholder is at this exact locus.','readable ink left as \\ill{}',False,True,'c07_or_on.png',[816,1327,922,1386],cs='retained',confidence='low',hmark=r'\ill{} immediately after Or',qualified=True)
row('D20','word after cancelled on','peut','par','peut','A descending p is followed by the low eu continuation and final raised t turn.','misread word',False,True,'c07_or_on.png',[948,1340,1054,1388],confidence='medium')
row('D21','following verb','considérer','construction','considérer','The long low beginning is followed by a tall d and the small raised accent/ending strokes; the complete visible run reads considérer.','misread word',False,True,'c07_or_on.png',[1090,1329,1432,1383],confidence='medium')
row('D22','cancelled noun under inserted égalité',r'\unsure{formule|relation}',r'\note{« égalité » remplace un mot biffé en début de ligne}', 'formule','The initial descending f and its crossing, the following rounded/arched sequence, and the later tall l are visible through the two cancellation runs. Formule is supported; relation is removed. The extreme f descender is clipped in this crop but was fully visible on half b. H’s note describes a replaced word without giving it.','omission',True,True,'c08_old_noun.png',[273,1447,500,1545],cs='resolved',confidence='medium')
row('D23','cancelled variable before hat Sigma minus',r'\unsure{Y|Z}',r'\note{... devant « $=\widehat\Sigma_\alpha^-$ » un $X$ est biffé}', 'literal cancelled Y-like cluster, with Y / Z / X alternatives','An upper branching pair, a heavy descending diagonal and a short lower foot survive. Y remains strongest; the foot supports Z and the crossing supports H’s X. The whole cancelled glyph is retained once.','misread symbol or index',True,True,'c09_old_variable.png',[572,1558,640,1636],cs='retained',confidence='low',qualified=True,source_ids=['C022-G07'])
row('D24','cancelled continuation beneath equality','dans lequel','dans laquelle','dans lequel','The ending after the q/u run closes with el; there is no added le sequence for laquelle. This was readable on half b.','misread word',False,True,None,{'image':'half b','origin':[0,1101],'bbox':[303,575,665,700]})
row('D25','live fermées emphasis',r'\uline{fermées}', 'fermées',r'\uline{fermées}','A separate underline lies below fermées. The following disjointes has its own underline, already represented by H emph.','omission',False,True,None,{'image':'half b','origin':[0,1101],'bbox':[567,765,784,845]})
row('D26','last line endpoint','ce qui est immédiat','ce qui est immédiat.','ce qui est immédiat','The last t ends with its long slant/return; the paper to its right contains no detached terminal point.','text not on the page',False,True,None,{'image':'half b','origin':[0,1101],'bbox':[293,1164,1040,1242]})
row('D27','isolated lower oblique stroke','absent','absent','qualified literal descending oblique stroke','One short dark diagonal lies in the gap above/right of disjointes and below the preceding line. It is detached from les and from the older fermées descender. Its role and hand remain undetermined.','omission',True,True,'c10_detached_stroke.png',[1212,1832,1240,1858],confidence='high',qualified=True,source_ids=['C022-M01'])
row('D28','isolated trace left of cancellation frame','absent','absent','qualified short upright/curving trace','A tiny narrow stroke sits left of the main frame in the blank interval above prouvons. Its shape is preserved without a letter or role assignment.','omission',True,True,'c05_cancelled_upper.png',[247,887,257,908],confidence='medium',qualified=True,source_ids=['C022-M02'])
row('D29','small point inside final Sigma','absent','absent','qualified point inside the final Sigma body','A detached dark point lies in the open interior, separated from the upper oblique body stroke. It is part of the complete S17 source group but has its own unresolved role and hand.','omission',True,True,'c11_bottom_pair.png',[1207,1976,1216,1986],confidence='high',cluster='CL_S17',qualified=True,source_ids=['C022-M03','C022-S17'])
row('D30','small relation after bottom Z','=','=', 'qualified paired/returning literal sign, primary equals','The small top and bottom runs appear to turn together at the right. The visible returning shape is reproduced; its exact join and interpretation remain qualified. The primary equals reading is unchanged in H. H’s count here concerns the visible returning geometry, not the editorial qualifier.','drawing or diagram',True,True,'c11_bottom_pair.png',[975,1991,998,2010],confidence='low',qualified=True,source_ids=['C022-G09'])
row('D31','shared upper rule over first cancelled RHS Sigma',r'\overline{\Sigma_\alpha^-}',r'\overline{\Sigma_\alpha^-}', 'same visible barred Sigma, with closure-rule/frame sharing qualified','The local dark upper run sits on the connected upper frame. It is preserved once, together with the letter head below it. The bar reading remains first; the relation of the local run to the cancellation boundary remains open. Its complete high extent was seen on half a; c05 begins just below its top.','other',True,False,None,{'image':'half a','origin':[0,0],'bbox':[1398,765,1508,849]},confidence='low',cluster='CL_S11',qualified=True,source_ids=['C022-S11','C022-G05-PATHS'])

# Each separated Sigma head is independently checked. Connected ordinary heads
# are documented in notation and have no witness-correction flag.
no_change={3,6,12}
crop_for={1:'c02_top_right.png',2:'c02_top_right.png',3:'c02_top_right.png',4:'c03_first_conditions.png',5:None,6:'c04_main_annotations.png',7:'c04_main_annotations.png',8:'c04_main_annotations.png',9:'c04_main_annotations.png',10:'c05_cancelled_upper.png',11:None,12:'c05_cancelled_upper.png',13:'c06_soit.png',14:'c09_old_variable.png',15:'c09_old_variable.png',16:'c11_bottom_pair.png',17:'c11_bottom_pair.png'}
for g in sig:
    n=int(g['id'][-2:])
    if n in no_change:continue
    cl='CL_ANNOTATION_LEFT' if n==7 else ('CL_ANNOTATION_RIGHT' if n in (8,9) else f'CL_S{n:02}')
    row(f'DS{n:02}',f'Sigma locus {n:02}, full bbox {g["observed_bbox"]}', 'ordinary Sigma macro with the locally recorded index/sign/roof/bar', 'ordinary Sigma macro in the body or its explanatory annotation', 'literal separate short head and angled body with unchanged index/sign and existing roof/bar', 'The upper short run and body entrance were inspected locally. The source draws the observed spacing rather than joining the head into a standard printed Sigma. Each index, raised sign and roof/bar is owned by this complete glyph once; shared bars are explicitly assigned to the surrounding path owner.','drawing or diagram',True,True,crop_for[n],g['observed_bbox'],confidence='medium',cluster=cl,qualified=True,source_ids=[g['id']])

# Exact witness spans accompany every shorthand field above. These are literal
# file excerpts, including actual local punctuation and note macro boundaries.
hranges={
'D01':(2,3),'D02':(2,3),'D03':(2,5),'D04':(4,5),'D05':(4,5),'D06':(4,5),'D07':(6,8),'D08':(9,17),'D09':(12,20),'D10':(12,20),'D11':(13,14),'D12':(18,20),'D13':(27,30),'D14':(27,30),'D15':(27,30),'D16':(32,46),'D17':(35,36),'D18':(37,39),'D19':(40,41),'D20':(40,41),'D21':(40,41),'D22':(40,46),'D23':(42,46),'D24':(43,43),'D25':(48,48),'D26':(58,58),'D27':(48,52),'D28':(32,34),'D29':(50,51),'D30':(50,51),'D31':(32,33)}
sranges={1:(3,5),2:(3,5),3:(6,8),4:(13,14),5:(13,14),6:(24,25),7:(27,30),8:(27,30),9:(27,30),10:(32,33),11:(32,33),12:(35,36),13:(37,39),14:(42,46),15:(42,46),16:(50,51),17:(50,51)}
hl=H.splitlines();cl=C.splitlines()
canchors={'D01':'On procède','D02':'On procède','D03':'On procède','D04':'On procède','D05':'On procède','D06':'On procède','D07':'On procède','D08':r'\left\{','D09':r'\makebox','D10':r'\makebox','D11':'alors que','D12':r'\makebox','D13':r'\underset{\inserted{\overline V','D14':r'\hspace{1em}','D15':r'\hspace{1em}','D16':r'\deleted{Comme','D17':r'\deleted{\overline{\Sigma','D18':r'\deleted{Soit','D19':r'\deleted{Or}','D20':r'\deleted{Or}','D21':r'\deleted{Or}','D22':r'\deleted{Or}','D23':r'\deleted{\unsure{Y','D24':r'\deleted{dans lequel','D25':'Or dans','D26':'ce qui est','D27':'Or dans','D28':r'\deleted{Comme','D29':'Y=','D30':'Y=','D31':r'\deleted{Comme'}
for d in diff:
    for key in ('C','H','reading'):
        if isinstance(d[key],str):d[key]=d[key].replace("\\'", "'")
    span=sranges[int(d['id'][2:])] if d['id'].startswith('DS') else hranges[d['id']]
    d['H_exact_source_lines']=list(span);d['H_exact_source']='\n'.join(hl[span[0]-1:span[1]])
    if d['id'] in canchors:
        hit=next((i for i,x in enumerate(cl,1) if canchors[d['id']] in x),None)
        d['C_exact_source_lines']=[hit,hit] if hit else None;d['C_exact_source']=cl[hit-1] if hit else None
    else:
        sn=int(d['id'][2:]);occ={1:2,2:3,3:1}.get(sn,sn)
        sm=list(re.finditer(r'\\Sigma',C))[occ-1]
        ln=C.count('\n',0,sm.start())+1
        d['C_exact_source_lines']=[ln,ln];d['C_exact_source']=cl[ln-1]
        d['C_actual_Sigma_occurrence']=occ
    d['H_apparatus_classification']='H note text is witness apparatus; only its actual quoted/manuscript readings and described states are compared. The quoted exact span remains unmodified.'

rows=[]
doubt_defs=[
 ('C022-R01','opening, after hatted terms','(',['—'],'resolved',['D04'],['opening curve present']),
 ('C022-R02','top right, last word','disjoints',['disjointes'],'retained',['D06'],['terminal e/no-e and closing-parenthesis contact']),
 ('C022-R03','second line of first brace, first crossed relation','≠',['='],'retained',['D09'],['relation candidate; cancellation itself visibly present']),
 ('C022-R04','below right side of main equality','crossed vertical =',['=','⇒'],'retained',['D14'],['connector glyph','cancelled/live status of connector']),
 ('C022-R05','inside cancellation after Or','on',['—'],'retained',['D19'],['whole small word']),
 ('C022-R06','under interlinear égalité','formule',['relation'],'resolved',['D22'],['whole old noun']),
 ('C022-R07',"after l’espace, old variable",'Y',['Z'],'retained',['D23'],['old variable candidate; cancelled state remains explicit']),
]
for i,(id,loc,reading,alts,status,ds,parts) in enumerate(doubt_defs,1):
    actual=[d for d in diff if d['id'] in ds]
    rows.append(dict(source_id=id,source_row_ordinal=i,section='Doubtful readings',source_location=loc,source_reading=reading,source_alternatives=alts,source_macro_and_table_agree=True,status=status,decision_ids=ds,local_parts=parts,extra_supported_alternatives=['X'] if i==7 else [],duplicate_source_mentions=[],original_identity_count=1,local_records=actual))

local_glyph_audit=[]
for g in sig:
    n=int(g['id'][-2:]); alts=['letter head or local retrace','independent upper run'] if n not in no_change else []
    local_glyph_audit.append(dict(**g,crop=crop_for[n],local_alternatives=alts,primary='Sigma with literal upper run and body',printed_qualifier=(n in (1,11)),qualifier_reason='first recurring head-role occurrence' if n==1 else ('independent shared frame/bar qualification' if n==11 else 'first-occurrence rule; later local candidates remain in this record' if alts else 'locally connected ordinary head'),witness_change=n not in no_change))

doubts=[]
for d in diff:
    if d['C_doubt_status']=='retained' or (d['qualified_difference'] and d['id'] not in ('D09','D10') and not d['id'].startswith('DS')):
        doubts.append(dict(id=d['id'],location=d['location'],reading=d['reading'],alternatives=(['X','Z'] if d['id']=='D23' else ['see complete local reading/state alternatives and literal source']),confidence=d['confidence'],reason=d['evidence'],crop=d['readers_crop'],source_row_id=next((r['source_id'] for r in rows if d['id'] in r['decision_ids']),None),physical_cluster=d['physical_cluster']))

# Inventory keeps original identities, updates the actual selected states, and
# interleaves graphical components at their observed page positions.
inv=json.loads(read('packets/022/C_inventory.json'))
ys=[110,161,211,240,310,370,441,431,575,695,780,770,746,850,1060,1060,1240,1358,1365,1360,1495,1453,1480,1602,1602,1725,1800,2000,2115,2220,2310]
for v,y in zip(inv,ys):
 v['hand']='his hand';v['source_identity']='C_inventory '+v['element'];v['page_order_y']=y
 if v['element']=='022.01':v['first_words_or_objects']='cancelled On/Un procède/procéde/procédé par récurrence sur card K,'
 if v['element']=='022.04':v['first_words_or_objects']='(si V=... les hatted Sigma (alpha in K, partial closing curve, étant disjoints/disjointes)'
 if v['element'] in ('022.11','022.12'):v['first_words_or_objects']+='; live inserted primary / cancelled inserted alternative'
 if v['element']=='022.13':v['first_words_or_objects']='shared horizontal plus three ticks, connector glyph and cancellation role qualified'
 if v['element']=='022.21':v['first_words_or_objects']='formule, cancelled, source doubt resolved'
 if v['element'] in ('022.24','022.25'):v['first_words_or_objects']='cancelled Y/Z/X = hatted Sigma minus = Sigma minus union E'
 if v['element']=='022.27':v['first_words_or_objects']='Or dans X on a les deux parties fermées disjointes; fermées and disjointes each underlined'
for g in sig:
 inv.append(dict(sheet_kind='text',hand='his hand',element=g['id'],kind='drawing',position='full bbox '+str(g['observed_bbox']),first_words_or_objects='complete literal Sigma, index '+g['index'][2]+', raised '+g['sign'][2]+('; hat' if g['hat'] else '')+('; closure/shared upper rule' if g['bar'] or g['shared_bar'] else ''),transcribed='yes',page_order_y=g['observed_bbox'][1],source_identity='new literal component of an existing formula',component_confidence='medium',source_group=g['id']))
extra=[
 ('I_G01','his hand','drawing',255,'flat bracket and paired downward equality ticks','C022-G01'),
 ('I_G02','undetermined hand','drawing',214,'partial right-edge closing curve after K; relation to parenthesis qualified','C022-G02'),
 ('I_G03','his hand','deletion',425,'old relation/empty-set cluster and cancelling strokes','C022-G03'),
 ('I_BRACE','his hand','drawing',290,'looped brace and crossing trivial arrow','C022-G04'),
 ('I_G06','his hand','drawing',740,'shared horizontal and three oblique connector ticks','C022-G06'),
 ('I_FRAME','his hand','drawing',774,'connected cancellation frame and interior diagonals; all literal path commands','C022-G05-PATHS'),
 ('I_M02','undetermined hand','drawing',891,'small isolated upright/curving trace left of frame','C022-M02'),
 ('I_G07','his hand','deletion',1570,'cancelled Y/Z/X literal cluster with foot and crossings','C022-G07'),
 ('I_M01','undetermined hand','drawing',1837,'detached short falling oblique stroke','C022-M01'),
 ('I_U1','his hand','text',1905,'underline under fermées','C022-G05'),
 ('I_U2','his hand','text',1906,'separate underline under disjointes','C022-G05'),
 ('I_M03','undetermined hand','drawing',1981,'small point in final Sigma interior; hand/role unresolved','C022-M03'),
 ('I_G09','his hand','drawing',1997,'small paired/returning sign after Z, primary equals','C022-G09'),
 ('I_ARCHIVE','undetermined hand','text',2327,'archive numeral 21, recorded only in a TeX comment',None),
]
for ident,hand,kind,y,words,gid in extra:inv.append(dict(sheet_kind='text',hand=hand,element=ident,kind=kind,position='local region near full-scan y='+str(y),first_words_or_objects=words,transcribed='yes',page_order_y=y,source_group=gid))
inv.sort(key=lambda v:(v['page_order_y'],v['element']))

# Stack-derived literal path ownership. No rendered bounds or image comparison is computed.
events=[]
for m in re.finditer(r'% (BEGIN|END) (C022-[A-Z0-9-]+)|\\(?:draw|fill)\b[^\n]*',T):events.append(m)
stack=[];paths=[];parents={}
for m in events:
 if m.group(1)=='BEGIN':
  parents[m.group(2)]=stack.copy();stack.append(m.group(2))
 elif m.group(1)=='END':
  if stack and stack[-1]==m.group(2):stack.pop()
 else:
  paths.append(dict(id=f'P{len(paths)+1:03}',owner=stack[-1] if stack else None,ancestor_groups=stack[:-1],start_char=m.start(),line=T.count('\n',0,m.start())+1,literal=m.group(0)))
(OUT/'path_components.json').write_text(json.dumps(paths,ensure_ascii=False,indent=2)+'\n')
ownership=[]
for g in groups:
 ownership.append(dict(id=g['id'],ancestors=parents.get(g['id'],[]),source_start=g['start_char'],source_end_exclusive=g['end_char_exclusive'],source_lines=[g['start_line'],g['end_line']],enclosing_line_prefix=g['enclosing_line_prefix'],following_line=g['following_line'],direct_components=[v['id'] for v in paths if v['owner']==g['id']],source_sha256=g['sha256'],coordinate_map='Declared in the literal group: local x=X-x0 and y=Y-y0, with x=0.008 cm and y=-0.008 cm; base-west node and zero inner/outer separation. Nested source origins are declared explicitly.',ownership='Read the exact Owns comment in source_groups.json; word-bearing parent groups own their stated complete wording, child mark-only groups own no adjoining word.'))
(OUT/'group_ownership.json').write_text(json.dumps(ownership,ensure_ascii=False,indent=2)+'\n')

rawC=[d for d in diff if d['diff_C']];rawH=[d for d in diff if d['diff_H']]
clustersC=collections.defaultdict(list);clustersH=collections.defaultdict(list)
for d in rawC:clustersC[d['physical_cluster']].append(d['id'])
for d in rawH:clustersH[d['physical_cluster']].append(d['id'])
counts=dict(difference_records=len(diff),raw_diff_C_rows=len(rawC),raw_diff_H_rows=len(rawH),proposed_physical_C_count=len(clustersC),proposed_physical_H_count=len(clustersH),C_clusters=dict(clustersC),H_clusters=dict(clustersH),C_actual_source_doubt_rows=7,C_resolved_source_doubt_rows=2,C_retained_source_doubt_rows=5,C_compound_row_with_explicit_glyph_and_state_parts=['C022-R04'],H_actual_local_ill_markers=2,H_changed_rows_with_actual_local_marker=[d['id'] for d in diff if d['diff_H'] and d['marked_in_H']],sigma_loci=17,sigma_graphical_difference_rows=14,connected_sigma_heads_no_correction=[3,6,12],literal_source_groups=len(groups),literal_draw_or_fill_commands=len(paths),deep_crops=11,full_views=1,half_views=2,failed_unseen_deliveries=0,notes='These are reader proposals only. Raw flags are preserved; the root adjudicates. The old relation/empty set share one physical cluster. Each complete lower annotation clusters its state and constituent head changes. The final Sigma point and head cluster once. A source-row identity is never merged into the physical-change count.')

notes=[
 'The author strikes the opening induction on card K and adds On note d’abord que. He records V as the complement of an indexed union of hatted positive Sigma terms and adds an indexed intersection of negative Sigma terms below it. The page writes barred V intersect E_alpha nonempty, then V intersect Sigma_alpha^- nonempty alors que V intersect Sigma_alpha^+ is empty.',
 'After De façon précise, je dis que, the author writes barred V intersect E_alpha = closure of Sigma_alpha^- intersect E_alpha, with qui est donc nonempty and two small lower annotations. He cancels an inverse-inclusion argument involving x and a neighbourhood W, then another formulation in a space whose crossed variable remains Y/Z/X. The live continuation names Y = hatted Sigma_alpha^+ and Z = the union over beta in K minus {alpha} of hatted Sigma_beta^+, calling them fermées and disjointes with separate underlines.',
 'The final written equality is closure(X minus (Y union Z)) intersect Y = closure(X minus Y) intersect Y. The author follows it with ce qui est immédiat. This is an attributed account of the sheet; no proof or mathematical equivalence was checked.',
 'The author’s exact evaluative words are trivial and ce qui est immédiat; the visible draft corrections are preserved. No explicit authorial uncertainty wording is legible. All unsure qualifications in this reader source are editorial.',
 'No title, date or authorial page count is written. The lower-left archive numeral is 21 and is represented only by the archive comment. H’s page{21} is a source administrative page label, not an additional manuscript number.',
 'No mathematical expectation selected a missing mark. The visible head gaps, shared horizontal/frame, old relation and variable remain graphical or qualified. There are no mathematical check events.'
]

report=dict(scan=22,reader='C',start_utc='2026-11-20 23:47:20 UTC',end_utc=None,full_image_viewed=True,halves_viewed=True,complete_visual_read=True,differences=diff,doubts=doubts,inventory=inv,notes=notes,notation=local_glyph_audit,check_events=[],crops=crops,brief_feedback=['A scalar C_doubt_status cannot encode the right connector’s glyph/state parts by itself; the original row identity and both components are preserved in C_doubt_source_map.', 'Some physically connected cancellation runs also occupy a possible closure-bar position. The selected source draws that shared run once and records its role uncertainty.', 'The first crop of several prose targets clipped a descender or a bar already seen on the supplied halves. These exact boundary limitations are reported; no crop was reopened.'],C_doubt_source_map=rows,counts_proposed=counts,source_group_audit_file='source_groups.json',source_ownership_audit_file='group_ownership.json',literal_path_audit_file='path_components.json',image_audit_file='image_audit.json',source_coordinate_convention=dict(full_image_size=[1691,2362],half_a_origin=[0,0],half_b_origin=[0,1101],half_size=[1691,1261],half_b_offset_derivation='2362 - 1261 = 1101',graphics='All new paths are manual approximations. Coordinates were transcribed from the displayed image; local source coordinates use the explicit subtraction map and fixed pixel units. No curve-extrema, image-difference or rendered-metric calculation was performed.'),S_coverage=dict(source_row='SA01-K81-06',source_scope='81/15-22',source_author_reported_no_scan_view=True,exact_quoted_examples_present=False,local_result='The quoted Sigma_1/U_s examples have no exact occurrence on this page. The principal visible bars already occur in current C and H; this sheet supplies no inferred missing closure bar.',current_bar_loci=['first braced V','precise-equality V and Sigma','lower left V annotation','shared upper run above lower right Sigma','first cancelled RHS Sigma/shared top frame','inverse-inclusion Sigma and V','Soit Sigma and V','next-line x in barred V','final two whole parenthesized expressions'],administrative_only=True),processing_provenance=dict(packet_files_read=['C.tex','H.tex','metadata.json','C_doubts.txt','C_notes.txt','C_inventory.json','S_rows.json','notation.md'],C_notes_blank=True,other_scans_in_notation_context_only=True,brief_truncation=dict(initial_output_truncated=True,recovery_complete=True,recovery_ranges=['1-82','83-164','165-260']),image_order='whole, half a, half b, c01 through c11',failed_unseen_deliveries=[],no_other_reader_or_other_page_inspected=True,no_OCR=True,no_external_sources=True,no_compilation=True,no_rendering=True,no_installation=True,checkpoint=dict(paused_utc='2026-11-20 23:58:02 UTC',saved_first_complete_draft=True,release='root message: Checkpoint20 raw snapshot is complete',read_only_findings='one extra M03 brace and incomplete anchored source-boundary extraction; both repaired after release'),crop_boundary_limits=['c01 lower boundary cuts the already viewed que descender; the word itself is readable','c05 top y775 lies below the highest point of the shared RHS Sigma upper bar; half a supplies the complete run','c06 ends before the separately read rencontre line and near qu’il descender; half b supplies its continuation','c08 clips the extreme f descender of formule; half b supplies its full extent','c10 top clips a continuation of the old fermées descender; the detached target and les are complete'],source_only_arithmetic=['image dimension subtraction to locate half b','manual affine coordinate subtraction for path placement','line/character-offset bookkeeping, path counts and cryptographic hashes'],scope_of_arithmetic='Administrative/source placement only; no mathematical statement was tested.'),input_hashes={str(p.relative_to(ROOT)):sha(p) for p in [ROOT/'packets/022/C.tex',ROOT/'packets/022/H.tex',ROOT/'packets/022/metadata.json',ROOT/'packets/022/C_doubts.txt',ROOT/'packets/022/C_notes.txt',ROOT/'packets/022/C_inventory.json',ROOT/'packets/022/S_rows.json',ROOT/'packets/022/notation.md',ROOT/'out/PREAMBLE.tex',ROOT/'out/briefs/brief_v20_scan022.md']},status='complete reader draft pending final source audit and UTC freeze')
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(OUT/'C_doubt_source_map.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(OUT/'H_local_marker_audit.json').write_text(json.dumps(dict(actual_markers=[{'literal':r'\ill{}','location':'after rencontre','count':1,'decision':'D18'},{'literal':r'\ill{}','location':'after Or','count':1,'decision':'D19'}],no_uncertain_macro=True,local_differences=[{'id':d['id'],'H':d['H'],'marked_in_H':d['marked_in_H'],'marker':d['H_local_doubt_marker']} for d in diff],note='The full struck block, a note describing a struck word, and page-level apparatus do not establish local uncertainty markers.'),ensure_ascii=False,indent=2)+'\n')

md='''# Scan 022 — reader C

The author replaces an opening induction on `card K` with “On note d’abord que”, then states the two nonemptiness conditions and a more precise boundary equality. The cancelled middle drafts use an inverse inclusion, a point `x`, and a neighbourhood `W`. The live ending names two separately underlined closed, disjoint parts `Y` and `Z` and writes the final closure/intersection equality, followed by “ce qui est immédiat”. These are the author’s written assertions; no proof check was performed.

## Line-by-line reading audit

| Page region | Reading and state | Local uncertainty |
| --- | --- | --- |
| Opening struck line | On/Un procède/procéde/procédé par récurrence sur card K, | Initial word and accent/crossing cluster remain qualified. |
| Interlinear restart | On note d’abord que | Insertion and wording are clear. |
| Second struck opening | pour prouver que | Readable; full que descender was seen on half a. |
| Parenthetical V line | (si V=X minus indexed union of hatted Sigma plus, les hatted Sigma plus (alpha in K, étant disjoints/disjointes) | Small opening parenthesis resolved; partial right-edge closing curve preserved; final ending retained uncertain. |
| Lower addition to V | indexed intersection of Sigma minus, with two descending ticks | Flat bracket and ticks drawn literally. |
| First braced condition | barred V intersect E_alpha nonempty | Bar and indices visible. |
| Second braced condition | V intersect Sigma minus, cancelled neq/equals and old empty-set, replacement neq empty-set, alors que V intersect Sigma plus equals empty-set | Old relation stays qualified. Looped brace and crossing trivial arrow retained. |
| Introduction | De façon précise, je dis que | Readable accents and comma retained. |
| Main equality | barred V intersect E_alpha equals barred Sigma minus intersect E_alpha (qui est donc nonempty) | Main reading clear. |
| Lower annotations | barred V intersect hatted Sigma plus; barred Sigma minus intersect hatted Sigma plus | Both complete live/cancelled insertion states remain qualified. Right connector’s glyph and strike/bar role remain open. |
| Cancelled Comme line | Comme V subset Sigma minus, on a V intersect E_alpha subset barred Sigma minus intersect E_alpha, | Shared upper frame/bar over right Sigma is preserved once and qualified. |
| Cancelled next line | prouvons l’inclusion inverse | Readable. |
| Cancelled inverse display | barred Sigma minus intersect E_alpha subset barred V intersect E_alpha | No endpoint period supported. |
| Cancelled Soit line | Soit x in barred Sigma minus intersect E_alpha, prouvons x in barred V intersect E_alpha i.e. | Readable bars, x and i.e. retained. |
| Cancelled continuation | x in barred V, soit W un voisinage de x, montrons qu’il rencontre | No additional word or full stop after rencontre is supplied. |
| Cancelled restart | Or on peut considérer cette | on remains uncertain; peut considérer is readable against H’s par construction. |
| Corrected noun line | cancelled formule, inserted égalité, comme égalité dans | formule resolved from its own surviving f/arches/l. |
| Cancelled space/equality | l’espace, cancelled Y/Z/X = hatted Sigma minus = Sigma minus union E_alpha | Old variable remains qualified; all visible crossings and foot retained. |
| Cancelled final wording | dans lequel on a deux parties fermées disjointes | lequel readable against H’s laquelle. Connected frame and lower return retained. |
| Live restart | Or dans X on a les deux parties fermées disjointes | Both fermées and disjointes are underlined. |
| Detached lower stroke | short falling oblique | Drawn with unresolved role and hand. |
| Bottom Y/Z display | Y=hatted Sigma_alpha plus, Z=union over beta in K minus {alpha} of hatted Sigma_beta plus | Small relation after Z remains qualified; a small point inside final Sigma is preserved with unresolved role/hand. |
| Final instruction/display | et on doit prouver; closure(X minus (Y union Z)) intersect Y = closure(X minus Y) intersect Y | Both existing whole-expression bars retained. |
| Last line/archive | ce qui est immédiat; archive 21 | No terminal period; 21 is comment-only. |

## Principal collation decisions

The reading retains **alors que**, **peut considérer**, **dans lequel**, and the underline under **fermées**. It resolves the old noun as **formule**, while retaining the old relation, the right connector, **on**, the old **Y/Z/X** variable, and **disjoints/disjointes** as local doubts. The two lower annotations retain their complete live/cancelled state alternatives. The literal source preserves the flat upper bracket, looped brace, connected cancellation runs, seventeen complete Sigma groups, and three separately qualified small traces.

There are seven actual C doubtful-reading source rows: two resolved and five retained. Their identities, the right connector’s glyph/state parts, every local H marker scope, every witness-change flag, physical-cluster count proposal, literal path and source boundary are in the structured audit. Ordinary connected Sigma heads at loci 03, 06 and 12 carry no witness-correction flag. No image was reopened, and no compilation or rendering was performed.
'''
(OUT/'reading.md').write_text(md)
print(json.dumps(counts,ensure_ascii=False))
