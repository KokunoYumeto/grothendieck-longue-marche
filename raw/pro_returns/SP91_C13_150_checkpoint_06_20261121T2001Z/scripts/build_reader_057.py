from pathlib import Path
import json, csv, os

ROOT = Path('/workspace/scratch/b12af914b284')
OUT = ROOT / 'edition/reader_returns'
CROP_DIR = ROOT / 'edition/crops'
scan = '057'
boxes = {
'p01_firstline':[300,65,1620,165],
'p02_ouencore':[300,142,1450,230],
'p03_topdisplay':[530,230,1130,310],
'p04_tuple':[460,350,950,425],
'p05_fibre':[305,435,1645,520],
'p06_Pd':[290,527,810,620],
'p07_structure':[1130,591,1655,697],
'p08_ens':[305,700,1585,795],
'p09_systeme':[1030,790,1645,865],
'p10_avecN':[305,885,875,985],
'p11_margin':[35,950,745,1245],
'p12_correspondantles':[430,980,1640,1155],
'p13_cinserts':[300,1163,1650,1310],
'p14_correspondants':[300,1305,1640,1425],
'p15_b1':[300,1415,1655,1525],
'p16_fortiori':[300,1525,1185,1625],
'p18_correspondent':[300,1715,1650,1822],
'p19_b2':[305,1800,1605,1915],
'p20_dit':[305,1900,1605,2010],
'p21_lesespaces':[395,2020,1540,2125],
'p22_half':[310,2115,1450,2210],
'p23_satisf':[1470,2108,1620,2208],
'p24_final':[315,2190,1620,2340],
}

def crop(name):
    return f'crops/150_scan057_{name}.png'

tex = r'''\scanpage{57}
\mspage{24}
de l'ens à $N(x)+1$ éléments, où $N(x)=\operatorname{card}(\Sigma_{\unsure{<|\leq}x})$.
Ou encore, si on regarde l'application-but
\[
\Sigma^{<}(d)\longrightarrow\unsure{\Sigma}=\Sigma^{<}(0)
\]
\[
(x_0<-<x_d)\longmapsto x_d
\]
la fibre de $x\in\Sigma$ s'identifie à l'ens \deleted{des parties}
$\unsure{\mathfrak P|\mathcal P}_d(\{1,.-,N(x)\})$.
La structure relative de $\Sigma^{\unsure{<|*}}(1)$ sur $\Sigma=\Sigma^{<}(0)$
% Isolated dark written sign directly below the bare middle Sigma, between
% this line and the next: two short forked left strokes joined to a compact
% loop or oval at the right. Identity and mathematical attachment unassigned.
\illegible{1}
est donc celle d'un ens tot. ordonné relatif, qui
permet de reconstituer le système des $\Sigma^{*}(d)$
\deleted{avec} $(d\in\mathbb N)$ avec les applications semi-simpliciales
correspondant aux morphismes cofinaux entre
les ens tot. ordonnés-types.
% Slanted marginal note beside the preceding three lines; its words are
% not an insertion after semi-simpliciales. The final circled character is unclear.
\margin{Tout ceci est donc à faire indépendt de toute condition topologique \unsure{\textcircled{a}}.}

\textcircled{c} $\forall\ x\in\Sigma$, les germes \inserted{$B_\alpha$} de sous-espaces \inserted{bordants} de $\Sigma$ en $x$
correspondants, par \unsure{\textcircled{a}}, aux $z_\alpha\in\Sigma^{\unsure{<|*}}(1)$ au dessus
de $x$ (par $\Sigma^{\unsure{<|*}}(1)\overset{\underline b}{\unsure{-|\longrightarrow}}\Sigma$) sont mutuellement transver-
saux (et à fortiori distincts).
Les germes intersections de certains des $B_\alpha$
correspondent donc aux pts des $\Sigma^{\unsure{<|*}}(d)$ au dessus
de $x$ (par $\Sigma^{\unsure{<|*}}(d)\overset{\underline b}{\relbar\joinrel\relbar}\Sigma$), comme
images du \deleted{\unsure{dit}} germe de $\Sigma^{\unsure{<|*}}(d)$ en ces pts.
% Separate cancelled small looped glyph immediately before Les; no letter assigned.
\deleted{\illegible{1}} Les espaces $\Sigma^{*}(d)$ $(d\in\mathbb N)$ et les
applications $\tfrac12$ simpliciales cofinales entre eux, \deleted{\unsure{satisfa}}
% In the preceding cancellation a small final loop follows the tall f;
% its reading as a remains doubtful, and the abandoned word is not completed.
ou encore l'espace relatif $\Sigma^{\unsure{<|*}}(1)$ sur $\Sigma^{<}(0)$ et la
structure d'ordre relative, est décrit entièrement
% Pale bottom-left foliation, apparently another hand; the top authorial number is 24.
\margin{56}
'''

changes=[]
def change(place, C, H, final, against_C, against_H, kind, cat, marked, confidence, evidence, cn=None, box=None, consequence=''):
    changes.append({'id':f'057-{len(changes)+1:02d}', 'place':place, 'C':C, 'H':H, 'final':final,
        'against_C':against_C, 'against_H':against_H, 'kind':kind, 'error_category':cat,
        'marked_in_H':marked, 'confidence':confidence, 'evidence':evidence,
        'crop':crop(cn) if cn else 'page', 'box':boxes[cn] if cn else box,
        'mathematical_consequence':consequence})

change('line 1, first ens', "l'ens", "l'ens.", "l'ens", False,True,
       'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',False,'high',
       'The connected final s ends without a detached point before the separately written à. Retain the unpointed short form.', 'p01_firstline')
