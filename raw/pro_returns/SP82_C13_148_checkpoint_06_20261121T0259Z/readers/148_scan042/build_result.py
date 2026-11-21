from pathlib import Path
import csv
import json
import re

OUT = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan042')
PACKET = Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan042')
candidate = (OUT / 'candidate.tex').read_text()
manifest = json.loads((OUT / 'crop_plan.json').read_text())
crops = {r['label']: r for r in manifest}

def evidence(label):
    r = crops[label]
    return {'crop': r['crop'], 'box': r['box']}

figures = re.findall(r'\\figure\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}', candidate, re.S)
objects_figure, catalogue_figure = figures
diamond = re.search(r'\\diagram\{\\begin\{tikzcd\}.*?\\end\{tikzcd\}\}', candidate, re.S).group()

changes = []
def change(place, c, h, final, ink, label, confidence, kind, against_c, against_h, math=False):
    changes.append(dict(place=place, c=c, h=h, final=final, ink=ink, **evidence(label),
                        confidence=confidence, kind=kind, against_c=against_c,
                        against_h=against_h, math=math))

change('Heading: initial letter', 'opérations de recollage / sommes',
       'Opérations de recollage / sommes', 'opérations de recollage / sommes',
       'The initial closed o occupies the body-height band; the accent and the later tall t and l strokes rise above it. The slash is a separate long oblique stroke.',
       'heading', 'medium', 'misread word', False, True)
change('Objects heading: initial letter', 'Objets; diagrammes', 'objets; diagrammes',
       'objets; diagrammes',
       'The first small loop stays below the following tall b stroke. The two separated marks after objets form the written semicolon.',
       'objects', 'high', 'misread word', True, False)
change('Objects list: Sommets initial', 'Sommets de marquage', 'sommets de marquage',
       r'Sommets de \uline{marquage}',
       'The initial broad S rises above the following low o and m sequence. The rule runs below marquage, across its descending strokes, without deleting the word.',
       'objects', 'medium', 'misread word', False, True)
change('Objects group: two left braces and their spans',
       'One brace joining the two circle lines; no outer brace around the objects group.',
       'Editorial description of one brace joining the four lines after objets; diagrammes.',
       objects_figure,
       'There are two distinct ink braces. The large left brace begins above the objets baseline and ends below cercles marqués et non marqués. A shorter inner brace joins only cercles de raccord and cercles de découpage.',
       'objects', 'high', 'drawing or diagram', True, True)
change('Objects list: parenthetical continuation', '(périphériques, intérieurs)',
       '(périphériques / internes)', r'(périphériques\\intérieurs',
       'The lower word has the extended accented sequence after int- and ends in the longer -ieurs run. The tall opening parenthesis is visible at the left. There is no distinct comma or slash after périphériques, and the final s of intérieurs is not followed by a separate closing-parenthesis stroke.',
       'objects', 'high', 'misread word', True, True)
change('Condition: cancelled word', r'\deleted{\unsure{de}}', r'\struck{\ill{}}',
       r'\deleted{\unsure{de}}',
       'A compact word-sized block has upright remnants crossed by dense diagonal strokes. Those remnants admit de, but the cancellation prevents a complete letter-by-letter resolution; the inherited doubt is retained.',
       'condition', 'low', r'readable ink left as \ill{}', False, True)
change('Left diamond: cancelled letters before the top vertex', r'\deleted{\unsure{SD}}',
       'Absent from the node; the editorial note calls a preceding overwritten letter illegible.',
       r'\deleted{\unsure{SD}}',
       'The blackened group before the live calligraphic glyph contains several transverse cancellation strokes, a curved left remnant and an upright with a rounded right side. SD remains only a tentative reading under that hatching.',
       'diamonds', 'low', r'readable ink left as \ill{}', False, True, True)
change('Left diamond: live top calligraphic glyph, M0643', r'\unsure{\mathcal T}',
       r'\mathcal T', r'\mathcal T',
       'The angular upper cap, short rightward turn and broad lower return match the calligraphic T forms after S, D and SD on this same sheet. The top live glyph is separate from the cancelled block to its left; its letter strokes are not hidden by that cancellation.',
       'diamonds', 'medium', 'misread symbol or index', True, False, True)
