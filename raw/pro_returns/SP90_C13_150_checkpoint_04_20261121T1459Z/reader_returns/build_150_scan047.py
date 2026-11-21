from pathlib import Path
import json, re

BASE = Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
PACKET = Path('/workspace/scratch/481648fc487b/reader_packets/150_scan047')
TEX = BASE / 'reader_returns/150_scan047.tex'
C = (PACKET/'C.tex').read_text()
H = (PACKET/'H.tex').read_text()
T = TEX.read_text()

coords = {
 'folio19':[66,42,140,105], 'empty_pair_corresp':[300,38,1531,143],
 'flag_lui_equal':[304,135,829,235], 'lui_abbreviation':[1223,233,1610,322],
 'cancel_minus':[1224,310,1652,404], 'top_margin':[236,348,507,499],
 'maximal_clause':[755,496,1367,604], 'contenu_ds':[804,669,1416,758],
 's_ident':[1410,667,1653,756], 'drap_first':[301,728,940,849],
 'live_minus':[658,921,1272,1019], 'strict_initial':[896,1011,1191,1092],
 'ou_supset':[306,1390,815,1486], 'first_cyl_map':[1089,1357,1445,1488],
 'second_cyl_map':[1420,1472,1668,1550], 'initial_dans':[994,1557,1450,1649],
 'fibrant_target':[289,1642,1059,1760], 'si_tuple_insert':[1230,1601,1639,1702],
 'cancel_si':[1236,1651,1576,1727], 'tuple_d':[327,1721,664,1810],
 'cancel_alors':[641,1705,1225,1799], 'decomposition_d':[1224,1693,1610,1806],
 'cancel_plusgrand':[315,1765,1642,1845], 'live_tuple_d0':[321,1805,860,1883],
 'correspondent_aux':[842,1799,1586,1876], 'cancel_par_donc':[305,1849,945,1935],
 'cancel_ce_sont':[930,1824,1647,1926], 'cancel_beta':[307,1899,1118,2020],
 'right_insertion':[1062,1893,1585,2093], 'cancel_forme_formula':[299,1990,1093,2111],
 'contenant_delete':[632,2089,780,2170], 'lower_insert_cancel':[773,2114,1595,2216],
 'corresp_biunivoque':[1061,2156,1639,2230], 'bottom_display':[331,2210,1549,2313],
 'folio46':[20,2297,81,2348], 'lui_dash_complete':[620,137,1120,240]
}

D = dict(scan=47, reader='reader_a', line_count=28, changes=[], marks=[], inventory=[], doubts=[], notes=[], check_events=[], notation=[], abbreviations=[], hand_log=[], second_boxes=[])

def change(place, c, h, final, evidence, crop, kind, err, cc=False, hh=False, conf='high', mh=False, cons=''):
    assert c == '[absent]' or c in C, ('C quote',place,c)
    assert h == '[absent]' or h in H, ('H quote',place,h)
    assert final in T, ('final',place,final)
    D['changes'].append(dict(place=place,C=c,H=h,final=final,evidence=evidence,crop=f'150_scan047_{crop}.jpg',box=coords[crop],confidence=conf,kind=kind,error_kind=err,marked_in_H=mh,change_C=cc,change_H=hh,consequential=cons))

change('line 1 / pair of loop-and-stem symbols',r'(\varnothing,\varnothing)',r'(\emptyset,\emptyset)',r'(\phi,\phi)',
 'Each symbol has a small loop crossed by a long descending stem, rather than the conventional oval with a short diagonal slash. This agrees with the phi shape established locally, but the current ink was inspected independently. Both symbols and the intervening comma are visible despite the long cancellation.',
 'empty_pair_corresp','misread symbol or index','symbols and indices',True,True)
change('line 1 / corresp.', 'corresp. au drapeau', 'correspond au drapeau', 'corresp. au drapeau',
 'The p descender is followed by a separate point and then au; no ond ending is written.',
 'empty_pair_corresp','abbreviation expanded or spelling modernised','abbreviation/spelling',False,True)
change('line 2 / flag without braces',r'$i,j$ lui',r'$\lbrace i,j\rbrace$ lui',r'$i,j$ lui',
 'The two dotted letters and comma are written without separate enclosing braces. The nearby long diagonal belongs to the cancellation, not a delimiter.',
 'flag_lui_equal','text not on the page','text not on page',False,True)
change('line 2 / verbal equality after lui',r'lui $\unsure{=}$','lui-même --',r'lui $=$ \textendash{}',
 'Two separate horizontal bars follow lui. There are no letters spelling même. The enlarged context confirms exactly one detached prose dash before si.',
 'flag_lui_equal','abbreviation expanded or spelling modernised','abbreviation/spelling',True,True)
change('line 3 / second verbal equality',r'lui-\unsure{mê},','lui-même,',r'lui-$=$,',
 'A short hyphen follows lui, then two horizontal bars and a comma. The purported mê is a two-bar sign; both bars survive the global cancellation.',
 'lui_abbreviation','misread word','words',True,True)
change('line 4 / cancelled connector',r'\Sigma_{ij}-\Sigma_i',r'\Sigma_{ij}\to\Sigma_i',r'\Sigma_{ij}-\Sigma_i',
 'The connector is a single headless horizontal stroke. The j descender and the short preceding i with its dot are distinct on the source Sigma.',
 'cancel_minus','misread symbol or index','symbols and indices',False,True)
change('left margin beside lisse / hyp.',r'\unsure{top.|hyp.}',r'hyp.\ C.\ I','hyp. C.',
 'The first letter has the tall h stem; the following joined descending y/p strokes and final point support hyp., rather than top. The separate final notation is still doubtful and is not resolved by this decision.',
 'top_margin','misread word','words',True,False,'medium',True)
change('left margin beside lisse / placement and underline',r'\inserted{(\unsure{top.|hyp.}\unsure{C$^\infty$|C.I})}',r'dans la marge, en face de « lisse », « (\uncertain{hyp.\ C.\ I}) » souligné, également sous les traits.',r'\margin{\deleted{\uline{(hyp. C.\unsure{$^{t}$|I})}}}',
 'The parenthetical annotation sits to the left of lisse, with a separate curved underline, and is crossed by the same long diagonal as the cancelled paragraph. H explicitly records this placement and underline in its note; that note is witness evidence, not added manuscript text.',
 'top_margin','insertion or placement','insertion placement',True,False,'high',True)
