from pathlib import Path
import json

base = Path('/workspace/scratch/88012a0a2bcc')
work = base / 'SP77_C13_147_work'
src = base / 'inputs/SP77_C13_147_texts/pages/147_scan045.tex'
draft = src.read_text()
replacements = [
    (r"des arêtes de $G'$", r"des arêtes de $\unsure{C'|G'}$"),
    (r"\inserted{$\unsure{\overline m|=}$}", r"\inserted{$\overline m$}"),
    (r"\mathrm{déf}", r"\mathrm{def}"),
    (r"pour $\forall\alpha\in S$", r"pour $\unsure{\forall|\mathrm{tt}}\alpha\in S$"),
]
for old, new in replacements:
    assert draft.count(old) == 1, (old, draft.count(old))
    draft = draft.replace(old, new)
(work / 'drafts/147_scan045.tex').write_text(draft)

specs = [
    ('01_formula55', [275, 160, 1255, 270]),
    ('02_GprimeG0', [505, 300, 805, 390]),
    ('03_edgesG', [485, 538, 1060, 640]),
    ('04_G0G', [525, 650, 875, 750]),
    ('05_ordinaire', [235, 770, 650, 895]),
    ('06_correction', [260, 1030, 735, 1150]),
    ('07_mbar', [710, 1020, 850, 1130]),
    ('08_data', [245, 1235, 1170, 1405]),
    ('09_IS', [710, 1745, 1015, 1845]),
    ('10_composite', [595, 1870, 1210, 2040]),
    ('11_quantifier', [935, 2000, 1370, 2105]),
    ('12_genus', [235, 2100, 1385, 2344]),
    ('13_footer', [20, 2280, 90, 2345]),
]
crop = {name: f'crops/147_scan045_{name}.jpg' for name, box in specs}
bounds = dict(specs)
def locus(name):
    return crop[name] + ' (' + ','.join(map(str, bounds[name])) + ')'

changes = []
def change(place, C, H, final, dc, dh, kind, evidence, name, confidence, consequential, category):
    changes.append(dict(id=f'045-{len(changes)+1:02}', place=place, C=C, H=H, final=final,
        diff_C=dc, diff_H=dh, kind=kind, evidence=evidence, crop=crop[name],
        box=bounds[name], confidence=confidence, consequential=consequential,
        error_category=category))

change("arêtes de ... contractées, graph letter",
    r"G'", r"C'", r"\unsure{C'|G'}", True, False,
    "misread symbol or index",
    "The letter has an open curved body and a short rising lower terminal ending in a thick nub. No separately extended descending G-foot is clear. C-prime is the first visual reading, but the terminal could be a compressed G-foot, so G-prime remains an explicit alternative.",
    '03_edgesG', 'medium', True, 'Symbols and indices')
change("interlinear replacement, word after soit",
    "fixé", "fini", "fixé", False, True, "misread word",
    "After the tall looped f and short i, the crossing/angular x is visible; the final e has a separate accent. The word is fixé, not fini. The entire replacement above the line reads soit fixé, et.",
    '06_correction', 'high', False, 'Words')
change("baseline soit and attachment of the replacement soit",
    r"\inserted{soit fixé, et} \deleted{soit}",
    r"soit \struck{\ill{}} \add{fini, et}",
    r"\inserted{soit fixé, et} \deleted{soit}",
    False, True, "deletion state",
    "The baseline word soit is traversed by a heavy horizontal cancellation; its s, linked middle letters and tall final t remain visible. The separate word soit is written above it as the start of the replacement phrase. H's live baseline soit and unread struck material do not preserve these states.",
    '06_correction', 'high', False, 'Struck text')
change("insertion after provienne",
    r"\inserted{$\unsure{\overline m|=}$}", r"\add{\ill{}}",
    r"\inserted{$\overline m$}", False, True, r"readable ink left as \ill{}",
    "The lower sign has a short upright, two humps and a descending end, with an independent arched bar above. The lower part is not a second straight equality bar. The insertion leader attaches it between provienne and d'un.",
    '07_mbar', 'high', False, 'Readable ink left as illegible')
