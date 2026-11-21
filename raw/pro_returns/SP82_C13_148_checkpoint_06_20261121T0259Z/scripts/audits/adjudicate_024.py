#!/usr/bin/env python3
"""Mechanically apply the main reader's 32 crop adjudications for scan024.

The main reader supplied these decisions after personally viewing every differing
crop. This script performs no image recognition, chooses no reading, does not
compile TeX, and does not alter either locked reading TSV or shared audit logs.
Run once, then have the main reader review and run record_audit.py 24.
"""
from pathlib import Path
import csv
import json
import re
from PIL import Image

B = Path(__file__).resolve().parents[2]
stem = B / 'second/148_scan024'
with Path(str(stem) + '_comparison.tsv').open() as f:
    comp = {r['box']: r for r in csv.DictReader(f, delimiter='\t')}
with Path(str(stem) + '_boxes.tsv').open() as f:
    boxes = {r['box']: r for r in csv.DictReader(f, delimiter='\t')}
rp = B / 'reviews/148_scan024.json'
p = json.loads(rp.read_text())
page = B / 'pages/148_scan024.tex'
t = page.read_text()
ap = Path(str(stem) + '_adjudications.json')
assert not p.get('second_audit') and not ap.exists(), 'Non-idempotent: already applied.'

graphics = ['cup_tree', 'top_sphere', 'pair_spheres', 'left_labeled',
            'middle_spheres', 'center_signs', 'cap_segment', 'sphere_map',
            'target_sphere', 'right_loop', 'small_circles', 'lower_ovals',
            'lower_sphere', 'dome', 'diamond_formulas']

def body(name):
    s = comp['S24-' + name]['second']
    return s.split('\n', 1)[1].rsplit(r'\end{tikzpicture}', 1)[0].rstrip().splitlines()

def omit(lines, *starts):
    for start in starts:
        assert sum(line.startswith(start) for line in lines) == 1, start
    return [line for line in lines if not any(line.startswith(s) for s in starts)]

def before(lines, start):
    i = next(i for i, line in enumerate(lines) if line.startswith(start))
    return lines[:i]

def replace_line(lines, start, replacement):
    assert sum(line.startswith(start) for line in lines) == 1, start
    return [replacement if line.startswith(start) else line for line in lines]

bodies = {name: body(name) for name in graphics}
bodies['cup_tree'] = omit(bodies['cup_tree'], r'\draw (670,0)', r'\draw (773,0)')
bodies['top_sphere'] = omit(bodies['top_sphere'], r'\draw[->] (655,40)', r'\draw[->] (732,134)')
bodies['pair_spheres'] = omit(bodies['pair_spheres'], r'\draw (195,0)')
bodies['left_labeled'] = omit(bodies['left_labeled'], r'\draw (451,492)', r'\draw (823,0)')
bodies['left_labeled'] = [line for line in bodies['left_labeled'] if not line.startswith(r'\node')]
for x, y, label in [(614, 69, "Q'"), (61, 373, 'a'), (292, 485, r'\unsure{b}'),
                    (329, 367, r'\unsure{c}'), (197, 221, 'd'),
                    (330, 278, r'\circlearrowleft'), (440, 503, r"\ell''"),
                    (683, 625, 'Q')]:
    bodies['left_labeled'].append(rf'\node[rotate=90] at ({x},{y}) {{\({label}\)}};')
bodies['middle_spheres'] = omit(bodies['middle_spheres'], r'\draw (570,0)', r'\draw (1272,0)')
bodies['middle_spheres'] = replace_line(
    bodies['middle_spheres'], r'\draw[dashed,->] (1377,351)',
    r'\draw[line width=1pt] (1377,390) .. controls (1388,459) and (1412,500) .. (1444,522);'
    '\n' + r'\draw[->] (1377,369) -- (1382,411);')
bodies['center_signs'] = omit(bodies['center_signs'], r'\draw (449,163)',
    r'\draw[->,line width=1pt] (678,0)', r'\draw (700,219) -- (790,875)',
    r'\draw (0,558)', r'\draw (0,699)')
