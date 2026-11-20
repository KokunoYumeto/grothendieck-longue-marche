from pathlib import Path
import json
import re

root=Path('/workspace/scratch/be39e9f81d6d/out/readings/scan013/R1')
reading=r'''\scanpage{13}
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=2.3em,row sep=2.2em]
1\arrow[r]\&Z\arrow[r,dash]\&G\arrow[r,dash]\&\Gamma\arrow[r,dash]\&1\&[3.2em](E)\\
1\arrow[r,dash]\&Z\arrow[u,"\unsure{2|\wr}"']\arrow[r,dash]\&G'\arrow[u]\arrow[r,dash]
 \&\Gamma'\arrow[u]\arrow[r,dash]\&1\&(E')
\end{tikzcd}}

Si l'extension $(E)$ \unsure{splitte|splitt.}, l'ext. $E'$ aussi.

% Raised abbreviated label and its curved, headless lead to Toute.
\noindent
\begin{tikzpicture}[baseline=(t.base)]
\node[anchor=base west,inner sep=0] (t) at (0,0) {Toute};
\node[anchor=base west,inner sep=0] at (-.12,.63) {\inserted{Rmq}};
\draw[line width=.4pt] (-.15,.14) .. controls (-.20,.43) and (.42,.43) .. (.79,.62);
\end{tikzpicture}
extension splittée $G$ de un $\Gamma$ par un $Z$ provient par image inverse d'\deleted{\unsure{une}}l'ext. splittée
% The formula stands alone at the left; the divider is lower and to its right.
% The two remote marks and the point below the lower rule are not assigned punctuation.
\figure{\begin{tikzpicture}[x=.009cm,y=.009cm]
\node[anchor=base west,inner sep=0] at (0,0) {$\displaystyle Z.\operatorname{Aut}(Z).$};
\node[inner sep=0] at (875,39) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=-.3ex]
 \draw[line width=.7pt,line cap=round] (0,1.5)--(.4,.7);
 \fill (.5,-.6) ellipse (.4pt and .6pt);
\end{tikzpicture}}};
\draw[line width=.5pt] (503,-82)--(739,-72);
\draw[line width=.45pt] (511,-102)--(724,-100);
\node[inner sep=0] at (729,-107) {\unsure{\begin{tikzpicture}[baseline=-.3ex]
 \fill (0,0) circle (.25pt);
\end{tikzpicture}}};
\node[inner sep=0] at (1034,-94) {\unsure{\begin{tikzpicture}[baseline=-.3ex]
 \fill (0,0) circle (.3pt);
\end{tikzpicture}}};
\end{tikzpicture}}

4) \quad Ens. de petit cardinal

a) \uline{Cardinal 2}\qquad Ens de cardinal 2 $\longleftrightarrow$ \unsure{torseur|torseurs} \unsure{sur|sous} $\mathbb{Z}_2$ ou encore, \uline{espace affine \unsure{\deleted{sous}|\deleted{sur}|sous|sur}} $\deleted{\unsure{\mathbb{Z}|Z}}\mathbb{F}_2$ (ou encore, \deleted{\illegible{1}} espace affine de dim 1 sur corps $\mathbb{F}_2$ --- car les espaces vect. de dim 1 sur $\mathbb{F}_2$ sont can. isomorphes \ldots)

% Two bent border strokes leave the upper-left and lower-right corners unjoined.
% The parenthetical statement is below the right half of the enclosure.
\figure{\begin{tikzpicture}
\node[anchor=base west,inner sep=0] (bx) at (0,0)
 {$\displaystyle \operatorname{Aff}(1,\mathbb{F}_2)\simeq
 \operatorname{Aff}(\mathbb{Z}_2)\simeq\unsure{\mathfrak{S}|\mathcal{S}}_2$};
\draw ([xshift=-.30cm,yshift=.18cm]bx.north west)
 -- ([xshift=.28cm,yshift=.36cm]bx.north east)
 -- ([xshift=.34cm,yshift=-.04cm]bx.south east);
\draw ([xshift=-.34cm,yshift=.04cm]bx.north west)
 -- ([xshift=-.25cm,yshift=-.25cm]bx.south west)
 -- ([xshift=.31cm,yshift=-.11cm]bx.south east);
\node[anchor=base east,inner sep=0] at ([xshift=-.45cm,yshift=-.90cm]bx.south east)
 {$\displaystyle (\unsure{\mathcal{A}|A}_2=\{1\})$};
\end{tikzpicture}}

b) \uline{Cardinal 3}
\[
\begin{array}{@{}c@{\;}c@{\;}c@{\;}c@{\;}c@{\;}c@{\;}c@{}}
\mathfrak{S}_3&\simeq&\operatorname{Aff}(1,\mathbb{F}_3)&\simeq&\operatorname{Gl}(2,\mathbb{F}_2)&\simeq&\operatorname{GP}(1,\mathbb{F}_2)\\
&&\rotatebox{90}{$\simeq$}&&&&\rotatebox{90}{$=$}\\
&&\mathbb{F}_3^{+}\mathbin{.}\mathbb{F}_3^{*}&&&&\operatorname{Gl}(2,\mathbb{F}_2)/\mathbb{F}_2^{*}\\[-.3ex]
&&\begin{array}{@{}c@{\qquad}c@{}}\rotatebox{90}{$\unsure{\simeq|=}$}&\rotatebox{90}{$=$}\end{array}&&&&\\[-.3ex]
&&\begin{array}{@{}c@{\qquad}c@{}}\mathbb{Z}_3&\mathbb{Z}_2\end{array}&&&&
\end{array}
\]
\[
\mathcal{A}_3\simeq\deleted{\unsure{\mathbb{Z}|Z}}\mathbb{F}_3^{+}(\simeq\mathbb{Z}_3)
\]
% archive sheet number: 12
'''
(root/'reading.tex').write_text(reading)

