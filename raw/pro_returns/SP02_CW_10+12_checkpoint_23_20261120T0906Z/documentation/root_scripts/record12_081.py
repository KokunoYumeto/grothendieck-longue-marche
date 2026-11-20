from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B12-01',12,81,'cancelled_draft')
H='[No H text supplied.]'
def ch(place,C,final,shows,crop,kind='other',confidence='high',against_C=False,consequential=False):
 r.change(place,C,H,final,shows,crop,kind,confidence,against_C,False,False,consequential)
def stack(base,ins,pos='.5',shift='0cm'):
 return r'\mbox{\begin{tikzpicture}[baseline=(base.base)]'+'\n'+r'\node[inner sep=0] (base) {'+base+r'};'+'\n'+r'\path (base.north west) -- coordinate[pos='+pos+r'] (at) (base.north east);'+'\n'+r'\node[anchor=south,inner sep=0,yshift=.04cm,xshift='+shift+r'] at (at) {\inserted{'+ins+r'}};'+'\n'+r'\end{tikzpicture}}'
pour=stack('vérifiés. CQFD',r'pour $M$','.67')
r.edit(r'vérifiés\inserted{pour $M$}. CQFD',pour)
ii=stack('1.,','(ii)','.95')
r.edit(r'1.\inserted{(ii)},',ii)
sred=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {$\deleted{S_i}$};
\node[anchor=south west,inner sep=0,xshift=-.18cm,yshift=-.06cm] at (base.north west) {\inserted{$S_{\mathrm{réd}},$}};
\end{tikzpicture}}'''
r.edit(r"$\deleted{S_i}\inserted{\unsure{S_{\mathrm{réd}'}|S_{\mathrm{réd}},}}$",sred)
r.edit('$z$ est un point','$z$ e st un point')
longu='long'+stack('e','u')+'urs'
r.edit(r'long\inserted{u}eurs',longu)
r.edit(r'\unsure{engendre}',r'\unsure{engendr}')
r.edit(r'\unsure{supposons}','supposons')
endmark=r'''\unsure{\mbox{\begin{tikzpicture}[baseline=0cm,x=1cm,y=1cm]
% Two-lobed terminal mark: its value as punctuation or a final letter is unresolved.
\draw[line width=.5pt] (.10,.19) .. controls (.06,.17) and (.03,.13) .. (.03,.10);
\fill (.025,.045) circle (.018cm);
\end{tikzpicture}}}'''
upper=r'''\margin{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=base west,rotate=32,inner sep=0] at (0,.50) {\handwritten{Corollaire pour}};
\node[anchor=base west,rotate=32,inner sep=0] at (.10,0) {\handwritten{$\unsure{x|t}$ \unsure{soit|est} $F$ régulier'''+endmark+r'''}};
% The grouping stroke stands above and to the right of the slanting note.
\draw[line width=.4pt] (2.82,2.96) -- (3.03,3.02) .. controls (3.00,2.48) and (3.11,1.58) .. (3.00,1.31) -- (3.13,1.25);
\end{tikzpicture}}'''
old_upper=r'\margin{\handwritten{$\left.\begin{gathered}\text{\unsure{Corollaire|Condition} pour}\\\unsure{x|t}\ \text{\unsure{soit|est}}\ F\ \text{\unsure{régulier}.}\end{gathered}\right]$}}'
r.edit(old_upper,upper)
marker=r'''\mbox{\begin{tikzpicture}[baseline=0cm,x=1cm,y=1cm]
\draw[line width=.5pt] (0,-.25) -- (.17,.22) .. controls (.20,.39) and (.31,.29) .. (.24,.20) -- (.15,.16);
\end{tikzpicture}}'''
old_lower=r"\inserted{\handwritten{$F$ n'a pas de cycles premiers immergés \unsure{passant} par $x$.}}"
r.edit(old_lower,marker)
lower=r'''\margin{\inserted{\handwritten{\shortstack[l]{'''+marker+r''' $F$ n'a pas de\\cycles premiers\\immergés \unsure{passant}\\par $x$.}}}}'''
r.edit(r'$\operatorname{supp}F=S$}',r'$\operatorname{supp}F=S$}'+'\n'+lower)
r.edit(r"$F/tF$ n'ait pas de cycles premiers associés",r"$F/tF$ n'ait pas de cyles premiers \unsure{associé}")
r.edit(r'\unsure{e xactement|exactement}','e xactement')
ch('interlinear pour M',r'vérifiés\inserted{pour $M$}. CQFD',pour,'pour M is typed on a raised line over the end of vérifiés and the beginning of CQFD. Its M descends to the top of Q. There is no insertion leader; the upper line is preserved over the corresponding part of the base.','pourM; CQFD; bcverifies','insertion or placement','high',True)
ch('Corollary 3 reference (ii)',r'1.\inserted{(ii)},',ii,'Both dotted i letters and their parentheses are typed above the comma after 1., extending right toward supposons. C places the insertion on the reading line; its raised position is retained.','ref1ii','insertion or placement','high',True)
ch('Corollary 3, replacement above S_i',r"\deleted{S_i}\inserted{\unsure{S_{\mathrm{réd}'}|S_{\mathrm{réd}},}}",sred,'The replacement S stands above and to the left of the x-canceled S_i. réd is lowered relative to that raised S. The following mark has the round head and leftward descending tail of a comma, at the raised S baseline; it differs from the upright prime after T. This resolves the C macro/table doubt to a comma and preserves both vertical levels.','Sredalter; Sredcontext; Sredpunct; xTprime','insertion or placement','high',True)
ch('Corollary 3, z e st',r'$z$ est un point',r'$z$ e st un point','There is a conspicuous blank interval after e before st. In the nearby x est son the e and s occupy adjacent normal typing positions. The internal gap is retained.','zpoint; zpointfine; estcontrol','other','high',True)
ch('Proposition 4 proof, raised u',r'long\inserted{u}eurs',longu,'The base reads longeurs, with a separate u directly above the first e. It is not typed in a new baseline cell between g and e.','longueurs','insertion or placement','high',True)
ch('Proposition 4 proof reference',r'\unsure{8|6}',r'\unsure{8|6}','Two enclosed white areas favor 8, but the unusually thick left side and internal strokes show overtyping. Comparison with 6 in 5.6.2/Corollaire 6 and 8 in 8.1.4 does not securely recover the component or final numeral. C macro/table doubt remains.','ref8; ref8fine; ref562; ref814; cor6title','misread symbol or index','low')
ch('Proposition 4 proof, clipped right edge',r'\unsure{engendre}',r'\unsure{engendr}','The visible letters end in the complete r; the photographed black edge starts immediately at its right shoulder. No final e can be seen in either the whole image or supplied half. The visible prefix is retained with a clipping doubt, without supplying an unseen letter.','engendre; edgeeng','text not on the page','high',True)
ch('Proposition 5, canceled supposons',r'\unsure{supposons}','supposons','The two p descenders survive independently of the cancellation x row; s/u at the beginning, the rounded o cells, medial/final s curves and n shoulder can be followed in the split enlargements. The word remains canceled and the C macro/table doubt is removed.','supposcancel; supposfirst; supposlast','misread word','medium',True)
ch('upper marginal note, first word',r'\unsure{Corollaire|Condition}','Corollaire','The upright enlargement shows Co, two successive tall l strokes, the looped a, dotted i, short r and compressed terminal e. The two tall strokes do not show the d bowl and crossed t that Condition would require.','margin1; margin1native; margin1first','misread word','medium',True)
ch('upper marginal note, x/t and verb',r'\unsure{x|t} \unsure{soit|est}',r'\unsure{x|t} \unsure{soit|est}','The variable is made from two crossing oblique strokes, favoring x; its long rising stroke still permits a cursive t. The next word is compressed into a nearly horizontal stroke and a small terminal upstroke. Neither the middle letters nor the proposed verb can be separated securely. These two C doubts remain.','margin1; margin1verb','misread word','low')
ch('upper marginal note, régulier and terminal mark',r'\unsure{régulier}.','régulier '+endmark,'The r/acute-accented beginning, g descender, flattened u, tall l, dotted i and final er strokes support régulier. After it are a short oblique upper stroke and a separate lower spot. They are not securely a period, a final s or an exclamation mark, so the two visible shapes are drawn under a doubt mark rather than assigned a punctuation value.','margin1regular; margin1end','drawing or diagram','medium',True)
ch('upper marginal note and grouping stroke','two-line note with right square bracket',upper,'The note rises to the right. The separate grouping stroke is nearly vertical on the unrotated sheet, extends well above the note, and has a short top cap and bent lower foot. Its relative placement is reproduced instead of making a centered mathematical bracket around the words.','margin1; margin1native','drawing or diagram','high',True)
ch('Corollary 6, cyles','cycles','cyles','The five consecutive cells are c, y, l, e, s. The y is followed immediately by the tall l; there is no second c or deleted cell between them.','cyles','misread word','high',True)
ch('Corollary 6, clipped associé','associés',r'\unsure{associé}','The acute and almost all of the final e are visible at the black right edge. No separate s cell survives beyond it. Only the visible prefix is transcribed, with the clipping identified as the uncertainty.','assocideedge; edgeassoc','text not on the page','high',True)
ch('lower marginal insertion and paired reference marks',old_lower,marker+' [paired with marginal note] '+lower,'The four handwritten lines occupy the lower left margin, outside the cancellation strokes. A loop with a long descending oblique stem precedes the note; an identical reference mark stands immediately after Alors in the typed line. Both marks are reproduced, and the note is kept in the margin rather than inside the globally canceled typed paragraph.','Alorsleader; markercontext; margin2; margin2lower','insertion or placement','high',True)
ch('lower marginal note, passant',r'\unsure{passant}',r'\unsure{passant}','The p descender and terminal tall t are distinct. Between them only a few very faint short strokes survive; the medial letters cannot all be separated even in the tightly cropped upright enlargement. The C macro/table doubt remains.','margin2; margin2lower; margin2passant','misread word','low')
ch('Corollary 6, e xactement',r'\unsure{e xactement|exactement}','e xactement','The opening e is separated from x by a visible blank wider than the intervals inside xactement. The same anomalous spacing is independently seen in e st above. All the letters are clear; the spacing is preserved and the C macro/table doubt is removed.','exacts; exactcontext; zpointfine; estcontrol','other','high',True)
for place,reading,shows,crops in [
 ('top formula, underlined prime-ideal letter',r'M_{\underline{p}_i}','The lower bar extends beneath the full p bowl as well as its stem, unlike the short stem feet in pqr and supp. The i is lowered again relative to p.','pindex; longineq; pqr; Ssupp'),
 ('unfilled relation spaces',r'\operatorname{long}M/tM\qquad\operatorname{long}M_{\underline{p}_i}; x\quad X; T\quad V(t); x\quad\operatorname{Ass}F/tF','The top length comparison, both x/X occurrences, T/V(t), and x/Ass each have a blank slot. No relation sign or intersection is supplied. The final S_i cap V(t) does have a distinct handwritten arch.','longineq; xblankX; xXet; Tprimecomp; xAss; SicapV'),
 ('typewriter slips retained','pqr; par Z; réguliers; par X','The q has a descender; the Z and final X have capital height; réguliers has r-s at the end, without an inserted e. None is regularized.','pqr; parZ; reguliers; parX'),
 ('structure-sheaf notation',r'\underline{O}_{S_{\mathrm{réd}},z}','The O has a single continuous underline. S is lowered, réd is lowered again, and z returns to the S level after a comma.','Oredz'),
 ('canceled phrases','un cas; supposons de point générique x.; T\' est un; et','The local rows of cancellation x strokes remain distinct from the long diagonals through the typed page. The words and the prime on T can be followed beneath them.','uncas; supposcancel; deletedpoint; Tprimecancel; xXet'),
 ('right edge, corollaire and final S','corollaire; S','At corollaire the remaining e curve and middle survive next to r at the edge. At the final equality the curved upper and lower portions identify S despite the clipped right side. These visible letter parts support C without completing a wholly absent cell.','corollairedge; edgecor; supportend')]:
 ch(place,reading,reading,shows,crops)
r.doubt('Proposition 4 proof reference','8','6 or unresolved overtyping','low','Two loops favor 8; overlapping strokes prevent a secure unique numeral.')
r.doubt('Proposition 4 proof, right edge','engendr','ending beyond the photographed edge','medium','Only the visible prefix is transcribed; no final e is supplied.')
r.doubt('upper margin, variable','x','t','low','Two crossed oblique strokes, with an unusually long rising arm.')
r.doubt('upper margin, verb','soit','est','low','The middle cursive strokes are compressed into a nearly horizontal line.')
r.doubt('upper margin, after régulier','drawn upper oblique stroke and lower spot','exclamation mark; final s; punctuation','low','The visible shape is reproduced under an in-place doubt mark without choosing a letter or punctuation value.')
r.doubt('Corollary 6, right edge','associé','ending beyond the photographed edge','medium','No separate final s is visible; the text stops at the identifiable é.')
r.doubt('lower marginal note','passant','','low','p and final t are clear; medial letters remain faded and compressed.')
r.notation('underlined typed prime-ideal letter',r'M_{\underline{p}_i}','12:081 top display: underline extends under the p bowl, and i is a second lower level.')
r.notation('nested structure-sheaf indices',r'\underline{O}_{S_{\mathrm{réd}},z}','12:081 Corollary 3: O underlined once, nested réd, comma before z at S level.')
r.notation('blank relation slots',r'x\quad X; T\quad V(t); x\quad\operatorname{Ass}F/tF','12:081 blank slots preserved; the later S_i cap V(t) is visibly different and has a hand-drawn intersection.')
r.notation('typewriter internal gaps','e st; e xactement','12:081 two visibly separated initial e letters, compared with normally spaced est on the same sheet.')
r.notation('paired handwritten insertion marks','loop with long descending oblique stem','12:081 identical mark after Alors and before the lower marginal note; represented in TikZ.')
for a,e in [('sss','si et seulement si'),('CQFD',"ce qu'il fallait démontrer"),('long','longueur'),('réd','réduit'),('comp irred','composantes irréductibles')]:
 r.r.setdefault('abbreviations',[]).append(dict(abbreviation=a,expansion=e,attestations='12:081'))
r.r['inventory_overrides']={
 '081-09':dict(first_words_or_objects='raised S_réd followed by comma, above canceled S_i'),
 '081-17':dict(first_words_or_objects='Corollaire pour; qualified x/t and soit/est; régulier and unresolved terminal mark; upper-right grouping stroke'),
 '081-21':dict(kind='margin note',first_words_or_objects="F n'a pas de cycles premiers immergés; qualified passant; par x.; paired reference mark")}
for i,(text,kind,position,hand) in enumerate([
 ('loop and descending oblique stem after Alors','drawing','Corollary 6 after Alors','his hand'),
 ('matching loop and descending oblique stem before lower marginal note','drawing','lower left margin','his hand'),
 ('unresolved two-part terminal mark after régulier','drawing','upper marginal note end','his hand'),
 ('cyles; visible clipped associé; e xactement','text','Corollary 6','typewriter'),
 ('archive sheet number 80 retained as comment','margin note','bottom-left corner','another unnamed hand')],1):
 r.r['inventory_extra'].append(dict(scan='12:081',sheet_kind='cancelled_draft',hand=hand,element=f'081-R{i:03d}',kind=kind,position=position,first_words_or_objects=text,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops12_081.json').read_text())+json.loads(Path('work/fine12_081.json').read_text())
r.r['inspection_note']='Root alone viewed the whole page and both actual supplied halves before reading C/H; inspected all10 C macro doubts,7 table doubts,4 slips,5 abbreviations and21 inventory elements. H has no text and all H flags are false. All87 crops were viewed (68 initial,19 fine), including both slanting notes rotated upright, each local deletion and insertion, all decisive formula indices/signs and clipped right-edge words. Additional Sred context showed that no comma occurs after the later Sred in the Proposition4 proof. The supplied halves were reread line by line after the initial and first16 fine crops; the last3 fine crops then settled the remaining terminal-mark, faded-word and punctuation observations. The upper marginal terminal shape remains unidentified and drawn; no meaning or final letter is silently assigned. The top replacement comma is read by its baseline and downward tail. Both matching lower insertion reference marks are drawn, and the lower handwriting remains outside the canceled typed paragraph. Line-end maxima-/les is joined from visible letters. Archive80 remains a comment. Context is sealed; no audit or mathematical check is claimed.'
r.save('work/record12_081.json')
