from pathlib import Path
import json

root = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
out = root / 'edition/reader_reports'
out.mkdir(parents=True, exist_ok=True)
crop_boxes = json.loads((root / 'edition/crops/145_scan017_crop_boxes.json').read_text())
crop_keys = {int(k.split('_')[2]): k for k in crop_boxes}

def crop(n):
    key = crop_keys[n]
    return {'crop': 'crops/' + key + '.png', 'box': crop_boxes[key]}

tex = r'''\scanpage{17}
\mspage{7}
Le groupe fondamental mixte est défini à la Malgoire, \deleted{\unsure{correspondant|comprenant}} les classes $(\gamma,\unsure{l|\lambda})$ d'un $\gamma\in\Gamma$ et d'une classe de chemins $l$/de $P$ dans $\gamma^{-1}(P)$, en définissant
\[
(\gamma,l)(\gamma',l')=(\inserted{\gamma\gamma',}\gamma'^{-1}(l)\circ l')
\]
i.e. ``composant les chemins comme des fonctions'' (c'est la convention pour faire opérer \uline{à gauche} le groupoïde fondamental sur les fibres d'un rev. étale \inserted{$U'$}, à une classe de chemins $l$ de $x$ à $y$ étant associé $l_\bullet:U'_{\unsure{a|x}}\longrightarrow U'_y\ldots$)

On choisit des éléments
\[
\sigma_0,\sigma_1,\sigma_\infty\qquad\text{sur}\qquad\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty
\]
comme les couples d'un $\sigma_i$, et des chemins \inserted{$\lambda_i$} de $P$ à $\bar P=\sigma_iP$ qui se fait sur \deleted{l'unique} \inserted{celui des} demi-grands cercles de $P$ à $\bar P$, \deleted{stable par \unsure{à} la symétrie} \inserted{ens. des pts fixes} \deleted{$\tau\sigma_i$} de la symétrie $\dot\tau\dot\sigma_i=\dot\sigma_i\dot\tau$ (symétrie p.r. \unsure{au|à} plan, fixant $P,\bar P,a_i$ $(=0,1\text{ ou }\infty)$ et échangeant les deux autres $a_j,a_k$), et \unsure{ne|un} passant pas par $a_i$. \deleted{\unsure{Au}} Désignant par $l_0,l_1,l_\infty$ \inserted{(pour $1\in\Gamma$)} les lacets en sens direct autour des $0,1,\infty$ à partir de $P$, en allant vers $\unsure{a_0,a_1,a_\infty|0,1,\infty}$ suivant des des quarts de grands cercles, on trouve
\[
(1)\qquad\big|\quad l_\infty\unsure{l'_1|l_1}l_0=1
\]
(et non $l_0l_1l_\infty=1$ ! \unsure{?} On peut l'écrire $l_0^{-1}l_1^{-1}l_\infty^{-1}=1$)
et les relations
\mspage{16}
'''

changes = []
def change(n, place, C, H, final, ink, confidence, kind, cc, hc, marked, cr, cats, math='', **extra):
    assert cc or hc
    changes.append(dict(id=f's017-{n:02d}', place=place, C=C, H=H, final=final,
        ink=ink, confidence=confidence, kind=kind, c_changed=cc, h_changed=hc,
        marked_in_H=marked, **crop(cr), error_category=cats, math_consequence=math, **extra))

change(1, 'Opening paragraph, first tuple', r'$(\gamma,l)$', r'$(\gamma, \lambda)$', r'$(\gamma,\unsure{l|\lambda})$',
    'The second sign has a tall closed upper loop and a rightward lower foot, favouring l; a left branch and retracing leave lambda possible. The plain l in the product has the same loop-and-foot structure without this extra branch.',
    'medium', 'misread symbol or index', False, True, 'yes', 2, [1], 'The path-component symbol remains locally uncertain; no global identification is imposed.')
change(2, 'Opening paragraph, line beginning l/de P', r'$l$ de $P$', r'$l$/de $P$', r'$l$/de $P$',
    'A long separate oblique stroke curves down-left immediately after l and before de. It is not part of the l loop and has no dot. Its precise separator function is not inferred.',
    'high', 'omission', True, False, 'no', 3, [3])
change(3, 'Product display, first component on right', r"(\inserted{\gamma\gamma',}\gamma'^{-1}(l)\circ l')", r"\bigl(\gamma\gamma',\; \gamma'^{-1}(l) \circ l'\bigr)", r"(\inserted{\gamma\gamma',}\gamma'^{-1}(l)\circ l')",
    'Gamma gamma-prime and its comma sit above the line of gamma-prime inverse(l); the opening parenthesis is prolonged upwards around the addition.',
    'high', 'insertion or placement', False, True, 'yes', 4, [6], 'Retains the authorial addition of the group component.')
