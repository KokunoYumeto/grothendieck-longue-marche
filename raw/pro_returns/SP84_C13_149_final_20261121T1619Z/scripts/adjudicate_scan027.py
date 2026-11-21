"""One-use implementation of root's personally inspected scan027 choices.

This script serializes the authorized choices and reconciles metadata. It does
not inspect images, choose readings, alter frozen inputs, or compile TeX.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import csv
import hashlib
import json

from write_adjudications import write
from validate_audit_integrity import load_crop_rectangles, check_rectangle


ROOT = Path(__file__).resolve().parents[1]
STEM = '149_scan027'
REPORT = ROOT / f'reviews/{STEM}.json'
PAGE = ROOT / f'pages/{STEM}.tex'
CHOICES = ROOT / f'second/{STEM}_audit_choices.json'
DIRECTIVE = ROOT / f'documentation/{STEM}_audit_choices.json'
CHANGED = {'b05', 'b06', 'b14', 'b16', 'b17', 'b22', 'b25', 'b26'}


def rows(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert not CHOICES.exists(), 'One-use script: audit choices already exist.'
assert not (ROOT / f'second/{STEM}_adjudications.tsv').exists()
assert not (ROOT / 'documentation/scan027_implementation_reader_a.json').exists()
report_before = json.loads(REPORT.read_text())
assert report_before['root_approved'] and not report_before.get('audited')
assert len(report_before['changes']) == 35
report = copy.deepcopy(report_before)
page_before = PAGE.read_text()
page = page_before
directive_before = DIRECTIVE.read_bytes()
choices = json.loads(directive_before)
first = {x['box']: x['reading'] for x in rows(ROOT / f'second/{STEM}_first.tsv')}
second = {x['box']: x['reading'] for x in rows(ROOT / f'second/{STEM}_second.tsv')}
boxes = {x['box']: x for x in rows(ROOT / f'second/{STEM}_boxes.tsv')}
different = {x['box'] for x in rows(ROOT / f'second/{STEM}_token_differences.tsv')}
frozen_paths = [ROOT / f'second/{STEM}_{tail}' for tail in (
    'boxes.tsv', 'first.tsv', 'second.tsv', 'token_differences.tsv',
    'comparison_provenance.json', 'crop_manifest.tsv', 'second_notes.md')]
frozen_before = {str(p.relative_to(ROOT)): sha(p) for p in frozen_paths}
assert len(first) == 28 and len(different) == 24
assert set(choices) == different
assert {k for k, v in choices.items() if v['changed'] == 'yes'} == CHANGED
assert all(v['personally_inspected'] is True for v in choices.values())


def final(box):
    choice = choices[box]
    return (first[box] if choice['selection'] == 'first' else
            second[box] if choice['selection'] == 'second' else choice['final'])


def evidence_crop(box):
    return choices[box].get('crop', f'crops/{STEM}_second_{box}.png')


def evidence_box(box):
    return choices[box].get('pixel_box', [int(boxes[box][k]) for k in ('x0', 'y0', 'x1', 'y1')])


# Validate all extended evidence rectangles before any output is written.
known_rectangles = load_crop_rectangles(ROOT)
for box in choices:
    crop = evidence_crop(box)
    rectangle = evidence_box(box)
    assert (ROOT / crop).is_file(), crop
    check_rectangle(rectangle, f'{STEM}/{box}')
    assert crop in known_rectangles, crop
    assert tuple(rectangle) == known_rectangles[crop], (box, crop, rectangle)
assert evidence_box('b12') == evidence_box('b14') == [310, 925, 1635, 1220]
assert evidence_box('b15') == [310, 1225, 1635, 1440]


def replace_once(old, new):
    global page
    assert page.count(old) == 1, (old, page.count(old))
    page = page.replace(old, new, 1)


def unwrap_deleted(text):
    assert text.startswith(r'\deleted{') and text.endswith('}')
    return text[len(r'\deleted{'):-1]


# The displayed equation has display delimiters in the page and dollar
# delimiters in the frozen box. The lower box wrappers share one page-level
# deletion, so only their inner strings are substituted there.
assert first['b05'].startswith('$') and first['b05'].endswith('$')
replace_once(first['b05'][1:-1], final('b05')[1:-1])
for box in ('b06', 'b14', 'b16', 'b17'):
    replace_once(first[box], final(box))
for box in ('b22', 'b25', 'b26'):
    replace_once(unwrap_deleted(first[box]), unwrap_deleted(final(box)))

changes = {x['id']: x for x in report['changes']}


def update_change(id, box, reading, **extra):
    changes[id].update(final=reading, evidence=choices[box]['evidence'],
                       crop=evidence_crop(box), box=evidence_box(box), **extra)


update_change('c01', 'b02', changes['c01']['final'])
update_change('c02', 'b02', changes['c02']['final'])
update_change('c04', 'b05', final('b05')[1:-1], against_C=True, against_H=False)
changes['c04']['evidence'] += ' Witness flags in this row concern the generic argument letters; the operator insertion state is separately collated in c05.'
update_change('c06', 'b06', r'\unsure{\gamma|\sigma}', against_C=True, against_H=False)
update_change('c16', 'b16', r'\unsure{i.e|v.c}', confidence='medium')
changes['c16']['evidence'] += ' The new v.c alternative is certainty-only. This existing row remains a departure from both witnesses solely because both supply an unwritten terminal stop after their favored i.e; no additional witness count is added for the new doubt.'
update_change('c19', 'b17', 'envisagé', confidence='high')
update_change('c25', 'b22', r'\unsure{Je pense|Je ferai}', confidence='medium', against_C=True)
update_change('c31', 'b25', r'\unsure{convenable|connexe}', confidence='medium',
              against_C=True, against_H=False,
              place='Cancelled L21, final adjective and following punctuation',
              C='connexe,', H='convenable')
update_change('c33', 'b26', 'hyp ni ne modifie', against_C=True)


def add_change(id, box, place, c_reading, h_reading, reading, kind, category,
               confidence, mathematical=False):
    assert id not in changes
    item = dict(id=id, place=place, C=c_reading, H=h_reading, final=reading,
                evidence=choices[box]['evidence'], crop=evidence_crop(box),
                box=evidence_box(box), confidence=confidence,
                against_C=True, against_H=True, kind=kind,
                error_category=category, marked_in_H=False,
                mathematical=mathematical)
    report['changes'].append(item)
    changes[id] = item


add_change('c36', 'b14', 'L11, both function arguments in the inline pair',
           r"$\pi_1(j)$ et $\pi_1(j')$",
           r"$\pi_1(j)$ et $\pi_1(j')$",
           final('b14'), 'misread symbol or index', 'Symbols and indices',
           'medium', True)
add_change('c37', 'b17', 'NB margin, initial letter after the underlined heading',
           'ceci', 'ceci', 'Ceci', 'misread word', 'Words', 'high')
add_change('c38', 'b17', 'NB margin, group after correspondant',
           'à un', 'à un', r'\unsure{au|à un}', 'misread word', 'Words', 'medium')

for decision in report['decisions']:
    assert decision['id'] in ('M1054', 'M1055')
    decision['crop'] = evidence_crop('b02')
    decision['box'] = evidence_box('b02')
    if decision['id'] == 'M1054':
        assert decision['reading'] == "f'" and decision['decision'] == 'first'
        decision['evidence'] = "Root's full-formula audit b02 reaffirms the distinct raised prime after the tall stem and closed lower loop of f. It lies before the closing parenthesis. The neighboring later j forms are not used to normalize this first argument."
    else:
        assert decision['reading'] == '=' and decision['decision'] == 'first'
        decision['evidence'] = "Root's full-formula audit b02 reaffirms two live equality bars over older e/t strokes. The old conjunction remains separately deleted; its curved remnants are not an independent isomorphism wave."

new_doubts = []
for doubt in report['doubts']:
    place = doubt['place']
    if place == 'NB margin, word after ouvert':
        # The adjective has been resolved to envisagé by root. Its old
        # qualified arbitraire record is preserved in the implementation log.
        continue
    if place == 'Display L3, both argument letters':
        doubt.update(reading=r'\gamma', alternatives=[r'\sigma'],
                     reason=choices['b05']['evidence'])
    elif place == 'L4, argument before Im':
        doubt.update(reading=r'\gamma', alternatives=[r'\sigma'],
                     reason=choices['b06']['evidence'])
    elif place == 'Cancelled L19, first words':
        doubt.update(reading='Je pense', alternatives=['Je ferai'],
                     reason=choices['b22']['evidence'])
    elif place == 'Cancelled L21, punctuation after connexe':
        doubt.update(place='Cancelled L21, final adjective', reading='convenable',
                     alternatives=['connexe'], reason=choices['b25']['evidence'])
    new_doubts.append(doubt)
new_doubts.extend([
    dict(place='L11, both arguments in the inline fundamental-group pair',
         reading="$\\pi_1(f)$ et $\\pi_1(f')$",
         alternatives=["$\\pi_1(j)$ et $\\pi_1(j')$"], confidence='medium',
         reason=choices['b14']['evidence']),
    dict(place='L14, short form before u=0', reading='i.e', alternatives=['v.c'],
         confidence='medium', reason=choices['b16']['evidence']),
    dict(place='NB margin, group after correspondant', reading='au',
         alternatives=['à un'], confidence='medium', reason=choices['b17']['evidence']),
])
report['doubts'] = new_doubts

report['notes'][0] = 'Historical first-reading provenance: GPT-6 Astra Pro, effort not exposed, run SP84_C13_149. At that stage only scan027 packet, its source/halves, shared instructions and provided notation were consulted; no second-reading return, OCR, external research or TeX compilation was used. Later root adjudication and the explicitly non-independent consultations are recorded separately below.'
report['notes'][1] = 'Historical first-reading extent: one whole image for layout, both prepared full-resolution halves once line by line, followed by 23 saved enlarged crops. Existing saved crops were reused for unresolved NB punctuation and the short form before u=0. All agreed text, formula indices, underlines, deletion boundaries and insertion attachments were inspected. During the later audit, root added two original-pixel scope supplements for clipped b12/b14 and b15; their exact source rectangles are documented and used in the adjudications, without altering neutral boxes or frozen readings.'
report['notes'][3] = "The page converts the written equality of fundamental-group maps into a conjugation relation with inserted int(alpha), then states a reduction involving open U and translation parameter u. The displayed functions, named functions and final j=j' remain j forms; the intervening inline fundamental-group pair is f/f-prime favored under j/j-prime alternatives. The written concluding claim j=j' and u=0 is retained without repairing this local inconsistency. These statements were transcribed, not proved or otherwise checked."
report['notes'][4] = 'The NB margin begins with capital Ceci and says the reduction is no stronger than the corollary. It refers to a finite étale covering corresponding to a subgroup. The compressed group after correspondant favors au, with à un retained as an alternative. The adjective after ouvert is now resolved as envisagé: its own descending g loop and accented ending distinguish it from the superseded arbitraire proposal. The two terminal punctuation strokes remain qualified as . --.'
report['notes'][6] = "The bottom five-row paragraph is enclosed/cancelled with a frame and oblique strokes. It now starts with Je pense favored under the retained Je ferai alternative; the frame masks part of the distinguishing initial. The independently struck affaibli and généraliser/généralisé remain qualified. The complete final adjective of the reduction line favors convenable with connexe as an alternative; its high ending belongs to the word, so the former following comma/point qualification is removed. The next clause has undotted hyp before ni ne modifie. The faint final row ends at variété at the sheet edge; no continuation or terminal stop is supplied. H's explanatory continuation note is not source ink."
report['notes'][8] = "No expected mathematics settled a letter or supplied a connector. Gamma is now favored at the three matching generic-element occurrences by the two-arm/descending-loop comparison with scan013 c15, while sigma remains explicit. U, Y, the display/definition/closing j forms, opening f-prime, unprimed f in the label and translation parameter u are retained from their local forms. Only the two inline arguments retain f/j and f-prime/j-prime doubt. The first y map is headed without a left bar; the second has a definite left bar and uncertain right head; the Im map retains a shaft first with an arrowhead alternative."
report['notes'][9] = "Both packet marks, M1054 and M1055, remain resolved to their first alternatives after root's full opening-formula audit. The cancelled opening now favors Je pense rather than Je ferai, with both retained. Affaibli and généraliser/généralisé remain qualified. The former adjective doubt in the NB margin is resolved to envisagé; the former punctuation doubt after the lower adjective is removed because the supposed point lies inside the now-complete word extent."
report['notes'][10] = 'Witness counts follow favored readings. Reversing sigma/gamma, Je pense/Je ferai and convenable/connexe changes the relevant existing flags; removal of the lower hyp stop is recorded in the existing clause locus. The new inline f/j pair, capital Ceci and favored au each differ from both witnesses and receive substantive rows. Adding the v.c alternative to the already undotted i.e is certainty-only and adds no extra count. Its existing c16 remains a departure from both witnesses only for their supplied final dot. No added uncertainty alone is counted as a new witness correction.'
report['notes'][11] = 'The neutral audit boxes and their first-reading strings remain historical and frozen. They cover whole doubtful formulas, both margins, all additions and cancellations, all C/H different words, numbered pi occurrences, zero and both page/folio numbers. Final readings are in the adjudications. The original b12/b14 and b15 scopes clipped letter tops; the two saved supplements repair that evidence scope, with explicit original-pixel rectangles, without revising any frozen input.'
report['notes'].append('Independent audit: reader_c supplied the frozen second reading; root personally inspected all 24 differing boxes, the scope supplements and the specified original crops, and authorized the exact choices in documentation/149_scan027_audit_choices.json. Eight boxes change: b05, b06, b14, b16, b17, b22, b25 and b26. Reader_a serialized those choices without a new visual reading during implementation. The earlier reader_a function/Greek consultation and reader_c word/stop consultation are explicitly post-comparison and non-independent. Frozen inputs and the root choice directive remain unchanged.')

report['hand'][2]['consistency'] = 'All three occurrences match. Root compared their two upper arms and narrow descending loop with scan013 c15 gamma, favoring gamma while retaining sigma because no secure local sigma contrast was available.'
report['hand'][2]['misread'] = 'C gives sigma and H gamma; the final order is qualified gamma/sigma at all three occurrences.'
report['hand'][6]['consistency'] = 'The i.e/v.c short form has a central point and no final stop. Tjrs, OPS and the cancelled lower hyp are undotted. The opening hyp., rev., th. and cf. retain their independent written stops.'
report['hand'][6]['misread'] = 'Both witnesses add a terminal stop to i.e; C also supplies a stop to the cancelled lower hyp. H shortens the fully written étale to ét..'
report['hand'].extend([
    dict(habit='Closed lower loops can distinguish locally f-like function letters from open-hook j forms, but overlap with parentheses can prevent certainty.',
         pages=[27], consistency='Opening b02 favors f-prime. Display b05, the named pair and final equality have straight stems/open hooks. Only the b14 inline pair has closed loops without a securely independent crossbar; f/j alternatives remain there.',
         misread='Both witnesses give certain j/j-prime in the inline pair. Root retains f/f-prime first under explicit alternatives, without normalizing to the surrounding functions.'),
    dict(habit='A cancellation diagonal must not also be counted as an x, and the complete right-hand letter extent must precede any punctuation judgment.',
         pages=[27], consistency='The final adjective after non vide has a high doubled stem/loop and long return, favoring the b/l/e ending of convenable. Its compressed middle remains doubtful; the small dark mark lies before that high ending, not after the word.',
         misread='The first pass followed C connexe and qualified a following comma/point. Root now favors convenable with connexe retained and removes the misplaced punctuation.'),
])

report['notation'][2].update(rendering=r'\unsure{\gamma|\sigma}',
    evidence='Root adjudications b05/b06 and comparison with scan013 c15: two upper arms and a narrow descending closed loop favor gamma. Sigma remains an alternative because no secure local sigma comparator was available.')
report['notation'].append(dict(
    written='two closed-loop function arguments in the inline pair',
    rendering=final('b14'),
    meaning='The inline exterior-agreement pair as written; function identity remains locally uncertain.',
    evidence='Root adjudication b14, supplement original pixels (310,925,1635,1220): closed lower loops favor f/f-prime, but no independent crossbar is secure where parentheses overlap. Displayed, defined and closing j forms are unchanged.'))

assert report['abbreviations'][3]['form'] == 'i.e'
report['abbreviations'][3].update(form=r'\unsure{i.e|v.c}',
    expansion='id est for the favored i.e; alternative v.c not expanded',
    place='L14, before u=0; central point present, no terminal dot supplied')
assert report['abbreviations'][8]['form'] == 'hyp.'
report['abbreviations'][8].update(form='hyp', place='cancelled L22, without a terminal stop; distinct from opening L\'hyp.')

inventory = {x['element']: x for x in report['inventory']}
inventory['conjugation equation']['first_words_or_objects'] = r"\pi_1(j')(\unsure{\gamma|\sigma})"
inventory['NB note']['first_words_or_objects'] = r'\uline{NB} Ceci n\textquotesingle est'
inventory['boxed cancelled paragraph']['first_words_or_objects'] = r'\unsure{Je pense|Je ferai} d\textquotesingle ailleurs'

for coverage in report['diff_coverage']:
    row = coverage['row']
    if row == 6:
        coverage['reason'] = 'The first display argument now favors gamma with sigma retained, based on root comparison with the two-arm/descending-loop form in scan013 c15. The displayed function remains j-prime.'
    elif row == 8:
        coverage['reason'] = 'The second display argument matches the first and now carries gamma/sigma in that order. Operator insertion state remains separately c05.'
    elif row == 9:
        coverage['reason'] = 'The third generic letter before Im now favors gamma with sigma retained. Root inspected the whole formula; the labelled connector remains the qualified headless shaft in c07.'
    elif row == 17:
        coverage['reason'] = 'Final equation is u=0 with a real stop after zero. The short form is now unsure i.e/v.c without a terminal stop; c16 already records removal of the stop supplied by both witnesses, and the added alternative creates no extra witness count.'
    elif row == 19:
        coverage['reason'] = 'The extra adjective after ouvert is resolved as envisagé by its own g-descender loop and accented ending, against C omission and H donné. Independent audit also corrects agreed lowercase ceci and à un in separate new loci c37/c38.'
    elif row == 23:
        coverage['reason'] = 'Composite row: semicolon after arithmétique is c23; the Si-note separator/state is c24; the cancelled opening now favors Je pense with Je ferai retained in c25. H margin ordering remains editorial.'
    elif row == 28:
        coverage['reason'] = 'The full final adjective now favors convenable with connexe retained. Its high ending is part of the word and no detached punctuation follows it, so c31 includes removal of the former comma/point qualification. Ce qui ne détruit pas remains restored from the following row in c32.'
    elif row == 29:
        coverage['reason'] = 'The masked/omitted block reads undotted hyp ni ne modifie in c33, then la conclusion) OPS in c34. The lower hyp has no independent terminal dot; the opening hyp. remains unchanged. OPS is not expanded.'

report['metadata_corrections'].append(dict(
    reason='Root-authorized independent adjudication reconciled through the one-use scan027 implementation; complete before/after record history is preserved in documentation/scan027_implementation_reader_a.json. The three new substantive loci are c36–c38; historical first audit boxes and every frozen input remain unchanged.',
    directive='documentation/149_scan027_audit_choices.json'))

# Validate the concrete page and metadata before the first mutation.
assert len(report['changes']) == 38 and len(report['doubts']) == 12
assert len(report['decisions']) == 2 and len(report['diff_coverage']) == 30
assert len(report['inventory']) == len(report_before['inventory']) == 16
assert sum(x['against_C'] for x in report['changes']) == 20
assert sum(x['against_H'] for x in report['changes']) == 29
for field in ('checks', 'audit_boxes', 'root_reviewed_crops', 'reader', 'lines_read'):
    assert report[field] == report_before[field], field
assert final('b05')[1:-1] in page
for box in ('b06', 'b14', 'b16', 'b17'):
    assert final(box) in page
for box in ('b22', 'b25', 'b26'):
    assert unwrap_deleted(final(box)) in page
assert r"désignant par $j,j'$" in page and r"$j=j'$" in page
assert r"L'hyp." in page and 'les hyp ni ne modifie' in page
assert r'\unsure{,|.}' not in page and 'arbitraire' not in page
assert r'\prime' not in page and r'\unsure{\sigma|\gamma}' not in page
assert PAGE.read_text() == page_before and json.loads(REPORT.read_text()) == report_before
assert DIRECTIVE.read_bytes() == directive_before
assert frozen_before == {str(p.relative_to(ROOT)): sha(p) for p in frozen_paths}

CHOICES.write_bytes(directive_before)
write(27, CHOICES)
PAGE.write_text(page)
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
assert frozen_before == {str(p.relative_to(ROOT)): sha(p) for p in frozen_paths}
assert DIRECTIVE.read_bytes() == directive_before

history = []
for field in ('changes', 'decisions', 'doubts', 'notes', 'hand', 'notation',
              'abbreviations', 'inventory', 'diff_coverage', 'metadata_corrections'):
    before, after = report_before[field], report[field]
    for i in range(max(len(before), len(after))):
        old = before[i] if i < len(before) else None
        new = after[i] if i < len(after) else None
        if old != new:
            history.append(dict(record=f'{field}[{i}]', before=old, after=new))
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
counts = lambda value: dict(places=len(value['changes']),
    against_C=sum(bool(x['against_C']) for x in value['changes']),
    against_H=sum(bool(x['against_H']) for x in value['changes']))
log = dict(
    implemented_utc=now, implemented_by='reader_a', visual_adjudicator='root',
    independent_reader='reader_c', directive='documentation/149_scan027_audit_choices.json',
    directive_sha256=hashlib.sha256(directive_before).hexdigest(),
    postcomparison_consultations=['documentation/scan027_postcomparison_consultation_reader_a.md',
                                 'documentation/scan027_postcomparison_consultation.md'],
    changed_boxes=sorted(CHANGED), new_substantive_records=['c36', 'c37', 'c38'],
    counts_before=counts(report_before), counts_after=counts(report),
    page_before_sha256=hashlib.sha256(page_before.encode()).hexdigest(),
    page_after_sha256=sha(PAGE), history=history,
    validation=dict(frozen_inputs_unchanged=True, frozen_sha256=frozen_before,
                    root_directive_unchanged=True, no_new_visual_reading_during_implementation=True,
                    evidence_rectangles_verified=len(choices),
                    explicit_supplement_boxes={x:evidence_box(x) for x in ('b12','b14','b15')}))
(ROOT / 'documentation/scan027_implementation_reader_a.json').write_text(
    json.dumps(log, ensure_ascii=False, indent=2) + '\n')
(ROOT / 'documentation/scan027_implementation_reader_a.md').write_text(
    '# Scan027: implementation of root adjudication\n\n'
    f'Implemented: {now}. Visual adjudicator: root; serializer: reader_a; frozen independent reader: reader_c.\n\n'
    'The exact 24 choices in documentation/149_scan027_audit_choices.json were copied without alteration and serialized. Eight boxes change: b05, b06, b14, b16, b17, b22, b25 and b26. No new visual reading, OCR, external source, or TeX compilation was used during implementation. The two earlier consultations are explicitly post-comparison and non-independent.\n\n'
    'The Greek alternatives now favor gamma. Only the inline function pair favors f/f-prime under j/j-prime alternatives; displayed, named and closing j forms are retained. The short form is unsure i.e/v.c without a final dot. The NB note has capital Ceci, unsure au/à un, and resolved envisagé. The cancelled passage favors Je pense and convenable under retained alternatives, removes the misplaced punctuation after that adjective, and writes lower hyp without a stop. Opening hyp. remains unchanged.\n\n'
    'Three new substantive loci cover the inline function pair, note capitalization and note article. Existing records cover the other changes. The report now has 38 substantive places, 20 against C and 29 against H; the new i.e/v.c doubt does not create an extra count. Both mark decisions remain resolved. Twelve localized doubts remain.\n\n'
    'Neutral boxes, first/second returns, token differences, comparison provenance, crop manifest and second-reader notes remain byte-for-byte unchanged. The b12/b14 supplement uses original pixels (310,925,1635,1220), and b15 uses (310,1225,1635,1440), explicitly in the audit choices/adjudications. The complete before-and-after metadata history, page hashes and preserved-input hashes are in scan027_implementation_reader_a.json. No aggregate assembly was performed.\n')
print(json.dumps(dict(scan=27, choices=len(choices), changed_boxes=len(CHANGED),
    metadata_records_updated=len(history), counts=counts(report), frozen_inputs_unchanged=True)))
