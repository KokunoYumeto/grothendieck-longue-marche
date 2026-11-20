import json
from pathlib import Path

ROOT = Path('/workspace/scratch/8f839dff4bf0')
WORK = ROOT / 'SP74_C13_143+145_work'
KEY = '143_scan016'
packet = json.loads((ROOT / 'reader_packets' / f'{KEY}.json').read_text())
accepted_report = json.loads((WORK / 'reviews' / f'{KEY}_accepted.json').read_text())
accepted = (WORK / 'pages' / f'{KEY}.tex').read_text()

before_groupoid = r'\inserted{le groupoïde} $\Pi_1$'
after_groupoid = r'''\begin{tikzpicture}[baseline=(object.base)]
\node[inner sep=0pt] (object) at (0,0) {$\Pi_1$};
\node[anchor=south,inner sep=0pt] at (-.25,.32) {\inserted{le groupoïde}};
\draw[line width=.3pt] (-.45,-.10) .. controls (-.46,.10) and (-.33,.26) .. (-.15,.27) .. controls (.45,.30) and (.75,.30) .. (.80,.53);
\end{tikzpicture}'''
before_bitorseur = r'Pour ceci, considérons le \inserted{$\pi_1$-}bitorseur'
after_bitorseur = r'''Pour ceci, considérons le \begin{tikzpicture}[baseline=(word.base)]
\node[anchor=base west,inner sep=0pt] (word) at (0,0) {bitorseur};
\node[anchor=base east,inner sep=0pt] at (.15,.46) {\inserted{$\pi_1$-}};
\draw[line width=.3pt] (-.57,.22) .. controls (-.25,.39) and (-.13,.15) .. (-.19,-.22);
\end{tikzpicture}'''

findings = [
    {
        'place': 'Reconstruction paragraph, interlinear le groupoïde and its attachment to Pi-one (inventory E08)',
        'before': before_groupoid,
        'after': after_groupoid,
        'reason': 'The words stand above the line, extending left over the end of reconstruit. A separate dark curved guide runs beneath the inserted phrase, bends over the cap region of Pi, descends beside its left stem, and has an upward curl at its right end. This is a physical insertion guide, not a cover tilde over Pi. The accepted fragment marks the insertion but gives neither the raised placement nor this curved stroke. The proposed TikZ preserves the relative attachment and curve without changing the words or the groupoid letter. The native half supplies the complete inserted words; the existing tight crop supplies the guide geometry.',
        'confidence': 'high',
        'crop': 'crops/143_scan016_main_reconstructed.png',
        'box': [315, 600, 1635, 900],
        'against_C': True,
        'against_H': True,
        'C': before_groupoid,
        'H': r'\marginal{interligne : « le groupoïde »} $\Pi_1$',
        'kind': 'insertion or placement',
        'consequential': False,
        'marked_in_H': False,
        'decision_updates': [],
        'certainty_only': False,
        'existing_difference_row': None,
        'scope': 'Drawing and relative placement only; no cover accent is added to Pi.'
    },
    {
        'place': 'Pour ceci paragraph, interlinear pi-one hyphen and hook before bitorseur (inventory E14)',
        'before': before_bitorseur,
        'after': after_bitorseur,
        'reason': 'The pi-one and its hyphen are raised over the gap before the initial b and extend above its beginning. Beneath the prefix is a separate hook-shaped dark guide: it begins at the upper left, curves right, and descends nearly vertically immediately before b. It has no arrowhead. Neither the guide nor its physical relation to the word is reproduced by an inline inserted wrapper. The initial b is heavily retraced, but no distinct cancelled predecessor can be separated, so no deletion is invented. Existing action and definition crops stop on opposite sides of the complete insertion locus; one new tight crop was made for this newly unresolved feature.',
        'confidence': 'high',
        'crop': 'crops/143_scan016_auditA_bitorseur_insertion.png',
        'box': [900, 1815, 1325, 1955],
        'against_C': True,
        'against_H': True,
        'C': before_bitorseur,
        'H': r'Pour ceci, considérons le \marginal{interligne : « $\pi_1$- »} bitorseur',
        'kind': 'insertion or placement',
        'consequential': False,
        'marked_in_H': False,
        'decision_updates': [],
        'certainty_only': False,
        'existing_difference_row': None,
        'scope': 'Drawing and relative placement only; the visible pi-one hyphen remains live.'
    }
]

