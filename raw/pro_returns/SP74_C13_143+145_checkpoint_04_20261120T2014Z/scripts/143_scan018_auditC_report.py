from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

BASE = Path('/workspace/scratch/8f839dff4bf0')
WORK = BASE / 'SP74_C13_143+145_work'
KEY = '143_scan018'
packet = json.loads((BASE / 'reader_packets' / f'{KEY}.json').read_text())
accepted_report = json.loads((WORK / 'reviews' / f'{KEY}_accepted.json').read_text())
accepted_path = WORK / 'pages' / f'{KEY}.tex'
accepted_bytes = accepted_path.read_bytes()
before_tex = accepted_bytes.decode()

# Static report writer only. All source inspections preceded this script.
dot_bar = r'''\mathord{\begin{tikzpicture}[x=1ex,y=1ex,baseline=0pt]
\fill (0.10,0.23) circle (0.08);
\draw[line width=0.45pt,line cap=round] (0.39,0.18)--(0.71,0.18);
\end{tikzpicture}}'''
prefix_guide = r'''\begin{tikzpicture}[baseline=(iso.base),x=1cm,y=1cm]
\node[anchor=base west,inner sep=0pt] (iso) at (0,0) {isom};
\node[anchor=base west,inner sep=0pt] at (-0.18,0.42) {\inserted{$\pi$-}};
\draw[thin,line cap=round] (-0.20,-0.18) .. controls (-0.17,0.16) and (0.00,0.24) .. (0.35,0.31);
\end{tikzpicture}'''

crop_boxes = {
    'A_unique-iso': [655, 1310, 1235, 1450],
    'A_tuple': [495, 165, 1475, 275],
    'A_body-point': [900, 1210, 1205, 1335],
    'main_objects_pi': [250, 325, 1030, 425],
    'A_replacement': [290, 1145, 735, 1265],
    'A_margin': [1000, 685, 1650, 1190],
    'A_first-isom': [260, 440, 1125, 572],
    'A_isom-diagram': [265, 835, 1040, 1155],
    'A_prose-isom': [1180, 1235, 1535, 1333],
    'A_lower-cancellations': [320, 2030, 1645, 2275],
    'A_final-pi': [1000, 2225, 1350, 2337],
    'A_body-ending': [235, 1410, 1540, 1585],
}

findings = []
def add_finding(fid, place, before, after, reason, confidence, crop, C, H,
                kind, against_C=True, against_H=True, certainty_only=False,
                revised_rows=None, extra=None):
    assert before in before_tex, (fid, 'before', before)
    for witness, quote in [('C', C), ('H', H)]:
        assert quote == '[no witness]' or quote in packet['witness_' + witness], (fid, witness, quote)
    item = {
        'id': fid, 'place': place, 'before': before, 'after': after,
        'reason': reason, 'confidence': confidence,
        'crop': f'crops/{KEY}_{crop}.png', 'box': crop_boxes[crop],
        'against_C': against_C, 'against_H': against_H, 'C': C, 'H': H,
        'kind': kind, 'consequential': False, 'marked_in_H': False,
        'decision_updates': [], 'certainty_only': certainty_only,
        'revises_accepted_change_rows': revised_rows or [],
    }
    if extra:
        item.update(extra)
    findings.append(item)

add_finding(
    '143_scan018-auditC-F1',
    'Defining tuple: continuation marks immediately after the set input',
    r'\mathfrak Z\ldots', r'\mathfrak Z' + dot_bar,
    'The existing tuple crop shows exactly two compact continuation marks after Z: one slanted point followed by one short horizontal stroke, around native x834–854, y228–231. No distinct third point is visible. The absence of a comma remains confirmed; the conventional three-point ellipsis is replaced by a literal drawing of the two marks. The stroke is not interpreted as a mathematical minus.',
    'high', 'A_tuple', r'Z,\ldots', r'\mathfrak{Z}\ldots',
    'other', revised_rows=[4])

