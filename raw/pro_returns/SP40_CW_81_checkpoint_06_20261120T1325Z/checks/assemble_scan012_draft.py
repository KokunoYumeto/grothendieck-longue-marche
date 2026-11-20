#!/usr/bin/env python3
"""Text-only mechanical collation of scan012 reader returns.

Reads only packet012 and the three reader012 text returns.  Writes only the
record draft and mapping named below.  It does not inspect images, run OCR,
render or compile TeX, or perform mathematical checks.  Ink choices remain
pending until root supplies them.
"""
from pathlib import Path
from collections import defaultdict
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import re

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'
REPORT_PATHS = {r: f'out/readers/012/{r}/report.json' for r in 'ABC'}
TEX_PATHS = {r: f'out/readers/012/{r}/reading.tex' for r in 'ABC'}
reports = {r: json.loads((BASE / p).read_text()) for r, p in REPORT_PATHS.items()}
texts = {r: (BASE / p).read_text() for r, p in TEX_PATHS.items()}
source_tex = (BASE / 'packets/012/C.tex').read_text()
source_H = (BASE / 'packets/012/H.tex').read_text()
source_inventory = json.loads((BASE / 'packets/012/C_inventory.json').read_text())
metadata = json.loads((BASE / 'packets/012/metadata.json').read_text())
diffs = {r: {x['id']: x for x in reports[r]['differences']} for r in 'ABC'}
diff_index = {r: {x['id']: i for i, x in enumerate(reports[r]['differences'])} for r in 'ABC'}

def ref(path, pointer=None, **kw):
    out = {'path': path}
    if pointer is not None:
        out['pointer'] = pointer
    out.update(kw)
    return out

def source_range(path, text, start, end):
    return ref(path, line_start=text.count('\n', 0, start) + 1,
               line_end=text.count('\n', 0, end) + 1,
               exact_excerpt=text[start:end])

def exact_ref(path, text, literal):
    at = text.find(literal)
    if at < 0:
        return ref(path, exact_excerpt=literal, found=False)
    return source_range(path, text, at, at + len(literal))

def line_ref(r, literal):
    text = texts[r]
    at = text.find(literal)
    if at < 0:
        return []
    start = text.rfind('\n', 0, at) + 1
    end = text.find('\n', at)
    if end < 0:
        end = len(text)
    return [source_range(TEX_PATHS[r], text, start, end)]

def statement_ref(r, literal):
    text = texts[r]
    at = text.find(literal)
    if at < 0:
        return []
    start = text.rfind('\n', 0, at) + 1
    # Each supplied literal starts within the first line of its statement.
    end = text.find(';', at)
    if end < 0:
        return []
    return [source_range(TEX_PATHS[r], text, start, end + 1)]

def comment_block(r, prefix, next_pattern=None):
    text = texts[r]
    at = text.find(prefix)
    if at < 0:
        return []
    start = text.rfind('\n', 0, at) + 1
    if next_pattern:
        m = re.search(next_pattern, text[at + len(prefix):], re.M)
        end = at + len(prefix) + m.start() if m else len(text)
    else:
        m = re.search(r'^% (?:A012-|B\d{3}|N\d\d:|Short labels:|archive sheet)', text[at + len(prefix):], re.M)
        end = at + len(prefix) + m.start() if m else len(text)
    return [source_range(TEX_PATHS[r], text, start, end)]

original_paths = []
for m in re.finditer(r'^\\path\[fill=black,even odd rule\]', source_tex, re.M):
    end = source_tex.index(';', m.start()) + 1
    original_paths.append(source_range('packets/012/C.tex', source_tex, m.start(), end))
if len(original_paths) != 68:
    raise RuntimeError('Original C path inventory changed; mechanical review is required.')

B_path_audit = {x['path']: x for x in reports['B']['source_path_audit']}
original_path_refs = {i: dict(original_paths[i - 1], source_path=i,
                              bbox=B_path_audit[i]['bbox']) for i in range(1, 69)}

def path_refs(r, numbers):
    out = []
    for n in numbers:
        x = exact_ref(TEX_PATHS[r], texts[r], original_path_refs[n]['exact_excerpt'])
        x['source_C_path'] = n
        x['retained_exactly'] = x.get('found', True)
        out.append(x)
    return out

def bbox_from_paths(numbers):
    boxes = [B_path_audit[n]['bbox'] for n in numbers]
    return [min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes)]

def combined_bbox(boxes):
    boxes = [b for b in boxes if b]
    return [min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes)] if boxes else None

def rowref(r, row_id):
    return ref(REPORT_PATHS[r], f'/differences/{diff_index[r][row_id]}', row_id=row_id)

def crop_path(r, p):
    return f'out/readers/012/{r}/{p}' if p else None

# The H rereading note controls the earlier label count.  The final section
# and note explicitly assigned to feuillet13 are excluded from scan012.
H_DRAWING = source_H[source_H.index('\\drawing'):source_H.index('\\note')].strip()
H_NOTE = source_H[source_H.index('\\note'):source_H.index('\\section')].strip()
H_EXCLUDED = source_H[source_H.index('\\section'):].strip()
H_DISKS = 'disques coupés\nde cordes, une région triangulaire ou quadrangulaire hachurée'
H_VARIANTS = 'des variantes introduites par « ou »'
H_RIGHT = 'À droite, deux axes fléchés en équerre et, dans l’angle,\ndes courbes qui se croisent et deux disques coupés d’arcs'
# Use exact source apostrophes, which are ASCII in this packet.
H_RIGHT = "À droite, deux axes fléchés en équerre et, dans l'angle,\ndes courbes qui se croisent et deux disques coupés d'arcs"

specs = []
def add(key, location, A=(), B=(), C=(), paths=(), c_inventory=(),
        kind='omission', dc=False, dh=False, h='[omitted]',
        hgroup=None, hcount=False, count_parent=None, bbox=None,
        role='local', note='', marked='no', doubt_source=None):
    specs.append(dict(key=key, location=location, rows={'A': list(A), 'B': list(B), 'C': list(C)},
                      paths=list(paths), c_inventory=list(c_inventory), kind=kind,
                      diff_C=dc, diff_H=dh, H=h, H_group_key=hgroup,
                      H_group_count_row=hcount, count_parent_key=count_parent,
                      bbox=bbox, role=role, assembly_note=note,
                      marked_in_H=marked, C_doubt_source_row=doubt_source))

marked_paths = [34, 36, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]
right_paths = [25, 32, 33, 38, 39, 41, 52, 54, 55, 56, 60, 61, 62, 64, 67]
third_paths = [4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22, 24]

add('label', 'Fourth upper oval: OK/Ok label', ['A012-01'], ['B001'], ['D001'],
    c_inventory=['012.08'], kind='other', h='quatre disques sont marqués « OK » (ou « ok »)', marked='yes', doubt_source=1)
add('ou', 'Word between lower-left miniature ovals', ['A012-02'], ['B002'], ['D002'],
    c_inventory=['012.23'], kind='other', h=H_VARIANTS, hgroup='parenthetical', doubt_source=2)
add('marked_state', 'Large lower-left marked oval: editorial state', ['A012-03'], ['B003'], ['D003b'],
    paths=marked_paths, c_inventory=['012.18'], kind='other', h=H_DISKS,
    hgroup='marked_oval', doubt_source=3,
    note='This state doubt is already present in original C doubtful-readings row 3. A local unsure annotation introduces no independent C reading change.')