change('line 8 / ds',r'contenu ds',r'contenus dans',r'\unsure{contenus|contenu} ds',
 'After the possible final s of contenu there is a separate looped d and short s-like run. The full letters of dans are absent. The number ending remains a separate narrow doubt, not an established C error.',
 'contenu_ds','abbreviation expanded or spelling modernised','abbreviation/spelling',False,True,'medium')
change('line 8 / Sigma index',r'ds $\Sigma_{ij}$',r'dans $\Sigma_j$',r'ds $\Sigma_{ij}$',
 'Before the long descending j there is a short i attached near the Sigma foot with a detached dot. The index is ij rather than j alone.',
 'contenu_ds','misread symbol or index','symbols and indices',False,True,'high')
change('line 8 / s’ ident body',r"s'\unsure{ident} donc",r"d'où $\simeq",r"s'\unsure{ident} donc",
 'A small s-like loop and a distinct apostrophe precede the compressed body; this is not the taller initial d of d’où. The body does not separate every letter of ident, so the existing doubt is retained.',
 's_ident','misread word','words',False,True,'medium')
change('line 9 / donc',r"s'\unsure{ident} donc",r"d'où $\simeq",r"s'\unsure{ident} donc",
 'The next baseline begins with donc before the raised equivalence sign; it is a separate visible word missing from H’s sequence.',
 'drap_first','omission','omissions',False,True)
change('line 9 / raised equivalence insertion',r'\inserted{$\simeq$}',r"d'où $\simeq\mathrm{Drap}",r'\inserted{$\simeq$}',
 'The wave and lower horizontal bar are above the baseline between donc and Drap; they are an insertion. H gives the sign inline without recording its inserted position.',
 'drap_first','insertion or placement','insertion placement',False,True)
change('line 9 / first interval has no dummy dot',r'I_{i<\cdot<j}',r'I_{i<\cdot<j}',r'I_{i< <j}',
 'The two less-than signs are adjacent with blank paper between them; there is no central dark dot. The two letters are dotted i and descending j.',
 'drap_first','text not on the page','text not on page',True,True)
change('line 12 / strict inclusion',r"d\subsetneqq d'",r"d\subsetneq d'",r"d\subsetneq d'",
 'The curved subset bottom is followed by one separate lower bar crossed by a slant. There is no second separate lower bar; the curved bottom must not be counted as one.',
 'strict_initial','misread symbol or index','symbols and indices',True,False)
change('line 16 / no comma before où',r"$\Sigma_{d''}$ où",r"$\Sigma_{d''}$, où",r"$\Sigma_{d''}$ où",
 'No independent punctuation stroke stands between the indexed Sigma and où. The low loop and detached accent belong to où.',
 'ou_supset','text not on the page','text not on page',False,True)
change('line 16 / strict superset',r"d''\supsetneqq d'",r"d''\supsetneq d'",r"d''\supsetneq d'",
 'As in the preceding strict subset, there is one separate crossed lower bar beneath the curved relation, not two.',
 'ou_supset','misread symbol or index','symbols and indices',True,False)
change('line 16 / raised sign is cancelled',r'\overset{\unsure{\alpha}}{\hookrightarrow}',r"au-dessus du symbole de la première flèche vers $\Sigma_{d'}$, un signe barré.",r'\overset{\deleted{\unsure{\alpha}}}{\hookrightarrow}',
 'An independent oblique stroke crosses the small raised alpha-like loop and tail. The underlying letter stays doubtful; the deletion state is clear. H explicitly describes this crossed sign in its note.',
 'first_cyl_map','deletion state (struck given live or live given struck)','struck text',True,False,'high',True)
change('line 16 / first cylinder arrow has a hook',r"\Sigma_{d''}\overset{\unsure{\alpha}}{\hookrightarrow}\Sigma_{d'}",r"\Sigma_{d''}\to\Sigma_{d'}",r"\Sigma_{d''}\overset{\deleted{\unsure{\alpha}}}{\hookrightarrow}\Sigma_{d'}",
 'A short hooked return is visible at the left end of the shaft, and a distinct head at its right. H’s plain arrow omits the hook; the cancelled raised sign is accounted for separately.',
 'first_cyl_map','misread symbol or index','symbols and indices',False,True)
change('line 18 / dans',r"segment initial dans $d''$",r"segment initial de $d''$",r"segment initial dans $d''$",
 'The tall looped d is followed by a long low a/n/s sequence; the word is dans, not the shorter de.',
 'initial_dans','misread word','words',False,True)
change('line 19 / target prime',r"\Sigma_{d''}\longrightarrow\Sigma_{d'}$ soit",r"\Sigma_{d''}\to\Sigma_d$ soit",r"\Sigma_{d''}\longrightarrow\Sigma_{d'}$ soit",
 'A separate raised prime follows the d in the target subscript. It remains distinct from the closing parenthesis and the following word.',
 'fibrant_target','misread symbol or index','symbols and indices',False,True)
change('line 19 / fibrant',r'\unsure{fibrant}',r'soit fibrant)',r'soit fibrant)',
 'The long f, dotted i, tall b return, low ran sequence and final t are readable in this live word. The crossing nearby is from the cancelled lower line, not a strike through the word itself.',
 'fibrant_target','misread word','words',True,False)
change('insertion above line 19 / tuple continuation',r"si $d'=(i_1- i_n)$",r"si $d'=(i_1,\ldots,i_n)$,",r"si $d'=(i_1-i_n)$",
 'The tuple has a dotted i with subscript 1, one continuous horizontal dash, and i with a low n. There are no internal commas or continuation dots.',
 'si_tuple_insert','misread symbol or index','symbols and indices',False,True)
change('insertion above line 19 / no following comma',r"\inserted{si $d'=(i_1- i_n)$},",r"\add{si $d'=(i_1,\ldots,i_n)$,}",r"\inserted{si $d'=(i_1-i_n)$}",
 'The closing parenthesis ends the raised insertion; there is no independent following comma. Both witnesses supplied one, at different markup positions.',
 'si_tuple_insert','text not on the page','text not on page',True,True)
