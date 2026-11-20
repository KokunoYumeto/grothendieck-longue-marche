"""Write Reader C's second-reading record; no image reading or TeX compilation."""
from pathlib import Path
import copy
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/8f839dff4bf0')
WORK = ROOT / 'SP74_C13_143+145_work'
KEY = '143_scan021'
packet = json.loads((ROOT / 'reader_packets' / f'{KEY}.json').read_text())
accepted_path = WORK / 'pages' / f'{KEY}.tex'
accepted_report_path = WORK / 'reviews' / f'{KEY}_accepted.json'
accepted = accepted_path.read_text()
accepted_report_bytes = accepted_report_path.read_bytes()
prior = json.loads(accepted_report_bytes)

before = r'\pi_{t\to t\prime}'
# The source witnesses and accepted fragment use a literal apostrophe, not \prime.
before = "\\pi_{t\\to t'}"
after = "\\pi_{t\\unsure{\\mathbin{-}|\\to}t'}"
assert accepted.count(before) == 1
candidate = accepted.replace(before, after)

existing_crops = [
    ('crops/143_scan021_readerB_cancelled_fibres.png', [930, 270, 1640, 433]),
    ('crops/143_scan021_readerB_live_groupoid_glyphs.png', [468, 1093, 1175, 1310]),
    ('crops/143_scan021_main_alors.png', [335, 900, 1015, 990]),
    ('crops/143_scan021_readerB_components_restart.png', [339, 1525, 1455, 1748]),
    ('crops/143_scan021_readerB_centralise_assumption.png', [329, 1865, 1660, 2085]),
    ('crops/143_scan021_readerB_final_tail.png', [340, 2087, 1650, 2345]),
]
viewed_crop_paths = {x[0] for x in existing_crops}
new_crop = 'crops/143_scan021_auditC_morphism_set.png'
new_box = [1005, 1360, 1673, 1525]

finding = {
    'id': KEY + '-auditC-F1',
    'place': 'Morphism-set formula, connector between t and t-prime inside the pi subscript',
    'before': before,
    'after': after,
    'reason': 'The short thin shaft ends in a rounded, slightly raised blunt stub. No securely pointed arrowhead or separate lower arm is distinguishable. A bare shaft is the physical first reading; a compressed arrow remains possible. The t, terminal t-prime and the rest of the formula are clear and are not changed. This is a local sign uncertainty, not an unqualified claim that an arrowhead is missing.',
    'confidence': 'low',
    'crop': new_crop,
    'box': new_box,
    'against_C': True,
    'against_H': True,
    'C': "\\pi_{t\\to t'}",
    'H': "\\pi_{t \\to t'}",
    'kind': 'misread symbol or index',
    'consequential': True,
    'marked_in_H': False,
    'decision_updates': [],
    'certainty_only': False,
    'existing_change_row': None,
    'inventory_element': 'E07',
    'main_consultation': 'Main independently inspected this same crop and agreed that its rounded/upturned endpoint lacks a clearly separate lower arm. Main agreed to bare-shaft-first uncertainty, not an unqualified omitted-head reading. Reader C did not inspect any cross-page comparison image.'
}

