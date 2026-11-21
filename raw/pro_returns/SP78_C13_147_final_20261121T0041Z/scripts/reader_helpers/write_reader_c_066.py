from pathlib import Path
import json

ROOT=Path('/workspace/scratch/ea90d891106a')
WORK=ROOT/'SP78_C13_147_work'
OUT=WORK/'reader_returns/147_scan066'
OUT.mkdir(parents=True,exist_ok=True)
boxes={1:[320,27,1200,175],2:[309,207,1580,476],3:[339,486,1645,708],
4:[350,645,1666,818],5:[353,790,1614,902],6:[30,683,360,857],
7:[358,887,1640,1026],8:[346,1125,1657,1390],9:[337,1380,1660,1603],
10:[327,1588,1640,1726],11:[314,1705,1672,1932],12:[384,1932,1663,2035],
13:[311,2020,1666,2200],14:[315,2189,746,2313],15:[326,2255,1498,2351],
16:[1331,2186,1660,2345],17:[25,2291,87,2348],18:[750,2183,1342,2267]}

heading=r"$3^\circ)$ \uline{Cas \unsure{de|des}} $\widehat M^!_{0,5}$, ou $\widehat M_{0,I}$"
last_label=r"\unsure{I^{\mathrm{IV}}|I'''|I''}(2)"
diagram=r"""\diagram{\begin{tikzpicture}[x=1cm,y=1cm,line width=.55pt]
\node at (-1.1,.4) {$(81)$};
\draw (0,.95)--(9.6,.95);
\draw (2,1.55)--(2,-.65);
\draw (4.8,1.55)--(4.8,-.65);
\node at (.9,1.3) {$\text{Codim }0$};
\node at (3.35,1.3) {$\text{codim }1$};
\node at (7.25,1.3) {$\text{codim }2$};
\fill (.85,0) circle (1.4pt);
\node[above] at (.85,.22) {$I(5)$};
\draw[->] (1.65,-.05)--(2.35,-.05);
\node[above] at (1.8,-.05) {$(10)$};
\draw (2.95,0)--(4.05,.04);
\fill (2.95,0) circle (1.7pt);
\fill (4.05,.04) circle (1.7pt);
\node[above] at (2.95,.26) {$I'(2)$};
\node[above] at (4.05,.26) {$I''(3)$};
\draw[->] (4.45,.05)--(5.15,.05);
\node[above] at (4.6,.05) {$(3)$};
\draw (5.9,.03)--(7.08,.07);
\draw (7.19,.07)--(8.32,.12);
\fill (5.9,.03) circle (1.4pt);
\fill (7.08,.07) circle (1.7pt);
\fill (8.32,.12) circle (1.7pt);
\node[above] at (5.9,.28) {$I'(2)$};
\node[above] at (7.08,.28) {$I'''(1)$};
\node[above] at (8.32,.28) {$\unsure{I^{\mathrm{IV}}|I'''|I''}(2)$};
\end{tikzpicture}}"""
tuple_insert=r"\inserted{$(\unsure{\{a',a''\}},I'')$}"
strike1=r"\deleted{\unsure{$\simeq\mathbb P$}}"
strike2=r"\deleted{\unsure{$\mathbb P^1_{0,3}\mathfrak S_3$}}"
precision=r"\inserted{(plus précisément, un $\widehat M_{0,I''(3)\amalg(*)}\simeq(\mathbb P^1_{I''})_{\mathbb Z}$)}"
start=r"Dans \unsure{de|le} $\widehat M^!_{0,5}$ il y a dix ``diviseurs à l'infini'' "+tuple_insert+r", dont chacun est un $\widehat M^!_{0,4}$ "+strike1+","
having=r"(ayant comme on avait vu, et \unsure{avait|aurait}) trois points à l'infini --- les"
count=r"pts à l'infini sont en nb total $\frac{30}{2}=15$,"
partition_intro=r"correspondant aux partitions de $I(5)$ de"
partition_middle=r"type $(2,2,1)$, alors que les diviseurs à l'infini correspondent aux parties \inserted{$I'$} de"
qualifier=r"$I$ de cardinal $2$. Deux tels diviseurs, correspondant à des parties $I',I''\in\mathfrak P_2(I)$,"
criterion=r"se rencontrent sss \deleted{elles} on a $I'\cap I''=\phi$,"
second_sss=r"\unsure{sss|\deleted{sss}}"
partition_end=r"i.e. "+second_sss+r" $I',I''$ et $I\smallsetminus(I'\cup I'')$ forment justement une partition de $I$ de type $(2,2,1)$."
margin=r"\margin{$\mathbb P^1_{I''}\overset{\mathrm{def}}{=}\unsure{\mathbb P^1_{\mathbb Z}\wedge_{\mathfrak S_3}\widetilde{I''}}$}"
lower1="D'après l'étude combinatoire de l'icosaèdre,"
lower2=r"choisissant une orientation de $I$ --- ce qui détermine un icosaèdre orienté, ou encore un"
lower3=r"icos. \unsure{gauche|graphe}) les $10$ diviseurs à l'infini \deleted{\unsure{en ordre}}"
lower4=r"de $\widehat M_{0,I}$, i.e. les \inserted{$10$} éléments de $\mathfrak P_2(I)$,"
unfinished=r"\inserted{ou (par} \deleted{\unsure{correspon-}}"

