from pathlib import Path
import json

base = Path('/workspace/scratch/88012a0a2bcc')
work = base / 'SP77_C13_147_work'
draft = (base / 'inputs/SP77_C13_147_texts/pages/147_scan048.tex').read_text()
replacements = [
    (r'\unsure{arêtes}', 'arêtes'),
    (r'Soit, pour tt ', r'Soit, pour \unsure{tt|$\forall$} '),
    (r"\unsure{G^!|G'_{\cdot}}", r"G'_{\cdot}"),
    (r"$S'$ et $C'$)\deleted{$\unsure{=A'|C'}$},",
     r"$S'$ et $\overset{\deleted{\unsure{\sim}}}{C'}$)\deleted{$\unsure{=\widetilde{A}'\vert C')}$},"),
    (r'\unsure{m.graphe}', 'm.graphe'),
    (r"S'_\alpha\mathbin{\text{---}}\mathbf{N}",
     r"S'_\alpha\unsure{\mathbin{\text{---}}|\longrightarrow}\mathbb N"),
    (r"g':S'\mathbin{\text{---}}\mathbf{N}",
     r"\underline{g}':S'\mathbin{\text{---}}\mathbb N"),
]
for old, new in replacements:
    assert draft.count(old) == 1, (old, draft.count(old))
    draft = draft.replace(old, new)
(work / 'drafts/147_scan048.tex').write_text(draft)

specs = [
    ('01_heading', [870,20,970,80]),
    ('02_opening', [315,35,1660,180]),
    ('03_quotes', [315,180,1355,285]),
    ('04_pi', [305,285,1010,385]),
    ('05_conn', [1080,285,1680,390]),
    ('06_pourtt', [835,385,1640,520]),
    ('07_alpha', [315,385,1640,615]),
    ('08_ssgraphe', [1315,700,1670,815]),
    ('09_subgraph', [305,830,710,955]),
    ('10_struck', [1090,795,1677,960]),
    ('11_mgraphe', [755,950,1075,1145]),
    ('12_genre', [1290,1045,1575,1155]),
    ('13_localmap', [300,1155,655,1290]),
    ('14_gmap', [1145,1135,1625,1290]),
    ('15_correction', [705,1625,1570,1780]),
    ('16_rigidite', [305,1785,815,1940]),
    ('17_etalors', [305,1925,620,2050]),
    ('18_alors', [305,2140,565,2260]),
    ('19_footer', [15,2280,100,2355]),
]
crop = {name: f'crops/147_scan048_{name}.jpg' for name, box in specs}
bounds = dict(specs)
def locus(name):
    return crop[name] + ' (' + ','.join(map(str, bounds[name])) + ')'
def dq(text):
    return chr(96)*2 + text + "''"

changes = []
def change(place, C, H, final, dc, dh, kind, evidence, name, confidence, consequential, category):
    changes.append(dict(id=f'048-{len(changes)+1:02}', place=place, C=C, H=H,
        final=final, diff_C=dc, diff_H=dh, kind=kind, evidence=evidence,
        crop=crop[name], box=bounds[name], confidence=confidence,
        consequential=consequential, error_category=category))

change("quotation of contractent en un point",
    dq('contractent en un point'), "« contractent en un point »",
    dq('contractent en un point'), False, True, "other",
    "The opening mark is a small joined pair of high ticks, and the closing mark consists of two separate upright ticks. The closing mark is not a pair of angle-shaped guillemets.",
    '03_quotes', 'high', False, 'Other')
change("bracketed connectedness statement",
    '0-conn.', '0-connexe', '0-conn.', False, True,
    "abbreviation expanded or spelling modernised",
    "After the zero and hyphen, conn ends in two flattened humps and a separate low dot. There is no written exe continuation.",
    '05_conn', 'high', False, 'Abbreviations expanded, spelling modernised')
