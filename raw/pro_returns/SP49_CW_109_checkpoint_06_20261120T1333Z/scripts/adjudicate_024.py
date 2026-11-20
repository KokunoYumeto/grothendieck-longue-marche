"""Main-reader decisions for scan024, after the three independent final returns."""
from common import *
R=load_page(24)
T={r:(W/f'readers/024/{r}/reading.tex').read_text() for r in 'ABC'}
ch={r:{x['id']:x for x in R[r]['changes']} for r in 'ABC'}
Q=chr(96)*2
text=T['B']
def repl(a,b):
 global text
 assert a in text,a
 text=text.replace(a,b,1)
def ap(n):return f'readers/024/A/crops/{n:02}.jpg'
def bp(n):return f'readers/024/B/crops/{n:02}.jpg'
def cp(name):return 'readers/024/C/crops/'+name+'.jpg'
def a(id):return ch['A'][id]
def b(id):return ch['B'][id]
def c(id):return ch['C'][id]

repl('l.-9 '+Q+'Riemannian', 'l.-9 '+a('mark-after-nine')['reading']+' '+Q+'Riemannian')
repl(r'\deleted{\unsure{'+Q+'for}}',c('193-cancelled-for')['reading'])
repl(r'p\unsure{196|191}',r'p\unsure{191|196}')
repl(Q+"it is''",r"\unsure{'|``}it is''")
# Preserve the upper streak and low point once each; a dotless i avoids adding
# a second dot at a position not present in this small group.
is_marks=r'\i s\tikz[baseline=0pt,x=0.08cm,y=0.08cm]{\draw[line width=0.4pt] (0,2.3)--(1.8,1.8);\fill (1,0) circle (0.22);} a'
repl('is. a',is_marks)
repl(r'l.20\deleted{\unsure{?}}',r'l.20\deleted{\unsure{7|?}}')
repl(r'\unsure{*|``}',r'\unsure{*|\deleted{``}|``}')
repl("do you mean 'that",r"do you mean \unsure{!|'}that")
repl('c.f p.32','c.f. p.32')

# Anchor the long rules around the reference column and writing, rather than
# placing a disconnected full-height geometry panel before the text.
start=text.index('% Two full-height ink rules')
end=text.index('p.\\unsure{191}',start)
text=text[:start]+r'''\begingroup
\setlength{\parindent}{0pt}
\tikz[remember picture,overlay]{\coordinate (scan24-rule-top) at (0,0);}

'''+text[end:]
refs=[r'p.\unsure{191}','192','193.','194',r'p\unsure{191|196}','198','200','201','202','203','204','205','206','207','208','209','210','213','p216','p217','p.219','221',r'\deleted{\unsure{1|2}}224']
for ref in refs:
 needle=ref+' '
 if ref=='194':needle=' 194 '
 assert needle in text,ref
 prefix=r'\hangindent=1.2cm\hangafter=1 \makebox[1.2cm][l]{'+ref+'}'
 text=text.replace(needle,(' '+prefix if ref=='194' else prefix),1)
# Indent continuation paragraphs to the writing column, without changing words.
for marker in ['l.-9 '+a('mark-after-nine')['reading'],'l.-19 '+Q,'l-8 '+Q,'l17 '+Q,'l-9 '+Q,'line -10 \\& -9:','l.17 '+Q]:
 repl('\n\n'+marker,'\n\n'+r'\hangindent=1.2cm\hangafter=1 \hspace*{1.2cm}'+marker)
repl(r'\makebox[1.2cm][l]{198}',r'\tikz[remember picture,overlay]{\coordinate (scan24-faint-top) at (0,0);}\makebox[1.2cm][l]{198}')
text+=r'''
% The left rule separates references from writing. The right rule intersects
% long entries. The faint outer trace is recorded without assigning an origin.
\tikz[remember picture,overlay]{\coordinate (scan24-rule-bottom) at (0,0);}
\figure{\begin{tikzpicture}[remember picture,overlay]
  \coordinate (scan24-bottom-left) at (scan24-rule-top |- scan24-rule-bottom);
  \draw[line width=0.3pt] ([xshift=1.08cm,yshift=1.6ex]scan24-rule-top)
    -- ([xshift=1.07cm,yshift=-1ex]scan24-bottom-left);
  \draw[line width=0.3pt] ([xshift=.93\linewidth,yshift=1.6ex]scan24-rule-top)
    -- ([xshift=.927\linewidth,yshift=-1ex]scan24-bottom-left);
  \draw[gray,line width=0.18pt] ([xshift=1.06\linewidth]scan24-faint-top)
    -- ([xshift=1.062\linewidth]scan24-bottom-left);
\end{tikzpicture}}
\endgroup
'''