proposed='\n'.join([r'\scanpage{66}',r'\mspage{32}',heading,diagram,
start+' '+strike2+' '+precision+' '+having+' '+count+' '+partition_intro+' '+partition_middle+' '+qualifier+' '+criterion+' '+partition_end,
margin,'',lower1+' '+lower2+' '+lower3+' '+lower4+' '+unfinished,r'\margin{65}',''])

changes=[]
def change(place,C,H,final,evidence,crop,confidence='high',against_C=False,against_H=True,
           kind='other',marked_in_H=False,error_sheet_kind='other',consequential=False):
    changes.append({'id':f'066-{len(changes)+1:02d}','place':place,'C':C,'H':H,'final':final,
        'evidence':evidence,'crop':f'147_scan066_place{crop:02d}.png','box':boxes[crop],
        'confidence':confidence,'against_C':against_C,'against_H':against_H,'kind':kind,
        'marked_in_H':marked_in_H,'error_sheet_kind':error_sheet_kind,'consequential':consequential})

change('Heading, de/des','de','des',r'\unsure{de|des}',
       'A looped d is followed by a long low exit ending in a hook. The hook does not securely separate final e from an additional s; de is preferred without excluding des.',1,
       confidence='medium',kind='misread word',error_sheet_kind='words')
change('Heading, ending after M_{0,I}',r'$\widehat M_{0,I}$',r'$\widehat M_{0,I}$.',r'$\widehat M_{0,I}$',
       'The last serifed I is followed by blank paper, without a detached dark period.',1,
       kind='text not on the page',error_sheet_kind='text not on page')
change('Diagram 81, first column header','codim 0','codim 0','Codim 0',
       'The first C rises to the ascender height of the adjacent d. The initial c in each of the later two headers is visibly lower, so only the first header is capitalized.',2,
       against_C=True,kind='misread word',error_sheet_kind='words')
change('Diagram 81, arrow positions and right-hand segment gap',
       r'\begin{array}{c|c|c} point\xrightarrow{(10)} & segment\xrightarrow{(3)} & continuous three-point chain\end{array}',
       r'\begin{array}{c|c|c} point\xrightarrow{(10)} & segment\xrightarrow{(3)} & continuous three-point chain\end{array}',
       diagram,
       'Both arrow shafts cross their respective vertical rules, with arrowheads to the right. In the last column a small white gap remains between the filled middle point and the start of the right segment; the TikZ preserves that gap without inferring a different graph topology. All six vertices are filled. H’s separate drawing file was not supplied; the comparison concerns its provided array.',2,
       against_C=True,kind='drawing or diagram',error_sheet_kind='drawings and diagrams',consequential=True)
change('Diagram 81, last codimension-2 label (M1044)',r"\unsure{I^{\mathrm{IV}}|I'''}(2)",r"I''(2)",last_label,
       'The superscript is a pair of dense overworked clusters. A straight first stroke and branched second cluster favor IV, but a cluster of primes is not excluded. The adjacent middle label has three narrow raised strokes. No mathematical ordering is used to regularize the last mark.',2,
       confidence='low',kind='misread symbol or index',marked_in_H=True,error_sheet_kind='symbols and indices',consequential=True)
change('Opening prose, small word between Dans and M','(nothing)','(nothing)',r'\unsure{de|le}',
       'At the main baseline after Dans there is a small initial loop with a taller returning stem and a long low exit. It resembles de, with le a possible alternative. No independent cancellation crosses it. It sits above the end of the sloping tuple insertion, so its attachment is recorded as a remaining doubt.',3,
       confidence='medium',against_C=True,kind='omission',error_sheet_kind='omissions')
change('Opening prose, quotation marks and their scope',"``diviseurs à l'infini''",r"\og diviseurs\fg{} à l'infini","``diviseurs à l'infini''",
       'Two short raised marks precede diviseurs. The matching pair follows l’infini on the next line, not diviseurs. They are quotation strokes rather than angular guillemets.',3,
       kind='insertion or placement',error_sheet_kind='insertions put in wrong place')
change('First inserted tuple (M1045)',r"\inserted{$(\unsure{\{a',a''\}|I'(2)},I'')$}",
       r"\uncertain{($\simeq(\{0,1,\infty\},I'')$)}",tuple_insert,
       'The sloping addition has an opening parenthesis, curly braces around two small a-like entries separated by a comma, then I with two primes. No initial equivalence sign or three-member 0,1,infinity set is exposed. The first family of C readings is supported; the tiny prime count within the pair remains tentative.',3,
       confidence='medium',kind='misread symbol or index',marked_in_H=True,error_sheet_kind='symbols and indices',consequential=True)
change('First canceled trial after M!_{0,4}',r'\deleted{\unsure{$\simeq\mathbf P$}}',r'\struck{\ill{}}',strike1,
       'Several diagonal strokes cross a short relation and a P-like outline. The P retains two parallel uprights. The relation under the crossing is not fully exposed, so the whole trial remains doubtful while the double-stroked alphabet is preserved.',3,
       confidence='low',against_C=True,kind='deletion state',marked_in_H=True,error_sheet_kind='struck text')
change('Second canceled trial below the inserted precision',r'\deleted{\unsure{$\mathbf P^1_{0,3}\mathfrak S_3$}}',
       r'\struck{$\widehat M_{0,3}$,\ill{}}',strike2,
       'Dense zigzags cross the old line. Two P uprights, the small 0,3 group, and a large looped group-sign with lower 3 can be traced, but other strokes remain obscured. C’s entire trial stays tentative; neither the leading hatching nor its original formula is claimed fully recovered.',4,
       confidence='low',against_C=True,kind='deletion state',marked_in_H=True,error_sheet_kind='struck text',consequential=True)