change(4, 'Quotation around composant les chemins comme des fonctions', "``composant les chemins comme des fonctions''", '« composant les chemins comme des fonctions »', "``composant les chemins comme des fonctions''",
    'Both ends have two short high strokes; no paired angle forms are present.',
    'high', 'other', False, True, 'no', 5, [10])
change(5, 'Explanatory paragraph, emphasis at à gauche', r'à \uline{gauche}', 'à gauche', r'\uline{à gauche}',
    'The horizontal underline starts under the preceding à, well to the left of the g descender, and runs beneath the complete phrase. It is separate from that descender.',
    'high', 'other', True, True, 'no', 6, [10])
change(6, 'After rev. étale', r"\inserted{$U'$}", r"$U'/U$", r"\inserted{$U'$}",
    'A single U-prime is interlinear. A long curved placement stroke descends from it to the comma after étale; no second U appears below that stroke.',
    'high', 'insertion or placement', False, True, 'no', 7, [6, 9], 'Does not add a denominator or base U to the covering notation.')
change(7, 'Inline fibre map, symbol before colon', r'l:', r'l_* :', r'l_\bullet:',
    'A filled low point stands immediately after the l foot. Farther right are the two separate points of the colon. The low point has no distinguishable asterisk arms, so the literal dot is retained.',
    'high', 'misread symbol or index', True, True, 'no', 8, [1, 3], 'Preserves a visible low mark on the path-induced map without supplying an asterisk.')
change(8, 'Inline fibre map, first fibre subscript', r"U'_x", r"U'_x", r"U'_{\unsure{a|x}}",
    'The small subscript is an oval with a descending right stroke, more a-like than crossed x. At this size a retraced x cannot be excluded; the earlier prose variable is not used to normalize it.',
    'low', 'misread symbol or index', True, True, 'no', 8, [1], 'Potential mismatch between the prose endpoint x and the written fibre label is left visible.')
change(9, 'End of first explanatory parenthesis', r"U'_y\ldots$).", r"U'_y$ …)", r"U'_y\ldots$)",
    'Three low ellipsis points occur before the long closing parenthesis. The area immediately after that parenthesis is blank; no additional full stop is present.',
    'high', 'text not on the page', True, False, 'no', 8, [9])
change(10, 'Display after On choisit des éléments', r'\sigma_0,\sigma_1,\sigma_\infty\quad\text{sur}\quad\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty', r'\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty\quad\text{sur}\quad\sigma_0,\sigma_1,\sigma_\infty', r'\sigma_0,\sigma_1,\sigma_\infty\quad\text{sur}\quad\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty',
    'Each right-hand sigma has an isolated point above its roof. None of the three left-hand sigmas has such a point; the dark end of the left infinity-indexed sigma roof remains on the roof.',
    'high', 'misread symbol or index', False, True, 'no', 9, [1], 'The displayed elements lie over the dotted symbols, in the written order.')
change(11, 'After comme les couples d’un sigma_i', 'et des chemins', 'et du chemin/des chemins', 'et des chemins',
    'After et there is one word with a d loop and terminal s, followed directly by chemins. No separate du chemin or slash is written.',
    'high', 'text not on the page', False, True, 'no', 10, [2, 9])
change(12, 'Above chemins before de P', r'\inserted{$\lambda_i$}', '', r'\inserted{$\lambda_i$}',
    'The interlinear lambda with its low i is joined by a curved placement stroke to the gap between chemins and de. The native half supplied the highest tip clipped at the upper edge of crop10.',
    'high', 'omission', False, True, 'no', 10, [3, 6], 'Retains the names of the chosen paths.')
change(13, 'After qui se fait sur', r"\deleted{l'unique} \inserted{celui des}", r'\struck{\ill{}} celui des', r"\deleted{l'unique} \inserted{celui des}",
    'The crossed word has a tall l, apostrophe, u/n minims, i, large q loop and descender, and ending ue. The clearly separate words celui des sit above the horizontal cancellation.',
    'high', r'readable ink left as \ill{}', False, True, 'yes', 12, [5, 6, 7])
change(14, 'Cancelled phrase after grands cercles de P à P-bar', r'\deleted{stable par la symétrie}', r'\struck{\ill{}}', r'\deleted{stable par \unsure{à} la symétrie}',
    'The cancellation crosses stable, par, la, and symétrie. Between par and la there is an additional isolated low loop with a short upper accent-like stroke, plausibly à; its precise letters remain obscured by the cancellation and overlap.',
    'medium', 'deletion state', True, True, 'yes', 13, [3, 5, 7])
