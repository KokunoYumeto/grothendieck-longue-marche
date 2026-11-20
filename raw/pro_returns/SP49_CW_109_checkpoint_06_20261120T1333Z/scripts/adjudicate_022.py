"""Root adjudication after three independent scan022 returns and 33 crop views."""
from common import *
R=load_page(22)
texts={r:(W/f'readers/022/{r}/reading.tex').read_text() for r in 'ABC'}
ch={r:{d['id']:d for d in R[r]['changes']} for r in 'ABC'}
text=texts['A']
def replace(a,b):
 global text
 assert a in text,a
 text=text.replace(a,b,1)

# Preserve one physical boundary pair, low after the first inclusion, with its
# attachment explicitly doubtful. The first-formula and quotation decisions are
# separately recorded below.
boxA=next(x for x in R['B']['changes'] if x['id']=='boxed_unto')
replace(boxA['c'],boxA['reading'])
replace(r'\deleted{\unsure{does}}',r'\deleted{does}')
replace(r"147 \deleted{\unsure{st}} line 2 ``standard'",r"147 \deleted{st} line 2 \unsure{``|`}standard'")
replace(r"line 20\unsure{.|,} ``with'",r"line 20\unsure{.|,} \unsure{``|`}with'")
replace(r"\deleted{we'll \unsure{work|write}}",r"\deleted{we\unsure{'}ll work}")
replace(r"\deleted{``handiness''}",r"``\deleted{handiness}''")
replace(r'\node[inner sep=0pt](oldns){\deleted{\unsure{n \&}}};',r'\node[inner sep=0pt](oldns){\deleted{\unsure{n \&|n \& s}}};')
replace(r'\unsure{\uline{s}|S|$s_1$}',r'\unsure{\uline{s}|S|$s_1$|$S_1$}')
viewed=json.loads((W/'records/root_022_viewed.json').read_text())+['crops/022/03_circled_151.jpg']
decisions=[]
def add(id,place,c,final,abc,evidence,crops,confidence='medium',kind='other',diff=True,consequential=None):
 d=dict(id='022-'+id,place=place,c=c,h=None,final=final,readers=dict(zip('ABC',abc)),evidence=evidence,crops=crops if isinstance(crops,list) else [crops],confidence=confidence,kind=kind,diff_c=diff,diff_h=False,marked_in_H=False)
 if consequential:d['consequential']=consequential
 decisions.append(d)
def cp(n):
 return next(str(p.relative_to(W)) for p in (W/'readers/022/C/crops').glob(f'{n:02}_*.jpg'))
def ap(n):
 return next(str(p.relative_to(W)) for p in (W/'readers/022/A/crops').glob(f'{n:02}_*.jpg'))
def ar(id):return ch['A'][id]['reading']
def br(id):return ch['B'][id]['reading']
def cr(id):return ch['C'][id]['reading']

