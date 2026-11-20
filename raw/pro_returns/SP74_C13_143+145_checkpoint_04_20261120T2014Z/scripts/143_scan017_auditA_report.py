import json
from pathlib import Path

ROOT = Path('/workspace/scratch/8f839dff4bf0')
WORK = ROOT / 'SP74_C13_143+145_work'
KEY = '143_scan017'
packet = json.loads((ROOT / 'reader_packets' / f'{KEY}.json').read_text())
prior = json.loads((WORK / 'reviews' / f'{KEY}_accepted.json').read_text())
accepted = (WORK / 'pages' / f'{KEY}.tex').read_text()

before_set = r'\inserted{\ne\varnothing},'
after_set = r'''\begin{tikzpicture}[baseline=(comma.base)]
\node[anchor=base,inner sep=0pt] (comma) at (0,0) {$,$};
\node[anchor=base,inner sep=0pt] at (-.13,.50) {$\inserted{\ne\varnothing}$};
\draw[line width=.3pt] (-.22,-.28) .. controls (-.13,.06) and (.30,.29) .. (.36,.48) .. controls (.39,.58) and (.35,.60) .. (.30,.61);
\end{tikzpicture}'''
before_groupoid = r'\inserted{\unsure{non vide|$\ne\varnothing$}} connexe'
after_groupoid = r'''\begin{tikzpicture}[baseline=(word.base)]
\node[anchor=base west,inner sep=0pt] (word) at (0,0) {connexe};
\node[anchor=base east,inner sep=0pt] at (.20,.52) {\inserted{\unsure{non vide|$\ne\varnothing$}}};
\draw[line width=.3pt] (-.18,-.20) .. controls (-.28,.02) and (-.02,.27) .. (.36,.42) .. controls (.51,.50) and (.53,.57) .. (.40,.60);
\end{tikzpicture}'''

findings = [
    {
        'place': 'Action-set row, raised nonempty condition and long curved attachment (inventory E07)',
        'before': before_set,
        'after': after_set,
        'reason': 'The crossed pair of horizontal strokes and diagonally slashed oval stand above the line, over the end of ens and the following gap. A distinct long dark guide starts below the baseline at the left, rises diagonally right through the insertion gap, and curls left at its upper end beside the condition. The baseline comma lies to the right of the lower part of the guide. The guide has no arrowhead. Both the relative raised placement and the drawn guide are absent from the accepted inline inserted wrapper. The condition itself remains ne-varnothing; neither wording nor punctuation is changed.',
        'confidence': 'high',
        'crop': 'crops/143_scan017_readerC_action-set.png',
        'box': [470, 1089, 1559, 1230],
        'against_C': True,
        'against_H': True,
        'C': before_set,
        'H': r'\neq \emptyset,',
        'kind': 'insertion or placement',
        'consequential': False,
        'marked_in_H': False,
        'decision_updates': [],
        'certainty_only': False,
        'existing_difference_row': 'Extends accepted change row 9, Action-set row, acting group and abbreviation punctuation, by reproducing its described but undrawn guide; its textual reading is retained.'
    },
    {
        'place': 'Small interlinear addition before connexe, curved attachment (inventory E10; M0690 content unchanged)',
        'before': before_groupoid,
        'after': after_groupoid,
        'reason': 'A separate thick guide begins below the writing line just before connexe, turns upward beside the initial c, then bends right above the word and curls left at its upper end. The small doubtful inscription sits above the end of groupoïde and before connexe, separate from this guide. Its visible content remains only a small loop with an upper entry stroke and a short detached horizontal stroke; the guide does not supply the missing letters or mathematical signs. The accepted inline wrapper records the addition but omits this physical raised placement and curved attachment.',
        'confidence': 'high',
        'crop': 'crops/143_scan017_readerC_groupoid-insertion.png',
        'box': [733, 1408, 1224, 1549],
        'against_C': True,
        'against_H': True,
        'C': before_groupoid,
        'H': r'\marginal{interligne : « \uncertain{non vide} »} connexe',
        'kind': 'insertion or placement',
        'consequential': False,
        'marked_in_H': False,
        'decision_updates': [],
        'certainty_only': False,
        'existing_difference_row': None,
        'scope': 'High confidence concerns the guide and placement only. M0690 remains low-confidence and undecided; H’s uncertainty concerns the content, not the omitted guide.'
    },
]

