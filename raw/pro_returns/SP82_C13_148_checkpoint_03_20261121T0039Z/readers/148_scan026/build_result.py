from pathlib import Path
import json
import re

PACKET = Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan026')
META = json.loads((PACKET / 'meta.json').read_text())
OUT = Path(META['output'])
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()

boxes = {
    'top_correspondence': [105,164,1110,382],
    'orientation_line': [22,380,518,497],
    'covering_line': [565,355,1512,516],
    'pants': [112,468,522,927],
    'top_teardrop': [1078,80,1148,213],
    'top_tetrahedron': [1210,65,1490,291],
    'three_point_sphere': [1515,150,1646,300],
    'central_thickened_graph': [420,185,1383,1074],
    'struck_varieties': [850,716,1290,812],
    'relation': [485,821,1345,953],
    'r_curves': [788,930,1335,1033],
    'bottom_oval_note': [765,1038,1142,1165],
    'ring_chain': [1342,552,1680,922],
    'large_loop_sign': [1355,325,1628,540],
    'small_loop_stem': [40,778,215,972],
    'torus': [142,947,414,1226],
    'figure_eight': [485,950,710,1262],
    'folio': [30,1249,104,1319],
    'segment_zero_one': [907,574,1132,729],
    'sigma_braces': [1182,542,1369,631],
}

def crop(label):
    return f'crops/148_scan026_{label}.png'

def scope(text, xy):
    start = text.index(r'\begin{scope}[shift={(' + xy + r')}]')
    end = text.index(r'\end{scope}', start) + len(r'\end{scope}')
    return text[start:end]

def chunk(text, start, end):
    a = text.index(start)
    b = text.index(end, a)
    return text[a:b].rstrip()

def fig(code):
    return r'\figure{\begin{tikzpicture}[x=.0065cm,y=-.0065cm,line cap=round,line join=round]' + '\n' + code + '\n' + r'\end{tikzpicture}}'

candidate = C

def replace(old, new):
    global candidate
    assert candidate.count(old) == 1, (old, candidate.count(old))
    candidate = candidate.replace(old, new, 1)

replace(r'\unsure{\text{conn}}', r'\text{conn}')
replace(r'\text{Cartes }\uline{\text{cellulaires}}', r'\text{cartes }\uline{\text{cellulaires}}')
replace(r'\arrow[r,leftrightarrow]', r'\arrow[r,leftarrow,shift left=.6ex]\arrow[r,shift right=.6ex]')
replace(r'\margin{\unsure{\(\mathrm{or}^{t}\)|orient.}}' + '\ntriangulée', r'\inserted{\(\mathrm{or}^{t}\)}\,/\,triangulée')
replace(r'revêtements de \(\mathbb P^1_{\unsure{\mathbb Q|\mathbb C}}\)', r'\unsure{revêtements|\deleted{revêtements}} de \(\mathbb P^1_{\mathbb C}\)')
replace(r'\(\mathbb R\)-\unsure{courbes|cartes} algébriques', r'\(\mathbb R\)-courbes algébriques')
replace(r'\unsure{ses|sans} pts fixes', r'ss pts fixes')

old_sphere = scope(C, '1577,221')
new_sphere = r'''\begin{scope}[shift={(1577,221)}]
\draw (0,0) ellipse (46 and 55);
\foreach \x/\y in {-6/-44,38/8,-31/48}{\draw (\x,\y) circle (15);}
\foreach \x/\y in {-6/-44,38/8}{\fill (\x,\y) circle (5);}
\draw[line width=1.2pt] (-31,48) circle (5);
\end{scope}'''
replace(old_sphere, new_sphere)

old_triangle = r'''\draw (498,645)--(788,356)--(849,681);
\draw (498,645) .. controls (658,640) and (748,707) .. (847,686);'''
new_triangle = r'''\draw (498,645)--(788,356);
\draw (795,365)--(820,502)--(815,506);
\draw (822,516)--(849,681);
\draw (498,650) .. controls (658,640) and (748,707) .. (847,686);'''
replace(old_triangle, new_triangle)

old_sigmas = r'''\node at (1211,574) {\(\sigma_0\ \sigma_1\ \sigma_2\)};
\draw (1200,608)--(1200,615)--(1275,617)--(1275,608) (1294,612)--(1294,618)--(1353,620)--(1353,614);'''
new_sigmas = r'''\node[font=\scriptsize] at (1219,578) {\(\sigma_0\)};
\node[font=\scriptsize] at (1277,584) {\(\sigma_1\)};
\node[font=\scriptsize] at (1336,586) {\(\sigma_2\)};
\draw (1215,607)--(1213,615)--(1277,619)--(1277,611) (1298,615)--(1296,621)--(1352,623)--(1352,616);'''
replace(old_sigmas, new_sigmas)

