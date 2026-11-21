from pathlib import Path
import json

ROOT = Path('/workspace/scratch/12caffedf246/edition')
OUT = ROOT / 'reports'
QQ = chr(96) * 2

UP = r'\mathrel{\tikz[baseline=-.5ex,x=1em,y=1em]{\draw[line width=.4pt] (0,0)--(.9,0)--(.9,.13);}}'
DOWN = r'\mathrel{\tikz[baseline=-.5ex,x=1em,y=1em]{\draw[line width=.4pt] (0,0)--(.9,0)--(.9,-.10);}}'
SOMMET = r'''\overbrace{\mathcal D_r\longrightarrow D_*}^{\inserted{\text{morphismes OPENQUOTEpremier sommet''}}}'''.replace('OPENQUOTE', QQ)

F206 = r'''\[
\tag{206}
\begin{gathered}
\left\{\begin{aligned}
\mathcal D_*^*&=\coprod_{d_0\geq d_1\cdots\geq d_r\geq0}D^*_{d_0,d_1,\ldots,d_r}\\
&=\text{image inverse de }D_*^*=\coprod_{d\in\mathbf N}D_d^*\text{ par}\\
&\quad\text{le morphisme }\unsure{0|o}:\mathcal D_*UPTURN D_*\\
&\quad\text{défini par les }D_{d_0,\ldots,d_r}\longrightarrow D_{d_0}
\end{aligned}\right.\\
\text{i.e. défini par les }SOMMET
\end{gathered}
\]'''.replace('UPTURN', UP).replace('SOMMET', SOMMET)

CHAIN = r'''\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
\&\&\bullet\rlap{\(\,0\)}\arrow[d,no head]\\
\text{(transposé de}\&\underset{0}{\bullet}\arrow[ur]\&\bullet\rlap{\(\,1\)}
\arrow[d,no head,to path={(\tikztostart.south)--([yshift=2pt]\tikztotarget.center)--++(-.045,.04)\tikztonodes}]\&\text{)}\\
\&\&{}\rlap{\(\,2\)}\\
\&\&\vdots\arrow[d]\\
\&\&{}\rlap{\(\,r\)}
\end{tikzcd}}'''

F207 = r'''\[
\tag{207}
\left\{\begin{aligned}
P_{d_0,d_1,\ldots,d_r}&=\text{image inverse du }\overbrace{P_{d_0}}^{G_d\text{-torseur}}\text{ sur }D_{d_0}\\
&\qquad\text{par }D_{d_0,\ldots,d_r}DOWNTURN D_{d_0}\\
P^*_{d_0,d_1,\ldots,d_r}&=P_{d_0,\ldots,d_r}\mid D^*_{d_0,\ldots,d_r}
\end{aligned}\right.
\]'''.replace('DOWNTURN', DOWN)

CEST = r"\unsure{c'est}\inserted{\unsure{là|sont}} des"
ANALYT = r'Groupes \unsure{analytiques|analytiq}'

F208 = r'''\[
\tag{208}
\begin{aligned}
G_{d_0,\ldots,d_r}&=\text{image inverse de }G_{d_0}\\
&\quad\text{sur }\unsure{D_0|d_0}\text{, par }D_{d_0,\ldots,d_r}UPTURN D_{d_0}\\
G^*_{d_0,\ldots,d_r}&=G_{d_0,\ldots,d_r}\mid D^*_{d_0,\ldots,d_r}.
\end{aligned}
\]'''.replace('UPTURN', UP)

D209 = r'''\diagram{\(\bigl(\unsure{209}\bigr)\quad\)
\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]
\bigl(\widetilde\Pi_{d_0-d_r}\overset{\mathrm{déf}}{=}\unsure{\Pi_1|\pi_1}P^*_{d_0,\ldots,d_r}
\arrow[r]\arrow[d]
\&\unsure{\Pi_1|\pi_1}P^*_{d_0}\bigl(\overset{\mathrm{déf}}{=}\widetilde\Pi_{d_0}\bigr)\arrow[d]\\
\Pi_{d_0,-d_r}=\unsure{\Pi_1|\pi_1}\unsure{D_{d_0,\ldots,d_r}|D^*_{d_0,\ldots,d_r}}
\arrow[r,no head,to path={(\tikztostart.east)--([xshift=-2pt]\tikztotarget.west)--++(0,.055)\tikztonodes}]
\&\unsure{\Pi|\pi}D_{d_0}\bigl(\overset{\unsure{\mathrm{déf}|\mathrm{def}}}{=}\Pi_{d_0}\bigr)
\arrow[ul,phantom,"2\text{-cart.}" description]
\end{tikzcd}}'''