candidate = accepted
for item in findings:
    assert candidate.count(item['before']) == 1, item['place']
    candidate = candidate.replace(item['before'], item['after'], 1)
    assert item['C'] in packet['witness_C'], ('C', item['place'])
    assert item['H'] in packet['witness_H'], ('H', item['place'])
    assert item['after'] in candidate, item['place']

crop_boxes = [
    ('143_scan016_readerB_first_isom_display.png', [375, 138, 1662, 400]),
    ('143_scan016_readerB_action_diagram.png', [420, 1505, 1665, 1862]),
    ('143_scan016_main_reconstructed.png', [315, 600, 1635, 900]),
    ('143_scan016_readerB_hom_tors_prose.png', [840, 515, 1647, 605]),
    ('143_scan016_readerB_cancelled_comme.png', [315, 635, 538, 726]),
    ('143_scan016_readerB_cancelled_les_operations.png', [294, 909, 675, 1018]),
    ('143_scan016_readerB_bitorseur_definition.png', [650, 1935, 1665, 2061]),
    ('143_scan016_readerB_final_isom_pair.png', [545, 2154, 1280, 2357]),
    ('143_scan016_main_On_note.png', [255, 2055, 1620, 2200]),
    ('143_scan016_main_on_aura.png', [330, 80, 1095, 170]),
    ('143_scan016_main_factorisant.png', [290, 1245, 1640, 1515]),
]

