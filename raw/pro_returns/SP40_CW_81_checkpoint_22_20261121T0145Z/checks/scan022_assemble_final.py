"""Root-directed scan022 source assembly; literal operations only.

Reader files and the released candidate bank remain immutable. Drawing numbers
are copied from selected source or the root journal. No geometry is evaluated.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path('/workspace/scratch/94548b74fbe0')
BANK_PATH = ROOT / 'out/checks/scan022_candidate_sources.json'
BANK_SHA = 'b62665bf7b4a38af2483819782b88aab6de247074d64d53333a4c717c39eae38'
DRAFT_PATH = ROOT / 'out/checks/scan022_final_draft.tex'
MAP_PATH = ROOT / 'out/checks/scan022_final_source_map.json'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def rel(path):
    return str(path.relative_to(ROOT))


assert sha(BANK_PATH.read_bytes()) == BANK_SHA
bank = json.loads(BANK_PATH.read_text())
base_path = ROOT / 'out/readers/022/A/reading.tex'
base = base_path.read_text()
assert sha(base.encode()) == bank['source_files']['A']['reading.tex']['root_released_sha256']
journal_path = ROOT / 'out/checks/scan022_source_support_journal_phase_009.md'
journal = journal_path.read_text()
assert sha(journal.encode()) == 'ff49b9f3a2054a51287c3e41878cfcac616aef22d554178235dce4c23ec92fe7'
count_authorization_path = ROOT / 'out/checks/scan022_root_count_authorization.json'
assert sha(count_authorization_path.read_bytes()) == '8e5bd8cf8567cf99309f892c76d9c3b3f838df7e07ad11960b4054ddc920f279'
count_authorization = json.loads(count_authorization_path.read_text())
journal_sections = {}
section_matches = list(re.finditer(r'^## (\d+) — ', journal, re.M))
for index, match in enumerate(section_matches):
    end = section_matches[index + 1].start() if index + 1 < len(section_matches) else len(journal)
    journal_sections[int(match.group(1))] = journal[match.start():end]
assert all(section in journal_sections for section in range(1, 16))


def pointer(reference):
    value = bank
    for part in reference.split('/')[1:]:
        value = value[part]
    return value


def group(reader, identity):
    return bank['readers'][reader]['groups'][identity]


def node(reader, identity):
    matches = [n for n in bank['readers'][reader]['nodes'].values() if n.get('original_reader_node_id') == identity]
    assert len(matches) == 1
    return matches[0]


def span_ref(span):
    return {k: v for k, v in span.items() if k != 'literal_source'}


operations = []


def add_operation(identity, start, end, replacement, section, selected_sources, edits=None, note=''):
    assert start <= end
    operations.append({
        'id': identity, 'base_start_char': start, 'base_end_char_exclusive': end,
        'replacement': replacement, 'root_journal_section': section,
        'root_journal_literal': journal_sections[section],
        'selected_sources': selected_sources, 'literal_edits': edits or [],
        'note': note, 'main_approved': False,
    })


def change_text(identity, old, changes, section, donor=None):
    new = old
    edits = []
    for before, after in changes:
        occurrences = new.count(before)
        assert occurrences > 0, (identity, before)
        new = new.replace(before, after)
        edits.append({'old': before, 'new': after, 'literal_occurrences': occurrences})
    return new, edits


def change_a_node(identity, changes, section, donor=None):
    original = node('A', identity)['source_span']
    replacement, edits = change_text(identity, original['literal_source'], changes, section)
    sources = [{'bank_pointer': f'/readers/A/nodes/{node("A", identity)["id"]}', 'span': span_ref(original)}]
    if donor:
        sources.append(donor)
    add_operation('word-' + identity, original['start_char'], original['end_char_exclusive'], replacement, section, sources, edits)


def imported_group(reader, identity):
    original = group(reader, identity)['marker_span']
    new = original['literal_source']
    edits = []
    unit_pairs = [('x=0.0088cm', 'x=0.085mm'), ('y=-0.0088cm', 'y=-0.085mm')] if reader == 'B' else [('x=0.008cm', 'x=0.085mm'), ('y=-0.008cm', 'y=-0.085mm')]
    for before, after in unit_pairs:
        occurrences = new.count(before)
        if occurrences:
            new = new.replace(before, after)
            edits.append({'old': before, 'new': after, 'literal_occurrences': occurrences, 'authority': 'Root assembly directive: selected x/y units 0.085mm and -0.085mm; all numeric coordinates retained.'})
    return new, edits, {'bank_pointer': f'/readers/{reader}/groups/{identity}', 'span': span_ref(original)}


def replace_a_group(a_identity, reader, identity, section, additional_changes=None):
    original = group('A', a_identity)['marker_span']
    replacement, edits, source = imported_group(reader, identity)
    if additional_changes:
        replacement, extra = change_text(identity, replacement, additional_changes, section)
        edits.extend(extra)
    add_operation('replace-' + a_identity, original['start_char'], original['end_char_exclusive'], replacement, section, [source], edits)


def insert_after_a_group(a_identity, reader, identity, section):
    at = group('A', a_identity)['marker_span']['end_char_exclusive']
    replacement, edits, source = imported_group(reader, identity)
    add_operation('insert-' + identity, at, at, replacement, section, [source], edits)


# §§01–03: the A base owns the fixed-position words; complete imports own their labels.
change_a_node('T01', [(r'\unsure{On|Un}', r'\unsure{Un|On}')], 1)
change_a_node('T02', [(r'proc\unsure{è|é|e}de', r'\unsure{procède|procéde|procédé|procede}')], 1)
insert_after_a_group('A022-G01-opening-cancellations', 'B', 'B022-M01', 1)
replace_a_group('A022-G03-initial-union', 'B', 'B022-G02', 1)

opener, opener_edits, opener_source = imported_group('B', 'B022-G03')
opener, more = change_text('B022-G03', opener, [
    (r'{\unsure{%', r'{%'),
    ('}};\n% END B022-G03', '};\n% END B022-G03'),
    (r'\phantom{$\unsure{(}\alpha\in K$}', r'\phantom{$(\alpha\in K$}'),
    ('% Role/state: C022-R01 retained: parenthesis primary; attachment as a left lead into alpha remains possible.', '% Role/state: Root §02 resolves the opening curve as a parenthesis; its adjoining alpha-in-K remains owned here.'),
    (r'% Complete reading/state candidates: (\alpha\in K | \alpha\in K with the same visible left lead', r'% Root selected reading: (\alpha\in K'),
], 2)
opener_edits.extend(more)
closers, closer_edits, closer_source = imported_group('B', 'B022-G04')
closers, more = change_text('B022-G04', closers, [
    (r'\phantom{$\unsure{)|)\,)}$}', r'\phantom{\unsure{one spanning )|two separate ) )}}'),
    ('% Complete reading/state candidates: ) | ) )', '% Root complete reading/state candidates: one spanning ) | two separate ) )'),
], 2)
closer_edits.extend(more)
old = group('A', 'A022-G04-alpha-parentheses')['marker_span']
add_operation('replace-parenthetical-components', old['start_char'], old['end_char_exclusive'], opener + closers, 2, [opener_source, closer_source], opener_edits + closer_edits)
change_a_node('T11', [(r'\unsure{etant|étant} \unsure{disjoints|disjointes}', 'etant disjoints')], 2)
replace_a_group('A022-G05-underformula-guide', 'B', 'B022-G05', 3)
replace_a_group('A022-G06-intersection-insertion', 'B', 'B022-G06', 3)
replace_a_group('A022-S03', 'B', 'B022-S03', 3)

# §04: one old relation/empty-set cluster replaces the two A groups together.
old_relation = group('A', 'A022-G08-old-relation')['marker_span']
old_emptyset = group('A', 'A022-G09-old-emptyset')['marker_span']
replacement, edits, selected_source = imported_group('B', 'B022-G08')
add_operation('replace-old-relation-and-emptyset', old_relation['start_char'], old_emptyset['end_char_exclusive'], replacement, 4, [selected_source], edits)

# §06: C's copied full base-west anchor and its local origin are supplied metadata.
c_s10 = group('C', 'C022-S10')
c_node_ref = c_s10['complete_enclosing_node_ref']
c_node_span = pointer(c_node_ref)['source_span']
c_literal = c_node_span['literal_source']
c_literal, c_edits = change_text('C022-S10', c_literal, [
    ('at (495,214)', 'at (740,844)'),
    ('x=0.008cm', 'x=0.085mm'),
    ('y=-0.008cm', 'y=-0.085mm'),
    (r'\mbox{\begin{tikzpicture}', r'\unsure{\mbox{\begin{tikzpicture}'),
    ('\\end{tikzpicture}}\n% END C022-S10', '\\end{tikzpicture}}}\n% END C022-S10'),
], 6)
c_literal = ('% Root import C022-S10: original parent origin (245,630), original parent node anchor (495,214).\n'
             '% Copied declared full base-west anchor (740,844), inner box xmin=-1, inner origin (741,844).\n'
             '% Root §06 locally qualifies the physical head/return role; Sigma_alpha^- remains primary.\n' + c_literal + '\n')
old = group('A', 'A022-S10')['marker_span']
add_operation('replace-A022-S10', old['start_char'], old['end_char_exclusive'], c_literal, 6, [{'bank_pointer': c_node_ref, 'span': span_ref(c_node_span)}, {'bank_pointer': '/readers/C/groups/C022-S10/raw_reader_node_anchor'}], c_edits, 'Copied anchor correspondence from C node metadata; no coordinate values calculated.')

# §07: the root-supplied point uses its full-scan bbox and center directly.
root_point = r'''% BEGIN R022-M01-plain-V-adjacent-point
% Root §07 supplies bbox (1158,843,1166,851), center (1162,847), radius .7.
% The base-west anchor and picture baseline copy bbox-left x=1158 and center y=847.
% Owns this locally qualified point alone; the adjoining plain V remains in A label T27.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1158,847) {\unsure{%
\begin{tikzpicture}[x=0.085mm,y=-0.085mm,baseline={(1158,847)}]
\path[use as bounding box] (1158,843) rectangle (1166,851);
\fill (1162,847) circle[radius=.7];
\end{tikzpicture}%
}};
% END R022-M01-plain-V-adjacent-point
'''
point_node = node('A', 'T27')['source_span']
point_at = base.index('\n', point_node['end_char_exclusive']) + 1
add_operation('insert-root-adjacent-point', point_at, point_at, root_point, 7, [{'root_journal_section': 7, 'root_group_id': 'R022-M01-plain-V-adjacent-point'}], note='All bbox/center/radius numbers are literal root instructions. The wrapper copies bbox-left and center-baseline values without translating path numbers.')

# §§08–11: exact whole-word alternatives and the selected lower frame interruption.
replace_a_group('A022-S12', 'B', 'B022-S12', 8)
change_a_node('T48', [(r'\unsure{formule|relation}', 'formule')], 10)
b_second_equality = next(n for n in bank['readers']['B']['nodes'].values() if n.get('raw_reader_text_ownership', {}).get('text') == r'\unsure{égalité|egalité}')
change_a_node('T51', [('égalité', r'\unsure{égalité|egalité}')], 10, {'bank_pointer': f'/readers/B/nodes/{b_second_equality["id"]}', 'span': span_ref(b_second_equality['source_span'])})
insert_after_a_group('A022-G12-local-on-and-noun-cancellations', 'B', 'B022-M06', 10)
change_a_node('T59', [(r'ferm\unsure{é|è|e}es', r'ferm\unsure{è|é|e}es')], 11)
old_wrap = next(p for p in bank['readers']['A']['paths'].values() if p['owner'] == 'A022-G14-cancellation-frame' and p['source_span']['literal_source'].startswith(r'\draw[line width=.5pt] (307,1731)'))
new_wrap_paths = []
for begin in [r'\draw[line width=.3pt,line cap=round] (308,1736)', r'\draw[line width=.35pt,line cap=round] (296,1809)']:
    new_wrap_paths.append(next(p for p in bank['readers']['B']['paths'].values() if p['owner'] == 'B022-G14' and p['source_span']['literal_source'].startswith(begin)))
replacement = '% Root §11: the following two literal B022-G14 paths retain their interruption.\n' + '\n'.join(p['source_span']['literal_source'] for p in new_wrap_paths)
old = old_wrap['source_span']
add_operation('replace-final-frame-wrap', old['start_char'], old['end_char_exclusive'], replacement, 11, [{'bank_pointer': f'/readers/B/paths/{p["id"]}', 'span': span_ref(p['source_span'])} for p in new_wrap_paths], note='Both B paths inherit the selected A parent units. Their numeric paths remain literal; the original A continuous wrap is replaced once.')

# §§12–14: complete point-only imports and the separately owned relation after Z.
insert_after_a_group('A022-G14-cancellation-frame', 'B', 'B022-M07', 12)
change_a_node('T67', [(r'$Z=$', r'$Z\phantom{=}$')], 14)
c_relation = group('C', 'C022-G09')
c_relation_node_ref = c_relation['complete_enclosing_node_ref']
c_relation_node_span = pointer(c_relation_node_ref)['source_span']
c_relation_literal, c_relation_edits = change_text('C022-G09', c_relation_node_span['literal_source'], [
    ('at (340,-15)', 'at (975,2006)'),
    ('x=0.008cm', 'x=0.085mm'),
    ('y=-0.008cm', 'y=-0.085mm'),
], 14)
c_relation_literal = ('% Root import C022-G09: original parent origin (635,2021), original parent node anchor (340,-15).\n'
                      '% Copied declared full base-west anchor (975,2006), inner box xmin=-4, inner origin (979,2006).\n' + c_relation_literal + '\n')
z_node_span = node('A', 'T67')['source_span']
relation_at = base.index('\n', z_node_span['end_char_exclusive']) + 1
add_operation('insert-C022-G09-relation', relation_at, relation_at, c_relation_literal, 14, [{'bank_pointer': c_relation_node_ref, 'span': span_ref(c_relation_node_span)}, {'bank_pointer': '/readers/C/groups/C022-G09/raw_reader_node_anchor'}], c_relation_edits, 'A T67 retains visible Z and an invisible equals placeholder inside its original resize declaration; this complete C group supplies the one visible relation.')
replace_a_group('A022-M05-sigma-inner-point', 'B', 'B022-M04', 14)

# Source-administration comment: the original A header remains literal provenance.
header_at = base.index('\n') + 1
add_operation('assembly-header', header_at, header_at,
              '% Root-selected source draft; main_adjudicated=false; main_approved=false.\n'
              '% A layout with the explicitly selected B/C/root replacements; original reader files remain immutable.\n',
              15, [{'root_assembly_directive': 'A base layout with only root-selected groups/wording applied'}],
              note='Administrative source header only; no ink choice or count is inferred from this comment.')


# Assemble disjoint edits against the immutable base offsets.
operations.sort(key=lambda op: (op['base_start_char'], op['base_end_char_exclusive']))
cursor = 0
parts = []
segments = []
final_position = 0
for operation in operations:
    start, end = operation['base_start_char'], operation['base_end_char_exclusive']
    assert cursor <= start, ('overlapping source operations', operation['id'])
    if cursor < start:
        unchanged = base[cursor:start]
        parts.append(unchanged)
        segments.append({'kind': 'retained_A_source', 'base_start_char': cursor, 'base_end_char_exclusive': start, 'final_start_char': final_position, 'final_end_char_exclusive': final_position + len(unchanged)})
        final_position += len(unchanged)
    replacement = operation['replacement']
    parts.append(replacement)
    operation['final_start_char'] = final_position
    operation['final_end_char_exclusive'] = final_position + len(replacement)
    segments.append({'kind': 'root_source_operation', 'operation_id': operation['id'], 'base_start_char': start, 'base_end_char_exclusive': end, 'final_start_char': final_position, 'final_end_char_exclusive': final_position + len(replacement)})
    final_position += len(replacement)
    cursor = end
if cursor < len(base):
    retained = base[cursor:]
    parts.append(retained)
    segments.append({'kind': 'retained_A_source', 'base_start_char': cursor, 'base_end_char_exclusive': len(base), 'final_start_char': final_position, 'final_end_char_exclusive': final_position + len(retained)})
draft = ''.join(parts)


def final_span(start, end):
    return {
        'path': rel(DRAFT_PATH), 'record_attachment_path': rel(DRAFT_PATH).removeprefix('out/'),
        'start_char': start, 'end_char_exclusive': end,
        'start_utf8_byte': len(draft[:start].encode()), 'end_utf8_byte_exclusive': len(draft[:end].encode()),
        'start_line': draft.count('\n', 0, start) + 1,
        'end_line': draft.count('\n', 0, end - 1) + 1,
        'sha256_utf8': sha(draft[start:end].encode()), 'literal_source': draft[start:end],
    }


for operation in operations:
    operation['final_span'] = final_span(operation['final_start_char'], operation['final_end_char_exclusive'])
    operation['base_source_literal'] = base[operation['base_start_char']:operation['base_end_char_exclusive']]

output_groups = {}
group_stack = []
for match in re.finditer(r'% (BEGIN|END) ((?:[ABC]|R)022-[A-Za-z0-9-]+)', draft):
    identity = match.group(2)
    if match.group(1) == 'BEGIN':
        group_stack.append((identity, match.start()))
    else:
        opened, start = group_stack.pop()
        assert opened == identity
        end = draft.find('\n', match.end())
        end = len(draft) if end < 0 else end + 1
        output_groups[identity] = {'id': identity, 'final_span': final_span(start, end), 'main_approved': False}
assert not group_stack

# A labels retain their original identity comments through all root wording edits.
label_spans = {}
for match in re.finditer(r'^% LABEL (T\d+):[^\n]*\n', draft, re.M):
    start = draft.index('\\node', match.end())
    end = draft.index('\n', start)
    label_spans[match.group(1)] = final_span(start, end)


def command_end(text, start):
    depth = 0
    at = start
    while at < len(text):
        char = text[at]
        if char == '\\':
            at += 2
            continue
        if char == '%':
            at = text.find('\n', at)
            assert at >= 0
        elif char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
        elif char == ';' and depth == 0:
            return at + 1
        at += 1
    raise AssertionError(('source node terminator', start))


def final_group_chain(start, end):
    enclosed = [item for item in output_groups.values() if item['final_span']['start_char'] <= start and end <= item['final_span']['end_char_exclusive']]
    return [item['id'] for item in sorted(enclosed, key=lambda item: (item['final_span']['start_char'], -item['final_span']['end_char_exclusive']))]


node_final_spans = {}
for match in re.finditer(r'(?m)^\\node\b', draft):
    end = command_end(draft, match.start())
    identity = 'R022-node-L' + str(draft.count('\n', 0, match.start()) + 1).zfill(4)
    node_final_spans[identity] = {'id': identity, 'final_span': final_span(match.start(), end), 'source_group_ancestors': final_group_chain(match.start(), end)}
for item in output_groups.values():
    start, end = item['final_span']['start_char'], item['final_span']['end_char_exclusive']
    enclosing = [node for node in node_final_spans.values() if node['final_span']['start_char'] < start and end <= node['final_span']['end_char_exclusive']]
    closest = min(enclosing, key=lambda node: node['final_span']['end_char_exclusive'] - node['final_span']['start_char']) if enclosing else None
    item['complete_enclosing_node_final_ref'] = '/node_final_spans/' + closest['id'] if closest else None
    item['selected_source_complete'] = True

path_final_spans = {}
for match in re.finditer(r'(?m)^\\(?:draw|fill)\b[^\n]*;', draft):
    literal = match.group()
    chain = final_group_chain(match.start(), match.end())
    owner = chain[-1] if chain else None
    identity = 'R022-path-L' + str(draft.count('\n', 0, match.start()) + 1).zfill(4)
    exact_sources = []
    for reader, data in bank['readers'].items():
        for source_path in data['paths'].values():
            if source_path['source_span']['literal_source'] == literal:
                exact_sources.append({'bank_pointer': f'/readers/{reader}/paths/{source_path["id"]}', 'original_owner': source_path['owner'], 'span': span_ref(source_path['source_span'])})
    owning_operation = next((operation for operation in operations if operation['final_start_char'] <= match.start() and match.end() <= operation['final_end_char_exclusive']), None)
    if owner == 'R022-M01-plain-V-adjacent-point':
        assert literal == r'\fill (1162,847) circle[radius=.7];'
        attribution = {'root_journal_section': 7, 'root_group_id': owner}
    else:
        assert exact_sources, ('untraced literal path', identity, literal)
        attribution = {'exact_literal_source_matches': exact_sources}
        owner_matches = [candidate for candidate in exact_sources if candidate['original_owner'] == owner]
        if owner_matches:
            attribution['selected_original_owner_match'] = owner_matches
    if owning_operation:
        attribution['assembly_operation_id'] = owning_operation['id']
        attribution['root_journal_section'] = owning_operation['root_journal_section']
    path_final_spans[identity] = {'id': identity, 'owner': owner, 'source_group_ancestors': chain, 'final_span': final_span(match.start(), match.end()), 'source_attribution': attribution}

# The attributed content note cites exact selected source spans, including prose
# adjoining the final display. It reports the author's writing without a check.
closing_literal = ('et on doit prouver\n\\[\n'
                   '\\overline{(X\\setminus(Y\\cup Z))}\\cap Y=\\overline{(X\\setminus Y)}\\cap Y\n'
                   '\\]\nce qui est immédiat')
closing_at = draft.index(closing_literal)
content_note = {
    'main_approved': False,
    'attributed_only': True,
    'check_events': [],
    'text': "The manuscript opens with a cancelled recurrence on card K, gives intersection and nonemptiness conditions, and states an equality involving E_alpha. Its cancelled inverse-inclusion and neighbourhood argument contains the locally cancelled on and the replacement of formule by an inserted égalité. The restart names two closed disjoint parts Y and Z. The author then writes the final displayed equality and calls it « ce qui est immédiat ». These are manuscript assertions, with no proof, refutation or computation supplied by this transcription.",
    'exact_selected_source_refs': {
        'cancelled_recurrence': ['/A_label_final_spans/T01', '/A_label_final_spans/T02', '/A_label_final_spans/T03', '/A_label_final_spans/T04'],
        'first_conditions': ['/A_label_final_spans/T13', '/A_label_final_spans/T14', '/graphical_group_final_spans/A022-S04', '/graphical_group_final_spans/B022-G08', '/A_label_final_spans/T15', '/A_label_final_spans/T16', '/A_label_final_spans/T17', '/graphical_group_final_spans/A022-S05', '/A_label_final_spans/T18'],
        'prose_and_main_equality': ['/A_label_final_spans/T19', '/A_label_final_spans/T20', '/graphical_group_final_spans/A022-S06', '/A_label_final_spans/T21', '/A_label_final_spans/T22'],
        'cancelled_ie': ['/A_label_final_spans/T36', '/A_label_final_spans/T37'],
        'cancelled_on_and_noun_correction': ['/A_label_final_spans/T44', '/A_label_final_spans/T48', '/A_label_final_spans/T49'],
        'restart': ['/A_label_final_spans/T61', '/A_label_final_spans/T62', '/A_label_final_spans/T63', '/A_label_final_spans/T64'],
        'Y_Z_definitions': ['/A_label_final_spans/T65', '/graphical_group_final_spans/A022-S16', '/A_label_final_spans/T66', '/A_label_final_spans/T67', '/graphical_group_final_spans/C022-G09', '/graphical_group_final_spans/A022-G16-final-union', '/graphical_group_final_spans/A022-S17'],
    },
    'final_prose_and_display': final_span(closing_at, closing_at + len(closing_literal)),
}

# Required source-freeze boundaries: braces, environments, math delimiters,
# command-token slips and comment/newline joins. This supplies assembler checks;
# root's independent final source audit remains separate.
brace_stack = []
environment_stack = []
math_stack = []
errors = []
at = 0
line = 1
while at < len(draft):
    char = draft[at]
    if char == '\n':
        line += 1
        at += 1
        continue
    if char == '%':
        end = draft.find('\n', at)
        if end < 0:
            break
        at = end
        continue
    if char == '\\':
        match = re.match(r'\\(begin|end)\{([^}]+)\}', draft[at:])
        if match:
            if match.group(1) == 'begin':
                environment_stack.append((match.group(2), line))
            elif not environment_stack or environment_stack.pop()[0] != match.group(2):
                errors.append(['environment boundary', line, match.group()])
            at += match.end()
            continue
        if at + 1 < len(draft) and draft[at + 1] in '[]':
            if draft[at + 1] == '[':
                math_stack.append(('display', line))
            elif not math_stack or math_stack.pop()[0] != 'display':
                errors.append(['display boundary', line])
            at += 2
            continue
        if at + 2 < len(draft) and draft[at + 1] == '\\' and draft[at + 2].isalpha():
            errors.append(['double-backslash command token', line])
        at += 2
        continue
    if char == '{':
        brace_stack.append(line)
    elif char == '}':
        if brace_stack:
            brace_stack.pop()
        else:
            errors.append(['extra closing brace', line])
    elif char == '$':
        if math_stack and math_stack[-1][0] == 'dollar':
            math_stack.pop()
        else:
            math_stack.append(('dollar', line))
    at += 1
errors.extend(['unclosed brace', source_line] for source_line in brace_stack)
errors.extend(['unclosed environment', name, source_line] for name, source_line in environment_stack)
errors.extend(['unclosed math delimiter', name, source_line] for name, source_line in math_stack)
for match in re.finditer(r'\\\[(.*?)\\\]', draft, re.S):
    if '\n\n' in match.group(1):
        errors.append(['physical paragraph blank inside display', draft.count('\n', 0, match.start()) + 1])
for operation in operations:
    replacement = operation['replacement']
    if replacement and replacement.split('\n')[-1].startswith('%') and draft[operation['final_end_char_exclusive']:operation['final_end_char_exclusive'] + 1] != '\n':
        errors.append(['comment/newline splice', operation['id']])
assert not errors, errors

base_source_dispositions = {'groups': {}, 'nodes': {}, 'paths': {}}
for component_kind, entries in [('groups', bank['readers']['A']['groups']), ('nodes', bank['readers']['A']['nodes']), ('paths', bank['readers']['A']['paths'])]:
    for identity, component in entries.items():
        original_span = component['marker_span'] if component_kind == 'groups' else component['source_span']
        start, end = original_span['start_char'], original_span['end_char_exclusive']
        affected = [operation for operation in operations if operation['base_start_char'] < end and start < operation['base_end_char_exclusive']]
        retained_segments = [segment for segment in segments if segment['kind'] == 'retained_A_source' and segment['base_start_char'] <= start and end <= segment['base_end_char_exclusive']]
        if not affected:
            assert retained_segments or component_kind == 'groups', ('unmapped base component', component_kind, identity)
        disposition = {
            'original_bank_pointer': f'/readers/A/{component_kind}/{identity}',
            'original_source_span': span_ref(original_span),
            'disposition': 'root-authorized literal edit or replacement' if affected else 'retained original A source',
            'assembly_operation_ids': [operation['id'] for operation in affected],
        }
        if component_kind == 'groups' and identity in output_groups:
            disposition['current_group_ref'] = '/graphical_group_final_spans/' + identity
        base_source_dispositions[component_kind][identity] = disposition

selected_state_metadata = {
    'A022-G10-lower-annotations': {
        'root_journal_section': 6,
        'complete_candidates_or_state': group('A', 'A022-G10-lower-annotations')['raw_reader_metadata']['complete_candidates_or_state'],
        'scope': 'Both complete formulas share this live-inserted/deleted-inserted state question. The source outer graphical qualifier remains intact.',
        'source_ref': '/readers/A/groups/A022-G10-lower-annotations/raw_reader_metadata/complete_candidates_or_state',
    },
    'A022-S11': {
        'root_journal_section': 6,
        'complete_candidates_or_state': group('A', 'A022-S11')['raw_reader_metadata']['complete_candidates_or_state'],
        'scope': 'Complete barred primary and unbarred alternative, with cancelled-passage state and the original local graphical qualifier retained. The shared upper run remains in G14.',
        'source_ref': '/readers/A/groups/A022-S11/raw_reader_metadata/complete_candidates_or_state',
    },
    'C022-S10': {
        'root_journal_section': 6,
        'primary': r'\Sigma_\alpha^-',
        'qualification': 'physical head/return role locally qualified',
        'raw_anchor_metadata': c_s10['raw_reader_node_anchor'],
        'source_parent_declarations': c_s10['inherited_declaration_refs'],
    },
    'recurring_head_role': {
        'root_journal_section': 1,
        'first_printed_qualifier_group': 'A022-S01',
        'later_local_role_records': ['A022-S02', 'A022-S04', 'A022-S05', 'A022-S07', 'A022-S08', 'A022-S13', 'A022-S14', 'A022-S15', 'A022-S17'],
    },
    'C022-G09': {
        'root_journal_section': 14,
        'primary': '=',
        'qualification': 'locally qualified returning relation',
        'raw_anchor_metadata': c_relation['raw_reader_node_anchor'],
        'source_parent_declarations': c_relation['inherited_declaration_refs'],
    },
    'complete_final_Sigma_cluster': {
        'root_journal_section': 14,
        'group_ids': ['A022-S17', 'B022-M04', 'A022-M06-below-beta-point'],
        'scope': 'One complete Sigma body/head/roof/plus/beta group and its two separately owned point-only groups.',
    },
}

source_map = {
    'scan': 22, 'status': 'frozen root-selected source; root approval pending',
    'main_adjudicated': False, 'main_approved': False,
    'draft_path': rel(DRAFT_PATH), 'record_attachment_path': rel(DRAFT_PATH).removeprefix('out/'),
    'draft_sha256_utf8': sha(draft.encode()),
    'final_draft_sha256': sha(draft.encode()),
    'candidate_bank': {'path': rel(BANK_PATH), 'sha256': BANK_SHA},
    'base_source': {'path': rel(base_path), 'sha256': sha(base.encode())},
    'journal_snapshot': {'path_at_read': rel(journal_path), 'sha256_utf8': sha(journal.encode()), 'literal_source': journal},
    'root_count_authorization': {'path': rel(count_authorization_path), 'sha256': sha(count_authorization_path.read_bytes()), 'scope': 'Root-supplied count/confidence/physical-parent authorization; copied without recomputation.'},
    'counts': count_authorization['counts'],
    'C_original_rows': count_authorization['C_original_rows'],
    'applied_journal_sections': list(range(1, 16)),
    'uniform_mapping_authority': 'Root directive: all selected imported x units become 0.085mm and y units -0.085mm; original numeric path coordinates and origin/baseline mappings remain explicit. No coordinate calculations or metric validation performed.',
    'operations': operations, 'assembly_segments': segments,
    'graphical_group_final_spans': output_groups, 'A_label_final_spans': label_spans,
    'node_final_spans': node_final_spans, 'path_final_spans': path_final_spans,
    'base_source_dispositions': base_source_dispositions,
    'selected_state_metadata': selected_state_metadata,
    'attributed_content_note': content_note,
    'pending_regions': [],
    'assembler_literal_validation': {'errors': errors, 'all_final_draw_fill_paths_traced': True, 'brace_environment_math_boundaries': 'passed', 'plain_command_tokens': 'passed', 'display_paragraph_boundaries': 'passed', 'comment_newline_splices': 'passed', 'scope': 'Required selected-source freeze checks only; no independent coverage/count/public-record audit performed.'},
    'source_only_scope': 'Literal source extraction, root-authorized replacements, exact source offsets and source balancing; selected independent audit remains separately assigned by root.',
    'assembler_script': {'path': rel(Path(__file__)), 'sha256': sha(Path(__file__).read_bytes())},
}
assert not DRAFT_PATH.exists() and not MAP_PATH.exists(), 'Preserve an existing stage; choose a new stage filename.'
DRAFT_PATH.write_text(draft)
MAP_PATH.write_text(json.dumps(source_map, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'draft': {'path': rel(DRAFT_PATH), 'sha256': sha(DRAFT_PATH.read_bytes())}, 'map': {'path': rel(MAP_PATH), 'sha256': sha(MAP_PATH.read_bytes())}, 'status': source_map['status']}, ensure_ascii=False))
