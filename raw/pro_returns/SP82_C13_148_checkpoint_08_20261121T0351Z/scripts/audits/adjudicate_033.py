#!/usr/bin/env python3
"""Mechanically implement root's sealed scan033 decisions.

Only the supplied decisions and exact geometry instructions determine edits.
Witnesses are used solely for collation matching. No image interpretation, OCR,
research, TeX compilation, record_audit, shared-log edit, or rebuild is performed.
Run without arguments for validation; --apply writes the three local outputs.
"""
from pathlib import Path
from decimal import Decimal
import argparse
import csv
import hashlib
import json
import os
import re

B = Path(__file__).resolve().parents[2]
stem = B / 'second/148_scan033'
page = B / 'pages/148_scan033.tex'
review_path = B / 'reviews/148_scan033.json'
working_path = Path(str(stem) + '_root_working.json')
adjudication_path = Path(str(stem) + '_adjudications.json')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tsv(suffix):
    with Path(str(stem) + suffix).open(encoding='utf-8', newline='') as f:
        return {r['box']: r for r in csv.DictReader(f, delimiter='\t')}


comp = tsv('_comparison.tsv')
boxes = tsv('_boxes.tsv')
working = json.loads(working_path.read_text(encoding='utf-8'))
working_hash = sha(working_path)
root = {e['box']: e for e in working}
p = json.loads(review_path.read_text(encoding='utf-8'))
t = page.read_text(encoding='utf-8')
original = t
assert not adjudication_path.exists() and not p.get('second_audit'), \
    'Non-idempotent: scan033 adjudication has already been applied.'
assert len(working) == 34 and sum(e['choice'] == 'revised' for e in working) == 22
assert set(root) == {k for k, r in comp.items() if r['different'] == 'yes'}
assert 'finalrootdecision' in root['S33-programme2-live']['instructions'].replace(' ', '')
protected = [Path(str(stem) + s) for s in (
    '_first.tsv', '_second.tsv', '_boxes.tsv', '_comparison.tsv',
    '_token_differences.tsv')]
protected_hashes = {str(f): sha(f) for f in protected}


def once(s, old, new):
    assert s.count(old) == 1, (old[:160], s.count(old))
    return s.replace(old, new, 1)


def change_page(old, new):
    global t
    t = once(t, old, new)


def meta(key):
    b = boxes[key]
    return dict(crop=f'crops/second/148_scan033/{key}.png',
                box=[int(b[k]) for k in ('x0', 'y0', 'x1', 'y1')])


def evidence(key, **override):
    return dict(ink=root[key]['ink'], confidence=root[key]['confidence'],
                **meta(key)) | override


def body(s):
    m = re.search(r'\\begin\{tikzpicture\}(?:\[[\s\S]*?\])?\s*([\s\S]*?)\\end\{tikzpicture\}', s)
    assert m
    return m.group(1).strip()


def replace_body(s, new):
    return once(s, body(s), new)


finals = {}
new_label = r"\unsure{\tau'|\tau}_{\deleted{\unsure{\pi,\rho}}\inserted{r}}"
layer_b = r'\unsure{2\times60|\deleted{1\times120}\inserted{2\times60}}'
layer_c = r'\unsure{1\times120|\deleted{2\times60}\inserted{1\times120}}'
old_lower_equality = r'\unsure{1\times120=2\times60|2\times60=2\times60}'
article = r'\unsure{un|les}'
group = r'\unsure{\mathfrak G_K|\mathfrak S_K}'
cancelled_start = r'\deleted{2) \unsure{Éli.|Réduire}}'
live_type = r'\mathrm I_{\unsure{20|10}}'
relation_word = r'\unsure{relativement|relationnel|relèvement}'
gauches = r'\deleted{``\unsure{gauches}}'
replacement_adjective = r"\inserted{``tétraédrales''}"

# Table cells remain in the original array and original order.
k = 'S33-row420insert'
old_added_equation = r'120=1\times120=1\times120'
new_added_equation = r'120=1\times120=1\times\unsure{220|120}'
old_head = r'\draw[line width=1.1pt](-.4,.08)--(-.3,.05);'
new_head = r'\draw[line width=1.1pt](-.25,.16)--(-.4,.08)--(-.25,-.03);'
finals[k] = once(once(comp[k]['first'], old_added_equation,
                     new_added_equation), old_head, new_head)
change_page(old_added_equation, new_added_equation)
change_page(old_head, new_head)

k = 'S33-subtotal1020'
finals[k] = once(comp[k]['first'], r'\unsure{900}', r'\unsure{900|780}')
change_page(r'\unsure{900}', r'\unsure{900|780}')

finals['S33-row1020b'] = once(comp['S33-row1020b']['first'],
    r'120=2\times60=', '120=' + layer_b + '=')
finals['S33-row1020c'] = once(once(comp['S33-row1020c']['first'],
    r'120=1\times120=', '120=' + layer_c + '='),
    r"\unsure{\tau'_r|\tau_r^1}", new_label)
finals['S33-row1020e'] = once(comp['S33-row1020e']['first'],
    r'\unsure{2\times60=2\times60}', old_lower_equality)
old_rows = [
    r'120=2\times60=1\times120',
    r'120=2\times60=2\times60',
    r'120=1\times120=2\times60',
    r'120=1\times120=2\times60',
    r'\inserted{3\times}120=\deleted{\unsure{2\times60=2\times60}}\inserted{3\times40=3\times40}',
    r'120=2\times60=2\times60',
    r'60=1\times60=2\times30',
]
new_rows = old_rows[:]
new_rows[1] = '120=' + layer_b + r'=2\times60'
new_rows[2] = '120=' + layer_c + r'=2\times60'
new_rows[4] = once(new_rows[4], r'\unsure{2\times60=2\times60}', old_lower_equality)
change_page(('\\\\\n').join(old_rows), ('\\\\\n').join(new_rows))
change_page(r"\unsure{\tau'_r|\tau_r^1}", new_label)

k = 'S33-total'
finals[k] = once(once(comp[k]['first'], r'\unsure{1580|1500}',
    r'\unsure{1580|1380}'), r'\unsure{12}', r'\unsure{9|12}')
change_page(r'\unsure{1580|1500}', r'\unsure{1580|1380}')
change_page(r'\unsure{12}', r'\unsure{9|12}')

k = 'S33-programme1'
s = once(comp[k]['first'], r'\unsure{les|un}', article)
s = once(s, r'\unsure{\mathfrak S_K|\mathfrak G_K}', group)
s = once(s, r'sommets, se partageant entre \(9\) orbites)',
    r'sommets, se partageant \deleted{entre} \(9\) orbites)')
finals[k] = s
change_page(comp[k]['first'], s)