add_finding(
    '143_scan018-auditC-F2',
    'Defining tuple: final action datum',
    r'\mathcal G,\unsure{a|\sim}', r'\mathcal G,a',
    'The local graph has a small rising left shoulder, a compressed middle and a descending right exit. It has no secure closed a-loop, but no stroke establishes a distinct relation sign. The main reader supplied the independently inspected comparison with the explicitly named action map a on scan017, whose a has this same compressed shoulder-and-wave form. This identifies the same handwritten a contextually at medium confidence. It is not a repair of a clear relation sign, and Reader C did not open scan017 during this audit.',
    'medium', 'A_tuple', r'\mathcal G,a', r'G, \sim',
    'misread symbol or index', against_C=False, against_H=True,
    certainty_only=True, revised_rows=[5],
    extra={
        'removes_remaining_doubt': 'defining tuple final output',
        'context_provenance': 'Main reader supplied the scan017 action-map comparison in the audit018 task messages; only scan018 ink was directly inspected by Reader C.',
        'preferred_character_unchanged': True,
    })

add_finding(
    '143_scan018-auditC-F3',
    'Projection diagram: continuation after cat. discrète',
    r'(\widetilde\Pi\text{ cat. discrète}\ldots)',
    r'(\widetilde\Pi\text{ cat. discrète}' + dot_bar + ')',
    'The existing central-diagram crop shows one compact point and one short low horizontal stroke after discrète and before the closing parenthesis. There is no separate third point. The words and closing parenthesis are unchanged; the two visible continuation marks are drawn without normalizing them to a three-point ellipsis.',
    'high', 'A_isom-diagram', r'(\widetilde\Pi\text{ cat. discrète})',
    r'(\widetilde{\Pi} \text{ cat.\ discrète\ldots})',
    'other', revised_rows=[12])

add_finding(
    '143_scan018-auditC-F4',
    'Right marginal note: lower extent of the vertical separator',
    r'\draw (0,0.20)--(0,-2.95);',
    r'\draw (0,0.20)--(0,-2.40);',
    'The physical separator ends after the F(j) line and just above the tilde of the final equivalence. The accepted drawing extends its rule below that final equivalence. Shortening only the endpoint preserves the visible relation between the rule and the lower formula; the rule itself, pointer and marginal words are unchanged.',
    'high', 'A_margin', '[no witness]', 'à droite, séparé par un trait vertical',
    'drawing or diagram', against_C=True, against_H=False, revised_rows=[16],
    extra={'comparison_note': 'H describes a vertical separator but specifies no lower endpoint. This fixes the accepted drawing rather than asserting that H describes the wrong extent.'})

add_finding(
    '143_scan018-auditC-F5',
    'Projection explanation: curved attachment guide beneath the inserted pi-prefix',
    r'\inserted{$\pi$-}isom', prefix_guide,
    'The existing unique-isomorphism crop shows a thin unheaded curve rising from below and left of isom to just beneath the elevated pi-prefix and its dash. The accepted insertion wrapper records the prefix but omits this physical curve. The proposed inline TikZ places the prefix above the word and draws the guide; it retains isom without a stop and leaves the bare fibre-to-fibre shaft unchanged.',
    'high', 'A_unique-iso', r'\inserted{$\pi$-}',
    r'\marginal{interligne : « $\pi$- »}',
    'drawing or diagram', revised_rows=[25],
    extra={'inventory_element': 'E20', 'comparison_note': 'Both witnesses record the inserted pi-prefix; neither quoted encoding draws its curved guide. The word isom was already accepted and is not counted as a new lexical correction.'})

candidate = before_tex
for finding in findings:
    assert candidate.count(finding['before']) == 1, (finding['id'], candidate.count(finding['before']))
    candidate = candidate.replace(finding['before'], finding['after'], 1)
for finding in findings:
    assert finding['after'] in candidate

