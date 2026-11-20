from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone

BASE = Path('/workspace/scratch/8f839dff4bf0')
WORK = BASE / 'SP74_C13_143+145_work'
KEY = '143_scan014'
packet = json.loads((BASE / 'reader_packets' / f'{KEY}.json').read_text())
accepted = json.loads((WORK / 'reviews' / f'{KEY}_accepted.json').read_text())
source_path = WORK / 'pages' / f'{KEY}.tex'
source_bytes = source_path.read_bytes()
tex = source_bytes.decode()

# These are records of the images actually displayed during Reader C's audit.
# No image operations, OCR, compilation, or accepted-file mutations occur here.
crop_boxes = {
    'main_first_display': [420, 150, 1100, 390],
    'main_quon_decrire': [365, 850, 1590, 1075],
    'main_compatibility': [360, 1570, 1670, 1650],
    'readerB_les_appl': [470, 413, 672, 522],
    'readerB_first_aut_map': [600, 1390, 1645, 1537],
    'readerB_cancelled_peut_se': [900, 1753, 1215, 1861],
    'readerB_lower_group_maps': [640, 1950, 1645, 2165],
    'readerB_final_clause': [375, 2160, 1565, 2250],
    'readerB_final_deduite': [370, 2242, 1050, 2310],
    'readerB_final_envisagees': [1050, 2235, 1662, 2314],
}

reasons = {
    1: 'The pi-one lies wholly below the small wedge. The tilde, prime, I and final E are separately visible; the right leg of pi curves inward.',
    2: 'The J row has the same low wedge label, with a curved right leg. The hooked J is not an I or a Y; the prime and tilde are present.',
    3: 'The l-e-s strokes are live and to the left of the thick strike through the following word. The cancelled word retains a visible initial bowl and a p-descender, but its obscured ending remains tentative.',
    4: 'The short continuation at the left reads i-s-o followed by a point. No final m is visible after o.',
    5: 'Each of this row\'s three pi-one labels is below its wedge; the parenthesized right factor closes after B-gamma. Both X primes and tildes are visible.',
    6: 'All three labels in the J row are below their wedges. The extra pair of parentheses around B-gamma is visible and retained; it is not supplied by analogy with the I row.',
    7: 'The prose begins with the descending q of qu\'on, then peut and décrire; the following tall l and low aide strokes support à l\'aide. They do not form H\'s qui proviennent à droite.',
    8: 'The right-set abbreviation ends with the low ens exit and no following point. The larger pi has a straight left leg and an inward-curving right leg like the first display, so its flat cap alone is not read as a capital Pi.',
    9: 'The right-hand wedge in the I row has its pi-one visibly below it. I, prime, tilde and B-gamma were checked on both sides of the displayed equivalence.',
    10: 'The corresponding J row likewise has a low pi-one. Both J occurrences have the hooked lower return; the final B has a gamma below it.',
    11: 'The terminal hom is followed by blank paper: neither a final s nor a separate full stop is visible. The preceding words are lesquels reviennent à la donnée.',
    12: 'The first connector has a long shaft ending in a short raised blunt stub. This is less decisively pointed than the two lower connectors; the accepted uncertain bare-shaft representation is retained.',
    13: 'A short dark stroke is detached above the initial A. Whether it is a mathematical bar or part of the capital\'s formation remains unresolved; the explicit alternative is retained.',
    14: 'There is genuine crossed ink below Aut, beginning with a readable e-loop. The remaining letters are entangled with hatching, so ens remains tentative and deleted.',
    15: 'After et itou pour, the source gives X-prime(J) with one closing parenthesis. H\'s second closing parenthesis is not visible.',
    16: 'The op strokes have no terminal point. The two following abbreviated locutions do retain their visible points: à g. et à dr.',
    17: 'The paragraph begins with Or, followed by la donnée de ces applications. The large initial O, low r, and the separate donnée strokes are present; H\'s substituted wording is not supported.',
    18: 'After variable and its comma, the short word ends with the raised t-hook of équivaut; there is no separate alant ending.',
    19: 'The cancellation retains a long p-like descender, a t-upright and a terminal e-like loop; the low intervening strokes coincide with the strike. The tentative peut se is retained without upgrading confidence.',
    20: 'The lower source has the repeated two-lobed extension glyph, a prime, a lower Gamma-prime, and a union with gamma-in-Gamma-prime underneath. The E/Sigma alphabet alternative stays explicit; no physical index is altered.',
    21: 'The first lower target has the outer closing parenthesis and then blank paper, with no comma. Both lower map shafts have visible right-pointing tips; the second tip is mostly above its shaft.',
    22: 'The first celle ends in a flat e exit, unlike the later hooked plural celles. The compact following verb ends in a t-hook and is retained as est, not sont.',
    23: 'The same rounded extension glyph and prime recur on the final line. This repetition supports consistency of encoding but does not settle its alphabet.',
    24: 'Four separate terminal points follow the last J expression. The extra final point beyond an ellipsis is retained.',
    25: 'The lower-left graphite numeral has a 1 followed by two rightward bowls of 3. It is transcribed as 13, with no attribution of the pencil hand.',
    26: 'All three X graphs in the Aut/Bij row carry their tildes and primes. The shared mathfrak encoding is retained; this is a font/encoding confirmation, not a new symbol correction.',
    27: 'The lower second target has a tilde, a prime and the hooked J in parentheses. The shared X encoding is retained without a new material row.',
    28: 'The first final-line X has its tilde and prime and argument I. Its encoding remains the shared convention; the following comma is present.',
}