change("cancelled number before the supplementary-data formula",
    r"\deleted{\unsure{(55)|(56)}}",
    '[absent from the transcription; an editorial note mentions un numéro biffé]',
    r"\deleted{\unsure{(55)|(56)}}", False, True, "omission",
    "A parenthesized numerical cluster is visibly cancelled to the left of I-prime. Its strokes survive through dense crossing; the second digit and parts of the first are not individually secure. The two existing candidate readings are retained under doubt, not resolved.",
    '08_data', 'low', False, 'Omissions')
change("supplementary-data formula, between S-prime and the labelled map to N",
    r"I'\longrightarrow S',\xrightarrow{\unsure{g'|\underline{g'}}}\mathbb N",
    r"I' \to S', \quad S' \xrightarrow{g'} \mathbb{N}",
    r"I'\longrightarrow S',\xrightarrow{\unsure{g'|\underline{g'}}}\mathbb N",
    False, True, "text not on the page",
    "There is one S-prime, followed by a comma and then the labelled arrow to the double-stroked N. The gap contains no second S-prime. The arrow's uneven doubled portion is a retraced shaft, not two consistently separate parallel shafts.",
    '08_data', 'high', True, 'Text that is not on the page')
change("composed-map display, vertical identification below I-prime",
    r"\underset{\substack{\Vert\,\mathrm{déf}\\I}}{I'}\longrightarrow S'\unsure{\longrightarrow|{-}}S",
    r"I \overset{\text{déf}}{=} I' \to S' \to S",
    r"\underset{\substack{\Vert\,\mathrm{def}\\I}}{I'}\longrightarrow S'\unsure{\longrightarrow|{-}}S",
    False, True, "insertion or placement",
    "I-prime begins the horizontal composite. Two short vertical identification strokes, the adjacent definition abbreviation, and a lower I are written beneath it. They are not a horizontal prefixed I-equals-I-prime expression. The accent difference in the abbreviation is logged separately.",
    '10_composite', 'high', False, 'Insertions put in the wrong place')
change("definition abbreviation beside the vertical identification",
    r"\mathrm{déf}", r"\text{déf}", r"\mathrm{def}", True, True,
    "abbreviation expanded or spelling modernised",
    "The d ascender, short e and long descending f are present. There is no separate accent stroke over the e; the unaccented written abbreviation def is retained.",
    '10_composite', 'high', False, 'Abbreviations expanded, spelling modernised')
change("annotation below the summation set S-prime-alpha in (56)",
    r"\underset{\substack{\Vert\\\text{Sommets}\\\text{de }G'(\alpha)}}{S'_\alpha}",
    "[S'_alpha alone in the formula; the source annotation is quoted only in H's editorial note]",
    r"\underset{\substack{\Vert\\\text{Sommets}\\\text{de }G'(\alpha)}}{S'_\alpha}",
    False, True, "insertion or placement",
    "The set S-prime-alpha has two vertical identification strokes below it, then a capital-S Sommets and a second line de G-prime(alpha). The prime on G is distinct and alpha is parenthesized at baseline. The annotation is part of the written formula.",
    '12_genus', 'high', False, 'Insertions put in the wrong place')
change("lower-left handwritten page number",
    r"\mspage{44}", "[absent]", r"\mspage{44}", False, True, "omission",
    "Two separate tall pencil digits have the same open top and low cross/turn, each reading 4. The footer reads 44.",
    '13_footer', 'high', False, 'Omissions')

decisions = []
def decision(id, result, reading, evidence, name, confidence):
    decisions.append(dict(id=id, cote='147', scan='45', decision=result, reading=reading,
        **{'what the ink shows': evidence}, crop=locus(name), confidence=confidence))

decision('M1003', 'undecided', r"\unsure{\longrightarrow|{-}}",
    "The first relation in (55) is a long shaft with a small raised/downturned terminal nub. A fully distinct pair of arrowhead wings is not established; arrow and literal stroke remain alternatives.",
    '01_formula55', 'medium')
decision('M1004', 'undecided', r"\unsure{\longrightarrow|{-}}",
    "The second relation in (55) has a short dark downturned end, but not a clearly separated complete arrowhead. The full formula, G-prime, G-zero and G, has been read together.",
    '01_formula55', 'medium')
decision('M1005', 'undecided', r"\unsure{\to|{-}}",
    "The inline G-prime/G-zero relation has one short downturned right-end stroke. It could be a compressed arrowhead or a hooked end to a headless shaft.",
    '02_GprimeG0', 'medium')
