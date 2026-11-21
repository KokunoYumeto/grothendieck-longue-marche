"""Literal extraction from the released scan022 reader sources only.

No source mutation, image access, rendering, geometry evaluation or ink selection.
The checks below bind extracted strings/offsets to the frozen source bytes.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path('/workspace/scratch/94548b74fbe0')
OUT = ROOT / 'out/checks/scan022_candidate_sources.json'
EXPECTED = {
    'A': {
        'reading.tex': 'a3c0703526396b6f051d7848d124239ae8c982a16216087d8d0c9ce3c38ba21a',
        'report.json': 'f48a1b4ba7ad9f5282b7cbd88060ce5e2f8a88571545a9ce17fe926221e6b7f4',
        'final_immutable.json': '83a21af3704afce201622138b3d42eae953bf86d285990fed2c4663ced297424',
    },
    'B': {
        'reading.tex': 'b7fe0dd99b386b2d82088258c562b6fec6e7bc32d98e609cda893fd0f95c97de',
        'report.json': '3405958c3ff67dfa90de79e3371c10aba2e5fe4f07de03d5b7fbaee744c57b30',
        'manifest.json': '32ae2aa61c47fe38ad4c59c33ca9fd1643b22a836519b123ac4145739b7f41f5',
    },
    'C': {
        'reading.tex': '87afac463f08e2c689a501d71572b33de43996a9c285fdea20b4ee0b446a26d9',
        'report.json': '6f571c4e494d87048135df4ab6de96a72a5296dbcf3e813db1e68135a530e3d3',
        'return_manifest.json': '4045f9077f9e1b0232a35d67d2cade17059e838bb4b965d52ed3d3cfd578dbb8',
    },
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def rel(path):
    return str(path.relative_to(ROOT))


def file_ref(path):
    data = path.read_bytes()
    return {'path': rel(path), 'sha256_utf8_file': digest(data)}


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def json_ref(path, pointer):
    return {'path': rel(path), 'json_pointer': pointer}


class Source:
    def __init__(self, reader):
        self.reader = reader
        self.path = ROOT / f'out/readers/022/{reader}/reading.tex'
        self.data = self.path.read_bytes()
        self.text = self.data.decode('utf-8')
        self.lines = self.text.splitlines(keepends=True)
        self.starts = [0]
        for line in self.lines:
            self.starts.append(self.starts[-1] + len(line))

    def span(self, start, end, literal=True):
        excerpt = self.text[start:end]
        item = {
            'path': rel(self.path),
            'start_char': start,
            'end_char_exclusive': end,
            'start_utf8_byte': len(self.text[:start].encode('utf-8')),
            'end_utf8_byte_exclusive': len(self.text[:end].encode('utf-8')),
            'start_line': self.text.count('\n', 0, start) + 1,
            'end_line': self.text.count('\n', 0, end - 1) + 1 if end > start else self.text.count('\n', 0, start) + 1,
            'sha256_utf8': digest(excerpt.encode('utf-8')),
        }
        if literal:
            item['literal_source'] = excerpt
        return item

    def from_bytes(self, start, end):
        return len(self.data[:start].decode('utf-8')), len(self.data[:end].decode('utf-8'))

    def exact_line(self, line):
        return self.span(self.starts[line - 1], self.starts[line])

    def unique(self, literal):
        first = self.text.find(literal)
        assert first >= 0, ('missing literal', self.reader, literal[:90])
        assert self.text.find(literal, first + 1) == -1, ('nonunique literal', self.reader, literal[:90])
        return first, first + len(literal)


def command_end(text, start):
    """Find a literal command's semicolon outside braced content/comments."""
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
    raise AssertionError(('no command terminator', start))


def argument_end(text, opening):
    depth = 1
    at = opening + 1
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
            if depth == 0:
                return at + 1
        at += 1
    raise AssertionError(('no argument terminator', opening))


def source_comments(source, start, end):
    comments = []
    for match in re.finditer(r'%[^\n]*(?:\n|$)', source.text[start:end]):
        comments.append(source.span(start + match.start(), start + match.end()))
    return comments