change("after Soit, pour, before the line-broken membership expression",
    'tt', r'\forall', r'\unsure{tt|$\forall$}', False, True,
    "misread symbol or index",
    "The mark has two tall joined strokes, a low return, a separate descending right foot, and one common cross stroke. These favor joined tt, but its resemblance to the author's universal-quantifier shape is real; the local choice remains explicitly doubtful. The whole line-broken membership expression is included in crop 07.",
    '07_alpha', 'medium', False, 'Symbols and indices')
change("une composante connexe du ... graphe",
    'ss-graphe', 's-graphe', 'ss-graphe', False, True, "misread word",
    "Before the short hyphen there are two joined s bodies: a first low hooked body and a second taller return. The written abbreviation has doubled s.",
    '08_ssgraphe', 'high', False, 'Words')
change("subgraph label before de G-prime défini par",
    r"\unsure{G^!|G'_{\cdot}}", r"G'_{!}", r"G'_{\cdot}", True, True,
    "misread symbol or index",
    "The capital G has a detached high prime and a separate compact low dot. The lower mark has no upright stem. The high prime is not an exponent exclamation mark, and the low mark is not a subscript exclamation mark.",
    '09_subgraph', 'high', True, 'Symbols and indices')
change("small cancelled supralinear mark over C-prime in défini par S-prime et C-prime",
    r"C'", r"C'", r"\overset{\deleted{\unsure{\sim}}}{C'}", True, True,
    "omission",
    "Above the live C-prime is a separate small cancelled cluster. Beneath the zigzag cancellation, a curved/wavy return survives. A tilde is a tentative reconstruction only; the original mark is not securely recoverable. Its position over C-prime is preserved rather than silently omitting the cancelled ink.",
    '10_struck', 'low', True, 'Omissions')
change("cancelled expression following the first closing parenthesis after C-prime",
    r")\deleted{$\unsure{=A'|C'}$},",
    r", \struck{\ill{}})",
    r")\deleted{$\unsure{=\widetilde{A}'\vert C')}$},",
    True, True, "omission",
    "A live closing parenthesis precedes the cancelled expression. Under the diagonal strikes are two equality strokes, an A-like body with a raised wavy stroke and prime, a nearly vertical restriction bar, a C-like body/prime, and another closing parenthesis at the right. The expanded reading is wholly tentative because the cancellation crosses these strokes. The comma below the first closing-parenthesis area remains live.",
    '10_struck', 'low', True, 'Struck text')
change("graph term after et G-underlined-prime-alpha le",
    r'\unsure{m.graphe}', 'MD-graphe', 'm.graphe', False, True,
    "abbreviation expanded or spelling modernised",
    "A low m-shaped abbreviation is followed by a separate full stop and the word graphe. There are no capital M and D or a hyphen at this place. The g has a round head and a long, almost straight descender.",
    '11_mgraphe', 'high', False, 'Abbreviations expanded, spelling modernised')
change("quotation of genre",
    dq('genre'), "« genre »", dq('genre'), False, True, "other",
    "Both sides of genre have paired short upright ticks, not angle-shaped guillemets.",
    '12_genre', 'high', False, 'Other')
change("local genre map from S-prime-alpha",
    r"S'_\alpha\mathbin{\text{---}}\mathbf{N}",
    r"S'_\alpha \to \mathbb{N}",
    r"S'_\alpha\unsure{\mathbin{\text{---}}|\longrightarrow}\mathbb N",
    True, True, "misread symbol or index",
    "S has a high prime and lowered alpha. The relation shaft ends in a small tooth/downturn whose status as an arrowhead is not secure, so the literal-shaft reading is kept first under doubt. N has two distinct parallel strokes along its left limb, supporting the double-stroked alphabet rather than a merely bold N.",
    '13_localmap', 'medium', True, 'Symbols and indices')
change("inducing map label and map from S-prime",
    r"g':S'\mathbin{\text{---}}\mathbf{N}",
    r"g' : S' \to \mathbb{N}",
    r"\underline{g}':S'\mathbin{\text{---}}\mathbb N",
    True, True, "misread symbol or index",
    "The round-headed g has a straight descending stem and a separate horizontal bar crossing below the head; this bar is not a returning descender loop. The prime is detached above-right. The map shaft ends in a short down-hook without two converging arrowhead wings. The N again has a doubled left limb.",
    '14_gmap', 'high', True, 'Symbols and indices')