change(15, 'Interlinear replacement over cancelled stable phrase', r'\inserted{\unsure{ens. des pts fixes}}', 'qui est fixé par la symétrie', r'\inserted{ens. des pts fixes}',
    'The upper line reads ens. (with an explicit following stop), des, pts, fixes. The abbreviated pts has a low p stem and compact t/s strokes. There is no independent live qui est fixé. Tall upper tips were read on the native half before the crop was made.',
    'high', 'insertion or placement', False, True, 'yes', 13, [2, 6], 'Preserves the author’s fixed-point-set description and abbreviations.')
change(16, 'Beginning of de la symétrie line', r'\deleted{$\tau\sigma_i$}', '', r'\deleted{$\tau\sigma_i$}',
    'A horizontal cancellation crosses tau and sigma; the sigma subscript i remains below. No over-dots are visible on this cancelled pair.',
    'high', 'omission', False, True, 'no', 14, [3, 7])
change(17, 'Live symmetry commutation formula', r'\dot\tau\dot\sigma_i=\dot\sigma_i\dot\tau', r'\tau\sigma_i=\sigma_i\tau', r'\dot\tau\dot\sigma_i=\dot\sigma_i\dot\tau',
    'Four separate high points occur, one for each tau/sigma, with the i indices lower and distinct. The equals sign has two short horizontal strokes.',
    'high', 'misread symbol or index', False, True, 'no', 14, [1], 'Keeps the formula on the dotted symmetries.')
change(18, 'Description of the plane', ', fixant', 'passant par', ', fixant',
    'A comma follows plan. The next word has a tall f, small i, crossed x, and the remaining ant strokes; there is no separate par after it.',
    'high', 'misread word', False, True, 'no', 15, [2])
change(19, 'Parenthesis naming a_i', r'(=0,1\text{ ou }\infty)', r'(=0,1\ldots\infty)', r'(=0,1\text{ ou }\infty)',
    'Between the upright 1 and the two-loop infinity sign there is a small oval/dot followed by a continuous shallow u-like stroke, not a row of separate ellipsis points.',
    'medium', 'misread word', False, True, 'no', 16, [2])
change(20, 'End of symmetry description and next line beginning', r'\unsure{ne} passant pas par $a_i$', r'\uncertain{un} \ill{} \uncertain{pour $1(-1)$}', r'\unsure{ne|un} passant pas par $a_i$',
    'The compressed short word before passant favours ne but does not fully distinguish un. Passant has a deep p and tall final t; the next line plainly begins pas par a_i. The interlinear pour parenthesis belongs with the subsequent lacet labels.',
    'medium', 'misread word', False, True, 'yes', 17, [2, 3, 6], 'The negative wording is preserved with a local uncertainty on ne.', additional_crops=[crop(18)])
change(21, 'Cancelled short word before Désignant', r'\deleted{\unsure{Au}}', r'\struck{\ill{}}', r'\deleted{\unsure{Au}}',
    'The large crossed initial has an A-like triangular structure followed by a low u-like return. Multiple cancelling strokes entangle its centre, so Au is retained as a doubtful rather than fully recovered reading.',
    'medium', r'readable ink left as \ill{}', False, True, 'yes', 18, [5, 7])
change(22, 'Insertion linked after l_0,l_1,l_infty', r'\inserted{(pour $1\in\Gamma$)}', r'\uncertain{pour $1(-1)$}', r'\inserted{(pour $1\in\Gamma$)}',
    'The small parenthesis reads pour, an upright 1, membership sign with its middle stroke, and an angular Gamma with a left stem and right roof. Its curved connector runs to the place after the three l labels, before les.',
    'high', 'insertion or placement', False, True, 'yes', 17, [1, 6], 'Retains the identity element in Gamma as the insertion states.', additional_crops=[crop(18)])
change(23, 'H’s duplicated lacet sentence', '', r"les lacets \struck{\ill{}} par $a_i$. Désignant par $l_0,l_1,l_\infty$", '',
    'The native lower half has one continuous pas par a_i followed by the short cancelled word and one Désignant par l_0,l_1,l_infty. There is no earlier les lacets or repeated Désignant clause. Crop18 shows the sole transition; crop17 shows the insertion causing the apparent overlap.',
    'high', 'text not on the page', False, True, 'yes', 18, [9], additional_crops=[crop(17)])
change(24, 'Lacets around the three marked points', r'autour des $0,1,\infty$', r'autour de $0,1,\infty$', r'autour des $0,1,\infty$',
    'The short word after autour has a d loop and a clear dark terminal s hook before the separate zero.',
    'high', 'misread word', False, True, 'no', 19, [2])
