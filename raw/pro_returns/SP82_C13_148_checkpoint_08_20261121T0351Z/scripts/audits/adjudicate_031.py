#!/usr/bin/env python3
"""Apply the main reader's completed scan031 adjudications once.

All 53 differing crops were personally viewed by root. This script performs
mechanical transcription and record synchronization only. It does not inspect
images, compile TeX, run record_audit, rebuild, or modify shared logs.
"""
from pathlib import Path
from decimal import Decimal
import csv
import hashlib
import json
import re
import sys

B = Path(__file__).resolve().parents[2]
stem = B / 'second/148_scan031'
page = B / 'pages/148_scan031.tex'
review_path = B / 'reviews/148_scan031.json'
adjudication_path = Path(str(stem) + '_adjudications.json')


def load_tsv(suffix):
    with Path(str(stem) + suffix).open() as f:
        return {r['box']: r for r in csv.DictReader(f, delimiter='\t')}


def resolve_level_zero_index(review, entry, crop):
    """Apply root's late013 decision without adding a certainty-only C/H row."""
    changed = False
    for row in review['changes']:
        if row['place'] == 'Level0 middle type index and absent prime':
            row.update(final=r'\mathrm{III}_4', ink=entry['ink'],
                       confidence='high', **crop)
            changed = True
    assert changed
    old_count = len(review['unresolved'])
    review['unresolved'] = [
        u for u in review['unresolved'] if u['place'] != 'level0 middle index']
    assert len(review['unresolved']) == old_count - 1
    for note in review['notes']:
        if note['id'] == '148-031-N15':
            note['text'] = (
                'The main reader re-viewed the complete fixed level-table crop and '
                'compared the middle lower index with the clear4 in I4 on its top '
                'row. Its angled arm crosses a separate upright and rightward bar: '
                'the table reads III4. The corresponding main block retains III1, '
                'so this author index inconsistency remains literal. No arithmetic '
                'or expected label changes the source. Additional H differences at '
                'retained doubtful glyphs, struck entries, the level2 underline and '
                'foliation remain recorded.')
    for inv in review['inventory']:
        if inv['element'] == 'level table':
            inv['first_words_or_objects'] = (
                'niveau2; niveau1; niveau0 with middle III4, unlike main III1 heading; '
                '62,240,240 and overline542 unchanged')
    review['notation'].append(dict(
        form=r'\mathrm{III}_4', pages=[31],
        observed_use='Middle index in the niveau0 row of the level table.',
        caution=(
            'Root identifies the same angled arm, separate upright and bar as the '
            'clear4 in I4 in this crop. The main block is headed III1; retain the '
            'author index inconsistency without normalizing either occurrence.')))
    review['hand_log'].append(dict(
        pages=[31], hand='his hand', holds_at_every_observed_occurrence=True,
        witness_effect=(
            'The existing Level0 C/H correction retains4 and now resolves its '
            'earlier1 alternative; no extra certainty-only correction is counted.'),
        habit=(
            'Within the complete level-table crop, the angled left arm crossing '
            'a separate upright and rightward bar identifies the lower middle4 '
            'by comparison with the clear4 in I4 on the top row.')))
    review['notes'].append(dict(
        id='148-031-INDEX', type='completed root index revisit',
        text=(
            'The later root decision for031_c_013 resolves the favored4 in the '
            'niveau0 middle index while preserving the main III1 heading. The '
            'existing C/H row is updated and the resolved doubt removed. The '
            'source MARKS list for scan031 and its48 review decisions contain no '
            'corresponding table-index ID; no new MARKS identifier is invented.')))


# The base pass ran once with21 revisions. Root then authorized one additional
# decision013. This guarded follow-up ran once; the ordinary path below also
# reproduces the complete22-decision result from the original page.
if sys.argv[1:] == ['--root-followup-013']:
    current = page.read_text()
    review = json.loads(review_path.read_text())
    entries = json.loads(adjudication_path.read_text())
    root_entries = json.loads(Path(str(stem) + '_root_working.json').read_text())
    updated = next(e for e in root_entries if e['box'] == '031_c_013')
    assert updated['choice'] == 'revised' and updated['confidence'] == 'high'
    old_entry = next(e for e in entries if e['box'] == '031_c_013')
    assert old_entry['choice'] == 'first', 'Non-idempotent:013 follow-up already applied.'
    assert not review.get('second_audit'), 'Root audit already recorded; do not overwrite it.'
    assert sum(e['choice'] == 'revised' for e in entries) == 21
    old = r'\mathrm{III}_{\unsure{4|1}}'
    new = r'\mathrm{III}_4'
    assert current.count(old) == 1
    new_page = current.replace(old, new, 1)
    comparison = load_tsv('_comparison.tsv')
    rect = load_tsv('_boxes.tsv')['031_c_013']
    crop = dict(crop='crops/second/148_scan031/031_c_013.jxl',
                box=[int(rect[k]) for k in ('x0', 'y0', 'x1', 'y1')])
    new_entry = {k: v for k, v in updated.items() if k != 'instructions'}
    new_entry.update(final=comparison['031_c_013']['first'].replace(old, new, 1),
                     crop=crop['crop'], crop_box=crop['box'])
    entries[entries.index(old_entry)] = new_entry
    resolve_level_zero_index(review, updated, crop)
    locked = [Path(str(stem) + s) for s in
              ('_first.tsv', '_second.tsv', '_boxes.tsv',
               '_comparison.tsv', '_token_differences.tsv')]
    hashes = {str(f): hashlib.sha256(f.read_bytes()).hexdigest() for f in locked}
    assert sum(e['choice'] == 'revised' for e in entries) == 22
    assert len(review['changes']) == 83 and len(review['decisions']) == 48
    assert len(review['unresolved']) == 15
    assert new_page.count(r'\mathrm{III}_1\ (\text{triple triangle sem.-gauche})') == 1
    assert new_page.count(r'\mathrm{I}_{10}') == current.count(r'\mathrm{I}_{10}')
    assert all(hashlib.sha256(f.read_bytes()).hexdigest() == hashes[str(f)] for f in locked)
    page.write_text(new_page)
    review_path.write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n')
    adjudication_path.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(scan=31, followup='013', adjudications=len(entries),
                         revised_boxes=22, changes_rows=83, decisions=48,
                         unresolved=15, protected_tsv_hashes_unchanged=True)))
    raise SystemExit