candidate = accepted
for item in findings:
    assert candidate.count(item['before']) == 1, item['place']
    candidate = candidate.replace(item['before'], item['after'], 1)
    assert item['C'] in packet['witness_C'], ('C', item['place'])
    assert item['H'] in packet['witness_H'], ('H', item['place'])
    assert (WORK / item['crop']).exists()

crop_boxes = [
    ('143_scan017_readerC_action-set.png', [470, 1089, 1559, 1230]),
    ('143_scan017_readerC_groupoid-insertion.png', [733, 1408, 1224, 1549]),
    ('143_scan017_readerC_tuple.png', [1024, 1301, 1491, 1421]),
    ('143_scan017_readerC_action-map.png', [350, 1758, 1062, 1878]),
    ('143_scan017_readerC_extension.png', [450, 1025, 1594, 1127]),
    ('143_scan017_main_action_group.png', [1210, 1520, 1620, 1655]),
    ('143_scan017_readerC_deleted-word.png', [373, 1662, 988, 1773]),
    ('143_scan017_main_upper_groups.png', [290, 375, 1635, 575]),
    ('143_scan017_readerC_quotient.png', [938, 575, 1568, 726]),
    ('143_scan017_readerC_formula-numbers.png', None),
    ('143_scan017_main_category_C.png', [375, 1220, 1375, 1320]),
]

