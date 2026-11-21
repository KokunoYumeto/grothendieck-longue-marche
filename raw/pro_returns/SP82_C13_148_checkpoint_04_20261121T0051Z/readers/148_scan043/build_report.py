from pathlib import Path
import csv
import json

OUT = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan043')
PACKET = Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan043')
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
candidate = (OUT / 'candidate.tex').read_text()
boxes = json.loads((OUT / 'crop_boxes.json').read_text())
marks = list(csv.DictReader((PACKET / 'marks.tsv').open(), delimiter='\t'))
diffs = list(csv.DictReader((PACKET / 'differences.tsv').open(), delimiter='\t'))

def span(s, first, last):
    a = s.index(first)
    b = s.index(last, a) + len(last)
    return s[a:b]

changes = []
def change(key, c, h, final, ink, crop, confidence='high', kind='misread word', ac=True, ah=True, math=False, certainty=False):
    row = dict(id=key, place=key.replace('043.', ''), c=c, h=h, final=final,
               ink=ink, crop='crops/148_scan043_' + crop + '.png', box=boxes[crop],
               confidence=confidence, kind=kind, against_c=ac, against_h=ah, math=math)
    if certainty:
        row['certainty_resolution'] = True
    changes.append(row)

change('043.header_false_cancellation', r'\deleted{\illegible{1}}principaux', r'\struck{\ill{}}principaux',
       'principaux', 'The dense strokes are joined to the initial pr/i of principaux; there is no separately bounded word or independent deletion line before it.',
       'header', kind='text not on the page')
change('043.header_Tours', 'Tour', 'Tour', r'\unsure{Tours|Tour}',
       'A heavy separate zigzag follows the r-like shoulder. It favors an s, but the retouched exit of r cannot be excluded; the agreement with la does not settle the ink.',
       'header', 'medium')
change('043.header_struck_systemes', r'\deleted{systèmes de groupoïdes}', r'\struck{système de groupoïdes}',
       r'\deleted{\unsure{systèmes|système} de groupoïdes}',
       'The cancellation crosses the entire phrase. A low terminal stroke before de may be s, but it is entangled with the strike; the plural remains the first tentative reading.',
       'header', 'low', ac=False)
change('043.prelude_RTD', r'\mathrm{RTD}_{\ldots}', r'\mathbb{R}\mathbb{T}D\ldots', r'\mathrm{RTD}\ldots',
       'R, T and D each have a single main stem; the three detached short dots are low on the same baseline, not an index. This contrasts with the clearly doubled T below.',
       'paragraph', kind='misread symbol or index', math=True)
change('043.operations_quotes', "(``les 10 opérations'')", '« les 10 opérations »', "(``les 10 opérations'')",
       'The opening and closing quotation marks are pairs of short high strokes, not angle-shaped guillemets; 1 and the following round 0 are distinct.',
       'paragraph', kind='other', ac=False)
change('043.operations_interline', span(C, r"\inserted{(``les 10 opérations'')}", r'\unsure{réalis.}'),
       span(H, '(« les 10 opérations »)', 'ou autres'),
       r"\inserted{(``les 10 opérations''), \unsure{réalis.}}",
       'The parenthesis and following small word share the raised/interlinear line. The small word has a tall l-like stroke and favors réalis.; its compressed initial strokes do not securely resolve the word. The curved placement stroke belongs to this addition.',
       'paragraph', 'medium', kind='insertion or placement')
change('043.prelude_false_extra_deletion', None, r'\struck{\ill{}}, ou autres', r'\unsure{réalis.}',
       'No separate crossed word stands between the operations parenthesis and the small interlinear word. The horizontal strike below runs through représentant on the lower baseline.',
       'paragraph', kind='text not on the page', ac=False)
change('043.prelude_un', 'dans un groupoïde', 'dans ce groupoïde', 'dans un groupoïde',
       'The short word after dans consists of two connected low humps, u-n; it does not have the open initial c of ce.',
       'paragraph', ac=False)
change('043.prelude_groupoide_comma', 'groupoïde\ndont', 'groupoïde, dont', 'groupoïde dont',
       'There is no detached comma after groupoïde. The nearby long descending curve continues the insertion leader from the interlinear parenthesis.',
       'paragraph', kind='text not on the page', ac=False)
change('043.prelude_struck_RTD_letters', r'\deleted{\unsure{\mathrm{RTD}}}', r'\struck{\ill{}}', r'\deleted{\unsure{\mathrm{RTD}}}',
       'Three capital-sized components remain under the diagonal hatching: a left loop/stem, a central upright and bar, and a right rounded component. RTD is a tentative reading, not a resolved cancellation.',
       'paragraph', 'low', kind=r'readable ink left as \ill{}', ac=False, math=True)
change('043.prelude_live_comma', r'\mathrm{RTD}}},\ ', None, ',',
       'A separate short curved downstroke survives at the right of the cancelled capital cluster, before the live doubled T.',
       'paragraph', kind='omission', ac=False, math=True)
change('043.prelude_Ttop', r'\unsure{\mathbb T}_{\mathrm{top}}', r'\mathbb{T}_{\mathrm{top}}', r'\mathbb T_{\mathrm{top}}',
       'Two parallel vertical strokes enclose a narrow white channel beneath the long top bar; the lowered letters are t-o-p.',
       'paragraph', kind='misread symbol or index', ah=False, math=True, certainty=True)
change('043.diagram_Ttop', r'\unsure{\mathbb T}_{\mathrm{top}}', r'\mathbb{T}_{\mathrm{top}}', r'\mathbb T_{\mathrm{top}}',
       'The diagram label has the same two upright strokes under one crossbar; the low top index is clear.',
       'upper_links', kind='misread symbol or index', ah=False, math=True, certainty=True)
change('043.top_singular', 'cas topologique', 'cas topologiques', 'cas topologique',
       'The final e runs into its exit stroke; there is no independently formed terminal s before the opening parenthesis.',
       'top_caption', ac=False)
change('043.top_toriques', r'\unsure{torique|topologiques}', 'topologiques)', 'toriques',
       'After the struck cluster, the live word has t-o-r-i, a descending q, and a low u-e-s ending; it is shorter than topologiques and includes the final s.',
       'top_caption', certainty=True)
change('043.top_false_close', r'\unsure{torique|topologiques})', 'topologiques)', 'toriques',
       'The live word ends with its low final stroke, followed by clear paper. No closing parenthesis is present on this row.',
       'top_caption', kind='text not on the page')