change('line 20 / d tuple continuation',r'd=(i_1,-i_p)',r'd=(i_1,\ldots,i_p)',r'd=(i_1,-i_p)',
 'There is a comma after i_1, one horizontal dash, then i_p with no second comma. A separate comma follows the closing parenthesis in the prose.',
 'tuple_d','misread symbol or index','symbols and indices',False,True)
change('line 21 / cancelled subscript and second phrase',r'plus grand élément de $d_p$ et plus grand élément',r'plus grand élément \ill{} de $d$ \ill{}',r'plus \unsure{grand élément} de $d_p$ et plus \unsure{grand élément}',
 'The lower p is attached below the d, followed by et plus and another long grand élément group. The two compressed groups remain doubtful, but the p and the repeated phrase are more than the blank illegible spans supplied by H.',
 'cancel_plusgrand',r'readable ink left as \ill{}','readable ink left as illegible',False,True,'medium',True)
change('line 22 / avec',r"avec $d'_0",r"\ill{} $d'_0=",r"avec $d'_0=",
 'The live line begins avec, with an initial low a group and the v/e/c run, before the clearly separated d-prime-zero. H leaves this in an illegible span.',
 'live_tuple_d0',r'readable ink left as \ill{}','readable ink left as illegible',False,True,'medium',True)
change('line 22 / live tuple and ensuing clause',r"avec $d'_0=(i_{p+1},i_{p+2}--i_n)$, alors les $d''$ correspondent aux",r"$d'_0=(i_{p+1},i_{p+2},\ldots,i_n)$, alors les $d''$ correspondant aux",r"avec $d'_0=(i_{p+1},i_{p+2}\mathinner{\cdot-}i_n)$, alors les $d''$ correspondent aux",
 'This baseline lies between two separately cancelled baselines. The thin stroke above belongs to plus grand élément and that below to par d-prime; neither crosses the avec line. H’s struck wrapper incorrectly includes this entire live line.',
 'live_tuple_d0','deletion state (struck given live or live given struck)','struck text',False,True)
change('line 22 / tuple has point then dash',r'i_{p+2}--i_n',r'i_{p+2},\ldots,i_n',r'i_{p+2}\mathinner{\cdot-}i_n',
 'Exactly two continuation marks intervene: a compact point and a longer horizontal dash. They are not two dashes, and no extra commas or third dot are visible.',
 'live_tuple_d0','misread symbol or index','symbols and indices',True,True)
change('line 22 / correspondent',r'correspondent aux',r'correspondant aux',r'correspondent aux',
 'The ending after the long p descender has a small e-like mark, then the n run and tall final t. It supports correspondent; the a bowl of H’s correspondant is not formed.',
 'correspondent_aux','misread word','words',False,True,'medium')
change('line 23 / par d-prime',r"\unsure{par $d'$}",r"aux $d'$",r"\unsure{par $d'$}",
 'A separate cancelled group beginning with a p descender precedes d-prime. Its compressed a/r run remains uncertain, but H omits the whole word after the preceding live aux.',
 'cancel_par_donc','omission','omissions',False,True,'medium')
change('line 23 / parenthetical word before inequality',r'donc $\alpha\leq\beta$',r'$d_\alpha$, $\alpha\le\beta$',r'\unsure{donc} $\alpha\leq\beta$',
 'A tall initial loop is followed by a continuous baseline word; no separate lower alpha subscript and intervening comma are visible. The word-body remains compressed under the strike, hence doubtful donc rather than a resolved reading.',
 'cancel_par_donc','misread word','words',False,True,'medium')
change('line 23 / ce sont',r'ce sont les drapeaux',r'on a les drapeaux',r'\unsure{ce sont} les drapeaux',
 'The low two-word body ends with a short upright before les and favors ce sont. The strike coincides with its middle letters, so the phrase remains narrowly doubtful; H’s on a is not adopted.',
 'cancel_ce_sont','misread word','words',False,True,'low')
change('line 23 / word after drapeaux',r'drapeaux où',r'drapeaux ayant',r'drapeaux \unsure{où}',
 'The small terminal group is compressed under the cancellation. The proposed où remains doubtful; no grammatical completion was used to decide it.',
 'cancel_ce_sont','misread word','words',False,True,'low')
change('lines 24–25 / et is within the cancelled draft',r"élément, et \unsure{formé d'indices}",r"I_{>\alpha}$} et \struck{formé d'éléments}",r"élément, et \unsure{formé d'indices}",
 'Et lies at the right end of the beta line within the crossed draft, before the cancelled formé group. H places it live after the old formula.',
 'right_insertion','deletion state (struck given live or live given struck)','struck text',False,True,'medium')
change('right end of cancelled line 24 / formé d’indices',r"\unsure{formé d'indices}",r"formé d'éléments",r"\unsure{formé d'indices}",
 'The tall f, low formé body, d loop, apostrophe and short dotted following run favor d’indices, but the crossing obscures individual middle letters. Its place is before the following old formula, not after it as H sets it. This is retained as a strict cancelled doubt.',
 'right_insertion','misread word','words',False,True,'low')
change('line 25 / no de la before forme',r"\unsure{forme} $d\coprod",r"de la forme $d\amalg",r"\unsure{forme} $d\coprod",
 'The next cancelled baseline starts at the f-like upright and compressed forme body. No separate de la precedes it. The preceding et and formé d’indices are on the line above.',
 'cancel_forme_formula','text not on the page','text not on page',False,True,'medium')
change('line 25 / dummy dot before greater-than alpha',r'I_{\cdot>\alpha}',r'I_{>\alpha}',r'I_{\cdot>\alpha}',
 'There is a distinct dark point below and to the right of the capital I, before the greater-than sign and alpha. It is not the frame stroke underneath.',
 'cancel_forme_formula','omission','omissions',False,True)
change('right insertion / cancelled finis',r'\deleted{\unsure{finis}}','[absent]',r'\deleted{\unsure{finis}}',
 'A separate short word is crossed beneath drapeaux before the new interval formula. Its tall first stroke and dotted short strokes support the tentative finis, but every letter is not separately recoverable.',
 'right_insertion','omission','omissions',False,True,'medium')