row_reasons = {
    1: 'The heading is underlined and has no separate full stop after alpha. On va définir follows to its right.',
    2: 'The first input is the rounded two-lobed extension glyph. Shared E/Sigma uncertainty remains; it is not resolved by the action datum a.',
    3: 'The set graph has the angular upper turn, three-like lower curve and return seen throughout this sheet; the existing mathfrak Z encoding is retained without a new font-only finding.',
    4: 'No comma lies between the set graph and the suspension. The suspension itself has two marks, so F1 revises this row\'s accepted three-point encoding.',
    5: 'The low shoulder-and-wave admits compressed a. F2 identifies it contextually as the named action datum, retaining the already-preferred a and removing its alternative.',
    6: 'The orbit-set expression retains the same set graph, slash and compact lowercase pi, followed by its separate uncertain point.',
    7: 'Both fibre subscripts are j; only the second carries a prime. The existing set-letter encoding is retained.',
    8: 'A real vertical separator stands between the three-line definition and d\'où groupoïde Pi. It is not an arrow or part of a letter.',
    9: 'The preliminary covered-Pi formula is crossed out; the tilde, j subscript, equality and set-j are retained inside the cancellation.',
    10: 'To its right the live declaration is Ob tilde-Pi equals the set letter. No j is supplied to this replacement declaration.',
    11: 'The diagram quantifier is forall z,z-prime in the set, with the prime on the second z and no added condition.',
    12: 'There are two continuation marks after discrète, not the three supplied by ldots; F3 revises only their encoding.',
    13: 'The lower diagram RHS has the two fibre arguments with j and j-prime. No pi subscript is added to this Isom from the upper definition.',
    14: 'The older parenthesis is crossed by the long rising strike. Where the low lettering is buried, où, les, images and the final close remain explicitly tentative.',
    15: 'The replacement has a separate point above each z, not a bar. The live si has its i-dot; both j equalities and the second prime are present.',
    16: 'The rule is present, but its lower endpoint is above the final equivalence. F4 corrects the accepted drawing\'s excessive lower extent.',
    17: 'The leftward pointer has two parallel shafts and a left head, crossing the marginal separator near the functor line.',
    18: 'Between par and foncteur, the space and attachment curve do not supply a separate un. No word is added from H\'s tentative gloss.',
    19: 'The small contr.-like word sits above foncteur and is live. Its minute middle strokes remain uncertain, as M0694 records.',
    20: 'The thin curved guide beneath contr. is already drawn and correctly attaches the interlinear qualification to foncteur. It is not a cancellation through the inserted word.',
    21: 'The functor target is Ens with no following comma on this line. The source has a raised small circle and the arrow has a right head.',
    22: 'F(j) equals the ornate set with lower j; the j has a long return. The shared alphabet encoding is retained.',
    23: 'A comma precedes three suspension marks, the third somewhat elongated. No extra comma follows them. The three-mark count is retained.',
    24: 'The /F starts below the base Pi; the accepted subscript placement is supported independently of any categorical interpretation.',
    25: 'The word has an additional low terminal m stroke beyond iso and no detached stop. Its accepted isom remains; F5 adds the omitted physical insertion guide.',
    26: 'The source fibre retains its set graph and j subscript. No change of alphabet is newly counted.',
    27: 'The target fibre has j-prime, not an unprimed j. The prime and set outline are individually visible.',
    28: 'The link between the fibres is a bare horizontal shaft, with no point at either end. H\'s arrowhead is not supplied.',
    29: 'Four distinct terminal marks follow the final z-prime, with the last horizontally elongated. The accepted four-mark count remains.',
    30: 'There is no comma between l\'instant and on. The following n\'a pas utilisé remains as written.',
    31: 'The glyph after utilisé is the same rounded extension letter, without a prime. Shared alphabet uncertainty remains.',
    32: 'The occurrence after l\'op. de is individually checked and retains the same E/Sigma alternative.',
    33: 'The operated-on set has the ornate outline used above and is followed by a visible full stop. The existing encoding remains.',
    34: 'The quotient expression is the G graph equals the extension glyph divided by lowercase pi. Both sides and the slash were inspected; the numerator alphabet stays uncertain.',
    35: 'The extension letter operates on the covered Pi here. The tilde belongs to Pi and is not added to the acting letter.',
    36: 'The extension letter after Comme is the same local graph; this occurrence too remains provisional E/Sigma.',
    37: 'The left side of the lower equality is the ornate set graph. No different variable is introduced by its wider lower curve.',
    38: 'The right side begins with a rounded capital E followed by ns, not Ob. The covered Pi and outer parentheses are visible.',
    39: 'En fait is live: its long descending f continues into the area below, but no cancellation runs through the phrase. This differs from the actual horizontal strike on the lower line.',
    40: 'The crossed phrase runs across a line break. Initial and tall strokes support tentative opérant librement; the internal low letters are not sufficiently clear to remove doubt.',
    41: 'The cancelled article before pi has an upright l and a small e-loop. It remains deleted, not omitted or left unreadable.',
    42: 'The abbreviation is capital Pi followed by auto and one continuation stroke, represented by the retained TeX --- convention. No morphismes ending is visible.',
    43: 'The final target graph has an inward-curving right leg meeting toward the left stem, like the preceding compact pi. It is retained as literal lowercase pi despite the possible expectation of capital Pi.',
    44: 'The lower-left pencil numeral is 17. Its writer is unnamed, as is the writer of the upper-right 9.',
    45: 'The quotient is followed by a dark point in a high position. Its physical presence is clear but punctuation versus stray ink remains uncertain; the existing unsure point stays.',
}