changes[-1]['mark_ids'] = ['M0643']
change('Right diamond: top vertex', 't', r'\mathbb L', r'\unsure{t|\mathbb L}',
       'Two close upright strokes are joined at the top; a distinct crossbar projects right around mid-height, and a bent foot projects right below. The crossbar favors t, while the doubled outline leaves the alphabet unresolved.',
       'diamonds', 'medium', 'misread symbol or index', False, True, True)
change('Right diamond: left vertex', 'st', r'S\mathbb L', r's\unsure{t|\mathbb L}',
       'The initial s is visibly shorter than the following doubled upright and than the large S in the left diamond. The following glyph repeats the middle crossbar and rightward foot of the top right glyph.',
       'diamonds', 'medium', 'misread symbol or index', False, True, True)
change('Right diamond: right vertex', 'dt', r'd\mathbb L', r'd\unsure{t|\mathbb L}',
       'A small lower loop and ascending staff form d. The following doubled upright again has a middle crossbar and a lower right foot; its t-versus-L reading remains explicit.',
       'diamonds', 'medium', 'misread symbol or index', False, True, True)
change('Right diamond: bottom vertex', 'sdt', r'Sd\mathbb L', r'sd\unsure{t|\mathbb L}',
       'The first s is small, followed by the loop-and-staff d. The last tall sign repeats the crossbar and bent foot seen at the other three vertices.',
       'diamonds', 'medium', 'misread symbol or index', False, True, True)
change('Diamonds: origin of the upper middle connecting arrow',
       r'S\mathcal T\arrow[rrr,bend left=20]', r'D\mathcal T\arrow[rr]',
       r'D\mathcal T\arrow[rr,bend left=15]',
       'The thin stroke begins immediately above D followed by the calligraphic letter, curves slightly downward to the right, and ends in a clear arrowhead before the right diamond\'s left vertex. The short S-to-D line farther left ends without a head and does not continue into this arrow.',
       'diamonds', 'high', 'drawing or diagram', True, False, True)
change('Catalogue item 2: preposition', 'de', 'du', r'\unsure{de|du}',
       'After the d loop and staff, the final low joined stroke is strongly flattened. It does not separate cleanly enough into an e loop or a u trough to settle de against du.',
       'items123', 'low', 'misread word', False, True)
change('Catalogue item 3: initial prefix', 'surmarquage', 'marquage', 'surmarquage',
       'Before the m run there is a separate initial s curve, then the low joined u and r strokes. The word begins well before the m; those prefix strokes are live and continuous with the word.',
       'items123', 'high', 'omission', False, True)
change('Catalogue item 4: punctuation after partiel', ',', '(nothing)', r'\unsure{,}',
       'A small dark point lies just after the closing parenthesis, but its short tail is not securely distinguished from the mottled paper. The comma is retained only in doubt.',
       'items45', 'low', 'omission', False, True)
change('Catalogue item 5: underline extent', r'\uline{amalgamation}', r'\emph{amalgamation}',
       '\\node at (0.90,-3.40) {amalgamation ou recollage};\n\\draw (0.70,-3.63) -- (2.62,-3.60);',
       'The separate rule begins left of the first a and stops beneath the middle portion of amalgamation, while several letters continue clearly to the right. The rule does not extend under the whole word.',
       'items45', 'high', 'drawing or diagram', True, True)
change('Catalogue item 5: cancelled wording and possible opening parenthesis',
       r'(\deleted{\unsure{avec données de}}', r'\struck{\ill{}} (',
       r'\deleted{\unsure{avec (données de}}',
       'A densely cancelled short group follows recollage. Farther right, a curved descending stroke precedes surviving tall letter parts, and the horizontal strike continues through that old line. It may be an opening parenthesis after avec; the words and the position of this curve remain doubtful. The closing parenthesis at the far right remains live.',
       'items45', 'low', 'deletion state', True, True)
change('Catalogue item 5: interlinear replacement', r'\inserted{sans gommage!}',
       '(sans gommage !)', r'\inserted{sans gommage!}',
       'Sans gommage! is written on a higher baseline above the crossed-out phrase. Its g descenders and final exclamation mark are distinct from the horizontal cancellation below.',
       'items45', 'high', 'insertion or placement', False, True)
