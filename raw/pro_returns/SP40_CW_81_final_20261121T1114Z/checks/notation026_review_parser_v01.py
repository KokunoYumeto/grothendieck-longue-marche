#!/usr/bin/env python3
"""Decode only the human projection, verify exact source bytes, save new proof files.

This independent inverse does not read data.json to recover report values.
It preserves ordered members and exact JSON scalar types. Existing codec,
projection, manifest, path-map, proof and replay files are only read.
"""
from pathlib import Path
import hashlib
import json
import re
import argparse

BASE = Path('/workspace/scratch/94548b74fbe0/out/checks')
arguments = argparse.ArgumentParser()
arguments.add_argument('--prefix', choices=['notation026_new_review_', 'notation026_review_'], required=True)
arguments.add_argument('--source', required=True)
args = arguments.parse_args()
PREFIX = args.prefix
SOURCE = Path(args.source)
manifest = json.loads((BASE / (PREFIX + 'manifest.json')).read_bytes())
EXPECTED_SHA256 = manifest['source_sha256']
assert not (BASE / (PREFIX + 'projection_parser_proof.json')).exists()
NEW_FILES = {
    PREFIX + 'projection_parser.py',
    PREFIX + 'projection_parser_proof.json',
    PREFIX + 'projection_parser_proof.txt',
}

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def existing_outputs():
    return {
        path.name: sha256(path.read_bytes())
        for path in sorted(BASE.glob(PREFIX + '*'))
        if path.name not in NEW_FILES and path.is_file()
    }

before = existing_outputs()
source_bytes = SOURCE.read_bytes()
assert sha256(source_bytes) == EXPECTED_SHA256
projection_paths = [BASE / name for name in manifest['projection_files']]
projection_parts = [path.read_bytes() for path in projection_paths]
projection = b''.join(projection_parts).decode('utf-8')
decoder = json.JSONDecoder()


def whitespace(pos):
    while pos < len(projection) and projection[pos].isspace():
        pos += 1
    return pos


def read_ref(pos):
    pos = whitespace(pos)
    if projection[pos] == '@':
        match = re.match(r'@([SN])(\d{4})', projection[pos:])
        assert match, ('Invalid value reference', pos)
        tag = {'S': 'string', 'N': 'node'}[match[1]]
        return [tag, int(match[2])], pos + len(match[0])
    value, end = decoder.raw_decode(projection, pos)
    assert not isinstance(value, (dict, list)), ('Container without N alias', pos)
    return ['value', value], end


def read_member(pos):
    key, pos = decoder.raw_decode(projection, whitespace(pos))
    assert isinstance(key, str), ('Non-string member key', pos)
    pos = whitespace(pos)
    assert projection[pos] == ':', ('Missing member colon', pos)
    ref, end = read_ref(pos + 1)
    return [key, ref], end


def read_node(pos):
    pos = whitespace(pos)
    start = projection[pos]
    assert start in '{[', ('Invalid container opener', pos)
    kind = 'object' if start == '{' else 'array'
    close = '}' if start == '{' else ']'
    pos = whitespace(pos + 1)
    values = []
    while projection[pos] != close:
        if kind == 'array':
            value, pos = read_ref(pos)
        elif projection[pos] == '@':
            match = re.match(r'@M(\d{4})', projection[pos:])
            assert match, ('Invalid member reference', pos)
            value = ['member', int(match[1])]
            pos += len(match[0])
        else:
            member, pos = read_member(pos)
            value = ['inline', member]
        values.append(value)
        pos = whitespace(pos)
        if projection[pos] == ',':
            pos = whitespace(pos + 1)
            assert projection[pos] != close, ('Trailing comma', pos)
        else:
            assert projection[pos] == close, ('Missing separator', pos)
    return [kind, values], pos + 1


pools = {'S': [], 'M': [], 'N': []}
spans = []
for match in re.finditer(r'^([SMN])(\d{4}) = ', projection, re.MULTILINE):
    kind = match[1]
    index = int(match[2])
    assert index == len(pools[kind]), ('Missing, repeated, or reordered ID', kind, index)
    if kind == 'S':
        value, end = decoder.raw_decode(projection, match.end())
        assert isinstance(value, str)
    elif kind == 'M':
        value, end = read_member(match.end())
    else:
        value, end = read_node(match.end())
    pools[kind].append(value)
    spans.append((match.start(), end))
assert all(previous[1] <= following[0] for previous, following in zip(spans, spans[1:]))
root_matches = list(re.finditer(r'^ROOT = @N(\d{4})$', projection, re.MULTILINE))
assert len(root_matches) == 1
root_ref = ['node', int(root_matches[0][1])]
assert {key: len(values) for key, values in pools.items()} == {'S': manifest['string_aliases'], 'M': manifest['member_aliases'], 'N': manifest['subtree_aliases']}

active = set()
cache = {}
used = {'S': set(), 'M': set(), 'N': set()}


