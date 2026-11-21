from pathlib import Path
import csv
import json
import os

ROOT = Path('/workspace/scratch/b12af914b284')
OUT = ROOT / 'edition/reader_returns'
INDEX = ROOT / 'edition/scripts/150_scan064_crop_index.json'
index = json.loads(INDEX.read_text())
index['crops']['p25_enfait'] = [1368, 1150, 1670, 1250]
boxes = index['crops']

diagram = r'''\diagram{\begin{tikzcd}[column sep=9mm,row sep=13mm,arrows={line width=.6pt},execute at end picture={
% Upper b: four separate hook components, with unequal lengths.
\draw[line width=.7pt,line cap=round] ([xshift=7.1pt,yshift=6.0pt]s64upper.east) -- ([xshift=8.6pt,yshift=6.6pt]s64upper.east);
\draw[line width=.6pt,line cap=round] ([xshift=5.3pt,yshift=4.6pt]s64upper.east) -- ([xshift=4.6pt,yshift=3.6pt]s64upper.east);
\draw[line width=.6pt,line cap=round] ([xshift=4.3pt,yshift=2.5pt]s64upper.east) .. controls +(0pt,-1.5pt) and +(-1pt,0pt) .. ([xshift=5.4pt,yshift=.8pt]s64upper.east);
\draw[line width=.6pt,line cap=round] ([xshift=6.4pt,yshift=.5pt]s64upper.east) .. controls +(.5pt,.2pt) and +(-.5pt,0pt) .. ([xshift=7.6pt,yshift=.8pt]s64upper.east);
% Central b-prime: four components; the second one is visibly faint.
\draw[line width=.6pt,line cap=round] ([xshift=7.2pt,yshift=6.2pt]s64centre.east) -- ([xshift=8.2pt,yshift=6.8pt]s64centre.east);
\draw[line width=.4pt,black!45,line cap=round] ([xshift=5.9pt,yshift=5.3pt]s64centre.east) -- ([xshift=5.2pt,yshift=4.5pt]s64centre.east);
\draw[line width=.6pt,line cap=round] ([xshift=4.4pt,yshift=3.3pt]s64centre.east) .. controls +(0pt,-1.5pt) and +(-.2pt,.5pt) .. ([xshift=4.4pt,yshift=1.6pt]s64centre.east);
\draw[line width=.6pt,line cap=round] ([xshift=5.3pt,yshift=1.0pt]s64centre.east) -- ([xshift=7.1pt,yshift=.6pt]s64centre.east);
% Upper-right b: three detached pieces at the source.
\draw[line width=.6pt,line cap=round] ([xshift=-8.7pt,yshift=4.8pt]s64right.north west) .. controls +(-.7pt,.9pt) and +(0pt,-.5pt) .. ([xshift=-9.1pt,yshift=6.0pt]s64right.north west);
\draw[line width=.6pt,line cap=round] ([xshift=-8.0pt,yshift=3.8pt]s64right.north west) -- ([xshift=-6.7pt,yshift=3.1pt]s64right.north west);
\draw[line width=.6pt,line cap=round] ([xshift=-5.6pt,yshift=3.0pt]s64right.north west) .. controls +(.6pt,0pt) and +(-.4pt,-.4pt) .. ([xshift=-4.5pt,yshift=3.5pt]s64right.north west);
% Lower b: one detached upper curl, and one lower bend joined to the shaft.
\draw[line width=.7pt,line cap=round] ([xshift=4.7pt,yshift=4.1pt]s64lower.east) .. controls +(0pt,1pt) and +(-.8pt,.4pt) .. ([xshift=6.4pt,yshift=5.3pt]s64lower.east);
\draw[line width=.6pt,line cap=round] ([xshift=4.0pt,yshift=2.4pt]s64lower.east) .. controls +(-.2pt,-2.6pt) and +(-2pt,0pt) .. ([xshift=7pt]s64lower.east);
% s-prime: two unequal visible shafts merge at one head.  Its source curl
% comprises a long U-like part and a separate right arc, with a pen gap.
\draw[->,line width=.85pt,line cap=round] ([xshift=-2.5pt,yshift=8.0pt]s64centre.north west) -- ([yshift=-2pt]s64upper.south east);
\draw[line width=.5pt,line cap=round] ([xshift=.8pt,yshift=9.1pt]s64centre.north west) .. controls +(-3pt,4pt) and +(4pt,-3pt) .. ([yshift=-2pt]s64upper.south east);
\draw[line width=.7pt,line cap=round] ([xshift=-10pt,yshift=7pt]s64centre.north west) .. controls +(0pt,-3pt) and +(-2pt,0pt) .. ([xshift=-3.5pt,yshift=4.5pt]s64centre.north west) .. controls +(1.5pt,0pt) and +(0pt,-1.3pt) .. ([xshift=-2pt,yshift=6.3pt]s64centre.north west);
\draw[line width=.6pt,line cap=round] ([xshift=-.8pt,yshift=5.1pt]s64centre.north west) .. controls +(2.1pt,.6pt) and +(1pt,-1pt) .. ([xshift=1.2pt,yshift=8.0pt]s64centre.north west);
\node[anchor=east] at ([xshift=-18mm,yshift=3pt]s64left.west) {$(40)$};
\node[anchor=west] at ([xshift=34mm,yshift=-3mm]s64bottom.east) {,};
}]
&|[alias=s64upper]|\Sigma^{\unsure{<|*}}(1)\arrow[rr,"\uline{b}",start anchor=east,shorten <=9pt]\arrow[dl,"\uline{s}"']&&|[alias=s64top]|\Sigma&\\
|[alias=s64left]|\Sigma&&|[alias=s64centre]|\Sigma^{*}(2)\arrow[ul,phantom,"\uline{s'}"']\arrow[rr,"\uline{b}'",start anchor=east,shorten <=9pt]\arrow[dl,"\uline{p}"']\arrow[ur,phantom,"\text{cart}" description]\arrow[dr,phantom,"\text{cart}" description]&&|[alias=s64right]|\Sigma^{\unsure{<|*}}(1)\arrow[ul,"\uline{b}"',start anchor=north west,shorten <=7pt]\arrow[dl,"\uline{s}"]\\
&|[alias=s64lower]|\Sigma^{\unsure{<|*}}(1)\arrow[ul,"\uline{s}"']\arrow[rr,"\uline{b}",start anchor=east,shorten <=7pt]&&|[alias=s64bottom]|\Sigma&
\end{tikzcd}}'''