findings=[]
def add(id,place,c,h,final,evidence,confidence,kind,marked_in_H,diff_c,diff_h,bbox,crop='',doubt_action='',s_id='',math_note=''):
    findings.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,confidence=confidence,kind=kind,marked_in_H=marked_in_H,diff_c=diff_c,diff_h=diff_h,bbox=bbox,crop=('readings/scan013/R1/'+crop if crop else ''),doubt_action=doubt_action,s_id=s_id,math_note=math_note))

add('C01','Top diagram, label to the right of the left upward arrow',r'\unsure{2|\wr}',r'\mathrm{id}',r'\unsure{2|\wr}',
    'Crop 01 shows one small hooked form with a low right foot, not the separate letters i and d. The two alternatives in C remain possible; label is on the right of the upward shaft.', 'medium','misread symbol or index',False,False,True,[558,137,601,186],'01_vertical_label.png','retain',math_note='The extension argument does not license changing this uncertain ink to an identity label.')
add('C02','Sentence immediately below the diagram',r'\unsure{splitte}','splittée',r'\unsure{splitte|splitt.}',
    'Crop 02 has splitt followed by a short detached flat ending and a separate comma. No secure acute or second final e is visible. The ending may be a compressed e or an abbreviation stop.', 'medium','misread word',False,True,True,[804,326,972,385],'02_splitte.png','retain')
add('C03','Raised label before Toute',r'\inserted{\unsure{Rmq}}',r'\emph{Remarque}',r'\inserted{Rmq}, raised above Toute with a curved headless lead',
    'Half a resolves the capital R, compressed m and descending q. The label is raised, and a curved stroke runs from its right down to the start of Toute; the actual word Remarque is not written.', 'high','insertion or placement',False,True,True,[288,403,438,510],'','resolve')
add('C04','Remark, between d apostrophe and live l ext.',r"d'\deleted{\unsure{une}}l'ext.",r"d'une ext.",r"d'\deleted{\unsure{une}}l'ext.",
    'Crop 03 shows a dark horizontal cancellation across the compressed u/n/e region, followed by a tall live l and apostrophe. The canceled word remains only a probable une.', 'medium','deletion state (struck given live or live given struck)',False,False,True,[966,545,1212,585],'03_cancelled_une.png','retain')