# Six handwritten lines, an independent upright, and a detached lower curve.
# The two strokes are not joined, closed into a box, or given an arrowhead.
margin_lines = [
    'en particulier,', 'écrire toutes les', 'flèches comme', 'composés de',
    'flèches ``provenant de', r"la dim. modulaire \(\leq1\)''",
]
margin_node = ('\n'.join([r'\node[anchor=north west,align=left,font=\small,text width=4cm] at (42,15) {',
    ('\\\\\n').join(margin_lines), '};']))
margin_strokes = '\n'.join([
    r'\draw[line width=.4pt] (28,5)--(28,255);',
    r'\draw[line width=.4pt] (0,282)..controls(82,292)and(192,299)..(348,299)..controls(411,299)and(472,297)..(524,301)--(526,319);',
])
margin_tikz = '\n'.join([
    r'\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round,line join=round]',
    margin_node, margin_strokes, r'\end{tikzpicture}',
])
finals['S33-margin'] = r'\margin{\figure{' + margin_tikz + '}}'
change_page(comp['S33-margin']['first'], finals['S33-margin'])

finals['S33-cancelled-start'] = cancelled_start
change_page(comp['S33-cancelled-start']['first'], cancelled_start)

k = 'S33-programme2-live'
s = once(comp[k]['first'], 'du niveau', r'\unsure{du|de} niveau')
s = once(s, r'\mathrm I_{10}', live_type)
finals[k] = s
change_page(comp[k]['first'], s)

k = 'S33-programme2-deleted'
s = once(comp[k]['first'], r'\deleted{et \(\mathrm{II}_1\) (',
    r'\deleted{et \(\mathrm{II}_1\) \deleted{\unsure{ceux}} (')
s = once(s, r'\unsure{qui}', r'\unsure{ceux|qui}')
s = once(s, r'\unsure{relationnel|relativement}', relation_word)
finals[k] = s
change_page(comp[k]['first'], s)

k = 'S33-programme3'
s = once(comp[k]['first'], r"\deleted{\unsure{gauches}} ``tétraédrales''",
    gauches + ' ' + replacement_adjective)
finals[k] = s
finals['S33-gauches'] = gauches
change_page(comp[k]['first'], s)  # The overlapping gauches box is not applied again.

# Drawing bodies retain the first global coordinates and first styles.
graphic_keys = ['S33-pants', 'S33-four_top', 'S33-four_middle',
                'S33-cancelled_drawing', 'S33-five_holes', 'S33-sphere_left',
                'S33-sphere_right', 'S33-large_surface', 'S33-isolated-arc']
gb = {k: body(comp[k]['first']) for k in graphic_keys}

k = 'S33-pants'
gb[k] = once(gb[k],
    r'(2369,263)..controls(2397,241)and(2422,210)..(2438,181)',
    r'(2346,271)..controls(2382,244)and(2409,209)..(2425,178)')
gb[k] += '\n' + '\n'.join([
    r'\draw[pencil] (2285,206)--(2308,145);',
    r'\draw[pencil] (2483,275)--(2517,244);',
])

D = Decimal
u = D('.68')
points = [(D('2725'), D('147')), (D('2751'), D('176')),
          (D('2741'), D('215')), (D('2725'), D('244'))]


def mix(a, b):
    return tuple((1-u)*x + u*y for x, y in zip(a, b))


def coord(point):
    return '(' + ','.join(format(x.normalize(), 'f') for x in point) + ')'


a = [mix(points[i], points[i+1]) for i in range(3)]
b = [mix(a[i], a[i+1]) for i in range(2)]
split = mix(b[0], b[1])
split_curve = '\n'.join([
    r'\draw[fine,dash pattern=on 1.2pt off 1.4pt] ' + coord(points[0])
    + '..controls' + coord(a[0]) + 'and' + coord(b[0]) + '..' + coord(split) + ';',
    r'\draw[fine] ' + coord(split) + '..controls' + coord(b[1]) + 'and'
    + coord(a[2]) + '..' + coord(points[3]) + ';',
])
k = 'S33-four_top'
gb[k] = once(gb[k],
    r'\draw[fine,dash pattern=on 1.2pt off 1.4pt] (2725,147)..controls(2751,176)and(2741,215)..(2725,244);',
    split_curve)
gb[k] += '\n' + '\n'.join([
    r'\draw[fine] (2676,274)--(2674,284)--(2679,284);',
    r'\draw[fine] (2595,141)--(2610,105);',
])

k = 'S33-four_middle'
old_triangles = '\n'.join([
    r'\draw[cut] (2408,408)--(2447,464)--(2508,415)--cycle;',
    r'\draw[cut] (2508,415)--(2509,379)--(2543,420)--cycle;',
])
new_cuts = '\n'.join([
    r'\draw[cut] (2408,408)..controls(2446,399)and(2488,402)..(2543,420);',
    r'\draw[cut] (2420,416)--(2447,464)--(2508,415)--(2507,373);',
    r'\draw[cut] (2507,373)--(2543,420);',
])
gb[k] = once(gb[k], old_triangles, new_cuts)

k = 'S33-cancelled_drawing'
native_cancelled = body(comp[k]['second'])
native_cancelled = once(native_cancelled,
    r'\draw[line width=.55pt] (187,82) .. controls (192,65) and (205,65) .. (202,48);',
    r'\draw[gray,line width=.35pt] (184,27) .. controls (212,31) and (214,62) .. (187,82);')
native_cancelled = once(native_cancelled,
    r'\draw[inkgreen,line width=1pt,dash pattern=on 4pt off 5pt] (144,28) -- (143,65) -- (189,82);',
    '\n'.join([
        r'\draw[inkgreen,line width=1pt,dash pattern=on 4pt off 5pt] (144,28) -- (143,65);',
        r'\draw[inkgreen,line width=1pt,dash pattern=on 4pt off 5pt] (55,67) .. controls (91,60) and (136,57) .. (187,82);',
        r'\draw[inkgreen,line width=1pt,dash pattern=on 4pt off 5pt] (143,65) .. controls (135,90) and (120,113) .. (110,122);',
    ]))
ratio = D('.006') / D('.019')


def scale_pt(m):
    return format((D(m.group(1))*ratio).quantize(D('.000000001')), 'f').rstrip('0').rstrip('.') + 'pt'


scaled_cancelled = re.sub(r'(?<![A-Za-z0-9.])([0-9]*\.?[0-9]+)pt',
                          scale_pt, native_cancelled)
gb[k] = '\n'.join([
    '% Cancellation is represented by the actual crossed strokes, with no abstract strike.',
    r'\begin{scope}[shift={(2621,369)}]',
    scaled_cancelled, r'\end{scope}',
])

k = 'S33-five_holes'
gb[k] = once(gb[k],
    r'(2382,727)..controls(2403,727)and(2434,729)..(2443,736)',
    r'(2392,725)..controls(2408,726)and(2432,728)..(2444,729)')