legend = r'''\diagram{\begin{tikzcd}[column sep=large,arrows={line width=.6pt},execute at end picture={
% Four disconnected marks: an upper slant, then three short dot-like pieces.
\draw[line width=.7pt,line cap=round] ([xshift=6.3pt,yshift=6.1pt]s64legend.east) -- ([xshift=8pt,yshift=6.8pt]s64legend.east);
\fill ([xshift=5.1pt,yshift=4.8pt]s64legend.east) circle[radius=.48pt];
\fill ([xshift=5.3pt,yshift=3.1pt]s64legend.east) circle[radius=.48pt];
\fill ([xshift=6pt,yshift=1.7pt]s64legend.east) circle[radius=.43pt];}]
|[alias=s64legend]|{}\arrow[r,start anchor=east,shorten <=8pt]&{}
\end{tikzcd}}'''

margin = r'''\margin{donc, dans le cas de $\uline{p}:\Sigma^{\unsure{<|*}}(2)\mathrel{\unsure{-|\longrightarrow}}\Sigma^{\unsure{*|<}}(1)$,
le fibré des bords est l'image de $\Sigma^{\unsure{<|*}}(3)$}'''

lower = r'''fibrantes et propres \unsure{\}} (\unsure{voire|voir}, de plus : fibres
des variétés à bord, dont le bord est
dans le cas de $\unsure{\uline{s}|\uline{s'}}:\Sigma^{\unsure{<|*}}(1)\longrightarrow\Sigma$, l'image
% A short dark raised stroke above this s may be a pen-start or a prime;
% both readings are retained.  No identification with the later s-prime is imposed.
de $\Sigma^{\unsure{<|*}}(2)\overset{\uline{s'}}{-}\Sigma^{*}(1)$
% The initial curve before i.e. continues below the insertion and into its
% long leader.  It is not separately repeated as a literal parenthesis.
\inserted{i.e. l'ens des $(x\prec y)$ tels que $y$ \uline{ne soit pas} successeur de $x$}).
% The insertion is above this map; successeur de x wraps at its right end.
% The following note is oblique in the left margin beside the fibre/boundary passage.
''' + margin + r'''
On fera attention
que les applications fibrantes $\uline{s},\uline{p}$ n'ont \deleted{\unsure{rien}}\inserted{rien}
de surjectif --- l'image de $\unsure{\uline{s}|s}$ est formé des $x\in\Sigma$
qui \uline{ne sont pas maximaux}, celle de $p$ est formé
des $(x\prec y)$ tels que $y$ ne soit pas maximal.
% Pale bottom-left foliation, another hand; no authorial page number at the head.
\margin{63}'''

tex = r'''\scanpage{64}
Les morphismes les plus importants dans la
situation apparaissent dans le diagramme
% The curved leader attaches hexagonal immediately before the live suivant.
\inserted{hexagonal} suivant
''' + diagram + r'''

où les flèches marquées ''' + legend + r''' (en fait,
$\uline{b},\deleted{\unsure{p_2}},\uline{b'},\uline{s'}$) sont des immersions bordantes \inserted{propres},
% propres is above bordantes; its surrounding curve continues into the
% insertion leader, ending after bordantes before the separate comma.
et les flèches marquées $\longrightarrow$ (en fait,
$\uline{s}$ et $\uline{p}$) sont (dans le cas équisingulier)
''' + lower + '\n'

changes = []
def change(place, C, H, final, against_C, against_H, kind, cat, conf, crop, evidence, marked=False, consequence=''):
    changes.append(dict(id=f'064-{len(changes)+1:02}', place=place, C=C, H=H, final=final,
        against_C=against_C, against_H=against_H, kind=kind, error_category=cat,
        marked_in_H=marked, confidence=conf, evidence=evidence,
        crop=f'crops/150_scan064_{crop}.png', box=boxes[crop], mathematical_consequence=consequence))

change('opening line, after importants', 'de la', 'dans la', 'dans la', True, False, 'misread word', 'Words', 'high', 'p01_de_la',
       'After d there is a low connected ns-like continuation before the separate tall l of la; the extent exceeds the two-letter de reading. Root independently agrees.')
change('opening insertion before suivant', r'\inserted{hexagonal} suivant', r'\add{hexagonal suivant}', r'\inserted{hexagonal} suivant', False, True, 'insertion or placement', 'Insertions put in the wrong place', 'high', 'p02_hexagonal',
       'hexagonal is written above the baseline. Its curved leader ends just before the live suivant; suivant is on the main baseline and outside the insertion.')
for place, crop in [('upper indexed node','p04_upper_map'),('right indexed node','p06_centre_right'),('lower indexed node','p09_bottom_map')]:
    change('diagram (40), '+place, r'\Sigma^{<}(1)', r'\Sigma^{*}(1)', r'\Sigma^{\unsure{<|*}}(1)', False, True, 'misread symbol or index', 'Symbols and indices', 'low', crop,
           'The raised sign has compact angular/curved arms and is crowded against the opening parenthesis. The leading local candidate is <; a compressed star remains open. This comparison records the leading proposal rather than a settled rejection of H.', consequence='The written superscript of this node remains unresolved.')
change('diagram (40), central node', r'\Sigma^{<}(2)', r'\Sigma^{*}(2)', r'\Sigma^{*}(2)', True, False, 'misread symbol or index', 'Symbols and indices', 'high', 'p05_sprime',
       'The small raised mark at the central Sigma has visibly crossing arms. The following numeral is a looped 2.', consequence='The central object is transcribed with the locally visible star.')
change('diagram (40), direction of s-prime edge', r'\arrow[ul,hook,"\uline{s\'}"]', r'\arrow[u, hook, "\underline s\'"]', 'central node to upper-left indexed node, diagonal up-left', False, True, 'drawing or diagram', 'Drawings and diagrams', 'high', 'p03_diagram',
       'The central indexed object lies to the right of the upper indexed object; both retraced shafts run diagonally up-left into one head. H’s vertical u setting does not reproduce that alignment.')
