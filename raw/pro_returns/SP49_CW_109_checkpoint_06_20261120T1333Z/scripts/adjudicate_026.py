"""Root adjudication of scan026 from all three final returns and retained crops."""
from common import *
R=load_page(26); T={r:(W/f'readers/026/{r}/reading.tex').read_text() for r in 'ABC'}
CH={r:{x['id']:x for x in R[r]['changes']} for r in 'ABC'}
def ch(r,i): return CH[r][i]
def a(i): return ch('A',i)
def b(i): return ch('B',i)
def c(i): return ch('C',i)
def ap(i): return 'readers/026/A/crops/'+next((W/'readers/026/A/crops').glob(f'{i:02}_*.jpg')).name
def bp(i): return f'readers/026/B/crops/{i:02}.jpg'
def cp(i): return f'readers/026/C/crops/{i:02}.jpg'
text=T['A']; replacements=[]
def repl(old,new):
 global text
 assert old in text,old
 text=text.replace(old,new,1);replacements.append((old,new))
fleft=b('276-left-quote-state')['reading'];fright=b('276-right-quote-state-height')['reading']
repl(a('f-quotes-state')['reading'],fleft+'$f$'+fright)
ref=r'''l-1\tikz[baseline=(old8.base)]{\node[inner sep=0pt] (old8) {\deleted{\unsure{8}}};\node[anchor=base west,inner sep=0pt] at ([xshift=.1em,yshift=.3ex]old8.base west) {7};}'''
repl(r'l-\deleted{18}17',ref)
repl(r"with\deleted{\unsure{''}}...",r"with\deleted{\unsure{''|'}}...")
repl(r'structure\uuline{s}',c('287-three-underlines')['reading'])
repl(r'\deleted{\unsure{do}}',c('288-cancelled-letters')['reading'])
repl(r'\deleted{\unsure{l6}}',r'\deleted{l\unsure{6}}')
repl(r"\deleted{by} ``\deleted{as well}''",r"\deleted{by} \unsure{\deleted{``}|``}\deleted{as well}''")
repl(r"``too\deleted{\unsure{''}} in",r"``too\deleted{''} in")
repl(r"\unsure{``|'}were''",r"\raisebox{.8ex}{\unsure{``|'}}were''")
repl(r"l8 ``developed''",'l8 '+b('293-developed-point')['reading'])
repl(r"l.16 'developed'' l.17 ``doesn't''",r"l.16 'developed'' "+b('299-two-low-points')['reading'])
repl(r"with \deleted{\unsure{''}} finite",r"with \deleted{\unsure{''|'}} finite")
trace=c('faint-upper-left-trace')['reading'].replace('gray!55','gray!35')
repl('% upper-left stray strokes',trace+'\n% upper-left stray strokes')

D=[]
def add(i,place,old,final,abc,evidence,crops,confidence='medium',kind='other',diff=True):
 D.append(dict(id='026-'+i,place=place,c=old,h=None,final=final,readers=dict(zip('ABC',abc)),evidence=evidence,crops=crops if isinstance(crops,list) else [crops],confidence=confidence,kind=kind,diff_c=diff,diff_h=False,marked_in_H=False))
def pick(r,i,abc,evidence,crops,confidence=None):
 x=ch(r,i);add(i,x['place'],x['c'],x['reading'],abc,evidence,crops,confidence or x['confidence'],x.get('kind','other'))
pick('A','top-equals-height',[a('top-equals-height')['reading'],b('top-equals-height')['reading'],c('top-equal-height')['reading']],
 'Two distinct horizontal strokes are raised above the crossed right-pointing relation. Root preserves their position; the earlier single/double shaft doubt remains. Insertion brackets in C reader are an encoding choice, not additional ink.',ap(1),'high')