# Evidence is the view actually used in this audit, not automatically the crop
# cited by the first reader. A crop is named only if C displayed it this pass.
evidence = {
    1: 'main_first_display', 2: 'main_first_display',
    3: 'readerB_les_appl', 4: 'half1', 5: 'half1', 6: 'half1',
    7: 'main_quon_decrire', 8: 'main_quon_decrire',
    9: 'half1 and half2 overlap', 10: 'half1 and half2 overlap',
    11: 'half2', 12: 'readerB_first_aut_map', 13: 'readerB_first_aut_map',
    14: 'readerB_first_aut_map', 15: 'half2', 16: 'main_compatibility',
    17: 'half2', 18: 'half2', 19: 'readerB_cancelled_peut_se',
    20: 'readerB_lower_group_maps', 21: 'readerB_lower_group_maps',
    22: 'readerB_final_clause', 23: 'half2', 24: 'half2', 25: 'half2',
    26: 'readerB_first_aut_map', 27: 'readerB_lower_group_maps', 28: 'half2',
}

confirmed = []
for i, old in enumerate(accepted['changes'], 1):
    literal = old['final']
    if i in (1, 2, 5, 6, 9, 10):
        literal = literal.replace(r'\simeq', r'&\simeq', 1)
    if i == 15:
        literal = r"\text{et itou pour }\widetilde{\mathfrak X}'(J)"
    assert literal in tex, (i, literal)
    for witness in ('C', 'H'):
        quote = old[witness]
        assert quote == '[no witness]' or quote in packet['witness_' + witness], (i, witness, quote)
    view = evidence[i]
    item = {
        'accepted_change_row': i,
        'place': old['place'],
        'C': old['C'],
        'H': old['H'],
        'accepted': literal,
        'audit_result': 'confirmed without candidate change',
        'reason': reasons[i],
        'confidence': old['confidence'],
        'evidence': view,
        'material_scope': 'notation encoding only' if i in (26, 27, 28) else 'existing decision; no new change',
    }
    if view in crop_boxes:
        item['crop'] = f'crops/{KEY}_{view}.png'
        item['box'] = crop_boxes[view]
    else:
        item['crop'] = 'page'
        item['box'] = None
    confirmed.append(item)