first=r'\unsure{R|K}_h\subset\unsure{R|K}_n'
add('first-inclusion','p.116 line -6, original inclusion',r'\unsure{R|K}_{\unsure{h|n}}\subset R_n',first,[first,r'\unsure{R|K}_{h}\subset \unsure{R|K}_n',r'\unsure{R|K}_h\subset \unsure{R|K}_n'],'Root confirms a tall first subscript stem with a low arch: h. Each original capital separately has a pale incomplete upper contour over dark K-like diagonals, so R/K remains possible at both occurrences. The later clear replacement R does not decide the faded capitals.',cp(1),kind='misread symbol or index',consequential='The first original subscript resolves to h; the second original capital acquires its own R/K doubt. The written replacement R_h subset Sigma_h is unchanged.')
boundary=r"\raisebox{-1.1ex}{\unsure{''}}"
add('boundary-pair','Between the first inclusion and commutation',"R_n$'' should be $R_h\\subset\\Sigma_h$.\n\np117 line 11 \\& 12, ``commutation",first+"$"+boundary+" should be $R_h\\subset\\Sigma_h$.\n\np117 line 11 \\& 12, commutation",["$"+boundary+" should be $R_h\\subset\\Sigma_h$.\n\np117 line 11 \\& 12, commutation","$'' should be $R_h\\subset\\Sigma_h$.\n\np117 line 11 \\& 12, commutation",r'$ should be $R_h\subset\Sigma_h$.'+'\n\np117 line 11 \\& 12, '+r'\unsure{``}commutation'],'Only one pair is physically present below/right of the first inclusion and above/left of commutation. Root adopts A’s low placement and explicit attachment doubt. B assigns it unreservedly to the first line; C places it at the second line. C witness duplicates the pair. The final has one pair, not a reconstructed second pair.',[cp(1),cp(2),ap(2)],kind='insertion or placement')
add('boxed-insertion','p.119 line5, boxed addition and arrowhead',boxA['c'],boxA['reading'],[boxA['c'],boxA['reading'],boxA['c']],'Root sees the tiny trace immediately beneath the top-left enclosure, without two secure independent opening strokes before not; B’s new doubt is adopted. The quotes around unto and onto are distinct. At the far-right arrow tip, a second angular stroke is visible; B’s additional head contour is retained. No textual meaning is assigned to the head retracing.',cp(3),'low','drawing or diagram')
add('margin-geometry','Left of p.123, cancelled marginal reference',ch['A']['cancelled-margin-geometry']['c'],ar('cancelled-margin-geometry'),[ar('cancelled-margin-geometry'),ch['A']['cancelled-margin-geometry']['c'],cr('C022-03')],'Root confirms the left position and several long nonparallel crossings, including a lower return beyond the letters. A’s left-margin placement and drawn paths are adopted. The interior punctuation is decided separately, without confusing secure cancellation extent with secure letters.',cp(4),'high','insertion or placement')
add('margin-leading-sign-retained','Cancelled p122 reference, first sign',r'\unsure{?}',r'\unsure{?}',[r'\unsure{?}',r'\unsure{?}','?'],'Root sees a clear upper question-like hook, but its lower end enters the crossing and no separate dot can be isolated. A/B’s retained doubt is adopted against C’s resolution. The complete visible sign remains represented.',cp(4),'low',diff=False)
add('p132-single-opener','p132 line -14, opening quotation',"``wasn't''","`wasn't''",["`wasn't''"]*3,'One detached curved upright precedes the word; the two closing strokes and internal apostrophe are separate. All readers and root resolve a single opener.',cp(8),'high')
add('deleted-does','p.146, cancelled word',r'\deleted{\unsure{does}}',r'\deleted{does}',[r'\deleted{\unsure{does}}',r'\deleted{does}',r'\deleted{\unsure{does}}'],'Root adopts B with medium confidence: the first low bowl and tall looped ascender give d, the next closed loop gives o, followed by an open e turn and the final curled s. The horizontal crossings obscure junctions but leave these bodies separately visible. The adjacent live contraction is not used to restore them.',cp(11),'medium')
add('or','p.146 line -1, connector',r'\unsure{or}','or',['or']*3,'The closed left oval and right short shoulder with its long exit are distinguishable. Root resolves the word with all three readers, at medium confidence because the join is heavy.',cp(12))
add('deleted-st','147, cancelled start before line2',r'\deleted{\unsure{st}}',r'\deleted{st}',[r'\deleted{\unsure{st}}',r'\deleted{st}',r'\deleted{st}'],'Root adopts B/C: a low s curl with a separate lower turn precedes a tall t stem and crossbar. The rising cancellation is distinguishable from those letter contours. The later standard is not used as evidence.',cp(13))
add('147-standard-opener','147 line2, opener before standard','``',r'\unsure{``|`}',['``',r'\unsure{``|`}','``'],'Root sees a compact raised peak with two short joined legs. A double opener is favoured, but one bent stroke remains possible. B’s occurrence-specific new doubt is adopted; the clear single closer remains single.',ap(13))
add('line20-punctuation','147 line20, after reference number','','\\unsure{.|,}',[r'\unsure{.|,}','.',r'\unsure{,|.}'],'A low oblique dark mark stands apart from the high opener. Its compact body at the reference baseline favours a period, while its slight tail permits comma. Root adopts A’s preference and retained alternative rather than B’s certain stop.',cp(14))
add('line20-opener','147 line20, opener before with','``',r'\unsure{``|`}',['``',r'\unsure{`|``}',r'\unsure{``|`}'],'The high curved cap has joined ends but no secure internal separation. Root favours the fused double form, also allowing one curved stroke. A’s unmarked double is not adopted. The single closer after with and double closer after to are unchanged.',cp(14))
add('149-opener','149., pair before line7',r'\unsure{``}','``',['``']*3,'Two separate short raised uprights precede the large l loop. All readers resolve the pair; root confirms on C’s crop.',cp(16),'high')
add('circled151-angle','Circled151 oval at arrow endpoint',ch['A']['circled151-angle']['c'],ar('circled151-angle'),[ar('circled151-angle'),ch['A']['circled151-angle']['c'],ch['A']['circled151-angle']['c']],'Root’s one tight geometry crop confirms the oval’s long axis rises to the right. A’s approximately32-degree rotation is adopted. The curved arrow reaches its upper edge; no different reference number is inferred. The angle is a geometric approximation.','crops/022/03_circled_151.jpg','high','drawing or diagram')
add('work','Circled151 right continuation, cancelled verb',r'\unsure{work|write}','work',[r'\unsure{work|write}','work',r'\unsure{work|write}'],'Root adopts B at medium confidence: a low w is followed by a closed o, a short r connection, and a tall final stem with a right arm consistent with k. The rounded second body does not support the r-i sequence of write. Crossing strokes still limit confidence.',cp(19))
add('well-apostrophe','Circled151 right continuation, cancelled apostrophe',"we'll",r"we\unsure{'}ll",["we'll",r"we\unsure{'}ll","we'll"],'The w, e and two tall l loops are visible, but no independent apostrophe can be isolated above their crowded join. Root adopts B’s new doubt; grammar does not supply a definite apostrophe.',cp(19),'low')
add('terminal-fragment','Circled151 right continuation, live fragment after cancellation',r'\unsure{in|n}',r'\unsure{n|in}',[r'\unsure{n|in}','n',r'\unsure{n|in}'],'One initial upright and one low arch favour n. Root keeps A/C’s joined-in alternative because the crowded left edge does not securely exclude an attached i; B’s certain n is not adopted. The separate next-line in (2) remains unchanged.',cp(19),'low')
add('handiness-quotes','p.153, cancellation scope around handiness',r"\deleted{``handiness''}",r"``\deleted{handiness}''",[r"\deleted{``handiness''}",r"``\deleted{handiness}''",r"``\deleted{handiness}''"],'Root confirms the zigzag through the word. The opening pair lies above-left and the closing strokes above-right, outside the actual crossings. B/C’s scope leaves those quote strokes live while cancelling the legible word.',cp(20),kind='deletion state (struck given live or live given struck)')
oldfrag=ar('p153-cancelled-raised-strokes').replace(r'\unsure{n \&}',r'\unsure{n \&|n \& s}')
add('old-n-ampersand','p.153, cancelled fragment after handy',r'\deleted{\unsure{n \&}}',oldfrag,[ar('p153-cancelled-raised-strokes'),r'\deleted{\unsure{n \&}}',r'\deleted{\unsure{n \&|n \& s}}'],'Root preserves the two separate raised strokes identified by A as drawn marks of uncertain attribution. The final curled/descending body could be part of the ampersand or a further s, as C proposes; both old-letter segmentations remain doubtful. The later live n and ampersand do not settle the cancelled forms.',cp(21),'low')
finals=ar('p153-s-tail').replace(r'\unsure{\uline{s}|S|$s_1$}',r'\unsure{\uline{s}|S|$s_1$|$S_1$}')
add('s-lower-stroke','p.153, final live s-shaped sign',r'\unsure{\uline{s}|S}',finals,[ar('p153-s-tail'),br('153_low_s_mark'),r'\unsure{\uline{s}|S}'],'Root sees a short low hook joined to a substantial downstroke. A straight underline alone omits that geometry. A’s drawn downstroke is retained with lower/upper case and low1 alternatives; B’s subscript interpretation is possible, not established. No mathematical meaning is inferred from the wordplay.',cp(21),'low','misread symbol or index',consequential='The final s/S-shaped sign has a lower hook and descending stroke omitted by a simple underline. A subscript1 is now an explicit unresolved alternative, with the observed stroke drawn; no formula has been normalized.')
add('allo','p154 line9, cancelled start',r'\deleted{\unsure{allo}}',r'\deleted{allo}',[r'\deleted{allo}']*3,'Root confirms the low initial a bowl, two tall looped l strokes and separate final closed o. All four letters survive the cancellation independently.',cp(22),'high')
add('will-opener','p154 line9, before will','``will','will',['will','``will','will'],'The gap before will has no opener at that line height. The marks above it belong to the preceding line. Root adopts A/C’s removal of the supplied pair against B’s retention; the closing pair after handle is kept.',cp(22),'high','text not on the page')
add('to-it','p154 line-6, final cancelled fragment',r'\deleted{\unsure{it}}',r'\deleted{\unsure{to|it}}',[r'\deleted{\unsure{to|it}}']*3,'A tall crossed stem and right-hand closed oval favour to. The heavy shared lower strokes still permit it. All readers and root widen/reorder the candidate without asserting certainty.',cp(23),'low')
add('last-quotes','p154 line-2, both quote groups',"``standard''",r"\unsure{``|`}standard\unsure{''|'}",[r"\unsure{``|`}standard\unsure{''|'}"]*3,'Each group is a joined upright/loop with no secure separation into two strokes. Both occurrences are marked independently, with paired forms favoured. The two separate doubt entries preserve their individual status.',cp(25))
for aid,bid,cid,crop in [('left-rule','left_rule','C022-15','crops/022/01_left_rule.jpg'),('right-rule','right_rule','C022-16','crops/022/02_right_rule.jpg'),('far-left-trace','faint_left_trace','C022-17',ap(24)),('upper-left-ring','pale_oval','C022-18',ap(23)),('lower-left-mark','lower_bent_mark',None,ap(25))]:
 x=ch['A'][aid]
 creading=cr(cid) if cid else r'\draw[thin] ([xshift=.67em,yshift=.1ex]s022bottom) -- ++(.21em,-.2ex) -- ++(-.06em,.3ex);'
 add(aid,x['place'],'',x['reading'],[x['reading'],br(bid),creading],'Root confirms the visible geometry on the listed crop. '+x['evidence']+' No textual value, editorial function or author identity is assigned to the mark.',crop,'high' if aid in ['left-rule','right-rule'] else 'medium','drawing or diagram')