PROSE209 = r'On a donc un diagramme $2$-cartésien de groupoïdes'
tex = '\n'.join([
    r'\scanpage{129}',
    'ment définir tout de suite', F206, CHAIN, '',
    'Nous allons définir', F207,
    CEST + ' torseurs sous les ' + ANALYT, '(tores)', F208,
    PROSE209, D209, r'\margin{128}', ''
])

boxes = {
    '206first':[495,135,1090,305], '206maps':[615,320,1655,565],
    'sommet':[680,548,1560,865], '207':[575,930,1680,1370],
    'cest':[245,1395,700,1510], 'groupes':[1155,1385,1680,1510],
    '208':[625,1598,1680,1945], '209top':[335,2018,1570,2208],
    '209bottom':[410,2207,1580,2318], 'footer':[20,2305,125,2355],
    '206brace':[230,160,490,570], '209number':[210,2145,340,2295]
}

rows=[]
def row(place,C,H,final,ink,crop,confidence,kind,against_C,against_H,category,math=False,marked=False):
    rows.append(dict(place=place,C=C,H=H,final=final,scan_shows=ink,
        crop=f'crops/147_scan129_{crop}.jpg',box=boxes[crop],confidence=confidence,
        kind=kind,against_C=against_C,against_H=against_H,marked_in_H=marked,
        math_consequential=math,error_category=category))

row('(206), coproduct range',r'd_0\geq d_1\cdots\geq d_r\geq0',
    r'd_0 \geqslant d_1 \geqslant \dots \geqslant d_r \geqslant 0',
    r'd_0\geq d_1\cdots\geq d_r\geq0',
    'After the low 1 there are three small continuation strokes, followed by a distinct greater-than sign and its lower bar before d_r. There is no extra greater-than pair immediately after d_1.',
    '206first','high','text not on the page',False,True,'Symbols and indices',True)
row('(206), left brace and its lower boundary',
    r'\left\{\begin{aligned}\mathcal D_*^*&=\coprod_{d_0\geq d_1\cdots\geq d_r\geq0}D^*_{d_0,d_1,\ldots,d_r}\\&=\text{image inverse de }D_*^*=\coprod_{d\in\mathbf N}D_d^*\text{ par}\\&\quad\text{le morphisme }\unsure{0|o}:\mathcal D_*\longrightarrow D_*\\&\quad\text{défini par les }D_{d_0,\ldots,d_r}\longrightarrow D_{d_0}\\&\quad\text{i.e. défini par les }\mathcal D_r\longrightarrow D_*\end{aligned}\right.',
    '(no left brace)', F206,
    'A continuous left brace runs from the first formula down to the line défini par les D..., ending near y550. The i.e. line is below its lower end. C encloses that final line too; H sets no brace.',
    '206brace','high','insertion or placement',True,True,'Drawings and diagrams')
row('(206), map after le morphisme',r'\mathcal D_*\longrightarrow D_*',r'\mathcal{D}_{*} \to D_{*}',
    r'\mathcal D_*'+UP+r'D_*',
    'The horizontal shaft ends in a compact upward turn with a rounded dark return. A complete two-sided head cannot be separated securely, unlike the following two plainly headed maps. The literal turn is reproduced; directional intention remains open.',
    '206maps','medium','misread symbol or index',True,True,'Symbols and indices',True)
row('(206), raised first-summit annotation',r'''\inserted{morphismes OPENQUOTEpremier sommet''}'''.replace('OPENQUOTE',QQ),
    r'\add{morphismes « premier sommet »}',SOMMET,
    'The full words and paired quotation strokes sit above the D_r-to-D_* map. A long bracket under the words spans that map; its left downward curve is connected to the bracket, not an independent opening parenthesis. C places the insertion after the complete display; H drops the physical bracket.',
    'sommet','high','insertion or placement',True,True,'Insertions put in the wrong place')
row('below (206), transposé', 'transposé de','transposés de','transposé de',
    'The final é has a raised accent; the following space begins before de. There is no additional final s between é and de.',
    'sommet','high','misread word',False,True,'Words')