viewed=json.loads((W/'records/root_024_viewed.json').read_text())
viewed+=['crops/024/01_left_rule.jpg','crops/024/02_right_rule.jpg','crops/024/03_point_usual.jpg']
(W/'records/root_024_viewed.json').write_text(json.dumps(viewed,indent=2))
decisions=[]
def add(id,place,old,final,abc,evidence,crops,confidence='medium',kind='other',diff=True,consequential=None):
 d=dict(id='024-'+id,place=place,c=old,h=None,final=final,readers=dict(zip('ABC',abc)),evidence=evidence,crops=crops if isinstance(crops,list) else [crops],confidence=confidence,kind=kind,diff_c=diff,diff_h=False,marked_in_H=False)
 if consequential:d['consequential']=consequential
 decisions.append(d)
for n,id,cid in [(1,'left-rule','rules-left'),(2,'right-rule','rules-right')]:
 x=b(id)
 add(id,x['place'],'',x['reading'],[a(id)['reading'],x['reading'],c(cid)['reading']],'The root narrow crop confirms a continuous near-vertical rule. '+x['evidence']+' Final TikZ anchors its course to the text block and reference column, retaining the physical relationship rather than a separate geometry panel.',f'crops/024/0{n}_'+('left' if n==1 else 'right')+'_rule.jpg','high','drawing or diagram')
