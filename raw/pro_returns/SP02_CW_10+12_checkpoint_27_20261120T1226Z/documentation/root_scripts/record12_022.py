from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B12-01',12,22,'cancelled_draft')
H='[No H text supplied.]'
def ch(place,C,final,shows,crop,kind='other',confidence='high',against_C=False,consequential=False):
 r.change(place,C,H,final,shows,crop,kind,confidence,against_C,False,False,consequential)
orword=r'\rlap{O}or'; supp=r'suppose\unsure{r}'; aff=r'\rlap{U}affine'; par=r'\unsure{\rlap{\S}par|par}'; elem=r'\unsure{\rlap{l}élément|Élément|élément}'
r.edit('Or par raison',orword+' par raison')
r.edit(r'\unsure{supposer}',supp)
r.edit(r'\unsure{uffine|affine|Uffine}',aff)
r.edit(r'\unsure{par}',par)
r.edit(r'\unsure{Élément|élément}',elem)
r.edit(r'\deleted{\unsure{alors}}',r'\deleted{alors}')
r.edit(r"i'\ (F'\ U')",r"\rlap{\(v\)}i'\ (F'\ U')")
stack=r'''\mbox{\begin{tikzpicture}[baseline=(base.base),x=1cm,y=1cm]
\node[anchor=west,inner sep=0] (base) at (0,0) {soit $x\quad\operatorname{Ass}F$};
\node[anchor=west,inner sep=0] at (-.15,.45) {\inserted{un élément maximal de}};
\end{tikzpicture}}'''
r.edit(r'soit $x$ \inserted{un élément maximal de} $\operatorname{Ass}F$',stack)
r.edit('% A long diagonal cancellation runs from the third text line to the end of the first paragraph.','% A long oblique cancellation crosses the Remplaçant paragraph; its exact upper scope is uncertain.\n% The pale upper extension is visible between the second and third lines. No verbal text is supplied in the empty formula slots.')
ch('opening cell','Or',orword,'The first cell contains a tall pale closed O and a darker smaller o, sharing the baseline; r is separate and clear. Both overlapping impressions are retained without assigning chronology.','Or; OrA','misread word','high',True)
ch('line1 clipped right edge',r'\unsure{supposer}',supp,'The letters suppose are complete. Beyond e, two small left-facing ink remnants meet the black right edge at the top-serif and baseline heights; the r stem and shoulder are clipped. Only the last cell remains qualified.','supposer; supposeA','misread word','medium',True)
ch('voisinage ouvert, first cell',r'\unsure{uffine|affine|Uffine}',aff,'The cell shows two full-height vertical stems with upper serifs and a rounded U bottom, together with the smaller closed a bowl and right foot. The following ffine is clear. C doubt is resolved as an overlap, not as a choice of one cleaned word.','affine; affineA','misread word','high',True)
ch('Passant, canceled two-letter word',r'\deleted{\unsure{au|en}}',r'\deleted{\unsure{au|en}}','The two underlying letters are crossed by typed x impressions. An a-like bowl and a u-like lower curve favor au, but enough strokes are covered that en is retained as the alternative.','aucancel; auA','other','low')
ch('canceled phrase after aussitôt que',r"\deleted{sur $U'$, l'intersection des}",r"\deleted{sur $U'$, l'intersection des}",'The s/u/r traces, U with raised prime, comma, l and apostrophe, dotted i and successive intersection/des letters are readable beneath the x row. C table-only doubt is resolved; deletion is retained.','cancelphrase','other','high')
ch('en vertu de, overprinted par',r'\unsure{par}',par,'The p stem/bowl and following ar are visible. Additional upper horizontal/curved strokes and a descending lower sweep overlap the p; they suggest a section-sign impression but do not separate securely. The overlap remains explicitly uncertain, and de par is not grammatically repaired.','par; parA','misread word','low',True)
ch('hand references 3.3. and 3',r'\handwritten{3.3.}; \handwritten{3}',r'\handwritten{3.3.}; \handwritten{3}','Both references have smooth sloping angular tops and free curved lower sweeps unlike the broken typewriter outlines. The first has two 3s and two points; the second is a single 3. C table doubt about typed versus handwritten is resolved.','ref33; prop3','other','high')
ch('un élément maximal de insertion placement',r'soit $x$ \inserted{un élément maximal de} $\operatorname{Ass}F$',stack,'The insertion is typed on a separate line starting slightly to the left of soit and ending beyond the base Ass F. No caret or leader chooses an exact verbal attachment point. Its words and the base sequence soit x Ass F are preserved as two spatial levels.','insertmax; xAssF','insertion or placement','high',True)
ch('canceled il existe un voisinag',r'\deleted{il existe un voisinag}',r'\deleted{il existe un voisinag}','The first span has dotted i and the tall l and t under x cancellation. The continuation ends in the descending g loop; no following e lies before the next live si. C table-only doubt is resolved in favor of voisinag.','ilexiste; unvoisinag','other','high')
ch('aucun autre, next line first cell',r'\unsure{Élément|élément}',elem,'The small rounded e with its acute is crossed by a full-height vertical with a left top serif and broad lower foot. Its shape is closer to the adjacent typewriter l than to the separately compared capital E, whose three arms extend right. An l/é overlap is favored; the fused cell remains qualified.','element; elementA; Econtrol; lcontrol','misread word','medium',True)
ch('target i prime of v prime',r"i'\ (F'\ U')",r"\rlap{\(v\)}i'\ (F'\ U')",'A dotted i with vertical stem and lower foot shares a cell with two oblique v legs meeting at the bottom. The raised prime follows both impressions. C retains only i prime.','vprimemap; ivB','misread symbol or index','high',True,True)
ch('canceled alors before réf',r'\deleted{\unsure{alors}}',r'\deleted{alors}','The a bowl, l ascender with top serif, o oval, r shoulder and final s curves can each be followed beneath the cancel x row. C macro and table doubt are resolved.','cancelalors','misread word','high',True)
ch('oblique cancellation scope','Remplaçant through Ass F1 canceled; upper scope uncertain','same represented span; upper scope explicitly uncertain','A thin pale upper extension passes between the opening lines and becomes clearer through the Remplaçant paragraph; the dark continuous stroke descends and bends right through the paragraph, ending just above Bien entendu. The exact semantic upper boundary cannot be inferred from this one stroke. C cancellation is retained with an explicit scope qualification.','diagorigin; diagstartA; diagtop; diagmid; diagbottom','deletion state','medium')
for place,reading,shows,crop in [
 ('typed rulle','rulle','Initial r has a short shoulder and no second vertical stem; the following ulle is clear. C retained slip is confirmed.','rulle'),
 ('En vertu de théorème','En vertu de théorème','The small vowel has a closed upper opening and a horizontal midstroke, giving e. No u is substituted to repair the phrase.','de'),
 ('image inverse dans U','image inverse dans U','The capital has two upper stems joined by a low curved bottom, with no X diagonals or raised prime. C retained slip is confirmed.','inverseU'),
 ('donc le transformé','donc le transformé','The fourth letter is open at the right with no t ascender or crossbar. C donc is confirmed.','donc'),
 ('parenthesis after kernel identity','(re-platitude)','The first two letters are re with a hyphen; all following letters and the closing parenthesis/full stop are visible.','replat'),
 ('right edge of NB line','card Ass','The entire card Ass is visible, followed by a narrow blank paper strip and then the black image edge. No F is visible or supplied.','cardedge')]:
 ch(place,reading,reading,shows,crop)
