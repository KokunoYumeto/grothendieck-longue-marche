"""One-use implementation of root's personally inspected scan025 decisions.

Reader B serializes the root decisions; no new image reading is made here.
Frozen first/second readings, neutral boxes and comparison inputs are checked
before and after.  The supplied witness texts are read only.  This script calls
the established adjudication writer and completion recorder, never assemble's
first-reading approval path.  Aggregate rebuilding is left to root.
"""
from pathlib import Path
from datetime import datetime, timezone
import copy
import csv
import hashlib
import json

from write_adjudications import write
from finish_audit import finish

R = Path(__file__).resolve().parents[1]
B = R.parent
STEM = '149_scan025'


def rows(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def differences(before, after, path=()):
    if type(before) is not type(after):
        return [{'path': list(path), 'before': before, 'after': after}]
    if isinstance(before, dict):
        out = []
        for key in before.keys() | after.keys():
            if key not in before or key not in after:
                out.append({'path': list(path + (key,)), 'before': before.get(key),
                            'after': after.get(key)})
            else:
                out.extend(differences(before[key], after[key], path + (key,)))
        return sorted(out, key=lambda x: repr(x['path']))
    if isinstance(before, list) and len(before) == len(after):
        return sum((differences(a, b, path + (i,))
                    for i, (a, b) in enumerate(zip(before, after))), [])
    return [] if before == after else [{'path': list(path), 'before': before, 'after': after}]


def counts(report):
    c = [x for x in report['changes'] if x['against_C'] or x['against_H']]
    return dict(places=len(c), against_C=sum(x['against_C'] for x in c),
                against_H=sum(x['against_H'] for x in c),
                **{level: sum(x['confidence'] == level for x in c)
                   for level in ['high', 'medium', 'low']})


page_path = R / f'pages/{STEM}.tex'
report_path = R / f'reviews/{STEM}.json'
choices_path = R / f'documentation/{STEM}_audit_choices.json'
log_path = R / f'documentation/{STEM}_audit_implementation.json'
assert not choices_path.exists() and not log_path.exists()
assert not (R / f'second/{STEM}_adjudications.tsv').exists()
report = json.loads(report_path.read_text())
assert report['root_approved'] and not report.get('audited')
original_report = copy.deepcopy(report)
page = original_page = page_path.read_text()
protected = sorted((R / 'second').glob(f'{STEM}_*'))
protected_hashes = {str(p.relative_to(R)): digest(p) for p in protected if p.is_file()}
first = {x['box']: x['reading'] for x in rows(R / f'second/{STEM}_first.tsv')}
second = {x['box']: x['reading'] for x in rows(R / f'second/{STEM}_second.tsv')}
boxes = {x['box']: x for x in rows(R / f'second/{STEM}_boxes.tsv')}
token_differences = rows(R / f'second/{STEM}_token_differences.tsv')
assert len(first) == 26 and len(token_differences) == 45

# Both actual witnesses supply a lowered 1 in the second action.
C = (B / 'source/SP84_C13_149_texts/pages/149_scan025.tex').read_text()
H = (B / 'source/SP84_C13_149_texts/hua/hua_149_scan025.tex').read_text()
C_pair = r'$\pi_1(f),\pi_1(g)$'
H_pair = r'$\pi_1(f), \pi_1(g)$'
assert C_pair in C and H_pair in H
choices = {}


def choose(key, evidence, final=None):
    choices[key] = dict(personally_inspected=True,
                        selection='first' if final is None else 'custom',
                        evidence=evidence, changed='no' if final is None else 'yes')
    if final is not None:
        choices[key]['final'] = final


choose('b01', 'The author number has a straight first upright, then a curved upper 2 with a flat foot. It reads 12. The two readings differ only by the manuscript-page macro, so retain the existing number and wrapper.')
choose('b02', 'The first pi has two legs and a roof plus a separate lowered 1 before (f). The second pi has only its two legs and roof immediately followed by the opening parenthesis of (g); no separate low 1 is present there. Both actual witnesses supplied that second 1. Remove only that unsupported index, retaining the comma and both arguments.', r'$\pi_1(f),\pi(g)$')
choose('b05', 'Before X there is one d ascender and one e under retracing, not two independently written de groups and not a separately cancelled additional de. Retain one live de. The opening and closing quotation marks are paired raised short ticks. The second reading changes quotation serialization and qualifies de without supplying contrary ink.')
choose('b06', 'The live word has one compact m/o/r prefix before the p descender and h; there is no additional h-o-m-o syllable sequence to support homomorphismes. The heavier initial traces are retracing, not a whole-word cancellation. Retain Les morphismes; 1 with its raised degree mark is the same source number in both serializations.')
choose('b08', 'The complete diagram has X, J and G, with two separately headed rightward arrows. The can label has no terminal stop; the phi label crosses the second shaft. A distinct comma follows G. The second reading uses inline arrow syntax for the same objects, heads, labels and punctuation, so retain the existing diagram macro.')
choose('b11', 'The item number is 2 with a raised degree mark. A straight cancellation crosses phi est; the live baseline then reads Un tel hom phi est. The second reading agrees with that cancellation and live text, changing only the degree-mark serialization.')
choose('b12', 'The H has a separate low 1, an empty first argument before the comma, and a double-stroked Z with lower ell in its second argument. The closing parenthesis is clear. No detached stop follows it; the next baseline starts capital Ce. The second reading selected only the formula inside the wider box, so its shorter scope does not remove the surrounding prose.')
choose('b13', 'Exactly three separate points follow denses. No closing parenthesis occurs after the third point. Literal three dots and the ellipsis macro encode the same marks, so retain the existing representation.')
relation = r'\unsure{\simeq|\overset{\sim}{\longrightarrow}}'
formula = r'H_{\unsure{1|n}}(X,\mathbb Z_\ell)' + relation + r'H_1(J,\mathbb Z_\ell)'
choose('b14', 'The relation has a clear upper wave and a long straight lower shaft. Its tiny upturned terminal does not securely distinguish a shaft from a separate arrowhead, so retain simeq first and allow an arrow with a tilde. The left H index remains a joined 1/n-like hump, unlike the separate clear right 1; the independent unqualified 1 does not settle that shape. The complete formula, parentheses, doubled Z and ell indices are retained. This adds relation uncertainty without changing the favored reading against either witness.', '3°) $' + formula + '$')
choose('b15', 'The cancellation leaves the l and e of le and an initial c visible. Its following medial/final letters are obscured by the strike. Retain deleted le with tentative cas; the independent c... records the same incomplete recovery rather than a secure competing word.')
choose('b16', 'The parenthesized par 3-degree is raised and has a curved attachment into the gap before que. Its endpoint belongs to the continuous leader, not to an extra comma. The degree-mark syntax is the only reading difference; retain the insertion and attachment.')
choose('b17', 'The upper H_1(f)=H_1(g) has separate clear 1 indices. In the lower equality, the left index joins directly to H and forms a complete low hump; nearby standalone 1 forms do not resolve whether this joined form is 1 or n. The right H_1(psi) has a clear separate 1. Retain the complete lower formula with localized 1/n uncertainty; the independent confident 1 does not erase the joined contour.')
choose('b18', 'The opening si has a separate i dot. Both compositions contain actual circles: f=phi circle can and g=psi circle can. The comma and closing parenthesis are distinct. The two serializations differ only in math scope and spacing; retain the same source text and formulas.')
choose('b19', 'The numeral is 2 followed by a raised degree mark and a separate closing parenthesis. The difference is degree-mark syntax only; retain par 2-degree-parenthesis.')
choose('b20', 'The left phi has its loop and stem. The right glyph has a middle stem rising above an open two-prong cup, comparable to the psi in the preceding g composition. Its curled right arm does not close into the phi loop. These visible strokes settle psi, independently of the expected conclusion. The equality has two bars and the following comma is separate. Resolve M1049 to its psi alternative.', r'$\varphi=\psi$,')
choose('b22', 'A tall b with its lower bowl survives the cancellation, and a separate right parenthesis is likewise crossed. The letters are sufficiently visible to retain deleted b) without extending the uncertainty to the parenthesis.')
state = r'\unsure{en|\deleted{en}|\deleted{si}}'
choose('b25', 'There is only one compact group between moins and la. A crossed little loop and following short point/return permit si as an alternative to en, while the live-versus-cancelled state remains open. Retain live en first, then cancelled en and cancelled si; do not add a second en unit. The following la, car. and 0 remain clear. Broadening the state/letter alternatives leaves the favored reading unchanged and adds no substantive against-C count.', '(du moins ' + state + r' la car. $0$')
assert set(choices) == {x['box'] for x in token_differences}
assert sum(x['changed'] == 'yes' for x in choices.values()) == 4

page_replacements = []
for key in ['b02', 'b14', 'b20', 'b25']:
    before, after = first[key], choices[key]['final']
    assert page.count(before) == 1, (key, before)
    page = page.replace(before, after, 1)
    page_replacements.append(dict(box=key, before=before, after=after))


def crop_fields(key):
    return dict(crop=f'crops/{STEM}_second_{key}.png',
                box=[int(boxes[key][c]) for c in ('x0', 'y0', 'x1', 'y1')])


def update_change(cid, key, **extra):
    item = next(x for x in report['changes'] if x['id'] == cid)
    item.update(evidence=choices[key]['evidence'], **crop_fields(key), **extra)


report['changes'].append(dict(
    id='audit_b02_pi_index', place='Opening line, second pi action before (g)',
    C=C_pair, H=H_pair, final=choices['b02']['final'],
    evidence=choices['b02']['evidence'], **crop_fields('b02'),
    confidence='high', against_C=True, against_H=True,
    kind='misread symbol or index', error_category='Symbols and indices',
    marked_in_H=False, mathematical=True,
    audit_first=first['b02'], audit_second=second['b02']))
update_change('c16', 'b20', final=r'$\varphi=\psi$', confidence='high',
              against_C=True, against_H=False,
              audit_first=first['b20'], audit_second=second['b20'])
update_change('c18', 'b25', final=state + r' la car. $0$',
              against_C=False, against_H=True,
              audit_first=first['b25'], audit_second=second['b25'])
for item in report['decisions']:
    if item['id'] == 'M1049':
        item.update(decision='alternative', reading=r'\psi', confidence='high',
                    evidence=choices['b20']['evidence'], **crop_fields('b20'))
    elif item['id'] == 'M1050':
        item.update(reading=state + ' la', evidence=choices['b25']['evidence'],
                    **crop_fields('b25'))

report['doubts'] = [x for x in report['doubts'] if 'M1049' not in x['place']]
for item in report['doubts']:
    if item['place'] == 'Main line 15, left H subscript in item 3':
        item.update(reading=formula, reason=choices['b14']['evidence'])
    elif 'M1050' in item['place']:
        item.update(reading=state + ' la', alternatives=['live en', r'\deleted{en}', r'\deleted{si}'],
                    reason=choices['b25']['evidence'])
    elif item['place'] == 'Main line 17, left H subscript before phi':
        item['reason'] = choices['b17']['evidence']
report['doubts'].append(dict(
    place='Main line 15, relation and terminal head in complete item 3 formula',
    reading=formula, alternatives=[r'\simeq', r'\overset{\sim}{\longrightarrow}'],
    confidence='medium', reason=choices['b14']['evidence']))
report.setdefault('resolved_observations', []).append(dict(
    place='Main line 18, M1049 right glyph in the complete equality',
    reading=r'\varphi=\psi', alternatives=[], confidence='high',
    reason=choices['b20']['evidence'], **crop_fields('b20')))

report['notes'][1] = 'S025.2 — The page proposes examining the induced actions of f and g on abelianized fundamental groups and their ell-adic components. The opening notation is literally pi_1(f), pi(g): the second pi has no separate lowered1. It states three facts involving a generalized Jacobian: factorization through can, determination of a group homomorphism from its action on H1 or ell-power torsion points, and a relation between the H groups of X and J whose small terminal head remains uncertain. This is a summary of the manuscript, not a proof check.'
report['notes'][2] = 'S025.3 — The deduction invokes items3 and2 and ends with equality of f and g. The independent audit resolves the intermediate equality to phi=psi from the right glyph’s open cup and central stem. The two joined left H subscripts remain1|n; no mathematical value has been used to force them. The relation in item3 now also retains simeq/arrow-with-tilde uncertainty. These doubts are localized and the complete affected formulas are retained.'
report['notes'][6] = 'S025.7 — After du moins there is only one compact group, favored as live en with cancelled en and cancelled si alternatives, then clear la car.0. Its letter and cancellation-state doubts do not support a second en. The source ellipsis consists of three points; no closing parenthesis follows it, and no opening parenthesis precedes the capital Ce.'
report['notes'][9] = 'Root approved the first transcription after personally inspecting c01–c20 and reviewing its records. At that stage the joined H indices and final phi/psi glyph remained doubtful. The subsequent independent audit resolves the latter to psi, while retaining both joined-index doubts and adding localized uncertainty to the item3 relation.'
report['notes'].append('Independent audit: /root/reader_b froze26 image-only box readings before comparison. Root personally inspected all17 differing boxes, covering45 token-difference spans, and changed4 boxes. The missing second pi index and resolved psi change favored readings; the item3 relation and the alternatives for the single group after du moins change certainty only. All frozen inputs remain unchanged. No new mathematical check event is asserted.')

for item in report['hand']:
    if item['habit'].startswith('Phi may'):
        item['habit'] = 'Local phi has a closed loop around its stem; psi has an open two-prong cup with a central upright.'
        item['consistency'] = 'The right glyph of the final phi=psi equality has the open cup and raised middle stem, matching psi in the preceding g composition. Its curled right arm does not close into a phi loop; this local contrast resolves M1049.'
        item['misread'] = 'C favors phi while allowing psi; H gives psi. Root’s independent-audit crop comparison selects psi.'
    if item['habit'].startswith('Thick retracing'):
        item['consistency'] = 'The compact morph- prefix is retraced but not cancelled, with no extra h-o-m-o syllables. The single group after du moins has genuine crossing/overlap and remains live en/cancelled en/cancelled si.'
report['hand'].append(dict(
    habit='The two legs of pi must be distinguished from a separate lowered index1.',
    pages=[25], consistency='The opening pi_1(f) has a distinct additional low1; the following pi(g) begins its parenthesis immediately after the two pi legs. Other clear pi_1 instances retain their indices.',
    misread='Both C and H supplied1 after the second opening pi; the frozen independent reading and root stroke comparison omit it.'))

for item in report['notation']:
    if item['written'] == 'π with subscript 1':
        item['written'] = 'π, with or without a separately written subscript1'
        item['rendering'] = r'\pi_1(f),\pi(g); \pi_1; \pi_1(G)'
        item['evidence'] = 'The first opening action has a separate low1. The second opening action has only the two pi legs followed immediately by (g), so its supplied1 is removed. The second-line group and lower pi_1(G) retain clear separate indices.'
    elif item['written'] == 'tilde over one horizontal stroke':
        item['rendering'] = relation
        item['evidence'] = choices['b14']['evidence']
report['notation'].append(dict(written='phi equals psi', rendering=r'\varphi=\psi',
    meaning='Intermediate equality in the deduction, read from the ink',
    evidence=choices['b20']['evidence']))
for item in report['inventory']:
    if item['element'] == 'e08':
        item['first_words_or_objects'] = '3°) $' + formula + '$'
    elif item['element'] == 'e15':
        item['first_words_or_objects'] = state
        item['position'] = 'main line22, one crowded word with unresolved letters and live/cancelled state'
for item in report['diff_coverage']:
    if item['row'] == 17:
        item['reason'] = 'Root audit resolves M1049 to psi: its open cup and raised central stem agree with H and reverse C’s favored phi. This remains one substantive place.'
    elif item['row'] == 19:
        item['reason'] = 'One group remains before clear la: favored live en with cancelled en/si alternatives. H’s extra split is unsupported. Broader uncertainty adds no new substantive count against C.'
report['notes'].append('Witness accounting: the shared C/H second pi index error was not a supplied C–H difference row, so it is added as audit_b02_pi_index with actual witness snippets. The20 original difference-coverage rows remain in their original order; c16 now counts against C only. Relation-head uncertainty is recorded in doubts and the audit table, without an additional substantive change row; c18 retains its existing H-only count for the unsupported split and omitted la.')

assert [x['row'] for x in report['diff_coverage']] == list(range(1, 21))
assert all(x['kind'] in {'misread word', 'misread symbol or index', 'omission',
 'text not on the page', 'deletion state', 'insertion or placement',
 'abbreviation expanded or spelling modernised', 'readable ink left as \\ill{}',
 'drawing or diagram', 'other'} for x in report['changes'])
choices_path.write_text(json.dumps(choices, ensure_ascii=False, indent=2) + '\n')
write(25, choices_path)
page_path.write_text(page)
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
finish(25, '/root/reader_b')
final_report = json.loads(report_path.read_text())
assert all(digest(R / path) == value for path, value in protected_hashes.items())
log = dict(completed_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
           authorization='Root supplied decisions after personally viewing all17 differing crops; implemented after CP05 packaging release.',
           page_replacements=page_replacements,
           report_edits=differences(original_report, final_report),
           before_counts=counts(original_report), after_counts=counts(final_report),
           protected_hashes=protected_hashes, protected_inputs_unchanged=True,
           boxes=26, differing_boxes=17, token_spans=45, changed_boxes=4,
           new_ink_reading_by_implementer=False, aggregate_rebuild_deferred_to_root=True)
log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'counts': log['after_counts'], 'frozen_inputs_unchanged': True,
                  'log': str(log_path.relative_to(R))}))
