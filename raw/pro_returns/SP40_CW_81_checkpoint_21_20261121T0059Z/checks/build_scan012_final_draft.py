#!/usr/bin/env python3
"""Text-only TeX assembly under root's scan012 decisions.

This file reads text only. It never opens an image, performs OCR, runs a
renderer/compiler, adjudicates a manuscript reading, or writes a page/record.
Only the four explicitly assigned draft/assembly files are written.
"""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
import re

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'
TEX = OUT / 'scan012_final_draft.tex'
MAP = OUT / 'scan012_tex_mapping.json'
REPORT = OUT / 'scan012_tex_assembly.md'
ROOT_LOG = OUT / 'scan012_main_decisions.md'
SCALE = 'x=0.0076cm,y=-0.0076cm,line join=round,line cap=round'
source = (BASE / 'packets/012/C.tex').read_text()
root_log = ROOT_LOG.read_text()
reader_tex = {r: (BASE / f'out/readers/012/{r}/reading.tex').read_text() for r in 'ABC'}
reader_prose = {r: (BASE / f'out/readers/012/{r}/reading.md').read_text() for r in 'ABC'}
reader_reports = {r: json.loads((BASE / f'out/readers/012/{r}/report.json').read_text()) for r in 'ABC'}
c_marks = {m['id']: m for m in json.loads((BASE / 'out/readers/012/C/marks_manifest.json').read_text())}
paths = re.findall(r'\\path\[fill=black,even odd rule\]\s*.*?;', source, re.S)
labels = re.findall(r'\\node\[inner sep=0pt[^\n]*;', source)
assert len(paths) == 68
assert len(labels) == 8
for r, text in reader_tex.items():
    assert all(text.count(p) == 1 for p in paths), r

sections = {}
starts = list(re.finditer(r'^(\d+)\. ', root_log, re.M))
for i, m in enumerate(starts):
    end = starts[i+1].start() if i+1 < len(starts) else len(root_log)
    sections[int(m.group(1))] = root_log[m.start():end].strip()

def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()

def span(text, literal):
    p = text.index(literal)
    return {'line_start': text.count('\n', 0, p) + 1,
            'line_end': text.count('\n', 0, p + len(literal)) + 1}

def reader_body(reader, start, stop):
    """Return source draw/fill statements between observed text delimiters."""
    s = reader_tex[reader]
    p = s.index(start)
    q = s.index(stop, p + len(start))
    selected = s[p:q]
    return '\n'.join(re.findall(r'\\(?:draw|path|fill)\[[^\]]*\].*?;', selected, re.S))

def ellipse(x, y, rx, ry, tone):
    return rf'\path[fill=black!{tone}] ({x},{y}) ellipse[x radius={rx},y radius={ry}];'

def a_local(start, stop, dx, dy):
    """Apply the explicit source local-to-full translation to A's path text."""
    body = reader_body('A', start, stop)
    def number(s, offset):
        out = format(Decimal(s) + Decimal(str(offset)), 'f')
        return out.rstrip('0').rstrip('.') if '.' in out else out
    return re.sub(r'\(([-.\d]+),([-.\d]+)\)',
                  lambda m: '('+number(m[1],dx)+','+number(m[2],dy)+')',body)

marks = []
covered = {('A','A012-04'), ('B','B004'), ('C','D004')}

def add(id, entry, location, bbox, body, confidence, aliases=(), source_choice='', alternatives=''):
    assert entry in sections, (id, entry)
    assert body.strip() and all(v is not None for v in bbox)
    marks.append({'id': id, 'root_entry': entry, 'location': location,
                  'bbox_full_pixels': bbox, 'tex_body': body.strip(),
                  'confidence': confidence, 'source_aliases': [list(x) for x in aliases],
                  'source_choice': source_choice,
                  'alternatives_comment': alternatives,
                  'hand': 'undetermined', 'role': 'undetermined',
                  'surface_origin': 'undetermined',
                  'status': 'root-approved geometry; final page approval pending'})
    covered.update(aliases)

# Root entry 1 selects A's gap-only pieces; alternative longer reader paths
# remain source alternatives and are never layered over the selected pieces.
add('A08_left_rim', 1, 'pale interval in the upper right-group oval left rim',
    [875,627,885,658], reader_body('A','% A012-08:','% A012-09a:'), 'medium',
    [('A','A012-08'),('B','B005'),('C','D_N11')], 'A exact gap-only draw statement',
    'B005 and C N11 are comparison alternatives; their longer courses are not additionally drawn.')
