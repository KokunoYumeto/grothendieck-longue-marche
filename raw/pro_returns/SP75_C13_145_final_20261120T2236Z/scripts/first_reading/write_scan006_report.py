from pathlib import Path
import json,csv
root=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
out=root/'edition/reader_reports'
boxes=json.loads((out/'145_scan006_crop_boxes.json').read_text())
tex=r'''\scanpage{6}
par $\rho$, mais pas de $\unsure{\mathfrak S_3|\mathcal S_3}$, car on a p.ex
\[
\inserted{\sigma_0\sigma_1\bigl(=\sigma_1\sigma_\infty=\sigma_\infty\sigma_0\bigr)=\rho}
\]
\[
\deleted{[\sigma_0,\sigma_1]\unsure{\sigma_0^{-1}\sigma_1^{-1}}=(\sigma_0\sigma_1)^2=\rho^2}\qquad\text{dans }\unsure{\mathfrak S_3|\mathcal S_3}
\]
mais dans $\operatorname{Aut}(\pi)$, \deleted{$\sigma_0\sigma_1$}
\[
\sigma_0\sigma_1(l_0)=\sigma_0(l_\infty)=l_1=\rho(l_0)
\]
\margin{$\unsure{2|z|t}$}
\[
\begin{aligned}
\sigma_0\sigma_1(l_1)&=\sigma_0(l_\infty^{-1}l_0^{-1})=\sigma_0(l_\infty)^{-1}\sigma_0(l_0)^{-1}\\
&=l_1^{-1}(l_1^{-1}l_\infty^{-1})^{-1}=l_1^{-1}l_\infty l_1
\end{aligned}
\]
\[
\begin{aligned}
\sigma_0\sigma_1(l_\infty)&=(l_1^{-1}l_\infty l_1)^{-1}l_1^{-1}=l_1^{-1}l_\infty^{-1}\deleted{l_1}\\
&=l_1^{-1}(l_\infty^{-1}l_1^{-1})l_1=l_1^{-1}l_0l_1
\end{aligned}
\]
donc $\sigma_0\sigma_1=\operatorname{int}(l_1^{-1})\rho$ dans $\operatorname{Aut}(\pi)$
et de $\bar m$
\[
\sigma_1\sigma_\infty=\operatorname{int}(l_\infty^{-1})\rho
\]
\[
\sigma_\infty\sigma_0=\operatorname{int}(l_0^{-1})\rho
\]

On a une représentation de $\unsure{\mathfrak S_3|\mathcal S_3}$ dans le groupe \uline{extérieur} à lacets seulement. Notons qu'on ne peut espérer réaliser cette opération extérieure par une vraie opération (du moins pour le groupe discret) vu que $\unsure{\mathfrak S_3|\mathcal S_3}$ opérant sur $\mathbb P^1_{\mathbb C}\setminus\{0,1,\infty\}$ n'a pas de pt fixe. Le fait qu'on ait pu faire opérer $\mathbb Z/3\mathbb Z$ \inserted{sur $\unsure{\pi|\Pi}$ lui-$\bar m$} \unsure{provient|pvt} du fait que son action sur $\mathbb P^1_{\mathbb C}-\{0,1,\infty\}$ admet un (et $\bar m$ deux!) point fixe\inserted{, savoir $\unsure{\pm\bar j|-\bar j|\pm j}$ ($j$ racine primitive troisième de $1$)} qu'on \deleted{\unsure{pourra}} \unsure{a} pris comme origine pour calculer le $\pi_1$

Signalons aussi qu'on écrira dans le groupe de Teichmüller \inserted{$\Gamma_{0,3}$ opérant sur $\unsure{\pi_{0,3}|\Pi_{0,3}}$} la ``conjugaison complexe''
\mspage{5}
'''
(out/'145_scan006.tex').write_text(tex,encoding='utf-8')
def crop(n): return f'crops/145_scan006_{n}.png'
def ch(i,place,C,H,final,ink,confidence,kind,c_changed,h_changed,marked,n,cat,math=''):
 return dict(id=f's006-{i:02d}',place=place,C=C,H=H,final=final,ink=ink,confidence=confidence,kind=kind,c_changed=c_changed,h_changed=h_changed,marked_in_H=marked,crop=crop(n),box=boxes[n],error_category=cat,math_consequence=math)