change('diagram (40), equation number', '(40) after the diagram', '(40) before the diagram; note: le numéro (40) à gauche', '(40) to the left of the diagram', True, False, 'insertion or placement', 'Insertions put in the wrong place', 'high', 'p03_diagram',
       'The parenthesised digits 4 and 0 sit far to the left of the left bare Sigma, near the central row. H’s explanatory note explicitly records that position.')
for place, C, H, crop, final, evidence in [
    ('upper b source hook',r'\draw[densely dotted] ([xshift=7pt]s64upper.east) arc[start angle=270,end angle=90,radius=3pt];',r'\arrow[r, hook, "\underline b"]','p04_upper_map','four disconnected, unequal hook pieces','An upper slant, a short upper-left piece, a lower-left bent piece and a short lower piece are separated by white gaps.'),
    ('central b-prime source hook',r'\draw[densely dotted] ([xshift=7pt]s64centre.east) arc[start angle=270,end angle=90,radius=3pt];',r'\arrow[rr, hook, "\underline b\'"]','p06_centre_right','four disconnected hook pieces, one faint','There are four separate pieces; the upper-middle stroke is pale grey between the dark upper slant and lower-left piece.'),
    ('upper-right b source hook',r'\draw[densely dotted] ([xshift=-5pt,yshift=5pt]s64right.north west) arc[start angle=135,end angle=315,radius=3pt];',r'\arrow[ul, hook, "\underline b"\']','p07_upperright','three disconnected hook pieces','A short upright/curled piece, a lower-left slant and a lower-right curved piece remain separated.'),
    ('lower b source hook',r'\draw[densely dotted] ([xshift=7pt]s64lower.east) arc[start angle=270,end angle=90,radius=3pt];',r'\arrow[r, hook, "\underline b"]','p09_bottom_map','detached upper curl; lower bend continuous with the shaft','The small upper curl is detached. The lower left bend runs without a pen gap into the horizontal shaft.')]:
    change('diagram (40), '+place, C, H, final, True, True, 'drawing or diagram', 'Drawings and diagrams', 'high', crop,
           evidence+' The proposed TikZ paths retain these component counts and their unequal lengths instead of a uniform dotted or smooth arc.')
change('diagram (40), s-prime shaft and source curl', r'\arrow[ul,hook,"\uline{s\'}"]', r'\arrow[u, hook, "\underline s\'"]', 'one edge with two unequal visible shafts merging at one head; U-like source curve plus separate right arc', True, True, 'drawing or diagram', 'Drawings and diagrams', 'high', 'p05_sprime',
       'Two dark paths with unequal source endpoints converge into one upper-left head. The source decoration has a long U-like component and a separate right arc, with a visible gap. The return draws the two paths with different weights; it does not assign two mathematical edges.')
change('diagram (40), lower horizontal b label side', r'\arrow[rr,"\uline{b}"\',start anchor=east,shorten <=7pt]', r'\arrow[r, hook, "\underline b"]', r'\uline{b} above the lower horizontal shaft', True, False, 'insertion or placement', 'Insertions put in the wrong place', 'high', 'p09_bottom_map',
       'The b and its short underline are above the lower horizontal shaft. C’s swapped label option places them below it.')
change('diagram (40), s-prime label side', r'\arrow[ul,hook,"\uline{s\'}"]', r'\arrow[u, hook, "\underline s\'"]', r'\uline{s\'} to the upper/right of the slanted shaft', True, True, 'insertion or placement', 'Insertions put in the wrong place', 'high', 'p05_sprime',
       'The s-prime label is on the right/upper side of the up-left shaft. Its underline extends horizontally beneath the prime’s position.')
change('diagram (40), lower-left s label side', r'\arrow[ul,"\uline{s}"]', r'\arrow[ul, "\underline s"]', r'\uline{s} above/right of the lower-left arrow', True, True, 'insertion or placement', 'Insertions put in the wrong place', 'high', 'p03_diagram',
       'The underlined s lies above/right of the shaft from the lower indexed node to the left bare Sigma.')
change('diagram (40), b-prime underline scope', r'\uline{b\'}', r'\underline b\'', r'\uline{b}\'', True, False, 'other', 'Other', 'high', 'p06_centre_right',
       'The horizontal underline ends beneath b, before the raised prime. This local scope differs from the longer s-prime underline.')
change('diagram (40), p edge and label', r'\arrow[dl,"p"\']', r'\arrow[d, "p_2"\']', r'\arrow[dl,"\uline{p}"\']', True, True, 'misread symbol or index', 'Symbols and indices', 'high', 'p08_p_arrow',
       'A p with a separate short horizontal bar below/right of its bowl labels the diagonal down-left shaft. No curved numeral 2 is visible. The p descender extends below the offset underline.', consequence='The label retains a written bar on p rather than the index 2 given by H.')
change('diagram (40), trailing comma', r'\end{tikzcd}},', r'\end{tikzcd}', 'comma at the lower right of the figure', True, True, 'insertion or placement', 'Insertions put in the wrong place', 'high', 'p03_diagram',
       'A separate comma sits beyond and below the lower-right region of the figure. It is drawn at that position in the proposed setting.')
change('first arrow legend', r'\draw[densely dotted] ([xshift=7pt]s64legend.east) arc[start angle=270,end angle=90,radius=3pt];', r'\hookrightarrow', 'rightward arrow with four detached source marks', True, True, 'drawing or diagram', 'Drawings and diagrams', 'high', 'p10_legend',
       'One upper slanted segment is followed by three distinct dot-like pieces around the source. All four are separate from one another and from the shaft; the terminal right head is clear.')
change('first en fait punctuation', '(en fait,', '(en fait', '(en fait,', False, True, 'omission', 'Omissions', 'high', 'p25_enfait',
       'A separate low curved comma follows fait at the right edge. It is independent of the t stroke; root confirmed it on p25.')
change('cancelled label in the b/b-prime/s-prime list', r'\deleted{\unsure{p_2}}', r'\struck{\ill{}}', r'\deleted{\unsure{p_2}}', False, True, r'readable ink left as \ill{}', 'Readable ink left as illegible', 'low', 'p11_blist_cancel',
       'Under the cancellation a looped p-like stem and a low 2-like curve remain partly legible. Crossing strokes prevent secure separation of every stroke, so p_2 remains explicitly doubtful; no underline is independently forced through the crossing.', marked=True, consequence='The tentative cancelled map label is retained as p_2 with doubt.')
