import sys
sys.path.insert(0,'out/scripts')
from work import commit
R=[
(r'\unsure{\nu|v}',r'\nu'),
(r'\scriptsize\unsure{;|,}',r'\scriptsize;'),
(r'C^{i}_{\deleted{i}y}',r'C^{i}_{\deleted{i}\handwritten{y}}'),
(r'par\deleted{\unsure{a}}fait',r'par\deleted{a}fait'),
(r'''\[
  \deleted{Z^{i}_{y}=\operatorname{Spec}(H^{0}(X^{i}_{y\,\mathrm{réd}},\underline O_{X^{i}_{y\,\mathrm{réd}}}))}
  \deleted{\,,\qquad Z=\unsure{\textstyle\prod}_{i}Z^{i}_{y}\,,}
  \tag*{\deleted{(4.18)}}
\]
\deleted{de sorte que l'on a simplement $Z^{i}_{y}$ est le spectre d'une extension finie $k(y)_{i}$ de $k(y)$, de degré séparable}''',r'''\figure{\begin{tikzpicture}[x=1mm,y=1mm,line cap=round,every node/.style={anchor=base west,inner sep=0pt,font=\scriptsize}]
  \node at (0,15) {$\deleted{(4.18)}$};
  \node at (35,15) {$\deleted{Z^{i}_{y}=\operatorname{Spec}(H^{0}(X^{i}_{y\,\mathrm{réd}},\underline O_{X^{i}_{y\,\mathrm{réd}}}))\,,\qquad Z=\unsure{\textstyle\prod|\textstyle\coprod}_{i}Z^{i}_{y}\,,}$};
  \node at (0,7) {\deleted{de sorte que l'on a simplement $Z^{i}_{y}$ est le spectre d'une extension finie}};
  \node at (0,0) {\deleted{$k(y)_{i}$ de $k(y)$, de degré séparable}};
  \draw (0,-.5) -- (0,16) .. controls (10,17) and (26,18) .. (40,18)
    -- (146,17) .. controls (151,17) and (151,15) .. (155,11);
  \draw (154,10) -- (72,8) -- (72,-1) .. controls (50,-2) and (22,-1) .. (0,-1);
  \draw (18,15) .. controls (21,9) and (27,3) .. (33,0);
  \draw (42,15) .. controls (46,12) and (49,5) .. (53,3);
  \draw (66,15) .. controls (67,11) and (71,9) .. (77,8);
  \draw (91,15) .. controls (93,13) and (94,11) .. (97,10);
  \draw (109,12) -- (114,10);
  \draw (20,11.5) -- (20.4,11.1);
\end{tikzpicture}}'''),
(r'finie\inserted{\handwritten{ de $k(y)$,}} de degré',r'''finie\tikz[baseline=0pt,x=1em,y=1ex,line cap=round]{
  \path[use as bounding box] (0,-.7) rectangle (.1,4.0);
  \node[overlay,anchor=base west,inner sep=0pt] at (-1.0,2.5) {\inserted{\handwritten{de $k(y)$,}}};
  \draw[overlay] (0,-.7) .. controls (-.3,1.2) and (.2,1.4) .. (.7,1.4)
    -- (5.1,1.6) .. controls (5.5,1.6) and (5.6,1.9) .. (5.6,2.7);
} de degré'''),
(r'\margin{\handwritten{\unsure{---|$\sim$}}}',r'''\margin{\tikz[x=1em,y=1ex,line cap=round]{
  \draw[gray] (0,1.3) .. controls (.5,.8) and (1.0,.5) .. (1.8,.25);
  \draw (.45,.45) .. controls (.7,.15) and (.85,.25) .. (.85,.5)
    .. controls (1.0,.25) and (1.3,.5) .. (1.7,.25);
}}'''),
(r'\unsure{x|i}',r'\unsure{x|a|i}'),
(r'\deleted{\unsure{,}}\handwritten{\unsure{;|.}}',r'\deleted{\unsure{,|;}}\handwritten{,}'),
(r'\underline{\mathrm Z}_{Z_{\deleted{\unsure{y}}}}',r'\underline{\mathrm Z}_{Z_{\deleted{y}}}'),
(r'\handwritten{\deleted{\unsure{\to}}\textstyle\prod_{i}}',r'''\handwritten{\tikz[baseline=-.6ex]{
  \node[inner sep=0pt] (p) {$\displaystyle\prod_i$};
  \node[overlay,inner sep=0pt] at ([yshift=.3ex]p.center) {$\deleted{\unsure{\to}}$};
}}'''),
(r'tra\deleted{\unsure{o}}\handwritten{n}\deleted{\unsure{i}}sition',r'tra\deleted{o}\handwritten{n}\deleted{i}sition'),
(r"\deleted{\unsure{dont chacun}}\inserted{et qu'un tel noyau}",r'''\tikz[baseline=(old.base)]{
  \node[inner sep=0pt,anchor=base west] (old) {\deleted{dont chacun}};
  \node[overlay,inner sep=0pt,anchor=base west] at ([yshift=1.0em]old.base west) {\inserted{et qu'un tel noyau}};
  \path (old.north) ++(0,1.0em);
}'''),
(r't\deleted{\unsure{o}}rouve',r't\deleted{o}rouve')]
L=[]
def a(p,c,h,f,ink,conf='high',ac=False,ah=True,k='other',mh='no',cons=None):
 d=dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh)
 if cons:d['consequential']=cons
 L.append(d)