row('below (206), chain diagram and H abstract replacement',
    r'\begin{tikzcd}\&\bullet\,0\arrow[d]\\\underset{0}{\bullet}\arrow[ur]\&1\arrow[d]\\\&2\arrow[d,no head]\\\&\vdots\arrow[d]\\\&r\end{tikzcd}',
    r'$\{0\} \to \Delta_r$',CHAIN,
    'There are three solid points: the separate source 0, the upper chain 0, and chain 1. The 0-to-1 shaft ends in the round point, with no arrowhead. The next descending shaft has a one-sided leftward turn at 2. There is no separate shaft from 2 into the continuation marks. The oblique entering edge and final descending edge have complete heads. Neither braces around the source 0 nor the text Delta_r is written.',
    'sommet','medium','drawing or diagram',True,True,'Drawings and diagrams',True,True)
row('(207), image inverse du', 'image inverse du','image inverse de','image inverse du',
    'The second word after inverse has a d loop and upright followed by a low connected u ending; it is not a lone e after d.',
    '207','high','misread word',False,True,'Words')
row('(207), annotation over P_{d_0}',r'G_d\text{-torseur}',r'$G_{d_0}$-torseurs',r'G_d\text{-torseur}',
    'The G has one low d, with no independent lower 0. A hyphen precedes torseur. The ending exits from r without a separate final s. The curved bracket points to P_{d_0}.',
    '207','high','misread symbol or index',False,True,'Symbols and indices',True)
row('(207), map connector',r'\unsure{\text{---}|\longrightarrow}',r'\to',DOWN,
    'The shaft is almost horizontal; a tiny dark terminal segment turns downward. Neither a left endpoint bar/hook nor a complete right arrowhead is visible. A literal shaft with that turn retains the ink without deciding intended direction.',
    '207','medium','misread symbol or index',True,True,'Symbols and indices',True)
row('after (207), c’est and raised word',r"\unsure{c'est}\inserted{\unsure{là|sont}}",r"\uncertain{c'est-à-dire}",
    r"\unsure{c'est}\inserted{\unsure{là|sont}}",
    'A c and apostrophe survive at the left; the low following strokes are retraced and cross the insertion leader. Above them are a tall first stroke, low join and small triangular final loop, favoring là, but their full segmentation and attachment are not secure. There are no separate inked à-dire words on the baseline.',
    'cest','medium','misread word',False,True,'Words',False,True)
row('after (207), Groupes', 'Groupes','groupes','Groupes',
    'The initial has a large open upper capital curve, reaching well above the following low letters, plus a retraced inner/descending loop. It is larger than the nearby lower-case g form; no distinct earlier letter can be separated.',
    'groupes','high','misread word',False,True,'Words')
row('(208), base after sur',r'\unsure{D_0|D_{d_0}}',r'D_{d_0}',r'\unsure{D_0|d_0}',
    'A single tall looped D/d-like glyph is followed by one small low oval 0 and a comma. No second d-shaped upright or bowl can be separated before that 0. The capital/lower-case identity of the first glyph remains open.',
    '208','medium','misread symbol or index',False,True,'Symbols and indices',True)
row('(208), map connector',r'\unsure{\text{---}|\longrightarrow}',r'\to',UP,
    'The shaft has a short upward turn at the right end, without an independently visible second wing. Both endpoints have been checked; no source hook or bar is present.',
    '208','medium','misread symbol or index',True,True,'Symbols and indices',True)
row('(208), absent left brace',r'\begin{aligned}',r'\begin{cases}',r'\begin{aligned}',
    'The two equations are unbraced. There is blank paper immediately before their initial G letters; no counterpart of the large braces of (206) and (207) is drawn.',
    '208','high','text not on the page',False,True,'Symbols and indices')
row('(209), opening curve before the upper-left definition',r'\bigl(', '(nothing)',r'\bigl(',
    'A detached opening-parenthesis-shaped curve survives before the first tilde-Pi. Its upper part is retraced, but the long lower arc is separate from the letter. No matching closing parenthesis follows that upper-left definition.',
    '209top','medium','omission',False,True,'Symbols and indices')
row('(209), upper-left named index',r'\widetilde\Pi_{d_0- d_r}',r'\widetilde{\Pi}_{d_0 \dots d_r}',r'\widetilde\Pi_{d_0-d_r}',
    'The low 0 is followed by a short horizontal dash and then d_r. No flanking comma or array of separate dots is visible in this named index.',
    '209top','high','misread symbol or index',False,True,'Symbols and indices')
row('(209), lower-left named index',r'\Pi_{d_0,\ldots,d_r}',r'\Pi_{d_0 \dots d_r}',r'\Pi_{d_0,-d_r}',
    'A low comma follows d_0, then a horizontal dash before d_r. There is no second comma after that dash. This differs from both the unpunctuated upper-left index and the comma/continuation/comma indices on the P and D terms.',
    '209bottom','high','misread symbol or index',True,True,'Symbols and indices')