change(25, 'Retraced labels after en allant vers', r'0,1,\infty', r'0,1,\infty', r'\unsure{a_0,a_1,a_\infty|0,1,\infty}',
    'All three clusters contain a distinct low a-like loop overlapping the nominal numeral or infinity strokes. The middle cluster has a dark crossing under its upright 1, and the first and third have doubled round strokes. The order of overwriting cannot be separated securely, so no deleted layer is invented.',
    'low', 'misread symbol or index', True, True, 'no', 21, [1], 'The destinations remain uncertain between a-indexed labels and the bare three values.')
change(26, 'Line break between suivant des and des quarts', 'suivant des', 'suivant des', 'suivant des des',
    'Crop25 shows suivant followed by a complete des at the preceding line end. Crop20 begins with another d loop, e connection, and terminal s before quarts. Both copies are written and neither is cancelled.',
    'high', 'omission', True, True, 'no', 25, [3], '', additional_crops=[crop(20)])
change(27, 'Before de grands cercles', r'\unsure{quarts}', 'segments', 'quarts',
    'The initial q has a descending loop, followed by u/a/r strokes and a tall crossed t before terminal s. There is no opening s or medial g descender to support segments.',
    'high', 'misread word', False, True, 'no', 20, [2], 'Retains the stated quarter-circle description.')
change(28, 'Numbered relation, vertical mark after (1)', r'(1)\qquad\big|\quad', r'(1)\qquad', r'(1)\qquad\big|\quad',
    'A long independent vertical stroke stands between the number and the first l factor. It is not an opening parenthesis or part of l_infty.',
    'high', 'omission', False, True, 'no', 22, [3])
change(29, 'Numbered relation, factor before l_0', r'l_1', r'l_1', r"\unsure{l'_1|l_1}",
    'A short dark upright tick is separate from the next l_0 upper loop and lies high to the right of the l_1 factor. It could be a prime; whether it is an intended modifier or a stray mark cannot be determined.',
    'low', 'misread symbol or index', True, True, 'no', 22, [1, 3], 'A possible prime in the displayed relation is preserved; no algebraic normalization is made.')
change(30, 'Parenthesis after ! and the doubtful intervening mark', r"\unsure{?} On peut l'écrire", r"\uncertain{Voir} par l'écriture", r"\unsure{?} On peut l'écrire",
    'The clause has a large O joined to n, a low p with long descender followed by eut, and l apostrophe écrire. The preceding looped vertical mark remains doubtful and is not read as the V of Voir.',
    'high', 'misread word', False, True, 'yes', 23, [2], 'Preserves the author’s wording introducing the inverse-product relation.')
change(31, 'Lower left handwritten number', r'\mspage{16}', '', r'\mspage{16}',
    'The lower-left ink consists of a long sloping entry and upright 1, followed by an open rising stem closing into the lower loop of 6.',
    'high', 'omission', False, True, 'no', 24, [3])

decisions = []
def decision(id, which, reading, ink, cr, confidence):
    decisions.append(dict(id=id, decision=which, reading=reading, ink=ink, **crop(cr), confidence=confidence))
decision('M0818','first',r'\sigma_i','The roof has no detached point above it. The small mark beneath its right side belongs to the index i.',10,'high')
decision('M0819','first',r'\sigma_i','The sigma after the equals sign has no high point; the visible point is immediately over its low index i.',11,'high')
decision('M0820','first','ens. des pts fixes','The upper line has ens followed by a separate stop, des, compact pts, and fixes. Native-half reading supplied tall upper tips clipped by crop13; no abbreviation is expanded.',13,'high')
decision('M0821','undecided',r'\unsure{au|à}','An upper accent-like stroke is clear above the initial closed loop; the low continuation might contain a u or be only the exit stroke of à.',15,'medium')
decision('M0822','undecided',r'\unsure{ne|un}','A short arch followed by a nearly flat e-like continuation favours ne, but the compressed two-letter sequence does not safely exclude un.',17,'medium')
decision('M0823','first','quarts','The q descender and tall t with its cross stroke distinguish quarts from H segments.',20,'high')
decision('M0824','undecided',r'\unsure{?}','The intervening sign has an upper loop, an elongated middle stroke, and a lower fork/return; a normal separated question-mark dot is not plain.',23,'low')
unlisted = [
    dict(id='U017-01', source_mark=r'\deleted{\unsure{comprenant|correspondant}}', decision='undecided', reading=r'\deleted{\unsure{correspondant|comprenant}}', ink='A late deep descender and long sequence of low minims favour correspondant. Cancellation masks enough of the middle that every letter cannot be recovered; the choice remains open.', **crop(1), confidence='low'),
    dict(id='U017-02', source_mark=r'\deleted{\unsure{Au}}', decision='undecided', reading=r'\deleted{\unsure{Au}}', ink='The large initial is A-like and a following low return is u-like, but repeated cancellation intersects the letter skeletons.', **crop(18), confidence='medium')
]