change('043.top_margin', 'découpage top.', r'\marginal{dimension top.}', 'découpage top.',
       'The rising first word contains the c/ou sequence and a long descending p loop, followed by age; top. is on the next short line at the right margin.',
       'top_margin', ac=False)
change('043.paired_arrows', r'\arrow[r,shift left]\arrow[from=r,shift left]', r'\arrow[r, leftrightarrow]',
       r'\arrow[r,shift left]\arrow[from=r,shift left]',
       'Each of the three comparisons has two distinct parallel shafts, one pointing each way, with two-sided pointed arrowheads. None is a single double-ended shaft or a pair of one-sided harpoons.',
       'upper_links', kind='drawing or diagram', ac=False, math=True)
change('043.an_staggered_pair', r'\arrow[ur,shift left]\arrow[from=ur,shift left]', r"\mathbb{T}'_{\mathrm{an}} \arrow[r, leftrightarrow]", 
       r"\mathbb T'_{\mathrm{an}}\arrow[ur,shift left]\arrow[from=ur,shift left]",
       'The primed analytic label is visibly lower than the main analytic label. Both connecting shafts slope up to the right/down to the left; they are not horizontal.',
       'upper_links', kind='drawing or diagram', ac=False, math=True)
change('043.hyp_staggered_pair', r"\mathbb T'_{\mathrm{hyp}}\arrow[u]\arrow[r,shift left]\arrow[from=r,shift left]", r"\mathbb{T}'_{\mathrm{hyp}} \arrow[u] \arrow[r, leftrightarrow]",
       r"\mathbb T'_{\mathrm{hyp}}\arrow[uu]\arrow[ur,shift left]\arrow[from=ur,shift left]",
       'The primed hyperbolic label is lower than the main hyperbolic label. The two comparison shafts are visibly diagonal, one up-right and the other down-left. The separate upward arrow on the left still joins the primed hyperbolic and primed analytic labels.',
       'upper_links', kind='drawing or diagram', math=True)
change('043.short_annotation_arrow', span(C, r"\mathbb T'_{\mathrm{an}}\arrow[uu,", r'\end{gathered}"]'), None,
       r'\begin{gathered}\uparrow\\\text{à pts marqués}\\\text{et \unsure{drs.|dirs.} tangts}\\\text{complexes}\\\text{\unsure{qconq.|qcq.}}\end{gathered}',
       'Only a short upward shaft appears immediately above the four-line note. No shaft passes through or below that note to the primed analytic object. The short arrow is retained without supplying a full map between the two primed objects.',
       'upper_links', kind='drawing or diagram', math=True)
change('043.left_annotation_words', span(C, r'\text{et \unsure{drs.} tangts}', r'\text{\unsure{qconq.}}'),
       span(H, 'et vect.', 'correspondants'),
       r'et \unsure{drs.|dirs.} tangts complexes \unsure{qconq.|qcq.}',
       'The first abbreviation begins with an ascender-and-loop d, followed by a compressed r/i-r sequence and terminal s-like stroke. tangts is abbreviated on the line; complexes occupies its own line. The last line begins with a descending q and short rounded letters, not the long word correspondants.',
       'upper_links', 'medium', ac=False)
change('043.diff_old_close', r'\deleted{pts \unsure{trous} pointés}', r'\struck{pts \ill{}}',
       r'\deleted{pts \unsure{trous} pointés)}',
       'The lower right curved parenthesis belongs to the old baseline passage after the p-descender and accented ending of pointés. The cancelling line reaches that old closing curve. The middle word remains obscured.',
       'diff_caption', 'medium', kind='deletion state')
change('043.diff_inserted_border', r'\inserted{bord. toriques})', r'bord lisse\supplied{s} ?)',
       r'\inserted{bord toriques)}',
       'The raised replacement reads bord, then t-o-r-i-q-u-e-s, and has its own higher closing curve. There is no separate full stop after bord. The live higher parenthesis is distinct from the cancelled lower one.',
       'diff_caption', kind='insertion or placement')
change('043.diff_struck_parenthesis', r'\deleted{\text{(avec \unsure{presque} pts marqués)}}', r'\struck{(ou \ill{} des pts repères)}',
       r'\deleted{(avec \unsure{peu de|presque} pts marqués)}',
       'The first low letters favor avec. Before pts there is a short p-e-u-like group followed by a separate d-e-like group; the long cancelling line prevents certification of every letter. The final word has the marked q descender and accented ending of marqués, not repères.',
       'diff_caption', 'medium')
change('043.diff_margin', 'déc. diff', r'\marginal{dim.\ diff}', 'déc. diff',
       'The first abbreviation has the loop-and-upright d, a low e and open c ending followed by a dot; it lacks the succession of humps of dim. The following two tall f strokes read diff.',
       'diff_margin', ac=False)
change('043.analytic_singular', '-analytique', '-analytiques', 'analytique',
       'The final e ends in one exit stroke before the parenthesis; no distinct extra s is written.',
       'analytic_caption', ac=False)
change('043.analytic_inserted_C', r'\mathbb C\text{-analytique', r'\mathbf{C}$-analytiques', r'\inserted{\mathbb C\text{-}}\text{analytique}',
       'C and the short hyphen stand above the baseline. A separate sloping placement stroke descends to the beginning of analytique; the prefix is an interlinear addition.',
       'analytic_caption', kind='insertion or placement', math=True)
change('043.analytic_g_state', None, None, r'\unsure{\deleted{g}|g}',
       'A compact g-like loop and descending stroke precede the live t of toriques. A tiny crossing stroke at its top may cancel it, but overtracing cannot be excluded. Its presence is retained and the deletion state is not forced.',
       'analytic_caption', 'low', kind='omission')
change('043.analytic_toriques', r'\unsure{torique|analytiques}', r'\uncertain{analytiques}', 'toriques',
       'After the entangled initial glyph, the live sequence has a tall t, rounded o, short r-i, descending q and low u-e-s ending; it is not the longer word analytiques.',
       'analytic_caption', certainty=True)
change('043.analytic_margin', r'\text{déc. en }\unsure{\mathbb C^\infty?}', r'\marginal{dim.\ $\mathbf{C}$-\ill{}}',
       r'déc. en $\unsure{\mathbb C^\infty?}$',
       'The upper words read déc. en. Below, the C has a doubled stroke and a small raised looped sign with a further question-like stroke. Those raised marks remain unresolved; neither a definite infinity nor a baseline hyphen-word is imposed.',
       'analytic_margin', 'low', ac=False, math=True)