def expand(ref):
    kind, value = ref
    if kind == 'value':
        return value
    if kind == 'string':
        assert 0 <= value < len(pools['S'])
        used['S'].add(value)
        return pools['S'][value]
    assert kind == 'node'
    assert 0 <= value < len(pools['N'])
    used['N'].add(value)
    if value in cache:
        return cache[value]
    assert value not in active, ('Reference cycle', value)
    active.add(value)
    node_kind, values = pools['N'][value]
    if node_kind == 'array':
        answer = [expand(ref) for ref in values]
    else:
        pairs = []
        for mode, member in values:
            if mode == 'member':
                assert 0 <= member < len(pools['M'])
                used['M'].add(member)
                pair = pools['M'][member]
            else:
                assert mode == 'inline'
                pair = member
            pairs.append(pair)
        assert len(pairs) == len({key for key, ref in pairs}), ('Duplicate object key', value)
        # Python dict construction retains the displayed member order.
        answer = {key: expand(ref) for key, ref in pairs}
    active.remove(value)
    cache[value] = answer
    return answer


report = expand(root_ref)
assert all(used[key] == set(range(len(pools[key]))) for key in pools), 'Unreachable definitions'
replayed = (json.dumps(report, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
assert replayed == source_bytes, 'Source and projection replay bytes differ'
existing_replay = (BASE / (PREFIX + 'reconstructed.json')).read_bytes()
assert replayed == existing_replay

# An independent typed ordered-tree comparison supplements exact byte equality.
def typed_ordered(value):
    if isinstance(value, dict):
        return ('object', tuple((key, typed_ordered(child)) for key, child in value.items()))
    if isinstance(value, list):
        return ('array', tuple(typed_ordered(child) for child in value))
    return (type(value).__name__, json.dumps(value, ensure_ascii=False, separators=(',', ':')))

assert typed_ordered(report) == typed_ordered(json.loads(source_bytes))
assert SOURCE.read_bytes() == source_bytes, 'Source changed during verification'
after = existing_outputs()
assert before == after, 'A pre-existing output changed during verification'

proof = {
    'verification': 'Independent inverse of numbered human-readable projection files',
    'parser_source': str(Path(__file__)),
    'parser_source_sha256': sha256(Path(__file__).read_bytes()),
    'values_decoded_from': [path.name for path in projection_paths],
    'data_json_used_to_decode_values': False,
    'source_file': str(SOURCE),
    'source_byte_length': len(source_bytes),
    'source_sha256': sha256(source_bytes),
    'replayed_byte_length': len(replayed),
    'replayed_sha256': sha256(replayed),
    'expected_source_sha256': EXPECTED_SHA256,
    'expected_source_sha256_matches': sha256(source_bytes) == EXPECTED_SHA256,
    'direct_byte_for_byte_comparison': replayed == source_bytes,
    'first_mismatching_byte': None,
    'existing_reconstructed_json_byte_equal': replayed == existing_replay,
    'typed_ordered_tree_equal': typed_ordered(report) == typed_ordered(json.loads(source_bytes)),
    'definition_counts': {key: len(values) for key, values in pools.items()},
    'every_definition_reachable_from_root': all(used[key] == set(range(len(pools[key]))) for key in pools),
    'root': '@N' + f'{root_ref[1]:04d}',
    'source_unchanged_during_verification': SOURCE.read_bytes() == source_bytes,
    'all_preexisting_codec_outputs_unchanged': before == after,
    'preexisting_codec_output_sha256': before,
    'projection_file_byte_lengths': {path.name: len(data) for path, data in zip(projection_paths, projection_parts)},
    'no_claim_of_root_review': True,
}
proof_json = BASE / (PREFIX + 'projection_parser_proof.json')
proof_json.write_text(json.dumps(proof, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
proof_text = f'''INDEPENDENT HUMAN-PROJECTION INVERSE: EXACT BYTE PROOF

This parser reads only the numbered human text files for the literal values and
ordered S/M/N definitions. The manifest supplies file names, counts and the
expected fingerprint. No source artifact or data.json supplies recovered values.
The parser rejects repeated/missing IDs, undefined references, cycles, duplicate
keys, malformed separators and unreachable definitions. Every displayed definition
is reachable. Scalar types and complete member/array order are retained.

Finite inverse: a literal scalar expands to itself; S expands to its exact string;
M expands to its one key/value member; N expands each ordered child/member. The
recursion terminates because cycles are rejected and the alias graph is finite.
The expanded root is serialized with ensure_ascii=False, indent=2 and one LF.
Direct exhaustive byte comparison with the frozen input succeeds.

Source bytes: {len(source_bytes)}
Replayed bytes: {len(replayed)}
Source SHA256: {sha256(source_bytes)}
Replayed SHA256: {sha256(replayed)}
Definitions: {json.dumps({key: len(value) for key, value in pools.items()})}
Root: @N{root_ref[1]:04d}
First mismatching byte: none
Human projection files: {len(projection_paths)}

The source, prior projection, manifest, path map and machine replay are unchanged.
The accompanying JSON gives their complete before/after fingerprints. This proof
claims source preservation and exact reconstruction, without claiming root review.
'''
(BASE / (PREFIX + 'projection_parser_proof.txt')).write_text(proof_text, encoding='utf-8')
assert existing_outputs() == before
print(json.dumps({key: proof[key] for key in (
    'source_byte_length', 'source_sha256', 'replayed_byte_length', 'replayed_sha256',
    'direct_byte_for_byte_comparison', 'definition_counts',
    'every_definition_reachable_from_root', 'all_preexisting_codec_outputs_unchanged'
)}, indent=2))