add('f-left','276 l.15, left quote cluster',r'\unsure{``}',fleft,[a('f-quotes-state')['reading'],fleft,c('276-left-quote-state')['reading']],
 'Root confirms crossing returns through the high upright remnants. The cluster is cancelled; double versus single original quotation count remains uncertain, independently of the right group.',ap(2),'medium','deletion state (struck given live or live given struck)')
add('f-right','276 l.15, right quote cluster and low caret',r"\inserted{\unsure{''}}",fright,[a('f-quotes-state')['reading'],fright,c('276-right-quote-and-caret')['reading']],
 'The raised cluster is crossed and stands over a separate low two-legged caret. Root keeps the insertion encoding, cancellation and explicit height/caret; original quote count remains double/single. The caret does not supply an intact live quote.',ap(2),'medium','insertion or placement')
add('278-reference','278 first reference',r'l-\deleted{\unsure{18}}\unsure{17|14}',ref,[a('278-reference')['reading'],b('278-corrected-reference')['reading'],r'l-\deleted{\unsure{18}}17'],
 'One physical leading1 stands beside the overlaid final digits. Root represents that1 once. The new digit has a top bar, falling diagonal and cross-stroke, reading7; the older lower loop favors8 but its upper portion is buried. The old digit remains doubtful, against A/B resolution. Overlapping glyphs reproduce the correction instead of printing18 and17 successively.',ap(3),'medium','insertion or placement')
pick('A','definitely-opener',[a('definitely-opener')['reading'],b('278-definitely-opener')['reading'],c('278-definitely-opener')['reading']],
 'Two short lower legs meet in a compact apex; root favors a joined double opener but cannot exclude one bent stroke. The uncertainty is retained against B/C certainty.',ap(4),'low')
pick('A','wed-opener',[a('wed-opener')['reading'],b('278-wed-opener')['reading'],c('278-wed-opener')['reading']],
 'The high opener has two lobes and a shallow central return. Root agrees with the three readers on a joined double pair, at medium rather than high confidence. The internal apostrophe is separate.',ap(5),'medium')
pick('A','wasnt-opener',[a('wasnt-opener')['reading'],b('280-wasnt-opener')['reading'],c('280-wasnt-opener')['reading']],
 'A long left curl and separate higher short right stroke establish two components. Root confirms the double opener, correcting the earlier provisional root note written before this crop was actually displayed.',ap(6),'high')
pick('A','283-doesnt-opener',[a('283-doesnt-opener')['reading'],"``doesn't''","``doesn't''"],
 'The high fork is continuous, with a short branch from one dark upright. Root retains the independent double/single count uncertainty rather than assuming the repeated quotation pattern.',ap(8),'low')
pick('B','284-cancelled-quote-count',[r"\deleted{\unsure{''}}",b('284-cancelled-quote-count')['reading'],r"\deleted{\unsure{''}}"],
 'The crossed main body and detached high point do not disclose the original count. Root explicitly retains both double and single candidates; cancellation is clearer than identity.',ap(9),'low')
pick('C','287-three-underlines',[r'structure\uuline{s}',b('287-three-underlines')['reading'],c('287-three-underlines')['reading']],
 'Root sees a top horizontal, a dense middle returned level, and a separate lower curved stroke. The final draws all three levels locally beneath s. This preserves the retraced geometry without relying on nested underline macros.',ap(10),'high')
pick('C','288-cancelled-letters',[r'\deleted{\unsure{do}}',r'\deleted{\unsure{do}}',c('288-cancelled-letters')['reading']],
 'The d bowl and ascender are independently recognizable; the following small rounded body is obscured. Root narrows the uncertainty to o/e, following C reader; no grammar is used to choose the second letter.',ap(11),'medium')
pick('A','289-to-opener',[a('289-to-opener')['reading'],"``to''","``to''"],
 'The opening group is one angular dark body with connected upper/lower arms. Root retains double/single uncertainty for this occurrence; the closer has two separate strokes.',ap(12),'low')