r.doubt('line1 clipped last cell','supposer','final r only partly visible','medium','suppose clear; two left-serif remnants at the black edge favor r without establishing its complete outline.')
r.doubt('Passant canceled word','au','en','low','Two underlying cells obscured by x strikes.')
r.doubt('overprint in par',r'\rlap{\S}par','par','low','Extra curved strokes suggest section sign over p, but their exact identity remains uncertain.')
r.doubt('first cell of élément',r'\rlap{l}élément','Élément; élément','medium','Lower accented e and full-height l-like stem/serifs; overlap remains qualified.')
r.doubt('oblique cancellation upper scope','Remplaçant through Ass F1','may include opening two lines','medium','Long stroke is dark below and pale/indeterminate at the upper end; not a clear bracket defining a boundary.')
r.notation('blank mathematical slots','blank before standalone primes; blank relations and arrows; blank functor suffixes','12:022 x AssF; AssFprime Xprime_x Uprime; n 1; i:U X; v:F i(F U); vprime map; ui(O_Zi). All preserved as spacing, without symbols supplied.')
r.notation('typed tensor construction',r'\otimes_X: O with x overstrike and lowered X','12:022 transformé par; Ker identity. Both separately enlarged; first heavily retyped, second exposes O and crossed x.')
r.notation('prime versus exclamation',r"H'_i,G'_i,J',X',U',F',v',i'; F'_1; isolated primes",'12:022 every occurrence individually enlarged; raised compact typewriter apostrophes without exclamation dots.')
r.notation('underlined structures',r'\underline{Hom}; \underline O; \underline J; \uline{libre}','12:022 first identity; Spec quotient; bottom ui(O_Zi); libre single continuous rule.')
r.notation('typewriter overlaps',r'O/o; U/a; qualified section-sign/p; qualified l/é; v/i','12:022 opening; affine; par; élément; target of vprime','uncertain')
r.notation('kernel and associated-point indices',r'F_1; F_1 prime; Ass F_1=Ass F-x; Xprime_x','12:022 lowered l-shaped typewriter 1; lower x under Xprime; literal minus before x, no set braces.')
for a,e in [('Ass','associated points / points associés'),('Spec','spectre'),('Hom','homomorphismes'),('Ker','noyau'),('imm can','immersion canonique'),('réf','référence'),('hyp','hypothèse'),('NB','nota bene'),('card','cardinal'),('supp','support'),('prop.','proposition'),('quasi-coh.','quasi-cohérents')]:
 r.r.setdefault('abbreviations',[]).append(dict(abbreviation=a,expansion=e,attestations='12:022'))
