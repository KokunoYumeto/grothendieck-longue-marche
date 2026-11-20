from pathlib import Path
import json
root=Path('/workspace/scratch/d27bd2a88bca'); page='C123-02_123_scan023'; work=root/'out'/'work'
meta=json.loads((work/f'{page}_cropmeta.json').read_text())
C=(root/'packets'/page/'C.tex').read_text()
a_old=r'\mathrm{A}_{\deleted{\unsure{\mathrm{n}|\mathrm{r}}}\mathrm{r}}'
d_old=r'\mathrm{D}_{\deleted{\mathrm{n}}\mathrm{r}}'
a_new=r'\mathrm{A}_{\deleted{\unsure{\mathrm{n}|\mathrm{r}}}\unsure{\mathrm{r}|\mathrm{n}}}'
d_new=r'\mathrm{D}_{\deleted{\unsure{\mathrm{n}|\mathrm{r}}}\unsure{\mathrm{r}|\mathrm{n}}}'
old_dim=r'dim\deleted{\unsure{o|e}}ension'
new_dim=r'dim\deleted{\unsure{\$|S}}ension'
old_brie=r'Br\deleted{\unsure{e|i}}i\deleted{\unsure{i|e}}eskorn'
new_brie=r'\unsure{Br\deleted{e}i\deleted{i}eskorn|Br\deleted{i}e\deleted{e}iskorn}'
tex=r'\cotefile{123}'+'\n'+C
tex=tex.replace('analogous','analoguous').replace('characteristic','caracteristic')
tex=tex.replace(r'\inserted{\handwritten{n-}}',r'\inserted{\mathrm{n}-}')
tex=tex.replace(a_old,a_new).replace(d_old,d_new).replace(old_dim,new_dim).replace(old_brie,new_brie)
tex += '% Isolated non-text vertical mark below the signature; no character reading assigned.\n'
(work/f'{page}_draft.tex').write_text(tex)

changes=[]
def ch(id,line,c,h,final,scan_shows,b,confidence='high',kind='other',changed_C=False,changed_H=True,marked_in_H=False,consequential=False,certainty_only=False):
    changes.append(dict(id=id,line=line,c=c,h=h,final=final,scan_shows=scan_shows,crop=meta[b]['crop'],box=meta[b]['box'],confidence=confidence,kind=kind,changed_C=changed_C,changed_H=changed_H,marked_in_H=marked_in_H,consequential=consequential,certainty_only=certainty_only))