pick('A','291-pro',[r'\deleted{pro}']*3,
 'The descending p, low r shoulder and closed final o survive independently under the crossing. Root resolves the letters at medium confidence, without deriving them from the following property.',ap(14),'medium')
D[-1]['kind']='misread word'
pick('B','293-developed-point',["``developed''",b('293-developed-point')['reading'],"``developed''"],
 'Root confirms a compact pale oval below-left of the closing pair, after the final d. It is drawn once in gray without assigning punctuation or material origin.',bp(16),'medium')
add('293-old-ref-comma','p293 l-4, cancelled small reference and following comma',r'\deleted{\unsure{l6},',r'\deleted{l\unsure{6}},',
 [a('293-reference-comma')['reading'],r'\deleted{\unsure{l6}, Replace}',c('293-reference-and-comma')['reading']],
 'The tall loop supports l; the small lower loop favors6 but remains crossed. The detached comma is below-right, outside the reference cancellation and before the long crossing begins. Root narrows the letter doubt and keeps the comma live.',ap(16),'medium','deletion state (struck given live or live given struck)')
add('293-too-edges','p293 cancelled proposal, quotes around too',r"\deleted{``too''}",r"``\deleted{too}\unsure{\deleted{''}|''}",
 [a('293-too-quote-edges')['reading'],b('293-too-opening-live')['reading']+'; '+b('293-too-closing-state')['reading'],r"\deleted{``too''}"],
 'The opening pair is above the crossing with white separation. At the closer, one component meets a zigzag peak and the other stands higher; root agrees with A/B that its state remains uncertain. Word cancellation is secure.',[ap(17),bp(18)],'low','deletion state (struck given live or live given struck)')
add('293-aswell-edges','p293 cancelled proposal, quotes around as well',r"\deleted{``as well''}",r"\unsure{\deleted{``}|``}\deleted{as well}''",
 [a('293-aswell-quote-edges')['reading'],b('293-aswell-opening-state')['reading']+'; '+b('293-aswell-closing-live')['reading'],r"\deleted{``as well''}"],
 'The opening pair touches the rising tooth of the cancellation; root retains B’s state uncertainty, rather than A’s certain live or C’s certain cancelled reading. The closing pair stands independently above the stroke and remains live.',[ap(17),bp(18),cp(15)],'low','deletion state (struck given live or live given struck)')
pick('A','293-final-words',[r'\unsure{easier reading}']*3,
 'Two groups survive: low e/a/s-like turns in the first, and a d-like rise, i point and descending g in the second. Root narrows to easier reading; buried internal joins prevent an unqualified reading. The other C alternatives have no positive surviving support.',cp(15),'medium')
pick('A','293-final-period',['.']*3,
 'The low detached point is beyond the final return and endpoint of the cancellation. Root keeps it live, separately from the crossed final words.',cp(15),'high')
add('293-too-quote-resolved','p293 live continuation after too',r"\deleted{\unsure{''}}",r"\deleted{''}",
 [r"\deleted{\unsure{''}}",r"\deleted{''}",r"\deleted{''}"],
 'The tighter existing B crop shows two separate upper heads over a crossing return. Root follows B/C and resolves a cancelled double closer at medium confidence; the live word too is not struck.',[ap(18),bp(20)],'medium','misread symbol or index')
add('295-were-opener','295 before were',"``were''",r"\raisebox{.8ex}{\unsure{``|'}}were''",[a('295-were-opener')['reading'],b('295-were-opening-count')['reading'],c('295-were-opener')['reading']],
 'One compact lobed high group stands above-left of were. Root agrees on double/single uncertainty and preserves its unusually high placement. It is this opener, not a second unrelated point; the physical group is represented only once.',ap(19),'low','insertion or placement')
pick('A','296-functor-closer',[a('296-functor-closer')['reading'],"functor''","functor''"],
 'A left upright and high right hook meet in one group. Root cannot distinguish a fused double closer from one returned stroke, and retains A’s independent count doubt.',ap(21),'low')