doubts = [
    dict(place='Initial cancelled word after Malgoire',reading=r'\deleted{\unsure{correspondant|comprenant}}',alternatives=['correspondant','comprenant'],confidence='low',reason='Middle letters are crossed; the late descender favours the first reading but does not establish every letter.'),
    dict(place='Initial tuple second component',reading=r'\unsure{l|\lambda}',alternatives=['l',r'\lambda'],confidence='medium',reason='Tall upper loop favours l; anomalous left branch and retracing permit lambda.'),
    dict(place='First fibre subscript in the inline map',reading=r"U'_{\unsure{a|x}}",alternatives=['a','x'],confidence='low',reason='Oval with right downstroke favours a; the small retraced shape does not safely exclude x.'),
    dict(place='Within cancelled stable phrase, between par and la',reading=r'\unsure{à}',alternatives=['à','unidentified crossed short word or overlapping strokes'],confidence='low',reason='Separate low loop and upper accent-like stroke are real, but cancellation prevents full recovery.'),
    dict(place='p.r. ... plan',reading=r'\unsure{au|à}',alternatives=['au','à'],confidence='medium',reason='Upper accent visible; terminal continuation may be u or an exit stroke.'),
    dict(place='Before passant',reading=r'\unsure{ne|un}',alternatives=['ne','un'],confidence='medium',reason='Compressed pair favours ne but its individual letters are not fully separable.'),
    dict(place='Cancelled word before Désignant',reading=r'\deleted{\unsure{Au}}',alternatives=['Au','partly illegible cancelled short word'],confidence='medium',reason='A-like initial and u-like ending remain crossed and entangled.'),
    dict(place='Destination list after en allant vers',reading=r'\unsure{a_0,a_1,a_\infty|0,1,\infty}',alternatives=[r'a_0,a_1,a_\infty',r'0,1,\infty'],confidence='low',reason='All three forms are retraced with a-like loops; the separate before/after states cannot be securely recovered.'),
    dict(place='Middle factor in relation (1)',reading=r"\unsure{l'_1|l_1}",alternatives=[r"l'_1",r'l_1'],confidence='low',reason='A separate high tick can be a prime, but an incidental mark remains possible.'),
    dict(place='Between ! and On peut l’écrire',reading=r'\unsure{?}',alternatives=['?','unidentified looped mark'],confidence='low',reason='Loop and descending/forked stroke do not form a fully plain ordinary question mark.'),
]

inventory=[]
def inv(n,kind,pos,first,box):
    inventory.append(dict(element=f'E{n:02d}',kind=kind,position=pos,first_words_or_objects=first,box=box,sheet_kind='text',hand='his hand',transcribed='yes'))
inv(1,'text','Top centre manuscript number','7',[916,8,996,82])
inv(2,'text','Opening paragraph, four manuscript lines','Le groupe fondamental mixte est défini à la Malgoire',[230,70,1654,398])
inv(3,'deletion','Opening paragraph after Malgoire',r'\unsure{correspondant|comprenant}',crop(1)['box'])
inv(4,'display','Upper product definition',r"(\gamma,l)(\gamma',l')=",[350,380,1005,515])
inv(5,'insertion','Above first right component of product',r"\gamma\gamma',",[686,384,752,450])
inv(6,'text','Explanatory paragraph, five lines','i.e. ``composant les chemins comme des fonctions\'\'', [245,490,1655,950])
inv(7,'text','Underline in explanatory paragraph',r'\uline{à gauche}',crop(6)['box'])
inv(8,'insertion','Above étale, with descending placement stroke',r'U\prime',[719,737,799,866])
inv(9,'display','Inline fibre map at end of explanatory paragraph',r"l_\bullet:U'_{\unsure{a|x}}\longrightarrow U'_y\ldots",[1107,815,1658,950])
inv(10,'text','Short introduction above sigma display','On choisit des éléments',[243,986,961,1080])
inv(11,'display','Sigma lists around sur',r'\sigma_0,\sigma_1,\sigma_\infty sur \dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty',[526,1048,1292,1165])
inv(12,'text','Long path-selection and lacet paragraph','comme les couples d\'un',[244,1168,1665,2162])
inv(13,'insertion','Above chemins, before de P',r'\lambda_i',[1483,1110,1625,1235])
inv(14,'deletion','After qui se fait sur',"l'unique",[1113,1275,1410,1388])
inv(15,'insertion','Above cancelled l’unique','celui des',[1113,1220,1405,1290])
inv(16,'deletion','After grands cercles de P à P-bar',r'stable par \unsure{à} la symétrie',[931,1367,1566,1460])
inv(17,'insertion','Above cancelled stable phrase','ens. des pts fixes',[1013,1300,1566,1390])
inv(18,'deletion','Beginning of the next line',r'\tau\sigma_i',[245,1490,375,1557])
inv(19,'display','Inline live symmetry relation',r'\dot\tau\dot\sigma_i=\dot\sigma_i\dot\tau',[913,1452,1240,1561])
inv(20,'insertion','Interlinear right edge, linked after lacet triple',r'(pour $1\in\Gamma$)',[1455,1660,1665,1832])
inv(21,'deletion','Between pas par a_i. and Désignant',r'\unsure{Au}',[643,1745,733,1835])
inv(22,'display','Retraced point labels in the prose',r'\unsure{a_0,a_1,a_\infty|0,1,\infty}',crop(21)['box'])
inv(23,'text','Repeated word at successive line end and beginning','suivant des des quarts',[245,1930,1665,2152])
inv(24,'display','Relation (1) and independent left vertical stroke',r"(1)\quad\big|\quad l_\infty\unsure{l'_1|l_1}l_0=1",[491,2110,1012,2224])
inv(25,'text','Parenthetical correction/exclamation and inverse relation','(et non ... ! ... On peut l\'écrire ...)',[240,2138,1600,2296])
inv(26,'display','Final inline inverse-product formula',r'l_0^{-1}l_1^{-1}l_\infty^{-1}=1',[1260,2138,1585,2262])
inv(27,'text','Final continuation line','et les relations',[245,2260,716,2350])
inv(28,'text','Lower-left handwritten number','16',crop(24)['box'])