decision('M1006', 'first', r"\overline m",
    "The independent overbar sits above a humped m-shaped lower sign. The lower sign has more structure than a straight equality bar. The insertion and its leader have been checked.",
    '07_mbar', 'high')
decision('M1007', 'undecided', r"\unsure{g'|\underline{g'}}",
    "A round-headed g with a closed lower loop and a separate upper-right prime is clear. A horizontal segment at the top of the lower loop extends beneath the prime; it may be an underline or the return tail of g. Its independence is not secure enough to remove the doubt.",
    '08_data', 'medium')
decision('M1008', 'undecided', r"\unsure{I|I'}",
    "The capital has top and bottom bars and an upright stem. Its upper bar ends in a conspicuous downturned right-hand stroke; a separate prime is not established, but a prime joined to the serif cannot be excluded.",
    '09_IS', 'medium')
decision('M1009', 'undecided', r"\unsure{\to|{-}}",
    "The I/S relation has a single downturned nub at the right end and no plainly separate upper arrowhead wing. Both the shaft and endpoint have been inspected with the complete formula.",
    '09_IS', 'medium')
decision('M1010', 'undecided', r"\unsure{\longrightarrow|{-}}",
    "The first arrow of the composite has two clear wings; the second S-prime/S relation has only a small raised tooth and a short diagonal terminal. That local contrast does not settle the second stroke's arrowhead.",
    '10_composite', 'medium')

supplemental = [dict(id='U045-01', cote='147', scan='45',
    place='nested C doubt in the cancelled supplementary-data formula number',
    decision='undecided', reading=r"\deleted{\unsure{(55)|(56)}}",
    **{'what the ink shows': 'A parenthesized numerical cluster is crossed several times. Cancellation is certain; neither complete pair of digits can be certified through it.'},
    crop=locus('08_data'), confidence='low')]

box_readings = [
    ('01_formula55', 'full doubtful formula; formula number 55; subscript zero',
     r"(55)\qquad G'\unsure{\longrightarrow|{-}}G_0\unsure{\longrightarrow|{-}}G,"),
    ('02_GprimeG0', 'full doubtful formula; subscript zero',
     r"$G'\unsure{\to|{-}}G_0$"),
    ('03_edgesG', 'C/H graph-letter difference; new doubtful reading',
     r"de $\unsure{C'|G'}$ contractées"),
    ('04_G0G', 'full inline formula; subscript zero',
     r"$G_0\longrightarrow G$"),
    ('05_ordinaire', 'interlinear insertion and attachment',
     r"\inserted{ordinaire} de graphes."),
    ('06_correction', 'replacement insertion; struck passage; C/H word difference',
     r"\inserted{soit fixé, et} \deleted{soit}"),
    ('07_mbar', 'interlinear abbreviation and insertion leader',
     r"\inserted{$\overline m$}"),
    ('08_data', 'whole doubtful formula; cancelled numerical label; missing/present token',
     r"\deleted{\unsure{(55)|(56)}}\qquad I'\longrightarrow S',\xrightarrow{\unsure{g'|\underline{g'}}}\mathbb N,"),
    ('09_IS', 'full formula with two C doubts',
     r"$\unsure{I|I'}\unsure{\to|{-}}S$"),
    ('10_composite', 'whole doubtful formula; vertical identification and unaccented abbreviation',
     r"\underset{\substack{\Vert\,\mathrm{def}\\I}}{I'}\longrightarrow S'\unsure{\longrightarrow|{-}}S,"),
    ('11_quantifier', 'whole newly doubtful formula',
     r"pour $\unsure{\forall|\mathrm{tt}}\alpha\in S$"),
    ('12_genus', 'whole formula 56; raised numeral 1; lower annotation',
     r"(56)\qquad g_\alpha=\Big(\sum_{\alpha'\in\underset{\substack{\Vert\\\text{Sommets}\\\text{de }G'(\alpha)}}{S'_\alpha}}g'_{\alpha'}\Big)+h^1(G'(\alpha))."),
    ('13_footer', 'handwritten page number',
     r"\mspage{44}"),
]
boxes = []
for i, (name, kind, reading) in enumerate(box_readings, 1):
    x0,y0,x1,y1 = bounds[name]
    boxes.append(dict(box=f'045-B{i:02}', kind=kind, x0=x0, y0=y0, x1=x1, y1=y1, reading=reading))