add('right_state', 'Whole right-hand ruled and curved drawing group', ['A012-04'], ['B004'], ['D004'],
    paths=right_paths, c_inventory=['012.29','012.30','012.31','012.32'],
    kind='deletion state (struck given live or live given struck)', dc=True, dh=True,
    h=H_RIGHT + '\n' + H_NOTE, hgroup='right_group', hcount=True, role='H physical-object count',
    note='Proposed C=true records the newly added live/cancelled qualification. A and C-reader original false flags are preserved below. One physical H group also covers its local graphical detail changes.')
add('top_first', 'First large upper oval, hatched triangle and lower cap arc', B=['B027'], C=['D006'], paths=[2],
    c_inventory=['012.01'], kind='drawing or diagram', dh=True, h=H_DISKS, hgroup='top_first', hcount=True, role='H physical-object count')
add('top_small_first', 'Small upper alternative oval after the first ou', B=['B027'], C=['D006'], paths=[1],
    c_inventory=['012.03'], kind='drawing or diagram', dh=True, h=H_DISKS+'; '+H_VARIANTS, hgroup='top_small_first', hcount=True, role='H physical-object count')
add('top_second', 'Second large upper oval, uprights and thick crosspiece', B=['B027'], C=['D006'], paths=[3],
    c_inventory=['012.05'], kind='drawing or diagram', dh=True, h=H_DISKS, hgroup='top_second', hcount=True, role='H physical-object count')
add('top_third', 'Third large upper oval, hatched quadrilateral', B=['B027'], C=['D006'], paths=third_paths,
    c_inventory=['012.07'], kind='drawing or diagram', dh=True, h=H_DISKS, hgroup='top_third', hcount=True, role='H physical-object count')
add('top_fourth', 'Fourth large upper oval, hatched triangle and thick segment', B=['B027'], C=['D006'], paths=[5,13,18],
    c_inventory=['012.09'], kind='drawing or diagram', dh=True, h=H_DISKS, hgroup='top_fourth', hcount=True, role='H physical-object count')
add('top_small_right', 'Far-right small alternative oval with thick radius', B=['B027'], C=['D006'], paths=[23],
    c_inventory=['012.11'], kind='drawing or diagram', dh=True, h=H_DISKS+'; '+H_VARIANTS, hgroup='top_small_right', hcount=True, role='H physical-object count')
add('triangle', 'Triangle and separate filled point below first oval: triangle component', C=['D006'], paths=[30],
    c_inventory=['012.12'], kind='drawing or diagram', dh=True, h='un\ntriangle, un point', hgroup='triangle_point', hcount=True, role='H physical-object count',
    note='The triangle and filled point have separate component rows; their source inventory and local graph passage support one proposed H group, pending root H-count choice.')
add('filled_dot', 'Separate filled point beside the small triangle', C=['D006'], paths=[31], c_inventory=['012.12'],
    kind='drawing or diagram', h='un\ntriangle, un point', hgroup='triangle_point')
add('upper_loop', 'Detached upright looping mark before the thick tripod', ['A012-05'], ['B028'], ['D006'], paths=[27],
    c_inventory=['012.13'], kind='omission', dh=True, h='[omitted from H graph enumeration]', hgroup='upper_loop', hcount=True, role='H physical-object count')
add('tripod', 'Thick three-pronged figure', C=['D006'], paths=[29], c_inventory=['012.14'], kind='drawing or diagram',
    dh=True, h='un tripode épais en « Y »', hgroup='tripod', hcount=True, role='H physical-object count')
add('square', 'Square below third upper oval', C=['D006'], paths=[28], c_inventory=['012.15'], kind='drawing or diagram',
    dh=True, h='un carré', hgroup='square', hcount=True, role='H physical-object count')
add('stem_triangle', 'Triangle with rising stem below fourth upper oval', C=['D006'], paths=[26], c_inventory=['012.16'], kind='drawing or diagram',
    dh=True, h="un triangle\nsurmonté d'un segment", hgroup='stem_triangle', hcount=True, role='H physical-object count')
add('left_wedges', 'Far-left oval in the second register, two filled wedges', C=['D006'], paths=[35], c_inventory=['012.17'], kind='drawing or diagram',
    dh=True, h=H_DISKS, hgroup='left_wedges', hcount=True, role='H physical-object count', note='H gives a general disk description without separately locating this oval; root classification remains pending.')
add('marked_oval', 'Large marked left oval: complete physical drawing', ['A012-03'], ['B003'], ['D003a','D006'], paths=marked_paths,
    c_inventory=['012.18'], kind='drawing or diagram', dh=True, h=H_DISKS, hgroup='marked_oval', hcount=True, role='H physical-object count',
    note='Local state, underlying oval, inner hatching, outer loops, terminal extension and connection are cross-referenced; no extra H count for those local rows.')
add('parenthetical', 'Lower-left parenthetical pair of miniature alternatives', ['A012-07'], ['B029'], ['D006'], paths=[53,57,58,59,63,34],
    c_inventory=['012.20','012.21','012.22','012.23','012.24'], kind='omission', dh=True, h='[not separately located in H]; '+H_VARIANTS,
    hgroup='parenthetical', hcount=True, role='H physical-object count', bbox=[24,757,407,921],
    note='One H omission group contains two miniature ovals, both parenthesis arcs and detached left dash. Path 34 also includes the large marked oval; its lower-miniature component is the reference here.')
add('opening_arc', 'Opening parenthesis of lower miniature pair', ['A012-07'], ['B029'], ['D006'], paths=[53], c_inventory=['012.20'],
    kind='drawing or diagram', h='[not separately transcribed]; '+H_VARIANTS, hgroup='parenthetical')
add('closing_arc', 'Closing parenthesis of lower miniature pair', ['A012-07'], ['B029'], ['D006'], paths=[58], c_inventory=['012.20'],
    kind='drawing or diagram', h='[not separately transcribed]; '+H_VARIANTS, hgroup='parenthetical')
add('left_dash', 'Detached dash beside opening parenthesis', ['A012-07'], ['B029'], ['D007'], paths=[57], c_inventory=['012.20'],
    kind='drawing or diagram', h='[omitted]', hgroup='parenthetical', note='C-reader supplies a separate inventory row for this existing C path; original C inventory and A/B put it with the parenthesis assembly.')
add('lower_mini_left', 'Left miniature oval inside parentheses', B=['B029'], C=['D006'], paths=[59,63], c_inventory=['012.22'],
    kind='drawing or diagram', h='[not separately located]; '+H_VARIANTS, hgroup='parenthetical')
add('lower_mini_right', 'Right miniature oval, connected to the large marked oval', B=['B029'], C=['D006'], paths=[34], c_inventory=['012.24'],
    kind='drawing or diagram', h='[not separately located]; '+H_VARIANTS, hgroup='parenthetical', bbox=[238,779,381.5,894.5],
    note='The source path crosses the large-oval and lower-miniature loci. The full source path is retained as provenance; the local connection and miniature remain separately identified.')
add('central_oval', 'Central second-register oval with chords and hatched wedge', B=['B031'], C=['D006'], paths=[37], c_inventory=['012.25'],
    kind='drawing or diagram', dh=True, h=H_DISKS, hgroup='central_oval', hcount=True, role='H physical-object count')