confirmed = [
    {
        'element': 'E01', 'place': 'Opening continuation', 'crop': 'page',
        'evidence': 'Read d’où aussitôt la flèche envisagée in full. Apostrophes/accents and the final dark point are retained. The opening is lower-case d; there is no heading, upper pagination or added conjunction.'
    },
    {
        'element': 'E02', 'place': 'Entire upper request paragraph',
        'crop': ['crops/143_scan017_main_upper_groups.png', 'crops/143_scan017_readerC_formula-numbers.png', 'crops/143_scan017_readerC_quotient.png'],
        'evidence': 'Read Il faudrait encore expliciter comment (7) (8) résultent de la donnée de l’opération ... induisant une opération libre ... (ayant J comme ens quotient). The first reference has a crossed nearly vertical 7 whose curved crown is close to the opening parenthesis; the second has two crossed closed loops, 8. Each reference has its own parentheses. Both rounded group letters have separate high primes, both looped X objects have separate tildes/primes and capital J arguments, and the intervening pi has one low 1 followed by an open inclusion. Libre alone is underlined. Ens is visibly present before quotient, without a point after ens. Four dark, similarly weighted points follow the closing parenthesis. The isolated lower/right blot outside this line is not treated as an additional point.'
    },
    {
        'element': 'E03', 'place': 'Reformulation heading', 'crop': 'page',
        'evidence': 'The word Reformulation is live and has one underline. No separate final colon or period is secured, so none is supplied.'
    },
    {
        'element': 'E04', 'place': 'Introduction to braced system', 'crop': 'page',
        'evidence': 'Read Considérons les systèmes, including the accents and plural endings. The brace opens below this phrase and spans both rows, with no matching right brace.'
    },
    {
        'element': 'E05', 'place': 'Entire extension row', 'crop': 'crops/143_scan017_readerC_extension.png',
        'evidence': 'Read the five objects 1, pi, rounded E/Sigma, calligraphic G, 1 in order. Pi is unindexed and no group in this row is primed. All four connectors are bare shafts: first and last have small endpoint deposits, while the middle two end flat; none has the two-sided pointed head visible on the lower action map. The text is ext. de groupes, with a point after ext.; its compressed connected letter middles were compared locally with the later groupe. No normalized arrowheads or expanded ext. were added.'
    },
    {
        'element': 'E06', 'place': 'Entire action-set row', 'crop': 'crops/143_scan017_readerC_action-set.png',
        'evidence': 'The initial set letter has a diagonal top transition and a large 3-like lower return, retained as the provisional mathfrak Z rendering. The next group is unprimed E/Sigma, followed by one hyphen and ens without an abbreviation point. After the inserted condition comes a baseline comma and où, then unindexed pi, an open inclusion, the third unprimed E/Sigma and opère librement. Every sign and the final word ending were inspected; no final point is supplied.'
    },
    {
        'element': 'E07', 'place': 'Raised nonempty condition and guide', 'crop': 'crops/143_scan017_readerC_action-set.png',
        'evidence': 'The content has two crossed horizontal strokes and a slashed oval, supporting ne-varnothing. It is live and above the row. The large separate guide rises from below the baseline to a curl at the right of the inscription. Finding 1 reproduces its shape and placement; no additional punctuation is inferred from the curl.'
    },
    {
        'element': 'E08', 'place': 'First category declaration', 'crop': 'crops/143_scan017_main_category_C.png',
        'evidence': 'Read Ils forment une catégorie C. Catégorie is underlined by one stroke; its g descender is a letter stroke, not a second underline. C has a small curled upper turn and an open lower return. The paper immediately after C is blank: retain the accepted absence of a terminal point, despite C/H agreement on one.'
    },
    {
        'element': 'E09', 'place': 'Entire groupoid-and-action definition paragraph',
        'crop': ['crops/143_scan017_readerC_tuple.png', 'crops/143_scan017_readerC_action-map.png', 'crops/143_scan017_main_action_group.png', 'crops/143_scan017_readerC_deleted-word.png'],
        'evidence': 'Read Considérons les systèmes and all five tuple entries, delimiters and commas. The tuple has plain Pi, covered Pi, p, G and a small g with a closed upper bowl and a descending hooked return. The following marks are a short o, low u and high accent, supporting où rather than a colon. Continue: Pi est un groupoïde ... connexe, p: covered Pi to Pi un rev. universel de Pi, et G un groupe opérant [deletion] sur Pi par automorphismes par a: G to Aut(Pi). All eight capital-Pi occurrences, both cover tildes, both p forms, three G forms in this paragraph, colon pairs and two right arrowheads were checked. The action label is a low, slightly rising compressed a-wave without any descender; the distinct tuple g is retained. Rev. remains abbreviated. There is a dark point after the map and a live subsequent sentence Ils forment une catégorie C-prime with its own point.'
    },
    {
        'element': 'E10', 'place': 'Small groupoid insertion', 'crop': 'crops/143_scan017_readerC_groupoid-insertion.png',
        'evidence': 'The tiny loop/entry stroke and detached short bar do not spell securely either non vide or a complete ne-empty-set expression. M0690 remains undecided. The separately visible hooked guide is live and is reproduced in finding 2; it cannot be used as missing content.'
    },
    {
        'element': 'E11', 'place': 'Cancelled word after opérant', 'crop': 'crops/143_scan017_readerC_deleted-word.png',
        'evidence': 'A long dark horizontal strike crosses one word between opérant and the following live sur. A small upper loop, low left return and obscured following loop/strokes survive, admitting sur or de without deciding either. The preceding opérant and following sur Pi are live. No other deletion is inferred from heavy or retraced letter strokes.'
    },
    {
        'element': 'E12', 'place': 'Announcement of equivalences', 'crop': 'page',
        'evidence': 'Read On va définir des équivalences quasi-inverses l’une de l’autre, across all three lines. The plural endings and the hyphen in quasi-inverses are retained. No construction, equation number or concluding punctuation is added before the diagram.'
    },
    {
        'element': 'E13', 'place': 'Bottom two-arrow diagram', 'crop': 'page',
        'evidence': 'There are exactly two objects, C on the left and C-prime on the right. The upper shaft has a right head and alpha above it. The lower shaft has a left head and beta below it. The right-object prime is separate from the C; no label is moved across a shaft and no extra vertical connection or relation sign is supplied.'
    },
    {
        'element': 'E14', 'place': 'Lower-left pencil number', 'crop': 'page',
        'evidence': 'The native lower half shows 16: a thin slanting 1 and a 6 with a closed lower loop. Retain this lower-left pagination in an unnamed hand; do not attribute it to the author.'
    },
]