bodies['cap_segment'] = omit(bodies['cap_segment'], r'\draw (796,161)')
bodies['sphere_map'] = before(bodies['sphere_map'], r'\draw (269,0)')
bodies['sphere_map'] = omit(bodies['sphere_map'], r'\draw (484,410)',
    r'\fill (483,416)', r'\draw (132,642)', r'\draw (161,633)', r'\draw (490,450)')
bodies['sphere_map'] = replace_line(bodies['sphere_map'], r'\node at (826,626)',
                                   r'\node at (826,626) {$1$};')
bodies['sphere_map'] += [r'\node at (150,640) {$0$};',
                         r'\node at (530,456) {$\infty$};',
                         r'\node at (484,410) {$\unsure{0|\odot}$};']
bodies['target_sphere'] = before(bodies['target_sphere'], r'\draw (755,0)')
bodies['small_circles'] = omit(bodies['small_circles'], r'\draw (0,225)', r'\draw (819,0)')
bodies['small_circles'] = before(bodies['small_circles'], r'\draw (0,197)')
bodies['lower_ovals'] = omit(bodies['lower_ovals'], r'\draw (754,0)', r'\draw (959,0)')
bodies['dome'] = omit(bodies['dome'], r'\draw (318,0)', r'\draw (43,0)')
bodies['dome'] = replace_line(bodies['dome'], r'\draw[line width=1.5pt] (758,558)',
                              r'\draw[green!40!black,line width=1.5pt] (758,558) -- (885,182);')
# Add the green parallel trace immediately after the top black arc. The second
# reader's grayscale geometric description did not encode this visible color.
i = next(i for i, line in enumerate(bodies['dome']) if line.startswith(r'\draw[line width=1.7pt] (452,53)'))
bodies['dome'].insert(i + 1, r'\draw[green!40!black,line width=1.2pt] (456,59) .. controls (590,25) and (752,36) .. (841,86);')
for x, y, radius in [(331,118,8), (365,140,10), (409,135,8),
                     (805,139,8), (840,153,8), (887,185,10), (1014,225,8)]:
    bodies['dome'].append(rf'\fill ({x},{y}) circle ({radius});')
bodies['diamond_formulas'] = [line for line in bodies['diamond_formulas'] if not line.startswith(r'\node')]

# The diagrams were traced in display-image pixel coordinates. These scopes
# restore the native scan coordinates, retaining any rounding difference in the
# displayed height separately from its width. The diamond was read after a
# clockwise quarter-turn: native x=x0+(W/Hrot)*v, y=y1-(H/Wrot)*u.
display_dir = B.parent / 'blind_display/148_scan024'
scopes = {}
transforms = {}
for name in graphics:
    key = 'S24-' + name
    rect = [int(boxes[key][k]) for k in ('x0','y0','x1','y1')]
    x0, y0, x1, y1 = rect
    if name == 'diamond_formulas':
        dw, dh = Image.open(display_dir / (key + '_rotated.jpg')).size
        opts = f'shift={{({x0},{y1})}},rotate=90,xscale={{{y1-y0}/{dw}}},yscale={{{x1-x0}/{dh}}}'
        transforms[key] = {'display_size':[dw,dh], 'native_box':rect,
            'native_x':f'{x0}+({x1-x0}/{dh})*v', 'native_y':f'{y1}-({y1-y0}/{dw})*u'}
    else:
        dw, dh = Image.open(display_dir / (key + '.jpg')).size
        opts = f'shift={{({x0},{y0})}},xscale={{{x1-x0}/{dw}}},yscale={{{y1-y0}/{dh}}}'
        transforms[key] = {'display_size':[dw,dh], 'native_box':rect,
            'native_x':f'{x0}+({x1-x0}/{dw})*u', 'native_y':f'{y0}+({y1-y0}/{dh})*v'}
    scopes[name] = '\n'.join([rf'\begin{{scope}}[{opts}]'] + bodies[name] + [r'\end{scope}'])

# Retained uncertain signs and the vertical alphabet list use the original
# native-coordinate placement. No label is silently replaced with a literal
# geometric loop, nor with a differently oriented blind letter guess.
extra_nodes = {
    'top_sphere': r'\node at (740,190) {\(\unsure{\circlearrowleft^{3}|\mathfrak S_3}\)};',
    'center_signs': r'\node at (869,1028) {\(\unsure{\circlearrowleft|G}\)};',
}
for name, node in extra_nodes.items():
    scopes[name] += '\n' + node