add('lower_quadrilateral', 'Lower-left quadrilateral with diagonal', C=['D006'], paths=[68], c_inventory=['012.26'],
    kind='drawing or diagram', dh=True, h="un rectangle coupé d'une diagonale", hgroup='lower_quadrilateral', hcount=True, role='H physical-object count')
add('lower_zigzag', 'Detached lower upright zigzag', ['A012-06'], ['B030'], ['D006'], paths=[66], c_inventory=['012.27'],
    kind='omission', dh=True, h='[omitted from H graph enumeration]', hgroup='lower_zigzag', hcount=True, role='H physical-object count')
add('spoked_triangle', 'Lower triangle with three interior spokes', C=['D006'], paths=[65], c_inventory=['012.28'],
    kind='drawing or diagram', dh=True, h='un triangle à\npoint intérieur', hgroup='spoked_triangle', hcount=True, role='H physical-object count')
add('right_rules', 'Right group: repeated corner boundary lines', C=['D006'], paths=[25,32], c_inventory=['012.29'],
    kind='drawing or diagram', h=H_RIGHT+'\n'+H_NOTE, hgroup='right_group')
add('right_tall', 'Right group: upper tall oval and crossings', C=['D006'], paths=[33,41,55,60,61], c_inventory=['012.30'],
    kind='drawing or diagram', h=H_RIGHT, hgroup='right_group')
add('right_curves', 'Right group: extended crossing curves and local fragments', C=['D006'], paths=[25,38,39,52,54,56,62,64,67], c_inventory=['012.31'],
    kind='drawing or diagram', h=H_RIGHT, hgroup='right_group')
add('right_low', 'Right group: low rounded outline with curved chords', C=['D006'], paths=[25], c_inventory=['012.32'],
    kind='drawing or diagram', h=H_RIGHT, hgroup='right_group', note='C-reader assigns path 67 to the lower outline; A/B assign the same path to extended curves. The original path is preserved with both inventory provenances below.')
add('marked_terminal', 'Large left marked oval: pale last return and hooked endpoint', B=['B008'], dc=True,
    h='[fine terminal unspecified]; '+H_DISKS, hgroup='marked_oval', note='This new geometry is locally linked to original C doubt row 3 by B; it does not create a fourth original C doubt.')
add('pale_left_rim', 'Tall right oval: pale left-rim continuation', ['A012-08'], ['B005'], ['D_N11'], dc=True, h=H_RIGHT, hgroup='right_group')
add('pale_bottom_rim', 'Tall right oval: interrupted pale bottom return', ['A012-09a'], ['B006'], dc=True, h=H_RIGHT, hgroup='right_group',
    note='B006 also supplies the following slanted-rim locus. Its two bottom pieces remain individually referenced as components here. C-reader N12 supplies only its oblique-rim candidate, mapped separately.')
add('pale_slant_rim', 'Tall right oval: pale lower-right sloping return', ['A012-09b'], ['B006'], ['D_N12'], dc=True, h=H_RIGHT, hgroup='right_group')
add('terminal_main', 'Upper descending curve: pale terminal cluster, main stroke', ['A012-10'], ['B007'], ['D_N14'], dc=True, h=H_RIGHT,
    hgroup='right_group', note='Root directs one Boolean C count for the terminal-location cluster; the separate parallel residual has a zero-count component row.')
add('terminal_parallel', 'Upper descending curve: separate parallel residual terminal stroke', ['A012-10'], ['B007'], h=H_RIGHT,
    hgroup='right_group', count_parent='terminal_main', note='A/B draw this second stroke; C-reader supplies one main extension only. No agreement is imputed for the parallel component.')
add('right_vertical_trace', 'Thin pale oblique trace beside lower right vertical line', ['A012-11'], dc=True, h=H_RIGHT, hgroup='right_group')
add('lower_hook', 'Lower blank field: pale hook cluster, main curved stroke', ['A012-12'], ['B020'], ['D_N16'], dc=True, dh=True,
    note='Root directs one Boolean C/H count for this pale-hook-location cluster; separate foot and neighboring oblique components are mapped in zero-count rows.')
add('lower_hook_foot', 'Pale hook cluster: low separate foot stroke', ['A012-12'], count_parent='lower_hook',
    note='A has a separately drawn pale low foot piece. B/C-reader give the shared main hook, with no separately added foot statement.')
add('lower_hook_oblique', 'Pale hook cluster: short neighboring oblique stroke', ['A012-12'], count_parent='lower_hook',
    note='A has a separate short oblique next to the hook turn. B/C-reader return no separate added component here.')
add('apex_tick', 'Detached short upright above small triangle apex', ['A012-13a'], ['B009'], ['D_N05'], dc=True, dh=True)
add('triangle_gray', 'Small detached gray point between triangle and filled point', ['A012-13b'], ['B010'], ['D_N06'], dc=True, dh=True)
add('gap_pale', 'Pale elongated spot above-left of the small gap droplet', B=['B011'], C=['D_N07'], dc=True, dh=True)
add('gap_dark', 'Dark gap droplet and its very short pale upper stem', ['A012-14'], ['B012'], ['D_N08'], dc=True, dh=True)
add('upper_pair_left', 'Top gap: left detached mark and pale upper trace', ['A012-21a'], ['B013'], ['D_N01'], dc=True, dh=True)
add('upper_pair_right', 'Top gap: right detached mark and pale upper trace', ['A012-21b'], ['B014'], ['D_N02'], dc=True, dh=True)
add('upper_margin', 'Far upper-right margin: tiny detached point', ['A012-21c'], C=['D_N03'], dc=True, dh=True)
add('field_780', 'Detached point near (780,396), below upper second oval', ['A012-21d'], C=['D_N04'], dc=True, dh=True)
add('small_oval_point', 'Far-right small oval: gray point by inner lower rim', ['A012-17'], dc=True, h=H_DISKS, hgroup='top_small_right')
add('rule_end_point', 'Dark point under far-right end of upper horizontal rule', ['A012-18'], ['B017'], ['D_N10'], dc=True, h=H_RIGHT, hgroup='right_group')
add('rule_above_point', 'Pale mark just above left portion of right-group upper rule', ['A012-19'], C=['D_N09'], dc=True, h=H_RIGHT,
    hgroup='right_group', note='Text-reported location beside the right-group upper rule supports this proposed H group; final physical attachment remains pending root crop choice.')
add('zigzag_point_A', 'Pale point at A bbox [428,899,433,905]', ['A012-20'], dc=True, dh=True,
    note='A20/B015 physical identity remains pending root crop. The separate source coordinates are not merged by this assembler.')
add('zigzag_point_B', 'Pale point at B bbox [424,898,430,904]', B=['B015'], dc=True, dh=True,
    note='A20/B015 physical identity remains pending root crop. The separate source coordinates are not merged by this assembler.')
add('oval_below_point', 'Detached point immediately below tall right oval', B=['B018'], C=['D_N13'], dc=True, h=H_RIGHT, hgroup='right_group')
add('transverse_point', 'Detached point under lower rising transverse line', B=['B019'], dc=True, h=H_RIGHT, hgroup='right_group')
add('right_edge_dash', 'Independent right-paper-edge dash at fold height', ['A012-22'], ['B016'], ['D_N15'], dc=True, dh=True,
    note='Detached edge mark remains independent of the right-group H count, as directed by root.')