inventory = []
def item(kind, position, content):
    inventory.append(dict(scan=45, sheet_kind='text', hand='his hand',
        element=f'045-E{len(inventory)+1:02}', kind=kind, position=position,
        first_words_or_objects=content, transcribed='yes'))
item('text', 'top and upper paragraph', 'composé; où G-prime ... passage au quotient ... de graphes')
item('display', 'upper formula', '(55) G-prime ... G-zero ... G')
item('insertion', 'above the end of the upper paragraph', 'ordinaire')
item('text', 'middle paragraph', 'Supposons maintenant que G-prime ... grâce aux données supplémentaires')
item('insertion', 'above the cancelled baseline soit', 'soit fixé, et')
item('deletion', 'middle paragraph baseline before provienne', 'soit')
item('insertion', 'above the gap after provienne, with a leader', 'm with overbar')
item('deletion', 'left of the supplementary-data display', 'uncertain cancelled (55)/(56)')
item('display', 'supplementary-data display', 'I-prime to S-prime, labelled map to N')
item('text', 'lower paragraph', "où I-prime est un ens. fini. Alors G ... en définissant ...")
item('display', 'lower composed-map display', 'I-prime to S-prime ... S, with vertical def/I annotation')
item('text', 'below composed map', 'et en définissant, pour ... alpha in S')
item('display', 'bottom formula and its annotation', '(56) genus sum plus h superscript 1; Sommets de G-prime(alpha)')
item('text', 'lower-left footer in pencil', '44')

doubts = []
for d in decisions:
    if d['decision'] == 'undecided':
        doubts.append(dict(place=d['id'], reading=d['reading'], alternatives=d['reading'],
            confidence=d['confidence'], reason=d['what the ink shows']))
doubts.extend([
    dict(place='cancelled supplementary-data number (unindexed nested C doubt)',
         reading=r"\deleted{\unsure{(55)|(56)}}", alternatives='(55) | (56)', confidence='low',
         reason='The cancellation remains certain, but the crossed digits are not completely recoverable.'),
    dict(place='arêtes de ... contractées', reading=r"\unsure{C'|G'}", alternatives="C' | G'", confidence='medium',
         reason='The open curved body favors C; a minute terminal nub could also be the compressed foot of G. The expected graph name is not used to erase this local uncertainty.'),
    dict(place='pour ... alpha in S', reading=r"\unsure{\forall|\mathrm{tt}}",
         alternatives=r'\forall | \mathrm{tt}', confidence='medium',
         reason='The joined tall strokes include a low V-shaped turn, a high right peak and a cross stroke. They favor the universal quantifier, but an unusually joined double-t form remains possible; prior tt habits are not imposed without a clear local distinction.'),
])

notes = [
    dict(id='147-045-N01',
         text="Handwritten page 44 continues the graph-map factorization through G_0 in (55), then states how fixed MD-data on G-prime induce data on G. It keeps I equal to I-prime, gives the composed vertex map, and writes the genus in (56) as a sum over S-prime-alpha plus h superscript 1 of G-prime(alpha). This is a reading summary, not a verification of the construction. The source's comma before the labelled map to N and its single written S-prime are preserved."),
    dict(id='147-045-N02',
         text="The arêtes clause locally looks more like C-prime than G-prime, with G-prime retained as an explicit alternative; no mathematical correction is asserted. The interlinear phrase reads soit fixé, et, and the crossed baseline word is soit. The separate insertion is m with an overbar, retained as written. No complete reading of the cancelled formula number is certified."),
]