checks = [
    ('E01', 'Upper-right pencil pagination', 'The single 8 has upper and lower lobes. Retain 8, with no identification of the pencil hand. Checked in original and native upper half.', 'page'),
    ('E02', 'Opening sentence', 'Read Ceci noté, on aura donc, si in full. The detached short strokes of aura occupy more than a single a; the accent of noté and commas after noté and donc are visible. The variables are j and j-prime, followed by membership in capital J = Ob Pi-one. The high j-prime, low 1 and capital J are separate physical marks.', 'crops/143_scan016_main_on_aura.png'),
    ('E03', 'First displayed Isom equality', 'Checked both operators, all delimiters, indices and arguments. The first Pi has a low 1, comma and additional hooked glyph; retain f/phi doubt at M0688, not H omission. The defining label has d, f and a low n-like exit, supporting dfn at medium confidence. On the right, both cover letters have separate tildes and primes, with square brackets around j and j-prime. No extra bar is added above the serif of either Isom I.', 'crops/143_scan016_readerB_first_isom_display.png'),
    ('E04', 'Second row of opening display', 'The row begins with a wavy sign over a bar. The Isom index reads pi-one-tors à droite. There is a hyphen but no independent stop after tors: the following marks belong to à. Both cover tildes and X-primes, the prime on the second j, round argument parentheses and outer ordered-pair parentheses are visible.', 'crops/143_scan016_readerB_first_isom_display.png'),
    ('E05', 'Composition prose', 'Read la composition des chemins étant la composition des hom de pi-one-tors à droite. The hom ending is a long flat m exit, without a detached point. The word remains tors, not expanded torseurs. A short low horizontal trace after its s remains doubtful as an abbreviation point versus an exit stroke. The accent of à and the final point after droite are distinct.', 'crops/143_scan016_readerB_hom_tors_prose.png'),
    ('E06', 'Cancelled opening before On a donc', 'Cancellation crosses the low middle letters. Capital C and a following closed o-like loop survive; Comme remains the preferred but uncertain reading. The entire word is cancelled; On a donc reconstruit is live.', 'crops/143_scan016_readerB_cancelled_comme.png'),
    ('E07', 'Reconstruction prose and cover arguments', 'Read every word of On a donc reconstruit ... à l’aide de ... et de l’opération libre (à droite) de ... sur .... Both cover objects have tildes, primes and capital J arguments. The acting group is the smaller pi-one form. The groupoid Pi-one has no independent cover tilde; the curve near its cap belongs to the insertion guide. Final punctuation is retained.', 'crops/143_scan016_main_reconstructed.png'),
    ('E08', 'Interlinear le groupoïde', 'Both words are live and raised over the end of reconstruit and Pi-one. Proposed finding 1 reproduces the curved attachment; it is not a deletion stroke or mathematical accent.', 'crops/143_scan016_main_reconstructed.png'),
    ('E09', 'Cancelled restart [les opérations', 'The large initial left bracket is distinct from the following lower-case l. The surviving e/s and the operation word’s tall p, t, dots and final s support the accepted reading. Long oblique/horizontal cancellation strokes cross the block. The far-right curved stroke belongs to the word ending; no separate closing bracket is supplied.', 'crops/143_scan016_readerB_cancelled_les_operations.png'),
    ('E10', 'Question and object-action prose', 'Read Comment reconstituer l’opération de G-prime sur Pi-one ? L’opération sur Ob Pi-one=J n’est autre que l’opération donnée de G-prime sur J. Both groupoid capitals and their low 1 indices, both G primes, apostrophes and question punctuation were checked. No additional operation or omitted clause was inferred.', 'page'),
    ('E11', 'Factorisation parenthesis and introduction', 'The text reads factorisant celle de the primed rounded group, followed by closing parenthesis and point; then Soit g in G-prime, explicitons. The factorisant f has a long descender, and the membership sign and G prime are present. The rounded extension letter remains E/Sigma at low confidence.', 'crops/143_scan016_main_factorisant.png'),
    ('E12', 'Complete action diagram', 'All four objects and four connections were checked independently. The upper-left index is Pi-one; the upper-right Isom has no index. Both lower indices are pi-one. All four cover tildes/primes and j/j-prime or gj/gj-prime arguments are present. Upper arrow: right head, g with a Pi-one subscript above a separate wave, both labels above the shaft. Lower arrow: right head, question mark above a separate wave, both above its shaft. Each vertical connection is a pair of short parallel strokes, without arrowhead. No cap/serif is promoted to a tilde.', 'crops/143_scan016_readerB_action_diagram.png'),
    ('E13', 'Pour ceci sentence', 'Read Pour ceci, considérons le bitorseur, preserving the comma and the word bitorseur. The retraced initial b is live. No separate cancelled old character is secured underneath it.', 'crops/143_scan016_auditA_bitorseur_insertion.png'),
    ('E14', 'Raised pi-one hyphen prefix', 'The prefix is live above the start of bitorseur. Its low 1 and one hyphen are visible. Proposed finding 2 reproduces the hook-shaped insertion guide, distinct from the mathematical letter and from the b.', 'crops/143_scan016_auditA_bitorseur_insertion.png'),
    ('E15', 'Bitorseur definition', 'The B has a low g, followed by two dark, low spots and an open inclusion sign. Both primed rounded group letters remain locally compatible with E/Sigma. The prose reads image inv. de g par; inv. is an abbreviation and its point is visible. The final horizontal connector has a dark tiny endpoint that does not securely decide a bare stroke versus a minute arrowhead. G and its high prime are separate.', 'crops/143_scan016_readerB_bitorseur_definition.png'),
    ('E16', 'Final introductory line', 'The crossed t and following low exit establish note, and the following strokes read que l’on a; no hyp. is present. The enclosure really opens with a round parenthesis and closes with a right square bracket. The text reads grâce à l’op. de the primed rounded group sur the tilde-X-prime object. The argument is a barred capital I, retained literally; it is not regularised to J. Its cover tilde and prime are independent marks.', 'crops/143_scan016_main_On_note.png'),
    ('E17', 'First final isomorphism', 'The two covers are tilde-X-prime(gj) and tilde-X-prime(j). Wave and bar make the isomorphism sign. The wedge is on the formula baseline; pi-one is below and to its right. B has a heavily retraced low g, still compatible with the definition and lower-row g. No distinct deleted character is separable.', 'crops/143_scan016_readerB_final_isom_pair.png'),
    ('E18', 'Second final isomorphism', 'The two covers have high X-primes and j-primes in the arguments gj-prime and j-prime. Both cover tildes are separate from the relation wave. The pi-one is again below/right of its wedge, not superscript. The final B has a clear low g, with its loop and long return.', 'crops/143_scan016_readerB_final_isom_pair.png'),
    ('E19', 'Bottom-left pencil pagination', 'The pencil digits read 15 in the original and native lower half. The hand is unassigned. No author identity or source continuation is inferred from the number.', 'page'),
]