change('line 1, number of elements',r'N(x)+1',r'N(x)',r'N(x)+1',False,True,
       'omission','Omissions',False,'high',
       'Immediately after the closing parenthesis there is a small crossed plus and a separate upright 1, before éléments. Both belong to this first expression.', 'p01_firstline',
       consequence='The manuscript gives N(x)+1 elements here; H omits the written +1. No verification of the count has been undertaken.')
change('line 2, opening words',r'Ou encore',r'On \uncertain{a encore}',r'Ou encore',False,True,
       'misread word','Words',True,'high',
       'The initial capital O is followed by a single connected u. The next word is encore; there is no additional a between them.', 'p02_ouencore')
change('line 3, first superscript',r'\Sigma^{<}(d)',r'\Sigma^{*}(d)',r'\Sigma^{<}(d)',False,True,
       'misread symbol or index','Symbols and indices',False,'high',
       'The small exponent has two principal angular arms meeting at the left. No independent crossed stroke is visible in this occurrence.', 'p03_topdisplay')
change('line 3, last superscript',r'\Sigma^{<}(0)',r'\Sigma^{*}(0)',r'\Sigma^{<}(0)',False,True,
       'misread symbol or index','Symbols and indices',False,'high',
       'The last superscript is a small left-pointing angle with two arms. The parameter is a closed 0.', 'p03_topdisplay')
change('line 3, after the last formula',r'\Sigma^{<}(0)',r'\Sigma^{*}(0),',r'\Sigma^{<}(0)',False,True,
       'text not on the page','Text that is not on the page',False,'high',
       'The display ends at the closing parenthesis. There is no comma after it; the tuple map is separately written below.', 'p03_topdisplay')
change('line 4, tuple continuation',r'(x_0<--<x_d)',r'(x_0<\cdots<x_d)',r'(x_0<-<x_d)',True,True,
       'misread symbol or index','Symbols and indices',False,'high',
       'Between the two inequality signs there is one continuous short horizontal stroke, not two separately drawn strokes and not a row of dots. The terminal subscript has the loop and tall stem of d.', 'p04_tuple')
change('line 5, after identifie',r"s'identifie à",r"s'identifie :",r"s'identifie à",False,True,
       'misread word','Words',False,'high',
       'A small compressed a is accompanied by a detached oblique grave stroke. The lower mark has the body of a letter; the two levels do not form punctuation alone.', 'p05_fibre')
change('line 5, second ens',r"l'ens","l'ens.",r"l'ens",False,True,
       'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',False,'high',
       'The short form l’ens is followed directly by the cancelled des parties. No detached full stop follows ens.', 'p05_fibre')
change('line 6, continuation within the braces',r'\{1,--,N(x)\}',r'\lbrace 1,\ldots,N(x)\rbrace',r'\{1,.-,N(x)\}',True,True,
       'misread symbol or index','Symbols and indices',False,'high',
       'After the first comma, the first continuation mark is round and the next is a short horizontal dash. The following comma precedes N(x). The point-plus-dash sequence is retained locally.', 'p06_Pd')
change('line 7, final Sigma with parameter zero',r'\Sigma^{<}(0)',r'\Sigma^{*}(0)',r'\Sigma^{<}(0)',False,True,
       'misread symbol or index','Symbols and indices',False,'high',
       'The rightmost exponent has two clearly separated angular arms converging to the left. This occurrence is retained as <.', 'p07_structure')
change('between lines 7 and 8, isolated mark below the bare Sigma',r'(not recorded)',r'(not recorded)',r'\illegible{1}',True,True,
       'omission','Omissions',False,'medium',
       'A disconnected dark sign lies directly below the middle bare Sigma: two short forked strokes at the left join a horizontal stroke ending in a compact right loop or oval. It is represented as an unassigned fragment on its own source-position line, without a letter or mathematical attachment.', 'p07_structure',
       consequence='No mathematical value or attachment is assigned to this visible fragment.')
change('line 8, ens before tot.',r'ens tot.',r'ens.\ tot.',r'ens tot.',False,True,
       'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',False,'high',
       'The short form ens has no terminal point; the point after the following tot is separately visible. The two short forms are not given matching punctuation.', 'p08_ens')
change('line 9, after système des',r'\Sigma^{<}(d)',r'\Sigma^{*}(d)',r'\Sigma^{*}(d)',True,False,
       'misread symbol or index','Symbols and indices',False,'high',
       'This exponent has visibly crossing strokes and several radiating arms. It is a local asterisk, more articulated than the angular exponents elsewhere on this page.', 'p09_systeme')
change('line 10, cancelled word before the parenthesised index',r'\deleted{avec}',r'(not recorded)',r'\deleted{avec}',False,True,
       'omission','Struck text',False,'high',
       'The connected letters avec remain visible beneath a transverse cancellation immediately before (d in N). The later live avec les is separate.', 'p10_avecN')
change('between main lines 10 and 11, H insertion',r'(nothing)',r'\add{(i.e.\ : \uncertain{toute condition})}',r'(no main-text insertion here; toute condition belongs to the slanted margin)',False,True,
       'insertion or placement','Insertions put in the wrong place',True,'high',
       'The words toute condition follow indépendt de along the slanted marginal baseline. The main line continues from semi-simpliciales to correspondant; no separate parenthesised i.e. insertion is present there.', 'p11_margin')
change('line 12, article before ens',r'les ens',r'ens.',r'les ens',False,True,
       'omission','Omissions',False,'high',
       'A short les precedes ens at the beginning of the main line. Its placement is crowded by the slanted note, but it belongs with the horizontal main text. The full word is also visible in the margin-context crop.', 'p12_correspondantles')