record = dict(
    scan=45, reader='reader_b', line_count=25, changes=changes,
    decisions=decisions, supplemental_unindexed_C_doubts=supplemental,
    inventory=inventory, boxes=boxes, doubts=doubts,
    notation=[
        dict(form=r'G_0', meaning='intermediate quotient graph in the factorization',
             evidence='(55), the inline quotient map, and the later inline map to G',
             scope='All three lowered zero numerals on this page are included in full-formula blind boxes.'),
        dict(form=r'\overline m', meaning='written abbreviation for même',
             evidence='interlinear insertion after provienne, crop 07_mbar',
             scope='This local humped lower sign and independent bar are confirmed; other occurrences are not inferred.'),
        dict(form=r"h^1(G'(\alpha))", meaning='last summand in the stated genus formula',
             evidence='(56), full formula crop 12_genus',
             scope='The numeral 1 is raised, and G carries a separate prime; no conversion to a subscript is made.'),
        dict(form=r"G'(\alpha)", meaning='graph whose vertices label the summation and whose h-one appears in (56)',
             evidence='annotation beneath S-prime-alpha and final term of (56)',
             scope='Parentheses and alpha are baseline in both local occurrences.'),
        dict(form=r"\unsure{g'|\underline{g'}}", meaning='label on the map to N in the supplementary data',
             evidence='full data formula, crop 08_data',
             scope='Round g and prime are clear; underline versus long return tail remains local and unresolved.'),
    ],
    abbreviations=[
        dict(form='ens', expansion='ensemble'),
        dict(form='ens.', expansion='ensemble'),
        dict(form=r'\overline m', expansion='même'),
        dict(form='def', expansion='définition'),
    ],
    hand_log=[
        dict(habit='Some relation shafts terminate in a small one-sided hook or tooth; that is not enough by itself to certify an arrowhead.',
             pages='045', scope='Five marked relations remain locally undecided; the later inline G-zero/G and the first composite arrow have clear heads.',
             misread_places='M1003, M1004, M1005, M1009, M1010; no global arrow-to-dash replacement.'),
        dict(habit='A short lower-right foot can make the graph letter resemble C.',
             pages='045', scope='Only the arêtes clause is unresolved; the larger G labels elsewhere have distinct feet.',
             misread_places="C G-prime versus H C-prime in arêtes de ... contractées."),
        dict(habit='The m abbreviation has a visibly humped lower body beneath an independent overbar.',
             pages='045', scope='The inserted abbreviation after provienne only.',
             misread_places='M1006; H left this readable insertion as illegible.'),
        dict(habit='The return of a looped g can extend horizontally under its prime and resemble an underline.',
             pages='045', scope='The map label remains undecided; no systematic genus-label rule is inferred.',
             misread_places='M1007.'),
    ],
    notes=notes,
    check_events=[
        dict(statement_id=n['id'], date='2026-11-20',
             who='GPT-6 Astra Pro; inherited effort; SP77_C13_147 reader_b',
             type='carried as background without fault found',
             outcome='Reading only, no proof claim. The whole scan, native overlapping halves, and saved local crops were visually inspected; mathematical context did not replace uncertain or absent ink.')
        for n in notes
    ],
    coverage=dict(
        whole_viewed=True, halves_viewed=['top','bottom'], all_tokens_read=True,
        all_deletions_insertions_checked=True,
        differences_accounted="All 19 packet rows were reviewed. Scan metadata, wrappers around underlined G-prime, arrow/prime certainty alternatives, H's thin-space command after forall, and H's editorial-note wrappers are not substantive change rows. The arêtes letter, fixé/fini, struck/live soit and replacement placement, readable m-bar, cancelled numerical label, unwritten second S-prime, vertical I identification, formula annotation and footer are logged. The unaccented def was additionally checked against both witnesses. The g-label and relation-head doubts remain explicit. All word differences and changed places have a saved, inspected crop.",
        line_count_basis="25 physical lines/runs: 21 principal text, display, lower annotation and footer lines; one ordinaire insertion line; one interlinear level containing soit fixé, et and m-bar; and the two lower levels of the vertical def/I identification. Ordinary formula indices/exponents are not counted as additional lines.",
        numeral_coverage="55 and G_0 in box B01; inline G_0 in B02 and B04; cancelled (55)/(56) in B08; 56 and superscript 1 in B12; footer 44 in B13.",
        crop_reading_note="Every final saved crop was viewed. Crop 08 was extended upward before its label decision because the first boundary clipped the prime; the replacement includes the complete formula label. No decided place was recropped."
    ),
    unresolved=[d['place'] for d in doubts],
    crop_files=[crop[name] for name, box in specs]
)
(work / 'records/147_scan045.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
(work / 'records/147_scan045_crop_specs.json').write_text(json.dumps(
    [dict(name=name, box=box, crop=crop[name]) for name, box in specs], ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(scan=45, changes=len(changes), decisions=len(decisions),
    supplemental=len(supplemental), boxes=len(boxes), crops=len(specs),
    unresolved=len(doubts), line_count=25)))
