"""One-use implementation of root's approved scan026 visual adjudication.

Root personally inspected all nineteen differing boxes. Reader C entered these
decisions after the explicitly non-independent consultation documented alongside
them. This script does not choose readings or alter frozen comparison inputs.
"""
from pathlib import Path
import csv
import hashlib
import json
import re


ROOT = Path(__file__).resolve().parents[1]
STEM = '149_scan026'
REPORT_PATH = ROOT / f'reviews/{STEM}.json'
PAGE_PATH = ROOT / f'pages/{STEM}.tex'
CHOICES_PATH = ROOT / f'documentation/{STEM}_audit_choices.json'


def rows(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


report = json.loads(REPORT_PATH.read_text())
assert report['root_approved'] and not report.get('audited')
assert not CHOICES_PATH.exists(), 'Do not rerun an entered root adjudication.'
assert not (ROOT / f'second/{STEM}_adjudications.tsv').exists()
assert (ROOT / 'documentation/scan026_postcomparison_consultation.md').is_file()
provenance_path = ROOT / f'second/{STEM}_comparison_provenance.json'
provenance = json.loads(provenance_path.read_text())
frozen_paths = [ROOT / f'second/{STEM}_{kind}.tsv'
                for kind in ('boxes', 'first', 'second', 'token_differences')]
frozen_paths.append(provenance_path)
before_hashes = {str(p.relative_to(ROOT)): digest(p) for p in frozen_paths}
for kind, expected in provenance['sha256'].items():
    assert digest(ROOT / f'second/{STEM}_{kind}.tsv') == expected

first = {x['box']: x['reading'] for x in rows(ROOT / f'second/{STEM}_first.tsv')}
second = {x['box']: x['reading'] for x in rows(ROOT / f'second/{STEM}_second.tsv')}
different = {x['box'] for x in rows(ROOT / f'second/{STEM}_token_differences.tsv')}
boxes = {x['box']: x for x in report['audit_boxes']}
choices = {}


def choose(box, evidence, final=None):
    item = {'personally_inspected': True, 'adjudicator': '/root',
            'entered_by': '/root/reader_c',
            'selection': 'first' if final is None else 'custom',
            'evidence': evidence, 'changed': 'no' if final is None else 'yes'}
    if final is not None:
        item['final'] = final
    choices[box] = item


choose('b01', 'The initial C in the surrounding Cette is a tall open capital, already retained in the page. The adjective has its u/x run, dotted i and accent position in deuxième; the small marks do not form a separate 3 or 2. The second reading includes the opening parenthesis and cette as additional scope. Retain the first target reading and the existing capital Cette in its context.')
choose('b02', 'The cancelled opening retains the p descender and terminal r of tentative pour, but the central letters are obscured. The complete Y, G and Z formula and où G est were checked. Between G and Z is one local oblique; the apparent other arm belongs to the long cancellation, so retain backslash. In the finite-subgroup sign, one short horizontal and the upright are independent; an apparent second horizontal coincides with the strike, leaving +1/not-equal 1 unresolved. The live replacement deux applications constantes de X dans Y is inserted and not struck, with its terminal exclamation. The closing parenthesis belongs to the surrounding paragraph outside that insertion.')
choose('b03', 'The raised phrase has two short equality bars, G, a single backslash, Z, the comma and où G est. The apparent crossing arm comes from the long cancelling stroke rather than a multiplication sign. The nested first macros preserve both the raised insertion and its subsequent cancellation. Reversing the nested wrappers is a representation difference here, not a different source reading.')
choose('b04', 'The map i:Y-to-G has a definite right head with two converging components. The brace-like insertion leader has its cusp after baseline bien and before dans; it does not supply parentheses. The independent target omits the surrounding baseline words as scope. Retain the first attachment and baseline bien/dans.')

final6 = first['b06'].replace(r'\unsure{tout}', r'\unsure{tout|faut}')
choose('b06', 'Under the cancellation the initial tall stroke with a low hook can be t or f. The compressed middle joins do not securely distinguish ou from au, so broaden tout to tout/faut while keeping tout first. Donc remains cancelled. The raised D’autre part is a live insertion with its separate comma; neither the insertion nor its comma is absorbed into the cancellation.', final6)

choose('b07', 'The long strike crosses Quitte à remplacer. The following f and comma are live; only g has its own local cancellation. The predicate ends in a low open return after t, supporting dominante without a separate s. These words sit on the main baseline and are not a wholesale insertion. Retain the first reading and correction scope.')
choose('b08', 'The first open-set capital has heavy overlaid strokes and an internal return that permit V or W. No independent cancellation and replacement chronology can be separated, so do not reconstruct deleted V plus inserted W. Non vide is raised, with a curved leader attaching before the capital. The subset sign and Y are clear; retain V/W uncertainty and the first insertion scope.')
choose('b09', 'The beginning reads on aura donc. The initial open loop and low arch of on provide a comparison for b15. The heavily retraced capital still permits V/W without a separable old/new chronology. The plus is distinct; u has an open valley rather than a closed bowl. The subset, Y and terminal point are clear. Retain the first reading.')
choose('b11', 'The live upper V is a clear chevron over a thin rightward return. These traces do not recover a separate older U or establish a replacement. The lower g(U) subset V is crossed by the long strike. No independent comma follows it. Retain the first live/cancelled formulas and punctuation.')
choose('b12', 'The long cancellation masks part of donc qui; the q descender, short u and i dot support tentative qui without making every letter plain. The isolated Q-like loop has a diagonal tail but remains crossed and uncertain. The following quitte is live and lies beyond the first target scope. That added second-reader context changes no page reading.')
choose('b14', 'The f remains live; the comma and g are cancelled together. Envoie ends in a horizontal returning stroke after the low e, without an additional n body and independent upright t for envoient. The alternative placement of math delimiters around comma/g does not change the ink. Retain the first reading.')

final15 = first['b15'].replace(', et ', r', \unsure{on|et|ou} ')
choose('b15', 'The compressed connector begins with a tiny open loop and continues into a long low arch with a descending return. It resembles on in b09, while no distinct t upright or cross-stroke can be isolated. Preserve on/et/ou with on favored. The whole formula retains clear V+u subset Y, its comma, the literal g-circle-i order, tau with open u subscript, the second i-circle-f and its closing parenthesis and point.', final15)

choose('b16', 'The hooked initial s, i dot and t stem survive under the cancellation, but the a region is covered. Sait therefore remains tentative. The raised voit is clear and live, with its insertion state retained. The second reading’s unqualified sait is too definite.')

fragment = r'\unsure{\deleted{def.}|def.}'
final17 = first['b17'].replace(r'\deleted{$\unsure{f}$}', fragment)
choose('b17', 'After est there are two distinct tall uprights, a rounded left base and a right return, with a separate terminal point. The medial e is crowded, but the extent supports tentative def. rather than a single f. No independent accent is secure, so none is supplied. A rising diagonal crosses the bodies but joins a large letter return below est; its independence as cancellation remains unsettled. Retain cancelled def. first and live def. as the alternative. The existing f-prime, colon, X, uncertain shaft/head and literal U remain unchanged. The second reading’s opening (où is context outside the first target scope.', final17)

choose('b18', 'The map’s right end is a cap without a separable two-branch fork; retain the head/shaft uncertainty. The domain is the literal curved U, not V. The j, colon, Y, est l’inclusion and actual closing parenthesis remain intact.')
choose('b20', 'All three pi_1 objects have clear numeric 1 indices and arguments X, U, Y. The first shaft ends in a tiny cap only, so its head remains uncertain; the second has a large two-arm right head. The labels are pi_1(f-prime) and pi_1(j), with the prime separate. The first diagram encoding preserves these distinctions; ordinary arrows in the second reading would remove the first head doubt.')
choose('b21', 'The two shafts end in small caps without securely separated pointed heads, so both head doubts remain. All pi_1 indices and the X/U/Y objects are clear. The second label has upper overtracing compatible with j-prime or g-prime; no old/new letter chronology can be separated. The locally defined map favors j-prime, but the ink leaves the alternative open. Retain the first label order, its separate prime, the preceding prose and the diagram encoding.')

final22 = first['b22'].replace(r'\deleted{\unsure{j}}', r'\deleted{\unsure{j|g}}')
choose('b22', 'The cancelled glyph retains a lower j-like hook, but crossing strokes obscure the upper bowl or dot region and do not exclude g. Add g as an alternative while retaining j first. The later live j-prime has its own prime and is followed by the colon, literal U, the unchanged uncertain shaft/head and Y. Do not transfer the cancellation to that live map.', final22)

choose('b24', 'The small thin 25 at the lower left has a curved2 and a5 with its short upper bar and lower bowl. Its scale and thin stroke distinguish this foliation hand from the principal writing. Retain the margin convention; mspage would misattribute it as the author’s page numbering.')

assert set(choices) == different
changed_boxes = {k for k, x in choices.items() if x['changed'] == 'yes'}
assert changed_boxes == {'b06', 'b15', 'b17', 'b22'}
assert len(choices) == 19

page = PAGE_PATH.read_text()
for key in ('b06', 'b15', 'b17', 'b22'):
    assert page.count(first[key]) == 1, (key, 'old reading not unique')
    page = page.replace(first[key], choices[key]['final'], 1)
    boxes[key]['reading'] = choices[key]['final']

changes = {x['id']: x for x in report['changes']}


def update_change(change_id, box_id, final, **extra):
    item = changes[change_id]
    box = boxes[box_id]
    item.update(final=final, evidence=choices[box_id]['evidence'],
                crop=f'crops/{STEM}_second_{box_id}.png',
                box=[box[k] for k in ('x0', 'y0', 'x1', 'y1')],
                audit_first=first[box_id], audit_second=second[box_id], **extra)


update_change('c11', 'b06', r'\deleted{Donc \unsure{tout|faut}}',
              confidence='low', against_C=False, against_H=True)
update_change('c22', 'b15', r'\unsure{on|et|ou}',
              confidence='low', against_C=True, against_H=True)
update_change('c25', 'b17', fragment,
              place="Short fragment after f':X–U est; deletion state uncertain",
              confidence='low', against_C=True, against_H=True, kind='deletion state')
update_change('c30', 'b22', r'\deleted{\unsure{j|g}}',
              confidence='low', against_C=False, against_H=True)

decisions = {x['id']: x for x in report['decisions']}
decisions['M1051']['evidence'] = choices['b08']['evidence']
decisions['M1052']['evidence'] = choices['b09']['evidence']
decisions['M1053']['evidence'] = choices['b21']['evidence']

for item in report['doubts']:
    if item['place'] == 'After cancelled Donc':
        item.update(reading=r'\unsure{tout|faut}', alternatives=['tout', 'faut'],
                    reason=choices['b06']['evidence'])
    elif item['place'] == 'Cancelled glyph following est':
        item.update(place='Short fragment following est; reading and deletion state',
                    reading=fragment, alternatives=[r'\deleted{def.}', 'def.'],
                    reason=choices['b17']['evidence'])
    elif item['place'] == 'Final cancelled glyph':
        item.update(reading=r'\deleted{\unsure{j|g}}', alternatives=['j', 'g'],
                    reason=choices['b22']['evidence'])
    elif item['place'] == 'First open-set capital':
        item['reason'] = choices['b08']['evidence']
    elif item['place'] == 'Second open-set capital':
        item['reason'] = choices['b09']['evidence']
    elif item['place'] == 'Second diagram, second label':
        item['reason'] = choices['b21']['evidence']
report['doubts'].append({'place': 'Connector before the later g-circle-i equality',
                       'reading': r'\unsure{on|et|ou}',
                       'alternatives': ['on', 'et', 'ou'], 'confidence': 'low',
                       'reason': choices['b15']['evidence']})

report['notes'][4] = ('The first equality literally has (ig), with no composition circle, whereas its right-hand i-circle-f has a clear ring. The later equality literally uses g-circle-i. Its preceding connector is now on/et/ou uncertain, with on favored by the low-loop/arch comparison in b09. Neither formula order has been corrected from mathematical expectation.')
report['notes'][9] = ('The cancelled words tout/faut, donc qui and sait remain qualified where the strike hides letters. The final cancelled glyph is j/g uncertain. After the f-prime map’s est, the fragment is tentatively def., with both cancelled and live states preserved because the oblique crossing meets a large letter return. No accent is supplied; the possible expansion défini belongs only in the abbreviation list. The top cancelled pour remains qualified. Broadening tout and j without changing their favored readings adds no separate substantive count against C.')
report['notes'].append('Independent audit: root personally inspected all 19 differing boxes and approved changes in b06, b15, b17 and b22. Reader C supplied a separately documented post-comparison consultation for the connector and def. fragment, using b09 as the requested local comparison; this was not a second frozen independent read. The first and second TSVs, neutral boxes and comparison provenance remain unchanged. Current report audit-box readings follow the adopted text; the original first readings remain in the frozen first TSV. No mathematical assertion was proof-checked during this adjudication.')

for item in report['hand']:
    if item['habit'].startswith('Very compressed prose'):
        item['consistency'] = ('Visible in on aura donc and est ramené. The short connector before the later equality has the same low loop and arch as on, but remains on/et/ou uncertain because its letters are compressed. Cancellation also leaves tout/faut and sait unresolved; baseline non vide is separately clear.')
        item['misread'] = ('H leaves on aura donc unreadable, substitutes se ramène, and reads baseline non vide as inserted dense. C gives et and H où for the later flattened connector; the favored on differs from both.')
    elif item['habit'].startswith('Retraced V-like'):
        item['consistency'] = ('The first two open-set capitals are heavily retraced; the later V in V+u is clear. No separate cancellation/replacement chronology or uniform resolution is imposed.')

for item in report['notation']:
    if item['written'] == r'g\circ i=\tau_u(i\circ f)':
        item['evidence'] = ('c15 and independent b15 show g, separate circle and i in that literal order; tau has open u, and both right-hand letters, their circle, the parentheses and point are present. Only the preceding prose connector changes to on/et/ou uncertainty.')
    elif item['written'] == r"\pi_1(f'),\pi_1(j),\pi_1(\unsure{j'|g'})":
        item['evidence'] = ('c19–c20 and audit b20–b21 show the primes separately. The final j-prime/g-prime label retains upper overtracing without a recoverable old/new chronology; the nearby defined map favors j-prime but does not remove the ink doubt.')

assert not any(x['form'] == 'def.' for x in report['abbreviations'])
report['abbreviations'].append({'form': 'def.', 'expansion': 'possibly défini',
                               'place': 'after est in the f-prime map clause; the short form and its deletion state remain tentative, and no accent is supplied in the transcription'})

for item in report['inventory']:
    if item['element'] == 'Cancelled inference opening':
        item['first_words_or_objects'] = r'Donc \unsure{tout|faut}'
    elif item['element'] == 'Cancelled glyph after est':
        item.update(element='Fragment after est, deletion state uncertain',
                    first_words_or_objects=fragment)
    elif item['element'] == 'Final cancelled j-like glyph':
        item.update(element='Final cancelled j/g-like glyph',
                    first_words_or_objects=r'\unsure{j|g}')

for item in report['diff_coverage']:
    if item.get('change_id') in ('c11', 'c22', 'c25', 'c30'):
        item['reason'] = changes[item['change_id']]['evidence']

report['root_review_note'] += (' Independent adjudication: root personally inspected every differing box. The approved changes are tout/faut, on/et/ou, unaccented def. with uncertain deletion state, and cancelled j/g. Other formula, letter, number and correction-state readings remain as explicitly adjudicated. No new interpretation was selected by the implementing script.')
report['root_audit_reviewed_crops'] = [f'crops/{STEM}_second_{k}.png' for k in choices]

# Check only this approved page and report before writing. There is no TeX build.
assert len(report['changes']) == 33
assert sum(bool(x['against_C']) for x in report['changes']) == 15
assert sum(bool(x['against_H']) for x in report['changes']) == 28
assert len(report['doubts']) == 18
assert [x['row'] for x in report['diff_coverage']] == list(range(1, 44))
assert [x['id'] for x in report['decisions']] == ['M1051', 'M1052', 'M1053']
assert all(x['transcribed'] == 'yes' for x in report['inventory'])
assert all(x['kind'] in ('text', 'display', 'diagram', 'drawing', 'margin note', 'insertion', 'deletion') for x in report['inventory'])
assert r'\prime' not in page
assert r'\deleted{$\unsure{f}$}' not in page
assert r'\unsure{\deleted{def.}|def.}' in page
assert r'\unsure{on|et|ou}' in page
clean = '\n'.join(re.split(r'(?<!\\)%', line)[0] for line in page.splitlines())
depth = 0
for token in re.findall(r'\\[{}]|[{}]', clean):
    if token == '{':
        depth += 1
    elif token == '}':
        depth -= 1
    assert depth >= 0
assert depth == 0
assert len(re.findall(r'(?<!\\)\$', clean)) % 2 == 0
for key, item in choices.items():
    assert (ROOT / f'crops/{STEM}_second_{key}.png').is_file()
    if item['changed'] == 'yes':
        assert item['final'] in page

CHOICES_PATH.write_text(json.dumps(choices, ensure_ascii=False, indent=2) + '\n')
PAGE_PATH.write_text(page)
REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
assert {str(p.relative_to(ROOT)): digest(p) for p in frozen_paths} == before_hashes
print(json.dumps({'scan': 26, 'differing_boxes': len(choices),
                  'changed_boxes': sorted(changed_boxes), 'changes': len(report['changes']),
                  'against_C': 15, 'against_H': 28, 'doubts': len(report['doubts']),
                  'frozen_inputs_unchanged': True}))