picture_begin = r'\begin{tikzpicture}[x=.007cm,y=-.007cm,line cap=round,line join=round]'
def figure(contents):
    return '\n'.join([r'\figure{', picture_begin, contents, r'\end{tikzpicture}', '}'])

finals = {'S24-' + name: figure(scopes[name]) for name in graphics}
# Long crossing strokes belong to the full sheet. Their short duplicated crop
# fragments were omitted above. The center's explicit wings replace the former
# generic arrowhead, and its short arrows replace the old regularized cluster.
global_lines = '\n'.join([
    r'\draw (812,160)--(921,977);',
    r'\draw (450,666)--(640,2200);',
    r'\draw (335,1041) .. controls (397,1073) .. (369,1147);',
    r'\draw (1195,526)--(1340,1430);',
    r'\draw[->,line width=3pt] (785,1230)--(947,1238);',
    r'\draw (950,1190)--(1000,2180);',
    r'\node[rotate=90] at (165,592) {\(a\ b\ c\ d\)};',
])
whole_figure = figure('\n'.join(scopes[name] for name in graphics) + '\n' + global_lines)
start = t.index(r'\figure{')
end = t.index('}% crop-candidate: scan 24', start) + 1
t = t[:start] + whole_figure + t[end:]

note3 = (r'\margin{\deleted{\unsure{avec} un ens à trois éléments on fait '
         r'\(3\times2=6\) \unsure{cartes} \unsure{elliptiques} de type \((1,1)\)}}')
total = r'\unsure{1\deleted{4}\inserted{7}|1\deleted{7}\inserted{4}}'
word = r'\unsure{ponts|points}'
assert comp['S24-note3']['first'] in t
t = t.replace(comp['S24-note3']['first'], note3, 1)
assert r'\unsure{17|14}' in t and r'\unsure{cartes|points|ponts}' in t
t = t.replace(r'\unsure{17|14}', total).replace(r'\unsure{cartes|points|ponts}', word)
finals['S24-note3'] = note3
finals['S24-total'] = total
finals['S24-cartes-points-ponts'] = word
finals['S24-bottomtext1'] = comp['S24-bottomtext1']['first'].replace(r'\unsure{17|14}', total).replace(r'\unsure{cartes|points|ponts}', word)