add('C05','Cardinal 2, preposition after torseur',r'\unsure{sur|sous}','sous',r'\unsure{sur|sous}',
    'Crop 04 shows two compressed low returns and a short downturned terminal. A separate o is not secure; the end does not settle sur versus sous.', 'medium','misread word',False,False,True,[1456,1094,1528,1128],'04_torseur_preposition.png','retain')
add('C06','Underlined phrase after espace affine',r'\deleted{\unsure{sous}}','sur',r'\unsure{\deleted{sous}|\deleted{sur}|sous|sur}',
    'Crop 05 shows an initial sinuous hook, a small lower loop and a heavy horizontal middle/end. Cancellation is plausible, but the heavy stroke is not cleanly separable from the cursive joins. Both the word and its live/canceled state remain open.', 'low','deletion state (struck given live or live given struck)',False,True,True,[1016,1199,1094,1234],'05_cancelled_sous.png','retain',math_note='The expected preposition for an affine space was not used to choose a live word or a deletion state.')
add('C07','First overwritten field letter, before subscript 2',r'\deleted{\unsure{\mathbb{Z}}}\mathbb{F}_2',r'\mathbf{F}_2',r'\deleted{\unsure{\mathbb{Z}|Z}}\mathbb{F}_2',
    'Crop 06 shows a diagonal Z-like underform crossing the live doubled F stems. The overlay prevents a secure separation of a second underlying diagonal; doubled and plain Z remain alternatives.', 'medium','omission',False,True,True,[1111,1185,1167,1242],'06_overwritten_f2.png','retain')
add('C08','After the second ou encore',r'(ou encore, \deleted{\illegible{1}}',r'\struck{\ill{}} ou encore,',r'(ou encore, \deleted{\illegible{1}}',
    'Crop 07 leaves an initial hook and one low protrusion under a long horizontal cancellation, without enough surviving letters for a defensible word. The canceled item follows encore and its comma.', 'low','insertion or placement',True,False,True,[1426,1208,1541,1242],'07_cancelled_word.png','retain')
add('C09','Boxed formula, S alphabet (outer doubt)',r'\unsure{\mathfrak{S}|\mathcal{S}}',r'\mathfrak{S}',r'\unsure{\mathfrak{S}|\mathcal{S}}',
    'Crop 08 shows a broad curved enclosure, an inner return and a raised right tip. The decorative alphabet remains ambiguous. This row covers the alphabet only; the nested index is C10.', 'medium','misread symbol or index',False,False,False,[1142,1597,1220,1658],'08_s_subscript.png','retain')
add('C10','Boxed formula, S subscript (inner doubt)',r'_{\unsure{2|n}}',r'_2',r'_2',
    'Crop 08 has a short left hook falling into a low rightward foot, rather than an arched n with a downward terminal. The reading 2 is supported by this stroke sequence.', 'medium','misread symbol or index',False,True,False,[1204,1636,1248,1666],'08_s_subscript.png','resolve',math_note='The group-order calculation agrees with 2, but the subscript was selected from its hook and foot, not from cardinality.')
add('C11','Parenthetical A2 statement below the box',r'\unsure{\mathcal{A}|A}_2',r'\mathfrak{A}_2',r'\unsure{\mathcal{A}|A}_2',
    'Crop 09 shows a smooth open bowl and a short internal right upright, without the angular/doubled construction of a secure Fraktur A. Calligraphic versus plain cursive A remains open.', 'medium','misread symbol or index',False,False,True,[945,1716,1008,1774],'09_a_alphabet.png','retain')
add('C12','Vertical comparison between F3-plus and Z3',r'\rotatebox{90}{$\unsure{\simeq|=}$}',r'\note{... des signes $\simeq$ et $=$ verticaux ...}',r'\rotatebox{90}{$\unsure{\simeq|=}$}',
    'Crop 10 shows a heavy partly crossing curved left stroke and a straighter right stroke. A rotated simeq is favored, but the overinking leaves equality possible. The neighboring vertical equality is secure.', 'low','misread symbol or index',False,False,False,[734,2055,765,2091],'10_lower_relations.png','retain',math_note='Both candidate comparison signs are compatible with the additive group of F3 being cyclic of order 3; that fact cannot select the written mark.')