assert not sys.argv[1:], 'Only --root-followup-013 is supported.'


comp = load_tsv('_comparison.tsv')
boxes = load_tsv('_boxes.tsv')
working = json.loads(Path(str(stem) + '_root_working.json').read_text())
root = {e['box']: e for e in working}
p = json.loads(review_path.read_text())
t = page.read_text()
original = t
assert not adjudication_path.exists() and not p.get('second_audit'), \
    'Non-idempotent: scan031 adjudication has already been applied.'
assert len(working) == 53 and sum(e['choice'] == 'revised' for e in working) == 22
assert set(root) == {k for k, c in comp.items() if c['different'] == 'yes'}
protected = [
    Path(str(stem) + suffix)
    for suffix in ('_first.tsv', '_second.tsv', '_boxes.tsv',
                   '_comparison.tsv', '_token_differences.tsv')
]
protected_hashes = {str(f): hashlib.sha256(f.read_bytes()).hexdigest()
                    for f in protected}


def key(n):
    return f'031_c_{n:03d}'


def once(s, old, new):
    assert s.count(old) == 1, (old[:120], s.count(old))
    return s.replace(old, new, 1)


def change_page(old, new):
    global t
    t = once(t, old, new)


def meta(n):
    b = boxes[key(n)]
    return {
        'crop': f'crops/second/148_scan031/{key(n)}.png',
        'box': [int(b[k]) for k in ('x0', 'y0', 'x1', 'y1')],
    }


def evidence(n):
    return dict(ink=root[key(n)]['ink'],
                confidence=root[key(n)]['confidence'], **meta(n))


finals = {}

# Local text revisions retain the established line/cell layout in the page.
finals[key(3)] = once(comp[key(3)]['first'], r'K\simeq', 'K=')
finals[key(3)] = once(finals[key(3)],
                      r'\text{ens. des diagonales }\alpha',
                      r'\text{ens. des diagonales de}')
change_page(r'K\simeq\{P\}\amalg I', r'K=\{P\}\amalg I')
change_page(r'\text{ens. des diagonales }\alpha',
            r'\text{ens. des diagonales de}')

cancel_group = r'\deleted{\unsure{\mathbb Z_2|1}}'
finals[key(6)] = once(comp[key(6)]['first'],
                      r'\deleted{\unsure{1}}', cancel_group)
change_page(r'\deleted{\unsure{1}}', cancel_group)

# Root's completed cross-page revisit retains both originally primed forms.
assert root[key(11)]['choice'] == root[key(28)]['choice'] == 'first'
heading = r"\mathrm{III}'_2"
new_heading = heading + r'\ (\text{triple triangle gauche})'

ending = r'\unsure{codiagonales|codiagonale}'
lower_phrase = (r'\inserted{str.} \unsure{carré|carrée} en '
                r'\unsure{codiagonales|codiagonale}')
f12 = comp[key(12)]['first']
assert f12.count('codiagonales') == 2
f12 = f12.replace('codiagonales', ending)
f12 = once(f12, r'\inserted{str.} carré en',
            r'\inserted{str.} \unsure{carré|carrée} en')
finals[key(12)] = f12
assert t.count('codiagonales') == 2
t = t.replace('codiagonales', ending)
change_page(r'\inserted{str.} carré en',
            r'\inserted{str.} \unsure{carré|carrée} en')

finals[key(13)] = once(comp[key(13)]['first'],
                       r'\mathrm{III}_{\unsure{4|1}}', r'\mathrm{III}_4')
change_page(r'\mathrm{III}_{\unsure{4|1}}', r'\mathrm{III}_4')

opening_quotes = chr(96) * 2
old_note = comp[key(14)]['first'].split(r'\\', 1)[0]
new_note = (
    '(l’indice ' + opening_quotes
    + r"i'' indique l’ordre du \(G=\operatorname{Aut}^{+}\unsure{\}|)}\),"
      r' donc le nb de structures \deleted{est} \(120/i\))'
)
finals[key(14)] = once(comp[key(14)]['first'], old_note, new_note)
change_page(old_note, new_note)