ink = {
'S24-heading': 'The main reader viewed the rotated heading. A small i-like upright stands between the e and the two tall l strokes, supporting Mireille. The ampersand and enfants agree. The blind Mirelle alternative is not supported strongly enough to reopen this reading.',
'S24-cup_tree': 'The inner loop is open and uneven, the central stem has two closely spaced traces, and several lower parts are separated by visible gaps. A short horizontal connection has a rightward head. The independent tracing retains these details more closely than the former regularized cup and stem. Two upper-right curves belong to the neighboring sphere and are not duplicated.',
'S24-top_sphere': 'The outer boundary has an interruption near its upper-right end, with partial retracing at the top and lower-right. Three small directional marks and the broken interior paths are visible. Adopt those geometric details. The separate sign still has an outer loop, inner curl and small raised 3-like black mark; its identity remains circlearrowleft-with-3 versus script S_3, rather than treating the blind literal loops as a resolved sign.',
'S24-pair_spheres': 'The two outer contours have open gaps, and several small rings are themselves open or retraced. The lower-right narrow ring has a short descending leftward head. The independent paths preserve these irregular openings and retracings; the long line crossing the crop is retained once as a full-sheet connector.',
'S24-left_labeled': 'On the clockwise-rotated crop the upper label is Q prime, the opposite lower label is Q, and the short middle label is ell double prime. These are not the blind bar-g, alpha and equals guesses from the unrotated crop. The clear d and circular-arrow label remain; b and c still merge with darker vertex strokes. The new geometry preserves the central polygon, internal triangles, paired arcs, small arrows and open contours. A letter-shaped ell stroke is not duplicated as a drawing curve.',
'S24-middle_spheres': 'The left and central outer contours are uneven and partly open, with distinct peripheral rings. The short stroke left of the central oval starts in blank space and has a visible rightward head. In the right sphere the upper-left rear connection is broken, but the lower-left connection is solid apart from the short separated arrow near its beginning. Both filled side-boundary points and the four rings remain. The second tracing is corrected at that lower connection; crossing full-sheet lines are not duplicated.',
'S24-center_signs': 'The arrow cluster has several distinct converging head strokes and partially separate oblique stems, including the small upper-left arrow and the two wings at the long shaft. Retain these literal paths instead of the former regularized cluster. The separate large loop has an inward stroke but no unambiguous letter or arrowhead; circlearrowleft versus G remains doubtful. Neighboring cap fragments and duplicate long shafts are excluded.',
'S24-cap_segment': 'The outline is uneven and interrupted near the top. A small top point is separate from the larger interior point, and the short line leaving the interior point is solid. The descending connector starts on the heavy front arc and bends into the low loop. The numbered segment retains the filled 0 end, 1 label, and detached tick above its other end. The neighboring crossing curve is retained only in the full-sheet geometry.',
'S24-sphere_map': 'The crop shows a small ring near the top, broken rear meridians, separate short arrowheads on the equator, hatching and partially retraced boundaries. Keep the first labels: the left lower closed oval is 0, the two joined loops are infinity, and the right upright with flag and foot is 1 rather than alpha. The oval above infinity contains a central mark and short upright, so 0 versus circled point remains doubtful. The extra filled point adjoining that oval is a distinct mark. Literal traces of those labels are replaced with their text once, without making extra unlabeled rings.',
'S24-target_sphere': 'Three parallel strokes join the lower rings, with separate dark points at the rings and their contacts. The left lower appendages are short stems, and the right lower appendage contains two joined small loops. The outline and upper connection have visible gaps and partial retracing. Retain those paths and the small upper oval, while excluding the long crossing line and fragments of the adjacent cancelled note already transcribed elsewhere.',
'S24-right_loop': 'The small top oval has a separate short tick and an interrupted upward extension. The larger lower loop is partly retraced along its left and upper sides and ends in a long lower-right trailing curve. These literal contours are more faithful than a smooth closed loop with straight attachments; no alphabetic identity is assigned.',
'S24-small_circles': 'The two small circle outlines and several rings have open gaps, short crossing strokes and a leftward/downward boundary arrow. The separate narrow oval remains distinct. Adopt the literal traces, but omit two crossing full-sheet lines and the partial adjacent map and dome contours so that their ink is represented only once.',
'S24-lower_ovals': 'The large outer and inner ovals are uneven and open, the top rim has a doubled trace and an adjoining loop, and the lower small ring leads to two separate outgoing curves. The isolated narrow left oval is retained. The independent paths preserve these details more closely than the former regular ellipses and single spiral; neighboring upper and right context strokes are omitted.',
'S24-lower_sphere': 'The pole connection has two distinct contours, a small leftward arrow occurs below the rear dashed line, and a separate broken leftward arrow lies near the bottom. The rings are uneven or open, with filled marks at their contacts. Retain the thin outward upper-right ray and the explicit doubled edges, gaps and points; do not regularize their count or make the broken arrows continuous.',
'S24-dome': 'The black outline, two upper rings, rear broken arc, contact strokes, filled points and small crossing wiggle are visible. The main reader also confirmed three left-rim and four right-rim contact points. Retain the green trace parallel to the upper dark arc and the green right descending stripe, which the blind grayscale path text omitted. The independent black geometry is adopted with these color and point corrections, excluding the duplicated crossing line and neighboring small-circle fragment.',
'S24-diamond_formulas': 'The rotated crop has a curved four-sided outline with four filled vertices, four separate outside strokes and a thin crossing interior curve. Adopt the less regular independent paths and restore their original orientation and placement. Both formulas agree in letters, subscripts and signs; they remain once in the margin text, without duplicate nodes in the drawing.',
'S24-vertical_abcd': 'The rotated crop shows the four separate lowercase labels a, b, c and d in that order. The two readings differ only in spacing and margin wrappers; no textual change is made.',
'S24-note3': 'Three thin parallel oblique strokes traverse the whole paragraph and constitute its cancellation; a separate thick nearvertical stroke belongs to the drawing. After the doubtful initial avec, the low u and n and the compact ens are visible, rather than une classe. The next line has on fait, and 3 times 2 equals 6 is clear. The favored cartes and elliptiques outlines survive but are crossed too heavily to assert every letter, so both doubts are reopened. The final pair has two stem-and-foot ones, not a secure 4. No separate comma after éléments is seen.',
'S24-bottomtext1': 'The opening words and the full parenthesis are supported by the wide crop. The total superposes a long dark 7 diagonal and top bar with the short upright and crossbar of 4; their order is not established. The word after it begins with a looped descending p and has o, an n-like join, tall crossed t and final s; ponts is favored, points remains possible, and cartes is excluded. The short following word remains on/ou/or. The type phrase is physically interlinear below trouver, but its exact linear attachment remains uncertain. No arithmetic expectation chooses the overwritten total.',
'S24-bottomtext2': 'The word after deux has the longer drales ending and a tall l, supporting tétraédrales rather than tétraèdres. The cancelled word before inserted trois retains a q descender but is too heavily crossed to resolve every letter of quatre. The cancelled F-like glyph stays doubtful and separate from the first quoted J. The second numeric 1 retains its visible insertion and both live letters have left-hooked J feet. The remaining numbers and words agree.',
'S24-number23': 'The first pencil numeral has a curved upper stroke, oblique descent and rightward foot; the second has two rightward bows. Both readings are 23. The extra mspage wrapper is not an ink difference.',
'S24-on-peut-trouver': 'The rounded o and n join, descending p of peut with its crossed final t, and t-rouve-r sequence of trouver remain legible. The second reading adds neighboring interlinear type text already transcribed in its own insertion. That overlap does not require a second copy or settle the insertion attachment.',
'S24-total': 'The crop visibly superposes the long dark descending diagonal and top bar of 7 with the short upright, crossbar and diagonal of 4. Both components must be represented. Their intersections do not establish which was written last; 4-to-7 is favored from the dark long leg, with 7-to-4 explicitly retained. The arithmetic is not used to force a final 14.',
'S24-cartes-points-ponts': 'The opening stroke descends below the line and returns into a loop, supporting p rather than c. It is followed by an o, n-like joined strokes, a tall crossed t and a terminal s hook. There is no securely placed i dot. Favor ponts with points as the surviving alternative; cartes no longer fits the initial letter.',
'S24-short-word': 'A small closed o is followed by two joined humps. The ending remains too compact to distinguish n, u or r securely. Keep the first ordering on/ou/or; grammar does not resolve it.',
'S24-parenthesis': 'The tight box cuts the leading 1 and opening parenthesis, which are visible in the already-viewed wider bottomtext1 crop. The full reading is 14=3 times 4 plus a cancelled 3 times, then live 2. The 3 and multiplication cross are both struck; the final 2 is not. The blind initial 4 is a crop-boundary omission, not a change to the written number.',
'S24-quatre-trois': 'The cancelled word has the q-like descender, but the strike and the inserted trois obscure several following letters. Retain doubtful quatre under deletion and the clear inserted trois; the blind removal of doubt does not establish every cancelled letter.',
'S24-deux': 'The strike passes through deux only. The following 2 times 3 equals 6 is live and clear. Both readings preserve this scope; math and spacing wrappers are the only literal difference.',
'S24-cancelled-F': 'The cancelled glyph has an upper loop and crossing strokes, with two horizontals compatible with F. Its separate contours are not all recoverable, so F remains doubtful. It is not a certain live letter and is spatially separate from the quoted J.',
'S24-inserted-one': 'The enlarged crop shows a sloping top flag, thick upright and lower foot. This supports the inserted numeral 1 rather than the blind I alternative. Retain the first reading without adding uncertainty.',
'S24-final-J': 'The vertical stem ends in a distinct left-hooked foot below the long top bar. It is J in both readings; the math wrapper changes no letter.',
'S24-map-one': 'The numeral has an upright with a top approach/flag and a lower foot beside the heavy sphere boundary. Both readings give 1; the additional math wrapper changes no ink reading.',
}
assert set(ink) == {k for k, c in comp.items() if c['different'] == 'yes'}
low = {'S24-note3', 'S24-bottomtext1', 'S24-total', 'S24-cartes-points-ponts',
       'S24-short-word', 'S24-quatre-trois', 'S24-cancelled-F'}