x=b('faint-right-trace')
add('faint-right-trace',x['place'],'',x['reading'],['omitted',x['reading'],'omitted'],'Root confirms the faint intermittent narrow trace in B28. The long extent is recorded by B from the halves; the crop establishes the local geometry, not its origin or editorial function. For inspection only, the existing crop was rotated90 degrees without recropping, resizing or further enhancement; the derivative and log are retained.',bp(28),'medium','drawing or diagram')
x=a('mark-after-nine')
add('after-nine',x['place'],'',x['reading'],[x['reading'],'omitted','omitted'],'Root confirms the short detached oblique dark stroke, surrounded by pale copy haze, after9 and below the quotation-height pair. It is reproduced without naming a punctuation function.',ap(2),'medium','drawing or diagram')
x=c('193-cancelled-for')
add('for-and-opener',x['place'],x['c'],x['reading'],[a('cancelled-for')['reading'],x['c'],x['reading']],'Root resolves the old word as for: a tall looped f, small oval join and rightward r shoulder survive the crossings. The separate high quote cluster is thick and traversed by joined strokes; its cancellation state is not securely separable. The final resolves the letters while preserving the live/cancelled uncertainty of the opener.',ap(3),'medium','deletion state (struck given live or live given struck)')
x=b('left-margin-194')
add('left-margin',x['place'],x['c'],x['reading'],[a('left-note-placement')['reading'],x['reading'],c('194-left-margin')['reading']],'The cancelled word lies outside the left rule and is clipped at the sheet edge. Root confirms the left-side placement; the buried stating/starting alternatives remain unchanged.',ap(4),'high','insertion or placement')
x=b('points-194')
add('reference-points',x['place'],x['c'],x['reading'],['l-11',x['reading'],'l-11'],'Root confirms two detached dark points, one left of the l and one inside its tall loop. Neither is a stop after l. Their observed positions are drawn without interpreting their purpose.',bp(5),'medium','drawing or diagram')
x=c('196-reference')
add('p191-196',x['place'],x['c'],x['reading'],[a('page-number-order')['reading'],x['c'],x['reading']],'The last numeral has a surviving narrow descending stem without a securely closed lower bowl. Root favours191, as A/C, but retains196 because the low ink is washed out. The subsequent p197 insertion does not determine the faded digit.',ap(5),'medium')
x=b('apperent')
add('apperent',x['place'],x['c'],x['reading'],[x['reading']]*3,'The first vowel after the paired p descenders has the small open e-like loop and exit; another e follows r. All three and root read the literal apperent. No spelling correction is made.',ap(6),'high','misread word')
x=c('200-its-opener')
add('its-opening-retained',x['place'],x['c'],x['c'],[x['c'],x['c'],x['reading']],'Root retains the single opening stroke: the long oblique body has one continuous taper, unlike the two separately formed closing strokes. Its small lower notch does not establish a second quote. C’s proposed new uncertainty is not adopted.',ap(7),'medium',diff=False)
x=b('it-is-opener');new=r"\unsure{'|``}it is''"
add('it-is-opening',x['place'],x['c'],new,[x['c'],x['reading'],x['c']],'The high opener has an angular fork, one thick ascending limb and a short descending limb. A single bent quote is favoured, but a joined pair cannot be separated securely. Root therefore marks both readings rather than adopting B’s certain double opener or A/C’s certain single opener.',ap(8),'medium')
old=r'is\unsure{.} a'
add('is-marks','205, between is and a',old,is_marks,['is. a','is. a',c('205-is-mark')['reading']],'The low dark point is certain, with a separate short oblique streak above it. Root preserves both geometrically, without deciding whether the upper stroke is a displaced i-dot or an independent mark. Dotless i in the underlying word prevents reproducing that same possible dot twice. The word remains is; no grammar correction is made.',ap(9),'high','drawing or diagram')
old=r'\deleted{\unsure{?}}';new=r'\deleted{\unsure{7|?}}'
add('206-old-sign','206 after l.20',old,new,[a('206-cancelled-remnant')['reading'],old,c('206-old-sign')['reading']],'The crossed small remnant has a compact upper bar and downward stem. Root favours7; a question-like hook remains possible, without a detached dot. C’s9 alternative lacks a separately recoverable closed head, so the final retains7/question only. Its cancelled state is clear.',ap(10),'low')
x=b('point-207')
add('point-207',x['place'],'',x['reading'],[a('207-isolated-point')['reading'],x['reading'],c('207-isolated-point')['reading']],'The root crop shows a compact dark oblique point in otherwise blank space, to the right of the continuation and above its baseline. It is retained once, without attaching it to the sentence as punctuation.','crops/024/03_point_usual.jpg','high','drawing or diagram')
x=b('l7')
add('l7',x['place'],x['c'],x['reading'],[x['reading']]*3,'The curved/wavy stroke joins the top of the crossed7. There is no independent horizontal minus between the stop after l and7. All three readers and root resolve the reference as l.7.',ap(13),'high')
x=b('before-I');new=r'\unsure{*|\deleted{``}|``}'
add('before-I',x['place'],x['c'],new,[a('210-raised-mark')['reading'],x['reading'],c('210-opening-mark')['reading']],'A small central opening is surrounded by short projecting and crossed strokes. A star-like mark is favoured. A modified quotation group is also possible, and its apparent crossing may either be cancellation or part of the joined glyph. Root explicitly preserves that state uncertainty.',ap(14),'low')
x=b('right-marks-210')
add('right-marks',x['place'],'',x['reading'],[a('210-right-marks')['reading'],x['reading'],c('210-right-strokes')['reading']],'Root confirms two short separate oblique marks outside the right rule, with the right mark lower. Their approximate relative geometry is drawn; no function is assigned.',ap(15),'high','drawing or diagram')
old=b('216-opening-state')['c'];new=r'\deleted{line -10} '+Q+r"\deleted{that if the}\unsure{?'|''|?''} \deleted{(the repeated line -9)}"
add('216-edges','216 cancelled first entry',old,new,[a('216-cancellation-edges')['reading'],new,c('216-cancellation')['reading']],'The long cancellation crosses line-10, the three words and the parenthetic reference, but passes below both raised edge groups. The opening pair remains live. At the other edge a curved left component plus a right stroke favour question-mark/single-closer, while a double closer or joined question/double closer remain possible. Root adopts B’s ordering and preserves both edge groups outside deletion.',ap(16),'medium','deletion state (struck given live or live given struck)')
x=c('216-live-opening')
add('216-live-opener',x['place'],x['c'],x['reading'],[x['c'],x['c'],x['reading']],'The crop has a long upper body with a detached lower dark point, nearly vertically aligned, separate from the descender of the preceding line. Root follows C’s exclamation/single-quote uncertainty: the geometry favours!, but an opening stroke with a lower ink deposit remains possible. The grammar is not used to choose.',[cp('18-functor-opener'),ap(16)],'low')
x=b('219-t')
add('219-t',x['place'],x['c'],x['reading'],[x['c'],x['reading'],Q+c('219-its')['reading']+"''"],'Root follows B/C: the t has one continuous heavy stem, one crossbar and a closed retraced foot joining s. No independent earlier letter or cancelling stroke is identifiable. The conjectural deleted t is removed; the live its and both quotation pairs remain.',ap(18),'medium','text not on the page')
x=a('cf-point')
add('cf-stop',x['place'],x['c'],x['reading'],[x['reading'],x['c'],x['c']],'A dark low point sits immediately below/right of the f, before the next reference. It is distinct from the f stem and from the later i-dots in description below. Root adopts A’s final abbreviation stop at medium confidence.',ap(20),'medium','omission')
old=r'\unsure{j|J}_A'
add('first-j-retained','224 first functor occurrence',old,old,[a('first-j')['reading'],old,old],'The angular entry and long bottom hook have no separate dot or secure case distinction. Root retains C/B’s j/J uncertainty against A’s proposed resolution. Neither the variance check nor the later occurrences determine this glyph.',ap(20),'medium',diff=False)
x=b('low-arrow-stroke')
add('arrow-tick',x['place'],'',x['reading'],[a('stroke-under-arrow')['reading'],x['reading'],c('224-arrow-low-stroke')['reading']],'Root confirms the short detached near-vertical tick below the left portion of the first right arrow. The arrow itself has a clear right head and no source bar. The lower tick is drawn separately, without giving it an arrow-label function.',ap(20),'high','drawing or diagram')
x=b('second-j-case')
add('second-j',x['place'],x['c'],x['reading'],[x['c'],x['reading'],x['reading']],'This second angular hook was read independently. Its upper entry and long lower return do not secure case; root follows B/C and marks j/J here too.',ap(21),'medium','misread symbol or index',consequential='The second functor occurrence acquires an independent j/J uncertainty; the ink does not establish lowercase despite the same formula context.')
x=b('argument-X')
add('live-X',x['place'],x['c'],x['reading'],[x['reading']]*3,'Two strong oblique strokes cross to form the live X. The earlier upright and two rounded right bowls are separately visible underneath as B. Root resolves the live letter from those diagonals, with medium confidence because the overlap is heavy.',ap(21),'medium','misread symbol or index',consequential='The first overwritten functor argument is resolved as live X over cancelled B, from the crossing diagonals rather than the expected formula.')
x=b('point-before-so')
add('point-before-so',x['place'],'',x['reading'],[a('224-low-point')['reading'],x['reading'],c('224-question-point')['reading']],'The point is below-left of so and above-left of the following quotation group. Root confirms it is separate from that group and preserves it once as geometry.',ap(23),'high','drawing or diagram')
x=b('jb-case')
add('lower-j',x['place'],x['c'],x['reading'],[x['c'],x['reading'],x['reading']],'The small lower occurrence independently has an angular top and hooked descender without a distinct dot. Root retains B/C’s j/J uncertainty. The low two-bowled B subscript is clear; the nearby inserted numerator is a different unresolved locus.',ap(23),'medium','misread symbol or index',consequential='The question-line functor also acquires its own j/J uncertainty; this does not change or settle the separate B/A numerator.')
x=b('twice-colon')
add('twice-colon',x['place'],x['c'],x['reading'],[x['reading']]*3,'Root confirms two vertically separated dark points after twice, hence a colon. The separate earlier stop after20 remains present as in C.',ap(24),'high','omission')