change('Catalogue: vertical double-arrow positions',
       r'\updownarrow inline after items 2 and 5',
       'Two vertical double arrows between rows 2 and 3 and between rows 4 and 5.',
       '\\draw[<->] (9.10,-0.72) -- (9.10,-1.24);\n\\draw[<->] (12.00,-2.49) -- (12.00,-3.18);',
       'Both vertical strokes have visible heads at both ends. The first is beside the space following row 2; the second starts at the height of row 4 and ends beside row 5, rather than below row 5.',
       'items45', 'high', 'drawing or diagram', True, False, True)
change('Catalogue item 6: preposition after gommage', 'de', 'des', 'de',
       'The short group after gommage has the loop-and-staff d and a low finishing stroke; no separate terminal s curve is visible before the gap to cercles.',
       'items67', 'medium', 'misread word', False, True)
change('Catalogue item 7: preposition after gommage', 'de', 'des', 'de',
       'The group between gommage and cercles ends after a short low stroke following d; there is no further s-shaped turn before the space.',
       'items67', 'medium', 'misread word', False, True)
change('Catalogue item 7: final adjective', 'intérieurs', 'internes', 'intérieurs',
       'After the tall t, the remaining run is longer than -ernes and has an accent above its beginning, followed by the low joined -ieurs ending. The final word is intérieurs.',
       'items67', 'high', 'misread word', False, True)
change('Bottom-left foliation', r'\mspage{41}', '(nothing)', r'\margin{41}',
       'An open-topped 4 has a horizontal joining stroke and a long right upright; the following 1 has an oblique entry and a long descending shaft. These thin, separate figures are at the foot of the sheet, away from the main handwriting.',
       'folio', 'high', 'other', True, True)

decisions = [dict(id='M0643', decision='first', reading=r'\mathcal T',
    ink='The angular cap, short rightward turn and broad lower return match the same-page T forms after S, D and SD. The live glyph is spatially distinct from the cancelled group to its left. This is a medium-confidence resolution from visible letter shapes, not from a presumed diagrammatic meaning.',
    **evidence('diamonds'), confidence='medium')]

unresolved = []
def unresolved_row(place, reading, issue, alternatives, confidence, label):
    unresolved.append(dict(place=place, reading=reading, issue=issue, alternatives=alternatives,
                           confidence=confidence, **evidence(label)))
unresolved_row('Condition: cancelled word', r'\deleted{\unsure{de}}',
    'The compact cancellation obscures the individual letters.', ['de', 'unreadable cancelled short word'], 'low', 'condition')
unresolved_row('Left diamond: cancelled letters before the top vertex', r'\deleted{\unsure{SD}}',
    'Transverse cancellation strokes prevent certification of both proposed letters.', ['SD', 'unreadable cancelled letter group'], 'low', 'diamonds')
unresolved_row('Right diamond: repeated final glyph at all four vertices',
    r'\unsure{t|\mathbb L},\quad s\unsure{t|\mathbb L},\quad d\unsure{t|\mathbb L},\quad sd\unsure{t|\mathbb L}',
    'The mid-height crossbar favors t, while the doubled upright and foot leave the exact alphabet unresolved.', ['t', r'\mathbb L'], 'medium', 'diamonds')
unresolved_row('Catalogue item 2: preposition', r'\unsure{de|du}',
    'The final letter is flattened and does not securely distinguish e from u.', ['de', 'du'], 'low', 'items123')
unresolved_row('Catalogue item 4: punctuation', r'\unsure{,}',
    'The tiny point after the parenthesis may be punctuation or a paper/background mark.', [',', '(no punctuation)'], 'low', 'items45')
unresolved_row('Catalogue item 5: cancelled wording and opening parenthesis', r'\deleted{\unsure{avec (données de}}',
    'The old words are heavily crossed out. A curved stroke suggests an opening parenthesis after the first short word, but both its position and cancellation scope remain doubtful.',
    [r'\deleted{avec (données de}', r'(\deleted{avec données de}', r'\deleted{\illegible{3}}'], 'low', 'items45')

inventory = []
def inv(element, kind, position, first, hand='his hand'):
    inventory.append(dict(element=element, kind=kind, position=position,
        first_words_or_objects=first, sheet_kind='reused_typed', hand=hand, transcribed='yes'))