changes=[
 ch(1,'Upper replacement line, above the cancelled commutator',r'\inserted{\sigma_0\sigma_1\bigl(=\sigma_1\sigma_\infty=\sigma_\infty\sigma_0\bigr)=\rho}',r'\sigma_0\sigma_1\bigl(=\sigma_1\sigma_\infty=\sigma_\infty\sigma_0\bigr)=\rho',r'\inserted{\sigma_0\sigma_1\bigl(=\sigma_1\sigma_\infty=\sigma_\infty\sigma_0\bigr)=\rho}','The live formula is crowded above a fully cancelled prior line, in darker ink. Each sigma index and the final rho is visible. Its replacement/insertion position is preserved.','high','insertion or placement',False,True,'no','top_insert_and_strike',[6,7]),
 ch(2,'Cancelled first display, middle product and deletion extent',r'\deleted{[\sigma_0,\sigma_1]\unsure{\sigma_0^{-1}\sigma_1^{-1}}=(\sigma_0\sigma_1)^2=\rho^2}',r'\struck{[\sigma_0,\sigma_1]\ill{}}=\struck{(\sigma_0\sigma_1)^2=\rho^2}',r'\deleted{[\sigma_0,\sigma_1]\unsure{\sigma_0^{-1}\sigma_1^{-1}}=(\sigma_0\sigma_1)^2=\rho^2}','The bracketed sigma terms and the right-hand square and rho square remain readable under cancellation. Between the bracket and equals, sigma-like roofs and raised minus/one strokes survive, but hatching prevents confirming every base/index. Retain C’s proposed product as doubtful, rather than replacing it by an undifferentiated illegible stretch. The crossing/hatching belongs to the entire abandoned equation; the following dans and S are live.','low','readable ink left as \\ill{}',False,True,'yes','top_insert_and_strike',[1,5,7]),
 ch(3,'After mais dans Aut(pi), cancelled fragment',r'\deleted{\unsure{on a}}',r'\struck{\sigma_0\sigma_1}',r'\deleted{\sigma_0\sigma_1}','Two sigma roofs are visible, the first with its round lower 0 and the second with a descending index 1. The across-going stroke cancels them. The first cannot be an o followed by an n, and no separate prose a is present.','high','misread symbol or index',True,False,'no','aut_struck_words',[1,2,7]),
 ch(4,'et de, before the two cyclic formula lines',r'\unsure{=|\bar m}','même',r'\bar m','A detached horizontal overbar lies over a lower cursive trace with two low humps/joins. The lower trace is a letter m, not the second straight bar of an equals sign.','high','abbreviation expanded or spelling modernised',True,True,'no','de_meme_abbreviation',[1,8]),
 ch(5,'Qualification in the long prose paragraph','du moins',r'en \uncertain{restant}','du moins','The first word has the short d-rise and u continuation. The second has m, rounded o, dotted i, and final ns; it lacks the tall t required by restant. The following pour is separate.','high','misread word',False,True,'yes','du_moins',[2]),
 ch(6,'Insertion following Z/3Z',r'\inserted{sur $\pi$ lui-$=$}',r'\marginal{\uncertain{sur $\Pi$ lui-même}} $\mathbb Z/3\mathbb Z$',r'$\mathbb Z/3\mathbb Z$ \inserted{sur $\unsure{\pi|\Pi}$ lui-$\bar m$}','The hooked connector runs from the note above the group to a point after Z/3Z, not before it. Sur and lui are visible. The ending has a hyphen and an m-like lower trace with an overbar, not a written-out même. The thick pi has a top and two upright legs, but its case is not securely distinct in this small, reinforced writing.','medium','insertion or placement',True,True,'yes','sur_pi_insertion',[1,6,8]),
 ch(7,'Parenthesis et ... deux!',r'\unsure{=|\bar m}',r'\uncertain{(et même}',r'\bar m','The lower cursive m is joined into the preceding et, and has two short rises; above it stands a separate bar. The exclamation mark and closing parenthesis after deux are live.','high','abbreviation expanded or spelling modernised',True,True,'yes','et_meme_abbreviation',[1,8]),
 ch(8,'Sign and accented/barred j in fixed-point insertion',r'\unsure{-\bar j|-j|\pm j}',r'\pm j',r'\unsure{\pm\bar j|-\bar j|\pm j}','The sign preceding j is heavily reinforced, with a vertical component and two apparent horizontal strokes, hence plus/minus-like. A separate, long horizontal bar stands above the j. The dark reinforcing strokes leave the exact initial sign uncertain; the difference between a bar and an unusually long j-dot is also not eliminated. No mathematical substitution has been made.','low','misread symbol or index',True,True,'no','fixed_point_insertion_and_cancellation',[1]),
 ch(9,'Contents and attachment of fixed-point insertion',r'point fixe, \inserted{savoir $\unsure{-\bar j|-j|\pm j}$ ($j$ racine primitive troisième de $1$)}',r'le $\pi_1$ \marginal{, savoir $\pm j$ (racine primitive troisième de 1)}',r'point fixe\inserted{, savoir $\unsure{\pm\bar j|-\bar j|\pm j}$ ($j$ racine primitive troisième de $1$)}','The insertion begins with a comma and savoir. A clear descending j occurs immediately after the opening parenthesis and before racine; H omits it. The two-line note ends with the parenthesis and a connector that curves down to the location after point fixe, before qu’on, not after pi_1.','high','insertion or placement',True,True,'no','fixed_point_insertion_and_cancellation',[3,6]),
 ch(10,'Main line beneath the fixed-point insertion',r"qu'on \deleted{\unsure{pourra}} a pris",r'qui \uncertain{peut} être \struck{\ill{}} \uncertain{pris}',r"qu'on \deleted{\unsure{pourra}} \unsure{a} pris",'The live beginning has q/u strokes, an apostrophe and the low on continuation. The cancelled word begins with a tall p and ends in low connected strokes; cancellation obscures its interior, so pourra is not promoted to certainty. The short live form following it is probably a, but has an unusually long entry stroke; it remains doubtful. There is no separate legible peut être sequence as in H. Pris begins the next main line.','medium','misread word',False,True,'yes','fixed_point_insertion_and_cancellation',[2,5,7,9]),
 ch(11,'Final paragraph, verb after qu’on','a inclus',r'\uncertain{écrira}','écrira','An accented/dotted small initial e-like hook is followed by a c curve, short r/i strokes (with a detached i-dot), then ra. There is no tall l ascender corresponding to inclus. The compressed interior warrants a second reader, but favors H’s écrira.','medium','misread word',True,False,'yes','a_inclus',[2]),
 ch(12,'Teichmüller insertion and apparent closing parenthesis',r'de Teichmüller \inserted{$\Gamma_{0,3}$ opérant sur $\pi_{0,3}$}',r'\marginal{$\Gamma_{0,3}$ opérant sur $\Pi_{0,3}$} de Teichmüller)',r'de Teichmüller \inserted{$\Gamma_{0,3}$ opérant sur $\unsure{\pi_{0,3}|\Pi_{0,3}}$}','Gamma, its indices 0,3, opérant and sur are readable in the interline. The pi has two uprights and a slightly hooked right foot, but its case is not securely separable here. The large curve at the end of Teichmüller continues into the note’s connector; it is not an independent closing parenthesis. The note attaches after Teichmüller.','medium','insertion or placement',False,True,'no','teichmuller_insertion',[1,6,9]),
 ch(13,'Last line, quotation marks',"``conjugaison complexe''",'« conjugaison complexe »',"``conjugaison complexe''",'Two short upright oblique strokes stand above the left and right ends of the quoted phrase. They are doubled quotation strokes, not angle-shaped guillemets.','high','other',False,True,'no','conjugaison_quotes',[10]),
 ch(14,'Lower left margin, manuscript number',r'\mspage{5}','',r'\mspage{5}','A horizontal head, short left upright, middle shoulder and large lower curve form a clear 5.','high','omission',False,True,'no','manuscript_number',[3]),
 ch(15,'End of the first of the two cyclic formulas',r'\sigma_1\sigma_\infty=\operatorname{int}(l_\infty^{-1})\rho',r'\sigma_1\sigma_\infty=\mathrm{int}(l_\infty^{-1})\rho,',r'\sigma_1\sigma_\infty=\operatorname{int}(l_\infty^{-1})\rho','The first formula ends in the long descending tail of rho; no detached comma follows it. The next cyclic formula is on a separate lower line. Other H backslash-comma tokens in the same formulas are only TeX spacing and are excluded.','high','text not on the page',False,True,'no','two_cyclic_formulas',[9]),
 ch(16,'Small isolated mark to the right of the first calculation','','',r'\margin{$\unsure{2|z|t}$}','The mark is dark and compact, with an upper hooked/crossed stroke, a descending diagonal/curve, and a lower horizontal foot. It resembles 2, but z/t or a nonsemantic pen mark cannot be excluded. Both witnesses omit it. This provisional inclusion requires root adjudication.','low','omission',True,True,'no','isolated_right_mark',[3,10]),
 ch(17,'End of the sentence calculer le pi_1',r'le $\pi_1$.',r'le $\pi_1$ [insertion].',r'le $\pi_1$','After the subscript 1 the enlarged source area is blank: there is no dark dot corresponding to either witness’s full stop. The next paragraph begins on the following line.','high','text not on the page',True,True,'no','pi1_line_end',[9])
]
def dec(id,decision,reading,ink,n,confidence):
 return dict(id=id,decision=decision,reading=reading,ink=ink,crop=crop(n),box=boxes[n],confidence=confidence)