change("replacement above satisfait la condition",
    r"\deleted{satisfait la condition} \inserted{est stable (condition de}",
    r"\struck{satisfait la condition} \add{est stable} (condition de",
    r"\deleted{satisfait la condition} \inserted{est stable (condition de}",
    False, True, "insertion or placement",
    "The full baseline phrase satisfait la condition is traversed by one cancellation stroke. The complete phrase est stable (condition de is written on the separate upper level; the parenthesis and condition de belong to that insertion as C records.",
    '15_correction', 'high', False, 'Insertions put in the wrong place')
change("word before MD) in the rigidity condition",
    'rigidité', 'régularité', 'rigidité', False, True, "misread word",
    "The initial r and dotted i are followed by a looped g, a short i, a looped d, another short i, a tall t and an accented final e. The longer régularité sequence is not present.",
    '16_rigidite', 'high', True, 'Words')
change("consequence after le sont and the dash",
    'et alors', 'et dans ce cas', 'et alors', False, True, "misread word",
    "After et, the word has an initial rounded a, a tall l, and the flattened ors ending. No separate dans, ce or cas words are written.",
    '17_etalors', 'high', False, 'Words')
change("last line after si G-underlined-prime est un MD-graphe",
    'alors', 'donc', 'alors', False, True, "misread word",
    "The initial a loop joins a tall l, followed by the low ors sequence. There is no initial d or final c.",
    '18_alors', 'high', False, 'Words')
change("lower-left pencil numeral",
    r'\margin{47}', '[absent]', r'\margin{47}', False, True, "omission",
    "The first pencil digit is an open-topped 4; the second has a top bar, descending stroke and crossbar, reading 7. The footer reads 47.",
    '19_footer', 'high', False, 'Omissions')

decisions = [
    dict(id='M1016', cote='147', scan='48', decision='first', reading='arêtes',
         **{'what the ink shows': "The low initial a and r are followed by an accented e, the tall t, and the flattened es ending. The insertion de G-underlined-prime starts only after this complete word."},
         crop=locus('02_opening'), confidence='high'),
    dict(id='M1017', cote='147', scan='48', decision='undecided', reading=r'\unsure{\alpha}',
         **{'what the ink shows': "The first membership letter has a looped alpha-like body and crossing right tail, but several retraced loops obscure its original contour. Alpha remains the leading reading without being certified."},
         crop=locus('07_alpha'), confidence='medium'),
    dict(id='M1018', cote='147', scan='48', decision='alternative', reading=r"G'_{\cdot}",
         **{'what the ink shows': "A separate high prime stands to the right of G and a compact dot lies lower still. The dot has no vertical stem. The two marks occupy different levels."},
         crop=locus('09_subgraph'), confidence='high'),
    dict(id='M1019', cote='147', scan='48', decision='first', reading='m.graphe',
         **{'what the ink shows': "A low m-like group and full stop precede the separate word graphe. The long g descender, r/a low joins, p descender, h ascender and final e are present."},
         crop=locus('11_mgraphe'), confidence='high'),
]
supplemental = [
    dict(id='U048-01', cote='147', scan='48',
         place='nested C doubt in the cancelled expression after C-prime',
         decision='undecided',
         reading=r"\deleted{$\unsure{=\widetilde{A}'\vert C')}$}",
         **{'what the ink shows': "The equality strokes, angular A-like body, raised wavy mark/prime, near-vertical bar, C-like body/prime and final parenthesis can be followed only in parts through the cancellation. The reconstruction is extended but remains wholly doubtful; it is not a resolved C mark."},
         crop=locus('10_struck'), confidence='low'),
]