inv('heading', 'text', 'top left', 'opérations de recollage / sommes')
inv('objects-heading', 'text', 'upper left, within the outer brace height', 'objets; diagrammes')
inv('objects-list', 'text', 'upper left below objects heading', 'cercles de raccord; cercles de découpage; Sommets; cercles marqués')
inv('objects-braces', 'drawing', 'left edge of upper objects group', 'large outer brace and shorter inner brace joining the two circle lines')
inv('condition', 'text', 'upper left beneath objects list, two lines', '[condition ... anabélienne / ou de stabilité]')
inv('condition-deletion', 'deletion', 'after condition', r'\deleted{\unsure{de}}')
inv('paired-diamonds', 'diagram', 'upper right', 'two diamonds, one internal headless line, four right-pointing connecting arrows')
inv('top-vertex-deletion', 'deletion', 'before the first diamond top vertex', r'\deleted{\unsure{SD}}')
inv('types-annotation', 'margin note', 'under the right diamond', 'types combinatoires')
inv('catalogue-heading', 'text', 'below upper text and diagram', 'Catalogue opérations + structures')
inv('catalogue-1-3', 'text', 'middle left, first grouped items', '1) Somme / 2) gommage / 3) surmarquage')
inv('catalogue-first-brace', 'drawing', 'between numbers and words of items 1–3', 'first tall grouping brace')
inv('catalogue-first-arrow', 'drawing', 'right of item 2, extending toward item 3', 'vertical stroke with upward and downward arrowheads')
inv('catalogue-4', 'text', 'middle left beneath first group', '4) découpage (partiel)')
inv('catalogue-5', 'text', 'middle of page, second group', '5) amalgamation ou recollage')
inv('catalogue-5-rule', 'drawing', 'below left portion of amalgamation', 'short horizontal underline')
inv('catalogue-5-deletion', 'deletion', 'after recollage', r'\deleted{\unsure{avec (données de}}')
inv('catalogue-5-insertion', 'insertion', 'above the cancelled phrase in item 5', r'\inserted{sans gommage!}')
inv('catalogue-second-brace', 'drawing', 'between numbers and words of items 4–6', 'second tall grouping brace')
inv('catalogue-second-arrow', 'drawing', 'far right of items 4–5', 'vertical stroke with upward and downward arrowheads')
inv('catalogue-6', 'text', 'below amalgamation line', '6) bouchage de trous (= gommage de cercles de raccord)')
inv('catalogue-7', 'text', 'below the second grouping brace', '7) gommage de cercles intérieurs')
inv('closing-line', 'text', 'below catalogue', 'foncteurs et iso twist')
inv('folio', 'margin note', 'bottom left', '41', 'another unnamed hand')

notes = [
 dict(id='N42-001', statement_id='P42-outline', kind='content', place='whole manuscript proper',
      text='This sheet gives an objects list, a paired diagram of symbolic vertices, and a seven-item catalogue. The page does not state a proposition whose proof or numerical value was checked in this first reading.', status='observed; no mathematical check event'),
 dict(id='N42-002', statement_id='P42-diagram', kind='notation', place='paired diamonds',
      text='The four doubled right-hand glyphs are visually related, but this repetition has not been used to choose an alphabet by expected mathematical meaning. The t versus blackboard L alternatives remain explicit.', status='unresolved'),
 dict(id='N42-003', statement_id='P42-cancellation', kind='reading qualification', place='catalogue item 5',
      text='The interlinear replacement is legible. The crossed-out phrase and a possible opening parenthesis beneath it remain doubtful; no grammatical repair has been supplied to balance an uncertain old parenthesis.', status='unresolved'),
 dict(id='N42-004', statement_id='P42-foliation', kind='date and pagination', place='bottom left and whole sheet',
      text='The bottom number is 41 in a separate thin hand and is recorded as a margin entry. No date is visible in the source handwriting on this sheet.', status='observed'),
 dict(id='N42-005', statement_id='P42-background', kind='excluded layer', place='faint background, especially lower half',
      text='Faint regular rows and other pale show-through marks do not belong to the dark front-side manuscript. They have not been turned into source words, illegibility marks, or alternative readings.', status='excluded from diplomatic text'),
 dict(id='N42-006', statement_id='P42-underline', kind='layout', place='amalgamation',
      text='The source underline is shorter than the word. Its visible span is drawn rather than silently extended to every letter.', status='preserved')
]