row('(209), lower-left retraced D',r'\unsure{D_{d_0,\ldots,d_r}}',r'D^{*}_{d_0,\dots,d_r}',
    r'\unsure{D_{d_0,\ldots,d_r}|D^*_{d_0,\ldots,d_r}}',
    'The D has a heavy stem, duplicate upper arcs and internal crossings. There is no separable high star to its right. An embedded or overwritten star cannot be ruled out from the internal strokes, so bare D is the leading reading and D* remains explicit. The visible d_0, continuation, and d_r below are not cancelled.',
    '209bottom','medium','misread symbol or index',False,True,'Symbols and indices',True,True)
row('(209), lower-right unstarred D',r'\Pi D_{d_0}',r'\Pi D^{*}_{d_0}',r'\unsure{\Pi|\pi}D_{d_0}',
    'The D is followed only by its low d_0. The upper-right area is clear and contains no star. No subscript 1 is written on the preceding roof-and-legs sign either. H itself observes in a note that this star is not visible.',
    '209bottom','high','text not on the page',False,True,'Symbols and indices',True,True)
row('(209), bottom connector',r'\arrow[r]',r'\arrow[r]',
    r'\arrow[r,no head,to path={(\tikztostart.east)--([xshift=-2pt]\tikztotarget.west)--++(0,.055)\tikztonodes}]',
    'The long lower shaft ends in an upward terminal turn; no separate lower wing can be discerned. The other three square edges have full heads. The literal terminal stroke is retained without changing the mathematical claim.',
    '209bottom','medium','drawing or diagram',True,True,'Drawings and diagrams',True)
row('(209), central label',r'2\text{-cart.}', '(nothing in the set diagram)',r'2\text{-cart.}',
    'The central 2, hyphen, abbreviated cart and terminal point are dark and distinct between the two rows. H describes this real label only in its editorial note; the note is not copied as prose.',
    '209top','high','omission',False,True,'Omissions',True)
row('(209), number at left', '(209)', '(nothing beside the set diagram)',r'(\unsure{209})',
    'Three digits stand in parentheses. The first has an upper arch and downstroke with its lower return merging into the opening parenthesis; 2 is leading but not secure. The middle oval is 0 and the last 9 has a long descending return. H mentions the number only in its editorial note.',
    '209number','medium','omission',False,True,'Omissions')
row('bottom-left pencil number',r'\margin{128}', '(nothing)',r'\margin{128}',
    'The pencil inscription consists of an oblique/vertical 1, a curved 2 with returning baseline, and a two-loop 8. It is paler than the principal ink and detached from the diagram.',
    'footer','high','omission',False,True,'Omissions')

decisions=[]
def decision(id,which,reading,ink,crop,confidence):
    decisions.append(dict(id=id,decision=which,reading=reading,ink=ink,
        crop=f'crops/147_scan129_{crop}.jpg',box=boxes[crop],confidence=confidence))
decision('M1283','undecided',r'\unsure{0|o}',
    'The map label is a small closed oval with a pointed return. The nearby zero forms share that contour; neither shape nor the first-summit role distinguishes numeral 0 from letter o.', '206maps','medium')
decision('M1284','other',DOWN,
    'Literal shaft plus a tiny downward terminal, rather than an undecorated dash or a complete two-sided arrowhead; its intended function remains open.', '207','medium')
decision('M1285','undecided',r"\unsure{c'est}",
    'The initial c/apostrophe and following e-like loop are visible; the remaining low strokes overlap the long leader and retracing. No complete alternative word is secure.', 'cest','low')
decision('M1286','undecided',r'\unsure{là|sont}',
    'The raised unit has a tall first stroke and small final loop favoring là; the tiny possible accent and intermediate joins are too compressed to resolve it fully. The leader meets the preceding baseline near its t-like stroke.', 'cest','medium')
decision('M1287','first',r'\unsure{D_0|d_0}',
    'The original index fork is settled: there is one glyph followed directly by low 0, with no independent subscript d. A new case uncertainty D/d remains because the tall first glyph is cursive and looped.', '208','medium')
decision('M1288','other',UP,
    'Literal shaft with an upward terminal turn; neither a plain dash nor a complete two-sided head captures every visible stroke. Intended direction is left open.', '208','medium')
decision('M1289','undecided',r'\unsure{D_{d_0,\ldots,d_r}|D^*_{d_0,\ldots,d_r}}',
    'The D is heavily retraced; the internal crossings might conceal a decoration, but no separate star can be extracted. The whole square was reread, including both bare/possibly starred bases and all endpoint strokes.', '209bottom','medium')

