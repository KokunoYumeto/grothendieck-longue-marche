from pathlib import Path
import json

root=Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
packet=Path('/workspace/scratch/481648fc487b/reader_packets/150_scan031')
C=(packet/'C.tex').read_text(); H=(packet/'H.tex').read_text()
insert=r'\inserted{\unsure{de|dans} $\unsure{X_j,|X_{j\prime}}$}'
formula=r"$E_{k',k}=p_{jk}^{-1}(\overline E_{j',j})$"
assoc=r'\deleted{\unsure{associé}}'
assoc_insert=r"\inserted{(des $X_{j'}$ dans les $X_j$)}"
overwritten=r"\deleted{$X$}$E_{j',j}$"
canceled_nb=r'\deleted{\uline{NB} Une}'
margin=r'''\margin{\uline{NB} si $i,j$ ont pour borne inf $h$,
cela implique $X_i\cap X_j=X_h$. \unsure{même pour} \illegible{3} \unsure{c)} $\unsure{X_i\cap X_j}$.}'''
final_formula=r'$X_k\unsure{\}}\ne\varnothing$'
corollary_end=r'minorant $h$ (tel que \deleted{\unsure{le}} '+final_formula+r'\ldots)'

page=r'''\scanpage{31}
\mspage{10}
est ``transversal'' i.e. \deleted{\unsure{X|si}} $\exists$ voisinages cylindriques
de $X_{j'}$ '''+insert+r''' et un de $X_{k'}$ dans $X_k$, tel que l'application
$X_k\unsure{-|\to}X_j$ induit un \deleted{hom}\inserted{morphisme} sur les
cylindres (compatible avec les structures
cylindriques) et de plus
'''+formula+r'''.

Système de voisinages cylindriques '''+assoc+'\n'+assoc_insert+r'''
compatible avec une stratification : tel que
dans b, les '''+overwritten+r''' ($j$ fixé, $j'$ prédécesseur)
soient compatibles. Notion correspondante
pour les germes de voisinage cylindrique.

Stratification cylindrique : stratification munie
d'une telle ``structure cylindrique'', en
termes de germes de voisinages cylindriques.

'''+canceled_nb+r'''
\uline{NB} Une stratification précylindrique \inserted{resp. cylindrique}
est sûrement
``\unsure{équisingulier|équisingulière}'' au sens le plus fort qu'on
puisse introduire $\to$ (\unsure{C|cf.}) suite.

Mais j'ai oublié une condition, que j'exigerai
pour tte stratification :
\[
(0)\qquad \forall i,j\in I,\quad\text{on a}\quad
X_i\cap X_j=\bigcup_{k\le i,j}X_k
\]
'''+margin+r'''

Corollaire : Si $X_i\cap X_j\ne\varnothing$, alors $i,j$ ont un
'''+corollary_end+r'''
\margin{30}
'''

boxes={
'number10':[64,38,130,86], 'opening_est':[335,39,858,132],
'canceled_after_ie':[1012,56,1087,132], 'plural_neighborhoods':[1182,75,1668,170],
'inserted_dans':[436,118,733,249], 'map_induit':[512,272,982,366],
'morphisme_hom':[1111,225,1435,331], 'barred_formula':[1228,450,1665,566],
'associated_insert':[1184,581,1649,726], 'dans_b_canceled_x':[331,847,1605,953],
'singular_germes':[864,1051,1635,1161], 'structure_quotes':[721,1271,1413,1380],
'struck_nb':[305,1562,559,1664], 'live_nb_insert_state':[964,1558,1664,1780],
'equisingulier_phrase':[298,1727,1550,1832], 'introduire_suite':[302,1832,1194,1946],
'condition_abr':[312,2008,901,2115], 'zero_axiom':[382,2087,1454,2226],
'corollary_start':[328,2212,1470,2307], 'corollary_end':[317,2268,1444,2353],
'diagonal_margin':[52,1648,1216,2352], 'folio30':[21,2296,92,2347],
'margin_final_formula':[1058,1653,1220,1771], 'corollary_struck_and_tick':[1046,2225,1238,2352]
}
def crop(n):return f'150_scan031_{n}.jpg'
kinds={
'word':('misread word','words'), 'symbol':('misread symbol or index','symbols and indices'),
'omission':('omission','omissions'), 'absent':('text not on the page','text not on page'),
'state':('deletion state (struck given live or live given struck)','struck text'),
'placement':('insertion or placement','insertion placement'),
'abbr':('abbreviation expanded or spelling modernised','abbreviation/spelling'),
'ill':(r'readable ink left as \ill{}','readable ink left as illegible'), 'other':('other','other')}
changes=[]
def ch(place,c,h,final,evidence,n,kind,cC=False,cH=False,confidence='high',marked=False,consequential=''):
    k,e=kinds[kind]
    changes.append(dict(place=place,C=c,H=h,final=final,evidence=evidence,crop=crop(n),box=boxes[n],
        confidence=confidence,kind=k,error_kind=e,marked_in_H=marked,change_C=cC,change_H=cH,consequential=consequential))