gb[k] = once(gb[k],
    r'(2443,736)..controls(2442,764)and(2437,781)..(2436,797)',
    r'(2444,729)..controls(2441,751)and(2438,773)..(2434,791)')
gb[k] += '\n' + '\n'.join([
    r'\draw[pencil] (2391,647)--(2364,653)--(2391,791);',
    r'\draw[pencil] (2252,587)--(2294,548);',
])

k = 'S33-sphere_left'
gb[k] = once(gb[k],
    r'\draw[fine,dash pattern=on 1.4pt off .8pt] (2330,1093)..controls(2369,1098)and(2405,1092)..(2442,1116);',
    '\n'.join([
        r'\draw[fine] (2329,1090)..controls(2365,1094)and(2397,1089)..(2418,1097);',
        r'\draw[fine] (2426,1101)..controls(2434,1103)and(2439,1110)..(2442,1116);',
    ]))


def translate_coordinates(s, dx=2548, dy=959):
    def xy(m):
        return coord((D(m.group(1))+D(dx), D(m.group(2))+D(dy)))
    return re.sub(r'\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)', xy, s)


k = 'S33-sphere_right'
left_rear = '\n'.join([
    r'\draw[fine] (112,146)..controls(112,143)and(113,141)..(114,139);',
    r'\draw[fine] (118,133)..controls(132,121)and(143,121)..(154,134);',
    r'\draw[fine] (112,160)..controls(116,176)and(140,187)..(151,181)..controls(158,176)and(160,168)..(161,162);',
])
gb[k] = once(gb[k],
    r'\draw[fine,dash pattern=on 1.3pt off .9pt] (2653,1105)..controls(2648,1084)and(2677,1075)..(2692,1092)..controls(2710,1115)and(2690,1146)..(2669,1138)..controls(2652,1133)and(2646,1120)..cycle;',
    translate_coordinates(left_rear))
second_right = body(comp[k]['second'])
right_commands = []
for first_point in ('277,153', '320,179'):
    pattern = r'\\draw\[line width=\.65pt\] \(' + re.escape(first_point) + r'\)[\s\S]*?;'
    matches = re.findall(pattern, second_right)
    assert len(matches) == 1
    right_commands.append(matches[0].replace(r'\draw[line width=.65pt]', r'\draw[fine]', 1))
gb[k] = once(gb[k],
    r'\draw[fine,dash pattern=on 1.5pt off .6pt] (2824,1112)..controls(2816,1091)and(2842,1093)..(2860,1106)..controls(2882,1123)and(2867,1152)..(2844,1144)..controls(2826,1144)and(2820,1129)..cycle;',
    translate_coordinates('\n'.join(right_commands)))
gb[k] = once(gb[k],
    r'\draw[fine] (2695,1104)..controls(2708,1110)and(2724,1111)..(2736,1111);',
    translate_coordinates(r'\draw[fine] (163,149)--(193,155);'))
gb[k] = once(gb[k],
    r'\draw[fine,dash pattern=on 1.4pt off 1pt] (2754,1111)..controls(2780,1115)and(2803,1117)..(2822,1112);',
    translate_coordinates(r'\draw[fine] (228,155)--(274,157);'))
gb[k] += '\n' + translate_coordinates('\n'.join([
    r'\draw[fine,line width=.35pt,dash pattern=on 1.4pt off 1.1pt] (278,73)--(269,169);',
    r'\draw[fine,line width=.35pt,dash pattern=on 1.4pt off 1.1pt] (259,180)--(253,213);',
]))

k = 'S33-large_surface'
gb[k] = once(gb[k],
    r'\draw[fine,line width=.7pt] (\x-8,\y)--(\x+8,\y) (\x-5,\y-7)--(\x+5,\y+7) (\x-5,\y+7)--(\x+5,\y-7);',
    r'\draw[fine,line width=.7pt] (\x-8,\y)--(\x+8,\y) (\x,\y-8)--(\x,\y+8) (\x-5,\y-7)--(\x+5,\y+7) (\x-5,\y+7)--(\x+5,\y-7);')

k = 'S33-isolated-arc'
gb[k] = once(gb[k],
    r'\draw[pencil] (1978,699)..controls(1976,753)and(2037,766)..(2056,724);',
    '\n'.join([
        r'\draw[pencil,line width=.35pt] (1980,717)..controls(1982,744)and(1997,756)..(2019,753)..controls(2036,753)and(2047,749)..(2053,737);',
        r'\draw[lightgray,line width=.2pt] (2054,734)--(2057,720);',
    ]))

for k in graphic_keys:
    change_page(body(comp[k]['first']), gb[k])
    finals[k] = replace_body(comp[k]['first'], gb[k])

# Synchronize established witness rows; no new row for coordinates, macros,
# candidate-only additions, or unasserted earlier layering.
changes = {r['place']: r for r in p['changes']}


def revise(place, key, **updates):
    ev = evidence(key)
    if 'final' not in updates:
        # Retain the earlier, more local letter/placement evidence when root
        # preserves that reading and supplies wider fixed-crop context.
        ev['ink'] = changes[place]['ink'] + ' Main-reader fixed-crop decision: ' + ev['ink']
    changes[place].update(ev | updates)


revise('Count table, second row label', 'S33-row180b')
revise('420 group, first equation, final factor', 'S33-row420a')
label_figure = finals['S33-row420insert'].split(' ', 1)[1]
revise('420 group, added row label and leader', 'S33-row420insert',
       final=label_figure, against_h=True)
revise('420 group, fourth row label', 'S33-row420c')
revise('1020 group, replacement subtotal', 'S33-subtotal1020',
       final=r'\begin{array}{r}\inserted{1020}\\\deleted{\unsure{900|780}}\end{array}')
revise('1020 group, deleted former subtotal', 'S33-subtotal1020',
       final=r'\deleted{\unsure{900|780}}')
revise('1020 group, second equation middle product', 'S33-row1020b',
       final='120=' + layer_b + r'=2\times60')
revise('1020 group, third equation middle product', 'S33-row1020c',
       final='120=' + layer_c + r'=2\times60')
revise('1020 group, second row label', 'S33-row1020b')
revise('1020 group, fifth row leading multiplier', 'S33-row1020e')
revise('1020 group, fifth row cancelled equality', 'S33-row1020e',
       final=r'\deleted{' + old_lower_equality + '}', against_c=True)
brace_place = '1020 group, right grouping brace'
revise(brace_place, 'S33-row1020c',
       final=once(changes[brace_place]['final'], r"\unsure{\tau'_r|\tau_r^1}", new_label),
       ink=changes[brace_place]['ink'] + ' The revised third label is retained within that brace. ' + root['S33-row1020c']['ink'])
revise('1020 group, last row label', 'S33-row1020g')
revise('Total, cancelled former value', 'S33-total',
       final=r'\deleted{\unsure{1580|1380}}')