change('043.hyp_singular', 'géodésique)', 'géodésiques)', 'géodésique)',
       'The low final e runs directly into its exit before the closing parenthesis; no distinct terminal s can be separated.',
       'hyp_row', ac=False)
change('043.hyp_dec', r'\unsure{déc.|dim.} hyp.', r'\marginal{dim.\ hyp.}', 'déc. hyp.',
       'The first short word has a looped d followed by e and an open c-shaped end, then a detached dot; hyp. rises diagonally to the right.',
       'hyp_row', certainty=True)
change('043.Calg_label_no_hyphen', r'\mathbb T_{\mathbb C\mathrm{alg}}', r'\mathbb{T}_{\mathbf{C}\text{-alg}}', r'\mathbb T_{\mathbb C\mathrm{alg}}',
       'In the lowered label, the doubled C is followed immediately by a-l-g. No horizontal hyphen occupies the gap, in contrast to the explicit hyphen in the lower Q-bar label.',
       'lower_links1', kind='misread symbol or index', ac=False, math=True)
change('043.Calg_de_propagation', span(C, r'\deleted{rigidification} de', r'\text{propagation'), span(H, r'\struck{rigidification}', r'\uncertain{secondes}'),
       r'\deleted{rigidification} de propagation',
       'The word after the crossed rigidification is a separate live de at the right end of the line. The following line begins with p-r-o-p-a-g-a-t-i-o-n; there is no separately written plural s before the next short word.',
       'calg_caption', 'medium', ac=False)
change('043.Calg_cercles', r'\unsure{des ressorts|de secondes|du cercle}', r'\uncertain{secondes}', r'\unsure{de cercles|des cercles|du cercle}',
       'After propagation, the compressed preposition is open between de/des/du. The next letters favor low c-e-r-c followed by a tall l and low ending, rather than a d near the end of secondes or the multiple s/r/t sequence of ressorts. The final plural remains uncertain.',
       'calg_caption', 'medium')
change('043.Calg_false_close', 'doubles, plus pts marqués', 'doubles, plus pts marqués)', 'doubles, plus pts marqués',
       'After the accented final ending of marqués, the line is blank. No closing parenthesis is written.',
       'calg_caption', kind='text not on the page', ac=False)
change('043.Qalg_propagation', r'\unsure{propagation|pour opération|pour y obtenir}', span(H, 'propagations', r'$\underline{\mathcal{O}}$'), r'\unsure{propagation}',
       'The compressed first word favors propagation. Its descender and return stroke account for the apparent isolated loop; no independent underlined calligraphic O is securely present. The word is not fully resolved.',
       'qalg_caption', 'medium', ac=False)
change('043.Qalg_descente', r'\unsure{des ressorts|descendant|dessus via|des sections}', r'\uncertain{descendant}', r'\unsure{descente|descendant}',
       'The second line begins with a tall d, low e-s-c-like strokes and rounded middle humps, ending in a tall t-like stroke followed by low e. This favors descente; the compressed middle letters leave descendant viable.',
       'qalg_caption', 'medium')
change('043.Qalg_Gal_state', r'\unsure{\mathrm{Gal}/\mathbb Q}', r'\struck{\ill{}}$/\overline{\mathbf{Q}}$',
       r'\unsure{\mathrm{Gal}|\deleted{\mathrm G}\mathrm{al}}/\overline{\mathbb Q}',
       'The initial capital is heavily overtraced, while the following a and tall l are separate and live. The blob may be a retouched G or a cancelled G; the whole word is not demonstrably crossed. The reading and state remain explicit alternatives.',
       'qalg_caption', 'medium', kind='deletion state', ac=False, math=True)
change('043.Qalg_barred_Q', r'\unsure{\mathrm{Gal}/\mathbb Q}', r'\overline{\mathbf{Q}}', r'/\overline{\mathbb Q}',
       'A separate horizontal bar lies above the lower-line Q after the slash. It belongs to that denominator, not as an underline for an isolated object on the preceding line. The Q contains a doubled diagonal/stem stroke.',
       'qalg_caption', kind='misread symbol or index', ah=False, math=True)
change('043.comb_abbreviation', r'\unsure{quadr.}', r'\emph{à bord} \ill{}', r'\uline{à bord} \unsure{quadr.|qcq.}',
       'The underline ends below bord. A separate short q-initial abbreviation follows, with a descending first stroke and compressed middle letters; quadr./qcq. remain alternatives. It is not physically blank or wholly unreadable.',
       'comb_caption', 'medium', kind=r'readable ink left as \ill{}', ac=False)
change('043.Lego_label', r'\unsure{\mathrm{L\acute ego}}', r'\mathrm{Lego}', r'\mathrm{L\acute ego}',
       'Despite the retracing, the lowered label retains L, looped e, descending g and round o. A detached short accent lies above the e.',
       'lower_links2', kind='misread symbol or index', math=True, certainty=True)
change('043.Lego_les_10', 'les 10 pièces', r'\uncertain{10} pièces', 'les 10 pièces',
       'The short connected l-e-s group stands before the tall 1 and round 0; it is fully visible in the overlapping lower-links crop. Both digits are plain.',
       'lower_links2', ac=False)
change('043.Lego_du', 'pièces en jeu', 'pièces du jeu', 'pièces du jeu',
       'Between pièces and jeu is a small looped d followed by u, not the low e-n sequence of en.',
       'lego_caption', ah=False)
change('043.P_double_stem', r'\mathbb T_{\mathrm P}', r'\mathbb{T}_{\mathbb{P}}', r'\mathbb T_{\mathbb P}',
       'The final lowered P has two parallel upright strokes enclosing a white vertical channel beneath the bowl, so its doubled alphabet is visible rather than inferred from the object name.',
       'lower_links2', kind='misread symbol or index', ah=False, math=True)
change('043.pantalonique', r'\unsure{pantalonique}', 'pantalonnique', 'pantalonique',
       'Between the rounded o after the tall l and the dotted i there is one n-shaped hump. No second n is written.',
       'pant_caption', certainty=True)
change('043.pant_phrase', r'\unsure{comme seules pièces les|une seule pièce dite}', 'comme seules pièces les', 'comme seules pièces les',
       'The line has the separate low c-o-m-m-e group, then s-e-u-l-e-s with a tall looped l, then pièces and a final looped l-e-s. The sequence is not une seule pièce dite.',
       'pant_caption', ah=False, certainty=True)