change('inserted propres, punctuation', r'\inserted{propres}', r'\add{(propres)}', r'\inserted{propres}', False, True, 'text not on the page', 'Text that is not on the page', 'high', 'p12_propres',
       'The apparent left parenthesis runs continuously beneath the word into a long insertion leader, ending after bordantes. There is no separate closing parenthesis paired with it.')
change('inserted propres, attachment before comma', r'bordantes, \inserted{propres}', r'bordantes \add{(propres)},', r'bordantes \inserted{propres},', True, False, 'insertion or placement', 'Insertions put in the wrong place', 'medium', 'p12_propres',
       'The leader ends after the live bordantes, above the separate low comma. The insertion is placed between the word and that comma; its words are recorded separately from the surrounding leader.')
change('second parenthetical list, s et p', '$p$', '$p_2$', r'$\uline{p}$', True, True, 'misread symbol or index', 'Symbols and indices', 'high', 'p13_s_et_p',
       'The p is followed at a slightly lower level by a short straight horizontal bar, with no curved body or upper arm of a 2.', consequence='The second named label is transcribed with its written bar, without an index 2.')
change('after fibrantes et propres, M0606', r'\unsure{\}}', '(nothing)', r'\unsure{\}}', False, True, 'omission', 'Omissions', 'low', 'p14_brace_voire',
       'A dark, overdrawn upright with a curled top and lower left return stands before the opening parenthesis. The brace-like reading is retained without resolving the overdrawn form.')
change('parenthetical word after the overdrawn brace', 'voire', 'voir', r'\unsure{voire|voir}', False, True, 'misread word', 'Words', 'low', 'p14_brace_voire',
       'The letters voi and following r-like movement are visible; the terminal low compressed return does not securely separate a final e. The leading voire preserves C while voir remains open.')
change('after fibres', 'des variétés', 'variétés', 'des variétés', False, True, 'omission', 'Omissions', 'high', 'p15_des_varietes',
       'Before variétés is a separate connected des group: a looped initial d and low continuing e/s strokes. It is live text despite the nearby oblique marginal writing.')
change('body s map, source exponent', r'\Sigma^{<}(1)', r'\Sigma^{*}(1)', r'\Sigma^{\unsure{<|*}}(1)', False, True, 'misread symbol or index', 'Symbols and indices', 'low', 'p16_smap',
       'The raised sign has a compact left-pointing movement and joins the opening-parenthesis region. < is the leading local candidate; * remains an explicit alternative.', consequence='This source superscript remains unresolved.')
change('body s map, comma after target Sigma', r'\Sigma$, l\'image', r'\Sigma$ l\'image', r'\Sigma$, l\'image', False, True, 'omission', 'Omissions', 'high', 'p16_smap',
       'A separate low curved comma is visible between the target Sigma and the tall l of l’image.')
change('lower s-prime expression, source exponent', r'\Sigma^{<}(2)', r'\Sigma^{*}(2)', r'\Sigma^{\unsure{<|*}}(2)', False, True, 'misread symbol or index', 'Symbols and indices', 'low', 'p17_lower_smap',
       'A small open curved/angular sign is raised over the source Sigma. Its two-arm < reading leads, but the ink is too compact to eliminate the star alternative.', consequence='The source superscript remains unresolved.')
change('lower s-prime expression, target exponent', r'\Sigma^{<}(1)', r'\Sigma^{*}(1)', r'\Sigma^{*}(1)', True, False, 'misread symbol or index', 'Symbols and indices', 'high', 'p17_lower_smap',
       'The target’s small raised mark has clearly crossing strokes, separated from the opening parenthesis and numeral 1.', consequence='The target is transcribed with the locally crossed star.')
change('lower s-prime expression, shaft', r'\overset{\uline{s\'}}{-}', r'\xrightarrow{\underline s\'}', r'\overset{\uline{s\'}}{-}', False, True, 'misread symbol or index', 'Symbols and indices', 'high', 'p17_lower_smap',
       'The long horizontal stroke under the separately underlined s-prime ends plainly at both sides; no terminal arrowhead is visible.', consequence='The source’s unheaded connector is preserved.')
change('i.e. insertion, surrounding leader', r'\inserted{(i.e. l\'ens des $(x\prec y)$ tels que $y$ \uline{ne soit pas} successeur de $x$)}', r'\add{i.e.\ l\'ens.\ des $(x<y)$ tels que \uncertain{$y$ ne soit pas successeur de $x$}}', r'\inserted{i.e. l\'ens des $(x\prec y)$ tels que $y$ \uline{ne soit pas} successeur de $x$}', True, False, 'insertion or placement', 'Insertions put in the wrong place', 'high', 'p18_insertion',
       'The curve before i.e. continues beneath the first words into the long enclosing insertion leader. At the right the same leader rises around the wrapped ending. No separate pair of parentheses encloses the added text. The main closing parenthesis after the displayed expression remains.')
change('i.e. insertion, abbreviated ens', "l'ens", r"l'ens.", "l'ens", False, True, 'abbreviation expanded or spelling modernised', 'Abbreviations expanded, spelling modernised', 'high', 'p18_insertion',
       'After the final low stroke of ens there is a blank interval before des; no independent stop occurs there.')
change('i.e. insertion, tuple relation', r'(x\prec y)', '(x<y)', r'(x\prec y)', False, True, 'misread symbol or index', 'Symbols and indices', 'high', 'p18_insertion',
       'The left-pointing relation has curved arms. The tuple’s own round parentheses are independently visible.', consequence='The written curved relation is retained as prec.')
change('i.e. insertion, underline', r'\uline{ne soit pas}', 'ne soit pas', r'\uline{ne soit pas}', False, True, 'omission', 'Omissions', 'high', 'p18_insertion',
       'Separate underline strokes run below ne and soit pas. The preceding y has its own descending stroke and is outside this underline scope.', marked=True)
change('left marginal note, beginning', 'donc, dans le cas', 'dans le cas', 'donc, dans le cas', False, True, 'omission', 'Omissions', 'high', 'p19_margin',
       'The first oblique line starts with a looped d, low on and an open c, followed by a comma, before dans le cas.', marked=True)