change('line 12, ens punctuation',r'ens tot.',r'ens.\ tot.',r'ens tot.',False,True,
       'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',False,'high',
       'As in line 8, ens ends without a point, whereas the following tot has a distinct stop. The source hyphen in ordonnés-types is visible and retained.', 'p12_correspondantles')
change('slanted left margin, the verbal note',r'\unsure{Tout ceci est donc à faire indépendt de toute condition topologique}',r'tout ceci est purement ensembliste (\ill{}) indépendant des top.\ \ill{}',r'Tout ceci est donc à faire indépendt de toute condition topologique',False,True,
       'misread word','Words',True,'medium',
       'Three slanted runs give Tout ceci est donc à faire / indépendt de toute condition / topologique. The letters donc and faire have separate ascenders and word gaps; toute condition is readable on the second run, and the last run gives the full topologique. The short form indépendt is retained without expansion.', 'p11_margin',
       consequence='The margin says the work is to be done independently of any topological condition. This is an account of the manuscript wording, not an independently checked assertion.')
change('line 14, au dessus',r'au dessus',r'au-dessus',r'au dessus',False,True,
       'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',False,'high',
       'The two words are separated by a blank interval, with no connecting hyphen.', 'p14_correspondants')
change('line 15, first horizontal-mark label',r'\overset{b}{\unsure{-|\longrightarrow}}',r'\xrightarrow{\ b\ }',r'\overset{\underline b}{\unsure{-|\longrightarrow}}',True,True,
       'omission','Omissions',False,'high',
       'A short separate horizontal stroke lies directly under b and above the longer shaft. The underline is secure; the tiny terminal thickening of the longer shaft remains insufficient to settle whether an arrowhead was intended.', 'p15_b1')
change('lines 15–16, written division of transversaux','transver-\nsaux',r'transversaux','transver-\nsaux',False,True,
       'other','Other',False,'high',
       'The line ends with transver followed by a written hyphen; the next begins saux. The manuscript line division and its hyphen are retained.', 'p15_b1')
change('line 16, parenthesis',r'à fortiori',r'deux : deux',r'à fortiori',False,True,
       'misread word','Words',False,'high',
       'The first compact accented a is followed by a tall descending f and the connected sequence fortiori. The source gives à fortiori before distincts.', 'p16_fortiori',
       consequence='The manuscript describes distinctness with the words à fortiori. No separate implication has been proved here.')
change('line 18, au dessus',r'au dessus',r'au-dessus',r'au dessus',False,True,
       'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',False,'high',
       'As locally written after the Sigma(d) expression, au and dessus have a blank gap and no hyphen.', 'p18_correspondent')
change('line 19, second horizontal-mark label',r'\overset{b}{\unsure{-|\longrightarrow}}',r'\xrightarrow{\ b\ }',r'\overset{\underline b}{\relbar\joinrel\relbar}',True,True,
       'omission','Omissions',False,'high',
       'The b has a clearly separate short underline above the longer horizontal shaft. This row records the label underline; the shaft decision is recorded separately.', 'p19_b2')
change('line 19, second horizontal shaft',r'\unsure{-|\longrightarrow}',r'\xrightarrow{\ b\ }',r'\overset{\underline b}{\relbar\joinrel\relbar}',False,True,
       'drawing or diagram','Drawings and diagrams',False,'high',
       'The long horizontal stroke ends smoothly at the right, without a separate upper or lower arm forming a head. The first C alternative is retained as an extended unheaded rule; its length is encoded with joined relbars.', 'p19_b2')
change('line 21, before Les espaces',r'(not recorded)',r'\struck{\ill{}}',r'\deleted{\illegible{1}}',True,False,
       'omission','Struck text',True,'high',
       'A separate small looped glyph lies immediately to the left of the capital L. A heavy horizontal stroke crosses it. The loop remains visible, but a letter cannot be securely assigned.', 'p21_lesespaces')
change('line 22, junction between the fraction and simpliciales',r'$\unsure{\tfrac12}$-simpliciales',r'½ simpliciales',r'$\tfrac12$ simpliciales',True,False,
       'text not on the page','Text that is not on the page',False,'high',
       'The stacked 1 and 2 are followed by blank space and the initial s of simpliciales. There is no separate hyphen in that interval. The longer following horizontal stroke belongs inside the cursive word.', 'p22_half')
change('line 22, final cancelled fragment',r'\deleted{\unsure{satisf}}',r'\struck{\ill{}}',r'\deleted{\unsure{satisfa}}',True,False,
       'omission','Struck text',True,'low',
       'The cancellation leaves an initial s-like curve, a tall t, an i-dot, a tall looped f, and a small additional loop after that f. The final loop is retained tentatively as a in the incomplete fragment satisfa; no word is completed. Against C records the omitted residual loop. The exact letters remain open, so H’s unreadable state is not counted as a resolved textual error.', 'p23_satisf')
change('line 23, last superscript',r'\Sigma^{<}(0)',r'\Sigma^{*}(0)',r'\Sigma^{<}(0)',False,True,
       'misread symbol or index','Symbols and indices',False,'high',
       'The exponent on the last Sigma is a small left-pointing angle with two arms. Its 0 is written inside parentheses. The earlier exponent in the same line remains open separately.', 'p24_final')
change('line 24, predicate',r'est décrit',r'\uncertain{ces} décrivent',r'est décrit',False,True,
       'misread word','Words',True,'high',
       'The first short word reads est. In the next word the sequence after décri ends in a tall terminal t, followed by a gap before entièrement; no vent ending is visible.', 'p24_final')