revise('Total, double rule and replacement placement', 'S33-total',
       final=r'\begin{array}{r}\overline{\overline{\deleted{\unsure{1580|1380}}}}\\\inserted{1620}\end{array}')
revise('Total formula, current multiplier', 'S33-total', final='11', confidence='medium')
revise('Total formula, underlying multiplier', 'S33-total',
       final=r'\deleted{\unsure{9|12}}\inserted{11}')
revise('Programme 1, first word after déterminer', 'S33-programme1',
       final=article, against_c=False, against_h=True)
revise('Programme 1, entre before 14', 'S33-programme1-strikes')
revise('Programme 1, word replaced by orbites', 'S33-programme1-strikes')
revise('Programme 1, last word of cancelled phrase', 'S33-programme1-strikes')
revise('Programme 1, replacement orbites', 'S33-programme1-strikes')
revise('Programme 1, parenthetical word before 542', 'S33-programme1')
for place in ('Side note, composés', 'Side note, dimension abbreviation',
              'Side note, adjective after dim.'):
    revise(place, 'S33-margin')
revise('Programme 2, preposition before niveau', 'S33-programme2-live',
       final=r'\unsure{du|de}')
revise('Cancelled start, word following 2)', 'S33-cancelled-start',
       final=cancelled_start, against_c=True)
revise('Cancelled paragraph, short fragment before first repeated type',
       'S33-programme2-deleted', final=r'\unsure{ceux|qui} de type')
revise('Cancelled paragraph, word following twist', 'S33-programme2-deleted',
       final=relation_word, against_c=False, against_h=True)
revise('Cancelled paragraph, interlinear twist label', 'S33-programme2-deleted')
revise('Cancelled paragraph, un Autom. in the last line', 'S33-programme2-deleted')
revise('Programme 3, initial capital', 'S33-programme3')
revise('Programme 3, cancelled adjective', 'S33-gauches',
       final=gauches, against_c=True)
graphic_places = [
    'Upper three-ended surface', 'Upper four-opening surface',
    'Middle four-opening surface', 'Crossed drawing at middle right',
    'Five-opening surface with green cuts', 'Left lower sphere',
    'Right lower sphere', 'Large lower surface and marked rim',
    'Isolated pencil arc left of lower drawing group',
]
for key, place in zip(graphic_keys, graphic_places):
    revise(place, key, final=finals[key])


def add_change(place, key, c, h, final, kind, math, against_c=True, against_h=True):
    assert place not in changes
    p['changes'].append(dict(place=place, c=c, h=h, final=final, kind=kind,
        against_c=against_c, against_h=against_h, math=math, **evidence(key)))


add_change('420 group, inserted row final product', 'S33-row420insert',
    r'1\times120', r'1\times120', r'1\times\unsure{220|120}',
    'misread symbol or index', True)
add_change('1020 group, third label cancelled subscript and replacement',
    'S33-row1020c', r"\unsure{\tau'_r|\tau_r^1}", r"\tau'_r", new_label,
    'deletion state', True)
add_change('Programme 1, acting group', 'S33-programme1',
    r'\unsure{\mathfrak S}_K', r'\mathfrak{S}_K', group,
    'misread symbol or index', True)
add_change('Programme 1, entre before 9', 'S33-programme1',
    'entre', 'entre', r'\deleted{entre}', 'deletion state', False)
add_change('Side note, two independent framing strokes', 'S33-margin',
    '', r'\note{dans un cadre, à droite de 1) et 2)}',
    finals['S33-margin'], 'omission', False)
add_change('Programme 2, exceptional type subscript', 'S33-programme2-live',
    r'\mathrm I_{10}', r'\mathrm{I}_{10}', live_type,
    'misread symbol or index', True)
add_change('Cancelled paragraph, separately cancelled ceux', 'S33-programme2-deleted',
    '', '', r'\deleted{\unsure{ceux}}', 'omission', False)
add_change('Programme 3, replacement adjective insertion', 'S33-programme3',
    "``tétraédrales''", '« tétraédrales »', replacement_adjective,
    'insertion or placement', False)

marks = {r['id']: r for r in p['decisions']}
for mark, key, reading in [
    ('M0350', 'S33-row1020b', layer_b),
    ('M0351', 'S33-row1020c', layer_c),
    ('M0353', 'S33-row1020c', new_label),
    ('M0356', 'S33-programme1', group),
]:
    marks[mark].update(reading=reading, **evidence(key))
marks['M0353']['decision'] = 'undecided'
marks['M0356']['decision'] = 'undecided'

unresolved = {r['place']: r for r in p['unresolved']}


def doubt(place, key, reading, alternatives):
    record = dict(place=place, reading=reading, issue=root[key]['ink'],
                  alternatives=alternatives, confidence=root[key]['confidence'], **meta(key))
    if place in unresolved:
        unresolved[place].update(record)
    else:
        p['unresolved'].append(record)


doubt('1020 group, former subtotal', 'S33-subtotal1020',
      r'\deleted{\unsure{900|780}}', ['900', '780'])
doubt('1020 group, overwritten third label', 'S33-row1020c', new_label,
      [r"\tau'", r'\tau', r'cancelled \pi,\rho replaced by r'])
doubt('1020 group, cancelled fifth-row equality', 'S33-row1020e',
      r'\deleted{' + old_lower_equality + '}',
      [r'1\times120=2\times60', r'2\times60=2\times60'])
doubt('Total, cancelled former value', 'S33-total',
      r'\deleted{\unsure{1580|1380}}', ['1580', '1380'])
doubt('Total, former multiplier', 'S33-total',
      r'\deleted{\unsure{9|12}}', ['9', '12'])
doubt('Programme 1, article before syst.', 'S33-programme1', article, ['un', 'les'])
doubt('Programme 1, acting group', 'S33-programme1', group,
      [r'\mathfrak G_K', r'\mathfrak S_K'])
doubt('Cancelled start between items 1 and 2', 'S33-cancelled-start',
      cancelled_start, ['Éli.', 'Réduire'])
doubt('Cancelled paragraph, initial short fragment', 'S33-programme2-deleted',
      r'\unsure{ceux|qui} de type', ['ceux', 'qui'])
doubt('Cancelled paragraph, word after twist', 'S33-programme2-deleted',
      relation_word, ['relativement', 'relationnel', 'relèvement'])
doubt('Programme 3, cancelled adjective', 'S33-gauches', gauches,
      ['gauches', 'another cancelled adjective; opening quotes secure'])
doubt('420 group, inserted final numeral', 'S33-row420insert',
      r'\unsure{220|120}', ['220', '120'])
doubt('1020 group, second middle product layering', 'S33-row1020b', layer_b,
      [r'2\times60', r'possible overwritten 1\times120 under 2\times60'])