add('lower_dark', 'Isolated dark point near (790,1430)', ['A012-15'], ['B021'], ['D_N17'], dc=True, dh=True)
add('lower_657', 'Lower-field point near (657,1634)', ['A012-23a'], C=['D_N18'], dc=True, dh=True)
add('lower_1077', 'Lower-field point near (1077.5,1465)', ['A012-23b'], dc=True, dh=True)
add('lower_1454', 'Gray point above-left of lower-right dark pair', ['A012-23c'], ['B022'], ['D_N19'], dc=True, dh=True)
add('lower_pair_upper', 'Lower-right pair: upper dark point', ['A012-16a'], ['B023'], ['D_N20'], dc=True, dh=True)
add('lower_pair_lower', 'Lower-right pair: lower-left dark point', ['A012-16b'], ['B024'], ['D_N21'], dc=True, dh=True)
add('lower_185', 'Lower-left point near (185,1796)', ['A012-23d'], C=['D_N22'], dc=True, dh=True)
add('lower_699', 'Lower-field pale oblique near (699,1849)', C=['D_N23'], dc=True, dh=True)
add('lower_1359', 'Lower-right pale point near (1359,1932)', ['A012-23e'], C=['D_N24'], dc=True, dh=True)
add('lower_673', 'Lower-field gray point near (673,2001)', C=['D_N25'], dc=True, dh=True)
add('lower_487', 'Lower-field point near (487,2051)', ['A012-23f'], C=['D_N26'], dc=True, dh=True)
add('lower_upright', 'Lower-right pale upright cluster, upright and central darkening', C=['D_N27'], dc=True, dh=True,
    note='Root directs one Boolean C/H count for this nearby-trace cluster; the separate upper spot is component-mapped with no extra count.')
add('lower_upright_spot', 'Pale upright cluster: detached small upper spot', C=['D_N27'], count_parent='lower_upright')
add('foot_1658', 'Near right foot edge: small dark wedge/tick', ['A012-23h'], ['B025'], ['D_N28'], dc=True, dh=True)
add('foot_1418', 'Near foot, right of centre: tiny dark point', ['A012-23g'], ['B026'], ['D_N29'], dc=True, dh=True)
add('foot_686', 'Near bottom edge: detached point/slant near (686,2334)', ['A012-23i'], C=['D_N30'], dc=True, dh=True)

ids = {s['key']: f'012-D{i:02d}' for i, s in enumerate(specs, 1)}
bykey = {s['key']: s for s in specs}

# Exact local source slices for component rows. All literals below are from
# the text returns; these are provenance references, never image readings.
component_literals = {
 ('terminal_main','A'): ['(1609,912)'], ('terminal_main','B'): ['(1600,905)'],
 ('terminal_parallel','A'): ['(1605.5,912)'], ('terminal_parallel','B'): ['(1605,910.8)'],
 ('pale_bottom_rim','A'): ['(978.5,817.6)'], ('pale_bottom_rim','B'): ['(958,812.6)','(985,817.5)'],
 ('pale_slant_rim','A'): ['(997,810.5)'], ('pale_slant_rim','B'): ['(998,809.5)'],
 ('lower_hook','A'): ['(18,0) .. controls (25,5)'],
 ('lower_hook_foot','A'): ['(2,38) .. controls (7,36)'],
 ('lower_hook_oblique','A'): ['(22,31) -- (29,35)'],
 ('lower_upright','C'): ['(1446.2,2100.0)','(1445.0,2099.7)'],
 ('lower_upright_spot','C'): ['(1447.0,2096.2)'],
}
B_statement_literals = {
 'B009':['(216.4,445.8)'], 'B010':['(272,483.4)'], 'B011':['(443,483.8)'],
 'B012':['(452.8,498.3)','(453.4,501.2)'],
 'B013':['(590,40.5)','(590.8,45)'], 'B014':['(609.3,44)','(609.6,47.2)'],
 'B015':['(426.8,901.1)'], 'B016':['(1656.3,793.6)'],
 'B017':['(1643.2,532.4)'], 'B018':['(1034,823)'], 'B019':['(1231,860.4)'],
}

def candidate_tex_refs(s, r, row_id):
    k = s['key']
    if (k, r) in component_literals:
        return [x for literal in component_literals[k, r] for x in statement_ref(r, literal)]
    if k == 'label':
        return line_ref(r, 'at (1490,71)')
    if k == 'ou':
        return line_ref(r, 'at (196,861)')
    if r == 'A' and row_id.startswith('A012-') and s['diff_C']:
        return comment_block(r, '% '+row_id+':')
    if r == 'B' and row_id in B_statement_literals:
        return [x for literal in B_statement_literals[row_id] for x in statement_ref(r, literal)]
    if r == 'B' and row_id in {'B003','B004','B005','B006','B007','B008','B020','B021'}:
        return comment_block(r, '% '+row_id+(' /' if row_id == 'B003' else ':'))
    if r == 'B' and row_id in {'B022','B023','B024'}:
        return comment_block(r, '% B022--B024:')
    if r == 'B' and row_id in {'B025','B026'}:
        return comment_block(r, '% B025--B026:')
    if r == 'C' and row_id.startswith('D_N'):
        return comment_block(r, '% '+row_id[2:]+':')
    return path_refs(r, s['paths'])

def literal_C(s):
    if s['key'] == 'label':
        return '\\unsure{OK|Ok}', line_ref('A', 'at (1490,71)')[:0] + [exact_ref('packets/012/C.tex', source_tex, '\\node[inner sep=0pt] at (1490,71){\\unsure{OK|Ok}};')]
    if s['key'] == 'ou':
        lit = '\\node[inner sep=0pt,font=\\scriptsize] at (196,861){\\unsure{ou}};'
        return '\\unsure{ou}', [exact_ref('packets/012/C.tex', source_tex, lit)]
    refs = [deepcopy(original_path_refs[n]) for n in s['paths']]
    if s['key'] == 'marked_state':
        return 'overlaid zigzags | possible cancellation of the underlying oval', refs
    if refs:
        return '\n'.join(x['exact_excerpt'] for x in refs), refs
    return '[no added local path in original C]', []