# One observation for each existing, literal C/H collation row. A prior evidence
# crop is not represented as re-viewed unless it actually appears in the list above.
row_observations = [
    'The first fibre glyph has the flag-like top and broad return; the following j is low. Its alphabet remains open.',
    'The pi is low; the upward exit of the object glyph does not supply an independently identifiable slash. Keep the four alternatives, subscript first.',
    'The bare object-set glyph after dans has the same flag-like top and broad lower return.',
    'The lower exit of the object glyph is followed by blank paper; no separate comma is visible.',
    'The second fibre symbol and its j were read in the upper native half. The object glyph differs from the plain capped T of the adjacent map.',
    'The start is a low a followed by a tall l and joined ors, supporting alors rather than dont.',
    'The group glyph has two rounded lobes and some retracing; the E/Sigma encoding remains open without a separate deletion.',
    'The acted-on set has the same curled flag top and broad lower return as the cancelled set symbols.',
    'The groupoid uses single angle brackets, with local retracing, an object glyph, a separating comma and lower-case pi. Retracing does not establish double brackets.',
    'The first ens has no detached abbreviation point before des; this was checked in the native lower half.',
    'The object set after est has the same flag-top shape; its comma is retained. Checked in the native lower half.',
    'The second ens likewise lacks a detached point before des Isom; checked in the native lower half.',
    'The long cancellation crosses the low letters. Initial L, c-loop and p-like descender survive; the endings do not settle composantes versus composition.',
    'The large O and low n are followed by a tiny compact a-like mark. On a remains a medium-confidence reading, not a newly certain word.',
    'The component expression has pi with low zero and single angle brackets enclosing object glyph, comma and lower-case pi.',
    'The component quotient has a clear separate slash after its numerator, unlike the earlier low-pi locus.',
    'The small definition label has a looped d, tall f-like stroke and low rightward n-like return; dfn is retained at medium confidence.',
    'The pointed-set formula has lower-case pi with low 1, parentheses around the flag-top object and t, and equality to pi-sub-t. Checked in the native lower half.',
    'The opening of centralise is retraced, but no independent cancellation crosses the full word. It remains live.',
    'A distinct low point follows pi. Several much smaller high specks do not establish a second punctuation point; retain the period at medium confidence.',
    'On is crowded by the descender of que above. The following word has two p descenders and an ose ending, supporting On suppose, without final ons.',
    'A separate short horizontal dash follows the live isomorphism on the same line.',
    'The exit of termes is followed by a gap and on; no comma intervenes.',
    'The terminal rise of donné is followed by its comma without a further e. Retain the medium-confidence singular spelling.',
    'The final object-set glyph has a curled flag and broad lower sweep, distinct from the plain capped T and the following group letter.',
    'The final group letter has two rounded lobes; E/Sigma remains an alphabet question.',
    'The final group-ens has its hyphen and low letter sequence but no detached abbreviation period before de.',
    'The short word has a d ascender with a lower loop and one low e exit. There are no extra on-c strokes; M0699 remains alternative de.',
    'The final pi-ens is followed by a long descending comma, with no separate abbreviation full stop.',
    'The bottom-left graphite numeral 20 was read in the original and lower native half. The writing hand remains unnamed.',
]
assert len(row_observations) == len(prior['changes']) == 30
confirmed_rows = []
for number, (row, observation) in enumerate(zip(prior['changes'], row_observations), 1):
    viewed = row['crop'] in viewed_crop_paths
    confirmed_rows.append({
        'accepted_change_row': number,
        'place': row['place'],
        'C': row['C'],
        'H': row['H'],
        'reading': row['final'],
        'status': 'confirmed without revision',
        'confidence': row['confidence'],
        'observation': observation,
        'audit_evidence': row['crop'] if viewed else ('half1' if number == 5 else 'half2'),
        'crop_reused_in_this_audit': viewed,
        'prior_crop': row['crop'],
        'new_material_change': False,
    })