ch('opening word / est versus Soit','est',r'\struck{Soit}','est',
   'The overtraced word has the small e loops, s turn and tall crossed t of est. There is no four-letter Soit sequence. Its heavy lower return is part of the overtrace, not a cancellation crossing the word.',
   'opening_est','word',cH=True)
ch('opening word / live state','est',r'\struck{Soit}','est',
   'The e/s baseline is retraced, but no independent cancellation traverses the complete word; the t remains live.',
   'opening_est','state',cH=True)
ch('opening quotation marks',"``transversal''",'« transversal »',"``transversal''",
   'The opening is a pair of short high ticks; the terminal high mark is the writer’s compressed paired quotation mark, not a guillemet.',
   'opening_est','other',cH=True)
ch('cancellation after i.e.',r'\deleted{\unsure{X|si}}','[absent]',r'\deleted{\unsure{X|si}}',
   'A compact canceled cluster survives between i.e. and the existence sign. Crossing diagonal and horizontal strokes cannot securely separate the underlying X/si alternatives. H omits this real canceled cluster.',
   'canceled_after_ie','omission',cH=True,confidence='low')
ch('existence phrase / plural nouns','voisinages cylindriques','voisinage cylindrique','voisinages cylindriques',
   'The final low returns after the g/e group and the adjective’s terminal group support the plural endings in both words. H gives singular forms.',
   'plural_neighborhoods','word',cH=True)
ch('raised neighborhood phrase / attachment',r"de $X_{j'}$ \inserted{dans $X_j$}",r"\add{de $X_{j'}$,}",
   r"de $X_{j'}$ "+insert,
   'The baseline de Xj′ is live original text. A separate raised d-word and Xj-like formula are attached after it by a curved leader. The raised preposition is d plus a low return, hence de|dans remains uncertain; the low terminal tick is comma-like but may be a prime. H conflates the baseline phrase with the raised insertion.',
   'inserted_dans','placement',cH=True,confidence='medium')
ch('raised neighborhood phrase / terminal tick',r'\inserted{dans $X_j$}',r"\add{de $X_{j'}$,}",insert,
   'A small separate tick stands low to the right of the raised j. It must be represented, although comma versus prime is not securely decided. C records no such terminal mark; this row records the visible mark, not the mere addition of preposition uncertainty.',
   'inserted_dans','omission',cC=True,confidence='low')
ch('et un / leader mistaken for deletion','et un',r'\struck{et un}','et un',
   'The curved stroke passes above et un and leads from the raised insertion back to the baseline Xj′. It is not a strike through et un.',
   'inserted_dans','state',cH=True)
ch('map connector / retained graphical doubt',r'$X_k\unsure{-|\to}X_j$',r'$X_k\to X_j$',r'$X_k\unsure{-|\to}X_j$',
   'The short connector has only a tiny terminal downward return; it does not securely distinguish a headless stroke from the writer’s abbreviated arrowhead. The leading dash reading differs from H’s definite arrow, but no new change is counted against C.',
   'map_induit','symbol',cH=True,confidence='low',consequential='Direction is not supplied where the ink leaves dash/arrow unresolved.')
ch('map sentence / induit','induit','induise','induit',
   'The last letter is a tall t with a cross-stroke and curled terminal return, not the se sequence of induise.',
   'map_induit','word',cH=True)
ch('canceled hom / literal abbreviation',r'\deleted{\unsure{hom.}}',r'\struck{homéomorphisme}',r'\deleted{hom}',
   'The short canceled span contains a tall h, an o loop and the low m run. Its length and surviving strokes do not contain homéomorphisme. No separate terminal period is visible.',
   'morphisme_hom','abbr',cC=True,cH=True,confidence='medium')
ch('morphisme / raised replacement position',r'\deleted{\unsure{hom.}}\inserted{morphisme}',r'\add{morphisme} \struck{homéomorphisme}',
   r'\deleted{hom}\inserted{morphisme}',
   'Morphism(e) is written directly above the canceled short hom, as its replacement. The long descending stroke at the right belongs to the preceding line’s que, not to a cancellation of the insertion.',
   'morphisme_hom','placement',cH=True)
cf=r"$\overline E_{\unsure{k';k|k;k}}=p_{jk}^{-1}(\overline E_{\unsure{j';j|j;j}})$"
hf=r"E_{k;k}=p_{jk}^{-1}(E_{j';j})"
ch('upper equality / first E has no overbar',cf,hf,formula,
   'The first E has its ordinary connected top, middle and lower horizontal strokes. The top ends with a short upright return, but there is no separate line above it.',
   'barred_formula','symbol',cC=True,consequential='Distinguishes plain E on the left from barred E inside the inverse image.')
ch('upper equality / detached bar on right E',cf,hf,formula,
   'A separate horizontal bar is visibly detached above the E within the parentheses. H omits it.',
   'barred_formula','symbol',cH=True)
ch('upper equality / first index and comma',cf,hf,formula,
   'A high short prime follows the first k; a separate low comma then precedes the second k. There is no additional dot for a semicolon. The written index is k′,k.',
   'barred_formula','symbol',cC=True,cH=True,confidence='medium',consequential='Retains the first k prime and the literal comma separator.')