change('bottom left, pale foliation',r'\mspage{56}',r'(not recorded)',r'\margin{56}',False,True,
       'omission','Omissions',False,'high',
       'The pale grey figures 5 and 6 appear at the bottom left, apart from the dark main hand. The number is retained, with margin rather than authorial-page representation.',None,[23,2304,79,2343])

# Each supplied mark has an explicit result. Open alternatives remain undecided.
decisions = [
 {'id':'M0585','decision':'undecided','reading':r'\unsure{<|\leq}',
  'evidence':'The subscript begins with a left-pointing angular sign whose lower portion is thick. A distinct extra lower bar cannot be separated securely from the lower arm; the < / <= alternatives remain open.',
  'crop':crop('p01_firstline'),'box':boxes['p01_firstline'],'confidence':'low'},
 {'id':'M0586','decision':'undecided','reading':r'\unsure{\Sigma}',
  'evidence':'The target has the principal strokes of Sigma, together with small curved or retraced strokes at its right edge. Sigma remains the proposed reading, with the extra ink unresolved.',
  'crop':crop('p03_topdisplay'),'box':boxes['p03_topdisplay'],'confidence':'medium'},
 {'id':'M0587','decision':'first','reading':'Tout ceci est donc à faire indépendt de toute condition topologique',
  'evidence':'The slanted note can be followed in three runs: Tout ceci est donc à faire / indépendt de toute condition / topologique. All of these words belong to the note, including toute condition; indépendt remains in its short form.',
  'crop':crop('p11_margin'),'box':boxes['p11_margin'],'confidence':'medium'},
 {'id':'M0588','decision':'undecided','reading':r'\unsure{\textcircled{a}}',
  'evidence':'The terminal circle is clear, but its centre is a near-solid dark spot. The small bowl and stem needed to identify an a are not independently separable.',
  'crop':crop('p11_margin'),'box':boxes['p11_margin'],'confidence':'low'},
 {'id':'M0589','decision':'undecided','reading':r'\unsure{-|\longrightarrow}',
  'evidence':'The shaft ends in a tiny wedge or pressure thickening. It does not give sufficiently separate arms to settle a directed head. The b label has a separate underline, represented independently.',
  'crop':crop('p15_b1'),'box':boxes['p15_b1'],'confidence':'low'},
 {'id':'M0590','decision':'first','reading':r'\relbar\joinrel\relbar',
  'evidence':'The second long horizontal shaft has a smooth unheaded right endpoint. Its extent is represented by joined relbars, retaining the first C alternative as an unheaded line. A separate underline is also visible beneath b.',
  'crop':crop('p19_b2'),'box':boxes['p19_b2'],'confidence':'high'},
 {'id':'M0591','decision':'first','reading':r'\Sigma^{*}(d)',
  'evidence':'After Les espaces, the exponent has crossed strokes with multiple distinct arms. This local asterisk is legible; it is the first of C’s two alternatives.',
  'crop':crop('p21_lesespaces'),'box':boxes['p21_lesespaces'],'confidence':'high'},
 {'id':'M0592','decision':'first','reading':r'\tfrac12',
  'evidence':'The numerator is an upright 1 and the lower curled figure is 2, written as a compact stacked half. The numeral shapes are separable from the initial s of the following word.',
  'crop':crop('p22_half'),'box':boxes['p22_half'],'confidence':'high'},
]

inventory=[]
def inv(kind,position,words,hand='his hand',transcribed='yes'):
    inventory.append({'element':f'E{len(inventory)+1:02d}','kind':kind,'position':position,'first_words_or_objects':words,'sheet_kind':'text','hand':hand,'transcribed':transcribed})
inv('text','top left, outside the body','24')
inv('text','main lines 1–2',r"de l'ens à N(x)+1 éléments ... Ou encore, si on regarde l'application-but")
inv('diagram','main line 3, first display',r'\Sigma^{<}(d)\longrightarrow\unsure{\Sigma}=\Sigma^{<}(0)')
inv('diagram','main line 4, second display',r'(x_0<-<x_d)\longmapsto x_d')
inv('text','main line 5',r"la fibre de x in Sigma s'identifie à l'ens")
inv('deletion','end of main line 5',r'\deleted{des parties}')
inv('display','main line 6',r'\unsure{\mathfrak P|\mathcal P}_d(\{1,.-,N(x)\})')
inv('text','main lines 7–12',r"La structure relative de ... est donc celle d'un ens tot. ordonné relatif ... les ens tot. ordonnés-types.")
inv('text','interline immediately below the bare middle Sigma in line 7',r'\illegible{1}: two forked left strokes joined to a compact right loop or oval; identity and attachment unassigned',
    'uncertain; same dark ink as the body','yes, unassigned fragment with a source-position comment')
