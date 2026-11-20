from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B12-01',12,83,'cancelled_draft');H='[No H text supplied.]'
def ch(place,C,final,shows,crop,kind='other',confidence='high',against_C=False,consequential=False):
 r.change(place,C,H,final,shows,crop,kind,confidence,against_C,False,False,consequential)
cop=r'\text{\unsure{\rlap{p}c}\unsure{\rlap{r}o}p\rlap{f}rof}'
r.edit(r'\operatorname{copfof}',cop)
r.edit("ou ``intègre''",r"ou ``in\rlap{è}tègre''")
r.edit('argument qui est un anneau','argument qui e st un anneau')
noeth=r'noe\rlap{h}t\unsure{\rlap{t}h|h}érien'
r.edit(r'\unsure{noehhérien|noethérien}',noeth)
r.edit(r'On suppose\deleted{\unsure{r|x}}',r'On suppose\deleted{\unsure{x|r}}')
local=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {$\text{\unsure{\rlap{C}B|B}}^{\deleted{\unsure{x|'}}}$};
\node[anchor=south,inner sep=0,yshift=.12cm] at (base.north) {\inserted{local}};
\end{tikzpicture}}'''
r.edit(r"\inserted{local} $B^{\deleted{\unsure{'|x}}}$",local)
arc=r'''\mbox{\begin{tikzpicture}[baseline=(word.base)]
\node[inner sep=0] (word) {universellement};
% Thin shallow curved trace below the first half; no textual value or origin assigned.
\draw[line width=.3pt,opacity=.6] ([xshift=.30cm,yshift=-.13cm]word.south west) .. controls ([xshift=.65cm,yshift=-.32cm]word.south west) and ([xshift=1.25cm,yshift=-.35cm]word.south west) .. ([xshift=1.65cm,yshift=-.31cm]word.south west);
\end{tikzpicture}}'''
r.edit('universellement japonais',arc+' japonais')
insert=r'''\mbox{\begin{tikzpicture}[baseline=(left.base)]
\node[inner sep=0] (left) {Soit $k$ le corps résiduel de $A$,};
\node[anchor=base west,inner sep=0,xshift=.25cm] (right) at (left.base east) {Supposons $B$ plat sur $A$ et que};
\node[anchor=south west,inner sep=0,xshift=1.5cm,yshift=.15cm] (added) at (left.north west) {\inserted{et supposons le corps résiduel de $B$ fini sur celui de $A$.}};
\path (added.south west) -- coordinate[pos=.39] (bend) (added.south east);
\draw ([xshift=.05cm,yshift=-.03cm]left.south east) -- ([yshift=-.04cm]bend) -- ([yshift=-.04cm]added.south east) .. controls ([xshift=.09cm,yshift=-.04cm]added.south east) and ([xshift=.13cm,yshift=.01cm]added.south east) .. ([xshift=.13cm,yshift=.07cm]added.south east);
\end{tikzpicture}}'''
r.edit(r'Soit $k$ le corps résiduel de $A$, \inserted{et supposons le corps résiduel de $B$ fini sur celui de $A$.} Supposons $B$ plat sur $A$ et que',insert)
r.edit('Alors toutes les fibres',r'\rlap{a}Alors toutes les fibres')
r.edit('reformuler',r'ref\unsure{\rlap{r}o}rmuler')
ch('introduction, first quoted condition',r'\operatorname{copfof}',cop,'The fourth cell has the tall f hook/crossbar plus a separate lower r shoulder and terminal knob, unlike the simple final f. The first cell has a c curve plus a left serif, residual descending stem and foot compatible with p; the second has an o loop plus a left serif/inner stroke compatible with r. Those first two superpositions remain qualified. The third p descender/foot is clear, while the global diagonal crosses its right edge. No underlying whole word or typing chronology is inferred.','copfof;copfirst;copfourth;firstc;secondo;fourthfr;finalf;pccontrol;thirdp','misread word','medium',True,True)
ch('introduction, quoted intègre','intègre',r'in\rlap{è}tègre','The third cell contains a t stem and crossbar together with a full e middle/lower bowl and a grave above. The following è is a separate cell with its own grave. The plain t control lacks the extra left curve and middle bar. Both overlapping impressions are preserved without chronology.','intègre;integret;intgrave;toutt','misread word','high',True)
ch('theorem, argument qui est','qui est','qui e st','An entire typing space separates e from st; the preceding qui and following un are separately spaced. The internal gap is retained.','estspace','other','high',True)
ch('theorem, second noetherian adjective',r'\unsure{noehhérien|noethérien}',noeth,'The first e has no acute. In the next cell an h left ascender/serif and arch overlap a centered t ascender/crossbar. The following h has an additional central upper stroke and lower impression compatible with t, but a doubled or displaced impression cannot be excluded. The word-level C doubt is narrowed to that second overprinted cell; the final é, r, i, e, n are legible.','noethsecond;noethh1;noethh2;noethhcontrol','misread word','medium',True)
ch('theorem, after On suppose',r'\deleted{\unsure{r|x}}',r'\deleted{\unsure{x|r}}','The visible form has the two crossing diagonals and broad top/bottom feet of the x cancel. Its heavy upper-right part could include an r shoulder, but the underlying letter cannot be separated. The visible x is placed first and the r alternative is retained.','supposer;supposex;xcontrol','misread word','low',True)
ch('condition a, raised local and base letter',r"\inserted{local} $B^{\deleted{\unsure{'|x}}}$",local,'local is centered above the B and raised cancel cell, rather than preceding B on the baseline. Two B bowls are secure. A second continuous convex curve left of its vertical and extra upper/bottom ink are compatible with an overlapping C, but may be a displaced impression, so that component is qualified. The raised mark has x diagonals/feet; no separate prime can be isolated. Both levels, the qualified B/C superposition and the x/prime doubt are retained.','localinsert;Bprime;Bletter;Bcancel;Bcontrol;Ccontrol','insertion or placement','medium',True,True)
ch('after suivantes',r'\deleted{\unsure{x}}',r'\deleted{\unsure{x}}','A heavy x-shaped cell follows the final s, with fused interior ink. Its original content remains unrecoverable; the small right-hand spot cannot securely be separated from the overprinted foot. C macro/table doubt is retained.','suivantes;suivantesx','other','low')
ch('below universellement','[not represented]',arc,'A faint shallow curved trace descends from left to right and flattens beneath the first half of universellement. It is distinct from the steep black global cancellation nearby. The shape is drawn; no alphabetic content, purpose or definite origin is assigned.','alphaA;pencilarc','drawing or diagram','low',True)
ch('added residue-field hypothesis',r'\inserted{et supposons le corps résiduel de $B$ fini sur celui de $A$.}',insert,'The full sentence is typed above Soit k, starting to its right. A dark line begins after the comma following the baseline A, rises diagonally to below résiduel, runs beneath the remainder of the addition, and curls upward after its period. The text and connecting line are reproduced together, preserving the attachment and two levels.','insertall;insertBa;insertleader;Soitk;BplatA','insertion or placement','high',True,True)
ch('conclusion, Alors','Alors',r'\rlap{a}Alors','The initial cell combines a capital A apex, sloping legs and crossbar with a lower-case a upper curl and rounded lower bowl. Both impressions precede a separate l; neither chronology nor a preferred editorial capitalisation is supplied.','semicolonAlors;AlorsA;maximal1;maximal2','misread word','high',True)
ch('proof, reformuler','reformuler',r'ref\unsure{\rlap{r}o}rmuler','The fourth cell has an o lower loop and right curve together with an extra left vertical/foot and upper-right shoulder compatible with r. Fusion obscures their meeting, so the superposition is qualified. No replacement sequence is assigned.','reformuler;reformo;pccontrol','misread word','medium',True)
for place,reading,shows,crop in [
 ('introductory spelling','tels la','The final s of tels and two letters la are clear; the incongruous form is retained.','quotecondition'),
 ('first noetherian adjective','noéthériens','Two acute accents are independently visible, one above each of the two e letters before r.','noethfirst'),
 ('canceled theorem phrase','d\'anneaux locaux','The apostrophe, letter stems and curved lower parts remain visible under the x row. The cancellation is local in addition to the global diagonals.','anncancel'),
 ('condition a spelling','localise','The final e has no acute above it.','localise'),
 ('property symbols',r'\uuline{R}(C); r(C); \uuline{R}(C/tC); U_{\uuline{R}}(\operatorname{Spec}(C))','Each capital property R has two underlines; r before (C) is lowercase and singly underlined. The U has lowered R and two underlines beneath that index; the nested parentheses enclose Spec(C). The blank before r is not supplied with a relation sign.','RC1;BR;trC;RCtC;RC2;URSpec'),
 ('Greek labels',r'\alpha); \beta)','Both labels are handwritten before typed parentheses: alpha has a closed left loop and crossed right strokes; beta has a long descending stem and two right lobes.','alpha;beta'),
 ('condition beta punctuation','régulier,','The comma has a rounded head and a descending leftward tail; it is retained at the paragraph end.','regcomma'),
 ('geometric condition in both conclusions','Q géométrique','Both letters are oval with a lower-right tail, unlike the stem/bowls of R in the hypotheses. Both Q readings remain unchanged.','Qgeo1;Qgeo2'),
 ('fiber product expression',r'B\otimes_A k\ \text{sur}\ k','The typed round enclosure with crossing inner strokes lies between B and k; A is lowered beneath it. Both occurrences of k and the intervening sur are legible.','tensor;surk'),
 ('proof, morphism slots',r'A\quad B; A\quad A\prime; A\quad B','The A/B and A/A-prime pairs have visible blanks between them. The first and third blanks have no arrow; the second is crossed by a long cancellation stroke, without an arrowhead. The prime is a single raised short vertical mark.','AB1;ABproof;AAprime;ABhom'),
 ('proof, canceled restart','(NB alors','The opening parenthesis, N diagonal/stems, B bowls, a bowl, tall l, round o and r/s contours remain readable beneath the x row. The next line begins a new (NB.','NBdeleted;NBactual')]:
 ch(place,reading,reading,shows,crop)
r.doubt('first quoted condition, initial two cells',r'\rlap{p}c; \rlap{r}o','c/o with displaced impressions','medium','The descender/foot and inner serif strokes suggest p/c and r/o superposition; no whole earlier word is reconstructed.')
r.doubt('second noetherian adjective, second altered cell',r'\rlap{t}h','h with displaced impression','medium','The first h/t overprint is readable; the second upper central stroke is not fully separable.')
r.doubt('after On suppose','deleted x','deleted r under x','low','Visible cancel and underlying letter cannot be fully separated.')
r.doubt('condition a, main letter',r'\rlap{C}B','B with displaced impression','medium','B bowls are secure; the extra left curve is qualified.')
r.doubt('condition a, raised cancel','deleted x','deleted prime under x','low','No independent prime can be isolated from the heavy crossing strokes.')
r.doubt('after suivantes','deleted x','underlying mark undetermined','low','Interior fused; small spot cannot be securely separated from a foot.')
r.doubt('proof, fourth cell of reformuler',r'\rlap{r}o','o with another fused impression','medium','Extra left stem and upper-right shoulder are compatible with r, but not fully separable.')
r.doubt('trace below universellement','shallow curved trace','origin/function undetermined','low','The visible shape is reproduced without a textual interpretation.')
r.notation('property R and lowercase r',r'\uuline{R}; \underline{r}; U_{\text{\uuline{R}}}','12:083, theorem and a/b: capital R double-underlined; radical-like r singly underlined; U index lowered. Plain R in (B,R).')
r.notation('Q in geometric conclusion','Q','12:083 both conclusion occurrences have oval bodies and lower-right tails; no harmonisation to R.')
r.notation('typewriter superpositions',r'\rlap{f}r; \rlap{è}t; \rlap{h}t; \rlap{a}A','12:083, quoted condition, quoted intègre, second noetherian adjective, Alors. Other component readings remain qualified; chronology not asserted.')
r.notation('typed tensor sign',r'\otimes_A','12:083 round enclosing stroke with internal x-like crossing; A lowered beneath, B/k on baseline.')
r.notation('blank relations',r'A\quad B; t\quad\underline r(C); A\quad A\prime','12:083 visible blanks retained without arrows or membership sign.')
for a,e in [('IV','fourth section or part'),('NB','nota bene'),('i.e.','id est')]:r.r.setdefault('abbreviations',[]).append(dict(abbreviation=a,expansion=e,attestations='12:083'))
r.r['inventory_overrides']={'083-06':dict(first_words_or_objects='visible canceled x; possible underlying r'),'083-08':dict(position='centered above B and raised cancel cell'),'083-09':dict(first_words_or_objects='raised canceled x; possible prime'),'083-18':dict(first_words_or_objects='et supposons ... A.; line from comma after baseline A',position='above Soit k, leader beneath right part of insertion')}
extras=[('qualified p/c and r/o, clear f/r overprints','text','introductory quoted condition','typewriter'),('è/t overprint','text','introductory intègre','typewriter'),('h/t and qualified t/h overprints','text','second noetherian adjective','typewriter'),('qualified C/B overprint','text','condition a','typewriter'),('shallow curved trace, origin/function undetermined','drawing','below first half of universellement','another unnamed hand'),('bent insertion leader and terminal curl','drawing','residue-field addition','his hand'),('a/A overprint','text','Alors','typewriter'),('qualified r/o overprint','text','reformuler','typewriter'),('archive folio 82 retained as comment','margin note','bottom left','another unnamed hand')]
for i,(s,k,p,h) in enumerate(extras,1):r.r['inventory_extra'].append(dict(scan='12:083',sheet_kind='cancelled_draft',hand=h,element=f'083-R{i:03d}',kind=k,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops12_083.json').read_text())+json.loads(Path('work/crops12_083_fine.json').read_text())
r.r['inspection_note']='Root alone viewed whole083 and both actual supplied halves before witnesses, then all four C macro/table doubts, all six slips and all20 inventory elements. H has no text. All86 crop recipes were viewed, including22 initial fine controls and2 adaptive additions. The failed/truncated RCtC/RC2 display was repeated separately and only the successful displays counted. Two control crops missed their intended letter and were not evidence for that decision; the relevant controls occur in other successfully viewed crops. Both actual halves were reread line by line after initial crops; fine images were then inspected. Global diagonal cancellation, local x deletions, handwritten Greek labels, raised local, the inserted residue-field sentence and its leader, and the faint curved trace were distinguished. No slanted verbal marginal note occurs. C spelling slips were not normalised; overprints are retained without a chronology, and ambiguous components are marked. Archive82 remains a comment. Context remains sealed. This is first-pass collation, not the ordered audit or a mathematical check.'
r.save('work/record12_083.json')