doubt('1020 group, third middle product layering', 'S33-row1020c', layer_c,
      [r'1\times120', r'possible overwritten 2\times60 under 1\times120'])
doubt('Programme 2, preposition before niveau', 'S33-programme2-live',
      r'\unsure{du|de}', ['du', 'de'])
doubt('Programme 2, exceptional type', 'S33-programme2-live', live_type, ['20', '10'])
doubt('Cancelled paragraph, separately crossed word', 'S33-programme2-deleted',
      r'\deleted{\unsure{ceux}}', ['ceux', 'another short cancelled word'])

inventory = {r['element']: r for r in p['inventory']}
inventory_updates = {
    'I033-03': new_added_equation + r'; circled \tau_r^0 with two-winged left arrowhead',
    'I033-05': r'\deleted{\unsure{900|780}}',
    'I033-08': r'\deleted{' + old_lower_equality + '}',
    'I033-10': 'brace enclosing the last five labels; third label has a cancelled subscript and replacement r',
    'I033-11': r'1620=5\times60+11\times120; cancelled 1580|1380 and coefficient9|12; double rule retained',
    'I033-12': r'\deleted{\unsure{1580|1380}}',
    'I033-14': r'\deleted{\unsure{9|12}}',
    'I033-18': r'1) déterminer \unsure{un|les} syst. fondamental; acting group G|S; second entre cancelled',
    'I033-22': 'en particulier; six handwritten lines, independent left upright and separate hooked lower curve',
    'I033-23': cancelled_start,
    'I033-24': r'2) Reprendre la question; \unsure{du|de} niveau0; exception ' + live_type,
    'I033-25': r'et II1; nested cancelled ceux; ceux|qui; twist; relativement|relationnel|relèvement; un Autom. de = type',
    'I033-27': r'3) Eliminer; cancelled opening quotes before gauches; inserted ``tétraédrales' + "''",
    'I033-28': gauches,
    'I033-29': 'pants: three mouths, solid front diagonal, dashed rear diagonal, internal and two outer pencil traces',
    'I033-30': 'four top: four mouths, angular lower-left hook; upper dashed/lower solid black partition; two dashed green routes',
    'I033-31': 'four middle: four mouths, three upper ticks, lower-left bar, three green paths with shared curved route and inside gap',
    'I033-32': 'cancelled native fragment: actual oblique cancellation strokes, black routes, pencil outer curl, three continuing green paths',
    'I033-33': 'five holes: dashed upper and continuous lower green routes, angular pencil precursor and upper-left pencil segment',
    'I033-34': 'left sphere: two solid front rings, broken rear ring, two locally continuous right rear-route pieces',
    'I033-35': 'right sphere: rear rings with local gaps, separated solid rear-route pieces, dark dashed meridian over pencil routes',
    'I033-36': 'large unfinished surface: six four-arm stars, six filled dots, twelve ticks, pencil retraces; no paper-perforation points',
    'I033-37': 'bounded shallow U-shaped front pencil arc and lighter upward right continuation',
}
for name, reading in inventory_updates.items():
    inventory[name]['first_words_or_objects'] = reading
inventory['I033-22'].update(kind='margin note and drawing',
    position='right of item1; two independent framing strokes, no closed box')
for element, kind, position, reading in [
    ('I033-41', 'deletion and insertion', 'third label in1020 group', new_label),
    ('I033-42', 'deletion', 'item1 before9 orbites', r'\deleted{entre}'),
    ('I033-43', 'deletion', 'inside the large cancelled paragraph, after firstII1', r'\deleted{\unsure{ceux}}'),
    ('I033-44', 'insertion', 'above/right of crossed gauches in item3', replacement_adjective),
]:
    assert element not in inventory
    p['inventory'].append(dict(element=element, kind=kind, position=position,
        first_words_or_objects=reading, sheet_kind='reused_typed', hand='his hand', transcribed='yes'))

notes = {r['id']: r for r in p['notes']}
notes['N033-01']['text'] = (
    'The manuscript is on a reused listing sheet. The pale mirrored mechanical printing '
    'is reverse-side show-through, not front-face source text. The isolated front pencil '
    'arc is bounded to its open shallow U and lighter right continuation; the former '
    'high start in unrelated mirrored lettering is removed.')
notes['N033-03']['text'] = (
    'The inserted row in the420 group ends in1×220|120, with220 favored but doubtful. '
    'Its circled tau_r^0 has a curved leftward shaft and two angular wings. '
    'The former subtotal remains900|780 under inserted1020. The third lower label '
    'retains tau-prime|tau with cancelled doubtful pi,rho and inserted r.')
notes['N033-04']['text'] = (
    'The live middle factors remain2×60 in the second lower row and1×120 in the third. '
    'Possible earlier1×120 and2×60 layers are represented as alternatives, not asserted '
    'cancellations. In the fifth row, the cancelled equality favors1×120=2×60 over '
    '2×60=2×60; the inserted leading3× and both3×40 factors remain unchanged.')
notes['N033-05']['text'] = (
    'The cancelled total is1580|1380, and the older coefficient under inserted11 is9|12. '
    'The computations5×60+9×120=1380 and5×60+11×120=1620 identify arithmetic possibilities '
    'only. They do not prove the obscured ink. Likewise the pre-insertion lower-row sum780 '
    'does not displace the favored cancelled-subtotal reading900.')
notes['N033-06']['text'] = (
    'The large cancellation covers the full paragraph beginning etII1. A separately '
    'crossed doubtful ceux follows the first type and stays nested inside that deletion. '
    'The parenthetical beginning is ceux|qui; relativement is favored over relationnel '
    'and relèvement. The interlinear tw_{1/6} stays inside the cancellation; its slanted '
    'leader is not an extra slash. Au twist, mais - Attention, and un Autom. de = type remain.')
notes['N033-07']['text'] = (
    'The side note retains composés and la dim. modulaire≤1. Its six handwritten lines '
    'are accompanied by an independent left upright and a detached lower curved stroke '
    'ending in a small downward hook. They are not joined into a closed box and have '
    'no arrowheads. The cancelled final line retains = as the written same-type shorthand.')
notes['N033-09']['text'] = (
    'All eight main drawings, the isolated pencil arc, grouping curves and divider remain '
    'in the first global TikZ placement. Only the cancelled fragment uses the approved '
    'second native trace, translated by(2621,369), with point widths and dash lengths '
    'multiplied by.006/.019. Root specified local gaps, solid/dashed transitions, '
    'pencil continuations, hooks and green continuations. The large rim retains6stars, '
    '6dots and12ticks, with the vertical arm restored to each star. Paper perforations '
    'are excluded. Coordinate refinements receive no new substantive C/H row.')
notes['S033-C01']['text'] = (
    'The first equality in the420 group remains60=1×60=4×60. The final product is240; '
    'the unequal written chain is preserved.')