inv('deletion','beginning of main line 10, before (d in N)',r'\deleted{avec}')
inv('margin note','slanted left margin, beside main lines 10–12',r'Tout ceci est donc à faire indépendt de toute condition topologique \unsure{\textcircled{a}}.')
inv('text','main lines 13–16, circled c paragraph',r'\textcircled{c} forall x in Sigma, les germes ... (et à fortiori distincts).')
inv('insertion','above line 13, between germes and de',r'B_\alpha; curved leader enters the gap after germes')
inv('insertion','above line 13, between sous-espaces and de Sigma',r'bordants; curved leader enters before de')
inv('diagram','within main line 15, first b-labelled horizontal mark',r'\Sigma^{\unsure{<|*}}(1)\overset{\underline b}{\unsure{-|\longrightarrow}}\Sigma')
inv('text','main lines 17–20',r'Les germes intersections de certains des B_alpha ... images du ... germe de Sigma(d) en ces pts.')
inv('diagram','within main line 19, second b-labelled horizontal mark',r'\Sigma^{\unsure{<|*}}(d)\overset{\underline b}{\relbar\joinrel\relbar}\Sigma')
inv('deletion','main line 20, between du and germe',r'\deleted{\unsure{dit}}; letters obscured by a heavy transverse stroke')
inv('deletion','main line 21, immediately before Les espaces',r'\deleted{\illegible{1}}; separate small cancelled looped glyph')
inv('text','main lines 21–24',r'Les espaces Sigma*(d) ... applications 1/2 simpliciales ... ou encore ... est décrit entièrement')
inv('deletion','end of main line 22',r'\deleted{\unsure{satisfa}}; final small loop after the tall f is retained tentatively')
inv('text','bottom left, outside the body','56','apparently another hand, in pale grey writing','yes, as margin foliation')

# Adding uncertainty to an unchanged C form is recorded here rather than counted as a correction.
doubts=[
 {'place':'line 1, subscript in the cardinality formula (M0585)','reading':r'\Sigma_{\unsure{<|\leq}x}',
  'alternatives':r'C: < or \leq; H: \le','confidence':'low','reason':'The bottom of the small angular sign is too thick to separate an extra bar securely.'},
 {'place':'line 3, middle target (M0586)','reading':r'\unsure{\Sigma}',
  'alternatives':'Sigma with retracing or an unresolved remnant at the right','confidence':'medium','reason':'Sigma’s principal strokes are clear; the extra small right-edge strokes remain unassigned.'},
 {'place':'line 6, decorative P rendering','reading':r'\unsure{\mathfrak P|\mathcal P}_d',
  'alternatives':r'C: \mathfrak P; H: \mathcal P','confidence':'low','reason':'A broad right bowl, long stem and small eyelet-like loops are visible, but assigning that handwriting to a single TeX font remains open.'},
 {'place':'line 7, first Sigma superscript','reading':r'\Sigma^{\unsure{<|*}}(1)',
  'alternatives':r'C: \Sigma^{<}(1); H: \Sigma^{*}(1)','confidence':'low','reason':'The compact exponent has a thick junction and short projection; its individual strokes do not securely settle angle versus star.'},
 {'place':'between lines 7 and 8, below the middle Sigma','reading':r'\illegible{1}',
  'alternatives':'unassigned written sign; no letter or mathematical attachment selected','confidence':'low','reason':'The disconnected forked-and-looped ink is visible but cannot be identified from this occurrence.'},
 {'place':'slanted margin, terminal circled mark (M0588)','reading':r'\unsure{\textcircled{a}}',
  'alternatives':'a or an unassigned central mark inside a circle','confidence':'low','reason':'The centre is nearly solid; its internal letter structure is unresolved.'},
 {'place':'line 14, circled reference after par','reading':r'\unsure{\textcircled{a}}',
  'alternatives':'a or an unassigned central mark inside a circle','confidence':'low','reason':'The main-text ring has a compact central blob; an a is the witnesses’ reading, but its constituent strokes are not independently clear here.'},
 {'place':'line 14, Sigma after z_alpha in','reading':r'\Sigma^{\unsure{<|*}}(1)',
  'alternatives':r'C: <; H: *','confidence':'low','reason':'The raised sign is compact and heavily inked, with insufficient separation of the short arms.'},
 {'place':'line 15, first b-labelled formula superscript','reading':r'\Sigma^{\unsure{<|*}}(1)',
  'alternatives':r'C: <; H: *','confidence':'low','reason':'The small raised dark shape has a thick central junction; neither local alternative is excluded by the visible strokes.'},
 {'place':'line 15, first b-labelled shaft (M0589)','reading':r'\unsure{-|\longrightarrow}',
  'alternatives':'unheaded line or right arrow','confidence':'low','reason':'The rightmost wedge is too small to distinguish an intended head from a pressure thickening.'},
 {'place':'line 18, Sigma after pts des','reading':r'\Sigma^{\unsure{<|*}}(d)',
  'alternatives':r'C: <; H: *','confidence':'low','reason':'The local exponent consists of a tiny thick angular cluster; separate crossing strokes cannot be confidently read.'},
 {'place':'line 19, second b-labelled formula superscript','reading':r'\Sigma^{\unsure{<|*}}(d)',
  'alternatives':r'C: <; H: *','confidence':'low','reason':'Several short projections are visible, but overlap with the compact junction prevents a secure local choice.'},
 {'place':'line 20, cancelled fragment after du','reading':r'\deleted{\unsure{dit}}',
  'alternatives':r'C: dit; H: \ill{}','confidence':'low','reason':'A heavy transverse cancellation obscures most of the small letters. The retained C proposal remains a guess, not a resolved reading.'},
 {'place':'line 20, Sigma after germe de','reading':r'\Sigma^{\unsure{<|*}}(d)',
  'alternatives':r'C: <; H: *','confidence':'low','reason':'The exponent is a very small thick shape; its short strokes remain insufficiently distinct.'},
 {'place':'line 21, cancelled glyph before Les','reading':r'\deleted{\illegible{1}}',
  'alternatives':'unassigned small looped letter or sign','confidence':'low','reason':'The cancellation is certain, but the visible loop does not identify its letter.'},
 {'place':'line 22, cancelled word fragment at the right','reading':r'\deleted{\unsure{satisfa}}',
  'alternatives':r'satisfa; satisf followed by an unassigned loop','confidence':'low','reason':'The extra loop after the tall f is present, but its value as a and parts of the underlying sequence remain obscured by the strike.'},
 {'place':'line 23, first Sigma superscript','reading':r'\Sigma^{\unsure{<|*}}(1)',
  'alternatives':r'C: <; H: *','confidence':'low','reason':'The first raised sign has a thick meeting point and short projection; the nearby Sigma is also retraced. The later exponent in the same line is independently legible as <.'},
]

