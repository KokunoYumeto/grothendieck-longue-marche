from pathlib import Path
import csv, json, os

ROOT=Path('/workspace/scratch/b12af914b284')
OUT=ROOT/'edition/reader_returns'
index=json.loads((ROOT/'edition/scripts/150_scan070_crop_index.json').read_text())
boxes=index['crops']

first_map=r'\uline{\Sigma}\mathrel{\relbar\joinrel\relbar}\uline{I}'
second_map=r'\uline{\Sigma}\unsure{:}\mathrel{\relbar\joinrel\relbar}\uline{I}'
tuple_formula=r'''\uline{\Sigma}=(\Sigma=\Sigma(0),\quad
\underset{\underset{\Sigma\unsure{\times}\Sigma}{\cap}}{\Sigma(1)}
=\delta(\Sigma_{(0)})\amalg\Sigma^{<}(1))'''
mono_map=r'\Sigma_{ij}\unsure{\longrightarrow|-}\Sigma_j'
fork=r'''\diagram{\begin{tikzcd}[column sep=15mm,row sep=-4mm,execute at end picture={
% Two short, nearly parallel, slightly divergent shafts.  Their source
% heights differ.  The upper endpoint is dense and pointed; the lower
% endpoint contains a small loop, kept open in the drawing.
\draw[line width=.55pt,line cap=round] ([yshift=2pt]s70source.east) -- ([xshift=-2pt]s70upper.west);
\fill ([xshift=-3pt,yshift=.2pt]s70upper.west) --
([xshift=-2pt,yshift=1.4pt]s70upper.west) --
([xshift=-.9pt,yshift=.55pt]s70upper.west) --
([xshift=-1.4pt,yshift=-.65pt]s70upper.west) --
([xshift=-2.5pt,yshift=-.3pt]s70upper.west) -- cycle;
\draw[line width=.55pt,line cap=round] ([yshift=-2pt]s70source.east) -- ([xshift=-2.7pt]s70lower.west);
\draw[line width=.5pt] ([xshift=-2pt]s70lower.west) ellipse[x radius=.7pt,y radius=.6pt];
}]
& |[alias=s70upper]|\Sigma_i\\
|[alias=s70source]|\Sigma_{ij}&\\
& |[alias=s70lower]|\Sigma_j
\end{tikzcd}}'''
bottom=r'''$(\unsure{\Sigma|\Sigma_i},\Sigma_{ij},\ s_{ij}\ b_{ij}:$
'''+fork+r'''$),$
% The first tuple Sigma has a compact raised foot-tip; a separate i cannot
% be securely isolated.  No independent comma is assigned between s_ij and b_ij.
'''

tex=r'''\scanpage{70}
% No authorial number is visible at the head of this sheet.
Supposons en plus

d) toute flèche inversible de $\uline{\Sigma}$ est une identité
(p.ex. $\uline{\Sigma}$ est une catégorie définie par un ens
\uline{ordonné}).

Alors on conclut aisément que l'ens. pré-%
ordonné $I$ est \uline{ordonné}, et que tte \unsure{flèche|flèches}
de $\uline{\Sigma}$ qui n'est pas une identité i.e. $u\in\Sigma^{\unsure{*|<}}(1)$,
son image dans $I(1)$ n'est pas une identité;
\deleted{\unsure{i.e.}} Si $\uline{\Sigma}$ est associé à un
\deleted{\unsure{ens. ord.}}\inserted{espace top.}
ordonné $\Sigma=\Sigma_{(0)}$, cela signifie que
$'''+first_map+r'''$ est \inserted{une appl.}
\uline{strictement} croissante.
% pré- has a written line-end dash.  The upper-right ending of flèche is
% reworked, with a raised curl and sloping stroke; a final s remains open.
% The crossed i.e. and ens. ord. have obscured punctuation/letter joins.
% espace top. stands immediately above the cancelled ens. ord. after un.
% Sigma=Sigma_(0) follows ordonné on the rising main baseline, without an
% independent insertion leader or preceding comma.  The first map's shaft
% has a short downward terminal stub; both object symbols are underlined.
% The curved leader for une appl. enters immediately before strictement.

Revenons alors à un \deleted{catég} ens. ordonné topologique
\[
'''+tuple_formula+r'''
\]
% The squeezed live Sigma= lies just inside the opening parenthesis.
% The first (0) and following (1) have baseline placement; the inner (0)
% in delta's argument is lowered.  The cap and product remain vertical.
% The product sign has a looped left part and crossing right arms.
satisfaisant aux conditions a) b) c) et $1^\circ$) de la page (27)
(correspondant \inserted{moralement} \unsure{à|a} un déploiement d'une
stratification locale équisingulier), et tel que les comp. connexes
de $\Sigma$ \deleted{\unsure{sont|soient}} de dim finie.
Considérons alors \unsure{la|le} \deleted{\unsure{factorisation}}\inserted{morphisme}
canonique $'''+second_map+r'''$ avec $I=\pi_0(\Sigma)$,
% moralement has its own leader after correspondant; the possible grave
% on the following a lies within that leader zone.  The g-descender in
% équisingulier is continuous with the letter, not a separate underline.
% morphisme is above factorisation, not attached to the cancelled sont.
% The article's final small lobe leaves la/le open.  The cancelled word's
% right end reaches the paper edge.  The second map's two small tilted
% points are kept as an uncertain colon; its shaft has a dense terminal
% upright.  The target I is reworked, without an assigned older glyph.
et supposons de plus que pour $i<j$ ($i,j\in I$)
\[
'''+mono_map+r'''\quad\hbox{soit \uline{mono} i.e. plongement fermé}
\]
% The short terminal point of the mono-map is filled and compact; the
% arrow/shaft contour remains doubtful.  fermé meets the right edge,
% with an accent but no independent terminal full stop visible.
On est alors sous les conditions de p. 28,
données a) b) c)
'''+bottom+r'''% Pale bottom-left foliation, another hand.
\margin{69}
'''