decisions = []
source_row_coverage = {r: [] for r in 'ABC'}
row_targets = {r: defaultdict(list) for r in 'ABC'}
for s in specs:
    key = s['key']
    C_literal, C_refs = literal_C(s)
    rows = {r: [deepcopy(diffs[r][rid]) for rid in s['rows'][r]] for r in 'ABC'}
    box = s['bbox'] or (bbox_from_paths(s['paths']) if s['paths'] else combined_bbox([x.get('bbox') for rr in rows.values() for x in rr]))
    readers = {}
    provenance = {}
    crop_refs = []
    confidence_proposals = {}
    for r in 'ABC':
        direct = rows[r]
        source_refs = [rowref(r, rid) for rid in s['rows'][r]]
        slices = [x for rid in s['rows'][r] for x in candidate_tex_refs(s, r, rid)]
        if direct:
            readers[r] = [x['reading'] for x in direct]
            status = 'literal report candidate; component scope stated separately where relevant'
            confidence_proposals[r] = [x.get('confidence') for x in direct]
        elif s['paths']:
            slices = path_refs(r, s['paths'])
            retained = all(x.get('retained_exactly') for x in slices)
            readers[r] = ('Retains original C path(s) '+','.join(map(str,s['paths']))+' exactly; no separate report candidate for this local row.'
                          if retained else 'Original C path retention requires a text reconciliation; no agreement is imputed.')
            status = 'retained C path; no separate local report candidate'
        else:
            readers[r] = 'No added reading returned at this local locus; no agreement with another reader is imputed.'
            status = 'no added reading returned'
        # Related additions are recorded without attributing their extra
        # components to a reader who supplied only the shared component.
        related = []
        if key == 'terminal_parallel' and r == 'C':
            related = [rowref('C','D_N14')]
            readers[r] = 'D_N14 supplies one main terminal extension; no separate parallel residual is returned.'
        if key in {'lower_hook_foot','lower_hook_oblique'} and r in 'BC':
            rid = 'B020' if r == 'B' else 'D_N16'
            related = [rowref(r,rid)]
            readers[r] = f'{rid} supplies the main pale hook; no separate added {"foot" if key.endswith("foot") else "neighboring oblique"} component is returned.'
        provenance[r] = {'report_rows': source_refs, 'source_status': status,
                         'tex': slices, 'related_report_rows_without_component_candidate': related}
        for rid in s['rows'][r]:
            row_targets[r][rid].append(ids[key])
        for x in direct:
            p = crop_path(r, x.get('readers_crop'))
            if p and p not in crop_refs:
                crop_refs.append(p)
    confs = sorted({c for cs in confidence_proposals.values() for c in cs if c})
    evidence = {r: [{'source': rowref(r, rid), 'evidence': diffs[r][rid].get('evidence'),
                     'qualification': diffs[r][rid].get('qualification')} for rid in s['rows'][r]] for r in 'ABC'}
    hg = s['H_group_key']
    H_count_key = 'right_state' if hg == 'right_group' else ('triangle' if hg == 'triangle_point' else hg)
    decision = {
        'id': ids[key], 'key': key, 'location': s['location'], 'bbox': box,
        'C': C_literal, 'H': s['H'], 'final': None, 'evidence': None, 'confidence': None,
        'kind': s['kind'], 'diff_C': s['diff_C'], 'diff_H': s['diff_H'],
        'marked_in_H': s['marked_in_H'], 'C_doubt_status': None,
        'C_doubt_source_row': s['C_doubt_source_row'], 'root_decided': False,
        'main_approval_pending': True, 'main_counting_decision_pending': True,
        'readers': readers, 'reader_provenance': provenance,
        'reader_rows_exact': rows,
        'reader_original_flags': {r: [{'id': x['id'], 'diff_C': x.get('diff_C'), 'diff_H': x.get('diff_H'),
                                        'kind': x.get('kind'), 'confidence': x.get('confidence'),
                                        'C_doubt_status': x.get('C_doubt_status')} for x in rr] for r, rr in rows.items()},
        'reader_evidence': evidence,
        'supported_confidence_proposals': confidence_proposals,
        'proposed_confidence': confs[0] if len(confs) == 1 else None,
        'confidence_proposal_note': 'Only report-supported confidence levels are proposed. Different levels remain for root choice; no majority vote supplies an ink decision.',
        'candidate_crop_references': crop_refs,
        'source_crop_path': None,
        'witness_C_sources': C_refs,
        'witness_H_sources': [exact_ref('packets/012/H.tex', source_H, H_DRAWING), exact_ref('packets/012/H.tex', source_H, H_NOTE)],
        'role': s['role'], 'H_count_group': f'012-HG-{hg}' if hg else None,
        'H_count_decision': ids.get(H_count_key) if hg else None,
        'H_group_count_row': s['H_group_count_row'],
        'count_locus_key': 'scan012-'+(s['count_parent_key'] or key),
        'count_parent_decision': ids.get(s['count_parent_key']),
        'component_mapping': [], 'assembly_note': s['assembly_note'],
        'pending_fields': ['root final ink reading','root evidence','root confidence','root Boolean difference counts','root source-page attachment'],
        'root_page_source': None,
    }
    decisions.append(decision)

decisions_by_key = {d['key']: d for d in decisions}
for s in specs:
    if s['count_parent_key']:
        decisions_by_key[s['count_parent_key']]['component_mapping'].append({
            'decision_id': ids[s['key']], 'location': s['location'],
            'counted_at_parent': True, 'local_component_retained': True})
    for (key, r), literals in component_literals.items():
        if key == s['key']:
            decisions_by_key[key]['component_mapping'].extend([
                {'reader': r, 'source': rr, 'scope': 'one separately supplied path statement'}
                for literal in literals for rr in statement_ref(r,literal)])

# Add explicit unchanged audits for labels and archival apparatus.
label_lines = [l for l in source_tex.splitlines() if l.startswith('\\node')]
labels_audit = {
    'id': '012-AUD-LABELS', 'location': 'Eight short labels',
    'source_report_rows': [rowref('C','D005')],
    'C_exact': label_lines,
    'H_exact': 'quatre disques sont marqués « OK » (ou « ok »)',
    'source_H': exact_ref('packets/012/H.tex',source_H,H_NOTE),
    'reader_tex': {r: [exact_ref(TEX_PATHS[r],texts[r],l) for l in label_lines] for r in 'ABC'},
    'decision_ids': [ids['label'],ids['ou']],
    'note': 'Four OK loci and four ou loci are source-attributed to C-reader D005; the H rereading note supersedes the initial three-label description. Local doubts remain separate.',
    'root_decided': False,
}
archive_audit = {
    'id': '012-AUD-ARCHIVE', 'location': 'Bottom-left archive numeral',
    'source_report_rows': [rowref('C','D008')],
    'literal': '% archive sheet number: 11',
    'reader_tex': {r: line_ref(r,'% archive sheet number: 11') for r in 'ABC'},
    'note': 'Comment-only apparatus; no C/H manuscript reading difference counted.', 'root_decided': False,
}
audits = [labels_audit, archive_audit]
row_targets['C']['D005'].extend(['012-AUD-LABELS',ids['label'],ids['ou']])
row_targets['C']['D008'].append('012-AUD-ARCHIVE')

for r in 'ABC':
    for i, x in enumerate(reports[r]['differences']):
        target = list(dict.fromkeys(row_targets[r][x['id']]))
        source_row_coverage[r].append({
            'source': rowref(r,x['id']), 'decision_or_audit_ids': target,
            'reported_diff_C': x.get('diff_C'), 'reported_diff_H': x.get('diff_H'),
            'reported_C_doubt_status': x.get('C_doubt_status'), 'reported_kind': x.get('kind'),
            'mapped': bool(target),
        })

# Reader doubt entries are preserved verbatim and mapped through their actual
# source identities.  A's low confidence for role/hand is kept distinct from
# the same reader's higher confidence in an observed shape.
doubt_targets = {r: {} for r in 'ABC'}
source_doubt_coverage = {r: [] for r in 'ABC'}
for r in 'ABC':
    for i,x in enumerate(reports[r]['doubts']):
        if r == 'A':
            rid = x.get('id','').removeprefix('D-')
        elif r == 'B':
            rid = x.get('difference_id')
        else:
            local = x.get('local_id')
            rid = {'C.DR1.K':'D001','C.DR2.word':'D002','C.DR3.state':'D003b','right_group.state':'D004'}.get(local)
            if rid is None and local and re.fullmatch(r'N\d\d',local):
                rid = 'D_'+local
        targets = list(dict.fromkeys(row_targets[r].get(rid,[])))
        doubt_targets[r][i] = targets
        source_doubt_coverage[r].append({
            'source': ref(REPORT_PATHS[r],f'/doubts/{i}'), 'source_exact': deepcopy(x),
            'location_exact': x.get('location'), 'reading_exact': x.get('reading'),
            'alternatives_exact': x.get('alternatives'), 'decision_ids': targets, 'mapped': bool(targets)})