confirmed = [
    {'place': 'Top cancelled passage', 'checked': 'Read all words and formula objects through alors pi-t centralise. Two long oblique crossings cancel the block, including Phi(t):T to pi; puis also has its own local cancellation. P-j and the low j/t indices, colon before on considère and map arrow are retained.', 'evidence': ['original', 'half1', existing_crops[0][0], existing_crops[2][0]]},
    {'place': 'Live restriction and groupoid paragraph', 'checked': 'Considérons, restriction, opération, sur, à pi, d’où, groupoïde, objects and Isom(t,t-prime) were checked line by line. The two ens forms have no points. Single angle brackets are retained despite retracing. The group letter and object-set letter remain separately uncertain.', 'evidence': ['half1', 'half2', existing_crops[1][0]]},
    {'place': 'Morphism-set formula except indexed connector', 'checked': 'The enclosing pi is lower-case. Both t/t-prime positions, equality, curly braces, lambda in pi, the vertical separator, lambda t=t-prime and final baseline point are present. The first lambda is retraced; there is no independently recoverable deleted underletter to add. The indexed connector is the sole proposed material change.', 'evidence': ['half2', new_crop]},
    {'place': 'Cancelled restart and the two following formulas', 'checked': 'The restart remains cancelled and uncertain; On a remains live at medium confidence. The pi-zero formula has single angle brackets and a real slash in the quotient. The dfn label is retained. The pi-one formula keeps the source’s object-set argument and t, then pi-sub-t and its stabilisateur parenthesis; no expected alternative notation is supplied.', 'evidence': ['half2', existing_crops[3][0]]},
    {'place': 'Centralisation and commutativity', 'checked': 'The live centralise is not independently struck. Phi(t)(T), subset and lower-case pi remain, followed by the baseline point. On suppose precedes one underline under T commutatif. The plain T has a cap and vertical stem distinct from the flag-top object-set letter.', 'evidence': ['half2', existing_crops[4][0]]},
    {'place': 'Cancelled equality and live isomorphism', 'checked': 'The equality pi-sub-t=Phi-sub-t(T) is cancelled. The following Phi-sub-t:T isomorphism to pi-sub-t is live, with a visible arrowhead and tilde, followed by a separate dash. Phi(t) earlier and Phi-sub-t here remain distinct. No physical guide/caret accompanies this replacement.', 'evidence': ['half2', existing_crops[5][0]]},
    {'place': 'Last prose and pagination', 'checked': 'Du is separately struck. The live prose has d’autres termes without a comma, donné with its comma, en plus de the object set, group-ens de pi-ens, ending in a descending comma. M0699 is de. No continuation was consulted. Graphite 20 at bottom left belongs to an unnamed hand.', 'evidence': ['original', 'half2', existing_crops[5][0]]},
    {'place': 'Page-wide physical additions', 'checked': 'Margins, line ends, cancellation strokes, underlining, parentheses, single angle brackets and map shafts were checked against the full original and native halves. No omitted insertion word, guide, caret or marginal note was identified. The full visible lower edge and pencil numeral were included.', 'evidence': ['original', 'half1', 'half2']},
    {'place': 'Pi/pi and object-set comparisons', 'checked': 'All formula pi graphs on this page have the lower-case form, often with a rounded or inward-curving right leg. No capital Pi is substituted. All eleven flag-top object-set occurrences remain tau/calligraphic-T uncertainty. Both two-lobed group letters remain E/Sigma uncertainty. These are confirmations of existing rendering choices, not new material rows.', 'evidence': ['original', 'half1', 'half2', existing_crops[0][0], existing_crops[1][0], existing_crops[3][0], existing_crops[5][0]]},
]

inventory_observations = [
    'Whole-block cancellation and all top-line words and fibre symbols read; no missing boundary text.',
    'Puis has its own strike in addition to the oblique whole-block cancellation.',
    'P-j, t in the fibre, stabilisateur pi-sub-t, de t dans pi and on considère all retained.',
    'Phi(t), colon, plain T, rightward headed arrow and pi lie inside the whole cancellation.',
    'Alors, pi-sub-t and centralise are cancelled with the block.',
    'Restriction/action/groupoid words, object statement, two point-free ens forms and Isom(t,t-prime) checked.',
    'All formula objects retained; indexed connector revised only to explicit bare-shaft/arrow uncertainty.',
    'Cancelled restart has recoverable partial letters but unresolved ending; existing two alternatives retained.',
    'On a retained with the tiny a at medium confidence.',
    'Pi-zero, single brackets, quotient slash, dfn label, equalities and J checked.',
    'Pi-one with pointed object-set argument, pi-sub-t and stabilizer parenthesis checked.',
    'Live centralise, Phi(t)(T), subset pi, low point and On suppose checked.',
    'One continuous underline under T commutatif, not an insertion guide.',
    'Pi-sub-t=Phi-sub-t(T) is visibly crossed once.',
    'Live Phi-sub-t isomorphism has tilde, headed arrow, pi-sub-t and following dash.',
    'Du independently struck; no insertion guide attached.',
    'Final two lines retain donné, de, no comma after termes, no ens abbreviation points and final comma.',
    'Graphite 20 at bottom left; unnamed hand.',
]
inventory_confirmation = []
for item, obs in zip(prior['inventory'], inventory_observations):
    inventory_confirmation.append({'element': item['element'], 'position': item['position'], 'status': 'checked', 'observation': obs})