old_chain = scope(C, '1510,739')
new_chain = r'''\begin{scope}[shift={(1510,739)}]
\draw (-51,-105) .. controls (-6,-190) and (60,-192) .. (121,-136);
\draw (130,-26) .. controls (128,25) .. (111,80);
\draw (7,151) .. controls (-139,185) and (-119,53) .. (-116,7);
\draw (-74,-51) ellipse (49 and 64);
\draw (120,-79) ellipse (34 and 57);
\draw (111,80) .. controls (76,53) and (-25,101) .. (7,151) .. controls (55,187) and (151,126) .. (111,80);
\draw (-141,-74) .. controls (-158,-52) and (-146,-8) .. (-116,7);
\draw (108,87) .. controls (54,61) and (-4,113) .. (10,141);
\draw (7,151) .. controls (24,153) .. (47,143);
\foreach \x/\y in {-51/-105,-116/7,121/-136,111/80,7/151}{\fill (\x,\y) circle (3);}
\draw[line width=.8pt] (130,-26) circle (5);
\end{scope}'''
replace(old_chain, new_chain)

old_torus = scope(C, '287,1091')
new_torus = r'''\begin{scope}[shift={(287,1091)}]
\draw (0,0) ellipse (126 and 126);
\draw (-60,-7) .. controls (-28,-61) and (52,-85) .. (57,-25) .. controls (64,9) and (35,52) .. (-7,56) .. controls (-52,59) and (-64,32) .. (-60,9);
\draw[line width=1.2pt] (0,-126) .. controls (-105,-97) and (-154,35) .. (-77,106) .. controls (0,152) .. (73,102);
\draw (0,-126) .. controls (-23,-102) and (-22,-64) .. (-10,-53) .. controls (15,-40) and (26,-104) .. (0,-126);
\draw (-13,-97) .. controls (12,-125) and (40,-120) .. (57,-110);
\draw (0,-126) .. controls (52,-135) and (92,-109) .. (105,-72);
\fill (0,-126) circle (6);
\end{scope}'''
replace(old_torus, new_torus)

old_eight = scope(C, '522,1113')
new_eight = r'''\begin{scope}[shift={(522,1113)}]
\draw[line width=1.2pt] (0,0) .. controls (61,-237) and (282,-129) .. (107,-43) .. controls (55,-17) .. (0,0) .. controls (-64,177) and (152,178) .. (0,0);
\draw (0,0) .. controls (37,-20) and (63,-25) .. (90,-36);
\draw (43,-23)--(49,-29)--(53,-22);
\end{scope}'''
replace(old_eight, new_eight)

old_bottom_oval = r'''\draw (791,1105) .. controls (738,1062) and (903,1042) .. (926,1075);
\draw (947,1087) .. controls (998,1125) and (829,1160) .. (791,1105);
\foreach \x/\y in {878/1064,837/1127,925/1123}{\fill (\x,\y) circle (3);}'''
new_bottom_oval = r'''\draw (791,1105) .. controls (738,1062) and (903,1042) .. (926,1075);
\draw (947,1087) .. controls (998,1125) and (829,1160) .. (791,1105);
\foreach \x/\y in {878/1064,925/1123}{\fill (\x,\y) circle (3);}
\draw[line width=.8pt] (837,1127) ellipse (5 and 3);'''
replace(old_bottom_oval, new_bottom_oval)

OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'candidate.tex').write_text(candidate)

changes = []

def change(place, c, h, final, ink, label, kind, against_c, against_h, math=False, confidence='high'):
    # An empty snippet denotes absence, not an invented witness paraphrase.
    if c:
        assert c in C, ('C snippet not literal', place, c)
    if h:
        assert h in H, ('H snippet not literal', place, h)
    changes.append(dict(place=place, c=c, h=h, final=final, ink=ink,
                        crop=crop(label), box=boxes[label], confidence=confidence,
                        kind=kind, against_c=against_c, against_h=against_h, math=math))

change('Top definition: conn', r'\unsure{\text{conn}}', 'connexe', r'\text{conn}',
       'Four letters are present: an open c, rounded o, and two compressed n strokes. No e-x-e follows the last n.',
       'top_correspondence', 'abbreviation expanded or spelling modernised', True, True)