add('C13','Last display, overwritten field letter before subscript 3',r'\deleted{\unsure{\mathbb{Z}}}\mathbb{F}_3^{+}',r'\mathbf{F}_3^{+}',r'\deleted{\unsure{\mathbb{Z}|Z}}\mathbb{F}_3^{+}',
    'Crop 11 shows an oblique Z-like underform behind the live paired F stems and middle bar. The letter Z is strong, but overlap prevents a completely independent doubled/plain attribution.', 'medium','omission',False,True,True,[726,2154,798,2218],'11_overwritten_f3.png','retain')

add('F14','Top diagram, seven forward shafts other than the first',r'1\arrow[r]\&Z\arrow[r,dash]\&G\arrow[r,dash]\&\Gamma\arrow[r,dash]\&1; lower row all dash',r'Both rows have \arrow[r] at all four forward connections',r'First upper 1-to-Z arrow has a head; the other seven forward strokes are headless',
    'Half a shows two clear wings only on the upper first arrow. The other short horizontal strokes end bluntly or with one small pen spur; all three vertical arrows point upward.', 'high','drawing or diagram',False,False,True,[398,77,1030,257])
add('F15','Remark, introduction of Gamma and Z',r'de un $\Gamma$ par un $Z$',r'de $\Gamma$ par $Z$',r'de un $\Gamma$ par un $Z$',
    'Half a shows de, then a separately spaced un before Gamma, and another un after par. The nonstandard de un is retained.', 'high','omission',False,False,True,[1047,449,1491,510])
add('F16','Standalone Z.Aut(Z) formula',r'\[ Z.\operatorname{Aut}(Z). \]',r"... splittée $Z.\operatorname{Aut}(Z)$.",r'Z.Aut(Z). on a separate left-starting line',
    'Half a shows the short formula alone below the prose and at its left start, with a baseline product point and a final stop. Its placement is retained together with the following drawn divider.', 'high','insertion or placement',False,False,True,[280,656,532,720])
add('F17','Two-stroke divider below the remark',r'\figure{two drawn strokes}','No divider',r'Two slightly rising horizontal strokes, upper longer than lower',
    'Half a shows a long upper stroke and a separate shorter lower stroke. They are independent of the mathematics above.', 'high','omission',False,False,True,[780,763,1027,808])
add('F18','Cardinal 2, ending of torseur',r'torseur','torseurs',r'\unsure{torseur|torseurs}',
    'Crop 04 ends the noun with a small detached low hook. It may be the terminal r or an additional compressed s. The singular remains the primary reading, but the plural cannot be excluded.', 'medium','misread word',False,True,True,[1266,1072,1436,1138],'04_torseur_preposition.png')
add('F19','Two ou encore phrases and opening parenthesis',r'$\mathbb{Z}_2$ ou encore, ... $\mathbb{F}_2$ (ou encore,',r'$\mathbf{Z}_2$ (ou encore, ... $\mathbf{F}_2$ ... ou encore,',r'First ou encore has no opening parenthesis; an opening curve precedes the second ou encore',
    'Halves show no curve before the first ou at the left of the continuation. Crop 07 shows the tall opening curve before the second phrase. The final closing parenthesis remains after isomorphes and the ellipsis.', 'high','insertion or placement',False,False,True,[341,1184,1418,1262],'07_cancelled_word.png')
add('F20','Extent of underline in espace affine phrase',r'\uline{espace affine \deleted{\unsure{sous}}} $...\mathbb{F}_2$',r'\emph{espace affine sur $\mathbf{F}_2$}',r'Underline ends before the overwritten F2',
    'Half b and crop 06 show the rule ending to the left of the field letter. The alphabet macro equivalence between H bold and C mathbb is not a difference; the underline extent is.', 'high','drawing or diagram',False,False,True,[654,1180,1171,1268],'06_overwritten_f2.png')