raw_map = [[], [1], [2], [2], [3,4], [5], [], [], [], [6], [], [7], [8], [9], [10], [11], [12], [], [13], [14], [15], [16], [17], [18], [20,21], [], [22], [23], [24], [25,26], [27,28], [29], [30]]
raw_special = {
    1: 'The scanpage wrapper is an editorial locator, not an additional manuscript number.',
    7: 'Tikzcd environment syntax is not manuscript text; the actual cancelled map was checked.',
    8: 'Ampersand-replacement and environment options are markup, not manuscript text.',
    9: 'Different arrow implementations encode the same visibly headed arrow in the cancelled map.',
    11: 'H’s note describes the two oblique cancellation strokes; its editorial words are not source text.',
    18: 'Display-delimiter difference only; actual morphism formula checked separately, including the new connector doubt.',
    26: 'Display-delimiter difference only; the live isomorphism remains beside the cancelled equality.',
    33: 'Pencil 20 retained. H’s continuation note and end-document syntax are editorial; no next page was consulted.',
}
assert len(raw_map) == len(packet['differences']) == 33
raw_checks = []
for number, (row, mapped) in enumerate(zip(packet['differences'], raw_map), 1):
    raw_checks.append({'packet_difference_number': number, 'raw': copy.deepcopy(row), 'accepted_change_rows': mapped, 'status': 'checked', 'disposition': raw_special.get(number, 'Literal witness difference checked against the ink; existing accepted reading confirmed in the referenced row(s).')})

doubts = copy.deepcopy(prior['remaining_doubts'])
doubts.append({
    'place': finding['place'],
    'reading': after,
    'alternatives': 'Bare horizontal shaft between t and t-prime; a compressed right arrow.',
    'confidence': 'low',
    'reason': finding['reason'],
    'crop': new_crop,
    'box': new_box,
    'new_in_second_reading': True,
})

notes = [
    {'id': KEY+'-auditC-N1', 'text': 'The cancelled top text describes pi-torsors and their fibres, a stabilizer and Phi(t):T to pi. The second reading checks wording, indices, map and cancellation state. The source’s fibre/orbit notation remains uncertain; its mathematics is not used to supply a slash or an index.'},
    {'id': KEY+'-auditC-N2', 'text': 'The live action-groupoid account, morphism condition lambda t=t-prime and component/fundamental-group formulas were transcribed as written. The new low-confidence shaft/arrow alternative concerns only the tiny connector inside the morphism-set subscript. Its mathematical context does not establish a visibly absent head.'},
    {'id': KEY+'-auditC-N3', 'text': 'The source’s centralisation statement, underlined commutativity assumption, cancelled equality and live isomorphism are preserved. Phi(t) in the centralisation statement and Phi-sub-t in the replacement are distinct written forms. No mathematical validity check of these assertions was performed.'},
    {'id': KEY+'-auditC-N4', 'text': 'All four existing remaining doubts are retained unchanged; the indexed connector is a fifth. No existing collation row requires revised evidence or confidence, and no original MARK changes. Pure object-set and extension-letter alphabet questions do not create new material changes.'},
    {'id': KEY+'-auditC-N5', 'text': 'The final short word remains de under M0699; the source ends in pi-ens followed by a comma. No continuation was inspected. The bottom-left graphite 20 is attributed only to an unnamed hand. No omitted insertion guide or caret was found on this page.'},
]