add('A09a_low_return', 1, 'separate pale low return of the right-group upper oval',
    [976,811,996,822], reader_body('A','% A012-09a:','% A012-09b:'), 'medium',
    [('A','A012-09a'),('B','B006'),('C','D_N12')], 'A exact low-return statement',
    'The intervening gap before A09b is retained; B006/C N12 are source alternatives.')
add('A09b_lower_slant', 1, 'separate pale lower-right slant of the right-group upper oval',
    [994,788,1019,813], reader_body('A','% A012-09b:','% A012-10:'), 'medium',
    [('A','A012-09b'),('B','B006'),('C','D_N12')], 'A exact separated slant statement',
    'No connection is supplied between this slant and A09a.')
add('A10_two_terminal_wisps', 1, 'two pale wisps beyond the far-right descending terminal',
    [1603,908,1623,926], reader_body('A','% A012-10:','% A012-11:'), 'medium',
    [('A','A012-10'),('B','B007'),('C','D_N14')], 'Both A draw statements, one terminal-location refinement',
    'B007 supports two terminal wisps; no additional B or C duplicate is drawn.')
add('A11_side_oblique', 1, 'small gray oblique beside the right vertical',
    [1385,901,1399,912], r'\draw[black!25,line width=0.20pt] (1387,903.5) -- (1397,910);', 'low',
    [('A','A012-11')], 'A local segment translated by (1387,903.5) into full-pixel coordinates')
add('A19_above_rule_point', 1, 'detached point above the upper rule',
    [904,500,910,507], ellipse(907,503,1,.7,45), 'medium',
    [('A','A012-19'),('C','D_N09')], 'A small ellipse, full-coordinate center (907,503)',
    'C N09 supplies a short slanted-shape alternative at the same approved locus.')
add('B017_below_rule_point', 1, 'dark detached point below the far-right rule end',
    [1640,529,1647,537], r'\path[fill=black] (1643.2,532.4) ellipse[x radius=1.15,y radius=1.4];', 'high',
    [('A','A012-18'),('B','B017'),('C','D_N10')], 'B017 full-coordinate ellipse')
add('B018_below_oval_point', 1, 'small point below the upper right-group oval',
    [1031,820,1037,829], r'\path[fill=black!60] (1034,823) ellipse[x radius=1,y radius=1.1];', 'medium',
    [('B','B018'),('C','D_N13')], 'B018 full-coordinate ellipse')
add('B019_below_transverse_point', 1, 'small point below the lower transverse',
    [1228,857,1234,864], r'\path[fill=black!60] (1231,860.4) ellipse[x radius=0.9,y radius=1.3];', 'medium',
    [('B','B019')], 'B019 full-coordinate ellipse')
add('B016_right_edge_dash', 1, 'independent dash at the right paper edge',
    [1654,790,1674,799], reader_body('B','% B016:','% B017--B019:'), 'high',
    [('A','A012-22'),('B','B016'),('C','D_N15')], 'B exact draw statement reaching the reported paper edge',
    'A and C source geometries remain comparison alternatives; only B is drawn.')

add('B008_interrupted_return', 2, 'interrupted final return and dark hook of the large marked oval',
    [371,751,391,762], reader_body('B','% B008:','% B009--B012:'), 'medium',
    [('B','B008')], 'All three B008 draw/fill statements',
    'This local geometry supplements the retained original C doubt-3 group.')

# Root's new loci have approximate small shapes under the explicit authorizing
# coordinates and descriptions. R9 is already represented in source path 68.
add('R1', 3, 'compact triangular/rounded gray fleck in upper-left context of fourth oval',
    [1275,74,1281,80], r'\path[fill=black!30] (1276.4,78.2) -- (1277.4,75.4) .. controls (1278.1,75.2) and (1279.6,77.0) .. (1279.5,78.2) -- cycle;',
    'medium', source_choice='Root coordinate (1278,77); approximate local shape')
add('R2', 3, 'small upright gray fleck in upper-left context of fourth oval',
    [1294,91,1300,97], r'\path[fill=black!26] (1296.4,92.5) -- (1297.4,92.7) -- (1297.8,95.4) -- (1296.7,95.5) -- cycle;',
    'medium', source_choice='Root coordinate (1297,94); approximate local shape')
add('R3', 4, 'detached gray point inside first upper oval near (418,204)',
    [415,201,421,207], ellipse(418,204,1,1.2,24), 'medium', source_choice='Root coordinate; approximate gray point')
add('R4', 4, 'detached gray point inside first upper oval near (343,252)',
    [340,249,346,255], ellipse(343,252,1,1,22), 'medium', source_choice='Root coordinate; approximate gray point')
add('R5', 4, 'faint compact point within first upper oval lower cap',
    [332,359,338,365], ellipse(335,362,.8,.9,14), 'low', source_choice='Root coordinate; approximate faint point')