row_evidence = {
    1: 'half1', 2: 'A_tuple', 3: 'A_tuple', 4: 'A_tuple', 5: 'A_tuple',
    6: 'main_objects_pi', 7: 'A_first-isom', 8: 'half1', 9: 'half1', 10: 'half1',
    11: 'A_isom-diagram', 12: 'A_isom-diagram', 13: 'A_isom-diagram',
    14: 'A_replacement', 15: 'A_replacement',
    16: 'A_margin', 17: 'A_margin', 18: 'A_margin', 19: 'A_margin',
    20: 'A_margin', 21: 'A_margin', 22: 'A_margin', 23: 'A_margin', 24: 'A_margin',
    25: 'A_unique-iso', 26: 'A_unique-iso', 27: 'A_unique-iso', 28: 'A_unique-iso',
    29: 'A_body-ending', 30: 'half2', 31: 'half2', 32: 'half2', 33: 'half2',
    34: 'half2', 35: 'half2', 36: 'half2', 37: 'half2', 38: 'half2',
    39: 'A_lower-cancellations', 40: 'A_lower-cancellations', 41: 'A_lower-cancellations',
    42: 'A_lower-cancellations', 43: 'A_final-pi', 44: 'half2', 45: 'main_objects_pi',
}
updated_rows = {4: findings[0], 5: findings[1], 12: findings[2], 16: findings[3], 25: findings[4]}
font_only_rows = {3, 6, 7, 9, 10, 11, 13, 22, 26, 27, 33, 37}
confirmed = []
for i, row in enumerate(accepted_report['changes'], 1):
    for witness in ('C', 'H'):
        quote = row[witness]
        assert quote == '[no witness]' or quote in packet['witness_' + witness], (i, witness, quote)
    literal = row['final']
    assert literal in before_tex, (i, literal)
    new_literal = updated_rows[i]['after'] if i in updated_rows else literal
    assert new_literal in candidate, (i, new_literal)
    view = row_evidence[i]
    item = {
        'accepted_change_row': i, 'place': row['place'],
        'C': row['C'], 'H': row['H'],
        'accepted_before': literal, 'candidate_after': new_literal,
        'audit_result': 'revised as finding ' + updated_rows[i]['id'] if i in updated_rows else 'confirmed without change',
        'reason': row_reasons[i],
        'confidence': updated_rows[i]['confidence'] if i in updated_rows else row['confidence'],
        'evidence': view,
        'scope': 'retained alphabet encoding only; no new material finding' if i in font_only_rows else 'physical reading or accepted uncertainty checked',
        'crop': f'crops/{KEY}_{view}.png' if view in crop_boxes else 'page',
        'box': crop_boxes.get(view),
    }
    confirmed.append(item)