change('left marginal note, p label', 'p:', 'p_2 :', r'\uline{p}:', True, True, 'misread symbol or index', 'Symbols and indices', 'high', 'p19_margin',
       'The p has a short lower horizontal bar; a separate two-dot colon follows it. No lowered numeral 2 is present beside the p.', marked=True, consequence='The written marginal label carries a short bar, without H’s index 2.')
for place, C, H, final, aC, aH, evidence in [
    ('source',r'\Sigma^{<}(2)',r'\Sigma^{*}(2)',r'\Sigma^{\unsure{<|*}}(2)',False,True,'The source mark has an angular left-pointing movement crowded against the parenthesis; < leads but * remains open.'),
    ('target',r'\Sigma^{<}(1)',r'\Sigma^{*}(1)',r'\Sigma^{\unsure{*|<}}(1)',True,False,'The target mark appears to have short crossing branches, but they crowd against the parenthesis; * leads while < remains open.'),
    ('last expression',r'\Sigma^{<}(3)',r'\Sigma^{*}(3)',r'\Sigma^{\unsure{<|*}}(3)',False,True,'The final raised mark has a visible left angle adjoining the parenthesis; the short extra ink at the join leaves the star alternative open.')]:
    change('left marginal note, '+place+' exponent',C,H,final,aC,aH,'misread symbol or index','Symbols and indices','low','p19_margin',evidence+' The digits 2, 1 and 3 are separately legible in their local expressions.',marked=True,consequence='The local marginal superscript remains unresolved.')
change('left marginal note, connector', r'\longrightarrow', r'\to', r'\mathrel{\unsure{-|\longrightarrow}}', True, True, 'misread symbol or index', 'Symbols and indices', 'low', 'p19_margin',
       'The horizontal shaft ends in a short dark terminal thickening. No independent V-shaped head can be isolated. An unheaded shaft leads; an arrow remains the alternative.', marked=True, consequence='The terminal decoration of the marginal connector remains doubtful.')
change('left marginal note, ending', r'\Sigma^{<}(3)', r'\Sigma^{*}(3)$ \ldots', r'\Sigma^{\unsure{<|*}}(3)', False, True, 'text not on the page', 'Text that is not on the page', 'high', 'p19_margin',
       'The note ends after the closing parenthesis of the expression with numeral 3. No sequence of continuation dots follows it; surrounding isolated curves belong to the neighbouring main text.', marked=True)
change('final paragraph, fibrantes s label', 's', r'\underline s', r'\uline{s}', True, False, 'omission', 'Omissions', 'high', 'p21_labels',
       'The s has a visibly separate short underline, with a white gap between letter and bar. This row records the s underline only; the p comparison is separate.')
change('final paragraph, fibrantes p label', 'p', 'p_2', r'\uline{p}', True, True, 'misread symbol or index', 'Symbols and indices', 'high', 'p21_labels',
       'The p is followed below/right by a straight short bar; its stem continues down past that level. There is no curved numeral 2.', consequence='The written p bar is retained without an index 2.')
change('final paragraph, cancelled word before inserted rien', r'\deleted{\unsure{rien}}', r'\struck{aucune}', r'\deleted{\unsure{rien}}', False, True, 'misread word', 'Words', 'low', 'p20_rien',
       'A separate dot survives over an i-like position beneath the cancellation, with initial r-like movement and low continuing strokes. The heavy crossing conceals the stems and final tall return. rien is the leading surviving reading, still doubtful; the inserted rien above is clear.')
change('l’image de s, underline state', '$s$', r'$\underline s$', r'$\unsure{\uline{s}|s}$', True, False, 'other', 'Other', 'low', 'p22_forme1',
       'A very short lower stroke lies close to, or retraces, the base of the s. The underlined reading leads, but the plain letter remains explicit because the strokes are not cleanly separated. Root independently retained this same doubt.')
change('l’image de s est formé', 'formé', 'formée', 'formé', False, True, 'abbreviation expanded or spelling modernised', 'Abbreviations expanded, spelling modernised', 'high', 'p22_forme1',
       'The word ends in one low e-shaped ending with an accent above it, then a blank before des. There is no second final e.')
change('final paragraph, underline scope', r'\uline{ne sont pas maximaux}', r'ne sont pas \emph{maximaux}', r'\uline{ne sont pas maximaux}', False, True, 'omission', 'Omissions', 'high', 'p23_final',
       'One long underline starts beneath ne and continues beneath sont pas maximaux, ending before the comma. qui lies outside it.')
change('celle de p', '$p$', '$p_2$', '$p$', False, True, 'misread symbol or index', 'Symbols and indices', 'high', 'p23_final',
       'This p is a plain looped letter with a descender. There is no separate lower bar or numeral 2 at this particular occurrence.', consequence='The last p is retained without an index.')
change('celle de p est formé', 'formé', 'formée', 'formé', False, True, 'abbreviation expanded or spelling modernised', 'Abbreviations expanded, spelling modernised', 'high', 'p23_final',
       'The second formé also ends in one accented e-shaped ending. The following line begins des; no second e is written.')
change('last-line tuple', r'(x\prec y)', '(x<y)', r'(x\prec y)', False, True, 'misread symbol or index', 'Symbols and indices', 'high', 'p23_final',
       'The curved left-pointing relation remains visible beneath the nearby long underline. Its upper arm bends before meeting the left cusp.', consequence='The source’s curved relation is retained as prec.')
change('bottom-left foliation', r'\mspage{63}', '(nothing)', r'\margin{63}', True, True, 'other', 'Other', 'high', 'p24_foliation',
       'A pale thin 6 and 3 stand at the bottom-left edge, in a different hand from the dark text. They are retained as foliation, with no authorial page number supplied at the head.')

doubts = []
def doubt(place, reading, alternatives, reason):
    doubts.append(dict(place=place, reading=reading, alternatives=alternatives, confidence='low', reason=reason))
for place, crop in [('diagram upper node','p04_upper_map'),('diagram right node','p06_centre_right'),('diagram lower node','p09_bottom_map'),('body s map source','p16_smap'),('lower s-prime expression source','p17_lower_smap'),('margin source','p19_margin'),('margin final expression','p19_margin')]:
    doubt(place, r'\Sigma^{\unsure{<|*}}', '<; *', f'Compact raised arms close to the following parenthesis; local < leads but the star remains open. Inspected crop {crop}.')