add('C_N04', 5, 'gray point below the second upper oval',
    c_marks['N04']['bbox'], c_marks['N04']['tex'], 'medium',
    [('A','A012-21d'),('C','D_N04')], 'C reader N04 exact shape and position',
    'A21d is the source alternative at the same root-approved locus.')
add('R6', 5, 'faint gray point left of second upper oval upper-left side',
    [602,145,608,151], ellipse(605,148,.9,1.1,20), 'medium', source_choice='Root coordinate; approximate faint point')
add('A17_miniature_point', 8, 'detached point immediately inside far-right miniature bottom rim',
    [1586,394,1592,400], ellipse(1588.5,396.6,1.2,1.1,60), 'high',
    [('A','A012-17')], 'A17 small ellipse in full coordinates; same source bounding extent')
add('R7', 8, 'compact pale horizontal fleck outside far-right miniature top-left rim',
    [1583,286,1590,291], ellipse(1586.5,288.5,1.6,.65,24), 'medium', source_choice='Root coordinate; approximate pale horizontal fleck')
add('R8', 9, 'diffuse gray point within central lower oval lower-right interior',
    [680,745,688,753], ellipse(684,749,1.4,1.2,16), 'low', source_choice='Root coordinate; approximate diffuse gray point')
add('R10', 13, 'small gray point below the lower diagonal quadrilateral',
    [228,993,234,999], ellipse(231,996,1,.8,26), 'medium', source_choice='Root coordinate; no corresponding source-path component found')

if 16 in sections:
    add('A20_B015_one_patch', 16, 'one compact gray patch above/left of lower loop tip',
        [427,899,434,906], ellipse(430.5,902.5,1.2,1,24), 'medium',
        [('A','A012-20'),('B','B015')], 'Root-corrected center (430.5,902.5), A ellipse style',
        'A20 and B015 identify one bounded patch; B015 supplies a zero-count source cross-reference and no second path.')

if 17 in sections:
    add('A13a_triangle_tick',17,'separate black upright tick above the small triangle apex',
        [213,443,221,454],a_local('% A012-13a:','% A012-13b:',215.5,446.5),'high',
        [('A','A012-13a'),('B','B009'),('C','D_N05')],
        'A literal local shape translated by (215.5,446.5)')
    add('A13b_triangle_point',17,'small gray point between triangle and large filled point',
        [269,480,277,488],a_local('% A012-13b:','% A012-14:',270.8,481.8),'medium',
        [('A','A012-13b'),('B','B010'),('C','D_N06')],
        'A literal local shape translated by (270.8,481.8)')
    add('C_N07_gap_pale_spot',17,'pale elongated upright spot farther right of triangle',
        c_marks['N07']['bbox'],c_marks['N07']['tex'],'medium',
        [('B','B011'),('C','D_N07')],'C N07 exact full-coordinate graphic')
    add('A14_gap_droplet',17,'dark droplet with short separate pale upper stem',
        [449,496,458,508],a_local('% A012-14:','% A012-15:',451.9,498.6),'high',
        [('A','A012-14'),('B','B012'),('C','D_N08')],
        'A two literal local components translated by (451.9,498.6)',
        'The pale upper stroke and lower dark shape remain separate path statements.')
if 18 in sections:
    for nid,conf,aliases in [('N01','medium',[('A','A012-21a'),('B','B013'),('C','D_N01')]),
                             ('N02','high',[('A','A012-21b'),('B','B014'),('C','D_N02')])]:
        add('C_'+nid,18,c_marks[nid]['location'],c_marks[nid]['bbox'],c_marks[nid]['tex'],conf,
            aliases,'C reader '+nid+' exact local shape',
            'The selected source polygon remains literal; no ellipse replacement is supplied.')
if 19 in sections:
    add('C_N03',19,c_marks['N03']['location'],c_marks['N03']['bbox'],c_marks['N03']['tex'],'high',
        [('A','A012-21c'),('C','D_N03')],'C reader N03 exact full-coordinate compact shape')
if 20 in sections:
    add('A12_lower_hook_cluster',20,'pale lower-field hook, separate low foot, and nearby oblique',
        [382,1286,416,1329],a_local('% A012-12:','% A012-13a:',384,1288),'medium',
        [('A','A012-12'),('B','B020'),('C','D_N16')],
        'All three A12 literal local paths translated by (384,1288)',
        'Main upper descending hook and low return: medium. Separate lower foot: low. Nearby oblique: low. One cluster qualification; no joining stroke supplied.')
    marks[-1]['component_confidence'] = ['medium','low','low']