change('043.pant_struck_word', r"\deleted{``pantalon''}", r'\struck{pantalons}', r"\deleted{``\unsure{pantalon|pantalons}''}",
       'The cancellation crosses the word beginning with p and containing the tall t/l strokes. The terminal ending is covered and singular/plural cannot be certified. Short quotation ticks are retained with the tentative word.',
       'pant_caption', 'low', ac=False)
change('043.foliation', r'\mspage{42}', None, r'\margin{42}',
       'The pale handwritten bottom-left number has the open angled/crossed form of 4 followed by a curved 2 with a broad baseline. Its origin is unassigned, so it is retained as marginal foliation.',
       'foliation', kind='omission', ac=False)
change('043.reverse_listing_upper', span(C, r'\unsure{\texttt{24 CNU}}', r'\illegible{9}'), None, '',
       'All of these pale mechanical rows have laterally reversed character shapes and run behind the dark front handwriting. Their thin blue-gray strokes are bleed-through, not front text; no attempt is made to complete their words.',
       'bleed_upper', kind='text not on the page', ah=False)
change('043.reverse_listing_lower', C[C.index(r'\unsure{\texttt{ECRIT PAR}}'):].strip(), None, '',
       'The lower pale listing continues in mirrored monospaced letters behind the manuscript and under the final captions. It is the same reverse-side layer, not a second front text block.',
       'bleed_lower', kind='text not on the page', ah=False)

decisions = []
def decision(mid, choice, reading, ink, crop, confidence='high'):
    decisions.append(dict(id=mid, decision=choice, reading=reading, ink=ink,
                          crop='crops/148_scan043_' + crop + '.png', box=boxes[crop], confidence=confidence))

decision('M0644', 'undecided', r'\unsure{réalis.}', 'Tall l-like stroke favors réalis.; compressed first letters remain inseparable.', 'paragraph', 'medium')
decision('M0645', 'first', r'\mathbb T', 'Two parallel uprights under one long bar, with a white channel.', 'paragraph')
decision('M0646', 'first', r'\mathbb T', 'The diagram top T repeats the doubled upright explicitly.', 'upper_links')
decision('M0647', 'other', 'toriques', 'Short t-o-r-i-q-u-e-s sequence, including final low s; no topolog- sequence.', 'top_caption')
decision('M0648', 'other', 'toriques', 'The live word after the separate entangled glyph has t-o-r-i-q-u-e-s.', 'analytic_caption')
decision('M0649', 'undecided', r'\unsure{\mathbb C^\infty?}', 'Doubled C is clear; the raised loop and further question-like stroke are not securely classified.', 'analytic_margin', 'low')
decision('M0650', 'undecided', r'\unsure{drs.|dirs.}', 'Initial d loop and terminal s-like stroke are visible; compressed middle may include i.', 'upper_links', 'medium')
decision('M0651', 'undecided', r'\unsure{qconq.|qcq.}', 'A descending initial q and short rounded middle remain; the full abbreviation is not secure.', 'upper_links', 'medium')
decision('M0652', 'first', 'déc.', 'Looped d, low e and open c end followed by a separate dot.', 'hyp_row')
decision('M0653', 'undecided', r'\unsure{de cercles|des cercles|du cercle}', 'Low c-e-r-c followed by tall l favors cercle(s); preposition and ending remain compressed.', 'calg_caption', 'medium')
decision('M0654', 'undecided', r'\unsure{propagation}', 'The p/descending-loop/raised-t sequence favors propagation, but the compressed letters are not all certified.', 'qalg_caption', 'medium')
decision('M0655', 'undecided', r'\unsure{descente|descendant}', 'Initial d and final tall t plus low e favor descente; middle humps are compressed.', 'qalg_caption', 'medium')
decision('M0656', 'undecided', r'\unsure{\mathrm{Gal}|\deleted{\mathrm G}\mathrm{al}}/\overline{\mathbb Q}', 'al and slash/barred Q are clear; the overtraced G may be live or cancelled.', 'qalg_caption', 'medium')
decision('M0657', 'undecided', r'\unsure{quadr.|qcq.}', 'Descending q and abbreviated low letters visible, but middle forms do not distinguish quadr. from qcq.', 'comb_caption', 'medium')
decision('M0658', 'first', r'\mathrm{L\acute ego}', 'L-e-g-o survives retracing, and a short detached accent is above e.', 'lower_links2')
decision('M0659', 'first', 'pantalonique', 'One n-shaped hump lies between o and dotted i.', 'pant_caption')
decision('M0660', 'first', 'comme seules pièces les', 'Four separate groups read comme / seules / pièces / les; tall l and dotted/accented pieces distinguish them.', 'pant_caption')
decision('M0661', 'undecided', r'\unsure{triades|triade}', 'The t/r-i-a-d-e sequence is legible; the final low stroke may be s or the word exit before the point.', 'pant_caption', 'medium')
for n in range(662, 679):
    decision(f'M{n:04d}', 'other', '', 'Pale monospaced characters are laterally reversed and show through behind the front handwriting; they are not source text on this face.',
             'bleed_upper' if n <= 669 else 'bleed_lower')

inventory = []
def inv(element, kind, position, words, hand='main manuscript hand'):
    inventory.append(dict(element=element, kind=kind, position=position, first_words_or_objects=words,
                          sheet_kind='reused_typed', hand=hand, transcribed='yes'))