confirmed.extend([
    {
        'place': 'Opening, punctuation, and upper-right pagination',
        'accepted': r"\mspage{7}" + '\n' + r"En fait, si $Y'\longleftrightarrow E$, on a",
        'audit_result': 'confirmed',
        'reason': 'The upper-right graphite 7 and the complete opening were checked. Both heads of the horizontal Y-prime/E arrow are present. No source claim identifying the pencil writer is visible.',
        'evidence': 'original and half1',
    },
    {
        'place': 'Pi/pi case comparison across all twelve pi-one occurrences',
        'audit_result': 'retained lowercase pi; no new case alternative',
        'reason': 'All ten wedge labels and the two full-size prose graphs were inspected. The large prose graphs have an inward-curved right leg, matching the first two wedge labels; their flat caps alone do not establish a capital/lowercase contrast. Case is retained at medium confidence; the subscript placement is separately secure.',
        'confidence': 'medium',
        'evidence': 'both halves; main_first_display, main_quon_decrire and main_compatibility existing crops',
    },
    {
        'place': 'Primes, tildes, I/J arguments, gamma and Gamma-prime',
        'audit_result': 'confirmed occurrence by occurrence',
        'reason': 'All 18 covered X graphs were checked for tilde and prime. Every I/J argument, the six B-gamma occurrences, the variable gamma-in-Gamma-prime clause, the lower union index and the lower source subscript were inspected. No index was completed from the mathematical pattern.',
        'evidence': 'original and both halves, with the first display and both map crops for their unresolved neighboring forms',
    },
    {
        'place': "Cancellation within d'une applications",
        'accepted': r"d'\deleted{une}applications",
        'audit_result': 'confirmed',
        'reason': 'The short une is crossed out between the apostrophe and live applications. The apostrophe and the plural application word remain live; the wording is not grammatically repaired.',
        'evidence': 'half2',
    },
])

mark_reasons = {
    'M0670': 'Live l-e-s stands wholly before the strike on the next word; no cancellation crosses les.',
    'M0671': 'Flat-ended singular celle contrasts with later hooked plural celles, and compact est has its terminal t-hook.',
    'M0672': 'The first d is approached by the descender from the line above; the subsequent é-d-u-i-t-e sequence supports déduite. The wave below belongs to the following line\'s X tilde and is not an underline.',
    'M0673': 'The low env trace, dotted i, s-a, descending g, accent and terminal ées support envisagées. The source spelling is retained.',
}
mark_confirmations = []
original_ids = {x['id'] for x in packet['marks']}
for old in accepted['decisions']:
    assert old['id'] in original_ids
    item = {k: old[k] for k in ('id', 'decision', 'reading', 'confidence', 'crop', 'box')}
    item['audit_result'] = 'confirmed; no decision update'
    item['ink'] = mark_reasons[old['id']]
    mark_confirmations.append(item)
assert {x['id'] for x in mark_confirmations} == original_ids

doubt_reasons = [
    'Reader C sees the live les distinctly; the following cancelled word has an initial bowl and a p-descender, while the internal ending remains under thick ink. The same tentative appl. is retained.',
    'Reader C sees a blunt raised terminal stub on the first connector. The two lower tips are more pointed. The accepted preferred bare shaft remains uncertain; no expected map direction supplies a head.',
    'The short curved stroke over A is visibly detached, but its status as an accent rather than capital formation remains open.',
    'The initial e-loop is readable, but the crossed n/s-like strokes cannot be independently separated from the hatching.',
    'A p-like descender, t-upright and terminal e-loop survive; the intervening low letters coincide with the strike. The preferred peut se remains tentative.',
    'The lower source and final prose repeat the rounded two-lobed graph with a prime. Neither occurrence independently identifies the alphabet, so the shared E/Sigma alternative remains.',
]
remaining_doubts = []
for old, reason in zip(accepted['remaining_doubts'], doubt_reasons):
    item = dict(old)
    item['reason'] = reason
    item['audit_status'] = 'retained without removal or narrowing'
    remaining_doubts.append(item)

inventory_confirmation = []
for old in accepted['inventory']:
    item = dict(old)
    item['audit_status'] = 'checked and represented in unchanged candidate'
    inventory_confirmation.append(item)

# Raw packet indices cover textual differences plus mechanical wrapper/font
# differences. The latter are documented without creating material findings.
raw_row_map = {
    6: [1], 9: [2], 11: [4], 13: [5], 15: [5], 16: [5],
    18: [6], 20: [6], 21: [6], 23: [7], 24: [7], 25: [8],
    28: [9], 31: [10], 33: [11], 35: [12], 36: [14],
    42: [15], 43: [16], 44: [17], 45: [18, 19],
    47: [20], 50: [21], 53: [22], 54: [22], 55: [23], 58: [24, 25],
}
font_only = {3, 5, 7, 8, 14, 17, 19, 27, 29, 30, 37, 38, 39, 41, 49, 51, 56, 57}
raw_checks = []
for i, difference in enumerate(packet['differences'], 1):
    if i in raw_row_map:
        disposition = 'physical reading confirmed in the cited literal collation rows'
        if i == 58:
            disposition += '; H editorial commentary is not manuscript text'
    elif i in font_only:
        disposition = 'font/encoding or token spacing only; physical prime, tilde and argument checked; no material finding'
    elif i in (1, 2):
        disposition = 'editorial scan/page wrapper or unsupported authorship gloss; source pagination checked, no author attribution added'
    elif i == 48:
        disposition = 'equivalent arrow encoding; lower first arrow visibly has a right-pointing head'
    else:
        disposition = 'array/aligned/diagram wrapper or layout syntax only; corresponding physical arrangement checked'
    raw_checks.append({'packet_difference': i, 'accepted_change_rows': raw_row_map.get(i, []), 'disposition': disposition})