notes=[
 {'id':'150-057-N01','text':'The authorial page number is 24; a pale bottom-left foliation reads 56 and is represented separately. The page begins in mid-sentence. The manuscript gives an ensemble with N(x)+1 elements and writes N(x)=card(Sigma_{< or <= x}); the comparison sign remains open. It then displays an application-but and a tuple sent to its final entry. The author identifies the fibre of x with the displayed P_d expression. The P font and the cardinality subscript are not silently settled, and the displayed counting assertion has not been independently verified.'},
 {'id':'150-057-N02','text':'The manuscript says that the relative structure of Sigma(1) over Sigma=Sigma(0) is that of an ens tot. ordonné relatif, allowing the system of Sigma(d) and its cofinal semi-simplicial applications to be reconstituted. The slanted margin says: Tout ceci est donc à faire indépendt de toute condition topologique. The local superscripts are retained occurrence by occurrence, with clear stars at système des and Les espaces and explicit uncertainty at several compact forms. The isolated sign below the bare Sigma is recorded without assigning it a mathematical role.'},
 {'id':'150-057-N03','text':'In the paragraph marked by a circled c, the author writes that the inserted B_alpha, described by the inserted word bordants, correspond through a circled reference to points z_alpha over x and are mutually transverse, et à fortiori distincts. The next paragraph says that intersections of certain B_alpha correspond to points of Sigma(d) over x as images of the indicated germs. Both b labels have separate underlines. The first horizontal mark remains open as line or arrow, and the second has a visibly unheaded shaft. These are reports of the manuscript’s claims and marks, without an independent transversality or correspondence proof.'},
 {'id':'150-057-N04','text':'The closing passage speaks of Les espaces Sigma*(d), the applications 1/2 simpliciales cofinales, and the relative space with its order structure, ending est décrit entièrement at the page edge. A small cancelled glyph before Les, the cancelled dit proposal, and the final cancelled satisfa fragment are preserved. The last fragment has a residual loop after f; it has not been completed into a word. No mathematical theorem was checked in making these readings.'},
]

notation=[
 {'form':r'N(x)=\operatorname{card}(\Sigma_{\unsure{<|\leq}x})','meaning':'The quantity introduced by the author in the first line; the written comparison remains unresolved.','evidence':'Explicit first-line equality.','places':'line 1'},
 {'form':r'\Sigma^{<}(d), \Sigma^{*}(d), \Sigma^{\unsure{<|*}}(d)','meaning':'Local written superscripts on the Sigma expressions; no uniform replacement has been made.','evidence':'Angular forms in the top display and final zero expressions; crossed stars after système des and Les espaces; compact open forms elsewhere.','places':'lines 3, 7, 9, 14–15, 18–21, 23'},
 {'form':r'\unsure{\mathfrak P|\mathcal P}_d(\{1,.-,N(x)\})','meaning':'The P expression used in the author’s fibre description.','evidence':'Decorative P with eyelet-like stem details, subscript d and brace-delimited sequence.','places':'line 6'},
 {'form':r'(x_0<-<x_d)\longmapsto x_d','meaning':'The tuple and target of the manuscript’s displayed element map.','evidence':'A single continuation dash, a left bar on the mapsto shaft, and a right terminal head.','places':'line 4'},
 {'form':r'B_\alpha','meaning':'Label inserted for the germs described in the manuscript as bordants.','evidence':'Interlinear B_alpha with a curved leader after germes; later occurrence in the intersections paragraph.','places':'lines 13 and 17'},
 {'form':r'z_\alpha','meaning':'The points mentioned in the circled-c paragraph.','evidence':'z with a small alpha subscript immediately before membership in Sigma(1).','places':'line 14'},
 {'form':r'\underline b','meaning':'The separately underlined label above each of the two horizontal marks.','evidence':'Short underline between the b and the longer shaft in both crops.','places':'lines 15 and 19'},
 {'form':r'\tfrac12','meaning':'Written fractional modifier before simpliciales.','evidence':'Stacked 1 and 2 with a blank interval before the following word.','places':'line 22'},
 {'form':r'\textcircled{c}; \unsure{\textcircled{a}}','meaning':'A clear paragraph marker c and two circled references whose central letters remain doubtful.','evidence':'Circle and c separated in line 13; the other two rings enclose compact dark centres.','places':'margin; lines 13–14'},
]