hand_log = [
 dict(pages=['148_scan042'], habit='The right-diamond base glyph has a doubled upright with a middle crossbar and a rightward foot.',
      evidence='All four right-hand vertices show this structure, including the glyphs preceded by s, d and sd.',
      holds_at_every_observed_occurrence=True,
      witness_effect='C uses t and H blackboard L; the repeated physical form is recorded without settling that alphabet by context.'),
 dict(pages=['148_scan042'], habit='The s prefixes in the right diamond are smaller than the S prefixes in the left diamond.',
      evidence='The s before the left right-diamond glyph and the s in its bottom sd group both occupy a lower band than the tall left S forms.',
      holds_at_every_observed_occurrence=True,
      witness_effect='The right-hand prefixes are transcribed lowercase, against H’s uppercase S.'),
 dict(pages=['148_scan042'], habit='Low final letter strokes can be flattened into a short joined line.',
      evidence='The preposition following (partiel) in item 2 does not securely separate e from u; the short groups before cercles in items 6 and 7 show similarly compressed finishing strokes.',
      holds_at_every_observed_occurrence=False,
      witness_effect='The item 2 de/du alternative is retained; separate s strokes have not been added to items 6 and 7.')
]

notation = [
 dict(place='left diamond', form=r'\mathcal T; S\mathcal T; D\mathcal T; SD\mathcal T',
      observation='The same angular cap and broad lower return recur after the capital left prefixes; these visible comparisons support resolving the top instance at medium confidence.'),
 dict(place='right diamond', form=r'\unsure{t|\mathbb L}; s; d; sd',
      observation='Small s and d prefixes precede the repeated doubled glyph; no subscripts or primes are visible.'),
 dict(place='catalogue heading', form='+', observation='A small upright and crossing horizontal make a literal plus between opérations and structures.'),
 dict(place='catalogue arrows', form=r'\updownarrow', observation='Each source arrow is vertical with a head at both ends; the two placements are drawn in the catalogue.')
]

abbreviations = [dict(place='closing line', form='iso',
    observation='The short form iso is written without a visible following full stop and is left unexpanded.')]

second_boxes = []
def second(name, kind, box, reading):
    second_boxes.append(dict(box='S42-'+name, kind=kind, x0=box[0], y0=box[1], x1=box[2], y1=box[3], reading=reading))
second('heading', 'C/H different word', crops['heading']['box'], 'opérations de recollage / sommes')
second('objects-heading', 'C/H different word', [180,125,615,197], 'objets; diagrammes')
second('sommets', 'C/H different word', [96,265,558,329], r'Sommets de \uline{marquage}')
second('parenthetical', 'C/H different word', [554,253,747,320], r'(périphériques\\intérieurs')
second('objects-braces', 'drawing or diagram', crops['objects']['box'], objects_figure)
second('condition-deleted', 'struck passage', [355,359,415,416], r'\deleted{\unsure{de}}')
second('diamonds', 'whole doubtful formula and diagram', crops['diamonds']['box'], diamond)
second('top-deleted', 'struck passage', [790,114,853,166], r'\deleted{\unsure{SD}}')
second('types-note', 'margin note', [1183,421,1510,481], 'types combinatoires')
for number, box in [
    (1,[103,630,145,690]), (2,[105,691,147,751]), (3,[109,747,153,807]),
    (4,[108,827,152,893]), (5,[113,888,157,950]), (6,[114,974,158,1032]),
    (7,[119,1032,166,1092])]:
    second('number-'+str(number), 'handwritten number', box, str(number)+')')
second('item2-preposition', 'C/H different word', [586,676,680,719], r'\unsure{de|du}')
second('surmarquage', 'C/H different word', [181,744,526,817], 'surmarquage')
second('item4-punctuation', 'doubtful sign', [624,837,668,887], r'\unsure{,}')
item5_tikz = '\\figure{\\begin{tikzpicture}[x=1cm,y=1cm,every node/.style={anchor=west,inner sep=0pt,outer sep=0pt}]\n' + '\n'.join(
    line for line in catalogue_figure.splitlines()
    if any(token in line for token in [
        '{amalgamation ou recollage}', '\\draw (0.70,-3.63)',
        '\\deleted{\\unsure{avec (données de}}', '\\inserted{sans gommage!}',
        '\\node at (10.66,-3.24)'])) + '\n\\end{tikzpicture}}'