ch('upper equality / second index and comma',cf,hf,formula,
   'The first j is followed at upper right by a short prime, then by a low comma before the second j. The second j has its own dot, which must not be reassigned to a semicolon.',
   'barred_formula','symbol',cC=True,cH=True,confidence='medium')
ch('system definition / canceled associé',r'\deleted{associé}',r'\struck{\ill{}}',assoc,
   'A canceled word is present after cylindriques. Parts of the a/s run, the o loop, i dot and final accent survive; associé remains the leading reading, but the heavy horizontal strike prevents complete certainty. H leaves the whole span illegible.',
   'associated_insert','ill',cH=True,confidence='medium',marked=True)
ch('raised parenthesis / des versus avec',assoc_insert,r"(avec $X_{j'}$ dans les $X_j$)",assoc_insert,
   'The opening group has a compact d-like rise and e/s continuation, not the longer a-v-e-c sequence. The words and formulas read des Xj′ dans les Xj.',
   'associated_insert','word',cH=True)
ch('raised parenthesis / attachment to system definition',assoc_insert,r"(avec $X_{j'}$ dans les $X_j$)",assoc_insert,
   'The parenthesis is above the system-definition line, with a long bent leader ending at the canceled associé. It belongs to that definition; H places it after the preceding equality.',
   'associated_insert','placement',cH=True)
ch('reference to b / punctuation','dans b,','dans b),','dans b,',
   'After the b is a short low comma. No closing parenthesis is visible.',
   'dans_b_canceled_x','absent',cH=True)
ch('overwritten X before E',r"\deleted{\unsure{$X$}}$E_{j';j}$",r"$E_{j';j}$",overwritten,
   'Two crossing diagonals of an X remain underneath the vertical and horizontal strokes of the replacement E. This is a real overwritten X, not a decorative E flourish; the deletion is preserved separately.',
   'dans_b_canceled_x','symbol',cC=True,cH=True)
ch('system E index / comma separator',r"$E_{j';j}$",r"$E_{j';j}$",r"$E_{j',j}$",
   'The index repeats the high prime and distinct lower comma of the upper equality. No additional upper dot establishes a semicolon.',
   'dans_b_canceled_x','symbol',cC=True,cH=True,confidence='medium')
ch('germ phrase / singular forms','voisinage cylindrique.','voisinages cylindriques.','voisinage cylindrique.',
   'After the g/e and q/u/e endings there is no extra s stroke. The final stop follows the adjective’s single terminal e return.',
   'singular_germes','word',cH=True)
ch('structure cylindrique / quotation marks',"``structure cylindrique''",'« structure cylindrique »',"``structure cylindrique''",
   'Small high paired marks enclose the phrase. They are not angular guillemets.',
   'structure_quotes','other',cH=True)
ch('canceled NB Une line',r'\deleted{\uline{NB} \unsure{Une}}',r'\struck{\emph{Mettre}}',canceled_nb,
   'The first group is underlined NB: the N uprights and B lobes survive the sweeping cancellation. The following U has two tall strokes, then an n turn and e tail. The long left curve joins the cancellation and is not an independent opening parenthesis. Mettre does not fit these two groups.',
   'struck_nb','word',cC=True,cH=True)
ch('live NB / resp. insertion',r'\inserted{resp. cylindrique}',r'\add{\uncertain{resp.} cylindrique}',r'\inserted{resp. cylindrique}',
   'The raised insertion has the short r/e/s run, p descender and a detached period, followed by cylindrique. Its curved leader attaches after précylindrique.',
   'live_nb_insert_state','word',cH=True,marked=True)
ch('live NB / sûrement resolved',r'\unsure{sûrement}','sûrement','sûrement',
   'The s curve, u with a separate circumflex, short r/e/m/n run and final crossed t are present. No cancellation prevents reading the word.',
   'live_nb_insert_state','word',cC=True)
ch('live NB / est sûrement remains live',r'est \unsure{sûrement}',r'\struck{est sûrement}', 'est sûrement',
   'The long curve above est sûrement is the placement leader from resp. cylindrique; it does not cross the bodies of these words. The heavy final t return is not a strike.',
   'live_nb_insert_state','state',cH=True)
ch('live NB / H duplicate est',r'est \unsure{sûrement}',r'\struck{est sûrement} \uncertain{est}','est sûrement',
   'Only one est occurs on this baseline. No second est is inserted between sûrement and the following quoted adjective.',
   'live_nb_insert_state','absent',cH=True,marked=True)
ch('equisingularity adjective / unresolved ending',r'\unsure{équisingulier|équisingulière}','équisingulière',r'\unsure{équisingulier|équisingulière}',
   'The ending has a tall l, short dotted/marked i-e group and final r-like return, without an unequivocal extra e. Masculine équisingulier remains the leading reading, but the small terminal accent/dot and compressed end do not settle gender. H fixes the feminine. No change is counted against the retained C doubt.',
   'equisingulier_phrase','word',cH=True,confidence='medium')
ch('NB phrase / au rather than un','au sens','un sens','au sens',
   'The preposition is a short a-like mark and a low u return before the distinct sens group; it is not un.',
   'equisingulier_phrase','word',cH=True)
ch('NB phrase / le read from ink','le plus fort',r'\ill{} plus fort','le plus fort',
   'The tall looped l and its connected low e stand between sens and plus. A diagonal marginal stroke passes nearby but is separate.',
   'equisingulier_phrase','ill',cH=True,marked=True)