cd=doubt_decisions(R['B'],24,'B')
updates={1:(c('193-cancelled-for')['reading'],False,'Word for resolved; the separate opening pair remains doubtful between live and cancelled.'),3:(r'\unsure{191|196}',False,'Narrow final stem favours191; faded196 remains possible.'),5:(is_marks,True,'Low point and upper streak are certain geometry; their function is not assigned.'),6:(r'\deleted{\unsure{7|?}}',False,'Crossed upper bar/stem favours7, question remains possible; no secure9 head.'),8:(r'\unsure{*|\deleted{``}|``}',False,'Star-like or joined quote cluster; quote cancellation state also unresolved.'),12:(r'\deleted{B}X',True,'Crossing diagonals resolve the live X; root confidence medium because of overlap.')}
for i,(reading,resolved,evidence) in updates.items():
 cd[i].update(reading=reading,resolved=resolved,decision=('Resolved: ' if resolved else 'Retained: ')+evidence,evidence=evidence+' Main-reader crop decisions above supersede the original reader proposal.')
cd[12]['confidence']='medium'
cd[28]['reading']=cd[28]['reading'].replace('is. a',is_marks)
cd[28]['evidence']+=' Root records both upper streak and low point geometrically, with a dotless underlying i to avoid duplication.'
cd[33]['reading']=cd[33]['reading'].replace("mean 'that",r"mean \unsure{!|'}that")
cd[33].update(resolved=False,decision='Live wording confirmed; opener remains !/single-quote uncertain.',evidence='C crop18 and A crop16 establish the independent high body and low point. The dash after functor remains single; A crop17 confirms the higher stroke at i-dot height belongs to the following word.')
doubts=copy.deepcopy(R['B']['remaining_doubts'])
doubts[1]=copy.deepcopy(R['C']['remaining_doubts'][1])
doubts[3]=copy.deepcopy(R['C']['remaining_doubts'][3])
doubts[4].update(reading=r'\deleted{\unsure{7|?}}',alternatives='7; question mark',reason='Small crossed upper bar/stem, without a detached question-mark dot or securely closed9 head.')
doubts[5].update(reading=r'\unsure{*|\deleted{``}|``}',alternatives='star-like mark; cancelled double opener; joined live double opener',reason='Central white opening and crossed projections do not secure identity or cancellation state.')
doubts.insert(4,dict(place='200 opener before it is',reading=r"\unsure{'|``}",alternatives='single bent opener; fused pair',confidence='medium',reason='The angular fork is one joined body, not a securely separated pair.'))
doubts.insert(8,copy.deepcopy(R['C']['remaining_doubts'][9]))
inventory=copy.deepcopy(R['B']['inventory'])
inventory[8]['first_words_or_objects']='Cancelled for, letters resolved; opener state separately uncertain'
inventory[14]['first_words_or_objects']=inventory[14]['first_words_or_objects'].replace('ls7','p191/196 ls7')
inventory[23]['first_words_or_objects']='whether; wether; is with upper streak and separate low point before a castrated ram!'
inventory[25]['first_words_or_objects']='Cancelled small7/question remnant'
inventory[33]['first_words_or_objects']='Uncertain star-like group or quotation, with live/cancelled quote alternatives'
inventory[46]['first_words_or_objects']='224 line2 c.f. p.32'
extras={4:('drawing','After l.-9 before Riemannian','Separate short oblique stroke'),8:('text','Before cancelled for at193','Opening pair uncertain between cancelled and live'),23:('drawing','Between is and a at205','Upper oblique streak and distinct low point'),42:('text','Before that in live p216 question','Exclamation/single-opener uncertainty')}
inv=[]
for i,x in enumerate(inventory):
 inv.append(x)
 if i in extras:
  kind,pos,words=extras[i];inv.append(dict(sheet_kind='list',hand=x['hand'],element=str(i)+'a',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
for i,x in enumerate(inv,1):x['reader_element']='B'+x['element'];x['element']=f'{i:02}'

notes=copy.deepcopy(R['B']['notes'])
notes[2]=notes[2].replace('p196 l18','p191/196 l18')
notes[3]=notes[3].replace('a literal low point after is','a definite low point and upper streak beside is, reproduced geometrically without assigning punctuation function')
notes.append('Local mathematical check (S024-Hom-presheaf-construction): interpreting Hom as functor sets and A/a as the ordinary slice, u:a→a′ gives postcomposition A/a→A/a′; precomposition then gives Hom(A/a′,X)→Hom(A/a,X). Identities/composition follow from the corresponding postcomposition maps. Postcomposition by X→Y is covariant in X and commutes with these maps, so Cat→the presheaves on A is coherent under the ordinary size interpretation. This checks only the displayed construction and does not resolve j/J or the overwritten arguments; the cited page32 is not supplied.')
notes.append('Local mathematical check (S024-slice-description-types): if the small numerator is B, the bare assignment x↦B/x takes objects of B to categories and extends by postcomposition to B→Cat. The displayed j_B construction instead has type Cat→presheaves on B, X↦(x↦Hom(B/x,X)). These are different types under that interpretation, providing a conditional reason for the writer’s question. The unseen typescript is not declared wrong, and the uncertain numerator is not forced from mathematics.')
notes.append('Root preserves the p193 quotation state separately from the resolved cancelled word for; p216’s opening and terminal high groups remain live outside the cancellation. The live p216 opener remains !/single-quote uncertain. At p219 the heavy t is treated as retracing, not a recoverable additional cancelled letter. Three j/J occurrences are independently doubtful. Faint rules/points are reproduced without assigning editorial purpose, and the two main rules are anchored around the reference/text columns.')
events=[]
for r in 'ABC':
 for e in R[r]['math_checks']:
  sid='S024-Hom-presheaf-construction' if 'variance' in e['statement_id'] else 'S024-slice-description-types'
  ni=9 if 'Hom' in sid else 10
  events.append(dict(statement_id=sid,date='2026-11-20',who_model_effort_run=f'GPT-6 Astra Pro; effort not exposed; /root/scan024_{r.lower()}',type=e['type'],outcome=e['outcome']+f' Note N024.{ni}.'))
for sid,ni,summary in [('S024-Hom-presheaf-construction',9,'Checked slice postcomposition, contravariance in a, identities/composition, covariance in X and commutation, under ordinary small-category/functor-set interpretation.'),('S024-slice-description-types',10,'Compared the conditional B→Cat slice assignment with Cat→presheaves on B; no claim about the absent cited typescript or uncertain ink was inferred.')]:
 events.append(dict(statement_id=sid,date='2026-11-20',who_model_effort_run='GPT-6 Astra Pro; effort not exposed; /root',type='targeted proof check',outcome=summary+' Developed before final reader returns in records/math_scan024_root.md; later compared their independent local checks. '+f'Note N024.{ni}.'))
notation=copy.deepcopy(R['B']['notation'])
notation.extend([dict(sign=r'\unsure{191|196}',location='faded page reference before inserted p197',reading='191 favoured from narrow final stem;196 remains possible.',evidence='A crop05; no surrounding-number inference.'),dict(sign=r"\unsure{!|'}",location='live p216 opener',reading='Exclamation-like upper body plus lower point; single opener also possible.',evidence='C crop18 and A crop16 separate this mark from the prior-line descender.'),dict(sign='c.f.',location='p224 line2',reading='Final low abbreviation stop retained.',evidence='A crop20: distinct point after f, before p.32.')])
for x in notation:
 if x.get('sign')=='c.f':x['sign']='c.f.'
coverage='All three final full readings, literal changes, C doubt/context decisions and inventories compared. Root inspected30 distinct existing reader crops and3 new crops (two long rules and the point after usual). All reader/witness and reader/reader disagreements were decided on retained crops. Re-displays and the rotation-only B28 view derivative are not new crops. All64 inventory rows are represented. H is description only; no H comparison rows. No OCR, outside research or compilation. Seven actual bounded mathematical check events are recorded, separately from ink readings.'
rule_lines=re.findall(r'\\draw\[.*?;',text[text.index('% The left rule separates'):],re.S)
assert len(rule_lines)==3
for ident,line in zip(['024-left-rule','024-right-rule','024-faint-right-trace'],rule_lines):
 next(x for x in decisions if x['id']==ident)['final']=line
rec=write_record(24,'B','brief_v09.md',text,decisions,cd,doubts,notes,coverage,viewed=viewed,events=events,inventory=inv,notation=notation)
# Abbreviation expansion remains apparatus only; final spelling has its low stop.
for x in rec['abbreviations']:
 if x['form']=='c.f':x['form']='c.f.'
(W/'records/scan024.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2))
print('Scan024:',len(decisions),'decision rows;',sum(x['diff_c'] for x in decisions),'C changes;',len(doubts),'doubts;',len(inv),'inventory rows;',len(events),'check events.')