hand_log = [
    {'habit': 'Curled flag-like top and broad lower return in the object-set letter.', 'places': 'All eleven object-set occurrences.', 'scope': 'Compared in this page’s original and native halves, with existing crops reused locally.', 'misreadings': 'Tau/calligraphic-T remains open. Plain capped T and the group glyph were not conflated with it.'},
    {'habit': 'The object glyph’s rising exit can resemble part of a slash.', 'places': 'First orbit-set expression compared with the later explicit quotient.', 'scope': 'Both corresponding existing crops viewed once.', 'misreadings': 'Subscript-first uncertainty is retained for the first locus; the later clear slash does not repair it.'},
    {'habit': 'A tiny connector may end in a rounded raised stub without separately resolved arrow wings.', 'places': 'Morphism-set subscript t to t-prime.', 'scope': 'One new tight crop of this previously unrecorded locus, native box [1005,1360,1673,1525].', 'misreadings': 'Both witnesses supply an arrow; the audit retains bare shaft first and arrow as alternative.'},
    {'habit': 'Retracing can thicken a letter or bracket without creating an extra character or deletion.', 'places': 'Action-group letter, groupoid angle brackets, first lambda of the morphism set, live centralise.', 'scope': 'Whole-page/half reading and the respective local crops.', 'misreadings': 'No double angle bracket, extra deleted lambda underletter or cancellation of centralise is inferred.'},
    {'habit': 'Very compressed letters and descending strokes can crowd a following phrase.', 'places': 'Tiny a in On a; descender of que above On suppose.', 'scope': 'Existing components and centralise crops reused once.', 'misreadings': 'On a remains medium confidence; On suppose remains high confidence.'},
    {'habit': 'Final ens exits can be long without a separate abbreviation point.', 'places': 'Both l’ens forms and both final group-ens forms.', 'scope': 'All four checked; final comma read independently.', 'misreadings': 'No period from H is added.'},
    {'habit': 'Several tiny high specks can accompany a distinct baseline point.', 'places': 'After Phi(t)(T) subset pi.', 'scope': 'Existing centralise-assumption crop reused once.', 'misreadings': 'The definite lower point remains a period; the isolated high specks do not establish a colon.'},
]

report = {
    'key': KEY,
    'reader': 'C',
    'stage': 'second reading',
    'first_reader': 'B',
    'image_views': ['original', 'half1', 'half2'],
    'image_view_details': [
        {'view': 'original', 'path': packet['image'], 'successful_views': 1},
        {'view': 'half1', 'path': packet['halves'][0], 'box': packet['half_boxes'][0], 'successful_views': 1},
        {'view': 'half2', 'path': packet['halves'][1], 'box': packet['half_boxes'][1], 'successful_views': 1},
    ],
    'existing_crop_views': [{'crop': path, 'box': box, 'successful_views': 1} for path,box in existing_crops],
    'new_crops': [{'crop': new_crop, 'box': new_box, 'successful_views': 1, 'script': 'scripts/143_scan021_auditC_crops.py', 'reason': 'Previously unrecorded uncertainty in the tiny indexed connector; no existing crop covered this locus.'}],
    'view_log_note': 'A combined call for the components, centralise and final-tail crops was truncated before any image was displayed. It was not an inspection. Each was subsequently emitted and inspected individually once; those successful views are the ones recorded here.',
    'findings': [finding],
    'confirmed': confirmed,
    'collation_confirmation': confirmed_rows,
    'remaining_doubts': doubts,
    'remaining_doubt_disposition': [{'existing_place': d['place'], 'status': 'retained unchanged'} for d in prior['remaining_doubts']],
    'mark_confirmations': [dict(copy.deepcopy(d), audit_status='confirmed unchanged', audit_reader='C') for d in prior['decisions']],
    'decisions': copy.deepcopy(prior['decisions']),
    'inventory_confirmation': inventory_confirmation,
    'inventory_additions': [],
    'inventory_updates': [{'element': 'E07', 'field': 'first_words_or_objects', 'before': prior['inventory'][6]['first_words_or_objects'], 'after': 'pi-sub-t-(bare shaft or right arrow)-t-prime={lambda in pi | lambda t=t-prime}.', 'reason': 'Existing element retained; its indexed connector now records the new local uncertainty.'}],
    'raw_difference_checks': raw_checks,
    'notes': notes,
    'check_events': [
        {'statement_id': notes[0]['id'], 'type': 'carried as background without fault found', 'outcome': 'Reader C checked the cancelled torsor/fibre wording and symbols against ink; no torsor/fibre proposition was proved.', 'checked_by': 'Reader C, second reading'},
        {'statement_id': notes[1]['id'], 'type': 'carried as background without fault found', 'outcome': 'Reader C read the action-groupoid definitions and pi-zero/pi-one expressions without proving the identifications or completing the indexed connector from context.', 'checked_by': 'Reader C, second reading'},
        {'statement_id': notes[2]['id'], 'type': 'carried as background without fault found', 'outcome': 'Reader C checked the centralisation and commutativity/isomorphism statements as source text, without a mathematical proof check.', 'checked_by': 'Reader C, second reading'},
    ],
    'prior_check_event_attribution': 'The accepted report already records background-only readings. No earlier proof is claimed as an auditC check.',
    'hand_log': hand_log,
    'accepted_fragment_sha256_before': hashlib.sha256(accepted.encode()).hexdigest(),
    'accepted_report_sha256_before': hashlib.sha256(accepted_report_bytes).hexdigest(),
    'counts': {'material_findings': 1, 'certainty_only_findings': 0, 'confirmed_prior_collation_rows': 30, 'packet_difference_rows_checked': 33, 'original_marks_checked': 1, 'inventory_elements_checked': 18, 'remaining_doubts': 5, 'existing_crops_reused': 6, 'new_crops': 1},
}

