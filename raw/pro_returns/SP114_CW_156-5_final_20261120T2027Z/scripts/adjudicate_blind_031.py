"""Prepare, without applying, the main reader's scan031 blind audit.

All readings, evidence and inspection times were supplied by the main reader
after reviewing the29 fresh differing crops. This script makes no visual choices
and preserves the primary page, adjudicated record and sealed TSVs.
"""
from pathlib import Path
import csv, hashlib, json

r = Path(__file__).resolve().parents[1]
p = r / 'pages/J156-5-04_156-5_scan031.tex'
rec = json.loads((r / 'review/scan031_adjudicated.json').read_text())
comp = json.loads((r / 'second/J156-5-04_156-5_scan031_comparison.json').read_text())
fresh = json.loads((r / 'second/J156-5-04_156-5_scan031_blind_notes.json').read_text())
crop_notes = {x['box']: x for x in fresh['boxes']}
with (r / 'second/J156-5-04_156-5_scan031_boxes.tsv').open(newline='') as f:
    boxes = {x['box']: x for x in csv.DictReader(f, delimiter='\t')}

old_elt = r'\unsure{élémt|élément|élt}'
raised_elt = r'\unsure{élémt|élém\textsuperscript{t}|élément|élt}'
last_elt = r'\unsure{élémt|élém|élément|élt}'
old_lens = r"l'ens $F^A$ des $B\in F$ tels que $A\subset B$"
new_lens = r'\inserted{' + old_lens + '}'
old_addition = r'\inserted{\unsure{a un plus petit}}'
new_addition = r'\margin{\deleted{\inserted{\unsure{a un plus petit|$=$ un plus petit}}}}'
old_R = r"\deleted{\unsure{$\mathcal R_{F'}$-satu.|$\mathscr R_{F'}$-satu.}}"
new_R = r"\deleted{\unsure{$\mathcal R_{F'}$-satu.|$\mathscr R_{F'}$-satu.|$Q_{F'}$-satu.|$\mathcal O_{F'}$-satu.}}"
old_evident_pair = r"C'est évident si $A\in F$ c'est évident. Si"
new_evident_pair = r"C'est \unsure{évident} si $A\in F$ c'est \unsure{évident}. Si"
edits = [
    {'old': r'\deleted{i.e.}', 'new': r'\deleted{\unsure{i.e.}}'},
    {'old': r'\deleted{\unsure{=|\supset}}', 'new': r'\deleted{\unsure{\supset|=}}'},
    {'old': '\\[\n |F\'|=|F|\n\\]', 'new': '\\[\n |F\'|\\unsure{=|\\supseteq}|F|\n\\]'},
    {'old': 'petit ' + old_elt + " de $F'$", 'new': 'petit ' + raised_elt + " de $F'$"},
    {'old': r'et \deleted{\unsure{B}} $x\in B$', 'new': r'et \deleted{$\unsure{B\supset|B}$} $x\in B$'},
    {'old': r'\deleted{$B$ contient}', 'new': r'\deleted{$B$ \unsure{contient}}'},
    {'old': "l'unique " + old_elt + ' $A$', 'new': "l'unique " + raised_elt + ' $A$'},
    {'old': r'\unsure{lui|le}', 'new': 'lui'},
    {'old': old_lens, 'new': new_lens},
    {'old': old_addition, 'new': new_addition},
    {'old': old_elt + r" de $F$. C'est évident", 'new': raised_elt + r" de $F$. C'est évident"},
    {'old': old_evident_pair, 'new': new_evident_pair},
    {'old': r"\deleted{\unsure{str.} de de $F'$ raffine $F$. Si}",
     'new': r"\deleted{\unsure{str.} de de $F'$ \unsure{raffine} $F$. Si}"},
    {'old': old_elt + ". C'est évident", 'new': last_elt + ". C'est évident"},
    {'old': old_R, 'new': new_R},
    {'old': r'i.e. réunion de strates', 'new': r'i.e. réunion \unsure{de|des} strates'},
    {'old': r'(et à fortiori de $F\setminus G$)', 'new': r'et à fortiori de $F\setminus G$)'},
]

def transform(s):
    for e in edits:
        s = s.replace(e['old'], e['new'])
    return s