pick('B','299-two-low-points',["l.17 ``doesn't''",b('299-two-low-points')['reading'],"l.17 ``doesn't''"],
 'Root confirms two distinct dark points below the terminal t, the lower one farther left. They are drawn before the right rule without supplying a grammatical role.',bp(24),'high')
pick('B','302-cancelled-quote-count',[r"\deleted{\unsure{''}}",b('302-cancelled-quote-count')['reading'],r"\deleted{\unsure{''}}"],
 'The high blackened body has a small white hole but no secure original stroke count. Root explicitly retains double/single alternatives; cancellation remains certain.',ap(23),'low')
for i,n in [('left-rule',1),('right-rule',2)]:
 pick('A',i,[a(i)['reading'],b(i)['reading'],c(i)['reading']],
 'Root full-length narrow crop confirms the slightly irregular near-vertical course and its endpoints. '+('The short existing gap crop shows faint continuity at the thin intervals. ' if n==2 else '')+'The rule stays in the common text layout, not in a detached panel.',f'crops/026/0{n}_'+('left' if n==1 else 'right')+'_rule.jpg','high')
add('faint-left-trace','Far-left upper portion','',trace,['omitted',b('faint-left-trace')['reading'],c('faint-upper-left-trace')['reading']],
 'The existing C middle crop confirms the gray irregular trace. A new narrow extent crop, needed because no reader crop included its endpoints, shows it fading around the middle of the sheet, not continuing to301 as B drew it. Root follows C’s upper-half extent. Its physical origin is not assigned.',[cp(21),'crops/026/03_left_trace_extent.jpg'],'medium','drawing or diagram')
pick('A','upper-left-strokes',[a('upper-left-strokes')['reading'],'omitted','omitted'],
 'Root confirms two short darker oblique cores with faint connecting gray trails at the upper-left location. They are drawn geometrically without attributing a hand or textual purpose.',ap(24),'medium')

cd=doubt_decisions(R['C'],26,'C')
for i in [1,2,3,4,5,6,8,9,10,11,12,16]:
 cd[i]['evidence']='Root adjudication supersedes the preliminary reader wording. '+cd[i]['evidence']
cd[1]['reading']=fleft;cd[2]['reading']=fright
cd[3].update(reading=r'1\deleted{\unsure{8}}',resolved=False,decision='One shared leading1; old final8 remains uncertain beneath the new7.',evidence='Root A03: only one independent leading1; lower old loop survives but upper loop is buried.')
cd[4].update(reading=ref,resolved=True,decision='Replacement final7 resolved; leading1 shared once with the old reference.',evidence='Root A03: upper bar, falling diagonal and cross-stroke, without separate right stem for4.')
cd[5]['reading']=r"\deleted{\unsure{''|'}}"
cd[16]['reading']=r"\deleted{\unsure{''|'}}"
for x in cd:
 x['decision']=('Resolved/confirmed: ' if x.get('resolved') else 'Retained/narrowed: ')+x['reading']
doubts=[]
def doubt(place,reading,alts,reason,confidence='low'):
 doubts.append(dict(place=place,reading=reading,alternatives=alts,confidence=confidence,reason=reason))