# Only static structural and literal-source validation. No TeX compilation.
assert finding['C'] in packet['witness_C']
assert finding['H'] in packet['witness_H']
assert finding['before'] in accepted
assert finding['after'] in candidate
for row in confirmed_rows:
    assert row['C'] == '[no witness]' or row['C'] in packet['witness_C'], row
    assert row['H'] == '[no witness]' or row['H'] in packet['witness_H'], row
    assert row['reading'] in candidate, row
assert {d['id'] for d in report['decisions']} == {d['id'] for d in packet['marks']}
for path,_box in existing_crops + [(new_crop,new_box)]:
    assert (WORK/path).is_file(), path
assert len(inventory_confirmation) == 18
assert candidate.count('\\scanpage{') == 1
assert candidate.count('\\mspage{') == 1

# Lex control sequences first so escaped braces and double-backslash breaks
# cannot affect the group stack.
depth = 0
i = 0
while i < len(candidate):
    c = candidate[i]
    if c == '%':
        eol = candidate.find('\n',i)
        i = len(candidate) if eol == -1 else eol+1
        continue
    if c == '\\':
        i += 1
        if i < len(candidate) and candidate[i].isalpha():
            while i < len(candidate) and candidate[i].isalpha():
                i += 1
        else:
            i += 1
        continue
    if c == '{': depth += 1
    if c == '}':
        depth -= 1
        assert depth >= 0
    i += 1
assert depth == 0
stack = []
for match in re.finditer(r'\\(begin|end)\{([^{}]+)\}', candidate):
    if match.group(1) == 'begin': stack.append(match.group(2))
    else: assert stack.pop() == match.group(2)
assert not stack
assert accepted_path.read_text() == accepted
assert accepted_report_path.read_bytes() == accepted_report_bytes

tex_out = WORK/'reviews'/f'{KEY}_auditC.tex'
json_out = WORK/'reviews'/f'{KEY}_auditC.json'
tex_out.write_text(candidate)
report['validation'] = {'literal_witness_snippets': 'passed', 'literal_before_after': 'passed', 'all_original_marks': 'passed', 'balanced_braces_and_environments': 'passed', 'crop_files_exist': 'passed', 'accepted_files_unchanged': 'passed', 'tex_compilation': 'not performed', 'ocr_or_external_research': 'not performed'}
json_out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'tex':str(tex_out),'report':str(json_out),'counts':report['counts'],'validation':report['validation']},ensure_ascii=False,indent=2))