cd=doubt_decisions(R['A'],22,'A')
for idx,reading,evidence in [(18,r'\deleted{does}','Root adopts B: separate d ascender/bowl, o loop, e turn and s curl survive.'),(20,r'\deleted{st}','Root adopts B/C: independent s curves and t stem/crossbar survive.'),(26,'work','Root adopts B at medium confidence: closed o and final k arm distinguish work from write.')]:
 cd[idx].update(reading=reading,resolved=True,confidence='medium',decision='Resolved: '+reading,evidence=evidence+' Crop: '+(cp(11) if idx==18 else cp(13) if idx==20 else cp(19)))
cd[28].update(reading=r'\deleted{\unsure{n \&|n \& s}}',decision='Retained and widened: old final curl may be part of ampersand or a further s; two raised strokes separately drawn.')
cd[29].update(reading=r'\unsure{\uline{s}|S|$s_1$|$S_1$}',decision='Retained and widened: case and low1 interpretation unresolved; descending stroke explicitly drawn.')
doubts=[copy.deepcopy(d) for i,d in enumerate(R['A']['remaining_doubts']) if i not in [10,11,16]]
for d in doubts:
 if d['place']=='p.153 cancelled short fragment':d.update(reading=r'\deleted{\unsure{n \&|n \& s}}',alternatives='n &; n & s; two raised strokes have uncertain textual attribution',reason='The old final curl could be part of the ampersand or another s; cancellation prevents segmentation. Raised strokes are drawn independently.')
 if d['place']=='p.153 final s-like sign':d.update(reading=r'\unsure{\uline{s}|S|$s_1$|$S_1$}',alternatives='underlined s with pen tail; S with pen tail; s_1; S_1',reason='A low hook joins a long downstroke; its identity and the body’s case remain uncertain. The actual stroke is drawn.')
