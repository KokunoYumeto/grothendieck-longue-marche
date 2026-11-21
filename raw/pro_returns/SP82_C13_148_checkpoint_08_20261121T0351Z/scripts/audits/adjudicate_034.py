#!/usr/bin/env python3
"""Mechanically apply root's complete scan034 audit once, with --apply.

Root personally viewed all48 differing fixed crops and announced completion.
This script grew from a read-only box/page/review mapping scaffold. It makes
no image judgment, mathematical check, TeX compilation, audit recording,
shared-log change, or rebuild. Locked evidence TSVs remain byte-identical.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import re

B = Path(__file__).resolve().parents[2]
STEM = B / 'second/148_scan034'
PAGE = B / 'pages/148_scan034.tex'
REVIEW = B / 'reviews/148_scan034.json'
WORKING = Path(str(STEM) + '_root_working.json')
ADJUDICATIONS = Path(str(STEM) + '_adjudications.json')
EXPECTED_DIFFERENCES = 48
ROOT_ANNOUNCED_COMPLETE = True

# Existing C/H row indices are descriptive links, not new reading decisions.
# Several crop boxes share one existing composite witness difference.
CH_ROWS = {
    'top_number': [],
    'title_abbrev': [0],
    'title_cancel': [],
    'title_alg': [1],
    'title_characteristic': [],
    'definition_count': [],
    'definition_autom': [2],
    'definition_G': [3],
    'definition_identity': [],
    'cancelled_order': [],
    'max_autom': [4],
    'cancelled_order5': [5],
    'cancelled_ilest': [6],
    'order_condition': [6],
    'quotient_display': [],
    'operation_note': [7],
    'case1_number_order': [],
    'case1_orbit': [8],
    'case1_action': [],
    'case1_autom_D5': [9, 10],
    'case1_isom': [11],
    'pentagon_note': [12],
    'sphere5': [13],
    'case2_number_order': [],
    'case2_deleted': [14],
    'case2_replacement': [],
    'case2_mu4': [],
    'case2_relative_action': [15],
    'case2_pole': [16],
    'case2_group': [17, 18],
    'square_note': [19],
    'sphere4': [20],
    'case3_number_order_Alors': [21],
    'case3_deleted_symbol': [22],
    'case3_fixed_count': [],
    'case3_donc': [23],
    'case3_I': [24],
    'case3_J': [25],
    'case3_est': [25],
    'case3_struck_group': [26],
    'case3_replacement': [27, 28],
    'case3_colon': [29],
    'case3_Ens_count': [30],
    'association_A': [31],
    'association_deleted_symbol': [32],
    'association_inclusion': [],
    'association_ens': [33],
    'association_pour': [34],
    'association_1to1': [],
    'ending_omega': [35],
    'ending_field': [],
    'ending_group': [36],
    'partition_note': [37, 38],
    'bitetrahedron_note': [],
    'sphere3': [39],
    'folio': [40],
}
MARKS = {
    'title_characteristic': ['M0448'],
    'case2_pole': ['M0449'],
    'case3_replacement': ['M0450'],
    'association_inclusion': ['M0451'],
    'association_pour': ['M0452'],
    'ending_field': ['M0453'],
    'partition_note': ['M0454', 'M0455', 'M0456'],
}
UNRESOLVED = {
    'title_cancel': ['title, cancelled courbe'],
    'title_characteristic': ['title, characteristic phrase'],
    'cancelled_order5': ['cancelled order-5 group, initial stroke'],
    'cancelled_ilest': ['cancelled il est'],
    'case2_deleted': ['case 2, cancelled initial letter'],
    'case2_pole': ['case 2, pole symbol'],
    'case3_deleted_symbol': ['case 3, cancelled initial symbol'],
    'association_deleted_symbol': ['association, cancelled symbol after Sigma_J'],
    'association_inclusion': ['association, inclusion formula exponent'],
    'ending_field': ['ending, field letter'],
    'partition_note': [
        'third margin, initial word', 'third margin, word before ou symétries'],
}
SPHERE_KEYS = ('sphere5', 'sphere4', 'sphere3')
CONTEXTS = {
    'definition_autom': ('un ', ' non trivial'),
    'max_autom': ('tout ', ' d’ordre fini'),
    'case2_mu4': ('OPS que c’est ', ', sur lequel'),
}


def key(short):
    return '148034_' + short


def short(box):
    assert box.startswith('148034_')
    return box[len('148034_'):]


def read_tsv(suffix):
    with Path(str(STEM) + suffix).open() as handle:
        rows = list(csv.DictReader(handle, delimiter='\t'))
    assert len({r['box'] for r in rows}) == len(rows)
    return {r['box']: r for r in rows}


def once(text, old, new):
    assert text.count(old) == 1, (old[:120], text.count(old))
    return text.replace(old, new, 1)


def locate_first(box, reading, page):
    """Resolve original page spans, including wrapper/context exceptions."""
    name = short(box)
    if name == 'quotient_display':
        assert reading.startswith(r'\(') and reading.endswith(r'\)')
        body = reading[2:-2]
        assert page.count(body) == 1
        start = page.index(body)
        return start, start + len(body), 'display-formula body'
    if name in CONTEXTS:
        before, after = CONTEXTS[name]
        anchored = before + reading + after
        assert page.count(anchored) == 1, box
        start = page.index(anchored) + len(before)
        return start, start + len(reading), 'explicit surrounding text'
    assert page.count(reading) == 1, (box, page.count(reading))
    start = page.index(reading)
    return start, start + len(reading), 'literal unique occurrence'


def stage_page_replacements(page, mapping, finals):
    """Future edit utility; descending original spans avoid changed anchors.

    This function returns a string only and is never called by scaffold mode.
    It must receive complete root-approved finals, not partial working entries.
    """
    operations = []
    for box, final in finals.items():
        entry = mapping[box]
        if entry['location_method'] == 'display-formula body':
            assert final.startswith(r'\(') and final.endswith(r'\)')
            final = final[2:-2]
        operations.append((entry['start'], entry['end'], final, box))
    ordered = sorted(operations)
    for left, right in zip(ordered, ordered[1:]):
        assert left[1] <= right[0], (left[3], right[3])
    result = page
    for start, end, final, box in reversed(ordered):
        result = result[:start] + final + result[end:]
    return result


def crop_metadata(box, boxes):
    row = boxes[box]
    return dict(
        crop=f'crops/second/148_scan034/{box}.png',
        box=[int(row[k]) for k in ('x0', 'y0', 'x1', 'y1')])


def source_picture_metadata(reading):
    marker = r'\begin{tikzpicture}'
    if marker not in reading:
        return None
    header = reading[reading.index(marker):].split('\n', 1)[0]
    clip = re.search(r'\\clip \(0,0\) rectangle \(([^)]+)\);', reading)
    return dict(
        header=header, clip_extent=clip.group(1) if clip else None,
        commands=len(re.findall(r'\\(?:draw|fill|node|foreach)\b', reading)))


def load_state():
    page = PAGE.read_text()
    review = json.loads(REVIEW.read_text())
    comp = read_tsv('_comparison.tsv')
    first = read_tsv('_first.tsv')
    second = read_tsv('_second.tsv')
    boxes = read_tsv('_boxes.tsv')
    working = json.loads(WORKING.read_text())
    assert len(comp) == 56
    assert {short(k) for k in comp} == set(CH_ROWS)
    assert set(comp) == set(first) == set(second) == set(boxes)
    assert all(comp[k]['first'] == first[k]['reading'] for k in comp)
    assert all(comp[k]['second'] == second[k]['reading'] for k in comp)
    differences = {k for k, r in comp.items() if r['different'] == 'yes'}
    assert len(differences) == EXPECTED_DIFFERENCES
    assert {e['box'] for e in working} <= differences
    assert len({e['box'] for e in working}) == len(working)
    assert len(review['changes']) == 41
    known_marks = {m['id'] for m in review['decisions']}
    assert {m for ids in MARKS.values() for m in ids} == known_marks
    known_doubts = {u['place'] for u in review['unresolved']}
    assert {u for places in UNRESOLVED.values() for u in places} == known_doubts

    mapping = {}
    for box, row in comp.items():
        start, end, method = locate_first(box, row['first'], page)
        name = short(box)
        mapping[box] = dict(
            different=row['different'] == 'yes',
            start=start, end=end,
            page_line=page.count('\n', 0, start) + 1,
            exact_first_matches=page.count(row['first']),
            location_method=method,
            change_rows=[
                dict(index=i, place=review['changes'][i]['place'])
                for i in CH_ROWS[name]],
            marks=MARKS.get(name, []),
            unresolved_places=UNRESOLVED.get(name, []),
            second_picture=source_picture_metadata(row['second']),
            **crop_metadata(box, boxes))
        assert (B / mapping[box]['crop']).is_file()
    ordered = sorted((m['start'], m['end'], k) for k, m in mapping.items())
    overlaps = [(a[2], b[2]) for a, b in zip(ordered, ordered[1:])
                if a[1] > b[0]]
    assert not overlaps, overlaps
    assert {r['index'] for m in mapping.values() for r in m['change_rows']} == set(range(41))
    return dict(page=page, review=review, comparison=comp, boxes=boxes,
                working=working, differences=differences, mapping=mapping)


def require_complete_root_decisions(state):
    """Completion in a JSON file alone is not root's explicit go-ahead."""
    assert ROOT_ANNOUNCED_COMPLETE, 'Root has not announced the audit complete.'
    entries = state['working']
    assert len(entries) == EXPECTED_DIFFERENCES
    assert {e['box'] for e in entries} == state['differences']
    assert all(e['viewed_by_main'] is True for e in entries)
    assert all(e['choice'] in ('first', 'second', 'revised') for e in entries)
    assert not ADJUDICATIONS.exists()
    assert not state['review'].get('second_audit')


