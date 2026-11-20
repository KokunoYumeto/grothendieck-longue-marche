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
ROOT_LOG_PATH = 'out/checks/scan012_main_decisions.md'
root_log_text = (BASE/ROOT_LOG_PATH).read_text() if (BASE/ROOT_LOG_PATH).exists() else ''
TEX_MAPPING_PATH='out/checks/scan012_tex_mapping.json'
tex_mapping=json.loads((BASE/TEX_MAPPING_PATH).read_text()) if (BASE/TEX_MAPPING_PATH).exists() else None
root_sections = {}
root_section_refs = {}
root_starts = list(re.finditer(r'^(\d+)\. ',root_log_text,re.M))
for i,m in enumerate(root_starts):
    stop = root_starts[i+1].start() if i+1<len(root_starts) else len(root_log_text)
    number = int(m.group(1))
    root_sections[number] = root_log_text[m.start():stop].strip()
    root_section_refs[number] = {'path':ROOT_LOG_PATH,'pointer':f'numbered-entry-{number}',
                                'line_start':root_log_text.count('\n',0,m.start())+1,
                                'line_end':root_log_text.count('\n',0,stop)+1,
                                'exact_excerpt':root_sections[number]}
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
    hgroup='marked_oval', doubt_source=3, bbox=[154,562,390,831],
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
    bbox=[154,562,390,831],
    note='Local state, underlying oval, inner hatching, outer loops, terminal extension and connection are cross-referenced; no extra H count for those local rows. The proposed box is the union of reported large-oval boxes; the shared source path also includes the lower miniature.')
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
    kind='drawing or diagram', h='[not separately located]; '+H_VARIANTS, hgroup='parenthetical',
    note='The source path crosses the large-oval and lower-miniature loci. Its box is the full shared path extent, not a fabricated miniature-only bound. The local connection and miniature remain separately identified by the source-map subloci.')
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
add('lower_1352', 'Lower-right distinct gray spot below-left of N24', C=['D_N31'], dc=True, dh=True,
    note='C-reader final added-trace N31 is a separate physical spot; it remains individually mapped.')
add('lower_1359_upper', 'N24 compact-spot cluster: detached smaller upper spot', C=['D_N24'], count_parent='lower_1359',
    note='C-reader final source adds this separate upper component. A returns the main compact point only. One cluster count is proposed pending root physical grouping.')
if 3 in root_sections and 'full(1278,77)' in root_sections[3]:
    add('root_upper_1278','Root-only compact gray triangular/rounded fleck near (1278,77)',dc=True,dh=True,
        note='Root crop-log entry 3 supplies this new locus. Approximate center only; no unreported bounding box or character is invented.')
    add('root_upper_1297','Root-only smaller gray upright fleck near (1297,94)',dc=True,dh=True,
        note='Root crop-log entry 3 supplies this distinct new locus. Approximate center only; no unreported bounding box or character is invented.')
root_additions = [
    ('R1','root_upper_1278',3,[1278,77],'Compact gray triangular/rounded fleck near (1278,77)','medium','05_top_fourth_oval',None),
    ('R2','root_upper_1297',3,[1297,94],'Smaller gray upright fleck near (1297,94)','medium','05_top_fourth_oval',None),
    ('R3','root_first_418',4,[418,204],'Detached gray point inside first upper oval near (418,204)','medium','01_top_first_oval','top_first'),
    ('R4','root_first_343',4,[343,252],'Detached gray point inside first upper oval near (343,252)','medium','01_top_first_oval','top_first'),
    ('R5','root_cap_335',4,[335,362],'Faint compact point within first oval lower cap near (335,362)','low','01_top_first_oval','top_first'),
    ('R6','root_second_605',5,[605,148],'Faint isolated gray point left of second oval upper-left side near (605,148)','medium','03_top_second_oval',None),
    ('R7','root_mini_1586',8,[1586.5,288.5],'Compact pale gray horizontal fleck outside top-right miniature upper-left rim near (1586.5,288.5)','medium','06_top_right_miniature',None),
    ('R8','root_central_684',9,[684,749],'Small diffuse gray point within central lower oval lower-right interior near (684,749)','low','08_central_lower_oval','central_oval'),
    ('R9','root_quad_174',13,[174,941],'Existing C path68 component near (174,941), confirmed without a new path','medium','12_lower_diagonal_quadrilateral','lower_quadrilateral'),
    ('R10','root_quad_231',13,[231,996],'Small gray point below quadrilateral lower side near (231,996)','medium','12_lower_diagonal_quadrilateral','lower_quadrilateral'),
    ('R11','root_below_673',29,[672.6,2007.4],'Small pale upright gray patch immediately below N25; ellipse radii (0.65,1.0), black!20','low','C/17_lower_central_point',None),
]
for rid,key,section,center,reading,confidence,crop,hg in root_additions:
    if section in root_sections and not any(s['key']==key for s in specs):
        add(key,reading,dc=True,dh=hg is None,hgroup=hg,
            h=H_DISKS if hg else '[omitted]',
            note=f'Root-only {rid}, explicitly recorded in crop-log entry {section}. Approximate reported center; final graphical source is root\'s work.')

if 16 in root_sections:
    for s in specs:
        if s['key']=='zigzag_point_A':
            s['rows']['B']=['B015']
            s['assembly_note']='Root entry 16 identifies A20 and B015 as one bounded patch; D54 carries the one C/H count and D55 retains its source cross-reference.'
        if s['key']=='zigzag_point_B':
            s['diff_C']=False; s['diff_H']=False
            s['count_parent_key']='zigzag_point_A'
            s['assembly_note']='Root entry 16 explicitly identifies this as the same patch counted at D54. Original B015 candidate and flags remain preserved; no duplicate point is added.'
        if s['key']=='root_quad_174' and 'R9 is a confirmation with no C change' in root_sections[16]:
            s['diff_C']=False; s['diff_H']=False; s['kind']='other'
            s['paths']=[68]
            s['inventory_parent_key']='lower_quadrilateral'
            s['role']='existing C path component confirmation'
            s['assembly_note']='Root source-coordinate follow-up confirms R9 is already in path68. No added path, no C/H count and no duplicated physical inventory element.'
if 17 in root_sections:
    for s in specs:
        if s['key'] in {'apex_tick','triangle_gray'}:
            s['diff_H']=False
            s['H_group_key']='triangle_point'
            s['H']='un\ntriangle, un point'
            s['assembly_note']='Root entry17 explicitly assigns this small C addition to the triangle-plus-large-point H physical group.'