report = {
    'key': KEY,
    'reader': 'C',
    'stage': 'second reading',
    'first_reader': 'B',
    'image_views': ['original', 'half1', 'half2'],
    'image_view_note': 'The original was successfully displayed once. An initial half1 tool result was truncated before an image was visible; half1 was then successfully displayed once. Half2 was successfully displayed once. No extra full-page or enlarged-half view was used.',
    'existing_crop_views': [{'crop': f'crops/{KEY}_{name}.png', 'box': box, 'views': 1} for name, box in crop_boxes.items()],
    'new_crops': [],
    'findings': [],
    'confirmed': confirmed,
    'mark_confirmations': mark_confirmations,
    'remaining_doubts': remaining_doubts,
    'inventory_confirmation': inventory_confirmation,
    'inventory_additions': [],
    'raw_difference_checks': raw_checks,
    'notes': [
        {'id': f'{KEY}-auditC-N1', 'text': 'Complete second reading finished. No candidate change, material finding, certainty-only alteration, MARKS decision update, inventory addition, or removed/narrowed doubt is proposed.'},
        {'id': f'{KEY}-auditC-N2', 'text': 'All six equation rows, ten low wedge indices, twelve pi-one graphs, eighteen covered X graphs, the brace structures, three B-gamma map connectors, cancellation states, prose, four original MARKS, and both pencil numerals were checked. Glyph/encoding confirmations are not new material rows.'},
        {'id': f'{KEY}-auditC-N3', 'text': 'The accepted singular celle qu\'on cherche est, later plural celles, short iso. and hom, point-free ens and op, extra parentheses in the second J equation, and four final points are retained as written. The manuscript wording is not normalized.'},
        {'id': f'{KEY}-auditC-N4', 'text': 'The minute isolated point at approximately native (1072,248), lower-right of the first displayed E, was visible in the existing first-display crop. Its size is markedly smaller than ordinary prose punctuation; it was not promoted to a new stop. No crop was reopened or made for it.'},
        {'id': f'{KEY}-auditC-N5', 'text': 'The two pencil numerals remain attributed to an unassigned pencil hand. No date is present. H\'s editorial page and operator commentary is not inserted as source text.'},
        {'id': f'{KEY}-auditC-N6', 'text': 'Only this page\'s original, native halves, packet, accepted fragment/report and the ten listed existing crops were used, together with the authorized audit contract, reading guidelines and current notation table. No other page image, OCR, research or TeX compilation was used.'},
        {'id': f'{KEY}-auditC-N7', 'text': 'Insertion-guide check: no live interlinear insertion accompanied by a separate guide or caret was identified in the completed original/half views. The detached stroke above the first Aut is already represented by its accent/capital-formation alternative, and the strokes below it belong to the cancelled index. No guide was omitted by an inserted wrapper on this page.'},
    ],
    'check_events': [
        {'statement_id': f'{KEY}-N1', 'reader': 'C', 'stage': 'second reading', 'type': 'carried as background without fault found', 'outcome': 'Reader C visually collated the six displayed equation rows, their low wedge indices and the prose assertion relating the data. No contracted-product identity or equivalence was proved or computed.'},
        {'statement_id': f'{KEY}-N2', 'reader': 'C', 'stage': 'second reading', 'type': 'carried as background without fault found', 'outcome': 'Reader C checked the B-gamma map, Aut/Bij expressions, cancelled index, detached stroke and compatibility wording against the ink. No equivariance statement or homomorphism correspondence was independently verified.'},
        {'statement_id': f'{KEY}-N3', 'reader': 'C', 'stage': 'second reading', 'type': 'carried as background without fault found', 'outcome': 'Reader C read the lower union source and both underlying-set automorphism targets, confirming physical arrowheads and indices. No action law or compatibility theorem was checked.'},
        {'statement_id': f'{KEY}-N4', 'reader': 'C', 'stage': 'second reading', 'type': 'carried as background without fault found', 'outcome': 'Reader C checked the final operation sentence, its singular/plural forms, marks and punctuation. Its asserted identification is transcribed as the source statement, not certified mathematically.'},
    ],
    'hand_log': [
        {'habit': 'A flat-capped pi can have an upright left leg and an inward-curving right leg, including at prose size.', 'places': '143_scan014: first two wedge labels, de pi-one-ens, and compatibility sentence; all other wedge labels compared on the halves.', 'scope': 'All twelve pi-one occurrences on this page inspected; no claim about unviewed pages.', 'misreadings': 'No new C/H case swap found. Both witnesses retain pi. A flat cap alone does not justify changing it to Pi.'},
        {'habit': 'The contracted-product label is written well below and slightly right of the small wedge.', 'places': '143_scan014: all six equation rows, ten occurrences.', 'scope': 'H\'s superscript placement was checked against every occurrence.', 'misreadings': 'All ten are lower labels, as in C; H gives superscripts.'},
        {'habit': 'I has a capped stem, while J has a lower hooked return that can share the preceding parenthesis.', 'places': '143_scan014: all equation, map and final-line I/J arguments.', 'scope': 'All 18 X arguments and the two Y arguments checked; no I/J replacement found.', 'misreadings': 'No new I/J/Y confusion found on this page.'},
        {'habit': 'A short map-tip projection may sit mostly above the shaft; a raised blunt stub is less decisive.', 'places': '143_scan014: first B-gamma map and both lower maps.', 'scope': 'All three shafts and their endpoints inspected; first remains uncertain.', 'misreadings': 'C/H differ on the first connector. No head is supplied there from the expected mathematics.'},
        {'habit': 'A singular e can end with a flat exit, while plural s is a small downturned terminal hook.', 'places': '143_scan014: celle and later celles in final sentence.', 'scope': 'Both forms directly compared.', 'misreadings': 'H pluralizes the first form and changes compact est to sont.'},
        {'habit': 'Heavy cancellation can leave a clear initial or tall stroke while obliterating internal low letters.', 'places': '143_scan014: appl.-like word, first Aut index, and peut se-like phrase.', 'scope': 'Each unresolved locus was inspected using its one existing crop; uncertainty retained.', 'misreadings': 'No obscured word was made certain from witness agreement or expected terminology.'},
    ],
    'accepted_fragment_sha256': hashlib.sha256(source_bytes).hexdigest(),
    'candidate_unchanged': True,
    'completed_at': datetime.now(timezone.utc).isoformat(),
}