ch('r01','L02',r'be\handwritten{\raisebox{.6ex}{$\vert$}}interesting','be interesting',r'be\handwritten{\raisebox{.6ex}{$\vert$}}interesting',"After 'it would', be and interesting have no typed separating space. A thin pen stroke rises vertically above the join near the e. C's raised bar preserves it; H silently supplies normal word spacing and omits the stroke.",'b01',kind='omission')
ch('r02','L03',r'\underline{\mathrm{g}}\handwritten{\longrightarrow}\underline{\mathrm{h}}/\mathrm{W}, where \underline{\mathrm{g}}',r'\mathfrak{g}\to\mathfrak{h}/W, where \mathfrak{g}',r'\underline{\mathrm{g}}\handwritten{\longrightarrow}\underline{\mathrm{h}}/\mathrm{W}, where \underline{\mathrm{g}}',"In 'the canonical morphism …, where …', both g letters and h are ordinary typewritten lower-case characters with separate short underlines. None has the strokes of a handwritten fraktur letter. The single-shaft arrow is supplied in pen.",'b02',kind='misread symbol or index',consequential=True)
ch('r03','L04',r'\underline{\mathrm{h}} a Cartan subalgebra',r'\mathfrak{h} a Cartan subalgebra',r'\underline{\mathrm{h}} a Cartan subalgebra',"The line begins with ordinary typed h over a short horizontal underline, before 'a Cartan subalgebra'. H substitutes a fraktur alphabet.",'b03',kind='misread symbol or index',consequential=True)
ch('r04','L04',r'G on \underline{\mathrm{g}}',r'G on \mathfrak{g}',r'G on \underline{\mathrm{g}}',"In 'the orbits of G on …, and the analoguous', g has two ordinary typewriter bowls and a separate underline. It is not a fraktur character.",'b04',kind='misread symbol or index',consequential=True)
ch('r05','L04','analogous','analoguous','analoguous',"After 'and the', the typewriter gives a-n-a-l-o-g-u-o-u-s, with a distinct u immediately following g. The source spelling analoguous is retained.",'b04',kind='misread word',changed_C=True,changed_H=False)
ch('r06','L07',r'\deleted{\unsure{applicati}} map','map',r'\deleted{\unsure{applicati}} map',"Between 'of this' and 'map ?', an unfinished nine-position fragment is cancelled by typed x characters. Its beginning appli and final dotted position remain visible, but the central/final strokes are not all separable. C's applicati remains doubtful and is not completed to application.",'b06',confidence='low',kind='omission')
ch('r07','L07',r'believe that \deleted{this}','believe that',r'believe that \deleted{this}',"At the right end of 'There are some reasons to believe that', the cancelled word this retains t, h, dotted i and s. The final extra x belongs to the cancellation, not to an additional source word.",'b07',kind='omission')
ch('r08','L08',r'\inserted{\handwritten{n-}}\mathrm r-2',r'n-r-2',r'\inserted{\mathrm n-}\mathrm r-2',"The original line has r-2 after 'dimension'. The separate n- is placed above it, with a curved pen hook attaching before r. The n and dash have typewriter forms; the handwritten placement stroke is distinct. H merges the insertion into the line, while its editorial note acknowledges it.",'b08',kind='insertion or placement',marked_in_H=True,consequential=True)
ch('r09','L08',r'\deleted{the next lower after}\inserted{the next lower after}','the next lower after',r'\deleted{the next lower after}\inserted{the next lower after}',"After '(just', the phrase the next lower after appears twice: the upper typed instance is cancelled with x overstrikes, and the lower typed instance is live. All four cancelled words remain readable. H retains only the live wording.",'b09',kind='omission')
ch('r10','L10',a_old,r'A_{\uncertain{n}}',a_new,"In the diagram-family list, A's lowered character contains superposed n/r-like strokes. The r head, n-like right side and doubled foot do not establish a unique order of strikes. Both layers remain marked uncertain; r is not selected because it denotes rank nearby.",'b10',confidence='low',kind='deletion state (struck given live or live given struck)',marked_in_H=True,consequential=True)
ch('r11','L10',d_old,r'D_{\uncertain{n}}',d_new,"D's lowered character is also composite, with a dark right-hand foot and superposed upper strokes. A single n loses the correction state; assigning either layer conclusively would exceed what the crop shows. The whole A,D,E6,E7,E8 formula was inspected together.",'b10',confidence='low',kind='deletion state (struck given live or live given struck)',marked_in_H=True,consequential=True)
ch('r12','L11',r'in \inserted{\handwritten{all}} other cases','in all other cases',r'in \inserted{\handwritten{all}} other cases',"Between the diagram list and the line 'in other cases', the handwritten word all has an a and two tall l strokes. Its curved placement hook points before other. H gives the word inline and identifies the addition only in an editorial note.",'b10',kind='insertion or placement',marked_in_H=True)
ch('r13','L13','characteristic','caracteristic','caracteristic',"In 'this property will be … of the', the word begins c-a-r, with no h between c and a. The source spelling caracteristic is clear.",'b11',kind='misread word',changed_C=True,changed_H=False)
ch('r14','L13',r'homogene\deleted{\unsure{a|u}}ous','homogeneous',r'homogene\deleted{\unsure{a|u}}ous',"Inside the quoted word, an extra character after homogene is crossed with x before ous. Its rounded lower part and upright allow a or u; the cancellation prevents a secure choice. H drops the cancelled letter.",'b12',confidence='medium',kind='omission')
ch('r15','L13',"``homogene…ous''",'« homogeneous »',r"``homogene\deleted{\unsure{a|u}}ous''","The quoted term has two upright typed strokes at each end, not angle-shaped guillemets. The cancelled internal letter is recorded separately in r14.",'b12',kind='other')
ch('r16','L14',old_dim,'dimension',new_dim,"In 'the … of the set', the live e follows dim. The underlying character extends above the e with an S-like curved top and below it with two short prongs. These strokes suggest a dollar-sign-like or capital-S character, rather than C's o/e alternatives. The underlying character remains doubtful; its existence is not suppressed.",'b13',confidence='low',kind='misread word',changed_C=True)
ch('r17','L16',r'\mathrm x\handwritten{\in}\underline{\mathrm g}',r'x\in\mathfrak g',r'\mathrm x\handwritten{\in}\underline{\mathrm g}',"After 'contains a given element', the membership sign is handwritten, but g is typewritten with a separate underline. The whole x∈g expression and following question mark were inspected.",'b15',kind='misread symbol or index',consequential=True)
ch('r18','L19',old_brie,'Brieskorn',new_brie,"After 'a depth argument of', both adjacent positions following Br contain e/i features: rounded/barred forms and upright stems, with a clear dot over the first composite. The probable ei→ie correction is not conclusively ordered by the ink; the two possible pair orders are retained. H gives only the regular name.",'b17',confidence='medium',kind='deletion state (struck given live or live given struck)')
ch('r19','L20',r'\underline{\mathrm g}\handwritten{\longrightarrow}\underline{\mathrm h}/\mathrm W',r'\mathfrak g\to\mathfrak h/W',r'\underline{\mathrm g}\handwritten{\longrightarrow}\underline{\mathrm h}/\mathrm W',"In 'the fibers of your map', g and h again have ordinary typed forms and separate underlines. The pen arrow has one shaft and a right arrowhead. H substitutes fraktur letters.",'b18',kind='misread symbol or index',consequential=True)
ch('r20','L21',"``rational''",'« rational »',"``rational''","After 'are', rational is enclosed by two upright typewriter quote strokes on each side. The comma following the closing pair remains live.",'b20',kind='other')
ch('r21','L22',r'i\deleted{s}f','if',r'i\deleted{s}f',"After i.e., the second letter position contains the lower curves of s beneath the ascender, crossbar and stem of f. The underlying s remains visible, so simple if omits the correction state.",'b21',kind='deletion state (struck given live or live given struck)')
ch('r22','L23',r't\deleted{e}h\deleted{h}en','then',r't\deleted{e}h\deleted{h}en',"Before the R formula, the two middle positions of then retain both e loops and h stems. The underlying e/h transposition is retained as in C, instead of suppressing the earlier letters.",'b23',kind='deletion state (struck given live or live given struck)')
ch('r23','L23',r'\underline{\mathrm O}_{\mathrm F\prime}',r'\mathcal O_{F\prime}',r'\underline{\mathrm O}_{\mathrm F\prime}',"Inside the higher-direct-image formula, O is an ordinary upright typed ring with a separate short underline. It is not a calligraphic O. The F-prime index is below it; the separate cancelled upper mark is r24.",'b23',kind='misread symbol or index',consequential=True)
ch('r24','L23',r'\underline{\mathrm O}_{\mathrm F\prime}^{\deleted{\unsure{\mathrm t|*}}}',r'\mathcal O_{F\prime}',r'\underline{\mathrm O}_{\mathrm F\prime}^{\deleted{\unsure{\mathrm t|*}}}',"Above the live lower F-prime index, a small cancelled mark has upper prongs, a central upright and a horizontal stroke. The strike obscures whether the earlier character was t or *. C's doubt remains; H omits the cancelled upper position.",'b23',confidence='low',kind='omission',consequential=True)
ch('r25','L23',r'\deleted{\unsure{ot|to}}\handwritten{to}','to',r'\deleted{\unsure{ot|to}}\handwritten{to}',"After 'the answer', handwritten t and o visibly cover two earlier typed positions. The earlier sequence is compatible with ot, but the pen crosses prevent ruling out to. Both layers remain, with the earlier order explicitly doubtful.",'b24',confidence='medium',kind='deletion state (struck given live or live given struck)')
ch('r26','S01',r'\handwritten{A\,\unsure{Grothendieck}}',r'A.~Grothendieck',r'\handwritten{A\,\unsure{Grothendieck}}',"The signature begins with a distinct A whose cross stroke touches the following large G. No full stop follows A. The later name strokes are compressed; Grothendieck remains C's doubtful reading, not a newly resolved name.",'b25',kind='text not on the page')