if 29 in root_sections:
    for s in specs:
        if s['key']=='root_below_673':
            s['diff_C']=False; s['diff_H']=False
            s['count_parent_key']='lower_673'
            s['assembly_note']='Root R11 is a low-confidence local child of the N25 physical cluster; its own doubt marker and exact supplied ellipse geometry are preserved with zero added C/H count.'

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
 ('lower_1359','C'): ['(1358.7,1928.1)'],
 ('lower_1359_upper','C'): ['(1359.5,1923.9)'],
}
B_statement_literals = {
 'B009':['(216.4,445.8)'], 'B010':['(272,483.4)'], 'B011':['(443,483.8)'],
 'B012':['(452.8,498.3)','(453.4,501.2)'],
 'B013':['(590,40.5)','(590.8,45)'], 'B014':['(609.3,44)','(609.6,47.2)'],
 'B015':['(426.8,901.1)'], 'B016':['(1656.3,793.6)'],
 'B017':['(1643.2,532.4)'], 'B018':['(1034,823)'], 'B019':['(1231,860.4)'],
 'B021':['(789.3,1430.5)'],'B022':['(1454.5,1661)'],'B023':['(1529,1705.8)'],
 'B024':['(1524.1,1712.8)'],'B025':['(1656,2190.8)'],'B026':['(1418,2290)'],
}

