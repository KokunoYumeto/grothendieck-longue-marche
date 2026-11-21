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
STAGE = '014'
DRAFT_PATH = ROOT / f'out/checks/scan022_selected_stage_{STAGE}.tex'
MAP_PATH = ROOT / f'out/checks/scan022_selected_stage_{STAGE}.map.json'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def rel(path):
    return str(path.relative_to(ROOT))


assert sha(BANK_PATH.read_bytes()) == BANK_SHA
bank = json.loads(BANK_PATH.read_text())
base_path = ROOT / 'out/readers/022/A/reading.tex'
base = base_path.read_text()
assert sha(base.encode()) == bank['source_files']['A']['reading.tex']['root_released_sha256']
journal_path = ROOT / 'out/checks/scan022_main_decisions.md'
journal = journal_path.read_text()
journal_sections = {}
section_matches = list(re.finditer(r'^## (\d+) — ', journal, re.M))
for index, match in enumerate(section_matches):
    end = section_matches[index + 1].start() if index + 1 < len(section_matches) else len(journal)
    journal_sections[int(match.group(1))] = journal[match.start():end]
assert all(section in journal_sections for section in range(1, 15))


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
    'scan': 22, 'status': 'partial root-selected assembly through section 14; closing-content approval remains pending',
    'main_adjudicated': False, 'main_approved': False,
    'draft_path': rel(DRAFT_PATH), 'record_attachment_path': rel(DRAFT_PATH).removeprefix('out/'),
    'draft_sha256_utf8': sha(draft.encode()),
    'candidate_bank': {'path': rel(BANK_PATH), 'sha256': BANK_SHA},
    'base_source': {'path': rel(base_path), 'sha256': sha(base.encode())},
    'journal_snapshot': {'path_at_read': rel(journal_path), 'sha256_utf8': sha(journal.encode()), 'literal_source': journal},
    'applied_journal_sections': list(range(1, 15)),
    'uniform_mapping_authority': 'Root directive: all selected imported x units become 0.085mm and y units -0.085mm; original numeric path coordinates and origin/baseline mappings remain explicit. No coordinate calculations or metric validation performed.',
    'operations': operations, 'assembly_segments': segments,
    'graphical_group_final_spans': output_groups, 'A_label_final_spans': label_spans,
    'selected_state_metadata': selected_state_metadata,
    'pending_regions': ['final conventional equality/content approval'],
    'source_only_scope': 'Literal source extraction, root-authorized replacements, exact source offsets and source balancing; selected independent audit remains separately assigned by root.',
    'assembler_script': {'path': rel(Path(__file__)), 'sha256': sha(Path(__file__).read_bytes())},
}
assert not DRAFT_PATH.exists() and not MAP_PATH.exists(), 'Preserve an existing stage; choose a new stage filename.'
DRAFT_PATH.write_text(draft)
MAP_PATH.write_text(json.dumps(source_map, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'draft': {'path': rel(DRAFT_PATH), 'sha256': sha(DRAFT_PATH.read_bytes())}, 'map': {'path': rel(MAP_PATH), 'sha256': sha(MAP_PATH.read_bytes())}, 'status': source_map['status']}, ensure_ascii=False))