# Keep marginpar outside sout: the source has one continuous cancellation, but
# its text is split into two wrapper spans around the marginal insertion.
cancel_first = next(x['first'] for x in comp if x['box'] == '031-B27')
cancel_transformed = transform(cancel_first)
before_addition, after_addition = cancel_transformed.split(new_addition)
assert before_addition.startswith(r'\deleted{') and after_addition.endswith('}')
split_cancel = (before_addition.rstrip() + '}\n'
                '% @ one continuous source cancellation; wrappers split only to place the cancelled insertion in the margin\n'
                + new_addition + '\n' + r'\deleted{' + after_addition.lstrip())
edits.append({'old': cancel_transformed, 'new': split_cancel})

O = {
    1: ('20:11:52', 'The first numeral has an open upper hook and a closed lower loop joining the following oval0. It is30, not80. Retain the manuscript folio independently of the scan number.', 'high'),
    2: ('20:11:52', 'The cancelled i.e. retains the i dot and punctuation stops, but the strike masks part of e; add doubt without changing its preferred letters. The plain F-prime and the cancelled support |F-prime|= are clear. The a) at the crop edge is not made doubtful merely because the excerpt clips its surroundings.', 'medium'),
    3: ('20:11:52', 'In the small cancelled relation, a right-hand curve joins the ends of two horizontal traces around a white counter, favouring superset over equals; the masked left side prevents complete resolution. Change the preferred old sign to superset and keep equals as the alternative. Both underbraces, their support labels, the union, bars, slant strokes and final live superset remain visible and unchanged.', 'low'),
    4: ('20:12:04', 'The standalone support relation has a short upper shaft with a downward hook and a separate lower stroke. Keep equals as preferred but admit superset-with-bar. No terminal point is supplied after the right support bar; the mathematical conclusion does not resolve the hooked form.', 'medium'),
    5: ('20:12:04', 'The short final t-like stroke is close to the baseline and connected to the low m run, though a slightly raised t is possible. Preserve élémt first and add the raised-t form alongside élément/élt; do not expand the word by grammar.', 'medium'),
    6: ('20:12:04', 'Immediately after G-prime, the densely blackened diamond or obliterated tiny circle differs from an ordinary punctuation dot. Retain its cancelled doubtful circle. At the right of the first A exponent, an additional old parenthesis/question-like hook remains under the curve; the blind excerpt drops that ink. Keep both old marks and the clear live circle/G-prime exponent.', 'low'),
    7: ('20:12:18', 'Under the cancellation, the B has two loop remnants and a separate right-facing curve or shaft after it. Preserve that additional sign as a doubtful superset after B, with B alone retained as the alternative. The following x-in-B stays live.', 'low'),
    8: ('20:12:18', 'The cancelled B is followed by a c-like start and a terminal t, while the middle letters of contient are crossed through; retain contient with doubt. The nonempty-intersection sign has an oval on a long stem, so retain phi rather than the blind slashed-circle normalization. The wider excerpt includes the old B-plus-relation already adjudicated in B07.', 'medium'),
    9: ('20:12:18', 'The small thick exponent has a pale centre but is not a perfectly resolved circle. Retain circle, bullet and star alternatives. The inclusion, following B and bare OK are clear; the blind longer excerpt merely adds the already-transcribed donc.', 'medium'),
    10: ('20:12:34', 'Curved old G strokes remain beneath the live F in the support, and two older B loops are overwritten by the angular live A before membership. Keep both doubtful old letters and live A/F. The blind reading would omit or change their recorded state.', 'low'),
    11: ('20:12:34', 'The short élément form has the low connected medial run and a small final t-like rise. As at the first occurrence, retain baseline élémt first and add the raised-t alternative without resolving the spelling as a full word.', 'medium'),
    12: ('20:12:34', 'The cancelled initial si has a dot and s-like loop; x is masked, while membership and A remain visible. Retain doubt around the whole old phrase. The following lui is resolved from its own crop, not inferred from the cancellation or expected syntax.', 'low'),
    13: ('20:12:45', 'A tall looped l, low u shoulder and a separate dotted short upright establish lui. Resolve the previous lui/le doubt to lui and preserve c’est lui plus petit exactly, without adding le or grammatical linking words.', 'high'),
    14: ('20:17:54', 'The tight crop, confirmed against the wide B28 crop, shows one C-shaped initial e flowing into t. The clear space before that e contains no separate opening parenthesis. Omit the supplied opening parenthesis, retain et à fortiori de F-minus-G in place after él. de F, and preserve the visible closing parenthesis before qui.', 'high'),
    15: ('20:12:45', 'The verb contient, following x, comma and OK with its exclamation are present. The difference between OK~! and OK ! is only TeX spacing; keep the first reading.', 'high'),
    16: ('20:12:57', 'The raised replacement shows the s/u/b/d/v/i/s/e sequence sufficiently clearly to retain subdivise without a new doubt. The old raffine remains doubtful beneath its strike. No separate old word is inserted: the neighbouring long strokes belong to the f descenders.', 'high'),
    17: ('20:12:57', 'After the tall l, the adverb runs into a long flat stroke and terminal t without a separate -ement sequence. Retain seult as preferred and seulement as an unresolved alternative, rather than adopt the blind expansion.', 'medium'),
    18: ('20:12:57', 'The old first word has a q bowl and descender followed by low u/e, supporting que rather than pour. The old tout has a tall first t and terminal t, but its middle is masked, so retain its doubt. The second que is live; the additional blind A-subset-B material belongs to the cancelled passage below and is already transcribed there.', 'medium'),
    19: ('20:13:10', 'The cancelled initial sign has the V-like legs and crossbar of forall, not four letters Soit. A-in-F-prime and doubtful et occupy the lower baseline. The l’ens F-superscript-A des B-in-F tels que A-subset-B clause is visibly raised above the subsequent est contenu dans line, so mark the entire clause inserted after et while retaining the outer cancellation. The verbal phrase remains doubtful as est contenu dans/contienne.', 'high'),
    20: ('20:13:10', 'The small left addition sits to the left of1-degree and above the abbreviated élément line. Its initial closed oval favours a; there is no separate vertical stroke, while two horizontal edges leave equals as an alternative. Preserve a un plus petit first, record = un plus petit, and mark its marginal placement within the insertion and enclosing cancellation.', 'medium'),
    21: ('20:13:38', 'The third short élément form again permits a slightly raised t, added as an alternative to the existing baseline preference. Both cancelled occurrences of évident retain their visible ends but have their middle letter bodies masked by strikes; add doubt to each. Preserve the duplicated C’est évident si A-in-F c’est évident. Si sequence rather than streamline it.', 'low'),
    22: ('20:13:38', 'The beginning has a curved s, t ascender, r-like return and stop, followed by two separate de loops before F-prime. Retain doubtful str. and both de groups, rather than replace them with illegible. The later raffine retains its double-f loops, but the middle and ending are masked; add doubt to that verb.', 'medium'),
    23: ('20:13:56', 'The cancelled initial symbol again has the legs and crossbar of forall, not Soit. A thick older internal stroke remains under the live A in the set predicate, so retain the doubtful old B. The l’ens wording without a point, braces, separator bar, membership and subset signs are visible. The blind longer context does not erase those old strokes.', 'high'),
    24: ('20:13:56', 'The fourth live short élément form ends in a tiny upturn which may be t but has no secure crossbar. Keep élémt first and add élém as an alternative, with the separate full stop outside the doubt. The entire old (B=A), including its parentheses, is cancelled; the separate live (on prend B=A) is retained below it.', 'medium'),
    25: ('20:14:06', 'The old capital exposes an upper/lower loop and diagonal foot favouring R, while the strike still admits Q or script O. Retain the script-R candidates first and add those alternatives. In the following abbreviation only one high ascender corresponding to t is secure; no separate b/l pair establishes stable, so keep satu. The clear above-line fermé dans F-prime replaces the whole cancelled expression.', 'low'),
    26: ('20:14:06', 'The2-degree label, primes and intersection signs are clear. In the first i.e. réunion de strates phrase, the small d loop and short terminal hook cannot exclude a final s; preserve de with des as an alternative. The later réunion de strates de G-prime remains unchanged. The closed paired angles in G-prime double-less-than F are retained. The final audit excerpt includes this changed first article, beyond the shorter sealed first excerpt.', 'medium'),
    27: ('20:14:30', 'The whole cancelled area confirms the raised l’ens clause, the left-margin a/equals un plus petit insertion, both crossed évident occurrences and the third abbreviated élément. Retain the doubtful et and cancelled forall that the blind reading drops or calls Soit. The lower str. fragment belongs to the adjoining cancelled line; all its recovered text is preserved. Apply the separately recorded local changes without counting this overlapping box as an additional physical locus.', 'medium'),
    28: ('20:17:45', 'The wide context confirms the separate dotted upright of lui and the blank space before the single e-to-t stroke of et à fortiori. No opening parenthesis is present there, whereas a closing one follows F-minus-G. Retain lui, omit the supplied opener, preserve the unmatched closer and leave the source syntax c’est lui plus petit unrepaired.', 'high'),
    29: ('20:17:45', 'The wider b heading confirms the legible inserted subdivise, the doubtful cancelled raffine, the short seult/seulement alternative and deleted que tout with its second live que. The apparent extra old material before the adverb consists of descenders from the prior-line word. No additional change is made in this overlapping context.', 'high'),
}