def candidate_tex_refs(s, r, row_id):
    k = s['key']
    if (k, r) in component_literals:
        return [x for literal in component_literals[k, r] for x in statement_ref(r, literal)]
    if k == 'label':
        return line_ref(r, 'at (1490,71)')
    if k == 'ou':
        return line_ref(r, 'at (196,861)')
    if k in {'marked_state','right_state'}:
        if r == 'B':
            return comment_block(r, '% '+row_id+(' /' if row_id == 'B003' else ':')) + path_refs(r,s['paths'])
        coordinate = 'at (156.5,564)' if k == 'marked_state' else 'at (809.5,348.6)'
        return line_ref(r, coordinate) + path_refs(r,s['paths'])
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
        if key == 'pale_bottom_rim' and r == 'C':
            related = [rowref('C','D_N12')]
            readers[r] = 'D_N12 supplies the neighboring lower-right oblique; no separately added bottom-return path is returned. Its exact candidate is mapped at D36.'
        if key in {'lower_hook_foot','lower_hook_oblique'} and r in 'BC':
            rid = 'B020' if r == 'B' else 'D_N16'
            related = [rowref(r,rid)]
            readers[r] = f'{rid} supplies the main pale hook; no separate added {"foot" if key.endswith("foot") else "neighboring oblique"} component is returned.'
        if key == 'lower_1359_upper' and r == 'A':
            related = [rowref('A','A012-23e')]
            readers[r] = 'A012-23e supplies the main compact point near (1359,1932); no separate upper-spot component is returned.'
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
        'reader_bboxes_exact': {r:[{'source':rowref(r,rid),'bbox':diffs[r][rid].get('bbox')} for rid in s['rows'][r]] for r in 'ABC'},
        'source_path_bboxes_exact': [{'source_C_path':n,'bbox':original_path_refs[n]['bbox']} for n in s['paths']],
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
        'source_crop_path': None, 'crop': None,
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
for s in specs:
    if s['paths']:
        continue
    d=decisions_by_key[s['key']]
    seen={(x.get('reader'),x.get('source',{}).get('path'),x.get('source',{}).get('line_start'),x.get('source',{}).get('exact_excerpt'))
          for x in d['component_mapping'] if 'source' in x}
    for r,pr in d['reader_provenance'].items():
        full=texts[r]
        offsets=[0]
        for line in full.splitlines(keepends=True):
            offsets.append(offsets[-1]+len(line))
        for rr in pr['tex']:
            excerpt=rr.get('exact_excerpt','')
            for m in re.finditer(r'\\(?:draw|path|fill)(?=\[|\s)',excerpt):
                end=excerpt.find(';',m.start())
                if end<0:
                    continue
                base=offsets[rr['line_start']-1]
                part=source_range(TEX_PATHS[r],full,base+m.start(),base+end+1)
                ident=(r,part['path'],part['line_start'],part['exact_excerpt'])
                if ident not in seen:
                    seen.add(ident)
                    d['component_mapping'].append({'reader':r,'source':part,
                        'scope':'one graphical statement; enclosing source excerpt preserves any local coordinate frame',
                        'component_confidence':'source-attributed; no independent root confidence supplied here'})

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
        H_targets = list(dict.fromkeys(d['H_count_decision'] for d in decisions
                                     if d['id'] in target and d['H_count_decision']))
        source_row_coverage[r].append({
            'source': rowref(r,x['id']), 'decision_or_audit_ids': target,
            'H_group_count_decisions':H_targets,
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
 '012.20':['opening_arc','closing_arc'],'012.21':['label_parenthesis_ou'],
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
    return bykey[key].get('inventory_parent_key') or bykey[key]['count_parent_key'] or key if key in bykey else key

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
            if r=='C' and original=='012.12':
                keys=['triangle']
            if r=='A' and original=='012.20':
                keys=['opening_arc','closing_arc','left_dash']
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

for rid,key,section,center,reading,confidence,crop,hg in root_additions:
    if key in bykey:
        ik=ensure_inv(key)
        if key=='root_quad_174' and ik=='lower_quadrilateral':
            inv_entries[ik].setdefault('root_component_confirmations',[]).append({
                'root_addition_id':rid,'decision_id':ids[key],'reported_center':center,
                'source':deepcopy(root_section_refs[section]),
                'followup':deepcopy(root_section_refs[16]),
                'status':'existing path68 component; no new inventory element or path'})
            continue
        if ik!=key:
            inv_entries[ik].setdefault('root_component_additions',[]).append({
                'root_addition_id':rid,'decision_id':ids[key],'reported_center':center,
                'confidence':confidence,'source':deepcopy(root_section_refs[section]),
                'status':'new local component of existing physical cluster; no extra count'})
            continue
        inv_entries[ik]['root_source_evidence']=[deepcopy(root_section_refs[section])]
        inv_entries[ik]['reported_center']=center
        inv_entries[ik]['root_addition_id']=rid
        inv_entries[ik]['source_hand_candidates']=['undetermined hand']
        inv_entries[ik]['root_inventory_note']='Root-only observed component; final page attachment remains pending.'

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

# Explicit ink choices copied from completed root crop-log entries.  These
# leave the page and overall record unapproved and never supply a root page.
root_choice_records=[]
def apply_root_choice(key, section, final, confidence, crop, *, reader=None,
                      alternatives=None, doubt_reading=None, qualification=None,
                      counts_confirmed=True):
    if section not in root_sections or key not in decisions_by_key:
        return
    d=decisions_by_key[key]
    d['final']=d['C'] if final==':C' else final
    d['evidence']=root_sections[section]
    d['confidence']=confidence
    d['crop']=crop.removeprefix('out/')
    d['source_crop_path']=crop
    if crop not in d['candidate_crop_references']:
        d['candidate_crop_references'].append(crop)
    d['root_decided']=True
    d['main_counting_decision_pending']=not counts_confirmed
    d['root_decision_source']=deepcopy(root_section_refs[section])
    d['root_selected_reader']=reader
    d['root_selected_candidate_sources']=deepcopy(d['reader_provenance'][reader]['tex']) if reader else []
    d['pending_fields']=['root final-page attachment','root overall approval']
    if not counts_confirmed:
        d['pending_fields'].append('root Boolean difference counts')
    if qualification:
        d['remaining_qualification']=qualification
    if key in {'label','ou','marked_state'}:
        d['C_doubt_status']='retained'
    matching=[x for x in doubts if x['decision_id']==d['id']]
    if not matching and qualification:
        x={'reading':None,'alternatives':None,'reason':None,'confidence':None,
           'location':d['location'],'decision_id':d['id'],'source_doubt_candidates':[],
           'count_locus_key':d['count_locus_key'],'count_parent_decision':d['count_parent_decision'],
           'source_C_row':d['C_doubt_source_row'],'main_approval_pending':True}
        doubts.append(x); matching=[x]
    for x in matching:
        x.update({'reading':doubt_reading or d['final'],'alternatives':alternatives or [],
                  'reason':root_sections[section], 'confidence':confidence,
                  'root_decided':True,'status':'root ink choice recorded; final page and overall approval pending',
                  'root_decision_source':deepcopy(root_section_refs[section]),'crop':d['crop']})
        if qualification:
            x['remaining_qualification']=qualification
    root_choice_records.append({'decision_id':d['id'],'source':deepcopy(root_section_refs[section]),
                                'confidence':confidence,'source_crop_path':crop,
                                'Boolean_counts_confirmed':counts_confirmed})

right_crop='out/readers/012/B/crops/c05_right_group.png'
left_crop='out/crops/012/07_left_lower_assembly.png'
fourth_crop='out/crops/012/05_top_fourth_oval.png'
apply_root_choice('right_state',1,'live graphic primary; cancellation retained as an alternative; original paths preserved','low',right_crop,
                  alternatives=['whole-group cancellation'],doubt_reading='live graphic',
                  qualification='Whole-group cancellation target and function remain unresolved; H biffé is retained as the explicit alternative.')
for key,rid,conf in [('pale_left_rim','A012-08','medium'),('pale_bottom_rim','A012-09a','medium'),
                     ('pale_slant_rim','A012-09b','medium'),('right_vertical_trace','A012-11','low')]:
    apply_root_choice(key,1,diffs['A'][rid]['reading'],conf,right_crop,reader='A',
                      qualification='Visible geometry retained; hand, role or precise faded endpoints remain qualified as in the root evidence.')
apply_root_choice('terminal_main',1,'Two pale roughly parallel terminal wisps, retained as one terminal-location refinement','medium',right_crop,
                  qualification='Pale endpoint geometry remains qualified; the two separate source paths remain component-mapped.')
apply_root_choice('terminal_parallel',1,'Separate parallel pale residual wisp beside the terminal main stroke','medium',right_crop,
                  qualification='Component of the one terminal-location refinement; no independent C/H count.')
for key,final,conf in [
    ('rule_above_point','Detached point above upper rule near (907,504)','medium'),
    ('rule_end_point','Dark point below far-right rule end near (1643,532)','high'),
    ('oval_below_point','Small point below upper oval near (1034,823)','medium'),
    ('transverse_point','Point below lower transverse curve near (1231,861)','medium'),
    ('right_edge_dash','Independent dash at right paper edge, preserving its visible course to the scan edge','high')]:
    apply_root_choice(key,1,final,conf,right_crop,qualification='Hand, role and surface origin remain undetermined.')
apply_root_choice('marked_state',2,'overlaid zigzags primary; cancellation of the large oval retained as an alternative','low',left_crop,
                  alternatives=['cancellation of the large oval'],doubt_reading='overlaid zigzags',
                  qualification='The state marker targets the larger oval. Its connected lower miniature remains live. This retains original C doubt row 3.')
apply_root_choice('ou',2,'\\unsure{ou}','medium',left_crop,doubt_reading='ou',
                  qualification='The compact first loop and compressed second run retain uncertainty; root recovered no competing word.')
for key in ['left_wedges','marked_oval','parenthetical','opening_arc','closing_arc','left_dash','lower_mini_left','lower_mini_right']:
    apply_root_choice(key,2,':C','high',left_crop)
apply_root_choice('marked_terminal',2,diffs['B']['B008']['reading'],'medium',left_crop,reader='B',
                  qualification='Interrupted pale continuation and dark hooked endpoint retained; faded geometry remains qualified.')
apply_root_choice('label',3,'\\unsure{OK|Ok}','medium',fourth_crop,alternatives=['Ok'],doubt_reading='OK',
                  qualification='K/k case remains qualified by the short curved lower outer branch.')
apply_root_choice('top_fourth',3,':C','high',fourth_crop)
for key,final,center in [
    ('root_upper_1278','Compact gray triangular/rounded fleck near (1278,77)',[1278,77]),
    ('root_upper_1297','Smaller gray upright fleck near (1297,94)',[1297,94])]:
    apply_root_choice(key,3,final,'medium',fourth_crop,counts_confirmed=False,
                      qualification='Approximate local geometry only. Hand, role and surface origin remain unresolved; no character or punctuation role supplied.')
    if key in decisions_by_key:
        decisions_by_key[key]['reported_center']=center
        decisions_by_key[key]['root_only_addition']=True
for key,section,crop in [
    ('top_first',4,'01_top_first_oval'),('top_second',5,'03_top_second_oval'),
    ('top_third',6,'04_top_third_oval'),('top_small_first',7,'02_top_small_alternative'),
    ('top_small_right',8,'06_top_right_miniature'),('central_oval',9,'08_central_lower_oval'),
    ('tripod',10,'09_thick_tripod'),('square',11,'10_upper_square'),
    ('stem_triangle',12,'11_stemmed_triangle'),('lower_quadrilateral',13,'12_lower_diagonal_quadrilateral'),
    ('spoked_triangle',14,'13_lower_spoked_triangle')]:
    apply_root_choice(key,section,':C','high',f'out/crops/012/{crop}.png')
apply_root_choice('field_780',5,diffs['C']['D_N04']['reading'],'medium','out/crops/012/03_top_second_oval.png',reader='C',
                  qualification='Detached graphical point with unknown hand, role and surface origin; root explicitly selects C-reader shape/position.')
apply_root_choice('small_oval_point',8,diffs['A']['A012-17']['reading'],'high','out/crops/012/06_top_right_miniature.png',reader='A',
                  qualification='Visible detached point inside the miniature lower rim; hand, role and surface origin remain undetermined.')
apply_root_choice('upper_loop',15,':C','high','out/readers/012/B/crops/c03_upper_loop.png')
apply_root_choice('lower_zigzag',16,':C','high','out/readers/012/B/crops/c04_lower_loop.png')
for key in ['zigzag_point_A','zigzag_point_B']:
    apply_root_choice(key,16,'One compact gray rounded patch; A-style small ellipse at approximate root center (430.5,902.5)','medium',
                      'out/readers/012/B/crops/c04_lower_loop.png',
                      qualification='Root identifies A20 and B015 as one bounded patch. Hand, role and surface origin remain unresolved; no duplicate point added.')
    if 16 in root_sections:
        decisions_by_key[key]['reported_center']=[430.5,902.5]
        decisions_by_key[key]['root_identity_resolution']='A20 and B015 are one physical patch, counted at D54.'
for key in ['triangle','filled_dot']:
    apply_root_choice(key,17,':C','high','out/readers/012/B/crops/c06_triangle_dots.png')
for key,rid,conf in [('apex_tick','A012-13a','high'),('triangle_gray','A012-13b','medium'),('gap_dark','A012-14','high')]:
    apply_root_choice(key,17,diffs['A'][rid]['reading'],conf,'out/readers/012/B/crops/c06_triangle_dots.png',reader='A',
                      qualification='Qualified local graphic; hand, role and surface origin unresolved. Root selects A coordinates/shape and retains distinct local path components.')
apply_root_choice('gap_pale',17,'Pale elongated upright spot near (443,484); C-reader compact qualified graphic','medium',
                  'out/readers/012/B/crops/c06_triangle_dots.png',reader='C',
                  qualification='Independent C/H omission; hand, role and surface origin unresolved.')
for key,final,conf in [
    ('upper_pair_left','Gray compact upright ovoid with darker core near (591,45); C-reader N01 local shape retained','medium'),
    ('upper_pair_right','Darker small triangular droplet with pale upper taper near (609,47); C-reader N02 local shape retained','high')]:
    apply_root_choice(key,18,final,conf,'out/readers/012/B/crops/c07_top_gap_traces.png',reader='C',
                      qualification='Independent qualified C/H omission; hand, role and surface origin unresolved.')
apply_root_choice('upper_margin',19,'Dark rounded triangular core with diffuse gray upper taper near (1659,55); C-reader N03 compact shape','high',
                  'out/crops/012/14_upper_right_point.png',reader='C',
                  qualification='Independent qualified C/H omission; hand, role and surface origin unresolved.')
apply_root_choice('lower_hook',20,'Pale descending hook and leftward low return, with the separate lower foot and neighboring oblique retained in one cluster','medium',
                  'out/readers/012/A/crops/05_lower_pale_trace.png',reader='A',
                  qualification='No letter, attachment, hand or surface origin assigned. The two nearby components retain their own low confidence below.')
apply_root_choice('lower_hook_foot',20,'Separate faint low foot stroke','low','out/readers/012/A/crops/05_lower_pale_trace.png',reader='A',
                  qualification='Faint supported component of D40 pale-hook cluster; no independent C/H count or supplied attachment.')
apply_root_choice('lower_hook_oblique',20,'Nearby faint short descending-right oblique','low','out/readers/012/A/crops/05_lower_pale_trace.png',reader='A',
                  qualification='Low-confidence supported component amid mottled background; part of D40 cluster with no independent C/H count.')
apply_root_choice('lower_dark',21,'Compact dark rounded triangular point with gray margins near (789,1430); A polygonal local shape','high',
                  'out/readers/012/A/crops/06_lower_single_point.png',reader='A',
                  qualification='Independent qualified C/H omission; hand, role and surface origin unresolved.')
for key,rid,final in [
    ('lower_pair_upper','A012-16a','Distinct upper-right dark roughly rounded point near (1529,1706); A local polygon'),
    ('lower_pair_lower','A012-16b','Distinct lower-left dark more triangular point near (1524,1713); A local polygon')]:
    apply_root_choice(key,22,final,'high','out/readers/012/B/crops/c09_lower_paired_spots.png',reader='A',
                      qualification='Separate qualified graphical mark with its own C/H omission row; hand, role and surface origin unresolved.')
apply_root_choice('lower_1454',22,'Detached gray upright compact patch near (1455,1661); C-reader N19 local shape','medium',
                  'out/readers/012/B/crops/c09_lower_paired_spots.png',reader='C',
                  qualification='Independent qualified C/H omission; hand, role and surface origin unresolved.')
apply_root_choice('lower_1077',23,'Small rounded dark core within gray margin near (1077.5,1465); A qualified point','high',
                  'out/crops/012/15_mid_lower_point.png',reader='A',
                  qualification='B and C-reader supplied no added local point. Root preserves A candidate with unknown hand, role and surface origin.')
apply_root_choice('lower_upright',24,'Restrained three-component candidate: irregular central patch, pale narrow continuation below and separated small upper point','low',
                  'out/readers/012/C/crops/12_faint_low_vertical.png',reader='C',
                  alternatives=['paper texture and diffuse shading without a stable stroke or character candidate'],
                  qualification='Coherent upright extent and origin remain uncertain amid mottled background. No letter, deliberate stroke, hand, role or surface origin is certified.')
apply_root_choice('lower_upright_spot',24,'Separated small upper point of the pale-upright candidate','low',
                  'out/readers/012/C/crops/12_faint_low_vertical.png',reader='C',
                  qualification='Low-confidence zero-count component of D70; background texture and diffuse shading remain part of the unresolved cluster alternative.')
if 24 in root_sections:
    note=deepcopy(reports['B']['notes'][6])
    note_ref=ref(REPORT_PATHS['B'],'/notes/6')
    d=decisions_by_key['lower_upright']
    d['readers']['B']=note['text']
    d['reader_provenance']['B']['source_status']='Explicit note-based alternative; B supplied no added graphical path at this locus.'
    d['reader_provenance']['B']['notes']=[{'source':note_ref,'source_exact':note}]
    d['reader_evidence']['B'].append({'source':note_ref,'evidence':note['text']})
    d['root_retained_source_alternative']={'reader':'B','source':note_ref,'source_exact':note}
    components=[
        {'component':'irregular central darker patch','confidence':'medium',
         'source':statement_ref('C','(1445.0,2099.7)')[0],'root_decision_source':deepcopy(root_section_refs[24])},
        {'component':'extended pale upright continuation','confidence':'low',
         'source':statement_ref('C','(1446.2,2100.0)')[0],'root_decision_source':deepcopy(root_section_refs[24])},
        {'component':'separated small upper point','confidence':'low','decision_id':ids['lower_upright_spot'],
         'source':statement_ref('C','(1447.0,2096.2)')[0],'root_decision_source':deepcopy(root_section_refs[24])},
    ]
    d['root_component_confidences']=components
    for x in doubts:
        if x['decision_id']==ids['lower_upright']:
            x['root_component_confidences']=deepcopy(components)
            x['source_alternative_notes']=[{'source':note_ref,'source_exact':note}]
apply_root_choice('foot_1658',25,'Small dark triangular wedge near (1658,2190); B025 actual triangle polygon','high',
                  'out/readers/012/B/crops/c10_foot_right_traces.png',reader='B',
                  qualification='Independent qualified C/H omission; hand, role and surface origin undetermined. C-reader N28 thin diagonal remains an exact source candidate, not the selected polygon.')
apply_root_choice('foot_1418',25,'Separate compact dark rounded point near (1418,2290); C-reader N29 local shape','high',
                  'out/readers/012/B/crops/c10_foot_right_traces.png',reader='C',
                  qualification='Independent qualified C/H omission; hand, role and surface origin undetermined.')
apply_root_choice('lower_185',26,'Compact dark upright core with gray perimeter near (185,1796); C-reader N22 local shape','high',
                  'out/readers/012/C/crops/14_lower_left_speck.png',reader='C',
                  qualification='Independent qualified C/H omission; hand, role and surface origin unresolved.')
apply_root_choice('lower_699',27,'Short gray diagonal with darker elongated middle and diffuse ends near (700,1853); C-reader N23 qualified shape','medium',
                  'out/readers/012/C/crops/15_lower_oblique.png',reader='C',
                  qualification='Independent qualified C/H omission; no character, hand, role or surface origin supplied.')
apply_root_choice('lower_1359',28,'Compact triangular/rounded core with gray upper and lower extensions near (1359,1932); C-reader N24 polygon, with separate upper point in the same cluster','medium',
                  'out/readers/012/C/crops/16_lower_fold_spot.png',reader='C',
                  qualification='Main N24 and separate upper point share one C/H cluster change; hand, role and surface origin unresolved.')
apply_root_choice('lower_1359_upper',28,'Separate compact gray upper point near (1359.5,1923.9); C-reader N24 second path','medium',
                  'out/readers/012/C/crops/16_lower_fold_spot.png',reader='C',
                  qualification='Explicit zero-count local child of N24 cluster D67; hand, role and surface origin unresolved.')
apply_root_choice('lower_1352',28,'Detached compact gray spot near (1352,1954); C-reader N31 local shape','medium',
                  'out/readers/012/C/crops/16_lower_fold_spot.png',reader='C',
                  qualification='Separate C/H omission row; hand, role and surface origin unresolved.')
apply_root_choice('lower_673',29,'Small dark upright oval core with gray perimeter near (672.7,2002.6); C-reader N25 local ellipse','high',
                  'out/readers/012/C/crops/17_lower_central_point.png',reader='C',
                  qualification='Point cluster with separately qualified low-confidence R11 directly below; hand, role and surface origin unresolved.')
for key,section,crop,rid,final,conf in [
    ('lower_657',30,'16_lower_left_centre_point','D_N18','Dark rounded compact core with gray lower margin near (657,1634); C-reader N18 shape','high'),
    ('lower_487',31,'17_lower_left_point','D_N26','Small dark compact point with gray slightly upright margin near (487,2051); C-reader N26 shape','high'),
    ('foot_686',32,'18_lowest_point','D_N30','Short gray descending-right oblique with darker middle and diffuse ends near (686.5,2333.5); C-reader N30 stroke','medium')]:
    apply_root_choice(key,section,final,conf,f'out/crops/012/{crop}.png',reader='C',
                      qualification='Independent qualified C/H omission; hand, role and surface origin unresolved. No character is supplied.')
for key in ['right_rules','right_tall','right_curves','right_low']:
    apply_root_choice(key,1,':C','high',right_crop)
    if decisions_by_key[key]['root_decided']:
        decisions_by_key[key]['confidence_scope']='Shape geometry; whole-group editorial state has low confidence only at D04.'
        decisions_by_key[key]['root_confidence_instruction_exact']='Draft D29–D32 geometry confirmations can use root log1/Bc05 with high shape confidence, zeroC/H parent D04; whole-group state remains low only atD04.'
for rid,key,section,center,reading,confidence,crop,hg in root_additions:
    if section in root_sections and key in decisions_by_key:
        if section!=3:
            root_crop=f'out/readers/012/C/crops/{crop[2:]}.png' if crop.startswith('C/') else f'out/crops/012/{crop}.png'
            apply_root_choice(key,section,reading,confidence,root_crop,
                              qualification='Qualified graphical mark; hand, role and surface origin remain undetermined. No character is supplied.')
        decisions_by_key[key]['reported_center']=center
        decisions_by_key[key]['root_only_addition']=True
        decisions_by_key[key]['root_addition_id']=rid
        if key=='root_quad_174' and 16 in root_sections and 'R9 is a confirmation with no C change' in root_sections[16]:
            decisions_by_key[key]['evidence']=root_sections[13]+'\n\n'+root_sections[16]
            decisions_by_key[key]['root_decision_followup']=deepcopy(root_section_refs[16])
            decisions_by_key[key]['existing_C_component']=True
            decisions_by_key[key]['root_only_addition']=False
            decisions_by_key[key]['root_only_confirmation']=True
            decisions_by_key[key]['new_path_required']=False
            decisions_by_key[key]['remaining_doubt']=False
            decisions_by_key[key].pop('remaining_qualification',None)
            for x in doubts:
                if x['decision_id']==ids[key]:
                    x['reason']=decisions_by_key[key]['evidence']
                    x['root_decision_followup']=deepcopy(root_section_refs[16])
if 29 in root_sections:
    parent=decisions_by_key['lower_673']
    parent['root_component_confidences']=[
        {'component':'N25 dark-cored point','confidence':'high','decision_id':ids['lower_673'],'source':deepcopy(root_section_refs[29])},
        {'component':'R11 pale patch immediately below','confidence':'low','decision_id':ids['root_below_673'],'source':deepcopy(root_section_refs[29])}]
    for x in doubts:
        if x['decision_id']==ids['lower_673']:
            x['root_component_confidences']=deepcopy(parent['root_component_confidences'])
for key in ['root_upper_1278','root_upper_1297']:
    if key in decisions_by_key and decisions_by_key[key]['root_decided']:
        decisions_by_key[key]['main_counting_decision_pending']=False
        decisions_by_key[key]['pending_fields']=['root final-page attachment','root overall approval']
for n,key in [(1,'label'),(2,'ou'),(3,'marked_state')]:
    if decisions_by_key[key]['root_decided']:
        actual_C_doubt_map[n-1]['source_row_final_status']='retained'
        actual_C_doubt_map[n-1]['root_decision_source']=deepcopy(decisions_by_key[key]['root_decision_source'])
        actual_C_doubt_map[n-1]['status_basis']='Root explicitly retains this original source doubt; overall approval remains pending.'
        for local in actual_C_doubt_map[n-1]['local_subloci']:
            local_decision=next(d for d in decisions if d['id']==local['decision_id'])
            if local_decision['root_decided']:
                local['root_decided']=True
                local['status']='retained qualification' if local['decision_id']==ids[key] else 'source geometry preserved or explicitly refined by root'
                local['root_decision_source']=deepcopy(local_decision['root_decision_source'])
for group in H_collation_groups:
    parent=next(d for d in decisions if d['id']==group['count_decision'])
    group['root_group_count_confirmed']=parent['root_decided'] and not parent['main_counting_decision_pending']
    group['main_classification_pending']=not group['root_group_count_confirmed']
    group['main_approval_pending']=True
    if parent.get('root_decision_source'):
        group['root_decision_source']=deepcopy(parent['root_decision_source'])

# Keep one top-level doubt record for each nearby-trace cluster. The full
# component records remain nested with their source identities, while all
# source-doubt coverage pointers still name every mapped component decision.
raw_assembled_doubts=deepcopy(doubts)
doubts_by_id={x['decision_id']:x for x in doubts}
kept_doubts=[]
for x in doubts:
    if x['decision_id']==ids.get('root_quad_174'):
        continue
    parent=x.get('count_parent_decision')
    if x['decision_id']==ids['marked_oval']:
        parent=ids['marked_state']
        x['state_doubt_scope_note']='The whole-oval H geometry row carries source-doubt provenance; the editorial-state doubt is represented at the state decision.'
    if parent and parent in doubts_by_id:
        doubts_by_id[parent].setdefault('component_doubts',[]).append(x)
        doubts_by_id[parent].setdefault('component_decision_ids',[]).append(x['decision_id'])
    else:
        kept_doubts.append(x)
doubts=kept_doubts

# Attach the text clerk's exact selected bodies and proposed draft spans.
# These references do not claim approval or attachment to a final page.
tex_selection_coverage=[]
if tex_mapping:
    root_key_by_id={r:k for r,k,*_ in root_additions}
    for i,item in enumerate(tex_mapping.get('new_graphical_additions',[])):
        if item['id'] in root_key_by_id:
            targets=[ids[root_key_by_id[item['id']]]]
        else:
            aliases=item.get('source_aliases',[])
            targets=list(row_targets[aliases[0][0]].get(aliases[0][1],[])) if aliases else []
        # Propagate a shared wrapper only to source-linked component rows.
        for s in specs:
            if s['count_parent_key'] and ids[s['count_parent_key']] in targets:
                parent=bykey[s['count_parent_key']]
                if any(set(s['rows'][r]) & set(parent['rows'][r]) for r in 'ABC'):
                    targets.append(ids[s['key']])
        targets=list(dict.fromkeys(targets))
        entry={'source':ref(TEX_MAPPING_PATH,f'/new_graphical_additions/{i}'),
               'addition_id':item['id'],'root_entry':item['root_entry'],
               'tex_body_exact':item['tex_body'],'source_choice_exact':item['source_choice'],
               'source_aliases_exact':item.get('source_aliases',[]),
               'draft_source':ref('out/checks/scan012_final_draft.tex',**item['draft_span']),
               'final_page_attachment_pending':True}
        for d in decisions:
            if d['id'] in targets:
                d.setdefault('selected_graphical_tex_provenance',[]).append(deepcopy(entry))
                d.setdefault('proposed_page_sources',[]).append(deepcopy(entry['draft_source']))
        tex_selection_coverage.append({'addition_id':item['id'],'source':entry['source'],
                                       'decision_ids':targets,'mapped':bool(targets)})
    pmap={x['source_path']:x for x in tex_mapping.get('source_paths',[])}
    for s in specs:
        d=decisions_by_key[s['key']]
        for n in s['paths']:
            if n in pmap:
                d.setdefault('proposed_page_sources',[]).append(dict(pmap[n]['draft'],source_C_path=n))
    for item in inventory:
        item['proposed_page_sources']=[deepcopy(span) for d in decisions if d['id'] in item['decision_ids']
                                       for span in d.get('proposed_page_sources',[])]
    for d in decisions:
        if d['key'] in {'right_curves','right_low'}:
            d['shared_component_cross_reference']={'source_C_path':67,'canonical_component_id':'012-C-path67',
                'decision_ids':[ids['right_curves'],ids['right_low']],
                'literal_occurrences_in_proposed_draft':pmap[67]['literal_occurrences_in_draft'],
                'draft_source':pmap[67]['draft'],'change_count':False,
                'note':'One existing detached component near (985,912); source inventory attribution differs, with no duplicate inventory element or path.'}

# Compact public comparison cells; all exact contour strings remain under
# provenance and the original path/source references are unchanged.
geometry_summaries={
 'right_state':'Repeated corner rules, intersecting curves and two oval groups; original C supplies no explicit cancelled/live qualification',
 'top_first':'Oval with hatched triangle, crossing chords and lower cap arc',
 'top_small_first':'Small alternative oval with crossing chords and central dark patch',
 'top_second':'Oval with three upright chords, thick crosspiece and marked endpoints',
 'top_third':'Oval with hatched quadrilateral and crossing chord system',
 'top_fourth':'Oval with hatched triangle, thick segment and interrupted rim pieces',
 'top_small_right':'Small alternative oval with thick radius/crosspiece and crossing chords',
 'triangle':'Small triangle with projecting apex-side strokes', 'filled_dot':'Separate large filled point beside the triangle',
 'upper_loop':'Narrow upright looping graphic', 'tripod':'Heavy three-pronged graphic', 'square':'Irregular four-sided square with local gap',
 'stem_triangle':'Triangle with rising upper stem', 'left_wedges':'Left oval with crossed chords and two dark wedges',
 'marked_oval':'Large oval with crossing chords, inner hatching and overlaid zigzags',
 'parenthetical':'Lower parenthetical pair of miniature ovals, their ou labels, two parenthesis arcs and detached left dash',
 'opening_arc':'Opening parenthesis arc', 'closing_arc':'Closing parenthesis arc', 'left_dash':'Detached short dash by opening parenthesis',
 'lower_mini_left':'Left miniature oval with wedge and separate internal diagonal',
 'lower_mini_right':'Right miniature oval with radii, in the lower portion of shared path34',
 'central_oval':'Central lower oval with crossing chords/curves and central wedge hatching',
 'lower_quadrilateral':'Uneven quadrilateral with ascending diagonal and extended lower-left stroke',
 'lower_zigzag':'Tall angular looping/zigzag graphic', 'spoked_triangle':'Elongated triangle with three interior spokes and projecting lower-right hook',
 'right_rules':'Repeated upper and left boundary strokes of the right group',
 'right_tall':'Tall right-group oval with its crossing curves and interrupted rim',
 'right_curves':'Extended crossing curves and detached local fragments of the right group',
 'right_low':'Low rounded right-group outline with curved chords',
 'root_quad_174':'Existing path68 excursion near (174,941), confirmed without an added path',
}
for s in specs:
    d=decisions_by_key[s['key']]
    if not s['paths']:
        continue
    old_C=d['C'];old_final=d['final']
    path_label=', '.join(str(n) for n in s['paths'])
    prov={'original_C_path_ids':s['paths'],'C_literal_exact':old_C,
          'final_literal_exact':old_final,'geometry_unchanged_by_compact_presentation':True}
    d['literal_graphics_provenance']=prov
    summary=geometry_summaries.get(s['key'],s['location'])
    if '\\path[' in old_C:
        d['C']=summary+f' (original C paths: {path_label}).'
    if old_final and '\\path[' in old_final:
        d['final']=summary+f'; original C paths {path_label} retained.'
    elif old_final and s['key'] in {'right_state','marked_state'}:
        d['final']=old_final+f' Original C paths: {path_label}.'
    if d['final'] and s['H_group_count_row']:
        added=[x['id'] for x in decisions if x['H_count_group']==d['H_count_group'] and x['id']!=d['id'] and x['diff_C'] and x['root_decided']]
        if added:
            d['final']+=' Approved local additions: '+', '.join(added)+'.'
        qualifications={'marked_oval':'Editorial-state qualification: '+ids['marked_state']+'.',
                        'parenthetical':'Between-miniature ou qualification: '+ids['ou']+'.',
                        'top_fourth':'Upper label case qualification: '+ids['label']+'.'}
        if s['key'] in qualifications:
            d['final']+=' '+qualifications[s['key']]
for s in specs:
    d=decisions_by_key[s['key']]
    children=[decisions_by_key[t['key']] for t in specs if t['count_parent_key']==s['key'] and decisions_by_key[t['key']]['root_decided']]
    if children and d['final']:
        if s['key']=='zigzag_point_A':
            d['final']+=' Source alias '+ids['zigzag_point_B']+' refers to this same patch.'
        else:
            d['final']+=' Local qualified components: '+', '.join(x['id']+' ('+x['confidence']+')' for x in children)+'.'
    if s['key']=='lower_upright' and d['root_decided']:
        d['final']+=' Central patch medium; extended upright low.'

root_notes=(
    'The sheet preserves four large upper ovals, two small upper alternatives, lower oval constructions, '
    'a parenthetical pair of miniatures, the small triangle and separate filled point, two upright looping graphics, '
    'a thick three-pronged graphic, a square, a stemmed triangle, a lower diagonal quadrilateral, a three-spoked triangle, '
    'and the connected right-hand group of repeated rules, crossing curves and two oval forms. '
    'There are four OK loci and four ou loci. The upper-right OK/Ok case and the compressed between-miniature ou remain qualified. '
    'The three original C doubt rows are retained: the third concerns the marked left oval and its possible cancellation. '
    'Its connected lower miniature remains live. The added whole-right-group qualification retains live graphic primary '
    'with cancellation as the explicit alternative to H’s biffé. H’s rereading note supersedes its original three-OK count.\n\n'
    'All original C paths and labels are retained, with approved pale continuations and detached graphical marks mapped locally. '
    'A20 and B015 form one physical patch. R9 is an existing path68 component, with no new path, change count or remaining doubt. '
    'Path67 is retained once inside the right group, with both source inventory attributions preserved. '
    'Terminal wisps, the pale hook, the faint upright, N24 with its upper point and N25 with R11 retain their component mappings '
    'and local confidence levels. The faint upright keeps B’s paper-texture/diffuse-shading alternative. '
    'Detached marks retain uncertainty about hand, role and surface origin; no character is supplied for them. '
    'OK → okay is an approved possible expansion; the manuscript abbreviation stays unexpanded.\n\n'
    'The archive numeral 11 remains comment-only apparatus. The H tail section and its note explicitly assigned to feuillet13 '
    'are excluded from this scan. No theorem or computation was performed by any reader or root; all check-event lists remain empty. '
    'The final graphical source is assembled from the exact retained paths and the locally recorded additions.'
)
abbreviations[0]['root_decided']=True
abbreviations[0]['root_approval_basis']='Root explicitly approves OK → okay as a possible expansion; manuscript form remains unexpanded.'
for audit in audits:
    audit['root_decided']=True
    audit['root_audit_basis']='Root confirms all three complete reading.md audits were read; no additional unmapped content remains beyond the recorded R11 component.'
counts={
    'decision_candidates':len(decisions),'decision_loci':len(decisions),
    'actual_C_doubt_source_rows':len(actual_C_doubt_map),
    'mapped_C_doubt_local_subloci':sum(len(x['local_subloci']) for x in actual_C_doubt_map),
    'source_difference_rows':{r:len(reports[r]['differences']) for r in 'ABC'},
    'source_doubt_rows':{r:len(reports[r]['doubts']) for r in 'ABC'},
    'source_inventory_rows':{r:len(reports[r]['inventory']) for r in 'ABC'},
    'witness_C_inventory_rows':len(source_inventory),'inventory_elements':len(inventory),
    'C_difference_loci':sum(d['diff_C'] is True for d in decisions),
    'H_difference_loci':sum(d['diff_H'] is True for d in decisions),
    'actual_C_doubts_retained':sum(x['source_row_final_status']=='retained' for x in actual_C_doubt_map),
    'actual_C_doubts_resolved':sum(x['source_row_final_status']=='resolved' for x in actual_C_doubt_map),
    'remaining_doubt_or_graphic_uncertainty_loci':len(doubts),
    'remaining_qualified_unique_count_keys':len({x['count_locus_key'] for x in doubts}),
    'H_physical_groups':len(H_collation_groups),'check_events':0,
    'status':'Boolean tally of current root-supplied ink choices and groupings; main_adjudicated remains false.',
}
for witness in 'CH':
    counts[f'{witness}_difference_confidence']={c:sum(d[f'diff_{witness}'] is True and d['confidence']==c for d in decisions)
                                               for c in ['high','medium','low']}

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
 'filename':'J81-02_81_scan012.tex','brief_version':'brief_v10_scan012.md',
 'main_adjudicated':False,'main_approved_utc':None,
 'draft_status':'All root ink choices, evidence, confidence and Boolean groupings are recorded. Final-page attachment and root overall approval remain pending.',
 'decisions':decisions,'doubts':doubts,'inventory':inventory,
 'notes':root_notes,
 'abbreviations':abbreviations,'check_events':[],
 'reader_check_events':{r:deepcopy(reports[r].get('check_events',[])) for r in 'ABC'},
 'check_events_note':'Reader event lists are empty. No event is generated by text assembly.',
 'workflow_note':'All32 root crop-log choices are entered. The record assembler used text alone: no image inspection, cropping, OCR, web lookup, compilation/rendering or mathematical check. Root confirms all three complete reading.md audits contain no additional unmapped material beyond the recorded R11. Exact source paths, selected graphical bodies, source confidence/flags and component qualifications remain in provenance. Final-page attachment and root overall approval remain pending.',
 'source_reports':REPORT_PATHS,'source_readings':TEX_PATHS,
 'source_audits':{r:{k:deepcopy(v) for k,v in reports[r].items() if k in ['notes','notation','brief_feedback','source_C_doubt_rows','C_doubt_source_map','source_doubt_map','structural_validation','workflow']} for r in 'ABC'},
 'source_fingerprints':fingerprints,
 'root_log_snapshot_fingerprint':hashlib.sha256(root_log_text.encode()).hexdigest(),
 'reader_completion':{r:{k:reports[r].get(k) for k in ['reader','start_utc','end_utc','full_image_viewed','halves_viewed','complete_visual_read']} for r in 'ABC'},
 'root_adjudication_log':ROOT_LOG_PATH,'root_page_source':None,
 'root_choices_recorded':root_choice_records,
 'proposed_root_page_source':'out/checks/scan012_final_draft.tex',
 'tex_selection_coverage':tex_selection_coverage,
 'tex_mapping_source':ref(TEX_MAPPING_PATH),
 'tex_mapping_root_log_fingerprint':tex_mapping.get('root_log',{}) if tex_mapping else None,
 'root_messages_exact':[
     'C is FINAL at13:20:22 UTC, now17 crops and31 added-trace entries. All three completed returns are available.',
     'Keep component mappings for terminal pair and lower hook, but one Boolean C/H count per physical graphic cluster: A10/B007 two terminal strokes are one terminal-location change; A12 hook plus nearby short foot/oblique fragments are one pale-hook-location change. C N27 upright/central patch/detached upper spot can be mapped component-wise but one nearby-trace cluster count. Additional detail can be child subloci or zero-count rows with explicit parent cross-reference. A20/B015 identity still pending root crop; no merge yet.'
 ],
 'actual_C_doubt_map':actual_C_doubt_map,
 'raw_assembled_doubts':raw_assembled_doubts,
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
 'counting_policy':'Draft counts use only Boolean diff_C/diff_H values; original source flags are separately preserved. One H row per whole physical sketch/group. Local C refinements share the relevant H row. Terminal pair, pale-hook cluster and lower-upright cluster each have one count row with zero-count components. '+('Root entry16 identifies A20/B015 as one patch counted at D54, with D55 a zero-count source cross-reference. ' if 16 in root_sections else 'A20/B015 identity remains pending and is not merged. ')+'Explicit root counting confirmations are recorded per row; overall approval remains pending.',
 'counts':counts,
 'proposed_counts':{
     'decision_candidates':len(decisions),'actual_C_doubt_source_rows':len(actual_C_doubt_map),
     'mapped_C_doubt_local_subloci':sum(len(x['local_subloci']) for x in actual_C_doubt_map),
     'source_difference_rows':{r:len(reports[r]['differences']) for r in 'ABC'},
     'source_doubt_rows':{r:len(reports[r]['doubts']) for r in 'ABC'},
     'source_inventory_rows':{r:len(reports[r]['inventory']) for r in 'ABC'},
     'witness_C_inventory_rows':len(source_inventory),'inventory_union_candidates':len(inventory),
     'C_difference_loci':sum(d['diff_C'] is True for d in decisions),
     'H_difference_loci':sum(d['diff_H'] is True for d in decisions),
     'H_physical_groups':len(H_collation_groups),'check_events':0,
     'status':'mechanical proposal only; root approval pending'},
 'assembly_timestamp_utc':datetime.now(timezone.utc).isoformat(),
 'assembly_revision':'All final reader text rows and all32 root crop-log choices mapped. Public C/final cells are compact; exact contour text and selected graphical bodies remain in provenance. Main approval and final-page attachment remain pending.',
 'coverage_status':{'all_source_rows_mapped':all_mapped,'unmapped':unmapped,
                    'reader_C_final_timestamp_present':bool(reports['C'].get('end_utc')),
                    'root_completion_confirmation_pending':False,
                    'root_ink_choice_pending':any(not d['root_decided'] for d in decisions),
                    'root_inventory_attachment_pending':True,
                    'tex_additions_mapped':len(tex_selection_coverage),
                    'all_tex_additions_mapped':all(x['mapped'] for x in tex_selection_coverage),
                    'uncovered_prose_issue':None},
 'attention_items':[
     {'decision_ids':[ids['zigzag_point_A'],ids['zigzag_point_B']],
      'issue':'Root entry16 identifies A20/B015 as one bounded patch. D54 carries one C/H addition; D55 preserves B source identity with zero additional count.' if 16 in root_sections else 'A20/B015 may refer to one pale point or two neighboring points. Text bboxes and coordinates differ; root crop identity decision required.'},
     {'decision_ids':[ids['right_state']],
      'issue':'A/C-reader report diff_C=false for a newly added state qualification; proposed Boolean C=true follows root instruction, while source flags remain exact.'},
     {'decision_ids':[ids['rule_above_point']],
      'issue':'Root log1 explicitly places D53 in D04 right-group H parent; diff_H=false.'},
     {'decision_ids':[ids['right_curves'],ids['right_low']],
      'issue':'One literal path67 component near (985,912) is retained; D31/D32 preserve differing source inventory attributions without duplicate inventory/path or change count.'},
 ],
}

if not all_mapped:
    raise RuntimeError('Unmapped source rows remain: '+json.dumps(unmapped,ensure_ascii=False))

(OUT/'scan012_record_draft.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')

def md(v):
    return str(v).replace('|','\\|').replace('\n',' / ')
lines=[
 '# scan012 — text-only candidate mapping', '',
 'This is a mechanical draft. `main_adjudicated=false`. Explicit root crop-log choices are recorded with their exact evidence. Remaining choices, final-page attachment and overall approval remain pending.', '',
 '## Coverage', '',
 '| Source | Difference rows | Doubt entries | Inventory rows |',
 '|---|---:|---:|---:|',
 *[f"| {r} | {len(reports[r]['differences'])} | {len(reports[r]['doubts'])} | {len(reports[r]['inventory'])} |" for r in 'ABC'], '',
 f"All source rows are mapped. The {len(source_inventory)} original C inventory rows map into {len(inventory)} physical inventory elements, including explicit triangle/point and parenthesis/dash components. Reader C final timestamp: {reports['C'].get('end_utc')!r}.", '',
 f"Current Boolean tally: C {counts['C_difference_loci']}; H {counts['H_difference_loci']}. All three original C doubts are retained. There are {len(doubts)} physical doubt/graphic-qualification groups, with local component confidence retained. All {len(tex_selection_coverage)} selected graphical additions map to decisions. Main approval remains pending.", '',
 '## Candidate loci', '',
 'The C/H columns remain draft Boolean values; explicit root confirmations are tagged per row. Source flags remain unchanged in `reader_original_flags` and source coverage. The JSON carries all literal candidates, evidence, excerpts and source pointers.', '',
 '| ID | Physical locus | A rows | B rows | C-reader rows | Proposed C/H | H count row / cluster parent |',
 '|---|---|---|---|---|---|---|',
]
for s,d in zip(specs,decisions):
    grouping=d['count_parent_decision'] or d['H_count_decision'] or 'independent'
    lines.append(f"| {d['id']} | {md(d['location'])} | {','.join(s['rows']['A']) or 'no separate candidate'} | {','.join(s['rows']['B']) or 'no separate candidate'} | {','.join(s['rows']['C']) or 'no separate candidate'} | {d['diff_C']}/{d['diff_H']} | {grouping} |")
lines += ['', '## Explicit root choices recorded', '',
          '| Decision | Reading scope | Confidence | Root log entry | Source crop |',
          '|---|---|---|---|---|']
for d in decisions:
    if d['root_decided']:
        final='Original C paths retained' if d['final']==d['C'] and d['witness_C_sources'] else d['final']
        lines.append(f"| {d['id']} | {md(final)} | {d['confidence']} | {d['root_decision_source']['pointer']} | {d['source_crop_path']} |")
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
                  'C_differences':counts['C_difference_loci'],'H_differences':counts['H_difference_loci'],
                  'remaining_doubt_groups':len(doubts),'tex_additions_mapped':len(tex_selection_coverage),
                  'all_root_ink_choices_entered':all(d['root_decided'] for d in decisions),
                  'main_adjudicated':False},ensure_ascii=False))