ch('NB phrase / qu’on','qu\'on','que',"qu'on",
   'The long q descender is followed by the small u/apostrophe group and o/n ending. The apostrophe and final low n return support qu’on.',
   'equisingulier_phrase','word',cH=True)
ch('NB continuation / puisse introduire','puisse introduire',r'\ill{} \ill{}','puisse introduire',
   'The first p descender and broken u/i/s/s/e run are visible. The next word has an i, crossed t, round o and d/u/i/r/e sequence. They are ordinary live words, despite the marginal line crossing nearby.',
   'introduire_suite','ill',cH=True,marked=True)
ch('NB continuation / rightward arrow',r'\illegible{1}',r'\ill{} \ill{}',r'$\to$',
   'A horizontal shaft ends in an oblique returning head pointing right after introduire. The tall crossing loop immediately to its left belongs to the diagonal marginal continuation, not to an extra main-line word.',
   'introduire_suite','symbol',cC=True,cH=True)
ch('NB continuation / suite','suite.',r'\uncertain{suite}.','suite.',
   'The s/u/i group, i dot, tall crossed t and final e are legible, followed by a detached stop.',
   'introduire_suite','word',cH=True,marked=True)
ch('condition sentence / pour rather than de','de tte stratification', 'pour les stratifications','pour tte stratification',
   'A descending p and broken low o/u/r strokes form the main-line preposition. A separate diagonal marginal word crosses above it. The following abbreviation has two t uprights sharing a cross-stroke and a final e.',
   'condition_abr','word',cC=True,cH=True,confidence='medium')
ch('condition sentence / literal tte and singular noun','tte stratification','les stratifications','tte stratification',
   'The abbreviated tte and the singular final -tion are visible. No s follows the noun before the colon. The abbreviation is retained, without expansion to toute.',
   'condition_abr','abbr',cH=True)
ch('intersection axiom / label zero',r'(0)','[absent]',r'(0)',
   'The digit 0 is enclosed by two curved parentheses at the left of the axiom. A diagonal marginal stroke crosses the vicinity, but the label remains legible.',
   'zero_axiom','omission',cH=True)
ch('intersection axiom / no terminal stop',r'X_i\cap X_j=\bigcup_{k\le i,j}X_k',r'X_i\cap X_j=\bigcup_{k\le i,j}X_k .',r'X_i\cap X_j=\bigcup_{k\le i,j}X_k',
   'The union expression ends at Xk; the native half shows blank paper after it, without a separate full stop. The crop’s upper edge does not include the complete tops of the union and final X, which were read in the native half.',
   'zero_axiom','absent',cH=True)
ch('diagonal margin / first sentence',r'\uline{NB} si $i,j$ ont pour borne inf $h$,',r'\emph{NB} si $i,j$ ont un \ill{} $h$,',r'\uline{NB} si $i,j$ ont pour borne inf $h$,',
   'Read along the slanted note: underlined NB, si i,j ont pour, then borne inf h on the next short line. The words pour, borne and inf have surviving stems and loops; un is not the written preposition.',
   'diagonal_margin','word',cH=True)
ch('diagonal margin / implication clause',r'cela implique $X_i\cap X_j=X_h$',r'\uncertain{$\inf(i,j)$} \ill{} $X_i\cap X_j=X_h$',r'cela implique $X_i\cap X_j=X_h$',
   'The next slanted line begins cela, followed by the connected implique group. The separate formula below reads Xi∩Xj=Xh. The word group is not an inf(i,j) expression.',
   'diagonal_margin','word',cH=True,confidence='medium',marked=True)
ch('diagonal margin / retained uncertain continuation',r'\unsure{même pour} \illegible{3} \unsure{c)} $\unsure{X_i\cap X_j}$',r'\ill{} \ill{} \ill{} minorant',r'\unsure{même pour} \illegible{3} \unsure{c)} $\unsure{X_i\cap X_j}$',
   'A long final marginal line continues upward across several main-text baselines and ends beside/below précylindrique. Some strokes support the inherited même pour and terminal Xi∩Xj readings, but overlapping main text prevents secure intervening words or the c)-like mark. H does not preserve these candidate words/formula. This is a substantive H disagreement with unresolved evidence, not a newly resolved C reading.',
   'diagonal_margin','ill',cH=True,confidence='low',marked=True)
ch('marginal note / H’s final minorant belongs to body',r'minorant $\unsure{k|h}$',r'\ill{} \ill{} \ill{} minorant',r'minorant $h$',
   'The plainly horizontal minorant belongs to the last line of the corollary. It is not on the slanted marginal continuation that ends above it. H duplicates it into the margin note.',
   'diagonal_margin','placement',cH=True)
ch('corollary / capital Si','Corollaire : Si','Corollaire : si','Corollaire : Si',
   'The S after the colon is a tall capital form with a high upper curve and large lower loop; it is larger than the following i.',
   'corollary_start','word',cH=True)