second=[]
def sb(n,kind,coords,reading):
    second.append(dict(box=f'B{n:02d}',kind=kind,coords=coords,reading=reading))
sb(1,'handwritten manuscript number',[916,8,996,82],r'\mspage{7}')
sb(2,'cancelled C doubt; lexical disagreement',crop(1)['box'],r'\deleted{\unsure{correspondant|comprenant}}')
sb(3,'complete first tuple and Gamma membership; symbol disagreement',crop(2)['box'],r"$(\gamma,\unsure{l|\lambda})$ d'un $\gamma\in\Gamma$")
sb(4,'visible slash and complete inverse endpoint formula',crop(3)['box'],r'$l$/de $P$ dans $\gamma^{-1}(P)$,')
sb(5,'complete product formula; interlinear insertion and handwritten inverse exponent',[350,380,1005,515],r"$(\gamma,l)(\gamma',l')=(\inserted{\gamma\gamma',}\gamma'^{-1}(l)\circ l')$")
sb(6,'quotation punctuation disagreement',crop(5)['box'],"i.e. ``composant les chemins comme des fonctions''")
sb(7,'underline scope disagreement',crop(6)['box'],r'\uline{à gauche}')
sb(8,'interlinear U-prime insertion and unsupported /U in H',crop(7)['box'],r"d'un rev. étale \inserted{$U'$}, à")
sb(9,'complete doubtful fibre-map formula and end punctuation',[1107,815,1658,950],r"$l_\bullet:U'_{\unsure{a|x}}\longrightarrow U'_y\ldots$)")
sb(10,'complete sigma display with all numeric indices, first C sigma doubt, and path-label insertion',[238,986,1645,1240],r"On choisit des éléments \[\sigma_0,\sigma_1,\sigma_\infty\qquad\text{sur}\qquad\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty\] comme les couples d'un $\sigma_i$, et des chemins \inserted{$\lambda_i$} de")
sb(11,'second C sigma doubt; complete endpoint formula; cancellation and replacement',[242,1220,1658,1384],r"$P$ à $\bar P=\sigma_iP$ qui se fait sur \deleted{l'unique} \inserted{celui des} demi-")
sb(12,'cancelled phrase with newly noticed doubtful word and interlinear abbreviated replacement',[900,1300,1648,1460],r'\deleted{stable par \unsure{à} la symétrie} \inserted{ens. des pts fixes}')
sb(13,'cancelled pair and complete live dotted commutation formula',[244,1440,1663,1580],r'\deleted{$\tau\sigma_i$} de la symétrie $\dot\tau\dot\sigma_i=\dot\sigma_i\dot\tau$ (symétrie')
sb(14,'C preposition doubt, lexical disagreement, all point labels and parenthetical handwritten values',[245,1530,1665,1668],r'p.r. \unsure{au|à} plan, fixant $P,\bar P,a_i$ $(=0,1\text{ ou }\infty)$ et')
sb(15,'complete negative passage, cancelled C doubt, lacet labels and identity insertion; H duplication',[244,1618,1666,1850],r'échangeant les deux autres $a_j,a_k$), et \unsure{ne|un} passant pas par $a_i$. \deleted{\unsure{Au}} Désignant par $l_0,l_1,l_\infty$ \inserted{(pour $1\in\Gamma$)} les')
sb(16,'lexical des/de disagreement and full handwritten list',[240,1830,1665,1948],r'lacets en sens direct autour des $0,1,\infty$ à partir')
sb(17,'complete retraced doubtful label group and following repeated-word first occurrence',[244,1930,1665,2048],r'de $P$, en allant vers $\unsure{a_0,a_1,a_\infty|0,1,\infty}$ suivant des')
sb(18,'C quarts doubt; lexical segments disagreement; repeated-word second occurrence',[244,2044,1665,2162],r'des quarts de grands cercles, on trouve')
sb(19,'complete numbered relation including all handwritten numbers, vertical stroke and possible prime',[491,2110,1012,2224],r"$(1)\qquad\big|\quad l_\infty\unsure{l'_1|l_1}l_0=1$")
sb(20,'complete parenthetical formulas, doubtful authorial mark and lexical clause disagreement; all inverse exponents',[240,2138,1600,2296],r"(et non $l_0l_1l_\infty=1$ ! \unsure{?} On peut l'écrire $l_0^{-1}l_1^{-1}l_\infty^{-1}=1$)")
sb(21,'handwritten lower-left number',crop(24)['box'],r'\mspage{16}')