change('Right caption: lowercase cartes and underline', r'\text{Cartes }\uline{\text{cellulaires}}', 'cartes cellulaires', r'\text{cartes }\uline{\text{cellulaires}}',
       'The initial c is a small open curve, unlike the tall C in the first Carte. A separate long horizontal stroke runs under cellulaires only.',
       'top_correspondence', 'misread word', True, True)
change('Two opposed correspondence shafts', r'\arrow[r,leftrightarrow]', r'$\longleftrightarrow$', r'\arrow[r,leftarrow,shift left=.6ex]\arrow[r,shift right=.6ex]',
       'The upper horizontal shaft has a leftward head at its left end and stops without a right head. A distinct lower shaft ends in a rightward head. The intervening gap is visible along their lengths.',
       'top_correspondence', 'drawing or diagram', True, True, True)
change('Left continuation prefix: or with superscript t', r'\margin{\unsure{\(\mathrm{or}^{t}\)|orient.}}', r'\add{orient.}', r'\inserted{\(\mathrm{or}^{t}\)}',
       'The prefix has baseline o-r and a small raised t. There are no intervening i-e-n letters and no terminal period. It is placed before the slash at the head of the continuation.',
       'orientation_line', 'abbreviation expanded or spelling modernised', True, True, True)
change('Slash before triangulée', '', r'\, /\,'.replace(' ', ''), r'\, /\,'.replace(' ', ''),
       'A distinct long oblique stroke separates the raised-t abbreviation from the next word.',
       'orientation_line', 'omission', True, False)
change('Singular triangulée', 'triangulée', 'triangulées', 'triangulée',
       'After the accented e, the final small e ends with a short exit stroke. There is no extra terminal s loop.',
       'orientation_line', 'misread word', False, True)
change('Canceled or overwritten prefix before revêtements', r'\margin{\unsure{\(\deleted{\mathbf Z}n-\)|\(\deleted{\mathbf Z/n}\)}}', r'\struck{$\mathbf{Z}/n$}', r'\margin{\unsure{\(\deleted{\mathbf Z}n-\)|\(\deleted{\mathbf Z/n}\)}}',
       'A heavily retraced Z-like figure is followed by an n-shaped arch and a short horizontal stroke. An independent slash and the full cancellation scope cannot be separated securely from the heavy ink and curved stroke below.',
       'covering_line', 'deletion state', False, True, True, 'low')
change('Subscript of the projective line', r'\mathbb P^1_{\unsure{\mathbb Q|\mathbb C}}', r'\mathbf{P}^{1}', r'\mathbb P^1_{\mathbb C}',
       'Below the doubled P and raised 1 is an open curved C with an inner/doubled stroke. There is no independent lower-right Q tail; a thin diagonal belongs to the drawing passing through this place.',
       'covering_line', 'misread symbol or index', True, True, True)
change('R-courbes algébriques', r'\(\mathbb R\)-\unsure{courbes|cartes} algébriques', r'$\mathbf{R}$-courbes algébriques', r'\(\mathbb R\)-courbes algébriques',
       'After c-o-u-r, the word has a tall curved b ascender and a low ending. No crossed t is present. The full phrase and the doubled R were read in the crop.',
       'r_curves', 'misread word', True, False)
change('Fixed-point note: ss', r'\unsure{ses|sans} pts fixes', 'sans pts fixes', 'ss pts fixes',
       'Two compressed cursive s loops precede the separate descending p of pts. There is no intervening e, and no a-n sequence. The following pts fixes is visible.',
       'bottom_oval_note', 'abbreviation expanded or spelling modernised', True, True)
change('Relation: final numeral 1', r'(\sigma_0\sigma_1)^3=1', r'(\sigma_0\sigma_1)^{3} = \underline{1}', r'(\sigma_0\sigma_1)^3=1',
       'The 1 has a sloping entry, upright stem, and horizontal foot touching that stem. No detached underline is visible. The lower oblique line is a graph edge, separate from the numeral.',
       'relation', 'misread symbol or index', False, True, True)
change('Bottom-left foliation', r'\margin{25}', '', r'\margin{25}',
       'The lighter hand writes a curved-top 2 with a long lower foot, followed by a 5 with a top bar and rounded lower turn.',
       'folio', 'omission', False, True)
change('Top-right three-point oval', old_sphere, 'une petite boucle à deux points', new_sphere,
       'Three outer rings occur at the upper, right, and lower-left positions. The first two inner marks are filled; the lower-left inner mark encloses a small clear center. H elsewhere calls this a three-point sphere, but its final drawing clause says two points.',
       'three_point_sphere', 'drawing or diagram', True, True, True)