change('right insertion / interval belongs to insertion',r"\inserted{\unsure{les} drapeaux \deleted{\unsure{finis}} $d''_0\subset I_{\cdot>i_p}$}",r"\add{des \uncertain{drapeaux}} $d''_0\subset I_{>i_p}$",r"\inserted{\unsure{les|des} drapeaux \deleted{\unsure{finis}} $d''_0\subset I_{\cdot>i_p}$\unsure{)|,}}",
 'The new d-double-prime-zero interval is written in the same crowded right-side replacement as drapeaux, above contenant. H ends its insertion wrapper before the formula. The first word and terminal curved mark are still doubtful.',
 'right_insertion','insertion or placement','insertion placement',False,True,'medium',True)
change('right insertion / dummy dot before greater-than i_p',r'I_{\cdot>i_p}',r'I_{>i_p}',r'I_{\cdot>i_p}',
 'A separate black point is written between the lower-right foot of I and the greater-than sign. The p descender and dot of the indexed i are separately visible to its right.',
 'right_insertion','omission','omissions',False,True)
change('line 26 / cancelled group after contenant',r'\deleted{\unsure{$d_0$|les}}','[absent]',r'\deleted{\unsure{$d_0$|les}}',
 'A heavily overwritten group stands between contenant and strictement. The lower loop is compatible with a subscript zero, while the rest overlaps a tall stroke; the two C alternatives cannot be resolved. H omits the cancelled group entirely.',
 'contenant_delete','omission','omissions',False,True,'medium')
change('line 27 / cancelled c’est donc un group',r"\deleted{\unsure{c'est donc un}}",r'\struck{\ill{}}',r"\deleted{\unsure{c'est donc un}}",
 'The c and apostrophe, a small loop, the tall d-like loop, and following low strokes survive underneath the cancellation. They support the tentative phrase but do not separate every letter; the doubt is preserved rather than declaring the whole span plain.',
 'lower_insert_cancel',r'readable ink left as \ill{}','readable ink left as illegible',False,True,'low',True)
change('insertion above line 27 / l’un de ces',r"l'un de ces",r"\uncertain{l'ensemble de ces}",r"l'un de ces",
 'The tall l loop is followed by an apostrophe and the short u/n run, then separately de ces. There is no longer ensemble body.',
 'lower_insert_cancel','misread word','words',False,True,'high',True)
change('insertion above line 27 / l’ens des',r"ou l'ens des",r'ou des',r"ou l'ens des",
 'Between ou and des, the l/apostrophe and compressed ens are written. There is no terminal point after ens. H omits this abbreviated group.',
 'lower_insert_cancel','omission','omissions',False,True)
change('line 27 / corresp.',r'corresp. biunivoque',r'correspondance bijective',r'corresp. biunivoque',
 'The p descender is immediately followed by a separate stop; no ondance ending is written.',
 'corresp_biunivoque','abbreviation expanded or spelling modernised','abbreviation/spelling',False,True)
change('line 27 / biunivoque',r'biunivoque',r'bijective',r'biunivoque',
 'The word begins with looped b and dotted i, then a longer u/n/i/v/o run and the q descender. This is biunivoque, not the shorter bijective.',
 'corresp_biunivoque','misread word','words',False,True)
change('line 28 / cancelled internal delimiter',r'\deleted{\unsure{\}}}','[absent]',r'\deleted{\unsure{\}|)}}',
 'An independently crossed vertical curved mark follows the first interval. Its exact close-delimiter shape remains doubtful between a curly close and a rounded close. H leaves the cancelled mark out.',
 'bottom_display','omission','omissions',False,True,'medium')
change('line 28 / continuation marks in final Drap formula',r'\coprod--\coprod',r'\amalg\cdots\amalg',r'\coprod\mathinner{-\,-\,\cdot}\coprod',
 'Exactly three continuation marks are present after the middle coproduct: two tiny horizontal strokes and one point. Their mixed shapes are preserved literally rather than normalized to three dots.',
 'bottom_display','misread symbol or index','symbols and indices',True,True)
change('bottom-left foliation / 46',r'\mspage{46}','[absent]',r'\margin{46}',
 'The light thin 46 sits at the lower-left edge, unlike the dark upper 19. Its digits are clear, but its authorship cannot be established from this leaf; it is not asserted as his own page numbering.',
 'folio46','other','other',True,True,'medium')

# The partial frame and looping cancellation are an actual graphic around ordinary text.
graphic = T[T.index(r'\leavevmode\rlap{\begin{tikzpicture}'):T.index(r'\deleted{\unsure{par')]
change('cancelled lower draft / partial frame and loop','[absent]',r"le passage biffé, depuis « plus grand élément », est en partie encadré et barré d'une boucle",graphic.rstrip(),
 'The lower draft has a left vertical edge, a long low returning edge, and a broad looping oblique cancellation over its lines. The paths are reproduced without drawing the text as graphics. H explicitly records both frame and loop in its note, so this is not counted as absent from H.',
 'cancel_forme_formula','drawing or diagram','drawings and diagrams',True,False)

def mark(original, decision, reading, evidence, crop, confidence='medium'):
    i = C.index(original)
    assert reading in T, ('mark reading',original,reading)
    D['marks'].append(dict(mark=original,context=C[max(0,i-32):i+len(original)+38].strip(),decision=decision,reading=reading,evidence=evidence,crop=f'150_scan047_{crop}.jpg',box=coords[crop],confidence=confidence))

mark(r'\unsure{=}','first','$=$','Both horizontal bars are separately visible under the general cancellation; no letter body occupies their position.','flag_lui_equal','high')
mark(r'\unsure{mê}','other',r'lui-$=$,','The cropped group consists of a preceding short hyphen, two equality bars, then comma, not the letters mê.','lui_abbreviation','high')
mark(r'\unsure{top.|hyp.}','alternative','hyp. C.','The h ascender and the successive y/p descenders with a final point are visible; no round initial t/o sequence is present.','top_margin','medium')
mark(r'\unsure{C$^\infty$|C.I}','undecided',r'C.\unsure{$^{t}$|I}',
     'Narrowed only: an open C and point precede a raised upright with a short right foot. There are no infinity loops. The upper nearby bar can belong to non on the main line; a raised t-like form and I remain possible.','top_margin','low')