if 21 in sections:
    add('A15_lower_dark_point',21,'compact dark rounded triangular point in lower field',
        [784,1425,794,1436],a_local('% A012-15:','% A012-16a:',787.3,1427.6),'high',
        [('A','A012-15'),('B','B021'),('C','D_N17')],
        'A literal local polygon translated by (787.3,1427.6)')
if 22 in sections:
    add('A16a_upper_pair_point',22,'upper-right dark member of the lower-right pair',
        [1525,1702,1534,1712],a_local('% A012-16a:','% A012-16b:',1527.9,1704.6),'high',
        [('A','A012-16a'),('B','B023'),('C','D_N20')],
        'A literal local polygon translated by (1527.9,1704.6)')
    add('A16b_lower_pair_point',22,'lower-left dark member of the lower-right pair',
        [1519,1709,1528,1719],a_local('% A012-16b:','% A012-17:',1522.8,1711.3),'high',
        [('A','A012-16b'),('B','B024'),('C','D_N21')],
        'A literal local polygon translated by (1522.8,1711.3)')
    add('C_N19',22,c_marks['N19']['location'],c_marks['N19']['bbox'],c_marks['N19']['tex'],'medium',
        [('A','A012-23c'),('B','B022'),('C','D_N19')],'C N19 exact full-coordinate shape')
if 23 in sections:
    add('A23b_mid_lower_point',23,'small point near (1077.5,1465)',[1074,1462,1081,1468],
        ellipse(1077.5,1465,.6,.8,40),'high',[('A','A012-23b')],
        'A point-list center and ellipse radii/tone in full coordinates')
if 24 in sections:
    add('C_N27_low_upright_cluster',24,c_marks['N27']['location'],c_marks['N27']['bbox'],c_marks['N27']['tex'],'low',
        [('C','D_N27')],'C N27 exact three-component restrained candidate',
        'B retains a texture/diffuse-shading alternative. Central patch: medium; continuation and detached upper point: low. Deliberate stroke and surface origin remain unresolved.')
    marks[-1]['component_confidence'] = ['low','medium','low']
if 25 in sections:
    add('B025_foot_edge_wedge',25,'small dark triangular wedge near the right foot edge',
        [1654,2187,1661,2193],r'\path[fill=black] (1656,2190.8) -- (1658.8,2190.7) -- (1658,2189.2) -- cycle;','high',
        [('A','A012-23h'),('B','B025'),('C','D_N28')],'B025 exact triangular polygon, per root attribution correction',
        'C N28 is a thin diagonal source alternative. Root explicitly selected the B025 polygon after the text-only source comparison; no image was reopened.')
    add('C_N29',25,c_marks['N29']['location'],c_marks['N29']['bbox'],c_marks['N29']['tex'],'high',
        [('A','A012-23g'),('B','B026'),('C','D_N29')],'C N29 exact compact-point shape')
if 26 in sections:
    add('C_N22',26,c_marks['N22']['location'],c_marks['N22']['bbox'],c_marks['N22']['tex'],'high',
        [('A','A012-23d'),('C','D_N22')],'C N22 exact full-coordinate shape')
if 27 in sections:
    add('C_N23',27,c_marks['N23']['location'],c_marks['N23']['bbox'],c_marks['N23']['tex'],'medium',
        [('C','D_N23')],'C N23 exact full-coordinate oblique')
if 28 in sections:
    add('C_N24_fold_cluster',28,'main fold-adjacent compact spot and its separate upper point',
        c_marks['N24']['bbox'],c_marks['N24']['tex'],'medium',
        [('A','A012-23e'),('C','D_N24')],'C N24 exact polygon and separate upper ellipse',
        'Main polygon: medium. Detached upper point: medium. One physical cluster with two explicit local components.')
    marks[-1]['component_confidence'] = ['medium','medium']
    add('C_N31',28,c_marks['N31']['location'],c_marks['N31']['bbox'],c_marks['N31']['tex'],'medium',
        [('C','D_N31')],'C N31 exact detached gray-spot shape')
if 29 in sections:
    add('C_N25',29,c_marks['N25']['location'],c_marks['N25']['bbox'],c_marks['N25']['tex'],'high',
        [('C','D_N25')],'C N25 exact compact ellipse')
    add('R11',29,'pale upright patch immediately below C N25',
        [670,2005,675,2010],ellipse(672.6,2007.4,.65,1.0,20),'low',
        source_choice='Root exact requested center (672.6,2007.4), radii (0.65,1.0), black!20',
        alternatives='A separately qualified zero-count local child of the N25 physical cluster; no punctuation value or deliberate-mark origin is assigned.')
    marks[-1]['cluster_parent'] = 'C_N25'
    marks[-1]['count_as_independent_change'] = False