ch('corollary / minorant h',r'minorant $\unsure{k|h}$',r'minorant $k$',r'minorant $h$',
   'The letter has a straight upright and one simple arch, unlike the two-branch k that follows in Xk. The written h is retained even though the later formula still has k.',
   'corollary_end','symbol',cC=True,cH=True,confidence='medium',consequential='Preserves the manuscript’s h/k mismatch rather than repairing the variable.')
ch('corollary / canceled le',r'\deleted{\unsure{le}}','[absent]',r'\deleted{\unsure{le}}',
   'A heavily canceled group precedes Xk. An e-like open double curve survives on its right and tall strokes remain at the left, but the l/e sequence cannot be fully separated from the cancellation. The inherited le remains doubtful; H omits the canceled material.',
   'corollary_struck_and_tick','omission',cH=True,confidence='low')
ch('corollary / detached graphical mark before inequality',r'$X_k\ne\varnothing$',r'$X_k\neq\emptyset$',final_formula,
   'Between Xk and the inequality is a detached tall curly/semicolon-like stroke with a long lower return. Neither witness records it. A right-brace shape is given only as a graphical doubt; no semantic role or correction is inferred.',
   'corollary_struck_and_tick','omission',cC=True,cH=True,confidence='low',consequential='Accounts for visible ink without forcing it into a mathematical operation.')
ch('bottom-left foliation / 30',r'\margin{30}','[absent]',r'\margin{30}',
   'The small 3 and closed 0 are written at the lower left in thin lighter ink. The hand is uncertain; this is not automatically the author’s own foliation.',
   'folio30','omission',cH=True)

marks=[]
def mark(m,ctx,decision,reading,evidence,n,confidence):
    marks.append(dict(mark=m,context=ctx,decision=decision,reading=reading,evidence=evidence,crop=crop(n),box=boxes[n],confidence=confidence))
mark(r'\unsure{X|si}','cancellation between i.e. and exists','undecided',r'\unsure{X|si}','Dense crossing strokes do not identify the underlying X/si cluster securely.','canceled_after_ie','low')
mark(r'\unsure{-|\to}','X_k connector X_j','undecided',r'\unsure{-|\to}','Only a tiny terminal return is present; dash versus abbreviated arrowhead remains unresolved.','map_induit','low')
mark(r'\unsure{hom.}','canceled word below morphisme','other','hom','Surviving h upright, o loop and low m run; no detached final period.','morphisme_hom','medium')
mark(r"\unsure{k';k|k;k}",'first E index in upper equality','other',r"k',k",'The upper short stroke is a prime and the separate lower curved mark is a comma, with no additional semicolon dot.','barred_formula','medium')
mark(r"\unsure{j';j|j;j}",'barred E index inside inverse image','other',r"j',j",'An upper-right prime and lower comma follow the first j; the final j has its own dot.','barred_formula','medium')
mark(r'\unsure{$X$}','overwritten X beneath E in dans b line','first',r'$X$','Two crossing X diagonals survive beneath the live E strokes.','dans_b_canceled_x','high')
mark(r'\unsure{Une}','canceled underlined NB followed by Une','first','Une','Two tall U strokes followed by the low n turn and e tail are legible through the cancellation.','struck_nb','high')
mark(r'\unsure{sûrement}','live NB clause after est','first','sûrement','The letters and separate circumflex over u are legible; the nearby leader does not cancel them.','live_nb_insert_state','high')
mark(r'\unsure{équisingulier|équisingulière}','quoted adjective in live NB','undecided',r'\unsure{équisingulier|équisingulière}','A final r-like return is visible but the small marked terminal group does not securely settle an additional e or the accent.','equisingulier_phrase','medium')
mark(r'\illegible{1}','after puisse introduire and before parenthetical reference','other',r'$\to$','Horizontal shaft and clear returning head point right; the tall neighboring loop is part of the diagonal margin.','introduire_suite','high')
mark(r'\unsure{C|cf.}','parenthetical reference before suite','undecided',r'\unsure{C|cf.}','A C-like curved form is present, but crossing marginal strokes prevent securely separating a possible small f and stop.','introduire_suite','low')
mark(r'\unsure{même pour}','long final diagonal margin line after X_i cap X_j = X_h','undecided',r'\unsure{même pour}','Low strokes amid crossing main text give only provisional support to the inherited words.','diagonal_margin','low')
mark(r'\illegible{3}','middle of final diagonal margin line','undecided',r'\illegible{3}','Several small word groups are crossed by the main text and remain unreadable; no contextual expansion is supplied.','diagonal_margin','low')
mark(r'\unsure{c)}','diagonal margin immediately before final formula','undecided',r'\unsure{c)}','The curved/angular mark is not securely separated from adjacent strokes; a relation-like form is also visually possible, so c) stays provisional.','margin_final_formula','low')
mark(r'\unsure{X_i\cap X_j}','final formula in long diagonal margin line','undecided',r'\unsure{X_i\cap X_j}','Crossed X-like forms, a rounded cap and descending final index are present, but overlap with précylindrique prevents full index certainty.','margin_final_formula','low')
mark(r'\unsure{k|h}','minorant in corollary','alternative','h','The simple arch after the upright differs from the later k’s two branches.','corollary_end','medium')
mark(r'\unsure{le}','canceled word before X_k in corollary','undecided',r'\unsure{le}','An e-like right-hand curve and tall left strokes remain, but most of the cluster is covered by the cancellation.','corollary_struck_and_tick','low')

