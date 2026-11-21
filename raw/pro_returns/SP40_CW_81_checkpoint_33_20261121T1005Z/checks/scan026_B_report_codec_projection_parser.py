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

BASE = Path('/workspace/scratch/94548b74fbe0/out/checks')
PREFIX = 'scan026_B_report_codec_'
SOURCE = Path('/workspace/scratch/94548b74fbe0/out/readers/026/B/report.json')
EXPECTED_SHA256 = 'a179435ea1b8c12387b1fb0c035b430efff397544c3392c35183b6dc6bfcc20e'
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
projection_paths = [BASE / (PREFIX + f'projection_{i:02d}.txt') for i in range(1, 11)]
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
assert {key: len(values) for key, values in pools.items()} == {'S': 228, 'M': 691, 'N': 1010}

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
    'parser_source': str(BASE / (PREFIX + 'projection_parser.py')),
    'parser_source_sha256': sha256((BASE / (PREFIX + 'projection_parser.py')).read_bytes()),
    'report_values_decoded_from': 'projection_01.txt through projection_10.txt only',
    'data_json_used_to_decode_report': False,
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
proof_text = '''INDEPENDENT HUMAN-PROJECTION INVERSE: EXACT BYTE PROOF

The accompanying projection_parser.py reads all ten human-readable projection
chunks. It decodes every displayed S literal, every displayed M member, and every
displayed N ordered container, then expands the single displayed root @N1009.
It recovers no report values from data.json or the original report.

The parser preserves scalar types and the displayed object-member/array order.
It rejects missing or repeated definition IDs, undefined references, reference
cycles, duplicate object keys, malformed separators, and unreachable definitions.
All 228 S definitions, 691 M definitions, and 1,010 N definitions are reachable.

Finite inverse argument: a literal scalar expands to itself; an S reference
expands to its whole literal string; an M reference expands to its whole ordered
key/value member. An N array expands each displayed child in its displayed index;
an N object expands each displayed member in its displayed position. Induction
on finite node height establishes preservation of every ordered subtree. Every
source field and complete candidate state therefore survives the inverse. This
argument is supplemented by the direct exhaustive byte comparison below.

The recovered root is serialized as UTF-8 JSON with ensure_ascii=False, indent=2,
and one trailing LF. Direct comparison of the resulting byte strings succeeded:

Source byte length:   566169
Replayed byte length: 566169
First mismatching byte: none
Source SHA-256:
  a179435ea1b8c12387b1fb0c035b430efff397544c3392c35183b6dc6bfcc20e
Replayed SHA-256:
  a179435ea1b8c12387b1fb0c035b430efff397544c3392c35183b6dc6bfcc20e

The comparison checks actual bytes, independently of the SHA-256 comparison.
The replay also equals the existing reconstructed.json file byte for byte.
A separate typed ordered-tree comparison with the source parse succeeded.

Checksums of every pre-existing codec output were recorded before and after
verification. Every pre-existing projection, codec, manifest, path map, original
proof, build script, and replay remained unchanged. The source remained unchanged.
Only this new parser source and its new JSON/text proof files were written.
The JSON proof contains the complete unchanged-output checksum inventory.

This verifies the codec. It makes no claim that root has read or reviewed B.
'''
(BASE / (PREFIX + 'projection_parser_proof.txt')).write_text(proof_text, encoding='utf-8')
assert existing_outputs() == before
print(json.dumps({key: proof[key] for key in (
    'source_byte_length', 'source_sha256', 'replayed_byte_length', 'replayed_sha256',
    'direct_byte_for_byte_comparison', 'definition_counts',
    'every_definition_reachable_from_root', 'all_preexisting_codec_outputs_unchanged'
)}, indent=2))