notes['S033-C04']['text'] = (
    'The fifth row of the1020 group remains3×120=3×40=3×40. Its left value is360 and '
    'the two right values are120. This unequal chain is preserved without correction.')
p['notes'].extend([
    dict(id='N033-NOTATION', type='completed root notation revisit', text=(
        'Root favorsI_{20} while retainingI_{10} in the scan033 live exception atniveau0. '
        'The comparison supplied by root putsI_{10} atniveau2 on scan031; that different '
        'level does not settle this sentence. The reading remainsI_{20|10}, withdu|de '
        'also unresolved. No forced harmonization or scan031 edit was made.')),
    dict(id='N033-PROGRAMME', type='main-reader adjudication', text=(
        'Item1 favorsun|les and ornateG_K|S_K, retainsaux|avec andsommets, and cancels '
        'the second entre before9orbites. The crossed earlier2) beginsÉli.|Réduire; '
        'the abbreviation stop is retained. Item3 keeps plainEliminer and the opening '
        'quotes before doubtfulgauches, without supplying closing quotes. The quoted '
        'tétraédrales is a replacement insertion. The overlapping programme3/gauches '
        'boxes are represented only once in the page.')),
    dict(id='N033-BLIND', type='main-reader adjudication', text=(
        'Root personally viewed all34 differing fixed crops and supplied22 revised '
        'decisions in the final root working JSON. This script applies those decisions '
        'mechanically; it does not make a new ink judgment. All first/second/boxes/'
        'comparison/token TSVs are preserved byte for byte. Existing C/H rows are '
        'synchronized, with no new row for coordinate, macro, or added-doubt-only '
        'changes. No image reading, OCR, external research, TeX compilation, '
        'record_audit, shared-log edit, or shared-output rebuild was performed.')),
])

# All new numerical checks are explicitly computations, never ink evidence.
assert 5*60 + 9*120 == 1380 and 5*60 + 11*120 == 1620
assert 6*120 + 60 == 780 and 780 + (3*120-120) == 1020
for statement_id, outcome in [
    ('S033-C05', '5×60+9×120=1380;5×60+11×120=1620. These are computations only and do not identify cancelled digits.'),
    ('S033-C06', '6×120+60=780;780+(3×120−120)=1020. This pre-insertion/current count comparison is computation only, not proof of the obscured subtotal.'),
]:
    assert all(r['statement_id'] != statement_id for r in p['checks'])
    p['checks'].append(dict(statement_id=statement_id, date='2026-11-21',
        who='mechanical implementer, GPT-6 Astra Pro; arithmetic requested by root',
        type='computation or formal certificate', outcome=outcome))
    p['notes'].append(dict(id=statement_id, type='computation', text=outcome))

p['hand_log'][0]['holds_at_every_observed_occurrence'] = (
    'Yes for unobscured gamma forms on this page; root favors tau-prime|tau for the '
    'overwritten third lower label, whose cancelled subscript and replacement r remain explicit.')
p['hand_log'][1].update(
    habit='The clear primes are short detached strokes without the entry and full baseline foot of the explicit numerical1; the overwritten third tau remains tau-prime|tau.',
    holds_at_every_observed_occurrence='Clear labels support the contrast; the crowded third label is retained under doubt.',
    witness_effect='M0349 andM0354 retain prime alternatives; M0353 now includes the cancelled pi,rho subscript and inserted r.')
p['hand_log'][4].update(
    habit='The acting-group glyph has a large open loop and an inner return bar, favoring ornate G over S.',
    holds_at_every_observed_occurrence='One local occurrence; G|S remains uncertain.',
    witness_effect='The favored reading is reversed to G_K|S_K after root inspection; no group identity is inferred.')
p['hand_log'].append(dict(pages=[33],
    habit='The small first subscript digit in the live exception has a curved top and low curled return, favoring2 but also admitting a compact hooked1.',
    holds_at_every_observed_occurrence='Local uncertainty only; root supplied the scan031 comparison without treating its different level as decisive.',
    witness_effect='Both witnesses haveI10; the final reading favorsI20 while retainingI10.'))
for n in p['notation']:
    if n['form'] == r'\unsure{\mathfrak S_K|\mathfrak G_K}':
        n.update(form=group, meaning='Ornate G is favored over S; the acting group is not identified from mathematical expectation.')
p['notation'].extend([
    dict(form=new_label, meaning='Third lower count label: uncertain tau-prime/tau, cancelled doubtful pi,rho, inserted r.', place='third row of1020 group'),
    dict(form=live_type, meaning='Live exception atniveau0;20 is favored while10 remains possible. Root’s031 I10 atniveau2 does not settle it.', place='programme2 live clause'),
])

diff_notes = {
    311: 'Inserted1020 and cancelled900|780 retain their positions; arithmetic780 does not settle the obscured ink.',
    312: 'Cancelled older equality favors1×120=2×60 with2×60=2×60 retained; inserted3× and both3×40 factors remain.',
    314: 'Tau-prime|tau remains doubtful; the omitted cancelled pi,rho subscript and replacement r are now explicit.',
    323: 'Cancelled1580|1380, double rules, inserted1620 and older coefficient9|12 are retained; arithmetic is separately labeled computation.',
    331: 'Un|les remains doubtful withun favored; syst. and singularfondamental stay as read.',
    339: 'Delimiter syntax is not substantive; the independently revised favored group reading isG_K|S_K and is recorded separately.',
    344: 'Se is retained, and the second entre before9orbites is cancelled.',
    347: 'Cancelled2)Éli.|Réduire remains doubtful; six-line margin note and two independent framing strokes are represented separately.',
    353: 'Cancelled2) is clear; abbreviatedÉli. is favored overRéduire, with its stop retained.',
    355: 'Du|de niveau0 and exceptionalI20|10 remain unresolved; no harmonization with031 I10 atniveau2 is imposed.',
    362: 'A separately cancelled doubtfulceux precedes the parenthesis; its first word isceux|qui, followed byde type.',
    368: 'Relativement is favored overrelationnel andrelèvement. Au twist and the insertedtw1/6 remain; no standalone slash is supplied.',
    372: 'Opening quotes precede cancelled doubtfulgauches; no closing pair is supplied there. Quotedtétraédrales is a replacement insertion.',
    374: 'First global drawing placement retained with root-specified refinements; bounded pencil arc retained, mirrored printing and paper perforations excluded;32 foliation unchanged.',
}
for r in p['differences_review']:
    if r['source_row'] in diff_notes:
        r['note'] = diff_notes[r['source_row']]