change('Central thin triangular strokes: breaks and kink', old_triangle,
       'un graphe trivalent dont trois arêtes sont épaissies en bandes', new_triangle,
       'The rising diagonal stops before the nearly vertical side. That side has a small bent end near y=505 and resumes below a visible gap. The curved lower stroke starts a little below the diagonal endpoint.',
       'central_thickened_graph', 'drawing or diagram', True, True, True)
change('Sigma list and two brackets', old_sigmas,
       r'$\sigma_0\,\sigma_1\,\sigma_2$, les deux' + '\n' + 'derniers soulignés par une accolade', new_sigmas,
       'The three sigma symbols carry subscripts 0, 1, 2. The first shallow bracket runs approximately x=1213 to 1277, from beneath the first subscript toward the middle sigma body. The second runs x=1296 to 1352, beginning just right of the middle subscript and lying below the third sigma. A clear gap separates the brackets. The three nodes are positioned separately over these strokes.',
       'sigma_braces', 'drawing or diagram', True, True, True)
change('Large loop sign', r'\node at (187,-61) {\(\pm\)};',
       'une de ses arêtes portant une grande boucle', r'\node at (187,-61) {\(\pm\)};',
       'Inside the repeated loop is a vertical stroke crossing an upper horizontal bar, with a second lower horizontal bar. The two-bar plus/minus form is visible.',
       'large_loop_sign', 'omission', False, True, True)
change('Three-ring chain', old_chain, 'une chaîne de cercles', new_chain,
       'Three ovals are joined by curved connecting strokes. The lower mark on the right oval encloses a clear center. The bottom oval slopes upward to the right and has an inner partial retrace; the left oval also has an exterior partial stroke.',
       'ring_chain', 'drawing or diagram', True, True, True)
change('Torus sketch: open inner contour and top loop', old_torus, 'un tore', new_torus,
       'The inner contour has separated ends at the left. A narrow vertical loop reaches its upper rim from the filled top point. Short open arcs are visible at the upper right; they do not form an extra closed oval.',
       'torus', 'drawing or diagram', True, True, True)
change('Figure-eight sketch: small angular retrace', old_eight, 'une boucle en huit', new_eight,
       'The upper lobe returning toward the crossing is retraced. Its small mark has an angular upward projection rather than a round point; the tracing preserves that projection without assigning an arrow direction.',
       'figure_eight', 'drawing or diagram', True, True, True, 'medium')
change('Bottom oval: lower-left open mark', old_bottom_oval, 'un ovale portant trois points', new_bottom_oval,
       'The top and lower-right marks are solid. The lower-left mark is a small dark outline with a clear center; the oval itself remains open at its right-hand gap.',
       'bottom_oval_note', 'drawing or diagram', True, True, True)

decisions = []
def decision(id, decision_value, reading, ink, label, confidence):
    decisions.append(dict(id=id, decision=decision_value, reading=reading, ink=ink,
                          crop=crop(label), box=boxes[label], confidence=confidence))

decision('M0268', 'first', 'conn', 'The four written letters stop after the second n; there is no exe ending.', 'top_correspondence', 'high')
decision('M0269', 'first', r'\(\mathrm{or}^{t}\)', 'Baseline o-r is followed by raised t; there is no i-e-n sequence or full-stop.', 'orientation_line', 'high')
decision('M0270', 'undecided', r'\unsure{\(\deleted{\mathbf Z}n-\)|\(\deleted{\mathbf Z/n}\)}', 'Heavy crossing strokes cover the Z-like figure; n and a short bar survive, but the putative slash and cancellation extent do not separate securely.', 'covering_line', 'low')
decision('M0271', 'alternative', r'\mathbb C', 'An open curved body and inner stroke form C; the apparent tail belongs to the diagonal of the drawing.', 'covering_line', 'high')
decision('M0272', 'undecided', r'\unsure{seulement}', 'An initial short s-like stroke, a tall l-like rise and a terminal upright/loop remain, but the compressed medial run and crossing loop prevent secure identification of every letter.', 'covering_line', 'medium')
decision('M0273', 'first', 'courbes', 'The tall b ascender after the low c-o-u-r run distinguishes courbes from cartes.', 'r_curves', 'high')
decision('M0274', 'other', 'ss', 'Two compact s loops are written; neither an intervening e nor a-n is visible.', 'bottom_oval_note', 'high')

inventory = []
def inv(element, kind, position, words, hand='his hand'):
    inventory.append(dict(element=element, kind=kind, position=position,
                          first_words_or_objects=words, sheet_kind='text',
                          hand=hand, transcribed='yes'))