for place,reading,alts,reason in [
 ('p.119 boxed addition, before not',r'\unsure{``}','opening pair; enclosure trace','The small trace merges with the enclosure; two independent quote strokes are not secure.'),
 ('147 line2, opening quote',r'\unsure{``|`}','fused double; single bent quote','A compact peak with joined legs does not securely separate the stroke count.'),
 ('147 line20, opening quote',r'\unsure{``|`}','fused double; single curved quote','The high cap-shaped mark has joined ends.'),
 ('Circled151, cancelled apostrophe',r"we\unsure{'}ll",'apostrophe; covered/absent independent mark','No separate apostrophe can be isolated above the crowded e-ll join.')]:
 doubts.append(dict(place=place,reading=reading,alternatives=alts,confidence='low' if 'apostrophe' in place or 'not' in place else 'medium',reason=reason))
inv={int(d['element']):copy.deepcopy(d) for d in R['A']['inventory']}
inv[7]['first_words_or_objects']='curving rightward arrow with additional angular head stroke'
inv[36]['first_words_or_objects']='does, cancelled; four letter bodies readable'
inv[39]['first_words_or_objects']='st, cancelled; surviving s and t contours'
inv[61]['first_words_or_objects']="we'll work, cancelled; apostrophe uncertain"
inv[65]['first_words_or_objects']='handiness cancelled; surrounding quote strokes remain live'
inv[67]['first_words_or_objects']='n & / n & s, cancelled and uncertain'
inv[81]['kind']='margin note'
order=[76,77,78,1,79]+list(range(2,76))+[80,81]
inventory=[inv[i] for i in order]
for i,d in enumerate(inventory,1):d['reader_element']='A'+d['element'];d['element']=f'{i:02}'
notes=copy.deepcopy(R['A']['notes'])
notes[5]='The p.153 correction cancels handiness while its quote strokes remain outside the crossing. The handy n & s/S-like wording is followed by would be better. The last sign has a low hook and long downstroke: a low1 is possible, with case and meaning unresolved. The stroke is reproduced without deriving a formula from the wordplay.'
notes.append('The one physical quote pair between the first two entries is kept low at its observed position, with attachment uncertain; no duplicate opener is supplied. The p154 will phrase has no visible opening pair, while its closer remains. Faint marginal traces and rules are reproduced without assigning editorial purpose or material origin.')
notation=copy.deepcopy(R['A']['notation'])
notation.append(dict(sign=r'\unsure{\uline{s}|S|$s_1$|$S_1$}',location='p.153 final sign, root adjudication',reading='Case and low1/underline interpretation remain uncertain; downstroke drawn',evidence='C crop21 shows a short low hook joined to a long vertical. The nearby s_1=delta_0 is not used to impose a subscript here.'))
write_record(22,'A','brief_v07.md',text,decisions,cd,doubts,notes,'All three finalized full readings, differences, C-context decisions and inventories were compared. Root inspected thirty existing reader crops and three new tight geometry crops. Each witness/reader disagreement has a root crop decision; repeated covered cancellations were considered together only where they occupied the same compact locus. Final81-row inventory follows physical order, with full-page rules first and nested elements next to their text. H has description only. No OCR, outside research or compilation was used; no substantive mathematical check is claimed for this correction-only sheet.',viewed=viewed,inventory=inventory,notation=notation)
print('Scan022:',sum(d['diff_c'] for d in decisions),'C changes;',len(decisions),'decision rows;',len(doubts),'doubt loci;',len(inventory),'inventory rows.')