doubt('margin target',r'\Sigma^{\unsure{*|<}}(1)','*; <','Short apparent crossing branches are crowded against the parenthesis; the star leads locally without resolving the angle alternative.')
doubt('cancelled label in first list',r'\deleted{\unsure{p_2}}','p_2; partly unreadable cancelled label','Crossing strokes obscure part of the p-like stem and low 2-like curve; the C doubt is retained.')
doubt('M0606, after fibrantes et propres',r'\unsure{\}}','right brace; unresolved overdrawn mark','The curled upright is heavily overdrawn, so no exact brace glyph is forced. The mark is retained in the text.')
doubt('word after the brace',r'\unsure{voire|voir}','voire; voir','The final low return may be an e or the terminal motion of r; neither completion is imposed.')
doubt('body s map label',r'\unsure{\uline{s}|\uline{s\'}}',r'\uline{s}; \uline{s\'}','A short independent-looking dark stroke sits above/right of the s. It may be a pen-start or a compressed prime. C and H both read s; adding this alternative alone is not counted as a textual change.')
doubt('margin connector',r'\mathrel{\unsure{-|\longrightarrow}}','unheaded shaft; rightward arrow','The terminal thickening has no independently separable V; a head cannot be excluded.')
doubt('cancelled word replaced by rien',r'\deleted{\unsure{rien}}','rien; unresolved crossed letter strokes','The i dot remains, but the heavy cancellation obscures letter stems and the terminal return.')
doubt('l’image de s, underline',r'\unsure{\uline{s}|s}',r'\uline{s}; s','The lower stroke is very close to, or retraces, the s base. The alternative plain s remains open.')