a('opening nu',r'\unsure{\nu|v}',r'\nu',r'\nu','mu_nu8x and nu73516x: the right stroke curves outward and then returns left at its high tip, unlike a simple straight v arm. The same curved form recurs in the lower formulas.','high',True,False)
a('low mark within multiplicité',r'\unsure{;|,}','absent','small lowered semicolon','straypunct22x: two separate dark components are visible, an upper point and a lower hooked stroke; their separation supports a semicolon. Its unusual low position is preserved.','high',True,True,'omission')
a('C index in first prose line',r'C^i_{\deleted i y}',r'C^i_y',r'C^i_{\deleted i\handwritten y}','Cindex18x: the old typed i dot and lower serif remain behind a dark handwritten y with a looped descender.','high',True,True,'omission')
a('left margin at respectivement',r'\unsure{x|$\times$}','absent',r'\unsure{x|$\times$}','margx20x: two fine sloping strokes intersect, with one much longer upward/right and downward/left. This does not distinguish a literal x from a cross mark.','low',False,True,'omission')
a('overtyped letter in parfait',r'par\deleted{\unsure a}fait','parfait',r'par\deleted a fait','parafait12x: a complete lower bowl and right-hand upright/foot of a typed a remain underneath the f ascender and crossbar.','medium',True,True,'omission')
a('cancelled formula, first réd index',r'X^i_{y\,\mathrm{réd}}',r'X^i_y',r'X^i_{y\,\mathrm{réd}}','cancel1mid7x: r, accented é and tall d are visible at the lower right of the first X/y despite the x overtyping.','high',False,True,'omission')
a('cancelled formula, O alphabet and index',r'\underline O_{X^i_{y\,\mathrm{réd}}}',r'\mathcal O_{X^i_y}',r'\underline O_{X^i_{y\,\mathrm{réd}}}','cancel1mid7x: O is a typed oval with a separate lower horizontal underline; the second réd follows the lower y. There is no script O contour.','high',False,True,'misread symbol or index')
a('cancelled product/coproduct sign',r'\unsure{\prod}_i',r'\coprod',r'\unsure{\prod|\coprod}_i','cancel1right6x and cancelprod22x: typed cancellation x marks cover the sign position; the lower i stem and serif remain, but an upper versus lower joining bar cannot be established. Product/coproduct remains explicitly unresolved, and the visible index is retained.','low',True,True,'misread symbol or index')
a('cancellation enclosure and diagonals','deleted text only','struck text only','stepped enclosure, oblique cancellation strokes and small short stroke, drawn around the three cancelled lines','cancelALL3x plus the six enlarged segments: a long upper rule turns down at right; the lower boundary steps down after the second line and encloses the third line’s left segment. Five internal slanting strokes and one small short stroke remain distinct from typed x cancellation.','high',True,True,'drawing or diagram')
a('de k(y), insertion and leader','inline insertion after finie','inline addition after finie','raised de k(y), with lower curved rule and leader after finie','dek10x and dekupright10x rotated +3 degrees: the words and comma lie above the line; the supporting curved stroke descends into the gap between finie and de degré and turns up at right.','high',True,True,'insertion or placement')
a('margin above (4.20)',r'\unsure{---|\sim}','absent','drawing of pale slanting stroke and darker short hooked/wavy stroke','margdash16x: the pale diagonal crosses a shorter dark shallow loop and irregular extension. A single typographic dash or tilde loses the two-part shape; it is now reproduced as a drawing without assigning a letter.','medium',True,True,'drawing or diagram')
a('(4.20), overwritten index of Z',r'\deleted{\unsure{x|i}}y','y',r'\deleted{\unsure{x|a|i}}y','Z20oldindex20x: a lower rounded remnant at left and an upright/right foot remain behind y. The covered letter cannot be securely separated as x, a or i; the rounded remnant warrants retaining a as an additional possibility.','low',True,True,'omission')
a('(4.20), product sign',r'\prod',r'\coprod',r'\prod','prod20x9: one long top horizontal joins two descending uprights; their lower ends are unjoined.','high',False,True,'misread symbol or index',cons='The surviving (4.20) writes a product sign, whereas H gives a coproduct.')
a('(4.20), cancelled punctuation',r'\deleted{\unsure{,}}','absent',r'\deleted{\unsure{,|;}}','end20x24: the upper mark is heavily overwritten by dark crossing strokes; the original punctuation cannot be distinguished securely as comma or semicolon.','low',True,True,'omission')
a('(4.20), surviving punctuation',r'\handwritten{\unsure{;|.}}','period','comma','end20x24: the isolated lower dark mark has a clear descending leftward tail. The upper ink is cancellation, so it does not supply a live upper dot for a semicolon.','medium',True,True,'misread symbol or index')
for place,old,new,crop in [('(4.19)','17','19','num19x12'),('(4.20)','18','20','num20x12'),('(4.21)','19','21','num21x12'),('(4.22)','20','22','num22x12'),('prose reference after (4.22)','19','21','ref21x12'),('(4.23)','21','23','num23x12'),('(4.24)','22','24','num24x12')]:
 a(place+', numbering','old '+old+' overwritten by '+new,'only final '+new+' in text; general note gives old sequence 18–23','old '+old+' overwritten by '+new,crop+': the old typed numeral outlines remain under thicker handwritten replacement strokes. In particular the first old final digit is 7, and the last is 2; the source corrections are retained individually.','high',False,True,'omission')