coverage=[]
def cov(row,status,ids=None,explanation=''):
    v=dict(row=row,status=status)
    if ids:
        v['change_id']=f's017-{ids[0]:02d}'
        if len(ids)>1:v['related_change_ids']=[f's017-{i:02d}' for i in ids[1:]]
    if explanation:v['explanation']=explanation
    coverage.append(v)
cov(1,'macro/editorial',explanation='C scanpage17 versus H editorial page-header tokens; both identify handwritten7, which is separately inventoried.')
cov(2,'macro/editorial',explanation='H editorial de l’auteur has no manuscript content.')
cov(3,'macro/editorial',explanation='Choice-alternative tokenization. The cancelled word remains undecided in U017-01 and doubts; no certainty-only error is counted.')
cov(4,'substantive',[1])
cov(5,'substantive',[2])
cov(6,'macro/editorial',explanation='H \\; is TeX spacing, not a written semicolon. Actual interlinear γγ′ placement is recorded at s017-03.')
cov(7,'substantive',[4])
cov(8,'substantive',[4])
cov(9,'substantive',[6])
cov(10,'substantive',[7])
cov(11,'macro/editorial',explanation='C \\ldots and H literal ellipsis represent the same three visible points.')
cov(12,'substantive',[9],explanation='C adds a post-parenthesis full stop; H’s following explanatory note is editorial and excluded. Its insertion observation is reflected in s017-03.')
cov(13,'macro/editorial',explanation='C sigma alternatives: M0818 resolves to undotted sigma_i on crop10; H agrees with the surviving symbol.')
cov(14,'substantive',[11])
cov(15,'substantive',[12])
cov(16,'macro/editorial',explanation='C sigma alternatives: M0819 resolves to undotted sigma_i on crop11; H agrees with the surviving symbol.')
cov(17,'substantive',[13])
cov(18,'substantive',[14,15])
cov(19,'substantive',[14,15,16,17],explanation='Tokenized across the corrected phrase: cancelled words, interlinear fixed-point wording, cancelled tau-sigma pair, and dotted live symmetry formula are separately preserved.')
cov(20,'substantive',[18])
cov(21,'substantive',[19])
cov(22,'substantive',[20,22])
cov(23,'substantive',[21])
cov(24,'substantive',[22,23])
cov(25,'substantive',[22,23])
cov(26,'substantive',[24])
cov(27,'substantive',[27])
cov(28,'substantive',[28])
cov(29,'macro/editorial',explanation='The comma token comes from H math thin space \\,; it is not a written comma.')
cov(30,'macro/editorial',explanation='Joined C tokens versus H thin spacing between factors; the newly observed high tick is separately reported at s017-29.')
cov(31,'macro/editorial',explanation='Joined versus separated math tokens; the factor sequence is the same.')
cov(32,'macro/editorial',explanation='Joined versus separated math tokens; the factor sequence is the same.')
cov(33,'substantive',[30],explanation='On peut l’écrire differs lexically. The intervening manuscript mark remains doubtful under M0824.')
cov(34,'substantive',[31],explanation='The handwritten16 is present and omitted by H. H’s long explanatory note is editorial and supplies no extra manuscript words.')