if 30 in sections:
    add('C_N18',30,c_marks['N18']['location'],c_marks['N18']['bbox'],c_marks['N18']['tex'],'high',
        [('A','A012-23a'),('C','D_N18')],'C N18 exact full-coordinate shape')
if 31 in sections:
    add('C_N26',31,c_marks['N26']['location'],c_marks['N26']['bbox'],c_marks['N26']['tex'],'high',
        [('A','A012-23f'),('C','D_N26')],'C N26 exact full-coordinate shape')
if 32 in sections:
    add('C_N30',32,c_marks['N30']['location'],c_marks['N30']['bbox'],c_marks['N30']['tex'],'medium',
        [('A','A012-23i'),('C','D_N30')],'C N30 exact full-coordinate descending-right oblique',
        'The outer scan boundary supplies no additional character.')

right = {25,32,33,38,39,41,52,54,55,56,60,61,62,64,67}
marked = {34,36,40,42,43,44,45,46,47,48,49,50,51}
states = [
    {'id':'right_group_state', 'entry':1, 'paths':sorted(right), 'bbox':[809.5,348.6,1648.4,1177.4],
     'comment':'Live graphic primary; whole-group cancellation remains the supported alternative. No chronology is supplied.'},
    {'id':'original_C_doubt3', 'entry':2, 'paths':sorted(marked), 'bbox':[156.5,564,381.5,894.5],
     'comment':'Existing C doubt 3: overlaid zigzags primary; cancellation of the larger oval remains an alternative. The shared lower miniature remains live.'},
]

def qualified_graphic(id, bbox, body, comment):
    """Place a literal full-coordinate graphic without shifting its geometry.

    The nested picture's fixed box starts at xmin. Its baseline yref is placed
    at the same full-coordinate yref by a base-west outer anchor. The graphical
    drawing lives in an overlay scope, so stroke widths and the question-mark
    annotation cannot change the chosen graphic origin.
    """
    x0,y0,x1,y1 = bbox
    yref = (y0+y1)/2
    return '\n'.join([
        f'% BEGIN QUALIFIED GRAPHIC {id}',
        '% '+comment.replace('\n','\n% '),
        rf'\node[inner sep=0pt,outer sep=0pt,anchor=base west] at ({x0},{yref}) {{\unsure{{\begin{{tikzpicture}}[{SCALE},baseline={{({x0},{yref})}}]',
        rf'\path[use as bounding box] ({x0},{y0}) rectangle ({x1},{y1});',
        r'\begin{scope}[overlay]', body, r'\end{scope}',
        r'\end{tikzpicture}}};',
        f'% END QUALIFIED GRAPHIC {id}',
    ])

parts = [r'\scanpage{12}',
         '% Assembly draft only; final approval remains with the root reader.',
         '% All source full-pixel coordinates and literal C contour blocks are retained.',
         '% Editorial descriptions and alternatives appear only in comments.',
         r'\figure{\begin{tikzpicture}['+SCALE+']']

for n, p in enumerate(paths, 1):
    state = next((x for x in states if n == min(x['paths'])), None)
    if state:
        body = '\n'.join(f'% C source path {i:02d}: literal block retained once.\n'+paths[i-1] for i in state['paths'])
        parts.append(qualified_graphic(state['id'], state['bbox'], body,
                                      f"Root entry {state['entry']}. {state['comment']}"))
    elif n not in right | marked:
        parts.extend([f'% C source path {n:02d}: literal block retained once.', p])
parts += ['% The eight original label nodes are retained literally once each.'] + labels
for mark in marks:
    comment = (f"Root entry {mark['root_entry']}; {mark['location']}; confidence {mark['confidence']}.\n"
               'Hand, role, and surface origin are undetermined; no character or semantic role is supplied.\n'
               + mark['source_choice'])
    if mark['alternatives_comment']:
        comment += '\n'+mark['alternatives_comment']
    block = qualified_graphic(mark['id'], mark['bbox_full_pixels'], mark['tex_body'], comment)
    mark['qualified_tex'] = block
    parts.append(block)
parts += [r'\end{tikzpicture}}', '% archive sheet number: 11', '']
draft = '\n'.join(parts)

# Literal-preservation checks only. No original path is replaced or duplicated.
assert len(re.findall(r'\\path\[fill=black,even odd rule\]', draft)) == 68
assert all(draft.count(p) == 1 for p in paths)
assert all(draft.count(label) == 1 for label in labels)
assert len(marks) == len({m['id'] for m in marks})
assert not any(m['id'] == 'R9' for m in marks)
for m in marks:
    assert r'\unsure{\begin{tikzpicture}' in m['qualified_tex']
TEX.write_text(draft)

