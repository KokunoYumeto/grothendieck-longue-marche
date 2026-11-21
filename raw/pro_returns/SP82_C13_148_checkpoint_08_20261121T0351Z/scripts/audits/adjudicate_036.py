#!/usr/bin/env python3
"""Apply root's completed scan036 adjudication once, without image judgments.

The read-only scaffold maps chart projections and a shared deletion wrapper.
--apply uses the completed 29-entry root file, retaining those owners and all
locked TSVs. It writes only page036, review036 and adjudications036. Root owns
record_audit and shared rebuilds; this script performs neither.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import re

B = Path(__file__).resolve().parents[2]
STEM = B / 'second/148_scan036'
PAGE = B / 'pages/148_scan036.tex'
REVIEW = B / 'reviews/148_scan036.json'
WORKING = Path(str(STEM) + '_root_working.json')
ADJUDICATIONS = Path(str(STEM) + '_adjudications.json')
ROOT_ANNOUNCED_COMPLETE = True

CH_ROWS = {
    1: [], 2: [0], 3: [1], 4: [2,3], 5: [4,5], 6: [6,7],
    7: [8,9], 8: [10,11], 9: [12,13], 10: [14,15], 11: [16],
    12: [17,18,19,20,21,22,23], 13: [24], 14: [25,26,27],
    15: [28], 16: [29,30,31], 17: [31], 18: [], 19: [32,33],
    20: [34,35], 21: [], 22: [36], 23: [37,38], 24: [39],
    25: [40,41], 26: [], 27: [42], 28: [43,44], 29: [45],
}
MARKS = {
    3: ['M0461'], 12: ['M0462'], 19: ['M0463'],
    20: ['M0464'], 23: ['M0465'], 28: ['M0466'],
}
DOUBT_ROWS = {
    4: [0], 7: [1], 8: [2], 9: [3,4], 12: [5,6],
    19: [7,8], 20: [9], 22: [10], 23: [11],
    24: [12], 26: [13], 28: [14],
}
INVENTORY_ROWS = {
    1: [0], 2: [1], 3: [2], 4: [3,4], 5: [5], 6: [6,7],
    7: [8,9], 8: [10,11], 9: [12,13], 10: [14], 11: [15],
    12: [16,17,18,19], 13: [19], 14: [19,20], 15: [21],
    16: [22,23,24,25], 17: [26], 18: [27], 19: [28,29,30],
    20: [31,32,33,34], 21: [35], 22: [36], 23: [37],
    24: [38], 25: [39,40,41], 26: [40], 27: [42,43], 28: [44], 29: [45],
}
DETAIL_PARENT = {17: 16, 26: 25}
SHARED_WRAPPER = {9: 'case_c_long_deletion', 10: 'case_c_long_deletion'}


def key(n):
    return f'S36-{n:02d}'


def tsv(suffix):
    with Path(str(STEM) + suffix).open() as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    assert len({r['box'] for r in rows}) == len(rows)
    return {r['box']: r for r in rows}


def unique(text, needle):
    assert text.count(needle) == 1, (needle[:150], text.count(needle))
    start = text.index(needle)
    return start, start + len(needle)


def whitespace_span(text, reading):
    pattern = r'\s+'.join(re.escape(token) for token in reading.split())
    matches = list(re.finditer(pattern, text))
    assert len(matches) == 1, (reading[:100], len(matches))
    return matches[0].span()


def strip_picture(reading):
    s = reading[reading.index(r'\begin{tikzpicture}'):]
    header_end = s.index(']') + 1
    return s[header_end:s.rindex(r'\end{tikzpicture}')].strip()


def strip_deleted(reading):
    assert reading.startswith(r'\deleted{') and reading.endswith('}')
    return reading[len(r'\deleted{'):-1]


def command_norm(s, ignore_options=False):
    s = re.sub(r'\s+', '', s)
    if ignore_options:
        s = re.sub(r'^(\\(?:draw|fill|node))\[[^\]]*\]', r'\1', s)
    return s


def command_parts(text, offset=0):
    return [
        dict(start=offset+m.start(), end=offset+m.end(), text=m.group())
        for m in re.finditer(r'\\(?:draw|fill|node)\b.*?;', text, re.S)
    ]


def select_commands(candidates, body, ignore_options=False):
    selected = []
    for desired in command_parts(body):
        norm = command_norm(desired['text'], ignore_options)
        hits = [c for c in candidates
                if command_norm(c['text'], ignore_options) == norm]
        assert len(hits) == 1, (desired['text'], len(hits))
        selected.append(hits[0])
    return selected


def nodes_at(commands, coordinates):
    selected = []
    for xy in coordinates:
        needle = 'at(' + xy + ')'
        hits = [c for c in commands if c['text'].startswith(r'\node')
                and needle in command_norm(c['text'])]
        assert len(hits) == 1, (xy, len(hits))
        selected.append(hits[0])
    return selected


def secondary_picture(reading):
    if r'\begin{tikzpicture}' not in reading:
        return None
    s = reading[reading.index(r'\begin{tikzpicture}'):]
    header = s[:s.index(']')+1]
    bounds = re.search(r'rectangle \(([^)]+)\)', s)
    return dict(header=header, rectangular_extent=bounds.group(1) if bounds else None)


def load_state():
    page = PAGE.read_text()
    review = json.loads(REVIEW.read_text())
    comp = tsv('_comparison.tsv')
    first, second, boxes = tsv('_first.tsv'), tsv('_second.tsv'), tsv('_boxes.tsv')
    working = json.loads(WORKING.read_text()) if WORKING.exists() else []
    assert set(comp) == {key(n) for n in range(1,30)}
    assert set(comp) == set(first) == set(second) == set(boxes)
    assert all(r['different'] == 'yes' for r in comp.values())
    assert all(comp[k]['first'] == first[k]['reading'] for k in comp)
    assert all(comp[k]['second'] == second[k]['reading'] for k in comp)
    assert {r['box'] for r in working} <= set(comp)
    assert len({r['box'] for r in working}) == len(working)
    assert len(review['changes']) == 46 and len(review['decisions']) == 6

    header = comp[key(16)]['first'].split('\n', 1)[0]
    chart_start, _ = unique(page, header)
    chart_end = page.index(r'\end{tikzpicture}', chart_start) + len(r'\end{tikzpicture}')
    chart = page[chart_start:chart_end]
    chart_commands = command_parts(chart, chart_start)
    mapping = {}

    def assign(n, spans, method, owner=None):
        box = key(n)
        rect = [int(boxes[box][a]) for a in ('x0','y0','x1','y1')]
        mapping[box] = dict(
            owner=owner or ('combined_chart' if 16 <= n <= 27 else 'page'),
            method=method,
            ranges=[dict(start=a, end=b,
                         line=page.count('\n', 0, a)+1,
                         source=page[a:b]) for a,b in spans],
            exact_first_matches=page.count(comp[box]['first']),
            changes=[dict(index=i, place=review['changes'][i]['place']) for i in CH_ROWS[n]],
            marks=MARKS.get(n, []),
            doubts=[dict(index=i, place=review['unresolved'][i]['place'])
                    for i in DOUBT_ROWS.get(n, [])],
            inventory=[dict(index=i, element=review['inventory'][i]['element'])
                       for i in INVENTORY_ROWS[n]],
            parent_detail_owner=key(DETAIL_PARENT[n]) if n in DETAIL_PARENT else None,
            shared_wrapper=SHARED_WRAPPER.get(n),
            second_picture=secondary_picture(comp[box]['second']),
            crop=f'crops/second/148_scan036/{box}.png', crop_box=rect)
        assert (B / mapping[box]['crop']).is_file()

    def assign_commands(n, selected, method):
        assign(n, [(c['start'], c['end']) for c in selected], method)

    # Contiguous text/whole-picture readings that are already literal in the page.
    for n in (1,2,3,4,5,7,8,11,13,15,22,23,24,28,29):
        assign(n, [unique(page, comp[key(n)]['first'])],
               'literal first extraction', owner='combined_chart' if 22<=n<=24 else 'page')
    for n in (12,14):
        assign(n, [whitespace_span(page, comp[key(n)]['first'])],
               'same text with source line breaks')

    # S36-06 is a projection of a displayed formula, then a prose case reference.
    b_start = page.index('que\n\\[\nK=')
    b_reference = 'Contient le cas ' + r'\(3^\circ\)' + ' (bitétraédral)'
    _, b_end = unique(page, b_reference)
    assign(6, [(b_start, b_end)], 'display/formula/prose projection',
           owner='case_b_display_and_reference')

    # S36-09 and10 project two portions of one existing cancellation wrapper.
    first9 = comp[key(9)]['first']
    inserted9, deleted9 = first9.split(r' \deleted', 1)
    body9 = strip_deleted(r'\deleted' + deleted9)
    body10 = strip_deleted(comp[key(10)]['first'])
    assign(9, [unique(page, inserted9), unique(page, body9)],
           'insertion plus initial body of shared deletion',
           owner='case_c_insertion_and_long_deletion')
    assign(10, [unique(page, body10)], 'continuation inside shared deletion',
           owner='case_c_long_deletion')
    assert body9 + ' ' + body10 in page
    shared_deletion = r'\deleted{' + body9 + ' ' + body10 + '}'
    deletion_range = unique(page, shared_deletion)

    # Graph prefix is embedded in a larger table, not a second standalone picture.
    graph_body = strip_picture(comp[key(16)]['first'])
    assign(16, [unique(page, graph_body)],
           'graph/header prefix inside combined chart')
    assign_commands(17, select_commands(
        chart_commands, strip_picture(comp[key(17)]['first']), ignore_options=True),
        'detail projection of S36-16; first extraction omits explicit widths')
    assign_commands(18, nodes_at(chart_commands, ['167,1860','460,1865','720,1854']),
                    'three count-node payloads')
    assign_commands(19, nodes_at(
        chart_commands, ['202,1954','30,1968','31,2010','35,2054','52,2092']),
        'five realization-label/count nodes in their existing positions')
    assign_commands(20, select_commands(
        chart_commands, strip_picture(comp[key(20)]['first'])),
        'vertical rule and three calculation nodes')
    assign_commands(21, nodes_at(chart_commands, ['683,1944']),
                    'right calculation node')
    # The short stroke is adjacent to the canceled left words; preserve its ownership.
    stroke24 = unique(page, r'\draw (90,2237)--(132,2235);')
    mapping[key(24)]['adjacent_existing_stroke'] = dict(
        start=stroke24[0], end=stroke24[1], source=page[stroke24[0]:stroke24[1]])
    assign_commands(25, nodes_at(
        chart_commands, ['159,2335','265,2335','640,2320','635,2404']),
        'four NB/count nodes; preserve combined-chart layout')
    pyramid_node = nodes_at(chart_commands, ['640,2320'])[0]
    factor_text = r'5\times3\times2=30'
    factor_start = pyramid_node['start'] + pyramid_node['text'].index(factor_text)
    target2 = factor_start + factor_text.index('2=30')
    assign(26, [(target2, target2+1)],
           'last factor2 within S36-25 pyramid-count node; not prose dimensions')
    assign_commands(27, select_commands(
        chart_commands, strip_picture(comp[key(27)]['first'])),
        'eight long-arrow strokes only; context graph fragments belong to S36-16/17')

    assert set(mapping) == set(comp)
    assert {c['index'] for m in mapping.values() for c in m['changes']} == set(range(46))
    assert {i['index'] for m in mapping.values() for i in m['inventory']} == set(range(46))
    assert {d['index'] for m in mapping.values() for d in m['doubts']} == set(range(15))
    assert {d for m in mapping.values() for d in m['marks']} == {
        d['id'] for d in review['decisions']}
    # Only these two nested overlaps are intentional; neither becomes duplicate ink.
    for child, parent in DETAIL_PARENT.items():
        assert all(any(p['start'] <= c['start'] and c['end'] <= p['end']
                       for p in mapping[key(parent)]['ranges'])
                   for c in mapping[key(child)]['ranges'])

    covered_chart_commands = []
    residual_chart_commands = []
    for command in chart_commands:
        owners = []
        for n in range(16,28):
            ranges = list(mapping[key(n)]['ranges'])
            extra = mapping[key(n)].get('adjacent_existing_stroke')
            if extra:
                ranges.append(extra)
            if any(r['start'] < command['end'] and command['start'] < r['end'] for r in ranges):
                owners.append(key(n))
        (covered_chart_commands if owners else residual_chart_commands).append(
            dict(**command, owners=owners))
    assert len(residual_chart_commands) == 2
    assert all(any(s in c['text'] for s in ('{nb}', '{comp.}'))
               for c in residual_chart_commands)
    return dict(
        page=page, review=review, comparison=comp, working=working, mapping=mapping,
        chart_owner=dict(start=chart_start, end=chart_end, header=header),
        shared_deletion_owner=dict(start=deletion_range[0], end=deletion_range[1],
                                   source=shared_deletion),
        residual_chart_commands=residual_chart_commands)


def require_complete_root(state):
    assert ROOT_ANNOUNCED_COMPLETE, 'Root has not announced all29 decisions complete.'
    assert len(state['working']) == 29
    assert {e['box'] for e in state['working']} == set(state['comparison'])
    assert all(e['viewed_by_main'] is True for e in state['working'])
    assert not ADJUDICATIONS.exists() and not state['review'].get('second_audit')


def once(text, old, new):
    assert text.count(old) == 1, (old[:120], text.count(old))
    return text.replace(old, new, 1)


def picture(body, header):
    return header + '\n' + body.strip() + '\n' + r'\end{tikzpicture}'


def apply_completed(state):
    require_complete_root(state)
    original, p, comp = state['page'], state['review'], state['comparison']
    root = {r['box']: r for r in state['working']}
    mapping = state['mapping']
    checks_before = json.dumps(p['checks'], ensure_ascii=False, sort_keys=True)
    boxes_before = json.dumps(p['second_boxes'], ensure_ascii=False, sort_keys=True)
    locked = [Path(str(STEM) + s) for s in (
        '_first.tsv', '_second.tsv', '_boxes.tsv',
        '_comparison.tsv', '_token_differences.tsv')]
    hashes = {str(f): hashlib.sha256(f.read_bytes()).hexdigest() for f in locked}
    assert hashlib.sha256(PAGE.read_bytes()).hexdigest() == (
        '29ad9824902b171e934e439af5637408fae7ce3a4c577a29f2dd7cda1a6cd2c5')
    assert hashlib.sha256(REVIEW.read_bytes()).hexdigest() == (
        '9d49773793cbf6412aff8652773301940a2d173dc02bfca6a2a88747312e7994')
    finals = {}
    replacements = []
    chart_header = state['chart_owner']['header']

    def stage(old, new):
        a, b = unique(original, old)
        replacements.append((a, b, new))

    def first(n):
        return comp[key(n)]['first']

    def text_revision(n, old, new):
        finals[key(n)] = once(first(n), old, new)
        if original.count(first(n)) == 1:
            stage(first(n), finals[key(n)])
        else:
            stage(old, new)

    text_revision(3, r'M_{0,5}^{!}', r'M_{0,\unsure{5|\bar I}}^{!}')
    finals[key(5)] = (
        r'b) \(\operatorname{Card}K^\sigma=3\), En prenant un repère '
        r'\(0,1,\infty\) dans \(K^\sigma\), on trouve')
    stage(first(5), finals[key(5)])

    inserted9 = r'\inserted{\unsure{Soit} \(K\setminus K^\sigma=I\), donc}'
    deleted9 = (
        r'On \unsure{prend comme repère|prend pour coordonnées|peut prendre comme points} '
        r'\(\unsure{t_0|\infty}\),')
    deleted10 = once(
        strip_deleted(first(10)), '. OP', r'. \unsure{OP|\(\sigma P\)}')
    finals[key(9)] = inserted9 + r' \deleted{' + deleted9 + '}'
    finals[key(10)] = r'\deleted{' + deleted10 + '}'
    stage(mapping[key(9)]['ranges'][0]['source'], inserted9)
    new_shared_deletion = r'\deleted{' + deleted9 + ' ' + deleted10 + '}'
    stage(state['shared_deletion_owner']['source'], new_shared_deletion)

    text_revision(12, 'un antiautomorphisme',
                  r'un \unsure{antiautomorphisme|anti-isomorphisme}')
    text_revision(20, r'\unsure{(|c}', r'\unsure{c|C}')
    finals[key(23)] = r'\inserted{(\unsure{polyèdres|tétraèdres}-pointés)}'
    stage(first(23), finals[key(23)])
    factor = r'\unsure{2|\deleted{1}\inserted{2}|\deleted{4}\inserted{2}}'
    old_product = r'5\times3\times2=30'
    new_product = r'5\times3\times' + factor + '=30'
    finals[key(25)] = once(first(25), old_product, new_product)
    finals[key(26)] = r'\(' + factor + r'\)'
    # A scoped product replacement, never either prose dimension 2.
    stage(old_product, new_product)
    text_revision(28, r'\unsure{\sigma}', r'\unsure{\sigma|0}')

    # Only two fixed-box paths replace the old cancellation zigzag.
    second17 = command_parts(strip_picture(comp[key(17)]['second']))
    main_cancel = next(c['text'] for c in second17 if '(37,88)' in c['text'])
    thin_cancel = next(c['text'] for c in second17 if '(39,84)' in c['text'])
    main_cancel = once(main_cancel, 'line width=1.25pt', 'line width=.6pt')
    thin_cancel = once(thin_cancel, 'line width=.7pt', 'line width=.35pt')
    cancel_scope = (
        r'\begin{scope}[shift={(760,1645)}]' + '\n' +
        main_cancel + '\n' + thin_cancel + '\n' + r'\end{scope}')
    detail_parts = [r['source'] for r in mapping[key(17)]['ranges']]
    old_cancel = next(c for c in detail_parts if '(825,1679)' in c)
    stage(old_cancel, cancel_scope)
    graph_body = once(strip_picture(first(16)), old_cancel, cancel_scope)
    finals[key(16)] = picture(graph_body, chart_header)
    detail_body = '\n'.join(
        cancel_scope if c == old_cancel else c for c in detail_parts)
    finals[key(17)] = picture(detail_body, chart_header)
    # The S20 projection inherits the actual chart's styles and positions.
    final20_commands = '\n'.join(
        r['source'].replace(r'\unsure{(|c}', r'\unsure{c|C}')
        for r in mapping[key(20)]['ranges'])
    finals[key(20)] = picture(final20_commands, chart_header)

    # Seven literal arrow-only paths; the intervening blank is not bridged.
    second27 = comp[key(27)]['second']
    arrow_body = second27[
        second27.index('% Left upper arrow:'):
        second27.index('% All readable material')]
    arrow_commands = [c['text'] for c in command_parts(arrow_body)]
    assert len(arrow_commands) == 7
    assert all(c.startswith(r'\draw[') for c in arrow_commands)
    arrow_scope = (
        r'\begin{scope}[shift={(525,1695)}]' + '\n' +
        '\n'.join(arrow_commands) + '\n' + r'\end{scope}')
    old_arrow_commands = mapping[key(27)]['ranges']
    arrow_start, arrow_end = old_arrow_commands[0]['start'], old_arrow_commands[-1]['end']
    arrow_old = original[arrow_start:arrow_end]
    assert len(command_parts(arrow_old)) == 8
    assert re.sub(r'\s+', '', arrow_old) == ''.join(
        re.sub(r'\s+', '', r['source']) for r in old_arrow_commands)
    stage(arrow_old, arrow_scope)
    stage('% Arrows from the two structure counts to the corresponding graphs.',
          '% Open upper heads, a hooked right tail, and a separate lower arrow.')
    finals[key(27)] = picture(arrow_scope, chart_header)
    assert set(finals) == {k for k, r in root.items() if r['choice'] == 'revised'}
    assert len(finals) == 13

    # Independent replacement spans preserve the chart and shared text owners.
    replacements.sort()
    assert all(a[1] <= b[0] for a, b in zip(replacements, replacements[1:]))
    t = original
    for a, b, new in reversed(replacements):
        t = t[:a] + new + t[b:]

    full_chart_crop = dict(crop='crops/148_scan036_chart.jxl',
                           box=[20,1502,1295,2458])

    def evidence(n, confidence=None):
        m, r = mapping[key(n)], root[key(n)]
        return dict(ink=r['ink'], confidence=confidence or r['confidence'],
                    crop=m['crop'], box=m['crop_box'])

    def change(i, n, **updates):
        p['changes'][i].update(**evidence(n))
        p['changes'][i].update(updates)

    # Updating existing covered places does not create additional correction rows.
    change(1, 3, final=finals[key(3)][2:-2])
    change(4, 5, ink=(
        'After the descending comma following 3, no cancelled word precedes the '
        'large E of En. Root retained the absence of H’s supposed cancellation.'))
    change(5, 5, place='b: un before repère', final='un',
           kind='misread word', against_c=True)
    p['changes'][10]['ink'] = (
        'The initial letter of this occurrence is a large open C. Root also '
        'confirmed a capital C in the case b occurrence; neither is normalized '
        'from its witnesses’ lower-case card.')
    change(12, 9, final=inserted9, against_c=True)
    change(13, 9, final=r'\deleted{' + deleted9 + '}',
           against_c=True, math=True)
    change(19, 12, final=r'\unsure{antiautomorphisme|anti-isomorphisme}',
           ink=root[key(12)]['ink'] + (
               ' The first singular ending is retained; the added central-word '
               'alternative is a doubt, not an additional correction row.'))
    third_graph = graph_body[graph_body.index(
        '% The sloping extra middle branch is crossed out; the upright remains.'):]
    change(31, 17, final=picture(third_graph, chart_header))
    change(32, 19)
    change(33, 19)
    change(35, 20, final=r'\unsure{c|C}', against_c=True,
           kind='misread symbol or index')
    change(37, 23, place='lower chart: replacement caption and first word',
           final=finals[key(23)], against_c=True)
    change(38, 23, final='-pointés', against_c=True)
    for i in (37,38):
        p['changes'][i]['additional_crops'] = [full_chart_crop.copy()]
    change(42, 27, place='lower chart: separated curved arrows, heads and tail hook',
           final=finals[key(27)], against_c=True)
    change(43, 28, final=finals[key(28)])
    change(44, 28, final=r'\unsure{\sigma|0}')

    # Both witnesses have lower-case card and a stop in case b; these are new
    # concrete readings, separate from the existing article row.
    p['changes'].append(dict(
        place='b: initial capital in Card', c=r'\operatorname{card}',
        h=r'\mathrm{card}', final=r'\operatorname{Card}',
        kind='other', against_c=True, against_h=True, math=False,
        **evidence(5)))
    p['changes'].append(dict(
        place='b: comma after fixed-point count 3', c='.', h='.', final=',',
        kind='other', against_c=True, against_h=True, math=False,
        **evidence(5)))

    # There are six source MARKS, with no invented ID for new doubts.
    marks = {d['id']: d for d in p['decisions']}
    for n, mark_ids in MARKS.items():
        for mark_id in mark_ids:
            d = marks[mark_id]
            d.update(**evidence(n))
            if mark_id == 'M0461':
                d.update(decision='first', reading=r'U_{0,3}', confidence='high',
                         ink=(
                             'Root retained the U argument and its 0,3 indices. '
                             'The separate reopened 5/bar-I doubt is in the '
                             'preceding M subscript, not in this source MARK.'))
            elif mark_id == 'M0464':
                d.update(decision='undecided', reading=r'\unsure{c|C}')
            elif mark_id == 'M0465':
                d.update(decision='undecided', reading=r'\unsure{polyèdres|tétraèdres}',
                         additional_crops=[full_chart_crop.copy()])
            elif mark_id == 'M0466':
                d.update(decision='undecided', reading=r'\unsure{\sigma|0}')

    def doubt(i, n, reading=None, alternatives=None, issue=None, confidence=None):
        e = evidence(n, confidence)
        d = p['unresolved'][i]
        d.update(crop=e['crop'], box=e['box'], confidence=e['confidence'],
                 issue=issue or e['ink'])
        if reading is not None:
            d['reading'] = reading
        if alternatives is not None:
            d['alternatives'] = alternatives

    for i, n in ((0,4),(1,7),(2,8),(3,9),(5,12),(10,22),(12,24)):
        doubt(i, n)
    doubt(4, 9,
          reading=r'\deleted{\unsure{prend comme repère|prend pour coordonnées|peut prendre comme points}}',
          alternatives=['prend comme repère','prend pour coordonnées',
                        'peut prendre comme points'])
    doubt(6, 12, confidence='low')
    cluster_alternative = (
        'multiplicités / multiples as a reading of the whole overlapping cluster, '
        'not independently assigned to either baseline')
    for i, own in ((7, ['modulaires','spéciales']), (8, ['polyédriques'])):
        doubt(i, 19, alternatives=own + [cluster_alternative],
              issue=root[key(19)]['ink'] + (
                  ' The multiplicités/multiples proposal is an alternative for '
                  'the combined overlapping ink, not an added live word.'))
    doubt(9, 20, reading=r'\unsure{c|C}', alternatives=['c','C'])
    doubt(10, 22, alternatives=['tétraèdre-pyr','tétraèdre-pyramide'])
    doubt(11, 23, reading=r'\unsure{polyèdres|tétraèdres}',
          alternatives=['polyèdres','tétraèdres'])
    p['unresolved'][11]['additional_crops'] = [full_chart_crop.copy()]
    doubt(13, 26, reading=factor,
          alternatives=['2', r'\deleted{1}\inserted{2}',
                        r'\deleted{4}\inserted{2}'])
    p['unresolved'][13]['additional_crops'] = [full_chart_crop.copy()]
    doubt(14, 28, reading=r'\unsure{\sigma|0}', alternatives=[r'\sigma','0'])

    def add_doubt(n, place, reading, alternatives):
        e = evidence(n)
        p['unresolved'].append(dict(
            place=place, reading=reading, alternatives=alternatives,
            issue=e.pop('ink'), **e))

    add_doubt(3, 'a: second subscript of M',
              r'\unsure{5|\bar I}', ['5', r'\bar I'])
    add_doubt(9, 'c: coordinate at end of first cancelled clause',
              r'\unsure{t_0|\infty}', [r't_0',r'\infty'])
    add_doubt(10, 'c: terminal abbreviation or symbol in long deletion',
              r'\unsure{OP|\(\sigma P\)}', ['OP',r'\(\sigma P\)'])
    add_doubt(12, 'c: compressed middle of anti...morphisme',
              r'\unsure{antiautomorphisme|anti-isomorphisme}',
              ['antiautomorphisme','anti-isomorphisme'])

    def inventory(i, n, **updates):
        p['inventory'][i].update(**updates)
        p['inventory'][i].update(crop=mapping[key(n)]['crop'],
                                 box=mapping[key(n)]['crop_box'])

    inventory(2, 3, first_words_or_objects=finals[key(3)][2:-2])
    inventory(5, 5, first_words_or_objects=(
        r'b) Card K^\sigma=3, En prenant un repère'))
    inventory(12, 9, first_words_or_objects=inserted9)
    inventory(13, 9, first_words_or_objects=deleted9)
    inventory(14, 10, first_words_or_objects=deleted10)
    inventory(18, 12, element='cancelled sign after anti...morphisme',
              position='after the doubtful antiautomorphisme/anti-isomorphisme, before involutif')
    inventory(26, 17, first_words_or_objects=(
        'oblique branch crossed by two angular turns, a lower closed returning loop '
        'and a short thin retrace; upright remains live'))
    inventory(32, 20, element='small c/C after 60',
              first_words_or_objects=r'\unsure{c|C}')
    inventory(37, 23, element='inserted lower parenthetical caption',
              kind='insertion', first_words_or_objects=finals[key(23)])
    inventory(40, 26, first_words_or_objects=new_product)
    inventory(42, 27, first_words_or_objects=(
        'long right curve, open upper head near third graph, sharp free lower hook'))
    inventory(43, 27, element='separate inner curved arrows',
              first_words_or_objects=(
                  'upper curve to second graph with open head; blank break; '
                  'separate lower curve with downward/rightward open head'))
    inventory(44, 28, first_words_or_objects=(
        r'first pyramidal outline, upper circuit and outer loop retained; central \unsure{\sigma|0}'))

    notes = {n['id']: n for n in p['notes']}
    note_text = {
        'S036-C01': (
            r'Case a writes K^\sigma=K, identifies the resulting real points with '
            r'M_{0,\unsure{5|\bar I}}^{!}\simeq Sym_2^*(U_{0,3}), and gives real '
            'dimension 2 and case 1° (pentagonal). The intended five-point setting '
            'does not resolve the tiny subscript ink.'),
        'S036-C02': (
            r'Case b writes Card K^\sigma=3, followed by a comma, and chooses un '
            r'repère 0,1,infinity dans K^\sigma. It writes '
            'K={0,1,infinity,lambda,bar lambda}, with lambda in the Poincaré '
            'half-plane, real dimension 2, and case 3° (bitétraédral).'),
        'S036-C03': (
            r'Case c writes Card K^\sigma=1 and K^\sigma={P}; its interlinear '
            r'insertion reads \unsure{Soit} K\setminus K^\sigma=I, donc. '
            'The canceled construction begins capital On, has an uncertain '
            'central phrase and a t_0/infinity candidate, continues with numeric '
            '0=sigma 0, and ends in uncertain OP/sigma P. The two canceled '
            'clauses remain one continuous deletion owner.'),
        'S036-C04': (
            'The paragraph says that the four-point system on a complex sphere '
            'admits an involutive antiautomorphisme/anti-isomorphisme, called '
            'conjugaison, has real modular dimension 1, and gains one real '
            'dimension on adding P, for total dimension 2. It refers to the '
            'square-pyramidal case 2°. The first long-word reading is favored '
            'but its compressed middle remains doubtful.'),
        'S036-C06': (
            'The first chart column gives 12 realizations. The two overlapping '
            'label baselines retain doubtful live modulaires/spéciales and '
            'canceled polyédriques; multiplicités/multiples is recorded as an '
            'unresolved reading of the combined cluster, not an added word.'),
        'S036-C10': (
            'The manuscript’s final factors read 5×3×2=30. The last 2 is marked '
            'with a doubt concerning a possible earlier 1 or 4 underneath; '
            'the final numeral and the existing arithmetic check are unchanged.'),
        'S036-N03': (
            'Root checked the fixed factor detail and complete existing chart. '
            'The upper curve and broad foot secure final 2; a separate thin '
            'upright may be an earlier 1 or 4, or part of the retraced 2. '
            'All three source-state alternatives remain explicit.'),
        'S036-N04': (
            'The third graph retains its upright free branch, separate canceled '
            'diagonal, vertex and baseline gap. Two angular crossing turns and '
            'a lower returning cancellation loop replace the old zigzag. '
            'The chart arrows retain upper open heads, the right lower hook, '
            'and a separate lower downward/rightward head. The inner upper '
            'and lower segments have an actual blank interval between them.'),
        'S036-N05': (
            'The bottom sketch retains the first geometry and physical size, '
            'including its interrupted left side and upper outer-loop head. '
            'The central open rounded glyph remains sigma/0, with sigma favored; '
            'no topological meaning has been assigned.'),
        'S036-N06': (
            'The full bowl with returning ends after the first 60 favors c; '
            'its case remains c/C. The canceled upper caption remains doubtful. '
            'The lower replacement is inserted (polyèdres/tétraèdres-pointés), '
            'with polyèdres favored and no second e in pointés.'),
    }
    for ident, text in note_text.items():
        notes[ident]['text'] = text
    p['notes'].append(dict(
        id='S036-N11', statement_id='S036-N11', kind='reading workflow',
        place='second reading and combined chart', status='observed by main reader',
        text=(
            'Root personally viewed all 29 differing fixed crops and the complete '
            'pre-existing chart, using its JPEG proxy after the PNG display '
            'was truncated. Only root’s supplied decisions were implemented. '
            'The chart remains one .009cm-coordinate figure: the two cancellation '
            'paths are translated by (760,1645), at .6pt and .35pt, and the seven '
            'arrow-only paths by (525,1695), with their supplied widths. '
            'Context words, graph fragments, bounding boxes and clips are excluded.'),
        crop=full_chart_crop['crop'], box=full_chart_crop['box']))

    for h in p['hand_log']:
        if h['habit'] == 'Different initial case in card/Card':
            h.update(
                habit='Capital Card in both local fixed-point counts',
                holds_at_every_observed_occurrence=True,
                witness_effect='C and H use lower-case card for both cases b and c.',
                evidence=(
                    'Root confirmed the tall open C above the a/r bodies in '
                    'case b and retained capital Card in case c. The earlier '
                    'claim that b begins with a small c is superseded.'))
    p['hand_log'].append(dict(
        pages=[36], habit='Detached digit top bars and serifed capital I',
        holds_at_every_observed_occurrence=False,
        witness_effect=(
            'C and H both give 5 in the M subscript; the tiny source form remains '
            '5/bar-I after root’s local comparison. Neither witness overbars the '
            'separate I in the complement formula or pair.'),
        evidence=(
            'Root compared the tiny subscript with the clear 5 forms in S36-18 '
            'and S36-21: their top bars can be detached from the lower curve. '
            'A detached top alone therefore does not prove an overbar. '
            'The ordinary I has its own upper and lower serifs, while the pair’s '
            'Sigma has a normal zigzag top; neither receives an extra bar.'),
        crops=[mapping[key(n)]['crop'] for n in (3,9,11,18,21)]))
    p['notation'][0].update(
        form=r'M_{0,\unsure{5|\bar I}}^{!}\simeq\mathrm{Sym}_2^*(U_{0,3})',
        observed_use=(
            'Case a retains the exclamation exponent, starred symmetric square '
            'and U argument. The second M subscript favors 5 but admits a serifed '
            'I with a bar in its compressed lower form.'),
        caution=(
            'The star and exclamation are separate marks, neither a prime. '
            'A detached digit top bar alone does not prove an overline; the '
            'five-point mathematical setting does not settle this ink.'))
    p['notation'][1]['caution'] = (
        'The complement I has its own upper and lower serifs, not a separate '
        'overbar. Keep numeric 0 and a separate sigma in the canceled equation; '
        'the preceding canceled coordinate remains t_0/infinity.')
    p['notation'][2].update(
        observed_use=(
            'The four-point-system pair has an ordinary zigzag capital Sigma '
            'and serifed capital I, without distinct additional overbars.'),
        caution=(
            'Horizontal tops belonging to the letters are not added bars. '
            'The separate bottom glyph remains sigma/0.'))
    p['abbreviations'][-1].update(
        form=r'OPS / \unsure{OP|\(\sigma P\)}',
        expansion='not established by an explicit expansion on this sheet',
        place='oblique margin / end of the single long canceled construction',
        confidence='low')

    diff_notes = {
        648: (
            'Operator-spacing command in H, not a written comma after card. '
            'The independently observed capital Card and the comma after 3 '
            'are logged as separate source readings.'),
        650: 'Root reads live un before repère, changing C pour; H leaves this place canceled and unread.',
        668: 'The live insertion is doubtful Soit, the complement formula and comma, followed by the omitted donc.',
        669: (
            'The first canceled clause begins On. The middle phrase remains '
            'uncertain; t_0 is favored over infinity. It shares one deletion '
            'wrapper with the following et on choisit clause.'),
        679: (
            'Only muni d’ is struck; admettant remains doubtful, with one live un. '
            'The following singular long word is antiautomorphisme/anti-isomorphisme.'),
        700: (
            'The mark after 60 is doubtful c/C, with a full open bowl; '
            'the neighboring right-column equation is layout context.'),
        701: (
            'The canceled upper caption remains doubtful. Its inserted '
            'replacement reads (polyèdres/tétraèdres-pointés), with no extra e.'),
        703: (
            'The numerical 60/120 opposition is alignment. The lower replacement '
            'caption is inserted and favors polyèdres-pointés.'),
        705: (
            'The outer arrow has an upper open head and a small free lower hook. '
            'Its context is already supplied by the chart; no semicolon follows 30.'),
        706: (
            'The left upper arrow ends above a blank break; a separate lower '
            'arrow resumes and has a downward/rightward open head. Final factor 2 '
            'is clear, with uncertain plain/replaced-1/replaced-4 source states.'),
        707: (
            'First geometry and size are retained, including interrupted left '
            'edge and direction marks; only the central sigma/0 doubt broadens.'),
    }
    for d in p['differences_review']:
        if d['source_row'] in diff_notes:
            d['note'] = diff_notes[d['source_row']]
        if d['source_row'] == 650:
            d['place'] = 'b: un before repère'

    p['reading_workflow']['second_reading'] = (
        'Root completed all 29 literal DIFF crops and revisited the complete '
        'existing chart crop for S36-23 and S36-26. The implementer opened no '
        'images and made no new reading decisions; no OCR or TeX compilation.')
    p['main_reader_review']['second_adjudication'] = (
        '29 main-viewed differences: 16 first, 13 revised. The combined chart '
        'and shared long deletion retain their owners; revised details and '
        'parent projections are synchronized.')
    p['main_reader'] = (
        'Root personally viewed all 29 fixed differences and the complete saved '
        'chart via its JPEG proxy after truncated PNG output. These completed '
        'root decisions are mechanically implemented here, with no independent '
        'image judgment by the implementer.')
    p['blind_graphic_transforms'] = {
        key(17): dict(
            basis='native crop pixels', translation=[760,1645],
            outer_units_cm=['.009','-.009'], line_widths_pt=['.6','.35'],
            ownership='two replacement cancellation strokes inside first S36-16 chart prefix',
            excluded='second upright, diagonal, ellipse, vertex and context horizontal segments',
            physical_sizing='explicit final widths supplied by root; no further rescaling'),
        key(27): dict(
            basis='native crop pixels', translation=[525,1695],
            outer_units_cm=['.009','-.009'],
            line_widths_pt=['.35','.6','.45','.7','.5','.35','.68'],
            paths=7, replaced_paths=8,
            blank_break_local=[[117,404],[85,504]],
            blank_break_global=[[642,2099],[610,2199]],
            excluded='context graph strokes, nodes, bounding box and clip',
            physical_sizing='retain second explicit widths as instructed by root'),
    }

    entries = []
    for item in state['working']:
        entry = {k: item[k] for k in
                 ('box','choice','viewed_by_main','ink','confidence')}
        n = int(item['box'].split('-')[1])
        entry.update(crop=mapping[key(n)]['crop'], crop_box=mapping[key(n)]['crop_box'])
        if entry['choice'] == 'revised':
            entry['final'] = finals[key(n)]
        if n in (23,25,26):
            entry['additional_crops'] = [full_chart_crop.copy()]
        if n == 3:
            entry['additional_crops'] = [
                dict(crop=mapping[key(j)]['crop'], box=mapping[key(j)]['crop_box'])
                for j in (18,21)]
        if n in DETAIL_PARENT:
            entry['projection_of'] = key(DETAIL_PARENT[n])
        entries.append(entry)

    # Concrete ownership, source-state and locked-evidence checks; no TeX build.
    assert len(entries) == 29 and all(e['viewed_by_main'] is True for e in entries)
    assert len(p['changes']) == 48 and len(p['decisions']) == 6
    assert len(p['unresolved']) == 19 and len(p['inventory']) == 46
    assert all((B/e['crop']).is_file() for e in entries)
    assert all((B/extra['crop']).is_file()
               for e in entries for extra in e.get('additional_crops', []))
    assert t.count(cancel_scope) == t.count(arrow_scope) == 1
    assert old_cancel not in t
    assert cancel_scope in finals[key(16)] and cancel_scope in finals[key(17)]
    assert new_product in finals[key(25)] and factor in finals[key(26)]
    assert t.count(new_product) == 1 and t.count(factor) == 1
    assert t.count(r'\(2\)') == original.count(r'\(2\)')
    assert t.count(new_shared_deletion) == 1
    assert t.count(r'\deleted{') == original.count(r'\deleted{') + 2
    assert t.count(r'\inserted{') == original.count(r'\inserted{') + 3
    assert t.count(finals[key(23)]) == 1 and '-pointées' not in t
    assert t.count(r'\operatorname{Card}') == 2
    assert t.count(r'\margin{35}') == t.count(r'\mspage{3}') == 1
    assert first(15) in t
    assert once(finals[key(28)], r'\unsure{\sigma|0}', r'\unsure{\sigma}') == first(28)
    for c in state['residual_chart_commands']:
        assert t.count(c['text']) == 1
    assert len(re.findall(r'\\figure\{', t)) == 3
    assert t.count(r'\begin{tikzpicture}') == t.count(r'\end{tikzpicture}') == 3
    assert t.count(r'\begin{scope}') == t.count(r'\end{scope}') == 2
    assert r'\clip' not in t and 'use as bounding box' not in t
    assert '(659,2076)' not in t and '(623,2377)' not in t
    assert '(117,404)' in arrow_scope and '(85,504)' in arrow_scope
    assert r'\ellipse' not in cancel_scope and 'ellipse' not in cancel_scope
    # Revised final projections carry the actual page commands and text, not
    # the independently read neighboring context in their larger crop.
    for n in (16,17,20,27):
        for command in command_parts(strip_picture(finals[key(n)])):
            assert t.count(command['text']) == 1, (n, command['text'])
    for n in (3,5,23,28):
        assert t.count(finals[key(n)]) == 1
    assert inserted9 in t and deleted9 + ' ' + deleted10 in t
    assert re.sub(r'\s+', '', finals[key(12)]) in re.sub(r'\s+', '', t)
    level = 0
    for m in re.finditer(r'(?<!\\)[{}]', t):
        level += 1 if m.group() == '{' else -1
        assert level >= 0, m.start()
    assert level == 0
    assert json.dumps(p['checks'], ensure_ascii=False, sort_keys=True) == checks_before
    assert json.dumps(p['second_boxes'], ensure_ascii=False, sort_keys=True) == boxes_before
    assert all(hashlib.sha256(f.read_bytes()).hexdigest() == hashes[str(f)] for f in locked)
    PAGE.write_text(t)
    REVIEW.write_text(json.dumps(p, ensure_ascii=False, indent=2) + '\n')
    ADJUDICATIONS.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(
        scan=36, adjudications=len(entries), revised_boxes=len(finals),
        first_boxes=len(entries)-len(finals), change_rows=len(p['changes']),
        against_c=sum(bool(c['against_c']) for c in p['changes']),
        against_h=sum(bool(c['against_h']) for c in p['changes']),
        decisions=len(p['decisions']), unresolved=len(p['unresolved']),
        inventory=len(p['inventory']), checks_unchanged=True,
        chart_figures=1, detail_projections_synchronized=True,
        locked_tsv_sha256_unchanged=hashes), ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mapping', action='store_true')
    parser.add_argument('--apply', action='store_true',
                        help='Apply the completed main-reader decisions once.')
    args = parser.parse_args()
    if args.apply:
        assert not ADJUDICATIONS.exists(), 'Non-idempotent: scan036 already applied.'
    state = load_state()
    if args.apply:
        apply_completed(state)
        return
    files = [PAGE, REVIEW] + [Path(str(STEM) + s) for s in
        ('_first.tsv','_second.tsv','_boxes.tsv','_comparison.tsv','_token_differences.tsv')]
    summary = dict(
        mode='read-only mapping; --apply performs the one-time audit', boxes=29, differences=29,
        current_root_entries=len(state['working']),
        root_announced_complete=ROOT_ANNOUNCED_COMPLETE,
        mapped_change_rows=46, mapped_marks=6, mapped_inventory=46, mapped_doubts=15,
        combined_chart=state['chart_owner'],
        detail_owners={key(c): key(p) for c,p in DETAIL_PARENT.items()},
        shared_cancellation_boxes=[key(9),key(10)],
        retained_chart_context=state['residual_chart_commands'],
        projection_boxes=[k for k,m in state['mapping'].items()
                          if m['method'] != 'literal first extraction'],
        native_second_picture_headers={k:m['second_picture'] for k,m in state['mapping'].items()
                                       if m['second_picture']},
        sha256={str(f.relative_to(B)): hashlib.sha256(f.read_bytes()).hexdigest()
                for f in files},
        files_written=[])
    print(json.dumps(state['mapping'] if args.mapping else summary,
                     ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