inv('043.I01', 'text', 'top two baselines', r'\unsure{les|Les} douze avatars principaux de la \unsure{Tours|Tour}')
inv('043.I02', 'deletion', 'top, after title colon', r'\deleted{\unsure{systèmes|système} de groupoïdes}')
inv('043.I03', 'text', 'prelude above diagram', r'groupoïde $\mathrm{RTD}\ldots$ avec structures')
inv('043.I04', 'insertion', 'interlinear after structures', r"\inserted{(``les 10 opérations''), \unsure{réalis.}}")
inv('043.I05', 'deletion', 'prelude after dont le', r'\deleted{\unsure{représentant}}')
inv('043.I06', 'deletion', 'prelude before live doubled T', r'\deleted{\unsure{\mathrm{RTD}}}')
inv('043.I07', 'display', 'prelude ending', r'\deleted{\unsure{\mathrm{RTD}}},\ \mathbb T_{\mathrm{top}}')
inv('043.I08', 'diagram', 'left column and aligned captions, most of page', r'\mathbb T_{\mathrm{top}},\mathbb T_{\mathrm{diff}},\mathbb T_{\mathrm{an}},\mathbb T_{\mathrm{hyp}},\mathbb T_{\mathbb C\mathrm{alg}},\mathbb T_{\overline{\mathbb Q}\text{-}\mathrm{alg}},\mathbb T_{\mathrm{comb}},\mathbb T_{\mathrm{L\acute ego}},\mathbb T_{\mathbb P};\mathbb T^{\prime}_{\mathrm{diff}},\mathbb T^{\prime}_{\mathrm{an}},\mathbb T^{\prime}_{\mathrm{hyp}}')
inv('043.I09', 'text', 'right of top diagram label', 'cas topologique (à bord')
inv('043.I10', 'deletion', 'top caption after bord', r'\deleted{\unsure{géod.}}')
inv('043.I11', 'margin note', 'far right, top caption', 'découpage top.')
inv('043.I12', 'text', 'right of differentiable label', 'cas différentiable (à')
inv('043.I13', 'deletion', 'differentiable caption old baseline', r'\deleted{pts \unsure{trous} pointés)}')
inv('043.I14', 'insertion', 'above differentiable old baseline', r'\inserted{bord toriques)}')
inv('043.I15', 'deletion', 'line below differentiable caption', r'\deleted{(avec \unsure{peu de|presque} pts marqués)}')
inv('043.I16', 'margin note', 'far right, differentiable caption', 'déc. diff')
inv('043.I17', 'margin note', 'left between primed differentiable and analytic objects', r'à pts marqués et \unsure{drs.|dirs.} tangts complexes \unsure{qconq.|qcq.}')
inv('043.I18', 'text', 'right of analytic label', r'cas \inserted{$\mathbb C$-}analytique')
inv('043.I19', 'insertion', 'above beginning of analytique', r'\inserted{\mathbb C\text{-}}')
inv('043.I20', 'deletion', 'analytic caption, possible crossed glyph before toriques', r'\unsure{\deleted{g}|g}')
inv('043.I21', 'margin note', 'far right, analytic caption', r'déc. en $\unsure{\mathbb C^\infty?}$')
inv('043.I22', 'text', 'right of hyperbolic label', 'cas hyperbolique (à bord géodésique)')
inv('043.I23', 'margin note', 'far right, hyperbolic caption', 'déc. hyp.')
inv('043.I24', 'text', 'right of complex-algebraic label, four lines', r'cas $\mathbb C$-algébrique (courbes MD,')
inv('043.I25', 'deletion', 'complex-algebraic caption, second line', r'\deleted{rigidification}')
inv('043.I26', 'text', 'right of rational-algebraic label, two lines', r'cas $\overline{\mathbb Q}$-alg. (\unsure{propagation}')
inv('043.I27', 'deletion', 'possible cancelled initial G before al', r'\unsure{\mathrm{Gal}|\deleted{\mathrm G}\mathrm{al}}')
inv('043.I28', 'text', 'right of combinatorial label, two lines', r'cas combinatoire, via cartes orientées \uline{à bord}')
inv('043.I29', 'text', 'right of Légo label, two lines', "cas combinatoire ``Légo'', avec les 10 pièces du jeu")
inv('043.I30', 'text', 'right of final P label, three lines', "cas combinatoire ``pantalonique'', avec comme seules pièces les")
inv('043.I31', 'deletion', 'bottom caption before triades/triade', r"\deleted{``\unsure{pantalon|pantalons}''}")
inv('043.I32', 'margin note', 'bottom left', '42', 'pale foliation hand, origin unassigned')

unresolved = [
    dict(place='header initial', reading=r'\unsure{les|Les}', issue='Bare tall initial stroke does not securely distinguish lower-case l from capital L.', alternatives=['les','Les'], confidence='medium'),
    dict(place='header Tour(s)', reading=r'\unsure{Tours|Tour}', issue='Heavy final zigzag favors s but may be a retouched r exit.', alternatives=['Tours','Tour'], confidence='medium'),
    dict(place='struck header noun', reading=r'\deleted{\unsure{systèmes|système} de groupoïdes}', issue='The terminal s-like stroke lies on the cancellation.', alternatives=['systèmes','système'], confidence='low'),
    dict(place='interlinear short word', reading=r'\unsure{réalis.}', issue='Tall l favors réalis.; the compressed first letters remain uncertain.', alternatives=['réalis.','ou autres'], confidence='medium'),
    dict(place='struck représentant', reading=r'\deleted{\unsure{représentant}}', issue='The heavy strike and edge compression prevent certification of every letter.', alternatives=['représentant'], confidence='low'),
    dict(place='struck capitals in prelude', reading=r'\deleted{\unsure{\mathrm{RTD}}}', issue='Three capital-sized remnants are crossed by diagonal hatching; RTD remains tentative.', alternatives=[r'\mathrm{RTD}'], confidence='low'),
    dict(place='struck word in top caption', reading=r'\deleted{\unsure{géod.}}', issue='The first ascender and descending loop survive, but the middle letters are covered.', alternatives=['géod.'], confidence='low'),
    dict(place='struck differentiable middle word', reading=r'\deleted{pts \unsure{trous} pointés)}', issue='Two horizontal cancellation strokes obscure the middle word.', alternatives=['trous'], confidence='low'),
    dict(place='lower differentiable cancellation', reading=r'\deleted{(avec \unsure{peu de|presque} pts marqués)}', issue='Short p-e-u and d-e groups are favored, but the cancelling line covers the joins.', alternatives=['peu de','presque'], confidence='medium'),
    dict(place='left note first abbreviation', reading=r'\unsure{drs.|dirs.}', issue='The compressed middle may include an i; not expanded in the text.', alternatives=['drs.','dirs.'], confidence='medium'),
    dict(place='left note last abbreviation', reading=r'\unsure{qconq.|qcq.}', issue='The number of rounded middle letters is uncertain.', alternatives=['qconq.','qcq.'], confidence='medium'),
    dict(place='analytic border initial glyph', reading=r'\unsure{\deleted{g}|g}toriques', issue='A g-like form precedes toriques; the small upper cross may be cancellation or overtracing.', alternatives=[r'\deleted{g}toriques','gtoriques'], confidence='low'),
    dict(place='analytic margin whole formula', reading=r'\unsure{\mathbb C^\infty?}', issue='Doubled C is clear; raised looped and question-like marks are not securely identified. Infinity is a tentative witness reading, not a settled exponent.', alternatives=[r'\mathbb C^\infty?',r'\mathbb C^{?}'], confidence='low'),
    dict(place='complex-algebraic propagation phrase', reading=r'\unsure{de cercles|des cercles|du cercle}', issue='The tall near-final l favors cercle(s); short preposition and final s are compressed.', alternatives=['de cercles','des cercles','du cercle'], confidence='medium'),
    dict(place='rational-algebraic first word', reading=r'\unsure{propagation}', issue='Compressed letter joins favor propagation but cannot all be certified.', alternatives=['propagation','pour opération','pour y obtenir'], confidence='medium'),
    dict(place='rational-algebraic second line', reading=r'\unsure{descente|descendant}', issue='Initial d and final t-e favor descente, but the middle is compressed.', alternatives=['descente','descendant'], confidence='medium'),
    dict(place='Gal initial state', reading=r'\unsure{\mathrm{Gal}|\deleted{\mathrm G}\mathrm{al}}/\overline{\mathbb Q}', issue='G is heavily overtraced; al and the barred denominator Q are clear. Retouching versus cancellation of G is unresolved.', alternatives=[r'\mathrm{Gal}/\overline{\mathbb Q}',r'\deleted{\mathrm G}\mathrm{al}/\overline{\mathbb Q}'], confidence='medium'),
    dict(place='combinatorial abbreviation', reading=r'\unsure{quadr.|qcq.}', issue='The descending q is clear but compressed middle strokes do not select the abbreviation.', alternatives=['quadr.','qcq.'], confidence='medium'),
    dict(place='cancelled pantalon ending', reading=r"\deleted{``\unsure{pantalon|pantalons}''}", issue='Strike covers the terminal ending; singular/plural is unresolved.', alternatives=['pantalon','pantalons'], confidence='low'),
    dict(place='live triade ending', reading=r'\unsure{triades|triade}', issue='Final low stroke may be s or a word exit before the point.', alternatives=['triades','triade'], confidence='medium'),
]