medium = {'S24-bottomtext2', 'S24-on-peut-trouver', 'S24-parenthesis', 'S24-map-one'}
entries = []
for key, c in comp.items():
    if c['different'] != 'yes':
        continue
    confidence = 'low' if key in low else 'medium' if key in medium or key in finals else 'high'
    entry = dict(box=key, choice='revised' if key in finals else 'first',
                 viewed_by_main=True, ink=ink[key], confidence=confidence)
    if key in finals:
        entry['final'] = finals[key]
    entries.append(entry)

def crop_fields(key):
    return dict(crop=f'crops/second/148_scan024/{key}.png',
                box=[int(boxes[key][k]) for k in ('x0','y0','x1','y1')])

def update_row(index, key, final=None, confidence=None, **extra):
    r = p['changes'][index]
    r.update(ink=ink[key], **crop_fields(key), **extra)
    if final is not None:
        r['final'] = final
    if confidence:
        r['confidence'] = confidence

# Broaden the existing local geometric rows where they already document the
# same object, without creating a second row for each new TikZ path command.
for index, name in [(2,'top_sphere'), (3,'diamond_formulas'), (4,'left_labeled'),
                    (5,'middle_spheres'), (6,'middle_spheres'), (7,'center_signs'),
                    (8,'cap_segment'), (11,'target_sphere'), (12,'small_circles'),
                    (13,'lower_sphere'), (14,'dome')]:
    key = 'S24-' + name
    update_row(index, key, finals[key], 'medium')
    p['changes'][index]['ink'] += ' Earlier witness differences at this object remain as recorded in the witness columns.'