r.r['inventory_overrides']={'022-03':dict(hand='another unnamed hand',position='long oblique stroke across first paragraph; upper scope uncertain'),'022-07':dict(position='typed above soit x Ass F; no leader')}
extras=[('opening O/o overlap','text','line1','typewriter'),('U/a overlap','text','voisinage ouvert','typewriter'),('qualified extra mark over p','text','par before 3.3.','another unnamed hand'),('qualified l/é overlap','text','élément','typewriter'),('v/i overlap','text','target of vprime','typewriter'),('empty mathematical slots and isolated primes','text','throughout canceled paragraph and bottom ui term','typewriter'),('libre underline','text','generic flatness sentence','typewriter'),('archive sheet number 21, retained as comment','margin note','bottom-left corner','another unnamed hand')]
for i,(s,t,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='12:022',sheet_kind='cancelled_draft',hand=h,element=f'022-R{i:03d}',kind=t,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=sum([json.loads(Path('work/'+p).read_text()) for p in ['crops12_022.json','fine12_022.json','last12_022.json','de12_022.json']],[])
r.r['inspection_note']='Root alone viewed whole022 and both actual supplied halves before C/H; H has no text for this mapped page, and no H collation rows are created. All6 C macro doubts, all matching doubts/slips/abbreviations rows and all12 C inventory rows were read. All85 crop recipes were actually viewed; unvoisinag/Uopenx from a truncated call were re-viewed before counting them. Every mathematical sign, index, blank formula slot, cancellation, insertion and C doubt was enlarged. No slanted verbal writing occurs; references and typed interlinear insertion were viewed upright. Both supplied halves were reread line by line after the crops. The global oblique cancellation is encoded with deleted; its scope remains qualified in the page comment and doubt record. Archive21 remains comment only. Context remains sealed; no OCR, parallel transcription, audit or mathematical check has occurred.'
r.save('work/record12_022.json')