confirmed.extend([
    {'place': 'Upper-right pagination and complete opening', 'candidate_after': r'\mspage{9}', 'audit_result': 'confirmed', 'reason': 'The graphite 9, underlined heading and On va définir were checked; no author or date is inferred.', 'evidence': 'original and half1'},
    {'place': 'All Pi/pi, tilde, prime and index occurrences', 'audit_result': 'confirmed except the separately identified contextual a resolution', 'reason': 'Input lowercase pi, output Pi and covered Pi, both object declarations, all j/j-prime fibres, two dotted z replacements, the functor circle and /F index, the action paragraph, capital Pi-auto and final lowercase pi were inspected separately. The final pi was not regularized from the mathematical role.', 'evidence': 'original and both halves, plus the listed local crops'},
    {'place': 'Central projection arrow and repeated prose down-arrow', 'audit_result': 'confirmed', 'reason': 'The diagram arrow has a long shaft and a downward head. The prose begins with a separate smaller downward arrow; both are represented. No arrowhead is added to the later bare fibre link.', 'evidence': 'original, both halves, A_isom-diagram and A_unique-iso'},
    {'place': 'Body point abbreviation before de Isom', 'candidate_after': r'\unsure{pt|p\textsuperscript{t}}', 'audit_result': 'existing uncertainty retained', 'reason': 'The t is small and high beside a long p descender, but its foot approaches the bowl baseline. The crop does not securely decide ordinary pt versus raised t.', 'evidence': 'A_body-point', 'crop': f'crops/{KEY}_A_body-point.png', 'box': crop_boxes['A_body-point']},
    {'place': 'Replacement above the cancelled central parenthesis', 'audit_result': 'placement confirmed; no extra guide supplied', 'reason': 'The live si parenthesis sits directly above the cancelled version. The long rising line below it is the cancellation across the older text, not an independent insertion guide or underline of the replacement.', 'evidence': 'A_replacement'},
])

mark_reasons = {
    'M0691': 'The capital I has top and bottom serifs, with a closely joined curling s immediately to its right. The following om is visible; the whole formula and its lower pi were checked independently of the prior proof note.',
    'M0692': 'The lower diagram RHS uses the same joined I-plus-s formation as its LHS and the upper definition. The short following om and both fibre arguments are present; no Hom substitution is made.',
    'M0693': 'The replacement starts with curved s and separately dotted i, giving si. Both following z graphs carry dots rather than bars.',
    'M0694': 'The live insertion has a c-like opening and compressed contr.-like sequence, but its tiny middle joins remain uncertain. The attachment guide, not the complete spelling, is secure.',
    'M0695': 'The prose operator again begins with the serifed stem and attached curled s, compressed into a broad outline before om. This agrees with the other local Isom forms.',
    'M0696': 'The en and tall descending f of fait are live. The downward f stroke is not a strike through en fait; the actual lower cancellation is separately visible.',
    'M0697': 'The final graph\'s right leg curves inward toward the left stem and exits right, unlike the separated verticals of the nearby capital Pi-auto. Lowercase pi remains the literal reading at medium confidence.',
}
mark_confirmations = []
original_ids = {m['id'] for m in packet['marks']}
for old in accepted_report['decisions']:
    assert old['id'] in original_ids
    item = {k: old[k] for k in ('id', 'decision', 'reading', 'confidence', 'crop', 'box')}
    item['audit_result'] = 'confirmed; no original MARKS decision update'
    item['ink'] = mark_reasons[old['id']]
    mark_confirmations.append(item)

remaining_doubts = []
for old in accepted_report['remaining_doubts']:
    if old['place'] == 'defining tuple final output':
        continue
    item = dict(old)
    item['audit_status'] = 'retained without narrowing'
    if old['place'].startswith('action-group letter:'):
        item['audit_evidence'] = 'Each occurrence was inspected on this page; no local identification displaces the shared E/Sigma alternative.'
    elif 'canceled old parenthesis' in old['place']:
        item['audit_evidence'] = 'Existing A_replacement crop inspected once; thick cancellation still prevents independent recovery of the complete letters or terminal close.'
    elif old['place'] == 'marginal insertion above foncteur':
        item['audit_evidence'] = 'Existing A_margin inspected once; physical insertion and guide clear, compressed letters still uncertain.'
    elif old['place'] == 'lower canceled phrase across the line break':
        item['audit_evidence'] = 'Existing A_lower-cancellations inspected once; the visible separated strokes do not justify full certainty.'
    elif 'isolated point' in old['place']:
        item['audit_evidence'] = 'Existing main_objects_pi inspected once; high dark point retained as uncertain punctuation.'
    else:
        item['audit_evidence'] = 'Existing A_body-point inspected once; t height remains ambiguous.'
    remaining_doubts.append(item)

