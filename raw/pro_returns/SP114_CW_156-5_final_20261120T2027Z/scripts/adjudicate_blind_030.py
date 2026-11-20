"""Prepare the main reader's explicit scan030 blind-audit decisions.

This script records decisions supplied after the main reader inspected all34
differing fresh crops. It does not make visual decisions, apply the audit, or
modify any primary page or sealed first/second reading.
"""
from pathlib import Path
import csv, hashlib, json

r = Path(__file__).resolve().parents[1]
p = r / 'pages/J156-5-04_156-5_scan030.tex'
rec = json.loads((r / 'review/scan030_adjudicated.json').read_text())
comp = json.loads((r / 'second/J156-5-04_156-5_scan030_comparison.json').read_text())
by_box = {x['box']: x for x in comp}
fresh = json.loads((r / 'second/J156-5-04_156-5_scan030_blind_notes.json').read_text())
crop_notes = {x['box']: x for x in fresh['boxes']}
with (r / 'second/J156-5-04_156-5_scan030_boxes.tsv').open(newline='') as f:
    boxes = {x['box']: x for x in csv.DictReader(f, delimiter='\t')}

old_member = by_box['030_membership_two']['first']
new_member = r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node at (0,0) {$A'$};
\node at (.6,0) {$\cap$};
\node at (1.2,0) {$B'$};
\node[anchor=west] at (1.75,0) {$\in F.G,$};
\node[rotate=-90] at (0,-.5) {$\in$};
\node[rotate=-90] at (1.2,-.5) {$\in$};
\node at (0,-1) {$F$};
\node at (1.2,-1) {$G$};
\node[anchor=west] at (4,0) {et $A'\cap B'\subset A\cap B$ \deleted{\unsure{bien|i.e.}}, alors};
\node[anchor=west] (ins) at (2,-.9) {\inserted{i.e. $A'^\circ\cap B'^\circ\ne\phi$}};
\draw (3.45,-.1) to[out=-70,in=95] (2,-.7);
\end{tikzpicture}}'''
old_left_relation = r'''G\arrow[r,phantom,"\leq" description]\&F\arrow[d,phantom,"\rotatebox{90}{$\preceq$}" description]'''
new_left_relation = r'''G\arrow[r,phantom,"\leq" description]\&F\arrow[d,phantom,"\rotatebox{90}{$\unsure{\preceq|\ll}$}" description]'''
new_deleted_word = r'\deleted{\unsure{bien|i.e.}}'
new_terminal = r'\unsure{$C_3$.|Cor.|C6.}'
new_old_term = r'\deleted{(\unsure{F\setminus G|F.G|F\times G}\unsure{2|?})}'
edits = [
    {'old': r'\margin{(résulte de a), en regardant supports)}',
     'new': r'\margin{(\unsure{résulte} de a), en regardant supports)}'},
    {'old': r'\uline{explicitation}', 'new': r'\uline{\unsure{explicitation|explication}}'},
    {'old': r'\deleted{\unsure{or}}', 'new': r'\deleted{\unsure{or|ces|ce}}'},
    {'old': 'et dans les deux cas le sens', 'new': r'et dans les deux cas \unsure{le|les} sens'},
    {'old': old_member, 'new': new_member},
    {'old': r"d'où $G'$ avec", 'new': r"d'où $G'$ \unsure{avec}"},
    {'old': old_left_relation, 'new': new_left_relation},
    {'old': r'\unsure{Cor.|C6.}', 'new': new_terminal},
    {'old': r'\unsure{\leq|<}', 'new': r'\unsure{\leq|<|\preceq}'},
    {'old': r'\uline{Cor}.', 'new': r'\uline{Cor.}'},
    {'old': r'\deleted{\unsure{(F.G)}}', 'new': new_old_term},
    {'old': r'\deleted{raffine}', 'new': r'\deleted{\unsure{raffine}}'},
]

def transform(s):
    """Apply the supplied page edits also to overlapping sealed excerpts."""
    for e in edits:
        s = s.replace(e['old'], e['new'])
    # These excerpts end before the full page anchors or isolate one component.
    s = s.replace(r'\deleted{\unsure{\text{i.e.}}}', new_deleted_word)
    if s == 'le':
        s = r'\unsure{le|les}'
    if s.endswith('et dans les deux cas le '):
        s = s[:-3] + r'\unsure{le|les} '
    return s

# UTC entries are the main reader's inspection times (or recorded by-times),
# supplied by the main reader; no new visual inspection is represented here.
O = {
    'abc': ('20:05:17', 'Each implication has two shafts. Row a has the doubled less-than; row b has the curved subdivision sign; row c has the straight less-or-equal. Product dots sit low. The final star is raised but detached to the right of G, so it remains a call sign rather than a G exponent. The preceq/preccurlyeq and period/cdot differences are representations of the same observed signs.', 'high'),
    'margin_a': ('20:05:17', 'The small comment reads trivial par déf. de the doubled less-than comme Inf. The I has bilateral serifs, partly overlapping the f above; the n is low and the final f has a long descender. These strokes support Inf without an added doubt.', 'high'),
    'margin_b': ('20:05:17', 'The initial r and accented e of résulte are heavily blackened or retraced, while the following su/lt/e strokes survive. Keep résulte as the preferred reading but restore doubt; de a), en regardant supports is unchanged.', 'medium'),
    'star_heading': ('20:05:27', 'The underlined word exposes expli-, a tall l, a dotted i, c, a long low middle segment and the final t/i/on run. A small separate stroke after c does not securely establish the extra -it- of explicitation. Preserve explicitation first and add explication as an alternative. The star remains a separate gloss marker.', 'medium'),
    'star_formula': ('20:05:27', 'The complete formula shows F-prime dot G, the opening brace, A in F dot G, the separator, A subset support F-prime and the closing brace. Both support bars and the high prime are visible. The blind difference is only period/cdot formatting.', 'high'),
    'deleted_FG': ('20:05:27', 'F-prime dot G is under two crossing cancellation strokes, and its low product dot is visible. The period/cdot spelling does not change the reading or deletion scope.', 'high'),
    'or': ('20:05:47', 'The tiny cancelled group before the separate large live Or has rounded loops and a rightward terminal beneath the strike. These admit or, ces or ce. Retain or first, add ces/ce, and keep the following live Or and F-prime dot G est formé outside the deletion.', 'low'),
    'phi_pair': ('20:05:47', 'Both empty-set glyphs have an oval on a long slanting stem, so phi is retained rather than normalizing them to a slashed circle. The first B-in-G is clear; the second terminal G/L remains clipped. This overlapping excerpt also receives the cancelled-or alternatives and the le/les doubt decided in their own tight crops; the formulas themselves are retained.', 'medium'),
    'edge_G': ('20:05:47', 'The terminal letter at the far cut edge has a visible descending left stroke and a low right foot that can look like L, while its upper and right ink are clipped. Retain G/L rather than resolve G from context. The longer blind A-cap-B context is already present on the page.', 'medium'),
    'le': ('20:06:00', 'A tall looped l is followed by a long flattened stroke with a downward hook. The compressed ending does not securely distinguish le from les. Retain le as preferred and record les as the alternative.', 'medium'),
    'parenthesis': ('20:06:00', 'The stops of p.r. and accent of à are visible. After F and the comma, a short d with a vertical foot joins a long low run before the high-prime F. The compressed middle does not settle full dans versus ds, so retain that doubt and the visible closing parenthesis.', 'medium'),
    'cancelled_membership': ('20:06:00', 'A short local strike crosses A-cap-B inside the longer horizontal cancellation through the entire abandoned parenthesis. The A shapes and cap are visible, and a raised dark prime remains at the upper right of F, though partly near the crop edge. Retain nested deletion, the F prime and the comma; the blind omission of the local strike and prime is not adopted.', 'medium'),
    'membership_one': ('20:06:18', 'A and B lie on the main baseline, each with a rotated membership sign below; F-prime is below A and G below B. The main membership is in F-prime dot G, followed by i.e. and the circled A/B nonempty-intersection formula with phi. The existing display records this geometry; the blind TikZ version is an equivalent representation.', 'high'),
    'membership_two': ('20:06:18', 'A-prime and B-prime both carry their high primes, with downward membership signs over F and G. A thin headless curve descends from the comma after F dot G and turns left toward the beginning of the inserted i.e. formula. Restore that leader explicitly in TikZ; retain all members, primes, circles and phi. The old word after the containment is changed separately to doubtful bien/i.e. on its tight crop.', 'high'),
    'inserted_ie': ('20:06:18', 'The two stops of i.e., both high primes and circles on A and B, and the oval on the long stem of phi are visible. Retain the inserted formula exactly. Its attachment leader is reproduced as part of the encompassing second-membership drawing, without changing the formula.', 'high'),
    'deleted_ie': ('20:06:27', 'The heavy zigzag strikes leave an initial tall b-like loop, a separate dot in the middle and a low terminal n-like run. Two separate abbreviation stops are not apparent. Prefer bien but retain i.e. because the cancellation hides parts of the letters.', 'low'),
    'repeated_que': ('20:06:27', 'A-prime in F-prime precedes the clear live words Or on sait que. The blind excerpt merely includes that already-transcribed prefix. Retain this que and the second que after the explanatory parenthesis; do not regularize the repetition.', 'high'),
    'left_heading': ('20:06:44', 'In the upright rotated crop, the underlined heading has Expli-, c, a narrow i/t sequence and a low -er ending, supporting Expliciter rather than Explication. The next compact s/o/i/t group reads soit, without an extra -en- sequence for soient. Retain the separate underline and colon.', 'medium'),
    'left_note': ('20:06:54', 'G≤F is horizontal, with F-prime below F. The intervening paired short curved or angled strokes have no long shaft; retain a rotated preceq as preferred, with ll as an alternative and no Downarrow. The flattened connective after G-prime remains avec with doubt. The following G-prime relations, set formula, inverse image and map are retained. The separate terminal label receives the C-subscript3 alternative preferred on its own crop.', 'medium'),
    'left_terminal': ('20:09:56', 'The isolated terminal mark has a large open C followed by a smaller low two-lobed curl and a detached stop. The low curl favours a subscript3 over a closed 6 or joined or. Prefer C-subscript3 with its stop, retaining Cor. and C6. as alternatives rather than claiming certainty.', 'medium'),
    'right_opening': ('20:09:56', 'The first groups show the broad U/n run, descending p with a low eu run, then dotted i and a long f in vif. The following writing supports on trouve par, F-prime dot G equals G-prime, un G-prime, tel que. Retain these words; the blind Alors que ici/inf and avec do not match those strokes.', 'medium'),
    'right_square': ('20:09:56', 'F-prime and F are on the upper row and G-prime and G below. Both horizontal relations have curved parallel lower strokes. Each vertical relation has a downward angle with a separate adjacent bar, consistent with the rotated less-or-equal used in the first reading, not a long-shaft arrow. Retain the square and its four relations; the blind excerpt also includes neighbouring text already separately recorded.', 'high'),
    'unicite': ('20:10:17', 'The small line reads mais il faut vérifier encore l’unicité, with a continuous separate underline beneath unicité. The two readings differ only by the surrounding margin wrapper, already supplied by the full note.', 'high'),
    'amene': ('20:10:17', 'The initial C/e/l/a group, the low amène run with its accent, the separate accented à and the two descending g strokes in dégager support Cela amène à dégager. The blind margin wrapper adds no source text.', 'high'),
    'ab': ('20:10:17', 'The live a/b formulas distinguish doubled less-than, curved subdivision and straight less-or-equal, with double-shaft implications. In the cancelled fragment after the second R, the overstrike reaches the lower implication shaft and continues through P and the next relation, so retain that arrow inside the deletion. The masked relation still prefers less-or-equal, with less-than and curved subdivision as alternatives. All live letters and implications remain unchanged.', 'medium'),
    'cor': ('20:10:17', 'The heading shows Cor. with the stop above the terminal reach of its underline, so include the stop within uline. C6 is clear. The v/a movement, tall l, b loop and final l/e support valable, retained without the blind added doubt.', 'high'),
    'quand': ('20:10:17', 'The long initial V, dotted and ascending strokes of Vérifions, the descending q and low u/an/d of quand, and the accented même are visible. The following C7 has a small low 0. The two readings differ only in math-mode boundaries.', 'high'),
    'C70': ('20:10:17', 'The capital C, crossed descending 7 and separate small low oval 0 are visible. The 0 belongs to the C7 reference in the main line; the large stroke to its right is the marginal boundary. Retain the subscript and add no stop.', 'high'),
    'c7_diagram': ('20:10:30', 'The live G≤F is horizontal. Below G, the paired curved subdivision strokes lead toward G-prime and differ from the straight horizontal less-or-equal bar; keep the rotated preceq without a new leq alternative. The existence symbol and two-line subdivision clause remain in their existing relative positions.', 'high'),
    'construction': ('20:10:30', 'The live equation has F-prime, equality, G-prime, a union cup and the later parenthesized F-minus-G. The abandoned parenthesized middle term receives the reading decided on its tight crop: a descending oblique operator beneath upward hatching and an additional turned mark before its closing parenthesis. The live construction and réunion disjointe are unchanged.', 'low'),
    'deleted_construction': ('20:10:30', 'Beneath the dense up-right hatching, an oblique descending mark survives between the first F-like letter and the G loop with its lower foot. Prefer F-minus-G, retaining F dot G and F times G. A further small turned mark before the separate closing parenthesis resembles 2 or a question mark and must not be omitted. The whole parenthesized term remains cancelled and low-confidence.', 'low'),
    'bottom_b': ('20:10:30', 'The two f descenders and the dotted i of the old raffine remain, but the heavy horizontal strike masks portions of the initial and final low letters. Restore doubt around raffine. The live que, raised subdivise, following F and et remain as transcribed.', 'medium'),
    'upper_grouping': ('20:11:12', 'The upper note is bounded on the left by the long grouping stroke and its separate lower-starting companion. Retain their existing relative placement, the Un peu vif opening, the square of horizontal subdivision and vertical less-or-equal signs, and the underlined unicité. The blind single-line boundary and differing words do not replace the first reading.', 'high'),
    'lower_grouping': ('20:11:12', 'The lower boundary begins with a curved entry, descends beside a and the first b row, steps right below that row and descends beside the indented continuation. Retain that stepped geometry. Its overlapping cancelled relation gains the preceq alternative decided in the ab crop; the first implication remains inside the deletion and all live formulas are unchanged.', 'medium'),
}

def evidence(k):
    key = '030_' + k
    b = boxes[key]
    f = crop_notes[key]
    crop = f['crop_path'].removeprefix('deliverable/')
    assert (r / crop).is_file(), crop
    co = [int(b[z]) for z in ('x0', 'y0', 'x1', 'y1')]
    assert co == [f['source_bounds'][z] for z in ('x0', 'y0', 'x1', 'y1')]
    return {'evidence': O[k][1], 'crop': crop, 'box': co,
            'rotation': f['rotation_degrees_counterclockwise'],
            'main_decision': 'Main-reader decision after independent blind reading; see the first/second/final audit.'}

decisions = []
for x in comp:
    if not x['different']:
        continue
    k = x['box'].removeprefix('030_')
    tm, ev, confidence = O[k]
    final = transform(x['first'])
    decisions.append({'box': x['box'], 'changed': final != x['first'],
                      'final': final, 'evidence': ev, 'confidence': confidence,
                      'crop': evidence(k)['crop'],
                      'rotation_degrees': crop_notes[x['box']]['rotation_degrees_counterclockwise'],
                      'viewed_utc': f'2026-11-20 {tm} UTC'})
assert len(decisions) == 34
assert {x['box'] for x in decisions} == {x['box'] for x in comp if x['different']}

updates = []
def up(id, k, **fields):
    updates.append({'id': id, 'fields': {**fields, **evidence(k)}})

up('030-006', 'margin_b', final=r'\unsure{résulte}', confidence='medium',
   against_C=False, against_H=False, certainty_only=True)
up('030-008', 'star_heading', final=r'\unsure{explicitation|explication}', confidence='medium',
   against_C=False, against_H=False, certainty_only=True)
up('030-010', 'or', final=r'\deleted{\unsure{or|ces|ce}} Or', confidence='low')
up('030-012', 'le', final=r'\unsure{le|les}', confidence='medium')
up('030-024', 'membership_two',
   final=r"\inserted{i.e. $A'^\circ\cap B'^\circ\ne\phi$}, with the headless curved attachment leader reproduced in the second-membership TikZ drawing",
   confidence='high')
up('030-025', 'deleted_ie', final=new_deleted_word, confidence='low', against_C=True, against_H=True)
up('030-029', 'left_note',
   final=r'G≤F horizontally, F-prime beneath F, joined by \rotatebox{90}{$\unsure{\preceq|\ll}$}',
   confidence='medium')
up('030-031', 'left_terminal', final=new_terminal, confidence='medium', against_C=True, against_H=True)
up('030-043', 'construction',
   final=r"F'=G'\cup" + new_old_term + r'(F\setminus G)',
   confidence='low', review_only=True, against_C=False, against_H=False)
up('030-044', 'deleted_construction', final=new_old_term, confidence='low', against_C=True, against_H=True)
up('030-047', 'bottom_b', final=r'\deleted{\unsure{raffine}}', confidence='medium',
   against_C=False, against_H=False, certainty_only=True)
up('030-056', 'cor', final=r'\uline{Cor.}', confidence='high', against_C=True, against_H=True)

unresolved = []
for old in rec['unresolved']:
    x = dict(old)
    k = None
    if x['place'] == 'small cancelled word before live Or':
        k = 'or'; x.update(reading=r'\deleted{\unsure{or|ces|ce}}', alternatives=['ces', 'ce'], confidence='low')
    elif x['place'] == 'cancelled text after A prime cap B prime subset A cap B':
        k = 'deleted_ie'; x.update(reading=new_deleted_word, alternatives=['i.e.'], confidence='low')
    elif x['place'] == 'left marginal note short terminal label':
        k = 'left_terminal'; x.update(reading=new_terminal, alternatives=['Cor.', 'C6.'], confidence='medium')
    elif x['place'] == 'right note b, deleted old implication':
        k = 'ab'; x.update(reading=r'\deleted{$\Rightarrow P\unsure{\leq|<|\preceq}$}',
                          alternatives=['<', r'\preceq'], confidence='medium')
    elif x['place'] == 'bottom construction abandoned parenthesized term':
        k = 'deleted_construction'; x.update(reading=new_old_term,
            alternatives=[r'F.G', r'F\times G', 'terminal mark: 2 or ?'], confidence='low')
    if k:
        x.update(reason=O[k][1], crop=evidence(k)['crop'])
    unresolved.append(x)
for place, reading, alternatives, k in [
    ('comment beside b), initial word', 'résulte', [], 'margin_b'),
    ('underlined starred gloss heading', 'explicitation', ['explication'], 'star_heading'),
    ('article immediately before sens', 'le', ['les'], 'le'),
    ('left oblique note connective after G-prime', 'avec', [], 'left_note'),
    ('left oblique note vertical relation from F to F-prime', r'\preceq', [r'\ll'], 'left_note'),
    ('bottom obligation b), cancelled verb', 'raffine', [], 'bottom_b'),
]:
    unresolved.append({'place': place, 'reading': reading, 'alternatives': alternatives,
                       'reason': O[k][1], 'confidence': O[k][2], 'crop': evidence(k)['crop']})

inventory = []
for old in rec['inventory']:
    x = dict(old)
    if x['element'] == 'comment on b':
        x['first_words_or_objects'] = r'(\unsure{résulte} de a), en regardant supports)'
    elif x['element'] == 'starred gloss heading':
        x['first_words_or_objects'] = r'* \unsure{explicitation|explication}, underlined'
    elif x['element'] == 'cancelled opening word':
        x['first_words_or_objects'] = r'\unsure{or|ces|ce}'
    elif x['element'] == 'cancelled i.e.':
        x.update(element='cancelled word after containment', first_words_or_objects=r'\unsure{bien|i.e.}')
    elif x['element'] == 'left note order arrangement':
        x['first_words_or_objects'] = r'G≤F, with F-prime below F and rotated \unsure{\preceq|\ll}'
    elif x['element'] == 'left note final short label':
        x['first_words_or_objects'] = r'\unsure{$C_3$.|Cor.|C6.}; separate line'
    elif x['element'] == 'right note revised implication':
        x['first_words_or_objects'] = r'old ⇒P\unsure{\leq|<|\preceq} between live P≤R and Q≤R'
    elif x['element'] == 'abandoned construction term':
        x['first_words_or_objects'] = r'(\unsure{F\setminus G|F.G|F\times G}\unsure{2|?}), heavily hatched'
    elif x['element'] == 'cancelled verb':
        x['first_words_or_objects'] = r'\unsure{raffine}'
    inventory.append(x)
inventory.append({'element': 'second-membership insertion leader', 'kind': 'drawing',
                  'position': 'centre, from comma after F.G down-left toward the inserted i.e.; [301,1158,1640,1352]',
                  'first_words_or_objects': 'thin headless curved attachment leader'})

changed_loci = [
    '030-006-certainty', '030-008-certainty', '030-010-alternatives', '030-012-alternatives',
    '030-025', '030-024-leader', '030-left-avec-certainty', '030-029-alternatives',
    '030-031', '030-right-b-relation-alternatives', '030-056', '030-044', '030-047-certainty',
]
assert len(changed_loci) == 13
before = p.read_text()
after = before
for e in edits:
    assert after.count(e['old']) == e.get('count', 1), (e['old'], after.count(e['old']))
    after = after.replace(e['old'], e['new'], e.get('count', 1))
assert old_member not in after and new_member in after
assert after.count(new_left_relation) == 1
assert r'G\arrow[r,phantom,"\leq" description]\arrow[d,phantom,"\rotatebox{90}{$\preceq$}" description]' in after

out = {
    'scan': 30, 'page_before_sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
    'edits': edits, 'decisions': decisions, 'record_updates': updates, 'new_changes': [],
    'unresolved_replace': unresolved, 'inventory_replace': inventory,
    'changed_loci': changed_loci,
    'notes_append': [
        'The blind audit restores the headless curved leader attaching the lower i.e. formula to membership in F.G; the formula, primes and phi empty-set notation remain unchanged. The cancelled word after the containment now prefers bien, with i.e. retained. The small terminal label of the left oblique note now prefers C-subscript3, with Cor./C6. retained: this is a visual preference from a low two-lobed curl, not an axiom identification imposed by the mathematics.',
        'The densely hatched old term in the bottom construction now prefers a parenthesized F-minus-G followed by a doubtful 2/question mark, with F.G and F-times-G alternatives. The additional turned mark remains visible before the closing parenthesis. This uncertain cancelled expression is preserved without repairing or using it in the live construction.',
        'The audit restores or expands local doubts in résulte, explicitation/explication, cancelled or/ces/ce, le/les, the oblique note’s avec and vertical subdivision/double-less-than sign, the old relation in marginal b, and cancelled raffine. The main C7 diagram retains its curved subdivision sign. The corollary underline includes the abbreviation’s stop. The two upper grouping strokes and lower stepped boundary remain as drawn.',
    ],
}
(r / 'second/scan030_adjudication_input.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(f'{len(decisions)} differing boxes recorded; {len(edits)} anchored edits; {len(changed_loci)} changed physical loci; audit not applied')