inventory=[]
def inv(kind,position,reading,hand='his hand'):
    inventory.append(dict(element=f'E{len(inventory)+1:02d}',kind=kind,position=position,
        first_words_or_objects=reading,sheet_kind='text',hand=hand,transcribed='yes'))
inv('text','top baseline, y60–120','ment définir tout de suite')
inv('display','upper block, y150–550',r'(206) \mathcal D_*^*=\coprod_{d_0\geq d_1\cdots\geq d_r\geq0}D^*_{d_0,d_1,\ldots,d_r}')
inv('insertion','above the i.e. map, y555–605',r'''\inserted{morphismes OPENQUOTEpremier sommet''}'''.replace('OPENQUOTE',QQ))
inv('display','below (206) brace, y600–650',r'\text{i.e. défini par les }'+SOMMET)
inv('diagram','upper-right chain and transposé parenthesis, y650–855',CHAIN)
inv('text','middle introductory baseline, y900–975','Nous allons définir')
inv('display','annotation over P_{d_0}, y935–1035',r'\overbrace{P_{d_0}}^{G_d\text{-torseur}}')
inv('display','middle system, y1030–1355',F207)
inv('text','baseline after (207), y1415–1505',CEST+' torseurs sous les '+ANALYT)
inv('insertion','raised unit over c’est, y1415–1450',r'\inserted{\unsure{là|sont}}')
inv('text','short parenthetical line, y1540–1590','(tores)')
inv('display','lower system, y1620–1920',F208)
inv('text','baseline above square, y1980–2045',PROSE209)
inv('diagram','bottom square and number, y2035–2310',D209)
inv('margin note','bottom-left corner, y2310–2345',r'\margin{128}','pencil hand, attribution undetermined')

doubts=[
    dict(place='(206), map label',reading=r'\unsure{0|o}',alternatives='numeral zero; lower-case o',confidence='medium'),
    dict(place='(206), first map connector',reading=UP,alternatives='literal upward terminal turn; reduced rightward arrowhead',confidence='medium'),
    dict(place='chain after (206), descending connector to 2',reading=r'\arrow[d,no head,to path={(\tikztostart.south)--([yshift=2pt]\tikztotarget.center)--++(-.045,.04)\tikztonodes}]',alternatives='one-sided leftward terminal; reduced downward arrowhead',confidence='medium'),
    dict(place='(207), map connector',reading=DOWN,alternatives='shaft with tiny downward terminal; reduced rightward arrowhead',confidence='medium'),
    dict(place='after (207), residual baseline',reading=r"\unsure{c'est}",alternatives='c’est with retracing/insertion leader; letters partly overwritten, no secure complete alternative',confidence='low'),
    dict(place='after (207), raised unit and attachment',reading=r'\inserted{\unsure{là|sont}}',alternatives='là, perhaps la if the possible accent is incidental; sont remains a weaker segmentation; exact insertion attachment uncertain',confidence='medium'),
    dict(place='after (207), clipped right-edge word',reading=r'\unsure{analytiques|analytiq}',alternatives='full ending compressed at the edge; visibly curtailed analytiq with no secure terminal point',confidence='medium'),
    dict(place='(208), small base glyph',reading=r'\unsure{D_0|d_0}',alternatives='capital/cursive D with 0; lower-case d with 0; no independent additional subscript d',confidence='medium'),
    dict(place='(208), map connector',reading=UP,alternatives='literal upward terminal; reduced rightward arrowhead',confidence='medium'),
    dict(place='(209), first left parenthesis',reading=r'\bigl(',alternatives='opening-parenthesis-shaped surviving curve with retraced upper section; its function and earlier layer are not secure',confidence='medium'),
    dict(place='(209), fundamental-groupoid signs',reading=r'\unsure{\Pi_1|\pi_1},\ \unsure{\Pi|\pi}',alternatives='capital Π leading from the roof and long legs; lower-case π not graphically separable on this page; the bottom-right sign has no 1',confidence='medium'),
    dict(place='(209), lower-left D',reading=r'\unsure{D_{d_0,\ldots,d_r}|D^*_{d_0,\ldots,d_r}}',alternatives='bare retraced D; star embedded in or obscured by the retracing',confidence='medium'),
    dict(place='(209), bottom connector',reading=r'\arrow[r,no head,to path={(\tikztostart.east)--([xshift=-2pt]\tikztotarget.west)--++(0,.055)\tikztonodes}]',alternatives='literal upward terminal turn; reduced rightward head',confidence='medium'),
    dict(place='(209), lower-right definition label',reading=r'\unsure{\mathrm{déf}|\mathrm{def}}',alternatives='déf with compressed accent; unaccented def',confidence='medium'),
    dict(place='(209), written number',reading=r'\unsure{209}',alternatives='209 leading; initial digit is open because its lower return merges with the parenthesis, no complete alternative number secure',confidence='medium')
]