p['blind_graphic_transforms'] = {
    'S33-cancelled_drawing': dict(native_origin=[2621, 369], native_clip=[0, 0, 226, 151],
        source_coordinate_cm='.019', target_coordinate_cm='.006', coordinate_scale=1,
        absolute_pt_width_and_dash_multiplier='6/19', outer_deleted_wrapper_removed=True,
        cancellation='actual strokes only'),
    'S33-four_top': dict(operation='de Casteljau split at t=.68',
        split_point=[str(v) for v in split], first_part='dashed fine black', second_part='solid fine black'),
    'S33-sphere_right': dict(local_origin=[2548, 959], coordinate_scale=1,
        first_global_coordinate_cm='.006', translated_second_commands=2,
        note='Local solid ring pieces and rear routes use first fine black weight; added dark meridian uses.35pt, on1.4pt off1.1pt.'),
    'S33-margin': dict(handwritten_lines=6, independent_framing_paths=2,
        coordinate_cm='.01', text_node=[42, 15], left_upright=[[28, 5], [28, 255]],
        lower_curve_end=[524, 301], downward_hook_end=[526, 319],
        closed_box=False, arrowheads=False),
}

entries = []
for item in working:
    entry = {k: v for k, v in item.items() if k != 'instructions'}
    entry.update(crop=meta(item['box'])['crop'], crop_box=meta(item['box'])['box'],
                 final=finals.get(item['box'], comp[item['box']]['first']))
    entries.append(entry)

# Exact mechanical checks of the requested edit set; no TeX execution.
assert set(finals) == {k for k, r in root.items() if r['choice'] == 'revised'}
assert len(entries) == 34 and len(finals) == 22
assert all(e['viewed_by_main'] is True for e in entries)
assert all((B/e['crop']).is_file() for e in entries)
assert t.count('Programme de travail :') == 1
assert t.count(gauches) == 1 and t.count(replacement_adjective) == 1
assert t.count(r'\deleted{entre}') == 2
assert t.count(r'\deleted{\unsure{ceux}}') == 1
assert t.count(new_label) == 1 and t.count(live_type) == 1
assert r'60=1\times60=4\times60' in t
assert new_rows[4] in t and r'\inserted{3\times40=3\times40}' in t
assert r'\overline{\overline{\deleted{\unsure{1580|1380}}}}' in t
assert r'\deleted{\unsure{9|12}}\inserted{11}' in t
assert r'\mathrm{III}_1' in t and original.count(r'\mathrm{III}_1') == t.count(r'\mathrm{III}_1')
assert r'\x27' not in t and all(r'\x27' not in e['final'] for e in entries)
assert len(margin_lines) == 6 and margin_node.count('\\\\\n') == 5
assert margin_strokes.count(r'\draw') == 2 and '--cycle' not in margin_strokes
assert '->' not in margin_strokes and '<-' not in margin_strokes
assert t.count(margin_tikz) == 1
for k in graphic_keys:
    assert t.count(gb[k]) == 1
assert gb['S33-four_middle'].replace(new_cuts, old_triangles) == body(comp['S33-four_middle']['first'])
assert t[t.index('% S033 grouping'):t.index('% S033 large_surface')] == original[original.index('% S033 grouping'):original.index('% S033 large_surface')]
assert r'\draw[cut] (2728,150)..controls(2752,182)and(2741,219)..(2729,243);' in t
assert r'\draw[cut] (2648,205)..controls(2698,190)and(2756,191)..(2797,201);' in t
assert r'(2450,367)--(2451,373) (2458,369)--(2459,374) (2467,369)--(2468,374)' in t
assert r'(2394,458)--(2408,455)' in t
assert r'(2745,1310)--(2715,1310)--(2737,1320)' in t
assert r'(2783,1304)--(2808,1296)--(2796,1308)' in t
assert r'(\x,\y-8)--(\x,\y+8)' in t
assert t.count(r'\fill (\x,\y) circle[radius=.7pt]') == 1
assert r'\deleted{' not in gb['S33-cancelled_drawing']
assert r'\begin{tikzpicture}' not in gb['S33-cancelled_drawing']
assert gb['S33-cancelled_drawing'].count(r'\clip') == 1
original_pts = [D(v) for v in re.findall(r'(?<![A-Za-z0-9.])([0-9]*\.?[0-9]+)pt', native_cancelled)]
scaled_pts = [D(v) for v in re.findall(r'(?<![A-Za-z0-9.])([0-9]*\.?[0-9]+)pt', scaled_cancelled)]
assert len(original_pts) == len(scaled_pts)
assert all(abs(y-x*ratio) <= D('.0000000005') for x,y in zip(original_pts, scaled_pts))
level = 0
for m in re.finditer(r'(?<!\\)[{}]', t):
    level += 1 if m.group() == '{' else -1
    assert level >= 0, m.start()
assert level == 0
for env in ('tikzpicture', 'scope', 'array'):
    assert t.count(r'\begin{' + env + '}') == t.count(r'\end{' + env + '}'), env
assert len(p['changes']) == 68 and len(p['inventory']) == 44
assert len(p['decisions']) == 100 and len(p['unresolved']) == 21
assert len(p['checks']) == 6
assert all(r['type'] == 'computation or formal certificate' for r in p['checks'])
assert all(sha(f) == protected_hashes[str(f)] for f in protected)
assert sha(working_path) == working_hash, 'Root working file changed during the run.'


def atomic(path, text):
    tmp = path.with_name(path.name + '.tmp')
    with tmp.open('w', encoding='utf-8', newline='') as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


parser = argparse.ArgumentParser()
parser.add_argument('--apply', action='store_true')
args = parser.parse_args()
if args.apply:
    atomic(page, t)
    atomic(review_path, json.dumps(p, ensure_ascii=False, indent=2) + '\n')
    atomic(adjudication_path, json.dumps(entries, ensure_ascii=False, indent=2) + '\n')
    assert all(sha(f) == protected_hashes[str(f)] for f in protected)
print(json.dumps(dict(scan=33, applied=args.apply, adjudications=len(entries),
    revised_boxes=len(finals), changes_rows=len(p['changes']),
    against_c=sum(bool(r['against_c']) for r in p['changes']),
    against_h=sum(bool(r['against_h']) for r in p['changes']),
    mark_decisions=len(p['decisions']), unresolved=len(p['unresolved']),
    inventory_rows=len(p['inventory']), computation_checks=len(p['checks']),
    native_pt_scale='6/19', split_point=[str(v) for v in split],
    protected_tsv_hashes_unchanged=True, root_working_sha256=working_hash,
    shared_outputs_rebuilt=False, record_audit_run=False)))