inventory = []
def element(kind, pos, words, hand='his hand', **extra):
    item=dict(element=f'E{len(inventory)+1:02}',kind=kind,position=pos,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes')
    item.update(extra)
    inventory.append(item)
element('text','head, three main baselines','Les morphismes les plus importants dans la situation apparaissent dans le diagramme ... suivant')
element('insertion','above suivant near the left of the third baseline',r'\inserted{hexagonal}',attachment='Curved leader ends immediately before live suivant; no isolated cancellation in morphismes.')
element('diagram','upper-middle sheet, numbered (40) at the left','Seven Sigma nodes; nine directed edges, with one retraced s-prime edge; two cart labels; comma at lower right',details='Top b hook: 4 detached pieces. Central b-prime hook: 4 pieces including one faint. Upper-right b hook: 3 pieces. Bottom b hook: detached upper curl and lower part joined to shaft. s-prime: two shafts merging at one head, source U-like part plus detached right arc. The b-prime underline covers b only; s-prime underline extends under the prime position.')
element('text','below the diagram, first two explanatory baselines','où les flèches marquées ... (en fait, b, [cancelled label], b′, s′) sont des immersions bordantes ... ,')
element('diagram','first explanatory line, arrow legend','Rightward shaft with one terminal head and four separated source-hook pieces')
element('deletion','first explanatory list after underlined b',r'\deleted{\unsure{p_2}}',details='The cancelled label remains partially legible and explicitly doubtful; no independently isolated underline is supplied.')
element('insertion','above bordantes at the right',r'\inserted{propres}',attachment='Continuous leader beneath the word reaches the place after bordantes and before the separate comma; no literal parentheses.')
element('text','next six main baselines, ending with the lower s-prime expression','et les flèches marquées ... fibrantes et propres ... des variétés à bord ... l’image de ...',details='Overdrawn brace, voire/voir, local Sigma forms, the possible raised stroke on s, and the unheaded s-prime shaft are retained with their local states.')
element('insertion','between the two body maps; ending wraps at far right',r"\inserted{i.e. l'ens des $(x\prec y)$ tels que $y$ \uline{ne soit pas} successeur de $x$}",attachment='Long leader runs beneath the words and rises at the right; it attaches after the lower map. The surrounding curve is recorded as an insertion leader, not an extra pair of text parentheses.')
element('margin note','oblique left margin alongside the fibre/boundary passage',margin,details='Four slanted baselines; leading donc, is present. Underlined p, digits 2/1/3, local exponent doubts and the terminal-shaft doubt are retained. No ellipsis supplied.')
element('text','final five main baselines, On fera attention through maximal.','On fera attention que les applications fibrantes ... n’ont ... de surjectif ...',details='s,p after fibrantes are separately underlined. The later s underline is doubtful; the final p is plain. Both occurrences spell formé. The underline covers ne sont pas maximaux.')
element('deletion','final paragraph after n’ont',r'\deleted{\unsure{rien}}',details='Heavy horizontal cancellation, surviving i dot and uncertain terminal return.')
element('insertion','directly above the cancelled word after n’ont',r'\inserted{rien}',attachment='The live replacement is above the cancelled word and is fully legible.')
element('margin note','bottom-left paper edge',r'\margin{63}','another unnamed hand',details='Pale foliation; no dark authorial number is visible at the head.')

def without_comments(s):
    return '\n'.join(line for line in s.splitlines() if not line.lstrip().startswith('%'))

audit = []
def audit_box(kind, box, reading):
    audit.append(dict(box=f'B{len(audit)+1:02}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=without_comments(reading)))
audit_box('lexical disagreement',[1435,75,1654,168],'dans la')
audit_box('insertion',[211,280,537,408],r'\inserted{hexagonal} suivant')
audit_box('doubtful formula; handwritten number; diagram',[145,600,1369,1106],diagram)
audit_box('insertion; struck passage; doubtful formula; handwritten number; lexical disagreement',[280,1148,1674,1390],
    r'où les flèches marquées '+legend+r''' (en fait,
$\uline{b},\deleted{\unsure{p_2}},\uline{b'},\uline{s'}$) sont des immersions bordantes \inserted{propres},''')
audit_box('medium-confidence departure; doubtful formula',[294,1386,1674,1604],r'''et les flèches marquées $\longrightarrow$ (en fait,
$\uline{s}$ et $\uline{p}$) sont (dans le cas équisingulier)''')
audit_box('margin note; insertion; struck passage; doubtful formula; handwritten number; lexical disagreement',[20,1603,1677,2352],lower)

purposes = {
'p00_morphismes':'Review heavy joins/overdrawing for a possible deletion; full word remains live.',
'p01_de_la':'C de la / H dans la lexical difference.',
'p02_hexagonal':'Insertion scope and its attachment before live suivant.',
'p03_diagram':'Whole diagram: all seven nodes, nine edges, indices, number 40, cart labels, source decorations and trailing comma.',
'p04_upper_map':'Upper whole map: compact exponent, digit 1, b label and four-part source hook.',
'p05_sprime':'Whole s-prime edge and adjacent nodes: central star, digit 2, retraced shafts, one head and split source curl.',
'p06_centre_right':'Central-to-right map: both exponents, b-prime underline scope and four-part hook.',
'p07_upperright':'Whole upper-right diagonal map: b underline, terminal head and three-part source hook.',
'p08_p_arrow':'Whole downward-left p edge: label bar versus digit 2 and both endpoint objects.',
'p09_bottom_map':'Whole lower map: digit 1, local exponent, b above shaft, detached upper curl and attached lower bend.',
'p10_legend':'Arrow legend: four separate source marks and terminal head.',
'p11_blist_cancel':'Cancelled p_2 versus H illegible; underlines, primes and cancellation state.',
'p12_propres':'Inserted propres, continuous leader versus literal parentheses, and comma attachment.',
'p13_s_et_p':'Underlined p versus p_2 in second parenthetical list.',
'p14_brace_voire':'M0606 overdrawn brace and lexical voire/voir difference.',
'p15_des_varietes':'Presence of des before variétés.',
'p16_smap':'Whole s map: raised mark above s, compact exponent, digit 1, arrow and comma.',
'p17_lower_smap':'Whole lower s-prime expression: source exponent, digits 2 and 1, target star, underline and unheaded shaft.',
'p18_insertion':'Complete small i.e. insertion: leader, abbreviated ens, curved relation, underline and wrapped ending.',
'p19_margin':'Entire oblique margin note, rotated -40 degrees: words, bars, exponents, shaft, digits 2/1/3 and absence of ellipsis.',
'p20_rien':'Cancelled rien/aucune difference and live inserted rien.',
'p21_labels':'s and p underlines in applications fibrantes; bar versus numeral 2.',
'p22_forme1':'First formé/formée difference and doubtful s underline.',
'p23_final':'Second formé/formée, plain final p, underline scope, final tuple and full stop.',
'p24_foliation':'Other-hand bottom foliation 63.',
'p25_enfait':'Separate comma after first en fait, omitted by H.'}

record = dict(
    scan='064', reader='reader_b', line_count=15,
    changes=changes,
    decisions=[dict(id='M0606',decision='undecided',reading=r'\unsure{\}}',
        evidence='The mark after propres is a densely overdrawn upright with curled upper and lower parts. The right-brace candidate remains possible, but its exact form cannot be resolved from the crop.',
        crop='crops/150_scan064_p14_brace_voire.png',box=boxes['p14_brace_voire'],confidence='low')],
    inventory=inventory,doubts=doubts,
    notes=[
      dict(id='150-064-N01',text='The author introduces a hexagonal diagram numbered (40), writes two interior cart labels, and describes the marked b, b-prime and s-prime morphisms as immersions bordantes, with propres inserted. The following paragraph calls s and the barred p fibrantes et propres in the stated équisingulier case, and describes the boundaries of fibres by images of the written Sigma expressions. These are reports of the manuscript’s assertions; no proof or separate mathematical verification was performed.'),
      dict(id='150-064-N02',text='The added i.e. explanation describes pairs (x prec y) for which y ne soit pas successeur de x. The oblique note begins donc, and describes the fibré des bords as an image of a Sigma expression with argument 3. The final paragraph says the fibrating applications have rien de surjectif, then describes the image of s using nonmaximal x and the image of p using pairs with nonmaximal y. Both occurrences of formé are retained exactly; they were not regularised to formée.'),
      dict(id='150-064-N03',text='There is no visible authorial page number at the head. The diagram’s (40) is at the left, and pale foliation 63 at the bottom belongs to another hand. Fifteen main prose baselines are counted; the diagram, oblique margin baselines and interlinear additions are inventoried separately. The strokes in morphismes were checked and show heavy joins rather than an independently isolable cancellation.'),
      dict(id='150-064-N04',text='Readings were chosen from local ink, with no mathematical identity used to replace one Sigma mark by another. The central diagram exponent and the lower body-map target are crossed stars; compact other forms retain explicit alternatives. A small dark mark above the s of the first body map may be a pen-start or a prime. The cancelled label and word, overdrawn brace, voire/voir ending, marginal terminal mark and later s underline remain doubtful.'),
      dict(id='150-064-N05',text='The diagram setting preserves seven objects and nine edges, counting the double visible tracing of s-prime as one edge with two shafts. Broken source decorations retain their component counts, gaps and the one faint piece. b-prime in the diagram is underlined beneath b only, while the s-prime underline reaches under the prime position. Curved insertion leaders around propres and the i.e. explanation are recorded as attachment marks rather than added text parentheses.'),
      dict(id='150-064-N06',text='Audit boxes B04–B06 merge adjacent or vertically overlapping writing so that their readings include all foreground text, insertions and margin material inside each rectangle; B06 includes the entire remaining lower block and foliation. This avoids submitting boxes whose readings silently discard intersecting marginal or interlinear strokes. Root may subdivide these source rectangles when finalising the blind-audit list.')
    ],
    check_events=[],
    notation=[
      dict(form=r'\Sigma^{*}(2),\Sigma^{*}(1)',meaning='Locally crossed superscripts on the author’s central diagram object and the target of the lower body expression.',evidence='Distinct crossing arms at the central node and at the lower expression target.',places='diagram (40), centre; lower s-prime expression, target'),
      dict(form=r'\Sigma^{\unsure{<|*}},\Sigma^{\unsure{*|<}}',meaning='Unresolved local raised forms; the transcription makes no uniform substitution among these candidates.',evidence='Compact angular or apparently crossed strokes crowded against opening parentheses.',places='three outer indexed diagram nodes; first body map; lower expression source; three margin expressions'),
      dict(form=r'\uline{b},\uline{b}\',\uline{s},\uline{s\'},\uline{p}',meaning='Map labels used in the diagram and the author’s ensuing descriptions.',evidence='Separate short bars below the letters; the p bars are shifted to the right of the descenders. b-prime and s-prime have different local underline scopes.',places='diagram (40); two parenthetical lists; margin note; applications fibrantes'),
      dict(form=r'\overset{\uline{s\'}}{-}',meaning='The connector as drawn in the author’s lower body expression.',evidence='An unheaded horizontal stroke below a separately underlined s-prime.',places='lower body expression'),
      dict(form='broken source hooks',meaning='Source decorations grouped by the author with the description immersions bordantes.',evidence='Four, four, three detached components; a lower hook partly joined to the shaft; the separately split s-prime source curl; four pieces in the legend.',places='diagram (40) and first arrow legend'),
      dict(form=r'\prec',meaning='Curved relation sign written inside the author’s pairs.',evidence='Curved left-pointing arms rather than a supplied straight-angle glyph.',places='i.e. insertion; last-line tuple'),
      dict(form='cart',meaning='The author’s written interior labels on two quadrilateral regions; their mathematical property was not checked.',evidence='One cart above and one below the central horizontal arrow.',places='diagram (40)')
    ],
    abbreviations=[
      dict(written='ens',expansion='ensemble',places='i.e. insertion, without a written stop'),
      dict(written='cart',expansion='cartésien',places='two interior labels in diagram (40), without written stops'),
      dict(written='i.e.',expansion='id est / c’est-à-dire',places='small insertion above the lower body expression')
    ],
    hand_log=[
      dict(habit='A short bar under p is displaced to the right of its descender and can be mistaken for a subscript.',places='diagram p; second parenthetical list; margin p; applications fibrantes p',scope='These four occurrences; the final p after celle de is plain.',witness_errors='H reads p_2 at all five places; C omits the four visible bars.'),
      dict(habit='Insertion leaders begin with a parenthesis-like curve and continue under the added words.',places='hexagonal; propres; i.e. explanation',scope='The three inspected leaders; each attachment was read independently.',witness_errors='H widens hexagonal insertion to suivant and supplies parentheses around propres; C supplies a separate inner parenthesis pair around the i.e. insertion.'),
      dict(habit='Raised Sigma marks vary in local openness and can merge with the following parenthesis.',places='all ten indexed Sigma expressions on this sheet',scope='Two crossed stars are secure; the remaining local forms are explicitly doubtful.',witness_errors='C gives < throughout; H gives * throughout. Neither pattern was applied globally.'),
      dict(habit='Source hooks contain real pen gaps, unequal pieces, and sometimes a lower part continuous with the shaft.',places='diagram’s b/b-prime edges, s-prime edge, first arrow legend',scope='Five decorated diagram edges and one legend; s-prime additionally has two retraced shafts.',witness_errors='C uses uniform dotted arcs or a generic hook; H uses generic smooth hooks.'),
      dict(habit='An underline may end before a prime or extend beneath its horizontal position; a very close retrace may remain ambiguous.',places='diagram b-prime; diagram s-prime; s in l’image de s',scope='Local scopes preserved rather than made uniform.',witness_errors='C underlines the diagram b-prime prime; the final s differs between C and H and remains unresolved.'),
      dict(habit='Very compressed terminal movement may obscure a final e, while other accented endings remain singular as written.',places='voire/voir; two formé occurrences',scope='voire/voir remains open; both formé spellings are secure.',witness_errors='H reads voir and regularises both formé to formée.')
    ],
    audit_boxes=audit,
    crops=[dict(file=f'crops/150_scan064_{name}.png',box=box,purpose=purposes[name]) for name,box in boxes.items()],
    unresolved=[d['place']+': '+d['reading'] for d in doubts],
    coverage=dict(whole_image_viewed=True,halves_viewed=['top','bottom'],all_tokens_read=True,
      all_C_insertions_deletions_checked=True,
      differences_considered=len(list(csv.DictReader((ROOT/'edition/packets/150_scan064/diffs.tsv').open(),delimiter='\t'))),
      macro_only_differences_ignored='scan markers and editorial H notes; wrapper equivalence inserted/add, deleted/struck, margin/marginal and uline/underline; layout whitespace and TeX alias syntax. H’s prose note already records the two cart labels and left number position, so those are not treated as omissions from H. Width spelling of a single long prose dash is not counted.')
)

# Remove Python's retained quote escapes in raw quoted record strings.  These
# are transcription-code quoting artefacts, never manuscript accent commands.
def unescape_record_quotes(value):
    if isinstance(value,str):
        return value.replace(chr(92)+chr(39),chr(39))
    if isinstance(value,list):
        return [unescape_record_quotes(v) for v in value]
    if isinstance(value,dict):
        return {k:unescape_record_quotes(v) for k,v in value.items()}
    return value
record = unescape_record_quotes(record)

# Check the returned records before either proposed page file becomes visible.
assert record['scan']=='064' and len(record['crops'])==26
assert all(item['transcribed']=='yes' for item in inventory)
assert {d['id'] for d in record['decisions']}=={'M0606'}
assert len({c['id'] for c in changes})==len(changes)
assert all((ROOT/'edition'/c['crop']).is_file() for c in changes)
assert all((ROOT/'edition'/c['file']).is_file() for c in record['crops'])
assert all(c['against_C'] or c['against_H'] for c in changes)
assert tex.count('\\begin{tikzcd}')==tex.count('\\end{tikzcd}')==2
assert r'\mspage{63}' not in tex
assert r'\margin{63}' in tex
json_text = json.dumps(record,ensure_ascii=False,indent=2)+'\n'
json.loads(json_text)
OUT.mkdir(exist_ok=True)
for dest, content in [(INDEX,json.dumps(index,ensure_ascii=False,indent=2)+'\n'),(OUT/'150_scan064.tex',tex),(OUT/'150_scan064.json',json_text)]:
    tmp=dest.with_name(dest.name+'.tmp')
    tmp.write_text(content)
    os.replace(tmp,dest)
print(json.dumps(dict(scan='064',changes=len(changes),against_C=sum(c['against_C'] for c in changes),against_H=sum(c['against_H'] for c in changes),doubts=len(doubts),crops=len(boxes),inventory=len(inventory),audit_boxes=len(audit)),ensure_ascii=False))