abbreviations=[
 {'written':'ens','expansion':'ensemble','places':'lines 1, 5, 8, 12; no terminal stop in these occurrences'},
 {'written':'tot.','expansion':'totalement','places':'lines 8 and 12'},
 {'written':'pts','expansion':'points','places':'lines 18 and 20'},
 {'written':'indépendt','expansion':'unresolved; no expansion inserted','places':'slanted marginal note'},
]
hand_log=[
 {'habit':'The short form ens is unpointed, whereas tot. has a separate terminal point.','places':'lines 1, 5, 8, 12','scope':'all four ens occurrences on this page and both tot. occurrences','witness_errors':'H supplies points after ens in all four places.'},
 {'habit':'A compressed à can have a very small lower body and detached grave stroke.','places':'line 5; compare the readable à fortiori in line 16 and à faire in the margin','scope':'the inspected local occurrences only','witness_errors':'H gives a colon after identifie and substitutes deux : deux for à fortiori.'},
 {'habit':'Sigma exponents vary locally in articulation: clear angles, clear crossed stars, and compact clusters.','places':'top display; système des; Les espaces; compact intermediate occurrences','scope':'only the individually inspected forms on this page','witness_errors':'C’s < after système des omits a clear crossed star; H’s stars replace several clear angular forms. Other comparisons remain open.'},
 {'habit':'Continuation marks have locally different shapes.','places':'tuple display and P_d set expression','scope':'the two inspected continuation sequences','witness_errors':'C has two dashes in both places; H renders both as dots. The tuple has one continuous dash, and the set has a point followed by a short dash.'},
 {'habit':'Each b has a short independent underline above its longer horizontal shaft.','places':'lines 15 and 19','scope':'both inline marks','witness_errors':'Both witnesses omit these label underlines. H also supplies an arrowhead to the second unheaded shaft.'},
 {'habit':'Interlinear B_alpha and bordants have curved leaders into word gaps.','places':'line 13','scope':'both insertions','witness_errors':'Their placement is retained from the source; no lexical correction is made to either witness here.'},
 {'habit':'The slanted note crosses the horizontal text zone while retaining its own baselines.','places':'left margin beside lines 10–12','scope':'the three runs of this note','witness_errors':'H duplicates toute condition as a main-text insertion and gives a different verbal marginal reading.'},
 {'habit':'Crossing strokes leave readable word outlines or small residual loops at their edges.','places':'des parties; avec; doubtful dit; glyph before Les; final satisfa fragment','scope':'all five cancelled units inspected separately','witness_errors':'H omits avec; C omits the separate cancelled glyph before Les and the residual loop following f in the final cancellation.'},
 {'habit':'The words au dessus are written without a connecting hyphen.','places':'lines 14 and 18','scope':'both occurrences','witness_errors':'H adds a hyphen in both occurrences.'},
 {'habit':'A pale grey lower foliation is visually distinct in ink from the dark top page number.','places':'top-left 24; bottom-left 56','scope':'the two written numbers outside the body','witness_errors':'H records only 24. The final representation keeps 56 as marginal foliation, with hand attribution qualified.'},
]

audit=[]
def aud(kind,xy,reading):
    audit.append({'box':f'B{len(audit)+1:02d}','kind':kind,'x0':xy[0],'y0':xy[1],'x1':xy[2],'y1':xy[3],'reading':reading})
aud('handwritten number',[27,46,80,92],r'24')
aud('lexical disagreement',[425,70,569,126],r"l'ens")
aud('handwritten number',[706,66,837,133],r'N(x)+1')
aud('doubtful formula',[1177,79,1613,161],r'N(x)=\operatorname{card}(\Sigma_{\unsure{<|\leq}x}).')
aud('lexical disagreement',[308,145,596,215],r'Ou encore,')
aud('doubtful formula',[535,230,1129,310],r'\Sigma^{<}(d)\longrightarrow\unsure{\Sigma}=\Sigma^{<}(0)')
aud('handwritten number',[463,348,950,425],r'(x_0<-<x_d)\longmapsto x_d')
aud('struck passage',[1180,434,1643,511],r"à l'ens \deleted{des parties}")
aud('doubtful formula',[291,527,810,620],r'\unsure{\mathfrak P|\mathcal P}_d(\{1,.-,N(x)\}).')
aud('doubtful formula',[1130,591,1655,697],r'\Sigma^{\unsure{<|*}}(1)\quad sur\quad\Sigma=\Sigma^{<}(0)'+'\n'+r'\illegible{1}')
aud('lexical disagreement',[848,716,943,766],r'ens')
aud('doubtful formula',[1464,789,1635,860],r'\Sigma^{*}(d)')
aud('struck passage',[308,951,420,976],r'\deleted{avec}')
aud('margin note',[34,950,744,1234],r'\deleted{avec}'+'\n'+r'correspondant'+'\n'+r'les ens tot.'+'\n'+r'\margin{Tout ceci est donc à faire indépendt de toute condition topologique \unsure{\textcircled{a}}.}')
aud('insertion',[741,1186,1090,1308],r'les germes \inserted{B_\alpha} de')
aud('insertion',[1092,1162,1469,1298],r'sous-espaces \inserted{bordants} de')
aud('doubtful formula',[305,1307,1642,1425],r'correspondants, par \unsure{\textcircled{a}}, aux z_\alpha\in\Sigma^{\unsure{<|*}}(1) au dessus')
aud('doubtful formula',[305,1415,1655,1525],r'de x (par \Sigma^{\unsure{<|*}}(1)\overset{\underline b}{\unsure{-|\longrightarrow}}\Sigma) sont mutuellement transver-')
aud('lexical disagreement',[303,1524,1185,1625],r'saux (et à fortiori distincts).')
aud('doubtful formula',[1216,1720,1653,1797],r'\Sigma^{\unsure{<|*}}(d) au dessus')
aud('doubtful formula',[577,1801,1342,1907],r'(par \Sigma^{\unsure{<|*}}(d)\overset{\underline b}{\relbar\joinrel\relbar}\Sigma),')
aud('struck passage',[305,1900,1605,2010],r'images du \deleted{\unsure{dit}} germe de \Sigma^{\unsure{<|*}}(d) en ces pts.')
aud('struck passage',[395,2020,1540,2125],r'\deleted{\illegible{1}} Les espaces \Sigma^{*}(d) (d\in\mathbb N) et les')
aud('handwritten number',[611,2127,932,2210],r'\tfrac12\quad simpliciales')
aud('struck passage',[1470,2108,1620,2208],r'\deleted{\unsure{satisfa}}')
aud('doubtful formula',[1042,2195,1467,2268],r'\Sigma^{\unsure{<|*}}(1)\quad sur\quad\Sigma^{<}(0)')
aud('lexical disagreement',[325,2273,1625,2338],r"structure d'ordre relative, est décrit entièrement")
aud('handwritten number',[23,2304,79,2343],r'56')