box_readings = [
    ('01_heading', 'handwritten author page number', r'\mspage{23}'),
    ('02_opening', 'resolved C word doubt; insertion and attachment; clear B',
     r"tel que $B$ soit l'ens des arêtes \inserted{de $\underline{G}'$} qui"),
    ('03_quotes', 'source quotation marks', 'se ' + dq('contractent en un point') + '.'),
    ('04_pi', 'whole formula; both handwritten subscript zeros',
     r"\pi_0(G')\overset{\sim}{\longrightarrow}\pi_0(G)"),
    ('05_conn', 'C/H abbreviation difference; handwritten zero',
     r"[donc $G$ est $0$-conn."),
    ('06_pourtt', 'cancelled prose', r'\deleted{Pour que}'),
    ('07_alpha', 'whole line-broken doubtful membership expression; C/H tt difference',
     r"ssi $G'$ l'est]. \deleted{Pour que} Soit, pour \unsure{tt|$\forall$} $\unsure{\alpha}\in S$ (ens des sommets de $\underline{G}$) $G'_\alpha$ le"),
    ('08_ssgraphe', 'C/H abbreviation difference', 'du ss-graphe'),
    ('09_subgraph', 'whole C-doubt monomial and nearby comparison',
     r"$G'_{\cdot}$ de $G'$"),
    ('10_struck', 'whole formula cluster with cancelled mark and cancelled expression',
     r"$S'$ et $\overset{\deleted{\unsure{\sim}}}{C'}$)\deleted{$\unsure{=\widetilde{A}'\vert C')}$},"),
    ('11_mgraphe', 'resolved C word doubt; C/H abbreviation difference', 'm.graphe'),
    ('12_genre', 'source quotation marks', dq('genre')),
    ('13_localmap', 'whole doubtful formula; double-stroked N',
     r"S'_\alpha\unsure{\mathbin{\text{---}}|\longrightarrow}\mathbb N"),
    ('14_gmap', 'whole corrected map formula; underline and literal relation stroke',
     r"\underline{g}':S'\mathbin{\text{---}}\mathbb N,"),
    ('15_correction', 'complete struck phrase and replacement insertion',
     r"\deleted{satisfait la condition} \inserted{est stable (condition de}"),
    ('16_rigidite', 'C/H word difference', 'rigidité MD)'),
    ('17_etalors', 'C/H word difference', 'et alors'),
    ('18_alors', 'C/H word difference', 'alors'),
    ('19_footer', 'handwritten margin numeral', r'\margin{47}'),
]
boxes = []
for i, (name, kind, reading) in enumerate(box_readings, 1):
    x0,y0,x1,y1 = bounds[name]
    boxes.append(dict(box=f'048-B{i:02}', kind=kind, x0=x0, y0=y0,
        x1=x1, y1=y1, reading=reading))

inventory = []
def item(kind, position, content, hand='his hand'):
    inventory.append(dict(scan=48, sheet_kind='text', hand=hand,
        element=f'048-E{len(inventory)+1:02}', kind=kind, position=position,
        first_words_or_objects=content, transcribed='yes'))
item('text', 'top centre', '23')
item('text', 'opening two lines', 'tel que B soit ... contractent en un point. On a')
item('insertion', 'upper-right above arêtes / qui', 'de G-underlined-prime')
item('display', 'upper formula line', 'pi-zero(G-prime) isomorphism pi-zero(G)')
item('text', 'same level as the display and following line', '[donc G est 0-conn. ssi G-prime l’est]')
item('deletion', 'before Soit in the upper paragraph', 'Pour que')
item('text', 'from Soit through défini par S-prime et C-prime', 'Soit, pour ... alpha in S ...')
item('deletion', 'small supralinear cluster above C-prime', 'tentatively a cancelled tilde-shaped mark')
item('deletion', 'after the first closing parenthesis following C-prime', 'tentatively = A-tilde-prime vertical-bar C-prime followed by closing parenthesis')
item('text', 'middle paragraph', 'et G-underlined-prime-alpha le m.graphe ... application genre ...')
item('text', 'two inline genre maps', 'S-prime-alpha to N; underlined g-prime: S-prime to N')
item('text', 'marking-set sentence and formulas', 'et en prenant comme ens de pts marqués ...')
item('display', 'lower-middle row of set formulas', 'B-tilde-prime = A-tilde-prime minus C-tilde-prime ...')
item('text', 'last paragraph', 'Alors G-underlined-prime ... rigidité MD ... Par suite ...')
item('deletion', 'baseline after Alors G-underlined-prime', 'satisfait la condition')
item('insertion', 'above that cancellation', 'est stable (condition de')
item('margin note', 'lower-left pencil footer', '47', hand='unattributed pencil numeral')