remaining = json.loads(json.dumps(accepted_report['remaining_doubts']))
audit_reasons = [
    ('The reused full first-display crop confirms a comma and an additional low hooked glyph after the 1. Its connected upper hook, upright and middle crossing favour f, with phi still possible; no separate accent supports an accented e. Nothing on this sheet independently names this extra index.', 'crops/143_scan016_readerB_first_isom_display.png', [375, 138, 1662, 400]),
    ('The low trace after the s is short and horizontal rather than a round isolated stop. It can still be an abbreviated ending mark or a detached exit. The candidate retains the existing local doubt, while the hom point and first-display tors point are absent.', 'crops/143_scan016_readerB_hom_tors_prose.png', [840, 515, 1647, 605]),
    ('The reused crop shows the capital C and o-like loop, but the cancellation intersects almost all the remaining low strokes. Comme is plausible, not securely recovered in every letter.', 'crops/143_scan016_readerB_cancelled_comme.png', [315, 635, 538, 726]),
    ('Both spots are dark, small and separate, with a slight diagonal offset. Their low position beside the g and below the inclusion leaves the interpretation as a colon uncertain. They are not introduced from pale show-through; no additional faint specks are transcribed.', 'crops/143_scan016_readerB_bitorseur_definition.png', [650, 1935, 1665, 2061]),
    ('The connector has a long horizontal shaft and a tiny dark downward/thickened termination. The reused crop does not securely separate two arrowhead branches, so the existing bare-stroke/arrow alternative remains local to this connector.', 'crops/143_scan016_readerB_bitorseur_definition.png', [650, 1935, 1665, 2061]),
    ('All four occurrences have rounded open upper and lower lobes with independent high primes. The local strokes remain compatible with the shared E/Sigma alternatives. The preferred E rendering is not a claim that H’s alphabet is certainly wrong.', 'page', None),
]
for item, (reason, crop, box) in zip(remaining, audit_reasons):
    item['audit_reason'] = reason
    item['crop'] = crop
    item['box'] = box
    item['audit_disposition'] = 'retained without narrowing'

cover_places = [
    ('First display, right Isom, first object', r'\widetilde{\mathfrak X}\prime[j]', 'square j brackets; no argument prime'),
    ('First display, right Isom, second object', r'\widetilde{\mathfrak X}\prime[j\prime]', 'square brackets; separate high j prime'),
    ('Opening display, torsor row, first object', r'\widetilde{\mathfrak X}\prime(j)', 'round j parentheses; no argument prime'),
    ('Opening display, torsor row, second object', r'\widetilde{\mathfrak X}\prime(j\prime)', 'round parentheses; separate high j prime'),
    ('Reconstruction, after à l’aide de', r'\widetilde{\mathfrak X}\prime(J)', 'capital J argument'),
    ('Reconstruction, after sur', r'\widetilde{\mathfrak X}\prime(J)', 'capital J argument'),
    ('Action diagram, lower left, first object', r'\widetilde{\mathfrak X}\prime(j)', 'round j parentheses'),
    ('Action diagram, lower left, second object', r'\widetilde{\mathfrak X}\prime(j\prime)', 'separate argument prime'),
    ('Action diagram, lower right, first object', r'\widetilde{\mathfrak X}\prime(gj)', 'g then j'),
    ('Action diagram, lower right, second object', r'\widetilde{\mathfrak X}\prime(gj\prime)', 'g then j with separate argument prime'),
    ('Parenthesis before final pair', r'\widetilde{\mathfrak X}\prime(I)', 'literal barred I, not J'),
    ('Final first row, left', r'\widetilde{\mathfrak X}\prime(gj)', 'g then j'),
    ('Final first row, right', r'\widetilde{\mathfrak X}\prime(j)', 'j with no argument prime'),
    ('Final second row, left', r'\widetilde{\mathfrak X}\prime(gj\prime)', 'separate argument prime'),
    ('Final second row, right', r'\widetilde{\mathfrak X}\prime(j\prime)', 'separate argument prime'),
]
pi_capital_places = [
    'Opening Ob Pi-one', 'First Isom subscript, also comma and extra f/phi glyph',
    'After reconstruit and the raised le groupoïde', 'Question: sur Pi-one',
    'Object-action prose: Ob Pi-one=J', 'Diagram upper-left Isom subscript',
    'Diagram upper arrow: subscript of g',
]
pi_lower_places = [
    'Opening display torsor subscript', 'Composition prose pi-one-tors',
    'Reconstruction prose acting group', 'Diagram lower-left Isom subscript',
    'Diagram lower-right Isom subscript', 'Raised prefix before bitorseur',
    'First final wedge index', 'Second final wedge index',
]