p['changes'][5]['place'] = 'Middle row, left and central small spheres'
p['changes'][1].update(final=whole_figure,
    ink='The sheet contains the outlines, rings, filled points, dashed paths, labels, colored strokes and full-page connecting lines reproduced below. The main reader personally inspected all 15 differing graphic boxes in the independent second reading and approved the local refinements documented separately. H describes the sheet instead of reproducing it; the cited crop is the middle group, not the entire sheet.',
    confidence='medium', **crop_fields('S24-middle_spheres'))

new_drawing_rows = [
    ('cup_tree', 'Cup and branching graph, open loop and doubled stem'),
    ('pair_spheres', 'Adjoining upper spheres, open contours and retracing'),
    ('sphere_map', 'Mapped sphere, top ring, equator arrows and boundary traces'),
    ('right_loop', 'Right-edge oval and loop, interrupted extensions and retracing'),
    ('lower_ovals', 'Lower double oval, doubled rim and outgoing curves'),
]
for name, place in new_drawing_rows:
    key = 'S24-' + name
    # These four original geometric fragments were unchanged from C before the
    # blind audit. The mapped sphere has earlier separate label corrections;
    # here the original C paths themselves supply the geometry witness.
    witness = comp[key]['first']
    if name == 'sphere_map':
        source = (B.parents[1] / 'source/SP82_C13_148_texts/pages/148_scan024.tex').read_text()
        a = source.index(r'\begin{scope}[shift={(578,1242)}]')
        z = source.index(r'\end{scope}', a) + len(r'\end{scope}')
        witness = figure(source[a:z])
    p['changes'].append(dict(place=place, c=witness, h='Drawing described only',
        final=finals[key], ink=ink[key], **crop_fields(key), confidence='medium',
        kind='drawing or diagram', against_c=True, against_h=True, math=True))

update_row(15, 'S24-note3', r'\unsure{avec} un ens', 'low')
update_row(16, 'S24-note3', r'\unsure{cartes}', 'low')
# C already doubted elliptiques; reopening that doubt is not a C change. H's
# unreadable placeholder still differs from the favored, explicitly doubtful word.
update_row(17, 'S24-note3', r'\unsure{elliptiques}', 'low', against_c=False)
update_row(19, 'S24-total', total, 'low', against_c=True)
update_row(20, 'S24-cartes-points-ponts', word, 'low', against_c=True)
# A new alternative to an unchanged favored 0, and doubt added around an
# unchanged quatre, do not themselves count as changes against C.
p['changes'][9]['against_c'] = False
p['changes'][24]['against_c'] = False
for index, key in [(0,'S24-heading'), (21,'S24-short-word'), (23,'S24-parenthesis'),
                   (24,'S24-quatre-trois'), (25,'S24-cancelled-F'),
                   (28,'S24-inserted-one'), (29,'S24-final-J'),
                   (30,'S24-number23'), (35,'S24-map-one'),
                   (36,'S24-on-peut-trouver'), (37,'S24-on-peut-trouver'),
                   (38,'S24-on-peut-trouver'), (39,'S24-bottomtext2')]:
    update_row(index, key)