old_count = r'\text{2 sommets-repères}\quad\deleted{\text{\unsure{repères}}}'
new_count = r'\text{2 sommets}\quad\deleted{\text{\unsure{-repères|-repère}}}'
finals[key(20)] = once(comp[key(20)]['first'], old_count, new_count)
change_page(old_count, new_count)

old_compat = r'\unsure{\vec Q|\vec G}'
f21 = comp[key(21)]['first']
assert f21.count(old_compat) == 2 and t.count(old_compat) == 2
f21 = f21.replace(old_compat, r'\widetilde G')
t = t.replace(old_compat, r'\widetilde G')
f21 = once(f21, r'\gamma_r^0', r'\gamma_r^{\unsure{0}}')
change_page(r'\gamma_r^0', r'\gamma_r^{\unsure{0}}')
finals[key(21)] = f21

outer_gamma = r"\gamma_r^{2'}"


def tikz(s):
    start = s.index(r'\begin{tikzpicture}')
    end = s.rindex(r'\end{tikzpicture}') + len(r'\end{tikzpicture}')
    return s[start:end]


def add_white_before_points(s, coordinates, radius):
    marker = r'\foreach \p in '
    start = s.index(marker)
    if coordinates is None:
        match = re.match(
            r'\\foreach \\p in (\{[^\n]*?\}) \{\\fill\[red!60!black\]',
            s[start:])
        assert match
        coordinates = match.group(1)
    white = (r'\foreach \p in ' + coordinates
             + r' {\fill[white] \p circle (' + radius + ');}\n')
    return s[:start] + white + s[start:]


graphs = {n: tikz(comp[key(n)]['second']) for n in range(35, 47)}

for n, start in [(36, '(6.0,1.0)'), (37, '(4.1,.9)')]:
    s = graphs[n]
    count = 0
    lines = []
    for line in s.splitlines():
        if line.startswith(r'\draw[edge] ' + start):
            line = line.replace(r'\draw[edge]',
                                r'\draw[red!55!black,line width=1.05pt]', 1)
            count += 1
        elif line.startswith(r'\draw[edge,dashed] ' + start):
            line = line.replace(
                r'\draw[edge,dashed]',
                r'\draw[red!55!black,line width=1.05pt,dashed]', 1)
            count += 1
        lines.append(line)
    assert count == (3 if n == 36 else 4)
    graphs[n] = '\n'.join(lines)

# Exact de Casteljau split at t=.60 for the approved rear-right I4 cubic.
D = Decimal
points = [(D('4.1'), D('.9')), (D('6.6'), D('-.2')),
          (D('7.3'), D('2.0')), (D('7.2'), D('4.4'))]
u = D('.60')


def mix(a, b):
    return tuple((1-u)*x + u*y for x, y in zip(a, b))


a = [mix(points[i], points[i+1]) for i in range(3)]
b = [mix(a[i], a[i+1]) for i in range(2)]
c = mix(b[0], b[1])


def coordinate(pt):
    return '(' + ','.join(format(x.normalize(), 'f') for x in pt) + ')'


split37 = (
    r'\draw[red!55!black,line width=1.05pt] ' + coordinate(points[0])
    + ' .. controls ' + coordinate(a[0]) + ' and ' + coordinate(b[0])
    + ' .. ' + coordinate(c) + ';\n'
    + r'\draw[red!55!black,line width=1.05pt,dashed] ' + coordinate(c)
    + ' .. controls ' + coordinate(b[1]) + ' and ' + coordinate(a[2])
    + ' .. ' + coordinate(points[3]) + ';'
)
graphs[37] = once(
    graphs[37],
    r'\draw[red!55!black,line width=1.05pt,dashed] (4.1,.9) .. controls (6.6,-.2) and (7.3,2.0) .. (7.2,4.4);',
    split37)

graphs[39] = once(graphs[39], r'\node at (1.1,6.9) {$1$};' + '\n', '')
header39, rest39 = graphs[39].split('\n', 1)
graphs[39] = (
    header39 + '\n'
    '% Eight explicit oblique strokes cancel this drawing; no secure alphabetic labels survive.\n'
    + rest39
)

graphs[40] = once(
    graphs[40],
    r'\draw[edge] (5.5,.5) .. controls (7.1,.6) and (7.6,1.4) .. (8.0,2.4) .. controls (9.4,4.7) and (7.9,7.2) .. (7.0,8.0) .. controls (5.9,9.4) and (4.8,9.7) .. (4.1,9.4);',
    '\n'.join([
        r'\draw[edge] (5.5,.5) .. controls (6.7,.6) and (7.6,1.4) .. (7.8,1.95);',
        r'\draw[edge] (8.25,2.9) .. controls (9.0,4.9) and (8.0,6.9) .. (7.35,7.6);',
        r'\draw[edge] (6.8,8.35) .. controls (5.9,9.4) and (4.8,9.7) .. (4.1,9.4);',
    ]))
graphs[40] = once(graphs[40], r'\draw[gray] (1.2,5.2)',
                   r'\draw[gray,dashed] (1.2,5.2)')
graphs[40] = add_white_before_points(graphs[40], '{(4.1,6.3)}', '.30')

graphs[41] = once(
    graphs[41],
    r'\node at (.2,7.9) {$3$};\node at (2.4,.0) {$1$};' + '\n', '')