S=r'\unsure{\mathfrak S_3|\mathcal S_3}'
Snote='A single ornate S has an outer loop, an inner return, and an upturned terminal; the subscript 3 is plain. The glyph is consistent at the four occurrences, but the isolated page does not securely distinguish the intended typographic Fraktur versus calligraphic alphabet. Retain the stated alternatives.'
decisions=[
 dec('M0773','undecided',S,Snote,'s3_opening','medium'),
 dec('M0774','undecided',S,Snote,'top_insert_and_strike','medium'),
 dec('M0775','alternative',r'\bar m','The lower line contains the two short cursive joins of m beneath a detached bar, rather than two equivalent straight equals strokes.','de_meme_abbreviation','high'),
 dec('M0776','undecided',S,Snote,'s3_representation','medium'),
 dec('M0777','undecided',S,Snote,'s3_operant','medium'),
 dec('M0778','alternative',r'\bar m','A lower cursive m joined from et has a separate horizontal overbar; the lower line is not straight.','et_meme_abbreviation','high'),
 dec('M0779','undecided',r'\unsure{\pm\bar j|-\bar j|\pm j}','The reinforced initial sign is plus/minus-like, while j has a separate long horizontal mark above it. The combined reading ± barred-j is newly allowed, but neither the sign nor the interpretation of the bar is fully secure.','fixed_point_insertion_and_cancellation','low'),
 dec('U006-01','undecided',r'\deleted{[\sigma_0,\sigma_1]\unsure{\sigma_0^{-1}\sigma_1^{-1}}=(\sigma_0\sigma_1)^2=\rho^2}','Unindexed C doubt: cancellation hatching obscures the bases and indices of the middle product; raised inverse strokes survive, but not every letter is plain.','top_insert_and_strike','low'),
 dec('U006-02','other',r'\deleted{\sigma_0\sigma_1}','Unindexed C doubt on on a: both sigma roofs, lower 0 and lower 1 are visible under the cancellation.','aut_struck_words','high'),
 dec('U006-03','first',r'\deleted{l_1}','Unindexed C doubt: the tall looped l and its lower single index stroke 1 remain traceable through the diagonal cancellation. The whole surrounding third calculation was read with the symbol.','linfty_formula','high'),
 dec('U006-04','undecided',r'\deleted{\unsure{pourra}}','Unindexed C doubt: initial p and final low trace survive, but the central connected letters are covered by the strike, so the word is not resolved.','fixed_point_insertion_and_cancellation','low')
]
doubts=[]
for place in ['Opening prose after pas de','Live dans at the right of the cancelled display','On a une représentation de','vu que ... opérant']:
 doubts.append(dict(place=place,reading=S,alternatives=[r'\mathfrak S_3',r'\mathcal S_3'],confidence='medium',reason='The ornate handwritten S is clear, but the isolated page does not settle the LaTeX alphabet. This is an alphabet-classification uncertainty, not doubt about S or the index 3.'))