inventory=[]
def inv(i,k,pos,first,hand='his hand'):
    inventory.append(dict(element=f'031.E{i:02d}',kind=k,position=pos,first_words_or_objects=first,sheet_kind='text',hand=hand,transcribed='yes'))
inv(1,'margin note','upper left','10; principal page number')
inv(2,'text','principal lines 1–5','est transversal i.e. exists voisinages cylindriques; compatible morphism and inverse-image equality')
inv(3,'deletion','line 1 between i.e. and existence sign','unresolved X/si cluster')
inv(4,'insertion','above line 2 after baseline X_j′','de|dans X_j with low comma/prime doubt, attached by curved leader')
inv(5,'deletion','line 3 below morphisme','hom')
inv(6,'insertion','above line 3','morphisme replaces hom')
inv(7,'display','right side of principal line 5',r"E_{k',k}=p_{jk}^{-1}(barred E_{j',j})")
inv(8,'text','principal lines 6–10','Système de voisinages cylindriques compatible avec une stratification; corresponding germs')
inv(9,'deletion','end of principal line 6','associé, uncertain through cancellation')
inv(10,'insertion','above end of principal line 6','(des X_j′ dans les X_j), with bent leader')
inv(11,'deletion','principal line 8, beneath live E','overwritten X')
inv(12,'text','principal lines 11–13','Stratification cylindrique: stratification munie d’une telle structure cylindrique')
inv(13,'deletion','principal line 14','underlined NB Une, entire aborted beginning canceled')
inv(14,'text','principal lines 15–17','underlined NB Une stratification précylindrique … est sûrement équisingulier/équisingulière …')
inv(15,'insertion','above right of principal line 15','resp. cylindrique, attached after précylindrique')
inv(16,'text','principal line 17','puisse introduire rightward arrow (C/cf.) suite')
inv(17,'text','principal lines 18–19','Mais j’ai oublié une condition, que j’exigerai pour tte stratification')
inv(18,'display','principal line 20','axiom (0): for all i,j in I, intersection equals union over k≤i,j')
inv(19,'margin note','diagonal from lower-left margin upward to below précylindrique','underlined NB si i,j ont pour borne inf h; cela implique X_i cap X_j=X_h; long doubtful continuation')
inv(20,'text','principal lines 21–22','Corollaire: Si intersection nonempty, i,j have minorant h, with later X_k retained')
inv(21,'deletion','principal line 22 before X_k','doubtful le under dense cancellation')
inv(22,'text','principal line 22 between X_k and inequality','detached curly/semicolon-like mark, represented by doubtful right brace')
inv(23,'margin note','extreme lower left','30','uncertain; thin lighter foliation ink')