doubt('Opening l.18',r'\deleted{\unsure{\Rightarrow|\to}}','double or single right arrow','Cancellation may account for an apparent second shaft.')
doubt('276 left of f',fleft,'double or single opening quotation','Crossing returns obscure original count.')
doubt('276 right of f',r"\inserted{\deleted{\unsure{''|'}}}",'double or single closing quotation','Raised crossed group above a separate low caret.')
doubt('278 old final numeral',r'\deleted{\unsure{8}}','8 favored','Upper old loop buried by the new7; the leading1 is represented once.')
doubt('278 before definitely',r"\unsure{``|'}",'double or single opener','Two legs join in one compact apex.')
doubt('283 before doesnt',r"\unsure{``|'}",'double or single opener','A short branch joins a single dark upright.')
doubt('284 cancelled closer',r"\deleted{\unsure{''|'}}",'double or single closer','The crossing masks the original group.')
doubt('288 false start',r'\deleted{d\unsure{o|e}}','do; de','The d is readable, but the next rounded body is crossed.','medium')
doubt('289 before to',r"\unsure{``|'}",'double or single opener','Upper and lower arms form one connected angular body.')
doubt('293 old reference',r'\deleted{l\unsure{6}}','l6 favored','The l loop is readable; the small following loop is partly buried.')
doubt('293 cancelled proposal, too closer',r"\unsure{\deleted{''}|''}",'cancelled or live double closer','One component meets a cancellation tooth while the other is higher.')
doubt('293 cancelled proposal, as well opener',r'\unsure{\deleted{``}|``}','cancelled or live double opener','The high group touches the rising cancellation stroke.')
doubt('293 cancelled final phrase',r'\unsure{easier reading}','easier reading favored; other C candidates rejected','Two word groups and surviving heights fit this reading, but internal joins remain hidden.','medium')
doubt('295 before were',r"\raisebox{.8ex}{\unsure{``|'}}",'double or single opener','A compact raised lobed group has no securely separable stroke count.')
doubt('296 after functor',r"\unsure{''|'}",'double or single closer','One upright and a joined upper hook could be one returned or two fused strokes.')
doubt('302 cancelled closer',r"\deleted{\unsure{''|'}}",'double or single closer','Dense overwritten body does not reveal the original count.')

inv=copy.deepcopy(R['A']['inventory'])
for x in inv:
 for old,new in replacements:x['first_words_or_objects']=x['first_words_or_objects'].replace(old,new)
inv[40]['first_words_or_objects']=fleft
inv[41]['first_words_or_objects']=fright
inv[42]['first_words_or_objects']=r"\deleted{\unsure{''|'}}"
inv[44]['first_words_or_objects']=r'\deleted{\unsure{8}}, after one shared live1'
inv[45]['first_words_or_objects']=r"\deleted{\unsure{''|'}}"
inv[46].update(kind='drawing',first_words_or_objects='Three returned underline levels below terminal s')
inv[54]['first_words_or_objects']=r'\unsure{\deleted{``}|``}'
inv[57]['first_words_or_objects']=r"\deleted{''}"
inv[58]['first_words_or_objects']=r"\deleted{\unsure{''|'}}"
extras=[('drawing','far-left upper half','Faint irregular gray trace; origin unassigned'),('insertion','278 first reference','Live7 over old uncertain8; shared1 written once'),('drawing','293 l8 after developed','Pale oval point below closing quote group; function unassigned'),('drawing','299 l17 under terminal t','Two distinct dark points left of right rule'),('text','archive corner number','25, preserved only as a TeX comment')]
for k,p,w in extras:inv.append(dict(sheet_kind='list',hand='hand or material origin not established' if k=='drawing' else inv[0]['hand'],element='added',kind=k,position=p,first_words_or_objects=w,transcribed='yes'))
def ikey(x):
 p=x['position'];m=re.search(r'y=(\d+)',p)
 if m:return int(m[1]),0
 if 'archive' in p:return 2400,0
 if 'nearly full' in p or 'right side' in p:return 70,0
 if 'far-left' in p:return 90,0
 if 'upper-left' in p:return 120,0
 if 'opening' in p or 'Opening' in p:return 100,1
 if 'f' in p and ('quote' in p or 'group' in p):return 165,1
 for ref,y in [(276,165),(278,300),(284,738),(287,930),(288,993),(291,1246),(293,1436),(295,1694),(296,1820),(299,2013),(302,2270)]:
  if str(ref) in p:return y,1
 return 165,1