notes=[
    'Scan129 only was read: the whole page and each native half were viewed once successfully, followed by twelve distinct first-pass crops, each viewed. An initial combined text/image call was truncated and provided no usable image view. No OCR, external research, other-page image/report consultation, or TeX compilation was performed. The packet difference file initially exposed trailing 130–131 diff rows because of a preparation parsing defect; root was immediately notified, those rows were not used, and no other-page file was accessed.',
    'The definitions on scan129 describe a first-summit inverse image for the starred D family, pullbacks of P and G, and their restrictions. The visible inequality chain omits a comparison sign after d_1. This omission is retained without inferring a corrected chain.',
    'The source distinguishes the generic-looking G_d annotation over P_{d_0}, the small D_0/d_0 base in (208), and the several plain or possibly starred D terms in (209). These are separate readings of the ink; no missing index or star is supplied from the expected definition. In particular, a bare D in (209) is not by itself treated as a mathematical objection.',
    'The long annotation bracket over the first-summit map is represented by an overbrace. Its downward left curve is attached to the bracket and is not transcribed as a free opening parenthesis. The large brace of (206) ends before the separate i.e. line. The early row of (207) sits immediately above the upper start of its drawn brace; its conventional aligned grouping is retained.',
    'All thirteen actual connectors were inspected at both ends: three in the upper definitions, four in the small chain, one each in (207) and (208), and four in (209). The source has no extra shaft between the chain numeral 2 and its continuation marks. Literal one-sided terminal turns are drawn with TikZ; their possible arrow intention is recorded as doubt rather than converted to a full head.',
    'The square is stated to be 2-cartesian in the manuscript. This first-reader report checks its copied objects, indices, labels and geometry, but does not claim to prove that particular statement from the isolated page. A covering hypothesis or any other earlier construction has not been consulted by this reader.',
    'A limited mathematical test concerns only the unrestricted assertion that every pullback square of analytic torus torsors becomes 2-cartesian on fundamental groupoids. Take E=C² minus {0}, B=P¹(C), and the principal C* quotient E→B; pull it back along a point of B. The fiber is C*. Using the standard background homotopy types S³, S² and S¹, three corner groupoids are equivalent to the terminal groupoid while the fiber groupoid has automorphism group Z. The comparison is therefore not an equivalence. This limits an unrestricted generalization; it does not refute the manuscript’s particular construction, whose preceding hypotheses were not available to this reader. No sphere simple-connectivity theorem was independently reproved here.',
    'The low roof-and-legs signs in (209) do not securely distinguish Π from π. Named Π variables retain their capital convention; the fundamental-groupoid operators carry local case uncertainty. The lower-right operator lacks a written 1 regardless of that case question.',
    'The retraced G in Groupes, the initial of torseur, the low c’est strokes, the upper-left opening curve of (209), and the lower-left D were each examined for an older readable layer. No separate cancelled word or index can be recovered confidently. Accordingly no new definite deletion is invented. All doubtful physical layers are retained in the local readings or doubts.',
    'The pencil 128 is physically present and paler than the principal ink. The formula number 209 is locally doubtful because its first digit has an unusually merged lower return; numerical sequence was not used to make it certain. H’s editorial comments about209,2-cart. and the D stars were not copied as prose, but the underlying real ink was recorded.',
    'The line_count is20 principal prose/display or diagram-label baselines, excluding the raised first-summit and torseur annotations, tiny coproduct bounds, individual chain levels, and the pencil footer. The element inventory separately covers those components.'
]