doubts=[
dict(place='cancellation after i.e.',reading=r'\deleted{\unsure{X|si}}',alternatives='X | si; cancellation sequence not recovered',confidence='low'),
dict(place='raised neighborhood phrase',reading=insert,alternatives='de | dans; raised X_j followed by comma | X_j′; no contextual correction',confidence='low'),
dict(place='map connector',reading=r'$X_k\unsure{-|\to}X_j$',alternatives='dash | right arrow with abbreviated terminal return',confidence='low'),
dict(place='canceled associé',reading=assoc,alternatives='associé remains provisional; a/s portions are heavily crossed',confidence='medium'),
dict(place='quoted equisingularity adjective',reading=r'\unsure{équisingulier|équisingulière}',alternatives='masculine ending preferred but extra e/accent not securely excluded',confidence='medium'),
dict(place='parenthetical reference before suite',reading=r'(\unsure{C|cf.})',alternatives='C | cf.; overlap prevents full separation of small strokes',confidence='low'),
dict(place='diagonal margin final line',reading=r'\unsure{même pour} \illegible{3} \unsure{c)} $\unsure{X_i\cap X_j}$',alternatives='Inherited provisional words retained; c)-like mark could be relation-like; intervening groups and final indices remain uncertain',confidence='low'),
dict(place='corollary canceled group',reading=r'\deleted{\unsure{le}}',alternatives='le remains provisional through dense cross-hatching',confidence='low'),
dict(place='corollary detached mark',reading=r'\unsure{\}}',alternatives='right brace is only a graphical approximation; curly/semicolon-like detached stroke has no established semantic role',confidence='low'),
]
notes=[
'This page continues the definition of a transversal configuration by cylindrical neighborhoods and a compatible morphism, with an inverse-image equality. It then defines a compatible system of cylindrical neighborhoods and a cylindrical stratification in terms of germs. These are reported claims, not independently checked definitions or implications.',
'The NB claims a precylindrical, respectively cylindrical, stratification is surely equisingular in a strongest sense still to be introduced. The adjective’s gender remains uncertain, and the arrow and doubtful parenthetical reference before suite are retained literally.',
'The added condition (0) expresses an intersection as a union of strata indexed by common lower bounds. The corollary reports that a nonempty intersection has a common lower bound. No proof, implication check, or independent computation was performed; check_events is intentionally empty.',
'The corollary visibly says minorant h, while its later nonempty stratum is still X_k. This authorial variable mismatch is preserved. A detached curly mark between X_k and the inequality is also preserved as a narrow graphical doubt, without assigning a mathematical function.',
'In the upper equality the left E is plain and the right E has a detached overbar. The indices read k′,k and j′,j with low comma separators; no semicolon dots are supplied. The same comma convention occurs in the later E index.',
'The inserted neighborhood phrase is genuinely raised and is attached after baseline X_j′. Its d-word and small terminal tick remain uncertain. The leader passes above et un, which is live. Likewise the leader from resp. cylindrique leaves est sûrement live.',
'The diagonal margin note occupies several short initial lines and one very long continuation, crossing the principal text up to the small formula beneath précylindrique. Its high crossing loop near introduire and the tiny slanted formula below précylindrique are marginal writing, not additional main-line words. The final marginal words have not been forced from mathematical expectation.',
'The canceled opening NB Une is distinct from the live NB below. The upper opening est is overtraced but live. The short canceled hom has no detached period; the full homéomorphisme supplied by H is not written there.',
'The heading 10 is retained as the principal handwritten page number, consistent with both witnesses and the dark ink of the manuscript. The small lower-left 30 is thin and lighter; its hand remains uncertain. Scan 31 is editorial metadata.',
'Line count 22 counts principal baselines including the separate canceled NB Une line and the axiom baseline, excluding raised insertions, the diagonal note and page numbers. The source’s l’appli-/cation line wrap is joined as application in the running transcription.',
'Twenty-four first-pass crops were viewed. Two additional localized crops address previously unaccounted final marginal-formula strokes and the corollary’s detached mark; neither resolves the remaining marginal words. The whole page and each native half were viewed once, with no OCR, other-page reading, external research or TeX compilation.',
'H’s bibliographical notes and its expected-index comment are editorial. Header emphasis macro differences are not counted as substantive manuscript readings. A retained uncertainty is counted against H only when the leading candidate or recorded ink substantively differs; adding uncertainty alone is not counted as a new C error.'
]
notation=[
dict(form=r"E_{k',k},\quad\overline E_{j',j}",meaning_or_shape='Plain first E; detached bar only on second E. High primes and separate low commas delimit the indices.',places='upper inverse-image equality; later E_j′,j'),
dict(form=r'X_k\unsure{-|\to}X_j',meaning_or_shape='Short connector with tiny terminal return; dash/arrow remains unresolved.',places='third principal line'),
dict(form=r'\to',meaning_or_shape='Clear rightward shaft with returning head used in running prose.',places='after puisse introduire'),
dict(form='h versus k',meaning_or_shape='The h in minorant has one simple arch; the k in later X_k has distinct branches. The mismatch is not regularized.',places='last principal line'),
dict(form=r'\unsure{\}}',meaning_or_shape='Graphical approximation of a detached curly/semicolon-like mark; semantic role unknown.',places='between final X_k and nonemptiness inequality')]
abbreviations=[
dict(form='i.e.',expansion='id est'),dict(form='hom',expansion='abbreviated homomorphism/homeomorphism word; intended expansion not settled from the canceled abbreviation'),
dict(form='resp.',expansion='respectivement'),dict(form='tte',expansion='toute'),dict(form='NB',expansion='nota bene'),dict(form='inf',expansion='inférieure in borne inf'),
dict(form='b',expansion='reference label; no closing parenthesis written'),dict(form='C | cf.',expansion='unresolved parenthetical reference; do not silently expand')]
hand_log=[
dict(habit='A curved insertion leader can cross or bracket nearby live words.',places='raised de/dans X_j above et un; resp. cylindrique above est sûrement',consistent='Both leaders can be followed back to their insertions; nearby words remain live.',witness_errors='H strikes et un and est sûrement, then duplicates est.'),
dict(habit='Heavy retracing of letters differs from cancellation.',places='opening est; overwritten X beneath E; canceled NB Une and hom',consistent='Live est lacks an independent canceling sweep, while the other listed spans have replacement/cancellation evidence.',witness_errors='H calls opening est struck Soit and canceled NB Une Mettre.'),
dict(habit='Comma separators and primes are distinct small strokes in indices.',places='upper k′,k and j′,j; later E_j′,j',consistent='High short prime followed by a separate low curved comma; no extra semicolon dot.',witness_errors='Both witnesses print semicolons; H also misses the first k prime.'),
dict(habit='An E’s own cap is not necessarily an overbar.',places='first and second E in upper equality',consistent='First E cap is connected; second E overbar is detached.',witness_errors='C adds a first overbar; H omits the second.'),
dict(habit='Small abbreviated forms may have no final stop.',places='canceled hom; tte; borne inf',consistent='No detached stop after hom; tte and inf retained as written.',witness_errors='C provisionally gives hom.; H expands homéomorphisme and changes tte stratification to les stratifications.'),
dict(habit='Diagonal marginal continuation can cross several otherwise unrelated text lines.',places='from lower-left NB up to formula below précylindrique',consistent='Orientation separates the note from principal text; remaining overlaps stay doubtful.',witness_errors='H transfers minorant from the corollary into its marginal-note transcription and leaves much readable initial marginal text illegible.'),
dict(habit='Variable letters may differ genuinely within a sentence.',places='minorant h followed by X_k',consistent='One clear h-shaped arch contrasts with later branched k; no harmonization.',witness_errors='H prints k; C’s h alternative is retained as the reading.')]