doubts = []
for d in decisions:
    entries = []
    for r in 'ABC':
        for i, targets in doubt_targets[r].items():
            if d['id'] in targets:
                entries.append({'reader':r,'source':ref(REPORT_PATHS[r],f'/doubts/{i}'),
                                'source_exact':deepcopy(reports[r]['doubts'][i])})
    if entries:
        doubts.append({
            'reading': None, 'alternatives': None, 'reason': None, 'confidence': None,
            'location': d['location'], 'decision_id': d['id'],
            'status': 'pending root ink choice; exact reader candidates retained below',
            'source_doubt_candidates': entries,
            'count_locus_key': d['count_locus_key'],
            'count_parent_decision': d['count_parent_decision'],
            'root_decided': False, 'main_approval_pending': True,
            'source_C_row': d['C_doubt_source_row'],
        })

source_doubt_text = (BASE/'packets/012/C_doubts.txt').read_text()
section = source_doubt_text.split('## Doubtful readings',1)[1].split('## Abbreviations',1)[0]
original_doubt_rows = [l for l in section.splitlines() if l.startswith('| 12 |')]
actual_C_doubt_map = []
source_map_keys = {'A':'source_C_doubt_rows','B':'C_doubt_source_map','C':'source_doubt_map'}
physical_doubt_subloci = {
 1: [('initial closed O', 'label'), ('second branching K/k', 'label')],
 2: [('initial small loop', 'ou'), ('compressed following run', 'ou')],
 3: [('underlying oval and chord network','marked_oval'), ('inner hatching','marked_oval'),
     ('outer zigzags and return loops','marked_oval'), ('editorial cancellation function','marked_state'),
     ('pale terminal extension reported by B','marked_terminal'), ('lower connection into miniature','lower_mini_right')],
}
for n, row in enumerate(original_doubt_rows,1):
    reader_maps = {r:{'source':ref(REPORT_PATHS[r],f'/{source_map_keys[r]}/{n-1}'),
                     'source_exact':deepcopy(reports[r][source_map_keys[r]][n-1])} for r in 'ABC'}
    local = [{'local_identity': name, 'decision_id':ids[k], 'status':None,
              'root_decided':False, 'classification':'new geometric refinement linked by B to row 3' if k=='marked_terminal' else 'source-doubt physical sublocus'}
             for name,k in physical_doubt_subloci[n]]
    actual_C_doubt_map.append({
        'source_row':n, 'source_id':f'C012-Doubtful-readings-{n:02d}',
        'source_row_exact':row, 'source':exact_ref('packets/012/C_doubts.txt',source_doubt_text,row),
        'reader_source_identities_and_subloci_exact':reader_maps,
        'decision_ids':list(dict.fromkeys(x['decision_id'] for x in local)),
        'local_subloci':local, 'source_row_final_status':None, 'proposed_status':'retained',
        'main_approval_pending':True,
        'status_basis':'All final reader source maps retain this original source row; root disposition pending.',
    })

# Physical H groups preserve the broad C-reader D006 row by explicit local
# mapping, and never add its aggregate source flag as another counted row.
H_collation_groups = []
for s in specs:
    if not s['H_group_count_row']:
        continue
    hg = s['H_group_key']
    children = [ids[t['key']] for t in specs if t['H_group_key']==hg]
    H_collation_groups.append({
        'id':f'012-HG-{hg}', 'location':s['location'], 'count_decision':ids[s['key']],
        'child_decisions':children, 'H_literal':s['H'],
        'source_H_drawing':exact_ref('packets/012/H.tex',source_H,H_DRAWING),
        'source_H_rereading_note':exact_ref('packets/012/H.tex',source_H,H_NOTE),
        'main_classification_pending':True,
        'policy':'Only the Boolean diff_H on the physical count row is proposed true; local graphical refinements cross-reference this row. Root may revise the proposal after crop inspection.'})

# Inventory union by physical element.  Original combined inventory rows are
# explicitly split when a reader inventories a separate physical component.
base_inventory_keys = {
 '012.01':['top_first'],'012.02':['label_top_ou'],'012.03':['top_small_first'],'012.04':['label_second_OK'],
 '012.05':['top_second'],'012.06':['label_third_OK'],'012.07':['top_third'],'012.08':['label'],
 '012.09':['top_fourth'],'012.10':['label_right_ou'],'012.11':['top_small_right'],
 '012.12':['triangle','filled_dot'],'012.13':['upper_loop'],'012.14':['tripod'],'012.15':['square'],
 '012.16':['stem_triangle'],'012.17':['left_wedges'],'012.18':['marked_oval'],'012.19':['label_lower_OK'],
 '012.20':['opening_arc','closing_arc','left_dash'],'012.21':['label_parenthesis_ou'],
 '012.22':['lower_mini_left'],'012.23':['ou'],'012.24':['lower_mini_right'],'012.25':['central_oval'],
 '012.26':['lower_quadrilateral'],'012.27':['lower_zigzag'],'012.28':['spoked_triangle'],
 '012.29':['right_rules'],'012.30':['right_tall'],'012.31':['right_curves'],'012.32':['right_low'],
}
label_descriptions = {
 'label_top_ou':('ou above first upper oval','ou'), 'label_second_OK':('OK above second upper oval','OK'),
 'label_third_OK':('OK above third upper oval','OK'), 'label_right_ou':('ou beside fourth upper oval','ou'),
 'label_lower_OK':('OK beside large marked oval','OK'), 'label_parenthesis_ou':('ou by opening parenthesis','ou'),
}
inv_entries = {}
inv_source_targets = {r:defaultdict(list) for r in ['witness_C','A','B','C']}

def inv_parent(key):
    return bykey[key]['count_parent_key'] or key if key in bykey else key

def ensure_inv(key):
    key = inv_parent(key)
    if key not in inv_entries:
        if key in bykey:
            s = bykey[key]
            first = s['location']
            kind = 'text' if key in {'label','ou'} else 'drawing'
            decision_ids = [ids[key]] + [ids[t['key']] for t in specs if t['count_parent_key']==key]
        elif key == 'archive':
            first='archive numeral 11, comment only'; kind='text'; decision_ids=[]
        else:
            first=label_descriptions[key][0]; kind='text'; decision_ids=[]
        inv_entries[key] = {
            'sheet_kind':'text','hand':None,'element':None,'kind':kind,'position':first,
            'first_words_or_objects':first,'transcribed':'pending root source attachment',
            'source_inventory':{r:[] for r in ['witness_C','A','B','C']},
            'decision_ids':decision_ids,'main_approval_pending':True,'root_page_sources':[],
            'transcribed_basis':'Source transcribed flags are preserved per reader; no root page is attached by this draft.',
            'source_hand_candidates':[],'component_decisions':decision_ids,
        }
    return key

def attach_inventory(r,i,x,keys):
    for key in dict.fromkeys(inv_parent(k) for k in keys):
        key=ensure_inv(key)
        path='packets/012/C_inventory.json' if r=='witness_C' else REPORT_PATHS[r]
        pointer=f'/{i}' if r=='witness_C' else f'/inventory/{i}'
        inv_entries[key]['source_inventory'][r].append({
            'source':ref(path,pointer),'source_element':x.get('element'),
            'source_hand':x.get('hand'),'source_transcribed':x.get('transcribed'),
            'source_exact':deepcopy(x),
            'physical_component_scope':key})
        hand=x.get('hand')
        if hand and hand not in inv_entries[key]['source_hand_candidates']:
            inv_entries[key]['source_hand_candidates'].append(hand)
        inv_source_targets[r][i].append(key)