notes = [
    dict(id='N043.1', text='The page presents twelve principal avatars of the Teichmüller tower in a vertical diagram: nine main labels and three primed variants. It supplies descriptive captions and operations/decomposition notes, without proving the relationships drawn.'),
    dict(id='N043.2', text='Counting the nine main objects and the three primed objects gives twelve, in agreement with the written heading. Only this enumeration was checked mathematically; no theorem about the category changes or the ten operations/pieces was proved from this isolated page.'),
    dict(id='N043.3', text='The final stroke in Tours may be an s even after la. The possible mismatch is preserved, not repaired by French agreement. Singular topologique, analytique and géodésique are retained from their visible endings.'),
    dict(id='N043.4', text='The short arrow above the left four-line annotation does not have a shaft through the annotation to the primed analytic object. The transcription keeps the short arrow literally and does not manufacture the longer map supplied by C.'),
    dict(id='N043.5', text='The topological and complex-algebraic captions have no visible closing parenthesis. The differentiable correction has two distinct closing curves: one in the cancelled old passage and one in the raised live replacement.'),
    dict(id='N043.6', text='The pale blue-gray mechanical listing is laterally reversed bleed-through behind the front manuscript and is excluded. The separate pale number 42 is readable front foliation of unassigned origin and is retained in the margin.'),
    dict(id='N043.7', text='H’s preliminary sheet description, layout synopsis, item-list punctuation and final section heading are editorial apparatus, not additional manuscript words. They were reviewed but not copied into the source transcription.'),
    dict(id='N043.8', text='The analytic margin exponent-like marks, the propagation/cercle(s) wording, the descente/descendant wording and two possible cancelled initials remain unresolved. No expected mathematical construction was substituted for the ink.'),
]

checks = [dict(statement_id='N043.2', date='2026-11-21',
               who='Reader B; GPT-6 Astra Pro; effort not exposed; run SP82_C13_148',
               type='computation or formal certificate',
               outcome='Enumerated the nine main labels top, diff, an, hyp, C alg, Qbar-alg, comb, Légo and P, and the three primed labels diff, an and hyp; computed 9 + 3 = 12. This agrees with douze in the heading. No equivalence or operations-count claim was certified.')]

hand_log = [
    dict(habit='The tower letter T is written with two parallel vertical strokes under a single long top bar.', pages=[43], scope='holds_at_every_observed_occurrence', holds_at_every_observed_occurrence=True,
         observed_scope='The live T_top in the prelude and all twelve live diagram T labels on scan 043.',
         witness_effect='Resolves C M0645 and M0646 as mathbb T; confirms the same alphabet in the remaining labels. The single-stem T in RTD is a different observed token and is not included in this habit.'),
    dict(habit='Paired comparison arrows are drawn as two separate shafts with full heads in opposite directions.', pages=[43], scope='holds_at_every_observed_occurrence', holds_at_every_observed_occurrence=True,
         observed_scope='All three primed/unprimed comparisons on scan 043.',
         witness_effect='C’s two-arrow construction is retained; H’s single double-ended arrow and its description as half-arrows do not reproduce the visible shafts and heads.'),
]

notation = [
    dict(form=r'\mathbb T_{\mathrm{top}},\mathbb T_{\mathrm{diff}},\mathbb T_{\mathrm{an}},\mathbb T_{\mathrm{hyp}}', observation='Live doubled-T labels for the four upper cases; primes distinguish the three left-column variants.', pages=[43]),
    dict(form=r'\mathbb T_{\mathbb C\mathrm{alg}},\mathbb T_{\overline{\mathbb Q}\text{-}\mathrm{alg}}', observation='No hyphen in the complex-algebraic lower label; explicit hyphen after barred Q in the next label.', pages=[43]),
    dict(form=r'\mathbb T_{\mathrm{comb}},\mathbb T_{\mathrm{L\acute ego}},\mathbb T_{\mathbb P}', observation='The Légo index has an accent; the final lowered P has an explicit doubled stem.', pages=[43]),
    dict(form=r'\mathrm{RTD}\ldots', observation='Plain single-stem letters in the prelude, followed by three baseline dots.', pages=[43]),
]

abbreviations = [
    dict(form='pts', expansion='points'),
    dict(form='tangts', expansion='tangents'),
    dict(form='déc.', expansion='découpage'),
    dict(form='top.', expansion='topologique'),
    dict(form='diff', expansion='différentiable'),
    dict(form='hyp.', expansion='hyperbolique'),
    dict(form='alg.', expansion='algébrique'),
    dict(form='comb', expansion='combinatoire'),
    dict(form=r'\unsure{réalis.}', expansion='réalisations, if the tentative reading is correct'),
    dict(form=r'\unsure{drs.|dirs.}', expansion='directions, if this abbreviation is correctly read'),
    dict(form=r'\unsure{qconq.|qcq.}', expansion='quelconques, if this abbreviation is correctly read'),
]