graphs[41] = once(
    graphs[41],
    r'\draw[line width=.8pt] (4.5,7.0)--(5.0,7.1) (4.6,7.3)..controls (5.2,7.3) and (5.2,7.8)..(4.5,8.1);' + '\n', '')
graphs[41] = once(
    graphs[41],
    r'\draw[edge] (2.6,1.7) .. controls (4.0,-.1) and (6.0,.4) .. (6.8,1.3);',
    r'\draw[edge] (2.85,1.4) .. controls (4.0,-.1) and (6.0,.4) .. (6.45,1.05);')
graphs[41] = once(
    graphs[41],
    r'\draw[edge] (2.6,1.7) .. controls (1.3,3.5) and (1.1,7.0) .. (2.2,8.6);',
    r'\draw[edge] (2.35,2.05) .. controls (1.3,3.5) and (1.1,7.0) .. (2.2,8.6);')
graphs[41] = once(
    graphs[41],
    r'\draw[edge,dashed] (6.8,1.3) .. controls (7.7,2.6) and (7.5,3.6) .. (7.5,4.6);',
    r'\draw[edge,dashed] (7.05,1.75) .. controls (7.7,2.6) and (7.5,3.6) .. (7.5,4.6);')

graphs[42] = add_white_before_points(
    graphs[42], '{(1.8,6.1),(5.3,6.5),(8.6,5.9)}', '.25')
graphs[43] = add_white_before_points(graphs[43], None, '.26')
graphs[43] = once(graphs[43], r'\overline{\unsure{P|\rho}}', r'\bar P')
graphs[43] = once(graphs[43], r'\unsure{P|\rho}', 'P')

graphs[44] = once(
    graphs[44],
    r'\draw[edge] (3.4,5.7)--(5.1,6.0)--(7.0,6.0) .. controls (8.8,5.9) and (9.5,5.5) .. (9.0,5.1) .. controls (8.6,4.7) and (7.7,4.6) .. (6.8,4.3);',
    '\n'.join([
        r'\draw[edge] (3.4,5.7)--(5.1,6.0)--(7.0,6.0) .. controls (8.8,5.9) and (9.5,5.5) .. (9.0,5.1);',
        r'\draw[edge,dashed] (9.0,5.1) .. controls (8.6,4.7) and (7.7,4.6) .. (6.8,4.3);',
    ]))
graphs[44] = add_white_before_points(graphs[44], None, '.26')

layer_labels = [
    r"\unsure{\alpha'|\deleted{\beta'}\inserted{\alpha'}}",
    r'\unsure{\beta|\deleted{\alpha}\inserted{\beta}}',
    r"\unsure{\beta'|\deleted{\alpha'}\inserted{\beta'}}",
]
graphs[45] = add_white_before_points(graphs[45], None, '.26')
for old, new in zip([
        r"\deleted{\unsure{\beta'}}\inserted{\alpha'}",
        r'\deleted{\unsure{\alpha}}\inserted{\beta}',
        r"\deleted{\unsure{\alpha'}}\inserted{\beta'}"],
        layer_labels):
    graphs[45] = once(graphs[45], old, new)

graphs[46] = once(
    graphs[46],
    r'\draw[edge] (4.3,6.2) .. controls (5.2,6.5) and (8.1,6.2) .. (7.7,5.3) .. controls (7.4,4.8) and (6.2,4.7) .. (5.7,4.7);',
    '\n'.join([
        r'\draw[edge] (4.3,6.2) .. controls (5.2,6.5) and (8.1,6.2) .. (7.7,5.3);',
        r'\draw[edge,dashed] (7.7,5.3) .. controls (7.4,4.8) and (6.7,4.8) .. (6.4,4.8);',
        r'\draw[edge] (6.4,4.8)--(5.7,4.7);',
    ]))
position46 = graphs[46].index(r'\foreach \p in ')
graphs[46] = (
    graphs[46][:position46]
    + r'\draw[edge] (2.9,4.6)--(3.6,4.6);' + '\n'
    + r'\draw[gray] (2.8,9.0)..controls(2.6,9.6)and(3.2,9.7)..(3.3,9.35);' + '\n'
    + graphs[46][position46:]
)
graphs[46] = add_white_before_points(graphs[46], '{(4.4,1.3)}', '.29')

for n, graph in graphs.items():
    change_page(comp[key(n)]['first'], graph)
    finals[key(n)] = graph


def graphic_body(s):
    return tikz(s).split('\n', 1)[1].rsplit(r'\end{tikzpicture}', 1)[0].strip()


margin_bodies = {n: graphic_body(comp[key(n)]['second']) for n in (50, 51, 52)}
margin_bodies[50] = once(
    margin_bodies[50], r'\draw[gray] (2.2,0)--(1.7,10);' + '\n', '')
for old, new in [
    (r'\fill (8.2,3.8)--(8.5,4.2)--(8.2,4.7)--cycle;',
     r'\draw[line width=.7pt] (8.2,3.8)--(8.5,4.2)--(8.2,4.7);'),
    (r'\fill (8.3,5.2)--(8.7,5.0)--(8.5,5.8)--cycle;',
     r'\draw[line width=.7pt] (8.3,5.2)--(8.7,5.0)--(8.5,5.8);'),
]:
    margin_bodies[50] = once(margin_bodies[50], old, new)