def ev(k):
    key = f'031-B{k:02}'
    b, f = boxes[key], crop_notes[key]
    co = [int(b[z]) for z in ('x0', 'y0', 'x1', 'y1')]
    assert co == [f['source_coordinates'][z] for z in ('x0', 'y0', 'x1', 'y1')]
    crop = f['crop_path'].removeprefix('deliverable/')
    assert (r / crop).is_file(), crop
    return {'evidence': O[k][1], 'crop': crop, 'box': co,
            'rotation': f['rotation_degrees_counterclockwise'],
            'main_decision': 'Main-reader decision after independent blind reading; see first/second/final audit.'}

before = p.read_text()
after = before
for e in edits:
    assert after.count(e['old']) == e.get('count', 1), (e['old'], after.count(e['old']))
    after = after.replace(e['old'], e['new'], e.get('count', 1))
assert after.count(raised_elt) == 3
assert after.count(last_elt) == 1
assert after.count(r'\unsure{évident}') == 2
assert r"réunion de strates de $G'$" in after
assert r"c'est lui plus petit él. de $F$ et à fortiori de $F\setminus G$)" in after

decisions = []
for x in comp:
    assert x['different']
    k = int(x['box'][-2:])
    final = transform(x['first'])
    if k == 20:
        final = new_addition
    if k == 26:
        # This sealed excerpt stops at A-cap-B, although the crop includes the
        # article decision. Extend the final excerpt with existing page text.
        final = after.split('% @ bottom, second condition\n', 1)[1].strip()
    decisions.append({'box': x['box'], 'changed': final != x['first'],
                      'final': final, 'evidence': O[k][1], 'confidence': O[k][2],
                      'crop': ev(k)['crop'], 'rotation_degrees': ev(k)['rotation'],
                      'viewed_utc': f'2026-11-20 {O[k][0]} UTC'})