for i,x in enumerate(source_inventory):
    attach_inventory('witness_C',i,x,base_inventory_keys[x['element']])
for r in 'ABC':
    for i,x in enumerate(reports[r]['inventory']):
        original = x.get('C_inventory_element') or x.get('source_inventory_element')
        if r=='B' and x.get('element') in base_inventory_keys:
            original=x['element']
        keys=[]
        if original:
            keys=base_inventory_keys[original]
        elif 'archive' in str(x).lower():
            keys=['archive']
        elif r=='C' and x.get('element')=='012.C.33':
            keys=['filled_dot']
        elif r=='C' and x.get('element')=='012.C.34':
            keys=['left_dash']
        elif r=='C' and x.get('element')=='012.C.36':
            keys=['marked_oval']
        elif r=='C' and x.get('element')=='012.C.37':
            keys=['right_rules','right_tall','right_curves','right_low']
        else:
            rid=x.get('difference_id')
            if r=='C' and x.get('element','').startswith('012.C.N'):
                rid='D_'+x['element'].split('.')[-1]
            target_ids=row_targets[r].get(rid,[])
            keys=[s['key'] for s in specs if ids[s['key']] in target_ids]
        attach_inventory(r,i,x,keys)

inventory=list(inv_entries.values())
inventory_ids={}
for i,(key,item) in enumerate(inv_entries.items(),1):
    item['element']=f'012.I{i:02d}'
    item['physical_key']=key
    inventory_ids[key]=item['element']
    item['root_hand_decision_pending']=True
inventory_coverage={}
for r in ['witness_C','A','B','C']:
    rows=source_inventory if r=='witness_C' else reports[r]['inventory']
    inventory_coverage[r]=[{
        'source':ref('packets/012/C_inventory.json' if r=='witness_C' else REPORT_PATHS[r],f'/{i}' if r=='witness_C' else f'/inventory/{i}'),
        'source_element':x.get('element'),
        'merged_elements':[inventory_ids[k] for k in dict.fromkeys(inv_source_targets[r][i])],
        'physical_keys':list(dict.fromkeys(inv_source_targets[r][i])),
        'mapped':bool(inv_source_targets[r][i]),
    } for i,x in enumerate(rows)]

# The explicit source path map also keeps inventory attribution differences
# (notably path 67) without changing the path or inventing agreement.
path_map=[]
for n in range(1,69):
    targets=[ids[s['key']] for s in specs if n in s['paths']]
    source_entries={}
    for r in 'BC':
        items=reports[r].get('source_path_audit',[])
        source_entries[r]=[{'source':ref(REPORT_PATHS[r],f'/source_path_audit/{i}'),'source_exact':deepcopy(x)}
                           for i,x in enumerate(items) if x.get('path',x.get('source_path',x.get('path_number')))==n]
    path_map.append({'source_C_path':n,'source_C':original_path_refs[n],
                     'decision_ids':targets,'reader_tex':{r:path_refs(r,[n])[0] for r in 'ABC'},
                     'reader_path_audit':source_entries,'root_attachment_pending':True})

abbreviations=[{
    'form':'OK','expansion':'okay','status':'possible expansion; manuscript form preserved',
    'source_C':exact_ref('packets/012/C_doubts.txt',source_doubt_text,'| 12 | OK | okay |'),
    'reader_sources':{r:[{'source':ref(REPORT_PATHS[r],f'/abbreviations/{i}'),'source_exact':deepcopy(x)}
                         for i,x in enumerate(reports[r].get('abbreviations',[]))] for r in 'ABC'},
    'root_decided':False,
}]

unmapped={
 'differences':{r:[x for x in source_row_coverage[r] if not x['mapped']] for r in 'ABC'},
 'doubts':{r:[x for x in source_doubt_coverage[r] if not x['mapped']] for r in 'ABC'},
 'inventory':{r:[x for x in inventory_coverage[r] if not x['mapped']] for r in ['witness_C','A','B','C']},
}
all_mapped=all(not rows for group in unmapped.values() for rows in group.values())
source_files=list(REPORT_PATHS.values())+list(TEX_PATHS.values())+[
    'packets/012/C.tex','packets/012/H.tex','packets/012/C_doubts.txt','packets/012/C_inventory.json','packets/012/metadata.json']
fingerprints={p:hashlib.sha256((BASE/p).read_bytes()).hexdigest() for p in source_files}

record={
 'scan':12,'folder':metadata['folder'],'their_page':metadata['their_page'],'hua_has':metadata['hua_has'],
 'filename':'J81-02_81_scan012.tex','brief_version':None,
 'main_adjudicated':False,'main_approved_utc':None,
 'draft_status':'Text-only candidate mapping. Root ink, evidence, confidence, H group counts and final-page attachment remain pending.',
 'decisions':decisions,'doubts':doubts,'inventory':inventory,
 'notes':'All source report candidates, original flags and source doubts remain attributed to their readers. The H rereading note supersedes three OK with four and limits the arrowhead assertion; its whole-right-group cancellation claim is retained as a witness reading. The subsequent section and note belong to feuillet13 and are excluded. No mathematical check was performed by this assembler.',
 'abbreviations':abbreviations,'check_events':[],
 'reader_check_events':{r:deepcopy(reports[r].get('check_events',[])) for r in 'ABC'},
 'check_events_note':'Reader event lists are empty. No event is generated by text assembly.',
 'workflow_note':'Text-only mechanical assembly; no image inspection, cropping, OCR, web lookup, TeX compilation/rendering, or mathematical check. All final decisions remain for root.',
 'source_reports':REPORT_PATHS,'source_readings':TEX_PATHS,
 'source_audits':{r:{k:deepcopy(v) for k,v in reports[r].items() if k in ['notes','notation','brief_feedback','source_C_doubt_rows','C_doubt_source_map','source_doubt_map','structural_validation','workflow']} for r in 'ABC'},
 'source_fingerprints':fingerprints,
 'reader_completion':{r:{k:reports[r].get(k) for k in ['reader','start_utc','end_utc','full_image_viewed','halves_viewed','complete_visual_read']} for r in 'ABC'},
 'root_adjudication_log':None,'root_page_source':None,'root_messages_exact':[],
 'actual_C_doubt_map':actual_C_doubt_map,
 'C_doubt_source_classification':{
     'actual_source_rows':3,
     'source_heading':'Doubtful readings',
     'row3_already_present_in_table':True,
     'row3_C_tex_local_wrapper_absent':True,
     'right_group_is_added_C_qualification':True,
     'right_group_decision_id':ids['right_state'],
     'new_geometric_terminal_linked_to_row3_is_not_new_original_doubt':ids['marked_terminal'],
 },
 'H_collation_groups':H_collation_groups,
 'source_row_coverage':source_row_coverage,'source_doubt_coverage':source_doubt_coverage,
 'inventory_coverage':inventory_coverage,'source_path_map':path_map,'unchanged_audit':audits,
 'excluded_source_conventions':[
     {'source':exact_ref('packets/012/H.tex',source_H,H_EXCLUDED),'text_exact':H_EXCLUDED,
      'reason':'H assigns the tail section and note to feuillet13; excluded apparatus for scan012.'},
     {'source':'archive numeral 11','representation':'% archive sheet number: 11','reason':'Archival apparatus retained as a comment.'}],
 'counting_policy':'Draft counts use only Boolean diff_C/diff_H proposals; original source flags are separately preserved. One H row per proposed whole physical sketch/group. Local C refinements share the relevant H row. Terminal pair, pale-hook cluster and lower-upright cluster each have one count row with zero-count components. A20/B015 identity remains pending and is not merged. All proposal counts await root decisions.',
 'counts':None,
 'proposed_counts':{
     'decision_candidates':len(decisions),'actual_C_doubt_source_rows':len(actual_C_doubt_map),
     'source_difference_rows':{r:len(reports[r]['differences']) for r in 'ABC'},
     'source_doubt_rows':{r:len(reports[r]['doubts']) for r in 'ABC'},
     'source_inventory_rows':{r:len(reports[r]['inventory']) for r in 'ABC'},
     'witness_C_inventory_rows':len(source_inventory),'inventory_union_candidates':len(inventory),
     'C_difference_loci':sum(d['diff_C'] is True for d in decisions),
     'H_difference_loci':sum(d['diff_H'] is True for d in decisions),
     'H_physical_groups':len(H_collation_groups),'check_events':0,
     'status':'mechanical proposal only; root approval pending'},
 'assembly_timestamp_utc':datetime.now(timezone.utc).isoformat(),
 'assembly_revision':'All available reader text rows mapped; no ink decisions selected.',
 'coverage_status':{'all_source_rows_mapped':all_mapped,'unmapped':unmapped,
                    'reader_C_final_timestamp_present':bool(reports['C'].get('end_utc')),
                    'root_completion_confirmation_pending':True,
                    'root_ink_choice_pending':True,'root_inventory_attachment_pending':True},
 'attention_items':[
     {'decision_ids':[ids['zigzag_point_A'],ids['zigzag_point_B']],
      'issue':'A20/B015 may refer to one pale point or two neighboring points. Text bboxes and coordinates differ; root crop identity decision required.'},
     {'decision_ids':[ids['right_state']],
      'issue':'A/C-reader report diff_C=false for a newly added state qualification; proposed Boolean C=true follows root instruction, while source flags remain exact.'},
     {'decision_ids':[ids['rule_above_point']],
      'issue':'Proposed right-group H attachment by reported location; final physical grouping remains for root.'},
     {'decision_ids':[ids['right_curves'],ids['right_low']],
      'issue':'C-reader assigns path 67 to lower outline; A/B assign it to extended curves. All exact source inventory references are preserved.'},
 ],
}