def strip_excerpt_fields(raw, fields):
    return {key: value for key, value in raw.items() if key not in fields}


bank = {
    'schema': 'scan022-released-graphical-candidate-sources-v01',
    'scan': 22,
    'status': 'complete released A/B/C source candidates; pending root ink journal',
    'released_readers': ['A', 'B', 'C'],
    'main_adjudicated': False,
    'main_approved': False,
    'selection_applied': False,
    'scope': 'Exact source extraction and source identity checks only. Numerical drawing declarations are copied literally and are not evaluated. No image, rendering or metric validation supports this bank.',
    'identity_convention': 'Original reader group/node/component identities remain explicit. Helper IDs describe source spans only. Source order and containment are textual and do not assert geometric adjacency or an ink interpretation.',
    'source_files': {},
    'readers': {},
    'source_notes': {},
    'extraction_validation': {
        'scope': 'Released-file SHA identities, exact source excerpts, source offsets, literal path commands and text-owner command matching only.',
        'selected_draft_created': False,
        'source_files_modified': False,
    },
}

for reader, expected_files in EXPECTED.items():
    directory = ROOT / f'out/readers/022/{reader}'
    refs = {}
    for name, expected in expected_files.items():
        reference = file_ref(directory / name)
        assert reference['sha256_utf8_file'] == expected, (reader, name, 'released hash mismatch')
        reference['root_released_sha256'] = expected
        reference['released_hash_matches'] = True
        refs[name] = reference
    bank['source_files'][reader] = refs
    source = Source(reader)
    groups = {}
    original_paths = []
    raw_labels = []
    raw_node_anchors = []
    reader_out = {'groups': groups, 'complete_compositions': {}, 'nodes': {}, 'paths': {}, 'declarations': {}}
    if reader == 'A':
        audit_path = directory / 'source_audit.json'
        audit = read_json(audit_path)
        refs['source_audit.json'] = file_ref(audit_path)
        refs['graphical_audit.json'] = file_ref(directory / 'graphical_audit.json')
        refs['structural_validation.json'] = file_ref(directory / 'structural_validation.json')
        raw_groups = audit['graphic_source_spans']
        original_paths = audit['all_literal_paths']
        raw_labels = audit['text_ownership']
        reader_out['reader_source_conventions'] = {
            key: audit[key] for key in ['shared_components', 'nested_group_ownership', 'word_boundary_audit', 'cancelled_label_handling', 'validation_scope', 'component_count_convention']
        }
        for index, raw in enumerate(raw_groups):
            start, end = source.from_bytes(raw['source_start_byte_utf8'], raw['source_end_byte_utf8'])
            assert source.text[start:end] == raw['complete_source_excerpt']
            groups[raw['id']] = {
                'id': raw['id'], 'reader_metadata_ref': json_ref(audit_path, f'/graphic_source_spans/{index}'),
                'raw_reader_metadata': strip_excerpt_fields(raw, ['literal_source', 'complete_source_excerpt', 'crop']),
                'marker_span': source.span(start, end),
            }
        for index, raw in enumerate(audit['complete_graphical_composites']):
            start, end = source.from_bytes(raw['source_start_byte_utf8'], raw['source_end_byte_utf8'])
            assert source.text[start:end] == raw['complete_source_excerpt']
            reader_out['complete_compositions'][raw['id']] = {
                'id': raw['id'], 'original_reader_id': raw['id'],
                'reader_metadata_ref': json_ref(audit_path, f'/complete_graphical_composites/{index}'),
                'raw_reader_metadata': strip_excerpt_fields(raw, ['complete_source_excerpt']),
                'source_span': source.span(start, end),
            }
        figure_start = source.text.index('\\figure{')
        figure_end = argument_end(source.text, figure_start + len('\\figure'))
        reader_out['complete_compositions']['A022-source-whole-figure'] = {
            'id': 'A022-source-whole-figure', 'original_reader_id': None,
            'helper_scope_identity': True,
            'scope': 'The one complete figure command in the immutable A source, including all its original nodes and local groups.',
            'source_span': source.span(figure_start, figure_end),
        }
    elif reader == 'B':
        group_path = directory / 'source_groups.json'
        raw_groups = read_json(group_path)
        raw_labels = read_json(directory / 'text_ownership.json')
        for name in ['source_groups.json', 'text_ownership.json', 'source_validation.json']:
            refs[name] = file_ref(directory / name)
        for index, raw in enumerate(raw_groups):
            start, end = raw['source_offsets_characters']
            assert source.text[start:end] == raw['source_excerpt']
            assert digest(raw['source_excerpt'].encode('utf-8')) == raw['source_sha256']
            groups[raw['id']] = {
                'id': raw['id'], 'reader_metadata_ref': json_ref(group_path, f'/{index}'),
                'raw_reader_metadata': strip_excerpt_fields(raw, ['source_excerpt', 'literal_commands', 'text_label_commands', 'crop']),
                'marker_span': source.span(start, end),
                'original_literal_commands_ref': json_ref(group_path, f'/{index}/literal_commands'),
                'original_text_label_commands_ref': json_ref(group_path, f'/{index}/text_label_commands'),
            }
            for command_index, command in enumerate(raw['literal_commands']):
                assert command in source.text[start:end]
                if re.match(r'\\(?:draw|fill)\b', command):
                    original_paths.append({'owner': raw['id'], 'command': command, 'metadata_ref': json_ref(group_path, f'/{index}/literal_commands/{command_index}')})
        for match in re.finditer(r'^% BEGIN FIGURE (B022-F\d+);[^\n]*\n', source.text, re.M):
            figure_id = match.group(1)
            end_marker = f'% END FIGURE {figure_id}\n'
            end = source.text.index(end_marker, match.end()) + len(end_marker)
            reader_out['complete_compositions'][figure_id] = {
                'id': figure_id, 'original_reader_id': figure_id,
                'scope': 'Complete original reader figure; every adjacent node and original local group inside this source span is retained.',
                'source_span': source.span(match.start(), end),
            }
    else:
        group_path = directory / 'source_groups.json'
        raw_groups = read_json(group_path)
        raw_ownership = read_json(directory / 'group_ownership.json')
        original_paths = read_json(directory / 'path_components.json')
        raw_node_anchors = read_json(directory / 'node_anchors.json')
        raw_sigmas = read_json(directory / 'sigma_groups.json')
        for name in ['source_groups.json', 'group_ownership.json', 'path_components.json', 'node_anchors.json', 'sigma_groups.json', 'source_audit.json']:
            refs[name] = file_ref(directory / name)
        ownership_by_id = {item['id']: (index, item) for index, item in enumerate(raw_ownership)}
        sigma_by_id = {item['id']: (index, item) for index, item in enumerate(raw_sigmas)}
        for index, raw in enumerate(raw_groups):
            start, end = raw['start_char'], raw['end_char_exclusive']
            assert source.text[start:end] == raw['source']
            assert digest(raw['source'].encode('utf-8')) == raw['sha256']
            span = source.span(start, end)
            assert span['start_utf8_byte'] == raw['start_utf8_byte']
            assert span['end_utf8_byte_exclusive'] == raw['end_utf8_byte_exclusive']
            ownership_index, ownership = ownership_by_id[raw['id']]
            groups[raw['id']] = {
                'id': raw['id'], 'reader_metadata_ref': json_ref(group_path, f'/{index}'),
                'raw_reader_metadata': strip_excerpt_fields(raw, ['source']),
                'marker_span': span,
                'raw_reader_ownership': ownership,
                'reader_ownership_ref': json_ref(directory / 'group_ownership.json', f'/{ownership_index}'),
            }
            if raw['id'] in sigma_by_id:
                sigma_index, sigma = sigma_by_id[raw['id']]
                groups[raw['id']]['raw_reader_sigma_metadata'] = sigma
                groups[raw['id']]['reader_sigma_metadata_ref'] = json_ref(directory / 'sigma_groups.json', f'/{sigma_index}')

    # These maps record literal lexical containment. No coordinate value is evaluated.
    def group_chain(start, end):
        candidates = [g for g in groups.values() if g['marker_span']['start_char'] <= start and end <= g['marker_span']['end_char_exclusive']]
        return [g['id'] for g in sorted(candidates, key=lambda g: (g['marker_span']['start_char'], -g['marker_span']['end_char_exclusive']))]

    node_matches = list(re.finditer(r'(?m)^\\node\b', source.text))
    for match in node_matches:
        start, end = match.start(), command_end(source.text, match.start())
        node_id = f'{reader}022-node-L{source.text.count(chr(10), 0, start) + 1:04d}'
        contained_groups = [g['id'] for g in groups.values() if start < g['marker_span']['start_char'] and g['marker_span']['end_char_exclusive'] <= end]
        reader_out['nodes'][node_id] = {
            'id': node_id, 'helper_scope_identity': True,
            'source_span': source.span(start, end),
            'source_group_ancestors': group_chain(start, end),
            'enclosed_marker_groups': contained_groups,
            'node_kind': 'enclosing node with marked graphical content' if contained_groups else 'literal leaf node',
        }

    for index, raw in enumerate(raw_labels):
        if reader == 'A':
            label_marker = f'% LABEL {raw["id"]}:'
            at = source.text.index(label_marker)
            start = source.text.index('\\node', at)
            end = command_end(source.text, start)
            metadata_ref = json_ref(directory / 'source_audit.json', f'/text_ownership/{index}')
        else:
            start, end = source.unique(raw['source_command'])
            metadata_ref = json_ref(directory / 'text_ownership.json', f'/{index}')
        node = next(n for n in reader_out['nodes'].values() if n['source_span']['start_char'] == start and n['source_span']['end_char_exclusive'] == end)
        node['original_reader_node_id'] = raw['id']
        node['raw_reader_text_ownership'] = raw
        node['reader_text_ownership_ref'] = metadata_ref

    # Keep path commands with their reader's original pointer and original owner.
    for index, raw in enumerate(original_paths):
        if reader == 'A':
            command = raw['command']
            line = raw['source_line']
            start = source.starts[line - 1] + source.lines[line - 1].index(command)
            end = start + len(command)
            metadata_ref = json_ref(directory / 'source_audit.json', f'/all_literal_paths/{index}')
            path_id = f'A022-path-L{line:04d}'
        elif reader == 'B':
            command = raw['command']
            owner_span = groups[raw['owner']]['marker_span']
            start = source.text.find(command, owner_span['start_char'], owner_span['end_char_exclusive'])
            assert start >= 0
            end = start + len(command)
            assert source.text.find(command, end, owner_span['end_char_exclusive']) == -1
            line = source.text.count('\n', 0, start) + 1
            metadata_ref = raw['metadata_ref']
            path_id = f'B022-path-L{line:04d}'
        else:
            command = raw['literal']
            start = raw['start_char']
            end = start + len(command)
            path_id = raw['id']
            metadata_ref = json_ref(directory / 'path_components.json', f'/{index}')
        assert source.text[start:end] == command
        assert re.match(r'\\(?:draw|fill)\b', command)
        reader_out['paths'][path_id] = {
            'id': path_id, 'original_component_id': raw.get('id'),
            'owner': raw['owner'], 'reader_metadata_ref': metadata_ref,
            'raw_reader_path_metadata': raw,
            'source_span': source.span(start, end),
            'source_group_ancestors': group_chain(start, end),
        }

    # Copy declarations as source tokens; inherited scope references bind them to each group.
    environments = []
    stack = []
    for match in re.finditer(r'\\(begin|end)\{(tikzpicture|scope)\}', source.text):
        if match.group(1) == 'begin':
            end = match.end()
            if source.text[end:end + 1] == '[':
                bracket_depth = 1
                end += 1
                while bracket_depth:
                    if source.text[end] == '[':
                        bracket_depth += 1
                    elif source.text[end] == ']':
                        bracket_depth -= 1
                    end += 1
            declaration_id = f'{reader}022-declaration-C{match.start()}'
            reader_out['declarations'][declaration_id] = {
                'id': declaration_id, 'kind': match.group(2),
                'source_span': source.span(match.start(), end),
                'source_group_ancestors': group_chain(match.start(), end),
            }
            environment = {'declaration_id': declaration_id, 'kind': match.group(2), 'start': match.start(), 'declaration_end': end}
            environments.append(environment)
            stack.append(environment)
        else:
            environment = stack.pop()
            assert environment['kind'] == match.group(2)
            environment['end'] = match.end()
    assert not stack
    for match in re.finditer(r'(?m)^\\(?:path\[use as bounding box\]|coordinate\b)[^\n]*;', source.text):
        declaration_id = f'{reader}022-declaration-C{match.start()}'
        reader_out['declarations'][declaration_id] = {
            'id': declaration_id,
            'kind': 'bounding-box' if match.group().startswith('\\path') else 'baseline-coordinate',
            'source_span': source.span(match.start(), match.end()),
            'source_group_ancestors': group_chain(match.start(), match.end()),
        }

    for group_id, group in groups.items():
        start, end = group['marker_span']['start_char'], group['marker_span']['end_char_exclusive']
        chain = group_chain(start, end)
        group['source_group_ancestors'] = [item for item in chain if item != group_id]
        group['immediate_source_parent_group'] = group['source_group_ancestors'][-1] if group['source_group_ancestors'] else None
        group['contained_group_ids'] = [g['id'] for g in groups.values() if start < g['marker_span']['start_char'] and g['marker_span']['end_char_exclusive'] <= end]
        group['direct_path_refs'] = [f'/readers/{reader}/paths/{p["id"]}' for p in reader_out['paths'].values() if p['owner'] == group_id]
        group['leaf_node_refs'] = [f'/readers/{reader}/nodes/{n["id"]}' for n in reader_out['nodes'].values() if n['node_kind'] == 'literal leaf node' and n['source_group_ancestors'] and n['source_group_ancestors'][-1] == group_id]
        group['inherited_declaration_refs'] = [f'/readers/{reader}/declarations/{env["declaration_id"]}' for env in environments if env['start'] < start and end <= env['end']]
        group['contained_declaration_refs'] = [f'/readers/{reader}/declarations/{d["id"]}' for d in reader_out['declarations'].values() if start <= d['source_span']['start_char'] and d['source_span']['end_char_exclusive'] <= end]
        group['literal_comment_spans'] = source_comments(source, start, end)
        line_start = source.text.rfind('\n', 0, start) + 1
        following_end = source.text.find('\n', end)
        if following_end < 0:
            following_end = len(source.text)
        else:
            following_end += 1
        group['same_line_prefix'] = source.span(line_start, start)
        group['immediate_following_line'] = source.span(end, following_end)
        enclosing_nodes = [n for n in reader_out['nodes'].values() if n['source_span']['start_char'] < start and end <= n['source_span']['end_char_exclusive']]
        if enclosing_nodes:
            closest = min(enclosing_nodes, key=lambda n: n['source_span']['end_char_exclusive'] - n['source_span']['start_char'])
            group['complete_enclosing_node_ref'] = f'/readers/{reader}/nodes/{closest["id"]}'
        else:
            group['complete_enclosing_node_ref'] = None
        anchor = next(((i, a) for i, a in enumerate(raw_node_anchors) if a['group'] == group_id), None)
        if anchor:
            group['raw_reader_node_anchor'] = anchor[1]
            group['reader_node_anchor_ref'] = json_ref(directory / 'node_anchors.json', f'/{anchor[0]}')
        outside_nodes = [n for n in reader_out['nodes'].values() if n['node_kind'] == 'literal leaf node']
        previous = [n for n in outside_nodes if n['source_span']['end_char_exclusive'] <= start]
        following = [n for n in outside_nodes if n['source_span']['start_char'] >= end]
        group['previous_leaf_node_in_literal_source'] = f'/readers/{reader}/nodes/{max(previous, key=lambda n: n["source_span"]["end_char_exclusive"])["id"]}' if previous else None
        group['following_leaf_node_in_literal_source'] = f'/readers/{reader}/nodes/{min(following, key=lambda n: n["source_span"]["start_char"])["id"]}' if following else None
        group['adjacency_scope'] = 'Previous/following node pointers describe source order only; original ownership comments and complete parent source delimit the candidate.'

    if reader == 'C':
        # A complete literal wrapper for each original top-level graphical parent.
        wrappers = {
            'C022-G01': '\\mbox{', 'C022-G02': '\\unsure{\\mbox{',
            'C022-G04': '\\mbox{', 'C022-G05': '\\figure{', 'C022-G08': '\\mbox{',
        }
        for group_id, wrapper in wrappers.items():
            marker = groups[group_id]['marker_span']
            start = source.text.rfind(wrapper, 0, marker['start_char'])
            assert start >= 0
            end = argument_end(source.text, start + wrapper.index('{'))
            assert end >= marker['end_char_exclusive']
            composition_id = f'{group_id}-complete-source-wrapper'
            reader_out['complete_compositions'][composition_id] = {
                'id': composition_id, 'original_reader_id': group_id, 'helper_scope_identity': True,
                'scope': 'Exact original enclosing command, retaining its qualification and all complete contained wording. Adjacent math delimiter/prose context stays available from the original source.',
                'source_span': source.span(start, end),
                'group_ref': f'/readers/C/groups/{group_id}',
            }

    for composition in reader_out['complete_compositions'].values():
        span = composition['source_span']
        start, end = span['start_char'], span['end_char_exclusive']
        composition['contained_group_refs'] = [f'/readers/{reader}/groups/{g["id"]}' for g in groups.values() if start <= g['marker_span']['start_char'] and g['marker_span']['end_char_exclusive'] <= end]
        composition['contained_leaf_node_refs'] = [f'/readers/{reader}/nodes/{n["id"]}' for n in reader_out['nodes'].values() if n['node_kind'] == 'literal leaf node' and start <= n['source_span']['start_char'] and n['source_span']['end_char_exclusive'] <= end]

    reader_out['source_order_group_ids'] = [g['id'] for g in sorted(groups.values(), key=lambda g: (g['marker_span']['start_char'], -g['marker_span']['end_char_exclusive']))]
    bank['readers'][reader] = reader_out