remaining = json.loads(json.dumps(prior['remaining_doubts']))
remaining[0].update({
    'audit_disposition': 'retained without narrowing',
    'audit_reason': 'All five rounded extension/action letters were rechecked. The first two have independent primes and the last three are unprimed; all remain compatible with the same E/Sigma alternatives. These preferred-alphabet rows are low-confidence and non-consequential.',
    'crop': ['crops/143_scan017_main_upper_groups.png', 'crops/143_scan017_readerC_extension.png', 'crops/143_scan017_readerC_action-set.png'],
})
remaining[1].update({
    'audit_disposition': 'retained without narrowing',
    'audit_reason': 'The reused crop supplies a small oval with an upper entry stroke and a separate short horizontal stroke beside the guide. These do not establish all letters of the verbal reading or all strokes of the symbolic alternative. The clearly symbolic first insertion cannot be copied into this different locus.',
    'crop': 'crops/143_scan017_readerC_groupoid-insertion.png', 'box': [733, 1408, 1224, 1549],
})
remaining[2].update({
    'audit_disposition': 'retained without narrowing',
    'audit_reason': 'The upper loop, low return and following strokes are intersected by the cancellation. Neither sur nor de can be recovered securely enough to suppress the alternative.',
    'crop': 'crops/143_scan017_readerC_deleted-word.png', 'box': [373, 1662, 988, 1773],
})