report=dict(scan=17,reader='reader_b',lines_read=33,
    layout='Upright single-hand text page: 25 principal prose/formula lines, six short interlinear additions, and two handwritten numbers (7 at top,16 at lower left). Three centred displays; several cancelled passages in the middle; no independent drawing or diagram. The vertical mark beside relation(1) is retained as part of its inscription.',
    changes=changes,decisions=decisions,unlisted_decisions=unlisted,doubts=doubts,inventory=inventory,second_boxes=second,
    notation=[
        'On this page Gamma has a left stem and roof with a short right tip, both in the initial membership clause and in the inserted (pour1∈Gamma). No Pi is supplied.',
        'The sigma display is undotted on the left and dotted on the right. The two inline sigma_i after d’un and P-bar= have no over-dot. All four symbols in the live tau/sigma commutation formula have high dots; the cancelled tau-sigma pair has none.',
        'The fibre-map label has a literal filled low dot, separate from its colon. Its intended conventional meaning is not established by the transcription.',
        'A possible prime-like tick beside l_1 in relation(1) is preserved as an alternative. No prime is inferred from the dark end of another letter.',
        'The three destinations after en allant vers are retraced and have a-like loops. Their precise layer sequence is not reconstructed.',
        'The long oblique stroke after the isolated path l is retained as a slash-like separator; its function remains open.'
    ],
    hand=[
        'Tall l loops usually return to a short lower right foot (product display and lacet symbols). The initial tuple sign is anomalously retraced and remains l|lambda; this is not made a universal letter rule.',
        'Small subscript i marks and high operator dots occupy distinct levels in the sigma formulas. H’s reversal of the display and loss of the live over-dots are corrected from those levels.',
        'Long curved placement strokes connect the U-prime and path-label additions with the line below; they are not extra letters or slash-U notation.',
        'Several ascenders and descenders cross adjacent interlinear material. The additional possible cancelled à is recorded separately from the upper replacement text.',
        'Short letter groups, notably au/à and ne/un, are compressed enough to remain local doubts despite intelligible surrounding syntax.'
    ],
    abbreviations=[
        dict(form='i.e.',expansion='id est',place='Introduction of the path-composition explanation'),
        dict(form='rev.',expansion='revêtement',place='d’un rev. étale'),
        dict(form='ens.',expansion='ensemble',place='Interlinear ens. des pts fixes'),
        dict(form='pts',expansion='points',place='Interlinear ens. des pts fixes'),
        dict(form='p.r.',expansion='par rapport',place='Parenthetical description of the symmetry plane')
    ],
    notes=[
        'The author defines the mixed fundamental group through pairs consisting of an element of Gamma and a homotopy class of paths from P to its inverse-translated image. He writes a product with an interlinear Gamma component and explains his convention of composing paths like functions so that the fundamental groupoid acts on the left on étale-cover fibres. These are statements of the manuscript, not independently checked claims.',
        'The second part chooses three elements over dotted symmetries, describes paths via semicircles and fixed-point loci, then introduces direct-oriented loops. The author writes relation(1), rejects the opposite displayed ordering, and supplies an inverse-product expression. The doubtful prime-like tick is left in relation(1), without using the later expression to erase it.',
        'The top handwritten number is7 and the lower-left number is16; no date is written. A looped mark after the exclamation point may be an authorial question mark and remains unsure. The plainly repeated des in suivant des des quarts is retained as an authorial repetition.',
        'Each C deletion was explicitly checked: initial correspondent/comprenant word; l’unique; stable par ... la symétrie; tau-sigma_i; and Au. Each C insertion was explicitly checked: gamma gamma-prime, U-prime, lambda_i, celui des, ens. des pts fixes, and (pour1∈Gamma). The uncertain cancelled words were not certified clear merely because their context suggested a reading.',
        'Read page.jpg once for layout and both supplied native halves once line by line. Twenty-five saved enlarged crops cover all lexical differences, resolved C doubts, and newly opened places. Some contextual upper tips are clipped in crops10,13,18,23; the prescribed native-half reading supplied those strokes, and the later blind-reading boxes extend to contain the full selected inscriptions. No second first-reading crop of a decided place was made. Crop25 addresses only the newly noticed preceding-line suivant des, complementary to crop20.',
        'No external research, OCR, other-page comparison, TeX compilation, proof check, or mathematical computation was used. Root independently reviewed all25 saved crops and agreed on retaining the local uncertainties and the repeated des. Remaining disagreements are reported from ink rather than repaired to expected mathematics.'
    ],check_events=[],diff_coverage=coverage)

(out/'145_scan017.tex').write_text(tex,encoding='utf-8')
(out/'145_scan017.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'scan':17,'changes':len(changes),'decisions':len(decisions),'unlisted_decisions':len(unlisted),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second),'diff_rows':len(coverage),'crops':len(crop_boxes)},ensure_ascii=False))