doubts += [
 dict(place='Cancelled first display, middle product',reading=r'\unsure{\sigma_0^{-1}\sigma_1^{-1}}',alternatives=[],confidence='low',reason='Cancellation hatching prevents every base letter/index from being verified; C’s proposed product remains possible.'),
 dict(place='sur pi lui-bar-m insertion',reading=r'\unsure{\pi|\Pi}',alternatives=[r'\pi',r'\Pi'],confidence='medium',reason='Thickened two-legged handwritten pi; case is not secure in the small inserted form.'),
 dict(place='Main line after Z/3Z and its insertion',reading=r'\unsure{provient|pvt}',alternatives=['provient','pvt'],confidence='low',reason='The form has an unmistakable p-descender and final tall t but strongly compressed interior; a contraction pvt is possible. Both witnesses give provient. This is a newly marked certainty question, not an asserted expansion.'),
 dict(place='Fixed-point insertion before the explanatory parenthesis',reading=r'\unsure{\pm\bar j|-\bar j|\pm j}',alternatives=[r'\pm\bar j',r'-\bar j',r'\pm j'],confidence='low',reason='Reinforcing strokes obscure the initial sign; the long horizontal above j may be a bar, although a very elongated dot is not wholly excluded.'),
 dict(place='Cancelled word following qu’on',reading=r'\deleted{\unsure{pourra}}',alternatives=[],confidence='low',reason='The cancellation covers the interior of the word; not all letters are plain.'),
 dict(place='Short live form after the cancelled word, before next-line pris',reading=r'\unsure{a}',alternatives=[],confidence='low',reason='The short form is probably a but has an unusually long initial descending stroke; preserved with a new doubt.'),
 dict(place='Teichmüller insertion, group acted upon',reading=r'\unsure{\pi_{0,3}|\Pi_{0,3}}',alternatives=[r'\pi_{0,3}',r'\Pi_{0,3}'],confidence='medium',reason='Both legs and indices are clear, but case cannot confidently be inferred from the small hand alone.'),
 dict(place='Right of first calculation',reading=r'\margin{$\unsure{2|z|t}$}',alternatives=['2','z','t','nonsemantic pen mark'],confidence='low',reason='Newly noticed dark isolated mark; its status as a semantic inscription requires root adjudication.')
]
def inv(el,kind,pos,first,box,hand='main manuscript hand'):
 return dict(element=el,kind=kind,position=pos,first_words_or_objects=first,box=box,sheet_kind='handwritten mathematical manuscript',hand=hand,transcribed='yes')