purposes={
'p01_firstline':'First ens, N(x)+1, and the entire cardinality formula containing M0585.',
'p02_ouencore':'Ou encore versus H On a encore; full second main line context.',
'p03_topdisplay':'Entire first displayed map, both exponents, target M0586, terminal punctuation.',
'p04_tuple':'Entire tuple map, continuation stroke and handwritten 0.',
'p05_fibre':'s’identifie à versus colon, ens punctuation, and individually checked deletion des parties.',
'p06_Pd':'Whole P_d expression, uncertain P rendering, point-plus-dash continuation, handwritten 1.',
'p07_structure':'Both relative-structure Sigma expressions, handwritten 1/0, and unassigned interlinear dark sign.',
'p08_ens':'Unpointed ens and pointed tot. in the relative-order sentence.',
'p09_systeme':'Local crossed star after système des.',
'p10_avecN':'Individually checked cancelled avec and neighbouring index expression.',
'p11_margin':'Entire slanted marginal note, M0587–M0588, and context for H’s duplicated main-text insertion; rotated -20 degrees.',
'p12_correspondantles':'Main-text correspondant and les ens tot. ordonnés-types beside the slanted note.',
'p13_cinserts':'Circled c and the individual B_alpha and bordants insertions with their leaders.',
'p14_correspondants':'Circled reference, local superscript, handwritten 1, and unhyphenated au dessus.',
'p15_b1':'Entire first b-labelled formula, its underline and unresolved shaft endpoint M0589, line-end transver-.',
'p16_fortiori':'saux continuation and à fortiori versus H deux : deux.',
'p18_correspondent':'Local Sigma(d) superscript and second unhyphenated au dessus.',
'p19_b2':'Entire second b-labelled formula, underline and unheaded shaft M0590.',
'p20_dit':'Individually checked doubtful cancellation dit and whole germe de Sigma(d) phrase.',
'p21_lesespaces':'Separate cancelled loop before Les and the whole Sigma*(d) expression containing M0591.',
'p22_half':'M0592 stacked half and the actual spacing before simpliciales.',
'p23_satisf':'Individually checked final cancelled fragment, including the residual small loop after f.',
'p24_final':'ou encore, final Sigma formulas with 1/0, and est décrit entièrement versus H ces décrivent.',
}

with (ROOT/'edition/packets/150_scan057/diffs.tsv').open(encoding='utf-8',newline='') as f:
    diff_count=len(list(csv.DictReader(f,delimiter='\t')))

result={
 'scan':scan,'reader':'reader_b','line_count':24,
 'changes':changes,'decisions':decisions,'inventory':inventory,'doubts':doubts,'notes':notes,
 'check_events':[], 'notation':notation,'abbreviations':abbreviations,'hand_log':hand_log,
 'audit_boxes':audit,
 'crops':[{'file':crop(n),'box':b,'purpose':purposes[n]} for n,b in boxes.items()],
 'unresolved':[
  'M0585: < versus <= in the first-line cardinality subscript.',
  'M0586: extra strokes at the right of the proposed target Sigma.',
  'Decorative P font in the fibre expression: frak versus cal remains open.',
  'Compact Sigma superscripts in lines 7 (first), 14, 15, 18, 19, 20 and 23 (first) remain < / * alternatives.',
  'Unassigned dark written sign below the middle Sigma in line 7; no letter or attachment selected.',
  'M0588: central letter of the margin’s circled mark; the main-text circled reference after par is independently doubtful too.',
  'M0589: tiny terminal wedge does not settle whether the first horizontal shaft has a head.',
  'Cancelled dit proposal remains uncertain.',
  'Small cancelled glyph before Les espaces remains illegible.',
  'Cancelled satisfa retains an uncertain final small loop; no full word has been supplied.',
 ],
 'coverage':{
  'whole_image_viewed':True,'halves_viewed':['top','bottom'],'all_tokens_read':True,
  'all_C_insertions_deletions_checked':True,'differences_considered':diff_count,
  'macro_only_differences_ignored':'Editorial scan label; H’s prose note for the top authorial number 24; equivalent card/operator, mathbb/braces and set-delimiter syntax; add/inserted and struck/deleted wrappers; circled-letter representation where H’s note explicitly records the circle; display grouping apart from its supplied comma; certainty-only wrappers. Open C/H superscript and P-font comparisons are individually recorded in doubts, without counting either open reading as rejected. The pale 56 is retained with qualified hand attribution and margin representation.',
 }
}

OUT.mkdir(parents=True,exist_ok=True)
for suffix,content in [('tex',tex),('json',json.dumps(result,ensure_ascii=False,indent=2)+'\n')]:
    path=OUT/f'150_scan057.{suffix}'
    temporary=path.with_name(path.name+'.tmp')
    temporary.write_text(content,encoding='utf-8')
    os.replace(temporary,path)

print(json.dumps({'scan':scan,'changes':len(changes),'decisions':len(decisions),'inventory':len(inventory),'doubts':len(doubts),'audit_boxes':len(audit),'crops':len(boxes),'packet_differences':diff_count},ensure_ascii=False))