# Execute only the existing validator's definitions, never its global report
# writer. The returned error array is explicitly asserted; no TeX run occurs.
validator_path = BASE / 'out/scripts/validate.py'
validator_prefix = validator_path.read_text().split('records=[json.loads', 1)[0]
validator_ns = {'__file__':str(validator_path)}
exec(validator_prefix, validator_ns)
structural_result = validator_ns['check_tex'](TEX)
assert structural_result['errors'] == [], structural_result['errors']

pending = []
for reader, report in reader_reports.items():
    for row in report['differences']:
        if row.get('diff_C') and (reader,row['id']) not in covered:
            pending.append({'reader':reader, 'id':row['id'], 'location':row['location'],
                            'bbox':row.get('bbox'), 'status':'pending root selection; excluded from this TeX draft'})

# The additive rows above are supplemented by explicit mappings for the
# retained labels, original geometry, and editorial source-state rows.
base_rows = {}
def base_row(reader, ids, source_paths=(), source_labels=(), state=None, entries=(), comment=None):
    for rid in ids:
        base_rows[(reader,rid)] = {'source_paths':list(source_paths),'source_labels':list(source_labels),
                                  'state_wrapper':state,'root_entries':list(entries),'comment':comment}
for r, rid in [('A','A012-01'),('B','B001'),('C','D001')]:
    base_row(r,[rid],source_labels=[4],entries=[3])
for r, rid in [('A','A012-02'),('B','B002'),('C','D002')]:
    base_row(r,[rid],source_labels=[8],entries=[2])
for r, rid in [('A','A012-03'),('B','B003'),('C','D003b')]:
    base_row(r,[rid],source_paths=sorted(marked),state='original_C_doubt3',entries=[2])
for r, rid in [('A','A012-04'),('B','B004'),('C','D004')]:
    base_row(r,[rid],source_paths=sorted(right),state='right_group_state',entries=[1])
for r, rid in [('A','A012-05'),('B','B028')]:
    base_row(r,[rid],source_paths=[27],entries=[15])
for r, rid in [('A','A012-06'),('B','B030')]:
    base_row(r,[rid],source_paths=[66],entries=[16])
for r, rid in [('A','A012-07'),('B','B029')]:
    base_row(r,[rid],source_paths=[34,53,57,58,59,63],source_labels=[7,8],entries=[2],
             comment='Path34 is shared with the larger marked oval; no literal contour is split or duplicated.')
base_row('B',['B027'],source_paths=range(1,25),source_labels=[1,2,3,4,5],entries=[3,4,5,6,7,8])
base_row('B',['B031'],source_paths=[37],entries=[9])
base_row('C',['D003a'],source_paths=sorted(marked),entries=[2])
base_row('C',['D005'],source_labels=range(1,9),entries=[2,3,4,5,6,7,8])
base_row('C',['D006'],source_paths=range(1,69),source_labels=range(1,9),entries=range(1,18),
         comment='Reader aggregate drawing-field audit is covered by the retained literal source paths; the root record clerk owns physical H grouping.')
base_row('C',['D007'],source_paths=[57],entries=[2])
base_row('C',['D008'],comment='Original archive sheet number: 11 retained as a comment only.')

reader_row_map = []
unmapped_rows = []
for reader, report in reader_reports.items():
    for index, row in enumerate(report['differences']):
        alias = (reader,row['id'])
        selected = [m['id'] for m in marks if list(alias) in m['source_aliases']]
        base = base_rows.get(alias)
        status = 'mapped' if selected or base is not None else 'UNMAPPED'
        entry = {'reader':reader,'source_id':row['id'],
                 'source_report':f'out/readers/012/{reader}/report.json',
                 'pointer':f'/differences/{index}','location':row['location'],
                 'selected_addition_ids':selected,'retained_source_mapping':base,'status':status}
        reader_row_map.append(entry)
        if status == 'UNMAPPED':
            unmapped_rows.append(entry)

row_aliases = {(x['reader'],x['source_id']) for x in reader_row_map if x['status']=='mapped'}
prose_audit = []
for reader, text in reader_prose.items():
    pattern = {'A':r'\bA012-\d{2}[a-z]?\b','B':r'\bB\d{3}\b','C':r'\bN\d{2}\b'}[reader]
    tokens = sorted(set(re.findall(pattern,text)))
    aliases = [('D_'+x if reader=='C' else x) for x in tokens]
    unmapped = [x for x in aliases if (reader,x) not in row_aliases]
    prose_audit.append({'reader':reader,'path':f'out/readers/012/{reader}/reading.md',
        'sha256':sha(text),'line_count':len(text.splitlines()),
        'sections':[line[3:] for line in text.splitlines() if line.startswith('## ')],
        'mentioned_candidate_ids':tokens,'unmapped_candidate_ids':unmapped,
        'coverage':'Prose drawing-register audits map to the 68 retained source paths and eight labels; all mentioned new-mark IDs map through the reader-row crosswalk.',
        'additional_prose_findings':[
            'The archive numeral is a retained source comment.',
            'The two isolated looping graphics remain source paths27 and66 without supplied characters.',
            'The left margin dash remains source path57; the separate right margin dash uses B016.',
            'No additional bounded graphical candidate was identified in these text audits beyond the mapped source rows.',
        ] + (['The B prose texture/diffuse-shading reading near (1446,2100) is retained in the C_N27_low_upright_cluster alternative comment under root entry24.'] if reader=='B' else [])})