inv('I026.01','text','upper left, first line','Carte cellulaire (pas orientée) conn')
inv('I026.02','text','upper left, second line','dont tous les sommets sont')
inv('I026.03','text','upper left, third line',r"d'ordre \(3\)")
inv('I026.04','insertion','between the degree line and the double arrow',r'ou \(1\)')
inv('I026.05','diagram','upper left to upper middle',r'two shafts, upper leftward and lower rightward; cartes \uline{cellulaires}')
inv('I026.06','insertion','far left at the head of the next line',r'\(\mathrm{or}^{t}\) /')
inv('I026.07','text','left continuation, below the correspondence',r'triangulée \(\simeq\)')
inv('I026.08','margin note','above and to the left of revêtements',r'\unsure{\(\deleted{\mathbf Z}n-\)|\(\deleted{\mathbf Z/n}\)}')
inv('I026.09','deletion','within the small prefix before revêtements',r'\deleted{\mathbf Z}; cancellation extent uncertain')
inv('I026.10','text','upper middle, crossed by drawing strokes',r'\unsure{revêtements|\deleted{revêtements}} de \(\mathbb P^1_{\mathbb C}\) ramifiés \unsure{seulement}')
inv('I026.11','text','line below the covering phrase',r'en \(0,1,\infty\),')
inv('I026.12','drawing','near the upper edge at x=1112','narrow doubled loop with crossing internal strokes')
inv('I026.13','drawing','upper right of center','tetrahedral outline and crossing diagonals')
inv('I026.14','drawing','near upper-right edge','oval with three circled marks')
inv('I026.15','drawing','left center',r'pants; \(A,B,C,c_B,c_A,b_C,b_A,a_C,a_B\); orientation arrows')
inv('I026.16','drawing','center, crossing the prose and formulas','branched graph with three band-like strokes and lower arrows')
inv('I026.17','drawing','under the band-like graph','thin triangular strokes with interrupted nearly vertical side')
inv('I026.18','drawing','right of center',r'retraced large loop containing \(\pm\)')
inv('I026.19','display','beneath the upper-right branch',r'\(\sigma_0\ \sigma_1\ \sigma_2\), with two separate lower brackets')
inv('I026.20','drawing','center-right under the branch',r'open oval and thick segment marked \(0\) and \(1\)')
inv('I026.21','deletion','middle-right, above the relation',r'\deleted{\unsure{variétés} algébriques d}')
inv('I026.22','display','across the lower center',r'\sigma_0^2=\sigma_1^2=\sigma_2^2=(\sigma_0\sigma_2)^2=(\sigma_0\sigma_1)^3=1')
inv('I026.23','text','below the relation',r'\(\mathbb R\)-courbes algébriques')
inv('I026.24','drawing','right side','three ovals joined by curved strokes')
inv('I026.25','drawing','lower left above the torus','large loop and small open loop connected by a sloping stem')
inv('I026.26','drawing','lower left','torus-like pair of contours, narrow upper loop, filled top point')
inv('I026.27','drawing','lower middle-left','two unequal lobes meeting in a figure-eight crossing')
inv('I026.28','drawing','near lower center','open oval with three marks, lower-left mark hollow')
inv('I026.29','text','beside the bottom oval, first line',r'\(\sigma_0,\sigma_1,\sigma_2\)')
inv('I026.30','text','beside the bottom oval, second line','ss pts fixes')
inv('I026.31','margin note','bottom-left corner','25','another unnamed hand (lighter foliation)')
inv('I026.32','drawing','above and to the left of the upper figure-eight lobe','short isolated slanted stroke')

unresolved = [
    dict(place='Prefix before revêtements', reading=r'\unsure{\(\deleted{\mathbf Z}n-\)|\(\deleted{\mathbf Z/n}\)}', issue='The overtraced Z-like figure, possible slash and cancellation extent cannot be separated securely.', alternatives=[r'\(\deleted{\mathbf Z}n-\)',r'\(\deleted{\mathbf Z/n}\)'], confidence='low'),
    dict(place='Deletion status of revêtements', reading=r'\unsure{revêtements|\deleted{revêtements}}', issue='The joined baseline and heavy final strokes can be retracing or cancellation; no distinct full-word strike is separable.', alternatives=['revêtements',r'\deleted{revêtements}'], confidence='low'),
    dict(place='Word after ramifiés', reading=r'\unsure{seulement}', issue='The medial letters are highly compressed and partly intersected by the large loop; every letter is not independently legible.', alternatives=['seulement'], confidence='medium'),
    dict(place='First word of the struck phrase', reading=r'\deleted{\unsure{variétés} algébriques d}', issue='The horizontal cancellation hides the low letter bodies in variétés; the word cannot be released from doubt letter by letter.', alternatives=['variétés'], confidence='low'),
]