change('Inserted precision, projective-space and base alphabets',r'(\mathbf P^1_{I\prime\prime})_{\mathbf Z}',
       r'(\mathbb P^1_{I\prime\prime})_{\mathbb Z}',r"(\mathbb P^1_{I''})_{\mathbb Z}",
       'The P has two separated vertical strokes and the Z has separated diagonals enclosing white space. They are double-stroked letters rather than solid bold forms.',4,
       against_C=True,against_H=False,kind='misread symbol or index',error_sheet_kind='symbols and indices')
change('Inserted precision, state and parenthetical extent',precision,
       r"\uncertain{plus précisément}, un $\widehat M_{0,I''(3)\amalg(*)}\simeq(\mathbb P^1_{I''})_{\mathbb Z}$",precision,
       'The plus précisément line is interlinear above the canceled calculation, beginning with a separate opening parenthesis. Its long bounding/connecting stroke passes beneath the inserted formula and above the old ayant line. The correction is kept as an inserted parenthetical, without turning that connector into a textual underline.',4,
       kind='insertion or placement',marked_in_H=True,error_sheet_kind='insertions put in wrong place')
change('Parenthetical prose after the canceled trial',r'(ayant comme on avait vu,',r'(\ill{} \ill{} et',r'(ayant comme on avait vu,',
       'The first word has the long descending y of ayant. The following groups have the open c and low humps of comme, a separate on, the final tall t of avait, and vu followed by a comma. These are live words beneath the insertion’s connecting stroke.',4,
       kind=r'readable ink left as \ill{}',marked_in_H=True,error_sheet_kind='readable ink left as illegible')
change('Parenthetical ending (M1046)',r'et \unsure{avait|aurait})',r'\uncertain{ayant})',r'et \unsure{avait|aurait})',
       'Et is separate at the line start. The following word ends in a dotted i and a tall t, without a y-descender. Its compressed middle strokes leave avait versus aurait unresolved; they do not support H’s ayant.',5,
       confidence='low',kind='misread word',marked_in_H=True,error_sheet_kind='words')
change('Count sentence, pts à l’infini',r"pts à l'infini",r'\ill{}',r"pts à l'infini",
       'The abbreviation has a long p-descender and crossed t followed by s. L’infini has the tall f and its descending return. The intervening à is very reduced, like the parallel phrase trois points à l’infini above.',7,
       kind=r'readable ink left as \ill{}',marked_in_H=True,error_sheet_kind='readable ink left as illegible')
change('Count sentence, nb total','nb total','tout','nb total',
       'After en there is a separate short n and a tall b. The next word has two tall crossed t strokes and a final l, forming total. The written abbreviation nb is retained.',7,
       kind='misread word',error_sheet_kind='words')
change('Divisor sentence, à l’infini after diviseurs',r"diviseurs à l'infini",r'diviseurs \ill{}',r"diviseurs à l'infini",
       'The end of the upper line has a reduced à after the retraced but live diviseurs. The next line begins l’infini with the same tall f form as the earlier occurrences.',8,
       kind=r'readable ink left as \ill{}',marked_in_H=True,error_sheet_kind='readable ink left as illegible')
change('Insertion after parties',r"parties \inserted{$I'$} de",r"parties $I'$ de",r"parties \inserted{$I'$} de",
       'The serifed I and one raised prime are above the prose baseline. A large descending insertion tick points to the gap between parties and de.',8,
       kind='insertion or placement',error_sheet_kind='insertions put in wrong place')
change('Qualifier after Deux tels diviseurs, both boundaries',
       r", correspondant à des parties $I',I''\in\mathfrak P_2(I)$,",
       r"(correspondant à des parties $I',I''\in\mathfrak P_2(I)$)",
       r", correspondant à des parties $I',I''\in\mathfrak P_2(I)$,",
       'A short descending comma follows diviseurs. The qualifier ends with the parenthesis belonging to P_2(I), followed by a separate descending comma. There is no additional enclosing pair of parentheses around the prose qualifier.',9,
       kind='other',error_sheet_kind='other')
change('Intersection condition, words around the canceled elles',r'sss \deleted{elles} on a',r'\struck{elles} ssi',r'sss \deleted{elles} on a',
       'Three connected s-shaped hooks precede elles. Elles has a distinct horizontal cancellation extending beyond its letters. After it, a separate on and small a precede the formula. There is no dotted final i in the first abbreviation.',10,
       kind='abbreviation expanded or spelling modernised',error_sheet_kind='abbreviations expanded spelling modernised',consequential=True)
change('Intersection condition, empty-set glyph',r'\varnothing',r'\emptyset',r'\phi',
       'The sign has a small closed loop high on a long slanted stem, with a substantially longer extension below the loop than above it. Its shape favors the author’s phi-like empty-set mark over a centered circle with a balanced slash.',10,
       confidence='medium',against_C=True,kind='misread symbol or index',error_sheet_kind='symbols and indices')
change('Abbreviation after i.e., spelling and cancellation state',r'\deleted{sss}','ssi',second_sss,
       'Three small connected hooks are visible. The rising diagonal can be followed as a cursive joining stroke like the live sss above; it does not securely form a separate strike extending beyond the letters. Live sss is preferred, while C’s deletion state remains an explicit alternative. No separate i dot is visible.',11,
       confidence='low',against_C=True,kind='deletion state',error_sheet_kind='struck text')