mark(r'\unsure{ident}','undecided',r"s'\unsure{ident}",'The leading s and apostrophe are clear, but the joined ident body does not separate all letters.','s_ident','low')
mark(r'\unsure{\alpha}','undecided',r'\deleted{\unsure{\alpha}}','A small loop with a curled tail is compatible with alpha but crossed by an independent oblique line. Only its deleted state is resolved.','first_cyl_map','low')
mark(r'\unsure{fibrant}','first','fibrant','The live word shows f, dotted i, b return, compressed ran and final t.','fibrant_target','high')
mark(r'\unsure{si on est le}','undecided',r'\unsure{si $d$ est le|si on est le}',
     'The subject is one loop with an upward return, favoring d, but the strike covers enough of the phrase that the original on reading cannot be excluded.','cancel_si','low')
mark(r"\unsure{alors $d''$ est de la forme}",'undecided',r"\unsure{alors|donc} $d''$ \unsure{est de la forme}",
     'The d with two primes is clear. The first word and subsequent low words are crossed along their baselines; narrowing exposes the secure formula but does not settle the words.','cancel_alors','low')
mark(r"\unsure{par $d'$}",'undecided',r"\unsure{par $d'$}",'The p descender and d-prime are visible, but the middle a/r strokes merge with the strike.','cancel_par_donc','low')
mark(r"\unsure{formé d'indices}",'undecided',r"\unsure{formé d'indices}",'Tall f and d strokes and some short dotted letters survive; the strike obscures the intervening letters, so the entire old word group remains doubtful.','right_insertion','low')
mark(r'\unsure{forme}','undecided',r'\unsure{forme}','The initial f-like upright is partly the frame/cancellation intersection and the remaining low run is not letter-by-letter plain.','cancel_forme_formula','low')
mark(r'\unsure{les}','undecided',r'\unsure{les|des}','The initial loop in the cramped replacement can be l- or d-like; the ending is short es. Both supported alternatives are retained.','right_insertion','low')
mark(r'\unsure{finis}','undecided',r'\unsure{finis}','The separate short crossed word has a tall initial stroke and points, but the middle and ending coincide with the strike.','right_insertion','low')
mark(r'\unsure{$d_0$|les}','undecided',r'\unsure{$d_0$|les}','The heavily overwritten group has lower loops and a tall stroke; neither the formula nor the word can be resolved from the overlapping ink.','contenant_delete','low')
mark(r"\unsure{c'est donc un}",'undecided',r"\unsure{c'est donc un}",'The c/apostrophe and tall d-like loop survive, while the middle letters and last group are under the cancellation.','lower_insert_cancel','low')
mark(r'\unsure{\}}','undecided',r'\unsure{\}|)}','A curved closing mark is struck through after the first interval. Its middle cusp is not secure enough to exclude a rounded parenthesis.','bottom_display','low')

def inv(element,kind,position,words,hand='his hand'):
    D['inventory'].append(dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind='text',hand=hand,transcribed='yes'))

inv('N01','margin note','upper left, [66,42,140,105]','19')
inv('D01','deletion','top six main rows, lines 1–6',r'\uline{privé} de $(\phi,\phi)$; three long oblique cancellation strokes')
inv('I01','insertion','left margin beside line 5, subsequently cancelled',r'(hyp. C.\unsure{$^{t}$|I}), separately underlined')
inv('T01','text','main lines 7–11',r"élément (pour être fibré sur $\Sigma_i$) … soit lisse.")
inv('I02','insertion','above line 9 between donc and Drap',r'$\simeq$')
inv('T02','text','main lines 12–19',r'Plus généralement, si $d\subsetneq d\prime$ … i.e.')
inv('D02','deletion','above first hooked cylinder map, line 16',r'\unsure{\alpha}')
inv('D03','deletion','line 19 after i.e.',r'\unsure{si $d$ est le|si on est le}')
inv('I03','insertion','raised over D03',r"si $d'=(i_1-i_n)$")
inv('T03','text','line 20, live tuple and decomposition',r"$d=(i_1,-i_p)$ … d'où $d'=d\coprod d'_0$")
inv('D04','deletion','line 20 between live tuple and d’où',r"\unsure{alors|donc} $d''$ \unsure{est de la forme}")
inv('D05','deletion','line 21, separate horizontal cancellation',r'plus \unsure{grand élément} de $d_p$ et plus \unsure{grand élément}')
inv('T04','text','line 22, live between two struck lines',r"avec $d'_0=(i_{p+1},i_{p+2}\mathinner{\cdot-}i_n)$, alors les $d''$ correspondent aux")
inv('D06','deletion','lower draft, lines 23–25, partially framed and looped over',r"\unsure{par $d'$} … $d''_0\subset I_{\cdot>\alpha}$")
inv('D07','deletion','right end of line 24 within D06',r"et \unsure{formé d'indices}")
inv('G01','drawing','around and across D06, lower draft',r'partial frame with left upright and lower returning edge; broad oblique loop, reproduced as graphic-only TikZ paths')
inv('I04','insertion','crowded right side of the lower draft, before contenant',r"\unsure{les|des} drapeaux … $d''_0\subset I_{\cdot>i_p}$\unsure{)|,}")
inv('D08','deletion','inside I04, under drapeaux',r'\unsure{finis}')
inv('T05','text','main lines 26–27',r"contenant … cofinal dans $d''_0$ … corresp. biunivoque avec")
inv('D09','deletion','line 26 after contenant',r'\unsure{$d_0$|les}')
inv('D10','deletion','line 27 between cofinal clause and corresp.',r"\unsure{c'est donc un}")
inv('I05','insertion','above D10 and preceding corresp.',r"l'un de ces $d''_0$, ou l'ens des $d''_0$, est en")
inv('F01','display','bottom main line 28',r'\operatorname{Drap}\bigl(I_{i_p<\cdot<i_{p+1}}\deleted{\unsure{\}|)}}\coprod I_{i_{p+1}<\cdot<i_{p+2}}\coprod\mathinner{-\,-\,\cdot}\coprod I_{i_{n-1}<\cdot<i_n}\bigr)')
inv('D11','deletion','within F01 after the first interval',r'\unsure{\}|)}')
inv('N02','margin note','bottom left in thin lighter strokes','46','uncertain attribution; thin foliation hand')