report = {
    'key': KEY,
    'reader': 'A',
    'stage': 'second reading',
    'first_reader': 'B',
    'image_views': ['original', 'half1', 'half2'],
    'workflow': {
        'original': {'path': packet['image'], 'dimensions': [1680, 2360], 'views': 1},
        'halves': [
            {'path': str(ROOT / 'halves/143_scan016_half1.png'), 'box': [0, 0, 1680, 1298], 'views': 1},
            {'path': str(ROOT / 'halves/143_scan016_half2.png'), 'box': [0, 1062, 1680, 2360], 'views': 1},
        ],
        'reused_crops': [{'path': 'crops/' + name, 'box': box, 'visible_inspections': 1} for name, box in crop_boxes],
        'new_crops': [{
            'path': 'crops/143_scan016_auditA_bitorseur_insertion.png',
            'box': [900, 1815, 1325, 1955],
            'reason': 'Complete prefix and guide occupy the gap between the earlier action-diagram and definition crop boxes.',
            'processing': 'Original crop enlarged to width 2800 with LANCZOS, then autocontrast and UnsharpMask radius 1.3, percent 140, threshold 2.',
            'visible_inspections': 1,
        }],
        'scope': 'Only this page, its packet, accepted fragment/report, existing crops, shared notation and reading contracts. No OCR, research, TeX compilation, other-page inspection, new whole-page view or enlarged-half view.',
        'display_note': 'A first hom_tors_prose emission was truncated before an image was visible; the existing file was then emitted successfully once. It was not recropped.'
    },
    'findings': findings,
    'confirmed': [dict(element=e, place=p, evidence=v, crop=c) for e, p, v, c in checks],
    'remaining_doubts': remaining,
    'inventory_checked': [
        dict(element=item['element'], position=item['position'], kind=item['kind'],
             audit_status='checked; guide/placement addition proposed' if item['element'] in ('E08', 'E14') else 'checked; accepted reading retained')
        for item in accepted_report['inventory']
    ],
    'inventory_additions': [
        {'parent_element': 'E08', 'kind': 'drawing', 'position': 'Beneath raised le groupoïde and beside Pi-one', 'first_words_or_objects': 'Curved insertion guide with downturned left attachment and upturned right end', 'transcribed': 'yes, in proposed candidate', 'hand': 'same principal ink hand'},
        {'parent_element': 'E14', 'kind': 'drawing', 'position': 'Beneath raised pi-one hyphen, immediately left of bitorseur', 'first_words_or_objects': 'Hook-shaped insertion guide without arrowhead', 'transcribed': 'yes, in proposed candidate', 'hand': 'same principal ink hand'},
    ],
    'physical_indices_and_marks': {
        'capital_Pi_occurrences': [{'place': p, 'reading': r'\Pi_1', 'index_position': '1 below/right of Pi; additional comma and f/phi retained at first Isom only'} for p in pi_capital_places],
        'lowercase_pi_occurrences': [{'place': p, 'reading': r'\pi_1', 'index_position': '1 below/right of pi; whole pi-one below wedge in each final row'} for p in pi_lower_places],
        'covers': [{'place': p, 'object': obj, 'marks': 'Separate cover tilde and high X prime both present; ' + desc} for p, obj, desc in cover_places],
        'B_subscripts': [
            {'place': 'Definition', 'reading': 'B_g', 'evidence': 'g below/right of B; loop and descender'},
            {'place': 'First final row', 'reading': 'B_g', 'evidence': 'g below/right, heavily retraced with multiple loops; no distinct cancelled predecessor'},
            {'place': 'Second final row', 'reading': 'B_g', 'evidence': 'clear low g with loop and long return'},
        ],
        'extension_group_primes': ['Factorisant parenthesis', 'Definition inclusion target', 'Definition connector source', 'Final operation parenthesis'],
        'G_primes': ['Reconstitution question', 'Given operation on J', 'Soit g in G-prime', 'Definition connector target'],
        'no_extra_accents': 'The reconstruction guide is not a Pi tilde; detached Isom I serifs are not bars; the two diagram waves are labels above their shafts.'
    },
    'marks_rechecked': [
        {'id': 'M0688', 'decision': 'undecided', 'reading': r'\unsure{\mathrm f|\phi}', 'confidence': 'low', 'disposition': 'Accepted decision retained after full-formula crop inspection.'},
        {'id': 'M0689', 'decision': 'first', 'reading': 'note', 'confidence': 'high', 'disposition': 'Accepted decision retained: n/o, crossed tall t and e exit; following words que l’on a.'},
    ],
    'existing_difference_review': 'All 26 accepted change rows and both witnesses were checked against the page. No existing row is proposed for reversal or confidence revision. Pure X alphabet encoding stays medium and non-consequential; pure E/Sigma alphabet rows stay low and non-consequential. The two final-product rows include an independently visible index-position difference from H, with C already placing the index low; their X-font differences are not evidence for a changed mathematical object.',
    'hand_log_metadata_correction': {'accepted_entry': 'The capital I in Isom can have a short top serif detached from the vertical stroke.', 'before_scope': 'All six operators on scan016 inspected.', 'after_scope': 'All seven operators on scan016 inspected: three in the opening display and four in the action diagram.', 'reason': 'The first equality has two Isom operators and the following isomorphism row has a third. This corrects a count in the hand-log scope, not manuscript text.'},
    'notes': [
        {'id': '143_scan016-auditA-N1', 'text': 'The page states Isom identifications for j,j-prime in the object set J and says path composition is composition of right-torsor homomorphisms. The extra index after Pi-one remains unread with confidence; it has not been silently deleted or assigned a mathematical meaning.'},
        {'id': '143_scan016-auditA-N2', 'text': 'The source says the groupoid has been reconstructed and asks how to reconstruct the G-prime action. Both interlinear expressions are live additions with physical attachment guides. The audit proposes reproduction of those guides only.'},
        {'id': '143_scan016-auditA-N3', 'text': 'The B_g definition and both final isomorphism formulas are transcribed as written. The parenthetical argument is I and the enclosure is an opening round parenthesis with a closing square bracket; no correction to J or to matched delimiters is made.'},
        {'id': '143_scan016-auditA-N4', 'text': 'The upper 8 and lower 15 are pencil pagination in an unnamed hand. No watermark, pale background writing or stray faint speck was added as source text.'},
    ],
    'check_events': [
        {'statement_id': '143_scan016-auditA-N1', 'type': 'carried as background without fault found', 'outcome': 'The Isom expressions and composition assertion were collated visually, with every index, delimiter and cover mark inspected. No proof of the identification or composition law was performed.'},
        {'statement_id': '143_scan016-auditA-N2', 'type': 'carried as background without fault found', 'outcome': 'The groupoid reconstruction and action question were read as source claims. Pi versus pi was read using visible forms and the page’s own groupoid/torsor notation; this was not an independent mathematical proof.'},
        {'statement_id': '143_scan016-auditA-N3', 'type': 'carried as background without fault found', 'outcome': 'The visible declaration g in G-prime and the three B_g forms were compared as local notation. No bitorsor law, inverse-image claim or contracted-product identity was independently established.'},
    ],
    'hand_log': [
        {'habit': 'The groupoid capital Pi and the acting-group pi share a flat cap and can both have nearly straight stems in compressed writing.', 'places': 'All seven capital-Pi occurrences and all eight lower-case-pi occurrences on scan016, listed separately in physical_indices_and_marks.', 'scope': 'Every occurrence checked. Tall full-size groupoid forms and smaller torsor forms support the accepted distinction. The lower-right diagram index is retraced; the page’s repeated local notation settles its pi encoding rather than the cap alone.', 'misreadings': 'No new Pi/pi alternative is introduced merely because a pi has a flat cap.'},
        {'habit': 'A curved guide under a raised insertion can pass near the top of a mathematical capital.', 'places': 'Raised le groupoïde at reconstruit Pi-one.', 'scope': 'One occurrence checked in original, native half and existing main crop.', 'misreadings': 'Do not read the guide as a cover tilde. Both witnesses and the accepted fragment omit its drawn shape.'},
        {'habit': 'A raised mathematical prefix may have a separate hook beneath it, attaching to the next word.', 'places': 'pi-one hyphen before bitorseur.', 'scope': 'One occurrence checked in native half and one new tight crop.', 'misreadings': 'The hook is not an opening parenthesis, a cancelled b, or part of pi-one. Neither witness draws it.'},
        {'habit': 'The Isom capital I can have a detached-looking upper serif.', 'places': 'Three Isom operators in the opening display and four in the action diagram.', 'scope': 'All seven operators checked in the display/diagram views; no detached serif was promoted to an overbar.', 'misreadings': 'Keep serifs distinct from the fifteen actual cover tildes and the diagram waves.'},
        {'habit': 'Small abbreviation endings may be long flat exits; a detached low horizontal trace need not be a round stop.', 'places': 'aura, hom, both tors occurrences, inv., note.', 'scope': 'All cited words checked; prose tors retains its point/exit uncertainty.', 'misreadings': 'Retain aura rather than a; retain hom without H’s added point; retain abbreviated tors and inv. rather than H’s expansions.'},
        {'habit': 'A g subscript can be retraced repeatedly without a distinguishable earlier cancelled letter.', 'places': 'First final B_g, compared locally with definition B_g and second final B_g.', 'scope': 'All three inspected.', 'misreadings': 'Do not infer a deletion from the heavy first-final g alone.'},
        {'habit': 'The rounded extension letter has two open lobes and remains alphabetically ambiguous.', 'places': 'All four primed occurrences on scan016.', 'scope': 'Every occurrence checked; E/Sigma alternatives retained consistently at low confidence.', 'misreadings': 'The preferred E rendering records a provisional reading, not a conclusive rejection of H’s Sigma.'},
    ],
    'unresolved_for_main': ['Adjudicate both physical insertion-guide findings.', 'Retain or adjudicate the six local doubts listed with their unchanged preferred readings.'],
    'summary': 'Complete second reading; two proposed insertion/guide reproductions, no word or mathematical-expression change, six existing doubts retained.'
}

assert accepted.count(r'\widetilde{\mathfrak X}') == 15
assert len(report['confirmed']) == 19
assert len(report['inventory_checked']) == 19
assert len(report['physical_indices_and_marks']['covers']) == 15
assert len(report['physical_indices_and_marks']['capital_Pi_occurrences']) == 7
assert len(report['physical_indices_and_marks']['lowercase_pi_occurrences']) == 8
mark_ids = {m['id'] for m in packet['marks']}
assert {m['id'] for m in report['marks_rechecked']} == mark_ids
for finding in findings:
    assert all(update['id'] in mark_ids for update in finding['decision_updates'])
    assert (WORK / finding['crop']).exists()

tex_path = WORK / 'reviews' / f'{KEY}_auditA.tex'
json_path = WORK / 'reviews' / f'{KEY}_auditA.json'
tex_path.write_text(candidate)
json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'tex': str(tex_path), 'json': str(json_path), 'findings': len(findings), 'remaining_doubts': len(remaining), 'inventory_checked': len(checks)}, ensure_ascii=False))