doubt_source_map = []
for reader, report in reader_reports.items():
    for index, row in enumerate(report['doubts']):
        if reader == 'A':
            rid = row['id'][2:]
        elif reader == 'B':
            rid = row['difference_id']
        else:
            local = row['local_id']
            rid = {'C.DR1.K':'D001','C.DR2.word':'D002','C.DR3.state':'D003b','right_group.state':'D004'}.get(local,'D_'+local)
        doubt_source_map.append({'reader':reader,'pointer':f'/doubts/{index}',
                                 'location':row['location'],'mapped_difference_id':rid,
                                 'status':'mapped' if (reader,rid) in row_aliases else 'UNMAPPED'})

source_path_map = []
for n, p in enumerate(paths, 1):
    coords = [tuple(map(float,x)) for x in re.findall(r'\(([-.\d]+),([-.\d]+)\)',p)]
    group = next((st['id'] for st in states if n in st['paths']), None)
    source_path_map.append({'source_path':n, 'sha256':sha(p), 'literal_occurrences_in_draft':draft.count(p),
        'source':{'path':'packets/012/C.tex', **span(source,p)},
        'draft':{'path':str(TEX.relative_to(BASE)), **span(draft,p)},
        'bbox_from_literal_vertices':[min(x for x,y in coords),min(y for x,y in coords),max(x for x,y in coords),max(y for x,y in coords)],
        'state_wrapper':group})
for m in marks:
    m['draft_span'] = span(draft,m['qualified_tex'])
    del m['qualified_tex']

mapping = {'scan':12, 'kind':'text-only assembly draft', 'root_final_approval_pending':True,
    'generated_utc':datetime.now(timezone.utc).isoformat(),
    'root_log':{'path':str(ROOT_LOG.relative_to(BASE)), 'sha256':sha(root_log), 'numbered_entries_present':sorted(sections)},
    'source_fingerprints':{'C_tex':sha(source), **{f'reader_{r}_tex':sha(t) for r,t in reader_tex.items()},
                           **{f'reader_{r}_prose':sha(t) for r,t in reader_prose.items()}},
    'constraints':{'images_opened':False,'ocr_used':False,'external_research_used':False,'tex_compiled':False,'mathematical_checks_run':False,
                   'original_C_paths_preserved_exactly_once':68,'original_C_label_nodes_preserved_exactly_once':8},
    'coordinate_wrapper':{'anchor':'base west','inner_baseline':'same literal (xmin,yref) as outer node position',
                          'bounding_box':'fixed supplied full-pixel rectangle','drawing_scope':'overlay',
                          'purpose':'retain literal full-pixel geometry independently of uncertainty annotation extent'},
    'source_paths':source_path_map,
    'source_labels':[{'literal':x,'occurrences':draft.count(x),'source':span(source,x),'draft':span(draft,x)} for x in labels],
    'state_wrappers':states, 'new_graphical_additions':marks,
    'existing_component_confirmations':[{'id':'R9','root_entry':13,'source_path':68,'new_path_added':False,
        'no_C_difference':True,'literal_excerpt':'(175.3,942) -- (173,941.4) -- (172.6,941) -- (172.6,940) -- (176.3,940)',
        'root_followup':'Retain the source excursion; no duplicate R9 path.'}],
    'pending_candidate_source_rows':pending,
    'all_reader_difference_rows':reader_row_map,
    'unmapped_reader_difference_rows':unmapped_rows,
    'reader_prose_audit':prose_audit,
    'reader_doubt_source_mapping':doubt_source_map,
    'structural_check':structural_result,
    'handoff':'No final page, record, cumulative transcription, or cumulative report was written.'}
MAP.write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')