inventory=[
 inv('T01','text','top opening, one line','par rho, mais pas de ...',[280,65,1510,165]),
 inv('I01','insertion','above cancelled top display','sigma_0 sigma_1 (= ...)=rho',[380,140,890,220]),
 inv('D01','deletion','top cancelled display','[sigma_0,sigma_1] ... rho^2',[315,200,990,300]),
 inv('T02','text','right of cancelled display','dans S_3',[1060,210,1290,300]),
 inv('T03','text','line before the three calculations','mais dans Aut(pi),',[275,320,825,400]),
 inv('D02','deletion','after Aut(pi), on same line','sigma_0 sigma_1',[858,340,985,395]),
 inv('F01','display','first calculation','sigma_0 sigma_1(l_0)=...',[385,400,1065,480]),
 inv('M01','margin note','right of first calculation','uncertain isolated 2/z/t',[1480,435,1520,477],'attribution uncertain; same dark appearance as ink accents'),
 inv('F02','display','second calculation, one long original row','sigma_0 sigma_1(l_1)=...',[385,475,1658,578]),
 inv('F03','display','third calculation, one long original row','sigma_0 sigma_1(l_infty)=...',[385,545,1658,655]),
 inv('D03','deletion','inside third calculation','l_1',[1138,560,1190,622]),
 inv('F04','display','concluding calculation line with prose donc/dans','donc sigma_0 sigma_1=int(l_1^-1)rho dans Aut(pi)',[240,670,1400,755]),
 inv('T04','text','between concluding calculation and two cyclic formulas','et de bar-m',[240,745,505,815]),
 inv('F05','display','first cyclic formula','sigma_1 sigma_infty=int(l_infty^-1)rho',[500,815,935,905]),
 inv('F06','display','second cyclic formula','sigma_infty sigma_0=int(l_0^-1)rho',[505,905,930,1000]),
 inv('T05','text','long lower prose paragraph, ten main rows','On a une représentation ...',[225,1025,1658,2150]),
 inv('I02','insertion','above Z/3Z, connector ends after group','sur pi lui-bar-m',[1265,1685,1540,1790]),
 inv('I03','insertion','above main point-fixe clause, two lines',', savoir ... (j racine primitive troisième de 1)',[1015,1905,1658,2040]),
 inv('D04','deletion','main line below fixed-point insertion','uncertain pourra',[1305,1988,1448,2040]),
 inv('T06','text','last paragraph, two main rows','Signalons aussi qu’on écrira ...',[230,2145,1635,2335]),
 inv('I04','insertion','between two final rows, attached after Teichmüller','Gamma_0,3 opérant sur pi_0,3',[430,2200,865,2305]),
 inv('M02','margin note','lower left','5',[35,2260,92,2335],'handwritten pagination; attribution not established')
]
B=[]
def sb(n,kind,coords,reading):B.append(dict(box=f'B{n:02d}',kind=kind,coords=coords,reading=reading))
sb(1,'C alphabet doubt',boxes['s3_opening'],r'pas de $\unsure{\mathfrak S_3|\mathcal S_3}$,')
sb(2,'replacement insertion, struck passage, C formula and alphabet doubts',boxes['top_insert_and_strike'],r'\inserted{\sigma_0\sigma_1(=\sigma_1\sigma_\infty=\sigma_\infty\sigma_0)=\rho}\quad\deleted{[\sigma_0,\sigma_1]\unsure{\sigma_0^{-1}\sigma_1^{-1}}=(\sigma_0\sigma_1)^2=\rho^2}\quad\text{dans }\unsure{\mathfrak S_3|\mathcal S_3}')
sb(3,'struck passage; C/H word-versus-symbol disagreement',boxes['aut_struck_words'],r'$\operatorname{Aut}(\pi)$, \deleted{$\sigma_0\sigma_1$}')
sb(4,'whole formula containing resolved C doubt on struck l_1; adjacent full calculation included to avoid fragmentary overlap',[380,475,1658,655],r'\sigma_0\sigma_1(l_1)=\sigma_0(l_\infty^{-1}l_0^{-1})=\sigma_0(l_\infty)^{-1}\sigma_0(l_0)^{-1}=l_1^{-1}(l_1^{-1}l_\infty^{-1})^{-1}=l_1^{-1}l_\infty l_1\quad\sigma_0\sigma_1(l_\infty)=(l_1^{-1}l_\infty l_1)^{-1}l_1^{-1}=l_1^{-1}l_\infty^{-1}\deleted{l_1}=l_1^{-1}(l_\infty^{-1}l_1^{-1})l_1=l_1^{-1}l_0l_1')
sb(5,'C resolved abbreviation doubt and H expansion',boxes['de_meme_abbreviation'],r'et de $\bar m$')
sb(6,'formula punctuation disagreement',boxes['two_cyclic_formulas'],r'\sigma_1\sigma_\infty=\operatorname{int}(l_\infty^{-1})\rho\qquad\sigma_\infty\sigma_0=\operatorname{int}(l_0^{-1})\rho')
sb(7,'C alphabet doubt',boxes['s3_representation'],r'de $\unsure{\mathfrak S_3|\mathcal S_3}$')
sb(8,'C/H lexical disagreement',boxes['du_moins'],'(du moins pour')
sb(9,'C alphabet doubt',boxes['s3_operant'],r'$\unsure{\mathfrak S_3|\mathcal S_3}$ opérant')
sb(10,'interlinear insertion, case and abbreviation disagreement, newly doubtful contracted word',boxes['sur_pi_insertion'],r'$\mathbb Z/3\mathbb Z$ \inserted{sur $\unsure{\pi|\Pi}$ lui-$\bar m$} \unsure{provient|pvt} du')
sb(11,'fixed-point insertion; C doubts and C/H lexical disagreements; cancellation; abbreviation; pi_1 punctuation',[230,1900,1658,2150],r"un (et $\bar m$ deux!) point fixe\inserted{, savoir $\unsure{\pm\bar j|-\bar j|\pm j}$ ($j$ racine primitive troisième de $1$)} qu'on \deleted{\unsure{pourra}} \unsure{a} pris comme origine pour calculer le $\pi_1$")
sb(12,'final verb disagreement; insertion; Greek case doubt; connector mistaken for parenthesis; quote forms',[230,2145,1635,2335],r"Signalons aussi qu'on écrira dans le groupe de Teichmüller \inserted{$\Gamma_{0,3}$ opérant sur $\unsure{\pi_{0,3}|\Pi_{0,3}}$} la ``conjugaison complexe''")
sb(13,'handwritten page number',boxes['manuscript_number'],r'\mspage{5}')
sb(14,'newly noticed isolated possible inscription',boxes['isolated_right_mark'],r'\margin{$\unsure{2|z|t}$}')
notation=[
 {'observation':r'\bar m abbreviates même; the lower m can look like the lower stroke of =.','observed_places':['et de before cyclic formulas','lui-bar-m insertion','et bar-m deux!'],'qualification':'The three lower traces are m-like and barred; these are local readings, not a claim about other pages.'},
 {'observation':'The same ornate S with an outer enclosure and inner return occurs with subscript 3 four times.','observed_places':['opening','dans after cancelled display','representation paragraph','opérant clause'],'qualification':'The letter and index are secure; Fraktur versus calligraphic font remains open.'},
 {'observation':'The three loop generators are l_0, l_1 and l_infty; inverse signs are raised -1.','observed_places':['three expanded calculations','concluding inner automorphism formulas'],'qualification':'All visible indices and inverse signs were read on this page; the cancelled middle product at the top remains doubtful.'},
 {'observation':'Aut(pi), int(l^-1) and rho are written repeatedly in the calculations.','observed_places':['introductory calculation line','concluding calculation and two cyclic formulas'],'qualification':'No definition or algebraic verification is supplied by this reader.'},
 {'observation':'The main prose uses blackboard-bold-looking P and C for the punctured projective line and Z/3Z for the cyclic group.','observed_places':['no-fixed-point sentence','cyclic fixed-point sentence'],'qualification':'The first set subtraction stroke is slanted; the later one is horizontal, preserved as setminus and minus respectively.'},
 {'observation':'Small interlinear pi forms are more angular/heavily inked than the clear main-line pi in Aut(pi) and pi_1.','observed_places':['sur pi lui-bar-m','Gamma_0,3 opérant sur pi_0,3'],'qualification':'Case retained as uncertain; no inferred uniformity between uppercase and lowercase was imposed.'}
]
hand=[
 {'habit':'A barred cursive m has a nearly horizontal lower body and can be read as an equals sign.','places':['et de bar-m','lui-bar-m','et bar-m deux'],'universal_on_page':'All three identified shorthand instances show a separate overbar and curved lower trace.','witness_misreadings':'C favors = in its alternatives and gives = plainly in lui-=; H expands all three to même.'},
 {'habit':'The sigma roof and compact low index survive a horizontal cancellation and can resemble connected prose.','places':['cancelled fragment after Aut(pi)'],'universal_on_page':'Observed at this one cancellation only.','witness_misreadings':'C’s on a is σ_0σ_1.'},
 {'habit':'Small accented e/c/r/i sequences can be compressed with low connectors and little vertical extent.','places':['final écrira'],'universal_on_page':'Local observation only.','witness_misreadings':'C gives a inclus; the absence of an l ascender and presence of the dotted/marked small sequence favor écrira.'},
 {'habit':'Insertion connectors make broad hooks that can resemble independent parentheses.','places':['sur pi insertion','fixed-point insertion','Gamma insertion at Teichmüller'],'universal_on_page':'All three prose insertions have connecting strokes; their shapes differ.','witness_misreadings':'H places the first before Z/3Z, the second after pi_1, and reads a closing parenthesis after Teichmüller.'},
 {'habit':'Prose strokes can compress a long word into a p-descender, very low interior joins and a final t.','places':['provient/pvt after Z/3Z'],'universal_on_page':'One unresolved instance.','witness_misreadings':'Both witnesses give a full provient; the ink may instead use a contraction.'},
 {'habit':'Double quotation marks are pairs of elevated short oblique strokes.','places':['conjugaison complexe'],'universal_on_page':'Only quoted phrase on this page.','witness_misreadings':'H substitutes guillemets.'}
]
abbreviations=[
 {'form':'p.ex','expansion':'par exemple','place':'opening line'},
 {'form':r'\bar m','expansion':'même','place':'et de before cyclic formulas; lui-bar-m insertion; et bar-m deux!'},
 {'form':'pt','expansion':'point','place':'n’a pas de pt fixe'},
 {'form':r'\operatorname{Aut}','expansion':'automorphismes','place':'calculation introduction and conclusion'},
 {'form':r'\operatorname{int}','expansion':'automorphisme intérieur','place':'three product formulas'},
 {'form':'pvt (possible reading only)','expansion':'provient','place':'after Z/3Z and its insertion; remains unresolved'}
]
rows=list(csv.DictReader((root/'packets/145_scan006/differences.tsv').open(encoding='utf-8'),delimiter='\t'))
subst={4:'s006-02',8:'s006-03',23:'s006-04',25:'s006-15',28:'s006-05',30:'s006-06',31:'s006-06',32:'s006-07',33:'s006-08',34:'s006-09',35:'s006-11',36:'s006-12',37:'s006-12',38:'s006-13',39:'s006-13'}
explain={
 1:'C scan identifier is editorial.',2:'Tokenized C alphabet doubt; retained and covered by M0773, not a substantive new reading.',
 3:'H TeX backslash-semicolon is mathematical spacing, not manuscript punctuation.',
 5:'C alphabet alternatives plus the beginning of H’s editorial note; M0774 covers the source alphabet doubt.',
 6:'Continuation of H’s editorial note about the cancelled equation, not added manuscript text.',
 7:'Continuation of H’s editorial note; its repeated formula is not a second inscription.',
 9:'aligned environment only.',10:'Display/aligned grouping only.',11:'H backslash-comma spacing only.',12:'H backslash-comma spacing only.',13:'H backslash-comma spacing only.',14:'Display/aligned grouping only.',15:'H backslash-comma spacing only.',16:'H backslash-comma spacing only.',17:'H backslash-comma spacing only.',18:'H backslash-comma spacing only.',19:'H backslash-comma between factors and tokenizer concatenation of 0 with the next l; same ink reading.',20:'Display boundary only.',21:'H backslash-comma spacing only.',22:'Display boundary only.',24:'H backslash-comma spacing only.',26:'H backslash-comma spacing only.',27:'Tokenized C alphabet doubt, preserved under M0776.',29:'Tokenized C alphabet doubt, preserved under M0777.'}