if not all_mapped:
    raise RuntimeError('Unmapped source rows remain: '+json.dumps(unmapped,ensure_ascii=False))

(OUT/'scan012_record_draft.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')

def md(v):
    return str(v).replace('|','\\|').replace('\n',' / ')
lines=[
 '# scan012 — text-only candidate mapping', '',
 'This is a mechanical draft. `main_adjudicated=false`. Final reading, root evidence, confidence, page attachment and approved counts remain pending.', '',
 '## Coverage', '',
 '| Source | Difference rows | Doubt entries | Inventory rows |',
 '|---|---:|---:|---:|',
 *[f"| {r} | {len(reports[r]['differences'])} | {len(reports[r]['doubts'])} | {len(reports[r]['inventory'])} |" for r in 'ABC'], '',
 f"All source rows are mapped. The {len(source_inventory)} original C inventory rows map into {len(inventory)} physical inventory candidates, including explicit triangle/point and parenthesis/dash components. Reader C final timestamp: {reports['C'].get('end_utc')!r}.", '',
 '## Candidate loci', '',
 'The C/H columns are Boolean proposals only. Source flags remain unchanged in `reader_original_flags` and source coverage. The JSON carries all literal candidates, evidence, excerpts and source pointers.', '',
 '| ID | Physical locus | A rows | B rows | C-reader rows | Proposed C/H | H count row / cluster parent |',
 '|---|---|---|---|---|---|---|',
]
for s,d in zip(specs,decisions):
    grouping=d['count_parent_decision'] or d['H_count_decision'] or 'independent'
    lines.append(f"| {d['id']} | {md(d['location'])} | {','.join(s['rows']['A']) or 'no separate candidate'} | {','.join(s['rows']['B']) or 'no separate candidate'} | {','.join(s['rows']['C']) or 'no separate candidate'} | {d['diff_C']}/{d['diff_H']} | {grouping} |")
lines += ['', '## Original C doubt identities', '',
          'The original doubtful-reading table has three rows. Its third row already records possible cancellation of the marked left oval. The right-group state qualification is a separate added C qualification.', '',
          '| Source row | Source identity | Candidate decisions | Local subloci |', '|---|---|---|---|']
for x in actual_C_doubt_map:
    lines.append(f"| {x['source_row']} | {x['source_id']} | {', '.join(x['decision_ids'])} | {md('; '.join(y['local_identity'] for y in x['local_subloci']))} |")
lines += ['', 'Every A/B/C source-map sublocus is also copied verbatim with its original identity and JSON pointer. The B terminal refinement remains locally linked to row 3 without becoming another original doubt row.', '',
          '## H physical-object groups', '',
          'B027 has six top-sketch rows. B031 has one central-oval row. The two lower-left large ovals each have a row. Each principal lower graph has explicit coverage. The miniature parenthetical pair and right-hand group each have one proposed H count row with local component references.', '',
          '| Group | Count row | Local decisions |', '|---|---|---|']
for x in H_collation_groups:
    lines.append(f"| {x['id']} | {x['count_decision']} | {', '.join(x['child_decisions'])} |")
lines += ['', '## Root attention', '',
          *[f"- {', '.join(x['decision_ids'])}: {x['issue']}" for x in record['attention_items']], '',
          '- Terminal strokes share one count at '+ids['terminal_main']+'; the parallel residual is mapped at '+ids['terminal_parallel']+'.',
          '- Pale-hook components share one count at '+ids['lower_hook']+'; foot and neighboring oblique remain mapped at '+ids['lower_hook_foot']+' and '+ids['lower_hook_oblique']+'.',
          '- Lower upright and detached upper spot share one count at '+ids['lower_upright']+'; the upper spot is component-mapped at '+ids['lower_upright_spot']+'.',
          '- No final count or approval is asserted. The final H section and its feuillet13 note are excluded; H’s rereading note controls the four-OK statement.', '',
          '## Inventory coverage', '',
          '| Union element | Physical element | Source inventory identities |', '|---|---|---|']
for x in inventory:
    sources=[]
    for r,rr in x['source_inventory'].items():
        if rr:
            sources.append(r+': '+', '.join(z['source_element'] for z in rr))
    lines.append(f"| {x['element']} | {md(x['position'])} | {md('; '.join(sources))} |")
lines += ['', 'No image, OCR, web, compiler, renderer or mathematical check was used for this assembly. All reader mathematical-event lists are empty.', '']
(OUT/'scan012_mapping.md').write_text('\n'.join(lines))
print(json.dumps({'draft':'out/checks/scan012_record_draft.json','mapping':'out/checks/scan012_mapping.md',
                  'decision_candidates':len(decisions),'inventory_candidates':len(inventory),
                  'all_source_rows_mapped':all_mapped,'C_reader_end_utc':reports['C'].get('end_utc'),
                  'main_adjudicated':False},ensure_ascii=False))