change('Partition sentence, state of the single forment','forment',r'\struck{forment}','forment',
       'There is only one word with the long f-descender. Its leftward horizontal stroke is attached to that f, and the following letters form one continuous word; no independent cancellation spans a second forment.',11,
       kind='deletion state',error_sheet_kind='struck text')
change('Partition sentence, following word','justement','forment','justement',
       'The word after forment begins with a deep j-descender and has the later tall crossed t. It is not a second occurrence beginning with f.',11,
       kind='misread word',error_sheet_kind='words')
change('Margin definition, P and Z alphabets',r"\mathbf P^1_{I''};\mathbf P^1_{\mathbf Z}",
       r"\mathbb P^1_{I''};\mathbb P^1_{\mathbb Z}",r"\mathbb P^1_{I''};\mathbb P^1_{\mathbb Z}",
       'Both P glyphs have two separated uprights. The lower Z has separated parallel diagonals and a white interior. These remain distinguishable after rotating the sloping note upright.',6,
       against_C=True,against_H=False,kind='misread symbol or index',error_sheet_kind='symbols and indices')
change('Margin definition, label over equals','déf','def','def',
       'The d has a tall loop and the f a long stem. Between them the e has no detached accent stroke above it; the spelling def is retained locally.',6,
       against_C=True,against_H=False,kind='misread word',error_sheet_kind='words')
change('Margin definition, contracted-product layout and final factor (M1047)',
       r"\unsure{\mathbf P^1_{\mathbf Z}\wedge_{\mathfrak S_3}\widetilde{I''}}",
       r'\mathbb P^1_{\mathbb Z}\wedge\mathfrak S_3\ill{}',
       r"\unsure{\mathbb P^1_{\mathbb Z}\wedge_{\mathfrak S_3}\widetilde{I''}}",
       'The S_3 lies below and to the right of the wedge. A separate raised factor follows, with a broad wavy cap over an I-like stem and additional trailing strokes. The cap is not a clean angular hat. The exact prime/trailing-stroke reading is not fully exposed, so the entire RHS remains doubtful rather than being resolved from the expected construction.',6,
       confidence='low',kind=r'readable ink left as \ill{}',marked_in_H=True,error_sheet_kind='readable ink left as illegible',consequential=True)
change('Lower paragraph, phrase after orienté','ou encore',r'\ill{}','ou encore',
       'After the comma there is a small closed o and long low u, followed by a separate group with the low e-n-c-o-r-e sequence. The next un is separately visible.',13,
       kind=r'readable ink left as \ill{}',marked_in_H=True,error_sheet_kind='readable ink left as illegible')
change('Lower paragraph, word after icos. (M1050)',r'\unsure{graphe|gauche}',r'\uncertain{grand}',r'\unsure{gauche|graphe}',
       'The initial g has a deep loop. Near the right is a c/h-like rise and low ending; there is no secure independent p-descender in the middle, so gauche is preferred. The intervening compressed strokes do not exclude graphe. There is no clear final tall d-loop supporting grand.',14,
       confidence='medium',against_C=True,kind='misread word',marked_in_H=True,error_sheet_kind='words')
change('Lower paragraph, first 10 before diviseurs',r'les $10$ diviseurs',r'les \add{10} diviseurs',r'les $10$ diviseurs',
       'The 1 and rounded 0 lie on the sloping baseline between les and diviseurs. There is no insertion tick or separate elevated placement here, unlike the second 10 on the final line.',18,
       kind='insertion or placement',error_sheet_kind='insertions put in wrong place')
change('Lower paragraph, canceled en ordre',r'\deleted{\unsure{en ordre}}','(nothing)',r'\deleted{\unsure{en ordre}}',
       'Two small words below l’infini are crossed by an independent heavy horizontal stroke. The first has an e-like loop and n exit; the second has partly exposed rounded and tall strokes. The complete en ordre reading remains tentative under the cancellation.',16,
       confidence='low',kind='omission',error_sheet_kind='struck text')
change('Final main line, inserted 10 before éléments',r'les \inserted{$10$} éléments',r'les éléments',r'les \inserted{$10$} éléments',
       'A small 10 sits above the gap after les, with a V-shaped insertion tick pointing to the start of éléments. It is a second written 10, distinct from the earlier baseline number.',15,
       kind='omission',error_sheet_kind='omissions',consequential=True)
change('Bottom-right unfinished insertion',r'\inserted{ou (par}',r'\add{ou \uncertain{(les}}',r'\inserted{ou (par}',
       'Ou is followed by an opening parenthesis and a large descending p with an upper loop, then the low a/r continuation. The descender does not support les. The parenthesis remains unclosed at this page end.',16,
       kind='misread word',marked_in_H=True,error_sheet_kind='words')
change('Bottom-right canceled continuation',r'\deleted{\unsure{correspon-}}',r'\struck{\uncertain{sommets}}',r'\deleted{\unsure{correspon-}}',
       'A separate heavy stroke crosses the lower word. Its beginning has an open c-like curve, followed by an o and several narrow upstrokes; the exposed right end has a small oval and a separate final dash. The full tentative correspon- reading is retained because the strike hides intervening letters; sommets is not supported by the exposed start.',16,
       confidence='low',kind='misread word',marked_in_H=True,error_sheet_kind='struck text')
