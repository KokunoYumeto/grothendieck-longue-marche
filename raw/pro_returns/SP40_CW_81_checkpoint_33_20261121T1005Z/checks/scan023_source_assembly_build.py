#!/usr/bin/env python3
"""Source-only execution of root's frozen scan023 assembly authorization.

Reads only released text sources.  No image, TeX engine, rendering, geometry
calculation, mathematical check, approval, or final-page operation occurs here.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path('/workspace/scratch/94548b74fbe0')
OUT = ROOT / 'out/checks'
DRAFT = 'out/checks/scan023_final_draft.tex'
MAP = 'out/checks/scan023_final_source_map.json'
PLAN = 'out/checks/scan023_root_assembly_plan.md'
JOURNAL = 'out/checks/scan023_main_decisions.md'
SCOPE = 'out/checks/scan023_root_scope_authorization.json'
UNION = 'out/checks/scan023_source_union.json'
BRIEF = 'out/briefs/source_record_brief_v05.md'
SOURCES = {r: f'out/readers/023/{r}/reading.tex' for r in 'ABC'}
cache = {}


def read(path):
    if path not in cache:
        cache[path] = (ROOT / path).read_bytes().decode('utf-8')
    return cache[path]


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def ref(path, start=0, end=None, literal=True):
    text = read(path)
    if end is None:
        end = len(text)
    body = text[start:end]
    ans = {
        'path': path, 'path_relative_to_out': path[4:] if path.startswith('out/') else path,
        'sha256_utf8': sha(text), 'file_sha256_utf8': sha(text),
        'char_start_zero_based': start, 'char_end_exclusive': end,
        'utf8_byte_start': len(text[:start].encode('utf-8')),
        'utf8_byte_end_exclusive': len(text[:end].encode('utf-8')),
        'start_byte_utf8': len(text[:start].encode('utf-8')),
        'end_byte_utf8': len(text[:end].encode('utf-8')),
        'line_start_one_based': text.count('\n', 0, start) + 1,
        'line_end_one_based': text.count('\n', 0, max(start, end - 1)) + 1,
        'span_sha256_utf8': sha(body),
    }
    if literal:
        ans['literal'] = body
    return ans


def find_span(path, literal, start=0, end=None):
    text = read(path)
    end = len(text) if end is None else end
    i = text.index(literal, start, end)
    assert text.find(literal, i + 1, end) == -1, ('ambiguous source fragment', path, literal[:100])
    return i, i + len(literal)


def literal_ref(path, literal, start=0, end=None):
    return ref(path, *find_span(path, literal, start, end))


def groups(text):
    stack = []
    result = []
    pat = re.compile(r'^% (BEGIN|END)(?: GROUP)? ([A-Z][0-9]{3}-[A-Z0-9]+)\r?\n', re.M)
    for m in pat.finditer(text):
        action, gid = m.group(1, 2)
        if action == 'BEGIN':
            stack.append({'id': gid, 'start': m.start(), 'begin_end': m.end(),
                          'parent_group': stack[-1]['id'] if stack else None})
        else:
            assert stack and stack[-1]['id'] == gid, ('group boundary', gid)
            g = stack.pop()
            g.update(end=m.end(), end_start=m.start())
            result.append(g)
    assert not stack, stack
    return sorted(result, key=lambda g: g['start'])


texts = {r: read(p) for r, p in SOURCES.items()}
original_groups = {r: {g['id']: g for g in groups(t)} for r, t in texts.items()}
source_maps = {r: json.loads(read(f'out/readers/023/{r}/source_map.json')) for r in 'BC'}
source_group_meta = {}
for rd, sm in source_maps.items():
    for g in sm['groups']:
        source_group_meta[g.get('id', g.get('group_id'))] = g
assert sha(read(JOURNAL)) == 'e47c66e9ceb1a9823bfa73ee6544e6068d84def3a91dee1547ab2e83ab4f07af'
assert sha(read(PLAN)) == 'dbb078b74042d49eec9ca1cc404270513ed91c02c7be796bc88311c0f2004193'
assert sha(read(SCOPE)) == 'ab98ffb03ea44a0cfc6541f322c51a1571930a0e256633ed752bbccb269a7a03'
for rd, expected in {
    'A': 'c62ae74f359cb583bc0c10d9a405faec361957f18663770428ae5620dfd018db',
    'B': '034cc7883fd101f4238f484f40942df66513b5c64a4393b9ef5614d274830370',
    'C': '9856c464942c4ce2b547e4fff9afe55b0bab9f626983853f5c052ace757e29f5',
}.items():
    assert sha(texts[rd]) == expected, ('reader freeze', rd)


def group_text(rd, gid):
    g = original_groups[rd][gid]
    return texts[rd][g['start']:g['end']]


def group_ref(rd, gid):
    g = original_groups[rd][gid]
    return ref(SOURCES[rd], g['start'], g['end'])


def plan_ref(number):
    p = read(PLAN)
    m = re.search(rf'^{number}\. ', p, re.M)
    end = p.find('\n', m.start())
    return ref(PLAN, m.start(), end + 1)


def journal_ref(number):
    p = read(JOURNAL)
    m = re.search(rf'^## {number:02d} ', p, re.M)
    nxt = re.search(r'^## ', p[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(p)
    return ref(JOURNAL, m.start(), end)


edits = []


def edit(name, old, new, plan_item, journal_sections, donor_refs=(), within=None, insertion_at=None):
    c = texts['C']
    if insertion_at is not None:
        a = b = insertion_at
    else:
        bounds = (0, len(c)) if within is None else (original_groups['C'][within]['start'], original_groups['C'][within]['end'])
        a, b = find_span(SOURCES['C'], old, *bounds)
    edits.append({
        'edit_id': name, 'original_start': a, 'original_end': b, 'replacement': new,
        'original_C_source': ref(SOURCES['C'], a, b),
        'donor_sources': list(donor_refs), 'root_plan_item': plan_item,
        'root_authorization': plan_ref(plan_item),
        'root_journal_sections': [journal_ref(n) for n in journal_sections],
        'main_approved': False,
    })


def wrap_group(g, prefix, suffix):
    # Wrap the complete active body while leaving every ownership marker on its own line.
    first = re.search(r'^\\', g, re.M).start()
    last = re.search(r'^% END ', g, re.M).start()
    return g[:first] + prefix + '\n' + g[first:last] + suffix + '\n' + g[last:]


edit('E01-prouvons', 'prouvons', r'\unsure{prouvons}', 1, [1],
     [literal_ref(SOURCES['B'], r'\unsure{prouvons}')])
opening = group_text('B', 'B023-G01').replace(
    '% Qualification: a is primary; character versus point-shaped mark remains unresolved.\n',
    '% Qualification: a is primary; character versus point-shaped mark remains unresolved.\n'
    '% Local trace scope: role, hand, attachment and surface origin undetermined.\n')
edit('E02-opening-a', " a $\\overline V", '\n' + opening + r'$\overline V', 1, [2],
     [group_ref('B', 'B023-G01')])

donor_a = r'\fill (1040,608) -- (1046,604) -- (1051,608) -- (1049,613) -- (1042,613) -- cycle;'
on_phrase = r'''% BEGIN GROUP R023-ON
% Root-composed whole on a phrase; parent C023-G04 origin (943,550), units .18pt, baseline (0,65).
% Child anchor (0,65), base west, inner sep=0, outer sep=0; rectangle (0,0)--(125,80), baseline (0,65).
% Complete phrase states: on a | on [point-shaped mark]. The local alternative concerns only the final a shape.
% Declared copied-coordinate correspondence from root: (1040,608),(1046,604),(1051,608),(1049,613),(1042,613)
% under shift (-943,-550) to (97,58),(103,54),(108,58),(106,63),(99,63); no metric validation.
\node[anchor=base west,inner sep=0,outer sep=0] at (0,65) {\unsure{\begin{tikzpicture}[x=.18pt,y=-.18pt,baseline={(0,65)}]
\path[use as bounding box] (0,0) rectangle (125,80);
\node[overlay,anchor=base west,inner sep=0,outer sep=0] at (0,0) {\phantom{on a\textbar on [point-shaped mark]}};
% label R023-ON-L01: the visible on occurs once inside the whole-phrase qualification.
\node[anchor=base west,inner sep=0,outer sep=0] at (0,65) {on};
\begin{scope}[shift={(-943,-550)}]
% path R023-ON-P01: selected final a shape; exact donor B023-G04.p1, with local role/hand/origin undetermined.
''' + donor_a + r'''
\end{scope}
\end{tikzpicture}}};
% END GROUP R023-ON'''
edit('E03-whole-on-a', r'\node[anchor=base west,inner sep=0,outer sep=0] at (0,65) {on a};',
     on_phrase, 3, [7], [group_ref('B', 'B023-G04'), literal_ref(SOURCES['B'], donor_a)], within='C023-G04')

display_e = wrap_group(group_text('B', 'B023-G05'), r'\text{%', '}')
edit('E04-display-E', '\\[\nE_\\beta', '\\[\n' + display_e, 4, [8], [group_ref('B', 'B023-G05')])
edit('E05-ce-qui-prouvera', r'ce qui \unsure{prouvera}', r'\unsure{ce qui|qui} \unsure{prouvera|prouve}', 5, [10],
     [literal_ref(SOURCES['A'], r'\unsure{qui|ce qui} \unsure{prouvera|prouve}'),
      literal_ref(SOURCES['B'], r'\unsure{ce|} qui \unsure{prouvera|prouve}')])
edit('E06-tels', r'\unsure{tels}', 'tels', 6, [14], [literal_ref(SOURCES['B'], 'tels que')])

def margin_group(gid):
    g = original_groups['B'][gid]
    a = texts['B'].rfind(r'\reversemarginpar\margin{%', 0, g['start'])
    b = texts['B'].index('}\\normalmarginpar', g['end']) + len('}\\normalmarginpar')
    return texts['B'][a:b], ref(SOURCES['B'], a, b)

m02, m02ref = margin_group('B023-M02')
edit('E07-lemma-point', '', m02 + '\n', 6, [16], [m02ref], insertion_at=texts['C'].index('\\[\n\\alpha\n'))
edit('E08-S06', group_text('C', 'C023-G09'), wrap_group(group_text('B', 'B023-S06'), r'\text{%', '}'),
     7, [18], [group_ref('B', 'B023-S06')])
edit('E09-verb-order', r'\unsure{précise|precise|provient|précise le|precise le}',
     r'\unsure{precise|précise|provient|precise le|précise le}', 9, [22],
     [literal_ref(SOURCES['B'], r'\unsure{precise|précise|provient|precise le|précise le}')])
edit('E10-du-comment', '% Owns exactly du/des/sens and the far-right point pair M04; no preceding verb is included.',
     '% Owns exactly firm du and the far-right point pair M04; no preceding verb is included.\n'
     '% Each point retains its separate unresolved role, hand, attachment and surface-origin scope.',
     9, [22], within='C023-G13')
edit('E11-du', r'\unsure{du|des|sens}', 'du', 9, [22], within='C023-G13')
m04, m04ref = margin_group('B023-M04')
edit('E12-corollary-oblique', '', m04 + '\n\n', 9, [23], [m04ref],
     insertion_at=texts['C'].index(r'\uline{Corollaire}'))

family = group_text('B', 'B023-G08')
family = re.sub(r'^% Complete reading:.*\n',
    lambda _: '% Complete reading: (Sigma_i^alpha)_(alpha in K) | (Sigma_i^alpha)_(alpha in I) | (Sigma_i^alpha)_(alpha in deleted(I)K) | (Sigma_i^alpha)_(alpha in deleted(K)I); primary K.\n', family, count=1, flags=re.M)
family = re.sub(r'^% Qualification:.*\n',
    lambda _: '% Qualification: Detached head role remains local. Four whole family-index states remain unresolved; closing parenthesis and external alpha share their junction.\n'
    '% Local i-hook/dot candidates: i-like hook with its point | foot retrace accompanied by an independent point.\n'
    '% The one point has separately undetermined role, hand, attachment and surface origin; the whole-family qualification preserves that scope.\n', family, count=1, flags=re.M)
family_old_annotation = r'$\phantom{(\Sigma_i^\alpha)_{\alpha\in\unsure{K|\deleted{I}K|I}},}$'
family_new_annotation = r'$\phantom{(\Sigma_i^\alpha)_{\alpha\in K},\mid(\Sigma_i^\alpha)_{\alpha\in I},\mid(\Sigma_i^\alpha)_{\alpha\in\deleted{I}K},\mid(\Sigma_i^\alpha)_{\alpha\in\deleted{K}I},}$'
assert family.count(family_old_annotation) == 1
family = family.replace(family_old_annotation, family_new_annotation)
family = family.replace('% PATH B023-G08.p4: one i-dot, not repeated in a separate i node.',
                        '% PATH B023-G08.p4: one point; i attachment or independent-point role, hand and surface origin remain locally undetermined.')
family = wrap_group(family, r'$\text{%', '}$')
edit('E13-family', group_text('C', 'C023-G14'), family, 10, [25],
     [group_ref('B', 'B023-G08'), group_ref('C', 'C023-G14')])

c15 = original_groups['C']['C023-G15']
rule_start = texts['C'].index('% path C023-G15-P01:', c15['start'])
rule_end = texts['C'].index('% label C023-G15-L01:', rule_start)
rule = group_text('B', 'B023-G10')
rule = rule.replace('% Complete reading: left vertical emphasis rule beside both lines of the corollary; six separately drawn runs retain the pale interruptions.\n',
    '% Complete reading: left vertical emphasis rule beside both lines of the corollary; six separately drawn runs retain the pale interruptions.\n'
    '% Selected parent C023-G15 supplies x=.22pt,y=-.22pt, origin (0,0), baseline (245,2140).\n'
    '% Every B023-G10 full-scan coordinate command is copied unchanged; donor B023-G11 units .25pt are preserved in provenance.\n')
edit('E14-corollary-rule', texts['C'][rule_start:rule_end], rule, 11, [29], [group_ref('B', 'B023-G10')])
edit('E15-S10-state-comment', "% Primary Sigma_alpha^+ remains; each small point's attachment/retrace/independent role remains qualified.",
     '% Complete states: Sigma_alpha^+ with both points | Sigma_(deleted i then alpha)^+ with the upper point retained.\n'
     '% Both literal points remain once in either state; predecessor/cancellation chronology remains unresolved.\n'
     "% Alpha upper-left point and plus upper-right point each retain separate attachment/retrace/independent-role, hand and surface-origin scopes.\n"
     '% Extra-run hand/origin scope below follows root plan item 12 and its frozen scope authorization; donor D34 keeps its own point-specific hand scope in provenance.\n'
     '% The short extra plus run separately retains retrace/unassigned-run role and undetermined local hand/origin; the main glyph remains in his hand.',
     12, [27], [group_ref('B', 'B023-S10')], within='C023-G18')
edit('E16-S10-state-annotation', r'\phantom{$\Sigma_\alpha^+$}',
     r'\phantom{$\Sigma_\alpha^+\mid\Sigma_{\deleted{i}\alpha}^+$}', 12, [27],
     [group_ref('B', 'B023-S10')], within='C023-G18')
edit('E17-final-comparison', r'\geq', r'\geqslant', 13, [31], [literal_ref(SOURCES['A'], r'\geqslant')])

# All replacements refer to the unchanged C scaffold, so no edit silently
# changes another edit's match or donor identity.
edits.sort(key=lambda e: e['original_start'])
cursor = 0
parts = []
partition = []
selected_len = 0
for e in edits:
    a, b = e['original_start'], e['original_end']
    assert a >= cursor, ('overlapping edits', e['edit_id'])
    unchanged = texts['C'][cursor:a]
    if unchanged:
        parts.append(unchanged)
        partition.append({'kind': 'unchanged_C', 'source_start': cursor, 'source_end': a,
                          'selected_start': selected_len, 'selected_end': selected_len + len(unchanged)})
        selected_len += len(unchanged)
    e['selected_start'] = selected_len
    parts.append(e['replacement'])
    selected_len += len(e['replacement'])
    e['selected_end'] = selected_len
    partition.append({'kind': 'root_authorized_edit', 'edit_id': e['edit_id'],
                      'source_start': a, 'source_end': b,
                      'selected_start': e['selected_start'], 'selected_end': e['selected_end']})
    cursor = b
tail = texts['C'][cursor:]
parts.append(tail)
partition.append({'kind': 'unchanged_C', 'source_start': cursor, 'source_end': len(texts['C']),
                  'selected_start': selected_len, 'selected_end': selected_len + len(tail)})
selected = ''.join(parts)
cache[DRAFT] = selected
sgroups = groups(selected)
gby = {g['id']: g for g in sgroups}


def transform_span(a, b):
    """Exact ordered coverage under the declared textual replacements."""
    covered = []
    for p in partition:
        sa, sb = p['source_start'], p['source_end']
        if sa == sb:
            if a <= sa < b:
                covered.append((p['selected_start'], p['selected_end']))
        elif max(a, sa) < min(b, sb):
            if p['kind'] == 'unchanged_C':
                covered.append((p['selected_start'] + max(a, sa) - sa,
                                p['selected_start'] + min(b, sb) - sa))
            else:
                covered.append((p['selected_start'], p['selected_end']))
    return covered


def closest_group(pos):
    candidates = [g for g in sgroups if g['start'] <= pos < g['end']]
    return min(candidates, key=lambda g: g['end'] - g['start'])['id'] if candidates else None


def unescaped(text, at):
    n = 0
    while at > 0 and text[at - 1] == '\\':
        n += 1
        at -= 1
    return n % 2 == 0


def comments_mask(text):
    chars = list(text)
    for m in re.finditer('%', text):
        if unescaped(text, m.start()):
            end = text.find('\n', m.start())
            end = len(text) if end < 0 else end
            chars[m.start():end] = ' ' * (end - m.start())
    return ''.join(chars)


masked = comments_mask(selected)


def balanced_end(text, pos, opening='{', closing='}'):
    assert text[pos] == opening
    depth = 1
    j = pos + 1
    while j < len(text):
        if unescaped(text, j):
            if text[j] == opening:
                depth += 1
            elif text[j] == closing:
                depth -= 1
                if depth == 0:
                    return j + 1
        j += 1
    raise AssertionError(('unclosed delimiter', pos, opening))


def command_end(pos):
    depth = 0
    j = pos
    while j < len(masked):
        if unescaped(masked, j):
            if masked[j] == '{':
                depth += 1
            elif masked[j] == '}':
                depth -= 1
            elif masked[j] == ';' and depth == 0:
                return j + 1
        j += 1
    raise AssertionError(('unterminated drawing command', pos))


def donor_group_ids(gid):
    if gid == 'R023-ON':
        return ['C023-G04', 'B023-G04']
    if gid in source_group_meta:
        return [gid]
    return []


def donor_matches(literal, gid):
    matches = []
    for dg in donor_group_ids(gid):
        rd = dg[0]
        source_g = original_groups[rd][dg]
        pos = texts[rd].find(literal, source_g['start'], source_g['end'])
        while pos != -1:
            matches.append({'donor_group': dg, 'source': ref(SOURCES[rd], pos, pos + len(literal))})
            pos = texts[rd].find(literal, pos + 1, source_g['end'])
    return matches


commands = []
for m in re.finditer(r'\\(draw|fill|path|node|coordinate)\b', masked):
    start = m.start()
    end = command_end(start)
    gid = closest_group(start)
    c = {'command_id': f'R023-CMD{len(commands) + 1:03d}', 'command': m.group(1),
         'selected_group_id': gid, 'selected_source': ref(DRAFT, start, end),
         'main_approved': False}
    content = selected[start:end]
    c['donor_exact_matches'] = donor_matches(content, gid)
    markers = list(re.finditer(r'^% (path|PATH|label|WORDS) ([^:]+):([^\n]*)', selected[:start], re.M))
    if markers and closest_group(markers[-1].start()) == gid:
        marker = markers[-1]
        c['nearest_ownership_marker'] = {'kind': marker.group(1), 'id': marker.group(2),
                                         'description': marker.group(3).strip(),
                                         'source': ref(DRAFT, marker.start(), marker.end())}
    else:
        c['nearest_ownership_marker'] = None
    if c['command'] in ('draw', 'fill'):
        marker = c['nearest_ownership_marker']
        assert marker and marker['kind'].lower() == 'path', ('unowned physical path', c['command_id'])
        c['physical_owner_id'] = marker['id']
        c['physical_ownership'] = 'sole owner; containing nodes/groups add no second physical instance'
        assert c['donor_exact_matches'], ('changed drawing command', c['command_id'])
    elif c['command'] == 'node':
        c['node_id'] = f'{gid}-N{sum(x["command"] == "node" and x["selected_group_id"] == gid for x in commands) + 1:02d}'
        c['node_role'] = ('invisible_state_annotation' if 'overlay' in content.split(' at ', 1)[0]
                          else 'containing_node' if r'\begin{tikzpicture}' in content else 'visible_word_or_formula_label')
        c['label_owner_id'] = (c['nearest_ownership_marker']['id'] if c['nearest_ownership_marker'] and c['nearest_ownership_marker']['kind'].lower() in ('label', 'words') else c['node_id'])
    else:
        c['structural_role'] = 'bounding_rectangle' if 'use as bounding box' in content else 'baseline_coordinate'
    c['root_edit_ids'] = [e['edit_id'] for e in edits if max(start, e['selected_start']) < min(end, e['selected_end'])]
    commands.append(c)


# Source contexts are literal declarations, never calculated point locations.
envs = []
stack = []
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}', masked):
    action, name = m.group(1, 2)
    if action == 'begin':
        e = {'environment': name, 'start': m.start(), 'open_end': m.end(),
             'parent_start': stack[-1]['start'] if stack else None}
        stack.append(e)
    else:
        assert stack and stack[-1]['environment'] == name, ('environment mismatch', name, m.start())
        e = stack.pop()
        e.update(end=m.end(), close_start=m.start())
        envs.append(e)
assert not stack
envs.sort(key=lambda e: e['start'])
contexts = []
for e in envs:
    if e['environment'] not in ('tikzpicture', 'scope'):
        continue
    pos = e['open_end']
    while pos < len(masked) and masked[pos].isspace():
        pos += 1
    decl_end = balanced_end(masked, pos, '[', ']') if masked[pos:pos+1] == '[' else e['open_end']
    decl = selected[e['start']:decl_end]
    parent = next((x for x in reversed(contexts) if x['start'] < e['start'] < x['end']), None)
    enclosing_nodes = [c for c in commands if c['command'] == 'node' and c['selected_source']['char_start_zero_based'] < e['start'] < c['selected_source']['char_end_exclusive']]
    node = min(enclosing_nodes, key=lambda c: c['selected_source']['char_end_exclusive'] - c['selected_source']['char_start_zero_based']) if enclosing_nodes else None
    ctx = {'context_id': f'R023-CTX{len(contexts) + 1:02d}', 'kind': e['environment'],
           'start': e['start'], 'end': e['end'], 'selected_group_id': closest_group(e['start']),
           'parent_context_id': parent['context_id'] if parent else None,
           'selected_source': ref(DRAFT, e['start'], e['end']),
           'literal_declaration': ref(DRAFT, e['start'], decl_end),
           'enclosing_node_id': node.get('node_id') if node else None,
           'anchor_and_placement_prefix': node['selected_source']['literal'].split('{', 1)[0] if node else None,
           'no_metric_validation': True, 'main_approved': False}
    for key in ('x', 'y'):
        found = re.search(rf'(?:\[|,){key}=([^,\]]+)', decl)
        ctx[key + '_unit_literal'] = found.group(1) if found else None
    base = re.search(r'baseline=(\{\([^{}]*\)\}|\([^)]*\))', decl)
    ctx['baseline_literal'] = base.group(1) if base else None
    shift = re.search(r'shift=(\{[^{}]*\})', decl)
    ctx['shift_literal'] = shift.group(1) if shift else None
    ctx['donor_exact_declaration_matches'] = donor_matches(decl, ctx['selected_group_id'])
    contexts.append(ctx)


def command_context(c):
    pos = c['selected_source']['char_start_zero_based']
    hit = [x for x in contexts if x['start'] <= pos < x['end']]
    return min(hit, key=lambda x: x['end'] - x['start']) if hit else None


for c in commands:
    ctx = command_context(c)
    c['context_id'] = ctx['context_id'] if ctx else None
    c['nested_command_ids'] = [x['command_id'] for x in commands if x != c and
                               c['selected_source']['char_start_zero_based'] < x['selected_source']['char_start_zero_based'] and
                               x['selected_source']['char_end_exclusive'] < c['selected_source']['char_end_exclusive']]


selected_groups = []
for g in sgroups:
    gid = g['id']
    donor_refs = [group_ref(dg[0], dg) for dg in donor_group_ids(gid)]
    direct = [c for c in commands if c['selected_group_id'] == gid]
    contained = [c for c in commands if g['start'] <= c['selected_source']['char_start_zero_based'] < g['end']]
    declarations = [ref(DRAFT, m.start(), m.end()) for m in re.finditer(r'^%[^\n]*', selected, re.M)
                    if g['start'] < m.start() < g['end'] and closest_group(m.start()) == gid]
    entry_ctx = [x for x in contexts if x['start'] < g['start'] < x['end']]
    entry_ctx = min(entry_ctx, key=lambda x: x['end'] - x['start']) if entry_ctx else None
    selected_groups.append({
        'group_id': gid, 'id': gid, 'parent_group': g['parent_group'],
        'selected_source': ref(DRAFT, g['start'], g['end']),
        'complete_exact_source': selected[g['start']:g['end']],
        'donor_complete_sources': donor_refs,
        'donor_map_records': [source_group_meta[dg] for dg in donor_group_ids(gid) if dg in source_group_meta],
        'direct_command_ids': [c['command_id'] for c in direct],
        'contained_command_ids': [c['command_id'] for c in contained],
        'child_group_ids': [x['id'] for x in sgroups if x['parent_group'] == gid],
        'source_declaration_spans': declarations,
        'entry_parent_context_id': entry_ctx['context_id'] if entry_ctx else None,
        'context_ids': [x['context_id'] for x in contexts if x['selected_group_id'] == gid],
        'root_edit_ids': [e['edit_id'] for e in edits if max(g['start'], e['selected_start']) < min(g['end'], e['selected_end'])],
        'physical_ownership': 'leaf draw/fill commands own their strokes once; containing group coverage is reciprocal reference',
        'main_approved': False,
    })


def boundary(pos):
    data = selected.encode('utf-8')
    offset = len(selected[:pos].encode('utf-8'))
    return {'char_offset_zero_based': pos, 'utf8_byte_offset': offset,
            'preceding_last_byte_hex': data[offset-1:offset].hex() or None,
            'following_first_byte_hex': data[offset:offset+1].hex() or None,
            'preceding_last_character': selected[pos-1:pos] or None,
            'following_first_character': selected[pos:pos+1] or None,
            'literal_before': selected[max(0,pos-70):pos],
            'literal_after': selected[pos:pos+70]}


for e in edits:
    e['selected_source'] = ref(DRAFT, e['selected_start'], e['selected_end'])
    e['splice_boundaries'] = {'left': boundary(e['selected_start']), 'right': boundary(e['selected_end'])}
    e['replacement_sha256_utf8'] = sha(e['replacement'])
    e['root_ink_choice_applied'] = True
for p in partition:
    p['source'] = ref(SOURCES['C'], p['source_start'], p['source_end'])
    p['selected_source'] = ref(DRAFT, p['selected_start'], p['selected_end'])

marker_boundaries = []
for g in sgroups:
    for k in ('start', 'begin_end', 'end_start', 'end'):
        marker_boundaries.append({'group_id': g['id'], 'boundary_kind': k, **boundary(g[k])})


def chosen_group_ref(gid):
    g = gby[gid]
    return ref(DRAFT, g['start'], g['end'])


union = json.loads(read(UNION))
coverage = []
override_groups = {
    'U023-02': 'B023-G01', 'U023-09': 'R023-ON', 'U023-11': 'B023-G05',
    'U023-27': 'B023-M02', 'U023-31': 'B023-S06', 'U023-44': 'B023-M04',
    'U023-48': 'B023-G08', 'U023-49': 'B023-G08', 'U023-50': 'B023-G08',
    'U023-52': 'C023-G15', 'U023-53': 'B023-G10', 'U023-54': 'C023-G18',
    'U023-55': 'C023-G17', 'U023-56': 'C023-G17', 'U023-57': 'C023-G19',
}
for n, locus in enumerate(union['loci']):
    lid = locus['locus_id']
    if lid in override_groups:
        spans = [chosen_group_ref(override_groups[lid])]
    else:
        spans = []
        for sr in locus['readers']['C']['actual_complete_source_spans']:
            assert sr['path'] == SOURCES['C']
            assert texts['C'][sr['char_start_zero_based']:sr['char_end_exclusive']] == sr['literal']
            spans += [ref(DRAFT, a, b) for a, b in transform_span(sr['char_start_zero_based'], sr['char_end_exclusive'])]
    # Merge only immediately adjacent selected spans; the source partition remains above.
    ranges = sorted(set((s['char_start_zero_based'], s['char_end_exclusive']) for s in spans))
    merged = []
    for a, b in ranges:
        if merged and a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(b, merged[-1][1]))
        else:
            merged.append((a, b))
    spans = [ref(DRAFT, a, b) for a, b in merged]
    assert spans, ('uncovered locus', lid)
    gids = [g['id'] for g in sgroups if any(max(g['start'], s['char_start_zero_based']) < min(g['end'], s['char_end_exclusive']) for s in spans)]
    coverage.append({
        'locus_id': lid, 'key': locus['key'], 'location': locus['location'],
        'source_union_ref': {'path': UNION, 'sha256_utf8': sha(read(UNION)), 'json_pointer': f'/loci/{n}'},
        'selected_source_spans': spans, 'selected_group_ids': gids,
        'reader_complete_source_refs': {r: locus['readers'][r]['actual_complete_source_spans'] for r in 'ABC'},
        'coverage_scope': 'exact selected source coverage; physical ownership is recorded per command and inherited through containing references',
        'main_approved': False,
    })


# One necessary source structural gate: braces, environments, math/text boundaries,
# comments, tokens, source-copy ownership and exact edit coverage.
brace_stack = []
brace_pairs = {}
for i, ch in enumerate(masked):
    if ch in '{}' and unescaped(masked, i):
        if ch == '{':
            brace_stack.append(i)
        else:
            assert brace_stack, ('extra closing brace', i)
            brace_pairs[brace_stack.pop()] = i
assert not brace_stack, ('unclosed braces', brace_stack)

wrappers = []
wrapper_names = r'unsure|text|mathop|mathrel|figure|margin|deleted|inserted|phantom|rlap|rotatebox|shortstack|makebox|uline'
for m in re.finditer(r'\\(' + wrapper_names + r')\b', masked):
    pos = m.end()
    optional_arguments = []
    while True:
        while pos < len(masked) and masked[pos].isspace():
            pos += 1
        if masked[pos:pos+1] != '[':
            break
        arg_end = balanced_end(masked, pos, '[', ']')
        optional_arguments.append(ref(DRAFT, pos, arg_end))
        pos = arg_end
    arguments = []
    for unused in range(2 if m.group(1) == 'rotatebox' else 1):
        while pos < len(masked) and masked[pos].isspace():
            pos += 1
        assert masked[pos:pos+1] == '{', ('wrapper argument', m.group(1), m.start())
        arg_end = brace_pairs[pos] + 1
        arguments.append(ref(DRAFT, pos, arg_end))
        pos = arg_end
    gid = closest_group(m.start())
    wrappers.append({
        'wrapper_id': f'R023-WR{len(wrappers) + 1:03d}', 'command': m.group(1),
        'selected_group_id': gid, 'selected_source': ref(DRAFT, m.start(), pos),
        'optional_argument_spans': optional_arguments, 'argument_spans': arguments,
        'donor_exact_matches': donor_matches(selected[m.start():pos], gid),
        'intersecting_group_ids': [g['id'] for g in sgroups if max(g['start'], m.start()) < min(g['end'], pos)],
        'root_edit_ids': [e['edit_id'] for e in edits if max(m.start(), e['selected_start']) < min(pos, e['selected_end'])],
        'main_approved': False,
    })
for g in selected_groups:
    g['wrapper_ids'] = [w['wrapper_id'] for w in wrappers if g['group_id'] in w['intersecting_group_ids']]
for c in commands:
    a, b = c['selected_source']['char_start_zero_based'], c['selected_source']['char_end_exclusive']
    c['enclosing_wrapper_ids'] = [w['wrapper_id'] for w in wrappers if
                                  w['selected_source']['char_start_zero_based'] <= a and
                                  b <= w['selected_source']['char_end_exclusive']]

# Text arguments and TikZ environments create text islands inside math.  Track
# their exact source extents; each island must restore its entry mode unchanged.
island_events = {}
for m in re.finditer(r'\\text\s*\{', masked):
    op = m.end() - 1
    island_events.setdefault(op + 1, []).append(('push', 'text argument', brace_pairs[op]))
    island_events.setdefault(brace_pairs[op], []).append(('pop', 'text argument', op + 1))
for e in envs:
    if e['environment'] == 'tikzpicture':
        island_events.setdefault(e['open_end'], []).append(('push', 'tikzpicture', e['close_start']))
        island_events.setdefault(e['close_start'], []).append(('pop', 'tikzpicture', e['open_end']))
math_mode = 'text'
mode_stack = []
math_events = []
blank_lines_inside_math = []
i = 0
while i < len(masked):
    for action, kind, peer in sorted(island_events.get(i, []), key=lambda t: t[0] != 'pop'):
        if action == 'push':
            mode_stack.append((math_mode, kind, i, peer))
            math_mode = 'text'
        else:
            assert math_mode == 'text', ('math unclosed inside text island', i, kind, math_mode)
            old, expected_kind, entry, end = mode_stack.pop()
            assert expected_kind == kind and end == i
            math_mode = old
    if masked.startswith('\\[', i):
        assert math_mode == 'text', ('display open in math', i, math_mode)
        math_mode = 'display'
        math_events.append({'token': r'\[', 'at': i})
        i += 2
    elif masked.startswith('\\]', i):
        assert math_mode == 'display', ('display close outside display', i, math_mode)
        math_mode = 'text'
        math_events.append({'token': r'\]', 'at': i})
        i += 2
    elif masked[i] == '$' and unescaped(masked, i):
        assert math_mode != 'display', ('inline dollar in display without text island', i)
        math_mode = 'inline' if math_mode == 'text' else 'text'
        math_events.append({'token': '$', 'at': i})
        i += 1
    else:
        if selected.startswith('\n\n', i) and math_mode != 'text':
            blank_lines_inside_math.append(i)
        i += 1
assert math_mode == 'text' and not mode_stack, ('unclosed final math mode', math_mode, mode_stack)
assert not blank_lines_inside_math, blank_lines_inside_math
controls = set(re.findall(r'\\([A-Za-z]+)', masked))
source_controls = set().union(*(set(re.findall(r'\\([A-Za-z]+)', comments_mask(t))) for t in texts.values()))
assert not (controls - source_controls), ('unexpected command token', controls - source_controls)
assert len(coverage) == 62
assert all(c['donor_exact_matches'] for c in commands if c['command'] in ('draw', 'fill'))
assert selected.count(donor_a) == 1
assert len([c for c in commands if c['selected_group_id'] == 'B023-G10' and c['command'] == 'draw']) == 6
assert len([c for c in commands if c['selected_group_id'] == 'B023-G10' and c['command'] == 'fill']) == 1
assert len([c for c in commands if c['selected_group_id'] == 'C023-G18' and c['command'] == 'fill']) == 2
assert len([c for c in commands if c['selected_group_id'] == 'B023-G08' and c['command'] == 'fill']) == 1
assert selected.count('\\node[anchor=base west,inner sep=0,outer sep=0] at (0,65) {on};') == 1
assert r'\node[anchor=base west,inner sep=0,outer sep=0] at (0,65) {on a};' not in selected
assert ''.join(p['selected_source']['literal'] for p in partition) == selected
assert not re.search(r'% END[^\n]*% BEGIN', selected)

layout_correspondence = {
    'R023-ON': {
        'root_authorization': plan_ref(3), 'selected_parent_group': 'C023-G04',
        'selected_parent_origin': '(943,550)', 'selected_parent_units': 'x=.18pt,y=-.18pt',
        'selected_parent_baseline': '(0,65)', 'selected_parent_rectangle': '(0,0)--(190,80)',
        'child_node_anchor': '(0,65); base west, inner sep=0, outer sep=0',
        'child_units': 'x=.18pt,y=-.18pt', 'child_baseline': '(0,65)',
        'child_rectangle': '(0,0)--(125,80)', 'donor_parent_origin': '(1036,553)',
        'donor_parent_shift': '(-1036,-553)', 'donor_parent_units': 'x=.20pt,y=-.20pt',
        'donor_parent_baseline': '(B023G04base) at (0,67)',
        'selected_shift': '(-943,-550)',
        'copied_full_scan_vertices': '(1040,608),(1046,604),(1051,608),(1049,613),(1042,613)',
        'root_declared_child_vertices': '(97,58),(103,54),(108,58),(106,63),(99,63)',
        'correspondence_source': 'Both coordinate descriptions copied from root item 3; no coordinate arithmetic performed.',
        'sole_literal_shape_owner': 'R023-ON-P01', 'donor_shape_owner': 'B023-G04.p1',
        'separate_ochre_owner': 'C023-G04-P01', 'no_metric_validation': True,
    },
    'B023-G10': {
        'root_authorization': plan_ref(11), 'selected_parent_group': 'C023-G15',
        'selected_parent_declaration': r'\begin{tikzpicture}[x=.22pt,y=-.22pt,baseline={(245,2140)}]',
        'selected_parent_origin': '(0,0)', 'selected_parent_rectangle': '(245,1905)--(1650,2145)',
        'donor_parent_group': 'B023-G11', 'donor_parent_units': 'x=.25pt,y=-.25pt',
        'donor_parent_baseline': '(B023G11base) at (0,252)',
        'donor_parent_scope_shift': '(-244,-1888)',
        'copied_coordinate_correspondence': 'All six draw commands and one fill command retain every donor full-scan coordinate token unchanged. They execute in the selected C parent; the B negative-origin scope is absent from the selected child.',
        'donor_complete_parent_source': group_ref('B', 'B023-G11'),
        'selected_complete_parent_source': chosen_group_ref('C023-G15'),
        'no_metric_validation': True,
    },
}

local_scopes = [
    {'scope_id': 'R023-OPENING-MARK', 'group_id': 'B023-G01', 'path_ids': ['B023-G01.p1'], 'role_hand_attachment_origin': 'undetermined; a primary, point-shaped mark alternative', 'root_journal': journal_ref(2)},
    {'scope_id': 'R023-ON-FINAL-MARK', 'group_id': 'R023-ON', 'path_ids': ['R023-ON-P01'], 'role_hand_attachment_origin': 'undetermined for the final a/point-shaped form within the whole phrase qualification', 'root_journal': journal_ref(7)},
    {'scope_id': 'R023-OCHRE', 'group_id': 'C023-G04', 'path_ids': ['C023-G04-P01'], 'role_hand_attachment_origin': 'undetermined independently of R023-ON', 'root_journal': journal_ref(7)},
    {'scope_id': 'R023-S07-POINT', 'group_id': 'C023-G10', 'path_ids': ['C023-G10-P05'], 'role_hand_attachment_origin': 'undetermined; alpha terminal point or independent point; main glyph his hand', 'root_journal': journal_ref(19)},
    {'scope_id': 'R023-RIGHT-UPPER-POINT', 'group_id': 'C023-G13', 'path_ids': ['C023-G13-P01'], 'role_hand_attachment_origin': 'undetermined independently of the lower point and firm du', 'root_journal': journal_ref(22)},
    {'scope_id': 'R023-RIGHT-LOWER-POINT', 'group_id': 'C023-G13', 'path_ids': ['C023-G13-P02'], 'role_hand_attachment_origin': 'undetermined independently of the upper point and firm du', 'root_journal': journal_ref(22)},
    {'scope_id': 'R023-FAMILY-POINT', 'group_id': 'B023-G08', 'path_ids': ['B023-G08.p3', 'B023-G08.p4'], 'role_hand_attachment_origin': 'i-hook/dot versus foot-retrace/independent-point locally unresolved; point hand and surface origin undetermined', 'root_journal': journal_ref(25)},
    {'scope_id': 'R023-S10-INDEX-POINT', 'group_id': 'C023-G18', 'path_ids': ['C023-G18-P03'], 'role_hand_attachment_origin': 'separately undetermined; alpha retrace, predecessor-i point, or independent trace; chronology unresolved', 'root_journal': journal_ref(27)},
    {'scope_id': 'R023-S10-PLUS-POINT', 'group_id': 'C023-G18', 'path_ids': ['C023-G18-P06'], 'role_hand_attachment_origin': 'separately undetermined; plus retrace or independent point', 'root_journal': journal_ref(27)},
    {'scope_id': 'R023-S10-EXTRA-RUN', 'group_id': 'C023-G18', 'path_ids': ['C023-G18-P05'],
     'role_hand_attachment_origin': 'local retrace/unassigned-run role and local hand/origin undetermined; main glyph remains in his hand',
     'authority_kind': 'root_selected_scope_under_plan_item_12', 'root_scope_authorization': ref(SCOPE),
     'donor_scope_preserved_separately': {
         'trace_hand_verbatim': 'undetermined hand for the separately qualified point(s); main text is his hand',
         'extra_run_part_verbatim': {'location': 'plus additional short cross-run', 'reading': 'visible upper run above main cross',
                                    'alternatives': ['retrace role', 'unassigned additional run'], 'confidence': 'high'},
         'extra_run_specific_hand_field': None,
         'source_ref': {'path': 'out/readers/023/C/report.json',
                        'sha256_utf8': '33c52723717a13e1be429eda330baf6e617f89e0ae762d6260d65975136f0401',
                        'json_pointer': '/differences/33', 'char_start_zero_based': 35335, 'char_end_exclusive': 37287,
                        'utf8_byte_start': 35350, 'utf8_byte_end_exclusive': 37303,
                        'line_start_one_based': 1000, 'line_end_one_based': 1057}},
     'root_journal': journal_ref(27)},
    {'scope_id': 'R023-FINAL-CUP-CROSS', 'group_id': 'C023-G17', 'path_ids': ['C023-G17-P06'], 'role_hand_attachment_origin': 'presence resolved; operation/attachment role unresolved', 'root_journal': journal_ref(28)},
]
for row in local_scopes:
    row['selected_command_ids'] = [c['command_id'] for c in commands if c.get('physical_owner_id') in row['path_ids']]
    row['selected_source_spans'] = [c['selected_source'] for c in commands if c.get('physical_owner_id') in row['path_ids']]
    row['main_approved'] = False

audit = {
    'scan': '023', 'source_only': True, 'main_adjudicated': False, 'main_approved': False,
    'draft_path': DRAFT, 'draft_sha256_utf8': sha(selected),
    'journal_sha256_utf8': sha(read(JOURNAL)), 'plan_sha256_utf8': sha(read(PLAN)),
    'root_scope_authorization_sha256_utf8': sha(read(SCOPE)),
    'necessary_gate': {
        'balanced_braces': True, 'balanced_environments': True, 'balanced_math_and_text_islands': True,
        'physical_paragraph_blanks_outside_math': True, 'command_tokens_grounded_in_frozen_sources': True,
        'comment_and_group_marker_line_boundaries': True, 'complete_source_partition': True,
        'all_leaf_draw_fill_commands_exactly_copied_from_named_donors': True,
        'all_62_loci_have_selected_source_coverage': True,
        'on_phrase_has_one_visible_on_and_one_donor_shape': True,
        'corollary_rule_has_six_draw_runs_one_fill_bead': True,
        'S10_two_points_once': True, 'family_one_point_once': True,
    },
    'counts': {'edits': len(edits), 'groups': len(sgroups), 'commands': len(commands),
               'draw_fill_commands': sum(c['command'] in ('draw', 'fill') for c in commands),
               'named_physical_path_owners': len({c['physical_owner_id'] for c in commands if c.get('physical_owner_id')}),
               'nodes': sum(c['command'] == 'node' for c in commands),
               'contexts': len(contexts), 'wrappers': len(wrappers), 'source_union_loci': len(coverage)},
    'scope_limit': 'One necessary source-only structural gate. No compilation, rendering, image access, image metadata, OCR, mathematical check, metric validation or coordinate calculation.',
    'concrete_remaining_issues': [],
}

result = {
    'schema': 'scan023-root-selected-exact-source-map-v1', 'scan': '023',
    'source_only': True, 'main_adjudicated': False, 'main_approved': False,
    'draft_path': DRAFT, 'draft_file': 'checks/scan023_final_draft.tex',
    'draft_sha256_utf8': sha(selected), 'final_draft_sha256': sha(selected),
    'file_sha256': sha(selected), 'span_convention': 'zero-based characters and UTF-8 bytes, end exclusive; one-based inclusive lines',
    'authority': {'brief': ref(BRIEF), 'assembly_plan': ref(PLAN), 'root_journal': ref(JOURNAL),
                  'root_scope_authorization': ref(SCOPE)},
    'frozen_source_files': {r: ref(p, literal=False) for r, p in SOURCES.items()},
    'frozen_map_files': {r: ref(f'out/readers/023/{r}/source_map.json', literal=False) for r in 'BC'},
    'source_union': ref(UNION, literal=False),
    'selected_groups': selected_groups, 'groups': selected_groups,
    'exact_command_ownership': commands, 'layout_contexts': contexts, 'exact_wrapper_ownership': wrappers,
    'declared_import_correspondences': layout_correspondence,
    'separate_local_qualification_scopes': local_scopes,
    'literal_replacements': edits, 'complete_selected_source_partition': partition,
    'group_marker_boundaries': marker_boundaries,
    'source_locus_coverage': coverage,
    'source_gate': audit,
    'limits': 'Manual drawing donors remain manual source approximations. Source assembly makes no rendered, metric, mathematical, count, ink or approval decision.',
}

(ROOT / DRAFT).write_bytes(selected.encode('utf-8'))
(ROOT / MAP).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
audit['source_map_path'] = MAP
audit['source_map_sha256_utf8'] = hashlib.sha256((ROOT / MAP).read_bytes()).hexdigest()
audit_path = OUT / 'scan023_source_assembly_gate.json'
audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'draft_path': DRAFT, 'draft_sha256_utf8': sha(selected),
                  'map_path': MAP, 'map_sha256_utf8': audit['source_map_sha256_utf8'],
                  'gate_path': str(audit_path.relative_to(ROOT)),
                  'gate_sha256_utf8': hashlib.sha256(audit_path.read_bytes()).hexdigest(),
                  'counts': audit['counts'], 'concrete_remaining_issues': []}, indent=2))