csource = Source('C')
note_spans = []
for literal in [
    '% Shared visible rule owned once by C022-G04 connector horizontal, (1009,749) to (1068,749).\n',
    '% Owns one shared horizontal and three short oblique ticks; vertical deleted equals / equals / implication candidates, no second closure rule.\n',
    '% Owns the complete lower-right formula: live inserted primary and deleted inserted alternative; shared upper run remains owned by G06.\n',
]:
    start, end = csource.unique(literal)
    note_spans.append(csource.span(start, end))
bank['source_notes']['C022-S08-stale-owner-comment'] = {
    'status': 'Original comment preserved; pending root source choice',
    'scope': 'The S08 comment literally names C022-G04. The connector source is C022-G06 and the A02 ownership comment literally names G06. No comment correction, shared-stroke reassignment or ink choice has been applied.',
    'literal_source_spans': note_spans,
    'literal_connector_path_ref': '/readers/C/paths/P048',
    'group_refs': ['/readers/C/groups/C022-S08', '/readers/C/groups/C022-G06', '/readers/C/groups/C022-A02', '/readers/C/groups/C022-G04'],
}

bank['extraction_validation']['released_source_hashes_match'] = True
bank['extraction_validation']['stored_group_literals_match_released_sources'] = True
bank['extraction_validation']['stored_path_literals_match_released_sources'] = True
bank['extraction_validation']['reader_text_owner_commands_match_released_sources'] = True
bank['extraction_validation']['scope_declarations_copied_without_coordinate_evaluation'] = True
bank['extraction_validation']['extractor'] = file_ref(Path(__file__))
assert not OUT.exists(), 'Preserve the existing candidate bank; choose a new revision filename.'
OUT.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'path': rel(OUT), 'sha256': digest(OUT.read_bytes()), 'status': bank['status']}, ensure_ascii=False))