lines = ['# Scan012 TeX assembly draft', '',
         '**Status: root final approval pending.** This is mechanical assembly from the numbered root decisions; the assembly clerk has not read or processed any image.', '',
         f"Root log snapshot contains numbered entries {', '.join(map(str,sorted(sections)))}.", '',
         '## Preserved source', '',
         '- All 68 original C fill-path blocks occur literally and exactly once.',
         '- All eight original C label nodes occur literally and exactly once, including the two original lexical uncertainty macros.',
         '- Source doubt 3 retains its large-oval state qualification. The shared lower miniature remains live in the root decision.',
         '- The right-hand group has the root-approved live/cancellation state qualification; every underlying path remains literal.',
         '- The archive sheet numeral is retained only as its original comment.', '',
         'The local graphic wrappers use the same full-coordinate inner baseline and outer base-west anchor. Fixed boxes and overlay scopes keep the ink placement independent of the question-mark extent. No verbal description has been inserted into the manuscript text.', '',
         '## Approved additions included', '',
         '| Assembly ID | Root entry | Source choice | Confidence |',
         '|---|---:|---|---|']
for m in marks:
    lines.append(f"| {m['id']} | {m['root_entry']} | {m['source_choice']} | {m['confidence']} |")
lines += ['', 'Every addition is in its own local graphical `\\unsure{...}` wrapper. Comments state that hand, role, and surface origin remain undetermined. Reader alternatives are recorded in comments and the JSON mapping.', '',
          '## Duplicate handling', '',
          '- R9 is already represented in the main closed subpath of C path 68 through `(175.3,942) -- (173,941.4) -- (172.6,941) -- (172.6,940) -- (176.3,940)`. The root accepted that finding. No R9 path is added, and it has no C difference.',
          '- R10 has no corresponding detached component in path 68 and remains an approved new gray point.',
          '- A20 and B015 are one patch at the root-corrected center `(430.5,902.5)`; one ellipse is included. B015 is only a source cross-reference.',
          '- The separated A09a and A09b geometry is preserved with its gap. The two A10 terminal wisps share one local qualification.', '',
          '## Pending candidate source rows', '',
          'These reader proposals have not yet been selected by a root decision consumed by this build. They are excluded from the draft. Rows here are reader source rows, so several rows can refer to the same physical locus; this table supplies no final locus count.', '',
          '| Reader | Source ID | Location |', '|---|---|---|']
for p in pending:
    lines.append(f"| {p['reader']} | {p['id']} | {p['location'].replace('|',' / ')} |")
if not pending:
    lines.append('| — | — | No pending additive reader source row. |')
lines += ['', '## Reader prose and source-row reconciliation', '',
          f"All {len(reader_row_map)} reader difference rows have explicit new-graphic or retained-source mappings; {len(unmapped_rows)} remain unmapped.",
          f"All {len(doubt_source_map)} reader doubt rows are cross-referenced to those mapped rows.",
          'The three reading.md prose audits were read as text. Their register descriptions, original contour inventories, local uncertainty descriptions, boundary notes, and new-mark lists are covered by the source-path, label, state, and addition mappings. No additional bounded candidate remains unaccounted for in those text audits.',
          'B’s prose alternative near `(1446,2100)` is explicitly retained in the low-upright cluster comment. Reader source cancellation alternatives remain in the two state wrappers. The source label `OK` remains literal; the possible expansion is confined to reader apparatus.',
          'C N24’s main and upper components remain one two-path qualified cluster. R11 is separately qualified at `(672.6,2007.4)` with the requested radii and gray tone, and is mapped as a zero-count child of C N25.', '',
          '| Reader prose | Explicit candidate IDs | Unmapped IDs |', '|---|---:|---|']
for p in prose_audit:
    lines.append(f"| {p['reader']} | {len(p['mentioned_candidate_ids'])} | {', '.join(p['unmapped_candidate_ids']) or 'none'} |")
lines += ['', '## Structural verification and scope', '',
          f"`out/scripts/validate.py` function `check_tex` returned `errors: {json.dumps(structural_result['errors'])}`; the empty array was asserted.",
          f"The draft contains {structural_result['marks']['unsure']} uncertainty macros, including the two original lexical macros, two state wrappers, and {len(marks)} local new-graphic wrappers.",
          'No compiler, renderer, OCR, browser, external research, or mathematical check was used. No final page, record, cumulative transcription, or cumulative report was written.', '',
          'The mapping records literal-path hashes and source/draft line spans, the eight labels, every selected addition, pending source rows, and the root-log fingerprint.', '']
REPORT.write_text('\n'.join(lines))
print(json.dumps({'draft':str(TEX.relative_to(BASE)), 'source_paths':68, 'labels':8,
                  'approved_local_additions':len(marks), 'pending_source_rows':len(pending),
                  'unmapped_reader_difference_rows':len(unmapped_rows),
                  'structural_errors':structural_result['errors'], 'root_final_approval_pending':True}))