second('item5', 'struck passage and insertion and underline', [183,844,1280,965], item5_tikz)
second('item6', 'C/H different word', [211,965,1404,1040], 'bouchage de trous (= gommage de cercles de raccord)')
second('item7', 'C/H different word', [218,1036,963,1105], 'gommage de cercles intérieurs')
second('arrow23', 'drawing or diagram', [917,683,960,751],
       r'\figure{\begin{tikzpicture}\draw[<->] (9.10,-0.72) -- (9.10,-1.24);\end{tikzpicture}}')
second('arrow45', 'drawing or diagram', [1295,834,1337,921],
       r'\figure{\begin{tikzpicture}\draw[<->] (12.00,-2.49) -- (12.00,-3.18);\end{tikzpicture}}')
second('folio', 'handwritten number and margin note', crops['folio']['box'], r'\margin{41}')

reading_rows = {
 877:('objects braces','Two source braces and their distinct spans are rendered in TikZ.'),
 879:('inner objects brace','The short inner brace ends after the second circle line.'),
 880:('parenthetical adjective and punctuation','Read intérieurs. Neither a comma/slash after périphériques nor a closing parenthesis after intérieurs is separately visible; retain only the opening parenthesis.'),
 882:('outer objects brace','The visible outer brace extends above the objects heading and below the last circle line.'),
 883:('condition deletion','Retain the uncertain cancelled de; the double-quote spelling follows source and conventions.'),
 886:('cancelled group before top vertex','Retain SD in cancellation and in doubt; H’s editorial note is not source prose.'),
 890:('right diamond top glyph','Keep explicit t versus blackboard L doubt.'),
 894:('middle connecting arrow','The headless S-to-D line is distinct; the long upper connecting arrow begins at D, not S.'),
 896:('two arrows issuing near D','Preserve both D-to-left-right-vertex and curved D-to-right-right-vertex arrows.'),
 897:('right diamond left vertex','Small s followed by the uncertain repeated glyph.'),
 899:('right diamond right vertex','Small d followed by the uncertain repeated glyph.'),
 902:('right diamond bottom vertex','Small sd followed by the uncertain repeated glyph.'),
 903:('top cancellation and diagram','Actual letters/strokes are represented; H’s explanatory prose is not copied into the source.'),
 904:('right glyph and annotation','Preserve types combinatoires below the right diamond; retain alphabet doubt and visible arrow connections.'),
 909:('item 2 preposition','Keep de|du unresolved from its flattened finishing stroke.'),
 911:('item 3','The prefix sur- is visible and live.'),
 914:('item 4 punctuation','Keep the tiny possible comma in doubt.'),
 916:('item 5 deletion and insertion','Cancelled old wording and possible parenthesis remain doubtful; sans gommage! is interlinear.'),
 919:('item 6 preposition','Read de; no separate terminal s is visible.'),
 922:('item 7 preposition','Read de; retain the seven catalogue numbers and two grouping braces.'),
 923:('item 7 adjective and double-arrow placement','Read intérieurs; draw the second double arrow beside rows 4–5.'),
 924:('bottom foliation','Retain 41 as an unassigned-hand margin entry. The source uses double quotation marks around twist.')
}
macro_notes = {
 872:'H’s paper-and-ink description is editorial metadata, not source text.',
 873:'H’s statement about author pagination is editorial metadata; the visible bottom 41 is separately inventoried.',
 874:r'The apparent comma is the LaTeX thin-space command \, before the slash, not a manuscript comma.',
 875:r'The apparent comma is the LaTeX thin-space command \, after the slash, not a manuscript comma.',
 876:'Itemize wrapper only.', 878:'List item wrapper only.', 881:'List item wrapper only.',
 884:'Different quotation glyph encodings; source double quotes are represented with the required two-backtick/two-apostrophe convention.',
 885:'Ampersand-replacement syntax only.',
 887:'dash and no head both encode the solid headless upper-left edge.',
 888:'dash and no head both encode the solid headless upper-right edge.',
 889:'Different matrix column counts; the same top connecting arrow is present.',
 891:'Alternative syntax for a solid headless edge.', 892:'Alternative syntax for a solid headless edge.',
 893:'Alternative syntax for a solid headless edge.', 895:'Alternative syntax for a solid headless edge.',
 898:'Alternative syntax for a solid headless edge.', 900:'Alternative syntax for a solid headless edge.',
 901:'Different matrix column counts for the same bottom connecting arrow.',
 905:'Array versus enumerate presentation wrapper.',
 906:'Both witnesses identify the first group as items 1–3; the source brace is drawn.',
 907:'List item wrapper only.', 908:'List item wrapper only.', 910:'List item wrapper only.',
 912:'Vertical-spacing instruction only.',
 913:'Both witnesses identify the second group as items 4–6; the source brace is drawn.',
 915:'List item wrapper only.', 917:'List item wrapper only.', 918:'List item wrapper only.',
 920:'List item wrapper only.', 921:'List item wrapper only.'
}
source_differences = list(csv.DictReader((PACKET/'differences.tsv').open(), delimiter='\t'))
differences_review = []
for r in source_differences:
    n = int(r['source_row'])
    if n in reading_rows:
        place, note = reading_rows[n]
        differences_review.append(dict(source_row=n, decision='reading decision', place=place, note=note))
    else:
        assert n in macro_notes, n
        differences_review.append(dict(source_row=n, decision='macro-only', place=r['words before'] or 'editorial prefatory note', note=macro_notes[n]))