notes = [
    dict(id='N026.01',kind='sheet',place='whole page',text='A landscape piece of kraft paper with irregular torn edges bears ink prose, formulas and sketches. The foliation is lighter and is not attributed to the main hand. No manuscript date is visible.'),
    dict(id='S026.01',kind='claim',place='top correspondence',text='The page places the description of a connected, unoriented cellular map, with vertices of order 3 and the interlinear addition or 1, in a two-way correspondence with cellular maps. This records the wording and arrow, without supplying a proof.',crop=crop('top_correspondence')),
    dict(id='S026.02',kind='claim',place='upper continuation',text='The continuation relates the triangulated/orientation wording to coverings of the complex projective line ramified at 0, 1 and infinity. The prefix, the deletion status of revêtements, and the word seulement remain qualified in the transcription.',crop=crop('covering_line')),
    dict(id='S026.03',kind='claim',place='relation',text='The displayed relation states that the three sigma squares, the square of sigma0 sigma2, and the cube of sigma0 sigma1 equal 1. All indices and exponents were transcribed from the crop; no algebraic proof or independent computation was performed.',crop=crop('relation')),
    dict(id='S026.04',kind='claim',place='bottom oval note',text='Beside the three-point oval, the page lists sigma0, sigma1, sigma2 and writes ss pts fixes. The abbreviation is retained, with its proposed expansion confined to the abbreviation list.',crop=crop('bottom_oval_note')),
    dict(id='N026.02',kind='deletion',place='struck phrase',text='The horizontal strike begins through the first word and extends beyond the final d. The doubtful first word remains doubtful. The phrase R-courbes algébriques is on the following lower line; no missing ending after d is supplied.',crop=crop('struck_varieties')),
    dict(id='N026.03',kind='witness',place='three-point oval',text='H is internally inconsistent: its earlier note names a three-point sphere, while the final drawing description gives two points. The ink has three circled positions.',crop=crop('three_point_sphere')),
    dict(id='N026.04',kind='reading',place='relation and segment label',text='The long lower stroke of 1 is attached to its stem in both the final relation and the segment label. It is not transcribed as a separate underline.',crop=crop('relation')),
    dict(id='N026.05',kind='scope',place='whole page',text='Twenty saved crop rectangles were prepared and viewed. Whole-page layout and both supplied halves were read once; all agreed words and signs were included. The central graph PNG exceeded the image-output transport limit, so exactly the same crop at the same pixel dimensions was viewed as a JPEG display copy. No OCR, outside source, other page or TeX compilation was used.'),
    dict(id='N026.06',kind='accounting',place='whole page',text='lines_read counts 28 distinct text-bearing lines or isolated label groups: the prose/formula lines, interlinear addition, nine pants labels, plus/minus sign, two segment labels, and foliation. Drawing-only strokes were inventoried separately.'),
    dict(id='N026.07',kind='reading',place='figure eight',text='The small angular mark on the returning upper lobe is traced as visible pen strokes; no directional meaning is assigned to it.',crop=crop('figure_eight')),
    dict(id='N026.08',kind='drawing',place='central crossing graph',text='The single crop-candidate comment is retained for the genuinely complex central graph and its crossing strokes. All figures are nevertheless reproduced in TikZ; the comment does not replace any drawing.',crop=crop('central_thickened_graph')),
]

hand_log = [
    dict(pages=[26],hand='his hand',observation='Connected prose can collapse medial letters into a nearly flat run, while a b ascender remains tall.',scope='Observed in courbes and algébriques; not asserted for other hands or every word.',witness_errors='C offered cartes beside courbes; the tall b settles this occurrence.'),
    dict(pages=[26],hand='his hand',observation='The numeral 1 can have a long horizontal foot attached to the upright.',scope='Observed in the relation and segment label; also consistent with the interlinear 1 and raised 1.',witness_errors='H supplies a separate underline to the relation-ending 1.'),
    dict(pages=[26],hand='his hand',observation='The written short form ss consists of two compact cursive loops.',scope='One occurrence, in ss pts fixes.',witness_errors='C offered ses or sans; H expanded sans.'),
    dict(pages=[26],hand='his hand',observation='The subscript C below P has an open rounded body and inner/doubled stroke.',scope='One occurrence; a diagonal drawing stroke crosses it.',witness_errors='C preferred Q; H omitted the subscript.'),
    dict(pages=[26],hand='his hand',observation='Sigma has a long horizontal arm with a hooked curved left body.',scope='Confirmed across the list above the relation, the relation itself and the bottom list.',witness_errors='No sigma-letter substitution found at these occurrences.'),
    dict(pages=[26],hand='his hand',observation='The initial C in Carte is taller than the small open c beginning cartes in the right caption.',scope='These two words on the same page.',witness_errors='C capitalized the right caption.'),
]