change('Bottom-left pencil foliation',r'\margin{65}','(nothing)',r'\margin{65}',
       'The lighter separate hand writes a looped 6 followed by a 5 with a horizontal top and curved lower body. It remains margin foliation, separate from the ink page number 32 at the top.',17,
       kind='omission',error_sheet_kind='omissions')

decisions=[
 {'id':'M1044','cote':147,'scan':66,'decision':'undecided','reading':last_label,
  'ink':'Overworked raised clusters favor IV, but prime groups III and II remain possible. Do not infer the index from the desired graph labels.',
  'crop':'147_scan066_place02.png (309,207,1580,476)','confidence':'low'},
 {'id':'M1045','cote':147,'scan':66,'decision':'undecided','reading':r"\unsure{\{a',a''\}}",
  'ink':'Curly braces and two small a-like entries are supported, excluding the single I′(2) family and H’s conventional three-element set. The small prime strokes remain incompletely separated.',
  'crop':'147_scan066_place03.png (339,486,1645,708)','confidence':'medium'},
 {'id':'M1046','cote':147,'scan':66,'decision':'undecided','reading':r'\unsure{avait|aurait}',
  'ink':'Dotted i and tall t at the end; no y-descender. The compressed middle does not separate avait from aurait.',
  'crop':'147_scan066_place05.png (353,790,1614,902)','confidence':'low'},
 {'id':'M1047','cote':147,'scan':66,'decision':'undecided',
  'reading':r"\unsure{\mathbb P^1_{\mathbb Z}\wedge_{\mathfrak S_3}\widetilde{I''}}",
  'ink':'P/Z are double-stroked and S_3 lies low beside the wedge. The wavy cap and I-like final stem survive, but the long trailing strokes do not securely resolve the whole final factor.',
  'crop':'147_scan066_place06.png (30,683,360,857), rotated -20 degrees','confidence':'low'},
 {'id':'M1048','cote':147,'scan':66,'decision':'first','reading':'icosaèdre',
  'ink':'The separate i, open c, rounded o, s, small a, accented e, tall looped d, and r/e ending can be followed in order.',
  'crop':'147_scan066_place12.png (384,1932,1663,2035)','confidence':'high'},
 {'id':'M1049','cote':147,'scan':66,'decision':'first','reading':'icosaèdre',
  'ink':'The repeated i-c-o-s-a-è-d-r-e sequence is present before orienté, including the raised accent and tall d-loop.',
  'crop':'147_scan066_place13.png (311,2020,1666,2200)','confidence':'high'},
 {'id':'M1050','cote':147,'scan':66,'decision':'undecided','reading':r'\unsure{gauche|graphe}',
  'ink':'The deep initial g and later c/h-like rise favor gauche; an independent p-descender is not secure. The compressed middle prevents a final choice against graphe.',
  'crop':'147_scan066_place14.png (315,2189,746,2313)','confidence':'medium'},
]