for item in report['existing_crop_views']:
    assert (WORK / item['crop']).is_file(), item['crop']
for item in confirmed:
    if 'accepted' in item:
        assert item['accepted'] in tex, item['place']
assert len(accepted['changes']) == 28
assert len(raw_checks) == len(packet['differences']) == 58
assert len(mark_confirmations) == 4
assert len(inventory_confirmation) == 23
assert tex.count(r'\mathbin{\wedge}_{\pi_1}') == 10
assert tex.count(r'\widetilde{\mathfrak X}') == 18
assert len(remaining_doubts) == 6

# Strictly static delimiter checks; no TeX process is launched.
tokens = re.findall(r'\\[A-Za-z]+|\\[^\n]|[{}]', tex)
depth = 0
for token in tokens:
    if token == '{':
        depth += 1
    elif token == '}':
        depth -= 1
        assert depth >= 0
assert depth == 0
env_stack = []
for match in re.finditer(r'\\(begin|end)\{([^{}]+)\}', tex):
    if match[1] == 'begin':
        env_stack.append(match[2])
    else:
        assert env_stack.pop() == match[2]
assert not env_stack

(WORK / 'reviews' / f'{KEY}_auditC.tex').write_bytes(source_bytes)
(WORK / 'reviews' / f'{KEY}_auditC.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
assert source_path.read_bytes() == source_bytes
print(json.dumps({'key': KEY, 'candidate_unchanged': True, 'findings': 0, 'confirmed_prior_rows': 28, 'original_marks': 4, 'existing_crops_reused': 10, 'new_crops': 0, 'remaining_doubts': 6, 'raw_differences_checked': 58, 'inventory_checked': 23, 'static_validation': 'passed'}))