a('(4.21), two underlined Z letters',r'\underline{\mathrm Z}',r'\underline{\mathbb Z}',r'\underline{\mathrm Z}','seq5x: each typed Z has one diagonal and separate lower underline; no parallel diagonal doubles either letter.','high',False,True,'misread symbol or index')
a('inline adjunction map, two underlined Z letters',r'\underline{\mathrm Z}',r'\underline{\mathbb Z}',r'\underline{\mathrm Z}','adjointmap8x: single diagonal strokes with separate horizontal underlines; both nested Z/y index levels are visible.','high',False,True,'misread symbol or index')
a('(4.22), three underlined Z letters',r'\underline{\mathrm Z}',r'\underline{\mathbb Z}',r'\underline{\mathrm Z}','adjoint7x: each Z has a single typed diagonal; the underline is below the body.','high',False,True,'misread symbol or index')
a('(4.22), cancelled final y',r'\deleted{\unsure y}','absent',r'\deleted y','zycancel26x: although the upper body is hatched, the typed upper-left serif and a continuous descender ending in an upturned left hook remain visible. These identify y.','medium',True,True,'omission')
a('(4.23), first prefix before Ker',r'\deleted{\unsure{\mathrm{Co}}}','absent',r'\deleted{\unsure{\mathrm{Co}}}','CoAx24: parts of two rounded typed contours remain under dense oblique black hatching; C/o cannot be separated securely enough to remove the doubt.','medium',False,True,'omission')
a('(4.23), second prefix before Ker',r'\deleted{\unsure{\mathrm{Co}}}','absent',r'\deleted{\unsure{\mathrm{Co}}}','CoBx24: the two positions retain curved remnants but are largely filled by the cancellation. The reading remains provisional.','medium',False,True,'omission')
a('(4.23), first-line Z alphabets',r'\underline{\mathrm Z}',r'\underline{\mathbb Z}',r'\underline{\mathrm Z}','eq23a4x: both coefficient Zs show one sloping diagonal, with an independent lower line; the base scheme Z is also plain and un-underlined.','high',False,True,'misread symbol or index')
a('(4.23), first product index',r'\prod_i',r'\prod',r'\prod_i','prodAx16: a short separate dot above a bent lower stem is written under the left side of the product sign.','high',False,True,'omission')
a('(4.23), second-line Q/Z alphabets',r'\underline{\mathrm Q}/\underline{\mathrm Z}',r'\underline{\mathbb Q}/\underline{\mathbb Z}',r'\underline{\mathrm Q}/\underline{\mathrm Z}','eq23b4x: each Q has one oval and short tail; each Z one diagonal; the horizontal lines lie below the letters.','high',False,True,'misread symbol or index')
a('(4.23), second product index',r'\prod_i',r'\prod',r'\prod_i','arrowBx14: a separate point and bent lower stem lie beneath the product sign, forming i.','high',False,True,'omission')
a('(4.23), cancelled arrow remnant','doubtful cancelled arrow before product','absent','doubtful cancelled arrow overlapping the inside of the product','arrowBx14: the live left arrow reaches the product’s left stem; a separate dark triangular/shaft-like mass occupies the gap between its stems. The old arrow reading stays doubtful and its overlapping position is preserved.','medium',True,True,'insertion or placement')
a('inline transition map, Q/Z alphabets',r'\underline{\mathrm Q}/\underline{\mathrm Z}',r'\underline{\mathbb Q}/\underline{\mathbb Z}',r'\underline{\mathrm Q}/\underline{\mathrm Z}','Htransition5x: single oval Qs and single-diagonal Zs, with distinct underlines, in both source and target.','high',False,True,'misread symbol or index')
a('transition correction layer',r'tra\deleted{\unsure o}\handwritten n\deleted{\unsure i}sition','transition',r'tra\deleted o\handwritten n\deleted i sition','transition10x and transitionold24x: an old oval o protrudes below the dark n; the next position preserves a separate i dot and straight stem/serif behind the overtyped s.','medium',True,True,'omission')
a('cancelled dont chacun',r'\deleted{\unsure{dont chacun}}',r'\struck{\ill{}}',r'\deleted{dont chacun}','oldchacun9x: d ascender, o bowl, n/t, c/h/a/c/u/n outlines remain readable between typed x marks and the horizontal black stroke.','medium',True,True,'readable ink left as \\ill{}','yes')
a('et qu’un tel noyau placement','inline insertion after cancelled words','inline addition after cancelled words','typed insertion raised directly above dont chacun','oldchacun9x: et starts over the old d; the added phrase runs above the cancelled phrase and projects rightward over the following line. No leader is added, because none is visible.','high',True,True,'insertion or placement')
a('cancelled mark after annihilator',r'\deleted{\unsure e}','absent',r'\deleted{\unsure e}','annihilator12x: a small rounded left contour and horizontal middle trace survive crossed strokes, but the complete e shape remains obscured.','medium',False,True,'omission')
a('(4.24), cancelled punctuation',r'\deleted{\unsure{;}}.','period only',r'\deleted{\unsure{;}}.','gcd9x and gcdpunct24x: an oblique cancellation crosses an upper hook-like remnant; the lower round point remains distinct. The semicolon identification is still provisional.','medium',False,True,'omission')
a('final hat-Z alphabet',r'\hat{\underline{\mathrm Z}}',r'\hat{\underline{\mathbb Z}}',r'\hat{\underline{\mathrm Z}}','last5x: the typed Z has one diagonal, an independent underline and a small handwritten roof-shaped hat above it.','high',False,True,'misread symbol or index')
a('final trouve correction',r't\deleted{\unsure o}rouve','trouve',r't\deleted o rouve','lastold20x: a complete typed oval o remains under the r stem/shoulder, with its lower curve extending to the right of r.','high',True,True,'omission')
I=[]
def i(kind,pos,text,hand='typewriter'):I.append(dict(kind=kind,position=pos,text=text,hand=hand))
i('text','upper right','20','his hand')
i('display','(4.19)','μ^i_y, ν^i_y','typewriter and his hand')
i('deletion','opening reference','old 7 below handwritten 9','typewriter and his hand')
i('text','first paragraph','la multiplicité radicielle ... respectivement (EGA IV 4.7.4.), - donc μ^i_y=1 si k(y) est parfait.','typewriter and his hand')
i('insertion','below middle of multiplicité','small lowered semicolon','typewriter')
i('deletion','first C index','i under y','typewriter')
i('insertion','first C index','y','his hand')
i('margin note','left of respectivement','uncertain x/cross','his hand')
i('insertion','EGA reference',' .7.4.','his hand')
i('deletion','within parfait','old a beneath f','typewriter')
i('text','before cancelled block','On ... considère aussi la plus petite extension galoisienne k(y)^i','typewriter')
i('deletion','after On','pose aussi','typewriter and his hand')
i('display','cancelled (4.18)','Z^i_y=Spec(H0(X^i_y réd, underlined O indexed by X^i_y réd)), Z=uncertain product/coproduct indexed i of Z^i_y,','typewriter')
i('deletion','three-line cancelled block','entire old (4.18) and de sorte que ... de degré séparable','typewriter and his hand')
i('drawing','around cancelled block','stepped enclosure, five oblique interior cancellation strokes and one short stroke','his hand')
i('text','continuation after cancellation','de k(y) tel que les composantes irréductibles ... soient géométriquement irréductibles: c’est une extension finie ... de degré ν^i_y. On pose','typewriter and his hand')
i('display','within continuation','(X^i_y) tensor over k(y) with k(y)^i; ν^i_y','typewriter and his hand')
i('insertion','above gap after finie','de k(y),','his hand')
i('drawing','beneath de k(y),','curved lower rule and leader to gap after finie','his hand')
i('drawing','left margin just above (4.20)','pale diagonal and short dark hooked/wavy stroke','his hand')
i('display','(4.20)','Z^i_y=Spec(k(y)^i), Z at corrected y=product Z^i_y,','typewriter and his hand')
i('deletion','(4.20) reference','18 overwritten by 20','typewriter and his hand')
i('deletion','(4.20) index','uncertain x/a/i beneath y','typewriter')
i('deletion','(4.20) punctuation','uncertain comma/semicolon','typewriter and his hand')
i('insertion','(4.20) punctuation','comma','his hand')
i('text','before exact sequence','Ceci posé, le faisceau E_y sur y s’insère dans une suite exacte de faisceaux','typewriter')
i('display','(4.21)','0→underlined Z_y→p_y*(underlined Z indexed Z_y)→underlined E_y→0,','typewriter and his hand')
i('deletion','(4.21) reference','19 overwritten by 21','typewriter and his hand')
i('text','adjunction paragraph','où p_y:Z_y→y est la projection structurale ... est adjoint de l’homomorphisme','typewriter and his hand')
i('display','embedded in adjunction paragraph','p_y:Z_y→y; underlined Z_y→p_y*(underlined Z indexed Z_y)','typewriter and his hand')
i('display','(4.22)','p_y upper-star(underlined Z_y)=underlined Z_Z→underlined Z_Z with cancelled y','typewriter and his hand')
i('deletion','(4.22) reference','0 overwritten by 2','typewriter and his hand')
i('deletion','(4.22), final index','y','typewriter and his hand')
i('text','between (4.22) and (4.23)','qui, sur la composante Z^i_y ... multiplication par a^i_y. La suite exacte ... associée à (4.21) ...','typewriter and his hand')
i('deletion','embedded cohomology reference','19 overwritten by 21','typewriter and his hand')
i('display','(4.23), first line','H1(y,E_y)=Ker(H2(y,Z_y)→product indexed i of H2(Z^i_y,Z))','typewriter and his hand')
i('deletion','(4.23) reference','1 overwritten by 3','typewriter and his hand')
i('deletion','first line before Ker','uncertain Co','typewriter and his hand')
i('display','(4.23), second line','=Ker(H1(y,Q/Z)→product indexed i of H1(Z^i_y,Q/Z)),','typewriter and his hand')
i('deletion','second line before Ker','uncertain Co','typewriter and his hand')
i('deletion','inside second product sign','uncertain old arrow','his hand')
i('text','paragraph below (4.23)','où la flèche ... est l’homomorphisme de transition évident, multiplié par a^i_y. Comme H1(y,E_y) ...','typewriter and his hand')
i('display','embedded in paragraph','H1(y,Q/Z)→H1(Z^i_y,Q/Z); a^i_y; H1(y,E_y)','typewriter and his hand')
i('deletion','within transition','old o and i','typewriter')
i('insertion','within transition','n','his hand')
i('insertion','above dont chacun','et qu’un tel noyau','typewriter')
i('deletion','below raised insertion','dont chacun','typewriter and his hand')
i('text','lower paragraph continuation','est manifestement annulé par a^i_y ν^i_y ... on voit que H1(y,E_y) est annulé par','typewriter and his hand')
i('deletion','after a^i_y ν^i_y','uncertain e','typewriter and his hand')
i('display','(4.24)','d_y=pgcd(a^i_y ν^i_y).','typewriter and his hand')
i('deletion','(4.24) reference','2 overwritten by 4','typewriter and his hand')
i('deletion','(4.24) punctuation','uncertain semicolon','typewriter and his hand')
i('text','final paragraph','Lorsque k(y) est fini ... pseudo-fini au sens de Serre, i.e. son groupe fondamental ... isomorphe à Z hat, alors on trouve','typewriter and his hand')
i('display','within final paragraph','Gal(overlined k(y)/k(y)); underlined Z with hat','typewriter and his hand')
i('deletion','final trouve','old o beneath r','typewriter')
commit(97,14,dict(replace=R,changes=L,inventory=I,sheet_kind='reused_typed',hand='typewriter and his hand',observations='Whole page then both supplied halves personally read before C/H. All 51 base crops, eight adaptive crops and one rotated-upright insertion crop personally displayed and read; exact boxes/scales in crop_manifest.tsv. Every typed word, accent, singular/plural, abbreviation and punctuation was read in the scan, including the cancelled three-line passage. All mathematics enlarged, including inline maps and a/Z/k/H terms, alphabets, star positions, indices, exponents, product signs, arrows, underlines and hat/bar. Old/new numbers checked individually; H’s following section title belongs to the next page and is excluded. Added cancellation drawing, raised insertions and their actual endpoints; all C doubt marks decided or retained. No readable watermark established. Archive 13 is comment only; manuscript 20 transcribed. This is collation, not the second audit and not mathematical validation.'))
with open('out/notation.tsv','a') as f:
 f.write('Handwritten nu\t97/14 opening and lower products\tRight stroke curves outward then returns left at its high tip; repeated same form\t\\nu\topening nu/v resolved\n')
 f.write('Product versus coproduct\t97/14 surviving (4.20), (4.23)\tTop joining bar and two descending stems, lower ends unjoined\t\\prod\tcancelled earlier sign remains product/coproduct uncertain\n')