margin_bodies[51] = once(
    margin_bodies[51], r'\draw[gray] (1.8,0)--(1.7,10);' + '\n', '')
margin_bodies[51] = once(
    margin_bodies[51],
    r'\fill (8.2,6.1)--(8.7,6.4)--(8.2,6.7)--cycle;',
    r'\draw[line width=.8pt] (8.2,6.1)--(8.7,6.4)--(8.2,6.7);')
margin_bodies[51] += '\n' + r'\draw[line width=.8pt] (7.8,5.4)--(7.7,6.3);'
margin_bodies[52] = once(
    margin_bodies[52],
    r'\draw[gray] (1.6,0)..controls (1.5,1.4) and (1.6,2.1)..(1.8,2.7);' + '\n', '')

transforms = {
    50: ('.24', '5.6815', '.175', '-.065'),
    51: ('.212173913', '2.764637681', '.171014493', '-.085507246'),
    52: ('.328', '-.0878', '.16', '-.078'),
}
margin_scopes = {}
for n, (sx, sy, ux, uy) in transforms.items():
    margin_scopes[n] = '\n'.join([
        rf'\begin{{scope}}[shift={{({sx},{sy})}}]',
        rf'\begin{{scope}}[x={ux}cm,y={uy}cm]',
        margin_bodies[n], r'\end{scope}', r'\end{scope}',
    ])

old_arrow1 = '\n'.join([
    r'\draw[thick] (.52,5.35)--(1.04,5.38)..controls(1.4,5.42)..(1.68,5.42);',
    r'\draw[thick] (1.68,5.42)..controls(1.34,5.29)..(1.04,5.38);',
])
old_arrow2 = '\n'.join([
    r'\draw[thick] (.52,2.32)..controls(1.15,2.37)..(1.65,2.4);',
    r'\draw[thick] (.52,2.32)..controls(1.15,2.3)..(1.65,2.28);',
    r'\draw[thick] (.52,2.32)..controls(1.15,2.2)..(1.7,2.17);',
])
guide = r'\draw[gray] (.52,7.3)..controls(.44,4.7)and(.55,1.5)..(.57,-.32);'
old_base = r'\draw[gray] (.6,-.47)..controls(1.12,-.45)and(1.52,-.52)..(1.72,-.51)--(1.73,-.55);'
change_page(old_arrow1, margin_scopes[50])
change_page(old_arrow2, margin_scopes[51])
change_page(old_base, margin_scopes[52])

for n in (50, 51, 52):
    body = (guide + '\n' if n == 52 else '') + margin_scopes[n]
    finals[key(n)] = '\n'.join([
        r'\begin{tikzpicture}[x=1cm,y=1cm,line cap=round,line join=round]',
        body, r'\end{tikzpicture}',
    ])

# Synchronize existing witness differences without counting extra uncertainty.
changes = {c['place']: c for c in p['changes']}


def revise(old_place, n, **updates):
    changes[old_place].update(**evidence(n), **updates)


revise('II2 count and live repères', 20,
       place='II2 count and single canceled repère(s)', final=new_count,
       against_c=True, against_h=True)
revise('III2prime codiagonales plural', 12,
       final=r'\text{\unsure{codiagonales|codiagonale}, }K=')
revise('III2prime lower carré en codiagonales', 12, final=lower_phrase)
revise('indice quotation marks', 14,
       final='l’indice ' + opening_quotes + "i''",
       against_c=True, against_h=True)
revise('II1 cancelled group entry before live equals', 6,
       final=cancel_group, against_c=True)
revise('Upper compatibility letter', 21, final=r'\widetilde G',
       against_c=True, against_h=True)
revise('Lower compatibility letter', 21, final=r'\widetilde G',
       against_c=True, against_h=True)
revise('gamma r0 target and exponent', 21,
       final=r'\mathrm{II}_1\xrightarrow{1\quad\gamma_r^{\unsure{0}}\quad6}\mathrm I_6')
revise('gamma r2prime exponent and target', 28, final=comp[key(28)]['first'])

graph_places = [
    'figure_i10', 'figure_i6', 'figure_i4', 'figure_ii2',
    'figure_ii2prime_canceled', 'figure_ii2prime_live', 'figure_ii1',
    'figure_iii2', 'figure_iii1_a', 'figure_iii1_b',
    'figure_iii2prime_a', 'figure_iii2prime_b',
]
for n, place in zip(range(35, 47), graph_places):
    revise(place, n, final=finals[key(n)])
for n, place in [(50, 'margin arrow1 course'), (51, 'margin arrow2 course'),
                 (52, 'margin bracket and detached base')]:
    revise(place, n, final=finals[key(n)])


def add_change(place, n, c, h, final, kind, math):
    assert place not in changes
    p['changes'].append(dict(
        place=place, c=c, h=h, final=final, kind=kind,
        against_c=True, against_h=True, math=math, **evidence(n)))


add_change(
    'I4 K equality', 3, r'K\simeq\{P\}\amalg I',
    r'K \simeq \lbrace P \rbrace \amalg I',
    r'K=\{P\}\amalg I', 'misread symbol or index', True)