# Every line and every separately visible state is inventoried in page order.
inv=[]
def item(kind,pos,first,hand='typewriter body with pen mathematical additions and corrections'):
    inv.append(dict(scan='23',sheet_kind='typescript',hand=hand,element=f'i{len(inv)+1:02}',kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
line_text=[
('L01',"are isomorphic to subgroups of the group of exterior automorphisms of G) ?"),
('L02',"In a different direction, it would beinteresting to know more about"),
('L03',r'the canonical morphism $\underline g\to\underline h/W$, where $\underline g$ is the Lie algebra of $G$ and'),
('L04',r'$\underline h$ a Cartan subalgebra, and of the orbits of $G$ on $\underline g$, and the analoguous'),
('L05',r'morphism of Steinberg $G\to T/W$ and the orbits of $G$ acting on itself. Do'),
('L06',r'you know for instance exactly how varies the rank (= rang of the tangent'),
('L07',r'map) of this … map ? There are some reasons to believe that …'),
('L08',r'for points of unipotent orbits of dimension $r-2$ (just …'),
('L09',r'the maximal dimension $n-r$), the rank is $r-1$ in case all roots have same'),
('L10',r'length (that is the corresponding diagrams $A,D,E_6,E_7,E_8$ are those corres-'),
('L11',r'ponding to Klein singularities), and $<r-1$ in … other cases; in the first'),
('L12',r'case, I would expect that there is just one orbit as stated, by the way,'),
('L13',r'and maybe this property will be caracteristic of the ``homogene…ous\'\' case'),
('L14',r'when all roots have same length. Also, what can be said of the dim…ension of'),
('L15',r'the set of all Borel subgroups containing a given element $g\in G$, resp.'),
('L16',r'whose Lie algebra contains a given element $x\in\underline g$ ? If $2N=n-r$ is the number'),
('L17',r'of roots and if the dimension of the orbit of the given element is $2N-2i$,'),
('L18',r'I would expect the dimension of the previous variety to be equal to $i$; the'),
('L19',r'inequality $\leqslant i$ would imply, by generalizing a depth argument of Br…skorn,'),
('L20',r"that the singularities of the fibers of your map $\underline g\to\underline h/W$ (resp. Steinberg's"),
('L21',r'$G\to T/W$ in case $G$ is simply connected instead of adjoint) are ``rational\'\','),
('L22',r"i.e. if $F$ is such a fiber and $F'\overset f\longrightarrow F$ a resolution of singularities of $F$,"),
('L23',r"then $R^if_*(\underline O_{F'}^{\deleted{\unsure{t|*}}})=0$ for $i>0$. Maybe the answer … most of the questions I am"),
('L24',r'asking are well known and I am just ignorant; for some of them, it would'),
('L25',r'indeed be scandalous that the experts do not know the answer ! In any case,'),
('L26',r'I would be grateful for any comment you would have on any of my questions.'),
('L27',r'Sincerely yours')]
states={
'L02':[('insertion','Above beinteresting',r'\handwritten{\raisebox{.6ex}{$\vert$}}','single pen separator stroke')],
'L03':[('insertion','Between typed g and h/W',r'\handwritten{\longrightarrow}','handwritten arrow')],
'L05':[('insertion','Between typed G and T/W',r'\handwritten{\longrightarrow}','handwritten arrow')],
'L07':[('deletion','Before map',r'\deleted{\unsure{applicati}}','typewritten cancelled fragment'),('deletion','After believe that',r'\deleted{this}','typewritten word cancelled with x overstrikes')],
'L08':[('insertion','Above r-2',r'\inserted{\mathrm n-}','typewritten insertion with handwritten placement hook'),('deletion','After just, upper instance',r'\deleted{the next lower after}','typewritten phrase cancelled with x overstrikes'),('insertion','After just, lower instance',r'\inserted{the next lower after}','typewritten replacement on a lowered baseline')],
'L10':[('deletion','Subscript of A',a_new,'typewriter n/r overstrikes'),('deletion','Subscript of D',d_new,'typewriter n/r overstrikes'),('insertion','Indices of E',r'\handwritten{6},\handwritten{7},\handwritten{8}','pen numerals')],
'L11':[('insertion','Before r-1',r'\handwritten{<}','handwritten inequality sign'),('insertion','Above other, with curved placement hook',r'\inserted{\handwritten{all}}','handwritten word')],
'L13':[('deletion','After homogene',r'\deleted{\unsure{a|u}}','extra typewritten letter cancelled with x')],
'L14':[('deletion','Inside dimension',new_dim,'typewriter correction; underlying curved character uncertain')],
'L15':[('insertion','Between g and G',r'\handwritten{\in}','handwritten membership sign')],
'L16':[('insertion','Between x and underlined g',r'\handwritten{\in}','handwritten membership sign')],
'L19':[('insertion','After inequality',r'\handwritten{\leqslant}','handwritten sign'),('deletion','In Brieskorn',new_brie,'typewriter e/i overstrikes')],
'L20':[('insertion','Between underlined g and h/W',r'\handwritten{\longrightarrow}','handwritten arrow')],
'L21':[('insertion','Between G and T/W',r'\handwritten{\longrightarrow}','handwritten arrow')],
'L22':[('deletion','In if',r'i\deleted{s}f','typewriter correction'),('insertion','From F-prime to F, below typed f label',r"\mathrm F'\overset{\mathrm f}{\handwritten{\longrightarrow}}\mathrm F",'handwritten arrow with typewritten objects and label')],
'L23':[('deletion','In then',r't\deleted{e}h\deleted{h}en','typewriter transposition correction'),('insertion','Subscript of f',r'\handwritten{*}','handwritten star'),('deletion','Above O subscript',r'\deleted{\unsure{\mathrm t|*}}','cancelled small typed upper mark'),('insertion','Between i and zero',r'\handwritten{>}','handwritten inequality sign'),('deletion','After answer',r'\deleted{\unsure{ot|to}}','overwritten typed positions'),('insertion','Over the preceding typed positions',r'\handwritten{to}','handwritten replacement')]
}
for l,t in line_text:
    item('text',l,t)
    for kind,pos,first,hand in states.get(l,[]): item(kind,l+', '+pos,first,hand)
item('text','S01, below closing at lower right',r'\handwritten{A\,\unsure{Grothendieck}}','handwritten signature')
item('margin note','Below signature, lower centre','% isolated non-text vertical mark; no character reading assigned','unattributed isolated mark; not identified as writing')
item('margin note','Lower left corner','% archive sheet number: 22','archive pencil foliation')

boxes=[]
def bx(id,kind,b,reading,xy=None):
    z=xy or meta[b]['box']; boxes.append(dict(box=id,kind=kind,x0=z[0],y0=z[1],x1=z[2],y1=z[3],reading=reading))
bx('s01','handwritten separator and joined words','b01',r'be\handwritten{\raisebox{.6ex}{$\vert$}}interesting',[964,182,1226,250])
bx('s02','whole formula and repeated underlined letter','b02',r'$\underline{\mathrm g}\handwritten{\longrightarrow}\underline{\mathrm h}/\mathrm W$, where $\underline{\mathrm g}$')
bx('s03','underlined letter','b03',r'$\underline{\mathrm h}$ a Cartan',[220,329,480,382])
bx('s04','underlined letter and differing word','b04',r'on $\underline{\mathrm g}$, and the analoguous')
bx('s05','whole formula with handwritten arrow','b05',r'$\mathrm G\handwritten{\longrightarrow}\mathrm T/\mathrm W$')
bx('s06','cancelled word','b06',r'this \deleted{\unsure{applicati}} map')
bx('s07','cancelled word','b07',r'that \deleted{this}')
bx('s08','whole formula with insertion','b08',r'dimension $\inserted{\mathrm n-}\mathrm r-2$')
bx('s09','cancelled and inserted phrase','b09',r'(just \deleted{the next lower after}\inserted{the next lower after}')
bx('s10','whole doubtful formula, pen numerals and insertion','b10',r'$'+a_new+','+d_new+r',\mathrm E_{\handwritten6},\mathrm E_{\handwritten7},\mathrm E_{\handwritten8}}$; $\handwritten{<}\mathrm r-1$ in \inserted{\handwritten{all}} other cases;')
bx('s11','differing word','b11','be caracteristic',[766,924,1071,983])
bx('s12','whole word with cancelled character','b12',r"``homogene\deleted{\unsure{a|u}}ous'' case")
bx('s13','overtyped character','b13','the '+new_dim+' of')
bx('s14','whole formula with handwritten sign','b14',r'$\mathrm g\handwritten{\in}\mathrm G$,',[1294,1063,1404,1118])
bx('s15','whole formula with handwritten sign','b15',r'$\mathrm x\handwritten{\in}\underline{\mathrm g}$ ?')
bx('s16','whole inequality','b16',r'inequality $\handwritten{\leqslant}\mathrm i$')
bx('s17','overtyped name','b17','of '+new_brie+',')
bx('s18','whole formula with handwritten arrow','b18',r'$\underline{\mathrm g}\handwritten{\longrightarrow}\underline{\mathrm h}/\mathrm W$')
bx('s19','whole formula with handwritten arrow','b19',r'$\mathrm G\handwritten{\longrightarrow}\mathrm T/\mathrm W$',[215,1458,359,1517])
bx('s20','quotation marks','b20',"are ``rational'',")
bx('s21','overtyped word','b21',r'i.e. i\deleted{s}f $\mathrm F$',[211,1520,425,1585])
bx('s22','whole labelled arrow','b22',r"$\mathrm F'\overset{\mathrm f}{\handwritten{\longrightarrow}}\mathrm F$")
bx('s23','whole doubtful formula and overtyped word','b23',r"t\deleted{e}h\deleted{h}en $\mathrm R^{\mathrm i}\mathrm f_{\handwritten{*}}(\underline{\mathrm O}_{\mathrm F'}^{\deleted{\unsure{\mathrm t|*}}})=0$ for $\mathrm i\handwritten{>}0$.")
bx('s24','overwritten words','b24',r'answer \deleted{\unsure{ot|to}}\handwritten{to}',[932,1588,1127,1658])
bx('s25','handwritten signature','b25',r'\handwritten{A\,\unsure{Grothendieck}}')
bx('s26','archive pencil number','b26','% archive sheet number: 22')
bx('s27','isolated non-text mark','b27','% isolated broken vertical mark; no character reading assigned')

report=dict(page=page,line_count=27,changes=changes,
 doubts=[
 dict(line='L07',reading=r'\deleted{\unsure{applicati}}',alternatives=[],confidence='low',reason='The cancelled nine-position fragment has visible appli and a final dotted position, but not every intervening letter can be separated from typed x strokes. It is not expanded to application.'),
 dict(line='L10',reading=a_new+', '+d_new,alternatives=[r'\deleted{n}r',r'\deleted{r}n',r'\deleted{n}n',r'\deleted{r}r'],confidence='low',reason='Both lowered characters are visibly composite. The layers and chronology remain uncertain; nearby rank notation is not evidence to override their strokes.'),
 dict(line='L13',reading=r'\deleted{\unsure{a|u}}',alternatives=['a','u'],confidence='medium',reason='The cancelled extra rounded character in homogene…ous permits a or u. Its x strike prevents resolution.'),
 dict(line='L14',reading=new_dim,alternatives=[r'dim\deleted{\$}ension',r'dim\deleted{S}ension'],confidence='low',reason='The curved underlying character rises above the live e and leaves two short strokes below its baseline. Dollar-sign-like and capital-S readings are offered provisionally; C’s lower-case o/e alternatives do not account well for those projections.'),
 dict(line='L19',reading=new_brie,alternatives=[r'Br\deleted{e}i\deleted{i}eskorn',r'Br\deleted{i}e\deleted{e}iskorn'],confidence='medium',reason='The first two post-Br positions have e/i composites. The letter pairs are visible but the chronology remains uncertain; the familiar surname does not remove that uncertainty.'),
 dict(line='L23',reading=r'\deleted{\unsure{\mathrm t|*}}',alternatives=['t','*'],confidence='low',reason='The small cancelled upper character in the O expression has surviving prongs and a bar. Cancellation prevents deciding the original sign. The whole vanishing formula was inspected.'),
 dict(line='L23',reading=r'\deleted{\unsure{ot|to}}\handwritten{to}',alternatives=['ot','to'],confidence='medium',reason='The live handwritten to is clear. Earlier typewriter curves and uprights are obscured by it, so ot/to remains unresolved.'),
 dict(line='S01',reading=r'A\,\unsure{Grothendieck}',alternatives=[],confidence='medium',reason='A and G are distinct. The middle and terminal name strokes are compressed enough that the whole name is not resolved from the crop alone.'),
 dict(line='L23',reading='answer',alternatives=[],confidence='low',reason='Additional overtyped-looking strokes occur in the w/e area: an interior curved/barred form at w and a short high upright at e. Both witnesses give answer. The earlier letters remain an open audit question pending root adjudication; no speculative earlier word has been supplied.'),
 ], inventory=inv,
 notes=[
 'Only this page packet and the shared conventions, errors and preamble were consulted. Whole image and both supplied halves were each viewed once; the halves were read line by line against both C and H.',
 'All 27 saved evidence crops were displayed. b24 was extended leftward to include the full newly noticed answer overtyping region. No OCR, text-recognition library, web source, other-page output or TeX compilation was used.',
 'Evidence crop metadata preserves original full-image coordinates. Crops are LANCZOS-enlarged to a 2500-pixel long edge, autocontrasted with cutoff 0.4 and lightly sharpened. There is no slanted marginal prose on this sheet requiring rotation.',
 'The s-series boxes are neutral targets for the next blind audit. They cover every insertion, cancellation, overtype, handwritten sign, pen numeral, signature and whole doubtful formula. Their readings describe complete target contents; clipped incidental context at a crop edge is not invented as new source text.',
 'The inserted n- appears typewritten, with serifs matching the text and a straight typewriter dash; only its attachment hook is handwritten. Removing C’s handwritten wrapper is a non-counted wrapper distinction. The insertion itself and H’s merged placement are recorded.',
 'Additional certainty marks in the A/D composite indices and the paired interpretation of the Brieskorn overtypes do not claim a newly deciphered letter. They make the existing ordering uncertainty explicit; their substantive H differences are the retained correction layers.',
 'The source’s ordinary typed g, h and O with short separate underlines are retained. H’s substitutions of fraktur g/h and calligraphic O are alphabet changes, not merely equivalent handwriting wrappers.',
 'The first line is a continuation of a question. No opening salutation, recipient, date or preceding content is reconstructed. The source line-end corres-/ponding is joined in the candidate; paragraphing and the closing/signature lines are preserved.',
 'The English forms analoguous, caracteristic, how varies and rang remain as typed. The number agreement in the answer … are well known remains. The cancelled homogene[a/u]ous character and the is→if and tehn→then correction states are not silently regularized.',
 'H’s explanatory note and the following French section heading about Diagrammes d’espaces homogènes refer beyond this letter leaf and are not ink on this scan. They are excluded from the page without importing or inspecting another leaf.',
 'The short broken vertical mark below the signature has no securely recognizable numeral or letter. It is logged as a non-text mark, with a candidate comment and audit box, rather than interpreted as page numbering.',
 'No local proof or calculation was performed. The author’s explicit expectations and questions are recorded as such. Formula inspections were visual transcription audits, not mathematical checks.'
 ],
 reading_notes=[
 'This leaf continues and closes an English letter. Its opening line ends a question about subgroups of exterior automorphism groups. The main paragraph asks about the canonical map from the Lie algebra to the Cartan quotient, Steinberg’s analogous group map, and their ranks and orbits.',
 'The author says there are reasons to believe that along unipotent orbits of dimension n−r−2 the rank is r−1 when all roots have equal length and smaller in the remaining cases. He further says “I would expect” uniqueness of the indicated orbit and wonders whether this characterizes the equal-root-length case. These remain proposed assertions and questions, not verified conclusions.',
 'He asks for the dimension of the variety of Borel subgroups containing a given group element, or whose Lie algebra contains a given Lie-algebra element. For an orbit of dimension 2N−2i, he writes that he would expect the variety to have dimension i. He says the inequality ≤i would imply rationality of the fibers by generalizing a depth argument attributed to Brieskorn.',
 'The source explains the proposed rationality conclusion by a higher-direct-image vanishing formula for a resolution F′→F. The formula’s small cancelled upper character remains uncertain and is preserved. No proof of the rank, orbit, dimension or rationality expectations was attempted here.',
 'The closing paragraph explicitly allows that many answers may already be known and that the writer may simply be ignorant. He asks for comments on any of his questions and closes “Sincerely yours”, followed by a handwritten A and a compressed name read tentatively as Grothendieck.',
 'Preserved source irregularities include joined beinteresting with a pen separator, analoguous, caracteristic, how varies, rang, number agreement in the answer … are, cancelled extra letters and several overtyped corrections. The two diagram indices and several cancelled or overwritten letters remain doubtful.',
 'One annotated typescript sheet is present: 26 body lines, a separate closing line and a handwritten signature. No title, date, original text page number or total page count is visible. Archive folio 22 is pencilled at the lower left. No mathematical diagram or drawing appears.'
 ],
 check_events=[dict(statement_id='123/023-background-maps-and-definition',type='carried as background without fault found',outcome='The named canonical and Steinberg quotient maps, and the source’s explanation of rationality through higher-direct-image vanishing, are carried as background only. No independent proof, calculation or mathematical verification was performed. The rank, uniqueness, dimension and rationality expectations, and all textual slips, are excluded from a checked status.')],
 visual_audit_events=[
 dict(statement_id='123/023-layout',type='visual transcription audit',outcome='Whole-page layout and both halves read; 27 typed lines including closing, signature, inserted material, cancellations and archive foliation inventoried.'),
 dict(statement_id='123/023-word-disagreements',type='visual transcription audit',outcome='The two differing live spellings were read letter by letter on b04 and b11. All cancellation-related word differences received displayed crops.'),
 dict(statement_id='123/023-formulas',type='visual transcription audit',outcome='Typed underlines, arrows, membership signs, E indices, n/r overtypes and the entire R formula inspected visually. No mathematical proof is implied.'),
 dict(statement_id='123/023-state-audit',type='visual transcription audit',outcome='Every visible insertion, cancelled span and overtyped place was checked on its saved crop. Ambiguous old letters and strike order remain explicit.'),
 dict(statement_id='123/023-signature-and-marks',type='visual transcription audit',outcome='Signature, archive numeral 22 and isolated lower vertical mark were inspected. The name doubt remains and no digit is inferred from the isolated mark.')
 ],
 notation=[
 '123/023: The Lie-algebra letters g and h are ordinary typewritten lower-case letters with separate short underlines, not fraktur. This holds at every occurrence inspected on this sheet.',
 '123/023: The structure-sheaf symbol is an ordinary typed O with a separate underline. The live F-prime index is below it; a cancelled t/*-like character occupies an upper position.',
 '123/023: Handwritten arrows have single horizontal shafts and ordinary right arrowheads. The resolution arrow has a typed f above it; the prime on F is a typed single stroke.',
 '123/023: The E indices are handwritten 6, 7 and 8. The A and D subscript n/r layers and their order remain uncertain; rank notation does not decide them.',
 '123/023: The handwritten weak inequality has a lower oblique stroke and is represented by leqslant. The other inequality signs are < and >. Membership signs have a curved left side and a short middle bar.',
 '123/023: Keep the source abbreviations resp. and i.e., and its paired upright double quotation marks. No guillemets are drawn.',
 '123/023: The inserted n- is typewritten and placed by a pen hook. The added all and overwritten to are handwritten.'
 ],
 hand_log=[
 '123/023: The pen membership sign has a faint upper curved arm and a stronger lower curve, but a distinct central bar. Both occurrences were inspected and read ∈.',
 '123/023: The handwritten all is small and pale, with two narrow tall l strokes; its insertion hook attaches before other. It is not a continuation of the crowded D subscript above it.',
 '123/023: The typewriter n/r subscript overprints are strongly squared and doubled. Their components and order remain uncertain at both A and D; nearby mathematical rank notation was not substituted for the ink.',
 '123/023: Several typewriter corrections retain two letters in one cell. The extra letter in homogeneous, the curved glyph in dimension and the e/i pair in Brieskorn require state-specific doubts rather than a silently regularized familiar word.',
 '123/023: Signature A and capital G are clear, while the middle and final surname strokes are compressed. The doubtful Grothendieck reading is retained; no punctuation after the initial A is supplied.'
 ],boxes=boxes,
 metadata=dict(full_image_size=[1687,2154],line_count_basis='27 typewritten lines: 26 body lines and closing; signature and interlinear additions counted separately',crop_transforms=meta,source_reading_status='first-reader candidate for parent adjudication; not a committed page'))
def clean(o):
    if isinstance(o,str): return o.replace("\\'", "'")
    if isinstance(o,list): return [clean(v) for v in o]
    if isinstance(o,dict): return {k:clean(v) for k,v in o.items()}
    return o
report=clean(report)
(work/f'{page}_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'draft':str(work/f'{page}_draft.tex'),'report':str(work/f'{page}_report.json'),'changes':len(changes),'inventory':len(inv),'doubts':len(report['doubts']),'boxes':len(boxes)},ensure_ascii=False))