assert len(decisions) == 29

updates = []
def up(id, k, **fields):
    updates.append({'id': id, 'fields': {**fields, **ev(k)}})

up('031-03', 3, final=r'\deleted{\unsure{\supset|=}}', confidence='low', against_C=True, against_H=True)
up('031-04', 4, final='no point', confidence='high')
up('031-05', 5, final=raised_elt, confidence='medium')
up('031-08', 7, final=r'\deleted{$\unsure{B\supset|B}$}', confidence='low', against_C=True, against_H=True)
up('031-13', 11, final=raised_elt, confidence='medium')
up('031-15', 13, final='lui', confidence='high', against_C=True, against_H=False)
up('031-16', 14, final=r'et à fortiori de $F\setminus G$)', confidence='high', against_C=True, against_H=True)
up('031-25', 19, final=r"$A\in F'$, \unsure{et}", confidence='medium', against_C=False, against_H=True)
up('031-26', 19, final="l'ens", confidence='high')
up('031-28', 20, final=new_addition, confidence='medium', against_C=True, against_H=True)
up('031-29', 21, final=raised_elt, confidence='low')
up('031-30', 22, final=r'\unsure{str.} de de', confidence='medium')
up('031-34', 24, final=last_elt, confidence='medium')
up('031-35', 25, final=new_R.removeprefix(r'\deleted{')[:-1], confidence='low', against_C=False, against_H=True)