second_boxes = []
def sb(key, kind, box, reading):
    second_boxes.append(dict(box=key, kind=kind, x0=box[0], y0=box[1], x1=box[2], y1=box[3], reading=reading))

sb('043.B01', 'different words and deletion', [281,25,1480,151], r'\unsure{les|Les} douze avatars principaux de la \unsure{Tours|Tour} de Teichmüller : \deleted{\unsure{systèmes|système} de groupoïdes}')
sb('043.B02', 'handwritten paragraph with insertions, deletions, formulas and number', boxes['paragraph'],
   candidate[candidate.index('groupoïde $'):candidate.index('\n\n\\diagram')].strip())
sb('043.B07', 'diagram and margin note', boxes['upper_links'],
   r'''\begin{tikzcd}[ampersand replacement=\&]
\&\mathbb T_{\mathrm{top}}\\
\mathbb T'_{\mathrm{diff}}\arrow[r,shift left]\arrow[from=r,shift left]\&\mathbb T_{\mathrm{diff}}\arrow[u]\\
\begin{gathered}\uparrow\\\text{à pts marqués}\\\text{et \unsure{drs.|dirs.} tangts}\\\text{complexes}\\\text{\unsure{qconq.|qcq.}}\end{gathered}\&\mathbb T_{\mathrm{an}}\arrow[u]\\
\mathbb T'_{\mathrm{an}}\arrow[ur,shift left]\arrow[from=ur,shift left]\&\\
\&\mathbb T_{\mathrm{hyp}}\arrow[uu]\\
\mathbb T'_{\mathrm{hyp}}\arrow[uu]\arrow[ur,shift left]\arrow[from=ur,shift left]\&
\end{tikzcd}''')
sb('043.B08', 'different words and deletion', boxes['top_caption'], r'cas topologique (à bord \deleted{\unsure{géod.}} toriques')
sb('043.B09', 'margin note', boxes['top_margin'], 'découpage top.')
sb('043.B10', 'insertions and deletions', boxes['diff_caption'], r'cas différentiable (à \deleted{pts \unsure{trous} pointés)} \inserted{bord toriques)} \deleted{(avec \unsure{peu de|presque} pts marqués)}')
sb('043.B11', 'margin note', boxes['diff_margin'], 'déc. diff')
sb('043.B12', 'insertion and possible deletion', boxes['analytic_caption'], r'cas $\inserted{\mathbb C\text{-}}$analytique (à bord \unsure{\deleted{g}|g}toriques)')
sb('043.B13', 'margin note and whole doubtful formula', boxes['analytic_margin'], r'déc. en $\unsure{\mathbb C^\infty?}$')
sb('043.B14', 'different word passage and margin note', boxes['hyp_row'], r'cas hyperbolique (à bord géodésique)\quad\text{déc. hyp.}')
sb('043.B15', 'whole formula', [287,1115,435,1230], r'\mathbb T_{\mathbb C\mathrm{alg}}')
sb('043.B16', 'different words and deletion', boxes['calg_caption'], r"cas $\mathbb C$-algébrique (courbes MD, munies d'une \deleted{rigidification} de propagation \unsure{de cercles|des cercles|du cercle} aux pts doubles, plus pts marqués")
sb('043.B17', 'whole formula', [288,1374,477,1495], r'\mathbb T_{\overline{\mathbb Q}\text{-}\mathrm{alg}}')
sb('043.B18', 'different words and whole doubtful formula', boxes['qalg_caption'], r'cas $\overline{\mathbb Q}$-alg. (\unsure{propagation} \unsure{descente|descendant} $\unsure{\mathrm{Gal}|\deleted{\mathrm G}\mathrm{al}}/\overline{\mathbb Q}$)')
sb('043.B19', 'underline and different word', boxes['comb_caption'], r'cas combinatoire, via cartes orientées \uline{à bord} \unsure{quadr.|qcq.}, avec sommets marqués')
sb('043.B20', 'whole formula', [318,1580,455,1655], r'\mathbb T_{\mathrm{comb}}')
sb('043.B21', 'whole formula', [325,1807,460,1905], r'\mathbb T_{\mathrm{L\acute ego}}')
sb('043.B22', 'different words and handwritten number', [550,1783,1411,1958], "cas combinatoire ``Légo'', avec les 10 pièces du jeu")
sb('043.B23', 'whole formula', [331,2080,405,2174], r'\mathbb T_{\mathbb P}')
sb('043.B24', 'different words and deletion', boxes['pant_caption'], r"cas combinatoire ``pantalonique'', avec comme seules pièces les \deleted{``\unsure{pantalon|pantalons}''} \unsure{triades|triade}.")
sb('043.B25', 'margin note and handwritten number', boxes['foliation'], r'\margin{42}')