def atomic_write(dest,content):
    tmp=dest.with_name(dest.name+'.tmp')
    tmp.write_text(content)
    os.replace(tmp,dest)

OUT.mkdir(exist_ok=True)
atomic_write(OUT/'150_scan070.tex',tex)

changes=[]
def ch(place,C,H,final,aC,aH,kind,cat,confidence,crop,evidence,marked=False,consequence=''):
    changes.append(dict(id=f'070-{len(changes)+1:02}',place=place,C=C,H=H,final=final,against_C=aC,against_H=aH,kind=kind,error_category=cat,marked_in_H=marked,confidence=confidence,evidence=evidence,crop=f'crops/150_scan070_{crop}.png',box=boxes[crop],mathematical_consequence=consequence))

ch('condition d), inversible','inversible',r'\emph{inversible}','inversible',False,True,'text not on the page','Text that is not on the page','high','p01_inversible','The word has its connected letter strokes and dotted i forms, with no independently drawn underline below it. H’s emphasis wrapper is not supported here.')
ch('first ens, in the example','ens','ens.','ens',False,True,'text not on the page','Text that is not on the page','high','p02_ens','The terminal s turns downward and stops; the following blank interval contains no abbreviation point.')
ch('first assertion, pré-ordonné','pré-ordonné','préordonné','pré-ordonné',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','high','p03_pre','A separate accent is above pré, and a distinct horizontal dash follows it at the line end before ordonné continues on the next line.')
ch('first assertion, tte','tte','toute','tte',False,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','high','p04_tte','Two adjacent tall t strokes share the crossbar, followed by one low e; the short form is written without ou.')
ch('before son image','son image','a son image','son image',False,True,'text not on the page','Text that is not on the page','high','p06_son','The baseline begins with the short s and following on strokes. No separate a precedes son.')
ch('after I(1)',r'$I(1)$ n\'est pas',r'$I(1)$ qui n\'est pas',r'$I(1)$ n\'est pas',False,True,'text not on the page','Text that is not on the page','high','p06_son','The I(1) group is followed directly by the two low portions and apostrophe of n’est; a qui group is not written between them.')
ch('after cancelled i.e.','Si','si','Si',False,True,'misread word','Words','high','p28_si','The initial has a tall upper loop and separate lower loop, substantially above the following short i; its outline supports the capital S. The i has a separate dot.')
ch('after ordonné before the equality','ordonné,','ordonné','ordonné',True,False,'text not on the page','Text that is not on the page','high','p09_eq','After the accented terminal of ordonné there is a gap before the first Sigma, without an independent comma. The comma following the complete equality is visible.')
ch('Sigma equality after ordonné, argument placement',r'\Sigma=\Sigma_{(0)}',r'\Sigma=\Sigma(0)',r'\Sigma=\Sigma_{(0)}',False,True,'misread symbol or index','Symbols and indices','medium','p09_eq','The small 0 is low beside the second Sigma, with its centre near the Sigma’s foot; the enclosing small parenthesis group is also lowered.')
ch('Sigma equality after ordonné, position',r'$\Sigma=\Sigma_{(0)}$',r'\add{$\Sigma=\Sigma(0)$}',r'$\Sigma=\Sigma_{(0)}$',False,True,'insertion or placement','Insertions put in the wrong place','low','p09_eq','The equality follows ordonné on the rising main baseline before cela. No independent leader isolates it as an interlinear insertion. Inline placement leads; the writing stage cannot be determined from the available strokes, so H’s addition-state interpretation remains open.')
ch('first Sigma-to-I expression, underlines',r'\uline{\Sigma}\longrightarrow\uline{I}',r'\Sigma\to I',first_map,False,True,'omission','Symbols and indices','high','p10_firstmap','One separate horizontal underline lies below each of Sigma and I. Each symbol also has its own lower body stroke, distinct from the underline.')
ch('first Sigma-to-I expression, connector',r'\longrightarrow',r'\to',r'\mathrel{\relbar\joinrel\relbar}',True,True,'misread symbol or index','Symbols and indices','high','p10_firstmap','The short shaft ends in a downward terminal stub. There is no exposed V-shaped head. The literal unheaded shaft is retained, with the stub documented in the page comment.')
ch('before strictement',r'\inserted{une appl.}','(nothing)',r'\inserted{une appl.}',False,True,'omission','Omissions','high','p11_uneappl','The small upper line reads une appl. with a distinct final stop. Its curved leader passes beneath the words and bends down immediately before strictement.')
ch('opening of the tuple, squeezed equality',r'\Sigma=\Sigma_{(0)}',r'\Sigma(0)',r'\Sigma=\Sigma(0)',False,True,'omission','Omissions','high','p13_tuple','A small live Sigma and two short equality strokes are squeezed just inside the large opening parenthesis, before the larger Sigma with argument 0. This row concerns the omitted Sigma=; argument height is recorded separately.',False,'The manuscript’s extra initial equality is retained.')
ch('tuple, first argument 0',r'\Sigma_{(0)}',r'\Sigma(0)',r'\Sigma(0)',True,False,'misread symbol or index','Symbols and indices','high','p13_tuple','The first round 0 and its parenthesis group sit beside the middle of the adjoining Sigma on the same local baseline.')
ch('tuple, argument 1 before equals',r'\Sigma_{(1)}',r'\Sigma(1)',r'\Sigma(1)',True,False,'misread symbol or index','Symbols and indices','high','p13_tuple','The (1) immediately before the equality has baseline placement beside its Sigma, unlike the inner 0 in the following delta argument.')
ch('tuple, inner delta argument',r'\delta(\Sigma_{(0)})',r'\delta(\Sigma(0))',r'\delta(\Sigma_{(0)})',False,True,'misread symbol or index','Symbols and indices','high','p13_tuple','Inside the outer delta parentheses, the inner small 0 and its own parenthesis group are shifted down beside the Sigma.')
ch('tuple, vertical cap/product arrangement',r'\underset{\underset{\Sigma\times\Sigma}{\cap}}{\Sigma_{(1)}}',r'\bigr),\qquad \Sigma(1)\subset\Sigma\times\Sigma ,',r'\underset{\underset{\Sigma\unsure{\times}\Sigma}{\cap}}{\Sigma(1)}',False,True,'drawing or diagram','Drawings and diagrams','high','p13_tuple','The arch-like cap is directly below the existing Sigma(1), and Sigma times Sigma is directly beneath that cap. The source has no separately repeated Sigma(1) or horizontal inclusion after the tuple. H’s note acknowledges the vertical cap; its displayed arrangement is still horizontal and repeated.')
ch('tuple, final superscript',r'\Sigma^{<}(1)',r'\Sigma^{*}(1)',r'\Sigma^{<}(1)',False,True,'misread symbol or index','Symbols and indices','high','p13_tuple','The small raised sign has a left junction and two short rightward arms. No additional crossed arms are exposed in this occurrence.')
ch('interlinear word and its attachment',r'\inserted{\unsure{moralement}}',r'\add{au moins}',r'\inserted{moralement}',False,True,'insertion or placement','Insertions put in the wrong place','high','p15_moral','The visible m-o-r-a-l group continues through compressed e-m-e-n strokes to a final t. Its continuous leader bends down after correspondant, before the following two baseline word groups. H places au moins after 1°), above the wrong baseline.')
ch('following correspondant and its insertion','à un','au',r'\unsure{à|a} un',False,True,'misread word','Words','medium','p15_moral','Two separate short baseline groups stand before déploiement. They support a/à followed by un. The possible grave lies in the leader zone, so its attachment remains explicitly uncertain.')
ch('stratification modifier','locale','localement','locale',False,True,'misread word','Words','high','p17_locale','The word has the initial looped l, low o-c-a sequence, second tall l and terminal e-like return, followed by a blank before équisingulier. No ment continuation follows.')
ch('after locale','équisingulier','équisingulière','équisingulier',False,True,'misread word','Words','high','p17_locale','The final i-e-r-sized strokes end before the closing parenthesis; no additional feminine e or grave accent is visible there. The large lower curve is continuous with the g descender.')
ch('cancelled word after Sigma','sont','soient',r'\unsure{sont|soient}',False,True,'misread word','Words','low','p18_sont','The initial s, o loop and tall final t are visible. The strike masks the middle n-like arch. sont leads; no independent i/e group is isolated, but soient remains an explicit alternative beneath the cancellation.')
ch('after the cancelled sont group','(nothing)',r'\add{\ill{}}','(nothing)',False,True,'text not on the page','Text that is not on the page','high','p20_factor','The nearby upper word morphisme belongs directly above the next line’s cancelled factorisation. There is no separate replacement insertion attached to the earlier cancelled sont group.',True)
ch('dimension short form','dim','dim.','dim',False,True,'text not on the page','Text that is not on the page','high','p19_dim','The low m ends before a blank interval leading to finie. There is no abbreviation point after dim; the final stop after finie is distinct.')
ch('replacement above factorisation',r'\inserted{morphisme}',r'\add{\ill{}}',r'\inserted{morphisme}',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','high','p20_factor','The live upper word has a low m-o-r group, a clear descending p, tall h and the following i-s-m-e strokes. It stands immediately above the crossed factorisation, with its end toward the paper edge.',True)
ch('canonical map, source-side points','(nothing)','(nothing)',r'\unsure{:}',True,True,'omission','Symbols and indices','medium','p21_canon','Two discrete dark points at different heights lie immediately right of the source Sigma and before the shaft. They form a tilted two-point group; their role is uncertain, so the proposed colon remains marked.')
ch('canonical map, connector',r'\longrightarrow',r'\longrightarrow',r'\mathrel{\relbar\joinrel\relbar}',True,True,'misread symbol or index','Symbols and indices','high','p21_canon','The short thin shaft ends in a dense small upright/stub, without an exposed V. The separate source and target underlines are retained.')
ch('after fermé','fermé.','fermé.','fermé',True,True,'text not on the page','Text that is not on the page','high','p24_ferme','The accented ending reaches the paper edge. No independent terminal full stop is visible before that edge.')
ch('final tuple, first Sigma',r'\Sigma_i',r'\Sigma_i',r'\unsure{\Sigma|\Sigma_i}',True,True,'misread symbol or index','Symbols and indices','low','p26_bottom','The Sigma ends in a compact raised/dense foot-tip. A separate i stroke and dot cannot be securely isolated. Plain Sigma leads; Sigma_i remains an explicit alternative, so this is a provisional comparison rather than a resolved error claim.',False,'The presence of the first tuple index remains unresolved.')
ch('final tuple, separation of s and b labels',r's_{ij},b_{ij}',r's_{ij},b_{ij}',r's_{ij}\ b_{ij}',True,True,'text not on the page','Text that is not on the page','high','p26_bottom','The two indexed label groups are separated by a visible gap but no independent comma stroke. The colon after b_ij consists of two distinct points and is retained.')
ch('final diagram geometry',r'\Sigma_{ij}\arrow[ur]\arrow[dr]',r'\Sigma_{ij}\rightrightarrows\Sigma_i,\Sigma_j',fork,True,True,'drawing or diagram','Drawings and diagrams','high','p26_bottom','There are three objects and two short, nearly parallel, slightly divergent shafts. The upper endpoint is dense and pointed; the lower endpoint has a small loop. The source heights and separate target levels are reproduced without converting the lower loop into a generic head.')
ch('after final outer parenthesis',r'$)$,',r'\bigr)',r'$),$',False,True,'omission','Omissions','high','p26_bottom','A separate sloping comma follows the large outer closing parenthesis at the lower-right edge.')
ch('bottom foliation',r'\mspage{69}','(nothing)',r'\margin{69}',True,True,'other','Other','high','p27_folio','The pale lower-left figures are 6 and 9 in another hand. There is no authorial number at the head. The foliation is retained separately as a margin element.')

decisions=[
dict(id='M0620',decision='first',reading='en',evidence='A small looped e joins the low n stroke; no tall d ascender precedes the final loop.',crop='crops/150_scan070_p00_open.png',box=boxes['p00_open'],confidence='high'),
dict(id='M0621',decision='first',reading='moralement',evidence='The m-o-r-a-l sequence, compressed following e-m-e-n strokes and final t are visible in the live interlinear word. Its leader enters after correspondant.',crop='crops/150_scan070_p15_moral.png',box=boxes['p15_moral'],confidence='high'),
dict(id='M0622',decision='undecided',reading=r'\unsure{la|le}',evidence='The tall looped l is clear; the following small filled lobe favours a but does not securely separate a from e. Both source alternatives remain.',crop='crops/150_scan070_p20_factor.png',box=boxes['p20_factor'],confidence='low')]

doubts=[]
def db(place,reading,alternatives,reason):
    doubts.append(dict(place=place,reading=reading,alternatives=alternatives,confidence='low',reason=reason))
db('word after tte',r'\unsure{flèche|flèches}','flèche; flèches','The upper-right ending has a reworked raised curl and sloping stroke. A final s cannot be separated securely from that reworking. Both witnesses lead with flèche, so the added doubt alone is not counted as a reading change.')
db('superscript in u membership',r'u\in\Sigma^{\unsure{*|<}}(1)','*; <','The raised mark has a looped left mass and short right branches; the dense joins do not securely settle star versus angle. Both witnesses read star.')
db('cancelled abbreviation before Si',r'\deleted{\unsure{i.e.}}','i.e.; obscured punctuation','A dotted first stem and e-like loop survive under the strike; the punctuation merges with the cancellation and stays doubtful.')
db('cancelled words below espace top.',r'\deleted{\unsure{ens. ord.}}','ens. ord.; obscured joins/final stop','The upper replacement’s p descender crosses the cancelled first group. The ord group is partly visible, while the last stop and some joins lie under the strike.')
db('equality after ordonné, writing state',r'$\Sigma=\Sigma_{(0)}$',r'inline equality; \inserted{\Sigma=\Sigma_{(0)}}','The group follows the rising main baseline with no independent leader. Its spatial position is clear, but the written stage of this compact group is not recoverable. H marks an addition; that historical interpretation remains open.')
db('product below vertical cap',r'\Sigma\unsure{\times}\Sigma','times with a looped/reworked left arm; unresolved exact contour','The left part forms a small loop while two rightward arms cross. The visible contour is retained as a local doubt on times; no expected product formula resolves it.')
db('a after moralement',r'\unsure{à|a}','à; a','The possible grave lies within the insertion leader zone; it cannot be independently isolated from that leader.')
db('cancelled verb after Sigma',r'\deleted{\unsure{sont|soient}}','sont; soient','The initial s, round o and tall t are legible; the cancellation masks the middle arch. The leading sont is retained with H’s alternative.')
db('M0622',r'\unsure{la|le}','la; le','The filled terminal lobe after the tall l favours a but leaves e possible.')
db('cancelled factorisation',r'\deleted{\unsure{factorisation}}','factorisation; obscured crossed ending','The tall f and t strokes and intervening letter fragments support factorisation, but the struck ending runs into the right paper edge and is not completely recovered.')
db('two points after canonical source Sigma',r'\unsure{:}','tilted colon-like group; unassigned two-point separator','Both dark points are visible within the formula row; their intended role remains uncertain.')
db('mono-map endpoint',mono_map,'rightward arrow; unheaded shaft with a filled terminal point','The compact filled point has no exposed V. The arrow reading leads, but its contour remains uncertain; both witnesses read an arrow.')
db('first Sigma in final tuple',r'\unsure{\Sigma|\Sigma_i}','Sigma; Sigma_i','Only a compact raised/dense foot-tip is isolated at the lower right of Sigma. A distinct index stroke is not securely recovered, so plain Sigma leads while the indexed candidate remains open.')

inventory=[]
def el(kind,pos,reading,hand='his hand',**kw):
    row=dict(element=f'E{len(inventory)+1:02}',kind=kind,position=pos,first_words_or_objects=reading,sheet_kind='text',hand=hand,transcribed='yes');row.update(kw);inventory.append(row)
el('text','opening four main baselines','Supposons en plus; d) toute flèche inversible ... ens ordonné).',details='No authorial number at the head; inversible has no added underline and the first ens has no stop.')
el('text','assertion paragraph, Alors through croissante','Alors on conclut ... l’ens. pré-ordonné I ... tte flèche ... son image ...',details='Written line-end hyphen retained. The reworked flèche ending and raised Sigma sign are doubtful.')
el('deletion','left start of the Si line',r'\deleted{\unsure{i.e.}}',details='The strike crosses the abbreviation; surviving dot/stem and loop do not settle all punctuation.')
el('deletion','right end of Si ... associé à un',r'\deleted{\unsure{ens. ord.}}',details='The first group is crossed also by the live replacement’s p descender; old joins and final stop remain doubtful.')
el('insertion','immediately above cancelled ens. ord.',r'\inserted{espace top.}',attachment='Replacement after un; above the cancelled group, before the following baseline ordonné.')
el('display','inline after ordonné',r'\Sigma=\Sigma_{(0)}',details='Compact equality on the rising main baseline, comma after it and no comma before. Historical insertion state remains open.')
el('display','right end of the equality/prose line',first_map,details='Separate underlines; unheaded shaft with short downward terminal stub.')
el('insertion','above strictly increasing phrase',r'\inserted{une appl.}',attachment='Curved leader passes below the two words and enters before strictement.')
el('text','Revenons paragraph opening','Revenons alors à un ... ens. ordonné topologique')
el('deletion','between un and ens. in that opening',r'\deleted{catég}',details='c/a fragments, tall t, accented e and g descender remain legible under the strike.')
el('display','ordered-space tuple and vertical relation',tuple_formula,details='Squeezed initial Sigma= retained. Baseline first (0)/(1), lowered inner (0), raised left angle; cap and lower product kept vertically aligned.')
el('text','conditions and parenthetical explanation','satisfaisant aux conditions a) b) c) et 1°) de la page (27) (correspondant ... à/a un déploiement d’une stratification locale équisingulier),')
el('insertion','above correspondant ... un déploiement',r'\inserted{moralement}',attachment='Leader bends down after correspondant. It does not attach to the preceding 1°) reference.')
el('text','finite-dimension wording and canonical map sentence','et tel que les comp. connexes de Sigma ... de dim finie. Considérons alors ... canonique ... avec I=pi_0(Sigma),',details='The cancelled verb is left cancelled, and the source’s resulting grammatical fragment is preserved.')
el('deletion','right end after Sigma in the components line',r'\deleted{\unsure{sont|soient}}',details='No separate replacement word is assigned to this cancelled group.')
el('deletion','right end after la/le on the next line',r'\deleted{\unsure{factorisation}}',details='Cancelled ending reaches the paper edge; full recovery remains doubtful.')
el('insertion','directly above factorisation',r'\inserted{morphisme}',attachment='Live upper word replaces factorisation. It is distinct from the earlier cancelled verb.')
el('display','canonical map and following equality',second_map+r',\quad I=\pi_0(\Sigma)',details='Two tilted source-side points retained as doubtful colon. Short shaft has a dense terminal upright; target I is reworked with no assigned prior letter.')
el('text','additional i<j clause','et supposons de plus que pour i<j (i,j in I)')
el('display','mono-map and its caption',mono_map+r'\quad\hbox{soit \uline{mono} i.e. plongement fermé}',details='Filled terminal point remains doubtful in shape. fermé continues on the next short line at the right edge, without a supplied stop.')
el('text','last two main baselines','On est alors sous les conditions de p.28, données a) b) c)')
el('diagram','final tuple and two-branch diagram',bottom,details='First tuple Sigma may have a compact i; kept plain-leading with alternative. No comma between s_ij and b_ij. Three diagram objects and two slightly divergent shafts; upper pointed dense endpoint and lower loop. Final outer comma retained.')
el('margin note','bottom left',r'\margin{69}','another unnamed hand',details='Pale foliation, separate from any authorial numbering.')

audit=[]
def ab(name,kind,reading):
    b=boxes[name]
    audit.append(dict(box=f'B{len(audit)+1:02}',kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=reading.strip()))
ab('p00_open','lexical disagreement','Supposons en plus')
ab('p01_inversible','lexical disagreement','inversible')
ab('p02_ens','lexical disagreement','ens')
ab('p03_pre','lexical disagreement',r'''l'ens. pré-
% The initial l is locally reworked; no recoverable older letter is assigned.
% The continuation ordonné is on the next baseline outside this rectangle.''')
ab('p04_tte','lexical disagreement',r'tte \unsure{flèche|flèches}')
ab('p05_ufmla','doubtful formula',r'''$u\in\Sigma^{\unsure{*|<}}(1)$,
% A clipped descender from the preceding word flèche enters the top edge.''')
ab('p06_son','handwritten number',r'''son image dans $I(1)$ n'est pas une identité;
% At the upper edge are clipped lower parts of the preceding baseline.
% At the lower right are portions of espace top. and its cancelled base,
% separately covered in B09; they are not part of the son image sentence.''')
ab('p07_ie','struck passage',r'\deleted{\unsure{i.e.}}')
ab('p08_espace','insertion',r'''un \deleted{\unsure{ens. ord.}}\inserted{espace top.}
% The live replacement is above the crossed group. A small upper-edge
% fragment belongs to the preceding identity clause's punctuation.''')
ab('p09_eq','doubtful formula',r'''ordonné $\Sigma=\Sigma_{(0)}$,
% The lower edge clips upper portions of the following une appl. insertion.
% Equality placement is on the rising main baseline; written stage is open.''')
ab('p10_firstmap','medium-confidence departure','$'+first_map+r'''$
% Literal short shaft with a downward terminal stub, no exposed V.''')
ab('p11_uneappl','insertion',r'''est \inserted{une appl.} \uline{strictement} croissante.
% The leader bends before strictement. Upper-edge fragments belong to
% ordonné and the following Sigma equality on the preceding baseline.''')
ab('p12_categ','struck passage',r'''\deleted{catég} ens. ordonné
% The lowest part of the g descender meets the lower boundary. A small
% mark at the lower edge belongs to the raised angle in the tuple below.''')
ab('p13_tuple','doubtful formula',r'''\[
'''+tuple_formula+r'''
\]
% A clipped lower loop from the preceding cancelled catég lies at the top.''')
ab('p14_refs','handwritten number',r'a) b) c) et $1^\circ$)')
ab('p15_moral','insertion',r'''(correspondant \inserted{moralement} \unsure{à|a} un déploiement
% The live insertion is above the baseline and its leader enters after
% correspondant. Upper-edge fragments belong to conditions and its labels.''')
ab('p16_page27','handwritten number',r'''de la page (27)
% A clipped descender from the preceding baseline enters the upper edge.''')
ab('p17_locale','lexical disagreement',r'''locale équisingulier),
% The broad lower curve belongs to g. A clipped upper part of the next
% line's Sigma enters at the lower right; that complete Sigma is in B19.''')
ab('p18_sont','struck passage',r'$\Sigma$ \deleted{\unsure{sont|soient}}')
ab('p19_dim','lexical disagreement',r'''de dim finie.
% An upper-edge descender is clipped from the preceding baseline.''')
ab('p20_factor','struck passage',r'''\unsure{la|le} \deleted{\unsure{factorisation}}\inserted{morphisme}
% morphisme is above the crossed word. The old f descender is clipped at
% the bottom; the old word's final strokes reach the right paper edge.
% A small upper-left fragment belongs to the preceding main baseline.''')
ab('p21_canon','doubtful formula','$'+second_map+r'''$ avec $I=\pi_0(\Sigma)$,
% The source-side colon represents the observed tilted two-point group.
% The target I is reworked, without assigning an earlier letter.''')
ab('p22_ij','doubtful formula',r'$i<j$ ($i,j\in I$)')
ab('p23_mono','doubtful formula','$'+mono_map+'$')
ab('p24_ferme','lexical disagreement',r'''soit \uline{mono} i.e. plongement fermé
% fermé is on the short lower continuation at the right edge; accent
% visible, no separate final stop. Tiny lower-edge fragments belong to
% the following main baseline, not to this caption.''')
ab('p25_p28','handwritten number',r'''de p. 28,
% Upper-edge loop: preceding fermé's f descender. At the bottom, the
% next diagram's upper target Sigma is clipped; complete target is in B27.''')
ab('p26_bottom','doubtful formula',r'''données a) b) c)
'''+bottom+r'''
% The top edge clips lower portions of the preceding On est alors line,
% including its right-end comma. The full final tuple and both diagram
% targets, shafts and outer closing parenthesis/comma are inside this box.''')
ab('p27_folio','handwritten number',r'\margin{69}')
ab('p28_si','lexical disagreement','Si')

purposes={
'p00_open':'Opening en/de choice M0620.',
'p01_inversible':'Check H’s underline/emphasis on inversible.',
'p02_ens':'Written ens without supplied stop.',
'p03_pre':'Reworked l, ens. stop, accent and line-end dash in pré-.',
'p04_tte':'Short tte versus toute; reworked ending of flèche.',
'p05_ufmla':'Whole u membership formula, raised sign, numeral1 and comma.',
'p06_son':'Son image clause, I(1), and H’s supplied a/qui.',
'p07_ie':'Cancelled abbreviation i.e. with obscured punctuation.',
'p08_espace':'Live espace top. above cancelled ens. ord.; placement after un.',
'p09_eq':'Whole equality after ordonné, punctuation, argument0 and writing-state question.',
'p10_firstmap':'Whole first Sigma-to-I expression, underlines and short terminal stub.',
'p11_uneappl':'Inserted une appl. and its leader before strictly increasing wording.',
'p12_categ':'Cancelled catég, following ens. stop and ordonné.',
'p13_tuple':'Whole tuple and vertical cap/product; squeezed equality, all degrees, final angle and product contour.',
'p14_refs':'Condition labels and handwritten1°).',
'p15_moral':'Moralement M0621, leader attachment and baseline a/à un.',
'p16_page27':'Complete page(27) reference.',
'p17_locale':'Locale/localement and équisingulier/équisingulière lexical differences.',
'p18_sont':'Whole cancelled sont/soient group beside Sigma.',
'p19_dim':'Dimension short form without stop and final finie. punctuation.',
'p20_factor':'Article M0622, cancelled factorisation and inserted morphisme; page-edge strokes.',
'p21_canon':'Whole canonical map plus equality, source-side points, reworked I, and numeral0.',
'p22_ij':'Complete i<j and parenthesised i,j membership.',
'p23_mono':'Whole Sigma_ij-to-Sigma_j expression and compact filled endpoint.',
'p24_ferme':'Mono caption, i.e. stops, accent and page-edge ending fermé.',
'p25_p28':'Reference p.28 and following comma.',
'p26_bottom':'Whole final data tuple and two-branch diagram, indices, punctuation and endpoint shapes.',
'p27_folio':'Pale other-hand foliation69.',
'p28_si':'Capital Si versus H lowercase si.'}

record=dict(scan='070',reader='reader_b',line_count=24,changes=changes,decisions=decisions,inventory=inventory,doubts=doubts,
notes=[
dict(id='150-070-N01',text='The manuscript adds condition d), stating that every invertible arrow of the underlined Sigma is an identity, and gives the ordered-set category as its example. It then says that the preordered I is ordered and that a nonidentity arrow has a nonidentity image in I(1). These are the author’s statements; they were not independently proved in this reading.'),
dict(id='150-070-N02',text='The author describes an associated ordered topological-space setting and calls the underlined Sigma-to-I application strictly increasing. The replacement espace top. lies above the cancelled ens. ord., and une appl. has a separate leader before strictement. The compact Sigma=Sigma_(0) follows ordonné on the rising main baseline; its historical addition state cannot be settled from a leader, since none is independently visible.'),
dict(id='150-070-N03',text='The next passage returns to a topological ordered set and writes the tuple with the extra squeezed initial Sigma=, a vertical cap/product relation, and local argument heights. It refers to conditions a), b), c), 1°) on p.27, inserts moralement after correspondant, and describes a déploiement of a stratification locale équisingulier. Those exact source endings are retained. No mathematical expectation was used to resolve the looped product sign.'),
dict(id='150-070-N04',text='The finite-dimension wording contains a cancelled sont/soient group and is left in its resulting source form. The following live morphisme replaces cancelled factorisation. The author then assumes the written Sigma_ij-to-Sigma_j map is mono, explained as plongement fermé, and refers to the conditions of p.28. The final tuple and two-branch diagram are transcribed literally, including the unsettled first Sigma index and the missing comma between the two indexed labels. These reports do not claim a checked implication.'),
dict(id='150-070-N05',text='M0620 resolves to en, M0621 to moralement, and M0622 remains la|le. The crossed abbreviations and factorisation remain doubtful, as do the reworked flèche ending, the first raised Sigma mark, the looped product contour, the accent under the insertion leader, and the cancelled verb’s middle. The canonical map’s two discrete tilted points are retained as unsure{:}; their role is not supplied.'),
dict(id='150-070-N06',text='No authorial page number is visible at the head. The pale bottom-left69 is another hand’s foliation and is represented as a margin element. The line count is24 principal text/formula baselines including the short fermé continuation; subordinate vertically placed product/diagram objects and interlinear insertions are inventoried separately. Written1°), reference27, reference28, the formula degrees and all pi-zero numerals are covered by targeted audit rectangles.'),
dict(id='150-070-N07',text='The two short Sigma-to-I shafts have terminal stubs rather than exposed V-shaped heads. The target I in the second map is reworked; its brown diagonal does not securely recover an older glyph, so none is assigned. The final diagram has three objects and two nearly parallel, slightly divergent shafts; a dense pointed upper endpoint and a small looped lower endpoint are drawn separately. Clipped neighbouring fragments are identified in the audit readings without reattaching them to the target phrase.')
],check_events=[],
notation=[
dict(form=r'\uline{\Sigma},\uline I',meaning='The underlined symbols written at the endpoints of the author’s category maps.',evidence='Separate added horizontal strokes beneath the body strokes of Sigma and I; first map especially clear.',places='first and canonical Sigma-to-I expressions; categorical Sigma occurrences'),
dict(form=r'\Sigma=\Sigma_{(0)}',meaning='The author’s equality following ordonné.',evidence='Two Sigmas, a two-stroke equality and a low parenthesised0; comma after the group.',places='first paragraph, after ordonné'),
dict(form=r'\Sigma=\Sigma(0),\ \Sigma(1),\ \delta(\Sigma_{(0)})',meaning='Literal local notation and argument heights in the author’s tuple.',evidence='Squeezed first Sigma=, baseline first0 and following1, lower inner0 in delta’s argument.',places='central display'),
dict(form=r'\underset{\underset{\Sigma\unsure{\times}\Sigma}{\cap}}{\Sigma(1)}',meaning='The source’s vertically arranged relation and lower product.',evidence='Separate cap immediately below Sigma(1); lower two Sigmas and a looped/crossing middle sign.',places='central display'),
dict(form=r'\Sigma^{\unsure{*|<}}(1);\ \Sigma^{<}(1)',meaning='Local raised forms beside Sigma, retained occurrence by occurrence.',evidence='Dense looped first mark; clear left-junction two-arm angle in the central tuple.',places='u membership and central tuple ending'),
dict(form=r'\mathrel{\relbar\joinrel\relbar}',meaning='Literal unheaded short shafts in the two Sigma-to-I expressions.',evidence='Downward terminal stub in the first; dense small upright in the second; no exposed V.',places='first map and canonical map'),
dict(form=r'\unsure{:}',meaning='The tilted two-point group after the canonical source Sigma; role uncertain.',evidence='Two discrete dark points immediately before the short shaft.',places='canonical map'),
dict(form=r'\unsure{\Sigma|\Sigma_i}',meaning='The unresolved first item of the author’s final tuple.',evidence='A raised/dense foot-tip is visible, but no separate index stroke is securely isolated.',places='last-line tuple')
],
abbreviations=[
dict(written='p.ex.',expansion='par exemple',places='opening parenthesis'),
dict(written='ens',expansion='ensemble',places='first example; no written stop'),
dict(written='ens.',expansion='ensemble',places='l’ens. pré-ordonné; cancelled ens. ord.; Revenons phrase'),
dict(written='tte',expansion='toute',places='first assertion'),
dict(written='i.e.',expansion='id est',places='first assertion, cancelled abbreviation, mono caption'),
dict(written='ord.',expansion='ordonné',places='cancelled ens. ord. candidate; final stop obscured'),
dict(written='top.',expansion='topologique',places='inserted espace top.'),
dict(written='appl.',expansion='application',places='inserted une appl.'),
dict(written='catég',expansion='catégorie',places='cancelled fragment before ens.'),
dict(written='comp.',expansion='composantes',places='components clause'),
dict(written='dim',expansion='dimension',places='de dim finie; no written stop'),
dict(written='p.',expansion='page',places='reference28')
],
hand_log=[
dict(habit='The same parenthesised degree can stand at different local heights.',places='equality after ordonné; central display',scope='Every0/1 group on this sheet read separately; no uniform baseline/subscript rule imposed.',witness_errors='C lowers the first two tuple groups; H gives the inner delta0 and the earlier equality0 at baseline.'),
dict(habit='Insertion leaders can cross the region of an accent and resemble an opening parenthesis.',places='une appl.; moralement and following a/à',scope='Both leaders traced individually; the a accent remains doubtful.',witness_errors='H omits une appl. and places au moins after1°) instead of moralement after correspondant.'),
dict(habit='A descender from live inserted writing can cross a cancelled word.',places='espace top. above ens. ord.; morphisme above factorisation',scope='Each live/cancelled layer read separately.',witness_errors='H has a spurious additional illegible insertion after the earlier cancelled verb and leaves morphisme illegible.'),
dict(habit='A long g descender forms a broad lower return resembling a separate curve or underline.',places='équisingulier',scope='The curve is continuous with this g only; no general glyph rule asserted.',witness_errors='No separate curve is assigned in either witness; the present reading confirms that state.'),
dict(habit='Compact terminal ink can conceal an index or a final letter.',places='flèche ending; first Sigma in final tuple; la/le',scope='These three places remain locally doubtful; no uniform completion from context.',witness_errors='Both witnesses give singular flèche and indexed first Sigma; H fixes la while C leaves la/le open.'),
dict(habit='Short forms have locally written point counts and line-end dashes.',places='ens; ens.; tte; dim; pré-',scope='Each stop and dash checked on its own crop.',witness_errors='H supplies stops after ens and dim, expands tte and omits the line-end hyphen.'),
dict(habit='Short shafts can end in dense stubs or loops instead of a generic open arrowhead.',places='two Sigma-to-I maps; mono-map; final two branches',scope='All five connectors read individually; mono-map contour remains doubtful.',witness_errors='Both witnesses use generic arrows; H also flattens the final two-level fork.'),
dict(habit='A very small two-point group may be written tilted beside a formula symbol.',places='after canonical source Sigma; colon after final b_ij',scope='Canonical group’s role remains doubtful; final label colon is clear.',witness_errors='Both witnesses omit the canonical source-side points.')
],audit_boxes=audit,
crops=[dict(file=f'crops/150_scan070_{n}.png',box=b,purpose=purposes[n]) for n,b in boxes.items()],
unresolved=[d['place']+': '+d['reading'] for d in doubts],
coverage=dict(whole_image_viewed=True,halves_viewed=['top','bottom'],all_tokens_read=True,all_C_insertions_deletions_checked=True,differences_considered=len(list(csv.DictReader((ROOT/'edition/packets/150_scan070/diffs.tsv').open(),delimiter='\t'))),macro_only_differences_ignored='Equivalent underline/emphasis wrappers where a physical underline is present; equivalent struck/inserted macros; line wrapping and math-environment syntax; H’s editorial continuity and page-reference notes. The ordering of adjacent replacement/strike macros for espace top. and ens. ord. does not change their common attachment after un. Newly added certainty-only doubts are kept in doubts rather than counted as reading changes.'))

def fix_quote_escapes(v):
    if isinstance(v,str): return v.replace(chr(92)+chr(39),chr(39))
    if isinstance(v,list): return [fix_quote_escapes(x) for x in v]
    if isinstance(v,dict): return {k:fix_quote_escapes(x) for k,x in v.items()}
    return v
record=fix_quote_escapes(record)

assert len(boxes)==29 and all((ROOT/'edition'/c['file']).is_file() for c in record['crops'])
assert len(audit)==29 and all(e['transcribed']=='yes' for e in inventory)
assert {d['id'] for d in decisions}=={'M0620','M0621','M0622'}
assert all(c['against_C'] or c['against_H'] for c in changes)
assert len({c['id'] for c in changes})==len(changes)
assert r'\illegible' not in tex and r'\mspage' not in tex
assert tex.count('\\begin{tikzcd}')==tex.count('\\end{tikzcd}')==1
payload=json.dumps(record,ensure_ascii=False,indent=2)+'\n'
json.loads(payload)
atomic_write(OUT/'150_scan070.json',payload)
print(json.dumps(dict(scan='070',changes=len(changes),against_C=sum(c['against_C'] for c in changes),against_H=sum(c['against_H'] for c in changes),doubts=len(doubts),inventory=len(inventory),audit_boxes=len(audit),crops=len(boxes))))