coverage=[]
for i,row in enumerate(rows,1):
 if i in subst:
  d={'row':i,'status':'substantive','change_id':subst[i]}
  if i==33:d['explanation']='One tokenization span combines the sign (s006-08), inserted clause and its j (s006-09), and the main-line qu’on/cancellation/a dispute (s006-10).'
  if i==34:d['explanation']='The note is a genuine insertion, but H locates it after pi_1; see s006-09.'
  if i==39:d['explanation']='Closing quote forms are s006-13; the source handwritten 5 omitted by H is s006-14. H’s long explanatory note is editorial and excluded.'
  coverage.append(d)
 else:coverage.append({'row':i,'status':'macro/editorial','explanation':explain.get(i,'Macro/editorial tokenization only.')})
report=dict(scan=6,reader='/root/reader_c',lines_read=29,
 layout='Upright manuscript leaf. Eleven upper prose/formula rows (including the replacement row), ten main rows of the long lower prose paragraph, two main rows of the final paragraph, four interlinear prose-note rows, a handwritten 5 at lower left, and one isolated mark at upper right: 29 read lines/isolated inscriptions. One top replacement, three further prose insertions, four cancellations. No diagram or drawing. The word extérieur is singly underlined.',
 changes=changes,decisions=decisions,doubts=doubts,inventory=inventory,second_boxes=B,notation=notation,hand=hand,abbreviations=abbreviations,
 notes=[
  'The author compares a cyclic permutation with products of three sigma automorphisms. He cancels a commutator-style equation, inserts the equal products in the permutation group, and then writes three explicit calculations on l_0, l_1 and l_infty. He states that sigma_0 sigma_1 differs from rho by conjugation with l_1 inverse, with two cyclic analogues. These are descriptions of his text, not a verification by this reader.',
  'The author says the S_3 representation exists only in the exterior group “à lacets”. The wording is retained. He writes “ne peut espérer réaliser” the exterior operation by a genuine one, with the express qualification “du moins pour le groupe discret”, and appeals to the absence of a fixed point on the punctured projective line. He contrasts this with the cyclic subgroup and its one, “et bar-m deux!”, fixed point(s). The inserted algebraic expression naming that point remains uncertain.',
  'The final paragraph begins “Signalons aussi qu’on écrira ...” in the proposed reading, against C’s “a inclus”. It mentions the Teichmüller group, an interlinear Gamma_0,3 acting on a pi/Pi group with subscript 0,3, and “conjugaison complexe”. The sentence continues beyond this page; no continuation was consulted.',
  'No date is visible. The lower-left handwritten page number is 5. No numbered display is visible. The small right-hand isolated 2/z/t-like mark is provisionally transcribed but needs adjudication as a possible stray pen mark. The margin number’s hand is not independently attributed.',
  'All three required views were made once, and every main and inserted line was read. Eighteen distinct first-reading crops were created and viewed once each. The bar-m forms were compared locally on the supplied page. No other page, other reader output, OCR, recognition software, external research, or mathematical proof check was used. No clear authorial mathematical slip was asserted or silently corrected.',
  'Certainty-only additions are recorded in doubts: the possible contraction provient/pvt, the short live a, and the case of the two inserted pi forms. The four ornate S alphabet choices and the two cancelled stretches remain open. C’s uncertainty on struck l_1 is resolved from its complete calculation crop. The new sign alternative ± barred-j is retained explicitly rather than forced to the expected fixed-point notation.'
 ],check_events=[],diff_coverage=coverage)