inventory=[]
def inv(kind,position,first,hand='his hand'):
    inventory.append({'scan':66,'sheet_kind':'text','hand':hand,'element':f'{len(inventory)+1:02d}',
                      'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
inv('text','top center','ink page number 32')
inv('text','top heading','3°) underlined Cas de|des, hat M!_{0,5}, ou hat M_{0,I}')
inv('diagram','upper ruled table, (81)','Codim0/codim1/codim2, six filled vertices, two labeled arrows crossing dividers, graph labels with doubtful last raised mark')
inv('text','first two prose baselines','Dans de|le M!_{0,5}, dix ``diviseurs à l’infini’’, dont chacun est un M!_{0,4}')
inv('insertion','sloping small addition over l’infini','({a′,a″},I″), prime count still doubtful')
inv('deletion','after first M!_{0,4}','tentative ≃ double-struck P')
inv('deletion','next old baseline, below precision insertion','tentative double-struck P^1_{0,3} S_3')
inv('insertion','interlinear correction above old canceled calculation','(plus précisément, un hat M_{0,I″(3)amalg(*)} ≃ (double-struck P^1_{I″})_Z)')
inv('margin note','sloping left margin beside canceled trial','P^1_{I″} def = tentative P^1_Z wedge_subS3 tilde I″')
inv('text','parenthetical prose and next baseline','(ayant comme on avait vu, et avait|aurait) trois points à l’infini — les')
inv('text','count baseline','pts à l’infini sont en nb total 30/2=15,')
inv('text','following three baselines','correspondant aux partitions de I(5) de type (2,2,1), alors que les diviseurs à l’infini correspondent aux parties I′ de I')
inv('insertion','above parties ... de','I′ with insertion tick')
inv('text','cardinality and divisor qualifier','de cardinal 2. Deux tels diviseurs, correspondant à des parties I′,I″ in P_2(I),')
inv('text','intersection condition baseline','se rencontrent sss, canceled elles, on a I′ cap I″ = phi-like empty set')
inv('deletion','within intersection condition','elles, under an independent horizontal cancellation')
inv('deletion','after i.e., next baseline','sss, live preferred with possible cancellation retained as an alternative')
inv('text','partition conclusion, two baselines','I′,I″ et complement forment justement une partition de I de type (2,2,1)')
inv('text','first three lines of lower paragraph','D’après l’étude combinatoire de l’icosaèdre, choisissant une orientation de I — ce qui détermine un icosaèdre orienté, ou encore un')
inv('text','fourth lower line','icos. gauche|graphe) les baseline 10 diviseurs à l’infini')
inv('deletion','small writing below final l’infini','tentative en ordre')
inv('text','last main baseline','de hat M_{0,I}, i.e. les inserted 10 éléments de P_2(I),')
inv('insertion','above les ... éléments','10 with insertion tick')
inv('insertion','bottom right, unfinished','ou (par')
inv('deletion','bottom-right lower line','tentative correspon-, final dash retained')
inv('margin note','bottom left','65','lighter pencil hand, not confidently attributed')

doubts=[
 {'place':'Heading','reading':'de','alternatives':'des','confidence':'medium','reason':'The final low hook does not securely exclude an additional s; uncertainty is marked in place.'},
 {'place':'M1044, last codimension-2 label','reading':last_label,'alternatives':'IV, triple prime, or double prime','confidence':'low','reason':'The raised strokes are densely overworked; graph-theoretic expectations do not settle them.'},
 {'place':'Opening prose after Dans','reading':r'\unsure{de|le}','alternatives':'de or le; possible attachment to adjacent sloping insertion','confidence':'medium','reason':'The word is visible at the main baseline with no separate strike, but the initial loop and its relation to the insertion are not fully secure.'},
 {'place':'M1045, inserted pair','reading':r"\unsure{\{a',a''\}}",'alternatives':'Exact small prime count within the supported two-entry braced set','confidence':'medium','reason':'Curly braces and two a-like bodies are visible; the tiny raised strokes remain crowded.'},
 {'place':'First canceled trial','reading':strike1,'alternatives':'Original relation partly hidden','confidence':'low','reason':'The double P uprights survive, but the entire canceled expression is not exposed. Unindexed C doubt retained.'},
 {'place':'Second canceled trial','reading':strike2,'alternatives':'Possible obscured prefix and internal strokes not recovered','confidence':'low','reason':'Dense hatching hides several characters; no every-character resolution is claimed. Unindexed C doubt retained.'},
 {'place':'M1046, parenthetical ending','reading':r'\unsure{avait|aurait}','alternatives':'avait or aurait','confidence':'low','reason':'The middle joining strokes are compressed; dotted i and final t exclude H’s ayant more securely than they distinguish the two C choices.'},
 {'place':'M1047, margin definition RHS','reading':r"\unsure{\mathbb P^1_{\mathbb Z}\wedge_{\mathfrak S_3}\widetilde{I''}}",'alternatives':'Final primed/tilded factor not wholly recovered','confidence':'low','reason':'Long strokes trail the I-like factor; the expected associated-bundle construction is not used to resolve it.'},
 {'place':'Second sss after i.e.','reading':second_sss,'alternatives':'Live sss or canceled sss','confidence':'low','reason':'The apparent slash may be the cursive joining stroke rather than an independent cancellation. Both states remain explicit.'},
 {'place':'M1050, word after icos.','reading':r'\unsure{gauche|graphe}','alternatives':'gauche or graphe','confidence':'medium','reason':'A c/h-like rise and lack of a secure p-descender favor gauche, but the compressed middle does not decide.'},
 {'place':'Canceled en ordre','reading':r'\deleted{\unsure{en ordre}}','alternatives':'Some letters hidden by horizontal strike','confidence':'low','reason':'The stroke clearly cancels the two small words; not every underlying letter is plain. Unindexed C doubt retained.'},
 {'place':'Canceled final continuation','reading':r'\deleted{\unsure{correspon-}}','alternatives':'Internal letters partly concealed','confidence':'low','reason':'Exposed initial c/o, later upstrokes, and final dash support C’s tentative reading, but the cancellation blocks a full resolution.'},
]

notes=[
 'The manuscript introduces the case of hat M!_{0,5} or hat M_{0,I}, draws three codimension columns, and states that there are ten divisors at infinity, each a copy of hat M!_{0,4}; an inserted refinement identifies a divisor with hat M_{0,I″(3)amalg(*)} and a projective line over Z. These geometric identifications were read as manuscript claims, not proved in this run. The tiny drawn gap in the last graph segment is preserved as ink geometry without asserting a disconnected intended graph.',
 'An independent finite enumeration on I={0,1,2,3,4} produced ten two-element subsets, three disjoint two-element partners for every subset, fifteen unordered disjoint pairs, and fifteen distinct partitions with block-size multiset (1,2,2). It also counted thirty ordered incidences and verified 30/2=15. This checks the combinatorial counts in the prose and arrow labels, not the geometric correspondence between these sets and boundary strata.',
 'The manuscript states that two such divisors meet exactly when their two-element subsets are disjoint, and describes the resulting partition as I′, I″, and I minus their union. The set partitions constructed in the finite enumeration have this form. The geometric intersection criterion itself was carried as background and was not independently established. The phi-like glyph is transcribed from its long-stemmed loop shape, not chosen to make the criterion true.',
 'The left margin gives a proposed definition of P^1_{I″} using P^1_Z, a wedge with lower S_3, and a tilded/primed final factor. The alphabets and lower placement are visible; the whole RHS remains doubtful. No associated-bundle or torsor construction was proved, and no expected formula was substituted for the unresolved trailing strokes.',
 'The lower paragraph invokes the combinatorial study of the icosahedron and claims that choosing an orientation of I determines an oriented icosahedron, then uses the abbreviation icos. with the unresolved word gauche|graphe. This orientation/icosahedron claim was read but not proved or checked against external material. The paragraph continues to the ten elements of P_2(I) and stops with the unfinished insertion ou (par and a canceled tentative correspon-.',
 'Diplomatic limits retained: de|des in the heading; the omitted small de|le after Dans, whose attachment is not fully secure; the overworked last graph index; the tiny prime count in the inserted pair; avait|aurait; both canceled formula trials; the margin RHS; uncertain cancellation of the second sss; gauche|graphe; and the canceled en ordre and correspon-. The unmatched closing parenthesis after gauche|graphe and the unfinished opening parenthesis in ou (par are retained. The two full icosaèdre readings were resolved only on their own saved crops.',
 'Reading coverage: full scan once for layout, each native half once, and eighteen unique crops saved and viewed. Crop02 is 3000 pixels wide; the others are 2600 pixels wide, with crop06 rotated -20 degrees. Physical_lines_read=33 counts author folio and heading (2), diagram header/labels/vertices-and-arrows (3), thirteen main-body prose baselines (13), sloping tuple insertion (1), inserted precision line (1), marginal formula and raised def label (2), inserted I′ (1), five lower-paragraph main lines (5), inserted 10 (1), canceled en ordre (1), bottom-right ou (par and canceled continuation as two separate marginal lines (2), and pencil foliation (1). Ordinary indices and superscripts belong to their formula bands. No OCR, internet lookup, or TeX compilation was used.',
 'Provisional, occurrence-specific hand observation: à is reduced to two separated dark marks in trois points à l’infini (crop05), pts à l’infini (crop07), correspondant à des parties (crop09), and the lower diviseurs à (crop18). The reading à here follows the repeated local form and syntax; this is not a rule that every colon-like sign is à. The first sss has three connected hooks without an i dot. The second abbreviation has a similar joining diagonal, so its cancellation state is not treated as certain.',
]

check_events=[
 {'statement_id':'147-066-N1','date':'2026-11-20','who':'reader_c; GPT-6 Astra Pro; reasoning effort not exposed','type':'carried as background without fault found','outcome':'Read the manuscript’s boundary-divisor and projective-line identifications while transcribing the diagram and correction. No independent geometric proof, moduli construction, or isomorphism verification was performed; cancellation and inscription uncertainties remain.'},
 {'statement_id':'147-066-N2','date':'2026-11-20T21:45:37Z','who':'reader_c; GPT-6 Astra Pro; reasoning effort not exposed','type':'computation or formal certificate','outcome':'Python itertools.combinations enumerated all two-element subsets of a five-element set and unordered disjoint pairs. Exact results: 10 subsets, partner-degree multiset {3:10}, 15 disjoint unordered pairs, 15 distinct partitions, all block-size types (1,2,2), 30 incidences, and 30/2=15. Assertions checked these finite results. The computation does not establish that the manuscript’s divisors/points realize this model.'},
 {'statement_id':'147-066-N3','date':'2026-11-20','who':'reader_c; GPT-6 Astra Pro; reasoning effort not exposed','type':'carried as background without fault found','outcome':'Read the claimed geometric equivalence between divisor intersection and disjoint index subsets. The finite enumeration checks the associated set configurations only. No geometric implication or converse was proved.'},
 {'statement_id':'147-066-N4','date':'2026-11-20','who':'reader_c; GPT-6 Astra Pro; reasoning effort not exposed','type':'carried as background without fault found','outcome':'Read the margin expression as a manuscript definition. Its final factor is still doubtful, so no exact identity or associated-bundle construction was verified or inferred from background expectations.'},
 {'statement_id':'147-066-N5','date':'2026-11-20','who':'reader_c; GPT-6 Astra Pro; reasoning effort not exposed','type':'carried as background without fault found','outcome':'Read the orientation/icosahedron statement and unfinished continuation. No independent icosahedral or orientation argument was performed, and no external source or other-page proof was consulted.'},
]

notation=[
 {'sign':r'\mathbb P,\mathbb Z','reading':'double-stroked projective P and base Z','evidence':'Separated parallel P uprights and Z diagonals in the insertion and margin; corresponding P uprights survive under both formula cancellations.','scope':'scan066, five P glyphs and two Z glyphs'},
 {'sign':'Codim / codim','reading':'capital initial only in first table header','evidence':'First C reaches ascender height; later initial c forms remain low.','scope':'scan066, diagram81'},
 {'sign':r'\phi','reading':'phi-shaped empty-set sign','evidence':'Small loop high on a long sloping stem with a long lower extension.','scope':'scan066, intersection condition'},
 {'sign':'sss','reading':'literal three-s abbreviation','evidence':'Three joined hooks without a separate i dot; second occurrence has uncertain cancellation state.','scope':'scan066, two successive logical clauses'},
 {'sign':'I with crowded raised strokes','reading':last_label,'evidence':'Overwork prevents secure IV versus prime-count distinction.','scope':'scan066, last diagram label'},
]
hand_log=[
 {'habit':'Reduced à may resemble two vertically separated dots or short marks.','pages':[66],'all_occurrences':'Provisional local comparison: trois points à l’infini, pts à l’infini, correspondant à des parties, and the lower diviseurs à; no global rule is inferred.','witness_misreadings':'H leaves some of these phrases illegible; the observation is retained as a reading aid, not a reason to change unrelated punctuation.'},
 {'habit':'Joined s hooks can resemble a diagonal strike.','pages':[66],'all_occurrences':'Both sss groups have rising joins; the second lacks a secure independent cancellation stroke.','witness_misreadings':'H normalizes to ssi; C marks the second occurrence as certainly deleted.'},
 {'habit':'Long f crossbar can be mistaken for a whole-word cancellation.','pages':[66],'all_occurrences':'The single forment has a long attached leftward f bar and continuous following letters.','witness_misreadings':'H gives a struck forment and then repeats forment where the next word is justement.'},
 {'habit':'Double-stroked P and Z retain separated inner white space.','pages':[66],'all_occurrences':'Five P and two Z glyphs checked, including the P outlines under cancellation.','witness_misreadings':r'C uses \mathbf where the visible glyphs are double-stroked.'},
 {'habit':'Final de/des hook can remain ambiguous.','pages':[66],'all_occurrences':'Heading de/des remains explicitly uncertain; the extra word after Dans is separately de/le uncertain.','witness_misreadings':'C and H select de and des respectively in the heading; both omit the extra small opening word.'},
]
abbreviations=[{'written':'pts','expansion':'points'},{'written':'nb','expansion':'nombre'},
 {'written':'sss','expansion':'si et seulement si (contextual expansion; literal sss retained)'},
 {'written':'i.e.','expansion':'id est'},{'written':'icos.','expansion':'icosaèdre'},
 {'written':'def','expansion':'définition'},{'written':'codim / Codim','expansion':'codimension'}]

second_boxes=[]
def second(kind,reading,crop=None,box=None):
    x0,y0,x1,y1=box if box is not None else boxes[crop]
    second_boxes.append({'box':f'B{len(second_boxes)+1:02d}','kind':kind,
                         'x0':x0,'y0':y0,'x1':x1,'y1':y1,'reading':reading})
second('handwritten number',r'\mspage{32}'+'\n'+heading,1)
second('doubtful formula',diagram,2)
second('insertion',start,3)
second('struck passage',strike2+' '+precision+" (ayant comme on avait vu,",4)
second('word disagreement',r"et \unsure{avait|aurait}) trois points à l'infini --- les",5)
second('margin note',margin,6)
second('handwritten number',count,7)
second('handwritten number',partition_intro,box=[354,1025,1663,1133])
second('insertion',partition_middle,8)
second('word disagreement',qualifier,9)
second('struck passage',criterion,10)
second('struck passage',partition_end,11)
second('word disagreement',lower1,12)
second('word disagreement',lower2,13)
second('word disagreement',r'icos. \unsure{gauche|graphe})',14)
second('handwritten number',r'les $10$ diviseurs à',18)
second('insertion',lower4,15)
second('struck passage',r"l'infini \deleted{\unsure{en ordre}}"+'\n'+unfinished,16)
second('margin note',r'\margin{65}',17)

report={'scan':66,'reader':'reader_c','physical_lines_read':33,'changes':changes,'decisions':decisions,
 'inventory':inventory,'doubts':doubts,'notes':notes,'check_events':check_events,'notation':notation,
 'hand_log':hand_log,'abbreviations':abbreviations,'second_boxes':second_boxes,
 'unresolved':['Heading de/des and the extra opening de/le with its attachment.',
 'M1044: overworked final graph superscript IV/III/II.',
 'M1045: tiny prime count within the supported braced a-pair.',
 'Both canceled formula trials remain tentative as whole expressions.',
 'M1046: avait/aurait; M1047: margin RHS, especially the final tilded/primed factor.',
 'Second sss: live preferred, cancellation retained as an alternative.',
 'M1050: gauche/graphe; canceled en ordre and correspon- remain uncertain.'],
 'witness_comparison':'C preserves most prose, short forms, correction states, and the unfinished ending. It omits the small word after Dans and needs double-stroked alphabets, first-header capitalization, divider-crossing arrow layout and the small segment gap, the phi-shaped glyph, unaccented def, and an explicit doubt about the second sss cancellation. H has the double-stroked alphabets and local def spelling but normalizes or misreads several short forms, moves the first quote boundary, supplies a conventional triple in the inserted tuple, leaves readable prose as ill, replaces comma boundaries with parentheses, misstates forment/justement, misses the second inserted 10 and canceled en ordre, and reads the bottom par/correspon- differently. Both full icosaèdre words are readable. Geometry in H’s unavailable separate drawing file was not assessed.'}

assert len(changes)==35
assert [x['id'] for x in decisions]==[f'M{i}' for i in range(1044,1051)]
for x in changes:
    assert (WORK/'crops'/x['crop']).is_file()
    assert x['against_C'] or x['against_H']
for n in boxes: assert (WORK/'crops'/f'147_scan066_place{n:02d}.png').is_file()
for e in check_events:
    n=int(e['statement_id'].rsplit('N',1)[1]); assert 1<=n<=len(notes)
assert all(not n.startswith('147-066-N') for n in notes)
assert proposed.count(r'\mathbb P')==5
assert proposed.count(r'\mathbb Z')==2
assert r'\margin{65}' in proposed and r'\mspage{32}' in proposed
assert r'\illegible' not in proposed
(OUT/'proposed.tex').write_text(proposed)
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'return_dir':str(OUT),'physical_lines_read':33,'crops':18,'changes':len(changes),
 'decisions':len(decisions),'inventory':len(inventory),'doubts':len(doubts),'second_boxes':len(second_boxes),
 'check_events':len(check_events)},ensure_ascii=False))
