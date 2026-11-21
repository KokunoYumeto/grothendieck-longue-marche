"""Bounded root-authorized scan022 source-comment repair.

Exactly three marker newline insertions and three donor-label comment changes.
The initial release remains immutable; all selected command strings remain exact.
"""
import copy
import difflib
import hashlib
import json
import re
from pathlib import Path

ROOT = Path('/workspace/scratch/94548b74fbe0')
CHECKS = ROOT / 'out/checks'
INITIAL = CHECKS / 'scan022_source_audit_initial_release'
EXPECTED = {
    'scan022_final_draft.tex': '843d6f48ca05cc4ecebce7a9fd2ced57005aece94e3b7b073f10acba3326b5e6',
    'scan022_final_source_map.json': '55bb48d1bee684955fdef861d78da6fb94a329c79acadae06f098efa90d710f9',
    'scan022_assembler_source_validation.json': '60cf4046e150459de06fa88b329dd8c5d99ae04f89b12b3141ef159c3f14a9dd',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


for name, expected in EXPECTED.items():
    assert sha((CHECKS / name).read_bytes()) == expected
    assert sha((INITIAL / name).read_bytes()) == expected
INITIAL_AUDIT = {
    'scan022_source_audit.json': 'aa5e3d1d23552403bf3c68f7c0436794c48afe143b6549ad0bfd40e27c0d3dc8',
    'scan022_source_audit.md': '1e624e72fc62c8318906530cc286437f6f37f60d9b9bd33b013486a1236e4ffc',
}
for name, expected in INITIAL_AUDIT.items():
    assert sha((CHECKS / name).read_bytes()) == expected

old_draft = (INITIAL / 'scan022_final_draft.tex').read_text()
old_map = json.loads((INITIAL / 'scan022_final_source_map.json').read_text())
old_validation = json.loads((INITIAL / 'scan022_assembler_source_validation.json').read_text())
source_edits = []
for following in ['B022-M01', 'B022-M06', 'B022-M07']:
    literal = '% BEGIN ' + following
    start = old_draft.index(literal)
    assert old_draft[start - 1] != '\n'
    source_edits.append({'id': 'newline-before-' + following, 'start_char': start, 'end_char_exclusive': start, 'old': '', 'new': '\n'})

comment_changes = [
    ('B022-M01', '% Ownership: Short detached slash below pour; the word pour stays in T03.', '% Ownership: Short detached slash below pour; the word pour remains in A label T06.'),
    ('B022-G08', '% Ownership: The old relation and its old empty-set glyph, including their local cancellation strokes; replacement is T10.', '% Ownership: The old relation and its old empty-set glyph, including their local cancellation strokes; replacement is A label T15.'),
    ('B022-M06', '% Ownership: Small point below the beginning of the old noun; noun itself belongs to T32.', '% Ownership: Small point below the beginning of the old noun; noun itself belongs to A label T48.'),
]
for group_id, before, after in comment_changes:
    assert old_draft.count(before) == 1
    start = old_draft.index(before)
    source_edits.append({'id': 'selected-label-comment-' + group_id, 'start_char': start, 'end_char_exclusive': start + len(before), 'old': before, 'new': after})
source_edits.sort(key=lambda item: item['start_char'])
cursor = 0
pieces = []
for edit in source_edits:
    assert old_draft[edit['start_char']:edit['end_char_exclusive']] == edit['old']
    pieces.extend([old_draft[cursor:edit['start_char']], edit['new']])
    cursor = edit['end_char_exclusive']
pieces.append(old_draft[cursor:])
new_draft = ''.join(pieces)


def moved(position, boundary):
    shift = 0
    for edit in source_edits:
        start, end = edit['start_char'], edit['end_char_exclusive']
        if start == end:
            if start < position or (start == position and boundary == 'start'):
                shift += len(edit['new'])
        elif end <= position:
            shift += len(edit['new']) - len(edit['old'])
        elif start < position < end:
            raise AssertionError(('span boundary lies inside changed comment', position, edit['id']))
    return position + shift


def current_span(start, end):
    return {
        'path': 'out/checks/scan022_final_draft.tex',
        'record_attachment_path': 'checks/scan022_final_draft.tex',
        'start_char': start, 'end_char_exclusive': end,
        'start_utf8_byte': len(new_draft[:start].encode()),
        'end_utf8_byte_exclusive': len(new_draft[:end].encode()),
        'start_line': new_draft.count('\n', 0, start) + 1,
        'end_line': new_draft.count('\n', 0, end - 1) + 1,
        'sha256_utf8': sha(new_draft[start:end].encode()),
        'literal_source': new_draft[start:end],
    }


new_map = copy.deepcopy(old_map)


def update_spans(value):
    if isinstance(value, dict):
        if value.get('path') == 'out/checks/scan022_final_draft.tex' and 'start_char' in value and 'end_char_exclusive' in value:
            replacement = current_span(moved(value['start_char'], 'start'), moved(value['end_char_exclusive'], 'end'))
            value.update(replacement)
        else:
            for child in value.values():
                update_spans(child)
    elif isinstance(value, list):
        for child in value:
            update_spans(child)


update_spans(new_map)
operations = new_map['operations']
by_id = {operation['id']: operation for operation in operations}
for identity in ['insert-B022-M01', 'insert-B022-M06', 'insert-B022-M07']:
    operation = by_id[identity]
    operation['replacement'] = '\n' + operation['replacement']
    operation.setdefault('bounded_source_repairs', []).append('A newline separates the preceding END marker comment from this BEGIN marker comment.')
for group_id, before, after in comment_changes:
    identity = 'replace-old-relation-and-emptyset' if group_id == 'B022-G08' else 'insert-' + group_id
    operation = by_id[identity]
    assert operation['replacement'].count(before) == 1
    operation['replacement'] = operation['replacement'].replace(before, after)
    operation['literal_edits'].append({'old': before, 'new': after, 'literal_occurrences': 1, 'scope': 'root-authorized active selected-label comment; donor wording remains immutable provenance'})

# Rebuild only the operation/segment offset mirrors using the unchanged base.
base = (ROOT / old_map['base_source']['path']).read_text()
assert sha(base.encode()) == old_map['base_source']['sha256']
cursor = 0
position = 0
replayed = []
segments = []
for operation in operations:
    start, end = operation['base_start_char'], operation['base_end_char_exclusive']
    assert cursor <= start
    if cursor < start:
        retained = base[cursor:start]
        replayed.append(retained)
        segments.append({'kind': 'retained_A_source', 'base_start_char': cursor, 'base_end_char_exclusive': start, 'final_start_char': position, 'final_end_char_exclusive': position + len(retained)})
        position += len(retained)
    replacement = operation['replacement']
    replayed.append(replacement)
    operation['final_start_char'] = position
    operation['final_end_char_exclusive'] = position + len(replacement)
    operation['final_span'] = current_span(position, position + len(replacement))
    segments.append({'kind': 'root_source_operation', 'operation_id': operation['id'], 'base_start_char': start, 'base_end_char_exclusive': end, 'final_start_char': position, 'final_end_char_exclusive': position + len(replacement)})
    position += len(replacement)
    cursor = end
if cursor < len(base):
    retained = base[cursor:]
    replayed.append(retained)
    segments.append({'kind': 'retained_A_source', 'base_start_char': cursor, 'base_end_char_exclusive': len(base), 'final_start_char': position, 'final_end_char_exclusive': position + len(retained)})
assert ''.join(replayed) == new_draft
new_map['assembly_segments'] = segments

# Correct the three formerly overextended END-comment group spans by parsing
# the explicitly repaired markers. All stable group/node/path IDs are retained.
stack = []
for match in re.finditer(r'% (BEGIN|END) ((?:[ABC]|R)022-[A-Za-z0-9-]+)', new_draft):
    identity = match.group(2)
    if match.group(1) == 'BEGIN':
        stack.append((identity, match.start()))
    else:
        opened, start = stack.pop()
        assert opened == identity
        end = new_draft.find('\n', match.end())
        end = len(new_draft) if end < 0 else end + 1
        new_map['graphical_group_final_spans'][identity]['final_span'] = current_span(start, end)
assert not stack

for field in ['node_final_spans', 'path_final_spans']:
    for identity, previous in old_map[field].items():
        assert new_map[field][identity]['final_span']['literal_source'] == previous['final_span']['literal_source'], ('selected command changed', field, identity)
for identity in old_map['A_label_final_spans']:
    assert new_map['A_label_final_spans'][identity]['literal_source'] == old_map['A_label_final_spans'][identity]['literal_source']
for before_id, following_id in [
    ('A022-G01-opening-cancellations', 'B022-M01'),
    ('A022-G12-local-on-and-noun-cancellations', 'B022-M06'),
    ('A022-G14-cancellation-frame', 'B022-M07'),
]:
    assert f'% END {before_id}\n% BEGIN {following_id}' in new_draft
    assert new_map['graphical_group_final_spans'][before_id]['final_span']['literal_source'].endswith(f'% END {before_id}\n')
new_map['draft_sha256_utf8'] = sha(new_draft.encode())
new_map['final_draft_sha256'] = sha(new_draft.encode())
new_map['bounded_source_repair'] = {
    'scope': 'Three joined-marker newline separators and three active donor-label comments only.',
    'initial_release_directory': 'out/checks/scan022_source_audit_initial_release',
    'initial_draft_sha256': EXPECTED['scan022_final_draft.tex'],
    'initial_map_sha256': EXPECTED['scan022_final_source_map.json'],
    'source_edits': source_edits,
    'stable_helper_identity_note': 'Node/path helper IDs retain their initial-release identity; their current span fields contain the repaired offsets and line numbers.',
    'initial_check_scope_limitation': 'The initial assembler comment/newline check inspected replacement tails and omitted these three insertion junctions. This bounded closure checks the exact repaired junctions.',
    'selected_node_path_and_A_label_literals_unchanged': True,
    'main_approved': False,
}
new_map['assembler_literal_validation']['bounded_comment_junctions'] = 'The three exact END-newline-BEGIN junctions and their group spans pass.'
new_map['assembler_literal_validation']['bounded_active_label_comments'] = 'M01→A T06; G08 replacement→A T15; M06 noun→A T48. Original donor comments remain in immutable source/provenance.'

new_map_bytes = (json.dumps(new_map, ensure_ascii=False, indent=2) + '\n').encode()
new_validation = copy.deepcopy(old_validation)
new_validation['draft']['sha256'] = sha(new_draft.encode())
new_validation['map']['sha256'] = sha(new_map_bytes)
new_validation['structural_result_copied_from_frozen_map'] = copy.deepcopy(new_map['assembler_literal_validation'])
new_validation['bounded_repair_scope'] = copy.deepcopy(new_map['bounded_source_repair'])
new_validation_bytes = (json.dumps(new_validation, ensure_ascii=False, indent=2) + '\n').encode()


def changes(before, after, pointer=''):
    result = []
    if isinstance(before, dict) and isinstance(after, dict):
        for key in sorted(before.keys() | after.keys()):
            path = pointer + '/' + key.replace('~', '~0').replace('/', '~1')
            if key not in before:
                result.append({'pointer': path, 'old_exists': False, 'new_exists': True, 'new': after[key]})
            elif key not in after:
                result.append({'pointer': path, 'old_exists': True, 'new_exists': False, 'old': before[key]})
            else:
                result.extend(changes(before[key], after[key], path))
    elif isinstance(before, list) and isinstance(after, list) and len(before) == len(after):
        for index, (left, right) in enumerate(zip(before, after)):
            result.extend(changes(left, right, pointer + '/' + str(index)))
    elif before != after:
        result.append({'pointer': pointer, 'old_exists': True, 'new_exists': True, 'old': before, 'new': after})
    return result


map_changes = changes(old_map, new_map)
validation_changes = changes(old_validation, new_validation)


def inverse(after, change_list):
    restored = copy.deepcopy(after)
    for change in change_list:
        parts = [part.replace('~1', '/').replace('~0', '~') for part in change['pointer'].split('/')[1:]]
        target = restored
        for part in parts[:-1]:
            target = target[int(part)] if isinstance(target, list) else target[part]
        key = int(parts[-1]) if isinstance(target, list) else parts[-1]
        if change['old_exists']:
            target[key] = copy.deepcopy(change['old'])
        else:
            del target[key]
    return restored


assert inverse(new_map, map_changes) == old_map
assert inverse(new_validation, validation_changes) == old_validation
source_diff = ''.join(difflib.unified_diff(old_draft.splitlines(keepends=True), new_draft.splitlines(keepends=True), fromfile='initial/scan022_final_draft.tex', tofile='repaired/scan022_final_draft.tex'))
diff_path = CHECKS / 'scan022_bounded_source_repair.diff'
closure_path = CHECKS / 'scan022_assembler_bounded_source_closure.json'
assert not diff_path.exists() and not closure_path.exists()
closure = {
    'scan': 22,
    'scope': 'Root-authorized bounded source-comment repair only.',
    'main_adjudicated': False, 'main_approved': False,
    'initial_release_directory': 'out/checks/scan022_source_audit_initial_release',
    'initial_independent_audit_hashes_unchanged': INITIAL_AUDIT,
    'old_hashes': EXPECTED,
    'new_hashes': {
        'scan022_final_draft.tex': sha(new_draft.encode()),
        'scan022_final_source_map.json': sha(new_map_bytes),
        'scan022_assembler_source_validation.json': sha(new_validation_bytes),
    },
    'source_edits': source_edits,
    'source_diff': {'path': 'out/checks/scan022_bounded_source_repair.diff', 'sha256': sha(source_diff.encode())},
    'map_field_changes': map_changes,
    'validation_field_changes': validation_changes,
    'inverse_replay_preserves_initial_map_and_validation': True,
    'selected_node_path_and_A_label_literals_unchanged': True,
    'inventory_permutation': None,
    'count_changes': None,
    'source_qualifier_changes': None,
    'assembler_script': {'path': 'out/checks/scan022_repair_source_boundaries.py', 'sha256': sha(Path(__file__).read_bytes())},
}

# Publish the exact bounded result after all source-specific assertions pass.
(CHECKS / 'scan022_final_draft.tex').write_text(new_draft)
(CHECKS / 'scan022_final_source_map.json').write_bytes(new_map_bytes)
(CHECKS / 'scan022_assembler_source_validation.json').write_bytes(new_validation_bytes)
diff_path.write_text(source_diff)
closure_path.write_text(json.dumps(closure, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'new_hashes': closure['new_hashes'], 'diff': closure['source_diff'], 'closure': {'path': 'out/checks/scan022_assembler_bounded_source_closure.json', 'sha256': sha(closure_path.read_bytes())}}, ensure_ascii=False))