check_events=[
    dict(statement_id='R129-formulas',type='used and rechecked in this run',outcome='Rechecked the literal indices, stars, inequality positions and named/operator Π forms of206–209 against the native halves and complete formula crops; no mathematical normalization was used.'),
    dict(statement_id='R129-connectors',type='used and rechecked in this run',outcome='Inspected both endpoints of the thirteen actual connectors, distinguished solid points from heads, removed the uninked2-to-continuation shaft, and preserved terminal turns literally.'),
    dict(statement_id='R129-209',type='carried as background without fault found',outcome='The manuscript’s particular 2-cartesian claim is transcribed. Its surrounding geometric hypotheses are outside this one-page reader’s evidence; it is not marked proved or refuted.'),
    dict(statement_id='MC129-generalization-background',type='carried as background without fault found',outcome='Used the standard facts P¹(C)≈S², C² minus {0} deformation retracts to S³, C* deformation retracts to S¹, π₁(S²)=π₁(S³)=0, and π₁(S¹)=Z. These background facts were not independently reproved.'),
    dict(statement_id='MC129-generalization-only',type='refuted, with refined statement id',outcome='Refuted only the unrestricted general pullback/torsor assertion: the C* quotient C² minus {0}→P¹(C) and its fiber over a point yield three terminal fundamental groupoids and one BZ. A 2-pullback of the three terminal groupoids is terminal. Refined statement ID MC129-R is the covering-base statement supplied by root, whose separate path-lifting proof this reader has not consulted. No refutation of the manuscript under its actual surrounding hypotheses is asserted.')
]

hand_log=[
    dict(habit='A short terminal hook can stand where a full arrow would be expected, but both wings are not independently visible.',places='129: first map in206; map in207; map in208; bottom edge of209; chain edge ending at2',scope='These five local ends only, compared with the complete heads on the same sheet.',misreadings='C/H full arrows, or C dash/arrow alternatives; literal terminal turns retained.'),
    dict(habit='A solid point at the end of a vertical shaft can be mistaken for a filled arrowhead.',places='129: chain point1 below0',scope='One local endpoint; its round contour differs from the angular final arrow at r.',misreadings='C omits the point at1 and supplies a down arrow; H editorial chain description also uses an arrow.'),
    dict(habit='Small cursive D/d and adjacent low0 can be mistaken for a capital D followed by d_0.',places='129: sur in208',scope='One small glyph; larger D and d forms elsewhere on 129 were compared, but case remains open.',misreadings='H supplies a second d; C originally offers D_0/D_{d_0}.'),
    dict(habit='Capital G can have a broad upper open curve and dense lower retracing.',places='129: Groupes after207; compared with G labels in207–208',scope='The prose capital is heavily retraced; no independent older letter is claimed.',misreadings='H gives lower-case groupes.'),
    dict(habit='The numeral 2 can have a lower return merging into an adjacent opening parenthesis.',places='129: number 209, compared locally with206–208',scope='The contour of209 remains less secure than the other local2 forms.',misreadings='C/H present209 without a local doubt.'),
    dict(habit='Π/π operators share a roof-and-two-legs outline.',places='129: three indexed operators and the unindexed lower-right operator in209',scope='Case remains open at those four operators; this is not generalized to all Greek letters.',misreadings='C/H choose Π without indicating local case uncertainty.'),
    dict(habit='Continuation dashes and commas vary within nearby multi-indices.',places='129: named Π indices in209 versus P/D tuple indices',scope='Upper-left d_0-d_r and lower-left d_0,-d_r are copied separately.',misreadings='H regularizes both to dots; C gives two commas in the lower-left named index.')
]

notation=[
    dict(notation=r'\unsure{0|o}:\mathcal D_*'+UP+r'D_*',meaning_or_form='Small oval map label, associated locally with the first-summit description; numeral/letter identity remains open.',places='129,(206)'),
    dict(notation=r'G_d\text{-torseur}',meaning_or_form='Literal d, without a lower 0, and singular torseur in the bracket above P_{d_0}.',places='129,(207)'),
    dict(notation=r'\unsure{D_0|d_0}',meaning_or_form='One cursive D/d glyph followed by low0; no additional subscript d is independently visible.',places='129,(208)'),
    dict(notation=r'\widetilde\Pi_{d_0-d_r};\quad\Pi_{d_0,-d_r}',meaning_or_form='Different literal punctuation in the upper- and lower-left named indices; do not insert the missing comma or replace the dash by a dotted range automatically.',places='129,(209)'),
    dict(notation=r'\unsure{\Pi_1|\pi_1};\quad\unsure{\Pi|\pi}D_{d_0}',meaning_or_form='Roof-and-legs fundamental-groupoid operator; case unresolved, with no written 1 at the lower-right occurrence.',places='129,(209)'),
    dict(notation=r'\unsure{D_{d_0,\ldots,d_r}|D^*_{d_0,\ldots,d_r}}',meaning_or_form='Retraced lower-left D, bare leading and star obscured/embedded as an alternative; the lower-right D is clearly bare.',places='129,(209)')
]

abbreviations=[
    dict(form='i.e.',expansion='id est'),
    dict(form='déf / def',expansion='définition; accent uncertain at the lower-right label of209'),
    dict(form='cart.',expansion='cartésien')
]