inventory_confirmation = []
for old in accepted_report['inventory']:
    item = dict(old)
    item['audit_status'] = 'checked against source and proposed fragment'
    inventory_confirmation.append(item)
inventory_updates = [
    {'element': 'E03', 'finding': findings[0]['id'], 'update': 'Input-tuple suspension is drawn as one point plus one short stroke.'},
    {'element': 'E08', 'finding': findings[2]['id'], 'update': 'Central discrète parenthesis has the same two-mark suspension, not a three-point ellipsis.'},
    {'element': 'E12', 'finding': findings[3]['id'], 'update': 'Separator endpoint is shortened to stop above the final equivalence.'},
    {'element': 'E20', 'finding': findings[4]['id'], 'update': 'Previously inventoried attachment curve is now actually drawn with its elevated pi-prefix.'},
]

raw_rows = {
    3: [1], 4: [2], 5: [4], 6: [5], 9: [8], 17: [14], 19: [16],
    20: [18], 21: [19, 20], 23: [21], 24: [23], 25: [24],
    29: [25], 30: [28], 31: [29], 32: [30], 33: [31], 34: [32],
    35: [34], 36: [35], 37: [36], 38: [38], 39: [39], 40: [40],
    41: [41], 42: [42], 43: [43], 44: [44],
}
raw_marks = {8: 'M0691', 16: 'M0692', 18: 'M0693', 27: 'M0695', 43: 'M0697'}
raw_checks = []
for i, difference in enumerate(packet['differences'], 1):
    if i in raw_marks:
        disposition = 'Literal preferred reading and supplied alternative independently checked under the original MARK; no new MARK created.'
    elif i in raw_rows:
        disposition = 'Physical difference checked in the cited literal collation rows; proposed revisions are identified there.'
    elif i in (1, 2):
        disposition = 'Editorial page wrapper or unsupported authorship gloss; both source numerals retained with pencil hand unnamed.'
    elif i in (7, 11):
        disposition = 'The apparent raw comma comes from H\'s thin-space macro, not source punctuation; wrapper difference only.'
    elif i == 22:
        disposition = 'Equivalent arrow macros; the functor has a visible right-pointing head and no added arrow label.'
    elif i == 26:
        disposition = 'H editorial marginal/cancellation description is not source wording; the underlying source material was read and represented.'
    elif i == 28:
        disposition = 'H editorial interline wrapper refers to the live pi-prefix; the source guide is separately restored in F5.'
    else:
        disposition = 'Display/diagram/array/gathered layout syntax only; physical rows, braces, arrow and parenthesis inspected separately.'
    raw_checks.append({'packet_difference': i, 'accepted_change_rows': raw_rows.get(i, []), 'original_mark': raw_marks.get(i), 'disposition': disposition})