result = dict(
 scan=42, reader='A',
 reader_metadata=dict(model='GPT-6 Astra Pro', effort='not exposed', run='SP82_C13_148', date='2026-11-21'),
 lines_read=21,
 reading_workflow=dict(
    whole_page_views=1, native_half_views=2,
    half_view_proxies=['half1_q95.jpg','half2_q95.jpg'],
    detail='The whole page was inspected once for layout. Both native-dimension overlapping halves were read once line by line, including agreed words and the blank lower portion. Twenty-one text baselines count: heading; objects heading; two circle lines; Sommets and the parenthetical continuation; final circle line; two condition lines; diagram annotation; catalogue heading; seven numbered item baselines; one interlinear replacement baseline; closing line; folio. The eight diagram vertices, all edges/arrowheads, two upper braces, two catalogue braces, two vertical double arrows and short underline were inspected separately. No OCR, web research or TeX compilation was used.',
    crop_views=8, recrops=0,
    crop_method='Each first crop is the original saved enhanced PNG rectangle; same-dimension quality95 JPEG proxies were used only for display. Changes cite original rectangles. Second-reading boxes may be tighter subrectangles.',
    mathematics='No independent mathematical proposition was evaluated; checks is intentionally empty.'),
 changes=changes, decisions=decisions, inventory=inventory, unresolved=unresolved,
 notes=notes, checks=[], hand_log=hand_log, notation=notation, abbreviations=abbreviations,
 second_boxes=second_boxes, differences_review=differences_review,
 crop_manifest=manifest,
 excluded_layers=[dict(layer='faint background show-through', position='throughout the sheet, most visible in the large blank lower half',
     reason='Pale regular rows and other show-through do not share the dark front manuscript line structure.', transcribed=False)]
)

marks = list(csv.DictReader((PACKET/'marks.tsv').open(), delimiter='\t'))
assert sorted(r['id'] for r in decisions) == sorted(r['id'] for r in marks)
assert len(set(r['source_row'] for r in differences_review)) == len(source_differences)
assert isinstance(result['lines_read'], int)
assert len(second_boxes) == len(set(r['box'] for r in second_boxes))
for r in changes:
    assert r['against_c'] or r['against_h']
    assert any(r['crop']==c['crop'] and r['box']==c['box'] for c in manifest)
for r in second_boxes:
    assert 0 <= r['x0'] < r['x1'] <= 1550
    assert 0 <= r['y0'] < r['y1'] <= 2244
    assert r['reading']
assert all(r['seen'] for r in manifest)
(OUT/'result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(dict(changes=len(changes), decisions=len(decisions), inventory=len(inventory),
    unresolved=len(unresolved), checks=len(result['checks']), second_boxes=len(second_boxes),
    differences_review=len(differences_review), crops=len(manifest)), ensure_ascii=False))