add_change(
    'I4 unfinished diagonals phrase', 3,
    r'\text{ens. des diagonales }\alpha',
    '\\text{ens.\\ des\ndiagonales } \\alpha',
    r'\text{ens. des diagonales de}', 'misread word', False)
add_change(
    'indice note du', 14, 'l’ordre de', "l'ordre de",
    'l’ordre du', 'misread word', False)
add_change(
    'indice note closing sign and comma', 14,
    r'\operatorname{Aut}^{+}\) ;', r'\mathrm{Aut}^{+}$,',
    r'\operatorname{Aut}^{+}\unsure{\}|)}\),',
    'omission', True)
add_change(
    'indice note est canceled', 14, 'est', 'est',
    r'\deleted{est}', 'deletion state', False)

decisions = {d['id']: d for d in p['decisions']}
for mark in ('M0310', 'M0312'):
    decisions[mark].update(decision='other', reading=r'\widetilde G',
                           **evidence(21))
decisions['M0317'].update(decision='alternative', reading=outer_gamma,
                          **evidence(28))

# The singular alternatives retain their existing favored plural readings:
# no new C/H difference is created for merely reopening those endings.
p['unresolved'] = [
    u for u in p['unresolved']
    if u['place'] not in ('upper compatibility symbol', 'lower compatibility symbol')
]
for u in p['unresolved']:
    place = u['place']
    if place == 'II2 struck word':
        u.update(reading=r'\deleted{\text{\unsure{-repères|-repère}}}',
                 issue=root[key(20)]['ink'], alternatives=['-repères', '-repère'],
                 confidence='medium', **meta(20))
    elif place == 'II1 canceled group material':
        u.update(reading=cancel_group, issue=root[key(6)]['ink'],
                 alternatives=[r'\mathbb Z_2', '1'], **meta(6))
    elif place == 'II1 figure P labels':
        u.update(reading=r'\unsure{P|\rho},\ \overline{\unsure{P|\rho}}',
                 issue=root[key(41)]['ink'],
                 alternatives=['P and barred P', 'rho and barred rho'], **meta(41))
    elif place == 'III2prime first figure overwritten labels':
        u.update(reading=r',\ '.join(layer_labels), issue=root[key(45)]['ink'],
                 alternatives=[
                     'retraced alpha-prime, beta, beta-prime without secure earlier forms',
                     'possible beta-prime to alpha-prime, alpha to beta, alpha-prime to beta-prime layers; order uncertain',
                 ], **meta(45))
    elif place == 'punctuation after Aut+':
        u.update(place='closing sign after Aut+', reading=r'\unsure{\}|)}',
                 issue=root[key(14)]['ink'], alternatives=[r'\}', ')'],
                 confidence='low', **meta(14))


def add_doubt(place, n, reading, alternatives):
    p['unresolved'].append(dict(
        place=place, reading=reading, issue=root[key(n)]['ink'],
        alternatives=alternatives, confidence='low', **meta(n)))


add_doubt('III2prime upper codiagonale(s) ending', 12,
          ending, ['codiagonales', 'codiagonale'])
add_doubt('III2prime lower carré(e) and codiagonale(s) endings', 12,
          lower_phrase, ['carré/carrée', 'codiagonales/codiagonale'])
add_doubt('upper diagonal gamma_r exponent', 21,
          r'\gamma_r^{\unsure{0}}', ['0', 'unresolved raised loop'])
resolve_level_zero_index(p, root[key(13)], meta(13))

for inv in p['inventory']:
    element = inv['element']
    if element == 'I4 block':
        inv['first_words_or_objects'] = 'I4 (pyramidale); K={P} amalg I; unfinished ens. des diagonales de'
    elif element == 'III2prime block':
        inv['first_words_or_objects'] = new_heading
    elif element == 'arrow_tau_pi_s' and inv['kind'] == 'text':
        inv['first_words_or_objects'] = new_count
    elif element == 'II2 separate canceled word':
        inv.update(element='II2 single canceled word', position='after 2 sommets',
                   first_words_or_objects=r'\deleted{\text{\unsure{-repères|-repère}}}')
    elif element == 'II2prime canceled sphere':
        inv['first_words_or_objects'] = 'eight explicit oblique cancellation segments'
    elif element == 'II1 canceled group entry':
        inv['first_words_or_objects'] = cancel_group
    elif element == 'indice note':
        inv['first_words_or_objects'] = new_note
    elif element == 'arrows_upper_middle':
        inv['first_words_or_objects'] = 'II2prime to I6; II1 to I6; both compatibility annotations use tilde G; gamma_r raised0 remains doubtful'
    elif element == 'arc_gamma_r2prime':
        inv['first_words_or_objects'] = outer_gamma + '; III2prime to I4, 1 to 2'
    elif element == 'III2prime figure label overtracing':
        inv['first_words_or_objects'] = r',\ '.join(layer_labels)
    elif element == 'II1 P-label overtracing':
        inv['first_words_or_objects'] = r'\unsure{P|\rho} and barred \unsure{P|\rho}'
    elif element in ('margin_arrow1', 'margin_arrow2', 'margin_bracket_base'):
        n = {'margin_arrow1': 50, 'margin_arrow2': 51, 'margin_bracket_base': 52}[element]
        inv['first_words_or_objects'] = finals[key(n)]
    elif element == 'figure_ii2prime_canceled':
        inv['first_words_or_objects'] = 'canceled sphere, eight oblique segments, five colored positions, no secure labels'
    elif element == 'figure_ii1':
        inv['first_words_or_objects'] = r'1 infinity 0 \unsure{P|\rho} barred \unsure{P|\rho}; u0 u1 u2 u3 u4 u5'