notation = [
    dict(form=r'\mathbb P^1_{\mathbb C}',use='Written after de in the covering phrase.',pages=[26],caution='The C is crossed by a thin diagram stroke; do not turn that crossing into a Q tail.'),
    dict(form=r'\mathbb R',use='Doubled R before -courbes algébriques.',pages=[26],caution='Retain the written real-field letter and hyphen.'),
    dict(form=r'\sigma_0,\sigma_1,\sigma_2',use='Repeated list and displayed relation; two separate shallow brackets below the upper list.',pages=[26],caution='Do not replace the two visible strokes by one brace or infer its scope from expected mathematics.'),
    dict(form=r'\pm',use='Inside the large retraced loop.',pages=[26],caution='Two horizontal bars and a single vertical are present.'),
    dict(form=r'a_B,a_C,b_C,b_A,c_B,c_A',use='Six labels at the paired points of the pants boundaries A, B, C.',pages=[26],caution='Read the actual upper/lower position and subscript, independently of a presumed cyclic order.'),
]

abbreviations = [
    dict(written='conn',proposed_expansion='connexe',place='top definition',confidence='high'),
    dict(written=r'\(\mathrm{or}^{t}\)',proposed_expansion='orienté / orientée',place='left continuation prefix',confidence='medium'),
    dict(written='ss',proposed_expansion='sans',place='bottom oval note',confidence='high'),
    dict(written='pts',proposed_expansion='points',place='bottom oval note',confidence='high'),
]

second_boxes = []
def second(label, kind, reading):
    x0,y0,x1,y1 = boxes[label]
    second_boxes.append(dict(box=f'B026_{len(second_boxes)+1:02d}',kind=kind,x0=x0,y0=y0,x1=x1,y1=y1,reading=reading))

top_final = chunk(candidate, r'\diagram{', r'\inserted{\(\mathrm{or}')
prefix_final = r'\margin{\unsure{\(\deleted{\mathbf Z}n-\)|\(\deleted{\mathbf Z/n}\)}}'
cover_final = prefix_final + '\n' + r'\unsure{revêtements|\deleted{revêtements}} de \(\mathbb P^1_{\mathbb C}\) ramifiés \unsure{seulement} en \(0,1,\infty\),'
central_final = chunk(candidate, r'\draw (529,370)', r'\begin{scope}[shift={(1370,494)}]') + '\n' + r'\draw (521,962)--(535,940);'
segment_final = chunk(candidate, r'\draw (945,684)', r'\begin{scope}[shift={(1510,739)}]')
small_loop_final = chunk(candidate, r'\draw (127,875)', r'\begin{scope}[shift={(287,1091)}]')
relation_final = r'\[\sigma_0^2=\sigma_1^2=\sigma_2^2=(\sigma_0\sigma_2)^2=(\sigma_0\sigma_1)^3=1\]'
second('top_correspondence','insertion / different word / handwritten number',top_final)
second('orientation_line','insertion / different word',r'\inserted{\(\mathrm{or}^{t}\)}\,/\,triangulée \(\simeq\)')
second('covering_line','margin note / deletion / whole doubtful formula / handwritten number',cover_final)
second('pants','drawing labels',fig(scope(candidate,'300,680')))
second('top_teardrop','drawing',fig(scope(candidate,'1112,150')))
second('top_tetrahedron','drawing',fig(scope(candidate,'1340,170')))
second('three_point_sphere','drawing',fig(new_sphere))
second('central_thickened_graph','drawing',fig(central_final))
second('struck_varieties','struck passage',r'\deleted{\unsure{variétés} algébriques d}')
second('relation','whole formula / handwritten numbers',relation_final)
second('r_curves','resolved C doubt',r'\(\mathbb R\)-courbes algébriques')
second('bottom_oval_note','different word / drawing / handwritten numbers',fig(new_bottom_oval) + '\n' + r'\(\sigma_0,\sigma_1,\sigma_2\)\quad ss pts fixes')
second('ring_chain','drawing',fig(new_chain))
second('large_loop_sign','drawing / sign',fig(scope(candidate,'1370,494')))
second('small_loop_stem','drawing',fig(small_loop_final))
second('torus','drawing',fig(new_torus))
second('figure_eight','departure from C below high confidence',fig(new_eight))
second('folio','margin note / handwritten number',r'\margin{25}')
second('segment_zero_one','drawing / handwritten numbers',fig(segment_final))
second('sigma_braces','drawing / handwritten indices',fig(new_sigmas))