review_map = {
925: ('editorial apparatus', []), 926: ('false separate cancellation removed', ['043.header_false_cancellation']),
927: ('terminal ending remains doubtful', ['043.header_struck_systemes']),
928: ('plain letters and baseline dots', ['043.prelude_RTD']),
929: ('visible quotation strokes retained', ['043.operations_quotes']), 930: ('visible quotation strokes retained', ['043.operations_quotes']),
931: ('tentative réalis. and interlinear placement; no extra deleted token', ['043.operations_interline','043.prelude_false_extra_deletion']),
932: ('un from ink', ['043.prelude_un']), 933: ('no comma at leader crossing', ['043.prelude_groupoide_comma']),
934: ('tentative cancelled capitals and live comma retained', ['043.prelude_struck_RTD_letters','043.prelude_live_comma']),
935: ('macro/layout syntax only', []), 936: ('macro/layout syntax only', []), 937: ('macro/layout syntax only', []),
938: ('caption and right note transcribed at diagram row', ['043.top_singular','043.top_toriques','043.top_false_close','043.top_margin']),
939: ('two separate arrow shafts', ['043.paired_arrows']),
940: ('caption cancellation and raised replacement read from ink', ['043.diff_old_close','043.diff_inserted_border','043.diff_struck_parenthesis','043.diff_margin']),
941: ('analytic caption and staggered left annotation retained', ['043.an_staggered_pair','043.short_annotation_arrow','043.left_annotation_words','043.analytic_singular','043.analytic_inserted_C','043.analytic_g_state','043.analytic_toriques','043.analytic_margin']),
942: ('two separate diagonal arrow shafts; primed hyp lower than main hyp', ['043.paired_arrows','043.hyp_staggered_pair']),
943: ('same main-arrow endpoints; uu compensates for staggered analytic row', []),
944: ('caption layout is editorial, actual words adjudicated separately', ['043.hyp_singular','043.hyp_dec','043.Calg_label_no_hyphen']),
945: ('singular ending retained', ['043.hyp_singular']), 946: ('déc. resolved', ['043.hyp_dec']),
947: ('macro/item-list punctuation only', []),
948: ('live de and following propagation retained', ['043.Calg_de_propagation']),
949: ('cercles alternatives from visible low letters and tall l', ['043.Calg_cercles']),
950: ('cercles alternatives remain uncertain', ['043.Calg_cercles']),
951: ('no closing parenthesis at end of source caption', ['043.Calg_false_close']),
952: ('propagation tentative; no separate underlined O', ['043.Qalg_propagation']),
953: ('descente/descendant and retouched/cancelled G remain open', ['043.Qalg_descente','043.Qalg_Gal_state','043.Qalg_barred_Q']),
954: ('macro/item-list punctuation only', []),
955: ('abbreviated visible word retained with alternatives', ['043.comb_abbreviation']),
956: ('macro/item-list punctuation only', []),
957: ('double-tick quotation convention from ink; Légo caption agrees', []),
958: ('les present before 10', ['043.Lego_les_10']),
959: ('du from ink', ['043.Lego_du']),
960: ('layout syntax; doubled final P separately recorded', ['043.P_double_stem']),
961: ('one n in pantalonique', ['043.pantalonique']),
962: ('live phrase resolved; cancelled singular/plural remains open', ['043.pant_phrase','043.pant_struck_word']),
963: ('triades/triade ending unresolved; retained in place', []),
964: ('folio retained; mirrored printing excluded; H section heading is editorial', ['043.foliation','043.reverse_listing_upper','043.reverse_listing_lower']),
}
differences_review = []
for row in diffs:
    n = int(row['source_row'])
    outcome, refs = review_map[n]
    differences_review.append(dict(source_row=n, c=row['witness C'], h=row['witness H'], decision=outcome, evidence=refs))

logical_line_counts = {
    'title_baselines_including_adjacent_cancelled_phrase': 2,
    'prelude_baselines': 3,
    'prelude_interlinear_addition': 1,
    'topological_caption': 1,
    'topological_margin': 2,
    'differentiable_baseline': 1,
    'differentiable_raised_replacement': 1,
    'differentiable_cancelled_lower_line': 1,
    'differentiable_margin': 1,
    'left_annotation': 4,
    'analytic_caption_baseline': 1,
    'analytic_raised_prefix': 1,
    'analytic_margin': 2,
    'hyperbolic_caption': 1,
    'hyperbolic_margin': 1,
    'complex_algebraic_caption': 4,
    'rational_algebraic_caption': 2,
    'combinatorial_caption': 2,
    'Lego_caption': 2,
    'pantalonique_caption': 3,
    'foliation': 1,
}

result = dict(
    scan=43, reader='B', model='GPT-6 Astra Pro', reasoning_effort='not exposed', run='SP82_C13_148',
    lines_read=sum(logical_line_counts.values()),
    lines_read_basis='Front-side textual baselines or separate short written runs, including interlinear additions, the raised C- prefix, marginal lines and foliation. The cancelled header phrase shares the second title baseline and is counted there. The twelve diagram labels and all arrows were audited separately and are not added as textual lines; reverse bleed-through is excluded.',
    logical_line_counts=logical_line_counts,
    reading_workflow=[
        'Whole source once for layout and front/reverse layers.',
        'Native half 1 once, every header/prelude line and upper diagram object, arrow, caption, margin, insertion and deletion against C.',
        'Native half 2 once, every lower diagram object, arrow, caption and correction, the foliation and the pale reversed listing against C.',
        'All 20 saved evidence crops actually viewed; selected existing crops reused to compare strokes, without making replacement crops.',
    ],
    changes=changes, decisions=decisions, inventory=inventory, unresolved=unresolved,
    notes=notes, checks=checks, hand_log=hand_log, notation=notation, abbreviations=abbreviations,
    second_boxes=second_boxes, differences_review=differences_review,
    reading_procedure=dict(whole_page_views=1, native_half_views=[1,1], crop_count=20,
                           every_crop_viewed=True, new_crops_after_first_set=0,
                           ocr=False, web_research=False, tex_compilation=False,
                           source_size=[1542,2243],
                           diagram_audit='Counted the nine main and three primed labels. Checked all eight main upward arrows, the left hyp-to-an upward arrow, all three opposed pairs and the separate short annotation arrow; rechecked heads and endpoints in the saved crops.',
                           output_scope='Reader output only; consolidated files not changed.')
)

errors = []
for row in changes:
    if row['c'] is not None and row['c'] not in C:
        errors.append([row['id'], 'C snippet not exact', row['c']])
    if row['h'] is not None and row['h'] not in H:
        errors.append([row['id'], 'H snippet not exact', row['h']])
assert len(decisions) == len(marks) == 35
assert {d['id'] for d in decisions} == {m['id'] for m in marks}
assert len({d['id'] for d in decisions}) == len(decisions)
assert len(differences_review) == len(diffs) == 40
assert len({b['box'] for b in second_boxes}) == len(second_boxes)
for b in second_boxes:
    assert 0 <= b['x0'] < b['x1'] <= 1542
    assert 0 <= b['y0'] < b['y1'] <= 2243
for row in changes + decisions:
    assert row['box'] in boxes.values()
    assert (OUT.parent.parent / row['crop']).exists()
assert all(set(n) == {'id','text'} for n in notes)
assert all(c['type'] in ['targeted proof check','computation or formal certificate'] for c in checks)
(OUT / 'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
(OUT / 'validation.json').write_text(json.dumps(dict(exact_snippet_errors=errors, counts={k:len(result[k]) for k in ['changes','decisions','inventory','unresolved','checks','second_boxes','differences_review']}), ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(exact_snippet_errors=errors, counts={k:len(result[k]) for k in ['changes','decisions','inventory','unresolved','checks','second_boxes','differences_review']}), ensure_ascii=False, indent=2))