def tikz_body(reading):
    picture = reading[reading.index(r'\begin{tikzpicture}'):]
    return picture.split('\n', 1)[1].rsplit(r'\end{tikzpicture}', 1)[0].strip()


def commands(body):
    return [part.strip() + ';' for part in body.split(';') if part.strip()]


def take_command(parts, start):
    hits = [c for c in parts if c.startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]


def figure(parts, units):
    return '\n'.join([
        r'\figure{\begin{tikzpicture}[' + units
        + ',line cap=round,line join=round]',
        *parts, r'\end{tikzpicture}}',
    ])


def apply_completed(state):
    require_complete_root_decisions(state)
    p = state['review']
    comp = state['comparison']
    original = state['page']
    root = {e['box']: e for e in state['working']}
    assert len(root) == 48
    assert sum(e['choice'] == 'revised' for e in root.values()) == 22
    locked = [Path(str(STEM) + s) for s in
              ('_first.tsv', '_second.tsv', '_boxes.tsv',
               '_comparison.tsv', '_token_differences.tsv')]
    hashes = {str(f): hashlib.sha256(f.read_bytes()).hexdigest() for f in locked}
    original_checks = json.dumps(p['checks'], ensure_ascii=False, sort_keys=True)
    original_second_boxes = json.dumps(p['second_boxes'], ensure_ascii=False, sort_keys=True)
    finals = {}

    def revise_text(name, old, new):
        finals[key(name)] = once(comp[key(name)]['first'], old, new)

    revise_text('title_characteristic', r'\unsure{de car. \(0\)}',
                r'\unsure{de} car. \(0\)')
    revise_text('definition_count', r'\operatorname{card}K=5',
                r'\operatorname{Card}K=5')
    revise_text('definition_identity', r'à \(1\)', r'\unsure{à|;} \(1\)')
    revise_text('cancelled_order5', r'\unsure{\nu}', r'\unsure{\forall|\nu}')

    operation = once(comp[key('operation_note')]['first'], 'est celle',
                     r'\unsure{est celle|usuelle}')
    operation = once(operation, r'\widehat{\mathbb G}_m',
                     r'\widehat{\mathbb G_m}')
    finals[key('operation_note')] = operation

    d5_commands = commands(tikz_body(comp[key('case1_autom_D5')]['second']))
    d5_loop = take_command(d5_commands, r'\draw[line width=.5pt] (375,30)')
    d5_inline = '\n'.join([
        r'\tikz[baseline=(d.base),x=.007cm,y=-.007cm,line cap=round,line join=round]{',
        r'\node (d) at (421,66) {$\mathbb D_5$};',
        d5_loop, '}',
    ])
    old_d5_inline = comp[key('case1_autom_D5')]['first'][len('autom. est '):]
    assert old_d5_inline.startswith(r'\tikz')
    finals[key('case1_autom_D5')] = 'autom. est ' + d5_inline
    revise_text('case1_isom', 'À isom. près', 'À isom près')
    revise_text('pentagon_note', 'pentagonale',
                r'\unsure{pentagon.le|pentagonale}')

    sphere5 = once(
        comp[key('sphere5')]['first'],
        r'\draw (.41,.14)--(.44,.12);',
        r'\draw (.38,.10)--(.42,.11)--(.44,.07);' + '\n'
        + r'\draw (.43,0)--(.43,-.03);')
    finals[key('sphere5')] = sphere5

    cancelled_case2 = r'\deleted{\(K=\operatorname{Card}I^g=1\)}'
    finals[key('case2_deleted')] = cancelled_case2
    revise_text('case2_pole', r'\unsure{\infty}', r'\unsure{\infty|0}')
    revise_text('case2_group', 'autom. est ', 'autom est ')

    sphere4_commands = commands(tikz_body(comp[key('sphere4')]['second']))
    omit4 = [
        r'\clip (0,0)', r'\fill (111,0)',
        r'\draw[line width=.6pt] (172,189)',
    ]
    for prefix in omit4:
        take_command(sphere4_commands, prefix)
    sphere4_commands = [
        c for c in sphere4_commands if not any(c.startswith(s) for s in omit4)]
    for i, c in enumerate(sphere4_commands):
        if c.startswith(r'\draw[line width=.75pt]'):
            c = c.replace('line width=.75pt', 'line width=.35pt', 1)
        elif c.startswith(r'\draw[line width=.8pt]'):
            c = c.replace('line width=.8pt', 'line width=.4pt', 1)
        elif c.startswith((r'\draw[line width=.5pt]', r'\draw[line width=.45pt]')):
            c = re.sub(r'line width=[.0-9]+pt', 'line width=.25pt', c, count=1)
        elif c.startswith(r'\fill (133,78)'):
            c = c.replace('radius=.5pt', 'radius=.425pt')
        elif c.startswith(r'\fill'):
            c = re.sub(r'radius=[.0-9]+pt', 'radius=1.275pt', c, count=1)
        else:
            raise AssertionError(c)
        sphere4_commands[i] = c
    first_fill4 = next(i for i, c in enumerate(sphere4_commands) if c.startswith(r'\fill'))
    sphere4_commands.insert(
        first_fill4, r'\draw[line width=.35pt] (67,79)--(61,86);')
    finals[key('sphere4')] = figure(sphere4_commands, 'x=.0075cm,y=-.00818cm')

    revise_text('case3_deleted_symbol', r'\unsure{\Sigma|K}',
                r'\unsure{\Sigma|K}_{\unsure{2}}')
    revise_text('case3_fixed_count', r'\operatorname{card}K^g=2',
                r'\operatorname{Card}K^g=2')
    revise_text('case3_donc', r'\inserted{donc \(K^g=\Sigma^g\)}',
                r'\inserted{donc \(K^g=\Sigma^g\),}')
    revise_text('case3_struck_group', r'\deleted{Le groupe total est}',
                r'\deleted{Le groupe \unsure{total est|des auto}}')
    revise_text('case3_Ens_count', r'de card \(3\)', r'de Card \(3\)')
    revise_text('association_deleted_symbol',
                r'\deleted{\unsure{\Sigma}}',
                r'\unsure{\deleted{\Sigma}|\deleted{g}\Omega|\deleted{G}\Omega}')
    revise_text('ending_omega', r'\omega(I)', r'\omega(\unsure{I|J})')
    finals[key('partition_note')] = (
        r'\unsure{Partition|Une partition} \(2\) et \(3\) '
        r'(par ordre de richesse en symétries)')

    sphere3_commands = commands(tikz_body(comp[key('sphere3')]['second']))
    take_command(sphere3_commands, r'\clip (0,0)')
    sphere3_commands = [c for c in sphere3_commands if not c.startswith(r'\clip')]
    for i, c in enumerate(sphere3_commands):
        if c.startswith(r'\draw[line width=.75pt]'):
            c = c.replace('line width=.75pt', 'line width=.35pt', 1)
        elif c.startswith(r'\draw[line width=.8pt]'):
            c = c.replace('line width=.8pt', 'line width=.4pt', 1)
        elif c.startswith(r'\draw'):
            c = re.sub(r'line width=[.0-9]+pt', 'line width=.25pt', c, count=1)
        elif c.startswith(r'\fill') and 'circle' in c:
            c = re.sub(r'radius=[.0-9]+pt', 'radius=1.275pt', c, count=1)
        elif c.startswith(r'\fill') and 'ellipse' in c:
            c = once(c, 'x radius=1.7pt,y radius=1.2pt',
                     'x radius=1.275pt,y radius=.9pt')
        else:
            raise AssertionError(c)
        sphere3_commands[i] = c
    first_fill3 = next(i for i, c in enumerate(sphere3_commands) if c.startswith(r'\fill'))
    sphere3_commands.insert(
        first_fill3,
        r'\draw[line width=.25pt] (22,92)..controls(16,99)and(17,110)..(22,116);')
    finals[key('sphere3')] = figure(sphere3_commands, 'x=.00706cm,y=-.0080cm')

    assert set(finals) == {k for k, r in root.items() if r['choice'] == 'revised'}
    # The comma moves into the insertion; consume its old outside occurrence.
    mapping = {k: dict(v) for k, v in state['mapping'].items()}
    donc_end = mapping[key('case3_donc')]['end']
    assert original[donc_end:donc_end+5] == ', et '
    mapping[key('case3_donc')]['end'] += 1
    t = stage_page_replacements(original, mapping, finals)

    def evidence(name):
        r = root[key(name)]
        return dict(ink=r['ink'], confidence=r['confidence'],
                    **crop_metadata(key(name), state['boxes']))

    def change(row, name, **updates):
        p['changes'][row].update(**evidence(name), **updates)

    # Existing rows cover these changed whole phrases, symbols, and drawings.
    change(5, 'cancelled_order5', final=finals[key('cancelled_order5')])
    change(7, 'operation_note', final=r'\margin{' + operation + '}')
    change(10, 'case1_autom_D5', final=d5_inline)
    change(11, 'case1_isom', final=finals[key('case1_isom')], against_c=True)
    change(12, 'pentagon_note', final=finals[key('pentagon_note')], against_c=True)
    change(13, 'sphere5', final=sphere5)
    change(14, 'case2_deleted', final=cancelled_case2)
    change(16, 'case2_pole', final=finals[key('case2_pole')])
    change(17, 'case2_group', final='autom', against_c=True)
    change(20, 'sphere4', final=finals[key('sphere4')])
    change(22, 'case3_deleted_symbol',
           place='case 3, cancelled initial symbol and small index',
           final=finals[key('case3_deleted_symbol')])
    original_connector_ink = p['changes'][23]['ink']
    change(23, 'case3_donc', final=finals[key('case3_donc')])
    p['changes'][23]['ink'] += ' ' + original_connector_ink
    change(26, 'case3_struck_group', final=finals[key('case3_struck_group')])
    change(32, 'association_deleted_symbol',
           final=finals[key('association_deleted_symbol')])
    change(35, 'ending_omega', final=finals[key('ending_omega')])
    change(37, 'partition_note',
           place='third oblique margin, opening doubt and richesse en',
           final=finals[key('partition_note')].removesuffix('symétries)'),
           against_c=True)
    change(39, 'sphere3', final=finals[key('sphere3')])

    # Three newly recorded capital Card readings; the fourth is in row14.
    def add_case_row(place, name, c, h, final, math):
        assert all(row['place'] != place for row in p['changes'])
        p['changes'].append(dict(
            place=place, c=c, h=h, final=final, kind='misread word',
            against_c=True, against_h=True, math=math, **evidence(name)))

    add_case_row(
        'definition, capital Card', 'definition_count',
        r'\operatorname{card}K=5', r'\mathrm{card}\, K = 5',
        r'\operatorname{Card}K=5', True)
    add_case_row(
        'case 3, capital Card in fixed-point count', 'case3_fixed_count',
        r'\operatorname{card}K^g=2', r'\mathrm{card}\, K^{g} = 2',
        r'\operatorname{Card}K^g=2', True)
    add_case_row(
        'case 3, capital Card in final three-element phrase', 'case3_Ens_count',
        r'de card \(3\)', 'de card 3', r'de Card \(3\)', False)

    marks = {d['id']: d for d in p['decisions']}
    marks['M0448'].update(decision='undecided',
                         reading=finals[key('title_characteristic')],
                         **evidence('title_characteristic'))
    marks['M0449'].update(decision='undecided',
                         reading=r'\(\unsure{\infty|0}\)', **evidence('case2_pole'))
    marks['M0450'].update(decision='first', reading='supposer',
                         **evidence('case3_replacement'))
    marks['M0451'].update(decision='undecided',
                         reading=comp[key('association_inclusion')]['first'],
                         **evidence('association_inclusion'))
    marks['M0453'].update(decision='undecided',
                         reading=comp[key('ending_field')]['first'],
                         **evidence('ending_field'))
    marks['M0454'].update(decision='undecided',
                         reading=r'\unsure{Partition|Une partition}',
                         **evidence('partition_note'))
    marks['M0455'].update(decision='other', reading='richesse',
                         **evidence('partition_note'))
    marks['M0456'].update(decision='first', reading='symétries',
                         ink=root[key('partition_note')]['ink'],
                         **crop_metadata(key('partition_note'), state['boxes']))

    p['unresolved'] = [
        u for u in p['unresolved']
        if u['place'] not in (
            'case 2, cancelled initial letter',
            'third margin, word before ou symétries')
    ]
    doubt_map = {
        'title, characteristic phrase': (
            'title_characteristic', finals[key('title_characteristic')], ['de']),
        'cancelled order-5 group, initial stroke': (
            'cancelled_order5', finals[key('cancelled_order5')], [r'\forall', r'\nu']),
        'case 2, pole symbol': (
            'case2_pole', r'\(\unsure{\infty|0}\)', [r'\infty', '0']),
        'case 3, cancelled initial symbol': (
            'case3_deleted_symbol', finals[key('case3_deleted_symbol')],
            [r'\Sigma', 'K', 'additional small index2, attachment and shape uncertain']),
        'association, cancelled symbol after Sigma_J': (
            'association_deleted_symbol', finals[key('association_deleted_symbol')],
            [r'\deleted{\Sigma}', r'\deleted{g}\Omega', r'\deleted{G}\Omega']),
        'association, inclusion formula exponent': (
            'association_inclusion', comp[key('association_inclusion')]['first'],
            [r'\Sigma_J^g', r'\Sigma_J']),
        'third margin, initial word': (
            'partition_note', r'\unsure{Partition|Une partition}',
            ['Partition', 'Une partition']),
    }
    for u in p['unresolved']:
        if u['place'] in doubt_map:
            name, reading, alternatives = doubt_map[u['place']]
            u.update(reading=reading, issue=root[key(name)]['ink'],
                     alternatives=alternatives,
                     confidence=root[key(name)]['confidence'],
                     **crop_metadata(key(name), state['boxes']))

    def add_doubt(place, name, reading, alternatives):
        assert all(u['place'] != place for u in p['unresolved'])
        p['unresolved'].append(dict(
            place=place, reading=reading, alternatives=alternatives,
            issue=root[key(name)]['ink'], confidence=root[key(name)]['confidence'],
            **crop_metadata(key(name), state['boxes'])))

    add_doubt('definition, mark before identity1', 'definition_identity',
              r'\unsure{à|;}', ['à', ';'])
    add_doubt('first margin, est celle or usuelle', 'operation_note',
              r'\unsure{est celle|usuelle}', ['est celle', 'usuelle'])
    add_doubt('pentagon margin, contraction', 'pentagon_note',
              r'\unsure{pentagon.le|pentagonale}', ['pentagon.le', 'pentagonale'])
    add_doubt('case 3, crossed group continuation', 'case3_struck_group',
              r'\unsure{total est|des auto}', ['total est', 'des auto'])
    add_doubt('ending, omega argument', 'ending_omega',
              r'\omega(\unsure{I|J})', ['I', 'J'])

    inv_updates = {
        'cancelled_order5': finals[key('cancelled_order5')],
        'operation_margin': operation,
        'case1_circled_D5': d5_inline,
        'pentagon_margin': finals[key('pentagon_note')],
        'case2_cancelled_equation': cancelled_case2,
        'case3_cancelled_symbol': finals[key('case3_deleted_symbol')],
        'case3_donc': finals[key('case3_donc')],
        'case3_cancelled_group': finals[key('case3_struck_group')],
        'association_cancelled_symbol': (
            r'\unsure{\deleted{\Sigma}|\deleted{g}\Omega|\deleted{G}\Omega}'),
        'partition_margin': finals[key('partition_note')],
        'sphere5': (
            'five points, three rear and two front; top inward tick, lower-left '
            'arc, tiny angular rear mark and separate short vertical below'),
        'sphere4': (
            'five main points; six unequal rear traces and tiny dot; short tail '
            'below left rear point; top and lower-left contour gaps'),
        'sphere3': (
            'four circular points and low elliptical point; three isolated rear '
            'traces, two solid rear segments, lower-left arc and doubled left contour'),
    }
    for inv in p['inventory']:
        if inv['element'] in inv_updates:
            inv['first_words_or_objects'] = inv_updates[inv['element']]
        if inv['element'] == 'case3_donc':
            inv['position'] = 'above Card K^g=2 and et, with its own inserted comma'
        elif inv['element'] == 'association_cancelled_symbol':
            inv['position'] = 'after Sigma_J; letter and cancellation extent uncertain'

    for note in p['notes']:
        if note['id'] == '148034_C04':
            note['text'] = (
                'For nu=5 the manuscript gives the orbit mu_5(k), the double-struck '
                'D_5 inside a loop open at the upper-left, and uniqueness up to '
                'isomorphism, with a pentagonal structure. The group identification '
                'and categorical assertion were transcribed but not independently proved.')
        elif note['id'] == '148034_C05':
            note['text'] = (
                'For nu=4 the live revised equation is K^g={P}; the canceled equation '
                'has plain initial K without a separate raised g, and capital Card. '
                'The complement is one orbit, the pole remains infinity|0, and the '
                'full group is Z/4Z ≃ mu_4(k). The category is compared with oriented '
                'squares. The orbit count was checked under C03; the full group and '
                'categorical assertions were not separately proved.')
        elif note['id'] == '148034_C06':
            note['text'] = note['text'].replace('card K^g=2', 'Card K^g=2')
        elif note['id'] == '148034_N02':
            note['text'] = (
                'Clear serif I is retained in permutation de I, the complements '
                'I minus {P} and I minus K^g, and the pentagon margin. The omega '
                'argument favors I but now explicitly admits J because of its '
                'returning foot. K and J occur elsewhere; none is silently '
                'regularized from the construction.')
        elif note['id'] == '148034_N03':
            note['text'] = (
                'The first margin has a roof spanning G_m and the wording '
                'est celle|usuelle. The crossed order-5 prefix favors forall while '
                'nu remains possible. The case3 canceled letter retains Sigma|K '
                'with an additional doubtful low2 index. Letter and cancellation '
                'extent after Sigma_J remain unresolved, as do the pole symbol, '
                'raised g cluster, field-letter case, and the opening Partition|'
                'Une partition. The later margin phrase is richesse en symétries.')
        elif note['id'] == '148034_N04':
            note['text'] = (
                'The replacement qu’on peut supposer mu_3 is written below the '
                'crossed Le groupe total est|des auto. The curved leader from '
                'Card K^g=2 to the inserted donc clause is not set as a parenthesis. '
                'The comma belongs inside that insertion; est une orbite remains live.')
    p['notes'].append(dict(
        id='N034-BLIND', type='main-reader adjudication',
        text=(
            'Root personally viewed all48 differing fixed crops and completed '
            'second/148_scan034_root_working.json before implementation. The '
            'operation, pentagon and partition margins were also viewed after '
            'rotation of the full saved crops by50 degrees clockwise. Root reopened '
            'the existing complete case3_est, association and ending evidence '
            'crops where fixed boxes clipped relevant letter parts. No new image '
            'judgment was made by the mechanical implementer. The eight literal '
            'matches were not reopened. The first, second, boxes, comparison and '
            'token-difference TSVs are preserved byte for byte.')))
    p['notes'].append(dict(
        id='N034-GEOMETRY', type='mechanical placement and sizing',
        text=(
            'The first sphere keeps its original .75 scale and receives the '
            'approved angular rear mark and separate short vertical. The second '
            'sphere uses native crop coordinates with x=.0075cm and y=-.00818cm; '
            'the third uses x=.00706cm and y=-.0080cm. Both use the explicit '
            'root-specified physical line widths and point radii. The inline '
            'D5 loop uses x=.007cm and y=-.007cm, a .5pt open path and the same '
            'double-struck label. Clip commands, overlapping text and specified '
            'neighboring strokes are omitted. No TeX compilation was performed.')))
    p['notes'].append(dict(
        id='N034-ACCOUNTING', type='mechanical audit accounting',
        text=(
            'Three new C/H rows record capital Card in the definition, the case3 '
            'fixed-count formula and de Card3. The canceled case2 Card is included '
            'in its existing complete-equation row. The additional canceled low2 '
            'is included in the existing canceled-symbol row. New alternatives, '
            'narrowed doubts, the inserted-comma wrapper and coordinate changes '
            'alone receive no additional C/H row. The canceled case2 K and the '
            'canceled symbol after Sigma_J have no source MARKS IDs among the '
            'nine scan034 entries; their existing doubts and C/H rows are updated '
            'without inventing identifiers. Existing mathematical checks are unchanged.')))

    p['hand_log'][0].update(
        holds_at_every_observed_occurrence=False,
        scope=(
            'Unobscured I and J on this leaf. The overtraced inclusion index and '
            'the omega argument with a returning base are excluded from certainty.'),
        witness_effect=(
            'H reads K in the case3 complement, where I remains clear. Both '
            'witnesses give omega(J); the final argument favors I but explicitly '
            'admits J after the main-reader revisit.'))
    p['hand_log'].append(dict(
        habit=(
            'The C of Card rises to the height of the d ascender above the a/r '
            'bodies in the four separately inspected occurrences.'),
        pages=[34], holds_at_every_observed_occurrence=True,
        scope='Definition, canceled case2 equation, case3 fixed-count formula and de Card3.',
        witness_effect='These four local capitals replace the witnesses’ lowercase card.'))
    p['hand_log'].append(dict(
        habit=(
            'The left full numeral1 in 1-1 has a flag and no basal foot; the right1 '
            'has a foot. Absence of a foot alone never decides prime versus numeral1.'),
        pages=[34], holds_at_every_observed_occurrence=False,
        scope='The two full-height numeral ones in the association correspondence.',
        witness_effect=(
            'Retain 1-1. Earlier prime decisions rely on the whole form, height '
            'and paired local notation, not a universal foot rule.')))

    for n in p['notation']:
        if n['form'] == r'\(I\)':
            n['observation'] = (
                'Clear serif I remains in several positions where K or J appears '
                'elsewhere. The omega argument favors I with J admitted explicitly.')
        elif n['form'] == r'\(\widehat{\mathbb G}_m\)':
            n.update(form=r'\(\widehat{\mathbb G_m}\)',
                     observation='The separately drawn roof spans the whole G_m label; no mathematical role is inferred.')
        elif n['form'] == r'\(\mathbb D_5\)':
            n['observation'] = (
                'D has two parallel stems and lowered5, inside a literal loop open '
                'at the upper-left. The later double-struck D_3 is not encircled.')
    p['notation'].append(dict(
        form=r'\operatorname{Card}',
        observation='Capital Card occurs at the four individually adjudicated counts.',
        place='definition, canceled case2 formula, case3 fixed count and de Card3'))
    for a in p['abbreviations']:
        if a['form'] == 'isom.':
            a['form'] = 'isom'
        elif a['form'] == 'card':
            a['form'] = 'Card'
    p['abbreviations'].extend([
        dict(form='autom', expansion='automorphisme / automorphismes',
             caution='Only the case2 group sentence lacks the stop; other local autom. forms remain.'),
        dict(form='pentagon.le', expansion='pentagonale',
             caution='Favored contraction; the full pentagonale remains an alternative.'),
    ])

    extra_crops = {
        'case3_est': [('crops/148_scan034_case3_est.jxl', [1520,1900,2205,2080])],
        'association_deleted_symbol': [('crops/148_scan034_association.jxl', [345,2423,2185,2655])],
        'association_inclusion': [('crops/148_scan034_association.jxl', [345,2423,2185,2655])],
        'ending_omega': [('crops/148_scan034_ending.jxl', [341,2632,2118,2859])],
        'ending_group': [('crops/148_scan034_ending.jxl', [341,2632,2118,2859])],
    }
    entries = []
    for item in state['working']:
        entry = {k: v for k, v in item.items() if k != 'instructions'}
        crop = crop_metadata(item['box'], state['boxes'])
        entry.update(crop=crop['crop'], crop_box=crop['box'])
        if item['choice'] == 'revised':
            entry['final'] = finals[item['box']]
        if short(item['box']) in extra_crops:
            entry['additional_crops'] = [
                dict(crop=path, box=rect)
                for path, rect in extra_crops[short(item['box'])]]
        entries.append(entry)

    p['blind_graphic_transforms'] = {
        key('case1_autom_D5'): dict(
            basis='native crop coordinates', x_cm='.007', y_cm='-.007',
            baseline='d.base', loop_line_width_pt='.5',
            label=r'\mathbb D_5', open_path_endpoints=[[375,30],[354,44]]),
        key('sphere5'): dict(
            basis='retained first normalized coordinates', retained_scale='.75',
            changes='approved tiny angular rear mark and separate short vertical only'),
        key('sphere4'): dict(
            basis='native crop coordinates', x_cm='.0075', y_cm='-.00818',
            scale_option=None, outer_line_pt='.35', front_line_pt='.4',
            rear_line_pt='.25', main_point_radius_pt='1.275',
            small_rear_point_radius_pt='.425'),
        key('sphere3'): dict(
            basis='native crop coordinates', x_cm='.00706', y_cm='-.0080',
            scale_option=None, outer_line_pt='.35', front_line_pt='.4',
            rear_and_retrace_line_pt='.25', circle_radius_pt='1.275',
            low_ellipse_radii_pt=['1.275','.9']),
    }
    p['main_reader'] = (
        'Root personally viewed all48 literal DIFF crops, rotated the complete '
        'three oblique-margin crops, and reopened the existing complete evidence '
        'crops identified in the adjudications where fixed crops clipped letter '
        'parts. The supplied root decisions determine all revised readings and '
        'graphic details. The mechanical implementer made no new image judgment.')

    # Validate only the concrete changes and locked evidence.
    assert len(entries) == 48 and len(finals) == 22
    assert all(e['viewed_by_main'] is True for e in entries)
    assert set(root) == state['differences']
    for entry in entries:
        assert (B / entry['crop']).is_file()
        for extra in entry.get('additional_crops', []):
            assert (B / extra['crop']).is_file()
    assert all(t.count(final) == 1 for final in finals.values())
    assert t.count(r'\inserted{donc \(K^g=\Sigma^g\),} et ') == 1
    assert r'\inserted{donc \(K^g=\Sigma^g\),},' not in t
    assert t.count('autom est') == 1 and t.count('autom.') == original.count('autom.') - 1
    assert t.count(r'\operatorname{Card}') == 3 and t.count(r'de Card \(3\)') == 1
    assert t.count(r'\mu_4') == original.count(r'\mu_4')
    assert d5_loop.endswith('.. (354,44);') and '--cycle' not in d5_loop
    assert r'\node[draw,circle' not in t
    assert r'\clip ' not in t and '(111,0)' not in t and '(172,189)' not in t
    assert '(32,134)' not in t and '(135,134)' not in t
    assert finals[key('sphere4')].count('circle[radius=1.275pt]') == 5
    assert finals[key('sphere4')].count('circle[radius=.425pt]') == 1
    assert finals[key('sphere3')].count('circle[radius=1.275pt]') == 4
    assert finals[key('sphere3')].count('ellipse[x radius=1.275pt,y radius=.9pt]') == 1
    for n in ('sphere4', 'sphere3'):
        assert 'scale=' not in finals[key(n)]
    assert r'\draw (.59,.07)--(.61,.02);' in sphere5
    assert r'\draw (-.03,.86)--(-.01,.80);' in sphere5
    assert t.count(r'\margin{33}') == 1 and t.count(r'\mspage{1}') == 1
    level = 0
    for m in re.finditer(r'(?<!\\)[{}]', t):
        level += 1 if m.group() == '{' else -1
        assert level >= 0, m.start()
    assert level == 0
    assert t.count(r'\begin{tikzpicture}') == t.count(r'\end{tikzpicture}') == 3
    assert json.dumps(p['checks'], ensure_ascii=False, sort_keys=True) == original_checks
    assert json.dumps(p['second_boxes'], ensure_ascii=False, sort_keys=True) == original_second_boxes
    assert len(p['changes']) == 44 and len(p['decisions']) == 9
    assert len(p['unresolved']) == 15 and len(p['inventory']) == 34
    assert all(hashlib.sha256(f.read_bytes()).hexdigest() == hashes[str(f)] for f in locked)
    PAGE.write_text(t)
    REVIEW.write_text(json.dumps(p, ensure_ascii=False, indent=2) + '\n')
    ADJUDICATIONS.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(
        scan=34, adjudications=len(entries), revised_boxes=len(finals),
        change_rows=len(p['changes']),
        against_c=sum(bool(c['against_c']) for c in p['changes']),
        against_h=sum(bool(c['against_h']) for c in p['changes']),
        decisions=len(p['decisions']), unresolved=len(p['unresolved']),
        inventory=len(p['inventory']), prior_checks_unchanged=True,
        protected_tsv_hashes_unchanged=True)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mapping', action='store_true',
                        help='Print the complete mechanical box-to-page/review map.')
    parser.add_argument('--apply', action='store_true',
                        help='Apply the completed main-reader decisions once.')
    args = parser.parse_args()
    if args.apply:
        assert not ADJUDICATIONS.exists(), 'Non-idempotent: scan034 audit already applied.'
    state = load_state()
    if args.apply:
        apply_completed(state)
        return
    files = [PAGE, REVIEW, Path(str(STEM) + '_first.tsv'),
             Path(str(STEM) + '_second.tsv'), Path(str(STEM) + '_boxes.tsv'),
             Path(str(STEM) + '_comparison.tsv'),
             Path(str(STEM) + '_token_differences.tsv')]
    summary = dict(
        mode='read-only scaffold', fixed_boxes=len(state['comparison']),
        differences=len(state['differences']),
        current_root_entries=len(state['working']),
        root_announced_complete=ROOT_ANNOUNCED_COMPLETE,
        mapped_page_occurrences=len(state['mapping']),
        mapped_existing_change_rows=41,
        marks=9, unresolved=12,
        location_exceptions=[
            dict(box_id=k, **m) for k, m in state['mapping'].items()
            if m['location_method'] != 'literal unique occurrence'],
        sphere_source_headers={
            key(k): state['mapping'][key(k)]['second_picture'] for k in SPHERE_KEYS},
        shared_change_rows={
            str(i): [k for k, m in state['mapping'].items()
                     if any(r['index'] == i for r in m['change_rows'])]
            for i in (6, 25)},
        sha256={str(f.relative_to(B)): hashlib.sha256(f.read_bytes()).hexdigest()
                for f in files},
        files_written=[])
    print(json.dumps(state['mapping'] if args.mapping else summary,
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