p['changes'].append(dict(place='Right-hand note, cancellation of whole paragraph',
    c='Live margin paragraph', h='Live paragraph described as crossed by a pencil line',
    final=note3, ink=ink['S24-note3'], **crop_fields('S24-note3'), confidence='medium',
    kind='deletion state', against_c=True, against_h=True, math=True,
    math_summary='The three-element construction is a cancelled source passage, not live text.'))
p['changes'].append(dict(place='Right-hand note, punctuation after éléments',
    c='éléments, on fait', h='éléments, on fait', final='éléments on fait',
    ink='No separate comma is visible after the terminal s of éléments in the enlarged saved note crop. The following oblique stroke is one of the paragraph cancellation strokes.',
    **crop_fields('S24-note3'), confidence='medium', kind='text not on the page',
    against_c=True, against_h=True, math=False))

decision_updates = {
    'M0257': (r'\unsure{cartes}', 'S24-note3'),
    'M0258': (r'\unsure{elliptiques}', 'S24-note3'),
    'M0262': (total, 'S24-total'),
    'M0263': (word, 'S24-cartes-points-ponts'),
}
for d in p['decisions']:
    if d['id'] in decision_updates:
        reading, key = decision_updates[d['id']]
        d.update(decision='undecided', reading=reading, ink=ink[key],
                 **crop_fields(key), confidence='low')
for u in p['unresolved']:
    if u['id'] in decision_updates:
        reading, key = decision_updates[u['id']]
        u.update(reading=reading, issue=ink[key], **crop_fields(key), confidence='low')
        if u['id'] == 'M0262':
            u['alternatives'] = '4 overwritten by 7 favored; 7 overwritten by 4 also possible'
        elif u['id'] == 'M0263':
            u['alternatives'] = 'points'
for mid, reading, place in [('M0257',r'\unsure{cartes}','cancelled right note, cartes'),
                             ('M0258',r'\unsure{elliptiques}','cancelled right note, elliptiques')]:
    assert not any(u['id'] == mid for u in p['unresolved'])
    p['unresolved'].append(dict(id=mid, place=place, reading=reading,
        issue=ink['S24-note3'], **crop_fields('S24-note3'), confidence='low'))
for u in p['unresolved']:
    if u['id'] == 'M0256':
        u.update(place='Cancelled right note, initial word', issue=ink['S24-note3'],
                 **crop_fields('S24-note3'))

p['inventory'].append(dict(element='I24-31', kind='deletion',
    position='middle-right, three oblique strokes through whole five-line note',
    first_words_or_objects='cancelled avec un ens à trois éléments … de type (1,1)',
    sheet_kind='text', hand='his hand', transcribed='yes'))
p['inventory'].append(dict(element='I24-32', kind='deletion',
    position='bottom-right, overwritten total after trouver',
    first_words_or_objects='superposed 4 and 7; replacement order uncertain',
    sheet_kind='text', hand='his hand', transcribed='yes'))
p['inventory'].append(dict(element='I24-33', kind='insertion',
    position='bottom-right, overwritten total after trouver',
    first_words_or_objects='replacement 7 or 4 over the other numeral',
    sheet_kind='text', hand='his hand', transcribed='yes'))
for inv in p['inventory']:
    if inv['element'] == 'I24-20':
        inv['first_words_or_objects'] = 'cancelled avec un ens à trois éléments'
inventory_order = list(range(1, 21)) + [31, 21, 32, 33] + list(range(22, 31))
inventory_rank = {f'I24-{n:02d}': i for i, n in enumerate(inventory_order)}
p['inventory'].sort(key=lambda r: inventory_rank[r['element']])