p['inventory'].append(dict(
    element='indice note canceled est', kind='deletion',
    position='between structures and 120/i in bottom-left note',
    first_words_or_objects=r'\deleted{est}', sheet_kind='text',
    hand='his hand', transcribed='yes'))

for note in p['notes']:
    if note['id'] == '148-031-N06':
        note['text'] = (
            'The upper gamma_pi,s prime remains retained. The main reader re-viewed '
            'the complete saved III2prime heading and outer gamma_r crops and compared '
            'the corresponding forms on scan033. Both short raised strokes lack a '
            'separate full baseline foot, unlike full numerical1 with flag and foot. '
            'The repeated type and map labels settle them as primes at high confidence; '
            'the first III-prime lower2 and gamma_r raised2-prime readings remain.')
    elif note['id'] == '148-031-N09':
        note['text'] = (
            'The broad lower gamma_r2 arc runs from III2prime to II2, with degree2 at '
            'each end. The narrow outer-right gamma_r arc runs from III2prime to I4, '
            'with1 at the tail and2 at the head. Its superscript is2-prime, retained '
            'after the main reader compared its short footless tick with the '
            'corresponding scan033 map label.')
    elif note['id'] == '148-031-N10':
        note['text'] = (
            'The lower end of gamma_pi,rho retains its curved hook without a second '
            'complete head. The revised upper marginal trace has two separately ending '
            'branches with angular return strokes, and the lower trace has three '
            'branches with their literal terminal returns. Neither margin trace uses '
            'filled normalized heads. The complete vertical guide occurs once.')
    elif note['id'] == '148-031-N11':
        note['text'] = (
            'Five colored marked positions remain distinct from smaller black junctions '
            'in each sphere. The canceled II2prime sphere retains eight explicit oblique '
            'segments and no secure alphabetic labels. The two lower-right figures '
            'have eight black junctions each. The newly traced paths preserve the '
            'approved white separations, partial retracings, angular patches and '
            'local solid/dashed distinctions. The three overwritten labels in the '
            'first lower-right sphere admit possible replacement layers without '
            'asserting their order.')
p['notes'].append(dict(
    id='148-031-BLIND', type='main-reader adjudication',
    text=(
        'The main reader personally viewed all53 differing fixed crops and supplied '
        'the decisions in second/148_scan031_root_working.json. The upper-middle '
        'compatibility crop was additionally rotated28 degrees clockwise; both '
        'labels read tilde G. The canceled II2 repère(s) is one word, not a live '
        'word plus another canceled copy. The I4 formula reads K= and ends with '
        'the unfinished diagonales de. The bottom note quotes i, reads du, retains '
        'an uncertain closing brace/parenthesis and cancels est. Twelve sphere '
        'traces were integrated in their original cells; three margin traces use '
        'the explicitly supplied coordinate transforms. Added uncertainties and '
        'coordinate changes alone receive no new C/H rows. The first/second/boxes/'
        'comparison/token TSVs remain unchanged. No new mathematical check, '
        'independent image reading, or TeX compilation was performed by the '
        'mechanical implementer.')))
p['notes'].append(dict(
    id='148-031-NOTATION', type='completed root notation revisit',
    text=(
        'The main reader completed the later notation revisit for cases031_c_011 '
        'and031_c_028 before this script ran. Both retain the first prime readings '
        'at high confidence. The root working record supplies the cross-page '
        '031/033 evidence; the mechanical implementer did not inspect scan033 '
        'or change the I10 heading. No certainty-only C/H row was added.')))

p['hand_log'][3].update(
    pages=[31, 33],
    holds_at_every_observed_occurrence=False,
    witness_effect=(
        'The upper gamma_pi,s prime remains; root’s 031/033 notation comparison '
        'retains the III2prime heading and gamma_r raised2-prime over numerical '
        'alternatives, including C’s proposed21.'),
    habit=(
        'In the corresponding 031/033 type and map labels inspected by root, a short '
        'detached prime lacks the full baseline foot of numerical1. Full1 has both '
        'flag and foot. The heavy entry on the031 title tick is not a separate '
        'numeral flag; the recurring primed form resolves that local ambiguity.'))
p['hand_log'].append(dict(
    pages=[31], hand='his hand', holds_at_every_observed_occurrence=True,
    witness_effect='Both upper-middle compatibility symbols become tilde G.',
    habit=(
        'In the two compatibility annotations, the roof is a continuous two-turn '
        'tilde without an arrowhead, over a G with open right return and inner bar. '
        'This local observation does not replace the arrowed Q in the I4 datum.')))