def doubt(place, reading, alternatives, conf='low'):
    assert reading in T, ('doubt reading',place,reading)
    D['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence=conf))

doubt('top cancelled margin / final notation',r'C.\unsure{$^{t}$|I}','Raised t-like upright/right foot, or capital I; no infinity loops.')
doubt('line 6 / maximal under strike',r'\unsure{maximal}','The overall m…l profile supports maximal but its middle letters are flattened beneath the oblique strike.')
doubt('line 8 / number ending of contenu',r'\unsure{contenus|contenu}','A separate low s-like group precedes ds; it may be a final s or an extended terminal return.','medium')
doubt('line 8 / abbreviated verb body',r"s'\unsure{ident}",'s and apostrophe are secure; ident remains the tentative compressed body.')
doubt('line 11 / connector',r'\Sigma_{ij}\unsure{-|\longrightarrow}\Sigma_i','One horizontal shaft with a tiny downward endpoint; minus and abbreviated arrow remain possible. This is uncertainty only, not a counted witness error.','medium')
doubt('line 16 / crossed raised label',r'\deleted{\unsure{\alpha}}','Alpha-like loop and tail survive, but the independent diagonal obscures the small letter.')
doubt('line 19 / cancelled si phrase',r'\unsure{si $d$ est le|si on est le}','One looped subject favors d; the compressed crossed group still permits the former on reading.')
doubt('line 20 / cancelled first word',r'\unsure{alors|donc}','The tall initial and short low body do not distinguish the C/H alternatives securely.')
doubt('line 20 / cancelled continuation after d-double-prime',r'\unsure{est de la forme}','The phrase is crossed at baseline; only the separate preceding d-double-prime is plain.')
doubt('line 21 / first grand élément',r'plus \unsure{grand élément} de','Compressed middle letters under the strike remain uncertain.')
doubt('line 21 / second grand élément',r'et plus \unsure{grand élément}','The second long run matches the phrase but is not separately readable letter by letter.')
doubt('line 23 / par d-prime',r"\unsure{par $d'$}",'P descender and d-prime survive, while a/r are merged with the strike.')
doubt('line 23 / word before inequality',r'\unsure{donc}','Tall initial loop and low run support donc; inner letters remain covered.')
doubt('line 23 / ce sont',r'\unsure{ce sont}','C’s two-word reading is favored but the cancellation covers much of the body; H reads on a.')
doubt('line 23 / word after drapeaux',r'\unsure{où}','C’s reading remains tentative against H ayant; the compressed crossed ending is not safely resolved.')
doubt('line 24 / formé d’indices',r"\unsure{formé d'indices}",'Tall and dotted strokes support this group, but not all crossed letters can be recovered; H reads formé d’éléments.')
doubt('line 25 / forme',r'\unsure{forme}','The f-like initial is intersected by the frame and the remainder is low and joined.')
doubt('right insertion / initial article',r'\unsure{les|des}','Small first loop can be an l or a d; terminal es supports both C/H alternatives.')
doubt('right insertion / cancelled finis',r'\unsure{finis}','Tall initial and dotted strokes survive but the baseline strike obscures individual letters.')
doubt('right insertion / terminal curved mark',r'\unsure{)|,}','The curve is taller than nearby commas but low near the subscript baseline. A close parenthesis or extended comma is possible; no opening delimiter is supplied.','medium')
doubt('line 26 / cancelled group after contenant',r'\unsure{$d_0$|les}','Heavily overwritten tall and low loops do not securely distinguish the formula and word.')
doubt('line 27 / cancelled phrase',r"\unsure{c'est donc un}",'Initial c/apostrophe and d-like loop survive; the remaining crossed letters do not settle the phrase.')
doubt('final display / deleted internal close',r'\unsure{\}|)}','A curly close or rounded close, crossed by a diagonal; neither is certain.')

D['notes'] = [
 'The page reports a description of flags indexing the boundary stratification of a fibration associated with an initial segment d inside d-prime. In the short preceding case it states that the absence of intermediate flags, equivalently the successor condition on j, gives the stated smoothness condition. These are reports of the manuscript, not results checked in this reading.',
 'The sheet is upright and is ordinary handwritten working text. Six opening lines are crossed by three long oblique strokes. The surviving main argument continues at élément, followed by a heavily revised lower draft.',
 'The dark upper-left 19 is his sheet number. The thin lower-left 46 is retained as a marginal foliation of uncertain attribution; no authorship inference is forced from it.',
 'The opening parenthesis before qui has no supplied matching close at the end of the cancelled paragraph. Neither braces around i,j nor an expanded même is supplied. Both verbal two-bar signs are written literally.',
 'The top cancelled connector is a headless dash. The corresponding live connector ends in a tiny downward return, so minus versus abbreviated arrow remains a narrow uncertainty. The two later cylinder inclusions have hooks and heads, while the fibration arrows are plain arrows.',
 'The first cylinder arrow has a separately crossed raised alpha-like sign. Its deletion state is clear, but its letter is not resolved. H records the crossed sign in an editorial note; this evidence is included in collation accounting without transcribing the editorial prose.',
 'The target of the later fibrant map visibly has a prime on d. It is retained even if a different target might be expected mathematically. No mathematical inference changed the target.',
 'Continuation marks are deliberately literal: first Drap has i<<j without a dot; the inserted d-prime tuple has one dash without commas; d has comma then one dash; the live d-prime-zero tuple has point then dash; the final display has two small strokes then a point between coproducts. The final display does have dark dummy dots inside each of its three interval indices.',
 'The line beginning avec, through correspondent aux, is live between separate cancelled lines. H incorrectly includes it in a struck wrapper. The later right-hand replacement, the cancelled finis inside it, and the lower replacement above c’est donc un are inventoried separately.',
 'The partial frame and broad loop around the lower cancelled draft are reproduced by graphic-only TikZ paths over ordinary LaTeX text. H’s note explicitly records the frame and loop; no H omission is counted for that graphical presence. These paths are a visual approximation of the strokes, not pictures of the words.',
 'The terminal curved mark of the right-hand insertion is retained as close-parenthesis versus comma, with no extra comma and no supplied opening parenthesis. The final display’s crossed internal closing mark remains curly-close versus rounded-close.',
 'All agreed tokens, indices, accents, punctuation, and deletion states were inspected in the whole-page view and the two native halves. Every saved deep crop was then actually viewed. No OCR, external source, other page, second-pass reading, mathematical proof check, or TeX compilation was used.',
 'There are 35 distinct cropped places and 36 saved crop images. The extra lui_dash_complete image expands the right-hand context of the initial flag_lui_equal crop, which clipped the continuation after the obvious dash. It confirms exactly one detached dash before si; both files are retained.',
 'New uncertainty alone and changes in uncertainty scope are recorded only in doubts/marks, not as substantive C errors. The remaining narrow C/H word disagreements are retained with their actual evidence and low confidence where the cancelled letters cannot be resolved.'
]

D['notation'] = [
 dict(form=r'\phi',meaning_or_shape='Small loop with a long crossing descending stem, used here for the empty-set pair; literal phi-like form.',places='cancelled first line, both entries of the pair'),
 dict(form='=',meaning_or_shape='Two horizontal bars used verbally after lui; the second instance has a preceding hyphen. No expansion to même in the text.',places='cancelled lines 2–3'),
 dict(form=r'I_{i< <j}',meaning_or_shape='Two adjacent less-than signs with no central dummy point.',places='first live Drap formula, line 9'),
 dict(form=r'\subsetneq,\supsetneq',meaning_or_shape='Subset/superset curved body with one separate lower bar crossed by a slant.',places='d inside d-prime and d-double-prime containing d-prime'),
 dict(form=r'\overset{\deleted{\unsure{\alpha}}}{\hookrightarrow}',meaning_or_shape='Hooked arrow with an independently cancelled raised alpha-like label.',places='first cylinder inclusion, line 16'),
 dict(form=r'd\coprod d\prime_0',meaning_or_shape='Two upward strokes joined by a lower bar; treated as the coproduct notation. No substantive distinction is inferred from H’s amalg macro.',places='live decomposition and cancelled old formula'),
 dict(form=r'\mathinner{\cdot-}',meaning_or_shape='Literal point followed by dash, exactly two continuation marks.',places='live d-prime-zero tuple'),
 dict(form=r'\mathinner{-\,-\,\cdot}',meaning_or_shape='Literal two short strokes followed by a point, exactly three mixed continuation marks.',places='final Drap display'),
 dict(form=r'I_{\cdot>\alpha}, I_{\cdot>i_p}',meaning_or_shape='Distinct dummy point before greater-than; alpha in the old draft and i_p in the replacement.',places='last old formula and right insertion')
]
D['abbreviations'] = [
 dict(form='corresp.',expansion='correspond / correspondance, according to its two sentence positions; not expanded in transcription'),
 dict(form='=',expansion='même in the verbal lui constructions'),
 dict(form='hyp.',expansion='hypothèse (tentative expansion; literal abbreviation retained)'),
 dict(form='il f. et s.',expansion='il faut et suffit'),
 dict(form='ds',expansion='dans'),
 dict(form='ssi',expansion='si et seulement si'),
 dict(form="s’ident",expansion="s’identifie / s’identifient (the written body itself remains doubtful)"),
 dict(form='i.e.',expansion='id est'),
 dict(form="l’ens",expansion="l’ensemble; no stop supplied")
]
D['hand_log'] = [
 dict(habit='Two-bar equality can replace verbal même and can follow a hyphen.',places='047 cancelled lui groups, lines 2–3',consistent='Both current instances have two separate bars; first has no preceding hyphen, second has one.',witness_errors='H expands both to même; C doubts the first and reads the second as mê.'),
 dict(habit='Empty-set notation has a small phi-like loop and a long crossing stem.',places='047 opening pair',consistent='Both current symbols agree with the local phi shape, confirmed from their own ink.',witness_errors='C and H normalize to varnothing/emptyset.'),
 dict(habit='A serif capital I may have a detached cap, and a small lower index can attach close to its foot.',places='047 first interval and final three intervals',consistent='Serif I is consistent across these occurrences; no J is inferred from a hooked foot.',witness_errors='None established for I/J on this page.'),
 dict(habit='Small i can be attached to the Sigma foot while its dot remains separate before a descending j.',places='047 Sigma_ij in the two connectors and in contenu(s) ds Sigma_ij',consistent='All inspected ij pairs have the short i/dot plus longer j.',witness_errors='H drops i in the contenu(s) expression.'),
 dict(habit='Continuation marks vary locally in number and shape.',places='047 first Drap interval, two short tuples, live d-prime-zero tuple, final display',consistent='They are not uniform: empty middle, one dash, point+dash, and two strokes+point all occur.',witness_errors='Both witnesses supply a dot in the first Drap; H normalizes tuple continuations; C miscounts/misforms two later groups.'),
 dict(habit='One lower crossed bar in a strict inclusion is distinct from the curved bottom of the subset body.',places='047 d subset d-prime and d-double-prime superset d-prime',consistent='Both strict signs have one separate lower bar.',witness_errors='C uses subsetneqq/supsetneqq, adding a second lower-bar reading.'),
 dict(habit='Very short arrow endpoint returns can remain ambiguous; clear hooks must be read independently.',places='047 live Sigma_ij connector and the two cylinder inclusions',consistent='The first live connector remains doubtful; both cylinder arrows have distinct hooks and heads.',witness_errors='H changes the cancelled headless dash to an arrow and omits the first cylinder hook.'),
 dict(habit='Crossing strokes can coincide with an entire low cursive word body, leaving only ascenders, descenders and points.',places='047 lower cancelled draft, si group, alors/donc group, formé and finis',consistent='Strict uncertainty is retained where not every letter can be recovered.',witness_errors='Several C/H word differences remain open rather than being settled grammatically.'),
 dict(habit='Short forms retain stops only where visible.',places='047 corresp. twice, ds, l’ens, hyp.',consistent='Separate stop after each corresp. and hyp.; none supplied after ds or l’ens.',witness_errors='H expands corresp. and ds, and omits l’ens in the lower insertion.')
]

top = T[T.index(r'\deleted{\uline{privé}'):T.index('élément (pour être fibré')].strip()
live_and_intro = T[T.index('élément (pour être fibré'):T.index(r"$\Sigma_{d''}$ où")].strip()
middle = T[T.index(r"$\Sigma_{d''}$ où"):T.index(' contenant ')].strip()
bottom_text = T[T.index('contenant '):T.index('\\[')].strip()
display = T[T.index('\\['):T.index('\\]')+2]

def box(label,kind,xy,reading,reason):
    D['second_boxes'].append(dict(box=label,kind=kind,coords=xy,reading=reading,reason=reason))

box('b01','handwritten number|margin note',[60,35,145,115],r'\mspage{19}',
    'Complete dark upper-left sheet number; no surrounding prose lies inside this box.')
box('b02','struck passage|insertion|margin note|doubt formula|C/H word difference|low-confidence departure',[220,25,1682,600],top,
    'All six cancelled opening rows and the cancelled underlined margin insertion, including both whole verbal-equality expressions, the phi pair, the whole doubtful C notation, maximal and every top C/H word difference. The 19 lies outside this box and has b01.')
box('b03','insertion|doubt formula|C/H word difference|low-confidence departure',[250,594,1680,1354],live_and_intro,
    'Complete live first paragraph with contenu(s), ds, s’ident, donc, raised equivalence and both whole Drap/connector formulas; also the complete following introduction through par les, including the strict initial-segment relation and the clear first fibration.')
box('b04','struck passage|insertion|doubt formula|handwritten number|C/H word difference|low-confidence departure',[270,1356,1680,2110],middle,
    'One coherent large block is needed because the interlinear insertions, cancellations and frame overlap. It includes every word wholly within the block, all three cylinder-related maps, cancelled alpha, si insertion and deletion, both tuples, the live decomposition and avec line, all three lower cancelled rows, the entire frame/loop, and the complete right replacement. Numeric 0,1,2 in the formulas and all proposed doubtful formulas are included whole. The next contenant line is not wholly inside this box.')
box('b05','struck passage|insertion|doubt formula|handwritten number|C/H word difference|low-confidence departure',[280,2095,1680,2231],bottom_text,
    'Complete two-line continuation beginning contenant, including the cancelled d_0/les group, all zero indices, the cancelled c’est donc un group, and the whole lower insertion through est en; concludes with corresp. biunivoque avec. Earlier frame/formula fragments and the beginning of the display are not complete content in this box.')
box('b06','struck passage|doubt formula|handwritten number|low-confidence departure',[295,2205,1665,2315],display,
    'The entire final Drap formula, including its cancelled internal close, every index and numerical digit, the three genuine dummy dots, and the exact mixed continuation marks. No fragment-only reading of the internal close or individual index is used.')
box('b07','handwritten number|margin note|low-confidence departure',[12,2288,90,2355],r'\margin{46}',
    'Complete thin lower-left foliation; attribution is uncertain, though the two digits are legible.')

D['crop_register'] = [dict(crop=f'150_scan047_{name}.jpg',box=xy,rotation_degrees=0,actually_viewed=True) for name,xy in coords.items()]
D['crop_counts'] = dict(distinct_places=35,saved_images=36,reason_for_extra='The first lui/dash crop clipped the next word; lui_dash_complete extends its context and confirms the dash count.')
D['coverage'] = dict(whole_page_views=1,native_top_views=1,native_bottom_views=1,all_agreed_tokens_read=True,all_deleted_and_inserted_spans_read=True,all_crops_actually_viewed=True,other_pages_read=False,ocr_used=False,second_reading_started=False,tex_compiled=False,mathematical_checks_performed=False)

def tex_braces_balanced(s):
    level=0
    for i,c in enumerate(s):
        if c not in '{}': continue
        j=i-1
        while j>=0 and s[j]=='\\': j-=1
        if (i-j-1)%2: continue
        level += 1 if c=='{' else -1
        if level<0: return False
    return level==0

def extract_marks(s):
    result=[]
    for m in re.finditer(r'\\(?:unsure|illegible)\{',s):
        lev=1; j=m.end()
        while lev:
            if s[j] in '{}':
                k=j-1
                while k>=0 and s[k]=='\\': k-=1
                if (j-k-1)%2==0: lev += 1 if s[j]=='{' else -1
            j+=1
        result.append(s[m.start():j])
    return result

assert tex_braces_balanced(T), 'Unbalanced TeX braces'
assert sorted(extract_marks(C)) == sorted(x['mark'] for x in D['marks']), 'Missing original C mark'
assert len(D['crop_register'])==36
for item in D['crop_register']:
    assert (BASE/'crops'/item['crop']).exists(), item['crop']
for item in D['second_boxes']:
    assert tex_braces_balanced(item['reading']), ('box braces',item['box'])
    assert 'PLACEHOLDER' not in item['reading']
allowed = {'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(x['kind'] in allowed for x in D['changes'])
assert all(x['change_C'] or x['change_H'] for x in D['changes'])
D['counts'] = dict(substantive_rows=len(D['changes']),change_C=sum(x['change_C'] for x in D['changes']),change_H=sum(x['change_H'] for x in D['changes']),original_C_marks=len(D['marks']),inventory_elements=len(D['inventory']),doubts=len(D['doubts']),second_boxes=len(D['second_boxes']))
D['validation'] = dict(all_C_quotes_source_exact=True,all_H_quotes_source_exact=True,H_explicit_note_readings_counted_as_evidence=True,all_final_change_readings_present_in_tex=True,all_original_C_marks_accounted_for=True,tex_braces_balanced=True,all_crop_paths_exist=True,audit_readings_literal_tex=True)
(BASE/'reader_returns/150_scan047.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(D['counts'],ensure_ascii=False))