report = {
    'key': KEY, 'reader': 'A', 'stage': 'second reading', 'first_reader': 'C',
    'image_views': ['original', 'half1', 'half2'],
    'workflow': {
        'original': {'path': packet['image'], 'dimensions': [1692, 2362], 'views': 1},
        'halves': [{'path': p, 'box': b, 'views': 1} for p, b in zip(packet['halves'], packet['half_boxes'])],
        'reused_crops': [{'path': 'crops/' + p, 'box': b, 'visible_inspections': 1} for p, b in crop_boxes],
        'new_crops': [],
        'box_note': 'The existing formula-numbers crop was inspected without recropping. Its original-coordinate box was not recorded in the supplied accepted/first-reader report, so it is not invented here. Both finding boxes are recorded exactly.',
        'scope': 'Only scan017 material and the supplied common contracts/notation were used. The original and each native half were viewed once. No other page, OCR, research, TeX compilation, extra whole-page view or enlarged-half view was used.'
    },
    'findings': findings,
    'confirmed': confirmed,
    'remaining_doubts': remaining,
    'inventory_checked': [dict(element=x['element'], kind=x['kind'], position=x['position'], audit_status='checked; physical guide addition proposed' if x['element'] in ('E07', 'E10') else 'checked; accepted reading retained') for x in prior['inventory']],
    'inventory_additions': [
        {'parent_element': 'E07', 'kind': 'drawing', 'position': 'After ens, from below the row to the right of the raised ne-empty-set condition', 'first_words_or_objects': 'Long upward-curving attachment guide with a curled upper end, no arrowhead', 'transcribed': 'yes, in proposed candidate', 'hand': 'principal ink hand'},
        {'parent_element': 'E10', 'kind': 'drawing', 'position': 'Before connexe, rising beside its c to the small doubtful insertion', 'first_words_or_objects': 'Separate hooked attachment guide with low stem and curled upper end', 'transcribed': 'yes, in proposed candidate', 'hand': 'principal ink hand'},
    ],
    'physical_marks_checked': {
        'Pi_occurrences': [
            {'place': 'Tuple, first component', 'reading': r'\Pi', 'marks': 'no cover or index'},
            {'place': 'Tuple, second component', 'reading': r'\widetilde\Pi', 'marks': 'high wave joined near the cap but distinct from its horizontal bar'},
            {'place': 'After tuple où', 'reading': r'\Pi', 'marks': 'plain two-legged capital'},
            {'place': 'p map source', 'reading': r'\widetilde\Pi', 'marks': 'separate high wave'},
            {'place': 'p map target', 'reading': r'\Pi', 'marks': 'plain cap, no tilde'},
            {'place': 'rev. universel de', 'reading': r'\Pi', 'marks': 'plain capital; following comma distinct'},
            {'place': 'Live sur after deletion', 'reading': r'\Pi', 'marks': 'plain capital'},
            {'place': 'Aut target argument', 'reading': r'\Pi', 'marks': 'plain capital within parentheses'},
        ],
        'pi_occurrences': [
            {'place': 'Upper subgroup inclusion', 'reading': r'\pi_1', 'marks': 'one low 1'},
            {'place': 'Extension kernel', 'reading': r'\pi', 'marks': 'no index'},
            {'place': 'Action-set inclusion', 'reading': r'\pi', 'marks': 'no index'},
        ],
        'covered_X_objects': [
            {'place': 'Upper paragraph after first sur', 'reading': r"\widetilde{\mathfrak X}'(J)", 'marks': 'separate tilde, X prime and capital J argument'},
            {'place': 'Upper paragraph after second sur', 'reading': r"\widetilde{\mathfrak X}'(J)", 'marks': 'separate tilde, X prime and capital J argument'},
        ],
        'extension_group_occurrences': [
            {'place': 'First acting group in upper paragraph', 'prime': True},
            {'place': 'Upper subgroup inclusion target', 'prime': True},
            {'place': 'Extension middle group', 'prime': False},
            {'place': 'Action-set prefix before ens', 'prime': False},
            {'place': 'Action-set inclusion target', 'prime': False},
        ],
        'G_occurrences': ['Extension quotient', 'Tuple fourth component', 'Prose un groupe declaration', 'Action-map source'],
        'p_occurrences': ['Tuple third component', 'Cover-map label'],
        'action_letters': [{'place': 'Tuple final component', 'reading': 'g', 'evidence': 'closed upper oval and separate descending hooked return'}, {'place': 'Action-map label before colon', 'reading': 'a', 'evidence': 'low compressed wave with short rise, no descending stroke'}],
        'category_objects': ['First declaration C, no terminal point', 'Second declaration C-prime, followed by a point', 'Bottom left C', 'Bottom right C-prime'],
        'underlines': ['libre', 'Reformulation', 'first catégorie'],
        'connectors': ['Four bare extension shafts', 'Cover map p: right arrowhead', 'Action map a: right arrowhead', 'Bottom alpha: upper right arrowhead', 'Bottom beta: lower left arrowhead'],
        'other': 'References (7) and (8), four upper continuation points, two curved insertion guides, one cancelled word, and pencil pagination 16 were each checked.'
    },
    'marks_rechecked': [{'id': 'M0690', 'decision': 'undecided', 'reading': r'\unsure{non vide|$\ne\varnothing$}', 'confidence': 'low', 'disposition': 'Accepted content decision retained; separate physical-guide finding proposed.'}],
    'existing_difference_review': 'All 16 accepted change rows, the two explicitly excluded G-rendering rows and all 29 raw packet differences were considered during the whole-page reading. No textual row is reversed or given a new confidence. Row 9’s insertion description is supplemented by an actual drawing. Pure G rendering remains excluded; X and Z alphabet encoding remains medium/non-consequential; pure E/Sigma rows remain low/non-consequential. Mixed diagram or insertion rows retain their independently supported geometric findings.',
    'notes': [
        {'id': '143_scan017-auditA-N1', 'text': 'The page requests that the relation of (7) and (8) to the given action be made explicit. The audit reads the request as written and does not treat it as a proof supplied here.'},
        {'id': '143_scan017-auditA-N2', 'text': 'The reformulation presents an extension and an action set whose kernel acts freely, then a groupoid with a universal cover and a group action. The first raised nonempty condition is legible; the small second insertion is not completed by analogy with it.'},
        {'id': '143_scan017-auditA-N3', 'text': 'The tuple’s last component is a visibly descending g, while the displayed action label is a low compressed a. The difference is preserved. This explicit action-map a is a useful local graphic specimen for main’s later comparison, but no other page was inspected during this audit.'},
        {'id': '143_scan017-auditA-N4', 'text': 'The source announces quasi-inverse equivalences alpha and beta with opposite arrow directions. Their construction is not given on this page. The audit reproduces two omitted attachment guides and otherwise preserves the accepted wording, mathematical letters, punctuation, deletions and source irregularities.'},
    ],
    'check_events': [
        {'statement_id': '143_scan017-auditA-N1', 'type': 'carried as background without fault found', 'outcome': 'References, action expressions and the author’s request were read visually. No mathematical derivation of (7) or (8) was attempted or used to add a mark.'},
        {'statement_id': '143_scan017-auditA-N2', 'type': 'carried as background without fault found', 'outcome': 'The extension/action-set and groupoid definitions were collated. Their intended correspondence did not determine M0690 or license substitution of a for the distinct tuple g.'},
        {'statement_id': '143_scan017-auditA-N4', 'type': 'carried as background without fault found', 'outcome': 'The stated quasi-inverse equivalence and both functor directions were transcribed. No categorical equivalence, freeness assertion or universal-cover claim was proved or computed.'},
    ],
    'hand_log': [
        {'habit': 'The explicit action-map a is compressed into a low, slightly rising wave, while a tuple g has an independently visible descending return.', 'places': 'Scan017 action map and tuple final component.', 'scope': 'Both loci rechecked once in their existing crops. The distinction is graphically present and retained.', 'misreadings': 'C uses a in both places; H uses g in both. Neither harmonization is adopted.'},
        {'habit': 'A long guide can rise from below a baseline and curl back beside a raised inscription.', 'places': 'Scan017 action-set nonempty insertion and small insertion before connexe.', 'scope': 'Both guides rechecked in existing crops. Their contents differ in legibility; only the first is securely symbolic.', 'misreadings': 'An inserted wrapper alone omits the physical guides. The second guide cannot be mistaken for letters or used to fill M0690.'},
        {'habit': 'Capital Pi is broad and tall here; the group pi may share a flat cap but is smaller in its local uses.', 'places': 'All eight Pi and three pi occurrences, individually listed in physical_marks_checked.', 'scope': 'Every occurrence rechecked, including both covered Pi forms and the sole pi subscript 1.', 'misreadings': 'No capital/lowercase swap is proposed merely from flat caps or straight stems.'},
        {'habit': 'The rounded E/Sigma letter recurs with independent primes only where written.', 'places': 'Five extension/action-group occurrences on scan017.', 'scope': 'All five rechecked; two primed, three unprimed.', 'misreadings': 'The shared E/Sigma alternative remains low-confidence; preferred E is not a conclusive rejection of Sigma.'},
        {'habit': 'Small deposits at a bare shaft’s endpoint do not necessarily form an arrowhead.', 'places': 'All four extension connectors, compared locally with the explicit p and a arrows and the bottom functor arrows.', 'scope': 'All connector endpoints checked in halves and the existing extension/action-map crops.', 'misreadings': 'H’s four supplied extension arrows are not adopted.'},
        {'habit': 'A crossed 7 with a curved crown may look looped beside a close opening parenthesis.', 'places': 'The adjacent references (7) (8).', 'scope': 'Both digits and four parentheses inspected in the existing formula-numbers crop.', 'misreadings': 'Agreement of witnesses was checked rather than assumed; the first crossed stem remains 7.'},
        {'habit': 'Short connected middles can flatten several letters, while genuine dots remain separately visible.', 'places': 'ens, groupes/groupe, quotient and the four continuation points.', 'scope': 'Both ens occurrences and both group words were compared locally; the four final points are dark and similarly weighted.', 'misreadings': 'Do not omit ens, expand ext./rev., supply an ens point, or reduce the four points to three.'},
    ],
    'unresolved_for_main': ['Adjudicate both physical insertion-guide reproductions.', 'Retain or adjudicate the three existing doubts: E/Sigma, M0690, and the cancelled sur/de word.'],
    'summary': 'Complete second reading; two guide/placement additions proposed, no word or mathematical-expression change, three existing doubts retained. No new crops.'
}

assert len(confirmed) == 14
assert len(report['inventory_checked']) == 14
assert len(report['physical_marks_checked']['Pi_occurrences']) == 8
assert len(report['physical_marks_checked']['pi_occurrences']) == 3
assert len(report['physical_marks_checked']['extension_group_occurrences']) == 5
assert accepted.count(r'\widetilde{\mathfrak X}') == 2
assert accepted.count(r'\widetilde\Pi') == 2
mark_ids = {x['id'] for x in packet['marks']}
assert {x['id'] for x in report['marks_rechecked']} == mark_ids
for item in findings:
    assert item['before'] in accepted and item['after'] in candidate
    assert all(x['id'] in mark_ids for x in item['decision_updates'])

tex_path = WORK / 'reviews' / f'{KEY}_auditA.tex'
json_path = WORK / 'reviews' / f'{KEY}_auditA.json'
tex_path.write_text(candidate)
json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'tex': str(tex_path), 'json': str(json_path), 'findings': len(findings), 'remaining_doubts': len(remaining), 'inventory_checked': len(confirmed), 'new_crops': 0}, ensure_ascii=False))