add('F21','Enclosure of the cardinal-2 formula',r'\boxed{\operatorname{Aff}(1,\mathbb{F}_2)\simeq\operatorname{Aff}(\mathbb{Z}_2)\simeq...}',r'\boxed{\operatorname{Aff}(1,\mathbf{F}_2)\simeq\operatorname{Aff}(\mathbf{Z}_2)\simeq...}',r'Two bent strokes enclose the formula, with small unjoined upper-left and lower-right corners',
    'Half b shows the top-right stroke separate from the left-bottom stroke; crop 08 also includes the unjoined lower-right endpoint. The TikZ border preserves these actual gaps, without treating them as mathematical omissions.', 'high','drawing or diagram',False,True,True,[526,1560,1278,1718],'08_s_subscript.png')
add('F22','Placement of parenthetical A2 = {1}',r'A separate centered display $(\unsure{\mathcal{A}|A}_2=\{1\})$',r'\boxed{...}\qquad(\mathfrak{A}_2=\{1\})',r'Parenthesis below the right half of the drawn box',
    'Half b places the entire parenthetical on the next lower baseline, with its start well to the right of the box center. It is neither on the formula baseline nor centered below the enclosure.', 'high','insertion or placement',False,True,True,[900,1707,1189,1798],'09_a_alphabet.png')
add('F23','Final display, recurring A alphabet',r'\mathcal{A}_3',r'\mathfrak{A}_3',r'\mathcal{A}_3',
    'Crop 11 repeats the smooth open-bowl A of the parenthetical above. The first-occurrence alphabet doubt is C11; the primary calligraphic form is repeated here.', 'medium','misread symbol or index',False,False,True,[554,2152,638,2217],'11_overwritten_f3.png')
add('F24','Detached two-part mark to right of Z.Aut(Z) line','No mark','No mark',r'\unsure{two small drawn strokes}, at its observed position',
    'Crop 12 shows two closely spaced dark teardrop-like traces below the prose. They are preserved geometrically, without calling them punctuation; writing versus stray ink/surface trace remains unresolved.', 'low','drawing or diagram',False,True,True,[1147,648,1166,667],'12_detached_mark.png')
add('F25','Small points beside the divider','No points','No points',r'\unsure{point below the lower rule end}; \unsure{remote point to its right}',
    'Crop 13 shows one tiny point just below the lower stroke endpoint and another isolated point farther right. Neither is safely identifiable as punctuation or a mathematical mark; both are drawn with uncertainty.', 'low','drawing or diagram',False,True,True,[998,782,1327,813],'13_detached_point.png')