def apply_root_margin_followup_20261121():
    """Guarded root correction, run independently of the non-idempotent main pass.

    Execute this function definition alone (the recorded invocation extracts its
    AST), then call it. Do not execute the top-level main pass again. The exact
    native frame coordinates were supplied by root after reviewing the same crop.
    """
    from pathlib import Path
    import hashlib
    import json
    import os

    base = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148')
    page_path = base / 'pages/148_scan033.tex'
    review_file = base / 'reviews/148_scan033.json'
    adjud_file = base / 'second/148_scan033_adjudications.json'
    current_page = page_path.read_text(encoding='utf-8')
    review = json.loads(review_file.read_text(encoding='utf-8'))
    adjudications = json.loads(adjud_file.read_text(encoding='utf-8'))
    protected_files = [base / ('second/148_scan033' + suffix) for suffix in (
        '_first.tsv', '_second.tsv', '_boxes.tsv', '_comparison.tsv',
        '_token_differences.tsv')]
    hashes = {str(f): hashlib.sha256(f.read_bytes()).hexdigest()
              for f in protected_files}
    assert len(adjudications) == 34
    assert sum(r['choice'] == 'revised' for r in adjudications) == 22
    counts = {key: len(review[key]) for key in
              ('changes', 'decisions', 'unresolved', 'inventory', 'checks')}
    assert counts == dict(changes=68, decisions=100, unresolved=21,
                          inventory=44, checks=6)
    margin = next(r for r in adjudications if r['box'] == 'S33-margin')
    frame_row = next(r for r in review['changes']
                     if r['place'] == 'Side note, two independent framing strokes')
    original_margin = margin['final']
    old_upright = r'\draw[line width=.4pt] (28,5)--(28,255);'
    old_curve = r'\draw[line width=.4pt] (0,282)..controls(82,292)and(192,299)..(348,299)..controls(411,299)and(472,297)..(524,301)--(526,319);'
    new_upright = r'\draw[line width=.4pt] (16,11)--(26,307);'
    new_curve = r'\draw[line width=.4pt] (0,264)..controls(8,299)and(25,321)..(60,329)..controls(100,329)and(130,323)..(150,327)--(153,334);'
    old_break = '\\\\\n'
    new_break = '\\\\[.08cm]\n'
    already_applied = new_upright in original_margin and new_curve in original_margin
    if already_applied:
        assert old_upright not in original_margin and old_curve not in original_margin
        corrected_margin = original_margin
    else:
        assert original_margin.count(old_upright) == original_margin.count(old_curve) == 1
        assert original_margin.count(old_break) == 5
        corrected_margin = original_margin.replace(old_upright, new_upright, 1)
        corrected_margin = corrected_margin.replace(old_curve, new_curve, 1)
        corrected_margin = corrected_margin.replace(old_break, new_break)
        # Explicit breaks alone determine the six lines; no automatic text-width wrap.
        corrected_margin = corrected_margin.replace(',text width=4cm', '', 1)
    assert corrected_margin.count(new_break) == 5
    assert corrected_margin.count(r'\draw') == 2
    assert corrected_margin.count(new_upright) == corrected_margin.count(new_curve) == 1
    assert ',text width=' not in corrected_margin
    assert '--cycle' not in corrected_margin and '->' not in corrected_margin
    assert current_page.count(original_margin) == 1
    assert frame_row['final'] == original_margin
    before_nonmargin = [r for r in adjudications if r['box'] != 'S33-margin']
    new_page = current_page.replace(original_margin, corrected_margin, 1)
    assert current_page.replace(original_margin, '', 1) == new_page.replace(corrected_margin, '', 1)
    correction_ink = (
        ' Root supplied the exact framing geometry: upright(16,11) to(26,307); '
        'detached lower curve from(0,264), through the two specified cubic segments, '
        'to(150,327), then a short hook to(153,334). The lower stroke ends near '
        'one quarter of the note width; it does not run beneath the full note.')
    if not already_applied:
        margin['final'] = corrected_margin
        margin['ink'] += correction_ink
        frame_row['final'] = corrected_margin
        frame_row['ink'] += correction_ink
    inventory_note = next(r for r in review['inventory'] if r['element'] == 'I033-22')
    inventory_note['first_words_or_objects'] = (
        'en particulier; six handwritten lines; independent near-vertical left '
        'stroke and short detached lower curve ending near one quarter of note '
        'width with a small downward hook')
    inventory_note['position'] = (
        'right of item1; independent upright and short lower curve, not a closed box')
    note = next(r for r in review['notes'] if r['id'] == 'N033-07')
    note['text'] = (
        'The side note retains composés and la dim. modulaire≤1 in six explicit '
        'lines. An independent near-vertical left stroke runs from(16,11) to '
        '(26,307). The detached lower curve starts at(0,264), turns beneath the '
        'left part of the note, reaches(150,327), and ends in a short downward '
        'hook at(153,334), near one quarter of note width. The strokes are not '
        'joined and have no arrowheads. The first five line breaks receive.08cm '
        'additional spacing; no automatic text-width wrapping is imposed. The '
        'cancelled final line retains=as the written same-type shorthand.')
    review['blind_graphic_transforms']['S33-margin'] = dict(
        handwritten_lines=6, explicit_internal_line_breaks=5,
        extra_line_spacing_cm='.08', automatic_text_width_wrap=False,
        independent_framing_paths=2, coordinate_cm='.01', text_node=[42, 15],
        left_upright=[[16, 11], [26, 307]], lower_curve_start=[0, 264],
        lower_curve_controls=[[[8, 299], [25, 321]], [[100, 329], [130, 323]]],
        lower_curve_segment_ends=[[60, 329], [150, 327]],
        lower_curve_end=[150, 327], downward_hook_end=[153, 334],
        lower_curve_extent='about one quarter of note width',
        closed_box=False, arrowheads=False,
        authority='Exact native coordinates supplied by root in the follow-up; no new ink judgment.')
    assert before_nonmargin == [r for r in adjudications if r['box'] != 'S33-margin']
    assert counts == {key: len(review[key]) for key in counts}
    assert sum(r['choice'] == 'revised' for r in adjudications) == 22
    assert all(hashlib.sha256(f.read_bytes()).hexdigest() == hashes[str(f)]
               for f in protected_files)

    def atomic_followup(path, content):
        tmp = path.with_name(path.name + '.tmp')
        with tmp.open('w', encoding='utf-8', newline='') as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)

    if not already_applied:
        atomic_followup(page_path, new_page)
        atomic_followup(review_file, json.dumps(review, ensure_ascii=False, indent=2) + '\n')
        atomic_followup(adjud_file, json.dumps(adjudications, ensure_ascii=False, indent=2) + '\n')
    else:
        assert json.loads(review_file.read_text()) == review
    assert all(hashlib.sha256(f.read_bytes()).hexdigest() == hashes[str(f)]
               for f in protected_files)
    result = dict(scan=33, followup='root margin geometry', already_applied=already_applied,
        six_explicit_lines=True, independent_strokes=2, lower_curve_end=[150, 327],
        downward_hook_end=[153, 334], choices_unchanged=True, counts=counts,
        protected_tsv_hashes_unchanged=True, main_pass_rerun=False,
        record_audit_run=False, shared_outputs_rebuilt=False)
    print(json.dumps(result))
    return result