for note in p['notes']:
    if note['id'] == 'N24-02':
        note['text'] = ('The total visibly superposes 4 and 7. A 4 corrected to 7 remains favored, but the reverse order is explicit as an alternative. The listed quantities give 2+3+6+6=17, while the separately written parenthesis after deletion is 14=3×4+2. Both source expressions remain; arithmetic does not choose the overwrite order.')
    elif note['id'] == 'N24-03':
        note['text'] = ('The whole right-hand note is crossed by three parallel oblique strokes and is now marked deleted. Its clear short form is un ens, followed by on fait 3×2=6. Avec, cartes and elliptiques remain doubtful under the cancellation. The final pair reads (1,1); its first 1 is dark and retraced, but no definite prior numeral is recoverable.')
    elif note['id'] == 'N24-05':
        note['text'] = ('The drawings remain schematic diplomatic reproductions. The independent second reading led to refinements in fifteen graphic boxes: open contours, doubled traces, separate arrowheads, rings and contact points. Correctly read first labels and both green strokes remain. Native coordinate scopes restore each drawing to its scan position, and overlapping neighbors and full-page lines are represented only once. The two large loop signs and crowded b/c labels remain doubtful.')
    elif note['id'] == 'N24-08':
        note['text'] = ('The cancelled right-hand note associates three elements with 3×2=6 elliptic cartes of type (1,1), with cartes and elliptiques themselves still doubtful. The sheet writes diag_Q ≃ omega_Q and diag_Q wedge omega_Q ≃ codiag_Q and enumerates canonical constructions from a four-element set. These are recorded as source claims; the only mathematical checks performed here remain the three elementary computations K24-01 through K24-03.')
p['notes'].append(dict(id='N24-BLIND', place='Independent second reading',
    text='The main reader personally inspected all 32 differing boxes. Fifteen graphic traces, the cancelled margin note, the overwritten total and the word after it were revised; the overlapping bottom-text box was updated consistently. The preferred word is now ponts, with points retained because no secure i dot survives. The narrow arithmetic crop omits the leading 1, which is visible in the wide crop. No new mathematical proof or computation was performed during this audit.'))
for h in p['hand_log']:
    if h['id'] == 'H24-02':
        h.update(crop='crops/second/148_scan024/S24-inserted-one.jxl',
            witness_effect='C preserved the inserted 1 and H omitted it. The blind I alternative was rejected on the visible numeral flag, upright and foot.')
p['hand_log'].append(dict(id='H24-05', pages='024',
    observation='The total has superposed 4 and 7 contours. Darker strokes suggest a final 7, but crossing order is not securely recoverable.',
    place='bottom total', crop='crops/second/148_scan024/S24-total.jxl',
    holds_at_every_observed_occurrence='One local overtrace; no general overwrite-order rule is inferred.',
    witness_effect='C supplied 17|14 without the two layers; H asserted 14 over 17. Both orders are now explicitly represented.'))
p['notation'].append(dict(form=total, place='bottom total',
    observation='The numeral stratigraphy is explicitly uncertain in both directions; these are source digit shapes rather than an arithmetic correction.',
    crop='crops/second/148_scan024/S24-total.jxl'))
p['blind_graphic_transforms'] = transforms

# Static integrity checks only; the task explicitly prohibits TeX compilation.
assert len(entries) == 32
assert len(finals) == 19
assert t.count(r'\begin{scope}') == t.count(r'\end{scope}') == 15
assert t.count('green!40!black') == 2
assert t.count(r'\operatorname{diag}_Q') == 2
assert t.count(r'\operatorname{codiag}_Q') == 1
for e in entries:
    assert (B / f'crops/second/148_scan024/{e["box"]}.png').is_file()
for key in ['S24-note3', 'S24-total', 'S24-cartes-points-ponts', 'S24-bottomtext1']:
    assert finals[key] in t, key
page.write_text(t)
rp.write_text(json.dumps(p, ensure_ascii=False, indent=2) + '\n')
ap.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'scan':24, 'adjudications':len(entries), 'revised_boxes':len(finals),
    'changes_rows':len(p['changes']), 'inventory_rows':len(p['inventory']),
    'against_c':sum(bool(r['against_c']) for r in p['changes']),
    'against_h':sum(bool(r['against_h']) for r in p['changes'])}))