report = {
    'key': KEY, 'reader': 'C', 'stage': 'second reading', 'first_reader': 'A',
    'image_views': ['original', 'half1', 'half2'],
    'image_view_note': 'Each original/native-half image was successfully displayed once. No extra full-page or enlarged-half view was used.',
    'existing_crop_views': [{'crop': f'crops/{KEY}_{name}.png', 'box': box, 'views': 1} for name, box in crop_boxes.items()],
    'new_crops': [], 'findings': findings, 'confirmed': confirmed,
    'mark_confirmations': mark_confirmations,
    'remaining_doubts': remaining_doubts,
    'removed_doubts': [{'place': 'defining tuple final output', 'before': r'\unsure{a|\sim}', 'after': 'a', 'confidence': 'medium', 'finding': findings[1]['id'], 'reason': 'Contextual identification of the same compressed handwritten a, with main-reader comparison explicitly attributed.'}],
    'inventory_confirmation': inventory_confirmation,
    'inventory_additions': [], 'inventory_updates': inventory_updates,
    'raw_difference_checks': raw_checks,
    'notes': [
        {'id': f'{KEY}-auditC-N1', 'text': 'Full second reading complete. Four material graphic/punctuation corrections and one certainty-only resolution are proposed. All seven original MARKS decisions remain unchanged. Fourteen of the fifteen accepted remaining doubts remain; only the tuple a/sim doubt is removed.'},
        {'id': f'{KEY}-auditC-N2', 'text': 'The input-tuple and central-parenthesis continuations each have two visible marks, represented by a point and short bar. The marginal F(j) continuation has three marks and the body z-prime continuation four; their counts are retained. The terminal marks in those latter groups are horizontally elongated, but no new mark is supplied or removed.'},
        {'id': f'{KEY}-auditC-N3', 'text': 'The named action datum a is a contextual reading of a graph admitting that hand formation, not correction of an unmistakable relation sign. The source comparison from scan017 was supplied by the main reader; Reader C inspected only scan018. The separate final lowercase pi is retained even though the surrounding mathematics may suggest Pi.'},
        {'id': f'{KEY}-auditC-N4', 'text': 'Both actual attachment guides were checked. The contr.-to-foncteur guide is already drawn; the pi-prefix guide was inventoried but absent from the accepted TeX and is added. The rising line through the old central parenthesis is a cancellation, not a further guide.'},
        {'id': f'{KEY}-auditC-N5', 'text': 'The existing separator was too long relative to the final marginal equivalence. Only its endpoint changes; the double left pointer, functor arrow, raised circle, subscript /F and all marginal wording remain.'},
        {'id': f'{KEY}-auditC-N6', 'text': 'The first, diagram and prose Isom forms were compared graphically through the joined serifed I and curled s. The earlier main-reader torsor proof in accepted note N7 is not attributed to this audit and was not repeated. No proof claim arises from this visual confirmation.'},
        {'id': f'{KEY}-auditC-N7', 'text': 'The crossed preliminary object formula, tentative older parenthesis, live en fait, two lower cancellations, unexpanded isom and Pi-auto continuation, bare fibre shaft, uncertain point abbreviation and both pencil numerals remain as read. The pencil hand is unnamed; no date is inferred.'},
        {'id': f'{KEY}-auditC-N8', 'text': 'Only this page\'s packet, original, native halves, accepted fragment/report and twelve listed existing crops were visually used, with the authorized contract, reading guidelines and current notation table. No other page image, OCR, external research or TeX compilation was used.'},
    ],
    'check_events': [
        {'statement_id': f'{KEY}-N1', 'reader': 'C', 'stage': 'second reading', 'type': 'carried as background without fault found', 'outcome': 'The input/output tuple, object declarations, Isom equality and composition statement were visually collated. The a identification uses supplied notation and a compared handwriting form; no construction or categorical equivalence was proved.'},
        {'statement_id': f'{KEY}-N2', 'reader': 'C', 'stage': 'second reading', 'type': 'carried as background without fault found', 'outcome': 'The projection diagram, dotted replacement, discrete-category note, functor and explanation were checked against visible words and strokes. No torsor assertion, uniqueness claim or marginal equivalence was independently proved during this audit.'},
        {'statement_id': f'{KEY}-N3', 'reader': 'C', 'stage': 'second reading', 'type': 'carried as background without fault found', 'outcome': 'The lower action and quotient assertions were read with their actual group graphs, cancellations and abbreviation. Final lowercase pi was retained from its form; no action law or quotient assertion was validated mathematically.'},
    ],
    'prior_check_attribution': {'statement_id': f'{KEY}-N7', 'performed_by': 'main reader, in first adjudication', 'prior_type': 'targeted proof check', 'auditC_reperformed': False, 'note': 'This prior event remains attributed to main; it is not duplicated as a proof check by Reader C.'},
    'hand_log': [
        {'habit': 'A small rising shoulder and flattened wave can be a compressed lowercase a.', 'places': '143_scan018: final entry of the defining tuple.', 'scope': 'This occurrence inspected directly; comparison with the explicitly named scan017 a was supplied by main, not independently viewed by Reader C.', 'misreadings': 'H gives sim. The ambiguous local graph is identified contextually as a, without changing a clear source slip.'},
        {'habit': 'Continuation notation can have only two physical marks: a compact point followed by a short stroke.', 'places': '143_scan018: after input Z and after central cat. discrète.', 'scope': 'Both loci inspected once in their existing crops; the separate three- and four-mark groups were also counted.', 'misreadings': 'The accepted ldots supplied a third point at both two-mark loci; literal drawings preserve the actual count.'},
        {'habit': 'A serifed I joined closely to curled s can form a broad H- or omega-like outline.', 'places': '143_scan018: first Isom equality, central Isom diagram and body Isom operator.', 'scope': 'All three original Isom/Hom MARKS and their local comparisons inspected.', 'misreadings': 'C\'s Hom alternatives are not selected; joined I+s supports Isom independently of the main reader\'s prior mathematical check.'},
        {'habit': 'Compact lowercase pi can have an inward-curving right leg, while capital Pi has separated uprights.', 'places': '143_scan018: input pi, quotient pi, Pi-auto and final target pi.', 'scope': 'Local capital/lowercase forms compared throughout this sheet.', 'misreadings': 'Final lowercase pi remains literal; H\'s capital Pi is not substituted from the expected argument.'},
        {'habit': 'An interlinear prefix can be attached by a thin rising unheaded curve.', 'places': '143_scan018: contr. above foncteur and pi-prefix above isom.', 'scope': 'Both guides inspected in existing crops; old-parenthesis cancellation distinguished from them.', 'misreadings': 'The pi-prefix wrapper omitted its curve; the curve is restored graphically.'},
        {'habit': 'A tall f descender can cross into a genuinely cancelled line below without cancelling its own word.', 'places': '143_scan018: en fait above crossed librement.', 'scope': 'The two lines inspected together in A_lower-cancellations.', 'misreadings': 'H treats the en fait locus as crossed illegible text; it is retained live.'},
        {'habit': 'Small accents over z are points, distinct from the longer transverse cancellation nearby.', 'places': '143_scan018: both z graphs in the si replacement.', 'scope': 'Both points inspected directly.', 'misreadings': 'H gives bars; source points remain dot accents.'},
    ],
    'accepted_fragment_sha256': hashlib.sha256(accepted_bytes).hexdigest(),
    'candidate_unchanged': False,
    'completed_at': datetime.now(timezone.utc).isoformat(),
}