differences_review = [
    dict(source_row=105,classification='macro-only',place='page wrapper and editorial sheet description',reason='H sheet description is editorial, not manuscript text.'),
    dict(source_row=106,classification='reading decision',place='Top definition: conn',reason='Keep the written abbreviation.'),
    dict(source_row=107,classification='reading decision',place='Two opposed correspondence shafts',reason='Both witnesses reduce the two opposed shafts to one double-headed shaft. The interlinear ou 1 itself agrees, apart from macro syntax.'),
    dict(source_row=108,classification='reading decision',place='Left continuation prefix: or with superscript t',reason='Retain the visible abbreviation and its placement.'),
    dict(source_row=109,classification='reading decision',place='Slash before triangulée; Singular triangulée',reason='The slash is present; no final s is visible.'),
    dict(source_row=110,classification='reading decision',place='Canceled or overwritten prefix before revêtements',reason='Alternatives retained; cancellation scope unresolved.'),
    dict(source_row=111,classification='reading decision',place='Canceled or overwritten prefix before revêtements',reason='Same unresolved prefix, not a separately secure quotient slash.'),
    dict(source_row=112,classification='macro-only',place='math delimiter after de',reason='Delimiter alone carries no reading difference.'),
    dict(source_row=113,classification='reading decision',place='Subscript of the projective line',reason='The written subscript is C.'),
    dict(source_row=114,classification='macro-only',place='math delimiter before branch points',reason='The word seulement remains explicitly doubtful in place; the reported token difference is a delimiter.'),
    dict(source_row=115,classification='macro-only',place='math delimiter after branch points',reason='No content change in 0,1,infinity or the following comma.'),
    dict(source_row=116,classification='reading decision',place='Deletion status of revêtements',reason='Status remains uncertain in the candidate and doubts record; no certainty-only changes row is added.'),
    dict(source_row=117,classification='reading decision',place='Full figures; Relation: final numeral 1',reason='TikZ reproduces all figures; detailed drawing decisions and the attached foot of 1 are recorded separately.'),
    dict(source_row=118,classification='macro-only',place='R math wrapper versus displaced H editorial note',reason='Both witnesses give R-courbes; the alignment artifact does not add the H editorial words to the page.'),
    dict(source_row=119,classification='reading decision',place='R-courbes algébriques',reason='The b ascender resolves C courbes/cartes.'),
    dict(source_row=120,classification='reading decision',place='Fixed-point note: ss; Sigma list and two brackets; struck phrase',reason='Keep ss; trace two brackets; retain variétés uncertainty and full strike scope.'),
    dict(source_row=121,classification='reading decision',place='Bottom-left foliation; all drawings',reason='Retain 25, reproduce all drawing objects, and exclude H editorial descriptions from manuscript prose.'),
]

for entry in hand_log:
    entry['holds_at_every_observed_occurrence'] = entry.pop('scope')
    entry['witness_effect'] = entry.pop('witness_errors')
for entry in abbreviations:
    entry['form'] = entry.pop('written')
    entry['expansion'] = entry.pop('proposed_expansion')

result = dict(scan=26,reader='reader_c',lines_read=28,changes=changes,decisions=decisions,
              inventory=inventory,unresolved=unresolved,notes=notes,checks=[],
              hand_log=hand_log,notation=notation,abbreviations=abbreviations,
              second_boxes=second_boxes,differences_review=differences_review)
(OUT / 'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')

# Static integrity only; these are not mathematical CHECK_EVENTS.
assert len(decisions)==7 and len({d['id'] for d in decisions})==7
assert {d['source_row'] for d in differences_review}==set(range(105,122))
assert len(second_boxes)==20 and len({b['box'] for b in second_boxes})==20
for entry in changes+decisions:
    label=entry['crop'].removeprefix('crops/148_scan026_').removesuffix('.png')
    assert entry['box']==boxes[label]
    assert (Path(META['crops'])/Path(entry['crop']).name).exists()
balance=0
for ch in re.sub(r'\\[{}]','',candidate):
    if ch=='{': balance+=1
    elif ch=='}': balance-=1
    assert balance>=0
assert balance==0
print(json.dumps({'candidate':str(OUT/'candidate.tex'),'result':str(OUT/'result.json'),
                  'changes':len(changes),'decisions':len(decisions),'inventory':len(inventory),
                  'unresolved':len(unresolved),'second_boxes':len(second_boxes),'differences_review':len(differences_review),
                  'checks':0},indent=2))