doubts = [
    dict(place='M1017, first membership letter',
         reading=r'\unsure{\alpha}', alternatives='alpha; original contour obscured by retracing',
         confidence='medium', reason=decisions[1]['what the ink shows']),
    dict(place='after Soit, pour', reading=r'\unsure{tt|$\forall$}',
         alternatives=r'tt | \forall', confidence='medium',
         reason='Joined tall strokes and a common cross stroke favor tt, but the locally similar quantifier form cannot be excluded.'),
    dict(place='cancelled mark over C-prime', reading=r'\deleted{\unsure{\sim}}',
         alternatives='tentative tilde-shaped decoration; original mark not securely recovered',
         confidence='low',
         reason='A small separate cluster above C-prime has a curved return beneath zigzag cancellation. Tilde is not certified.'),
    dict(place='cancelled expression after C-prime (unindexed C doubt)',
         reading=r"\deleted{$\unsure{=\widetilde{A}'\vert C')}$}",
         alternatives='tentative expanded equality/restriction expression; raised marks and letters remain crossed',
         confidence='low', reason=supplemental[0]['what the ink shows']),
    dict(place='S-prime-alpha/N relation',
         reading=r'\unsure{\mathbin{\text{---}}|\longrightarrow}',
         alternatives='literal long shaft | right arrow', confidence='medium',
         reason='The end has a small upper tooth and downturned terminal but no unambiguous complete head; both readings remain possible.'),
]
notes = [
    dict(id='147-048-N01',
         text="Author page 23, with pencil footer 47, describes a contraction, states an isomorphism on the pi-zero sets, defines graph fibers and their marked points, and relates stability of the original marked graph to stability of the local marked graphs. The final consequence for MD-graphs is carried as the author's assertion. No contraction construction or stability equivalence was proved during this reading."),
    dict(id='147-048-N02',
         text="The opening B is visibly written and is retained; H's note proposing C-prime is editorial context, not source text. The small cancelled mark over C-prime and the following crossed equality/restriction expression have been preserved tentatively. The latter has a near-vertical bar; it has not been silently changed into set difference or certified from the surrounding mathematics."),
]
record = dict(
    scan=48, reader='reader_b', line_count=23,
    changes=changes, decisions=decisions,
    supplemental_unindexed_C_doubts=supplemental,
    inventory=inventory, boxes=boxes, doubts=doubts,
    notation=[
        dict(form=r"G'_{\cdot}", meaning='subgraph defined by S-prime and C-prime in this paragraph',
             evidence='full monomial crop 09_subgraph',
             scope='One detached high prime and one separate low dot confirmed locally; not an exclamation mark.'),
        dict(form=r"\underline{g}'", meaning='inducing genus-map label',
             evidence='full formula crop 14_gmap',
             scope='The g has a straight descender and an independent lower crossbar; the high prime remains outside the underline.'),
        dict(form=r'\mathbb N', meaning='target of the two written genre maps',
             evidence='crops 13_localmap and 14_gmap',
             scope='Both occurrences have a doubled left limb.'),
        dict(form=r"G'_\alpha,\underline{G}'_\alpha",
             meaning='fiber graph and associated marked graph named in the main paragraph',
             evidence='native top half, lines beginning G-prime-alpha le and et G-underlined-prime-alpha',
             scope='Bare alpha is lowered; this is distinct from the baseline parenthesized alpha in the last paragraph.'),
        dict(form=r"\underline{G}'(\alpha)",
             meaning='local graph label in the stability statement and final consequence',
             evidence='native bottom half, the two final parenthesized-alpha graph labels',
             scope='Both parenthesized alpha labels are on the baseline.'),
    ],
    abbreviations=[
        dict(form='ens', expansion='ensemble'),
        dict(form='conn.', expansion='connexe'),
        dict(form='ssi', expansion='si et seulement si'),
        dict(form='ss-', expansion='sous-'),
        dict(form='pts', expansion='points'),
        dict(form='m.graphe', expansion='Graph term abbreviated by the author; expansion of m. not established on this page.'),
        dict(form='tt', expansion='tout, if the doubtful double-t reading is confirmed'),
    ],
    hand_log=[
        dict(habit='A separate prime and low dot can resemble one exclamation-like sequence if their levels are collapsed.',
             pages='048', scope='The single G-prime-dot label here is clear.',
             misread_places='M1018: C first candidate G exponent exclamation; H G-prime subscript exclamation.'),
        dict(habit='The g descender can be very long and nearly straight, with only a small terminal hook.',
             pages='048', scope='graphe and the g-prime map label; the independent bar on the latter is retained separately.',
             misread_places='The underline of g-prime is absent from both C and H.'),
        dict(habit='Double s in the abbreviation ss- is tightly joined and can look like one sign.',
             pages='048', scope='The ss-graphe occurrence in the subgraph parenthesis.',
             misread_places='H s-graphe.'),
        dict(habit='Joined tt and the universal-quantifier form remain difficult to distinguish from shape alone at this occurrence.',
             pages='048', scope='Only the mark after Soit, pour is left doubtful; no global identification is imposed.',
             misread_places='C tt versus H forall.'),
    ],
    notes=notes,
    check_events=[
        dict(statement_id=n['id'], date='2026-11-20',
             who='GPT-6 Astra Pro; inherited effort; SP77_C13_147 reader_b',
             type='carried as background without fault found',
             outcome='Reading only, no proof claim. The complete source, native halves and final saved crops were inspected. Uncertain cancelled ink remains uncertain.')
        for n in notes
    ],
    coverage=dict(
        whole_viewed=True, halves_viewed=['top','bottom'], all_tokens_read=True,
        all_deletions_insertions_checked=True,
        differences_accounted="All 30 packet rows were reviewed. Scan metadata, H's author-page note and expectation note, equivalent isomorphism-arrow macros, display/inline wrapping, thin-space commands mis-tokenized as commas, and dash-length syntax are not change rows. Actual quotation marks, conn., tt/forall, ss-, the graph prime/dot, the cancelled formula and parenthesis placement, m.graphe, both genre maps, insertion span, rigidité, both alors occurrences and footer 47 are logged. The cancelled mark over C-prime, doubled N limbs and underline on g-prime were additionally found in the full ink reading. H's expected C-prime was not substituted for the clear opening B.",
        line_count_basis="23 physical lines: author heading 23; 19 main written lines, with the pi-zero display and the first bracketed clause sharing one line; the upper de G-prime insertion; the lower est stable (condition de insertion; and pencil footer 47. The cancelled decoration over C-prime is a mathematical mark, not an added text line.",
        numeral_coverage="Author 23 in B01; both pi-zero subscripts in B04; the zero of 0-conn. in B05; pencil 47 in B19.",
        crop_reading_note="All nineteen final saved crops were viewed. Crop 07 was expanded, while its reading was still unresolved, to include both lines of the membership expression. Crop 11 was expanded before deciding m.graphe to include the complete long g descender. No decided place was recropped."
    ),
    unresolved=[d['place'] for d in doubts],
    crop_files=[crop[name] for name, box in specs],
)
(work / 'records/147_scan048.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
(work / 'records/147_scan048_crop_specs.json').write_text(json.dumps(
    [dict(name=name, box=box, crop=crop[name]) for name, box in specs],
    ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(scan=48, changes=len(changes), decisions=len(decisions),
    supplemental=len(supplemental), boxes=len(boxes), crops=len(specs),
    unresolved=len(doubts), line_count=23)))