second_boxes=[
    dict(box='B01',kind='doubtful formula',coords=[230,140,1655,650],reading=F206),
    dict(box='B02',kind='insertion',coords=[680,555,1560,650],reading=r'\(\text{i.e. défini par les }'+SOMMET+r'\)'),
    dict(box='B03',kind='doubtful formula',coords=[685,650,1325,858],reading=CHAIN),
    dict(box='B04',kind='doubtful formula',coords=[275,890,1680,1375],reading='Nous allons définir\n'+F207),
    dict(box='B05',kind='different words',coords=boxes['cest'],reading=CEST),
    dict(box='B06',kind='different words',coords=boxes['groupes'],reading='les '+ANALYT),
    dict(box='B07',kind='doubtful formula',coords=[235,1598,1680,1945],reading=F208),
    dict(box='B08',kind='doubtful formula',coords=[210,1965,1680,2320],reading=PROSE209+'\n'+D209),
    dict(box='B09',kind='margin note',coords=boxes['footer'],reading=r'\margin{128}')
]

checks=[
    dict(span=r'''\inserted{morphismes OPENQUOTEpremier sommet''}'''.replace('OPENQUOTE',QQ),finding='Both words and paired opening/closing quotes are live above the i.e. map. The connected bracket spans D_r→D_*; the left downward curve is part of that bracket, not a free parenthesis. The insertion is attached to that map in the proposal.'),
    dict(span=r'\inserted{\unsure{là|sont}}',finding='The small unit is genuinely raised above the c’est-like baseline. Its long curved leader comes down near the residual t-like stroke. The position after c’est is provisional; no full à-dire phrase is recoverable.'),
    dict(span=r"\unsure{c'est}",finding='The central low strokes are thick/retraced and cross the insertion leader. The image does not establish a separate deliberate cancellation spanning all of c’est, so the live doubtful reading is retained rather than inventing a definite deletion.'),
    dict(span=r'G_d\text{-torseur}',finding='The initial t area of torseur is retraced, but no stroke cancels the whole word. The final r and bracket remain live; no separate older word is recoverable.'),
    dict(span='Groupes',finding='The capital has a retraced inner/descending loop, without a separable earlier letter or an independently identifiable cancellation stroke. The full word remains live.'),
    dict(span=r'\bigl(\widetilde\Pi_{d_0- d_r}',finding='The opening curve before the upper-left term has a dense upper retracing but a clear lower arc. It is kept as an opening parenthesis with no invented matching close; no earlier readable label is reconstructed.'),
    dict(span=r'\unsure{D_{d_0,\ldots,d_r}}',finding='The D is overtraced internally. The low d_0 and following tuple strokes remain live and are not treated as cancelled merely because they sit near the retracing. A possibly embedded star is kept as a local alternative, not supplied as certain or discarded without notice.'),
    dict(span='C has no deleted macros on 129',finding='The entire sheet and all heavy/overlapping locations were nevertheless checked for cancellations. No independently legible cancelled word or index was securely identified; doubtful layers are documented above rather than normalized.')
]

report=dict(scan=129,reader='reader_c',line_count=20,rows=rows,decisions=decisions,
    inventory=inventory,doubts=doubts,notes=notes,check_events=check_events,
    hand_log=hand_log,notation=notation,abbreviations=abbreviations,
    second_boxes=second_boxes,
    unresolved=[
        'M1283: 0/o map label.',
        'M1285–M1286: residual c’est, raised là/sont, possible accent and exact attachment.',
        'Terminal-turn intention remains open at five connectors, although their visible geometry is reproduced.',
        'D_0/d_0 case in208 remains open after removal of the unsupported additional d subscript.',
        'The ending of analytiques is compressed/clipped at the right edge.',
        'M1289: bare/possibly starred retraced lower-left D in209.',
        'Π/π case at the four fundamental-groupoid operators, lower-right déf/def accent, and the function/earlier layer of the opening parenthesis in209.',
        'The initial digit of209 is not secure independently of its sequence; a local doubt remains.'
    ],deletion_insertion_checks=checks)

(OUT/'147_scan129_proposed.tex').write_text(tex,encoding='utf-8')
(OUT/'147_scan129_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(scan=129,rows=len(rows),against_C=sum(x['against_C'] for x in rows),
    against_H=sum(x['against_H'] for x in rows),marks=len(decisions),
    resolved=sum(x['decision']!='undecided' for x in decisions),crops=len(boxes),
    inventory=len(inventory),doubts=len(doubts),second_boxes=len(second_boxes),
    checks=len(checks)),ensure_ascii=False))