inv=sorted(inv,key=ikey)
for i,x in enumerate(inv,1):x['element']=f'{i:02}'
notes=copy.deepcopy(R['C']['notes'])
notes.append('The opening formulation is retained literally: is C=A? confusing as it stands., with equals raised over the crossed earlier sign. At278 the note says i.e we had better assume. At288 it says has no verb. I suggest; at293, feels awkward. What about; at296, analogues would work. These are the writer’s qualifications and proposals, not independently validated corrections.')
notes.append('Scope: no definitions for C and A are supplied, and the M-prime phrase is abbreviated by dots. Neither the equality nor the alleged absent verb in the unseen full sentence can be established from this sheet. Repeated commute-with suggestions and the dictionary claim are recorded without outside lookup or proof claims. No mathematical check event is counted.')
notes.append('The overwritten278 reference has one leading1 and a new7 over an uncertain old8. Fused quotation counts and the deletion states at two edges of the cancelled293 proposal remain marked individually. Both long black rules, the shorter faint far-left trace, upper-left strokes, pale point after developed and two low points near299 are reproduced without assigning the faint or isolated marks a purpose. The separate archive number25 is recorded only in a comment; no own manuscript pagination is supplied.')
notation=[dict(sign='raised equality over old arrow',location='opening l.18',reading=a('top-equals-height')['reading'],evidence='A01: two live high horizontals; old shaft count remains uncertain.'),dict(sign='shared reference numeral',location='278 first reference',reading=ref,evidence='A03: one leading1 and overlapping final digits; new7 clear, old8 uncertain.'),dict(sign='triple returned underline',location='287 terminal s',reading=c('287-three-underlines')['reading'],evidence='A10: top horizontal, dense middle return and distinct lower curve; geometry retained.'),dict(sign='ordinary capitals and prime',location='opening;288',reading=r'C, A, M\prime',evidence='All three halves readings confirm ordinary capitals and one separate high prime on M.'),dict(sign='quotation count and cancellation state',location='276,278,280,283,284,289,293,295,296,302',reading='Independent local decisions; singles retained, explicit double/single alternatives where fused; p293 quote-edge deletion states separately uncertain.',evidence='Root retained crops listed in changes; no pattern-based propagation.'),dict(sign='cancelled false starts',location='288;291;293',reading=r'\deleted{d\unsure{o|e}}; \deleted{pro}; \deleted{l\unsure{6}}',evidence='A11/A14/A16: surviving ascenders, loops and shoulders decide only the marked portions.'),dict(sign='1.1',location='297 line reference',reading='1.1',evidence='All three independently confirm the low intermediate point in half b.'),dict(sign='isolated faint/dark marks',location='293 developed;299;outer margins',reading='Drawn geometrically at observed positions; physical origin and punctuation function not assigned.',evidence='B16/B24/A24/C21 and root extent crop03.')]
viewed=json.loads((W/'records/root_026_viewed.json').read_text())
coverage='All three final full readings and reports were compared, including literal differences, all12 explicit C uncertainties and5 context decisions. Every reader/witness disagreement was adjudicated on a retained crop. Root reused31 distinct reader crops and made3 narrow extent crops (two black rules and the previously uncropped disputed endpoints of the faint trace); re-displays and one rotation of an existing crop are not new crops. Whole and half images stayed with the three independent readers. The full inventory has64 elements, including35 physical text lines, nested corrections, graphics and archive comment. Sixteen textual/state doubts remain. H is descriptive only; no H comparison rows or mathematical check events are claimed. No OCR, outside research or compilation.'
rec=write_record(26,'A','brief_v11.md',text,D,cd,doubts,notes,coverage,viewed=viewed,events=[],inventory=inv,notation=notation)
print('scan026:',len(D),'decisions;',sum(d['diff_c'] for d in D),'C changes;',len(doubts),'doubts;',len(inv),'inventory;',rec['crop_counts'])