new_changes = [{
    'id': '031-BL01', 'place': 'cancelled attempt, raised l’ens clause after et',
    'C': old_lens + ' (ordinary continuation within deletion)',
    'H': r"l'ens. $F^{A}$ des $B\in F$ tels que $A\subset B$ (ordinary cancelled text, reordered)",
    'final': new_lens, 'confidence': 'high', 'kind': 'insertion or placement',
    'against_C': True, 'against_H': True, 'H_marked': False,
    'certainty_only': False, 'consequential': True, **ev(19),
}]

unresolved = []
for old in rec['unresolved']:
    x = dict(old)
    k = None
    if x['place'] == 'case 2 c’est word':
        continue
    if x['place'] == 'support display cancelled relation':
        k = 3; x.update(reading=r'\supset', alternatives=['='])
    elif x['place'] == 'introductory argument élément word':
        k = 5; x.update(alternatives=[r'élém\textsuperscript{t}', 'élément', 'élt'])
    elif x['place'] == 'case 2 l’unique élément word':
        k = 11; x.update(alternatives=[r'élém\textsuperscript{t}', 'élément', 'élt'])
    elif x['place'] == 'cancelled attempt élément word':
        k = 21; x.update(alternatives=[r'élém\textsuperscript{t}', 'élément', 'élt'])
    elif x['place'] == 'restated condition 1 élément word':
        k = 24; x.update(alternatives=['élém', 'élément', 'élt'])
    elif x['place'] == 'case 1 cancelled capital before x in B':
        k = 7; x.update(reading=r'B\supset', alternatives=['B'])
    elif x['place'] == 'cancelled slanted insertion':
        k = 20; x.update(reading='a un plus petit', alternatives=[r'$=$ un plus petit'])
    elif x['place'] == 'final cancelled adjective':
        k = 25; x.update(reading=r"$\mathcal R_{F'}$-satu.", alternatives=[r"$\mathscr R_{F'}$-satu.", r"$Q_{F'}$-satu.", r"$\mathcal O_{F'}$-satu."])
    if k:
        x.update(reason=O[k][1], confidence=O[k][2], crop=ev(k)['crop'])
    unresolved.append(x)
for place, reading, alternatives, k in [
    ('opening cancelled abbreviation', 'i.e.', [], 2),
    ('standalone support equality, relation', '=', [r'\supseteq'], 4),
    ('case 1 cancelled verb after B', 'contient', [], 8),
    ('cancelled attempt, first évident', 'évident', [], 21),
    ('cancelled attempt, second évident', 'évident', [], 21),
    ('cancelled str. fragment, verb after F-prime', 'raffine', [], 22),
    ('first i.e. réunion de strates phrase, article', 'de', ['des'], 26),
]:
    unresolved.append({'place': place, 'reading': reading, 'alternatives': alternatives,
                       'reason': O[k][1], 'confidence': O[k][2], 'crop': ev(k)['crop']})

inventory = []
for old in rec['inventory']:
    x = dict(old)
    key = x['element']
    if key == 'support equality':
        x['first_words_or_objects'] = r"|F'|\unsure{=|\supseteq}|F|"
    elif key == '031-S01':
        x['first_words_or_objects'] = r'\unsure{i.e.}'
    elif key == '031-S03':
        x['first_words_or_objects'] = r'\unsure{\supset|=}'
    elif key == '031-S06':
        x['first_words_or_objects'] = r'$\unsure{B\supset|B}$'
    elif key == '031-S07':
        x['first_words_or_objects'] = r'$B$ \unsure{contient}'
    elif key == '031-S10':
        x['position'] = {**x['position'], 'attachment': 'Live c’est lui follows; lui resolved in blind audit.'}
    elif key == '031-S16':
        x['first_words_or_objects'] = r'\margin{\unsure{a un plus petit|$=$ un plus petit}}'
        x['position'] = {'box': ev(20)['box'], 'attachment': 'Left marginal insertion inside the cancelled block, above the élément line and left of its 1-degree label.'}
    elif key == '031-S17':
        x['first_words_or_objects'] = r"\unsure{str.} de de $F'$ \unsure{raffine} $F$. Si"
    elif key == '031-S21':
        x['first_words_or_objects'] = new_R.removeprefix(r'\deleted{')[:-1]
    inventory.append(x)