inventory=[]
def inv(element,kind,position,first,hand='his hand'):
    inventory.append(dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('I01','diagram','top, [398,77,1301,257]',"Two rows 1, Z, G, Gamma, 1 / 1, Z, G-prime, Gamma-prime, 1; (E), (E-prime)")
inv('I02','text','below diagram, [301,320,1332,392]',"Si l'extension (E) splitte, l'ext. E' aussi.")
inv('I03','insertion','above Toute, [288,403,398,488]','Rmq with curved headless lead')
inv('I04','text','upper-middle, [310,451,1493,621]','Toute extension splittée G de un Gamma par un Z provient par image inverse')
inv('I05','deletion','within remark, [1010,550,1079,586]','une, uncertain canceled underform')
inv('I06','display','left below remark, [280,656,532,720]','Z.Aut(Z).')
inv('I07','drawing','right of formula, [1147,648,1166,667]','Two detached small traces, writing status uncertain','unnamed hand')
inv('I08','drawing','above section 4, [780,763,1027,808]','Two divider strokes')
inv('I09','drawing','below lower divider endpoint, [1002,796,1015,809]','Tiny detached point, writing status uncertain','unnamed hand')
inv('I10','drawing','right of divider, [1304,783,1327,803]','Remote point, writing status uncertain','unnamed hand')
inv('I11','text','section heading, [301,892,1162,980]','4) Ens. de petit cardinal')
inv('I12','text','subsection a heading, [296,1074,638,1148]','a) Cardinal 2, underlined')
inv('I13','text','same baseline as a and continuing below fold, [343,1077,1627,1569]','Ens de cardinal 2, correspondence with a torseur, then two ou encore phrases')
inv('I14','deletion','underlined phrase, [1016,1199,1094,1234]','sous/sur, live-versus-canceled status uncertain')
inv('I15','deletion','overwritten first field letter, [1111,1185,1167,1242]','Z-like underform below F2')
inv('I16','deletion','after second encore, [1426,1208,1541,1242]','One physically unreadable canceled word')
inv('I17','drawing','underlined phrase, [654,1243,1121,1262]','Underline below espace affine and uncertain preposition')
inv('I18','display','box, [576,1595,1249,1680]','Aff(1,F2) simeq Aff(Z2) simeq S2')
inv('I19','drawing','enclosure, [526,1560,1278,1718]','Two bent border strokes with unjoined corners')
inv('I20','display','below right of box, [900,1707,1189,1798]','(A2 = {1})')
inv('I21','text','subsection b heading, [328,1781,676,1856]','b) Cardinal 3, underlined')
inv('I22','display','lower comparison chain, [519,1878,1500,1955]','S3 simeq Aff(1,F3) simeq Gl(2,F2) simeq GP(1,F2)')
inv('I23','display','below Aff term, [727,1957,875,2131]','Rotated comparison; F3-plus . F3-star; two vertical comparisons; Z3 and Z2')
inv('I24','display','below GP term, [1270,1950,1551,2059]','Rotated equals and Gl(2,F2)/F2-star')
inv('I25','display','last formula, [554,2149,987,2233]','A3 simeq F3-plus (simeq Z3)')
inv('I26','deletion','last field letter, [726,2154,798,2218]','Z-like underform below F3-plus')
inv('I27','margin note','lower-left corner, [45,2277,114,2328]','Archive foliation 12; recorded only as a TeX comment','unnamed hand')

notation=[
 dict(sign='Z / double-stroked Z',reading=r'Z above; \mathbb{Z}_2 and \mathbb{Z}_3 below',ink='The upper extension objects use a single diagonal. Lower group symbols have a distinct second diagonal. Each overwritten underform remains locally uncertain.',place='top diagram and remark; cardinal-2 and cardinal-3 formulas'),
 dict(sign='G, Gamma, primes',reading=r'G,\Gamma,G\prime,\Gamma\prime',ink='G is open and rounded with a small return; Gamma has an upright and upper arm; primes are separate raised ticks.',place='top diagram'),
 dict(sign='2-like vertical-arrow label',reading=r'\unsure{2|\wr}',ink='One small hooked form and rightward foot, without a separate i/d pair.',place='right of left upward arrow'),
 dict(sign='F',reading=r'\mathbb{F}',ink='Two neighboring uprights with top and middle bars; the visible live F is secure at both over-writings.',place='all field occurrences in subsection a and b'),
 dict(sign='Decorative S',reading=r'\unsure{\mathfrak{S}|\mathcal{S}}, then \mathfrak{S}',ink='Broad outer sweep, inner lower return, raised tip at right.',place='boxed S2; first term of subsection b'),
 dict(sign='Open-bowl A',reading=r'\unsure{\mathcal{A}|A}, then \mathcal{A}',ink='Smooth open bowl with a short internal right upright.',place='parenthetical A2; final A3'),
 dict(sign='Comparison signs',reading=r'\simeq; vertical \rotatebox{90}{$\simeq$}; vertical equals',ink='Horizontal comparisons have a wave above a separate bar. Vertical connectors likewise use two strokes; the lower-left one is overinked and remains unsure{simeq|=}.',place='box and subsection b'),
 dict(sign='Product point',reading='.',ink='Detached point lies near the operand baseline rather than at mid-height.',place='Z.Aut(Z) and F3-plus . F3-star'),
 dict(sign='Plus / star',reading=r'^{+}, ^{*}',ink='Raised cross after the additive field; raised asterisk after the multiplicative field. The first plus in the lower stack is heavily reinforced.',place='subsection b'),
 dict(sign='Gl / GP',reading=r'\operatorname{Gl},\operatorname{GP}',ink='The first name has a narrow tall l; the later name has an upright P. The GP G is heavily inked without a distinct doubled alphabet.',place='lower right chain and quotient'),
]
abbreviations=[
 dict(written='ext.',expansion='extension'),dict(written='Rmq',expansion='Remarque'),dict(written='Ens.',expansion='Ensembles'),dict(written='Ens',expansion='Ensemble(s)'),dict(written='dim',expansion='dimension'),dict(written='vect.',expansion='vectoriels'),dict(written='can.',expansion='canoniquement')]

unresolved=[
 dict(id='C01',place='top left vertical-arrow label',reading='2-like form',alternatives='2 | vertical wriggle',confidence='medium'),
 dict(id='C02',place='first sentence after (E)',reading='splitte',alternatives='splitte | splitt.',confidence='medium'),
 dict(id='C04',place="canceled word before l'ext.",reading='une',alternatives='une (probable; obscured middle)',confidence='medium'),
 dict(id='C05',place='after torseur',reading='sur',alternatives='sur | sous',confidence='medium'),
 dict(id='C06',place='after underlined espace affine',reading='canceled sous',alternatives='canceled sous | canceled sur | live sous | live sur',confidence='low'),
 dict(id='C07',place='first overwritten field letter',reading='double-stroked Z under F2',alternatives='double-stroked Z | plain Z',confidence='medium'),
 dict(id='C08',place='after second ou encore',reading='one unreadable canceled word',alternatives='no defensible lexical candidate',confidence='low'),
 dict(id='C09',place='boxed S alphabet, recurring in b',reading='Fraktur S',alternatives='Fraktur S | calligraphic S',confidence='medium'),
 dict(id='C11',place='A alphabet, first at A2 and recurring at A3',reading='calligraphic A',alternatives='calligraphic A | plain cursive A',confidence='medium'),
 dict(id='C12',place='left lower vertical comparison',reading='rotated simeq',alternatives='rotated simeq | rotated equals',confidence='low'),
 dict(id='C13',place='last overwritten field letter',reading='double-stroked Z under F3',alternatives='double-stroked Z | plain Z',confidence='medium'),
 dict(id='F18',place='noun before sur/sous',reading='torseur',alternatives='torseur | torseurs',confidence='medium'),
 dict(id='F24',place='detached two-part trace right of Z.Aut(Z)',reading='two drawn traces, no assigned sign',alternatives='writing/stray ink | surface trace',confidence='low'),
 dict(id='F25',place='two points near/right of divider',reading='two geometrically preserved points',alternatives='writing/stray ink | surface traces',confidence='low'),
]

report=dict(scan='013',reader='R1',start_utc='2026-11-20 03:35:34 UTC',end_utc=None,
 images_viewed=[
 '/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013.jpg',
 '/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013_a.jpg',
 '/workspace/scratch/be39e9f81d6d/source/SP38_CW_75_scans/J75-02_75_scan013_b.jpg'],
 reading_file=str(root/'reading.tex'),crop_count=13,findings=findings,inventory=inventory,notation=notation,abbreviations=abbreviations,
 notes=[
 'This manuscript page continues a discussion of extensions, states a splitting observation, and adds a raised Rmq about a split extension being obtained by inverse image from Z.Aut(Z).',
 'The internal section heading is 4) Ens. de petit cardinal, with a) Cardinal 2 and b) Cardinal 3. No date or manuscript page number is visible. The lower-left 12 is archive foliation and is only a TeX comment; its writer is recorded as unnamed.',
 'No explicit author question mark or doubt word was identified. The uncertainties in this return are reader doubts. The closing ellipsis in subsection a is written and retained.',
 'The nonstandard de un Gamma is written, as is par un Z. No grammatical correction has been made.',
 'The only definite forward arrowhead in the top horizontal rows is on the upper first connection; seven horizontal shafts remain headless. All three vertical arrows point upward.',
 'The contracted label Rmq is resolved from half a. Its raised placement and curved headless lead are reproduced in TikZ; it is not expanded in the reading.',
 'C doubts are numbered in textual order, including the illegible-word locus: C01 arrow label, C02 splitte, C03 Rmq, C04 une, C05 sur/sous, C06 canceled/live preposition, C07 first Z underform, C08 unreadable canceled word, C09 S alphabet, C10 S index, C11 A alphabet, C12 lower rotated comparison, C13 final Z underform. C09 and C10 explicitly separate the outer and nested doubts.',
 'H bold encodings for double-stroked fields/groups, emphasis macro choices for underlining, page marker 12, and its descriptive lower-sign note are not counted as added manuscript text or macro-only errors. The H lower wr notation is treated as its vertical-isomorphism encoding; the ink is rendered with its visible rotated two-stroke comparison.',
 'The boxed index resolves to 2 by its hooked entry and low foot. Group-order consistency was checked afterward and did not select the glyph. The extension diagram does not itself settle the uncertain vertical label; no identity map was supplied from mathematical expectation.',
 'The small detached marks near the formula/divider are preserved as geometry without a punctuation value. Their status as writing rather than stray ink or surface traces remains open.',
 'S.json is an empty array, so there are no S rows to confirm or overturn. The packet contains no H_drawings supplement.',
 'No OCR, recognition software, PDF text, web source, other page, other reader work, compilation or installation was used. The whole and each supplied half were viewed once, followed by 13 separately recorded tight crops.'
 ],
 checks=[
 dict(statement='Aff(1,F2), Aff(Z2), and S2 have the displayed order-2 identification; A2 is trivial.',event_type='actual finite-group calculation',reasoning='In F2 the only nonzero multiplier is 1, so x maps to x+b gives exactly two affine permutations. An automorphism of the additive group Z2 fixes its unique nonidentity element, leaving the same two translations. The two permutations of a two-element set contain only the identity as an even permutation.',outcome='The displayed claims are consistent under the usual meanings of these symbols.'),
 dict(statement='The groups Aff(1,F3) and Gl(2,F2) each identify with the permutations of a three-element set.',event_type='actual finite-group calculation',reasoning='Aff(1,F3) has 3 choices of translation and 2 nonzero multipliers, giving 6 distinct permutations of F3. In dimension 2 over F2 an ordered basis has 3 choices of first nonzero vector and 2 choices outside its span, giving 6 invertible matrices; their action on the 3 nonzero vectors is faithful. Each action therefore exhausts S3.',outcome='The order and action checks support the displayed comparison chain without deciding any uncertain handwriting.'),
 dict(statement='F3-plus is cyclic of order 3, F3-star is cyclic of order 2, and the F2-star quotient does not change Gl(2,F2).',event_type='actual arithmetic and quotient check',reasoning='Addition modulo 3 cycles through 0,1,2. The nonzero residues modulo 3 are 1 and 2, with 2 squared equal to 1. The only nonzero residue in F2 is 1, so the scalar subgroup in the displayed quotient is trivial. The even permutations on three letters are the identity and the two 3-cycles, hence form a cyclic order-3 group.',outcome='The lower group identifications and final A3 statement are consistent. This does not choose rotated simeq versus equals or an alphabet for A.'),
 dict(statement='One-dimensional vector spaces over F2 have a unique linear isomorphism between them.',event_type='actual small-vector-space check',reasoning='Each such space has exactly one nonzero vector. A linear isomorphism must send that vector to the sole nonzero vector of the target, and this assignment is linear and bijective.',outcome='The written can. isomorphes claim is verified for the stated field and dimension.')
 ],unresolved=unresolved,
 self_check={'complete_text_and_geometry_review':True,'original_C_doubts_mapped':13,'s_rows_present':0,'whole_viewings':1,'half_viewings':[1,1],'crop_viewings':13,'no_compilation':True})
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
manifest=json.loads((root/'crop_manifest.json').read_text())
for i,item in enumerate(manifest['crops'],1):
    item['visually_inspected']=True
    item['inspection_order']=i
manifest['crops'][12]['additional_observation']='The context also exposed a tiny point below the lower divider endpoint; it was inspected in this same crop, not recropped.'
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex, report.json, and inspected crop manifest.')