# Root-requested inventory schema and full numeric-formula coverage.
for item in report['inventory']:
 item['sheet_kind']='text'
 item['hand']='his hand'
for item in report['second_boxes']:
 if item['box']=='B04':
  item['coords']=[380,400,1658,655]
  item['kind']='three complete calculation displays, all handwritten indices and exponents; includes C doubt on struck l_1'
  item['reading']=r'\sigma_0\sigma_1(l_0)=\sigma_0(l_\infty)=l_1=\rho(l_0)\quad'+item['reading']
 if item['box']=='B05':
  item['coords']=[235,670,1410,820]
  item['kind']='complete concluding formula with handwritten indices and exponents; resolved C abbreviation doubt and H expansion'
  item['reading']=r'donc $\sigma_0\sigma_1=\operatorname{int}(l_1^{-1})\rho$ dans $\operatorname{Aut}(\pi)$ et de $\bar m$'
 if item['box']=='B09':
  item['coords']=[230,1490,1658,1710]
  item['kind']='C alphabet doubt; complete inline punctured-projective-line formula with every handwritten number'
  item['reading']=r"le groupe discret) vu que $\unsure{\mathfrak S_3|\mathcal S_3}$ opérant sur $\mathbb P^1_{\mathbb C}\setminus\{0,1,\infty\}$ n'a pas de pt fixe. Le"
report['second_boxes'].append(dict(box='B15',kind='complete second projective-line formula with handwritten numbers',coords=[1025,1815,1658,1918],reading=r'sur $\mathbb P^1_{\mathbb C}-\{0,1,\infty\}$ admet'))

(out/'145_scan006.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'tex':str(out/'145_scan006.tex'),'json':str(out/'145_scan006.json'),'crops':len(boxes),'changes':len(changes),'decisions':len(decisions),'remaining_doubts':len(doubts),'inventory_items':len(inventory),'second_boxes':len(B),'diff_rows':len(rows),'covered_rows':len(coverage)},ensure_ascii=False))