inventory.extend([
    {'element': '031-BL-I01', 'kind': 'insertion', 'position': {'box': ev(19)['box'], 'attachment': 'Raised above the est contenu dans line; attaches after doubtful et and remains within the outer deletion.'}, 'first_words_or_objects': old_lens, 'hand': 'his hand'},
    {'element': '031-BL-I02', 'kind': 'margin note', 'position': {'box': ev(20)['box'], 'attachment': 'Left of the cancelled 1-degree/élément lines, simultaneously marginal, inserted and cancelled.'}, 'first_words_or_objects': r'\unsure{a un plus petit|$=$ un plus petit}', 'hand': 'his hand'},
])

notes = list(rec['notes'])
notes[3] = 'In the second case the blind audit resolves the dotted ending as “c’est lui plus petit él. de F”; le and any supplied qui est are excluded. After él. de F, the ink reads “et à fortiori de F\\setminus G)” with a closing parenthesis but no opening parenthesis. The missing opener is not supplied for grammatical balance. H’s cf. définition and its reordered qui est are unsupported. The first three compressed élément forms retain a possible raised t; the fourth admits a terminal-free élém alternative. The two de-like groups in the cancelled lower line remain.'
notes[4] = 'The isolated support equality retains = as preferred but now admits superset-with-bar because the short upper shaft hooks downward; the support conclusion does not decide its shape. The earlier cancelled relation prefers superset with equals as alternative. The slanted a un plus petit addition is marginal, inserted and subsequently cancelled, with = un plus petit as an alternative. The l’ens clause is also raised and is marked inserted within the cancellation. The final crossed script-R adjective retains R as preferred with Q/O alternatives and is replaced above by fermé dans F-prime. The state and placement of these additions are recorded separately from their uncertain words.'
notes.append('The blind audit adds a doubtful superset after the old B in case1; it also restores local uncertainty in opening i.e., cancelled contient, both cancelled évident occurrences, the lower cancelled raffine and the first de/des before strates. The repeated évident sequence and the later plain de before strates de G-prime remain. The live argument and its conditional support check are not strengthened by these visual decisions.')

abbreviations = []
for old in rec.get('abbreviations', []):
    x = dict(old)
    if x['written'] == 'i.e.':
        x['certainty'] = 'opening cancelled occurrence doubtful; live final occurrence clear'
    elif x['written'] == 'élémt / élt / élément':
        x['written'] = r'élémt / élém\textsuperscript{t} / élém / élt / élément'
        x['certainty'] = 'first three allow a raised t; fourth allows élém; do not expand in text'
    abbreviations.append(x)
habits = []
for old in rec.get('hand_habits', []):
    x = dict(old)
    if x['habit'].startswith('The upper stroke of ='):
        x['witness_effect'] = 'Equals remains preferred at the standalone support relation, but the blind audit retains superset-with-bar as an alternative; the b-heading equality is unchanged.'
    elif x['habit'].startswith('The middle of élément'):
        x['witness_effect'] = 'No expansion; first three short forms permit a raised t, while the fourth permits a terminal-free élém. Seult retains its existing alternative.'
    habits.append(x)

changed_loci = [
    '031-opening-ie-certainty', '031-03', '031-support-equality-alternative',
    '031-05-raised-t-alternative', '031-08', '031-case1-contient-certainty',
    '031-13-raised-t-alternative', '031-15-resolved', '031-BL01', '031-28',
    '031-29-raised-t-alternative', '031-cancelled-evident-first', '031-cancelled-evident-second',
    '031-cancelled-fragment-raffine', '031-34-terminal-alternative', '031-35-capital-alternatives',
    '031-first-de-des-alternative', '031-16-opening-parenthesis',
]
assert len(changed_loci) == 18
out = {
    'scan': 31, 'page_before_sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
    'edits': edits, 'decisions': decisions, 'record_updates': updates, 'new_changes': new_changes,
    'unresolved_replace': unresolved, 'inventory_replace': inventory, 'notes_replace': notes,
    'abbreviations_replace': abbreviations, 'hand_habits_replace': habits,
    'changed_loci': changed_loci,
}
(r / 'second/scan031_adjudication_input.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(f'{len(decisions)} differing boxes recorded; {len(edits)} anchored edits; {len(changed_loci)} changed physical loci; audit not applied')