assert len(findings) == 5
assert sum(not f['certainty_only'] for f in findings) == 4
assert len(accepted_report['changes']) == 45
assert len(raw_checks) == len(packet['differences']) == 44
assert {x['id'] for x in mark_confirmations} == original_ids
assert len(mark_confirmations) == 7
assert len(inventory_confirmation) == 25
assert len(remaining_doubts) == 14
for item in report['existing_crop_views']:
    assert (WORK / item['crop']).is_file(), item['crop']
for item in confirmed:
    if 'candidate_after' in item:
        assert item['candidate_after'] in candidate, item['place']

# Strictly static delimiters and environment pairing, with \\ consumed as
# a control-symbol linebreak. No TeX compilation or page rendering occurs.
depth = 0
for token in re.findall(r'\\[A-Za-z]+|\\[^\n]|[{}]', candidate):
    if token == '{':
        depth += 1
    elif token == '}':
        depth -= 1
        assert depth >= 0
assert depth == 0
stack = []
for match in re.finditer(r'\\(begin|end)\{([^{}]+)\}', candidate):
    if match[1] == 'begin':
        stack.append(match[2])
    else:
        assert stack.pop() == match[2]
assert not stack

(WORK / 'reviews' / f'{KEY}_auditC.tex').write_text(candidate)
(WORK / 'reviews' / f'{KEY}_auditC.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
assert accepted_path.read_bytes() == accepted_bytes
print(json.dumps({'key': KEY, 'material_findings': 4, 'certainty_only_findings': 1, 'prior_rows_checked': 45, 'packet_differences_checked': 44, 'original_marks': 7, 'inventory_checked': 25, 'existing_crops_reused': 12, 'new_crops': 0, 'remaining_doubts': 14, 'static_validation': 'passed'}))