for notation in p['notation']:
    if notation['form'] == r'\vec Q=(Q,\omega)':
        notation['caution'] = (
            'The I4 datum retains its arrowed Q. The two upper-middle compatibility '
            'annotations independently read tilde G after root’s crop inspection.')
    elif notation['form'] == r"\gamma'_{\pi,s},\ \gamma_r^{2'}":
        notation.update(
            form=r"\gamma'_{\pi,s},\ \gamma_r^{2'},\ \mathrm{III}'_2",
            observed_use='Locally read raised strokes on the upper arrow, outer arrow and lower-right type heading.',
            caution=(
                'The upper gamma_pi,s prime remains. Root re-viewed the complete '
                '031 heading and outer-map crops and compared the corresponding033 '
                'short primes against full1 with flag and foot; both first prime '
                'readings are retained at high confidence.'))
p['notation'].append(dict(
    form=r'\widetilde G', pages=[31],
    observed_use='comp. avec tilde G and compat. avec tilde G on the upper-middle arrows.',
    caution='Both accents have two continuous turns and no arrowhead; neither is normalized to arrowed Q or G.'))

p['blind_graphic_transforms'] = {
    key(n): dict(shift=[sx, sy], local_x_cm=ux, local_y_cm=uy,
                 outer_x_cm='1', outer_y_cm='1',
                 explicit_pt_widths='retained as supplied by root',
                 full_vertical_guide='retained once outside the revised scopes')
    for n, (sx, sy, ux, uy) in transforms.items()
}
p['blind_graphic_transforms'][key(37)] = dict(
    operation='de Casteljau split of the approved rear-right cubic at t=.60',
    split_point=[str(v) for v in c],
    first_segment='solid', second_segment='dashed',
    color='red!55!black', line_width_pt='1.05')

entries = []
for item in working:
    entry = {k: v for k, v in item.items() if k != 'instructions'}
    n = int(item['box'].rsplit('_', 1)[1])
    entry['crop'] = meta(n)['crop']
    entry['crop_box'] = meta(n)['box']
    if item['choice'] == 'revised':
        entry['final'] = finals[item['box']]
    entries.append(entry)

# Structural verification is deliberately limited to the approved edit set.
assert set(finals) == {k for k, e in root.items() if e['choice'] == 'revised'}
assert all(e['viewed_by_main'] is True for e in entries)
assert len(entries) == 53 and len(finals) == 22
assert all((B / e['crop']).is_file() for e in entries)
for n in range(35, 47):
    assert t.count(finals[key(n)]) == 1
for n in (50, 51, 52):
    assert t.count(margin_scopes[n]) == 1
assert t.count(guide) == 1
assert t.count(r'\vcenter{\hbox{') == original.count(r'\vcenter{\hbox{')
assert r'\draw[edge,dashed] (9.0,5.1)' in t
assert r'\draw[edge,dashed] (7.7,5.3)' in t
assert r'\draw[edge] (2.9,4.6)--(3.6,4.6);' in t
assert r'\node at (1.1,6.9) {$1$};' not in t
assert r'\node at (.2,7.9) {$3$};' not in t
assert r'\node at (2.4,.0) {$1$};' not in t
assert r'\x27' not in t and all(r'\x27' not in e.get('final', '') for e in entries)
assert old_compat not in t and t.count(r'\gamma_r^{\unsure{0}}') == 1
assert t.count(r'\unsure{codiagonales|codiagonale}') == 2
assert t.count(r'\deleted{est}') == 1 and t.count(new_count) == 1
assert t.count(new_heading) == 1
assert r'\mathrm{III}^{\unsure{\prime|1}}_2' not in t
assert r'\mathrm{III}_{\unsure{4|1}}' not in t
assert r'\mathrm{III}_4' in t
assert t.count(r'\mathrm{III}_1\ (\text{triple triangle sem.-gauche})') == 1
assert t.count(outer_gamma) == 1
assert abs(float(transforms[50][0]) + .175*1.6 - .52) < 1e-12
assert abs(float(transforms[50][1]) - .065*5.1 - 5.35) < 1e-12
assert abs(float(transforms[51][0]) + .171014493*1.8 - .52) < 2e-9
assert abs(float(transforms[51][1]) - .085507246*5.2 - 2.32) < 2e-9
assert abs(float(transforms[51][0]) + .171014493*8.7 - 1.70) < 3e-9
level = 0
for m in re.finditer(r'(?<!\\)[{}]', t):
    level += 1 if m.group() == '{' else -1
    assert level >= 0, m.start()
assert level == 0
for env in ('tikzpicture', 'scope', 'tikzcd', 'gathered', 'array'):
    assert t.count(r'\begin{' + env + '}') == t.count(r'\end{' + env + '}'), env
assert all(hashlib.sha256(f.read_bytes()).hexdigest() == protected_hashes[str(f)]
           for f in protected)
assert len(p['changes']) == 83
assert len(p['inventory']) == 69
assert len(p['decisions']) == 48
assert len(p['unresolved']) == 15

page.write_text(t)
review_path.write_text(json.dumps(p, ensure_ascii=False, indent=2) + '\n')
adjudication_path.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(
    scan=31, adjudications=len(entries), revised_boxes=len(finals),
    changes_rows=len(p['changes']),
    against_c=sum(bool(c['against_c']) for c in p['changes']),
    against_h=sum(bool(c['against_h']) for c in p['changes']),
    decisions=len(p['decisions']), unresolved=len(p['unresolved']),
    inventory_rows=len(p['inventory']),
    resolved_notation=[key(11), key(28)],
    protected_tsv_hashes_unchanged=True,
    de_casteljau_split=[str(v) for v in c],
)))