second_boxes=[]
def audit(kind,coords,reading,reason):
    second_boxes.append(dict(box=f'b{len(second_boxes)+1:02d}',kind=kind,coords=coords,reading=reading,reason=reason))
audit('handwritten number',boxes['number10'],r'\mspage{10}','Complete handwritten principal page number.')
audit('C/H word difference',boxes['opening_est'],"est ``transversal''",'Est/Soit, live state and quoted word.')
audit('struck passage; doubt formula',boxes['canceled_after_ie'],r'\deleted{\unsure{X|si}}','Complete canceled cluster with C/proposed doubt.')
audit('C/H word difference',boxes['plural_neighborhoods'],'voisinages cylindriques','Both singular/plural word differences.')
audit('insertion; doubt formula; low-confidence departure',boxes['inserted_dans'],r"$X_{j'}$ "+insert+' et un','Raised phrase and whole doubtful formula, together with live neighboring words.')
audit('insertion; struck passage; C/H word difference; low-confidence departure',boxes['morphisme_hom'],r'\deleted{hom}\inserted{morphisme} sur','Short canceled abbreviation and raised replacement; C doubt resolution below high confidence.')
audit('doubt formula; C/H word difference',boxes['map_induit'],r'$X_k\unsure{-|\to}X_j$ induit','Whole formula containing C/proposed connector doubt and the induit/induise difference.')
audit('doubt formula; handwritten number; low-confidence departure',boxes['barred_formula'],formula+'.','Whole equality contains both original C index doubts and exponent −1; all bars and comma indices included.')
audit('insertion; struck passage; C/H word difference',boxes['associated_insert'],assoc+' '+assoc_insert,'Canceled associé and its raised parenthetical replacement, including des/avec difference.')
audit('struck passage; doubt formula; low-confidence departure',boxes['dans_b_canceled_x'],r"dans b, les "+overwritten+r" ($j$ fixé, $j'$ prédécesseur)",'Overwritten X, original C doubt, complete E index and b punctuation.')
audit('C/H word difference',boxes['singular_germes'],'voisinage cylindrique.','Singular/plural disagreements in both words.')
audit('C/H word difference',boxes['structure_quotes'],"``structure cylindrique'',",'Literal quotation marks around the phrase.')
audit('struck passage; C/H word difference',boxes['struck_nb'],canceled_nb,'Entire canceled NB Une; includes resolved C Une and H Mettre difference.')
audit('insertion; C/H word difference',boxes['live_nb_insert_state'],r'précylindrique \inserted{resp. cylindrique} est sûrement','Raised insertion and live est sûrement; diagonal marginal ink in this box is separately covered by the full margin box.')
audit('C/H word difference',boxes['equisingulier_phrase'],r"``\unsure{équisingulier|équisingulière}'' au sens le plus fort qu'on",'Complete disputed word groups; retained gender doubt and readable words H omits or changes.')
audit('C/H word difference; low-confidence departure',boxes['introduire_suite'],r'puisse introduire $\to$ (\unsure{C|cf.}) suite.','Words, arrow resolving C illegibility and doubtful parenthetical reference; overlapping marginal strokes are separately inventoried.')
audit('margin note; doubt formula; C/H word difference',boxes['diagonal_margin'],margin,'Entire diagonal note and its complete doubtful final formula, including all three retained marginal C doubts and illegible group; source crop was rotated −30 degrees for reading.')
audit('C/H word difference; low-confidence departure',boxes['condition_abr'],'pour tte stratification :','Medium-confidence departure from C de; literal abbreviation and singular noun.')
axiom=r'''\[
(0)\qquad \forall i,j\in I,\quad\text{on a}\quad
X_i\cap X_j=\bigcup_{k\le i,j}X_k
\]'''
audit('handwritten number',[382,2065,1454,2226],axiom,'Whole axiom with label 0; enlarged upper bounds include complete union and final X tops.')
audit('C/H word difference',boxes['corollary_start'],r'Corollaire : Si $X_i\cap X_j\ne\varnothing$, alors $i,j$ ont un','Capital Si versus H lower-case si and complete nonemptiness formula.')
audit('struck passage; doubt formula; low-confidence departure',boxes['corollary_end'],corollary_end,'Whole final line: resolved h alternative, canceled le doubt, complete formula with detached graphical doubt and ellipsis.')
audit('margin note; handwritten number',boxes['folio30'],r'\margin{30}','Complete lighter bottom-left foliation; hand uncertain.')

result=dict(scan=31,reader='reader_c',line_count=22,changes=changes,marks=marks,inventory=inventory,
    doubts=doubts,notes=notes,check_events=[],notation=notation,abbreviations=abbreviations,
    hand_log=hand_log,second_boxes=second_boxes)
(root/'reader_returns'/'150_scan031.tex').write_text(page)
(root/'reader_returns'/'150_scan031.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:len(result[k]) for k in ('changes','marks','inventory','doubts','check_events','second_boxes')},indent=2))
